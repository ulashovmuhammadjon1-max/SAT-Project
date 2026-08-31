# AP U.S. GOVERNMENT AND POLITICS 4.1 American Attitudes About Government and
# Politics -- 30 questions
# CED V.1 (c) 2026, Unit 4 American Political Ideologies and Beliefs.
# Learning objective 4.1.A: explain the RELATIONSHIP between CORE VALUES of U.S.
# citizens and ATTITUDES ABOUT THE ROLE OF GOVERNMENT.
# Suggested skill for this topic (CED p. 102): 1.D, concept application --
# describe political principles, institutions, processes, policies, and
# behaviors ILLUSTRATED IN different scenarios in context.
#
# Essential knowledge relied on. One statement, and every word of its
# parentheses is content:
#   EK 4.1.A.1 -- "DIFFERENT INTERPRETATIONS of core values affect the
#     relationship BETWEEN CITIZENS, as well as BETWEEN CITIZENS AND THE FEDERAL
#     GOVERNMENT. SOME of these core values INCLUDE:
#       i.   INDIVIDUALISM (each person has the ability to shape their life and
#            destiny through the choices they make)
#       ii.  EQUALITY OF OPPORTUNITY (all people are given an equal chance to
#            compete)
#       iii. FREE ENTERPRISE (pursuit of self-interest, competition, efficient
#            allocation of resources, and limited government regulation of the
#            market, as espoused by ADAM SMITH in writings such as THE WEALTH OF
#            NATIONS)
#       iv.  RULE OF LAW (every person, EVEN THOSE IN POWER, must follow and is
#            accountable to the same laws that govern all)"
#
# THE SENTENCE'S SUBJECT IS INTERPRETATIONS, NOT VALUES. This is the whole
# topic, and it is what a definition-recall bank would miss. EK 4.1.A.1 does not
# say core values produce attitudes about government; it says DIFFERENT
# INTERPRETATIONS of them do. So a near-universal endorsement of a value is
# perfectly consistent with sharp disagreement about what government should do
# in its name, and both tables in this module are built to show exactly that.
# Items 9 to 13 and 25 to 30 turn on it.
#
# EQUALITY OF OPPORTUNITY IS NOT EQUALITY OF OUTCOME. The framework's own gloss
# is "all people are given an EQUAL CHANCE TO COMPETE", which is a statement
# about the starting line. Substituting outcomes is the single most common error
# on this value and it is a different political position, so the verifier
# refuses any key that makes the substitution.
#
# THE LIST IS ILLUSTRATIVE. "SOME of these core values INCLUDE" -- four are
# named and the framework does not claim they are all of them. Item 8 makes that
# the question; no key anywhere treats the four as exhaustive.
#
# RULE OF LAW'S PARENTHESIS CONTAINS ITS POINT: "even those in power". A gloss
# that says only "everyone must obey the law" drops the clause that makes the
# value do any work, since a regime in which the rulers are exempt also has
# everyone else obeying the law.
#
# Documents the CED attaches to 4.1.A (p. 27): Adam Smith, "The Wealth of
# Nations". The framework names it inside the free enterprise parenthesis, which
# is why items 14 to 17 quote it.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: "The Wealth of Nations" is quoted
# verbatim. Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("4.1", "American Attitudes About Government and Politics", 4)

_ENDORSE = ("A hypothetical national survey asked respondents whether they endorse each of four "
            "core values, and then whether they would support a new federal program justified "
            "in that value's name.")
_ENDORSE_TABLE = dict(
    headers=["Core value", "Endorse the value (%)", "Support a federal program in its name (%)"],
    rows=[["Individualism", "89", "34"],
          ["Equality of opportunity", "93", "61"],
          ["Free enterprise", "78", "27"],
          ["Rule of law", "95", "52"]])

_READINGS = ("A hypothetical survey asked respondents what they take the value of equality of "
             "opportunity to require of government. The table reports the share of each group "
             "agreeing with each statement.")
_READINGS_TABLE = dict(
    headers=["What the value is taken to require", "Self-described liberals (%)",
             "Self-described conservatives (%)"],
    rows=[["Removing formal legal barriers to competition", "84", "91"],
          ["Public funding to equalize schooling before the competition begins", "76", "38"],
          ["Guaranteeing similar outcomes regardless of the competition", "22", "9"],
          ["Government stepping back from the market entirely", "14", "47"]])

QUESTIONS = [
 dict(q="According to the course framework, what affects the relationship between citizens and the federal government?",
   choices=[
     "Different interpretations of core values",
     "Agreement on a single interpretation of each core value",
     "The absence of any shared values",
     "The number of federal agencies in operation",
     "The length of a president's term"], ans=0,
   why="EK 4.1.A.1's grammatical subject is 'different interpretations of core values', not the values themselves. The claim is that a shared value read two ways produces two different views of what government should do."),

 dict(q="EK 4.1.A.1 says different interpretations of core values affect two relationships. What are they?",
   choices=[
     "The relationship between citizens, and the relationship between citizens and the federal government",
     "The relationship between the states and the relationship between the branches",
     "The relationship between Congress and the courts",
     "The relationship between political parties and interest groups",
     "The relationship between the United States and foreign governments"], ans=0,
   why="EK 4.1.A.1 names both: 'the relationship between citizens, as well as between citizens and the federal government.' The first is a claim about how citizens regard one another, which is easy to overlook next to the second."),

 dict(q="According to the framework's own gloss, what does INDIVIDUALISM hold?",
   choices=[
     "That each person has the ability to shape their life and destiny through the choices they make",
     "That each person must be given an identical share of the nation's wealth",
     "That government should provide for each person's needs directly",
     "That each person owes primary loyalty to a local community",
     "That each person should be free from all legal obligation"], ans=0,
   why="EK 4.1.A.1.i defines individualism in exactly these words. The framework's gloss is about a person's capacity to shape a life through choices, which is why it is a value about agency rather than about entitlement or exemption."),

 dict(q="According to the framework's own gloss, what does EQUALITY OF OPPORTUNITY hold?",
   choices=[
     "That all people are given an equal chance to compete",
     "That all people end up with similar results",
     "That all people receive an identical income",
     "That competition should be eliminated",
     "That government should assign each person an occupation"], ans=0,
   why="EK 4.1.A.1.ii's gloss is 'all people are given an equal chance to compete', which is a statement about the starting line rather than the finish. Substituting an equality of results describes a different political position from the one the framework names."),

 dict(q="A student defines equality of opportunity as the principle that everyone should end up in a similar position. What is the correction the course framework supports?",
   choices=[
     "The framework's gloss is an equal chance to compete, which concerns the conditions of competition rather than its results",
     "The framework's gloss is an identical income for every person",
     "The framework does not define equality of opportunity",
     "The framework treats equality of opportunity as a synonym for individualism",
     "The framework treats equality of opportunity as a synonym for the rule of law"], ans=0,
   why="EK 4.1.A.1.ii says all people are given an equal chance to compete. A principle about chances and a principle about outcomes generate different policy conclusions from the same starting words, which is precisely the disagreement EK 4.1.A.1 is about."),

 dict(q="According to the framework's own gloss, which elements make up FREE ENTERPRISE?",
   choices=[
     "Pursuit of self-interest, competition, efficient allocation of resources, and limited government regulation of the market",
     "Public ownership of major industries",
     "Government direction of prices and wages",
     "Equal division of profits among all workers",
     "Elimination of competition among firms"], ans=0,
   why="EK 4.1.A.1.iii names all four elements, and the fourth is LIMITED government regulation rather than none, which distinguishes this core value from the libertarian position EK 4.9.A.1 describes separately."),

 dict(q="According to the framework's own gloss, what does the RULE OF LAW require?",
   choices=[
     "That every person, even those in power, must follow and is accountable to the same laws that govern all",
     "That every law be approved by a majority in a referendum",
     "That courts rather than legislatures write the laws",
     "That laws be changed only by constitutional amendment",
     "That every person be permitted to choose which laws to obey"], ans=0,
   why="EK 4.1.A.1.iv includes the clause EVEN THOSE IN POWER, which is where the value does its work. A regime whose rulers are exempt also has everyone else obeying the law, so a gloss without that clause describes nothing distinctive."),

 dict(q="EK 4.1.A.1 introduces its four values with the phrase SOME of these core values INCLUDE. What does that wording indicate?",
   choices=[
     "That the four named values are examples rather than a complete list",
     "That only these four values exist in American political culture",
     "That the four values are ranked in order of importance",
     "That the four values are held by only some citizens",
     "That the framework rejects the four values it names"], ans=0,
   why="The words SOME and INCLUDE both mark the list as illustrative. A question that treated the four as exhaustive would be asserting a completeness the framework declines to claim."),

 dict(q="Two citizens both say they believe strongly in individualism. One favors a federal job training program and the other opposes it. How does EK 4.1.A.1 account for this?",
   choices=[
     "They interpret the same core value differently, and it is the interpretation rather than the value that shapes their attitude toward government",
     "One of them does not really hold the value",
     "The framework says core values never affect attitudes toward government",
     "The framework says individualism has only one possible interpretation",
     "The framework says such disagreements concern only state governments"], ans=0,
   why="EK 4.1.A.1's subject is DIFFERENT INTERPRETATIONS of core values. One citizen may read individualism as requiring that government not intervene and another as requiring that people be equipped to make real choices, and the framework treats both as interpretations of one value."),

 dict(q="Why does EK 4.1.A.1's focus on interpretations rather than on the values themselves matter for explaining American political disagreement?",
   choices=[
     "It explains how citizens who agree on a value can still disagree sharply about what government should do",
     "It explains why Americans hold no values in common",
     "It explains why every citizen reaches the same policy conclusion",
     "It explains why the federal government has no role in policy",
     "It explains why political disagreement is confined to elections"], ans=0,
   why="If the values themselves produced the attitudes, wide agreement on values would produce wide agreement on policy. The framework's sentence locates the variation in the interpretation, which is what allows consensus on a value to coexist with conflict over its application."),

 dict(q="A city debates whether to require a license for a new kind of small business. One side invokes free enterprise to oppose the requirement; the other invokes the rule of law to support applying the same standards to everyone. Which idea from EK 4.1.A.1 does the debate illustrate?",
   choices=[
     "That different core values, and different interpretations of them, can be invoked on opposite sides of the same policy question",
     "That only one of the two sides holds any core value",
     "That core values never appear in policy debates",
     "That the two values are identical in content",
     "That the federal government must resolve the dispute"], ans=0,
   why="EK 4.1.A.1 lists four values without ranking them, and both sides here are drawing on the framework's own list. The topic's objective is the relationship between core values and attitudes about the role of government, and that relationship runs in more than one direction."),

 dict(q="A citizen argues that a public official who broke a law should be prosecuted exactly as any other person would be. Which core value is the citizen invoking?",
   choices=[
     "The rule of law, because the framework's gloss covers even those in power",
     "Individualism, because the official made a choice",
     "Free enterprise, because prosecution affects the market",
     "Equality of opportunity, because the official had the same chance as others",
     "None of the four, because the framework's list concerns only economics"], ans=0,
   why="EK 4.1.A.1.iv's parenthesis is the point of the value: every person, EVEN THOSE IN POWER, must follow and is accountable to the same laws. The scenario is that clause applied."),

 dict(q="A citizen argues that a program removing a legal barrier to entering a licensed trade honors a core value. Which core value fits the argument most directly?",
   choices=[
     "Equality of opportunity, because the framework's gloss is an equal chance to compete",
     "Rule of law, because a licensing statute is a law",
     "Individualism, because trades are practiced by individuals",
     "Free enterprise, because the framework's gloss favors eliminating all government regulation",
     "None of the four, because licensing is a state matter"], ans=0,
   why="Removing a barrier to entry is an argument about the conditions under which people compete, which is EK 4.1.A.1.ii's gloss exactly. Free enterprise as the framework glosses it favors LIMITED regulation, not the elimination of all of it."),

 dict(q="Read the following excerpt.\n\n“It is not from the benevolence of the butcher, the brewer, or the baker, that we expect our dinner, but from their regard to their own interest.”\n—Adam Smith, The Wealth of Nations, 1776\n\nWhich element of the framework's gloss on free enterprise does this passage state?",
   choices=[
     "The pursuit of self-interest",
     "The efficient allocation of resources by a central authority",
     "The elimination of competition among sellers",
     "Government regulation of prices",
     "Equal division of profits among producers"], ans=0,
   why="EK 4.1.A.1.iii names the pursuit of self-interest first among free enterprise's elements and attributes the position to Adam Smith in The Wealth of Nations, which the CED lists as a document attached to 4.1.A."),

 dict(q="Read the following excerpt.\n\n“Every individual… intends only his own gain, and he is in this, as in many other cases, led by an invisible hand to promote an end which was no part of his intention.”\n—Adam Smith, The Wealth of Nations, 1776\n\nWhat does this passage claim about the relationship between individual motive and social result?",
   choices=[
     "That a result no one intended can follow from many people pursuing their own ends",
     "That individuals must intend the public good in order to produce it",
     "That individual gain and social benefit are always opposed",
     "That a central authority must direct individual action toward the public good",
     "That individuals cannot know their own interests"], ans=0,
   why="The passage separates the intention from the outcome, which is the argument behind EK 4.1.A.1.iii's pairing of the pursuit of self-interest with the efficient allocation of resources. The result is described as unintended rather than as directed."),

 dict(q="Why does the course framework name Adam Smith inside its gloss on free enterprise rather than in a separate statement?",
   choices=[
     "Because the framework identifies him as the source of the position the value describes",
     "Because he served in the United States government",
     "Because he wrote the Constitution's commerce provisions",
     "Because the framework treats his work as binding law",
     "Because he opposed the free enterprise position"], ans=0,
   why="EK 4.1.A.1.iii says free enterprise is 'as espoused by Adam Smith in writings such as The Wealth of Nations', which makes the text the framework's cited source for the value. The CED attaches the work to 4.1.A among its documents."),

 dict(q="A student cites The Wealth of Nations as legal authority for striking down a business regulation. What is the most important correction?",
   choices=[
     "The work is a source the framework cites for the content of a core value, not a provision of law a court applies",
     "The work has no connection to the course framework",
     "The work is part of the Constitution",
     "The work was written after the Constitution was ratified",
     "The work argues against free enterprise"], ans=0,
   why="EK 4.1.A.1.iii cites the work as the source of a position, and the framework's category for it is a core value rather than a rule of decision. Confusing a value's intellectual source with legal authority is the same error as citing the Gettysburg Address as a holding."),

 dict(q="How does the framework's gloss on free enterprise differ from a position of no government regulation at all?",
   choices=[
     "The framework's gloss names LIMITED government regulation of the market rather than none",
     "The framework's gloss names complete government control of the market",
     "The framework's gloss makes no mention of regulation",
     "The framework's gloss requires government ownership of firms",
     "The framework's gloss applies only outside the United States"], ans=0,
   why="EK 4.1.A.1.iii's fourth element is 'limited government regulation of the market'. EK 4.9.A.1 describes the position favoring little or no regulation separately, as libertarian, which is why the two are not the same value."),

 dict(q="Which pairing of a core value with the framework's own gloss is correct?",
   choices=[
     "Individualism, with the ability of each person to shape their life through the choices they make",
     "Equality of opportunity, with the guarantee that all people reach similar results",
     "Free enterprise, with the elimination of all competition",
     "Rule of law, with the exemption of officials from the laws they administer",
     "Individualism, with the requirement that government provide for each person's needs"], ans=0,
   why="EK 4.1.A.1.i's gloss is exactly this. Each of the other four pairings reverses or negates the framework's parenthesis, and the rule of law option reverses the clause EVEN THOSE IN POWER that gives the value its content."),

 dict(q="A commentator claims that because Americans overwhelmingly endorse the same core values, they should agree about the role of government. Which part of EK 4.1.A.1 is the commentator overlooking?",
   choices=[
     "That the framework locates the variation in different interpretations of those values rather than in the values themselves",
     "That the framework says Americans share no values",
     "That the framework names only one core value",
     "That the framework says core values have no bearing on government",
     "That the framework says agreement on values is impossible"], ans=0,
   why="EK 4.1.A.1's sentence begins with DIFFERENT INTERPRETATIONS, which is exactly what the commentator's inference skips. Shared endorsement of a value and shared conclusions about policy are different things."),

 dict(q="Which question would a political scientist studying LO 4.1.A be most likely to ask?",
   choices=[
     "How do citizens who share a value arrive at different views of what government should do about it?",
     "How many federal agencies were created in a given decade?",
     "How long does a Supreme Court case take to decide?",
     "How many members sit in the House of Representatives?",
     "Which state ratified the Constitution first?"], ans=0,
   why="LO 4.1.A is the relationship between core values and attitudes about the role of government, and EK 4.1.A.1 locates that relationship in interpretation. A research question that matches the objective has to be about the step from value to attitude."),

 dict(q="Two citizens both endorse the rule of law. One supports an investigation of a sitting official and the other calls it an improper attack on the officeholder. How does EK 4.1.A.1 describe what is happening?",
   choices=[
     "They interpret a shared value differently, which is what the framework says affects the relationship between citizens and the federal government",
     "One of them does not endorse the rule of law at all",
     "The framework says a shared value always produces a shared conclusion",
     "The framework says the rule of law has no application to officials",
     "The framework says such disputes are matters of free enterprise"], ans=0,
   why="EK 4.1.A.1's claim is about interpretations, and EK 4.1.A.1.iv's gloss explicitly covers those in power. The disagreement here is over what accountability requires in a particular case rather than over whether officials are accountable."),

 dict(q="EK 4.1.A.1 says interpretations of core values affect the relationship BETWEEN CITIZENS. What does that half of the sentence describe?",
   choices=[
     "How citizens regard and treat one another, not only how they regard government",
     "How the states regard one another",
     "How the branches of government check one another",
     "How political parties compete for office",
     "How the United States relates to other countries"], ans=0,
   why="The framework names two relationships and this is the first, which is easily lost next to the more familiar citizen and government relationship. A disagreement about what equality of opportunity requires is also a disagreement about what citizens owe each other."),

 dict(q="Which of the following best describes what LO 4.1.A asks a student to explain?",
   choices=[
     "How core values and attitudes about the role of government are connected",
     "The date on which each core value entered American political culture",
     "The number of citizens who hold each core value",
     "Which core value the Constitution declares supreme",
     "Which political party invented each core value"], ans=0,
   why="LO 4.1.A's own words are the relationship between core values of U.S. citizens and attitudes about the role of government. The framework supplies no dates, no counts, and no constitutional ranking of the values."),

 dict(q=_ENDORSE + " Which conclusion is best supported by the data?",
   table=_ENDORSE_TABLE,
   choices=[
     "Every value is endorsed by more than three-quarters of respondents, while support for a program in its name varies far more widely across the four values",
     "Endorsement of the values varies more widely than support for the programs",
     "No value is endorsed by a majority of respondents",
     "Support for a program in a value's name is identical across the four values",
     "Free enterprise is the most widely endorsed of the four values"], ans=0,
   why="Endorsement runs from 78 to 95, a range of 17 points, while program support runs from 27 to 61, a range of 34. Rule of law at 95 is the most endorsed, and free enterprise at 78 the least."),

 dict(q=_ENDORSE + " Which statement in the course framework does this pattern most directly illustrate?",
   table=_ENDORSE_TABLE,
   choices=[
     "That different interpretations of core values affect the relationship between citizens and the federal government",
     "That procedural due process requires non-arbitrary methods",
     "That civil rights are guaranteed to all persons",
     "That the government responds to social movements through court rulings and policies",
     "That the Supreme Court debate about affirmative action concerns the equal protection clause"], ans=0,
   why="EK 4.1.A.1 makes exactly this claim, and near-universal endorsement of values alongside widely varying support for federal programs in their names is the claim in observable form. The other four statements belong to Unit 3."),

 dict(q=_ENDORSE + " A student concludes from the table that Americans disagree fundamentally about the core values themselves. What is the most important correction?",
   table=_ENDORSE_TABLE,
   choices=[
     "Every value is endorsed by at least 78 percent of respondents, so the disagreement the table shows is about what government should do rather than about the values",
     "No value is endorsed by more than half of respondents",
     "The table reports endorsement but not program support",
     "The four values are endorsed at identical rates",
     "The table covers a single respondent, so no share can be computed"], ans=0,
   why="The first column's lowest figure is 78 percent, which is agreement rather than disagreement, and the variation sits entirely in the second column. That gap between the columns is the framework's point about interpretation."),

 dict(q=_READINGS + " Which conclusion is best supported by the data?",
   table=_READINGS_TABLE,
   choices=[
     "The two groups agree most closely about removing formal legal barriers and differ most about public funding to equalize schooling",
     "The two groups differ most about removing formal legal barriers",
     "The two groups agree on every statement in the table",
     "A majority of both groups endorses guaranteeing similar outcomes",
     "A majority of both groups endorses government stepping back from the market entirely"], ans=0,
   why="The gaps between the two columns are 7, 38, 13 and 33 points respectively, so the narrowest is on removing formal barriers and the widest on public funding. Both groups reject the outcome guarantee, at 22 and 9 percent."),

 dict(q=_READINGS + " What does the third row of the table show about how both groups understand equality of opportunity?",
   table=_READINGS_TABLE,
   choices=[
     "Both groups reject the reading that the value guarantees similar outcomes, which matches the framework's gloss of an equal chance to compete",
     "Both groups accept the reading that the value guarantees similar outcomes",
     "Only one group rejects the outcome reading",
     "The table reports no figures for that row",
     "The row shows the widest disagreement in the table"], ans=0,
   why="The row reports 22 percent and 9 percent, so neither group comes close to a majority. EK 4.1.A.1.ii's gloss is an equal chance to compete, and the data show both groups reading the value that way rather than as a guarantee of results."),

 dict(q=_READINGS + " A student concludes from the table that the two groups hold different core values. What is the most important correction?",
   table=_READINGS_TABLE,
   choices=[
     "Both groups endorse the same value and reject the same reading of it; they differ about what it requires of government, which is what the framework calls a difference of interpretation",
     "The two groups agree about what the value requires of government",
     "Only one of the two groups was asked about the value",
     "The table shows the two groups differing on every statement by the same amount",
     "The table shows neither group endorsing the value in any form"], ans=0,
   why="Both columns are above 84 percent on removing formal barriers and below 25 percent on guaranteeing outcomes, so the value and its outer limits are shared. The divergence appears on the two rows about what government should therefore do, which is EK 4.1.A.1's subject exactly."),
]
