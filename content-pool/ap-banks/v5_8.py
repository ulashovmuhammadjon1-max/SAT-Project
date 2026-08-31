# AP U.S. GOVERNMENT AND POLITICS 5.8 Electing a President -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# TWO learning objectives:
#   LO 5.8.A -- explain how THE DIFFERENT PROCESSES work in a U.S. presidential
#     election.
#   LO 5.8.B -- explain how THE ELECTORAL COLLEGE affects U.S. presidential
#     elections.
# Suggested skill for this topic (CED p. 116): 5.A, argumentation -- ARTICULATE A
# DEFENSIBLE CLAIM OR THESIS.
#
# Essential knowledge relied on:
#   EK 5.8.A.1 -- "The process and outcomes in U.S. presidential elections are
#     affected by:
#       i.   INCUMBENCY ADVANTAGE PHENOMENON (BENEFITS CURRENT OFFICEHOLDERS
#            POSSESS OVER CHALLENGERS)
#       ii.  OPEN AND CLOSED PRIMARIES (voting processes to elect candidates)
#       iii. CAUCUSES (CLOSED MEETINGS OF PARTY MEMBERS to SELECT CANDIDATES OR
#            DECIDE POLICY)
#       iv.  PARTY CONVENTIONS
#       v.   GENERAL (PRESIDENTIAL) ELECTIONS
#       vi.  THE ELECTORAL COLLEGE"
#   EK 5.8.B.1 -- "STATES CAN CHOOSE HOW THEY ALLOCATE THEIR ELECTORS; MOST
#     STATES USE A WINNER-TAKE-ALL SYSTEM. Because the results of the Electoral
#     College vote MAY NOT BE THE SAME AS THE POPULAR VOTE nationwide, there is
#     an ONGOING DEBATE over the Electoral College."
#
# EK 5.8.B.1 IS THREE HEDGED CLAIMS IN ONE SENTENCE AND EVERY HEDGE MATTERS:
#   * STATES CAN CHOOSE how they allocate electors -- the method is a state's
#     decision, not a national rule.
#   * MOST states use winner-take-all. Most, not all. The word is what makes the
#     first clause more than decoration.
#   * The Electoral College result MAY NOT BE THE SAME as the national popular
#     vote. May not, not does not and not always differs.
# And the sentence ends by recording an ONGOING DEBATE without taking a side.
# This is the topic in Unit 5 where a bank could most easily slip a position in
# while looking like it was reporting one, so the verifier refuses any key that
# argues for or against the Electoral College. Item 21 makes the framework's own
# neutrality the question.
#
# THE CAUCUS DEFINITION HAS A SECOND HALF PEOPLE DROP. EK 5.8.A.1.iii is "closed
# meetings of party members to select candidates OR DECIDE POLICY". A caucus in
# the framework's sense is not only a nominating device. Item 6 keeps it.
#
# WHY SEVERAL ITEMS ASK WHICH CLAIM IS DEFENSIBLE. The suggested skill is 5.A,
# articulating a defensible claim, and that is testable in multiple choice: a
# defensible claim TAKES A POSITION and CAN BE SUPPORTED by available evidence.
# A restatement of a fact takes no position; a sweeping assertion takes one that
# the evidence cannot reach. Items 17 to 20, 27 and 30 turn on that pair of
# requirements, which is what the skill actually names.
#
# NO REAL ELECTION IS NAMED. The CED's illustrative example for this topic is one
# presidential election, marked NOT REQUIRED -- and it is the election most often
# cited in the very debate EK 5.8.B.1 says is ongoing, so naming it would import
# a side as well as unrequired content.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.8", "Electing a President", 5)

_NOMINATING = ("A hypothetical study classified the fifty states by the method each uses to "
               "choose delegates in presidential nominating contests, and reports average "
               "participation as a share of the state's eligible voters.")
_NOMINATING_TABLE = dict(
    headers=["Nominating method", "States using it", "Average participation (%)"],
    rows=[["Open primary", "21", "31"],
          ["Closed primary", "17", "27"],
          ["Caucus", "6", "8"],
          ["Combination of methods", "6", "24"]])

_ELECTORS = ("A hypothetical study reports four states' electoral votes, how each allocates "
             "them, and the share of the state's popular vote won by the leading candidate.")
_ELECTORS_TABLE = dict(
    headers=["State", "Electoral votes", "Allocation method",
             "Leading candidate's share of the state's popular vote (%)"],
    rows=[["State A", "38", "Winner-take-all", "51"],
          ["State B", "29", "Winner-take-all", "50"],
          ["State C", "5", "By congressional district", "58"],
          ["State D", "12", "Winner-take-all", "72"]])

QUESTIONS = [
 dict(q="According to the course framework, what is the INCUMBENCY ADVANTAGE PHENOMENON?",
   choices=[
     "The benefits current officeholders possess over challengers",
     "The requirement that a president serve no more than two terms",
     "The advantage a party holds in states it has won before",
     "The head start given to the candidate who raises money first",
     "The benefit a challenger gains from being new to voters"], ans=0,
   why="EK 5.8.A.1.i's parenthesis defines it in exactly these words. It is a comparison between two positions in a race rather than a rule about terms or a fact about parties."),

 dict(q="According to the course framework, what are OPEN AND CLOSED PRIMARIES?",
   choices=[
     "Voting processes to elect candidates",
     "Meetings of party members held behind closed doors",
     "Conventions at which a party adopts its platform",
     "Elections in which electors are chosen",
     "Procedures for registering to vote"], ans=0,
   why="EK 5.8.A.1.ii's parenthesis calls them voting processes to elect candidates. The framework treats the open and closed varieties together in one item, so what they share is the voting."),

 dict(q="According to the course framework, what is a CAUCUS?",
   choices=[
     "A closed meeting of party members to select candidates or decide policy",
     "A primary election open to any registered voter",
     "A convention held after the nominating contests conclude",
     "A meeting of a legislature's committee chairs",
     "A gathering of electors to cast their votes"], ans=0,
   why="EK 5.8.A.1.iii's parenthesis defines it in exactly these words, and both purposes are the framework's own: selecting candidates OR deciding policy."),

 dict(q="What is the most important structural difference between a primary and a caucus, as the framework defines them?",
   choices=[
     "A primary is a voting process while a caucus is a meeting that participants attend",
     "A primary is held by a state and a caucus by the national government",
     "A primary selects candidates and a caucus selects electors",
     "A primary is closed and a caucus is open",
     "There is no difference in the framework"], ans=0,
   why="EK 5.8.A.1.ii calls primaries voting processes and EK 5.8.A.1.iii calls caucuses closed meetings, so the difference the framework draws is between casting a ballot and attending a gathering. Both open and closed varieties exist for primaries, so openness is not the distinction."),

 dict(q="What does the word CLOSED mean in the framework's definition of a caucus?",
   choices=[
     "That participation is limited to party members",
     "That the meeting is held in secret from the press",
     "That no new candidates may be proposed",
     "That the results are not announced",
     "That the meeting occurs after the primaries end"], ans=0,
   why="EK 5.8.A.1.iii describes a caucus as a closed meeting OF PARTY MEMBERS, so the restriction the word marks is on who may take part. The same sense of closed appears in EK 5.8.A.1.ii's closed primaries."),

 dict(q="Besides selecting candidates, what other purpose does EK 5.8.A.1.iii say a caucus may serve?",
   choices=[
     "Deciding policy",
     "Certifying election results",
     "Allocating electoral votes",
     "Registering new voters",
     "Drawing district boundaries"], ans=0,
   why="EK 5.8.A.1.iii's parenthesis reads 'to select candidates or decide policy', so a caucus in the framework's sense is not only a nominating device. The second purpose is the half a summary usually drops."),

 dict(q="Which two processes in EK 5.8.A.1's list come after a party has settled on a nominee?",
   choices=[
     "General presidential elections and the Electoral College",
     "Open and closed primaries and caucuses",
     "Party conventions and caucuses",
     "The incumbency advantage phenomenon and party conventions",
     "Caucuses and the Electoral College"], ans=0,
   why="EK 5.8.A.1's list runs from the advantages a candidate brings, through the nominating processes and the convention, to the general election and the Electoral College. Primaries, caucuses and conventions all belong to choosing a nominee."),

 dict(q="How many distinct processes or factors does EK 5.8.A.1 list as affecting the process and outcomes of presidential elections?",
   choices=[
     "Six",
     "Four",
     "Five",
     "Seven",
     "Three"], ans=0,
   why="EK 5.8.A.1 lists the incumbency advantage phenomenon, open and closed primaries, caucuses, party conventions, general elections and the Electoral College. Open and closed primaries are one item in the framework's own numbering rather than two."),

 dict(q="Which item in EK 5.8.A.1's list is not a process at all, but a condition affecting how the processes turn out?",
   choices=[
     "The incumbency advantage phenomenon",
     "Open and closed primaries",
     "Caucuses",
     "Party conventions",
     "General presidential elections"], ans=0,
   why="EK 5.8.A.1.i names benefits current officeholders possess over challengers, which is an advantage a candidate carries into any of the processes rather than a stage of the election. The framework's own sentence covers 'the process and outcomes', which is why a condition belongs on the list."),

 dict(q="How does EK 5.8.A.1's list relate to EK 5.9.A.1's list for congressional elections?",
   choices=[
     "Both lists include the incumbency advantage phenomenon, open and closed primaries, and caucuses, while only the presidential list includes party conventions and the Electoral College",
     "The two lists are identical",
     "The two lists have nothing in common",
     "Only the congressional list includes primaries",
     "Only the presidential list includes the incumbency advantage phenomenon"], ans=0,
   why="EK 5.9.A.1 names the incumbency advantage phenomenon, open and closed primaries, caucuses, and general elections, while EK 5.8.A.1 adds party conventions and the Electoral College. The overlap is what the two kinds of election share and the difference is what is distinctive about choosing a president."),

 dict(q="According to EK 5.8.B.1, who decides how a state's electors are allocated?",
   choices=[
     "The state itself",
     "Congress",
     "The Supreme Court",
     "The national party organizations",
     "The Electoral College"], ans=0,
   why="EK 5.8.B.1's first clause is that states can choose how they allocate their electors. The allocation method is a state decision rather than a national rule, which is why methods differ across states."),

 dict(q="According to EK 5.8.B.1, how many states use a winner-take-all system?",
   choices=[
     "Most of them",
     "All of them",
     "About half of them",
     "A small minority of them",
     "None of them"], ans=0,
   why="EK 5.8.B.1's word is MOST. It is what makes the first clause more than decoration: if every state used the same method, the freedom to choose would have no observable consequence."),

 dict(q="Why do the framework's two clauses about allocation depend on each other?",
   choices=[
     "Because the freedom to choose a method would have no visible consequence if every state chose the same one, and MOST records that not all do",
     "Because the framework says all states choose winner-take-all",
     "Because Congress sets the method for every state",
     "Because the two clauses contradict each other",
     "Because states may not change their method once chosen"], ans=0,
   why="EK 5.8.B.1 says states CAN CHOOSE and that MOST use winner-take-all, so the second clause is what shows the first is exercised differently in different places. Reading MOST as ALL would make the first clause idle."),

 dict(q="According to EK 5.8.B.1, what is the relationship between the Electoral College result and the nationwide popular vote?",
   choices=[
     "The results may not be the same",
     "The results are never the same",
     "The results are always the same",
     "The results are the same only in presidential election years",
     "The framework does not compare them"], ans=0,
   why="EK 5.8.B.1's phrase is 'may not be the same as the popular vote nationwide'. The modal states a possibility, so neither a claim that they always agree nor one that they always differ is the framework's."),

 dict(q="According to EK 5.8.B.1, what follows from the possibility that the two results differ?",
   choices=[
     "There is an ongoing debate over the Electoral College",
     "The Electoral College result is set aside",
     "Congress must resolve the difference",
     "The popular vote determines the outcome",
     "A new election is held"], ans=0,
   why="EK 5.8.B.1's final clause records an ONGOING DEBATE and nothing more. The framework reports that people disagree without saying who is right or what should follow."),

 dict(q="What position does the course framework take in the debate it describes over the Electoral College?",
   choices=[
     "None; it records that the debate is ongoing without endorsing either side",
     "That the Electoral College should be abolished",
     "That the Electoral College should be retained",
     "That the debate has been settled",
     "That the debate concerns only small states"], ans=0,
   why="EK 5.8.B.1 says there IS an ongoing debate, which is a report about the state of argument rather than a contribution to it. Supplying a position would present one side to a student with the framework's authority behind it."),

 dict(q="The suggested skill for this topic is articulating a defensible claim. What two things does a defensible claim require?",
   choices=[
     "That it takes a position, and that available evidence could support it",
     "That it is widely believed, and that it is short",
     "That it restates a fact, and that the fact is verifiable",
     "That it is controversial, and that it is unprovable",
     "That it names a source, and that the source is recent"], ans=0,
   why="A claim that takes no position is a restatement rather than a thesis, and a position no evidence could reach is not defensible however firmly it is held. Skill 5.A names both halves in the word DEFENSIBLE."),

 dict(q="Which of the following is a defensible claim rather than a restatement of fact?",
   choices=[
     "The method a state uses to allocate its electors shapes how much attention presidential campaigns give it",
     "Most states use a winner-take-all system to allocate electors",
     "States can choose how they allocate their electors",
     "The Electoral College is part of the presidential election process",
     "Presidential elections are held in the United States"], ans=0,
   why="The first option asserts a relationship that someone could dispute and that evidence could bear on, while the other four restate facts the framework states outright. Skill 5.A asks for a position, and a true sentence is not thereby a thesis."),

 dict(q="Which of the following is a position that available evidence could NOT establish, and so is not a defensible claim in the skill's sense?",
   choices=[
     "The Electoral College is the only fair way to elect a president",
     "Winner-take-all allocation concentrates campaign attention on a limited number of states",
     "Caucuses draw lower participation than primaries",
     "Incumbency confers advantages that challengers do not have",
     "Nominating methods vary across states"], ans=0,
   why="Fairness is a standard rather than an observation, so no election data settles it, and the word ONLY makes the assertion stronger still. The other four options are claims or facts that evidence could address."),

 dict(q="A student writes the thesis: THE ELECTORAL COLLEGE EXISTS. What is the most important problem with it as a claim?",
   choices=[
     "It states a fact no one disputes, so there is nothing for evidence to support",
     "It is too long to serve as a thesis",
     "It takes a position that cannot be defended",
     "It names no source",
     "It concerns presidential rather than congressional elections"], ans=0,
   why="Skill 5.A asks for a claim that could be defended, which presupposes that it could also be denied. A statement everyone accepts leaves an argument with nothing to do."),

 dict(q="Which of the following claims about the Electoral College could a student defend without the course framework itself taking a side in the debate?",
   choices=[
     "The allocation method a state chooses affects how a candidate's popular support in that state translates into electoral votes",
     "The Electoral College should be replaced by a national popular vote",
     "The Electoral College should be preserved in its current form",
     "The Electoral College debate has been resolved",
     "The Electoral College produces the correct result in every election"], ans=0,
   why="The first option is a claim about how the mechanism works, which evidence can address and which EK 5.8.B.1 supports by saying states choose their method. The second and third are the two sides of the debate the framework records without joining."),

 dict(q="Which of EK 5.8.A.1's six items does LO 5.8.B single out for its own objective?",
   choices=[
     "The Electoral College",
     "Party conventions",
     "Caucuses",
     "Open and closed primaries",
     "The incumbency advantage phenomenon"], ans=0,
   why="EK 5.8.A.1.vi names the Electoral College among the six, and LO 5.8.B then asks specifically how it affects presidential elections. The topic gives it a second objective because EK 5.8.B.1 has more to say about it than a list entry could carry."),

 dict(q="Which of the following does EK 5.8.B.1 NOT state?",
   choices=[
     "Whether the Electoral College should be changed",
     "That states can choose how they allocate their electors",
     "That most states use a winner-take-all system",
     "That the Electoral College result may differ from the nationwide popular vote",
     "That there is an ongoing debate over the Electoral College"], ans=0,
   why="EK 5.8.B.1 describes how allocation works, notes a possible divergence and reports a debate. Every other option restates part of its two sentences, and the one thing it withholds is a verdict."),

 dict(q="Why is it important that EK 5.8.B.1 uses MAY NOT BE THE SAME rather than a stronger phrase?",
   choices=[
     "Because a divergence between the two results is possible rather than routine, and the framework's own wording says only that much",
     "Because the framework is uncertain whether elections occur",
     "Because the two results are always different",
     "Because the two results are always identical",
     "Because the phrase refers to congressional elections"], ans=0,
   why="MAY NOT BE THE SAME states a possibility, which is a weaker claim than either always agreeing or always differing. It is also the premise of the debate the sentence goes on to record, and overstating it would misrepresent what the disagreement is about."),

 dict(q=_NOMINATING + " Which conclusion is best supported by the data?",
   table=_NOMINATING_TABLE,
   choices=[
     "Caucuses are used by the fewest states and draw the lowest average participation, under a third of either primary method's",
     "Caucuses are used by the most states",
     "Closed primaries draw the highest average participation",
     "Every method draws similar average participation",
     "Open primaries are used by fewer states than caucuses"], ans=0,
   why="Caucuses appear in 6 states, tied for fewest, with 8 percent participation against 31 for open primaries and 27 for closed. Open primaries are used by 21 states, the most in the table."),

 dict(q=_NOMINATING + " Which framework definitions do the first three rows correspond to?",
   table=_NOMINATING_TABLE,
   choices=[
     "EK 5.8.A.1.ii's open and closed primaries as voting processes, and EK 5.8.A.1.iii's caucuses as closed meetings of party members",
     "EK 5.8.B.1's allocation of electors",
     "EK 5.8.A.1.i's incumbency advantage phenomenon",
     "EK 5.3.A.1's four linkage institutions",
     "EK 5.2.A.2's influences on voter turnout"], ans=0,
   why="The rows are open primary, closed primary and caucus, which are the framework's own second and third items. EK 5.8.A.1.iii's definition of a caucus as a meeting participants attend is one reason a participation gap of that size is unsurprising."),

 dict(q=_NOMINATING + " Which of the following is a defensible claim that this data could support?",
   table=_NOMINATING_TABLE,
   choices=[
     "The nominating method a state uses is associated with how large a share of its eligible voters takes part",
     "Caucuses are used by six states",
     "States should abandon caucuses in favor of primaries",
     "Open primaries produce better nominees than closed primaries",
     "Participation in nominating contests has fallen over time"], ans=0,
   why="The first option asserts a relationship between two columns of the table, which is both a position and one this evidence bears on. The second restates a figure, the third and fourth take positions the data cannot settle, and the fifth concerns a trend the table does not report."),

 dict(q=_ELECTORS + " Which conclusion is best supported by the data?",
   table=_ELECTORS_TABLE,
   choices=[
     "Three of the four states use winner-take-all, and in two of those the leading candidate took every elector with about half the state's popular vote",
     "All four states use winner-take-all",
     "The state with the most electoral votes allocates them by congressional district",
     "The leading candidate won more than seventy percent of the popular vote in every state",
     "Every state allocates its electors by congressional district"], ans=0,
   why="States A, B and D use winner-take-all and State C allocates by congressional district, and the leading candidate's share is 51 and 50 percent in States A and B. State A has the most electoral votes at 38 and uses winner-take-all."),

 dict(q=_ELECTORS + " Which statement in the course framework does this table most directly illustrate?",
   table=_ELECTORS_TABLE,
   choices=[
     "EK 5.8.B.1's statement that states can choose how they allocate their electors and that most use a winner-take-all system",
     "EK 5.8.A.1.iii's definition of a caucus",
     "EK 5.8.A.1.i's incumbency advantage phenomenon",
     "EK 5.5.A.2's incorporation of third-party agendas",
     "EK 5.2.A.4's factors influencing voter choice"], ans=0,
   why="The allocation column shows two different methods in use across four states, which is the framework's CAN CHOOSE, and three of the four use the same one, which is its MOST. Nothing here concerns nominating processes or a candidate's advantages."),

 dict(q=_ELECTORS + " Which of the following is a defensible claim about the Electoral College that this data could support?",
   table=_ELECTORS_TABLE,
   choices=[
     "Under a winner-take-all rule, a state's entire bloc of electors can be awarded on the strength of a narrow popular margin",
     "The Electoral College should be abolished",
     "The Electoral College should be preserved",
     "State A has 38 electoral votes",
     "Winner-take-all allocation is unfair to voters in the minority"], ans=0,
   why="State A awards all 38 of its electors to a candidate with 51 percent of its popular vote and State B all 29 with 50 percent, so the first option is a position this evidence supports. The second, third and fifth take sides in the debate EK 5.8.B.1 records without joining, and the fourth restates a figure."),
]
