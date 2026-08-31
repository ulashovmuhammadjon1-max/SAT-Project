# AP U.S. GOVERNMENT AND POLITICS 4.7 Ideologies of Political Parties
# -- 30 questions
# CED V.1 (c) 2026, Unit 4 American Political Ideologies and Beliefs.
# Learning objective 4.7.A: explain how IDEOLOGIES OF THE TWO MAJOR PARTIES
# SHAPE POLICY DEBATES.
# Suggested skill for this topic (CED p. 108): 1.E, concept application --
# explain how political principles, institutions, processes, policies, and
# behaviors apply to different scenarios in context.
#
# Essential knowledge relied on. One sentence, and it is built out of hedges:
#   EK 4.7.A.1 -- "The Democratic Party (D or DEM) PLATFORMS GENERALLY ALIGN
#     MORE CLOSELY TO liberal ideological positions, and the Republican Party (R
#     or GOP) PLATFORMS GENERALLY ALIGN MORE CLOSELY TO conservative ideological
#     positions."
#
# THREE HEDGES, AND ALL THREE ARE DROPPABLE. This is the shortest statement in
# Unit 4 and the one where a careless paraphrase does the most damage, because
# what it turns into is a stereotype that a student will then apply to people:
#   PLATFORMS      The subject is a document a party adopts, not its voters and
#                  not its officeholders. "Democrats are liberal" is a claim
#                  about people that EK 4.7.A.1 does not make. The second table
#                  in this module exists to show individual variation and to
#                  make the point that such data neither confirms nor refutes a
#                  statement about platforms.
#   GENERALLY      Not always, and not every plank. The first table shows
#                  alignment rates between 59 and 88 percent, never 100.
#   ALIGN MORE CLOSELY TO
#                  A comparative, not an identity. A platform aligning more
#                  closely with a set of positions is not the same object as
#                  those positions, and the framework carefully declines to say
#                  the parties ARE the ideologies.
# Items 2 to 8 carry the three hedges and the verifier refuses their loss.
#
# THE IDEOLOGIES THEMSELVES ARE DEFINED ELSEWHERE IN THIS UNIT, and this module
# cites those statements rather than inventing content: EK 4.9.A.1 for the
# marketplace (liberal more regulation, conservative fewer, libertarian little
# or none beyond protecting property rights and voluntary trade) and EK
# 4.10.A.1 to 3 for social issues (liberal more national involvement,
# conservative less with more left to state governments, libertarian little
# national or state involvement except to protect private property or individual
# liberty). Nothing here attributes a position to a party that the framework
# does not attribute to an ideology.
#
# WHAT THIS MODULE REFUSES TO DO. It names no politician, no election, no piece
# of legislation and no contemporary controversy, and it takes no side. LO
# 4.7.A asks how party ideologies SHAPE POLICY DEBATES, which is a question
# about structure -- why debates recur along a predictable axis -- and not a
# question about who is right. The verifier enforces the refusal, because this
# is the topic in the whole bank where an author's own politics would be least
# visible to them and most visible to a student.
#
# Documents the CED attaches to 4.7.A (p. 27): Federalist No. 10. Items 15 to 19
# quote it verbatim; it is the framework's own source for why durable political
# divisions form at all.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("4.7", "Ideologies of Political Parties", 4)

_PLANKS = ("A hypothetical study coded every plank in the two major parties' most recent "
           "platforms, recording the share in each policy area that aligned with the "
           "ideological positions the course framework associates with that party.")
_PLANKS_TABLE = dict(
    headers=["Policy area", "Democratic platform planks aligning with liberal positions (%)",
             "Republican platform planks aligning with conservative positions (%)"],
    rows=[["Economic regulation", "81", "78"],
          ["Social policy", "76", "84"],
          ["Foreign policy", "62", "59"],
          ["Environmental policy", "88", "71"]])

_IDENTIFIERS = ("A hypothetical survey asked respondents about one policy question and recorded "
                "which position each held. The table groups respondents by the party they "
                "identify with.")
_IDENTIFIERS_TABLE = dict(
    headers=["Group", "Held the liberal position (%)", "Held the conservative position (%)",
             "Held neither position (%)"],
    rows=[["Democratic identifiers", "64", "21", "15"],
          ["Republican identifiers", "18", "69", "13"],
          ["Independents", "35", "38", "27"]])

QUESTIONS = [
 dict(q="According to the course framework, what do Democratic Party platforms generally align more closely to?",
   choices=[
     "Liberal ideological positions",
     "Conservative ideological positions",
     "Libertarian ideological positions",
     "No ideological positions at all",
     "Positions that vary randomly from year to year"], ans=0,
   why="EK 4.7.A.1 states this directly. The framework's subject is the party's PLATFORMS and its verb phrase is ALIGN MORE CLOSELY TO, which is a comparison rather than an identity."),

 dict(q="According to the course framework, what do Republican Party platforms generally align more closely to?",
   choices=[
     "Conservative ideological positions",
     "Liberal ideological positions",
     "Libertarian ideological positions",
     "No ideological positions at all",
     "Positions determined entirely by public opinion polling"], ans=0,
   why="EK 4.7.A.1 states this directly, using the same construction it uses for the other party. Both halves of the sentence are about platforms and both use the same hedges."),

 dict(q="What is the SUBJECT of EK 4.7.A.1's statement about the two parties?",
   choices=[
     "The parties' platforms",
     "The parties' voters",
     "The parties' members of Congress",
     "The parties' donors",
     "The parties' state organizations"], ans=0,
   why="EK 4.7.A.1's grammatical subject is 'The Democratic Party platforms' and 'the Republican Party platforms'. A platform is a document a party adopts, so the statement is about what parties commit to rather than about what any person believes."),

 dict(q="Why does it matter that EK 4.7.A.1 is a statement about platforms rather than about people?",
   choices=[
     "Because data about what individual voters believe neither confirms nor refutes a claim about what party platforms contain",
     "Because platforms have no relationship to what parties do",
     "Because voters are not permitted to disagree with a platform",
     "Because platforms are written by the federal government",
     "Because the framework says individual beliefs do not exist"], ans=0,
   why="EK 4.7.A.1's subject is the platforms, so a survey of individuals is measuring something else. Treating a statement about documents as a statement about persons is what turns the framework's careful sentence into a stereotype."),

 dict(q="EK 4.7.A.1 says platforms GENERALLY align with the relevant positions. What does that word indicate?",
   choices=[
     "That the alignment holds as a tendency rather than in every plank",
     "That the alignment holds in every plank without exception",
     "That the alignment holds only in presidential election years",
     "That the alignment has never actually been observed",
     "That the alignment is required by law"], ans=0,
   why="GENERALLY is a hedge, and the framework chose it in a sentence it could have written without one. A platform containing a plank that does not align is exactly what the word leaves room for."),

 dict(q="EK 4.7.A.1 says platforms align MORE CLOSELY TO a set of ideological positions. Why is that phrasing different from saying the platforms ARE those positions?",
   choices=[
     "Because it states a comparison of closeness rather than an identity, leaving the platform and the ideology as distinct things",
     "Because it means the platforms are unrelated to the ideologies",
     "Because it means the ideologies are written by the parties",
     "Because it means only one party has a platform",
     "Because it means the alignment changes every year"], ans=0,
   why="ALIGN MORE CLOSELY TO is comparative, and a comparison presupposes two distinct things being compared. The framework declines to say a party IS an ideology, which is the claim the phrasing was chosen to avoid."),

 dict(q="A student writes that according to the course framework, Democrats are liberals and Republicans are conservatives. Which correction does the framework support?",
   choices=[
     "The framework says the parties' platforms generally align more closely to those positions, which is a claim about documents and a tendency rather than about people and an identity",
     "The framework says the two parties have no ideological leanings",
     "The framework says the alignment runs the other way",
     "The framework says only one of the two parties has an ideology",
     "The framework says party platforms are identical"], ans=0,
   why="Three of the framework's own words are lost in the student's version: PLATFORMS, GENERALLY, and MORE CLOSELY. Each removal makes the sentence stronger and less accurate, and together they convert a description of documents into a claim about persons."),

 dict(q="Which of the following would be consistent with EK 4.7.A.1?",
   choices=[
     "A party platform containing several planks that do not align with the ideology the framework associates with that party",
     "A party platform that no member of the party has read",
     "A party platform written by the opposing party",
     "A party with no platform at all",
     "Two parties adopting identical platforms"], ans=0,
   why="EK 4.7.A.1's word GENERALLY leaves room for planks that do not align, which is what makes the first option consistent with it rather than a counterexample. The other options describe situations the framework's sentence does not address."),

 dict(q="According to the course framework's account of economic policy, what do LIBERAL ideologies favor regarding the marketplace?",
   choices=[
     "More governmental regulation of the marketplace",
     "Fewer regulations of the marketplace",
     "Little or no regulation beyond protecting property rights and voluntary trade",
     "Government ownership of all major industries",
     "Elimination of all taxation"], ans=0,
   why="EK 4.9.A.1 states that liberal ideologies favor more governmental regulation of the marketplace, conservative ideologies favor fewer regulations, and libertarian ideologies favor little or no regulation beyond the protection of property rights and voluntary trade."),

 dict(q="According to the course framework's account of economic policy, what do CONSERVATIVE ideologies favor regarding the marketplace?",
   choices=[
     "Fewer regulations of the marketplace",
     "More governmental regulation of the marketplace",
     "Government ownership of major industries",
     "Regulation of the marketplace by the courts rather than by Congress",
     "No marketplace at all"], ans=0,
   why="EK 4.9.A.1 assigns fewer regulations to conservative ideologies. The framework's word is FEWER, a comparative, which distinguishes the conservative position from the libertarian one it describes as favoring little or no regulation."),

 dict(q="How does the course framework distinguish the CONSERVATIVE position on marketplace regulation from the LIBERTARIAN one?",
   choices=[
     "Conservative ideologies favor fewer regulations, while libertarian ideologies favor little or no regulation beyond protecting property rights and voluntary trade",
     "Conservative ideologies favor more regulation and libertarian ideologies favor fewer",
     "The two positions are identical in the framework",
     "Conservative ideologies concern social issues and libertarian ideologies concern economic ones",
     "The framework does not describe a libertarian position"], ans=0,
   why="EK 4.9.A.1 names all three positions in one sentence, and the difference between the second and third is the difference between FEWER and LITTLE OR NO, with the libertarian position given two named exceptions."),

 dict(q="According to the course framework's account of social issues, what do LIBERAL ideologies generally favor?",
   choices=[
     "More national government involvement, with less responsibility left to state governments",
     "Less national government involvement, with more responsibility left to state governments",
     "Little national or state involvement of any kind",
     "Involvement only by local governments",
     "No government involvement in social issues at all"], ans=0,
   why="EK 4.10.A.1 states that liberal ideologies generally favor more national government involvement to address some social issues such as education and public health, with less responsibility left to state governments."),

 dict(q="According to the course framework's account of social issues, what do CONSERVATIVE ideologies generally favor?",
   choices=[
     "Less national government involvement, with more responsibility left to state governments",
     "More national government involvement, with less responsibility left to state governments",
     "Elimination of state governments",
     "Involvement only by the federal courts",
     "Identical involvement by national and state governments"], ans=0,
   why="EK 4.10.A.2 states this, and its structure mirrors EK 4.10.A.1 exactly: the same two variables, national involvement and state responsibility, moved in opposite directions."),

 dict(q="According to the course framework, what do LIBERTARIAN ideologies generally favor on social issues?",
   choices=[
     "Little national or state government involvement except when government is protecting private property or individual liberty",
     "More national involvement and less state involvement",
     "Less national involvement and more state involvement",
     "Equal involvement by national and state governments",
     "Involvement determined by public referendum"], ans=0,
   why="EK 4.10.A.3 states this, including the two exceptions. The libertarian position is not simply the conservative one taken further, because it applies to state governments as well as to the national one."),

 dict(q="Read the following excerpt.\n\n“A zeal for different opinions concerning religion, concerning government, and many other points, as well of speculation as of practice… have, in turn, divided mankind into parties, inflamed them with mutual animosity, and rendered them much more disposed to vex and oppress each other than to co-operate for their common good.”\n—James Madison, Federalist No. 10, 1787\n\nWhat does this passage claim about the origin of political parties?",
   choices=[
     "That differences of opinion on fundamental questions divide people into parties",
     "That parties are created by law and can be abolished by law",
     "That parties arise only where a government is badly designed",
     "That parties form only around economic questions",
     "That parties disappear once people cooperate"], ans=0,
   why="Madison's passage lists zeal for different opinions as one of the causes that have divided people into parties. The CED attaches Federalist No. 10 to 4.7.A, and this is the framework's own source for why durable political divisions form at all."),

 dict(q="Read the following excerpt.\n\n“The most common and durable source of factions has been the various and unequal distribution of property.”\n—James Madison, Federalist No. 10, 1787\n\nHow does this claim relate to the ideological positions the course framework describes?",
   choices=[
     "It identifies economic difference as a durable basis of political division, which is the axis EK 4.9.A.1 describes ideologies differing along",
     "It states that economic questions never divide people",
     "It states that property should be distributed equally",
     "It states that factions are created by government regulation",
     "It states that political divisions are temporary"], ans=0,
   why="EK 4.9.A.1 arranges liberal, conservative and libertarian ideologies along the question of how much government regulates the marketplace, and Madison names the distribution of property as the most durable source of division. The passage supplies a reason the economic axis recurs."),

 dict(q="Read the following excerpt.\n\n“The latent causes of faction are thus sown in the nature of man.”\n—James Madison, Federalist No. 10, 1787\n\nWhat follows from this claim for how political divisions should be handled?",
   choices=[
     "That they cannot be removed at their source, so a system must be designed to operate with them present",
     "That they will disappear once citizens are better educated",
     "That government should prohibit the formation of parties",
     "That divisions are the fault of particular politicians",
     "That divisions arise only in large countries"], ans=0,
   why="Madison locates the causes of faction in human nature rather than in a removable circumstance, which is why Federalist No. 10 turns to controlling the effects of faction rather than removing its causes. The CED attaches the essay to this topic."),

 dict(q="How does Federalist No. 10's account of faction relate to LO 4.7.A's concern with how party ideologies shape policy debates?",
   choices=[
     "It explains why durable divisions form at all, which is what makes recurring ideological debate a permanent feature rather than a passing condition",
     "It explains which party is correct on each policy question",
     "It explains how a platform is drafted",
     "It explains how many parties a country should have",
     "It has no bearing on the topic"], ans=0,
   why="LO 4.7.A asks how party ideologies shape policy debates, and Federalist No. 10 supplies the framework's own account of why political division is durable. The essay predicts recurring disagreement without predicting its content."),

 dict(q="A student cites Federalist No. 10 as evidence that one of the two major parties is closer to the founders' intentions. What is the most important correction?",
   choices=[
     "The essay concerns why factions form and how their effects may be controlled, and it names neither modern party nor any modern ideological position",
     "The essay explicitly endorses one of the two modern parties",
     "The essay has no connection to the course framework",
     "The essay was written after the parties were founded",
     "The essay argues that parties should be abolished"], ans=0,
   why="Federalist No. 10 dates from 1787 and its subject is faction in general, so it cannot name a modern party. Reading a founding document as an endorsement of a present-day position is the error, and the CED attaches the essay here for its account of division rather than for a verdict."),

 dict(q="LO 4.7.A asks how the ideologies of the two major parties SHAPE POLICY DEBATES. Which of the following best describes that shaping?",
   choices=[
     "Debates tend to recur along a predictable axis, because each party's platform commits it in advance to a general direction",
     "Debates are settled in advance by whichever party is larger",
     "Debates occur only on questions the platforms do not address",
     "Debates are conducted entirely by voters rather than by parties",
     "Debates have no relationship to party platforms"], ans=0,
   why="EK 4.7.A.1 associates each party's platform with a set of ideological positions, and EK 4.9.A.1 and EK 4.10.A.1 to 3 describe those positions as differing over how much government should do. A prior general commitment is what makes the same axis reappear across different issues."),

 dict(q="A legislature debates whether to add a new requirement to how a certain industry operates. Under the framework's account of ideologies, how would the debate most likely be structured?",
   choices=[
     "Around how much government should regulate the marketplace, since that is the axis EK 4.9.A.1 places the ideologies along",
     "Around whether the industry should exist at all",
     "Around which court should hear challenges to the requirement",
     "Around how many members the legislature has",
     "Around whether the Constitution should be amended"], ans=0,
   why="EK 4.9.A.1 arranges liberal, conservative and libertarian positions by how much regulation of the marketplace each favors, so a proposed regulation puts the parties' platforms on opposite sides of that axis. The scenario is an application of that arrangement."),

 dict(q="A legislature debates whether the national government or the states should take primary responsibility for a public health program. Under the framework's account of ideologies, how would the debate most likely be structured?",
   choices=[
     "Around how much involvement the national government should have and how much responsibility should be left to states, which is the axis EK 4.10.A.1 and EK 4.10.A.2 describe",
     "Around whether public health is a legitimate subject of any government action",
     "Around which political party is larger in the legislature",
     "Around whether the program should be funded by borrowing",
     "Around how long the debate should last"], ans=0,
   why="EK 4.10.A.1 and EK 4.10.A.2 describe liberal and conservative positions on social issues in exactly these terms, naming public health among the examples. The scenario places the question on the framework's own axis."),

 dict(q="Which of the following does EK 4.7.A.1 NOT state?",
   choices=[
     "Which of the two parties' positions is better for the country",
     "That Democratic Party platforms generally align more closely to liberal positions",
     "That Republican Party platforms generally align more closely to conservative positions",
     "That the alignment is a matter of platforms",
     "That the alignment holds generally rather than universally"], ans=0,
   why="EK 4.7.A.1 is descriptive throughout: it reports where each party's platforms sit relative to two sets of positions and makes no evaluation. Every other option restates part of the framework's single sentence."),

 dict(q="Why is EK 4.7.A.1 stated so cautiously, given that it is one of the shortest statements in the unit?",
   choices=[
     "Because a stronger version would assert something about individuals and about every plank that the framework is not claiming",
     "Because the framework is uncertain whether the parties exist",
     "Because the framework expects the alignment to reverse",
     "Because platforms are secret documents",
     "Because the framework treats all ideologies as identical"], ans=0,
   why="Each of the three hedges rules out a specific overstatement: PLATFORMS rules out a claim about people, GENERALLY rules out a claim about every plank, and MORE CLOSELY rules out an identity. The brevity of the sentence and its caution are not in tension."),

 dict(q=_PLANKS + " Which conclusion is best supported by the data?",
   table=_PLANKS_TABLE,
   choices=[
     "In every policy area both platforms align with the associated positions in a majority of planks, but in no area does either reach every plank",
     "Both platforms align in every plank in at least one policy area",
     "Neither platform aligns in a majority of planks in any area",
     "The two platforms align at identical rates in every area",
     "Alignment is highest for both platforms in the same policy area"], ans=0,
   why="The eight figures run from 59 to 88 percent, so all are above half and none reaches 100. The Democratic column peaks on environmental policy at 88 and the Republican column on social policy at 84, so the peaks fall in different areas."),

 dict(q=_PLANKS + " Which word in the course framework's statement do the figures in this table most directly support?",
   table=_PLANKS_TABLE,
   choices=[
     "GENERALLY, since alignment is high in every area but complete in none",
     "ALWAYS, since alignment is complete in every area",
     "NEVER, since alignment is absent in every area",
     "IDENTICAL, since the two columns match exactly",
     "RANDOM, since the figures show no pattern"], ans=0,
   why="EK 4.7.A.1 says platforms GENERALLY align more closely to the relevant positions, and a set of rates between 59 and 88 percent is a tendency rather than a rule. Nothing in the table reaches complete alignment or absence of it."),

 dict(q=_PLANKS + " A student concludes from this table that every plank in the Democratic platform takes a liberal position. What is the most important correction?",
   table=_PLANKS_TABLE,
   choices=[
     "The highest figure in that column is 88 percent, so at least some planks in every area do not align",
     "The table reports no figures for that platform",
     "Every figure in that column is below half",
     "The table reports only one policy area",
     "The table covers a single plank, so no share can be computed"], ans=0,
   why="The Democratic column reads 81, 76, 62 and 88, so the closest any area comes is 88 percent and the furthest is 62. EK 4.7.A.1's word GENERALLY is what accommodates the remainder, and a claim about every plank goes past both the data and the framework."),

 dict(q=_IDENTIFIERS + " Which conclusion is best supported by the data?",
   table=_IDENTIFIERS_TABLE,
   choices=[
     "A majority of each party's identifiers holds the position associated with that party, and in each case a substantial minority does not",
     "Every identifier of each party holds the position associated with that party",
     "No identifier of either party holds the position associated with that party",
     "Independents hold the liberal position more often than Democratic identifiers do",
     "The two parties' identifiers hold identical distributions of positions"], ans=0,
   why="Democratic identifiers split 64, 21 and 15 and Republican identifiers split 18, 69 and 13, so each has a clear majority and a minority of at least a third holding something else. Independents hold the liberal position at 35 percent, well below the Democratic figure."),

 dict(q=_IDENTIFIERS + " What is the most important limitation of this table as evidence about EK 4.7.A.1?",
   table=_IDENTIFIERS_TABLE,
   choices=[
     "EK 4.7.A.1 is a statement about party platforms, and this table measures what individuals believe",
     "The table does not report which party each respondent identifies with",
     "The table reports shares rather than counts",
     "EK 4.7.A.1 concerns only independents",
     "The table covers social issues, which the framework does not discuss"], ans=0,
   why="The framework's subject is the parties' platforms, which are documents, and a survey of identifiers measures persons. The two can vary independently, which is why data of this kind does not directly bear on the framework's sentence."),

 dict(q=_IDENTIFIERS + " A student argues that because 21 percent of Democratic identifiers hold the conservative position, the course framework's statement is wrong. What is the most important correction?",
   table=_IDENTIFIERS_TABLE,
   choices=[
     "EK 4.7.A.1 states an alignment of platforms, so figures about individual identifiers neither confirm nor refute it",
     "The framework states that every identifier holds the associated position",
     "The table shows no Democratic identifiers holding the conservative position",
     "The framework's statement concerns only Republican identifiers",
     "Twenty-one percent is a majority of that group"], ans=0,
   why="The student's figure is real and the inference is not, because the framework's claim and the table's measurement have different subjects. Refuting a statement about documents requires evidence about documents, which the first table in this topic supplies and this one does not."),
]
