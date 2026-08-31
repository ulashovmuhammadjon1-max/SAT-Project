# AP U.S. GOVERNMENT AND POLITICS 4.10 Ideology and Social Policy -- 30 questions
# CED V.1 (c) 2026, Unit 4 American Political Ideologies and Beliefs.
# TWO learning objectives:
#   LO 4.10.A -- explain how political ideologies VARY ON THE ROLE OF THE
#     GOVERNMENT IN ADDRESSING SOCIAL ISSUES.
#   LO 4.10.B -- explain how different ideologies AFFECT POLICY on social issues.
# Suggested skill for this topic (CED p. 111): 4.C, source analysis -- explain
# how the IMPLICATIONS of the argument or perspective in the source may affect
# political principles, institutions, processes, policies, and behaviors.
#
# Essential knowledge relied on:
#   EK 4.10.A.1 -- "LIBERAL ideologies generally favor MORE NATIONAL government
#     involvement to address some social issues such as EDUCATION AND PUBLIC
#     HEALTH, with LESS responsibility for these issues left to STATE
#     governments."
#   EK 4.10.A.2 -- "CONSERVATIVE ideologies generally favor LESS NATIONAL
#     government involvement to address some social issues such as education and
#     public health, with MORE responsibility for these issues left to STATE
#     governments."
#   EK 4.10.A.3 -- "LIBERTARIAN ideologies generally favor LITTLE NATIONAL OR
#     STATE government involvement EXCEPT when national or state government is
#     PROTECTING PRIVATE PROPERTY OR INDIVIDUAL LIBERTY."
#   EK 4.10.B.1 -- "POLICY TRENDS concerning the level of government involvement
#     in social issues reflect the SUCCESS OF CONSERVATIVE OR LIBERAL
#     PERSPECTIVES IN POLITICAL PARTIES."
#
# EK 4.10.A.1 AND EK 4.10.A.2 ARE EXACT MIRRORS, AND THE LIBERTARIAN POSITION IS
# NOT A THIRD POINT ON THE SAME LINE. This is the structural fact the whole topic
# turns on. The first two statements use the same two variables -- national
# involvement and state responsibility -- and move them in opposite directions;
# they disagree about WHICH LEVEL should act. The third disagrees about WHETHER
# EITHER SHOULD, restraining national and state government alike, with two named
# exceptions. So a student who has arranged the three on a single line from most
# to least government has the first two right and the third wrong, because the
# libertarian position is not the conservative one taken further: it removes the
# state option that EK 4.10.A.2 relies on. Items 4 to 9 turn on that, and the
# verifier refuses any key that treats the third as a further step along the
# axis of the first two.
#
# EK 4.10.B.1 ROUTES POLICY THROUGH PARTIES. Its subject is policy TRENDS, and
# what those trends reflect is "the success of conservative or liberal
# perspectives IN POLITICAL PARTIES" -- not the success of those perspectives in
# the public, and not their correctness. The prepositional phrase is the
# mechanism and it is the first thing a paraphrase drops. Items 10 to 14 carry
# it, and the first table exists to show a trend while the item on it points out
# that a trend alone does not identify what produced it.
#
# NO ILLUSTRATIVE CASE IS NAMED. The CED lists three Supreme Court cases against
# this topic and marks all three ILLUSTRATIVE EXAMPLES (NOT REQUIRED). Each is
# also a live political controversy, which makes naming one doubly wrong here:
# it would be content the exam cannot ask about, and it would drag a contested
# question into a bank that has no business taking a position on it. Item 24
# makes the required-versus-illustrative distinction the question instead, and
# the verifier allows only the CED's fourteen required cases.
#
# Required cases the CED attaches to 4.10.A (p. 31): Brown v. Board of
# Education, Engel v. Vitale, Wisconsin v. Yoder. All three concern whether a
# national rule displaces a state or local one on a social question, which is
# the axis EK 4.10.A.1 and EK 4.10.A.2 describe. Items 15 to 18 use them.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("4.10", "Ideology and Social Policy", 4)

_FUNDING = ("A hypothetical study reports, for four successive periods, how the funding of one "
            "social policy area was divided between the national government and state and local "
            "governments.")
_FUNDING_TABLE = dict(
    headers=["Period", "National government share (%)", "State and local share (%)"],
    rows=[["Period 1", "6", "94"],
          ["Period 2", "9", "91"],
          ["Period 3", "13", "87"],
          ["Period 4", "11", "89"]])

_LEVELS = ("A hypothetical survey asked respondents which level of government should take "
           "primary responsibility for each of four social issues, or whether government at "
           "either level should do little about it.")
_LEVELS_TABLE = dict(
    headers=["Social issue", "Primarily the national government (%)",
             "Primarily state governments (%)", "Little involvement at either level (%)"],
    rows=[["Public health", "48", "39", "13"],
          ["Education", "31", "58", "11"],
          ["Public safety", "26", "62", "12"],
          ["Environmental protection", "57", "31", "12"]])

QUESTIONS = [
 dict(q="According to the course framework, what do LIBERAL ideologies generally favor on social issues?",
   choices=[
     "More national government involvement, with less responsibility left to state governments",
     "Less national government involvement, with more responsibility left to state governments",
     "Little national or state government involvement",
     "Involvement by local governments only",
     "No government involvement of any kind"], ans=0,
   why="EK 4.10.A.1 states this, naming education and public health as its examples. The statement moves two variables at once: national involvement up and state responsibility down."),

 dict(q="According to the course framework, what do CONSERVATIVE ideologies generally favor on social issues?",
   choices=[
     "Less national government involvement, with more responsibility left to state governments",
     "More national government involvement, with less responsibility left to state governments",
     "Little national or state government involvement",
     "Involvement by the federal courts only",
     "No government involvement of any kind"], ans=0,
   why="EK 4.10.A.2 states this, and its structure mirrors EK 4.10.A.1 exactly. The two positions use the same two variables and move them in opposite directions, so they disagree about which level should act rather than about whether government should."),

 dict(q="According to the course framework, what do LIBERTARIAN ideologies generally favor on social issues?",
   choices=[
     "Little national or state government involvement, except when government is protecting private property or individual liberty",
     "More national government involvement and less state responsibility",
     "Less national government involvement and more state responsibility",
     "Involvement by state governments only",
     "Government involvement in every social issue"], ans=0,
   why="EK 4.10.A.3 states this, including its two exceptions. The position restrains state government as well as national government, which is what separates it from the conservative position rather than placing it further along the same line."),

 dict(q="What do EK 4.10.A.1 and EK 4.10.A.2 disagree about?",
   choices=[
     "Which level of government should take primary responsibility for a social issue",
     "Whether any government should address social issues at all",
     "Whether education is a social issue",
     "Whether the Constitution permits government action",
     "Whether state governments exist"], ans=0,
   why="Both statements accept that government addresses social issues and differ over the balance between national involvement and state responsibility. They use the same two variables and move them in opposite directions."),

 dict(q="How does the libertarian position in EK 4.10.A.3 differ structurally from the two positions before it?",
   choices=[
     "It restrains national and state government alike, so it disagrees about whether either should act rather than about which one should",
     "It favors more national involvement than either of the others",
     "It favors more state responsibility than the conservative position",
     "It concerns only economic issues rather than social ones",
     "It is identical to the conservative position"], ans=0,
   why="EK 4.10.A.1 and EK 4.10.A.2 trade national involvement against state responsibility, while EK 4.10.A.3 favors little of either. The third statement removes the state option the second relies on, which is a different kind of disagreement."),

 dict(q="A student arranges the three ideologies on a single line from most government involvement to least, placing libertarian just beyond conservative. What is the most important correction?",
   choices=[
     "The libertarian position is not the conservative one taken further, because the conservative position shifts responsibility to states while the libertarian position restrains states too",
     "The libertarian position favors more involvement than the conservative one",
     "The three positions cannot be compared at all",
     "The conservative position restrains state governments as well",
     "The liberal and conservative positions are identical"], ans=0,
   why="EK 4.10.A.2 leaves more responsibility to state governments, which is a transfer rather than a reduction in total government action. EK 4.10.A.3 favors little involvement at either level, so it is off the line the first two share rather than further along it."),

 dict(q="Which two social issues does the course framework name as examples in both EK 4.10.A.1 and EK 4.10.A.2?",
   choices=[
     "Education and public health",
     "Education and national defense",
     "Public health and immigration",
     "Housing and transportation",
     "Criminal justice and taxation"], ans=0,
   why="Both statements use the phrase 'some social issues such as education and public health', which makes those two the framework's own examples. Using the same pair in both statements is what makes the two positions directly comparable."),

 dict(q="What are the two exceptions EK 4.10.A.3 attaches to the libertarian position?",
   choices=[
     "When government is protecting private property or individual liberty",
     "When government is funding education or public health",
     "When a state rather than the national government acts",
     "When a majority of the public supports the action",
     "When a court has ordered the action"], ans=0,
   why="EK 4.10.A.3 names protecting private property and protecting individual liberty as the circumstances in which the position accepts government involvement. Those exceptions are inside the position, which is why it is not a position of no government."),

 dict(q="EK 4.10.A.1, EK 4.10.A.2 and EK 4.10.A.3 all use the word GENERALLY. What does that indicate?",
   choices=[
     "That each describes a tendency within an ideology rather than a position every adherent holds on every issue",
     "That each position applies only in general elections",
     "That the three positions are the same in general",
     "That the framework is uncertain whether the positions exist",
     "That each position applies only to issues named in the framework"], ans=0,
   why="The framework hedges all three statements the same way, so each is a characterization of a tendency. An adherent taking a different view on a particular issue is what the word leaves room for."),

 dict(q="According to the course framework, what do policy trends concerning the level of government involvement in social issues reflect?",
   choices=[
     "The success of conservative or liberal perspectives in political parties",
     "The success of conservative or liberal perspectives in the courts",
     "The success of conservative or liberal perspectives in the general public",
     "The correctness of one of the two perspectives",
     "The size of the federal budget"], ans=0,
   why="EK 4.10.B.1 states this, and the prepositional phrase IN POLITICAL PARTIES is the mechanism it names. Success within parties is not the same thing as success with the public or in the courts."),

 dict(q="Why does the phrase IN POLITICAL PARTIES matter to EK 4.10.B.1's claim?",
   choices=[
     "Because it locates the mechanism by which a perspective becomes policy in the parties that nominate and organize officeholders",
     "Because it means the public has no influence on policy",
     "Because it means courts decide social policy",
     "Because it means parties write the essential knowledge statements",
     "Because it means policy trends are unrelated to ideology"], ans=0,
   why="EK 4.10.B.1 could have said perspectives succeed in the country and it says they succeed in political parties. That routes ideological change into policy through party organizations, which is what makes the statement a claim about a process."),

 dict(q="EK 4.10.B.1's subject is policy TRENDS. What does that word indicate about the level of the claim?",
   choices=[
     "That the claim concerns the direction of policy over a period rather than any single enactment",
     "That the claim concerns only proposals that failed",
     "That the claim concerns a single moment in time",
     "That the claim concerns only state policy",
     "That the claim concerns only federal spending"], ans=0,
   why="A trend is a direction across time, so EK 4.10.B.1 is a claim about accumulated movement rather than about why any one law passed. A single enactment can run against a trend without refuting a statement about trends."),

 dict(q="A commentator says that because one social policy was expanded last year, the liberal perspective has succeeded within its party. Which limitation of EK 4.10.B.1 does this argument overlook?",
   choices=[
     "The framework's claim is about trends rather than about a single enactment, so one policy change is weak evidence about the direction of policy",
     "The framework says policy never changes",
     "The framework says parties have no role in policy",
     "The framework says only conservative perspectives succeed",
     "The framework says social policy is set by the courts"], ans=0,
   why="EK 4.10.B.1's subject is policy TRENDS concerning the level of government involvement, and a single enactment is one observation. The inference also runs backward from an outcome to a cause the framework names but the observation does not establish."),

 dict(q="Which of the following does EK 4.10.B.1 NOT state?",
   choices=[
     "Which of the two perspectives produces better social policy",
     "That policy trends concerning the level of government involvement reflect something",
     "That what they reflect is the success of conservative or liberal perspectives",
     "That the success in question is success within political parties",
     "That the trends concern social issues"], ans=0,
   why="EK 4.10.B.1 describes a relationship between party politics and policy direction and evaluates neither perspective. Every other option restates part of its single sentence."),

 dict(q="In Brown v. Board of Education (1954), the Supreme Court held that race-based school segregation violates the equal protection clause of the Fourteenth Amendment. How does the decision bear on the axis EK 4.10.A.1 and EK 4.10.A.2 describe?",
   choices=[
     "It imposed a national constitutional requirement on a matter that states had been deciding, which is a shift on the national and state axis those statements describe",
     "It left the question entirely to state governments",
     "It concerned economic regulation rather than a social issue",
     "It was decided under the libertarian position of EK 4.10.A.3",
     "It had no effect on the division between national and state authority"], ans=0,
   why="The CED attaches Brown to 4.10.A and states its holding under the Fourteenth Amendment, and education is one of the two social issues EK 4.10.A.1 and EK 4.10.A.2 name. A national rule displacing state practice is a movement along their shared axis."),

 dict(q="In Engel v. Vitale (1962), the Supreme Court held that school sponsorship of religious activities violates the Establishment Clause of the First Amendment. What does the case illustrate about the national and state division on social issues?",
   choices=[
     "A national constitutional limit constraining what state and local school authorities may do",
     "A transfer of authority from the national government to the states",
     "A decision leaving religious practice in schools to local majorities",
     "A decision about economic regulation",
     "A decision that applied only to the national government"], ans=0,
   why="The CED attaches Engel to 4.10.A and states its holding under the Establishment Clause. A school district is a state instrumentality, so the holding constrains state and local action on a social question."),

 dict(q="In Wisconsin v. Yoder (1972), the Supreme Court held that compelling Amish students to attend school past the eighth grade violates the Free Exercise Clause of the First Amendment. Which position in EK 4.10.A.3 does the outcome most resemble in its effect?",
   choices=[
     "A limit on government involvement at the state level in the name of protecting individual liberty",
     "An expansion of national government involvement in education",
     "A transfer of responsibility from the national government to states",
     "An increase in state authority over schooling",
     "A requirement that states fund religious schools"], ans=0,
   why="Compulsory attendance is state law, and the holding relieved a group of it on a liberty ground. EK 4.10.A.3 describes a position favoring little state involvement except where government is protecting individual liberty, and the outcome resembles that shape even though the case was decided on the Free Exercise Clause rather than on any ideology."),

 dict(q="What do the three required cases the CED attaches to this topic have in common?",
   choices=[
     "Each concerns whether a national rule displaces what a state or local authority had been doing on a social question",
     "Each concerns the regulation of the marketplace",
     "Each was decided under the equal protection clause",
     "Each expanded the authority of state governments",
     "Each concerned the powers of Congress"], ans=0,
   why="Brown, Engel and Yoder all involve a national constitutional rule applied against a state or local practice in education or religion, which is the national and state axis EK 4.10.A.1 and EK 4.10.A.2 describe. They rest on three different clauses, so the shared feature is the axis rather than the provision."),

 dict(q="A commentator argues that leaving a social issue to the states produces more variation in policy than a national rule does, and that this is the point of doing so. What does this argument imply about EK 4.10.A.2?",
   choices=[
     "That the position it describes accepts differing policies across states as a consequence of leaving responsibility there",
     "That the position it describes requires every state to adopt the same policy",
     "That the position it describes eliminates state governments",
     "That the position it describes concerns only national policy",
     "That the position it describes is identical to the libertarian one"], ans=0,
   why="EK 4.10.A.2 favors more responsibility for these issues left to state governments, and fifty responsible governments can reach different answers. Read for implications as skill 4.C directs, the argument names a consequence the position accepts rather than an objection to it."),

 dict(q="A commentator argues that a national rule on a social issue is preferable because it guarantees the same protection everywhere. Which position does the argument's implication align with?",
   choices=[
     "The liberal position of EK 4.10.A.1, which favors more national involvement with less responsibility left to states",
     "The conservative position of EK 4.10.A.2",
     "The libertarian position of EK 4.10.A.3",
     "None of the three, since uniformity is not a political question",
     "All three equally, since each concerns social issues"], ans=0,
   why="Uniform protection everywhere requires the national government to set the rule, which is the direction EK 4.10.A.1 describes. Skill 4.C asks what follows from an argument, and this argument's implication is a preference about which level acts."),

 dict(q="A commentator argues that government should act on a social issue only where someone's property or freedom is directly at stake, and otherwise leave the matter alone at every level. Which position does this most closely match?",
   choices=[
     "The libertarian position of EK 4.10.A.3",
     "The liberal position of EK 4.10.A.1",
     "The conservative position of EK 4.10.A.2",
     "None of the three, since the framework covers only national policy",
     "All three, since each mentions government"], ans=0,
   why="The argument restrains government at every level and carves out protection of property and freedom, which is EK 4.10.A.3's structure including both of its named exceptions. The conservative position would move the matter to states rather than leave it alone."),

 dict(q="A commentator argues that whichever perspective controls the major parties will eventually control social policy, whatever the public thinks at any moment. Which statement in the course framework does this argument most closely track?",
   choices=[
     "EK 4.10.B.1's claim that policy trends reflect the success of conservative or liberal perspectives in political parties",
     "EK 4.10.A.3's account of the libertarian position",
     "EK 4.1.A.1's list of core values",
     "EK 4.5.A.2's account of polling methodology",
     "EK 4.3.A.1's account of generational effects"], ans=0,
   why="EK 4.10.B.1 locates the success that matters for policy trends inside political parties, which is exactly what the argument asserts. Read for implications, the argument also predicts that policy can move without a corresponding movement in public opinion."),

 dict(q="The CED lists several Supreme Court cases alongside this topic and marks them as illustrative examples that are not required. Why does that designation matter especially here?",
   choices=[
     "Because treating one as required content would both misrepresent what the exam can ask and import a contested political question the framework does not settle",
     "Because the cases were all overruled",
     "Because the cases concern economic rather than social policy",
     "Because illustrative examples are always more important than required ones",
     "Because the framework provides no required cases for this unit"], ans=0,
   why="The CED distinguishes required content from illustrative examples marked NOT REQUIRED, and the examples listed for this topic are also live political disputes. Presenting one as course content would put outside content beside framework content and take a side the framework does not take."),

 dict(q="How do LO 4.10.A and LO 4.10.B differ in what they ask about?",
   choices=[
     "The first asks how ideologies vary on the role of government, and the second asks how ideologies affect the policy that results",
     "The first concerns the courts and the second concerns Congress",
     "The first concerns economic policy and the second social policy",
     "The two ask the same question in different words",
     "Neither concerns political ideologies"], ans=0,
   why="LO 4.10.A is about the positions themselves, which EK 4.10.A.1 to 3 describe, and LO 4.10.B is about how those positions translate into policy, which EK 4.10.B.1 routes through political parties. The topic pairs a description of beliefs with an account of their effect."),

 dict(q=_FUNDING + " Which statement best describes the data?",
   table=_FUNDING_TABLE,
   choices=[
     "The national share rose across the first three periods and then fell slightly in the fourth",
     "The national share fell across all four periods",
     "The national share rose across all four periods",
     "The national share was unchanged across the four periods",
     "The state and local share rose across the first three periods"], ans=0,
   why="The national share runs 6, 9, 13 and 11 percent, so it rises three times and then falls by 2 points. The state and local share is the complement and moves in the opposite direction throughout."),

 dict(q=_FUNDING + " Which statement in the course framework does this table most directly concern?",
   table=_FUNDING_TABLE,
   choices=[
     "EK 4.10.B.1's claim about policy trends concerning the level of government involvement in social issues",
     "EK 4.10.A.3's account of the libertarian position",
     "EK 4.9.B.2's account of monetary policy",
     "EK 4.5.A.1's four types of scientific poll",
     "EK 4.2.A.1's contributors to political socialization"], ans=0,
   why="The table records how the level of government involvement in one social policy area changed over four periods, which is EK 4.10.B.1's subject. The other statements concern an ideological position, monetary policy, polling, and socialization."),

 dict(q=_FUNDING + " A student concludes from this table which perspective succeeded within the political parties during these periods. What is the most important limitation?",
   table=_FUNDING_TABLE,
   choices=[
     "The table records the trend but reports nothing about parties, so it cannot identify what produced the movement it shows",
     "The table does not report the national share",
     "The table reports only one period",
     "The table shows no change across the periods",
     "The table reports parties but not funding"], ans=0,
   why="EK 4.10.B.1 says trends reflect the success of perspectives within political parties, and this table has two columns, neither of which measures a party. A trend is consistent with the framework's explanation without being evidence for it."),

 dict(q=_LEVELS + " Which conclusion is best supported by the data?",
   table=_LEVELS_TABLE,
   choices=[
     "Primary national responsibility leads on two of the four issues and primary state responsibility on the other two",
     "Primary national responsibility leads on all four issues",
     "Primary state responsibility leads on all four issues",
     "The third option is the most popular on at least one issue",
     "The four issues produce nearly identical distributions"], ans=0,
   why="National responsibility leads on public health at 48 and environmental protection at 57, while state responsibility leads on education at 58 and public safety at 62. The third column never rises above 13 percent."),

 dict(q=_LEVELS + " The three response columns correspond most closely to which set of statements in the course framework?",
   table=_LEVELS_TABLE,
   choices=[
     "EK 4.10.A.1, EK 4.10.A.2 and EK 4.10.A.3, which describe the liberal, conservative and libertarian positions on the role of government in social issues",
     "EK 4.9.A.1's three positions on regulation of the marketplace",
     "EK 4.5.A.1's four types of scientific poll",
     "EK 4.1.A.1's four core values",
     "EK 4.3.A.1's two effects on ideology"], ans=0,
   why="The columns offer primary national responsibility, primary state responsibility, and little involvement at either level, which are the three arrangements EK 4.10.A.1 to 3 describe. EK 4.9.A.1's three positions concern the marketplace rather than the national and state division."),

 dict(q=_LEVELS + " A student describes the third column as respondents who have no view on the issue. What is the most important correction?",
   table=_LEVELS_TABLE,
   choices=[
     "Favoring little involvement at either level is a position the framework describes, not an absence of one, since EK 4.10.A.3 states it with two named exceptions",
     "The third column reports no respondents on any issue",
     "The third column is the largest on every issue",
     "The table offers only two response options",
     "The table covers a single issue, so no comparison is possible"], ans=0,
   why="EK 4.10.A.3 describes favoring little national or state involvement, except to protect private property or individual liberty, as an ideological position in its own right. The column runs between 11 and 13 percent on every issue, which is a consistent minority holding a stated view rather than an absence of one."),
]
