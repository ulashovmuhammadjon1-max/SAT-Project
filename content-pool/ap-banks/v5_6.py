# AP U.S. GOVERNMENT AND POLITICS 5.6 Interest Groups Influencing Policymaking
# -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# TWO learning objectives:
#   LO 5.6.A -- explain the BENEFITS AND POTENTIAL PROBLEMS of interest group
#     influence on elections and policymaking.
#   LO 5.6.B -- explain how VARIATION IN TYPES of interest groups and the
#     RESOURCES they possess affects their ability to influence elections and
#     policymaking.
# Suggested skill for this topic (CED p. 116): 3.F, data analysis -- explain
# possible limitations of the VISUAL REPRESENTATION of the data provided.
#
# Essential knowledge relied on:
#   EK 5.6.A.1 -- interest groups "may represent VERY SPECIFIC OR MORE GENERAL
#     interests, and can EDUCATE VOTERS AND OFFICE HOLDERS, CONDUCT LOBBYING,
#     DRAFT LEGISLATION, and MOBILIZE MEMBERSHIP to apply pressure on and work
#     with legislators and government agencies. Interest groups may also file an
#     AMICUS CURIAE BRIEF (a written document submitted as a 'FRIEND OF THE
#     COURT' to provide additional information for justices to consider when
#     reviewing a case)."
#   EK 5.6.A.2 -- "In addition to working WITHIN party coalitions, interest
#     groups exert influence through IRON TRIANGLES and ISSUE NETWORKS that help
#     interest groups exert influence ACROSS political party coalitions."
#   EK 5.6.B.1 -- "The INEQUALITY of interest group resources affects the amount
#     of influence they may have on the policymaking process.
#       i.   Some interest groups, SUCH AS AARP, have LARGE MEMBERSHIPS, are
#            ABLE TO MOBILIZE those members, and possess ACCESS TO LARGE
#            FINANCIAL RESERVES.
#       ii.  Some interest groups have MORE DIRECT AND MORE FREQUENT ACCESS to
#            important people in the policy process.
#       iii. FREE RIDERS are individuals who BENEFIT FROM THE WORK OF AN INTEREST
#            GROUP WITHOUT PROVIDING FINANCIAL SUPPORT. Interest groups may deal
#            with this issue by providing SELECTIVE BENEFITS, GOODS AND SERVICES
#            THAT ARE ONLY AVAILABLE TO MEMBERS, to encourage more people to
#            join."
#
# EK 5.6.A.2'S PREPOSITION IS THE CONTENT. Interest groups work WITHIN party
# coalitions, and iron triangles and issue networks help them exert influence
# ACROSS political party coalitions. The framework's whole point in that sentence
# is the second preposition: these arrangements reach past party lines, which is
# why they are worth naming separately from ordinary coalition politics. A
# paraphrase that has iron triangles operating within a party has dropped the
# reason the statement exists. Items 9 to 12 turn on it.
#
# EK 5.6.B.1.i NAMES AARP, so the organization is course content here and may be
# named -- unlike the illustrative examples in this and other topics, which the
# CED marks NOT REQUIRED and which this module does not use.
#
# THREE RESOURCE ADVANTAGES, AND FREE RIDING IS THE ONE THAT IS NOT AN ADVANTAGE.
# EK 5.6.B.1.i and ii describe things a group HAS; EK 5.6.B.1.iii describes a
# PROBLEM groups face and the SELECTIVE BENEFITS they use against it. Reading the
# third item as a third kind of resource loses the structure of the statement.
#
# WHY THIS MODULE DESCRIBES CHARTS. The suggested skill is 3.F, and it is
# unusually specific: the limitations of the VISUAL REPRESENTATION of the data,
# not of the data itself. Those are different objects -- a truncated axis, a
# chart of shares that hides counts, a chart of counts that hides rates -- and a
# question about sampling or causation would be answering skill 3.E instead. So
# items 19 to 24 describe how a chart is DRAWN and ask what the drawing conceals,
# and both tables are paired with an item of that kind. Every described chart is
# labelled hypothetical and attributed to no one, for the reason set out in 4.8.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.6", "Interest Groups Influencing Policymaking", 5)

_RESOURCES = ("A hypothetical study reports four interest groups' memberships, how many members "
              "acted when the group asked, and their financial reserves.")
_RESOURCES_TABLE = dict(
    headers=["Interest group", "Members (thousands)", "Members who acted when asked (%)",
             "Financial reserves (millions of dollars)"],
    rows=[["Group J", "38000", "12", "310"],
          ["Group K", "120", "64", "45"],
          ["Group L", "2400", "31", "180"],
          ["Group M", "15", "78", "9"]])

_RIDERS = ("A hypothetical study paired four interest groups by the size of the population that "
           "benefits from their work, and recorded how many people pay dues and whether the "
           "group offers goods and services available only to members.")
_RIDERS_TABLE = dict(
    headers=["Interest group", "People who benefit from its work (thousands)",
             "Dues-paying members (thousands)", "Offers members-only goods and services"],
    rows=[["Group P", "900", "45", "No"],
          ["Group Q", "900", "310", "Yes"],
          ["Group R", "260", "22", "No"],
          ["Group S", "260", "104", "Yes"]])

QUESTIONS = [
 dict(q="According to the course framework, what range of interests may interest groups represent?",
   choices=[
     "Very specific interests or more general ones",
     "Only very specific interests",
     "Only broad national interests",
     "Only the interests of a single political party",
     "Only interests represented in Congress"], ans=0,
   why="EK 5.6.A.1 opens by saying interest groups may represent very specific or more general interests. The breadth of an interest is one of the variations LO 5.6.B asks about."),

 dict(q="Which four activities does EK 5.6.A.1 say interest groups can carry out?",
   choices=[
     "Educating voters and office holders, conducting lobbying, drafting legislation, and mobilizing membership",
     "Nominating candidates, running primaries, holding conventions, and managing campaigns",
     "Registering voters, counting ballots, certifying results, and seating members",
     "Appointing judges, confirming nominees, impeaching officials, and ratifying treaties",
     "Setting polling hours, issuing voter identification, funding polling places, and allowing early voting"], ans=0,
   why="EK 5.6.A.1 names exactly these four. The second option lists party functions from EK 5.3.B.1, and the last lists state election decisions from EK 5.2.A.2."),

 dict(q="According to EK 5.6.A.1, whom do interest groups mobilize their membership to work with and apply pressure on?",
   choices=[
     "Legislators and government agencies",
     "Voters and party officials",
     "Judges and juries",
     "Journalists and editors",
     "State governors only"], ans=0,
   why="EK 5.6.A.1's phrase is 'apply pressure on and work with legislators and government agencies'. Naming agencies alongside legislators is what connects this statement to EK 5.6.A.2's iron triangles."),

 dict(q="According to the course framework, what is an AMICUS CURIAE BRIEF?",
   choices=[
     "A written document submitted as a friend of the court to provide additional information for justices to consider when reviewing a case",
     "A written argument submitted by one of the parties to a case",
     "An order issued by a court to a lower court",
     "A statute passed by Congress about a pending case",
     "A summary of a case prepared by the justices themselves"], ans=0,
   why="EK 5.6.A.1's parenthesis defines it in exactly these words. The phrase FRIEND OF THE COURT marks the filer as someone other than a party, which is what makes it a way for an interest group to reach a court at all."),

 dict(q="What does the phrase FRIEND OF THE COURT indicate about who files an amicus curiae brief?",
   choices=[
     "That the filer is not a party to the case but is offering information for the justices to consider",
     "That the filer is one of the two parties to the case",
     "That the filer is a judge on another court",
     "That the filer is an employee of the court",
     "That the filer has been appointed by the president"], ans=0,
   why="EK 5.6.A.1's parenthesis describes the brief as providing ADDITIONAL information for justices to consider, which presupposes the filer is not the one whose case it is. That is precisely why the device is available to an interest group."),

 dict(q="An interest group prepares model language for a bill and gives it to a legislator's staff. Which activity named in EK 5.6.A.1 does this illustrate?",
   choices=[
     "Drafting legislation",
     "Conducting lobbying",
     "Educating voters",
     "Mobilizing membership",
     "Filing an amicus curiae brief"], ans=0,
   why="EK 5.6.A.1 names drafting legislation as one of the four activities, and supplying bill language is that activity directly. Lobbying and drafting are listed separately in the framework's own sentence."),

 dict(q="An interest group asks its members to contact their representatives about a pending bill. Which activity named in EK 5.6.A.1 does this illustrate?",
   choices=[
     "Mobilizing membership to apply pressure on legislators",
     "Drafting legislation",
     "Filing an amicus curiae brief",
     "Educating office holders",
     "Conducting lobbying by the group's own staff"], ans=0,
   why="EK 5.6.A.1 names mobilizing membership to apply pressure on and work with legislators and government agencies. What distinguishes it from lobbying is who does the contacting: the members rather than the group's staff."),

 dict(q="Which of EK 5.6.A.1's activities allows an interest group to influence a branch of government that it cannot lobby directly?",
   choices=[
     "Filing an amicus curiae brief",
     "Conducting lobbying",
     "Drafting legislation",
     "Mobilizing membership",
     "Educating voters"], ans=0,
   why="The other four activities are aimed at voters, legislators and agencies, while EK 5.6.A.1's amicus curiae brief provides information to justices reviewing a case. It is the one route on the framework's list that reaches a court."),

 dict(q="According to EK 5.6.A.2, what do iron triangles and issue networks help interest groups do?",
   choices=[
     "Exert influence across political party coalitions",
     "Exert influence within a single political party coalition",
     "Nominate candidates for office",
     "Register voters in several states",
     "File amicus curiae briefs"], ans=0,
   why="EK 5.6.A.2's own phrase is 'exert influence ACROSS political party coalitions'. The sentence's first clause already covers working WITHIN party coalitions, so the preposition is what the statement adds."),

 dict(q="EK 5.6.A.2 contrasts working WITHIN party coalitions with exerting influence ACROSS them. Why does that contrast matter?",
   choices=[
     "Because it identifies arrangements that reach past party lines, which is what makes them worth naming separately from ordinary coalition politics",
     "Because it means interest groups never work within a party coalition",
     "Because it means party coalitions do not exist",
     "Because it means iron triangles are part of the party organization",
     "Because it means interest groups may work with only one party"], ans=0,
   why="EK 5.6.A.2 says interest groups work within party coalitions IN ADDITION TO exerting influence through these arrangements, so both happen. The framework names iron triangles and issue networks because they operate across the party division rather than inside it."),

 dict(q="An interest group, a congressional committee, and a federal agency maintain a stable working relationship on one policy area that persists as party control of Congress changes. Which framework statement does this illustrate?",
   choices=[
     "EK 5.6.A.2's account of iron triangles helping interest groups exert influence across political party coalitions",
     "EK 5.6.A.1's account of amicus curiae briefs",
     "EK 5.6.B.1.iii's account of free riders",
     "EK 5.3.B.1's list of party functions",
     "EK 5.5.A.2's account of incorporated agendas"], ans=0,
   why="The three participants and the persistence across changes in party control are exactly what EK 5.6.A.2 describes, and the detail that it survives a change in control is the ACROSS in the framework's sentence. EK 5.6.A.1 names legislators and government agencies as the bodies groups work with."),

 dict(q="How does EK 5.6.A.2 relate to EK 5.6.A.1's statement that groups work with legislators and government agencies?",
   choices=[
     "EK 5.6.A.1 names the bodies a group deals with, and EK 5.6.A.2 names the stable arrangements through which those dealings can cross party lines",
     "The two statements describe unrelated activities",
     "EK 5.6.A.2 says groups do not work with agencies",
     "EK 5.6.A.1 concerns courts and EK 5.6.A.2 concerns legislatures",
     "The two statements are alternative wordings of one claim"], ans=0,
   why="EK 5.6.A.1's list of bodies -- legislators and government agencies -- names two of the three participants in the arrangements EK 5.6.A.2 describes. One statement gives the activity and the other the structure it can settle into."),

dict(q="According to EK 5.6.B.1, what affects the amount of influence interest groups may have on policymaking?",
   choices=[
     "The inequality of interest group resources",
     "The equality of interest group resources",
     "The number of political parties in the legislature",
     "The date of the next election",
     "The number of committees in Congress"], ans=0,
   why="EK 5.6.B.1's own noun is INEQUALITY: it is the differences among groups' resources, not their resources in general, that the framework says affects influence. LO 5.6.B asks about variation for the same reason."),

 dict(q="Which three resources does EK 5.6.B.1.i attribute to some interest groups, naming AARP as its example?",
   choices=[
     "Large memberships, the ability to mobilize those members, and access to large financial reserves",
     "Large memberships, favorable court rulings, and media ownership",
     "Access to justices, control of a party platform, and ballot access",
     "Selective benefits, free riders, and dues",
     "Committee assignments, staff, and office space"], ans=0,
   why="EK 5.6.B.1.i names all three, and it names AARP as its example, which makes that organization course content for this topic rather than an illustration a teacher supplies."),

dict(q="Why does EK 5.6.B.1.i name the ABILITY TO MOBILIZE members separately from having a large membership?",
   choices=[
     "Because a large membership that does not act supplies less influence than a smaller one that does",
     "Because mobilization is prohibited for large groups",
     "Because the two phrases mean the same thing",
     "Because only small groups can mobilize members",
     "Because mobilization concerns finances rather than members"], ans=0,
   why="EK 5.6.B.1.i lists having members and being able to mobilize them as two things, and EK 5.6.A.1 makes mobilizing membership an activity rather than a possession. A roster is not the same as a roster that responds."),

 dict(q="What second kind of resource advantage does EK 5.6.B.1.ii name?",
   choices=[
     "More direct and more frequent access to important people in the policy process",
     "A larger number of dues-paying members",
     "Ownership of a media outlet",
     "The right to file an amicus curiae brief",
     "A seat on a congressional committee"], ans=0,
   why="EK 5.6.B.1.ii names access that is both more direct and more frequent. It is an advantage independent of size, which is why the framework lists it separately from EK 5.6.B.1.i's memberships and reserves."),

 dict(q="According to the course framework, what is a FREE RIDER?",
   choices=[
     "An individual who benefits from the work of an interest group without providing financial support",
     "An individual who joins an interest group but does not attend meetings",
     "An interest group that receives government funding",
     "A legislator who accepts help from an interest group",
     "A member who pays dues but receives no benefits"], ans=0,
   why="EK 5.6.B.1.iii defines a free rider in exactly these words. Both halves matter: the person benefits, and the person does not pay."),

dict(q="According to the course framework, what are SELECTIVE BENEFITS and what problem do they address?",
   choices=[
     "Goods and services available only to members, offered to encourage more people to join and so to address free riding",
     "Payments an interest group makes to legislators",
     "Tax advantages an interest group receives from the government",
     "Services an interest group provides to the general public",
     "Discounts an interest group negotiates for nonmembers"], ans=0,
   why="EK 5.6.B.1.iii defines selective benefits as goods and services only available to members and says groups use them to encourage more people to join. The word ONLY is what makes them work against free riding: a benefit the public receives anyway gives no one a reason to pay."),

 dict(q="Why is EK 5.6.B.1.iii different in kind from EK 5.6.B.1.i and ii?",
   choices=[
     "The first two describe advantages a group possesses, while the third describes a problem groups face and a response to it",
     "The third describes an advantage and the first two describe problems",
     "All three describe the same advantage",
     "The third concerns courts and the first two concern legislatures",
     "The third applies only to groups with large memberships"], ans=0,
   why="EK 5.6.B.1.i and ii name memberships, reserves and access, all of which a group HAS. EK 5.6.B.1.iii names free riding, which a group SUFFERS, together with the selective benefits it may use against it, so reading the third as a third resource loses the statement's structure."),

 dict(q="A hypothetical bar chart shows four interest groups. The bars represent the share of members who took action when the group asked, and the tallest bar belongs to the group with the fewest members. What is the most important limitation of this visual representation?",
   choices=[
     "Showing a rate alone makes a small group look strongest, because the chart gives the viewer no way to see how many people each bar represents",
     "The chart uses bars rather than a line",
     "The chart shows four groups rather than three",
     "The chart does not identify which groups were surveyed",
     "The chart shows a share rather than a count, which is always an error"], ans=0,
   why="Skill 3.F asks about limitations of the visual representation rather than of the data, and a chart of rates omits the denominator by construction. A share is not an error in itself; the limitation is that this particular drawing leaves the size of each group invisible."),

 dict(q="A hypothetical bar chart shows the financial reserves of several interest groups, but its vertical axis begins at a value well above zero rather than at zero. What is the most important limitation of this visual representation?",
   choices=[
     "The truncated axis exaggerates the apparent differences between the groups, since the bars no longer show quantities in proportion",
     "The chart should have used more colors",
     "Financial reserves cannot be shown on a bar chart",
     "The chart omits the groups' memberships, which is a limitation of the data",
     "The chart shows too many groups to read"], ans=0,
   why="A bar's length reads as a quantity, so a baseline above zero makes ratios between bars appear larger than they are. That is a property of how the data was drawn, which is exactly what skill 3.F asks about."),

 dict(q="A hypothetical pie chart shows the share of lobbying contacts made by interest groups in one policy area. Every slice is labeled with a group's name, and one slice labeled OTHER accounts for a third of the circle. What is the most important limitation of this visual representation?",
   choices=[
     "A third of the contacts are hidden inside a single undifferentiated slice, so the chart cannot show how they are distributed among the groups it does not name",
     "Pie charts may not be used for lobbying data",
     "The chart shows shares rather than counts",
     "The chart does not report which policy area is involved",
     "The chart uses a circle rather than a rectangle"], ans=0,
   why="Skill 3.F concerns what the drawing conceals, and an aggregated residual category conceals whatever structure lies inside it. The stem states the policy area, so that is not what is missing."),

 dict(q="A student is asked to explain the limitations of a chart and writes that the underlying survey used too small a sample. Which skill has the student answered?",
   choices=[
     "A limitation of the data rather than of its visual representation, which is a different question",
     "A limitation of the visual representation, correctly",
     "Neither, since sample size is never a limitation",
     "Both equally, since the two are the same question",
     "A limitation of the argument rather than of the data"], ans=0,
   why="Skill 3.F is specifically about the limitations of the VISUAL REPRESENTATION of the data, while sample size is a property of the data itself and belongs to skill 3.E. The two are separate skills in the CED's own list."),

 dict(q="Which of the following is a limitation of a VISUAL REPRESENTATION rather than of the underlying data?",
   choices=[
     "A chart plotting only totals, so that differences in rates between groups cannot be seen",
     "A survey that reached only members of one organization",
     "A study covering a single year",
     "A question worded so as to favor one answer",
     "A sample too small to support a conclusion"], ans=0,
   why="Skill 3.F asks what a particular drawing conceals, and a chart of totals hides rates by construction even when the underlying figures include them. The other four options describe how the data was collected or worded, which belongs to skill 3.E."),

 dict(q=_RESOURCES + " Which conclusion is best supported by the data?",
   table=_RESOURCES_TABLE,
   choices=[
     "The group with the most members has the lowest share of members acting, but the largest number of members acting",
     "The group with the most members has the highest share of members acting",
     "The group with the fewest members has the largest financial reserves",
     "Every group has a similar share of members acting",
     "The group with the fewest members mobilizes the most people"], ans=0,
   why="Group J has 38000 thousand members and the lowest action rate at 12 percent, which still yields about 4560 thousand members acting, far more than any other group. Group M, the smallest, has the highest rate at 78 percent and mobilizes about 12 thousand people."),

 dict(q=_RESOURCES + " Which statement in the course framework do the three data columns most directly correspond to?",
   table=_RESOURCES_TABLE,
   choices=[
     "EK 5.6.B.1.i's large memberships, ability to mobilize members, and access to large financial reserves",
     "EK 5.6.B.1.iii's free riders and selective benefits",
     "EK 5.6.A.1's four activities of interest groups",
     "EK 5.6.A.2's iron triangles and issue networks",
     "EK 5.3.A.1's four linkage institutions"], ans=0,
   why="The columns are membership size, the share of members who acted, and financial reserves, which are EK 5.6.B.1.i's three resources in order. That statement lists them together because the framework's subject is the inequality among groups on exactly these dimensions."),

 dict(q=_RESOURCES + " A hypothetical chart of this data plots only the third column as bars, one per group. What is the most important limitation of that visual representation?",
   table=_RESOURCES_TABLE,
   choices=[
     "It would make the smallest group appear the most powerful, since the bars would show rates with no indication that one group has more than two thousand times another's membership",
     "It would exaggerate the differences between the groups' financial reserves",
     "It would fail to identify which groups were studied",
     "It would use bars where a line chart is required",
     "It would show a limitation of the data rather than of the chart"], ans=0,
   why="The third column is the share of members who acted, on which Group M leads at 78 percent while having 15 thousand members against Group J's 38000 thousand. A chart of that column alone omits the membership figures by construction, which is a limitation of the drawing rather than of the data."),

 dict(q=_RIDERS + " Which conclusion is best supported by the data?",
   table=_RIDERS_TABLE,
   choices=[
     "Within each pair of groups serving the same number of beneficiaries, the group offering members-only goods and services has far more dues-paying members",
     "The group with the most beneficiaries has the most dues-paying members",
     "Offering members-only goods and services makes no difference to dues-paying membership",
     "Every group has more dues-paying members than beneficiaries",
     "The two groups serving 260 thousand beneficiaries have equal dues-paying membership"], ans=0,
   why="At 900 thousand beneficiaries the figures are 45 against 310 thousand dues payers, and at 260 thousand they are 22 against 104. In every row the beneficiary count exceeds the dues-paying count, which is the pattern the free rider concept describes."),

 dict(q=_RIDERS + " Which statement in the course framework does this pattern most directly illustrate?",
   table=_RIDERS_TABLE,
   choices=[
     "EK 5.6.B.1.iii's free riders and the selective benefits groups use to encourage more people to join",
     "EK 5.6.B.1.ii's more direct and more frequent access to important people",
     "EK 5.6.A.2's iron triangles and issue networks",
     "EK 5.6.A.1's amicus curiae briefs",
     "EK 5.5.A.1's winner-take-all voting districts"], ans=0,
   why="The gap between beneficiaries and dues payers is free riding as EK 5.6.B.1.iii defines it, and the fourth column records exactly the response the framework names. The pairing by beneficiary count is what lets the two be seen together."),

 dict(q=_RIDERS + " A hypothetical chart of this data plots only the dues-paying membership of each group as bars. What is the most important limitation of that visual representation?",
   table=_RIDERS_TABLE,
   choices=[
     "It would hide the beneficiary population entirely, and with it the free riding that the comparison between the two columns reveals",
     "It would exaggerate the differences between the groups' dues-paying memberships",
     "It would fail to say whether each group offers members-only goods and services",
     "It would show counts where shares are required",
     "It would describe a limitation of the data rather than of the chart"], ans=0,
   why="Free riding is visible only as a gap between two columns, so a chart of one of them cannot show it however accurately it is drawn. Skill 3.F asks what a drawing conceals, and this drawing conceals the framework's own concept by construction."),
]
