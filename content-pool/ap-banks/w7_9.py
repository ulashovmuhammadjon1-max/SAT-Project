# AP WORLD HISTORY: MODERN 7.9 Causation in Global Conflict
# CED effective Fall 2026, Unit 7 Global Conflict, c. 1900 to the present.
# Unit 7 Learning Objective I: explain the relative significance of the causes
# of global conflict in the period 1900 to the present. Reasoning process:
# causation. Suggested skill 6.D, corroborate, qualify, or modify an argument
# using diverse and alternative evidence in order to develop a complex argument;
# the CED prints four things such an argument might do: explain nuance of an
# issue by analyzing multiple variables; explain relevant and insightful
# connections within and across periods; explain the relative historical
# significance of a source's credibility and limitations; explain how or why a
# historical claim or argument is or is not effective.
#
# THIS IS THE UNIT'S REASONING TOPIC, AND IT IS WRITTEN AS ONE. The CED says so
# in its own words: "The final topic in this unit focuses on the skill of
# argumentation and so provides an opportunity for your students to draw upon
# the key concepts and historical developments they have studied in this unit.
# Using evidence relevant to this unit's key concepts, students should practice
# the suggested skill for this topic." So almost every item here presents an
# argument and asks what evidence would corroborate, qualify or modify it, or
# asks what a stated argument can and cannot establish. Fact recall is not the
# point and is confined to items 12, 13 and 14, which restate the review key
# concepts the CED prints in this topic's own box.
#
# THE REVIEW KEY CONCEPTS the CED prints for this topic, in the framework's own
# words:
#   KC-6.1       Rapid advances in science and technology altered the
#                understanding of the universe and the natural world and led to
#                advances in communication, transportation, industry,
#                agriculture, and medicine.
#   KC-6.2       Peoples and states around the world challenged the existing
#                political and social order in varying ways, leading to
#                unprecedented worldwide conflicts.
#   KC-6.2.I     The West dominated the global political order at the beginning
#                of the 20th century, but both land-based and maritime empires
#                gave way to new states by the century's end.
#   KC-6.2.I.A   The older, land-based Ottoman, Russian, and Qing empires
#                collapsed due to a combination of internal and external
#                factors. These changes in Russia eventually led to communist
#                revolution.
#   KC-6.2.II.D  States around the world challenged the existing political and
#                social order, including the Mexican Revolution that arose as a
#                result of political crisis.
# The rest of the unit's key concepts are also available to this topic by the
# CED's own instruction, and the ones used here are KC-6.2.IV.B.i and
# KC-6.2.IV.B.ii (the causes of the two wars), KC-6.1.III.C.i and
# KC-6.1.III.C.ii (technology, tactics and casualties), KC-6.2.I.B (interwar
# territorial holdings) and KC-6.2.III.C (mass atrocities).
#
# THE HONEST ANSWER ABOUT "RELATIVE SIGNIFICANCE", which is the whole difficulty
# of this topic and is stated here so no key rests on an author's own ranking:
# the framework ranks a cause exactly ONCE. KC-6.2.IV.B.ii writes "and
# especially" before the rise to power of fascist and totalitarian regimes.
# KC-6.2.IV.B.i lists the causes of the first war without ranking any of them.
# So every item about weighing causes either keys to that single "especially",
# or keys to a REASONING move that is checkable without a ranking -- a cause
# cannot follow its effect; a factor present where no war came does not on its
# own explain where war came; a correlation in a table does not fix a direction;
# an argument that omits a cause the framework states is incomplete. No item
# anywhere in this module asserts a ranking the CED does not print.
#
# WHAT IS DELIBERATELY NOT ASKED. No item keys to a date, a battle, a treaty
# clause, a leader beyond those the CED names elsewhere in the unit, or a
# casualty total. No item asks a student to rank the causes of the First World
# War against one another, because the framework supplies no ranking to check
# such an answer against.
#
# SOURCES. The bank cannot show images, so every stimulus is an explicitly
# unattributed illustrative argument or source described in prose, or a table of
# illustrative data whose keyed conclusion is recoverable from the table alone.
# Nothing is attributed to a real person or document.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md.
TOPIC = ("7.9", "Causation in Global Conflict", 7)

_T_VARIABLES = dict(
    headers=["State (illustrative)",
             "Colonial territories claimed in the decade before the conflict, of the twelve then in dispute",
             "Years since its most recent territorial dispute with a neighbour, within the preceding decade"],
    rows=[["State 1", "7", "9"],
          ["State 2", "3", "2"],
          ["State 3", "5", "4"]])

_T_INDICES = dict(
    headers=["Theatre of operations (illustrative)",
             "Index of new weapons in service",
             "Index of casualties per month",
             "Excess of the casualty index over the weapons index"],
    rows=[["Theatre 1", "100", "100", "0"],
          ["Theatre 2", "180", "210", "30"],
          ["Theatre 3", "260", "330", "70"]])

QUESTIONS = [
 dict(q="What does this topic's suggested skill ask a student to do with an argument?",
   choices=[
     "Corroborate, qualify, or modify it using diverse and alternative evidence",
     "Restate it more briefly without adding evidence of any kind",
     "Identify the evidence the argument's own author used and stop there",
     "Explain the point of view and purpose of the argument's author",
     "Situate the argument within a broader historical context"], ans=0,
   why="Suggested skill 6.D for this topic is to corroborate, qualify, or modify an argument using diverse and alternative evidence in order to develop a complex argument, and the CED directs students to practise it on evidence relevant to this unit's key concepts, KC-6.2 among them. The other options are skills the CED attaches to other topics."),
 dict(q="What does this topic's learning objective ask a student to explain?",
   choices=[
     "The relative significance of the causes of global conflict in the period 1900 to the present",
     "The causes of global conflict without weighing any of them against the others",
     "The consequences of global conflict, leaving its causes aside",
     "The methods by which governments conducted their wars",
     "The territorial holdings of imperial states between the two world wars"], ans=0,
   why="Unit 7 Learning Objective I asks students to explain the relative significance of the causes of global conflict in the period 1900 to the present. The two objectives the other options describe belong to Unit 7 Learning Objectives G and E, which are the business of topics 7.7 and 7.5."),
 dict(q="In which of the framework's two lists of the causes of a world war does it mark one cause as weightier than the rest?",
   choices=[
     "In the list for the Second World War, where one cause is introduced by the word 'especially'",
     "In the list for the First World War, where one cause is introduced by the word 'especially'",
     "In both lists, each of which marks one cause as weightier",
     "In neither list, since the framework never weighs one cause against another",
     "In neither list, since the framework gives no causes for either war"], ans=0,
   why="KC-6.2.IV.B.ii writes 'and especially' before the rise to power of fascist and totalitarian regimes, while KC-6.2.IV.B.i lists imperialist expansion, competition for resources, territorial and regional conflicts, a flawed alliance system and intense nationalism without ranking any of them. The anchor carries both halves because attaching the ranking to the wrong war is the plausible error."),
 dict(q="A student is asked to argue which cause of the First World War mattered most. What does the framework's own statement leave that student to do?",
   choices=[
     "Argue the ranking from evidence, because the framework lists those causes without ranking them",
     "Read the ranking off the framework, which states plainly which cause mattered most",
     "Decline the question, because the framework names no causes of that war at all",
     "Apply the ranking the framework gives for the Second World War to the First",
     "Rank the causes by the order in which the framework happens to list them"], ans=0,
   why="KC-6.2.IV.B.i names five things among the causes of World War I and orders none of them, while the single ranking the framework prints, in KC-6.2.IV.B.ii, belongs to the second war. Unit 7 Learning Objective I asks for relative significance, so where the framework supplies no ranking the argument has to be built rather than quoted."),
 dict(q="An unattributed essay argues that the two world wars had entirely separate origins with nothing in common. Which evidence from the framework most directly qualifies that argument?",
   choices=[
     "That the settlement of the first war appears among the causes of the second, and that imperialism appears in both lists of causes",
     "That the two wars were fought by different generations of soldiers",
     "That new military technology raised casualty levels in both wars",
     "That governments used propaganda to mobilize populations in both wars",
     "That both wars ended with a negotiated settlement of some kind"], ans=0,
   why="KC-6.2.IV.B.ii opens its list with the unsustainable peace settlement after World War I and includes continued imperialist aspirations, while KC-6.2.IV.B.i names imperialist expansion among the first war's causes. Suggested skill 6.D asks for connections across periods, and a shared cause plus a settlement carried forward is such a connection."),
 dict(q="An unattributed argument holds that new military technology is what caused the global conflicts of the twentieth century. Which observation about the framework most directly qualifies it?",
   choices=[
     "The framework names new technology as what raised casualty levels, and names other things among the causes of each war",
     "The framework denies that new military technology existed in this period",
     "The framework names new technology among the causes of each war and nothing else",
     "The framework treats casualty levels as unrelated to how the wars were fought",
     "The framework treats the two wars as having had no causes it can identify"], ans=0,
   why="KC-6.1.III.C.i and KC-6.1.III.C.ii attribute increased levels of wartime casualties to new military technology, and to new tactics in the second case, while KC-6.2.IV.B.i and KC-6.2.IV.B.ii give each war a separate list of causes in which technology does not appear. The argument therefore moves a factor from one role in the framework to another."),
 dict(q="An unattributed argument explains the outbreak of a global conflict entirely by the economic pressures acting on one state. Which addition would most improve it as a complex argument?",
   choices=[
     "Evidence on the political and territorial pressures acting on the same state, weighed alongside the economic ones",
     "A longer description of the same economic pressures already described",
     "A list of the commanders appointed by that state's army",
     "An account of the geography of the state's frontier regions",
     "A note that the argument's author held no official position"], ans=0,
   why="Suggested skill 6.D asks students to explain nuance of an issue by analyzing multiple variables, and KC-6.2.IV.B.i names territorial and regional conflicts, a flawed alliance system and intense nationalism alongside competition for resources. Adding a second kind of pressure is what turns a single-variable account into an argument about relative significance."),
 dict(q="Two unattributed sources make the same claim about why a war began: one was produced by a government that fought in it, the other by an observer from a state that stayed out. What does the second source add to an argument resting on the first?",
   choices=[
     "Corroboration from a source with a different interest in the outcome",
     "Proof that the claim is correct, since two sources cannot both be mistaken",
     "Nothing, because only a participant's account can be used as evidence",
     "Nothing, because two sources making the same claim are always one source",
     "A refutation of the claim, since the two sources come from different states"], ans=0,
   why="Suggested skill 6.D asks students to corroborate an argument using diverse and alternative evidence and to weigh the relative significance of a source's credibility and limitations. KC-6.2.IV.B.i and KC-6.2.IV.B.ii state the causes at issue, and agreement between sources with different interests strengthens a claim without settling it."),
 dict(q="An unattributed argument asserts that intense nationalism was the decisive cause of a war but offers no evidence connecting nationalism to anything that happened. Why is the argument ineffective as it stands?",
   choices=[
     "It names a cause the framework lists but never shows how that cause produced the outcome",
     "It names a cause the framework does not list anywhere",
     "It names a consequence rather than a cause",
     "It concerns a period the framework does not cover",
     "It rests on a source rather than on an argument"], ans=0,
   why="KC-6.2.IV.B.i does name intense nationalism among the things that combined to escalate tensions into global conflict, so the fault is not in the choice of cause. Suggested skill 6.D asks students to explain how or why a claim or argument is or is not effective, and an assertion with no connecting evidence cannot support a judgement of relative significance."),
 dict(q="A historian proposes that a particular development was among the causes of a war, and evidence then shows that the development began only after the fighting had started. What follows for the proposal?",
   choices=[
     "It fails, because a cause cannot come after the outcome it is offered to explain",
     "It stands, because the framework lists causes without regard to when they occurred",
     "It stands, because a development during a war is still part of its history",
     "It fails, because the framework names no causes for any war",
     "It cannot be assessed, because the framework gives no dates of any kind"], ans=0,
   why="KC-6.2.IV.B.i and KC-6.2.IV.B.ii present their items as causes of the wars that followed them, and Unit 7 Learning Objective I asks for the relative significance of causes. Ordering is the one test a causal claim must pass before its weight can be argued at all."),
 dict(q="A factor said to explain why war came to one state is then found to have been present in several states that did not go to war. What does that finding establish?",
   choices=[
     "That the factor does not on its own account for where war came, though it may still be among the causes",
     "That the factor played no part in any state and must be dropped from the account",
     "That the factor is the decisive cause in every state where it was present",
     "That the states which did not go to war must have been misidentified",
     "That the framework's lists of causes are inconsistent with one another"], ans=0,
   why="KC-6.2.IV.B.i describes causes that combined to escalate tensions into global conflict rather than any one factor acting alone, and suggested skill 6.D asks for nuance drawn from multiple variables. A factor present in cases with different outcomes narrows what it can be made to explain without removing it from the list."),
 dict(q="What relation does the framework state between the challenges peoples and states made to the existing order and the conflicts of this period?",
   choices=[
     "The challenges came first, and the framework describes them as leading to unprecedented worldwide conflicts",
     "The conflicts came first, and the framework describes them as leading to challenges to the existing order",
     "The framework describes the two as unconnected features of the same century",
     "The framework describes both as consequences of advances in science and technology",
     "The framework describes both as consequences of the collapse of the maritime empires"], ans=0,
   why="KC-6.2 states that peoples and states around the world challenged the existing political and social order in varying ways, leading to unprecedented worldwide conflicts. The participle fixes the direction, and the anchor carries both halves because the reversed reading is the plausible error."),
 dict(q="The framework calls the worldwide conflicts of this period 'unprecedented'. What does that word assert?",
   choices=[
     "That the conflicts were without precedent",
     "That the conflicts closely resembled earlier wars in scale and kind",
     "That the conflicts were expected by the states that fought them",
     "That the conflicts were confined to a single region",
     "That the conflicts left the existing political and social order unchanged"], ans=0,
   why="KC-6.2 describes the challenges to the existing political and social order as leading to unprecedented worldwide conflicts. The adjective is the framework's own and it places these conflicts outside what had come before rather than in a series with it."),
 dict(q="What does the framework attribute to the rapid advances in science and technology of this period?",
   choices=[
     "An altered understanding of the universe and the natural world, and advances in communication, transportation, industry, agriculture, and medicine",
     "The collapse of the older land-based empires and the formation of new states",
     "The political crisis from which the Mexican Revolution arose",
     "The maintenance of colonial holdings between the two world wars",
     "The rise of extremist groups to power"], ans=0,
   why="KC-6.1 states that rapid advances in science and technology altered the understanding of the universe and the natural world and led to advances in communication, transportation, industry, agriculture, and medicine. The other four options are the subjects of KC-6.2.I.A, KC-6.2.II.D, KC-6.2.I.B and KC-6.2.III.C."),
 dict(q="Science and technology appear in the framework both as the source of advances in industry and medicine and as what raised the level of wartime casualties. What can a student build from that pairing?",
   choices=[
     "An argument that one broad development is presented in the framework with more than one kind of consequence",
     "An argument that the framework contradicts itself and one of the two statements must be discarded",
     "An argument that the framework treats technology as having no consequences at all",
     "An argument that the framework treats industry and medicine as causes of the wars",
     "An argument that the framework treats casualties as unconnected to how wars were fought"], ans=0,
   why="KC-6.1 attributes advances in communication, transportation, industry, agriculture and medicine to rapid advances in science and technology, while KC-6.1.III.C.i and KC-6.1.III.C.ii attribute increased levels of wartime casualties to new military technology and, for the second war, new tactics. Suggested skill 6.D asks for nuance drawn from multiple variables, and a single development with consequences of two kinds is exactly that."),
 dict(q="An unattributed account explains the collapse of the older land-based empires entirely by pressure from other states. Which framework statement most directly modifies that account?",
   choices=[
     "That those empires collapsed due to a combination of internal and external factors",
     "That those empires collapsed due to external factors acting alone",
     "That those empires did not collapse at all in this period",
     "That those empires were maritime rather than land-based",
     "That those empires collapsed as a result of advances in medicine"], ans=0,
   why="KC-6.2.I.A states that the older, land-based Ottoman, Russian, and Qing empires collapsed due to a combination of internal and external factors. Suggested skill 6.D asks students to modify an argument with alternative evidence, and the internal half of that combination is the half the account leaves out."),
 dict(q="An unattributed argument holds that every challenge to an existing political and social order in this period was set off by a world war. Which framework statement most directly qualifies it?",
   choices=[
     "That the Mexican Revolution is described as arising as a result of political crisis",
     "That the Mexican Revolution is described as arising from a world war",
     "That no state challenged its existing political and social order in this period",
     "That challenges to the existing order are described as confined to Europe",
     "That challenges to the existing order are described as having no causes at all"], ans=0,
   why="KC-6.2.II.D states that states around the world challenged the existing political and social order, including the Mexican Revolution that arose as a result of political crisis. A challenge the framework traces to a crisis inside a state is a counterexample to an argument that traces every such challenge to a world war."),
 dict(q="The table below reports two illustrative measures for three states in the years before a conflict. An argument claims that the state with the most colonial claims was also the state with the most recent territorial dispute. What does the table show?",
   table=_T_VARIABLES,
   choices=[
     "The state with the most colonial claims is the state longest without a territorial dispute, so the two measures do not point to the same state",
     "The state with the most colonial claims is also the state with the most recent territorial dispute, as the argument says",
     "All three states record the same number of colonial claims",
     "All three states last had a territorial dispute in the same year",
     "Neither measure varies at all across the three states"], ans=0,
   why="Read from the table alone: ranking the states by colonial claims and ranking them by how recently they last had a territorial dispute put different states at the top, and in fact reverse each other. KC-6.2.IV.B.i names imperialist expansion and territorial conflicts as separate items among the causes of war, and suggested skill 6.D asks for nuance drawn from analysing more than one variable."),
 dict(q="The table below reports illustrative index numbers for new weapons in service and for casualties per month in three theatres, with the third column giving the amount by which the second index exceeds the first. Which conclusion is best supported?",
   table=_T_INDICES,
   choices=[
     "Both indices rise across the three theatres, and the casualty index rises faster, so the gap between them widens",
     "Both indices rise across the three theatres, and the gap between them narrows",
     "The casualty index falls as the weapons index rises",
     "The two indices are equal to one another in every theatre",
     "The weapons index rises while the casualty index stays the same throughout"], ans=0,
   why="Read from the table alone: both indices increase from theatre to theatre, the third column equals the second minus the first in every row, and those differences themselves increase. KC-6.1.III.C.ii states that new military technology and new tactics led to increased levels of wartime casualties, and a table of this kind is the sort of evidence an argument about that claim would rest on."),
 dict(q="An unattributed argument about why a war began rests entirely on a single document produced by one of the governments that fought it. What does that origin require of anyone using the argument?",
   choices=[
     "That the government's interest in the account be weighed, and other evidence sought before the argument is relied on",
     "That the argument be discarded, since a participant's document can never be evidence",
     "That the argument be accepted, since a participant knew the events at first hand",
     "That the argument be treated as settled unless a second document contradicts it word for word",
     "That the document's date be established and nothing further be asked of it"], ans=0,
   why="Suggested skill 6.D asks students to explain the relative historical significance of a source's credibility and limitations and to use diverse and alternative evidence. KC-6.2.IV.B.ii names the causes at issue, and a government that fought the war is an interested party whose account is a starting point rather than a conclusion."),
 dict(q="Which addition would do most to turn a simple claim about why a global conflict began into the complex argument the suggested skill describes?",
   choices=[
     "Evidence on more than one of the causes the framework names, with a statement of how they bore on one another",
     "A restatement of the same claim in stronger language",
     "A longer narrative of the fighting that followed the outbreak",
     "A list of the states that took part on each side",
     "A description of the weapons each side carried"], ans=0,
   why="Suggested skill 6.D asks students to explain nuance of an issue by analyzing multiple variables, and KC-6.2.IV.B.i itself describes territorial and regional conflicts combining with a flawed alliance system and intense nationalism. An argument that shows how named causes bore on one another is doing what the skill and the sentence both describe."),
 dict(q="An unattributed argument connects the imperial holdings kept between the wars to the imperial aspirations named among the causes of the second war. Which pair of framework statements supports that connection?",
   choices=[
     "The statement that imperial states predominantly maintained control over colonial holdings, and the statement naming continued imperialist aspirations among the second war's causes",
     "The statement that empires gave way to new states, and the statement that governments took a more active role in economic life",
     "The statement that new military technology raised casualties, and the statement that the Mexican Revolution arose from political crisis",
     "The statement that the West dominated the political order in 1900, and the statement that extremist groups rose to power",
     "The statement that World War I was the first total war, and the statement that the Soviet government used Five Year Plans"], ans=0,
   why="KC-6.2.I.B states that between the two world wars imperial states predominantly maintained control over colonial holdings, and KC-6.2.IV.B.ii names continued imperialist aspirations among the causes of World War II. Suggested skill 6.D asks for connections across periods, and these two sentences are the framework's own on either side of the connection."),
 dict(q="What does it mean, for this topic, to say that one cause of a conflict was more significant than another?",
   choices=[
     "That an argument has been made for the ranking, since the framework itself ranks a cause only where it writes 'especially'",
     "That the framework has stated the ranking in every case and it need only be quoted",
     "That the cause appears earlier in the framework's list than the other does",
     "That the cause is the one named in the greatest number of framework statements",
     "That the ranking cannot be discussed at all, since significance is a matter of opinion"], ans=0,
   why="Unit 7 Learning Objective I asks for the relative significance of the causes of global conflict, and the only ranking the framework prints is the 'especially' in KC-6.2.IV.B.ii; KC-6.2.IV.B.i lists its causes unranked. Where the framework supplies no ranking, suggested skill 6.D's diverse and alternative evidence is what a ranking has to rest on."),
 dict(q="An unattributed argument gathers only the evidence that agrees with its own conclusion. Which criticism follows most directly from this topic's suggested skill?",
   choices=[
     "It has not used diverse and alternative evidence, which is what the skill requires of a complex argument",
     "It has used evidence at all, where the skill asks for argument without evidence",
     "It has reached a conclusion, where the skill asks for arguments without conclusions",
     "It concerns causes, where the skill asks only about consequences",
     "It concerns a period the skill does not cover"], ans=0,
   why="Suggested skill 6.D asks students to corroborate, qualify, or modify an argument using diverse and alternative evidence in order to develop a complex argument, and the CED directs students to draw on this unit's key concepts, KC-6.2 and KC-6.2.IV.B.ii among them. Evidence selected for agreement cannot qualify or modify anything."),
 dict(q="Evidence is found that agrees with an argument's claim and comes from a source with no stake in it. Which of the skill's three operations has that evidence performed?",
   choices=[
     "It has corroborated the argument",
     "It has qualified the argument by narrowing its scope",
     "It has modified the argument by changing what it claims",
     "It has refuted the argument",
     "It has left the argument in exactly the state it was in before"], ans=0,
   why="Suggested skill 6.D names corroborating, qualifying and modifying as three distinct things evidence can do to an argument. KC-6.2.IV.B.i and KC-6.2.IV.B.ii supply the claims at issue in this unit, and independent evidence agreeing with a claim is the first of the three rather than the second or the third."),
 dict(q="Evidence is found showing that an argument's claim holds in some of the cases it covers but not in others. Which of the skill's three operations has that evidence performed?",
   choices=[
     "It has qualified the argument, narrowing the range of cases the claim covers",
     "It has corroborated the argument across all of its cases",
     "It has refuted the argument in every case it covers",
     "It has left the argument's scope exactly as it was",
     "It has replaced the argument's claim with an unrelated one"], ans=0,
   why="Suggested skill 6.D names corroborating, qualifying and modifying as three distinct operations. KC-6.2.I.B's own wording, that imperial states PREDOMINANTLY maintained control, is the framework doing the same thing to itself, and evidence that a claim holds in some cases and not others narrows its range rather than overturning it."),
 dict(q="Which research question would put this topic's learning objective and its suggested skill to work together?",
   choices=[
     "Which of the causes of global conflict after 1900 carried the most weight, and on what evidence",
     "Which states possessed the largest armies in each decade after 1900",
     "Which treaties were signed at the close of each conflict after 1900",
     "Which cities grew fastest in the states that went to war after 1900",
     "Which crops were most widely traded between the combatant states"], ans=0,
   why="Unit 7 Learning Objective I asks students to explain the relative significance of the causes of global conflict in the period 1900 to the present, and suggested skill 6.D requires that the answer rest on evidence. A question asking which causes carried the most weight, and on what evidence, is the objective and the skill together."),
 dict(q="Why is causation the reasoning process the CED attaches to this final topic of the unit?",
   choices=[
     "Because the topic asks students to weigh the causes of conflict against one another rather than to describe the conflicts",
     "Because the topic asks students to trace what stayed the same across the century",
     "Because the topic asks students to compare two states with one another",
     "Because the topic asks students to describe the conduct of the fighting",
     "Because the topic asks students to establish the audience of a source"], ans=0,
   why="Unit 7 Learning Objective I asks for the relative significance of the causes of global conflict, which is a question about causes and their weight. The CED also states that this final topic draws on the unit's key concepts, KC-6.2 among them, so the material being weighed is the unit's own account of why these conflicts came."),
 dict(q="Which statement is inconsistent with the framework's account of why the conflicts of this period came about?",
   choices=[
     "The framework identifies a single cause that accounts for every conflict of the century",
     "The framework lists several causes for each of the two world wars",
     "The framework marks one cause of the Second World War as especially important",
     "The framework describes challenges to the existing order as leading to worldwide conflicts",
     "The framework describes imperial collapse as the work of internal and external factors together"], ans=0,
   why="KC-6.2.IV.B.i and KC-6.2.IV.B.ii each give a list of causes, KC-6.2 describes varied challenges leading to conflict and KC-6.2.I.A names a combination of factors, so no single cause is offered anywhere for everything. The other four options restate those statements."),
 dict(q="What is the soundest way for a student to build an argument about the relative significance of the causes of global conflict after 1900?",
   choices=[
     "Take the causes the framework names, weigh them against evidence of several kinds, and use the framework's own ranking where it gives one",
     "Choose one cause in advance and gather only the evidence that supports it",
     "Rank the causes in the order in which the framework happens to list them",
     "Avoid ranking altogether, since the framework never weighs one cause against another",
     "Rely on a single document produced by one of the governments that fought"], ans=0,
   why="Unit 7 Learning Objective I asks for relative significance and suggested skill 6.D asks that the argument be built from diverse and alternative evidence. KC-6.2.IV.B.ii supplies the framework's one explicit ranking, with the word 'especially', while KC-6.2.IV.B.i leaves its causes unranked, so both halves of the keyed method are needed."),
]
