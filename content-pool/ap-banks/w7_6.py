# AP WORLD HISTORY: MODERN 7.6 Causes of World War II
# CED effective Fall 2026, Unit 7 Global Conflict, c. 1900 to the present.
# Thematic focus Governance (GOV). Unit 7 Learning Objective F: explain the
# causes and consequences of World War II. Reasoning process: causation.
# Suggested skill 2.C, explain the significance of a source's point of view,
# purpose, historical situation, and/or audience, including how these might
# limit the use(s) of a source.
#
# THE HISTORICAL DEVELOPMENT THIS TOPIC RESTS ON, in the framework's own words:
#   KC-6.2.IV.B.ii  The causes of World War II included the unsustainable peace
#                   settlement after World War I, the global economic crisis
#                   engendered by the Great Depression, continued imperialist
#                   aspirations, and especially the rise to power of fascist and
#                   totalitarian regimes that resulted in the aggressive
#                   militarism of Nazi Germany under Adolf Hitler.
#
# Four features of that sentence carry every key here, and each is the
# framework's own wording rather than a gloss on it:
#   1. INCLUDED. The four causes are given as members of a list, not as a closed
#      enumeration. Items 6 and 29 turn on it.
#   2. ESPECIALLY. This is the one place in the unit where the framework ranks
#      a cause against the others, and it ranks the rise to power of fascist and
#      totalitarian regimes above the rest. Items 2, 15, 21 and 30 turn on it.
#   3. RESULTED IN. The direction runs from the rise to power of those regimes
#      to the aggressive militarism of Nazi Germany under Adolf Hitler, and not
#      the other way. Item 3 is the swap item and its anchor carries both halves.
#   4. CONTINUED. Imperialist aspirations are described as carrying on, which is
#      what links this sentence to KC-6.2.I.B in topic 7.5. Items 5 and 11.
#
# CONSEQUENCES. The learning objective covers consequences as well as causes,
# but this topic's own historical development states causes only. Where a
# consequence is keyed, the citation is to the framework sentence that supplies
# it: KC-6.1.III.C.ii, which states that new military technology and new tactics
# led to increased levels of wartime casualties. That is item 24, and it is the
# only one.
#
# BOUNDARY WITH 7.2 AND 7.9. Topic 7.2 holds KC-6.2.IV.B.i, the causes of the
# first war; items 11, 12 and 13 are the only ones that touch it, and each is a
# question about how the framework's TWO lists stand to one another rather than
# a second helping of the first war. Topic 7.9 holds the relative significance
# of the causes of global conflict under Learning Objective I; the ranking used
# here is only the one the framework itself writes into this sentence with the
# word "especially", and no item asks a student to rank the other three.
#
# WHAT IS DELIBERATELY NOT ASKED. No item keys to a date, a treaty article, a
# territorial claim, a battle, an election, a party name or a casualty total.
# The framework prints none of them for this topic. Adolf Hitler is named
# because KC-6.2.IV.B.ii names him; nothing is asserted about him beyond the
# words that sentence uses.
#
# SOURCES. The bank cannot show images and the framework prints no document text
# for this topic, so every stimulus is either an explicitly unattributed
# illustrative source or a table of illustrative data whose keyed conclusion is
# recoverable from the table alone. Nothing is attributed to a real person or
# document, and no quotation is invented for one.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md.
TOPIC = ("7.6", "Causes of World War II", 7)

_T_OUTPUT = dict(
    headers=["Country (illustrative)",
             "Index of industrial output at the onset of the crisis",
             "Index of industrial output three years later"],
    rows=[["Country D", "100", "54"],
          ["Country E", "100", "68"],
          ["Country F", "100", "78"]])

_T_ARMS = dict(
    headers=["State (illustrative)",
             "Share of government spending devoted to armed forces, earlier year (percent)",
             "Share of government spending devoted to armed forces, later year (percent)"],
    rows=[["State P", "12", "41"],
          ["State Q", "9", "17"],
          ["State R", "14", "22"]])

QUESTIONS = [
 dict(q="An unattributed memorandum circulated inside a foreign ministry in the 1930s argues that the borders imposed on the state at the end of the previous war were never acceptable to its people and cannot be defended for another generation. Which of the causes named by the framework does the memorandum express?",
   choices=[
     "The unsustainable peace settlement that followed the First World War",
     "The global economic crisis engendered by the Great Depression",
     "Continued imperialist aspirations",
     "The rise to power of fascist and totalitarian regimes",
     "New military technology and the tactics of total war"], ans=0,
   why="KC-6.2.IV.B.ii lists the unsustainable peace settlement after World War I first among the causes of World War II. A memorandum arguing that the borders the settlement imposed cannot be maintained is a statement of that grievance rather than of an economic, imperial or regime-based cause."),
 dict(q="Of the four causes the framework names for the Second World War, which one does it single out with the word 'especially'?",
   choices=[
     "The rise to power of fascist and totalitarian regimes",
     "The unsustainable peace settlement after the First World War",
     "The global economic crisis engendered by the Great Depression",
     "Continued imperialist aspirations",
     "The framework singles out none of the four and gives them equal weight"], ans=0,
   why="KC-6.2.IV.B.ii places 'and especially' before the rise to power of fascist and totalitarian regimes, which is the framework's own weighting of one cause against the rest. The other three appear in the same list without that qualifier."),
 dict(q="In what direction does the framework state the relationship between the rise to power of fascist and totalitarian regimes and the aggressive militarism of Nazi Germany under Adolf Hitler?",
   choices=[
     "The rise to power of those regimes resulted in the aggressive militarism of Nazi Germany under Adolf Hitler",
     "The aggressive militarism of Nazi Germany resulted in the rise to power of fascist and totalitarian regimes elsewhere",
     "The framework describes the two developments as unconnected",
     "The framework describes the aggressive militarism as a cause of the peace settlement",
     "The framework describes the rise to power of those regimes as a consequence of the Great Depression"], ans=0,
   why="KC-6.2.IV.B.ii says the rise to power of fascist and totalitarian regimes resulted in the aggressive militarism of Nazi Germany under Adolf Hitler. The verb fixes which development produced which, and the anchor for this item carries both halves because the reversed reading is the plausible error."),
 dict(q="How does the framework describe the economic cause of the Second World War?",
   choices=[
     "As a global economic crisis engendered by the Great Depression",
     "As a global economic crisis engendered by the peace settlement",
     "As an economic crisis confined to a single region",
     "As a period of rapid economic growth across the industrial states",
     "As an economic development the framework does not connect to the war"], ans=0,
   why="KC-6.2.IV.B.ii names the global economic crisis engendered by the Great Depression among the causes of World War II. The sentence supplies both the scale of the crisis and what engendered it, so an answer changing either one departs from the framework."),
 dict(q="The framework speaks of 'continued' imperialist aspirations among the causes of the Second World War. What does that word assert?",
   choices=[
     "That imperialist aspirations carried on from the earlier period rather than arising for the first time in the 1930s",
     "That imperialist aspirations were held for the first time by the states that went to war in 1939",
     "That imperialist aspirations had ended before the war began",
     "That imperialist aspirations belonged only to the states that had lost the previous war",
     "That imperialist aspirations were confined to Europe"], ans=0,
   why="KC-6.2.IV.B.ii names continued imperialist aspirations, and KC-6.2.I.B records that between the two world wars imperial states predominantly maintained control over colonial holdings and in some cases gained more. The adjective marks a continuity across the interwar years rather than a new departure."),
 dict(q="The framework's sentence says that the causes of the Second World War 'included' the four it goes on to name. What follows from that word?",
   choices=[
     "The four are given as members of the list rather than as a complete enumeration of every cause",
     "The four are given as the only causes the war can be said to have had",
     "The four are given as causes of the First World War rather than of the Second",
     "The four are given in order of decreasing importance from first to last",
     "The framework states that the war had no identifiable causes"], ans=0,
   why="KC-6.2.IV.B.ii opens with the phrase that the causes of World War II included the items it lists, which asserts membership without asserting completeness. The sentence ranks only one item, with the word 'especially', and it does not order the remaining three."),
 dict(q="The table below reports illustrative index numbers for industrial output in three countries, with the onset of the global economic crisis set at one hundred in each. Which conclusion is best supported?",
   table=_T_OUTPUT,
   choices=[
     "Output falls in all three countries, and the steepest fall is in Country D",
     "Output falls in all three countries, and the steepest fall is in Country F",
     "Output rises in all three countries across the period shown",
     "Output falls in only one of the three countries",
     "The three countries end the period at the same index of output"], ans=0,
   why="Read from the table alone: every country is based at the same index at the onset, every later figure is below that base, and subtracting gives one country the steepest fall. KC-6.2.IV.B.ii names the global economic crisis engendered by the Great Depression among the causes of the war, and a crisis reaching every country in the table is what global means here."),
 dict(q="The table below reports illustrative figures for the share of government spending devoted to armed forces in three states in two years of the 1930s. Which conclusion is best supported?",
   table=_T_ARMS,
   choices=[
     "The share rises in every state, and the largest increase in percentage points is in State P",
     "The share rises in every state, and the largest increase in percentage points is in State R",
     "The share falls in every state between the two years",
     "Only one of the three states devotes any spending at all to its armed forces",
     "The state with the highest share in the earlier year records the largest increase"], ans=0,
   why="Read from the table alone: every later share exceeds its earlier one, no share is zero, and subtracting gives one state the largest increase, which is not the state that began highest. KC-6.2.IV.B.ii names the aggressive militarism that resulted from the rise to power of fascist and totalitarian regimes, and a rising share of spending on armed forces is the kind of evidence that bears on it."),
 dict(q="An unattributed circular sent to its clients by a commercial bank in the early 1930s reports that export orders have collapsed in every market the bank serves and that unemployment is rising in each of them. The circular is best used as evidence of",
   choices=[
     "the global economic crisis that the framework counts among the causes of the Second World War",
     "the unsustainable character of the peace settlement that ended the First World War",
     "the rise to power of fascist and totalitarian regimes",
     "continued imperialist aspirations among the industrial states",
     "the new military technology that raised levels of wartime casualties"], ans=0,
   why="KC-6.2.IV.B.ii names the global economic crisis engendered by the Great Depression among the causes of World War II. Collapsed orders and rising unemployment across several markets at once is a report of that crisis and not of a settlement, a regime change or a weapon."),
 dict(q="An unattributed official statement issued by a government immediately after it has taken control of a neighbouring territory declares that it acted only to protect people of its own nationality living there. Which limitation on the statement's use is most significant?",
   choices=[
     "It is issued by the government whose action is in question, and its purpose is to justify that action",
     "It was issued at the time of the events, which makes it unusable as evidence",
     "It concerns a neighbouring territory, and no source about a neighbouring territory can be used",
     "It mentions nationality, which is a subject a historian cannot investigate",
     "It was issued in writing rather than delivered aloud, so its author cannot be identified"], ans=0,
   why="Suggested skill 2.C asks how a source's point of view and purpose limit its uses, and KC-6.2.IV.B.ii names continued imperialist aspirations and aggressive militarism among the causes of the war. A government explaining its own seizure of territory is the party with the strongest reason to describe it as something else."),
 dict(q="Which cause appears, in some form, both in the framework's list for the First World War and in its list for the Second?",
   choices=[
     "Imperialism, named as imperialist expansion for the first war and as continued imperialist aspirations for the second",
     "A flawed alliance system, which the framework names for both wars",
     "A global economic crisis, which the framework names for both wars",
     "The rise of fascist and totalitarian regimes, which the framework names for both wars",
     "Nothing appears in both of the framework's lists"], ans=0,
   why="KC-6.2.IV.B.i names imperialist expansion and competition for resources among the causes of World War I, and KC-6.2.IV.B.ii names continued imperialist aspirations among the causes of World War II. Imperialism is the element the two lists share, and the word 'continued' is the framework's own marker of that overlap."),
 dict(q="How does the framework connect the end of the First World War to the outbreak of the Second?",
   choices=[
     "The peace settlement that followed the first war is named among the causes of the second",
     "The peace settlement that followed the first war is named among the causes of the first",
     "The framework treats the two wars as having no connection that it states",
     "The framework names the second war among the causes of the first",
     "The framework treats the second war as a continuation of fighting that never stopped"], ans=0,
   why="KC-6.2.IV.B.ii opens its list of the causes of World War II with the unsustainable peace settlement after World War I, while KC-6.2.IV.B.i gives the earlier war its own separate causes. The settlement is therefore the framework's explicit link running forward from one war to the next."),
 dict(q="Which of the following does the framework name among the causes of the First World War but not among those it lists for the Second?",
   choices=[
     "A flawed alliance system",
     "Continued imperialist aspirations",
     "A global economic crisis engendered by the Great Depression",
     "The rise to power of fascist and totalitarian regimes",
     "An unsustainable peace settlement"], ans=0,
   why="KC-6.2.IV.B.i names a flawed alliance system, alongside territorial and regional conflicts and intense nationalism, among the things that escalated tensions into the First World War. KC-6.2.IV.B.ii's list for the Second names the other four items instead."),
 dict(q="A government in the 1930s tells its public that the state must obtain territory overseas that other powers now hold, and that its claim to such territory was set aside when the previous war was settled. Under the framework's list, this appeal is best classified as",
   choices=[
     "continued imperialist aspirations joined to a grievance about the peace settlement",
     "a global economic crisis engendered by the Great Depression",
     "the use of political propaganda to mobilize a population for war",
     "the collapse of an older land-based empire",
     "a government taking a more active role in economic life"], ans=0,
   why="KC-6.2.IV.B.ii names continued imperialist aspirations and the unsustainable peace settlement after World War I as two separate causes, and this appeal joins them: it demands colonial territory and blames the settlement for the loss of the claim. The remaining options belong to KC-6.2.IV.A.ii, KC-6.2.I.A and KC-6.3.I.B."),
 dict(q="A student writes that the framework explains the Second World War entirely by economic causes. What is the best correction?",
   choices=[
     "The framework lists political causes as well, and singles out the rise to power of fascist and totalitarian regimes",
     "The framework lists economic causes only, so the student's account is complete",
     "The framework lists no causes at all for the second war",
     "The framework lists new military technology as the war's only cause",
     "The framework attributes the war to the collapse of the older land-based empires"], ans=0,
   why="KC-6.2.IV.B.ii names one economic cause, the global economic crisis engendered by the Great Depression, alongside a settlement, imperialist aspirations and a rise to power of regimes, and it marks the last of these as especially important. An account limited to economics drops the cause the framework weights most heavily."),
 dict(q="An unattributed programme published by a political movement seeking office promises to overturn the terms imposed on the state after the previous war and to rebuild its armed forces. The programme is most useful as evidence of",
   choices=[
     "a movement joining a grievance about the peace settlement to a demand for rearmament",
     "a government that has already carried out a programme of rearmament",
     "the level of unemployment in the state at the time it was published",
     "the terms of the peace settlement as the victorious powers drafted them",
     "the result of the election that the movement went on to contest"], ans=0,
   why="Suggested skill 2.C asks what a source's purpose does to its usefulness, and a programme states what a movement intends rather than what it has achieved. KC-6.2.IV.B.ii names the unsustainable peace settlement and the rise to power of fascist and totalitarian regimes among the causes of the war, and this document is evidence of a movement bringing the two together."),
 dict(q="Two unattributed reports on the same country's economy survive, one written in the middle of the 1920s and one written in the early 1930s. Why does knowing when each was written matter to a historian using them?",
   choices=[
     "The later report is written during the global economic crisis, so the situation it describes is not the one the earlier report describes",
     "The earlier report is written during the global economic crisis, so its figures are the less reliable of the two",
     "The date of a report has no bearing on how a historian may use it",
     "The later report must be the more accurate simply because it was written later",
     "Only reports written after a war has ended may be used as evidence about an economy"], ans=0,
   why="Suggested skill 2.C names historical situation among the things that shape a source's significance, and KC-6.2.IV.B.ii dates the global economic crisis to the Great Depression. Two reports separated by the onset of that crisis describe different situations, so the difference between them is not by itself a sign that one is wrong."),
 dict(q="A government issues two documents in the same month: a broadcast addressed to its own population and a confidential note addressed to a foreign ministry. What does the difference in audience tell a historian?",
   choices=[
     "Each is shaped for the people meant to receive it, so the two may state the government's aims differently",
     "The broadcast must be truthful and the confidential note must be false",
     "The confidential note must be truthful and the broadcast must be false",
     "Audience makes no difference to the way either document should be read",
     "Only a document with a single named author can be interpreted at all"], ans=0,
   why="Suggested skill 2.C names audience among the things that shape a source's significance and limit its uses. KC-6.2.IV.B.ii records aggressive militarism among the causes of the war, and a government pursuing it has different reasons for what it tells its own people and what it tells another state."),
 dict(q="Which finding, if it were established, would most strengthen the claim that the peace settlement after the First World War contributed to the outbreak of the Second?",
   choices=[
     "Evidence that governments demanding territory in the 1930s justified those demands by the terms imposed on them in the settlement",
     "Evidence that industrial output fell sharply in many countries in the early 1930s",
     "Evidence that new military technology raised casualties in the fighting that followed",
     "Evidence that the settlement's borders were drawn with the help of a committee of experts",
     "Evidence that parts of the two wars were fought over the same ground"], ans=0,
   why="KC-6.2.IV.B.ii names the unsustainable peace settlement after World War I among the causes of the Second World War. A finding that the demands driving the later crisis were framed by reference to the settlement's own terms connects the settlement to the outbreak, which the other findings leave untouched."),
 dict(q="Which finding, if it were established, would most weaken that same claim about the peace settlement?",
   choices=[
     "Evidence that the governments making territorial demands in the 1930s had made the same demands before the settlement existed",
     "Evidence that the settlement redrew borders in more than one region",
     "Evidence that the settlement transferred colonies from one imperial power to another",
     "Evidence that the depression reduced trade among the states party to the settlement",
     "Evidence that the settlement was signed by a large number of states"], ans=0,
   why="A cause cannot follow its effect. KC-6.2.IV.B.ii names the settlement among the causes of the war, so a finding that the demands predate the settlement removes it from the chain rather than qualifying it. The other four findings describe the settlement and the period without bearing on the sequence."),
 dict(q="Why is causation the reasoning process the framework attaches to this topic?",
   choices=[
     "Because the framework's statement is a list of the war's causes with one of them singled out as especially important",
     "Because the framework's statement compares two states with one another",
     "Because the framework's statement traces what stayed the same across a century",
     "Because the framework's statement describes the conduct of a single campaign",
     "Because the framework's statement concerns the mobilization of populations rather than the origins of the war"], ans=0,
   why="KC-6.2.IV.B.ii is a statement of what caused World War II, and its 'and especially' marks one cause as weightier than the others. A sentence that both lists causes and ranks one of them is causation reasoning, whereas mobilization is the subject of KC-6.2.IV.A.ii in topic 7.7."),
 dict(q="Which research question is framed most directly by this topic's stated learning objective?",
   choices=[
     "What caused the Second World War, and what followed from it",
     "Which general commanded each army during the Second World War",
     "How many aircraft each state produced in each year of the war",
     "Which languages were spoken in the territories the war was fought over",
     "How the climate of Europe changed across the war years"], ans=0,
   why="Unit 7 Learning Objective F asks students to explain the causes and consequences of World War II, so a question framed as what caused the war and what followed from it restates the objective. The other four ask about matters the objective does not name."),
 dict(q="What does the framework's adjective 'unsustainable', applied to the peace settlement, assert?",
   choices=[
     "That the settlement could not be maintained, which is why it stands among the causes of the next war",
     "That the settlement was maintained without difficulty throughout the interwar period",
     "That the settlement was never signed by any of the states it concerned",
     "That the settlement dealt with economic questions rather than territorial ones",
     "That the settlement was drafted by the states that had lost the previous war"], ans=0,
   why="KC-6.2.IV.B.ii calls the peace settlement after World War I unsustainable and places it among the causes of World War II. An arrangement described as unable to hold, in a sentence explaining why a second war came, is being given as part of that explanation."),
 dict(q="The framework states that one consequence of the way the Second World War was fought was",
   choices=[
     "increased levels of wartime casualties, produced by new military technology and new tactics",
     "a fall in wartime casualties compared with the previous war",
     "the abandonment of military technology by agreement among the combatants",
     "the end of imperialist aspirations among all of the combatant states",
     "the withdrawal of governments from economic life"], ans=0,
   why="KC-6.1.III.C.ii states that new military technology and new tactics, including the atomic bomb, fire-bombing and the waging of total war, led to increased levels of wartime casualties. Unit 7 Learning Objective F covers consequences as well as causes, and this is the consequence the framework states."),
 dict(q="Two states both experience the global economic crisis; in one a fascist regime comes to power and in the other none does. What does the framework allow a student to conclude?",
   choices=[
     "That the framework names the crisis and the rise of such regimes separately among the war's causes, without stating that the crisis produced the regimes",
     "That the framework states the economic crisis always produced fascist regimes where it struck",
     "That the framework states the economic crisis had no political consequences anywhere",
     "That the framework denies that either development was a cause of the war",
     "That the framework treats the two states as having had identical politics"], ans=0,
   why="KC-6.2.IV.B.ii lists the global economic crisis engendered by the Great Depression and the rise to power of fascist and totalitarian regimes as two items in one list of causes. Listing them together states that each contributed to the war; it does not state that either produced the other."),
 dict(q="An unattributed diplomatic dispatch of the late 1930s reports that a neighbouring state has introduced conscription, doubled the size of its army and begun to press territorial demands on the states around it. The dispatch is best used as evidence of",
   choices=[
     "the aggressive militarism that the framework names among the causes of the Second World War",
     "the peace settlement's terms as the victorious powers originally drafted them",
     "a government withdrawing from an active role in economic life",
     "the collapse of an older land-based empire",
     "a colonial population being mobilized for the purpose of waging war"], ans=0,
   why="KC-6.2.IV.B.ii names the aggressive militarism of Nazi Germany that resulted from the rise to power of fascist and totalitarian regimes among the causes of the war. Conscription, a doubled army and demands on neighbours are the conduct such a description covers, whereas the other options belong to KC-6.3.I.B, KC-6.2.I.A and KC-6.2.IV.A.ii."),
 dict(q="An unattributed memoir published long afterwards by a former official of one of the victorious powers of the First World War argues that the settlement his government helped to draft had nothing to do with the war that came next. Which limitation on the memoir matters most?",
   choices=[
     "Its author helped to draft the settlement, so he has reason to defend it against the charge the framework's account makes",
     "It was written long after the events, so nothing in it can be used",
     "It concerns a settlement, and settlements lie outside a historian's subject",
     "It was published rather than kept private, so its author cannot be identified",
     "It is the work of one person, and evidence from a single author is never admissible"], ans=0,
   why="Suggested skill 2.C asks how point of view limits a source's uses, and KC-6.2.IV.B.ii names the unsustainable peace settlement after World War I among the causes of the Second World War. A drafter defending his own settlement against exactly that charge is the interested party, which is a limit on the source rather than a reason to discard it."),
 dict(q="The framework calls the economic crisis it names a global one. Which statement follows from that word?",
   choices=[
     "The crisis is described as reaching beyond any single state's economy",
     "The crisis is described as confined to the state in which it began",
     "The crisis is described as affecting only the states that had lost the previous war",
     "The crisis is described as affecting only colonial territories",
     "The crisis is described as one the framework does not characterise"], ans=0,
   why="KC-6.2.IV.B.ii names the global economic crisis engendered by the Great Depression among the causes of World War II. The framework's own adjective places the crisis across economies rather than inside one, which is what makes it a cause of a war fought among many states."),
 dict(q="Which statement is inconsistent with the framework's account of the causes of the Second World War?",
   choices=[
     "The war had a single cause, and the framework identifies that cause as the Great Depression",
     "An unsustainable peace settlement was among the war's causes",
     "A global economic crisis was among the war's causes",
     "Continued imperialist aspirations were among the war's causes",
     "The rise to power of fascist and totalitarian regimes was among the war's causes"], ans=0,
   why="KC-6.2.IV.B.ii names four causes and marks one of them as especially important, so an account reducing the war to one cause contradicts the sentence, and the framework's own weighting falls on the regimes rather than on the depression. The other four options restate items from the list."),
 dict(q="What is the most accurate summary of the framework's sentence on the causes of the Second World War for a student revising this topic?",
   choices=[
     "Several causes, among them a settlement that could not hold, a global slump and continued imperial ambition, with the rise of fascist and totalitarian regimes singled out",
     "A single cause, the rise of fascist and totalitarian regimes, with no other cause named",
     "Several causes, none of which the framework treats as weightier than the others",
     "Several causes, all of them economic, with no political cause named at all",
     "No causes, because the framework treats the war's origins as unknowable"], ans=0,
   why="KC-6.2.IV.B.ii lists the unsustainable peace settlement after World War I, the global economic crisis engendered by the Great Depression and continued imperialist aspirations, and then marks the rise to power of fascist and totalitarian regimes with the word 'especially'. A summary has to carry both the plurality of causes and that single ranking."),
]
