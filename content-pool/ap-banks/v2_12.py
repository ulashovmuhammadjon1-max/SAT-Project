# AP U.S. GOVERNMENT AND POLITICS 2.12 The Bureaucracy -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# Learning objective 2.12.A: explain how the bureaucracy carries out the
# responsibilities of the federal government.
# Suggested skill for this topic (CED p. 72): 4.B, explain how the argument or
# perspective in the SOURCE relates to political principles, institutions,
# processes, policies and behaviors.
#
# Essential knowledge relied on:
#   EK 2.12.A.1 -- "The federal bureaucracy is composed of DEPARTMENTS,
#     AGENCIES, COMMISSIONS, AND GOVERNMENT CORPORATIONS that implement policy
#     by:
#       i.   Writing and enforcing regulations
#       ii.  Issuing fines
#       iii. Testifying before Congress
#       iv.  Forming IRON TRIANGLES (alliances of congressional committees,
#            bureaucratic agencies, and interest groups that are prominent in
#            specific policy areas)
#       v.   Creating ISSUE NETWORKS (temporary coalitions that form to promote
#            a common issue or agenda)"
#   EK 2.12.A.2 -- "The civil service primarily uses a MERIT SYSTEM that
#     prioritizes hiring and promotion based on PROFESSIONALISM,
#     SPECIALIZATION, AND NEUTRALITY, as opposed to POLITICAL PATRONAGE, whereby
#     bureaucratic jobs are politically appointed."
#
# THE TWO PARENTHETICAL DEFINITIONS ARE EXAMINABLE TEXT AND THEY DIFFER ON TWO
# AXES, not one. Items 9 to 14 are built on both:
#   * MEMBERSHIP. An iron triangle has exactly THREE named corners --
#     congressional committees, bureaucratic agencies, interest groups. An issue
#     network is an open coalition with no fixed membership.
#   * DURATION. The CED calls an issue network TEMPORARY and calls an iron
#     triangle an ALLIANCE PROMINENT IN A SPECIFIC POLICY AREA, which is a
#     standing relationship. A student who knows only "triangles have three
#     sides" cannot tell which one a scenario describes when the coalition
#     happens to contain three kinds of actor.
#
# THE MERIT SYSTEM'S THREE CRITERIA ARE A CLOSED LIST: professionalism,
# specialization, NEUTRALITY. The third is the one that does the work in this
# topic, because it is what a patronage system cannot supply and what makes an
# agency's advice worth having when the administration changes. Items 15 to 20
# turn on it. Note also the CED's hedge: the civil service PRIMARILY uses a
# merit system, so political appointment persists at the top and item 18 says so.
#
# Documents the CED attaches to 2.12.A (p. 26-27): Federalist No. 70.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: Federalist No. 70 and constitutional
# text are quoted verbatim. The CED's illustrative examples for this topic --
# the FCC, the Pendleton Act, the TSA -- are marked NOT REQUIRED and none is
# named; the agencies used in scenarios are the ones EK 2.13.A.1 lists as
# required course content, or are unnamed.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. The
# verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.12", "The Bureaucracy", 2)

_HIRING = ("In a hypothetical national government, the table reports how positions in the "
           "executive branch were filled in three eras.")
_HIRING_TABLE = dict(
    headers=["Era", "Positions filled by competitive examination (%)", "Positions filled by political appointment (%)"],
    rows=[["Early era", "8", "92"],
          ["Middle era", "56", "44"],
          ["Recent era", "89", "11"]])

_ACTIONS = ("In a hypothetical study, the table reports how many times agencies in four policy "
            "areas took each kind of action in one year.")
_ACTIONS_TABLE = dict(
    headers=["Policy area", "Regulations issued", "Fines imposed", "Appearances before Congress"],
    rows=[["Environment", "214", "1,860", "31"],
          ["Transportation", "168", "940", "22"],
          ["Financial regulation", "97", "2,310", "40"],
          ["Veterans affairs", "45", "12", "17"]])

QUESTIONS = [
 dict(q="According to the course framework, the federal bureaucracy is composed of",
   choices=[
     "departments, agencies, commissions, and government corporations",
     "the two chambers of Congress and their committees",
     "the federal courts and their supporting offices",
     "the president, the vice president, and the Cabinet alone",
     "state agencies operating under federal supervision"], ans=0,
   why="EK 2.12.A.1 names exactly these four kinds of organization. The other options describe the other branches or a level of government the framework does not include in the federal bureaucracy."),

 dict(q="Which of the following is one of the ways the course framework says the bureaucracy implements policy?",
   choices=[
     "Writing and enforcing regulations",
     "Enacting statutes without congressional involvement",
     "Confirming the president's nominees",
     "Ratifying treaties with foreign governments",
     "Trying impeachments brought by the House"], ans=0,
   why="EK 2.12.A.1.i names writing and enforcing regulations. The other four options describe powers belonging to Congress or its chambers rather than to any agency."),

 dict(q="An agency finds that a company violated a rule the agency had issued and requires it to pay a penalty. Which of the framework's listed activities is this?",
   choices=[
     "Issuing fines",
     "Testifying before Congress",
     "Forming an iron triangle",
     "Creating an issue network",
     "Writing a regulation"], ans=0,
   why="EK 2.12.A.1.ii names issuing fines as a distinct activity from writing regulations, which EK 2.12.A.1.i covers. The agency here is enforcing a rule it had already written."),

 dict(q="An agency administrator appears before a congressional committee to answer questions about how her agency has spent its appropriation. Which listed activity is this, and which branch's power does it serve?",
   choices=[
     "Testifying before Congress, which serves Congress's oversight power",
     "Issuing fines, which serves the agency's enforcement power",
     "Writing regulations, which serves the president's management power",
     "Forming an iron triangle, which serves an interest group's influence",
     "Creating an issue network, which serves a temporary coalition"], ans=0,
   why="EK 2.12.A.1.iii names testifying before Congress, and EK 2.14.A.1.ii names investigation and committee hearings of bureaucratic activity as a form of oversight. The same event is on both lists from opposite sides."),

 dict(q="According to the course framework, an iron triangle is an alliance of",
   choices=[
     "congressional committees, bureaucratic agencies, and interest groups",
     "the president, the Cabinet, and the Executive Office of the President",
     "the House, the Senate, and the president",
     "federal courts, state courts, and administrative law judges",
     "three federal agencies working on a shared problem"], ans=0,
   why="EK 2.12.A.1.iv names exactly these three corners. The fifth option is the mistake of counting to three without checking WHICH three the framework names."),

 dict(q="According to the course framework, an issue network is",
   choices=[
     "a temporary coalition that forms to promote a common issue or agenda",
     "a permanent alliance among three fixed kinds of actor",
     "an association of federal agencies within a single department",
     "a committee of Congress with jurisdiction over one policy area",
     "a court-supervised body that resolves disputes among agencies"], ans=0,
   why="EK 2.12.A.1.v defines an issue network as a TEMPORARY coalition formed to promote a common issue or agenda, and the word temporary is the framework's own."),

 dict(q="What are the two most important differences between an iron triangle and an issue network as the framework defines them?",
   choices=[
     "An iron triangle has three fixed kinds of member and is a standing alliance; an issue network has open membership and is temporary",
     "An iron triangle is temporary and an issue network is permanent",
     "An iron triangle involves interest groups and an issue network does not",
     "An iron triangle operates in Congress and an issue network operates in the courts",
     "An iron triangle is created by statute and an issue network by executive order"], ans=0,
   why="EK 2.12.A.1.iv names three specific corners and describes an alliance prominent in a policy area; EK 2.12.A.1.v says temporary and does not fix membership. Membership and duration are the two axes."),

 dict(q="A committee chair, a bureau chief and the head of a trade association have worked together on the same policy area for many years, and each supports the others' interests. Which concept does this best illustrate?",
   choices=[
     "An iron triangle, since the three named corners work together in a specific policy area over time",
     "An issue network, since three parties formed a coalition",
     "An issue network, since the three come from different institutions",
     "Congressional oversight, since a committee chair is involved",
     "The merit system, since each holds a specialized position"], ans=0,
   why="The three actors are exactly EK 2.12.A.1.iv's corners and the relationship is durable and policy-specific. That a coalition contains three parties does not make it a triangle, which is why the second option fails."),

 dict(q="Journalists, several advocacy organizations, two agencies and a group of academic researchers come together for eighteen months to press for a change in one policy, then disperse. Which concept does this best illustrate?",
   choices=[
     "An issue network, since it is a temporary coalition formed to promote a common issue",
     "An iron triangle, since agencies and outside groups are both involved",
     "An iron triangle, since it concerns a single policy area",
     "Congressional oversight, since Congress is the target",
     "Political patronage, since participants were not hired by examination"], ans=0,
   why="EK 2.12.A.1.v's issue network is temporary and open in membership, and the coalition here contains actors outside the three corners and dissolves. Concerning one policy area is true of both concepts and does not distinguish them."),

 dict(q="Why does the framework's account of iron triangles matter for how policy is actually made?",
   choices=[
     "A durable alliance among the committee, the agency and the affected groups can shape a policy area with little participation from anyone else",
     "It shows that agencies are prohibited from communicating with interest groups",
     "It shows that Congress has no role in policy areas covered by an agency",
     "It shows that interest groups may issue regulations",
     "It shows that policy areas are assigned to agencies by the courts"], ans=0,
   why="A relationship among the three actors with the greatest stake and the greatest information can settle questions before they reach a wider audience. The other options assert prohibitions and powers that do not exist."),

 dict(q="According to the course framework, the civil service primarily uses",
   choices=[
     "a merit system that prioritizes hiring and promotion based on professionalism, specialization, and neutrality",
     "political patronage, whereby jobs are politically appointed",
     "election of agency officials by the voters",
     "appointment by the federal courts",
     "selection by lot from among qualified applicants"], ans=0,
   why="EK 2.12.A.2 names the merit system and its three criteria, and contrasts it with political patronage, which is the second option and the system it replaced."),

 dict(q="Which three criteria does the framework name as what a merit system prioritizes?",
   choices=[
     "Professionalism, specialization, and neutrality",
     "Loyalty, seniority, and geographic balance",
     "Party affiliation, seniority, and experience",
     "Education, wealth, and residence",
     "Neutrality, party affiliation, and specialization"], ans=0,
   why="EK 2.12.A.2's list is exactly these three. The fifth option is the trap: it keeps two of the three and substitutes party affiliation, which is what the merit system is defined AGAINST."),

 dict(q="According to the course framework, political patronage is a system in which",
   choices=[
     "bureaucratic jobs are politically appointed",
     "bureaucratic jobs are filled by competitive examination",
     "bureaucratic jobs are filled by the courts",
     "agencies are prohibited from hiring anyone",
     "agency heads are elected by the voters"], ans=0,
   why="EK 2.12.A.2 defines patronage in exactly these words as the contrast to the merit system. The second option describes the merit system's method rather than patronage's."),

 dict(q="Which of the three merit criteria is most directly at stake when an agency's staff continues to apply the same technical standards after a change of administration?",
   choices=[
     "Neutrality, since the standards did not change with the political leadership",
     "Specialization, since technical standards require expertise",
     "Professionalism, since the staff followed established procedures",
     "Patronage, since the staff kept their jobs",
     "Seniority, since experienced staff remained in place"], ans=0,
   why="All three criteria are present in a competent agency, but the fact that CHANGED political leadership did not change the standards is specifically what neutrality means in EK 2.12.A.2's list."),

 dict(q="Why does a merit-based civil service make an agency's expert advice more useful to a president than a patronage-based one would?",
   choices=[
     "Advice from officials who did not owe their jobs to the administration is more likely to report what is true rather than what is wanted",
     "Officials hired by examination are prohibited from advising the president",
     "Officials hired by examination serve fixed terms and cannot be replaced",
     "Officials hired by examination are elected by the voters",
     "Officials hired by examination outrank the Cabinet"], ans=0,
   why="Neutrality is valuable precisely because it removes the incentive to tell the appointing power what it wants to hear, which is the same institutional logic as Article III's tenure protections."),

 dict(q="The course framework says the civil service PRIMARILY uses a merit system. What does that qualification acknowledge?",
   choices=[
     "That some positions, particularly senior ones, are still filled by political appointment",
     "That the merit system applies only in wartime",
     "That the merit system was repealed and later restored",
     "That merit and patronage are the same system under different names",
     "That agencies may ignore the merit system whenever they choose"], ans=0,
   why="EK 2.12.A.2's word 'primarily' leaves room for the political appointments EK 2.5.A.1 records as subject to Senate confirmation, which sit at the top of departments and agencies."),

 dict(q="What is the strongest argument in favor of filling some senior bureaucratic positions by political appointment rather than by examination?",
   choices=[
     "An elected president needs officials who share the administration's priorities in order to direct the executive branch",
     "Political appointees are more technically expert than career officials",
     "Political appointees are cheaper to employ",
     "Political appointees may be removed by Congress at will",
     "Political appointees are required to be neutral"], ans=0,
   why="EK 2.14.B.1 says presidential ideology, authority and influence affect how agencies carry out the administration's goals, and appointees are the mechanism. The last option contradicts what a political appointment is."),

 dict(q="What is the strongest argument against extending political appointment further down into an agency?",
   choices=[
     "Continuity and expertise would be lost every time an administration changed, and advice would be shaped to fit expectations",
     "Political appointees cannot be confirmed by the Senate",
     "The Constitution forbids the president from making any appointments",
     "Agencies would be unable to issue regulations",
     "Congress would lose the power of the purse"], ans=0,
   why="The argument runs through EK 2.12.A.2's three criteria: professionalism and specialization are built over time and neutrality is what deep politicization removes. The other options assert falsehoods about the system."),

 dict(q="Read the following excerpt.\n\n“Energy in the executive is a leading character in the definition of good government. It is essential to the protection of the community against foreign attacks; it is not less essential to the STEADY ADMINISTRATION OF THE LAWS.”\n—Alexander Hamilton, Federalist No. 70, 1788\n\nHow does this passage relate to the modern bureaucracy?",
   choices=[
     "The steady administration Hamilton calls essential is what a permanent professional bureaucracy supplies",
     "Hamilton argues that laws should be administered by the legislature",
     "Hamilton argues against a professional civil service",
     "Hamilton argues that agencies should issue their own statutes",
     "Hamilton argues that administration should change with each election"], ans=0,
   why="The CED attaches Federalist No. 70 to 2.12.A, and the connection is the phrase 'steady administration of the laws': steadiness is what EK 2.12.A.2's professionalism and neutrality produce."),

 dict(q="Read the following excerpt.\n\n“He shall take Care that the Laws be faithfully executed.”\n—U.S. Constitution, Article II, Section 3\n\nWhat does this clause imply about the bureaucracy?",
   choices=[
     "The president is responsible for execution, but executing the laws of a large country requires an organization the clause does not itself describe",
     "The president must personally carry out every federal law",
     "The clause creates the federal departments and agencies by name",
     "The clause gives agencies authority independent of the president",
     "The clause requires that all officials be hired by examination"], ans=0,
   why="The duty is the president's and the text supplies no machinery, which is why Congress creates departments and agencies by statute and why EK 2.13.A.1 describes power DELEGATED by Congress."),

 dict(q=_HIRING + " Which conclusion is best supported by the data?",
   table=_HIRING_TABLE,
   choices=[
     "The share filled by examination rose from under a tenth to nearly nine tenths across the three eras",
     "The share filled by political appointment rose across the three eras",
     "Political appointment accounted for a majority of positions in every era",
     "The two shares were roughly equal in the recent era",
     "Examination accounted for a majority of positions in every era"], ans=0,
   why="Examination runs 8, 56 and 89 percent while political appointment runs 92, 44 and 11. Appointment held a majority only in the early era, and examination only from the middle era onward."),

 dict(q=_HIRING + " Which claim from the course framework do these data most directly illustrate?",
   table=_HIRING_TABLE,
   choices=[
     "That the civil service primarily uses a merit system as opposed to political patronage",
     "That the bureaucracy implements policy by writing and enforcing regulations",
     "That iron triangles form among committees, agencies and interest groups",
     "That issue networks are temporary coalitions",
     "That Congress oversees the bureaucracy through committee hearings"], ans=0,
   why="EK 2.12.A.2 contrasts the merit system with patronage, and a table showing examination replacing political appointment is that contrast over time. The other options name activities these columns do not measure."),

 dict(q=_HIRING + " Which feature of the data supports the framework's word 'primarily' rather than a claim that patronage has disappeared?",
   table=_HIRING_TABLE,
   choices=[
     "Political appointment still accounts for eleven percent of positions in the recent era",
     "Examination accounts for eighty-nine percent of positions in the recent era",
     "The two shares sum to one hundred in every era",
     "The early era shows almost no examination",
     "The middle era shows the two shares close together"], ans=0,
   why="EK 2.12.A.2 says the civil service PRIMARILY uses a merit system, and a residual eleven percent filled by appointment is exactly what that qualification leaves room for."),

 dict(q=_ACTIONS + " Which conclusion is best supported by the data?",
   table=_ACTIONS_TABLE,
   choices=[
     "The area issuing the most regulations is not the area imposing the most fines",
     "The area issuing the most regulations also imposes the most fines",
     "Every area imposed more fines than it issued regulations",
     "Appearances before Congress were most frequent in the area issuing the most regulations",
     "The four areas took each kind of action at similar rates"], ans=0,
   why="Environment leads on regulations with 214 while financial regulation leads on fines with 2,310 and on appearances with 40. Veterans affairs imposed 12 fines against 45 regulations, so not every area imposed more fines."),

 dict(q=_ACTIONS + " Which of the framework's listed bureaucratic activities are represented by columns of this table?",
   table=_ACTIONS_TABLE,
   choices=[
     "Writing and enforcing regulations, issuing fines, and testifying before Congress",
     "Forming iron triangles and creating issue networks",
     "Writing regulations and forming iron triangles",
     "Issuing fines and creating issue networks",
     "Testifying before Congress and forming iron triangles"], ans=0,
   why="The three columns correspond to EK 2.12.A.1.i, ii and iii. The framework's fourth and fifth activities are relationships rather than countable actions, which is why no column reports them."),

 dict(q=_ACTIONS + " A student concludes from the data that the environment agency is the most aggressive regulator. Which limitation of the data most undercuts that conclusion?",
   table=_ACTIONS_TABLE,
   choices=[
     "The table counts actions without regard to their scope, and one far-reaching regulation may matter more than fifty minor ones",
     "The table omits the number of regulations issued, so no comparison is possible",
     "The table covers a single policy area, so no comparison is possible",
     "The table reports percentages that do not sum to one hundred",
     "The table gives no information about fines"], ans=0,
   why="A count of actions treats every action as equivalent, which is the standard limitation of an unweighted tally. Four areas and all three columns are plainly present."),

 dict(q="Which pairing of a bureaucratic activity with the institution it most directly involves is correct?",
   choices=[
     "Testifying before Congress, with the legislative branch; issuing fines, with a regulated party",
     "Testifying before Congress, with the courts; issuing fines, with the legislative branch",
     "Writing regulations, with the judiciary; issuing fines, with the states",
     "Forming an iron triangle, with the courts; creating an issue network, with the states",
     "Issuing fines, with the president; testifying before Congress, with interest groups"], ans=0,
   why="EK 2.12.A.1.ii and iii name the two activities, and each is directed at the obvious counterparty: a fine falls on a regulated party, and testimony is given to a congressional committee."),

 dict(q="A student writes that the bureaucracy simply carries out instructions and makes no choices of its own. Which part of the framework's account most directly contradicts that?",
   choices=[
     "Agencies write the regulations that give a statute its operative content, which requires choices the statute leaves open",
     "Agencies are elected by the voters and therefore have their own mandate",
     "Agencies may enact statutes when Congress does not",
     "Agencies may declare statutes unconstitutional",
     "Agencies may appropriate funds for their own use"], ans=0,
   why="EK 2.12.A.1.i names writing regulations as an implementation activity, and EK 2.13.A.1 makes the discretion behind it explicit. The other options describe powers no agency holds."),

 dict(q="Which question would best test whether an iron triangle is operating in a given policy area?",
   choices=[
     "Do the same committee, the same agency and the same organized interests consistently support one another's positions over time?",
     "How many regulations has the agency issued in the past year?",
     "How many staff does the agency employ?",
     "How many times has the agency been sued?",
     "How large is the agency's budget compared with other agencies?"], ans=0,
   why="EK 2.12.A.1.iv's triangle is defined by a durable alliance among three specific kinds of actor, so the test has to look for consistency among those three over time. Size and activity measure the agency alone."),

 dict(q="Which statement best summarizes what the course framework says the bureaucracy does?",
   choices=[
     "It implements policy through regulation, enforcement, testimony, and relationships with committees and organized interests, staffed mainly on merit",
     "It makes law independently of Congress and the president",
     "It resolves constitutional disputes between the branches",
     "It exists only to advise the president and has no operational role",
     "It is composed entirely of officials appointed for their party loyalty"], ans=0,
   why="This gathers EK 2.12.A.1's five activities and EK 2.12.A.2's merit system into one sentence. Each other option contradicts one of the two statements."),
]
