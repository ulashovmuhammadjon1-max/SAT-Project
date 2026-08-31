# AP U.S. GOVERNMENT AND POLITICS 5.5 Third-Party Politics -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# Learning objective 5.5.A: explain how STRUCTURAL BARRIERS affect THIRD-PARTY
# AND INDEPENDENT CANDIDATE SUCCESS.
# Suggested skill for this topic (CED p. 116): 3.D, data analysis -- explain what
# the data IMPLIES OR ILLUSTRATES about political principles, institutions,
# processes, policies, and behaviors.
#
# Essential knowledge relied on. Two statements, two barriers:
#   EK 5.5.A.1 -- "IN COMPARISON TO PROPORTIONAL SYSTEMS, WINNER-TAKE-ALL voting
#     districts serve as a structural barrier to third-party and independent
#     candidate success. Winner-take-all voting ADVANTAGES THE TWO-PARTY SYSTEM
#     in the U.S."
#   EK 5.5.A.2 -- "The INCORPORATION OF THIRD-PARTY AGENDAS INTO PLATFORMS OF
#     MAJOR POLITICAL PARTIES serves as a barrier to third-party and independent
#     candidate success."
#
# THE SECOND BARRIER IS THE COUNTERINTUITIVE ONE AND IT IS THE HEART OF THIS
# TOPIC. EK 5.5.A.2 says a third party whose ideas SUCCEED -- taken up by a major
# party -- is thereby made LESS likely to succeed ELECTORALLY. Winning the
# argument costs it the reason voters had to support it. A student who has only
# absorbed the first barrier will explain every third-party failure by the
# electoral system and will have no account of the party that failed while its
# programme was being adopted. Items 9 to 14 and the second table are built on
# it, and that table is deliberately arranged so the proposals that were
# incorporated are the MOST popular ones, which is what makes item 30's
# correction the whole point of the statement.
#
# EK 5.5.A.1 IS A COMPARATIVE CLAIM, NOT AN ABSOLUTE ONE. Its first four words
# are IN COMPARISON TO PROPORTIONAL SYSTEMS. Winner-take-all is a barrier
# RELATIVE to an alternative the framework names, and the direction is stated:
# winner-take-all ADVANTAGES THE TWO-PARTY SYSTEM. Both the comparison and the
# direction are droppable, and reversing the direction -- treating proportional
# allocation as the barrier, or winner-take-all as a help to third parties -- is
# a clean falsehood. The verifier refuses both.
#
# BOTH STATEMENTS COVER INDEPENDENT CANDIDATES AS WELL AS THIRD PARTIES. The
# framework's phrase in both is "third-party AND INDEPENDENT CANDIDATE success",
# and an independent candidate has no agenda for a major party to incorporate in
# the same way, so the two barriers do not bear on independents identically.
# Item 19 makes that the question.
#
# Documents the CED attaches to 5.5.A (p. 27): Federalist No. 10, which is
# attached to 5.3.A through 5.7.A. Items 20 and 21 quote it verbatim.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.5", "Third-Party Politics", 5)

_SEATS = ("A hypothetical legislature of 100 seats is filled from single-member districts under "
          "a winner-take-all rule. The table reports each party's share of the votes cast, the "
          "seats it won, and the seats it would have won had the same votes been allocated "
          "proportionally.")
_SEATS_TABLE = dict(
    headers=["Party", "Share of votes cast (%)", "Seats won under winner-take-all",
             "Seats under proportional allocation"],
    rows=[["Major Party One", "42", "58", "42"],
          ["Major Party Two", "39", "40", "39"],
          ["Third Party A", "12", "2", "12"],
          ["Third Party B", "7", "0", "7"]])

_AGENDAS = ("A hypothetical study followed four proposals first advanced by third parties. For "
            "each it reports public support at the time, whether a major party later adopted the "
            "proposal into its platform, and the third party's vote share in the next election.")
_AGENDAS_TABLE = dict(
    headers=["Proposal", "Public support at the time (%)",
             "Adopted into a major party platform", "Third-party vote share next election (%)"],
    rows=[["Proposal 1", "61", "Yes", "3"],
          ["Proposal 2", "54", "Yes", "2"],
          ["Proposal 3", "38", "No", "9"],
          ["Proposal 4", "22", "No", "7"]])

QUESTIONS = [
 dict(q="According to the course framework, what serves as a structural barrier to third-party and independent candidate success, in comparison to proportional systems?",
   choices=[
     "Winner-take-all voting districts",
     "Proportional allocation of seats",
     "Open primary elections",
     "Automatic voter registration",
     "Party conventions"], ans=0,
   why="EK 5.5.A.1 names winner-take-all voting districts, and it names them in comparison to proportional systems. The comparison is part of the claim rather than background to it."),

 dict(q="EK 5.5.A.1 begins IN COMPARISON TO PROPORTIONAL SYSTEMS. What does that opening phrase do to the claim?",
   choices=[
     "It makes the claim comparative, so winner-take-all is a barrier relative to a named alternative rather than in the abstract",
     "It means proportional systems are the barrier",
     "It means the claim applies only outside the United States",
     "It means the two systems produce identical results",
     "It means the claim is about primaries rather than general elections"], ans=0,
   why="A barrier IN COMPARISON TO something is defined against that alternative, and the framework supplies the alternative in the same sentence. Dropping the phrase turns a comparison into an absolute claim the framework does not make."),

 dict(q="According to EK 5.5.A.1, what does winner-take-all voting advantage?",
   choices=[
     "The two-party system in the United States",
     "Third parties and independent candidates",
     "Proportional representation",
     "Incumbent officeholders in primaries",
     "State governments over the national government"], ans=0,
   why="EK 5.5.A.1's second sentence states this directly. It is the direction of the effect, and reversing it would make the same system a help to the candidates the first sentence says it obstructs."),

 dict(q="Why does a winner-take-all rule disadvantage a party with support spread thinly across many districts?",
   choices=[
     "Because only the leading candidate in each district wins anything, so support that falls short everywhere yields nothing",
     "Because such a party is barred from the ballot",
     "Because its votes are counted differently from other parties' votes",
     "Because it must win a majority of the national vote",
     "Because the framework requires proportional allocation"], ans=0,
   why="Under the rule EK 5.5.A.1 names, each district produces one winner, so votes for anyone else produce no seats. That mechanism is why the framework calls it a structural barrier rather than a matter of the party's appeal."),

 dict(q="Under a proportional system, how would a party with twelve percent of the votes across a hundred-seat legislature be expected to fare, compared with a winner-take-all system?",
   choices=[
     "It would be expected to win a share of seats near its share of votes, which winner-take-all does not guarantee",
     "It would win no seats at all",
     "It would win a majority of seats",
     "It would fare identically under both systems",
     "It would be barred from holding seats"], ans=0,
   why="Proportional allocation matches seats to vote shares, which is the alternative EK 5.5.A.1 compares winner-take-all against. Under winner-take-all a party can hold that share of the vote and win almost nothing if it leads in no district."),

 dict(q="What does the framework's term STRUCTURAL BARRIER indicate about the obstacle EK 5.5.A.1 describes?",
   choices=[
     "That it arises from how the electoral system is built rather than from the appeal of any particular candidate",
     "That it is written into the Constitution",
     "That it can be removed only by amendment",
     "That it applies only to candidates without funding",
     "That it is a temporary condition"], ans=0,
   why="A structural barrier is a feature of the arrangement itself, which is why EK 5.5.A.1 locates it in the voting districts rather than in the parties. EK 5.2.A.1 uses the same term for features of election administration that bear on turnout."),

 dict(q="A third party wins 15 percent of the vote in every district in a state and no seats. Which framework statement does this outcome illustrate?",
   choices=[
     "EK 5.5.A.1's account of winner-take-all districts as a structural barrier",
     "EK 5.5.A.2's account of the incorporation of third-party agendas",
     "EK 5.4.A.3.i's definition of a critical election",
     "EK 5.3.A.1's definition of a linkage institution",
     "EK 5.2.A.2's influences on voter turnout"], ans=0,
   why="Uniform support that never leads a district is exactly the case in which a winner-take-all rule converts substantial votes into no seats. Nothing in the scenario concerns a major party adopting the third party's programme."),

 dict(q="Which of the following does EK 5.5.A.1 NOT state?",
   choices=[
     "That the United States should adopt a proportional system",
     "That winner-take-all districts are a structural barrier in comparison to proportional systems",
     "That winner-take-all voting advantages the two-party system in the United States",
     "That the barrier affects independent candidates as well as third parties",
     "That the comparison is with proportional systems"], ans=0,
   why="EK 5.5.A.1 describes an effect and recommends nothing. Every other option restates part of the statement, including its coverage of independent candidates and its named comparison."),

 dict(q="According to EK 5.5.A.2, what second thing serves as a barrier to third-party and independent candidate success?",
   choices=[
     "The incorporation of third-party agendas into the platforms of major political parties",
     "The requirement that candidates be nominated in primaries",
     "The use of proportional allocation in some states",
     "The rising cost of campaigns",
     "The role of the media in setting the agenda"], ans=0,
   why="EK 5.5.A.2 states this directly. It is a second and quite different barrier from the electoral rule EK 5.5.A.1 describes, and it operates through the major parties rather than through the voting system."),

 dict(q="Why does a major party adopting a third party's proposals make it harder for that third party to succeed electorally?",
   choices=[
     "Because voters who supported the third party for those proposals can now obtain them by voting for a major party",
     "Because the third party is prohibited from advancing the proposals again",
     "Because the proposals become unpopular once a major party adopts them",
     "Because the third party loses its ballot access",
     "Because the major party is required to absorb the third party"], ans=0,
   why="EK 5.5.A.2 identifies the incorporation of agendas as the barrier, and the mechanism is that it removes the distinctive reason to vote for the smaller party. Nothing in the framework says the proposals become unpopular or that any legal consequence follows."),

 dict(q="What is unusual about the barrier EK 5.5.A.2 describes, compared with an ordinary obstacle?",
   choices=[
     "It operates through the third party's ideas succeeding rather than failing",
     "It operates only in presidential elections",
     "It applies only to parties that win seats",
     "It is imposed by a court rather than by voters",
     "It affects major parties rather than third parties"], ans=0,
   why="EK 5.5.A.2's barrier arises when a major party takes up the third party's agenda, which is the third party winning the argument. Its programme advances and its electoral prospects do not, which is why the statement is worth stating separately."),

 dict(q="A third party campaigns for years on one proposal, a major party adopts the proposal, and the third party's vote falls in the next election. Which framework statement explains this?",
   choices=[
     "EK 5.5.A.2's incorporation of third-party agendas into major party platforms",
     "EK 5.5.A.1's winner-take-all districts",
     "EK 5.4.A.1's candidate-centered campaigns",
     "EK 5.2.A.1's structural barriers to turnout",
     "EK 5.3.B.1's functions of political parties"], ans=0,
   why="The sequence is exactly EK 5.5.A.2's: an agenda incorporated into a major party's platform, followed by reduced success for the party that advanced it. The electoral rule did not change in the scenario, so EK 5.5.A.1 explains nothing about the fall."),

 dict(q="How does EK 5.5.A.2 relate to EK 5.3.B.1's list of party functions?",
   choices=[
     "A major party's platform is one of the listed functions, and EK 5.5.A.2 describes a consequence of what a major party puts in it",
     "The two statements describe the same function under different names",
     "EK 5.5.A.2 says major parties have no platforms",
     "EK 5.3.B.1 says third parties have no platforms",
     "The two statements are unrelated"], ans=0,
   why="EK 5.3.B.1.ii names party platforms as a function of political parties, and EK 5.5.A.2 is about what happens to a third party when a major party's platform absorbs its agenda. One statement names the activity, the other a consequence of it."),

 dict(q="Which of the following would be evidence for EK 5.5.A.2 rather than EK 5.5.A.1?",
   choices=[
     "A third party whose distinctive proposals appear in a major party's platform and whose vote then declines",
     "A third party that wins a substantial share of votes and almost no seats",
     "A third party whose support is spread evenly across districts",
     "A comparison of seat allocations under two different voting rules",
     "A finding that turnout is higher in presidential elections"], ans=0,
   why="EK 5.5.A.2's barrier runs through a major party's platform, so evidence for it has to involve incorporation. The second, third and fourth options all concern how votes become seats, which is EK 5.5.A.1's subject."),

 dict(q="What do EK 5.5.A.1 and EK 5.5.A.2 have in common?",
   choices=[
     "Both identify a barrier to third-party and independent candidate success",
     "Both concern the rules governing voting districts",
     "Both concern the platforms of major parties",
     "Both concern voter turnout",
     "Both recommend changes to the electoral system"], ans=0,
   why="The two statements name different mechanisms and share an object: third-party and independent candidate success. Neither recommends anything, and only the first concerns districts while only the second concerns platforms."),

 dict(q="A third party fails to win seats despite substantial support, and in the same period a major party adopts its leading proposal. Which framework statements are relevant?",
   choices=[
     "Both, since EK 5.5.A.1's electoral rule and EK 5.5.A.2's incorporation are separate barriers that can operate at once",
     "Only EK 5.5.A.1, since the party won no seats",
     "Only EK 5.5.A.2, since a proposal was adopted",
     "Neither, since the framework treats the two as alternatives",
     "Neither, since the party had substantial support"], ans=0,
   why="EK 5.5.A.1 and EK 5.5.A.2 describe different mechanisms and the framework does not present them as exclusive. A party can be denied seats by the voting rule while also losing its distinctive appeal to a major party's platform."),

 dict(q="A student explains every third-party failure by the winner-take-all electoral system. What does EK 5.5.A.2 add that the explanation misses?",
   choices=[
     "That a third party can also be undercut by major parties adopting its agenda, which is a barrier operating through ideas rather than through seat allocation",
     "That third parties never fail",
     "That the winner-take-all system does not exist",
     "That third parties are barred from the ballot",
     "That proportional systems produce the same outcomes"], ans=0,
   why="EK 5.5.A.2 names a second barrier the framework treats as independent of the first, and a single-cause explanation has no account of the party that fades while its programme is being adopted. Both statements are course content for this topic."),

 dict(q="Both framework statements refer to third-party AND INDEPENDENT CANDIDATE success. Why does that matter?",
   choices=[
     "Because the barriers described apply to candidates running without a party as well as to small parties, though an independent candidate has no party agenda for a major party to incorporate in the same way",
     "Because independent candidates are a kind of third party",
     "Because the framework covers only third parties",
     "Because independent candidates are barred from general elections",
     "Because independent candidates always win under winner-take-all"], ans=0,
   why="Both statements name independent candidates alongside third parties, so both barriers are stated to reach them. The winner-take-all obstacle applies straightforwardly to an independent, while EK 5.5.A.2's mechanism runs through a party agenda, which is a difference worth noticing."),

 dict(q="Read the following excerpt.\n\n“Extend the sphere, and you take in a greater variety of parties and interests; you make it less probable that a majority of the whole will have a common motive to invade the rights of other citizens.”\n—James Madison, Federalist No. 10, 1787\n\nWhat tension does this passage set up with the topic of third-party politics?",
   choices=[
     "It treats a greater variety of parties and interests as a benefit, while this topic describes structural features that reduce the number of parties winning office",
     "It argues that only two parties should exist",
     "It states that third parties are unconstitutional",
     "It concerns voter turnout rather than parties",
     "It has no bearing on the number of parties"], ans=0,
   why="Madison's argument treats variety among parties and interests as protective, and EK 5.5.A.1 says the winner-take-all rule advantages a two-party system. The CED attaches Federalist No. 10 to 5.5.A, and reading the two together sets a founding argument beside an institutional consequence."),

 dict(q="Read the following excerpt.\n\n“The latent causes of faction are thus sown in the nature of man.”\n—James Madison, Federalist No. 10, 1787\n\nHow does this claim bear on the persistence of third parties despite the barriers this topic describes?",
   choices=[
     "If the sources of political division are permanent, new parties will keep forming even where the system disadvantages them",
     "It predicts that third parties will disappear entirely",
     "It states that only two factions can exist at a time",
     "It argues that factions should be suppressed by law",
     "It has no bearing on why parties form"], ans=0,
   why="Madison locates the causes of faction in a standing condition rather than a removable one, so division keeps producing organizations. EK 5.5.A.1 and EK 5.5.A.2 describe why such organizations struggle to win office, which is a different question from why they appear."),

 dict(q="Which of the following does EK 5.5.A.2 NOT state?",
   choices=[
     "How often major parties incorporate third-party agendas",
     "That the incorporation of third-party agendas serves as a barrier",
     "That the incorporation happens into the platforms of major political parties",
     "That the barrier affects third-party success",
     "That the barrier affects independent candidate success"], ans=0,
   why="EK 5.5.A.2 identifies a mechanism and states no frequency. Every other option restates part of its single sentence."),

 dict(q="Why does the CED assign this topic a data analysis skill?",
   choices=[
     "Because both barriers show up as a gap between a party's support and its electoral success, which is a comparison of quantities",
     "Because the topic contains no concepts",
     "Because third parties publish more data than major parties",
     "Because the framework provides its own data set",
     "Because data analysis is the only skill used in Unit 5"], ans=0,
   why="The suggested skill for 5.5 is 3.D, explaining what data implies or illustrates, and each barrier is visible as a discrepancy: votes against seats for the first, and support against subsequent vote share for the second. Unit 5 uses six different skills across its thirteen topics."),

 dict(q="Which statement best summarizes what this topic establishes?",
   choices=[
     "Two barriers face third-party and independent candidates: one built into how votes become seats, and one arising when major parties adopt their agendas",
     "One barrier faces third parties, built into how votes become seats",
     "Third parties face no barriers in the United States",
     "The framework recommends replacing winner-take-all with proportional allocation",
     "Third parties fail because their ideas are unpopular"], ans=0,
   why="EK 5.5.A.1 and EK 5.5.A.2 name two distinct barriers with different mechanisms, and the framework recommends nothing. The last option is contradicted by EK 5.5.A.2, under which a third party is undercut precisely when its ideas prove popular enough to be adopted."),

 dict(q="EK 5.8.B.1 states that most states use a winner-take-all system to allocate their electoral votes. How does that bear on this topic?",
   choices=[
     "It applies the same rule EK 5.5.A.1 identifies as a structural barrier to the presidential contest, so a candidate can draw votes across many states and win no electors",
     "It shows that presidential elections use proportional allocation",
     "It shows that the barrier EK 5.5.A.1 describes applies only to legislatures",
     "It shows that third-party candidates are barred from presidential ballots",
     "It has no connection to third-party success"], ans=0,
   why="EK 5.5.A.1 identifies winner-take-all voting as the structural barrier, and EK 5.8.B.1 says most states allocate electors that way, so the same mechanism operates in the presidential contest. EK 5.8.B.1 also notes that states can choose how they allocate, which is why the framework says MOST rather than all."),

 dict(q=_SEATS + " What does the data most directly illustrate?",
   table=_SEATS_TABLE,
   choices=[
     "The two third parties together won 19 percent of the votes and 2 of the 100 seats under winner-take-all, against 19 seats under proportional allocation",
     "The two third parties won more seats under winner-take-all than under proportional allocation",
     "Each party's seats matched its vote share under winner-take-all",
     "The major parties won fewer seats than their vote shares under winner-take-all",
     "No party won any seats under proportional allocation"], ans=0,
   why="Third Party A and Third Party B hold 12 and 7 percent of votes, and 2 and 0 seats under winner-take-all against 12 and 7 under proportional allocation. Major Party One converts 42 percent of votes into 58 seats, which is more than its share rather than fewer."),

 dict(q=_SEATS + " Which statement in the course framework does this table most directly illustrate?",
   table=_SEATS_TABLE,
   choices=[
     "EK 5.5.A.1's claim that winner-take-all districts are a structural barrier in comparison to proportional systems",
     "EK 5.5.A.2's claim about the incorporation of third-party agendas",
     "EK 5.4.A.1's account of candidate-centered campaigns",
     "EK 5.3.A.1's definition of a linkage institution",
     "EK 5.2.A.2's influences on voter turnout"], ans=0,
   why="The table sets the same votes against two allocation rules, which is precisely the comparison EK 5.5.A.1 makes. Nothing here concerns a major party's platform, which is EK 5.5.A.2's subject."),

 dict(q=_SEATS + " What does the table imply about the two-party system, in the framework's terms?",
   table=_SEATS_TABLE,
   choices=[
     "That the winner-take-all rule advantages it, since both major parties hold a larger share of seats than of votes while both third parties hold a smaller one",
     "That the winner-take-all rule disadvantages it",
     "That the rule has no effect on the major parties",
     "That the third parties would win no seats under either rule",
     "That the table cannot bear on the number of parties"], ans=0,
   why="Major Party One converts 42 percent of votes into 58 seats and Major Party Two 39 into 40, while the third parties convert 12 and 7 into 2 and 0. EK 5.5.A.1's second sentence says winner-take-all voting advantages the two-party system, and this is that claim in numbers."),

 dict(q=_AGENDAS + " What does the data most directly illustrate?",
   table=_AGENDAS_TABLE,
   choices=[
     "The third parties whose proposals a major party adopted drew lower vote shares in the next election than those whose proposals were not adopted",
     "The third parties whose proposals were adopted drew higher vote shares afterward",
     "Adoption made no difference to the third parties' vote shares",
     "The proposals that were adopted had the least public support",
     "No proposal in the table was adopted by a major party"], ans=0,
   why="The two adopted proposals are followed by third-party vote shares of 3 and 2 percent, against 9 and 7 for the two not adopted. The adopted proposals also had the highest public support at 61 and 54 percent."),

 dict(q=_AGENDAS + " Which statement in the course framework does this pattern most directly illustrate?",
   table=_AGENDAS_TABLE,
   choices=[
     "EK 5.5.A.2's claim that the incorporation of third-party agendas into major party platforms is a barrier to third-party success",
     "EK 5.5.A.1's claim about winner-take-all voting districts",
     "EK 5.4.A.2's claim that parties adapt policies to demographic coalitions",
     "EK 5.3.B.1's list of party functions",
     "EK 5.2.A.4's factors influencing voter choice"], ans=0,
   why="The table's third column records incorporation into a major party platform and its fourth records what happened to the third party afterward, which is EK 5.5.A.2's mechanism and its effect. No column concerns how votes became seats."),

 dict(q=_AGENDAS + " A student concludes from this table that the third parties whose vote fell did so because their proposals were unpopular. What is the most important correction?",
   table=_AGENDAS_TABLE,
   choices=[
     "Those were the two most popular proposals in the table, at 61 and 54 percent, and the framework's mechanism is that a major party adopting a proposal removes the distinctive reason to vote for the third party",
     "Those proposals had the least public support in the table",
     "The table does not report public support",
     "Neither of those proposals was adopted by a major party",
     "The table covers a single proposal, so no comparison is possible"], ans=0,
   why="The support column runs 61, 54, 38 and 22, so the two proposals followed by falling third-party votes are the two most popular ones. EK 5.5.A.2 is the framework's explanation, and it turns on the proposals succeeding rather than failing."),
]
