# AP WORLD HISTORY: MODERN 6.8 Causation in the Imperial Age
# CED effective Fall 2026, Unit 6 Consequences of Industrialization, c. 1750 to
# c. 1900. This is the FINAL topic of the unit, and the CED says what that means:
#   "The final topic in this unit focuses on the skill of argumentation and so
#    provides an opportunity for your students to draw upon the key concepts and
#    historical developments they have studied in this unit. Using evidence relevant
#    to this unit's key concepts, students should practice the suggested skill for
#    this topic."
# So this module is written as a REASONING set, per HISTORY_BRIEF.md. It asks what
# a piece of evidence does to an argument, not what happened in a given year.
#
# Suggested skill category: Argumentation. Suggested skill 6.D: "Corroborate,
# qualify, or modify an argument using diverse and alternative evidence in order to
# develop a complex argument. This argument might:
#   - Explain nuance of an issue by analyzing multiple variables.
#   - Explain relevant and insightful connections within and across periods.
#   - Explain the relative historical significance of a source's credibility and
#     limitations.
#   - Explain how or why a historical claim or argument is or is not effective."
# Reasoning process: Causation.
#
# Unit 6 Learning Objective I: "Explain the relative significance of the effects of
# imperialism from 1750 to 1900."
#
# The CED prints no new historical development for this topic. What it prints
# instead is a REVIEW of the unit's four key concepts, in the framework's own words:
#   KC-5.1  The development of industrial capitalism led to increased standards of
#           living for some, and to continued improvement in manufacturing methods
#           that increased the availability, affordability, and variety of consumer
#           goods.
#   KC-5.2  As states industrialized, they also expanded existing overseas empires
#           and established new colonies and transoceanic relationships.
#   KC-5.3  The 18th century marked the beginning of an intense period of revolution
#           and rebellion against existing governments, leading to the establishment
#           of new nation-states around the world.
#   KC-5.4  As a result of the emergence of transoceanic empires and a global
#           capitalist economy, migration patterns changed dramatically, and the
#           numbers of migrants increased significantly.
#
# The unit's own statements, studied in topics 6.1 to 6.7, are the evidence this
# module reasons with: KC-5.2.III (ideologies used to justify imperialism),
# KC-5.2.I.A to KC-5.2.I.E (shifts in control, and economic imperialism),
# KC-5.2.II.B and KC-5.2.II.C (land expansion, and anti-imperial resistance),
# KC-5.3.III.D and KC-5.3.III.E (nationalism and anticolonial movements;
# rebellions influenced by religious ideas), KC-5.1.II.A and KC-5.1.II.C (export
# economies, and trade organized to European and American advantage), and
# KC-5.4.I to KC-5.4.III.C (the causes and effects of migration).
#
# THREE CAREFUL POINTS.
#   1. KC-5.1 says increased standards of living FOR SOME. That qualification is the
#      framework's own and is the single most useful thing in this topic for a
#      reasoning question, because it is exactly what qualifies an argument that
#      industrial capitalism raised living standards for everyone. Items 12 and 22
#      turn on it and no item drops it.
#   2. CAUSATION IS THE REASONING PROCESS, so the DIRECTION of each review
#      statement matters: industrialization to imperial expansion in KC-5.2, and
#      transoceanic empires and a capitalist economy to changed migration in
#      KC-5.4. Both reversals are offered as distractors and both anchors carry
#      two clauses.
#   3. AN ASSOCIATION IS NOT A CAUSE, and item 24 is built on the difference. The
#      hypothetical record in items 23 and 24 shows two quantities moving together
#      across four territories and settles nothing about why, which is the honest
#      thing for a causation topic to teach.
#
# WHAT THIS BANK DOES NOT DO. No item asks for a date, a person, a treaty or a
# quantity, because this topic prints none. Every source is UNATTRIBUTED and
# labelled illustrative; tables are labelled hypothetical and every keyed conclusion
# is recomputable from the table alone.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md. Dates are written "1750 to 1900".
TOPIC = ("6.8", "Causation in the Imperial Age", 6)

_T_INCOMES = dict(
    headers=["Group in one hypothetical industrializing society",
             "Real income at the start of the period (index)",
             "Real income at the end of the period (index)"],
    rows=[["Group 1", "100", "168"],
          ["Group 2", "100", "131"],
          ["Group 3", "100", "104"],
          ["Group 4", "100", "96"]])

_T_TERRITORIES = dict(
    headers=["Hypothetical territory",
             "Share of export earnings from its single largest commodity (percent)",
             "Share of its population living in towns at the end of the period (percent)"],
    rows=[["Territory 1", "82", "14"],
          ["Territory 2", "76", "19"],
          ["Territory 3", "41", "38"],
          ["Territory 4", "35", "44"]])

_T_EPISODES = dict(
    headers=["Hypothetical episode of resistance",
             "Appeal its leaders made",
             "Form the episode took"],
    rows=[["Episode 1", "Religious", "Direct resistance within an empire"],
          ["Episode 2", "Political authority and nationalism", "Creation of a new state on a periphery"],
          ["Episode 3", "Religious", "Rebellion"],
          ["Episode 4", "Political authority and nationalism", "Direct resistance within an empire"],
          ["Episode 5", "Religious and political together", "Rebellion"]])

QUESTIONS = [
 dict(q="What does this unit's final learning objective ask students to explain?",
   choices=[
     "The relative significance of the effects of imperialism from 1750 to 1900",
     "The exact year in which each empire acquired each of its territories",
     "The significance of one effect of imperialism, chosen in advance as the most important",
     "The biography of every official who administered a colony",
     "The rules of grammar used in imperial correspondence"], ans=0,
   why="Unit 6 Learning Objective I reads that students should explain the relative significance of the effects of imperialism from 1750 to 1900. The word relative is the framework's own, and it asks for a weighing rather than for dates, biographies or an effect nominated in advance."),
 dict(q="The course framework describes what the final topic of a unit is for. According to it, this topic gives students an opportunity to do what?",
   choices=[
     "To draw upon the key concepts and historical developments they have studied in the unit and practise the suggested skill",
     "To learn a set of key concepts that appear in no other topic of the unit",
     "To memorize the dates of the events named in the unit",
     "To study a period that the rest of the unit does not cover",
     "To replace the unit's key concepts with a single explanation"], ans=0,
   why="The CED's own description of this topic says that the final topic focuses on the skill of argumentation and provides an opportunity for students to draw upon the key concepts and historical developments they have studied in the unit, using evidence relevant to those key concepts. It introduces no new development, no new period and no list of dates, which is why Unit 6 Learning Objective I is a skill objective."),
 dict(q="The suggested skill for this topic names three things a student may do to an argument using diverse and alternative evidence. What are they?",
   choices=[
     "Corroborate it, qualify it, or modify it",
     "Repeat it, summarize it, or translate it",
     "Accept it, memorize it, or recite it",
     "Reject it, replace it, or ignore it",
     "Shorten it, lengthen it, or reorder it"], ans=0,
   why="Suggested skill 6.D reads: corroborate, qualify, or modify an argument using diverse and alternative evidence in order to develop a complex argument. Those three verbs are the framework's own, and Unit 6 Learning Objective I is the objective they serve; repeating, accepting or rejecting an argument outright is none of them."),
 dict(q="One of the things the suggested skill says a complex argument might do concerns the number of factors in play. Which is it?",
   choices=[
     "Explain nuance of an issue by analyzing multiple variables",
     "Settle an issue by identifying the single variable that explains it",
     "Avoid any issue in which more than one variable is present",
     "Reduce every issue to the intentions of one person",
     "Treat every variable as equally important without argument"], ans=0,
   why="Suggested skill 6.D lists explaining nuance of an issue by analyzing multiple variables among the things a complex argument might do, and Unit 6 Learning Objective I asks for a weighing of effects. Reducing an issue to one variable or to one person's intentions is the opposite of that, and calling every variable equally important abandons the weighing rather than performing it."),
 dict(q="Another of the suggested skill's listed possibilities concerns the sources an argument rests on. Which is it?",
   choices=[
     "Explain the relative historical significance of a source's credibility and limitations",
     "Establish that every source of the period is equally reliable",
     "Establish that no source of the period can be used at all",
     "Count the number of sources supporting each side",
     "Prefer whichever source is the longest"], ans=0,
   why="Suggested skill 6.D lists explaining the relative historical significance of a source's credibility and limitations. That is a judgement about what a particular source can and cannot show, which is neither a blanket ruling on all sources nor a count nor a preference for length, and it serves Unit 6 Learning Objective I's demand for relative significance."),
 dict(q="A third possibility the suggested skill lists concerns how an argument reaches beyond its own subject. Which is it?",
   choices=[
     "Explain relevant and insightful connections within and across periods",
     "Confine every argument strictly to a single topic",
     "Compare periods only where their dates are identical",
     "Treat each period as unconnected to every other",
     "Explain connections only where a document survives from both periods"], ans=0,
   why="Suggested skill 6.D lists explaining relevant and insightful connections within and across periods among the things a complex argument might do. Confining an argument to one topic, or refusing to relate periods at all, is what that possibility rules out, and Unit 6 Learning Objective I asks students to weigh effects that run across the unit's topics."),
 dict(q="The last of the suggested skill's listed possibilities concerns the argument itself. Which is it?",
   choices=[
     "Explain how or why a historical claim or argument is or is not effective",
     "Declare every historical claim effective by definition",
     "Declare every historical claim ineffective by definition",
     "Judge a claim solely by whether its author was well regarded",
     "Judge a claim solely by whether it is stated confidently"], ans=0,
   why="Suggested skill 6.D lists explaining how or why a historical claim or argument is or is not effective. That asks for reasons about the claim itself, which neither a blanket verdict nor a judgement of the author's standing nor the confidence of the wording supplies, and Unit 6 Learning Objective I is the objective the skill serves here."),
 dict(q="The unit review states what the development of industrial capitalism led to. What does it say?",
   choices=[
     "Increased standards of living for some, and continued improvement in manufacturing methods that increased the availability, affordability and variety of consumer goods",
     "Increased standards of living for everyone in every society it reached",
     "Falling standards of living everywhere, and a decline in the variety of consumer goods",
     "No change in standards of living, and no change in manufacturing methods",
     "Increased standards of living for some, and a fall in the availability of consumer goods"], ans=0,
   why="KC-5.1, printed in this unit's review, reads that the development of industrial capitalism led to increased standards of living FOR SOME, and to continued improvement in manufacturing methods that increased the availability, affordability, and variety of consumer goods. The qualification and the improvement are both parts of that sentence, so an option dropping either one misreports it."),
 dict(q="The unit review states what states did as they industrialized. What does it say?",
   choices=[
     "They expanded existing overseas empires and established new colonies and transoceanic relationships",
     "They surrendered their existing overseas empires and established no new colonies",
     "They confined their activity to their own borders",
     "They established new colonies but abandoned every empire they already held",
     "They established transoceanic relationships in place of any colonial holding"], ans=0,
   why="KC-5.2, printed in this unit's review, reads that as states industrialized, they also expanded existing overseas empires and established new colonies and transoceanic relationships. All three are asserted together, so an option that keeps one and denies the others misreports the sentence."),
 dict(q="What does the unit review say the intense period of revolution and rebellion against existing governments led to?",
   choices=[
     "The establishment of new nation-states around the world",
     "The abolition of the nation-state as a form of government",
     "The consolidation of every existing government in place",
     "The end of all rebellion against governments",
     "The transfer of every colony to a chartered company"], ans=0,
   why="KC-5.3, printed in this unit's review, reads that the intense period of revolution and rebellion against existing governments led to the establishment of new nation-states around the world. Consolidation of existing governments and abolition of the nation-state are each the reverse of that clause."),
 dict(q="The unit review gives the setting in which migration patterns changed dramatically and the numbers of migrants increased significantly. What is it?",
   choices=[
     "The emergence of transoceanic empires and of a global capitalist economy",
     "The closing of transoceanic empires and the collapse of world markets",
     "A general decline in the world's population",
     "The prohibition of migration by most governments",
     "The disappearance of the differences between societies"], ans=0,
   why="KC-5.4, printed in this unit's review, reads that as a result of the emergence of transoceanic empires and a global capitalist economy, migration patterns changed dramatically and the numbers of migrants increased significantly. Each rejected option asserts the opposite of one clause of that sentence."),
 dict(q="A student writes that industrial capitalism raised standards of living for everyone it reached. Which of the unit's review statements most directly qualifies that argument?",
   choices=[
     "The statement that industrial capitalism raised standards of living for some",
     "The statement that industrializing states expanded overseas empires",
     "The statement that migration patterns changed dramatically",
     "The statement that revolution led to new nation-states",
     "The statement that manufacturing methods continued to improve"], ans=0,
   why="KC-5.1's own wording is increased standards of living FOR SOME, which is narrower than the student's everyone and therefore limits the claim rather than contradicting or confirming it. Suggested skill 6.D calls that qualifying an argument, and the other review statements are about empire, migration and revolution and bear on this claim only indirectly."),
 dict(q="An argument holds that a particular process operated throughout a region. A student finds diverse evidence showing that it operated in most of the region but not in one part of it. Using that evidence to limit the argument's scope rather than to discard it is best described as",
   choices=[
     "qualifying the argument",
     "corroborating the argument without change",
     "rejecting the argument as wholly false",
     "ignoring the evidence as inconvenient",
     "replacing the argument with an unrelated one"], ans=0,
   why="Suggested skill 6.D names corroborate, qualify and modify as the three things a student may do to an argument with diverse and alternative evidence. Narrowing where a claim holds, while keeping the claim, is what qualifying means; it is neither confirmation without change nor a rejection, and Unit 6 Learning Objective I asks for exactly this kind of weighing."),
 dict(q="A student writes that overseas empires caused the states that held them to industrialize. How does this relate to what the unit review states?",
   choices=[
     "It reverses the direction the review gives, which runs from states industrializing to their expanding empires and establishing new colonies",
     "It restates the direction the review gives, which runs from empires to industrialization",
     "It agrees with the review, which gives no direction between the two",
     "It is unconnected to the review, which does not mention empires",
     "It is unconnected to the review, which does not mention industrialization"], ans=0,
   why="KC-5.2 reads that AS STATES INDUSTRIALIZED, they also expanded existing overseas empires and established new colonies and transoceanic relationships, which puts industrialization first in the order of that sentence. Causation is this topic's reasoning process, so the direction is the point, and both clauses of the key are needed because the exact reversal is offered."),
 dict(q="A student writes that the growth of migration in this period produced the transoceanic empires and the global capitalist economy. How does this relate to what the unit review states?",
   choices=[
     "It reverses the direction the review gives, which makes changed migration the result of those empires and that economy",
     "It restates the direction the review gives, which makes migration the cause of both",
     "It agrees with the review, which gives no direction between them",
     "It is unconnected to the review, which does not mention migration",
     "It is unconnected to the review, which does not mention a capitalist economy"], ans=0,
   why="KC-5.4 reads that AS A RESULT OF the emergence of transoceanic empires and a global capitalist economy, migration patterns changed dramatically and the numbers of migrants increased significantly. The phrase as a result of fixes which side is the cause, and the reversal is offered as a distractor, so both clauses of the key are needed."),
 dict(q="What does it mean to argue about the relative significance of the effects of imperialism, as this unit's final objective asks?",
   choices=[
     "To weigh the effects against one another and give reasons for ranking them as one does",
     "To list every effect the unit names without comparing them",
     "To choose the effect that is easiest to describe",
     "To declare that all effects were equally significant and stop there",
     "To count how many pages the framework devotes to each effect"], ans=0,
   why="Unit 6 Learning Objective I asks students to explain the relative significance of the effects of imperialism from 1750 to 1900, and suggested skill 6.D asks for a complex argument built with diverse evidence. A ranking with reasons is what those two together require; a bare list, an easy choice, a flat declaration of equality and a page count all avoid the weighing."),
 dict(q="A student explains imperial expansion in this period entirely by the ideologies used to justify it. Which criticism of that explanation does the suggested skill support?",
   choices=[
     "That the unit names economic and strategic factors alongside the ideological ones, so an explanation using one variable is less nuanced than the evidence allows",
     "That ideologies played no part in imperial expansion at all",
     "That an explanation should always rest on exactly one variable",
     "That the unit names no factor in imperial expansion other than ideology",
     "That ideological explanations cannot be supported by any source"], ans=0,
   why="KC-5.2.III names the ideologies used to justify imperialism, while KC-5.1.II.A names the need for raw materials and food and KC-5.1.II.C and KC-5.2.I.E describe trade organized to European and American advantage and economic imperialism. Suggested skill 6.D asks students to explain nuance by analyzing multiple variables, which is what a single-variable account gives up, and it does not follow that ideology played no part."),
 dict(q="An argument about conditions in a colony rests entirely on one report written by an official of the governing power. What does the suggested skill ask a student to say about that?",
   choices=[
     "That the report's credibility and its limitations both bear on how much the argument can carry",
     "That the report proves the argument, since it is an official document",
     "That the report is worthless, since its author served the governing power",
     "That the argument needs no evidence beyond a single document of any kind",
     "That official documents may never be used in a historical argument"], ans=0,
   why="Suggested skill 6.D asks students to explain the relative historical significance of a source's credibility and limitations, which is a judgement about what a source can and cannot bear rather than a verdict of proof or worthlessness. KC-5.4.III.C's account of receiving societies and KC-5.2.I.A's account of colonial administration both come from framework statements rather than from any one official's report, which is why a single document cannot settle a claim of this size."),
 dict(q="Two students defend the same conclusion about the effects of imperialism. One states the conclusion and asserts that it is obvious; the other names the process that produced it and points to evidence from the unit. Which is the more effective argument, and why?",
   choices=[
     "The second, because it states a mechanism and offers evidence a reader can test",
     "The first, because a shorter argument is easier to follow",
     "The first, because confidence is what makes an argument persuasive",
     "The second, but only because it is longer than the first",
     "Neither, because effectiveness cannot be judged in historical writing"], ans=0,
   why="Suggested skill 6.D asks students to explain how or why a historical claim or argument is or is not effective, so effectiveness is a judgement the framework expects to be made and defended. An argument naming a process and citing evidence gives a reader something to check, which brevity, confidence and length do not, and Unit 6 Learning Objective I asks for reasons behind a weighing."),
 dict(q="A student connects this unit's account of export economies to its account of migration. Which connection does the framework's own statements support?",
   choices=[
     "That economies producing raw materials for distant factories and a global capitalist economy that moved labour are parts of one interconnected system",
     "That export economies and migration are described by the framework as unrelated developments",
     "That migration is said by the framework to have ended the growth of export economies",
     "That export economies are said by the framework to have prevented all labour migration",
     "That the framework treats the two as belonging to different centuries"], ans=0,
   why="KC-5.1.II.A describes export economies growing to supply factories and urban populations, and KC-5.4 states that migration patterns changed as a result of transoceanic empires and a global capitalist economy. Suggested skill 6.D asks for relevant connections within and across periods, and these two statements describe the same economy from two sides rather than unrelated or opposed developments."),
 dict(q="The record below reports the real income of four groups in one hypothetical industrializing society, at the start and at the end of the period. Which conclusion does it support?",
   choices=[
     "Real income rose for most of the groups but did not rise for all of them",
     "Real income rose for every group in the society",
     "Real income fell for every group in the society",
     "Real income was unchanged for every group in the society",
     "Real income rose for exactly one group and fell for the rest"], ans=0,
   table=_T_INCOMES,
   why="Read from the record alone: three groups end above their starting index, at 168, 131 and 104, and one ends below it at 96. KC-5.1 states that industrial capitalism led to increased standards of living FOR SOME, and a record in which most but not all groups gain is that qualification in a table."),
 dict(q="A student uses the same hypothetical income record to argue that industrial capitalism raised living standards for everyone in this society. What does the record do to that argument?",
   choices=[
     "It qualifies the argument, because one of the four groups ends the period below where it began",
     "It corroborates the argument without change, because most groups gained",
     "It leaves the argument untouched, because the record reports no incomes",
     "It refutes the argument entirely, because no group gained",
     "It modifies the argument into a claim about manufacturing methods"], ans=0,
   table=_T_INCOMES,
   why="One group's index ends at 96 against a start of 100, so the everyone in the student's claim is wrong while the gains of the other three stand, which is what suggested skill 6.D calls qualifying rather than corroborating or refuting. KC-5.1's own wording, increased standards of living for some, is the framework statement the record illustrates."),
 dict(q="The table below reports, for four hypothetical territories, the share of export earnings coming from the largest single commodity and the share of the population living in towns. What pattern does it show?",
   choices=[
     "The territories with the most concentrated exports have the smallest urban shares",
     "The territories with the most concentrated exports have the largest urban shares",
     "Export concentration and urban share rise and fall together across the four",
     "The four territories have the same export concentration as one another",
     "The table gives export concentration but no urban share"], ans=0,
   table=_T_TERRITORIES,
   why="Read from the table alone: 82 percent concentration against 14 percent urban, 76 against 19, 41 against 38 and 35 against 44, so the two columns move in opposite directions across the four rows. KC-5.1.II.A describes export economies specializing in extraction and in food and industrial crops, which is the kind of economy the first column measures."),
 dict(q="A student argues from the same hypothetical table that concentrating exports on one commodity prevented towns from growing. What is the strongest objection to that argument?",
   choices=[
     "Four territories moving together show an association, which does not by itself establish which way any cause ran or whether a third factor produced both",
     "The table shows no association between the two columns at all",
     "The table shows the opposite association from the one the student describes",
     "An association among territories can never be evidence of anything",
     "The argument fails because the table does not name the territories"], ans=0,
   table=_T_TERRITORIES,
   why="The association is real in the table, running from 82 against 14 down to 35 against 44, so the objection cannot be that it is absent or reversed. Causation is this topic's reasoning process and suggested skill 6.D asks students to explain nuance by analyzing multiple variables, which is what a jump from an association among four cases to a single cause skips over."),
 dict(q="The record below lists five hypothetical episodes of resistance, the appeal each set of leaders made and the form the episode took. A student argues that resistance in this period was religious in inspiration throughout. What does the record do to that argument?",
   choices=[
     "It qualifies the argument, since two episodes rest on appeals to political authority and nationalism and one combines the two kinds of appeal",
     "It corroborates the argument without change, since every episode rests on a religious appeal",
     "It refutes the argument entirely, since no episode rests on a religious appeal",
     "It leaves the argument untouched, since the record does not report the appeals made",
     "It modifies the argument into a claim about the forms resistance took"], ans=0,
   table=_T_EPISODES,
   why="Read from the record alone: two episodes are led by an appeal to political authority and nationalism, one combines that with a religious appeal and two are religious, so the argument holds for part of the record and not for all of it. KC-5.3.III.E says some rebellions were influenced by religious ideas and KC-5.3.III.D names growing nationalism and questions about political authority, so the framework itself gives both, which is why suggested skill 6.D calls this qualifying."),
 dict(q="Using the same hypothetical record of resistance episodes, which episode combines an appeal to political authority and nationalism with the creation of a new state on a periphery?",
   choices=[
     "Episode 2",
     "Episode 1",
     "Episode 3",
     "Episode 4",
     "Episode 5"], ans=0,
   table=_T_EPISODES,
   why="Read from the record alone: Episode 2 is the only row pairing that appeal with that form, since Episode 4 makes the same appeal but takes the form of direct resistance within an empire and the remaining episodes are rebellions or direct resistance. KC-5.2.II.C names direct resistance within empires and the creation of new states on the peripheries as the forms anti-imperial resistance took, and KC-5.3.III.D names nationalism among its causes."),
 dict(q="A student argues that discontent with imperial rule expressed itself only in rebellion. Which of the unit's statements most directly qualifies that argument?",
   choices=[
     "The statement that anti-imperial resistance took various forms, including direct resistance within empires and the creation of new states on the peripheries",
     "The statement that ideologies were used to justify imperialism",
     "The statement that migrants often created ethnic enclaves",
     "The statement that industrial capitalism improved manufacturing methods",
     "The statement that export economies grew to supply distant factories"], ans=0,
   why="KC-5.2.II.C states that anti-imperial resistance took various forms, including direct resistance within empires and the creation of new states on the peripheries, which is broader than rebellion alone and therefore limits the student's claim. KC-5.3.III.E, that discontent led to rebellions some of which were influenced by religious ideas, is the statement the student has generalized from, and suggested skill 6.D calls this qualifying."),
 dict(q="What makes evidence diverse and alternative in the sense the suggested skill intends?",
   choices=[
     "That it comes from more than one kind of source or vantage point, including ones that do not simply agree with the argument",
     "That it comes from as many documents as possible, whatever they say",
     "That it comes only from sources the argument's author finds persuasive",
     "That it comes only from official documents of the period",
     "That it comes from sources written in more than one language"], ans=0,
   why="Suggested skill 6.D asks students to corroborate, qualify or modify an argument using diverse and alternative evidence in order to develop a complex argument, and an argument can only be qualified or modified by evidence that does not merely repeat it. A count of documents, a selection of congenial ones, a single category of source and a language test are none of them that, and Unit 6 Learning Objective I's weighing requires the same breadth."),
 dict(q="Which question about the effects of imperialism can be settled from the framework, and which cannot?",
   choices=[
     "Which kinds of effect the framework identifies can be settled; which single effect was the most significant cannot, since that is the argument the student is asked to make",
     "Which single effect was the most significant can be settled; which kinds of effect the framework identifies cannot",
     "Neither the kinds of effect nor the framework's own statements can be settled from it",
     "Both the kinds of effect and the exact year each began can be settled",
     "Only the number of colonies each state held can be settled"], ans=0,
   why="The unit review names four key concepts covering industrial capitalism, imperial expansion, revolution and migration, so the kinds of effect are settled by the framework. Unit 6 Learning Objective I asks students to explain relative significance, which means the ranking is the argument to be made and defended rather than a fact to be looked up, and the anchor carries both clauses because the exact reversal is offered."),
 dict(q="Taking the unit's four review key concepts together, what account of this period do they give?",
   choices=[
     "Industrial capitalism raised living standards for some and improved manufacturing, industrializing states expanded empires and built new colonies and transoceanic relationships, revolution and rebellion produced new nation-states, and migration changed dramatically and grew",
     "Industrial capitalism raised living standards for everyone, and no state expanded its empire during the period",
     "States expanded their empires, but neither revolution nor migration is part of the framework's account",
     "Revolution produced new nation-states, and the framework describes no economic development in the period",
     "The framework describes economic and political change but identifies no change in migration"], ans=0,
   why="KC-5.1, KC-5.2, KC-5.3 and KC-5.4 are the four statements the CED prints as this unit's review, and the key states each of them in turn, including KC-5.1's qualification that living standards rose for some. Each rejected option deletes one of the four or overstates KC-5.1, and Unit 6 Learning Objective I asks students to weigh these effects against one another rather than to drop any."),
]
