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
#   1. KC-5.1 says increased standards of living FOR SOME, and separately that
#      improved manufacturing increased the availability, affordability and variety
#      of consumer goods. The qualification is the framework's own and is the most
#      useful thing in this topic for a reasoning question, because it is exactly
#      what qualifies an argument that industrial capitalism raised living
#      standards for everyone. Items 8, 12, 22 and 30 carry it and no item drops it.
#
#      ITEMS 21 AND 22 WERE REBUILT ON THE SECOND CLAUSE, not the first, and the
#      reason is worth recording. Their first draft was a table of four groups'
#      real income indexed to a hundred. A cross-subject similarity scan then
#      found w5_7 item 23 -- written independently by a sibling agent for topic
#      5.7 -- to be the SAME table: four groups, the same base of a hundred, and
#      two of four end values identical (168 and 96). Both drafts had come from
#      KC-5.1's "for some" by the shortest route. Agents converge, which CLAUDE.md
#      warns of, and a similarity score is only useful if a match above it is read
#      rather than waved through. These items now rest on the consumer goods
#      clause and ask a different question of it, and item 22 turns on what a
#      record of ownership can and cannot establish about wellbeing.
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
# ITEMS 25 AND 26 WERE ALSO REBUILT, for the same reason as 21 and 22. Their first
# draft was a five-row register of resistance episodes with a form column and an
# appeal column, and the similarity scan matched it to w6_3 items 16 to 18, which a
# sibling had already built as a five-row register of resistance episodes with a
# form column and a religious-ideas column, down to an item asking which episode
# combined a new state on a periphery with the other attribute. Two agents reached
# the same table from the same key concepts. These items now tabulate ARGUMENTS --
# the evidence each rests on and whether it states a mechanism -- which is what
# suggested skill 6.D is actually about and what no other topic in this subject has
# reason to tabulate.
#
# WHAT THIS BANK DOES NOT DO. No item asks for a date, a person, a treaty or a
# quantity, because this topic prints none. Every source is UNATTRIBUTED and
# labelled illustrative; tables are labelled hypothetical and every keyed conclusion
# is recomputable from the table alone.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md. Dates are written "1750 to 1900".
TOPIC = ("6.8", "Causation in the Imperial Age", 6)

_T_GOODS = dict(
    headers=["Consumer good in one hypothetical industrializing society",
             "Households in every hundred owning it at the start of the period",
             "Households in every hundred owning it at the end of the period"],
    rows=[["A factory-woven cotton garment", "31", "92"],
          ["A cast-iron cooking vessel", "18", "74"],
          ["A printed book or newspaper", "9", "51"],
          ["A clock or watch", "6", "28"]])

_T_TERRITORIES = dict(
    headers=["Hypothetical territory",
             "Share of export earnings from its single largest commodity (percent)",
             "Share of its population living in towns at the end of the period (percent)"],
    rows=[["Territory 1", "82", "14"],
          ["Territory 2", "76", "19"],
          ["Territory 3", "41", "38"],
          ["Territory 4", "35", "44"]])

_T_ARGUMENTS = dict(
    headers=["Claim about this period, in a hypothetical set of student essays",
             "Evidence the claim rests on",
             "Whether the claim states a mechanism"],
    rows=[["Claim 1", "One official report", "No"],
          ["Claim 2", "Several kinds of source, including ones that disagree", "Yes"],
          ["Claim 3", "Several kinds of source, including ones that disagree", "No"],
          ["Claim 4", "One official report", "Yes"]])

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
 dict(q="The unit review says that continued improvement in manufacturing methods increased three things about consumer goods. Which three?",
   choices=[
     "Their availability, their affordability and their variety",
     "Their availability and their variety, but not their affordability",
     "Their affordability and their variety, but not their availability",
     "Their durability, their weight and the cost of carrying them",
     "Their scarcity, their price and their uniformity"], ans=0,
   why="KC-5.1, printed in this unit's review, reads that industrial capitalism led to continued improvement in manufacturing methods that increased the availability, affordability, and variety of consumer goods. Those three nouns are the framework's own; dropping one of them, or replacing the list with durability, weight, carriage, scarcity, price or uniformity, misreports the sentence."),
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
 dict(q="The unit review makes two assertions about migration itself in this period. Which pair does it make?",
   choices=[
     "That migration patterns changed dramatically, and that the numbers of migrants increased significantly",
     "That migration patterns changed dramatically, and that the numbers of migrants fell",
     "That the numbers of migrants increased, and that migration patterns were otherwise unchanged",
     "That neither the patterns of migration nor the numbers of migrants changed",
     "That migration ceased to cross the borders of states during the period"], ans=0,
   why="KC-5.4, printed in this unit's review, reads that migration patterns changed dramatically AND the numbers of migrants increased significantly. Both assertions stand in one sentence, so an option keeping one and reversing the other misreports it, and the anchor carries both because a distractor offers each half alone."),
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
 dict(q="The record below reports, for four consumer goods in one hypothetical industrializing society, how many households in every hundred owned each good at the start and at the end of the period. Which conclusion does it support?",
   choices=[
     "Every one of these goods reached more households by the end, and the goods that were already commonest spread furthest",
     "Every one of these goods reached more households by the end, and the goods that were rarest at the start spread furthest",
     "None of these goods reached more households by the end of the period",
     "All four goods spread to exactly the same extent",
     "Only one of these goods reached more households by the end of the period"], ans=0,
   table=_T_GOODS,
   why="Read from the record alone: the garment runs 31 to 92, the cooking vessel 18 to 74, the book or newspaper 9 to 51 and the clock 6 to 28, so all four spread and the rises fall in the same order as the starting figures. KC-5.1 states that continued improvement in manufacturing methods increased the availability, affordability, and variety of consumer goods, and the reversed reading of the pattern is offered as a distractor."),
 dict(q="A student uses the same hypothetical record of consumer goods to argue that industrial capitalism made every member of this society better off. Which statement best describes what the record can and cannot establish?",
   choices=[
     "It establishes that these four goods reached more households, but not that every member of the society was better off",
     "It establishes that every member of the society was better off, but not that these goods reached more households",
     "It establishes both of those things, since ownership of goods and wellbeing are the same measure",
     "It establishes neither, since none of the four goods reached more households",
     "It establishes nothing at all, since a record of this kind may not be used in a historical argument"], ans=0,
   table=_T_GOODS,
   why="Every column of the record counts households owning a good and no column reports an income, a wage or a person's condition, so the record reaches the availability of consumer goods and stops there. KC-5.1 keeps those apart itself, saying that industrial capitalism led to increased standards of living for some AND to improvements that increased the availability of consumer goods, and suggested skill 6.D asks students to explain the relative significance of a source's credibility and limitations."),
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
   why="The association is real in the table, running from 82 against 14 down to 35 against 44, so the objection cannot be that it is absent or reversed. Causation is this topic's reasoning process and suggested skill 6.D asks students to explain nuance by analyzing multiple variables, which is what a jump from an association among four cases to a single cause skips over. Unit 6 Learning Objective I asks for a weighing of effects, and a weighing rests on knowing which way a cause ran."),
 dict(q="The record below describes four claims about this period made in a hypothetical set of student essays, the evidence each rests on and whether each states a mechanism. Which claim best meets both of the tests the suggested skill sets?",
   choices=[
     "Claim 2",
     "Claim 1",
     "Claim 3",
     "Claim 4",
     "No claim in the record meets both tests"], ans=0,
   table=_T_ARGUMENTS,
   why="Read from the record alone: Claim 2 is the only row that both rests on several kinds of source, including ones that disagree, and states a mechanism. Suggested skill 6.D asks for diverse and alternative evidence and for an explanation of how or why a claim is effective, and those are the two columns; Claims 1, 3 and 4 each satisfy at most one of them, and Unit 6 Learning Objective I asks for the reasons behind a weighing, which is what a stated mechanism supplies."),
 dict(q="A student says that one of the claims in the same hypothetical record is as well supported as the strongest, because both state a mechanism. Which difference between them does the record show?",
   choices=[
     "The weaker claim rests on one official report, while the stronger rests on several kinds of source including ones that disagree",
     "The weaker claim rests on several kinds of source, while the stronger rests on one official report",
     "The weaker claim states no mechanism, while the stronger states one",
     "The two claims rest on the same evidence and differ only in length",
     "The record does not report what evidence any claim rests on"], ans=0,
   table=_T_ARGUMENTS,
   why="Read from the record alone: two claims state a mechanism, and the two are separated only by their evidence, one resting on a single official report and the other on several kinds of source including ones that disagree. Suggested skill 6.D asks for the relative historical significance of a source's credibility and limitations and for diverse and alternative evidence, and the reversal of which claim rests on which is offered as a distractor. Unit 6 Learning Objective I asks students to defend a weighing, which is why the evidence a claim rests on decides between two claims that both state a mechanism."),
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
