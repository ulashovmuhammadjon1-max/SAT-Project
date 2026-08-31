# AP U.S. GOVERNMENT AND POLITICS 4.9 Ideology and Economic Policy
# -- 30 questions
# CED V.1 (c) 2026, Unit 4 American Political Ideologies and Beliefs.
# TWO learning objectives, which is unusual in this unit:
#   LO 4.9.A -- explain how different political ideologies affect the ROLE OF
#     GOVERNMENT IN REGULATING THE MARKETPLACE.
#   LO 4.9.B -- explain how FISCAL AND MONETARY POLICY actions influence
#     economic conditions.
# Suggested skill for this topic (CED p. 110): 3.E, data analysis -- EXPLAIN
# POSSIBLE LIMITATIONS OF THE DATA PROVIDED.
#
# Essential knowledge relied on:
#   EK 4.9.A.1 -- "LIBERAL ideologies favor MORE governmental regulation of the
#     marketplace, CONSERVATIVE ideologies favor FEWER regulations, and
#     LIBERTARIAN ideologies favor LITTLE OR NO regulation of the marketplace
#     BEYOND THE PROTECTION OF PROPERTY RIGHTS AND VOLUNTARY TRADE."
#   EK 4.9.B.1 -- "FISCAL POLICY consists of actions taken by CONGRESS AND THE
#     PRESIDENT to influence economic conditions and includes KEYNESIAN AND
#     SUPPLY-SIDE positions."
#   EK 4.9.B.2 -- "MONETARY POLICY consists of actions taken by the FEDERAL
#     RESERVE (the Fed) to influence INTEREST RATES which affect broader economic
#     conditions. The Fed is an INDEPENDENT AGENCY which seeks to achieve MAXIMUM
#     EMPLOYMENT AND PRICE STABILITY."
#
# THE ACTOR IS WHAT SEPARATES FISCAL FROM MONETARY, and it is the classic
# reversal. The framework defines each policy by WHO TAKES THE ACTION -- Congress
# and the president for fiscal, the Federal Reserve for monetary -- before saying
# anything about instruments or effects. A student who has learned the two as
# "taxes and spending" against "interest rates" has the right examples and no
# rule for a case the examples do not cover. Items 9 to 13 and the second table
# turn on the actor, and the verifier refuses any key that swaps them.
#
# THE FED HAS THREE PROPERTIES IN ONE SENTENCE, and each is separately
# droppable: it is an INDEPENDENT agency, and it seeks MAXIMUM EMPLOYMENT and
# PRICE STABILITY -- two goals, not one. A summary that keeps only price
# stability describes a different institution from the one the framework
# describes. Items 14 to 16 carry all three.
#
# WHAT THIS MODULE WILL NOT DO: DEFINE KEYNESIAN AND SUPPLY-SIDE. EK 4.9.B.1
# NAMES both positions and defines NEITHER. Every textbook does define them, and
# supplying those definitions here would put content the framework does not
# state beside content it does, with the same authority and no way for a student
# to tell them apart -- the same refusal 3.13 makes about affirmative action
# outcomes and 3.12 about the separate but equal case. Item 17 makes the naming
# itself the question, and records honestly that the framework stops there.
# This is flagged rather than hidden: a teacher may well want to add the
# definitions, and they should know the bank did not get them from the CED.
#
# SKILL 3.E IS ABOUT WHAT DATA CANNOT SHOW, which is unusual and shapes all nine
# data items. Each table is followed by a limitation question: the interest rate
# table cannot establish the direction of causation, the action table cannot
# show whether an action worked, and the cross-country table cannot support a
# causal claim from one year and four countries that differ in every other way.
# Items 24, 27 and 30 are those three.
#
# NEITHER SIDE OF THE REGULATION DEBATE WINS HERE. EK 4.9.A.1 records three
# positions and no finding, so the cross-country table is built with NO
# consistent relationship between regulation and growth -- which is why item 30
# can ask what each side would cite without the module taking a side.
#
# Documents the CED attaches to 4.9.A and 4.9.B (p. 27): Adam Smith, "The Wealth
# of Nations", quoted verbatim in items 18 and 19.
# The CED's illustrative examples for this topic (positions on the inheritance
# tax and the minimum wage) are marked NOT REQUIRED and are not used.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("4.9", "Ideology and Economic Policy", 4)

_RATES = ("A hypothetical study reports, for four successive periods in one country, the central "
          "bank's target for a short term interest rate alongside two economic conditions.")
_RATES_TABLE = dict(
    headers=["Period", "Target interest rate (%)", "Unemployment rate (%)", "Inflation rate (%)"],
    rows=[["Period 1", "5.0", "4.1", "2.2"],
          ["Period 2", "2.5", "6.8", "1.4"],
          ["Period 3", "0.5", "8.9", "0.9"],
          ["Period 4", "3.0", "5.2", "2.8"]])

_ACTIONS = ("The table lists four hypothetical policy actions, the institution that took each, "
            "and how the course framework would classify it.")
_ACTIONS_TABLE = dict(
    headers=["Action taken", "Institution taking it", "Classification"],
    rows=[["Changed the target for a short term interest rate", "The Federal Reserve", "Monetary"],
          ["Enacted a change in tax rates", "Congress and the president", "Fiscal"],
          ["Enacted a change in federal spending levels", "Congress and the president", "Fiscal"],
          ["Changed the reserve requirement for banks", "The Federal Reserve", "Monetary"]])

_COUNTRIES = ("A hypothetical study reports, for four countries in a single year, the share of "
              "economic activity subject to government regulation alongside two economic "
              "conditions in that country that year.")
_COUNTRIES_TABLE = dict(
    headers=["Country", "Economic activity subject to regulation (%)", "Growth rate (%)",
             "Unemployment rate (%)"],
    rows=[["Country W", "18", "3.1", "5.2"],
          ["Country X", "31", "2.8", "4.9"],
          ["Country Y", "44", "3.4", "4.4"],
          ["Country Z", "57", "1.9", "7.1"]])

QUESTIONS = [
 dict(q="According to the course framework, what do LIBERAL ideologies favor regarding regulation of the marketplace?",
   choices=[
     "More governmental regulation of the marketplace",
     "Fewer regulations of the marketplace",
     "Little or no regulation beyond protecting property rights and voluntary trade",
     "Government ownership of all firms in the marketplace",
     "Regulation set by the Federal Reserve rather than by Congress"], ans=0,
   why="EK 4.9.A.1 states this directly. The framework's word is MORE, a comparative, so the position is defined relative to the other two rather than by a fixed amount of regulation."),

 dict(q="According to the course framework, what do CONSERVATIVE ideologies favor regarding regulation of the marketplace?",
   choices=[
     "Fewer regulations of the marketplace",
     "More governmental regulation of the marketplace",
     "Little or no regulation beyond protecting property rights and voluntary trade",
     "Government ownership of major industries",
     "Regulation of the marketplace by the courts"], ans=0,
   why="EK 4.9.A.1 assigns FEWER regulations to conservative ideologies. Fewer is a comparative and not an absence, which is the whole difference between this position and the libertarian one in the same sentence."),

 dict(q="According to the course framework, what do LIBERTARIAN ideologies favor regarding regulation of the marketplace?",
   choices=[
     "Little or no regulation beyond the protection of property rights and voluntary trade",
     "More governmental regulation of the marketplace",
     "Fewer regulations, but regulation of every industry",
     "Government ownership of the marketplace",
     "No protection of property rights of any kind"], ans=0,
   why="EK 4.9.A.1 states this, including the two exceptions. The libertarian position is not the absence of all government action, because the framework names protecting property rights and voluntary trade as things it does support."),

 dict(q="What is the difference between the conservative and libertarian positions as EK 4.9.A.1 states them?",
   choices=[
     "Conservative ideologies favor fewer regulations, while libertarian ideologies favor little or no regulation apart from two named exceptions",
     "Conservative ideologies favor no regulation and libertarian ideologies favor fewer",
     "The two positions are identical in the framework",
     "Conservative ideologies concern the marketplace and libertarian ideologies do not",
     "Libertarian ideologies favor more regulation than conservative ideologies"], ans=0,
   why="The framework's two phrases are FEWER regulations and LITTLE OR NO regulation, and the second carries the exceptions for property rights and voluntary trade. Treating the two as the same collapses a distinction the framework draws in one sentence."),

 dict(q="Why does EK 4.9.A.1 name two exceptions to the libertarian position rather than describing it as favoring no government action at all?",
   choices=[
     "Because protecting property rights and enforcing voluntary trade are themselves government functions the position supports",
     "Because the framework treats libertarian ideologies as favoring more regulation than conservative ones",
     "Because the exceptions apply only during economic downturns",
     "Because the exceptions were added by Congress",
     "Because property rights are not part of the marketplace"], ans=0,
   why="EK 4.9.A.1's phrase is 'beyond the protection of property rights and voluntary trade', which marks those as inside the position rather than outside it. A market requires enforceable ownership and enforceable agreements, so a position favoring markets is not a position favoring no government."),

 dict(q="A proposal would require firms in an industry to meet a new safety standard. Under EK 4.9.A.1, which position would be most likely to support it?",
   choices=[
     "The liberal position, since it favors more governmental regulation of the marketplace",
     "The conservative position, since it favors fewer regulations",
     "The libertarian position, since it favors little or no regulation",
     "None of the three, since the framework does not address safety",
     "All three equally, since safety is not an ideological question"], ans=0,
   why="EK 4.9.A.1 arranges the three positions by how much regulation of the marketplace each favors, and a new requirement on firms is more regulation. The framework's arrangement is what makes the prediction rather than any claim about safety in particular."),

 dict(q="EK 4.9.A.1 uses the comparatives MORE and FEWER rather than fixed quantities. What follows from that?",
   choices=[
     "The three positions are defined relative to one another rather than by any particular amount of regulation",
     "The three positions cannot be distinguished at all",
     "The positions apply only to newly created industries",
     "The framework specifies the exact number of regulations each favors",
     "The positions change automatically as the economy grows"], ans=0,
   why="A comparative needs something to compare against, and the framework supplies the other positions in the same sentence. This is why the ideologies can be ranked on the question without the framework naming any level of regulation as correct."),

 dict(q="Which of the following does EK 4.9.A.1 NOT state?",
   choices=[
     "Which of the three positions produces better economic outcomes",
     "That liberal ideologies favor more governmental regulation",
     "That conservative ideologies favor fewer regulations",
     "That libertarian ideologies favor little or no regulation beyond two exceptions",
     "That the three positions concern regulation of the marketplace"], ans=0,
   why="EK 4.9.A.1 describes three positions and evaluates none of them. Every other option restates part of its single sentence, and the framework's silence on outcomes is what keeps the statement descriptive."),

 dict(q="According to the course framework, who takes the actions that constitute FISCAL policy?",
   choices=[
     "Congress and the president",
     "The Federal Reserve",
     "The Supreme Court",
     "State legislatures",
     "The Department of the Treasury acting alone"], ans=0,
   why="EK 4.9.B.1 defines fiscal policy as actions taken by Congress and the president to influence economic conditions. The framework defines the policy by its actor before saying anything about instruments."),

 dict(q="According to the course framework, who takes the actions that constitute MONETARY policy?",
   choices=[
     "The Federal Reserve",
     "Congress and the president",
     "The Supreme Court",
     "The Department of Commerce",
     "State banking regulators"], ans=0,
   why="EK 4.9.B.2 defines monetary policy as actions taken by the Federal Reserve to influence interest rates which affect broader economic conditions. Actor first, instrument second."),

 dict(q="What is the most reliable way to tell whether a given action is fiscal or monetary policy, using the framework's definitions?",
   choices=[
     "Identify which institution took the action, since the framework defines each policy by its actor",
     "Identify whether the action concerned taxes or interest rates, since those are the only instruments",
     "Identify whether the action was intended to reduce unemployment",
     "Identify whether the action was taken during a recession",
     "Identify whether the action required a vote"], ans=0,
   why="EK 4.9.B.1 and EK 4.9.B.2 both begin with who takes the action, which gives a rule that covers cases the familiar examples do not. Learning the pair as taxes against interest rates supplies examples without supplying a criterion."),

 dict(q="A legislature passes and a president signs a change in federal spending intended to affect economic conditions. Under the course framework, this is",
   choices=[
     "fiscal policy, since it consists of actions taken by Congress and the president",
     "monetary policy, since it is intended to affect economic conditions",
     "monetary policy, since spending affects interest rates",
     "neither, since the framework covers only tax changes",
     "both, since the two categories overlap"], ans=0,
   why="EK 4.9.B.1's actor is Congress and the president, and both acted here. That an action aims at economic conditions does not make it monetary, because EK 4.9.B.2 assigns monetary policy to a different institution."),

 dict(q="The Federal Reserve changes the reserve requirement for banks. Under the course framework, this is",
   choices=[
     "monetary policy, since it is an action taken by the Federal Reserve",
     "fiscal policy, since it affects how much money circulates",
     "fiscal policy, since banks are regulated by Congress",
     "neither, since the framework mentions only interest rates",
     "both, since reserve requirements affect government revenue"], ans=0,
   why="EK 4.9.B.2 defines monetary policy by its actor, the Federal Reserve, so an action the Fed takes is monetary policy on the framework's own definition. The mention of interest rates describes what the Fed influences rather than exhausting what it may do."),

 dict(q="According to the course framework, what kind of agency is the Federal Reserve?",
   choices=[
     "An independent agency",
     "A committee of Congress",
     "A division of the Department of the Treasury",
     "A court established under Article III",
     "An office within the White House"], ans=0,
   why="EK 4.9.B.2 states that the Fed is an independent agency. Its independence is what distinguishes monetary policy from fiscal policy institutionally, since fiscal policy requires the elected branches to act."),

 dict(q="According to the course framework, what two things does the Federal Reserve seek to achieve?",
   choices=[
     "Maximum employment and price stability",
     "Price stability alone",
     "Maximum employment alone",
     "Balanced federal budgets and low taxes",
     "Economic growth and international competitiveness"], ans=0,
   why="EK 4.9.B.2 names both goals in one clause. A summary keeping only price stability describes a different institution from the one the framework describes, since two goals can point in different directions in a given situation."),

 dict(q="Why does it matter that the framework attributes TWO goals to the Federal Reserve rather than one?",
   choices=[
     "Because the two can point toward different actions at the same time, so the Fed's task involves weighing them against each other",
     "Because the two goals are always achieved together",
     "Because the second goal was added by Congress after the first",
     "Because the goals apply to fiscal policy rather than monetary policy",
     "Because the framework ranks the two in order of importance"], ans=0,
   why="EK 4.9.B.2 names maximum employment and price stability without ranking them, and a body pursuing two objectives may face situations in which they do not recommend the same course. The framework's silence on which comes first is part of what it says."),

 dict(q="EK 4.9.B.1 says fiscal policy includes Keynesian and supply-side positions. What does the course framework say about what those positions hold?",
   choices=[
     "It names them without defining either, so their content is not stated in the essential knowledge",
     "It defines both in detail in the same statement",
     "It defines the Keynesian position only",
     "It defines the supply-side position only",
     "It states that the two positions are identical"], ans=0,
   why="EK 4.9.B.1's sentence names the two positions and stops, so a definition of either would come from outside the framework's own statement. Noticing where the framework ends is part of reading it accurately."),

 dict(q="Read the following excerpt.\n\n“It is not from the benevolence of the butcher, the brewer, or the baker, that we expect our dinner, but from their regard to their own interest.”\n—Adam Smith, The Wealth of Nations, 1776\n\nWhich of the three positions in EK 4.9.A.1 does this reasoning most directly support?",
   choices=[
     "The libertarian position, since the passage argues that self-interest rather than direction produces the desired result",
     "The liberal position, since the passage concerns providing for people's needs",
     "The liberal position, since the passage mentions three trades",
     "None of the three, since the passage predates the United States",
     "All three equally, since each concerns the marketplace"], ans=0,
   why="The passage locates the source of provision in the participants' own interest rather than in any direction of them, which is the reasoning behind favoring little or no regulation. EK 4.1.A.1.iii attributes free enterprise to this work and the CED attaches it to 4.9."),

 dict(q="Read the following excerpt.\n\n“Every individual… intends only his own gain, and he is in this, as in many other cases, led by an invisible hand to promote an end which was no part of his intention.”\n—Adam Smith, The Wealth of Nations, 1776\n\nA student cites this passage as proof that government regulation of the marketplace is always harmful. What is the most important correction?",
   choices=[
     "The passage claims that unintended benefits can arise from self-interested action, which is not the same as a claim that regulation is always harmful",
     "The passage argues that government should regulate every market",
     "The passage has no bearing on economic policy",
     "The passage was written after the framework was published",
     "The passage states that individuals cannot know their own interests"], ans=0,
   why="The passage describes a mechanism and makes no claim about the effects of regulation, so the inference goes beyond it. EK 4.9.A.1 records three positions on regulation precisely because the question is contested rather than settled by any single argument."),

 dict(q="How do LO 4.9.A and LO 4.9.B differ in what they ask about?",
   choices=[
     "The first asks how ideologies affect the government's role in regulating the marketplace, and the second asks how fiscal and monetary actions influence economic conditions",
     "The first concerns the Federal Reserve and the second concerns Congress",
     "The first concerns economic conditions and the second concerns ideology",
     "The two ask the same question in different words",
     "Neither concerns the role of government"], ans=0,
   why="LO 4.9.A is about ideological positions on regulation and LO 4.9.B is about the mechanics of two kinds of policy action. The topic carries two objectives because it joins a question about beliefs to a question about institutions."),

 dict(q="The suggested skill for this topic asks students to explain possible LIMITATIONS of the data provided. Why is that skill a natural fit for economic data in particular?",
   choices=[
     "Because economic variables move together for many reasons, so a table showing an association rarely establishes which variable affected which",
     "Because economic data is always inaccurate",
     "Because economic data is never published quickly enough",
     "Because economic data concerns only the federal government",
     "Because economic data cannot be measured at all"], ans=0,
   why="Skill 3.E is about what data cannot show, and an association between two economic series is consistent with several explanations, including a third factor and reverse causation. The limitation is about inference from the data rather than about the data being wrong."),

 dict(q=_RATES + " Which statement best describes the data?",
   table=_RATES_TABLE,
   choices=[
     "Across the first three periods the target interest rate falls while unemployment rises, and in the fourth period both move in the opposite direction",
     "The target interest rate and unemployment rise together in every period",
     "The target interest rate is unchanged across the four periods",
     "Unemployment falls in every period",
     "Inflation is higher in every later period than in the one before"], ans=0,
   why="The target rate runs 5.0, 2.5, 0.5 and 3.0 while unemployment runs 4.1, 6.8, 8.9 and 5.2. The two move oppositely across the first three periods and both reverse in the fourth, and inflation falls before rising again."),

 dict(q=_RATES + " Which statement in the course framework does this table most directly concern?",
   table=_RATES_TABLE,
   choices=[
     "That monetary policy consists of actions taken by the Federal Reserve to influence interest rates which affect broader economic conditions",
     "That fiscal policy consists of actions taken by Congress and the president",
     "That liberal ideologies favor more governmental regulation of the marketplace",
     "That the Federal Reserve is a committee of Congress",
     "That conservative ideologies favor fewer regulations"], ans=0,
   why="The table pairs a target interest rate with unemployment and inflation, which are the interest rate and the broader economic conditions EK 4.9.B.2 names. Fiscal policy involves a different institution and does not appear in the table."),

 dict(q=_RATES + " What is the most important limitation of this data as evidence about the effects of monetary policy?",
   table=_RATES_TABLE,
   choices=[
     "The table shows the two series moving together but cannot show which one affected the other, or whether the central bank was responding to conditions rather than producing them",
     "The table does not report the target interest rate",
     "The table covers only one economic condition",
     "The table reports percentages rather than counts",
     "The table shows no relationship between the series at all"], ans=0,
   why="Skill 3.E asks for the limitations of the data provided, and an association between two series over four periods is consistent with influence running either way. A central bank that lowers rates because unemployment is rising would produce exactly this pattern without the rate change having caused anything."),

 dict(q=_ACTIONS + " Which conclusion is best supported by the table?",
   table=_ACTIONS_TABLE,
   choices=[
     "Every action taken by Congress and the president is classified as fiscal, and every action taken by the Federal Reserve as monetary",
     "The classification depends on whether the action concerned interest rates",
     "The classification depends on whether the action was intended to reduce unemployment",
     "Every action in the table is classified as fiscal",
     "Every action in the table is classified as monetary"], ans=0,
   why="The two Federal Reserve rows are both monetary and the two rows taken by Congress and the president are both fiscal, so the classification tracks the institution exactly. Two actions are fiscal and two are monetary."),

 dict(q=_ACTIONS + " Which pair of statements in the course framework does the pattern in this table reflect?",
   table=_ACTIONS_TABLE,
   choices=[
     "EK 4.9.B.1's assignment of fiscal policy to Congress and the president, and EK 4.9.B.2's assignment of monetary policy to the Federal Reserve",
     "EK 4.9.A.1's three ideological positions on regulation",
     "EK 4.1.A.1's four core values",
     "EK 4.8.A.2's balancing dynamic",
     "EK 4.5.A.1's four types of scientific poll"], ans=0,
   why="Both framework statements define their policy by the institution that acts, and the table's classification column follows the institution column exactly. The other statements concern ideology, values, and polling rather than the two policy categories."),

 dict(q=_ACTIONS + " What is the most important limitation of this table?",
   table=_ACTIONS_TABLE,
   choices=[
     "It records who took each action and how it is classified, but reports nothing about whether any action achieved what it was intended to achieve",
     "It does not identify the institution taking each action",
     "It classifies every action as monetary",
     "It reports economic conditions but not actions",
     "It covers a single action, so no comparison is possible"], ans=0,
   why="Skill 3.E asks what the data cannot show. Every column here concerns the action and its author, and none reports an outcome, so the table settles a classification question and leaves an effectiveness question untouched."),

 dict(q=_COUNTRIES + " Which statement best describes the data?",
   table=_COUNTRIES_TABLE,
   choices=[
     "The country with the highest growth rate is neither the least nor the most regulated of the four",
     "Growth falls steadily as the share of regulated activity rises",
     "Growth rises steadily as the share of regulated activity rises",
     "The least regulated country has the highest growth rate",
     "All four countries report the same growth rate"], ans=0,
   why="Regulation shares run 18, 31, 44 and 57 percent while growth runs 3.1, 2.8, 3.4 and 1.9. The highest growth belongs to the country at 44 percent, which is neither the lowest nor the highest regulation share, so neither steady pattern holds."),

 dict(q=_COUNTRIES + " Which of EK 4.9.A.1's three positions does this table support?",
   table=_COUNTRIES_TABLE,
   choices=[
     "None of them, since the table shows no consistent relationship between the share of regulated activity and either economic condition",
     "The liberal position, since the most regulated country appears in the table",
     "The conservative position, since the least regulated country has above average growth",
     "The libertarian position, since regulation appears in every country",
     "All three equally, since each concerns regulation"], ans=0,
   why="Growth does not rise or fall consistently with the regulation share, so a row can be found to fit almost any claim and the table as a whole fits none. EK 4.9.A.1 records three positions rather than a finding, which is what a table like this leaves intact."),

 dict(q=_COUNTRIES + " What is the most important limitation of this data as evidence about the effects of regulation?",
   table=_COUNTRIES_TABLE,
   choices=[
     "Four countries in a single year differ in many ways besides how much of their economic activity is regulated, so no effect of regulation can be separated out",
     "The table does not report growth rates",
     "The table reports too many countries to compare",
     "The table covers several years, which makes comparison impossible",
     "The table reports regulation but not unemployment"], ans=0,
   why="Skill 3.E asks for the limitations of the data provided, and countries differ in population, resources, institutions and history, any of which could account for the differences shown. A single year gives no way to observe what changed when regulation changed."),
]
