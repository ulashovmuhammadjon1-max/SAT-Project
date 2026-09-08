# AP U.S. HISTORY 3.5 The American Revolution
# Title copied verbatim from US_HISTORY_topics.json.
# Unit 3, Period 3: 1754 to 1800. Suggested skill 6.B, support an argument using specific
# and relevant evidence, with two printed bullets: describe specific examples of
# historically relevant evidence, and explain how specific examples of historically
# relevant evidence support an argument. Reasoning process printed for this topic:
# Causation.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 3: Learning Objective E
#       Explain how various factors contributed to the American victory in the Revolution.
#
#   THEMATIC FOCUS: America in the World (WOR)
#       Diplomatic, economic, cultural, and military interactions between empires, nations,
#       and peoples shape the development of America and America's increasingly important
#       role in the world.
#
#   KC-3.1.II.E  Despite considerable loyalist opposition, as well as Great Britain's
#                apparently overwhelming military and financial advantages, the Patriot
#                cause succeeded because of the actions of colonial militias and the
#                Continental Army, George Washington's military leadership, the colonists'
#                ideological commitment and resilience, and assistance sent by European
#                allies.
#
# THE WHOLE OF THIS TOPIC'S REQUIRED CONTENT IS THAT ONE SENTENCE, and it is unusually
# dense: two obstacles named with DESPITE, then four causes named with BECAUSE OF. So the
# module works the sentence clause by clause rather than reaching for material the page
# does not carry. Where a question needs more than the sentence supplies, it turns on the
# skill printed beside the title instead, which is a reasoning skill and needs no extra
# facts.
#
# WHAT IS NOT KEYED. The topic page's OPTIONAL SOURCES (a Christian Barnes letter, Lord
# Dunmore's proclamation, a Washington letter on Trenton, a Doehla diary on Yorktown, a
# Lafayette letter) are, in the CED's own words, "not required AP course content", and
# "None of the AP Exam questions require students to have studied these specific sources."
# No key here rests on any of them, and the verifier asserts it. George Washington and the
# Continental Army ARE keyed, because KC-3.1.II.E names them in the required content.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table= and
# every figure in them is explicitly hypothetical, since the CED prints no data here.
# PROSE ONLY: no LaTeX; a span of years is written "1754 to 1800", never with a hyphen.
# FIVE choices (A-E). Every invented source is marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("3.5", "The American Revolution", 3)

_T_ADVANTAGE = dict(
    headers=["Resource in a hypothetical comparison", "Britain (index)", "The states (index)"],
    rows=[["Trained soldiers under arms", "100", "28"],
          ["Warships in service", "100", "4"],
          ["Public funds available for war", "100", "19"]])

_T_FORCES = dict(
    headers=["Year in a hypothetical return", "Militia turnouts recorded",
             "Continental Army enlistments recorded"],
    rows=[["First", "9,000", "5,000"],
          ["Second", "7,500", "8,200"],
          ["Third", "6,400", "9,600"]])

_T_EVIDENCE = dict(
    headers=["Item of hypothetical evidence", "Cause it would support"],
    rows=[["A record of muskets and powder landed from a foreign port",
           "Assistance sent by European allies"],
          ["A county return of men marching out under their own local officers",
           "The actions of colonial militias"],
          ["An order moving regiments between two theatres over a single winter",
           "George Washington's military leadership"],
          ["A journal kept through a winter of shortage by a soldier who did not leave",
           "The colonists' ideological commitment and resilience"]])

QUESTIONS = [

 dict(q="Unit 3's Learning Objective E states what students should be able to explain about "
        "the Revolution. Which statement is it?",
      choices=[
        "Explain how various factors contributed to the American victory in the Revolution",
        "Explain how a single decisive factor produced the American victory in the Revolution",
        "Describe the campaigns of the Revolution in the order they were fought",
        "Explain why Great Britain entered the Revolution",
        "Compare the American Revolution with a revolution elsewhere in the same century"],
      ans=0,
      why="Unit 3: Learning Objective E reads 'Explain how various factors contributed to the "
          "American victory in the Revolution.' The word VARIOUS is what rules out a single "
          "decisive factor, and KC-3.1.II.E supplies four causes rather than one; the "
          "objective asks for explanation rather than narration or comparison."),

 dict(q="Which skill statement is printed beside this topic's title as the one students should "
        "practise here?",
      choices=[
        "Support an argument using specific and relevant evidence",
        "Identify and describe a claim or argument in a source",
        "Identify the evidence used in a source to support an argument",
        "Explain the point of view, purpose, historical situation, and audience of a source",
        "Identify patterns among or connections between historical developments and processes"],
      ans=0,
      why="Skill 6.B, support an argument using specific and relevant evidence, is printed on "
          "this topic page beside Unit 3: Learning Objective E. Skills 3.A and 3.B ask the "
          "student to find a claim or find evidence INSIDE a source, which is a different "
          "task from supporting an argument of one's own; the remaining two are skills 2.B "
          "and 5.A from other pages of this unit."),

 dict(q="The skill printed here carries two bullets beneath it. Which pair does the framework "
        "print?",
      choices=[
        "Describe specific examples of historically relevant evidence, and explain how "
        "specific examples of historically relevant evidence support an argument",
        "Describe specific examples of historically relevant evidence, and rank them by "
        "reliability",
        "Explain how specific examples support an argument, and identify the audience the "
        "argument addresses",
        "Summarise a historian's argument, and state whether it is convincing",
        "Identify a source's point of view, and explain its purpose"],
      ans=0,
      why="The two bullets printed under skill 6.B on this topic page are: describe specific "
          "examples of historically relevant evidence, and explain how specific examples of "
          "historically relevant evidence support an argument. Together they run from finding "
          "the evidence to showing what it does for the argument, which is what Unit 3: "
          "Learning Objective E's account of various contributing factors requires. Ranking by "
          "reliability, naming an audience and judging a historian are not among them."),

 dict(q="The unit's topic table assigns each topic a reasoning process. Which does it assign "
        "here?",
      choices=[
        "Causation",
        "Comparison",
        "Continuity and Change",
        "Argumentation",
        "Contextualization"],
      ans=0,
      why="The unit's topic table assigns Causation to this topic, which matches Unit 3: "
          "Learning Objective E asking how various factors CONTRIBUTED TO the American victory "
          "and matches KC-3.1.II.E's structure, in which four things are named as the reasons "
          "the Patriot cause succeeded. Comparison and Continuity and Change are assigned to "
          "other topics of this unit; the last two are skill categories."),

 dict(q="This topic sits under the thematic focus the framework calls America in the World. "
        "Which part of KC-3.1.II.E most directly answers to that focus?",
      choices=[
        "The assistance sent by European allies, which makes the outcome turn partly on "
        "interaction with other nations",
        "The actions of colonial militias, which were raised within the colonies themselves",
        "The colonists' ideological commitment, which was a matter of belief rather than of "
        "diplomacy",
        "The loyalist opposition, which was internal to the colonies",
        "The military leadership exercised within the Continental Army"],
      ans=0,
      why="The America in the World thematic focus states that diplomatic, economic, cultural, "
          "and military interactions between empires, nations, and peoples shape the "
          "development of America and its increasingly important role in the world. Of the "
          "elements KC-3.1.II.E names, the assistance sent by European allies is the one that "
          "crosses between nations; militias, commitment, loyalist opposition and command "
          "within the army are all internal to the conflict as the sentence describes it."),

 dict(q="KC-3.1.II.E gives the reasons the Patriot cause succeeded. Which set names all of "
        "them?",
      choices=[
        "The actions of colonial militias and the Continental Army, George Washington's "
        "military leadership, the colonists' ideological commitment and resilience, and "
        "assistance sent by European allies",
        "The actions of colonial militias and the Continental Army, and assistance sent by "
        "European allies",
        "George Washington's military leadership and the colonists' ideological commitment "
        "alone",
        "Assistance sent by European allies alone, since the framework treats it as decisive",
        "The weakness of Great Britain's military and financial position"],
      ans=0,
      why="KC-3.1.II.E names four things after the words BECAUSE OF: the actions of colonial "
          "militias and the Continental Army, George Washington's military leadership, the "
          "colonists' ideological commitment and resilience, and assistance sent by European "
          "allies. Three of the options drop at least one of the four, and the last inverts "
          "the sentence, which calls Britain's advantages apparently overwhelming rather than "
          "weak."),

 dict(q="KC-3.1.II.E opens by naming something inside the colonies that the Patriot cause had "
        "to succeed in spite of. What does the framework name?",
      choices=[
        "Considerable loyalist opposition",
        "The refusal of every colony to raise a militia",
        "The absence of any settled leadership in the Continental Army",
        "A general indifference among colonists to the outcome",
        "The withdrawal of all European support"],
      ans=0,
      why="KC-3.1.II.E begins 'Despite considerable loyalist opposition', which places "
          "substantial opposition among the colonists themselves. The same sentence names the "
          "actions of colonial militias, George Washington's military leadership, the "
          "colonists' ideological commitment and assistance sent by European allies among the "
          "reasons for success, so each of the other four options contradicts a clause of it."),

 dict(q="KC-3.1.II.E calls Great Britain's advantages APPARENTLY overwhelming. What does that "
        "word do for the framework's account?",
      choices=[
        "It records how the advantages looked at the time while leaving room for the outcome "
        "the sentence goes on to report",
        "It says the advantages did not exist",
        "It says the advantages made the outcome certain",
        "It restricts the advantages to financial ones",
        "It transfers the advantages to the Patriot side"],
      ans=0,
      why="KC-3.1.II.E says the Patriot cause succeeded DESPITE Great Britain's APPARENTLY "
          "overwhelming military and financial advantages. The word apparently keeps the "
          "sentence from asserting either that the advantages were unreal or that they settled "
          "the result, which is what makes the four causes it then names necessary; the "
          "advantages are Britain's and are both military and financial."),

 dict(q="What two kinds of advantage does KC-3.1.II.E attribute to Great Britain?",
      choices=[
        "Military and financial",
        "Military and diplomatic",
        "Financial and industrial",
        "Naval and territorial",
        "Financial advantages only"],
      ans=0,
      why="KC-3.1.II.E names Great Britain's apparently overwhelming MILITARY AND FINANCIAL "
          "advantages. The anchor carries both because each distractor keeps one of the pair "
          "or replaces it with a kind of advantage the sentence does not name."),

 dict(q="The first of KC-3.1.II.E's four causes names two kinds of fighting force. Which does "
        "the framework name?",
      choices=[
        "Colonial militias and the Continental Army",
        "Colonial militias alone",
        "The Continental Army alone",
        "The Continental Army and the navies of European allies",
        "Colonial militias and the regular forces of Great Britain"],
      ans=0,
      why="KC-3.1.II.E's first cause is 'the actions of colonial militias and the Continental "
          "Army', naming both together. The anchor carries both because two distractors keep "
          "one and drop the other; European assistance is a separate cause later in the same "
          "sentence, and British regulars are on the other side of the conflict."),

 dict(q="KC-3.1.II.E names one individual among the reasons for the Patriot success. Who is "
        "named, and for what?",
      choices=[
        "George Washington, for his military leadership",
        "George Washington, for his diplomatic negotiation with European allies",
        "An individual the framework leaves unnamed, for military leadership",
        "Benjamin Franklin, for his military leadership",
        "No individual at all, since the sentence names only groups"],
      ans=0,
      why="KC-3.1.II.E names George Washington's MILITARY LEADERSHIP as one of the four causes. "
          "The anchor carries both the name and the ground, because one distractor keeps the "
          "name and changes the ground while another keeps the ground and changes the name; "
          "assistance sent by European allies is listed separately from his leadership."),

 dict(q="The third of KC-3.1.II.E's causes names two qualities of the colonists. Which pair "
        "does the framework name?",
      choices=[
        "Ideological commitment and resilience",
        "Ideological commitment and financial strength",
        "Resilience and superiority of numbers",
        "Military training and discipline",
        "Unanimity of opinion across the colonies"],
      ans=0,
      why="KC-3.1.II.E names 'the colonists' ideological commitment and resilience'. Financial "
          "strength is what the same sentence attributes to Britain, training and numbers are "
          "not mentioned, and unanimity is contradicted by the considerable loyalist "
          "opposition the sentence opens with."),

 dict(q="The last of KC-3.1.II.E's causes concerns help from outside. How does the framework "
        "describe it?",
      choices=[
        "Assistance sent by European allies",
        "Assistance sent by every European power",
        "Assistance requested from European powers but not received",
        "Assistance sent by neighbouring colonies that remained under British rule",
        "Assistance in the form of money only"],
      ans=0,
      why="KC-3.1.II.E's fourth cause is 'assistance sent by European allies'. The word ALLIES "
          "is narrower than every European power, the assistance was sent rather than merely "
          "sought, its source is European rather than colonial, and the sentence puts no limit "
          "on the form it took."),

 dict(q="How is KC-3.1.II.E built as a sentence, and why does that structure matter for the "
        "objective it serves?",
      choices=[
        "It names two obstacles with the word despite and four causes with the words because "
        "of, which is what an account of various contributing factors requires",
        "It names one obstacle and one cause, so a single factor explains the outcome",
        "It names four obstacles and two causes, so the obstacles outweigh the causes",
        "It names causes without naming any obstacle, so nothing stood against the Patriot "
        "cause",
        "It names obstacles without naming any cause, so the outcome is left unexplained"],
      ans=0,
      why="KC-3.1.II.E puts considerable loyalist opposition and Great Britain's apparently "
          "overwhelming military and financial advantages after DESPITE, then four causes "
          "after BECAUSE OF. Unit 3: Learning Objective E asks how VARIOUS factors contributed "
          "to the American victory, so a sentence with one cause, or with no cause, or with "
          "the counts reversed would not serve it."),

 dict(q="Using the table of hypothetical comparative resources, what does the record support?",
      table=_T_ADVANTAGE,
      choices=[
        "One side leads on every measure recorded, and by a wide margin on each",
        "The two sides are close on every measure recorded",
        "Each side leads on at least one measure recorded",
        "The side that leads on soldiers trails on funds",
        "The measures recorded show no difference between the sides"],
      ans=0,
      why="Read from the table alone: the same column carries the larger figure in every row, "
          "and in each row the smaller figure is a small fraction of it. A picture of that "
          "shape is what KC-3.1.II.E means by Great Britain's APPARENTLY OVERWHELMING military "
          "and financial advantages, and the same sentence is why such a lead did not settle "
          "the outcome."),

 dict(q="Using the table of hypothetical returns of men under arms, which conclusion does the "
        "record support?",
      table=_T_FORCES,
      choices=[
        "Both kinds of force are recorded in every year, and the two move in opposite "
        "directions, so neither stands in for the other",
        "Only one kind of force is recorded in any year",
        "Both columns rise in every year",
        "Both columns fall in every year",
        "The two columns move together, so either could stand in for the other"],
      ans=0,
      why="Read from the table alone: every year records entries in both columns, one column "
          "falls at each step while the other rises, so they neither rise together nor fall "
          "together nor track one another. KC-3.1.II.E names the actions of colonial militias "
          "AND the Continental Army together as its first cause, which is why a record showing "
          "both present and behaving differently fits the framework's account."),

 dict(q="Using the table of hypothetical evidence, which item would support the cause that "
        "concerns help from outside the colonies?",
      table=_T_EVIDENCE,
      choices=[
        "The record of muskets and powder landed from a foreign port",
        "The county return of men marching out under their own local officers",
        "The order moving regiments between two theatres",
        "The journal kept through a winter of shortage",
        "None of the items supports that cause"],
      ans=0,
      why="Read from the table alone: exactly one row is matched to assistance sent by European "
          "allies, and it is the record of arms landed from a foreign port. The other three "
          "rows are matched to the remaining three causes KC-3.1.II.E names, which is what "
          "skill 6.B's bullets ask a student to do when they describe specific evidence and "
          "explain how it supports an argument."),

 dict(q="A hypothetical quartermaster's record, its author unnamed, lists tents, shoes and "
        "flour issued to regiments that had wintered in camp without pay. Which of "
        "KC-3.1.II.E's causes would such a record most directly support?",
      choices=[
        "The colonists' ideological commitment and resilience",
        "Assistance sent by European allies",
        "George Washington's military leadership",
        "Great Britain's apparently overwhelming financial advantages",
        "Considerable loyalist opposition"],
      ans=0,
      why="KC-3.1.II.E names the colonists' ideological commitment and resilience among the "
          "four reasons the Patriot cause succeeded, and men remaining with the army through a "
          "winter without pay is that resilience. Nothing in the record concerns a foreign "
          "ally, a commander's decisions, British finance or loyalist opposition, each of "
          "which is a different clause of the same sentence."),

 dict(q="Which of the following is NOT among the reasons KC-3.1.II.E gives for the Patriot "
        "success?",
      choices=[
        "The collapse of Great Britain's finances before the fighting began",
        "The actions of colonial militias",
        "George Washington's military leadership",
        "The colonists' resilience",
        "Assistance sent by European allies"],
      ans=0,
      why="KC-3.1.II.E describes Great Britain's military and financial advantages as "
          "apparently overwhelming, so a collapse of British finances before the fighting is "
          "the one option the sentence contradicts rather than states. The other four are "
          "named directly among its four causes."),

 dict(q="How does KC-3.1.II.E treat loyalist opposition, and what follows for a student writing "
        "about the Revolution?",
      choices=[
        "As an obstacle the Patriot cause succeeded despite, so a claim that the colonies were "
        "united behind independence cannot be supported from this sentence",
        "As one of the causes of the Patriot success, so it belongs among the contributing "
        "factors",
        "As an invention of later writers, so it needs no place in an account of the war",
        "As a movement confined to Great Britain rather than to the colonies",
        "As a development belonging to the years after the fighting"],
      ans=0,
      why="KC-3.1.II.E places considerable loyalist opposition after the word DESPITE, which "
          "makes it something the Patriot cause overcame rather than something that helped it, "
          "and CONSIDERABLE is the framework's own measure of its size. Unit 3: Learning "
          "Objective E asks about the factors that contributed to the victory, and loyalist "
          "opposition is on the other side of that account."),

 dict(q="A hypothetical dispatch, its author unnamed, reports that a fleet flying a foreign "
        "flag has anchored off the coast and that its commander has offered to act with the "
        "American forces ashore. Which framework claim does the dispatch illustrate?",
      choices=[
        "That assistance sent by European allies was among the reasons the Patriot cause "
        "succeeded",
        "That the colonists' ideological commitment was among those reasons",
        "That colonial militias were among those reasons",
        "That Great Britain's advantages were apparently overwhelming",
        "That loyalist opposition was considerable"],
      ans=0,
      why="KC-3.1.II.E names assistance sent by European allies as the last of its four causes, "
          "and a foreign fleet offering to act with American forces is that assistance. The "
          "other four options each name a different clause of the same sentence, two of them "
          "from the DESPITE half rather than the BECAUSE OF half."),

 dict(q="Why does the framework list four causes for the Patriot success rather than settling "
        "on one?",
      choices=[
        "Because Unit 3's Learning Objective E asks how VARIOUS factors contributed, and "
        "KC-3.1.II.E supplies four that operated together",
        "Because the framework is uncertain which of the four actually operated",
        "Because the four causes are alternative explanations, only one of which can be true",
        "Because three of the four belong to a later period",
        "Because the framework treats the outcome as unexplained"],
      ans=0,
      why="Unit 3: Learning Objective E asks students to explain how VARIOUS factors "
          "contributed to the American victory, and KC-3.1.II.E answers with four causes "
          "joined by AND rather than by OR. A list joined that way is a claim that they "
          "operated together, not a statement of uncertainty, a set of alternatives, or a "
          "refusal to explain."),

 dict(q="The first bullet under this topic's skill asks students to do what with evidence?",
      choices=[
        "Describe specific examples of historically relevant evidence",
        "Rank examples of evidence by how reliable each one is",
        "Count how many examples an argument uses",
        "Identify the audience an example was addressed to",
        "Summarise the argument of a secondary source"],
      ans=0,
      why="The first bullet printed under skill 6.B on this topic page reads 'Describe specific "
          "examples of historically relevant evidence'. Ranking, counting, naming an audience "
          "and summarising a secondary source are not what it asks, and the bullet's work is "
          "the first half of what Unit 3: Learning Objective E needs, since a claim about "
          "various contributing factors has to name the evidence for each."),

 dict(q="The second bullet under this topic's skill asks students to do what?",
      choices=[
        "Explain how specific examples of historically relevant evidence support an argument",
        "Explain why an argument was persuasive to the people who first heard it",
        "Explain how a source's point of view shaped what it recorded",
        "Explain the difference between a primary and a secondary source",
        "Explain how evidence should be arranged in chronological order"],
      ans=0,
      why="The second bullet printed under skill 6.B reads 'Explain how specific examples of "
          "historically relevant evidence support an argument'. It asks for the connection "
          "between an example and a claim, which is the step beyond simply describing the "
          "example, and it is what a student applying Unit 3: Learning Objective E must do for "
          "each of the four causes KC-3.1.II.E names."),

 dict(q="What is the difference between a claim and a piece of evidence, on the account this "
        "topic's skill assumes?",
      choices=[
        "A claim is the assertion an argument makes; evidence is the specific material offered "
        "in support of it",
        "Evidence is the assertion an argument makes; a claim is the specific material offered "
        "in support of it",
        "A claim and a piece of evidence are the same thing under two names",
        "A claim is always drawn from a primary source and evidence from a secondary one",
        "A claim concerns causes and evidence concerns consequences"],
      ans=0,
      why="Skill 6.B asks students to SUPPORT AN ARGUMENT using specific and relevant evidence, "
          "and its second bullet asks them to explain how examples support that argument, "
          "which only makes sense if the assertion and the material offered for it are "
          "different things. The anchor carries both halves because the leading distractor is "
          "this same distinction with the two terms exchanged; KC-3.1.II.E's four causes are "
          "claims for which such evidence would be gathered."),

 dict(q="A hypothetical muster roll, its author unnamed, records that men from one county "
        "assembled under officers chosen locally, served for a few weeks and then returned to "
        "their farms. Which of KC-3.1.II.E's causes does this bear on most directly?",
      choices=[
        "The actions of colonial militias",
        "The actions of the Continental Army as a standing force",
        "Assistance sent by European allies",
        "George Washington's military leadership",
        "Great Britain's apparently overwhelming military advantages"],
      ans=0,
      why="KC-3.1.II.E's first cause names the actions of colonial militias and the Continental "
          "Army together, and short local service under locally chosen officers is the militia "
          "half rather than the standing army half. None of the other three clauses of the "
          "sentence concerns how men were raised in a county."),

 dict(q="If a student argued that the Patriot cause succeeded only because of help from abroad, "
        "which part of the framework would count against the argument?",
      choices=[
        "KC-3.1.II.E lists assistance sent by European allies as one of four causes rather than "
        "as the whole explanation",
        "KC-3.1.II.E does not mention European assistance at all",
        "KC-3.1.II.E treats European assistance as an obstacle the Patriot cause overcame",
        "KC-3.1.II.E attributes the outcome entirely to George Washington's leadership",
        "KC-3.1.II.E leaves the causes of the outcome unstated"],
      ans=0,
      why="KC-3.1.II.E names assistance sent by European allies alongside the actions of "
          "colonial militias and the Continental Army, George Washington's military "
          "leadership, and the colonists' ideological commitment and resilience. It is "
          "therefore one of four, which is exactly what Unit 3: Learning Objective E means by "
          "various factors; the sentence neither omits it, nor places it among the obstacles, "
          "nor makes any single cause the whole account."),

 dict(q="A hypothetical intelligence summary, its author unnamed, sets out that one side has "
        "more trained troops, more ships and more money than the other, and concludes that the "
        "war will be short. Which framework claim shows why the conclusion does not follow?",
      choices=[
        "KC-3.1.II.E calls those advantages apparently overwhelming and still records that the "
        "Patriot cause succeeded",
        "KC-3.1.II.E denies that one side held greater military and financial resources",
        "KC-3.1.II.E says the war's length was settled by loyalist opposition",
        "KC-3.1.II.E attributes the outcome to the resources each side began with",
        "KC-3.1.II.E makes no claim about the outcome of the war"],
      ans=0,
      why="KC-3.1.II.E places Great Britain's apparently overwhelming military and financial "
          "advantages after DESPITE and then states that the Patriot cause succeeded, so a "
          "count of resources does not settle the result. The sentence affirms rather than "
          "denies the advantages, names loyalist opposition as an obstacle rather than a "
          "timetable, and gives four causes of its own for the outcome."),

 dict(q="Grouping KC-3.1.II.E's four causes, which pairing separates them by whether they come "
        "from inside the colonies or from outside?",
      choices=[
        "Militias and the Continental Army, Washington's leadership and the colonists' "
        "commitment come from inside; assistance sent by European allies comes from outside",
        "Assistance sent by European allies comes from inside; the other three come from "
        "outside",
        "All four causes come from outside the colonies",
        "All four causes come from inside the colonies",
        "The framework does not distinguish where any of the causes came from"],
      ans=0,
      why="Of the four causes KC-3.1.II.E names, three describe colonists and their forces and "
          "the fourth describes assistance SENT BY EUROPEAN ALLIES, which is what makes this "
          "topic answer to the America in the World thematic focus on interactions between "
          "nations. The anchor carries both halves because the leading distractor is the same "
          "grouping with inside and outside exchanged."),

 dict(q="Taken as a whole, what does KC-3.1.II.E establish about the American victory?",
      choices=[
        "That it was won against substantial internal opposition and a far better resourced "
        "opponent, through four causes operating together rather than any one of them alone",
        "That it was won easily, because Great Britain's position was weak from the start",
        "That it was won by a united population facing no opposition within the colonies",
        "That it was won by foreign assistance, to which the framework assigns the whole "
        "outcome",
        "That the framework describes the war without accounting for its outcome"],
      ans=0,
      why="KC-3.1.II.E holds all of it in one sentence: considerable loyalist opposition and "
          "Great Britain's apparently overwhelming military and financial advantages on one "
          "side, and four causes of Patriot success on the other. Each rejected option denies "
          "one of those clauses, and Unit 3: Learning Objective E asks precisely for the "
          "various factors the sentence supplies."),
]
