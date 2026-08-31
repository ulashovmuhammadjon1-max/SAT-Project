# AP U.S. GOVERNMENT AND POLITICS 5.1 Voting Rights and Models of Voting
# Behavior -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation (20 to 27 percent of the exam,
# the largest unit in the course).
# TWO learning objectives:
#   LO 5.1.A -- DESCRIBE the voting rights protections in the Constitution and in
#     legislation.
#   LO 5.1.B -- DESCRIBE different models of voting behavior.
# Suggested skill for this topic (CED p. 116): 1.D, concept application --
# describe political principles, institutions, processes, policies, and behaviors
# ILLUSTRATED IN DIFFERENT SCENARIOS IN CONTEXT.
#
# Essential knowledge relied on:
#   EK 5.1.A.1 -- "Expansion of opportunities for political participation are
#     found in the legal protections of the Amendments to the Constitution.
#       i.   The 14th Amendment granted CITIZENSHIP to all persons born or
#            naturalized in the U.S., including formerly enslaved people.
#       ii.  The 15th Amendment granted AFRICAN AMERICAN MEN the right to vote.
#       iii. The 17th Amendment changed the practice for electing SENATORS from a
#            vote by state legislatures to a DIRECT VOTE BY THE PEOPLE.
#       iv.  The 19th Amendment granted WOMEN the right to vote.
#       v.   The 24th Amendment eliminated POLL TAXES, a STRUCTURAL BARRIER to
#            voting.
#       vi.  The 26th Amendment lowered the VOTING AGE TO 18."
#   EK 5.1.B.1 -- "Various political models explain differences in voting
#     behavior.
#       i.   RATIONAL CHOICE voting refers to individuals who base their
#            decisions on what is perceived to be IN THEIR BEST INTEREST.
#       ii.  RETROSPECTIVE voting refers to individuals who decide whether the
#            party or candidate IN POWER should be REELECTED based on the RECENT
#            PAST.
#       iii. PROSPECTIVE voting refers to individuals who vote based on
#            PREDICTIONS of how a party or candidate WILL PERFORM IN THE FUTURE.
#       iv.  STRAIGHT TICKET voting refers to individuals who vote for ALL of the
#            candidates from ONE political party on a ballot."
#
# THE 14TH AMENDMENT IS THE ODD ONE IN ITS OWN LIST. Five of the six items grant
# or extend a vote; the 14th grants CITIZENSHIP. It belongs to a list about
# expanding participation because citizenship is the status the later
# protections attach to, but a student who reports it as having granted the vote
# has misstated the framework's own sentence. Item 3 makes the distinction the
# question and the verifier refuses the conflation.
#
# THE 24TH AMENDMENT IS DESCRIBED BY WHAT IT REMOVED, NOT WHOM IT ADDED. EK
# 5.1.A.1.v calls the poll tax a STRUCTURAL BARRIER -- the same term EK 5.2.A.1
# uses -- so this item is about clearing an obstacle rather than enfranchising a
# demographic. That is why the smallest row of the first table in this module is
# not the least important one, and item 27 says so.
#
# RETROSPECTIVE AND PROSPECTIVE ARE THE PAIR THAT SWAPS, and they swap because
# both concern performance. The framework separates them by TIME: retrospective
# looks at the RECENT PAST and asks whether those IN POWER should be REELECTED;
# prospective is a PREDICTION about the FUTURE. Items 13, 14 and 19 turn on it,
# the second table gives each its own row, and the verifier attributes a
# definition to the model named nearest before it so an item contrasting the two
# in one sentence is not reported.
#
# The CED attaches no foundational document and no required case to 5.1.A or
# 5.1.B. Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.1", "Voting Rights and Models of Voting Behavior", 5)

_EXPANSION = ("A hypothetical state records how many adults became eligible to vote after each "
              "of four changes in the law, against an adult population of 1700 thousand.")
_EXPANSION_TABLE = dict(
    headers=["Change in the law", "Adults newly eligible (thousands)",
             "Share of the adult population (%)"],
    rows=[["Extending the vote to women", "410", "24"],
          ["Extending the vote to African American men", "77", "5"],
          ["Eliminating poll taxes", "58", "3"],
          ["Lowering the voting age to 18", "96", "6"]])

_REASONS = ("A hypothetical exit poll asked voters which consideration mattered most in their "
            "choice. The table reports the share naming each and the model of voting behavior "
            "it illustrates.")
_REASONS_TABLE = dict(
    headers=["Consideration named as most important", "Share of voters (%)",
             "Model illustrated"],
    rows=[["What the officeholder has done over the past four years", "31", "Retrospective"],
          ["What the candidate promises to do if elected", "24", "Prospective"],
          ["Which outcome would leave the voter personally better off", "28", "Rational choice"],
          ["Supporting the whole slate of one party", "17", "Straight ticket"]])

QUESTIONS = [
 dict(q="According to the course framework, where are expansions of opportunities for political participation found?",
   choices=[
     "In the legal protections of the Amendments to the Constitution",
     "In the original text of Article I alone",
     "In executive orders issued by presidents",
     "In the rules of the two major political parties",
     "In treaties ratified by the Senate"], ans=0,
   why="EK 5.1.A.1's opening sentence locates these expansions in the legal protections of the amendments, and the six items that follow are all amendments. LO 5.1.A names legislation as well, but the essential knowledge statement itself lists amendments."),

 dict(q="According to the course framework, what did the 14th Amendment grant?",
   choices=[
     "Citizenship to all persons born or naturalized in the United States, including formerly enslaved people",
     "The right to vote to African American men",
     "The right to vote to women",
     "The direct election of senators",
     "The elimination of poll taxes"], ans=0,
   why="EK 5.1.A.1.i says the 14th Amendment granted citizenship, not the vote. Each of the other four options is the effect the framework attributes to a different amendment in the same list."),

 dict(q="Why is the 14th Amendment listed among expansions of political participation even though the framework describes it as granting citizenship rather than the vote?",
   choices=[
     "Because citizenship is the status the later voting protections attach to",
     "Because the framework treats citizenship and voting as the same thing",
     "Because the amendment also lowered the voting age",
     "Because the amendment eliminated poll taxes",
     "Because the amendment was ratified after the 15th"], ans=0,
   why="EK 5.1.A.1's list is introduced as expansions of opportunities for political participation, and the 15th, 19th, 24th and 26th all extend or protect voting by persons whose citizenship the 14th established. Reporting the 14th as having granted the vote misstates the framework's own sentence."),

 dict(q="According to the course framework, what did the 15th Amendment grant?",
   choices=[
     "The right to vote to African American men",
     "Citizenship to formerly enslaved people",
     "The right to vote to women",
     "The elimination of poll taxes",
     "The direct election of senators"], ans=0,
   why="EK 5.1.A.1.ii states this in exactly these words. The framework's phrase is African American MEN, which is why the 19th Amendment appears separately in the same list."),

 dict(q="According to the course framework, what did the 17th Amendment change?",
   choices=[
     "The practice for electing senators, from a vote by state legislatures to a direct vote by the people",
     "The practice for electing members of the House of Representatives",
     "The method of selecting presidential electors",
     "The voting age",
     "The use of poll taxes"], ans=0,
   why="EK 5.1.A.1.iii states this. It expands participation in a different way from the others: it does not add voters, it moves a decision from a legislature to the electorate."),

 dict(q="According to the course framework, what did the 19th Amendment grant?",
   choices=[
     "The right to vote to women",
     "Citizenship to all persons born in the United States",
     "The right to vote to African American men",
     "The elimination of poll taxes",
     "A lowered voting age"], ans=0,
   why="EK 5.1.A.1.iv states this directly. It appears separately from the 15th Amendment because the framework describes that amendment as granting the vote to African American men specifically."),

 dict(q="According to the course framework, what did the 24th Amendment eliminate, and how does the framework characterize it?",
   choices=[
     "Poll taxes, which it calls a structural barrier to voting",
     "Literacy tests, which it calls a demographic factor",
     "Residency requirements, which it calls a registration procedure",
     "Property requirements, which it calls a legal protection",
     "Voter identification requirements, which it calls an election type"], ans=0,
   why="EK 5.1.A.1.v names poll taxes and calls them a structural barrier to voting, which is the same term EK 5.2.A.1 uses for influences on turnout. The amendment is described by what it removed rather than by whom it added."),

 dict(q="According to the course framework, what did the 26th Amendment do?",
   choices=[
     "Lowered the voting age to 18",
     "Granted the vote to women",
     "Granted citizenship to formerly enslaved people",
     "Eliminated poll taxes",
     "Established direct election of senators"], ans=0,
   why="EK 5.1.A.1.vi states this. It is the last of the six items and the only one that changes an age threshold rather than a status, a barrier, or a method of election."),

 dict(q="Which of the six amendments in EK 5.1.A.1 expanded participation by changing WHO CHOOSES an officeholder rather than by changing who may vote?",
   choices=[
     "The 17th Amendment, which moved the election of senators from state legislatures to the people",
     "The 15th Amendment, which extended the vote to African American men",
     "The 19th Amendment, which extended the vote to women",
     "The 24th Amendment, which eliminated poll taxes",
     "The 26th Amendment, which lowered the voting age"], ans=0,
   why="EK 5.1.A.1.iii describes a change in the practice for electing senators rather than an addition to the electorate. The other four items either add voters or remove an obstacle facing them."),

 dict(q="According to the course framework, what does RATIONAL CHOICE voting refer to?",
   choices=[
     "Individuals who base their decisions on what is perceived to be in their best interest",
     "Individuals who decide whether those in power should be reelected based on the recent past",
     "Individuals who vote based on predictions of future performance",
     "Individuals who vote for all of one party's candidates on a ballot",
     "Individuals who do not vote at all"], ans=0,
   why="EK 5.1.B.1.i states this, and the framework's phrase is what is PERCEIVED to be in their best interest, which makes the model about the voter's own judgment rather than about an objective interest."),

 dict(q="According to the course framework, what does RETROSPECTIVE voting refer to?",
   choices=[
     "Individuals who decide whether the party or candidate in power should be reelected based on the recent past",
     "Individuals who vote based on predictions of how a candidate will perform in the future",
     "Individuals who base their decisions on their perceived best interest",
     "Individuals who vote for all of one party's candidates",
     "Individuals who vote only in presidential elections"], ans=0,
   why="EK 5.1.B.1.ii states this. Two elements are in the framework's own wording: the subject is the party or candidate IN POWER, and the evidence is the RECENT PAST."),

 dict(q="According to the course framework, what does PROSPECTIVE voting refer to?",
   choices=[
     "Individuals who vote based on predictions of how a party or candidate will perform in the future",
     "Individuals who decide whether those in power should be reelected based on the recent past",
     "Individuals who base their decisions on their perceived best interest",
     "Individuals who vote for all of one party's candidates",
     "Individuals who decide not to vote"], ans=0,
   why="EK 5.1.B.1.iii states this. Its evidence is a PREDICTION about the FUTURE, which is what distinguishes it from the retrospective model in the item before it."),

 dict(q="What distinguishes retrospective voting from prospective voting as the framework defines them?",
   choices=[
     "Retrospective voting judges a record from the recent past, while prospective voting rests on a prediction about future performance",
     "Retrospective voting concerns candidates and prospective voting concerns parties",
     "Retrospective voting occurs in midterm elections and prospective voting in presidential ones",
     "Retrospective voting is rational and prospective voting is not",
     "The two terms describe the same behavior"], ans=0,
   why="Both models concern performance, which is why they are confused, and EK 5.1.B.1 separates them by time direction alone. Both statements refer to a party or candidate, so the subject is not what distinguishes them."),

 dict(q="According to the course framework, what does STRAIGHT TICKET voting refer to?",
   choices=[
     "Individuals who vote for all of the candidates from one political party on a ballot",
     "Individuals who vote for candidates from more than one party on a ballot",
     "Individuals who vote only for the office at the top of the ballot",
     "Individuals who base their decisions on their perceived best interest",
     "Individuals who vote based on predictions of future performance"], ans=0,
   why="EK 5.1.B.1.iv states this, and the framework's word is ALL of the candidates from one party. It is the one model of the four defined by the pattern of the ballot rather than by the reasoning behind a choice."),

 dict(q="How does straight ticket voting differ in kind from the other three models EK 5.1.B.1 names?",
   choices=[
     "It describes the pattern of choices marked on a ballot, while the other three describe the reasoning behind a choice",
     "It applies only to presidential elections",
     "It is the only model that concerns political parties",
     "It is the only model the framework endorses",
     "It applies only to voters who are registered with a party"], ans=0,
   why="Rational choice, retrospective and prospective voting are each defined by what the voter is reasoning from, while EK 5.1.B.1.iv is defined by the marks on the ballot. A straight ticket voter could arrive there by any of the other three routes."),

 dict(q="A voter examines the past four years of an incumbent's record and decides the incumbent should not be returned to office. Which model does this illustrate?",
   choices=[
     "Retrospective voting, since the decision turns on the recent past record of the party or candidate in power",
     "Prospective voting, since the voter is deciding about a future term",
     "Rational choice voting, since the voter considered the decision carefully",
     "Straight ticket voting, since the voter opposed one party",
     "None of the four, since the voter chose against a candidate"], ans=0,
   why="EK 5.1.B.1.ii's two elements are both present: the subject is the officeholder in power and the evidence is the recent past. Every vote concerns a future term, so that feature does not make a vote prospective."),

 dict(q="A voter reads two candidates' proposals and votes for the one whose plans seem likely to work better if enacted. Which model does this illustrate?",
   choices=[
     "Prospective voting, since the decision rests on a prediction of future performance",
     "Retrospective voting, since the voter considered the candidates' records",
     "Rational choice voting, since the voter read the proposals",
     "Straight ticket voting, since the voter chose one candidate",
     "None of the four, since proposals are not performance"], ans=0,
   why="EK 5.1.B.1.iii defines prospective voting by a prediction of how a party or candidate will perform in the future, and judging plans not yet enacted is exactly such a prediction. Nothing in the scenario refers to a record already established."),

 dict(q="A voter concludes that one candidate's programs would leave the voter's own household better off and votes accordingly. Which model does this illustrate?",
   choices=[
     "Rational choice voting, since the decision rests on what the voter perceives to be in their best interest",
     "Retrospective voting, since the voter weighed programs",
     "Prospective voting, since the programs have not yet taken effect",
     "Straight ticket voting, since the voter chose one candidate",
     "None of the four, since household finances are not political"], ans=0,
   why="EK 5.1.B.1.i defines rational choice voting by the voter's perceived best interest, and the scenario names exactly that consideration. A prediction is involved, but the framework's distinguishing feature here is whose interest is being served rather than the tense."),

 dict(q="A voter marks every candidate from one party on a long ballot, having thought about only the race at the top. Which model does this illustrate?",
   choices=[
     "Straight ticket voting, since the voter chose all of one party's candidates on the ballot",
     "Rational choice voting, since the voter thought about the top race",
     "Retrospective voting, since the party held office previously",
     "Prospective voting, since the down-ballot officeholders have not yet served",
     "None of the four, since the voter considered only one race"], ans=0,
   why="EK 5.1.B.1.iv is defined by the pattern of the ballot, and every candidate from one party is that pattern regardless of how much thought went into it. The model describes what was marked rather than the reasoning behind it."),

 dict(q="Two analysts describe the same voter, one as a rational choice voter and one as a prospective voter. Can both be right, under the framework's definitions?",
   choices=[
     "Yes, because the two models pick out different features of a decision and nothing in the framework makes them exclusive",
     "No, because the framework says a voter fits exactly one model",
     "No, because rational choice voting is not a model in the framework",
     "Yes, but only if the voter votes in more than one election",
     "No, because prospective voting concerns parties rather than candidates"], ans=0,
   why="EK 5.1.B.1 says various political models EXPLAIN differences in voting behavior and does not assign each voter to one. A voter predicting future performance in order to serve a perceived interest satisfies both EK 5.1.B.1.i and EK 5.1.B.1.iii."),

 dict(q="Which of the following does EK 5.1.B.1 NOT state?",
   choices=[
     "Which of the four models describes the largest share of voters",
     "That rational choice voting rests on a perceived best interest",
     "That retrospective voting rests on the recent past",
     "That prospective voting rests on a prediction about the future",
     "That straight ticket voting means voting for all of one party's candidates"], ans=0,
   why="EK 5.1.B.1 defines four models and ranks none of them by prevalence. Every other option restates one of its four items."),

 dict(q="A state removes a requirement that had prevented some eligible adults from casting a ballot. Which item in EK 5.1.A.1 does this most closely resemble in kind?",
   choices=[
     "The 24th Amendment, which eliminated poll taxes, a structural barrier to voting",
     "The 15th Amendment, which extended the vote to African American men",
     "The 19th Amendment, which extended the vote to women",
     "The 17th Amendment, which changed how senators are elected",
     "The 14th Amendment, which granted citizenship"], ans=0,
   why="EK 5.1.A.1.v is the item in the list that removes an obstacle facing people who were otherwise eligible, rather than extending eligibility to a group that lacked it. The framework's own term for what was removed is a structural barrier."),

 dict(q="How do LO 5.1.A and LO 5.1.B differ in what they ask about?",
   choices=[
     "The first asks about legal protections for voting and the second about why voters choose as they do",
     "The first concerns state law and the second federal law",
     "The first concerns elections and the second concerns parties",
     "The two ask the same question in different words",
     "Neither concerns voting"], ans=0,
   why="LO 5.1.A is about protections in the Constitution and in legislation, described by EK 5.1.A.1's six amendments, while LO 5.1.B is about models of voting behavior, described by EK 5.1.B.1's four models. The topic joins who may vote to how voters decide."),

 dict(q="Why does the course framework treat the models in EK 5.1.B.1 as MODELS rather than as rules?",
   choices=[
     "Because each explains a pattern in voting behavior rather than predicting what any particular voter will do",
     "Because none of them has ever been observed",
     "Because each applies only to a single election",
     "Because the framework rejects all four",
     "Because voters are required by law to follow one of them"], ans=0,
   why="EK 5.1.B.1's own sentence is that various political models EXPLAIN DIFFERENCES in voting behavior. A model that explains differences accounts for variation across voters rather than dictating any one voter's choice."),

 dict(q=_EXPANSION + " Which conclusion is best supported by the data?",
   table=_EXPANSION_TABLE,
   choices=[
     "Extending the vote to women added far more newly eligible adults than any other change listed, more than four times the next largest",
     "The four changes added similar numbers of newly eligible adults",
     "Eliminating poll taxes added the most newly eligible adults",
     "Lowering the voting age added more newly eligible adults than extending the vote to women",
     "No change added more than a tenth of the adult population"], ans=0,
   why="The counts are 410, 77, 58 and 96 thousand, so extending the vote to women is more than four times the next largest at 96. That row is also 24 percent of the adult population, well above a tenth."),

 dict(q=_EXPANSION + " Which amendment in EK 5.1.A.1 corresponds to the largest row of this table?",
   table=_EXPANSION_TABLE,
   choices=[
     "The 19th Amendment",
     "The 15th Amendment",
     "The 24th Amendment",
     "The 26th Amendment",
     "The 17th Amendment"], ans=0,
   why="EK 5.1.A.1.iv attributes extending the vote to women to the 19th Amendment, and that row reports 410 thousand newly eligible adults, the largest in the table. The 17th Amendment appears in no row because it added no voters."),

 dict(q=_EXPANSION + " A student concludes from the smallest row that eliminating poll taxes was the least significant of the four changes. What is the most important qualification?",
   table=_EXPANSION_TABLE,
   choices=[
     "That row removed a structural barrier facing people who were already eligible, so counting newly eligible adults measures something different from what it accomplished",
     "That row reports the largest number in the table",
     "The table does not report a figure for that row",
     "Eliminating poll taxes added more adults than extending the vote to women",
     "The table covers a single change, so no comparison is possible"], ans=0,
   why="EK 5.1.A.1.v describes the poll tax as a structural barrier, so the 24th Amendment cleared an obstacle rather than enfranchising a new group. A count of newly eligible adults is the wrong measure for a change of that kind, even though the figure of 58 thousand is real."),

 dict(q=_REASONS + " Which conclusion is best supported by the data?",
   table=_REASONS_TABLE,
   choices=[
     "The consideration illustrating retrospective voting was named most often, and the one illustrating straight ticket voting least often",
     "The consideration illustrating prospective voting was named most often",
     "The four considerations were named by equal shares of voters",
     "A majority of voters named a single consideration",
     "The consideration illustrating rational choice voting was named least often"], ans=0,
   why="The shares are 31, 24, 28 and 17 percent, so the retrospective row leads and the straight ticket row trails. No single consideration reaches half, and the rational choice row at 28 is second rather than last."),

 dict(q=_REASONS + " Why does the first row of the table illustrate retrospective rather than prospective voting?",
   table=_REASONS_TABLE,
   choices=[
     "Because the consideration named is what an officeholder has already done, which is the recent past rather than a prediction",
     "Because the consideration named concerns a party rather than a candidate",
     "Because the voter is choosing in a midterm election",
     "Because retrospective voting is the more common model",
     "Because the framework defines retrospective voting by the size of the vote share"], ans=0,
   why="EK 5.1.B.1.ii defines retrospective voting by a judgment on the recent past of the party or candidate in power, and a record of what has already been done is exactly that. EK 5.1.B.1.iii would require a prediction about future performance instead."),

 dict(q=_REASONS + " A student argues that the first two rows describe the same model, since both concern how well someone performs in office. What is the most important correction?",
   table=_REASONS_TABLE,
   choices=[
     "The framework separates the two by time: one judges a record already established and the other predicts performance not yet observed",
     "The framework treats the two rows as the same model",
     "The two rows report identical shares of voters",
     "The first row concerns parties and the second concerns candidates",
     "Neither row corresponds to a model in the framework"], ans=0,
   why="Both models concern performance, which is why they are confused, and EK 5.1.B.1 distinguishes them by time direction alone. The two rows also report different shares, 31 and 24 percent, so the table treats them as distinct."),
]
