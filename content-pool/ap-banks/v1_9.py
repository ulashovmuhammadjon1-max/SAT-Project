# AP U.S. GOVERNMENT AND POLITICS 1.9 Federalism in Action -- 30 questions
# CED V.1 (c) 2026, Unit 1 Foundations of American Democracy.
# Learning objective 1.9.A: explain how the distribution of powers between
# national and state governments impacts policymaking.
# Suggested skill for this topic (CED p. 51): 5.B, support an argument or
# claim/thesis using relevant evidence. This module is weighted accordingly:
# a large share of its items give a claim and ask which evidence supports,
# weakens or is irrelevant to it, which is the shape 5.B tests.
#
# Essential knowledge relied on. There are only TWO statements, and they are
# short, so the discipline for this module is not coverage but restraint:
#   EK 1.9.A.1 -- "The allocation of powers between national and state
#     governments creates multiple access points for stakeholders and
#     institutions to influence public policy."
#   EK 1.9.A.2 -- "National policymaking is constrained by the sharing of
#     concurrent powers with state governments."
#
# TWO STATEMENTS, TWO DIRECTIONS, AND THE MODULE KEEPS THEM APART. EK 1.9.A.1 is
# about OPPORTUNITY -- more governments means more doors an outside actor can
# knock on. EK 1.9.A.2 is about CONSTRAINT -- more governments means the
# national government cannot deliver an outcome by itself. They are the same
# structural fact seen from opposite sides, and an item that blurs them tests
# nothing. Items 1 to 10 are access-point items, items 11 to 20 are constraint
# items, and item 26 asks a student to tell which of the two a scenario shows.
#
# NOTE ON A NEIGHBOURING TOPIC: EK 1.6.B.1 uses almost the same access-point
# sentence about SEPARATION OF POWERS, and EK 1.9.A.1 uses it about FEDERALISM.
# The distinction is real -- branches against levels -- and the v1_6 module owns
# the branches version. Every access-point item here turns on a state or local
# government, never on a second branch of the national government, so the two
# modules do not test the same thing twice.
#
# Documents the CED attaches to 1.9.A (p. 26-27): Federalist No. 10,
# Federalist No. 39, Federalist No. 51.
# Required cases the CED attaches to 1.9.A (p. 31-32): Shaw v. Reno,
# United States v. Lopez.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: Federalist No. 10 and No. 39 are quoted
# verbatim. Both tables are labelled hypothetical, because state-by-state policy
# counts could not be verified against a source here.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("1.9", "Federalism in Action", 1)

_ADOPT = ("In a hypothetical federal system of fifty states, the table reports how many "
          "states had adopted a particular regulatory policy in each of four years, and "
          "whether the national legislature had acted on the subject.")
_ADOPT_TABLE = dict(
    headers=["Year", "States that had adopted the policy", "National statute in force"],
    rows=[["Year 1", "3", "No"],
          ["Year 5", "11", "No"],
          ["Year 9", "26", "No"],
          ["Year 13", "38", "Yes"]])

_VENUE = ("In a hypothetical study, advocacy organizations were asked where they had pressed "
          "their principal policy goal during the preceding two years. Respondents could "
          "name more than one venue, so the column does not sum to one hundred.")
_VENUE_TABLE = dict(
    headers=["Venue", "Organizations naming it (%)"],
    rows=[["A state legislature", "71"],
          ["A federal agency", "58"],
          ["Congress", "54"],
          ["A state agency", "49"],
          ["A federal court", "33"],
          ["A local government", "31"]])

QUESTIONS = [
 dict(q="According to the course framework, the allocation of powers between national and state governments creates",
   choices=[
     "multiple access points for stakeholders and institutions to influence public policy",
     "a single national forum in which all policy questions are settled",
     "an obligation on the states to adopt whatever policy Congress prefers",
     "a prohibition on interest group activity at the state level",
     "identical policy outcomes in every state"], ans=0,
   why="EK 1.9.A.1 states this in exactly these words. The remaining options describe a unitary system, which is what a federal allocation of powers is not."),

 dict(q="An environmental organization unable to persuade Congress to restrict a practice instead wins restrictions in eleven state legislatures. Which claim does this episode best support?",
   choices=[
     "That the distribution of powers between levels gives an interest more than one place to pursue the same goal",
     "That state legislatures are constitutionally required to act when Congress declines to",
     "That Congress had no authority over the subject in the first place",
     "That interest groups exercise formal governmental powers of their own",
     "That a policy adopted by eleven states binds the other thirty-nine"], ans=0,
   why="EK 1.9.A.1 names the multiple access points the allocation creates, and a defeat nationally followed by wins in several states is that structure in operation. Nothing in the episode establishes an obligation on any legislature or a binding effect on other states."),

 dict(q="Which of the following is the best evidence for the claim that federalism multiplies the opportunities available to an organized interest?",
   choices=[
     "A single organization pursued the same policy before a state legislature, a state agency and a federal agency within one year",
     "A single organization employs more staff than it did a decade earlier",
     "Congress passed more statutes in one session than in the previous session",
     "A federal agency issued a rule after a public comment period",
     "A majority of citizens report following news about state government"], ans=0,
   why="The claim is about the NUMBER OF VENUES available, so the evidence must show one actor using several. Staff size, legislative output, a single rulemaking and news attention are each consistent with a system having only one access point."),

 dict(q="A national association of city governments lobbies Congress for a change in federal law and simultaneously asks thirty state legislatures for the same change in state law. Which feature of the constitutional system makes this strategy possible?",
   choices=[
     "Both levels of government hold authority over the subject, so either can act on it",
     "The Constitution requires Congress to consult state governments before legislating",
     "State legislatures may enact federal law when Congress fails to act",
     "Local governments hold powers reserved to them by the Tenth Amendment",
     "The Supremacy Clause obliges states to adopt whatever cities request"], ans=0,
   why="The strategy works because the subject falls within the authority of both levels, which is EK 1.7.A.4's concurrent powers seen from the advocate's side. The Tenth Amendment reserves powers to the states, not separately to local governments."),

 dict(q="Read the following excerpt.\n\n“Extend the sphere, and you take in a greater variety of parties and interests; you make it less probable that a majority of the whole will have a common motive to invade the rights of other citizens.”\n—James Madison, Federalist No. 10, 1787\n\nHow does this reasoning relate to the access points EK 1.9.A.1 describes?",
   choices=[
     "A greater variety of interests spread across a large republic makes it likely that any given interest will find some government receptive to it",
     "A greater variety of interests means that only the national government can act on any subject",
     "Madison argues that the states should be abolished so that one majority governs",
     "Madison argues that interest groups should be barred from petitioning government",
     "Madison argues that policy should be uniform across the whole republic"], ans=0,
   why="Madison's extended republic contains many interests and many governments, and the practical consequence is that a coalition defeated in one arena may be a majority in another. Nothing in the passage argues for abolishing the states or for uniformity."),

 dict(q="Read the following excerpt.\n\n“The proposed Constitution, therefore, is, in strictness, neither a national nor a federal Constitution, but a composition of both.”\n—James Madison, Federalist No. 39, 1788\n\nAccording to the course framework, one consequence of that composition is that it",
   choices=[
     "allows multiple access points for political participation while limiting the concentration of power",
     "guarantees that policy will be uniform throughout the country",
     "gives each state a veto over acts of Congress",
     "makes the national government the only forum for policy disputes",
     "removes the states from the policymaking process"], ans=0,
   why="EK 1.7.A.1 credits Federalist No. 39 with exactly this pair of effects, and EK 1.9.A.1 restates the access-point half as a fact about policymaking."),

 dict(q="A group that has failed to persuade a state legislature turns to a federal agency, and when that fails, files suit in federal court. Which is the most accurate description of this sequence?",
   choices=[
     "The group is using the several access points the distribution of powers creates, without any guarantee that one will succeed",
     "The group is exercising a constitutional right to have its policy adopted somewhere",
     "The group is violating the separation of powers by approaching more than one institution",
     "The group is required to exhaust state remedies before approaching any federal body",
     "The group has abandoned the political process by going to court"], ans=0,
   why="EK 1.9.A.1 describes access points as opportunities to influence policy, not entitlements to win, which is why the key names the absence of a guarantee. Approaching several institutions is what the structure invites rather than a violation of it."),

 dict(q="Which of the following would most WEAKEN the claim that federalism gives ordinary citizens meaningful additional access to policymaking?",
   choices=[
     "Evidence that the organizations able to press claims at several levels at once are overwhelmingly the best funded",
     "Evidence that state legislatures meet for fewer days each year than Congress does",
     "Evidence that the number of state agencies has grown over time",
     "Evidence that federal courts hear cases from every state",
     "Evidence that citizens may attend local government meetings"], ans=0,
   why="The claim is about access being meaningful for ordinary citizens, so the strongest rebuttal is that using multiple access points requires resources most citizens lack. Growth in agencies and courts hearing cases both describe the existence of venues rather than who can use them."),

 dict(q="A researcher wants to test EK 1.9.A.1's claim empirically. Which research design would test it most directly?",
   choices=[
     "Track a set of policy proposals and count how many distinct governments each was pressed before, and with what result",
     "Survey citizens about whether they trust state or national government more",
     "Compare the total budgets of state governments with the federal budget",
     "Count the number of statutes Congress enacted in each of the last twenty sessions",
     "Measure how long the average federal court case takes to resolve"], ans=0,
   why="The claim is about the number of venues an interest can use, so the design has to follow proposals across venues. Trust, budgets, legislative output and case duration each measure something real and none of them measures access."),

 dict(q="Which statement best distinguishes the access points created by FEDERALISM from those created by the separation of powers?",
   choices=[
     "Federalism multiplies venues across levels of government; the separation of powers multiplies them across branches within a level",
     "Federalism multiplies venues across branches; the separation of powers multiplies them across levels",
     "Only federalism creates access points; the separation of powers eliminates them",
     "Only the separation of powers creates access points; federalism eliminates them",
     "The two produce identical access points, so no distinction can be drawn"], ans=0,
   why="EK 1.9.A.1 attributes access points to the allocation of powers BETWEEN LEVELS and EK 1.6.B.1 attributes them to separation of powers and checks and balances among branches. Both are true and they operate on different axes."),

 dict(q="According to the course framework, national policymaking is constrained by",
   choices=[
     "the sharing of concurrent powers with state governments",
     "the requirement that every federal statute be approved by a majority of states",
     "the inability of Congress to legislate on any subject the states have addressed",
     "the requirement that federal agencies obtain a governor's consent before acting",
     "the absence of any national power to tax"], ans=0,
   why="EK 1.9.A.2 states this in exactly these words. The other options describe formal state vetoes that the Constitution does not contain; the constraint is practical, arising from shared authority rather than from a required approval."),

 dict(q="Congress enacts a national standard but relies on state agencies to inspect, license and enforce it. Which constraint on national policymaking does this arrangement illustrate?",
   choices=[
     "The national government's objective depends on the capacity and cooperation of governments it does not control",
     "The national government may not set standards in any area the states regulate",
     "State agencies may repeal federal statutes they find burdensome",
     "Congress must obtain the consent of each state legislature before a statute takes effect",
     "Federal courts may not review the actions of state agencies"], ans=0,
   why="EK 1.9.A.2 locates the constraint in shared authority, and a statute implemented by state officials is only as effective as those officials' capacity and willingness. No state may repeal a federal statute or veto its enactment."),

 dict(q="A federal program produces very different results in different states. Which explanation follows most directly from EK 1.9.A.2?",
   choices=[
     "The program's outcomes depend on state choices about implementation, which vary because the states share authority over the subject",
     "The program was unconstitutional in the states where it worked poorly",
     "Congress intended the program to fail in some states",
     "Federal statutes have no effect until a state adopts them by referendum",
     "The Supremacy Clause does not apply to programs administered by states"], ans=0,
   why="Concurrent authority means state decisions shape what a national policy becomes on the ground, which is precisely why uniform statutes yield uneven results. The other options assert constitutional rules that do not exist."),

 dict(q="Which of the following is the best evidence that concurrent powers constrain national policymaking rather than merely complicating it?",
   choices=[
     "A national policy goal went unmet because a majority of states declined to take the actions the policy depended on",
     "A national policy required more pages of regulation than an earlier one",
     "A national policy was debated in Congress for more than a year before passage",
     "A national policy was administered by a newly created federal agency",
     "A national policy was upheld by the Supreme Court against a constitutional challenge"], ans=0,
   why="A constraint is a limit on what the national government can accomplish, so the evidence has to be an unmet objective traceable to state choices. Length of debate, volume of regulation and litigation outcomes describe process rather than constraint."),

 dict(q="In United States v. Lopez (1995), the Supreme Court held that Congress exceeded its power under the Commerce Clause when it made possession of a gun in a school zone a federal crime. How does this decision bear on EK 1.9.A.2?",
   choices=[
     "It shows that national policymaking is constrained not only in practice by shared administration but in law by the limits of enumerated powers",
     "It shows that the states may nullify federal statutes they consider unwise",
     "It shows that Congress may regulate any activity occurring near a school",
     "It shows that federal courts may not review acts of Congress",
     "It shows that concurrent powers were abolished by the Commerce Clause"], ans=0,
   why="EK 1.9.A.2 names a practical constraint arising from shared powers, and Lopez adds a legal one: the CED states the holding as Congress exceeding its Commerce Clause power. A court invalidating a statute is not a state nullifying it."),

 dict(q="In Shaw v. Reno (1993), the Supreme Court held that majority-minority districts created under the Voting Rights Act of 1965 may be constitutionally challenged by voters if race is the only factor used in creating the district. How does the case illustrate the interaction of national and state authority in policymaking?",
   choices=[
     "A state exercises the districting power while a national constitutional standard limits how it may be exercised",
     "The national government draws all legislative districts, subject to state approval",
     "The states may ignore national voting statutes within their own borders",
     "Districting decisions are unreviewable in federal court",
     "The Voting Rights Act transferred districting authority to the Supreme Court"], ans=0,
   why="Districting is a state function, and the CED's statement of the holding subjects it to an Equal Protection limit. That combination -- state action bounded by a national standard -- is the ordinary texture of policymaking in a federal system."),

 dict(q="A senator argues that a proposed national policy should be enacted as a set of conditions on federal grants rather than as a direct mandate. Which consideration best explains that choice?",
   choices=[
     "Conditions on funds induce state action in areas where the national government's own authority to command is uncertain",
     "Conditions on funds require no appropriation from Congress",
     "Conditions on funds are binding on the states even if they refuse the money",
     "Conditions on funds may be imposed without any congressional vote",
     "Conditions on funds are unreviewable by any court"], ans=0,
   why="Grant conditions work through inducement rather than command, which is why they reach subjects where a direct order might exceed an enumerated power. A state that declines the funds is not bound, which is the feature the third option denies."),

 dict(q="Which scenario best illustrates EK 1.9.A.2 rather than EK 1.9.A.1?",
   choices=[
     "A national health initiative reaches only part of its target population because many states decline to expand the programs it relies on",
     "A trade association presses the same proposal on Congress, a federal agency and four state legislatures",
     "A citizen testifies at a city council meeting and later at a state hearing on the same issue",
     "An organization files suit in federal court after losing in a state legislature",
     "A coalition wins a policy in six states after failing to win it nationally"], ans=0,
   why="EK 1.9.A.2 is about what the national government cannot accomplish alone; the other four describe outside actors finding additional venues, which is EK 1.9.A.1. Keeping the two statements apart is the point of the item."),

 dict(q="A commentator writes that federalism makes national policy slower but also more durable. Which reasoning best supports the second half of that claim?",
   choices=[
     "A policy that has had to win support at more than one level has a broader base and is harder for any single change of control to undo",
     "A policy adopted by Congress may not be repealed once it takes effect",
     "State governments are constitutionally forbidden to alter federal programs",
     "Federal courts automatically uphold any policy adopted at two levels",
     "Policies adopted slowly are always better designed than policies adopted quickly"], ans=0,
   why="Durability follows from the breadth of the coalition a multi-level policy must assemble, not from any legal bar to repeal. The second, third and fourth options assert rules that do not exist."),

 dict(q="Which question would best test the claim that shared authority constrains national policymaking in a particular policy area?",
   choices=[
     "In that area, how often has a stated national objective failed to be achieved because state governments did not act?",
     "In that area, how many federal employees are assigned to the program?",
     "In that area, how many pages does the governing statute run to?",
     "In that area, how many years ago was the first federal statute enacted?",
     "In that area, how many committees of Congress claim jurisdiction?"], ans=0,
   why="EK 1.9.A.2's claim is about outcomes the national government cannot deliver alone, so the test must connect unmet objectives to state inaction. Staffing, statute length, program age and committee jurisdiction measure other things entirely."),

 dict(q=_ADOPT + " Which conclusion is best supported by the data?",
   table=_ADOPT_TABLE,
   choices=[
     "A majority of states had adopted the policy before any national statute was in force",
     "The national statute preceded adoption by any state",
     "Adoption by the states stopped once the national statute took effect",
     "Fewer than half the states had adopted the policy by Year 13",
     "The number of adopting states fell between Year 5 and Year 9"], ans=0,
   why="By Year 9 twenty-six of fifty states had adopted the policy with no national statute in force, and twenty-six is a majority. Adoption rises in every interval and reaches thirty-eight by Year 13."),

 dict(q=_ADOPT + " Which claim about federalism do these data most directly support?",
   table=_ADOPT_TABLE,
   choices=[
     "States can act as venues for a policy that has not yet succeeded nationally, and their action can precede national action",
     "National policy always precedes state policy in a federal system",
     "State governments may enact national statutes when Congress declines to",
     "A policy adopted by a majority of states automatically becomes national law",
     "The states and the national government are constitutionally barred from regulating the same subject"], ans=0,
   why="The sequence in the table is state adoption first and national action last, which is EK 1.9.A.1's access points producing policy rather than merely offering a hearing. Nothing in the table makes state adoption automatically national."),

 dict(q=_ADOPT + " A student concludes from the table that state adoption CAUSED the national statute. Which limitation of the data most undercuts that conclusion?",
   table=_ADOPT_TABLE,
   choices=[
     "The table shows only the order of events, and an order is not by itself evidence that one event produced the other",
     "The table omits the year in which the national statute took effect",
     "The table reports the policies of only one state",
     "The table gives no information about how many states adopted the policy",
     "The table covers a single year, so no sequence can be observed"], ans=0,
   why="Sequence is consistent with causation and also with both being driven by something else, which is the standard limitation of a time-ordered table. The table plainly reports four years, the count of adopting states and the status of the national statute."),

 dict(q=_VENUE + " Which conclusion is best supported by the data?",
   table=_VENUE_TABLE,
   choices=[
     "More organizations named a state legislature than named any other single venue",
     "More organizations named Congress than named any other single venue",
     "Every organization named at least three venues",
     "Fewer than half the organizations named any federal venue",
     "The venues named divide evenly between state and federal institutions"], ans=0,
   why="The state legislature row is 71 percent, the highest figure in the column, ahead of the federal agency at 58 and Congress at 54. The stem says respondents could name more than one venue, so nothing in the table shows how many each named."),

 dict(q=_VENUE + " Which claim from the course framework do these data most directly support?",
   table=_VENUE_TABLE,
   choices=[
     "That the allocation of powers between levels creates multiple access points for stakeholders to influence policy",
     "That national policymaking is constrained by the sharing of concurrent powers",
     "That interest groups prefer courts to legislatures",
     "That state governments have more constitutional authority than the national government",
     "That organizations are barred from approaching more than one venue"], ans=0,
   why="Six venues at four levels and branches, each named by a substantial share of organizations, is EK 1.9.A.1's multiple access points measured. The constraint statement at EK 1.9.A.2 is about national capacity and is not what this table reports."),

 dict(q=_VENUE + " A student computes that the percentages sum to two hundred and ninety-six and concludes that the table must contain an error. What is the correct response?",
   table=_VENUE_TABLE,
   choices=[
     "The stem states that respondents could name more than one venue, so the shares are not a distribution and need not sum to one hundred",
     "The student is right, and one of the rows must be mistaken",
     "The percentages should be divided by six to produce a valid distribution",
     "The table is invalid because no organization can use more than one venue",
     "The sum shows that some organizations were counted twice by mistake"], ans=0,
   why="A multiple-response item produces overlapping categories, and the stem says so explicitly, so a sum above one hundred is expected rather than erroneous. Recognizing what a percentage is a percentage OF is the data-limitation skill at CED 3.E."),

 dict(q="Which pair of consequences of federalism does the course framework identify for policymaking?",
   choices=[
     "More venues in which policy can be influenced, and less capacity for the national government to act alone",
     "More venues in which policy can be influenced, and greater national capacity to act alone",
     "Fewer venues in which policy can be influenced, and less national capacity to act alone",
     "Fewer venues in which policy can be influenced, and greater national capacity to act alone",
     "No effect on venues, and no effect on national capacity"], ans=0,
   why="EK 1.9.A.1 supplies the first half and EK 1.9.A.2 the second, and they point in opposite directions from the same structural fact: authority divided between levels."),

 dict(q="An advocate argues that a policy should be pursued nationally rather than state by state. Which argument best supports that position, given the course framework's account of federalism?",
   choices=[
     "A national statute applies everywhere at once, whereas a state-by-state campaign leaves the policy absent wherever it has not yet won",
     "A national statute cannot be challenged in court, whereas a state statute can",
     "State legislatures are constitutionally barred from acting on subjects Congress has considered",
     "A national statute requires no implementation by any other government",
     "State governments have no authority over any subject Congress may regulate"], ans=0,
   why="Uniform coverage is the genuine advantage of the national route, and it is the mirror image of EK 1.9.A.1's access points, which produce uneven results. The fourth option contradicts EK 1.9.A.2's point that national policy often depends on state implementation."),

 dict(q="An advocate argues the opposite, that a policy should be pursued state by state first. Which argument best supports THAT position?",
   choices=[
     "Winning in several states builds a record of results and a coalition that a later national campaign can use",
     "A state statute automatically becomes national law once a majority of states adopt it",
     "Congress may not enact a statute on a subject until the states have acted",
     "State statutes are exempt from review by federal courts",
     "The national government has no authority over any subject the states regulate"], ans=0,
   why="The genuine case for the state-first route is that it produces evidence and allies, which is EK 1.9.A.1's access points used sequentially. The other four options assert constitutional rules that do not exist."),

 dict(q="A student writes that federalism's only effect on policymaking is to slow things down. Which correction does the course framework most directly support?",
   choices=[
     "It also multiplies the places where policy can be influenced, which can speed a policy's adoption somewhere even as it delays adoption everywhere",
     "It has no effect on the pace of policymaking at any level",
     "It removes the states from policymaking, which accelerates national action",
     "It requires that every policy be adopted at both levels simultaneously",
     "It guarantees that policy will be identical across all fifty states"], ans=0,
   why="EK 1.9.A.1 and EK 1.9.A.2 together describe both effects: constraint on unified national action and opportunity for action somewhere. Reducing the topic to delay drops half of what the framework says."),
]
