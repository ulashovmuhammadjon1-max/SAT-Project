# AP U.S. GOVERNMENT AND POLITICS 2.10 The Court in Action -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# Learning objective 2.10.A: explain how LIFE TENURE can lead to debate about
# the Supreme Court's power.
# Suggested skill for this topic (CED p. 70): 2.C, explain how the facts, issue,
# holding, reasoning, decision and majority opinion of a REQUIRED case compare
# to a NON-REQUIRED case. So this module carries more SCOTUS-comparison items
# than any other in the unit, and each prints the non-required case's facts in
# the stem, as CED p. 29 promises the exam will do.
#
# READ THIS BEFORE ADDING ANYTHING: THE TITLE IS MISLEADING AND THE TOPIC IS
# NARROW. "The Court in Action" sounds like it should cover how cases reach the
# Court -- certiorari, the rule of four, oral argument, opinion assignment. It
# covers NONE of that. The framework never mentions the certiorari process
# anywhere, and EK 2.10.A.1 is this topic's ONLY essential-knowledge statement.
# See AP_US_GOV_CED.md note 3. An item here about how many justices must agree
# to hear a case would be off-syllabus, however natural it feels.
#
# The single statement, quoted in full because the whole module rests on it:
#   EK 2.10.A.1 -- "Life tenure for justices allows the court to function
#     INDEPENDENT OF THE CURRENT POLITICAL CLIMATE. As a result of this
#     independence, the Court CAN DELIVER CONTROVERSIAL OR UNPOPULAR court
#     decisions, which in turn CAN LEAD TO DEBATE ABOUT THE COURT'S POWER."
#
# THAT SENTENCE IS A THREE-LINK CHAIN, and the module is organised along it:
#     life tenure  ->  independence from the political climate   items 1-8
#     independence ->  capacity for unpopular decisions          items 9-16
#     unpopular decisions -> debate about the Court's power       items 17-20
# Each link is a separate claim and a student can accept one and reject the
# next. Items 27 to 30 attack the chain at each joint on purpose, because the
# CED's own verb is "CAN" at both steps -- life tenure ALLOWS, and unpopular
# decisions CAN LEAD TO debate. Neither is asserted as inevitable, and no item
# in this module states either as inevitable.
#
# Documents the CED attaches to 2.10.A (p. 26-27): Federalist No. 51,
# Federalist No. 78.
# Required cases the CED attaches to 2.10.A (p. 31-33): Baker v. Carr,
# United States v. Lopez.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: Article III and Federalist No. 78 are
# quoted verbatim. Non-required cases are described with the facts a student
# needs and are never named. Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere; vote splits
# are written in words, so "a five to four decision" and never the numeric form.
# The verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.10", "The Court in Action", 2)

_TENURE = ("In a hypothetical study of high courts in several countries, the table reports the "
           "tenure rule for the highest court's judges and the share of the court's decisions "
           "over one decade that went against the position of the sitting government.")
_TENURE_TABLE = dict(
    headers=["Tenure rule", "Number of courts", "Decisions against the government (%)"],
    rows=[["Tenure until a fixed retirement age", "6", "34"],
          ["Single long term, not renewable", "5", "31"],
          ["Fixed term, renewable by the government", "4", "11"],
          ["Term at the pleasure of the government", "3", "4"]])

_APPROVAL = ("In a hypothetical survey, respondents were asked whether they approved of a high "
             "court's performance, in the month before and the month after it issued a widely "
             "publicized and unpopular decision.")
_APPROVAL_TABLE = dict(
    headers=["Response", "Before the decision (%)", "After the decision (%)"],
    rows=[["Approve of the court", "58", "41"],
          ["Disapprove of the court", "27", "46"],
          ["No opinion", "15", "13"]])

QUESTIONS = [
 dict(q="According to the course framework, what does life tenure for justices allow?",
   choices=[
     "The court to function independent of the current political climate",
     "The court to decide which cases it will hear",
     "The court to enforce its own decisions without help from the other branches",
     "Justices to be removed only by the president who appointed them",
     "The court to issue advisory opinions when Congress requests them"], ans=0,
   why="EK 2.10.A.1 states this in exactly these words. Independence from the political climate is the first link in the chain the statement describes."),

 dict(q="Read the following excerpt.\n\n“The Judges, both of the supreme and inferior Courts, shall hold their Offices during good Behaviour, and shall, at stated Times, receive for their Services, a Compensation, which shall not be diminished during their Continuance in Office.”\n—U.S. Constitution, Article III, Section 1\n\nWhich two protections does this passage give federal judges?",
   choices=[
     "Tenure that does not expire, and a salary that may not be reduced while they serve",
     "A fixed term of years, and a salary set by the president",
     "Immunity from all lawsuits, and a guaranteed pension",
     "The right to be reappointed, and the right to choose their own cases",
     "Selection by the states, and removal only by the states"], ans=0,
   why="The clause pairs tenure during good behavior with a bar on diminishing judicial compensation, and both remove a lever the other branches could otherwise use. The passage says nothing about immunity, pensions or case selection."),

 dict(q="Why does protecting judicial salaries from reduction matter for the independence EK 2.10.A.1 describes?",
   choices=[
     "Without it, a legislature displeased with a decision could punish the judges financially without removing them",
     "Without it, judges would be unable to afford to remain in office",
     "Without it, the president could appoint additional judges",
     "Without it, judges would have to stand for election",
     "Without it, Congress could abolish the Supreme Court"], ans=0,
   why="Tenure protects the office and the salary clause protects its value, and together they close the two obvious routes to pressuring a judge who cannot be removed. The item is about the design, not about personal finances."),

 dict(q="A judge in a system where judges serve renewable terms must be reappointed by the government whose actions she reviews. What problem does that arrangement create?",
   choices=[
     "A judge who wants reappointment has a reason to avoid ruling against the government",
     "A judge who wants reappointment must decide cases more quickly",
     "The government loses the ability to appoint judges at all",
     "The judge becomes unable to hear cases involving private parties",
     "The judge must obtain legislative approval for each decision"], ans=0,
   why="EK 2.10.A.1 makes tenure the source of independence, so a tenure that depends on the party being judged reintroduces exactly the incentive tenure removes."),

 dict(q="Which statement best describes what 'independent of the current political climate' means in EK 2.10.A.1?",
   choices=[
     "A justice can rule against a popular position without risking removal from office",
     "A justice is unaware of public opinion when deciding a case",
     "A justice may decide cases without reference to law",
     "A justice is prohibited from having political views",
     "A justice may be removed only if public opinion demands it"], ans=0,
   why="Independence is an institutional condition -- the absence of a penalty for an unpopular ruling -- not a claim about what a justice knows or believes. The third option describes something the framework never suggests."),

 dict(q="A student writes that life tenure means a justice can never be removed from office. What is the correction?",
   choices=[
     "A justice may be impeached by the House and removed on conviction in a Senate trial, so tenure is not absolute",
     "A justice may be removed by the president at will",
     "A justice may be removed by a majority vote of the Supreme Court",
     "A justice may be removed by a state legislature",
     "The student is right, since the Constitution provides no method of removal"], ans=0,
   why="EK 1.6.B.2 defines impeachment as the House's charge and removal as conviction in a Senate trial, and Article III's tenure runs 'during good Behaviour.' The route exists and is deliberately difficult."),

 dict(q="Read the following excerpt.\n\n“Nothing can contribute so much to its firmness and independence as permanency in office; this quality may therefore be justly regarded as an essential ingredient in its constitution, and, in a great measure, as the citadel of the public justice and the public security.”\n—Alexander Hamilton, Federalist No. 78, 1788\n\nWhat claim does Hamilton make about tenure in this passage?",
   choices=[
     "That permanence in office is what makes judicial independence possible, and independence is what protects the public",
     "That permanence in office makes judges unaccountable and should be avoided",
     "That judges should serve fixed terms renewable by the legislature",
     "That the judiciary should have control over public security forces",
     "That independence matters less than efficiency in deciding cases"], ans=0,
   why="Hamilton calls permanency an essential ingredient and ties it to public justice and security, which is the argument EK 2.10.A.1 restates as tenure allowing independence from the political climate."),

 dict(q="Which of the following is the strongest argument AGAINST life tenure, given what EK 2.10.A.1 says it produces?",
   choices=[
     "The same insulation that lets a court resist popular pressure also lets it persist in an unpopular course indefinitely",
     "Justices with life tenure decide fewer cases each year",
     "Life tenure prevents the president from making any appointments",
     "Life tenure requires that all decisions be unanimous",
     "Life tenure is prohibited by Article III"], ans=0,
   why="The serious objection runs through the framework's own mechanism: insulation cuts both ways, and there is no electoral correction. The remaining options assert facts that are false of the system."),

 dict(q="According to EK 2.10.A.1, what follows from the Court's independence?",
   choices=[
     "The Court can deliver controversial or unpopular decisions",
     "The Court must decide cases in accordance with public opinion",
     "The Court can enforce its own decisions",
     "The Court can issue decisions before a case is filed",
     "The Court can amend the Constitution"], ans=0,
   why="EK 2.10.A.1's second link is that independence lets the Court deliver controversial or unpopular decisions. The word is CAN, not must, which is why the item asks what independence makes possible."),

 dict(q="In Baker v. Carr (1962), the Supreme Court held that redistricting did not raise political questions, allowing federal courts to hear cases challenging redistricting plans that may violate the Equal Protection Clause. Why is that decision a useful example for a topic about life tenure?",
   choices=[
     "It required state legislatures to face challenges to the districts that elected them, which no elected body would readily impose on itself",
     "It was decided unanimously, which shows that independence produces agreement",
     "It concerned the salaries of federal judges",
     "It was decided by justices who had been elected to their seats",
     "It was later reversed by constitutional amendment"], ans=0,
   why="A holding that opens legislative districting to judicial challenge asks legislators to accept review of the arrangement that put them in office, which is EK 2.10.A.1's point about what an insulated court can do."),

 dict(q="In United States v. Lopez (1995), the Supreme Court held that Congress exceeded its power under the Commerce Clause when it made possession of a gun in a school zone a federal crime. How does the decision illustrate EK 2.10.A.1?",
   choices=[
     "A court whose members face no election struck down a popular federal statute, which is what independence makes possible",
     "The Court deferred to Congress on the scope of its own powers",
     "The Court upheld the statute because it was popular",
     "The Court required Congress to enact a replacement statute",
     "The Court's decision was reversed by the Senate"], ans=0,
   why="The CED states the holding as Congress exceeding its Commerce Clause power, and invalidating a statute a legislature wanted is the kind of decision EK 2.10.A.1 says independence permits."),

 dict(q="A non-required case: a high court invalidates a statute that had passed both chambers by wide margins and enjoyed strong public support, and public criticism of the court follows. Which required case is the closest comparison, and why?",
   choices=[
     "United States v. Lopez (1995), because there too the Court held that Congress had exceeded a constitutional limit despite the statute's popularity",
     "Baker v. Carr (1962), because there too the Court declined to hear a districting challenge",
     "Marbury v. Madison (1803), because there too the Court upheld an act of Congress",
     "McCulloch v. Maryland (1819), because there too the Court struck down a federal statute",
     "New York Times Co. v. United States (1971), because there too the Court sided with the government"], ans=0,
   why="Lopez is the required case in which a federal statute was held beyond Congress's power, which matches the stem. The other four options each misstate the holding of the case they name."),

 dict(q="A non-required case: a high court holds that a long-standing state practice violates a constitutional guarantee, and several state officials announce they disagree. Which required case is the closest comparison?",
   choices=[
     "Baker v. Carr (1962), in which the Court held that federal courts may hear challenges to state districting plans under the Equal Protection Clause",
     "United States v. Lopez (1995), in which the Court held that Congress exceeded its Commerce Clause power",
     "Marbury v. Madison (1803), in which the Court established judicial review",
     "McCulloch v. Maryland (1819), in which the Court upheld an implied power of Congress",
     "Engel v. Vitale (1962), in which the Court held that school sponsorship of religious activities violates the Establishment Clause"], ans=0,
   why="The stem describes a federal constitutional limit imposed on a state practice, which is the Baker pattern of federal courts reaching state arrangements under the Fourteenth Amendment. Lopez and McCulloch concern national rather than state power."),

 dict(q="What does the phrase 'controversial or unpopular' in EK 2.10.A.1 add to the framework's account?",
   choices=[
     "It identifies the kind of decision that independence specifically makes possible, since a popular decision needs no insulation",
     "It means the Court prefers to decide cases the public opposes",
     "It means the Court's decisions are usually wrong",
     "It means that only unanimous decisions are protected",
     "It means the Court must consult public opinion before deciding"], ans=0,
   why="Independence is only load-bearing where a decision would otherwise be punished, so the phrase locates the value of tenure precisely. Nothing in the framework suggests the Court seeks unpopularity."),

 dict(q="Which scenario best illustrates the second link in EK 2.10.A.1's chain?",
   choices=[
     "A court rules against a policy supported by large majorities in both chambers and by most of the public",
     "A court rules in favor of a policy supported by most of the public",
     "A court declines to hear a case because no litigant has standing",
     "A legislature enacts a statute overturning a court's interpretation of that statute",
     "A president appoints a justice who shares his views"], ans=0,
   why="The second link is independence producing controversial or unpopular decisions, so the illustration has to be a ruling against a widely supported position. The fourth and fifth options illustrate checks ON the Court instead."),

 dict(q="Which of the following would be evidence that a court is NOT functioning independent of the political climate?",
   choices=[
     "The court's decisions consistently align with the position of whichever party controls the government at the time",
     "The court's decisions are sometimes unpopular",
     "The court's members were appointed by presidents of different parties",
     "The court's decisions are criticized by elected officials",
     "The court sometimes reaches unanimous decisions"], ans=0,
   why="Independence is measured by whether outcomes track the government's position, so consistent alignment with whoever holds power is the diagnostic. Criticism and unpopularity are what EK 2.10.A.1 predicts an independent court will attract."),

 dict(q="According to EK 2.10.A.1, what can controversial or unpopular decisions lead to?",
   choices=[
     "Debate about the court's power",
     "Automatic review of the decision by Congress",
     "Removal of the justices who joined the majority",
     "A constitutional requirement that the decision be reconsidered",
     "Suspension of the court's jurisdiction until the next election"], ans=0,
   why="EK 2.10.A.1's third link is that such decisions 'can lead to debate about the court's power.' Debate, not any automatic institutional consequence, which is what the other four options describe."),

 dict(q="After a high court issues a series of unpopular decisions, members of the legislature propose changing the number of seats on the court and limiting the cases it may hear. What does this reaction illustrate?",
   choices=[
     "The debate about the court's power that EK 2.10.A.1 says unpopular decisions can provoke",
     "The court's loss of the power of judicial review",
     "The automatic operation of a constitutional check on the judiciary",
     "The removal of justices by the legislature",
     "The reversal of the court's decisions by public referendum"], ans=0,
   why="EK 2.10.A.1's third link is debate about the court's power, and proposals to restructure the court are that debate taking institutional form. Nothing described has actually altered the Court's authority."),

 dict(q="Read the following excerpt.\n\n“Ambition must be made to counteract ambition. The interest of the man must be connected with the constitutional rights of the place.”\n—James Madison, Federalist No. 51, 1788\n\nHow does life tenure fit Madison's design?",
   choices=[
     "It attaches a justice's interest to the office rather than to any faction that might reward or punish her",
     "It gives justices an incentive to please whichever party appointed them",
     "It makes the judiciary dependent on the legislature for its continued existence",
     "It requires justices to run for re-election on their record",
     "It removes the judiciary from the system of checks and balances entirely"], ans=0,
   why="Madison's design connects an officeholder's personal interest to the institution's prerogatives, and tenure that no faction can end is what makes a justice's interest institutional rather than partisan."),

 dict(q="A commentator argues that life tenure has become far more consequential than the framers anticipated because people live much longer. Which observation best supports that argument?",
   choices=[
     "A single appointment now routinely shapes the Court's decisions for three decades or more",
     "The Court hears fewer cases than it once did",
     "The Senate confirms nominees by majority vote",
     "The Constitution does not fix the number of justices",
     "Federal judges may retire at any time"], ans=0,
   why="The argument is about DURATION, so the supporting evidence must be how long an appointment now lasts, which EK 2.5.A.2 identifies as the president's longest lasting influence. Caseload and Court size are separate matters."),

 dict(q=_TENURE + " Which conclusion is best supported by the data?",
   table=_TENURE_TABLE,
   choices=[
     "Courts whose judges cannot be removed or reappointed by the government ruled against it far more often than courts whose judges can be",
     "Courts whose judges serve at the pleasure of the government ruled against it most often",
     "All four groups of courts ruled against the government at similar rates",
     "The largest group of courts is the one whose judges serve renewable terms",
     "No group of courts ruled against the government in more than a fifth of decisions"], ans=0,
   why="The two secure-tenure rows are 34 and 31 percent against 11 and 4 percent for the two rows where the government controls a judge's future. The largest group is the six courts with tenure to a retirement age."),

 dict(q=_TENURE + " Which claim from the course framework do these data most directly support?",
   table=_TENURE_TABLE,
   choices=[
     "That secure tenure allows a court to function independent of the current political climate",
     "That courts follow precedent when deciding cases with similar facts",
     "That judicial review checks the power of the other branches",
     "That the judiciary has neither force nor will but merely judgment",
     "That unpopular decisions lead to debate about a court's power"], ans=0,
   why="EK 2.10.A.1's first link is tenure producing independence, and a table pairing tenure rules with rates of ruling against the government measures exactly that link. The other options name claims these columns do not test."),

 dict(q=_TENURE + " A student concludes from these data that changing a country's tenure rule would change how its court rules. Which limitation of the data most undercuts that conclusion?",
   table=_TENURE_TABLE,
   choices=[
     "Countries that adopt secure tenure may differ from others in many ways, so the tenure rule may not be what produces the difference",
     "The table omits the tenure rule, so no comparison is possible",
     "The table reports a single group of courts, so no comparison is possible",
     "The table reports counts rather than percentages, so no rate can be computed",
     "The table shows no difference between the groups"], ans=0,
   why="Comparing countries that already differ cannot isolate one institutional feature, which is the standard limitation of a cross-national comparison. All four groups, the tenure column and the percentage column are plainly present."),

 dict(q=_APPROVAL + " Which conclusion is best supported by the data?",
   table=_APPROVAL_TABLE,
   choices=[
     "Approval fell by seventeen points and disapproval rose by nineteen, so the decision cost the court substantial public support",
     "Approval and disapproval both fell after the decision",
     "A majority still approved of the court after the decision",
     "The share with no opinion rose sharply after the decision",
     "Disapproval exceeded approval before the decision"], ans=0,
   why="Approval runs 58 to 41 and disapproval 27 to 46. Approval ends below half, the no-opinion share falls slightly, and approval led disapproval by thirty-one points beforehand."),

 dict(q=_APPROVAL + " Which link in EK 2.10.A.1's chain do these data most directly illustrate?",
   table=_APPROVAL_TABLE,
   choices=[
     "That an unpopular decision can lead to debate about the court's power, since public support is what such debate draws on",
     "That life tenure allows the court to function independent of the political climate",
     "That the court follows precedent in cases with similar facts",
     "That judicial appointments are the president's longest lasting influence",
     "That the court can enforce its own decisions"], ans=0,
   why="The table measures what happens to public standing AFTER an unpopular decision, which is the third link. The first link concerns tenure, which the table does not report."),

 dict(q=_APPROVAL + " Which conclusion about the court's independence do these data support?",
   table=_APPROVAL_TABLE,
   choices=[
     "The court issued the decision despite the cost to its public standing, which is what tenure makes possible",
     "The court issued the decision because it expected public approval to rise",
     "The court's public standing was unaffected by the decision",
     "The court reversed the decision after approval fell",
     "The court's members lost their seats as a result of the decision"], ans=0,
   why="EK 2.10.A.1 says independence is what allows a court to deliver an unpopular decision, and a seventeen point fall in approval is the price the table records. Nothing in the table shows a reversal or any loss of office."),

 dict(q="Which of the following would most WEAKEN EK 2.10.A.1's first link, that life tenure allows a court to function independent of the political climate?",
   choices=[
     "Evidence that justices with life tenure vote in line with the preferences of the presidents who appointed them across their whole careers",
     "Evidence that justices with life tenure sometimes issue unpopular decisions",
     "Evidence that justices with life tenure are criticized by elected officials",
     "Evidence that justices with life tenure serve for many decades",
     "Evidence that justices with life tenure are confirmed by the Senate"], ans=0,
   why="The first link claims tenure removes political dependence, so the rebuttal must show that outcomes track a political variable anyway. The other four options are all consistent with the link rather than against it."),

 dict(q="Which of the following would most WEAKEN EK 2.10.A.1's third link, that unpopular decisions can lead to debate about the court's power?",
   choices=[
     "Evidence that periods of intense criticism of the court have not been preceded by unusually unpopular decisions",
     "Evidence that some court decisions are unpopular",
     "Evidence that the court has life tenure",
     "Evidence that the court sometimes rules against the government",
     "Evidence that elected officials sometimes praise the court"], ans=0,
   why="The third link connects unpopular decisions to debate, so the rebuttal must break the connection by showing debate arising without them. Note the framework says CAN LEAD TO, so occasional exceptions do not by themselves refute it."),

 dict(q="A student writes that EK 2.10.A.1 says life tenure guarantees that a court will rule independently. What is the correction?",
   choices=[
     "The framework says life tenure ALLOWS independence, which is a claim about what becomes possible rather than about what must occur",
     "The framework says life tenure prevents independence",
     "The framework says nothing about life tenure",
     "The framework says independence is guaranteed by Senate confirmation",
     "The framework says independence depends on public approval"], ans=0,
   why="EK 2.10.A.1's verbs are ALLOWS and CAN at every step, so the statement describes a capacity rather than a certainty. Reading a permissive claim as a guarantee is the most common misuse of this sentence."),

 dict(q="Which question would best test EK 2.10.A.1's account as a whole?",
   choices=[
     "Do courts with more secure tenure rule against the government more often, and does public criticism of a court follow its least popular decisions?",
     "How many cases does the court decide each year?",
     "How long is the average opinion the court issues?",
     "How many justices sit on the court?",
     "How often does the court hear cases from a particular state?"], ans=0,
   why="EK 2.10.A.1 is a chain with three links, and testing it as a whole means measuring the first link (tenure to independence) and the third (unpopular decisions to debate) together. Caseload, opinion length and Court size test none of them."),
]
