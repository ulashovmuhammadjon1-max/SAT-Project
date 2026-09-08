# AP U.S. HISTORY 8.3 The Red Scare  (title copied from US_HISTORY_topics.json)
# Unit 8, Period 8: 1945 to 1980. Thematic focus NAT, American and National Identity.
# Reasoning process: causation. Suggested skill 2.B, explain the point of view, purpose,
# historical situation, and/or audience of a source.
#
# THE REQUIRED COURSE CONTENT OF THIS TOPIC, in the framework's own words:
#
#   Unit 8 Learning Objective C
#       Explain the causes and effects of the Red Scare after World War II.
#
#   KC-8.1.II.A  Americans debated policies and methods designed to expose suspected
#                communists within the United States even as both parties supported the
#                broader strategy of containing communism.
#
#   THEMATIC FOCUS, American and National Identity (NAT), printed on this topic's page:
#                The development of and debates about democracy, freedom, citizenship,
#                diversity, and individualism shape American national identity, cultural
#                values, and beliefs about American exceptionalism, and in turn, these
#                ideas shape political institutions and society. Throughout American
#                history, notions of national identity and culture have coexisted with
#                varying degrees of regional and group identities.
#
# ONE SENTENCE OF HISTORICAL DEVELOPMENT IS ALL THIS TOPIC PRINTS, so two further
# framework sentences are used, and only where a question needs the surrounding structure
# the topic page assumes:
#   KC-8.1.II    Cold War policies led to public debates over the power of the federal
#                government and acceptable means for pursuing international and domestic
#                goals while protecting civil liberties.
#                -- the PARENT of KC-8.1.II.A, printed in the Unit 8 preview at topic 8.1.
#                It is what makes this topic a topic about causes: the Red Scare's debates
#                are the domestic case of the debates that sentence describes.
#   KC-8.1.I     United States policymakers engaged in a cold war with the authoritarian
#                Soviet Union ... -- cited only to mark the contrast KC-8.1.II.A itself
#                draws between measures at home and the broader strategy abroad.
#
# WHAT IS DELIBERATELY NOT KEYED. This topic invites strong general knowledge and live
# political disagreement, and the framework's own sentence is careful: it says Americans
# DEBATED the policies and methods, and that BOTH parties supported containment. So no key
# here rules on whether any method was justified, names a senator, a committee, a hearing
# or a case, or attributes a position to a party. The framework's sentence records a
# disagreement; keying one side of it would be exactly the guess HISTORY_BRIEF.md forbids.
#
# NO FIGURES: the three data items carry a table= and every figure in them is labelled
# hypothetical in the stem. PROSE ONLY; spans are written "1945 to 1980".
# FIVE choices (A-E). Invented sources are marked hypothetical.
TOPIC = ("8.3", "The Red Scare", 8)

_T_POSITIONS = dict(
    headers=["Speaker in a hypothetical set of statements",
             "Position recorded on containing communism abroad",
             "Position recorded on a proposed method of exposing suspected communists at home"],
    rows=[["Speaker 1", "Supports", "Supports"],
          ["Speaker 2", "Supports", "Opposes"],
          ["Speaker 3", "Supports", "Supports only with limits"],
          ["Speaker 4", "Supports", "Opposes"]])

_T_CASES = dict(
    headers=["Year (hypothetical record)",
             "Cases reviewed",
             "Cases closed with no finding against the person reviewed"],
    rows=[["1947", "120", "96"],
          ["1950", "260", "205"],
          ["1953", "310", "250"],
          ["1956", "180", "150"]])

_T_STATEMENTS = dict(
    headers=["Year (hypothetical record)",
             "Recorded statements supporting containment abroad (percent)",
             "Recorded statements criticising a domestic exposure method (percent)"],
    rows=[["1947", "91", "12"],
          ["1950", "93", "28"],
          ["1953", "90", "41"],
          ["1956", "92", "55"]])

QUESTIONS = [

 dict(q="Unit 8 Learning Objective C states what students should be able to explain about the "
        "Red Scare. What does the framework ask for?",
      choices=[
        "The causes and effects of the Red Scare after World War II",
        "The continuities and changes in Cold War policies from 1945 to 1980",
        "The point of view of every source produced during the Red Scare",
        "The extent to which the Red Scare reshaped national identity",
        "The causes of economic growth in the years after World War II"],
      ans=0,
      why="Unit 8 Learning Objective C reads 'Explain the causes and effects of the Red Scare "
          "after World War II.' The rejected options are Learning Objective B, a restatement of "
          "the suggested skill rather than an objective, Learning Objective Q's language about "
          "national identity, and Learning Objective D, each of which belongs to a different "
          "task of this unit."),

 dict(q="KC-8.1.II.A names what Americans debated. What does the framework say was at issue?",
      choices=[
        "Policies and methods designed to expose suspected communists within the United States",
        "Whether communism should be contained abroad at all",
        "Whether the United States should maintain an army in peacetime",
        "The wisdom of building a free-market global economy",
        "Whether the federal courts should be enlarged"],
      ans=0,
      why="KC-8.1.II.A states that Americans debated policies and methods designed to expose "
          "suspected communists within the United States. The sentence locates the disagreement "
          "in domestic exposure measures, and its second half says containment abroad was not "
          "what divided them; the remaining options name subjects the sentence does not raise."),

 dict(q="KC-8.1.II.A says that something was supported by both parties even while the debate "
        "went on. What was it?",
      choices=[
        "The broader strategy of containing communism",
        "The particular methods proposed for exposing suspected communists",
        "The removal of restrictions on political association",
        "A reduction in the power of the federal government",
        "The abolition of loyalty requirements for public employment"],
      ans=0,
      why="KC-8.1.II.A ends 'even as both parties supported the broader strategy of containing "
          "communism', so the shared ground is the strategy abroad. The methods at home are "
          "precisely what the first half of the sentence says was debated, and the other options "
          "name positions the sentence attributes to nobody."),

 dict(q="KC-8.1.II.A joins its two halves with the words 'even as'. What relation does that "
        "phrase establish between them?",
      choices=[
        "The disagreement over domestic methods ran at the same time as agreement on the broader "
        "strategy",
        "The disagreement over domestic methods ended once agreement on the strategy was reached",
        "Agreement on the strategy followed only after the domestic debate was settled",
        "The two halves describe the same dispute stated twice",
        "The disagreement and the agreement belong to different decades"],
      ans=0,
      why="'Even as' marks simultaneity together with contrast, so KC-8.1.II.A describes "
          "Americans disagreeing about domestic exposure measures at the same time as both "
          "parties supported containment. Reading it as a sequence in either direction, or as a "
          "repetition, loses the tension the sentence is built to record."),

 dict(q="KC-8.1.II.A speaks of exposing SUSPECTED communists. What does that word do in the "
        "sentence?",
      choices=[
        "It makes the target of the measures a matter of suspicion rather than of established "
        "fact",
        "It establishes that everyone investigated was in fact a communist",
        "It establishes that no one investigated was in fact a communist",
        "It restricts the sentence to people outside the United States",
        "It shows that the framework treats the measures as uncontroversial"],
      ans=0,
      why="KC-8.1.II.A describes measures 'designed to expose suspected communists', which "
          "describes whom the measures were aimed at without asserting what was found. The "
          "framework makes no finding either way about those investigated, restricts the "
          "measures to people within the United States, and reports the measures as debated "
          "rather than as accepted."),

 dict(q="KC-8.1.II.A places the exposure measures it describes in a particular place. Where?",
      choices=[
        "Within the United States",
        "Among allied governments abroad",
        "Inside the Soviet Union",
        "In the newly independent nations",
        "The sentence does not say"],
      ans=0,
      why="KC-8.1.II.A says the measures were designed to expose suspected communists 'within "
          "the United States', which is the contrast the sentence then draws with the broader "
          "strategy of containing communism abroad. The location is stated, so the last option "
          "is false, and none of the other places appears in the sentence."),

 dict(q="KC-8.1.II, the sentence beneath which KC-8.1.II.A sits in this unit, says Cold War "
        "policies led to public debates. What does that establish about the Red Scare's causes?",
      choices=[
        "That the debates over domestic measures arose from Cold War policies rather than "
        "independently of them",
        "That the debates over domestic measures caused the Cold War policies",
        "That the debates had no connection to Cold War policy",
        "That the debates concerned only the conduct of foreign policy",
        "That the framework offers no account of why the debates arose"],
      ans=0,
      why="KC-8.1.II states that Cold War policies led to public debates over the power of the "
          "federal government and acceptable means for pursuing international and domestic goals "
          "while protecting civil liberties, and KC-8.1.II.A is the domestic case of those "
          "debates. The direction of the framework's sentence runs from policy to debate, which "
          "is what Unit 8 Learning Objective C asks students to explain."),

 dict(q="Which pairing correctly matches KC-8.1.II.A's two halves to what they record?",
      choices=[
        "The first half records a disagreement among Americans, and the second records a point on "
        "which both parties agreed",
        "The first half records a point on which both parties agreed, and the second records a "
        "disagreement among Americans",
        "Both halves record disagreements",
        "Both halves record points of agreement",
        "Neither half records anything about agreement or disagreement"],
      ans=0,
      why="KC-8.1.II.A opens with Americans debating policies and methods of domestic exposure "
          "and closes with both parties supporting the broader strategy of containing communism, "
          "so the order is disagreement first and agreement second. Reversing them, or making "
          "both halves alike, misstates a sentence whose whole point is that the two coexisted."),

 dict(q="Which claim about the period does KC-8.1.II.A NOT support?",
      choices=[
        "The two major parties differed with each other over whether communism should be "
        "contained",
        "Americans disagreed about how suspected communists should be exposed",
        "Support for containing communism extended across both parties",
        "The exposure measures at issue were directed at people within the United States",
        "Debate over the exposure measures and support for containment occurred together"],
      ans=0,
      why="KC-8.1.II.A says the opposite of the first statement: both parties supported the "
          "broader strategy of containing communism, so containment was not what divided them. "
          "The four rejected statements each restate a part of the same sentence in nearly the "
          "framework's own words."),

 dict(q="The thematic focus printed on this topic's page concerns American and National "
        "Identity. According to that statement, what shapes American national identity and "
        "cultural values?",
      choices=[
        "The development of and debates about democracy, freedom, citizenship, diversity, and "
        "individualism",
        "The size of the federal budget and the balance of foreign trade",
        "The distribution of population between city and countryside",
        "The technologies available in each period",
        "The decisions of the executive branch alone"],
      ans=0,
      why="The thematic focus statement for American and National Identity, printed in this "
          "topic's Required Course Content, says the development of and debates about democracy, "
          "freedom, citizenship, diversity, and individualism shape American national identity, "
          "cultural values, and beliefs about American exceptionalism. A debate over acceptable "
          "means at home, which is what KC-8.1.II.A records, is a debate of exactly that kind."),

 dict(q="The suggested skill printed beside this topic is 2.B. How does the framework state it?",
      choices=[
        "Explain the point of view, purpose, historical situation, or audience of a source",
        "Explain the significance of a source's point of view, purpose, historical situation, or "
        "audience, including how these might limit the use or uses of a source",
        "Compare the arguments or main ideas of two sources",
        "Support an argument using specific and relevant evidence",
        "Identify patterns among or connections between historical developments and processes"],
      ans=0,
      why="Skill 2.B, printed beside this topic as the skill students practise in meeting Unit 8 "
          "Learning Objective C, asks them to explain the point of view, purpose, historical "
          "situation, and audience of a source. Skill 2.C, the near neighbour, adds the further "
          "step of explaining how those features might limit a source's use; the rest are other "
          "skills of this course."),

 dict(q="A hypothetical pamphlet of 1950, printed by an association of employers, argues that "
        "checks on employees' political associations protect the firms that adopt them. Applying "
        "skill 2.B, what is the pamphlet's point of view best described as?",
      choices=[
        "That of an interested party arguing from the position of employers who would apply the "
        "checks",
        "That of a court weighing the lawfulness of the checks",
        "That of the employees whose associations would be examined",
        "That of a foreign government observing the United States",
        "The pamphlet has no point of view, since it states a policy"],
      ans=0,
      why="KC-8.1.II.A records Americans debating policies and methods designed to expose "
          "suspected communists within the United States, and a pamphlet written by one side of "
          "that debate speaks from a position within it. Skill 2.B asks a student to name that "
          "position: the authors are the parties who would apply the checks, not the courts, the "
          "employees or an outside observer, and every argument is made from somewhere."),

 dict(q="A hypothetical circular of 1953 was distributed to the staff of a government "
        "department, setting out what employees must report about their own associations. "
        "Applying skill 2.B, what is its audience, and what does that tell a reader about the "
        "document?",
      choices=[
        "Its audience is the department's own employees, so it shows what the government was "
        "asking of people it employed rather than what the public was told",
        "Its audience is the general public, so it shows what the government wished voters to "
        "believe",
        "Its audience is a foreign government, so it is a document of diplomacy",
        "Its audience cannot be determined from a circular",
        "Its audience is the courts, so it is a legal filing"],
      ans=0,
      why="Skill 2.B asks students to explain a source's audience, and the audience here is "
          "stated by the document's own circulation. KC-8.1.II.A places the policies and methods "
          "under debate within the United States, and an internal instruction is evidence of what "
          "was required of employees rather than of what was said publicly."),

 dict(q="A hypothetical open letter of 1954 asks a legislature to narrow a procedure used to "
        "question people about their political associations. Applying skill 2.B, what is the "
        "letter's purpose?",
      choices=[
        "To persuade lawmakers to change a procedure, which makes it an argument for a position "
        "in the debate rather than a neutral description of one",
        "To record for historians what the procedure was",
        "To announce that the procedure has already been changed",
        "To defend the procedure against its critics",
        "To describe the international situation of the United States"],
      ans=0,
      why="KC-8.1.II.A records that Americans debated the policies and methods designed to expose "
          "suspected communists, and a letter urging a legislature to narrow such a procedure is "
          "one contribution to that debate. Skill 2.B asks for purpose, and the purpose of a "
          "petition to change something is persuasion, which is different from recording, "
          "announcing or defending."),

 dict(q="The table records hypothetical statements by four speakers. Which conclusion does the "
        "table alone support?",
      table=_T_POSITIONS,
      choices=[
        "All four speakers are recorded as supporting containment abroad while dividing over the "
        "method proposed at home",
        "The speakers divide over containment abroad as well as over the method at home",
        "All four speakers take the same recorded position on the method at home",
        "Every speaker recorded as opposing the method at home is also recorded as opposing "
        "containment",
        "No speaker is recorded as supporting the method at home"],
      ans=0,
      why="KC-8.1.II.A states that Americans debated policies and methods designed to expose "
          "suspected communists within the United States even as both parties supported the "
          "broader strategy of containing communism, which is agreement on one axis alongside "
          "disagreement on another. The speakers are hypothetical and every reading offered is "
          "recomputed from the table alone in the verifier."),

 dict(q="Using the hypothetical record of case reviews, which statement does the table support?",
      table=_T_CASES,
      choices=[
        "Cases reviewed rise to a peak and then fall, and in every year recorded more than three "
        "quarters of them closed with no finding against the person reviewed",
        "Cases reviewed rise in every year recorded",
        "Cases reviewed fall in every year recorded",
        "In every year recorded, fewer than half of the cases closed with no finding",
        "The number closed with no finding exceeds the number reviewed in at least one year"],
      ans=0,
      why="KC-8.1.II.A describes measures aimed at SUSPECTED communists, a word that describes "
          "whom the measures targeted without asserting what was found, so a record in which most "
          "reviews close without a finding is consistent with the framework rather than a "
          "correction of it. The figures are hypothetical and both the shape of the series and "
          "the proportion are recomputed from the table alone."),

 dict(q="Using the hypothetical record of recorded statements, which conclusion does the table "
        "support?",
      table=_T_STATEMENTS,
      choices=[
        "Support for containment abroad holds near the same high level in every year recorded, "
        "while criticism of the domestic method rises in every year",
        "Support for containment abroad falls sharply while criticism of the domestic method "
        "rises",
        "Both recorded shares hold near the same level across the record",
        "Criticism of the domestic method falls in at least one year recorded",
        "Support for containment abroad is recorded below half in at least one year"],
      ans=0,
      why="KC-8.1.II.A pairs continuing support for the broader strategy of containing communism "
          "with debate over the methods used at home, so a record in which one share is steady "
          "and the other moves is the shape that sentence describes. The figures are hypothetical "
          "and the steadiness of the first column, the rise of the second and the falsity of "
          "every rejected reading are recomputed from the table alone."),

 dict(q="A hypothetical broadcast script of 1951 defends a proposed exposure measure by arguing "
        "that the danger abroad requires vigilance at home. Which relation described in this "
        "topic's content does the argument rest on?",
      choices=[
        "The relation KC-8.1.II draws between Cold War policies and public debates over "
        "acceptable means at home",
        "The relation KC-8.1.II.A denies between containment and party division",
        "A relation between economic growth and domestic politics",
        "A relation between immigration and national identity",
        "A relation the framework says does not exist"],
      ans=0,
      why="KC-8.1.II states that Cold War policies led to public debates over the power of the "
          "federal government and acceptable means for pursuing international and domestic goals "
          "while protecting civil liberties, which is precisely the step from danger abroad to "
          "measures at home that the script makes. KC-8.1.II.A records that containment itself "
          "was not the dividing question."),

 dict(q="A hypothetical diary kept by a civil servant in 1952 records private doubts about a "
        "procedure the writer administered at work. Applying skill 2.B, what does the source's "
        "historical situation contribute?",
      choices=[
        "It was written by someone inside the procedure while it was being applied, which is "
        "evidence about how it was experienced at the time",
        "It was written privately, which means it cannot be evidence of anything public",
        "It was written by an official, so it can only report official policy",
        "It was written during the period, which makes it less useful than a later account",
        "Its situation cannot be determined from a private document"],
      ans=0,
      why="Skill 2.B asks for a source's historical situation, and this one is written from "
          "inside a procedure while it operated. KC-8.1.II.A records that Americans debated the "
          "methods designed to expose suspected communists, and a private record of doubt is one "
          "trace of that debate; being private, official or contemporary does not by itself "
          "disqualify a source."),

 dict(q="Which of the following would be the strongest evidence that the debates KC-8.1.II.A "
        "describes reached beyond a single institution?",
      choices=[
        "Statements arguing over the exposure methods drawn from several different kinds of "
        "organisation across the country",
        "A single long speech setting out one side of the argument",
        "A record of how one department administered its own procedure",
        "A count of how many people worked for the federal government",
        "A summary of foreign policy toward the Soviet Union"],
      ans=0,
      why="KC-8.1.II.A attributes the debate to Americans generally rather than to one body, so "
          "evidence of breadth has to come from more than one place. A single speech, one "
          "department's practice, an employment total and a summary of foreign policy each speak "
          "to something narrower than the claim, and the last concerns the strategy the sentence "
          "says both parties supported."),

 dict(q="A hypothetical study argues that the Red Scare had no causes outside the ambitions of "
        "the people who led it. Which sentence of this unit most directly qualifies that "
        "argument?",
      choices=[
        "KC-8.1.II, which says Cold War policies led to public debates over acceptable means for "
        "pursuing international and domestic goals",
        "KC-8.1.II.A, which says both parties supported the broader strategy of containing "
        "communism",
        "KC-8.1.I, which names the aims of United States policymakers",
        "Unit 8 Learning Objective C, which states the task rather than a development",
        "The thematic focus statement for American and National Identity"],
      ans=0,
      why="KC-8.1.II supplies a cause outside the motives of individuals by making Cold War "
          "policies the source of the public debates, which is what an argument from ambition "
          "alone leaves out, and Unit 8 Learning Objective C asks for causes. The other "
          "statements are true of the topic but do not by themselves name a cause of the "
          "debates."),

 dict(q="What effect of the Red Scare does this unit's content most directly support?",
      choices=[
        "Public debate over the power of the federal government and over acceptable means for "
        "pursuing domestic goals while protecting civil liberties",
        "The abandonment of the strategy of containing communism",
        "The removal of the federal government from domestic policy",
        "An agreement among Americans about the methods to be used at home",
        "The end of debate about national identity"],
      ans=0,
      why="KC-8.1.II names public debates over the power of the federal government and acceptable "
          "means for pursuing international and domestic goals while protecting civil liberties, "
          "and KC-8.1.II.A is the domestic instance of them. Containment was supported by both "
          "parties rather than abandoned, and the framework records disagreement about methods "
          "rather than agreement."),

 dict(q="A hypothetical newspaper advertisement of 1949 urges readers to report neighbours whose "
        "opinions they find suspicious. Applying skill 2.B, what is its intended audience?",
      choices=[
        "The general reading public, whom it asks to act",
        "Members of the legislature, whom it asks to pass a law",
        "Employees of a single firm, whom it instructs",
        "A foreign readership, whom it seeks to impress",
        "Historians, for whom it records the period"],
      ans=0,
      why="Skill 2.B asks students to explain a source's audience, and an advertisement placed in "
          "a newspaper and addressed to readers is aimed at the reading public. KC-8.1.II.A "
          "places the policies and methods under debate within the United States, and an appeal "
          "for ordinary people to take part is one of the methods that was debated."),

 dict(q="Two hypothetical statements from 1951, one urging wider use of an exposure procedure "
        "and one urging its restriction, both open by affirming that communism must be contained "
        "abroad. What does that shared opening best illustrate?",
      choices=[
        "The agreement on the broader strategy that KC-8.1.II.A says accompanied the domestic "
        "disagreement",
        "That the two statements were written by the same author",
        "That the disagreement between them was not genuine",
        "That containment abroad was itself the subject of the dispute",
        "That neither author held a position on domestic measures"],
      ans=0,
      why="KC-8.1.II.A records Americans debating domestic exposure measures 'even as both "
          "parties supported the broader strategy of containing communism', so a shared premise "
          "beneath opposed conclusions is exactly what the sentence describes. A common opening "
          "shows nothing about authorship, does not make the disagreement false, and the "
          "statements plainly do take opposed positions on the method."),

 dict(q="Why does KC-8.1.II.A's second half matter for explaining the Red Scare's causes?",
      choices=[
        "Because it rules out party disagreement over containment as the source of the dispute, "
        "leaving the means used at home as what was contested",
        "Because it shows the dispute was about foreign policy after all",
        "Because it shows one party opposed containment",
        "Because it shows the dispute had no causes at all",
        "Because it dates the dispute to the years before 1945"],
      ans=0,
      why="KC-8.1.II.A says both parties supported the broader strategy of containing communism, "
          "which removes the obvious partisan explanation and directs attention to the policies "
          "and methods at home that the first half of the sentence says were debated. Unit 8 "
          "Learning Objective C asks for causes, and eliminating a candidate cause is part of "
          "supplying one."),

 dict(q="A hypothetical school board resolution of 1953 requires teachers to sign a statement "
        "about their political associations. Which part of KC-8.1.II.A does the resolution most "
        "directly exemplify?",
      choices=[
        "A method designed to expose suspected communists within the United States",
        "The broader strategy of containing communism abroad",
        "A measure directed at people outside the United States",
        "An aim of building an international security system",
        "A means of creating a free-market global economy"],
      ans=0,
      why="KC-8.1.II.A describes policies and methods designed to expose suspected communists "
          "within the United States, and a requirement that employees declare their associations "
          "is such a method. The remaining options belong to KC-8.1.I's account of aims pursued "
          "abroad, which is the part of the framework KC-8.1.II.A contrasts with the domestic "
          "measures."),

 dict(q="A hypothetical account written in 1975 looks back on the period and treats the whole "
        "controversy as settled. Applying skill 2.B, what does its historical situation most "
        "directly explain about it?",
      choices=[
        "It was written long after the events, so it reports how the period was understood later "
        "rather than how it appeared at the time",
        "It was written long after the events, so it reports the period more accurately than any "
        "source from the period",
        "It was written in the United States, so it is not evidence about American opinion",
        "Its date makes it evidence about the 1940s rather than about the 1970s",
        "Its situation cannot be determined without knowing its author"],
      ans=0,
      why="Skill 2.B asks students to explain a source's historical situation, and a "
          "retrospective account is situated in the moment of writing as well as in the period "
          "described. KC-8.1.II.A records a debate that was live at the time, so a later verdict "
          "that it was settled is evidence about the later moment; distance neither guarantees "
          "accuracy nor removes a source from the historical record."),

 dict(q="Which statement best expresses how this topic connects a domestic development to the "
        "Cold War?",
      choices=[
        "Measures taken at home against suspected communists arose alongside a strategy of "
        "containing communism abroad that both parties supported",
        "Measures taken at home replaced the strategy of containing communism abroad",
        "The strategy abroad was adopted in order to end the debate at home",
        "The two developments belong to different periods of the course",
        "The framework treats the domestic measures as unrelated to the Cold War"],
      ans=0,
      why="KC-8.1.II.A places the debate over domestic exposure measures alongside both parties' "
          "support for the broader strategy of containing communism, and KC-8.1.II makes Cold War "
          "policies the source of such debates. Neither sentence has one displacing the other, "
          "and both place the developments in Period 8."),

 dict(q="A hypothetical study of the period counts only the statements of national politicians. "
        "Why might that fall short of what KC-8.1.II.A describes?",
      choices=[
        "The sentence attributes the debate to Americans generally, so a count confined to "
        "national politicians misses most of the people it names",
        "The sentence is about politicians only, so the study matches it exactly",
        "The sentence is about foreign governments, so politicians are irrelevant",
        "The sentence concerns a period the study does not cover",
        "The sentence makes no claim that any study could test"],
      ans=0,
      why="KC-8.1.II.A says that AMERICANS debated the policies and methods designed to expose "
          "suspected communists, and mentions both parties only for the point on which they "
          "agreed. A study restricted to national politicians therefore samples a fraction of the "
          "subject the sentence names, though it remains evidence about that fraction."),

 dict(q="Taken together, what do this topic's required sentence and its parent establish about "
        "the Red Scare?",
      choices=[
        "That it was a domestic argument about acceptable means, arising from Cold War policy and "
        "coexisting with agreement on containment",
        "That it was a partisan argument about whether to oppose communism at all",
        "That it was a foreign policy dispute with no domestic dimension",
        "That it produced agreement among Americans about the methods to be used",
        "That the framework offers no account of its causes or its effects"],
      ans=0,
      why="KC-8.1.II.A supplies the domestic argument about methods and the agreement on the "
          "broader strategy, and KC-8.1.II supplies the cause by making Cold War policies the "
          "source of public debates over acceptable means while protecting civil liberties. That "
          "combination is what Unit 8 Learning Objective C asks students to explain, and each "
          "rejected option contradicts one of the two sentences."),
]
