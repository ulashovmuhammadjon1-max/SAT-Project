# AP U.S. GOVERNMENT AND POLITICS 2.15 Policy and the Branches of Government -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# TWO learning objectives, and the unit's closing topic:
#   LO 2.15.A -- explain the EXTENT TO WHICH governmental branches can hold the
#     bureaucracy accountable GIVEN THE COMPETING INTERESTS of Congress, the
#     president, and the federal courts.
#   LO 2.15.B -- explain how the distribution of powers among the three branches
#     impacts policymaking.
# Suggested skill for this topic (CED p. 75): 3.D, EXPLAIN WHAT THE DATA IMPLIES
# OR ILLUSTRATES about political principles, institutions, processes, policies
# and behaviors.
#
# Essential knowledge relied on:
#   EK 2.15.A.1 -- "FORMAL AND INFORMAL powers of Congress, the president, and
#     the courts over the bureaucracy are used to maintain its accountability."
#   EK 2.15.B.1 -- "The allocation of powers among the THREE BRANCHES of
#     government creates MULTIPLE ACCESS POINTS for stakeholders and
#     institutions to influence public policy."
#   EK 2.15.B.2 -- "National policymaking is CONSTRAINED by the sharing of
#     powers BETWEEN THE THREE BRANCHES."
#
# THIS TOPIC OVERLAPS TWO OTHERS AND THE BOUNDARY IS DELIBERATE. Read this
# before adding items:
#   * EK 1.6.B.1 says the access-point sentence about SEPARATION OF POWERS AND
#     CHECKS AND BALANCES. v1_6 owns that version.
#   * EK 1.9.A.1 and EK 1.9.A.2 say the access-point and constraint sentences
#     about FEDERALISM -- levels of government. v1_9 owns those.
#   * EK 2.15.B.1 and EK 2.15.B.2 say them about THE THREE BRANCHES, in a unit
#     about the interaction of those branches and immediately after four topics
#     on the bureaucracy.
# So every access-point and constraint item in THIS module is set in the
# policymaking context Unit 2 has just built: agencies, oversight, appointments,
# rulemaking, litigation. No item here uses a state or local government as its
# additional venue, which is v1_9's territory, and no item is a bare restatement
# of the sentence, which is v1_6's. Item 12 makes the three-way distinction
# itself the question.
#
# LO 2.15.A's PHRASE "THE EXTENT TO WHICH" IS NOT DECORATION. The objective does
# not ask whether the branches CAN hold the bureaucracy accountable; it asks HOW
# FAR they can, GIVEN COMPETING INTERESTS. The competition is the point: three
# principals pulling an agency in three directions do not add up to tighter
# control, and may add up to less. Items 6 to 10 and 27 to 30 turn on that.
#
# Documents the CED attaches to 2.15.A (p. 26-27): Federalist No. 51,
# Federalist No. 70.
# Required cases the CED attaches to 2.15.B (p. 31): Marbury v. Madison.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: Federalist No. 51 is quoted verbatim.
# The CED's illustrative example for this topic, the legislative veto, is marked
# NOT REQUIRED and is not used. All three tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. The
# verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.15", "Policy and the Branches of Government", 2)

_TOOLS = ("The table lists six instruments used to hold the federal bureaucracy accountable, "
          "with the branch that wields each and whether the framework classifies it as a "
          "formal or an informal power.")
_TOOLS_TABLE = dict(
    headers=["Instrument", "Branch", "Formal or informal"],
    rows=[["Appropriating or withholding funds", "Legislative", "Formal"],
          ["Committee hearings and investigation", "Legislative", "Formal"],
          ["Appointment of agency leadership", "Executive", "Formal"],
          ["Public pressure on an agency's leadership", "Executive", "Informal"],
          ["Holding an agency action unlawful", "Judicial", "Formal"],
          ["Bargaining with committee leaders over an agency's budget", "Executive", "Informal"]])

_VENUES = ("In a hypothetical study, organizations seeking to change one federal regulation "
           "were asked which venues they used and whether the venue produced any change.")
_VENUES_TABLE = dict(
    headers=["Venue", "Organizations using it (%)", "Produced some change (%)"],
    rows=[["Comments filed with the agency", "84", "37"],
          ["Congressional committee staff", "61", "22"],
          ["The agency's political leadership", "52", "29"],
          ["Litigation in federal court", "38", "18"]])

_DELAY = ("In a hypothetical study, the table reports how long it took a policy to take effect, "
          "by how many of the three branches actively contested it.")
_DELAY_TABLE = dict(
    headers=["Branches actively contesting the policy", "Number of policies", "Median months to take effect"],
    rows=[["None", "24", "6"],
          ["One", "31", "14"],
          ["Two", "18", "29"],
          ["Three", "5", "47"]])

QUESTIONS = [
 dict(q="According to the course framework, what is used to maintain the bureaucracy's accountability?",
   choices=[
     "Formal and informal powers of Congress, the president, and the courts",
     "Formal powers of Congress alone",
     "The internal rules each agency adopts for itself",
     "Elections in which agency heads stand before the voters",
     "The merit system used to hire civil servants"], ans=0,
   why="EK 2.15.A.1 names all three branches and BOTH kinds of power. Restricting accountability to one branch or to formal powers alone drops most of what the statement says."),

 dict(q="Which of the following is a FORMAL power used to hold the bureaucracy accountable?",
   choices=[
     "Congress appropriating or withholding an agency's funds",
     "A president using public statements to pressure an agency's leadership",
     "A committee chair bargaining privately with an agency head",
     "An interest group publicizing an agency's failures",
     "A former official criticizing an agency in the press"], ans=0,
   why="EK 2.14.A.1.iii's power of the purse is an authority the Constitution and statute confer, which is what makes it formal. The other four operate through pressure rather than through any granted authority."),

 dict(q="Which of the following is an INFORMAL power used to hold the bureaucracy accountable?",
   choices=[
     "A president publicly pressing an agency to change a policy he cannot lawfully order it to change",
     "The Senate refusing to confirm an agency nominee",
     "A court holding an agency rule unlawful",
     "Congress reducing an agency's appropriation",
     "Congress enacting a statute narrowing an agency's authority"], ans=0,
   why="EK 2.4.A.2.iii classifies bargaining and persuasion as informal powers, and public pressure works without any authority to command. The other four are exercises of a granted power."),

 dict(q="Why does the framework include INFORMAL powers in its account of accountability at all?",
   choices=[
     "Much of what moves an agency happens through pressure and bargaining that no formal instrument records",
     "Informal powers are the only ones the Constitution grants",
     "Formal powers may not be used against agencies",
     "Informal powers bind agencies more strictly than statutes do",
     "The framework treats formal and informal powers as identical"], ans=0,
   why="EK 2.15.A.1 names both kinds because an account limited to statutes and court orders would miss most of the interaction. Informal powers are less binding, not more, which is why the fourth option fails."),

 dict(q="Which pairing of a branch with an instrument it uses over the bureaucracy is correct?",
   choices=[
     "The courts, with holding an agency action unlawful; Congress, with the power of the purse",
     "The courts, with the power of the purse; Congress, with holding an agency action unlawful",
     "The president, with committee hearings; Congress, with appointment of agency heads",
     "Congress, with issuing regulations; the courts, with appointing agency heads",
     "The president, with holding an agency action unlawful; the courts, with appointment"], ans=0,
   why="Judicial review of agency action is the courts' instrument and appropriation is Congress's; appointment belongs to the president and hearings to Congress. Each other option swaps at least one pair."),

 dict(q="LO 2.15.A asks about accountability GIVEN THE COMPETING INTERESTS of Congress, the president and the courts. What does that qualification add?",
   choices=[
     "The three branches do not want the same thing from an agency, so their combined pressure is not simply the sum of three controls",
     "Only one branch may hold an agency accountable at a time",
     "The three branches always agree about what an agency should do",
     "Competing interests make accountability impossible",
     "The qualification concerns disputes among agencies rather than among branches"], ans=0,
   why="The learning objective's own words are 'given the competing interests,' which is why the topic asks about the EXTENT of accountability rather than merely listing instruments."),

 dict(q="An agency receives a statutory mandate from Congress, a contrary priority from the administration, and a court order narrowing its options. What is the most accurate description of its position?",
   choices=[
     "It is accountable to three principals whose demands do not align, which limits how fully it can satisfy any of them",
     "It may choose which of the three to obey and disregard the others",
     "It is accountable to none of them, since the demands conflict",
     "It must obey whichever demand was made most recently",
     "It must refer the conflict to the Supreme Court before acting"], ans=0,
   why="EK 2.15.A.1 puts all three branches' powers on the same agency, and LO 2.15.A's competing interests are exactly this situation. None of the other options describes a rule that exists."),

 dict(q="Which conclusion about accountability follows most directly from the competition among the three branches?",
   choices=[
     "An agency with conflicting instructions has room to choose among them, which can leave it less controlled rather than more",
     "Three overlapping controls guarantee tighter control than one would",
     "Agencies faced with conflict always default to the president's preference",
     "Conflict among the branches has no effect on agency behavior",
     "Conflict among the branches transfers the agency to judicial supervision"], ans=0,
   why="This is the answer LO 2.15.A's phrase 'the extent to which' invites: overlapping and inconsistent controls create discretion rather than eliminating it, which is why the objective asks how far accountability reaches."),

 dict(q="Read the following excerpt.\n\n“Ambition must be made to counteract ambition. The interest of the man must be connected with the constitutional rights of the place.”\n—James Madison, Federalist No. 51, 1788\n\nWhat does Madison's design predict about three branches supervising one bureaucracy?",
   choices=[
     "Each branch will press its own institutional claim on the agency, so supervision will be contested rather than coordinated",
     "The three branches will divide the supervision neatly among themselves",
     "The branch with the strongest claim will supervise alone",
     "Supervision will cease once the branches disagree",
     "The agency will be supervised by whichever branch created it"], ans=0,
   why="Madison's mechanism is each institution defending its own prerogative, which produces competition rather than coordination -- and LO 2.15.A's phrase 'competing interests' is that prediction restated."),

 dict(q="Which observation would best support a claim that the branches DO hold the bureaucracy effectively accountable despite their competing interests?",
   choices=[
     "Agencies that departed from statutory requirements were reliably corrected, whichever branch first identified the departure",
     "Congress held more oversight hearings than in previous years",
     "The president appointed heads for every vacant agency position",
     "Federal courts received more challenges to agency rules than before",
     "Agencies published more regulations than in previous years"], ans=0,
   why="Effectiveness is measured by corrected departures rather than by the volume of oversight activity, and the phrase 'whichever branch' addresses LO 2.15.A's competing interests directly."),

 dict(q="According to the course framework, the allocation of powers among the three branches creates",
   choices=[
     "multiple access points for stakeholders and institutions to influence public policy",
     "a single point at which policy is decided",
     "an obligation on each branch to defer to the others",
     "a prohibition on outside participation in policymaking",
     "identical policy outcomes regardless of which branch acts"], ans=0,
   why="EK 2.15.B.1 states this in exactly these words. Note that EK 1.6.B.1 says the same of separation of powers and EK 1.9.A.1 of federalism; this statement is about the three branches."),

 dict(q="The course framework makes an access-point claim three times: about separation of powers, about federalism, and about the three branches. What distinguishes the three?",
   choices=[
     "They identify different sources of the additional venues: the branches' distinct functions, the two levels of government, and the branches' shared role in policymaking",
     "They are three ways of saying the same thing about federalism",
     "Only the federalism version concerns access points; the other two concern accountability",
     "They differ only in which unit of the course they appear in",
     "The framework makes the claim once, not three times"], ans=0,
   why="EK 1.6.B.1, EK 1.9.A.1 and EK 2.15.B.1 all describe additional venues, but the multiplier differs -- branches, levels, and the branches' joint role in making policy. Knowing which sentence a question is asking about is the skill."),

 dict(q="According to the course framework, national policymaking is constrained by",
   choices=[
     "the sharing of powers between the three branches",
     "the requirement that all three branches approve every regulation",
     "the inability of any branch to act without a constitutional amendment",
     "the absence of any national policymaking authority",
     "the requirement that policy be approved by a majority of states"], ans=0,
   why="EK 2.15.B.2 states this in exactly these words. The constraint arises from shared powers rather than from any rule requiring unanimous approval, which is what the second option invents."),

 dict(q="A president's policy priority requires a statute Congress will not pass, so the administration pursues it by regulation, and a court then holds the regulation exceeds the agency's authority. Which claim does this best illustrate?",
   choices=[
     "That national policymaking is constrained by the sharing of powers between the three branches",
     "That the allocation of powers creates multiple access points for stakeholders",
     "That agencies exercise discretion delegated by Congress without limit",
     "That the courts make national policy",
     "That the president may enact a statute when Congress declines to"], ans=0,
   why="EK 2.15.B.2's constraint is exactly this sequence: an objective blocked in one branch, attempted in another, and stopped by a third. The access-point claim is about opportunity, which is the mirror image."),

 dict(q="EK 2.15.B.1 and EK 2.15.B.2 describe the same structural fact. What is the difference between them?",
   choices=[
     "One describes the opportunity the structure creates for outside actors; the other describes the constraint it imposes on national action",
     "One concerns the branches and the other concerns the states",
     "One concerns formal powers and the other informal powers",
     "One applies to Congress and the other to the courts",
     "There is no difference; the two statements are identical"], ans=0,
   why="Divided authority multiplies the places a claim can be pressed and multiplies the agreements required to act. EK 1.9.A.1 and EK 1.9.A.2 make the same pair of claims about federalism."),

 dict(q="In Marbury v. Madison (1803), the Supreme Court established the principle of judicial review, empowering the Court to declare an act of the legislative or executive branch unconstitutional. How does the case bear on the distribution of powers among the branches?",
   choices=[
     "It added the courts as a venue in which a policy adopted elsewhere can be contested and stopped",
     "It gave the courts authority to enact policy of their own",
     "It removed the courts from the policymaking process",
     "It required Congress to obtain judicial approval before legislating",
     "It transferred the executive power to the judiciary"], ans=0,
   why="The CED attaches Marbury to 2.15.B, and the connection is structural: judicial review makes the courts a place where policy made by the other branches is tested, which is both an access point and a constraint."),

 dict(q="Which of the following best explains why a policy that all three branches support moves quickly while one that any branch opposes moves slowly?",
   choices=[
     "Shared powers mean action requires agreement, so each additional objecting branch adds a place where the policy can be delayed or stopped",
     "The Constitution sets a time limit for policies with unanimous support",
     "Opposition by any branch makes a policy unconstitutional",
     "Policies opposed by a branch are automatically referred to the voters",
     "Agencies may not implement a policy any branch has questioned"], ans=0,
   why="EK 2.15.B.2 locates the constraint in the sharing of powers, and the mechanism is the number of agreements required. The other options describe rules that do not exist."),

 dict(q="Which of the following is the strongest argument that the constraint EK 2.15.B.2 describes is a feature rather than a defect?",
   choices=[
     "A policy that has had to satisfy three separately constituted institutions rests on broader agreement and is harder to reverse abruptly",
     "Slow policymaking is always better than fast policymaking",
     "The framers intended that no national policy should ever be adopted",
     "Constraints prevent any branch from acting unconstitutionally",
     "Delay reduces the cost of every policy"], ans=0,
   why="The design's defence is the breadth of the coalition it forces, which is Federalist No. 51's argument applied to policymaking. The other options overstate the claim into something indefensible."),

 dict(q="Which of the following is the strongest argument that the constraint is a defect rather than a feature?",
   choices=[
     "Problems that require a timely national response may go unaddressed because agreement among three institutions is difficult to assemble",
     "The Constitution does not mention policymaking",
     "The branches are prohibited from cooperating",
     "Constraints on policymaking are unconstitutional",
     "Shared powers make every policy identical"], ans=0,
   why="The serious objection is the cost of delay when a response is needed, which follows directly from EK 2.15.B.2's constraint. The other options assert falsehoods rather than arguments."),

 dict(q=_TOOLS + " Which conclusion is best supported by the table?",
   table=_TOOLS_TABLE,
   choices=[
     "All three branches appear, and the executive branch is the only one with both a formal and an informal instrument listed",
     "Only formal instruments appear in the table",
     "The judicial branch has the most instruments listed",
     "The legislative branch has no formal instrument listed",
     "Every instrument listed is informal"], ans=0,
   why="The branch column shows legislative, executive and judicial, and the two informal rows are both executive. The legislature has two formal rows and the judiciary one."),

 dict(q=_TOOLS + " Which claim from the course framework does the table most directly illustrate?",
   table=_TOOLS_TABLE,
   choices=[
     "That formal and informal powers of Congress, the president, and the courts over the bureaucracy are used to maintain accountability",
     "That agencies exercise discretion delegated by Congress",
     "That the civil service uses a merit system",
     "That iron triangles form in specific policy areas",
     "That compliance monitoring can challenge policy implementation"], ans=0,
   why="EK 2.15.A.1 names all three branches and both kinds of power, and the table's two columns are exactly those two dimensions. The other options name statements the table does not report."),

 dict(q=_TOOLS + " A student concludes from the table that the judiciary is the weakest of the three in supervising agencies. Which limitation of the data most undercuts that conclusion?",
   table=_TOOLS_TABLE,
   choices=[
     "The table lists selected instruments rather than all of them, and one instrument may matter far more than several others",
     "The table omits the judicial branch entirely, so no comparison is possible",
     "The table reports how often each instrument is used",
     "The table covers a single branch, so no comparison is possible",
     "The table gives no information about whether an instrument is formal or informal"], ans=0,
   why="Counting rows in a curated list measures the list, and a single holding that an agency action is unlawful can reach further than several hearings. The judicial row and the formal column are plainly present."),

 dict(q=_VENUES + " Which conclusion is best supported by the data?",
   table=_VENUES_TABLE,
   choices=[
     "The most used venue was also the most likely to produce change, but no venue produced change in even half the attempts",
     "The least used venue was the most likely to produce change",
     "Every venue produced change in a majority of attempts",
     "Litigation was both the most used and the most effective venue",
     "The four venues were used by similar shares of organizations"], ans=0,
   why="Agency comments lead on both measures at 84 and 37 percent, and the highest success figure is 37. Litigation is the least used at 38 percent and the least effective at 18."),

 dict(q=_VENUES + " Which claim from the course framework do these data most directly illustrate?",
   table=_VENUES_TABLE,
   choices=[
     "That the allocation of powers among the three branches creates multiple access points for influencing policy",
     "That national policymaking is constrained by the sharing of powers",
     "That the civil service uses a merit system",
     "That compliance monitoring ensures funds are used properly",
     "That agencies form iron triangles with committees and interest groups"], ans=0,
   why="Four venues spanning the agency, a congressional committee, the administration and a federal court is EK 2.15.B.1's multiple access points measured. Note these are all NATIONAL institutions, which is what makes it the branches version rather than EK 1.9.A.1's federalism version."),

 dict(q=_VENUES + " What do the data imply about the value of using more than one venue?",
   table=_VENUES_TABLE,
   choices=[
     "Since no single venue succeeds more than about a third of the time, an organization able to use several has a better chance than one able to use only one",
     "Since the most used venue is the most effective, using others adds nothing",
     "Since litigation is least effective, no organization should use the courts",
     "Since the shares do not sum to one hundred, the table cannot be interpreted",
     "Since every venue succeeds more than half the time, one venue is enough"], ans=0,
   why="Low per-venue success rates are exactly what make multiple access points valuable, which is EK 2.15.B.1's point stated as an implication. The columns overlap because organizations used more than one venue, so they need not sum to one hundred."),

 dict(q=_DELAY + " Which conclusion is best supported by the data?",
   table=_DELAY_TABLE,
   choices=[
     "Time to take effect rose with each additional contesting branch, from six months to forty-seven",
     "Time to take effect fell as more branches contested a policy",
     "Most policies in the study were contested by all three branches",
     "Time to take effect was similar regardless of how many branches contested a policy",
     "No policy took more than two years to take effect"], ans=0,
   why="The median runs 6, 14, 29 and 47 months as the number of contesting branches rises from none to three. Only five of seventy-eight policies were contested by all three, and forty-seven months is nearly four years."),

 dict(q=_DELAY + " Which claim from the course framework do these data most directly illustrate?",
   table=_DELAY_TABLE,
   choices=[
     "That national policymaking is constrained by the sharing of powers between the three branches",
     "That the allocation of powers creates multiple access points for stakeholders",
     "That the bureaucracy implements policy by writing regulations",
     "That judicial appointments are the president's longest lasting influence",
     "That the merit system prioritizes professionalism and neutrality"], ans=0,
   why="EK 2.15.B.2's constraint is that shared powers slow national action, and a median rising with each contesting branch is that constraint measured. The access-point claim describes the same structure from the outside actor's side."),

 dict(q=_DELAY + " What do the data imply about the relationship between EK 2.15.B.1 and EK 2.15.B.2?",
   table=_DELAY_TABLE,
   choices=[
     "The same additional venues that give outside actors somewhere to press a claim are the places where a policy is delayed",
     "The two statements describe unrelated features of the system",
     "Access points speed policymaking while shared powers slow it, so the two cancel out",
     "The data contradict both statements",
     "The data support the access-point claim but refute the constraint claim"], ans=0,
   why="A branch that contests a policy is a branch someone reached, so the venue and the obstacle are the same institution seen from two sides. That identity is why the framework states both claims about one allocation of powers."),

 dict(q="Which question would best test LO 2.15.A's claim about the EXTENT of accountability given competing interests?",
   choices=[
     "When the three branches want different things from an agency, how often does the agency end up doing what any of them wanted?",
     "How many oversight hearings did Congress hold last year?",
     "How many agency officials are political appointees?",
     "How many regulations did agencies issue last year?",
     "How large is the federal bureaucracy compared with a decade ago?"], ans=0,
   why="LO 2.15.A asks how far accountability reaches GIVEN COMPETING INTERESTS, so the test has to condition on the branches disagreeing and then look at the outcome. Counts of hearings, appointees and regulations measure activity."),

 dict(q="Which statement best summarizes what this topic adds to the four bureaucracy topics before it?",
   choices=[
     "The instruments described separately are exercised at the same time by branches that want different things, so their combined effect is contested rather than cumulative",
     "The instruments described separately are exercised by a single branch acting alone",
     "The instruments described separately have no effect on agency behavior",
     "The instruments described separately are exercised only when an agency has broken the law",
     "The instruments described separately were replaced by the merit system"], ans=0,
   why="LO 2.15.A's 'given the competing interests' is the addition: topics 2.12 to 2.14 supply the instruments and this topic asks what happens when all of them operate at once on the same agency."),
]
