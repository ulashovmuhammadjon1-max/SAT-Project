# AP U.S. GOVERNMENT AND POLITICS 2.3 Congressional Behavior -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# Learning objective 2.3.A: explain how congressional behavior is influenced by
# election processes, partisanship, and divided government.
# Suggested skill for this topic (CED p. 62): 2.A, describe the facts, issue,
# holding, reasoning, decision and majority opinion of required cases.
#
# THE TOPIC TITLE HIDES ITS OWN CONTENTS. "Congressional Behavior" says nothing
# about districting or about representational roles, and both live here:
# EK 2.3.A.2 is where Baker v. Carr and Shaw v. Reno attach, and EK 2.3.A.4 is
# where the trustee / delegate / politico distinction lives. See
# AP_US_GOV_CED.md note 12. A bank that files those elsewhere leaves this topic
# looking thin and leaves the student unable to find them.
#
# Essential knowledge relied on, with the CED's own parenthetical definitions,
# which are the examinable text:
#   EK 2.3.A.1 -- behavior and governing effectiveness are influenced by
#     ideological divisions between parties. PARTISAN VOTING is "when members of
#     Congress vote based on their political party affiliation"; POLARIZATION is
#     "when political attitudes move toward ideological extremes"; GRIDLOCK is
#     "a situation in which no congressional action on legislation can be taken
#     due to a lack of consensus." Note the chain: partisan voting and
#     polarization CAN LEAD TO gridlock. They are three distinct things, not
#     three names for one.
#   EK 2.3.A.2 -- gerrymandering, redistricting and unequal representation of
#     constituencies "have been PARTIALLY addressed by Supreme Court cases that
#     opened the door for equal protection challenges to redistricting." The
#     word "partially" is the framework's own and items here respect it.
#   EK 2.3.A.3 -- DIVIDED GOVERNMENT is "when one party controls the presidency
#     and the other party controls at least one of the chambers of Congress."
#     It can lead to more intense partisanship, which "can result in members of
#     Congress voting against presidential initiatives and appointments,
#     especially those of a LAME DUCK president."
#   EK 2.3.A.4 -- accountability is affected by how representatives perceive
#     their roles: a TRUSTEE "will vote on issues based on their own knowledge
#     and judgement"; a DELEGATE "sees themselves as an agent of those who
#     elected them and will vote on issues based on the interests of their
#     constituents"; a POLITICO "uses a combination of these role conceptions."
#
# THE DEFINITION MOST OFTEN GOT BACKWARDS is divided government. The CED's
# threshold is AT LEAST ONE chamber, not both: a president of one party facing
# an opposing majority in the Senate alone is divided government. Item 13 is
# built on precisely that boundary.
#
# Required cases the CED attaches to 2.3.A (p. 31-32): Baker v. Carr,
# Shaw v. Reno.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: no case is quoted; both holdings are
# stated in the CED's own words as AP_US_GOV_CED.md reproduces them. Both tables
# are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. Vote splits
# are written in words ("five to four"), because mathfmt.convert would typeset
# the numeric form as subtraction. The verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.3", "Congressional Behavior", 2)

_PARTY = ("In a hypothetical national legislature, the table reports the share of recorded "
          "votes on which a majority of one party voted against a majority of the other, "
          "and the number of major bills enacted, in three periods.")
_PARTY_TABLE = dict(
    headers=["Period", "Votes dividing the parties (%)", "Major bills enacted"],
    rows=[["Earliest", "38", "94"],
          ["Middle", "57", "71"],
          ["Latest", "76", "42"]])

_ROLES = ("In a hypothetical survey, legislators were asked which consideration weighs most "
          "heavily when their own judgement conflicts with district opinion.")
_ROLES_TABLE = dict(
    headers=["Stated approach", "Safe district members (%)", "Competitive district members (%)"],
    rows=[["Own knowledge and judgement", "46", "21"],
          ["The interests of constituents", "29", "58"],
          ["A combination of the two", "25", "21"]])

QUESTIONS = [
 dict(q="According to the course framework, partisan voting is best defined as",
   choices=[
     "members of Congress voting based on their political party affiliation",
     "political attitudes moving toward ideological extremes",
     "a situation in which no congressional action can be taken for lack of consensus",
     "one party controlling the presidency while the other controls a chamber of Congress",
     "a legislator voting according to personal judgement rather than constituent opinion"], ans=0,
   why="EK 2.3.A.1 gives this definition in its own parenthesis. The second option is its definition of polarization and the third its definition of gridlock, which are distinct concepts in the same sentence."),

 dict(q="According to the course framework, polarization is best defined as",
   choices=[
     "political attitudes moving toward ideological extremes",
     "members of Congress voting based on their party affiliation",
     "the inability of Congress to act for lack of consensus",
     "the drawing of district lines to favor one party",
     "a president's party losing seats in a midterm election"], ans=0,
   why="EK 2.3.A.1 defines polarization as attitudes moving toward ideological extremes. Partisan voting is a behavior and polarization is a distribution of attitudes; the framework keeps them separate."),

 dict(q="According to the course framework, gridlock is best defined as",
   choices=[
     "a situation in which no congressional action on legislation can be taken due to a lack of consensus",
     "the practice of voting with one's party on most recorded votes",
     "the movement of political attitudes toward ideological extremes",
     "the use of a filibuster to prolong debate on a single bill",
     "a president's refusal to sign legislation passed by Congress"], ans=0,
   why="EK 2.3.A.1 defines gridlock in exactly these words. A filibuster is a Senate procedure under EK 2.2.A.3.ii and may contribute to gridlock without being gridlock."),

 dict(q="How does the course framework relate partisan voting, polarization and gridlock to one another?",
   choices=[
     "Partisan voting and polarization can lead to gridlock, so the three are distinct and causally ordered",
     "The three terms are interchangeable names for the same phenomenon",
     "Gridlock causes polarization, which in turn causes partisan voting",
     "Polarization prevents partisan voting, which is why gridlock occurs",
     "The framework treats all three as unrelated to congressional behavior"], ans=0,
   why="EK 2.3.A.1's sentence runs in one direction: partisan voting and polarization 'can lead to gridlock.' Collapsing the three or reversing the arrow both misstate the framework."),

 dict(q="A legislature records a large majority of its votes with nearly every member of each party opposing nearly every member of the other, and few major bills pass. Which sequence best describes what the course framework says is happening?",
   choices=[
     "Polarized attitudes produce partisan voting, and the resulting lack of consensus produces gridlock",
     "Gridlock produces polarization, which then produces partisan voting",
     "Partisan voting produces polarization, which then eliminates gridlock",
     "The absence of consensus produces polarization, which then prevents partisan voting",
     "None of these, because the framework makes no claim about the relationship"], ans=0,
   why="EK 2.3.A.1 places ideological division upstream and gridlock downstream, with partisan voting as the behavior in between. The observed pattern of party-line votes and few enactments is that chain."),

 dict(q="Which of the following would be evidence of gridlock as the course framework defines it, rather than merely of partisan voting?",
   choices=[
     "Bills with substantial support in both chambers failed to be enacted because no consensus could be assembled",
     "Most members of each party voted together on most recorded votes",
     "A survey found that members' policy positions had grown further apart",
     "One party gained a majority in a chamber it had not previously controlled",
     "A committee chair scheduled hearings on a bill the minority opposed"], ans=0,
   why="Gridlock is defined by the ABSENCE OF ACTION for lack of consensus, so the evidence has to be legislation not enacted. Party-line voting and growing distance between positions are the other two concepts in EK 2.3.A.1."),

 dict(q="According to the course framework, gerrymandering, redistricting and unequal representation of constituencies have been",
   choices=[
     "partially addressed by Supreme Court cases that opened the door for equal protection challenges to redistricting",
     "completely resolved by a constitutional amendment prohibiting the practice",
     "left entirely to the states, with no role for the federal courts",
     "transferred to Congress, which now draws all congressional districts",
     "eliminated by statute in every state"], ans=0,
   why="EK 2.3.A.2 uses the word PARTIALLY and credits Supreme Court cases with opening the door to equal protection challenges. The framework does not claim the problem was solved."),

 dict(q="In Baker v. Carr (1962), the Supreme Court held that redistricting did not raise political questions, allowing federal courts to hear cases challenging redistricting plans that may violate the Equal Protection Clause of the Fourteenth Amendment. What did the decision change?",
   choices=[
     "It made districting claims justiciable, so a court could decide them rather than dismissing them as political",
     "It required every state to adopt an independent redistricting commission",
     "It transferred the drawing of district lines from state legislatures to federal courts",
     "It held that districts must be equal in geographic area",
     "It held that race may never be considered in drawing a district"], ans=0,
   why="The CED states the holding as redistricting not raising political questions, which is a rule about whether a court may hear the case at all. Shaw v. Reno, not Baker, concerns race as a factor in line drawing."),

 dict(q="In Shaw v. Reno (1993), the Supreme Court held that majority-minority districts created under the Voting Rights Act of 1965 may be constitutionally challenged by voters if race is the only factor used in creating the district. Which statement of the holding is accurate?",
   choices=[
     "Such districts are open to challenge when race was the sole factor, not whenever race was considered at all",
     "Such districts are unconstitutional in every case",
     "Such districts may never be challenged once approved under the Voting Rights Act",
     "The decision required states to create additional majority-minority districts",
     "The decision applied only to districts drawn for state legislatures"], ans=0,
   why="The CED's wording is 'if race is the only factor used in creating the district,' which is a narrower rule than a ban on considering race. Overstating it is the most common error about this case."),

 dict(q="How do Baker v. Carr and Shaw v. Reno differ in what they decided?",
   choices=[
     "Baker held that districting claims may be heard in federal court; Shaw held what may make a particular district unconstitutional",
     "Baker held that districting claims may not be heard; Shaw held that they may",
     "Both cases concerned the sole use of race in drawing districts",
     "Both cases held that districting is a political question courts may not decide",
     "Baker concerned congressional districts and Shaw concerned the Electoral College"], ans=0,
   why="Baker is about justiciability, the threshold question, and Shaw about the substantive standard once a court reaches the merits. The CED's statements of the two holdings differ in exactly that way."),

 dict(q="A non-required case: voters challenge a state's congressional map, alleging that one district contains three times the population of another in the same state. A federal court agrees to hear the case. Which required case established that a federal court may do so?",
   choices=[
     "Baker v. Carr (1962), which held that redistricting did not raise political questions",
     "Shaw v. Reno (1993), which held that majority-minority districts may be challenged if race is the only factor used",
     "McCulloch v. Maryland (1819), which established the supremacy of federal law over state law",
     "United States v. Lopez (1995), which held that Congress exceeded its Commerce Clause power",
     "Marbury v. Madison (1803), which established the principle of judicial review"], ans=0,
   why="Unequal district populations are the Baker fact pattern, and the CED states that holding as redistricting not presenting political questions. Judicial review supplies the court's general authority, not the rule that makes this claim justiciable."),

 dict(q="According to the course framework, divided government exists when",
   choices=[
     "one party controls the presidency and the other party controls at least one chamber of Congress",
     "one party controls the presidency and the other party controls both chambers of Congress",
     "neither party holds a majority in either chamber of Congress",
     "the president's party holds a majority in both chambers",
     "the Supreme Court's majority was appointed by presidents of both parties"], ans=0,
   why="EK 2.3.A.3's threshold is AT LEAST ONE chamber, so control of both is sufficient but not necessary. The second option states a stricter condition than the framework does."),

 dict(q="A president of one party faces a Senate controlled by the other party while her own party holds a majority in the House. Under the course framework's definition, this situation is",
   choices=[
     "divided government, because the opposing party controls at least one chamber",
     "unified government, because the president's party controls a chamber",
     "unified government, because the opposing party does not control both chambers",
     "neither, because the framework's definition applies only to the House",
     "gridlock, which the framework treats as the same thing as divided government"], ans=0,
   why="EK 2.3.A.3 requires only that the other party control at least one chamber, and the Senate is one. Gridlock is a separate concept defined in EK 2.3.A.1 as an inability to act."),

 dict(q="According to the course framework, one consequence of divided government is that members of Congress may vote against",
   choices=[
     "presidential initiatives and appointments, especially those of a lame duck president",
     "their own party's leadership on procedural questions",
     "all legislation originating in the other chamber",
     "any bill reported by a committee they do not sit on",
     "the confirmation of judges nominated by presidents of their own party"], ans=0,
   why="EK 2.3.A.3 names presidential initiatives AND appointments and singles out the lame duck president. The other options describe behaviors the framework does not attribute to divided government."),

 dict(q="Why would opposition to a president's nominees be especially pronounced late in that president's final term?",
   choices=[
     "A president whose successor will soon be chosen has less leverage, and opponents can hope for a nominee more to their liking",
     "A lame duck president loses the constitutional power to nominate",
     "The Senate is constitutionally barred from confirming nominees in a president's final year",
     "Nominations lapse automatically at the end of each calendar year regardless of Senate action",
     "A lame duck president's party automatically loses its majority in both chambers"], ans=0,
   why="EK 2.3.A.3 names the lame duck president specifically, and the mechanism is the expected change in who will be nominating. No constitutional rule strips a president of the nomination power before the term ends."),

 dict(q="According to the course framework, a representative who votes on issues based on their own knowledge and judgement is acting as",
   choices=[
     "a trustee",
     "a delegate",
     "a politico",
     "a partisan",
     "a conferee"], ans=0,
   why="EK 2.3.A.4.i defines the trustee role in exactly these terms. The delegate at EK 2.3.A.4.ii votes on the interests of constituents, and the politico at EK 2.3.A.4.iii combines the two."),

 dict(q="A representative who sees herself as an agent of those who elected her and votes according to their interests is acting as",
   choices=[
     "a delegate",
     "a trustee",
     "a politico",
     "a whip",
     "a conferee"], ans=0,
   why="EK 2.3.A.4.ii defines the delegate as an agent of those who elected the member, voting on the basis of constituent interests, which is exactly the description in the stem."),

 dict(q="A representative votes with district opinion on issues his constituents follow closely and according to his own judgement on technical matters they do not. His approach is best described as",
   choices=[
     "the politico role, which combines the trustee and delegate conceptions",
     "the trustee role, since he sometimes uses his own judgement",
     "the delegate role, since he sometimes follows constituent opinion",
     "partisan voting, since he sometimes votes with his party",
     "gridlock, since he does not follow a single rule"], ans=0,
   why="EK 2.3.A.4.iii defines the politico as a member who uses a combination of the trustee and delegate conceptions, and a rule that switches by issue is that combination. Naming only one half describes only part of his behavior."),

 dict(q="A member of Congress votes for a treaty her constituents oppose, saying that she has studied the agreement in detail and believes it serves the country. Which role conception does her explanation invoke?",
   choices=[
     "The trustee role, since she rests the vote on her own knowledge and judgement",
     "The delegate role, since she claims to serve those who elected her",
     "The politico role, since she considered constituent opinion before rejecting it",
     "Partisan voting, since treaties are ratified by party-line votes",
     "None of the three, since role conceptions apply only to domestic legislation"], ans=0,
   why="EK 2.3.A.4.i's trustee votes on the basis of their own knowledge and judgement, which is the explanation she gives. Merely knowing what constituents think does not make a vote against them a politico's combination."),

 dict(q="According to the course framework, how do these role conceptions matter?",
   choices=[
     "Accountability to constituents in each chamber is affected by how representatives perceive their roles",
     "They determine which committee a member is assigned to",
     "They determine whether a member may file a discharge petition",
     "They establish the order in which members are recognized to speak",
     "They determine the outcome of conference committee negotiations"], ans=0,
   why="EK 2.3.A.4's opening sentence ties the three roles to accountability to constituents in each chamber. The framework attaches no procedural consequences to them."),

 dict(q=_PARTY + " Which conclusion is best supported by the data?",
   table=_PARTY_TABLE,
   choices=[
     "The share of party-dividing votes rose across the three periods while the number of major bills enacted fell",
     "Both the share of party-dividing votes and the number of major bills enacted rose",
     "The share of party-dividing votes exceeded half in every period",
     "More major bills were enacted in the latest period than in the earliest",
     "The number of major bills enacted stayed roughly constant across the three periods"], ans=0,
   why="The vote share runs 38, 57 and 76 while enactments run 94, 71 and 42. The earliest figure of 38 is below half, and enactments fall by more than half across the three periods."),

 dict(q=_PARTY + " Which claim from the course framework do these data most directly illustrate?",
   table=_PARTY_TABLE,
   choices=[
     "That partisan voting and polarization can lead to gridlock, a situation in which action cannot be taken for lack of consensus",
     "That divided government exists when one party controls the presidency and the other controls a chamber",
     "That representatives may conceive of their role as trustee, delegate or politico",
     "That gerrymandering has been partially addressed by Supreme Court cases",
     "That committee leadership is determined by the majority political party"], ans=0,
   why="Rising party-line voting alongside falling enactments is EK 2.3.A.1's chain from partisan voting to gridlock. The other four options each name a different essential-knowledge statement that these columns do not measure."),

 dict(q=_PARTY + " A student concludes that rising partisanship CAUSED the decline in enactments. Which limitation of the data most undercuts that conclusion?",
   table=_PARTY_TABLE,
   choices=[
     "Two series moving in opposite directions may both be responding to something else, and the table reports no other variable",
     "The table omits the number of major bills enacted, so no comparison is possible",
     "The table reports only a single period, so no trend can be seen",
     "The table gives percentages that do not sum to one hundred across the three periods",
     "The table shows the two series moving in the same direction, which rules out any relationship"], ans=0,
   why="A two-column table showing opposite trends is consistent with causation in either direction and with a common cause, which is the standard limitation. The table plainly carries both series across three periods."),

 dict(q=_ROLES + " Which conclusion is best supported by the data?",
   table=_ROLES_TABLE,
   choices=[
     "Members from safe districts most often name their own judgement, while members from competitive districts most often name constituent interests",
     "Members from both kinds of district most often name their own judgement",
     "A majority of members in both groups name a combination of the two approaches",
     "Members from competitive districts name their own judgement more often than safe district members do",
     "The same share of each group names constituent interests"], ans=0,
   why="Own judgement leads the safe column at 46 percent and constituent interests leads the competitive column at 58 percent. The combination row is 25 and 21, a minority in both groups."),

 dict(q=_ROLES + " Which of the framework's three role conceptions does the middle row of the table describe, and which does the first row describe?",
   table=_ROLES_TABLE,
   choices=[
     "The middle row describes the delegate and the first row describes the trustee",
     "The middle row describes the trustee and the first row describes the delegate",
     "Both rows describe the politico, in different words",
     "The middle row describes the politico and the first row describes the delegate",
     "Neither row corresponds to any of the framework's three role conceptions"], ans=0,
   why="EK 2.3.A.4.i's trustee votes on their own knowledge and judgement, which is the first row, and EK 2.3.A.4.ii's delegate votes on constituent interests, which is the middle row. The third row is the politico's combination."),

 dict(q=_ROLES + " Which explanation for the pattern in the data is most consistent with the course framework?",
   table=_ROLES_TABLE,
   choices=[
     "Members whose seats are at risk face sharper electoral accountability, which pushes them toward the delegate conception",
     "Members from safe districts are constitutionally required to vote on their own judgement",
     "Members from competitive districts are prohibited from exercising independent judgement",
     "The framework predicts that district competitiveness has no relationship to role conception",
     "Members from safe districts have no constituents to represent"], ans=0,
   why="EK 2.3.A.4's opening sentence ties role conceptions to accountability to constituents, and a competitive seat makes that accountability more immediate. Nothing constitutional or statutory dictates a member's role conception."),

 dict(q="Which of the following best explains why divided government can intensify partisanship rather than merely dividing control?",
   choices=[
     "Each party holds an institution it can use against the other, so conflict becomes the ordinary way of doing business",
     "Divided government suspends the constitutional powers of the branch the president does not control",
     "Divided government requires that all legislation pass by a two-thirds vote",
     "Divided government prevents committees from holding hearings",
     "Divided government transfers the veto power to the majority party in Congress"], ans=0,
   why="EK 2.3.A.3 says elections producing divided government can lead to more intense partisanship, and the mechanism is that each side controls a lever the other must get past. No constitutional rule changes when control divides."),

 dict(q="A commentator argues that congressional gridlock is a failure of individual legislators rather than a product of institutional conditions. Which evidence from the course framework most directly complicates that argument?",
   choices=[
     "Gridlock is tied to ideological division between the parties and to divided government, both of which are conditions no single member controls",
     "Gridlock is defined as a situation in which one member blocks all legislation",
     "Gridlock occurs only when a president is in the final year of a term",
     "Gridlock is a formal procedure available in the Senate but not the House",
     "Gridlock is a role conception a member may adopt"], ans=0,
   why="EK 2.3.A.1 attributes gridlock to a lack of consensus arising from ideological divisions, and EK 2.3.A.3 adds divided government, neither of which is a choice available to an individual member."),

 dict(q="Which question would best test the framework's claim that divided government intensifies partisanship?",
   choices=[
     "Do party-line votes and rejections of presidential nominees occur more often in periods of divided than of unified control?",
     "Do members of Congress hold more town meetings during periods of divided control?",
     "Are more bills introduced during periods of divided control?",
     "Do presidents issue more public statements during periods of divided control?",
     "Are committee chairs more experienced during periods of divided control?"], ans=0,
   why="EK 2.3.A.3's claim is about partisanship expressed as votes against presidential initiatives and appointments, so the test has to compare those behaviors across periods of divided and unified control."),

 dict(q="A student writes that a legislator must be either a trustee or a delegate. Which correction does the course framework most directly support?",
   choices=[
     "The framework names a third conception, the politico, which uses a combination of the two",
     "The framework names only the trustee, since a delegate exercises no judgement at all",
     "The framework names only the delegate, since every member is accountable to voters",
     "The framework treats the two as identical in practice",
     "The framework says a legislator's role conception is fixed by the chamber in which they serve"], ans=0,
   why="EK 2.3.A.4.iii names the politico as a member who uses a combination of these role conceptions, so the pair is not exhaustive. Nothing in the framework assigns a role conception by chamber."),
]
