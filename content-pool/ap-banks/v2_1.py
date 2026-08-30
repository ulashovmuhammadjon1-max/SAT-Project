# AP U.S. GOVERNMENT AND POLITICS 2.1 Congress: The Senate and the House of Representatives -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government (25-36% of
# the exam, the largest unit).
# Learning objective 2.1.A: describe the different structures, powers, and
# functions of each house of Congress.
# Suggested skill for this topic (CED p. 58): 1.C, COMPARE political principles,
# institutions, processes, policies, and behaviors. So most items here ask for a
# comparison between the two chambers rather than a fact about one of them.
#
# Essential knowledge relied on:
#   EK 2.1.A.1 -- "Republicanism, the democratic principle that the will of the
#     people is reflected in government debates and decisions by their
#     representatives, is shown in the bicameral structure of Congress. The
#     Senate is designed to represent states equally, while the House is
#     designed to represent the people."
#   EK 2.1.A.2 -- "Different membership sizes influence the formality of debate
#     in each chamber. Debate in the House, which has 435 members, is more
#     formal than in the Senate, with 100 members."
#   EK 2.1.A.3 -- "Interactions in Congress are affected by the two-party system
#     and term-length differences. One-third of the Senate is elected every two
#     years, creating a CONTINUOUS LEGISLATIVE BODY. All House members are
#     elected every two years."
#   EK 2.1.A.4 -- a CLOSED list of seven ways the enumerated and implied powers
#     let Congress participate in the policy process:
#       i.   passing a federal budget, raising revenue by laying and collecting
#            taxes, borrowing money, and coining money
#       ii.  declaring war and providing the funds to maintain the armed forces
#       iii. determining the process for naturalization
#       iv.  regulating interstate commerce
#       v.   creating federal courts and their jurisdictions
#       vi.  enacting legislation under the authority of the necessary and
#            proper clause
#       vii. conducting oversight of the executive branch, including federal
#            agencies in the bureaucracy
#
# THE CAUSAL CHAIN THE CED ACTUALLY ASSERTS, and the reason items 6 to 9 are
# built the way they are: size CAUSES formality. EK 2.1.A.2 does not simply
# report that House debate is more formal; it says the different membership
# sizes INFLUENCE that formality. A student who has memorised "the House is more
# formal" without the mechanism cannot answer a question about why a chamber of
# 435 needs rules a chamber of 100 does not.
#
# AND THE PHRASE MOST OFTEN LOST: "continuous legislative body." Staggered
# six-year Senate terms mean the Senate never stands for election as a whole, so
# it never ceases to exist between Congresses the way the House does. That is
# EK 2.1.A.3's own phrase and items 10 to 12 rest on it.
#
# Required cases the CED attaches to 2.1.A (p. 31-32): McCulloch v. Maryland,
# Baker v. Carr.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: constitutional text is quoted verbatim.
# The membership figures 435 and 100 are the CED's own. The turnover table is a
# labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere, because
# export_units.py runs every string through mathfmt.convert, which reads both as
# arithmetic. Vote splits and term spans are written out in words.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.1", "Congress: The Senate and the House of Representatives", 2)

_CHAMBER = ("The table compares selected features of the two chambers of Congress.")
_CHAMBER_TABLE = dict(
    headers=["Feature", "House of Representatives", "Senate"],
    rows=[["Number of members", "435", "100"],
          ["Length of a term in years", "2", "6"],
          ["Share of the chamber elected every two years", "All", "One third"],
          ["Basis of representation", "Population of a state", "Equal for every state"],
          ["Chamber in which revenue bills must originate", "Yes", "No"]])

_TURNOVER = ("In a hypothetical bicameral legislature built on the U.S. model, the table "
             "reports how many seats in each chamber were filled by a newly elected member "
             "after each of three consecutive elections.")
_TURNOVER_TABLE = dict(
    headers=["Election", "New members in the larger chamber", "New members in the smaller chamber"],
    rows=[["First", "62", "9"],
          ["Second", "48", "11"],
          ["Third", "71", "8"]])

QUESTIONS = [
 dict(q="According to the course framework, the bicameral structure of Congress reflects which democratic principle?",
   choices=[
     "Republicanism, the principle that the will of the people is reflected in government by their representatives",
     "Federalism, the sharing of power between the national and state governments",
     "Separation of powers, the assignment of distinct functions to distinct branches",
     "Popular sovereignty exercised through direct citizen votes on legislation",
     "Limited government secured by a written enumeration of rights"], ans=0,
   why="EK 2.1.A.1 names republicanism and defines it as the will of the people being reflected in debates and decisions by their representatives, then says the bicameral structure shows it."),

 dict(q="According to the course framework, the Senate is designed to represent",
   choices=[
     "states equally, while the House is designed to represent the people",
     "the people, while the House is designed to represent states equally",
     "both states and the people in the same proportion as the House",
     "the executive branch's interests within the legislature",
     "the federal judiciary, which has no elected membership"], ans=0,
   why="EK 2.1.A.1 states the two designs in exactly these terms, which is the Great Compromise of EK 1.5.A.1.i carried into the structure of the institution."),

 dict(q="A bill affecting a policy of intense concern to residents of the least populous states is far more likely to receive sustained attention in the Senate than in the House. Which structural feature best explains this?",
   choices=[
     "Equal representation gives a small state the same two votes as the largest state in the Senate but a much smaller share of the House",
     "The Senate is required by the Constitution to consider bills from small states first",
     "House members represent states while senators represent individual districts",
     "Small states are permitted to appoint additional senators when their interests are affected",
     "The Senate has more members than the House and can therefore consider more bills"], ans=0,
   why="EK 2.1.A.1's two bases of representation produce exactly this asymmetry: equal state representation magnifies a small state's weight in the Senate relative to its population share. The Senate is the smaller chamber, not the larger."),

 dict(q="Which comparison between the two chambers is accurate?",
   choices=[
     "The House has 435 members and the Senate has 100, and the larger size is associated with more formal rules of debate",
     "The Senate has 435 members and the House has 100, and the larger size is associated with less formal debate",
     "Both chambers have the same number of members, and their rules differ for historical reasons only",
     "The House has fewer members than the Senate, which is why its debate is more formal",
     "Membership size has no relationship to the formality of debate in either chamber"], ans=0,
   why="EK 2.1.A.2 gives both figures and asserts the relationship: different membership sizes influence the formality of debate, and debate in the House is more formal than in the Senate."),

 dict(q="Why does a chamber of 435 members need more elaborate rules governing debate than a chamber of 100?",
   choices=[
     "With four times as many members seeking recognition, unstructured debate would consume more time than the chamber has",
     "The Constitution requires the House to adopt rules that the Senate is forbidden to adopt",
     "House members are less experienced legislators than senators",
     "The House considers only bills that the Senate has already passed",
     "The House meets for fewer days each year than the Senate does"], ans=0,
   why="EK 2.1.A.2 makes size the cause of formality, and the mechanism is the scarcity of floor time relative to the number of members who want it. Nothing in the Constitution forbids the Senate to adopt rules; it has chosen looser ones."),

 dict(q="A senator speaks on the floor for several hours to delay a vote, a tactic that would be impossible in the House under its rules for debate. This contrast most directly illustrates",
   choices=[
     "the effect of chamber size on the formality of debate, since the smaller chamber can tolerate unlimited speech",
     "the constitutional requirement that revenue bills originate in the House",
     "the two-party system's effect on committee leadership",
     "the difference in the length of a term between the two chambers",
     "the Senate's role in representing the people rather than the states"], ans=0,
   why="EK 2.1.A.2 ties formality to size, and a chamber of 100 can afford floor time that a chamber of 435 cannot. Term length and revenue origination are real differences that do not explain this one."),

 dict(q="Which statement about the composition of debate in the two chambers is best supported by the course framework?",
   choices=[
     "Formality of debate differs between the chambers, and the framework attributes the difference to their different membership sizes",
     "Formality of debate is identical in the two chambers because both follow the same constitutional rules",
     "Debate in the Senate is more formal than in the House because senators serve longer terms",
     "Debate in the House is less formal than in the Senate because the House is closer to the people",
     "The framework makes no claim about debate in either chamber"], ans=0,
   why="EK 2.1.A.2 states both the difference and its cause. The third and fourth options each reverse the direction of the difference the framework asserts."),

 dict(q="According to the course framework, what makes the Senate a continuous legislative body?",
   choices=[
     "Only one third of its seats are filled at each election, so the chamber never stands for election as a whole",
     "It meets year round while the House adjourns between sessions",
     "Its members may serve an unlimited number of terms",
     "Its presiding officer is the vice president, who is not elected by the chamber",
     "It never adjourns while the president remains in office"], ans=0,
   why="EK 2.1.A.3 says one third of the Senate is elected every two years, 'creating a continuous legislative body,' whereas all House members are elected every two years. Continuity is about the turnover of membership, not about the calendar."),

 dict(q="All House members stand for election every two years, while senators serve six-year terms. What is the most important consequence of that difference for how members behave?",
   choices=[
     "A representative is never far from an election, which tends to keep short-term constituent concerns closer at hand than for a senator recently elected",
     "A senator has no electoral incentive of any kind, since six years is beyond the horizon of any voter",
     "A representative may ignore constituents entirely, since the term is too short to be held accountable",
     "A senator must run in every state, which makes national opinion the only relevant consideration",
     "Term length has no effect on legislative behavior in either chamber"], ans=0,
   why="EK 2.1.A.3 names term-length differences as one of the two things affecting interactions in Congress, and the mechanism is the proximity of the next election. The second and third options overstate the difference into an absolute."),

 dict(q="Besides term-length differences, which factor does the course framework identify as affecting interactions in Congress?",
   choices=[
     "The two-party system",
     "The Electoral College",
     "The federal judiciary's power of judicial review",
     "The size of the federal budget deficit",
     "The number of states in the union"], ans=0,
   why="EK 2.1.A.3 names exactly two factors, the two-party system and term-length differences. The others are real features of American government that this statement does not name."),

 dict(q="Read the following excerpt.\n\n“All Bills for raising Revenue shall originate in the House of Representatives; but the Senate may propose or concur with Amendments as on other Bills.”\n—U.S. Constitution, Article I, Section 7\n\nWhich statement about this provision is accurate?",
   choices=[
     "Revenue bills must begin in the House, but the Senate may amend them once they arrive",
     "Revenue bills must begin in the Senate and may not be amended by the House",
     "Revenue bills may begin in either chamber, and the other chamber may not amend them",
     "The Senate is barred from any role in legislation raising revenue",
     "The provision applies to all bills, not only to those raising revenue"], ans=0,
   why="The clause has two halves, and the second half preserves the Senate's amending power, which is why the House's advantage is one of sequence rather than of exclusion. EK 2.2.A.3.i records the origination rule as a House-specific procedure."),

 dict(q="Which of the following is one of the seven ways the course framework says the enumerated and implied powers allow Congress to participate in the public policy process?",
   choices=[
     "Conducting oversight of the executive branch, including federal agencies in the bureaucracy",
     "Appointing the heads of federal agencies without executive involvement",
     "Issuing executive orders that carry the force of law",
     "Negotiating and signing treaties with foreign governments",
     "Nominating justices to the Supreme Court"], ans=0,
   why="EK 2.1.A.4.vii names oversight of the executive branch including federal agencies. Appointment, executive orders, treaty negotiation and nomination are executive functions; Congress's role in the first and fourth is confirmation and ratification."),

 dict(q="Congress passes a statute establishing a new federal district court and specifying the categories of cases it may hear. Which of the framework's seven congressional powers does this exercise?",
   choices=[
     "Creating federal courts and their jurisdictions",
     "Enacting legislation under the necessary and proper clause alone",
     "Conducting oversight of the executive branch",
     "Determining the process for naturalization",
     "Regulating interstate commerce"], ans=0,
   why="EK 2.1.A.4.v names creating federal courts AND their jurisdictions, which is exactly what the statute does. The necessary and proper clause is a separate item on the same list and is not the specific power at work here."),

 dict(q="A congressional committee subpoenas records from a federal agency and holds hearings on whether the agency has implemented a statute as Congress intended. Which congressional power is being exercised?",
   choices=[
     "Oversight of the executive branch, including federal agencies in the bureaucracy",
     "The power to declare war",
     "The power to determine the process for naturalization",
     "The power to coin money",
     "The power to create federal courts"], ans=0,
   why="EK 2.1.A.4.vii names oversight of the executive branch including agencies in the bureaucracy, and hearings into how a statute has been implemented are its ordinary form."),

 dict(q="Which pair of powers appears together in EK 2.1.A.4's first item on the ways Congress participates in the policy process?",
   choices=[
     "Passing a federal budget and raising revenue by laying and collecting taxes",
     "Declaring war and confirming the president's nominees",
     "Regulating interstate commerce and ratifying treaties",
     "Coining money and appointing federal judges",
     "Conducting oversight and issuing pardons"], ans=0,
   why="EK 2.1.A.4.i groups passing a federal budget, raising revenue by taxation, borrowing money and coining money. Confirmation, ratification, appointment and pardons are not on the list at all or belong to the executive."),

 dict(q="In McCulloch v. Maryland (1819), the Supreme Court upheld Congress's power to charter a national bank, establishing the supremacy of the U.S. Constitution and federal laws over state laws. Which item on the framework's list of congressional powers does the decision most directly support?",
   choices=[
     "Enacting legislation under the authority of the necessary and proper clause",
     "Determining the process for naturalization",
     "Creating federal courts and their jurisdictions",
     "Declaring war and funding the armed forces",
     "Conducting oversight of the executive branch"], ans=0,
   why="No clause enumerates a power to charter a bank, so upholding it rests on the necessary and proper clause, which EK 2.1.A.4.vi names as one of the seven ways Congress participates in the policy process."),

 dict(q="In Baker v. Carr (1962), the Supreme Court held that redistricting did not raise political questions, allowing federal courts to hear cases challenging redistricting plans that may violate the Equal Protection Clause. Which chamber does the decision most directly affect, and why?",
   choices=[
     "The House, because its seats are apportioned among districts drawn within each state",
     "The Senate, because its seats are apportioned among districts drawn within each state",
     "Both chambers equally, because both are elected from districts",
     "Neither chamber, because the case concerned state legislatures only",
     "The Senate, because each state's two senators must come from different districts"], ans=0,
   why="EK 2.1.A.1 makes the House the chamber representing the people, and it is elected from districts drawn within states; senators are elected statewide, so no districting question arises for them."),

 dict(q="A student writes that the Senate is the more democratic chamber because each senator represents an entire state. What is the strongest objection?",
   choices=[
     "Equal state representation means a senator from the least populous state has the same vote as one representing tens of millions, so votes are far from equally weighted",
     "Senators are appointed rather than elected, so they are accountable to no one",
     "The Senate has more members than the House, so each senator represents fewer people",
     "The Senate may not vote on legislation, only debate it",
     "Senators serve two-year terms, which is too short for accountability"], ans=0,
   why="EK 2.1.A.1's design has the Senate representing states equally rather than people equally, which is precisely what makes per-voter weight unequal. Senators have been popularly elected since the Seventeenth Amendment and serve six-year terms."),

 dict(q="A commentator argues that the two chambers were designed to check each other rather than to duplicate each other. Which pair of features best supports that argument?",
   choices=[
     "Different bases of representation and different term lengths, so the two chambers respond to different constituencies on different timetables",
     "Identical membership sizes and identical rules of debate",
     "A shared presiding officer and a shared committee system",
     "Equal representation in both chambers and simultaneous election of all members",
     "The same term length in both chambers and the same basis of representation"], ans=0,
   why="EK 2.1.A.1 supplies the different bases of representation and EK 2.1.A.3 the different term lengths, and together they mean a majority in one chamber need not be a majority in the other. The other options describe a duplicate chamber rather than a checking one."),

 dict(q="Which question would best test the framework's claim that membership size influences the formality of debate?",
   choices=[
     "In legislatures of different sizes, do larger chambers adopt more restrictive rules governing floor time?",
     "In legislatures of different sizes, do members of larger chambers serve longer terms?",
     "In legislatures of different sizes, do larger chambers pass more legislation each year?",
     "In legislatures of different sizes, are members of larger chambers more likely to be re-elected?",
     "In legislatures of different sizes, do larger chambers meet in larger buildings?"], ans=0,
   why="EK 2.1.A.2's claim is a relationship between size and the formality of debate, so a test has to compare size against rules of debate across cases. Legislative output, re-election rates and term length measure other things."),

 dict(q=_CHAMBER + " Which conclusion is best supported by the table?",
   table=_CHAMBER_TABLE,
   choices=[
     "The larger chamber has the shorter term and replaces its entire membership at every election",
     "The larger chamber has the longer term and replaces one third of its membership at every election",
     "Both chambers replace the same share of their membership at every election",
     "Both chambers represent states equally",
     "Revenue bills may originate in either chamber"], ans=0,
   why="The House row shows 435 members, a two-year term and all seats filled at each election; the Senate shows 100, six years and one third. The last two rows show different bases of representation and House origination for revenue bills."),

 dict(q=_CHAMBER + " Which row of the table best explains why a majority in one chamber may not correspond to a majority in the other?",
   table=_CHAMBER_TABLE,
   choices=[
     "Basis of representation, since one chamber is apportioned by population and the other equally by state",
     "Number of members, since one chamber is larger than the other",
     "Length of a term in years, since one chamber's members serve longer",
     "Share of the chamber elected every two years, since one chamber turns over entirely",
     "Chamber in which revenue bills must originate, since only one chamber may begin them"], ans=0,
   why="A different basis of apportionment is what allows the same electorate to produce different majorities, which is EK 2.1.A.1's design. Size, term length and turnover shape behavior but do not by themselves change which coalition holds a majority."),

 dict(q=_CHAMBER + " A student concludes from the table that the House is the more powerful chamber because it is larger and originates revenue bills. Which limitation of the data most undercuts that conclusion?",
   table=_CHAMBER_TABLE,
   choices=[
     "The table lists no Senate-specific power, such as confirming appointments or ratifying treaties, so it cannot support a comparison of overall power",
     "The table omits the Senate entirely, so no comparison is possible",
     "The table reports opinions about the chambers rather than their features",
     "The table gives no information about the number of members in either chamber",
     "The table shows that the two chambers are identical in every respect"], ans=0,
   why="A comparison of power drawn from a table that lists one chamber's exclusive power and none of the other's is a conclusion produced by the selection of rows. The Senate column, the membership row and four differing rows are all plainly present."),

 dict(q=_TURNOVER + " Which conclusion is best supported by the data?",
   table=_TURNOVER_TABLE,
   choices=[
     "In every election the larger chamber seated at least four times as many new members as the smaller chamber",
     "The smaller chamber seated more new members than the larger chamber in at least one election",
     "New membership in the larger chamber declined at every election",
     "The two chambers seated the same number of new members in the second election",
     "Neither chamber seated any new members in the third election"], ans=0,
   why="The ratios are 62 to 9, 48 to 11 and 71 to 8, or roughly seven, four and nine to one. New membership in the larger chamber falls and then rises, and the third election seats the most new members of any."),

 dict(q=_TURNOVER + " Which feature of the U.S. Congress do these data most directly illustrate?",
   table=_TURNOVER_TABLE,
   choices=[
     "That staggering the smaller chamber's elections makes it a continuous body while the larger chamber is entirely renewed",
     "That the smaller chamber represents the people and the larger represents the states",
     "That the larger chamber has less formal rules of debate than the smaller",
     "That revenue bills must originate in the smaller chamber",
     "That members of the smaller chamber serve shorter terms"], ans=0,
   why="EK 2.1.A.3's continuous legislative body is exactly this pattern: a chamber that replaces only a fraction of its seats each time, against one that is renewed. Each other option reverses a fact stated in EK 2.1.A.1, EK 2.1.A.2 or EK 2.2.A.3.i."),

 dict(q=_TURNOVER + " A student concludes that members of the smaller chamber are more popular with voters than members of the larger chamber. Which limitation of the data most undercuts that conclusion?",
   table=_TURNOVER_TABLE,
   choices=[
     "Only a fraction of the smaller chamber's seats are contested at each election, so a low count of new members does not indicate a high rate of re-election",
     "The table omits the larger chamber, so no comparison is possible",
     "The table reports percentages rather than counts of members",
     "The table covers a single election, so no comparison over time is possible",
     "The table gives no information about how many new members were seated"], ans=0,
   why="A raw count of new members confounds turnover with the number of seats at stake, and in a staggered chamber most seats are not on the ballot at all. The table plainly reports counts for both chambers across three elections."),

 dict(q="Which statement best explains why the framework treats the two chambers' differences as a feature of the design rather than as an inconvenience?",
   choices=[
     "The differences force a bill to satisfy two differently constituted majorities before it can become law",
     "The differences allow either chamber to enact legislation without the other",
     "The differences ensure that the two chambers will always reach the same conclusion",
     "The differences give the president a vote in each chamber",
     "The differences make the legislative process faster than a single chamber would be"], ans=0,
   why="EK 2.1.A.1 grounds bicameralism in republicanism and the Great Compromise, and the point of two differently based chambers is that agreement between them is a broader test than agreement within one. Neither chamber can legislate alone."),

 dict(q="A representative and a senator from the same state take different positions on a bill affecting a single county. Which structural difference best explains the divergence?",
   choices=[
     "The representative answers to one district within the state while the senator answers to the state as a whole",
     "The representative serves a six-year term while the senator serves two years",
     "The senator was appointed by the governor and the representative was elected",
     "The representative may vote on revenue bills and the senator may not",
     "The senator represents the people and the representative represents the state"], ans=0,
   why="EK 2.1.A.1's bases of representation differ, so a county that dominates one House district is a small share of a senator's statewide constituency. The fifth option reverses the framework's own assignment of the two designs."),

 dict(q="Which of the following is NOT among the seven ways EK 2.1.A.4 says the enumerated and implied powers let Congress participate in the public policy process?",
   choices=[
     "Granting reprieves and pardons for offenses against the United States",
     "Declaring war and providing the funds necessary to maintain the armed forces",
     "Determining the process for naturalization",
     "Regulating interstate commerce",
     "Passing a federal budget and borrowing money"], ans=0,
   why="Reprieves and pardons are an executive power under Article II Section 2 and appear nowhere on EK 2.1.A.4's list. The other four options each restate one of the seven items."),

 dict(q="An essay argues that the House and the Senate should be understood as two different institutions rather than as two halves of one. Which evidence from the course framework most directly supports that argument?",
   choices=[
     "They rest on different bases of representation, differ in size by more than four to one, follow different rules of debate, and renew their membership on different schedules",
     "They meet in the same building and share a committee staff",
     "They are elected by the same voters on the same day for the same term",
     "They have identical rules of debate and identical membership sizes",
     "They both consider every bill in the same order and under the same procedures"], ans=0,
   why="EK 2.1.A.1, EK 2.1.A.2 and EK 2.1.A.3 supply four separate differences, and each is stated by the framework itself. The other options assert similarities the framework denies."),
]
