# AP U.S. GOVERNMENT AND POLITICS 5.9 Congressional Elections -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# Learning objective 5.9.A: explain how THE DIFFERENT PROCESSES work in U.S.
# CONGRESSIONAL elections.
# Suggested skill for this topic (CED p. 116): 5.B, argumentation -- SUPPORT AN
# ARGUMENT OR CLAIM USING RELEVANT EVIDENCE.
#
# Essential knowledge relied on. One statement, four items, and it is the
# shortest in Unit 5:
#   EK 5.9.A.1 -- "The process and outcomes in U.S. congressional elections are
#     affected by:
#       i.   INCUMBENCY ADVANTAGE PHENOMENON
#       ii.  OPEN AND CLOSED PRIMARIES
#       iii. CAUCUSES
#       iv.  GENERAL (PRESIDENTIAL AND MIDTERM) ELECTIONS."
#
# THIS LIST IS EK 5.8.A.1'S LIST WITH TWO ITEMS REMOVED AND ONE CHANGED, and both
# differences are the content of the topic:
#   * PARTY CONVENTIONS and THE ELECTORAL COLLEGE are absent. They belong to
#     choosing a president and have no place in a congressional election, so a
#     module that carried them over would be describing the wrong contest.
#   * EK 5.8.A.1.v reads "General (presidential) elections"; EK 5.9.A.1.iv reads
#     "General (PRESIDENTIAL AND MIDTERM) elections". Congressional elections
#     happen in BOTH kinds of year, and that single added word is what connects
#     this topic to EK 5.2.A.2.iii's statement that turnout is higher in
#     presidential elections than in midterm elections. Items 9 to 14 and the
#     second table turn on it, and the verifier refuses a congressional list that
#     drops MIDTERM or admits a presidential-only process.
#
# WHY SO MANY ITEMS ASK WHICH EVIDENCE SUPPORTS A CLAIM. The suggested skill is
# 5.B, supporting a claim with RELEVANT evidence, and relevance is the word doing
# the work: evidence can be true, interesting and about the right subject while
# bearing on a different claim than the one being made. Items 15 to 22 give a
# claim and ask which evidence reaches it, and several distractors are true
# statements that support some other claim -- which is the discrimination the
# skill actually names.
#
# The CED attaches no foundational document and no required case to 5.9.A. Both
# tables are labelled hypothetical and no real election, year or officeholder is
# named.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.9", "Congressional Elections", 5)

_INCUMBENTS = ("A hypothetical study reports, for four congressional election cycles, how many "
               "incumbents sought reelection and how many were reelected.")
_INCUMBENTS_TABLE = dict(
    headers=["Election cycle", "Incumbents seeking reelection", "Incumbents reelected",
             "Reelection rate (%)"],
    rows=[["Cycle 1", "398", "374", "94"],
          ["Cycle 2", "385", "331", "86"],
          ["Cycle 3", "402", "382", "95"],
          ["Cycle 4", "391", "355", "91"]])

_YEARTYPE = ("A hypothetical study reports congressional election turnout and the number of "
             "seats that changed party, across four elections of two kinds.")
_YEARTYPE_TABLE = dict(
    headers=["Election", "Type of year", "Congressional turnout (%)", "Seats changing party"],
    rows=[["Election 1", "Presidential", "62", "18"],
          ["Election 2", "Midterm", "44", "41"],
          ["Election 3", "Presidential", "60", "14"],
          ["Election 4", "Midterm", "41", "37"]])

QUESTIONS = [
 dict(q="According to the course framework, which four things affect the process and outcomes in U.S. congressional elections?",
   choices=[
     "The incumbency advantage phenomenon, open and closed primaries, caucuses, and general presidential and midterm elections",
     "The incumbency advantage phenomenon, party conventions, the Electoral College, and general elections",
     "Open and closed primaries, caucuses, party conventions, and the Electoral College",
     "Political parties, interest groups, elections, and media",
     "Structural barriers, political efficacy, demographics, and election type"], ans=0,
   why="EK 5.9.A.1 lists exactly these four. The second and third options import party conventions and the Electoral College, which EK 5.8.A.1 assigns to presidential elections and which EK 5.9.A.1 does not include."),

 dict(q="Which two items appear in EK 5.8.A.1's list for presidential elections but NOT in EK 5.9.A.1's list for congressional elections?",
   choices=[
     "Party conventions and the Electoral College",
     "Caucuses and open primaries",
     "The incumbency advantage phenomenon and caucuses",
     "General elections and closed primaries",
     "Open primaries and closed primaries"], ans=0,
   why="EK 5.8.A.1 lists six items and EK 5.9.A.1 lists four, and the two dropped are party conventions and the Electoral College. Both belong to choosing a president, so neither has a place in a congressional contest."),

 dict(q="Why does the Electoral College appear in the presidential list but not in the congressional one?",
   choices=[
     "Because it is the mechanism for choosing a president and has no role in electing members of Congress",
     "Because it was abolished for congressional elections",
     "Because states may choose whether to use it in congressional elections",
     "Because congressional elections use a proportional system instead",
     "Because the framework treats the two lists as identical"], ans=0,
   why="EK 5.8.B.1 describes the Electoral College as allocating electors in a presidential election, and EK 5.9.A.1 omits it entirely. Members of Congress are elected directly in their states and districts, so no intermediate body is involved."),

 dict(q="How does EK 5.9.A.1's fourth item differ from the corresponding item in the presidential list?",
   choices=[
     "It names general PRESIDENTIAL AND MIDTERM elections, while the presidential list names general presidential elections",
     "It names only midterm elections",
     "It names only presidential elections",
     "It names primaries rather than general elections",
     "The two items are worded identically"], ans=0,
   why="EK 5.8.A.1.v reads 'General (presidential) elections' and EK 5.9.A.1.iv reads 'General (presidential and midterm) elections'. The added word is the whole difference, and it records that congressional elections occur in both kinds of year."),

 dict(q="What follows from congressional elections occurring in both presidential and midterm years?",
   choices=[
     "The same office is contested under conditions that differ, including the turnout difference the framework records between the two kinds of election",
     "Members of Congress serve terms of unequal length",
     "Only half the states hold congressional elections in a midterm year",
     "Congressional elections in midterm years are advisory",
     "The framework treats the two kinds of year as identical"], ans=0,
   why="EK 5.9.A.1.iv names both kinds of year, and EK 5.2.A.2.iii states that there is more turnout for presidential elections than midterm elections. The office and the rules are the same; the electorate that turns out is not."),

 dict(q="According to the course framework, what is the incumbency advantage phenomenon?",
   choices=[
     "The benefits current officeholders possess over challengers",
     "The requirement that members of Congress stand for reelection",
     "The advantage of running in a presidential year rather than a midterm year",
     "The benefit of being nominated through an open rather than a closed primary",
     "The head start of the candidate whose party holds the presidency"], ans=0,
   why="EK 5.8.A.1.i supplies the parenthetical definition, and EK 5.9.A.1.i names the same phenomenon for congressional elections. It is a comparison between an officeholder and a challenger rather than between kinds of election or nomination."),

 dict(q="EK 5.9.A.1 says these four things affect the PROCESS AND OUTCOMES of congressional elections. What does naming both indicate?",
   choices=[
     "That the listed items shape how the election is conducted and also who wins it",
     "That process and outcomes are the same thing",
     "That only the process is affected",
     "That only the outcome is affected",
     "That the framework ranks process above outcome"], ans=0,
   why="EK 5.9.A.1's phrase is 'the process and outcomes', and its items cover both: primaries and caucuses are stages of the process, while the incumbency advantage bears on who wins. EK 5.8.A.1 uses the identical phrase for presidential elections."),

 dict(q="Which of EK 5.9.A.1's four items is a condition a candidate brings to the race rather than a stage of it?",
   choices=[
     "The incumbency advantage phenomenon",
     "Open and closed primaries",
     "Caucuses",
     "General presidential and midterm elections",
     "None of them"], ans=0,
   why="EK 5.9.A.1.i names an advantage a current officeholder possesses, which is carried into whatever stages follow, while the other three items are stages of the election itself. The same asymmetry appears in EK 5.8.A.1's longer list."),

 dict(q="A claim states that congressional elections are contested under different conditions depending on the year. Which framework statements together support it?",
   choices=[
     "EK 5.9.A.1.iv's naming of both presidential and midterm general elections, and EK 5.2.A.2.iii's statement that turnout is higher in presidential elections",
     "EK 5.8.B.1's account of the Electoral College, and EK 5.9.A.1.i's incumbency advantage",
     "EK 5.3.A.1's linkage institutions, and EK 5.5.A.1's winner-take-all districts",
     "EK 5.6.B.1's inequality of interest group resources, and EK 5.7.A.3's realignments",
     "EK 5.4.A.1's candidate-centered campaigns, and EK 5.1.B.1's models of voting behavior"], ans=0,
   why="One statement establishes that congressional elections occur in two kinds of year and the other establishes that those years differ in turnout, so together they reach the claim. Neither alone would: the first names the two years without comparing them and the second compares turnout without mentioning Congress."),

 dict(q="Why is EK 5.2.A.2.iii relevant to this topic even though it appears under voter turnout?",
   choices=[
     "Because EK 5.9.A.1.iv places congressional elections in both presidential and midterm years, and EK 5.2.A.2.iii states that turnout differs between them",
     "Because EK 5.2.A.2.iii concerns the Electoral College",
     "Because EK 5.9.A.1 lists voter turnout as a fifth item",
     "Because the two statements are identical",
     "Because EK 5.2.A.2.iii applies only to congressional elections"], ans=0,
   why="EK 5.9.A.1.iv's parenthesis names both kinds of year, which is exactly the comparison EK 5.2.A.2.iii makes. The connection runs through the two statements sharing a subject rather than through either mentioning the other."),

 dict(q="A midterm congressional election and a presidential-year congressional election differ in which respect that the framework states outright?",
   choices=[
     "Turnout, which EK 5.2.A.2.iii says is higher in presidential elections",
     "The length of the terms being contested",
     "The number of seats being contested in the House",
     "Whether primaries are used to nominate candidates",
     "Whether the incumbency advantage phenomenon operates"], ans=0,
   why="EK 5.2.A.2.iii states the turnout comparison directly. The framework says nothing that would make terms, the number of House seats, the use of primaries or the incumbency advantage differ between the two kinds of year."),

 dict(q="Which processes appear in BOTH EK 5.8.A.1's and EK 5.9.A.1's lists?",
   choices=[
     "The incumbency advantage phenomenon, open and closed primaries, and caucuses",
     "Party conventions and the Electoral College",
     "Only general elections",
     "Only caucuses",
     "None of them"], ans=0,
   why="Three items are common to both lists, and the fourth item on each concerns general elections but differs in which years it names. The overlap is what the two kinds of election share as processes."),

 dict(q="How do EK 5.8.A.1's and EK 5.9.A.1's treatments of caucuses compare?",
   choices=[
     "Both lists include caucuses, and the definition supplied in the presidential list applies to the term in both",
     "Only the presidential list includes caucuses",
     "Only the congressional list includes caucuses",
     "The two lists define caucuses differently",
     "Neither list includes caucuses"], ans=0,
   why="EK 5.9.A.1.iii names caucuses without a parenthesis, and EK 5.8.A.1.iii defines them as closed meetings of party members to select candidates or decide policy. The framework defines a term once and uses it in both lists."),

 dict(q="A student preparing for congressional elections studies party conventions in detail. What is the most important correction?",
   choices=[
     "Party conventions appear in the framework's presidential list and not in its congressional one",
     "Party conventions appear in neither list",
     "Party conventions appear in the congressional list and not the presidential one",
     "Party conventions are the only item common to both lists",
     "The two lists are identical, so the study is appropriate"], ans=0,
   why="EK 5.8.A.1.iv names party conventions among the six items affecting presidential elections, and EK 5.9.A.1's four items do not include them. Studying the right content for the wrong contest is the error the two lists' difference exists to prevent."),

 dict(q="The suggested skill for this topic is supporting a claim with RELEVANT evidence. What does the word RELEVANT add?",
   choices=[
     "That the evidence must bear on the particular claim being made, not merely be true and on the same subject",
     "That the evidence must be recent",
     "That the evidence must come from a government source",
     "That the evidence must be quantitative",
     "That the evidence must be widely known"], ans=0,
   why="Skill 5.B pairs supporting a claim with the requirement that the evidence be relevant, which is a relation between the evidence and the claim. A true statement about congressional elections can support some other claim entirely."),

 dict(q="A claim states that incumbency confers a substantial advantage in congressional elections. Which evidence is most relevant?",
   choices=[
     "The share of incumbents seeking reelection who are reelected, across several cycles",
     "The number of states that use open primaries",
     "The share of eligible voters who turned out in the most recent midterm",
     "The number of seats in the House of Representatives",
     "The number of candidates who ran unopposed in primaries"], ans=0,
   why="The claim is about how incumbents fare against challengers, so a reelection rate for incumbents is evidence bearing on it directly. The other four are true things about congressional elections that would support different claims."),

dict(
   q="A claim states that turnout in congressional elections depends on whether the year is a presidential or a midterm one. Which evidence is most relevant?",
   choices=[
     "Congressional turnout figures for several elections, labeled by which kind of year each was",
     "The reelection rate of incumbents over the same period",
     "The number of states using caucuses to nominate congressional candidates",
     "The share of voters who identify with each major party",
     "The number of amicus curiae briefs filed in election cases"], ans=0,
   why="The claim relates turnout to the kind of year, so the evidence has to carry both variables. Turnout figures without the year labels, or year labels without turnout, would each leave half the claim unaddressed."),

 dict(q="A claim states that the nominating method a state uses affects who wins congressional primaries. Which evidence would be relevant?",
   choices=[
     "A comparison of primary outcomes in states using open primaries with those in states using closed primaries",
     "The reelection rate of incumbents in general elections",
     "Turnout in presidential elections over several decades",
     "The number of electoral votes each state casts",
     "The share of party platforms addressing a given issue"], ans=0,
   why="The claim relates a nominating method to an outcome, so relevant evidence has to vary the method and observe the outcome. Electoral votes and party platforms concern other topics entirely, and general election reelection rates address a different stage."),

 dict(q="A student supports the claim that incumbency matters in congressional elections by citing the fact that congressional elections are held every two years. Why is this evidence not relevant?",
   choices=[
     "The frequency of elections says nothing about how incumbents fare against challengers, which is what the claim is about",
     "The frequency of elections is not a fact",
     "The claim cannot be supported by any evidence",
     "The evidence is too recent to be useful",
     "The evidence concerns the Senate rather than the House"], ans=0,
   why="Skill 5.B asks for evidence bearing on the claim, and the cited fact is true and about congressional elections without touching the comparison the claim makes. Relevance is a relation to the claim, not a property of the fact."),

 dict(q="Which of the following claims could the framework's own statements support without any additional data?",
   choices=[
     "Congressional elections occur in both presidential and midterm years",
     "Incumbents win more than ninety percent of congressional races",
     "Open primaries produce more moderate nominees than closed primaries",
     "Turnout in congressional elections has declined over the past century",
     "Most congressional districts are uncompetitive"], ans=0,
   why="EK 5.9.A.1.iv states that congressional general elections occur in presidential and midterm years, so the first claim is the framework's own. The other four are empirical claims about magnitudes and trends that no statement in the framework supplies."),

 dict(q="A student writes a thesis about congressional elections and cites the Electoral College as supporting evidence. What is the most important problem?",
   choices=[
     "The Electoral College has no role in congressional elections, so the evidence bears on a different contest",
     "The Electoral College is not mentioned anywhere in the framework",
     "The evidence is accurate but too general",
     "The evidence supports the opposite conclusion",
     "The Electoral College concerns only midterm elections"], ans=0,
   why="EK 5.8.A.1.vi places the Electoral College in the presidential list and EK 5.9.A.1 omits it, so it cannot bear on a claim about congressional elections. Skill 5.B's requirement of relevance is what the citation fails."),

 dict(q="Two students make different claims about the same table of congressional election data. What does skill 5.B require of each?",
   choices=[
     "That each cite the parts of the data bearing on their own claim, since the same table can support different claims through different figures",
     "That both cite the entire table",
     "That both reach the same claim",
     "That neither cite the table, since it is only data",
     "That each cite a different table"], ans=0,
   why="Relevance is a relation between a piece of evidence and a particular claim, so which figures matter depends on what is being argued. One table can be relevant to several claims through different columns."),

 dict(q="Which of the following does EK 5.9.A.1 NOT state?",
   choices=[
     "How large the incumbency advantage is",
     "That the incumbency advantage phenomenon affects congressional elections",
     "That open and closed primaries affect congressional elections",
     "That caucuses affect congressional elections",
     "That general presidential and midterm elections affect congressional elections"], ans=0,
   why="EK 5.9.A.1 names four things that affect the process and outcomes and gives no magnitude for any of them. Every other option restates one of its four items."),

 dict(q="Why is EK 5.9.A.1 shorter than EK 5.8.A.1?",
   choices=[
     "Because two of the presidential list's items concern choosing a president and have no counterpart in a congressional election",
     "Because congressional elections are less important",
     "Because the framework omitted items by mistake",
     "Because congressional elections involve no primaries",
     "Because the two lists cover different years"], ans=0,
   why="Party conventions and the Electoral College belong to the selection of a president, and the remaining items apply to both contests. The difference in length records a real difference between the two elections rather than an editorial choice."),

 dict(q=_INCUMBENTS + " Which conclusion is best supported by the data?",
   table=_INCUMBENTS_TABLE,
   choices=[
     "In every cycle at least eighty-five percent of incumbents seeking reelection were reelected",
     "The reelection rate fell below half in at least one cycle",
     "The reelection rate was identical in every cycle",
     "Fewer incumbents sought reelection than were reelected in one cycle",
     "The number of incumbents seeking reelection fell in every cycle"], ans=0,
   why="The reelection rates are 94, 86, 95 and 91 percent, so the lowest is 86. In every row the number reelected is smaller than the number seeking reelection, and the number seeking reelection rises and falls across the cycles."),

 dict(q=_INCUMBENTS + " Which claim does this evidence most directly support?",
   table=_INCUMBENTS_TABLE,
   choices=[
     "That the incumbency advantage phenomenon EK 5.9.A.1.i names operates in congressional elections",
     "That turnout is higher in presidential years than in midterm years",
     "That open primaries produce different nominees than closed primaries",
     "That party conventions affect congressional elections",
     "That states allocate electors differently"], ans=0,
   why="The table reports how incumbents fare when they seek reelection, which bears on EK 5.9.A.1.i's incumbency advantage and on nothing else in the framework's list. The second option concerns a comparison the table does not make and the last two concern presidential elections."),

 dict(q=_INCUMBENTS + " Which of the following would NOT be relevant evidence for a claim about the size of the incumbency advantage?",
   table=_INCUMBENTS_TABLE,
   choices=[
     "The number of states that use open rather than closed primaries",
     "The share of incumbents seeking reelection who were reelected",
     "The share of challengers who defeated an incumbent",
     "The margin by which incumbents won compared with the margin in open seats",
     "The number of incumbents who chose not to seek reelection"], ans=0,
   why="A count of nominating methods says nothing about how officeholders fare against challengers, which is what the claim is about. The other four all compare incumbents with challengers or with open seats, which is the comparison EK 5.9.A.1.i names."),

 dict(q=_YEARTYPE + " Which conclusion is best supported by the data?",
   table=_YEARTYPE_TABLE,
   choices=[
     "Congressional turnout was higher in both presidential years than in either midterm year, and more seats changed party in the midterm years",
     "Congressional turnout was higher in the midterm years",
     "The same number of seats changed party in every election",
     "More seats changed party in the presidential years",
     "Turnout and seats changing party moved in the same direction"], ans=0,
   why="Turnout reads 62 and 60 percent in the presidential years against 44 and 41 in the midterms, and seats changing party read 18 and 14 against 41 and 37. The two columns move in opposite directions across the two kinds of year."),

 dict(q=_YEARTYPE + " Which framework statements does this table bear on?",
   table=_YEARTYPE_TABLE,
   choices=[
     "EK 5.9.A.1.iv's naming of general presidential and midterm elections, and EK 5.2.A.2.iii's statement that turnout is higher in presidential elections",
     "EK 5.8.B.1's account of how states allocate electors",
     "EK 5.6.A.1's activities of interest groups",
     "EK 5.5.A.2's incorporation of third-party agendas",
     "EK 5.3.B.1's functions of political parties"], ans=0,
   why="The table's type-of-year column is EK 5.9.A.1.iv's distinction and its turnout column is the comparison EK 5.2.A.2.iii states. Nothing here concerns electors, interest groups, third parties or party functions."),

 dict(q=_YEARTYPE + " A student claims that congressional elections are contested under systematically different conditions in the two kinds of year. Which part of the data is the most relevant evidence?",
   table=_YEARTYPE_TABLE,
   choices=[
     "That both measured columns differ consistently by type of year rather than varying at random across the four elections",
     "That four elections are reported rather than three",
     "That turnout is reported as a percentage",
     "That the table names no candidates",
     "That the seats changing party are whole numbers"], ans=0,
   why="The claim is about a systematic difference between the two kinds of year, so the relevant evidence is that the difference holds in both columns and in both pairs of elections. The number of rows, the units and the absence of names are features of the table that bear on no claim about conditions."),
]
