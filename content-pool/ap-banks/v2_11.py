# AP U.S. GOVERNMENT AND POLITICS 2.11 Checks on the Judicial Branch -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# TWO learning objectives:
#   LO 2.11.A -- explain how the exercise of judicial review can lead to debate
#     about the Supreme Court's power.
#   LO 2.11.B -- explain how other branches in the government can LIMIT the
#     Supreme Court's power.
# Suggested skill for this topic (CED p. 71): 1.D, describe political
# principles, institutions, processes, policies and behaviors ILLUSTRATED IN
# DIFFERENT SCENARIOS IN CONTEXT.
#
# Essential knowledge relied on:
#   EK 2.11.A.1 -- "Political discussion about the Supreme Court's power is
#     illustrated by the ongoing debate over differing interpretations of
#     judicial review."
#     i.  "JUDICIAL ACTIVISM asserts that judicial review ALLOWS the courts to
#         overturn current Constitutional and case precedent or invalidate
#         legislative or executive acts."
#     ii. "JUDICIAL RESTRAINT asserts that judicial review SHOULD BE CONSTRAINED
#         to decisions that ADHERE TO current Constitutional and case
#         precedent."
#   EK 2.11.B.1 -- restrictions on the Supreme Court, a CLOSED list of five:
#     i.   "Congressional legislation to modify the impact of prior Supreme
#          Court decisions"
#     ii.  "Ratification of a Constitutional amendment"
#     iii. "Judicial appointments and confirmations which may shift the
#          ideological balance of the court"
#     iv.  "The president and states DELAYING IMPLEMENTATION of a Supreme Court
#          decision"
#     v.   "Enacting legislation to limit the cases the Supreme Court can hear
#          on appeal by removing the court's jurisdiction over a case"
#
# ACTIVISM AND RESTRAINT ARE POSITIONS ABOUT WHAT JUDICIAL REVIEW PERMITS, NOT
# LABELS FOR OUTCOMES A STUDENT LIKES OR DISLIKES. Both CED definitions are
# framed as assertions ABOUT JUDICIAL REVIEW: activism asserts it allows
# overturning precedent and invalidating acts; restraint asserts it should be
# constrained to decisions adhering to precedent. Neither is defined by which
# side of a case wins, and neither belongs to a political party. Items 3 to 10
# are written so that a student who has learned "activist means liberal" or
# "restraint means conservative" gets them wrong -- an activist decision can
# strike down a law of any kind, and a restrained one can uphold a law of any
# kind.
#
# THE FIFTH RESTRICTION IS THE ONE BANKS MISS. EK 2.11.B.1.v is legislation
# REMOVING THE COURT'S JURISDICTION over a class of appeals. It is not the same
# as EK 2.11.B.1.i, legislation modifying the impact of a decision already made:
# one changes what the Court may hear in future, the other changes what an
# existing decision accomplishes. Items 18 and 19 separate them.
#
# AND THE FOURTH IS THE ONE THAT IS NOT A LEGAL POWER AT ALL. EK 2.11.B.1.iv is
# the president and the states DELAYING IMPLEMENTATION. Nothing authorizes it;
# it works because the judiciary commands neither the sword nor the purse, which
# is Federalist No. 78's own premise. Item 16 makes that distinction explicit
# rather than letting a student file delay alongside the formal instruments.
#
# Documents the CED attaches to 2.11.A and 2.11.B (p. 26-27): Federalist No. 51,
# Federalist No. 78.
# Required cases the CED attaches to 2.11.A (p. 31-33): Marbury v. Madison,
# McCulloch v. Maryland, Brown v. Board of Education, New York Times Co. v.
# United States. To 2.11.B: Marbury v. Madison, Brown v. Board of Education.
# The CED's illustrative examples here -- Swann, Milliken, the court-packing
# plan, the Sixteenth Amendment -- are marked NOT REQUIRED and none is named.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: Federalist No. 78 is quoted verbatim.
# Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere; vote splits
# are written in words. The verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.11", "Checks on the Judicial Branch", 2)

_RESPONSE = ("In a hypothetical study, the table reports how a national legislature and the "
             "states responded to fifty high court decisions that struck down a statute.")
_RESPONSE_TABLE = dict(
    headers=["Response", "Number of decisions"],
    rows=[["No response; the decision stood as issued", "29"],
          ["New legislation modifying the decision's effect", "12"],
          ["Implementation delayed by officials for more than two years", "6"],
          ["Legislation removing the court's jurisdiction over such appeals", "2"],
          ["A constitutional amendment ratified", "1"]])

_VIEWS = ("In a hypothetical survey, respondents were asked when a high court should be "
          "willing to set aside an existing precedent.")
_VIEWS_TABLE = dict(
    headers=["Position", "Respondents holding it (%)", "Also say the court has too much power (%)"],
    rows=[["Only where the precedent conflicts with the constitutional text", "39", "24"],
          ["Where the precedent has proved unworkable in practice", "34", "31"],
          ["Whenever a majority of the court believes it was wrongly decided", "18", "58"],
          ["Never, under any circumstances", "9", "19"]])

QUESTIONS = [
 dict(q="According to the course framework, political discussion about the Supreme Court's power is illustrated by",
   choices=[
     "the ongoing debate over differing interpretations of judicial review",
     "the requirement that justices retire at a fixed age",
     "the process by which the Court selects the cases it will hear",
     "the annual report the Chief Justice delivers to Congress",
     "the number of cases the Court decides each term"], ans=0,
   why="EK 2.11.A.1 states this in exactly these words, and the two interpretations it goes on to name are judicial activism and judicial restraint."),

 dict(q="According to the course framework, judicial activism asserts that judicial review",
   choices=[
     "allows the courts to overturn current constitutional and case precedent or invalidate legislative or executive acts",
     "should be constrained to decisions that adhere to current constitutional and case precedent",
     "may be exercised only over acts of state governments",
     "requires the consent of Congress before a statute may be set aside",
     "applies only to cases involving individual rights"], ans=0,
   why="EK 2.11.A.1.i gives this definition verbatim. The second option is the framework's definition of judicial restraint, which is the opposing position in the same debate."),

 dict(q="According to the course framework, judicial restraint asserts that judicial review",
   choices=[
     "should be constrained to decisions that adhere to current constitutional and case precedent",
     "allows the courts to overturn current precedent or invalidate legislative acts",
     "should never be exercised at all",
     "belongs to Congress rather than to the courts",
     "should be exercised only when public opinion supports the result"], ans=0,
   why="EK 2.11.A.1.ii gives this definition verbatim. Restraint is a position about the SCOPE of review, not a rejection of review, which is why the third option overstates it."),

 dict(q="What is the fundamental disagreement between the two interpretations the framework describes?",
   choices=[
     "How far judicial review permits a court to depart from existing precedent and from the acts of the elected branches",
     "Whether courts should decide cases at all",
     "Which political party's appointees should sit on the Court",
     "Whether the Constitution should be amended more often",
     "Whether the Supreme Court should have nine members"], ans=0,
   why="Both EK 2.11.A.1.i and EK 2.11.A.1.ii are assertions about what judicial review allows or should be constrained to, so the disagreement is about the reach of the power rather than about personnel or party."),

 dict(q="A court overturns one of its own long-standing precedents and strikes down a statute enacted the previous year. A critic calls the decision an exercise of judicial activism. Under the framework's definitions, is the label apt?",
   choices=[
     "Yes, because the decision both overturned existing precedent and invalidated a legislative act",
     "No, because activism applies only to decisions that expand individual rights",
     "No, because a court may never overturn its own precedent",
     "Yes, but only because the statute was recent",
     "No, because the label applies only to decisions striking down executive acts"], ans=0,
   why="EK 2.11.A.1.i's definition names exactly these two moves, and the decision made both. The framework attaches the label to what the court DID rather than to the direction of the outcome."),

 dict(q="A court declines to disturb a precedent it considers questionable and upholds a statute several justices consider unwise. Which interpretation does the decision reflect?",
   choices=[
     "Judicial restraint, since the decision adhered to current precedent rather than departing from it",
     "Judicial activism, since the justices had private doubts about the statute",
     "Judicial activism, since the court decided the case at all",
     "Neither, since restraint applies only to constitutional cases",
     "Judicial restraint, since the statute was popular"], ans=0,
   why="EK 2.11.A.1.ii defines restraint as review constrained to decisions adhering to current precedent, which is what the court did. Private doubts about a statute are not a decision to invalidate it."),

 dict(q="A student writes that judicial activism is the practice of liberal judges and judicial restraint the practice of conservative ones. What is the most important correction?",
   choices=[
     "The framework defines both as positions about what judicial review permits, not as positions on any political question",
     "The framework defines both by which political party appointed the justice",
     "The framework says only conservative judges practice activism",
     "The framework says the two terms mean the same thing",
     "The framework says the labels apply only to lower courts"], ans=0,
   why="EK 2.11.A.1.i and EK 2.11.A.1.ii are both framed as assertions ABOUT JUDICIAL REVIEW, and neither mentions ideology. A court of any political complexion can overturn precedent or decline to."),

 dict(q="Which pair of decisions would both count as exercises of judicial activism under the framework's definition?",
   choices=[
     "One striking down a regulation of business and one striking down a restriction on speech",
     "One upholding a regulation of business and one upholding a restriction on speech",
     "One striking down a regulation of business and one upholding a restriction on speech",
     "One declining to hear a case and one upholding a precedent",
     "One following a precedent and one distinguishing a case on its facts"], ans=0,
   why="EK 2.11.A.1.i's definition turns on invalidating acts or overturning precedent, and both decisions in the first pair invalidate something. The political direction of the two is opposite, which is the point."),

 dict(q="Which criticism of judicial activism, as the framework defines it, is strongest?",
   choices=[
     "Setting aside the acts of elected officials transfers decisions from a body voters chose to one they did not",
     "It requires that courts decide cases within a fixed time",
     "It prevents courts from ever following precedent",
     "It gives the Supreme Court the power to enact statutes",
     "It requires a unanimous vote of the justices"], ans=0,
   why="The democratic objection is the serious one, and it follows directly from EK 2.11.A.1.i's invalidation of legislative and executive acts. The other options describe consequences activism does not have."),

 dict(q="Which criticism of judicial restraint, as the framework defines it, is strongest?",
   choices=[
     "A precedent that was wrong when decided stays in force, and constitutional limits go unenforced against the elected branches",
     "It requires courts to overturn precedent in every case",
     "It gives courts the power to rewrite statutes",
     "It prevents courts from hearing any constitutional case",
     "It requires courts to follow public opinion"], ans=0,
   why="If review is constrained to decisions adhering to current precedent, then an erroneous precedent is self-perpetuating and a limit nobody has yet enforced stays unenforced. The other options misdescribe what EK 2.11.A.1.ii asserts."),

 dict(q="In Brown v. Board of Education (1954), the Supreme Court held that race-based school segregation violates the Equal Protection Clause of the Fourteenth Amendment. How does the decision bear on the debate the framework describes?",
   choices=[
     "It departed from an established precedent to enforce a constitutional guarantee, which is why the same decision is cited on both sides of the activism debate",
     "It followed existing precedent, so it is an example of restraint alone",
     "It was decided without reference to the Constitution",
     "It concerned the powers of Congress rather than individual rights",
     "It was later overturned by constitutional amendment"], ans=0,
   why="The CED states the holding as race-based school segregation violating the Equal Protection Clause, which required departing from what had gone before. That is why the case is the standard test of anyone's definition of activism."),

 dict(q="According to the course framework, which of the following is one way other branches can restrict the Supreme Court?",
   choices=[
     "Congressional legislation to modify the impact of prior Supreme Court decisions",
     "A vote of the Cabinet to set aside a decision",
     "A referendum in which voters reverse a decision",
     "An order from the president vacating a decision",
     "A resolution of a state legislature nullifying a decision"], ans=0,
   why="EK 2.11.B.1.i names congressional legislation modifying the impact of prior decisions. The other four options describe actions no institution is authorized to take."),

 dict(q="Which restriction on the Supreme Court does the course framework identify as operating through the Constitution itself?",
   choices=[
     "Ratification of a constitutional amendment",
     "Congressional legislation modifying a decision's impact",
     "Delaying implementation of a decision",
     "Judicial appointments and confirmations",
     "Removing the Court's jurisdiction over a class of appeals"], ans=0,
   why="EK 2.11.B.1.ii names ratification of a constitutional amendment, which is the only item on the list that changes the document the Court interprets rather than working around a decision."),

 dict(q="How do judicial appointments and confirmations restrict the Supreme Court's power, according to the framework?",
   choices=[
     "They may shift the ideological balance of the court, changing which decisions it reaches in future",
     "They allow the president to remove sitting justices",
     "They allow the Senate to reverse decisions the Court has already issued",
     "They allow Congress to reduce the number of seats a justice may hold",
     "They allow a state to refuse to be bound by a decision"], ans=0,
   why="EK 2.11.B.1.iii names appointments and confirmations 'which may shift the ideological balance of the court,' and EK 2.9.A.2 supplies the consequence: new or rejected precedents. It operates prospectively, not on decided cases."),

 dict(q="According to the course framework, what can the president and the states do that restricts the effect of a Supreme Court decision?",
   choices=[
     "Delay implementation of the decision",
     "Reverse the decision by executive order",
     "Refer the decision back to the Court for reconsideration",
     "Remove the justices who joined the majority",
     "Declare the decision unconstitutional"], ans=0,
   why="EK 2.11.B.1.iv names the president and the states delaying implementation. The framework does not say they may reverse, refer or nullify a decision, and none of those powers exists."),

 dict(q="Delaying implementation differs from the other restrictions the framework lists in an important way. What is it?",
   choices=[
     "It is not a legal power at all; it works because the Court commands neither the sword nor the purse",
     "It is the only restriction that requires a constitutional amendment",
     "It is the only restriction available to Congress",
     "It is the only restriction that operates before a decision is issued",
     "It is the only restriction that requires the Court's own consent"], ans=0,
   why="Legislation, amendment, appointments and jurisdiction-stripping are all exercises of granted authority; delay is simply non-compliance, and it is effective for the reason Federalist No. 78 gives -- the judiciary depends on others to enforce its judgments."),

 dict(q="According to the course framework, Congress may limit the cases the Supreme Court can hear on appeal by",
   choices=[
     "enacting legislation removing the Court's jurisdiction over a case",
     "instructing the Court to decline to hear it",
     "requiring the Court to obtain the president's approval before hearing it",
     "referring the case to a state court instead",
     "abolishing the Court for the duration of the case"], ans=0,
   why="EK 2.11.B.1.v names enacting legislation to limit the cases the Court can hear on appeal by removing the Court's jurisdiction. The other options describe methods with no constitutional basis."),

 dict(q="What is the difference between the framework's first and fifth restrictions?",
   choices=[
     "The first changes what an existing decision accomplishes; the fifth changes what the Court may hear in future",
     "The first changes what the Court may hear in future; the fifth changes what an existing decision accomplishes",
     "Both change what an existing decision accomplishes, but only one requires the president's signature",
     "Both change what the Court may hear in future, and they differ only in name",
     "The first requires an amendment and the fifth requires a statute"], ans=0,
   why="EK 2.11.B.1.i is legislation modifying the impact of PRIOR decisions; EK 2.11.B.1.v is legislation removing jurisdiction over a class of appeals. One looks backward at a decided case, the other forward at cases not yet heard."),

 dict(q="A legislature responds to a decision interpreting a statute by amending the statute so that the Court's interpretation no longer produces the same result. Which restriction is being used?",
   choices=[
     "Congressional legislation to modify the impact of a prior Supreme Court decision",
     "Ratification of a constitutional amendment",
     "Removal of the Court's jurisdiction over the case",
     "Delaying implementation of the decision",
     "Judicial appointments and confirmations"], ans=0,
   why="EK 2.11.B.1.i is exactly this: legislation modifying the impact of a prior decision. Because the decision interpreted a statute rather than the Constitution, the legislature can respond by rewriting the statute."),

 dict(q="Why does the framework's second restriction, ratification of a constitutional amendment, reach decisions that legislation cannot?",
   choices=[
     "A decision resting on the Constitution cannot be undone by statute, because a statute is subordinate to the document the Court applied",
     "An amendment takes effect immediately while a statute does not",
     "An amendment requires only a majority in Congress",
     "A statute may not be enacted while a case is pending",
     "An amendment removes the Court's jurisdiction automatically"], ans=0,
   why="EK 2.11.B.1.i and EK 2.11.B.1.ii differ in what each can reach: a statutory interpretation can be rewritten by statute, but a constitutional holding can be changed only by changing the Constitution, per EK 1.5.A.2's Article V thresholds."),

 dict(q=_RESPONSE + " Which conclusion is best supported by the data?",
   table=_RESPONSE_TABLE,
   choices=[
     "A majority of the decisions drew no response at all, and the constitutional amendment route was used least",
     "A majority of the decisions were answered by new legislation",
     "The constitutional amendment route was used most often",
     "Delayed implementation was the most common response",
     "Every decision drew some response from the legislature or the states"], ans=0,
   why="Twenty-nine of fifty is a majority with no response, and the amendment row is the smallest at one. Legislation, delay and jurisdiction-stripping account for twenty between them."),

 dict(q=_RESPONSE + " Which of the framework's five restrictions is NOT represented by a row of this table?",
   table=_RESPONSE_TABLE,
   choices=[
     "Judicial appointments and confirmations, since no row concerns the court's composition",
     "Congressional legislation modifying a decision's impact, since no row mentions legislation",
     "Ratification of a constitutional amendment, since no row mentions an amendment",
     "Delaying implementation, since no row mentions delay",
     "Removing the court's jurisdiction, since no row mentions jurisdiction"], ans=0,
   why="Four of the five restrictions have a row: legislation, delay, jurisdiction removal and amendment. Appointments have none, which fits, since an appointment responds to no particular decision."),

 dict(q=_RESPONSE + " A student concludes that the other branches rarely constrain the court. Which limitation of the data most complicates that conclusion?",
   table=_RESPONSE_TABLE,
   choices=[
     "The table counts only responses to decisions that struck a statute down, and a court anticipating a response may decide differently in the first place",
     "The table omits decisions that drew no response, so the total is understated",
     "The table reports percentages that do not sum to one hundred",
     "The table covers a single decision, so no pattern can be observed",
     "The table gives no information about how many decisions were studied"], ans=0,
   why="Counting completed responses misses anticipation entirely, the same limitation as any table of enforcement actions. A no-response row is present, the counts sum to fifty, and the stem states the number studied."),

 dict(q=_VIEWS + " Which conclusion is best supported by the data?",
   table=_VIEWS_TABLE,
   choices=[
     "The most permissive position toward overturning precedent is the least widely held and the most associated with saying the court has too much power",
     "The most permissive position is the most widely held",
     "The position that a court should never overturn a precedent is the most widely held",
     "Every position is held by more than a quarter of respondents",
     "The four positions are associated with similar levels of concern about the court's power"], ans=0,
   why="The whenever-wrongly-decided row is 18 percent, the second smallest, and its 58 percent is the highest in the second column. The never row is smallest at 9, and the second column runs from 19 to 58."),

 dict(q=_VIEWS + " Which of the framework's two interpretations does the first row of the table most closely correspond to?",
   table=_VIEWS_TABLE,
   choices=[
     "Judicial restraint, since it would confine departures from precedent to conflicts with the constitutional text",
     "Judicial activism, since it permits departures from precedent",
     "Neither, since the framework does not define either position",
     "Both equally, since the framework treats them as the same",
     "Judicial activism, since it is the most widely held position"], ans=0,
   why="EK 2.11.A.1.ii's restraint constrains review to decisions adhering to current constitutional and case precedent, and confining departures to textual conflicts is the narrowest of the four positions listed."),

 dict(q=_VIEWS + " A commentator argues that people who favor a court freely overturning precedent are also the most worried about judicial power. Do the data support the argument?",
   table=_VIEWS_TABLE,
   choices=[
     "Yes, since the most permissive position pairs with the highest share saying the court has too much power",
     "No, since the most permissive position pairs with the lowest share saying the court has too much power",
     "No, since the second column is identical across all four positions",
     "Yes, but only because that position is the most widely held",
     "The data cannot address the argument, since the table reports no second measure"], ans=0,
   why="The whenever-wrongly-decided row combines 18 percent holding the position with 58 percent of those also saying the court has too much power, which is the highest figure in that column. Note that this is a correlation the table records, not an explanation of it."),

 dict(q="Which pair correctly matches a restriction from EK 2.11.B.1 with what it can and cannot reach?",
   choices=[
     "A statute can change the effect of a decision interpreting a statute; only an amendment can change the effect of a decision interpreting the Constitution",
     "A statute can change the effect of any decision, including one interpreting the Constitution",
     "An amendment can change only decisions interpreting statutes",
     "Neither a statute nor an amendment can change the effect of any decision",
     "Only removing jurisdiction can change the effect of a past decision"], ans=0,
   why="EK 2.11.B.1.i and EK 2.11.B.1.ii are separate items because they reach different things, and the reason is the hierarchy the Supremacy Clause establishes: a statute cannot override the document a constitutional holding rests on."),

 dict(q="Read the following excerpt.\n\n“The judiciary... has no influence over either the sword or the purse; no direction either of the strength or of the wealth of the society; and can take no active resolution whatever.”\n—Alexander Hamilton, Federalist No. 78, 1788\n\nWhich of the framework's five restrictions does this passage most directly help explain?",
   choices=[
     "The president and states delaying implementation of a decision",
     "Ratification of a constitutional amendment",
     "Judicial appointments and confirmations",
     "Congressional legislation modifying a decision's impact",
     "Removing the court's jurisdiction over a case"], ans=0,
   why="A court that commands neither force nor wealth depends on others to carry out its judgments, which is precisely why delay by the president or the states is effective. The other four restrictions are exercises of granted authority and need no such explanation."),

 dict(q="Which scenario best illustrates LO 2.11.A, debate about the Court's power, rather than LO 2.11.B, an actual limit on it?",
   choices=[
     "Commentators and officials argue publicly about whether a recent decision exceeded the proper scope of judicial review",
     "Congress enacts a statute modifying the effect of a recent decision",
     "The Senate confirms a justice who shifts the Court's ideological balance",
     "A constitutional amendment is ratified in response to a decision",
     "State officials delay implementing a decision for several years"], ans=0,
   why="EK 2.11.A.1 concerns political DISCUSSION about the Court's power, illustrated by the debate over interpretations of judicial review; the other four options are EK 2.11.B.1's restrictions actually operating."),

 dict(q="Which question would best test whether the restrictions in EK 2.11.B.1 meaningfully constrain the Supreme Court?",
   choices=[
     "When the Court has ruled against the elected branches, how often have those branches successfully used one of the listed restrictions to change the outcome?",
     "How many cases does the Court decide each term?",
     "How many justices have life tenure?",
     "How long does the average case take to reach the Court?",
     "How many opinions in a term are unanimous?"], ans=0,
   why="LO 2.11.B is about whether other branches CAN limit the Court's power, so the test must count occasions when a restriction was used and worked. Caseload, tenure and timing measure none of that."),
]
