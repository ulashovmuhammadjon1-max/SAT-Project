# AP WORLD HISTORY: MODERN 5.10 Continuity and Change in the Industrial Age
# CED effective Fall 2024, Unit 5 Revolutions, c. 1750 to c. 1900.
# Reasoning process: Continuity and Change. Suggested skill 6.C, use historical
# reasoning to explain relationships among pieces of historical evidence.
#
# THIS IS THE UNIT'S REASONING TOPIC, AND IT IS WRITTEN AS ONE. The CED says so
# itself on the topic page: "The final topic in this unit focuses on the skill of
# argumentation and so provides an opportunity for your students to draw upon the
# key concepts and historical developments they have studied in this unit. Using
# evidence relevant to this unit's key concepts, students should practice the
# suggested skill for this topic." So nothing here is recall of a definition. Every
# item asks what a piece of evidence supports, what it cannot support, how two
# pieces bear on one another, or how a claim has to be qualified to match the
# framework's own wording. The recall of these statements belongs to topics 5.1
# through 5.9 and is not repeated here.
#
# Learning objective:
#   Unit 5 LO K  Explain the extent to which industrialization brought change from
#                1750 to 1900.
#
# REVIEW: UNIT 5 KEY CONCEPTS, which is the heading the CED prints on this topic's
# page in place of "Historical Developments". In the framework's own words:
#   KC-5.1        The development of industrial capitalism led to increased
#                 standards of living FOR SOME, and to continued improvement in
#                 manufacturing methods that increased the availability,
#                 affordability, and variety of consumer goods.
#   KC-5.1.IV     Railroads, steamships, and the telegraph made exploration,
#                 development, and communication possible in interior regions
#                 globally, WHICH LED TO increased trade and migration.
#   KC-5.3        The 18th century marked the beginning of an intense period of
#                 revolution and rebellion against existing governments, leading to
#                 the establishment of new nation-states around the world.
#   KC-5.3.I.A    Enlightenment philosophies applied new ways of understanding and
#                 empiricist approaches to both the natural world and human
#                 relationships; they also reexamined the role that religion played
#                 in public life and emphasized the importance of reason.
#                 Philosophers developed new political ideas about the individual,
#                 natural rights, and the social contract.
#   KC-5.3.I      The rise and diffusion of Enlightenment thought that questioned
#                 established traditions in all areas of life OFTEN PRECEDED
#                 revolutions and rebellions against existing governments.
#   KC-5.3.II.i   Nationalism also became a major force shaping the historical
#                 development of states and empires.
#
# Because the CED instructs students to draw on everything studied in the unit,
# items here also reason from KC-5.1.II.B (a region's share falling while it
# CONTINUED to produce), KC-5.1.VI.A and KC-5.1.VI.C. Those are unit 5 statements;
# nothing is drawn from unit 6.
#
# WHAT MAKES A KEY CHECKABLE IN A REASONING TOPIC. Two things, and no item ships
# without one of them:
#   1. The key is what the framework's OWN WORDING allows. "For some", "at times",
#      "often preceded" and "accompanied" are each a limit on an inference, and
#      items 2, 9, 20, 26 and 29 turn on one of them. An argument that drops a
#      qualification is wrong against the CED, not merely against taste.
#   2. The key matches the SCOPE of the evidence offered. A record of one district
#      supports a claim about that district; a memoir supports a claim about the
#      family that wrote it; two figures rising together are two figures rising
#      together. Items 7, 18, 24 and 26 turn on that, which is skill 6.C stated
#      plainly.
#
# ON PERIODISATION. The CED states that events, processes, and developments are
# not constrained by the given dates and may begin before, or continue after, the
# period. Item 22 keys that statement itself, and no other item anywhere in this
# module rests on a boundary year. Dates are written "1750 to 1900".
#
# ONE PHRASE THE SHARED FIGURE GATE REJECTED, AND WHY IT WAS RIGHT TO. Item 27
# originally offered "Figures showing manufacturing rising steeply in some regions
# ...", meaning figures in the sense of numbers. wh_check's figure-language gate
# fired on it, because "figures showing" has the exact shape of a reference to a
# displayed illustration and a regex cannot tell the two senses apart from the
# words alone. Widening the shared gate to let it through would have weakened it
# for every other module in the subject, so the choice was reworded to "Records of
# manufacturing output ...", which says the same thing and cannot be misread. The
# checker was right; the content was ambiguous.
#
# ON SOURCES AND FIGURES. Section I is stimulus based and this bank cannot display
# images, so every stimulus is a TEXT or a table. No quotation is attributed to a
# real person or document -- each source is explicitly illustrative and
# unattributed. Table figures are HYPOTHETICAL and the stems say so; the CED
# prints no data.
TOPIC = ("5.10", "Continuity and Change in the Industrial Age", 5)

_T_REGIONS = dict(
    headers=["Region in the illustrative sample",
             "Index of manufacturing output, start of the period",
             "Index of manufacturing output, end of the period"],
    rows=[["Region 1", "100", "540"],
          ["Region 2", "100", "310"],
          ["Region 3", "100", "128"],
          ["Region 4", "100", "103"]])

_T_DISTRICTS = dict(
    headers=["Illustrative district", "Share of cloth made in factories (percent)",
             "Share of cloth made in households (percent)"],
    rows=[["District 1", "92", "8"],
          ["District 2", "61", "39"],
          ["District 3", "24", "76"],
          ["District 4", "5", "95"]])

_T_INLAND = dict(
    headers=["Decade of the illustrative sample", "Tonnage of goods carried inland (thousands)",
             "Persons recorded migrating into the interior (thousands)"],
    rows=[["First decade", "30", "4"],
          ["Second decade", "96", "19"],
          ["Third decade", "240", "58"],
          ["Fourth decade", "610", "141"]])

QUESTIONS = [
    dict(
        q="The final topic of this unit asks students to explain the extent to which "
          "industrialization brought change. What does the phrase the extent to which require of "
          "an answer?",
        choices=[
            "That it weigh how much changed against what stayed the same, rather than assert that everything changed",
            "That it assert that industrialization changed everything it touched",
            "That it assert that industrialization changed nothing",
            "That it list the year in which each change occurred",
            "That it confine itself to a single country"],
        ans=0,
        why="Unit 5 Learning Objective K asks for the EXTENT to which industrialization brought "
            "change, and the reasoning process assigned to this topic is continuity and change. "
            "A question about extent is answered by weighing, not by asserting either extreme.",
    ),
    dict(
        q="A student argues that industrialization raised the standard of living of everyone in "
          "the societies it reached. Which review statement in this unit most directly qualifies "
          "that argument?",
        choices=[
            "The statement that industrial capitalism led to increased standards of living for some",
            "The statement that railroads and steamships opened interior regions",
            "The statement that Enlightenment thought often preceded revolutions",
            "The statement that nationalism became a major force shaping states and empires",
            "The statement that the 18th century opened a period of revolution and rebellion"],
        ans=0,
        why="KC-5.1 is printed among this topic's review statements and it says FOR SOME. The "
            "student's claim is the same claim with that qualification removed, so the "
            "framework's own wording is what limits it.",
    ),
    dict(
        q="A student claims that new transport and communication increased the movement of goods "
          "and people during this period. Which piece of evidence would most directly support "
          "that claim?",
        choices=[
            "Records of more cargo and more travellers moving through places newly reached by rail and telegraph",
            "A list of the philosophers whose works circulated in the same decades",
            "The text of a constitution written by a newly established state",
            "A catalogue of the paintings exhibited in an industrial city",
            "The number of monarchs reigning in Europe at the start of the period"],
        ans=0,
        why="KC-5.1.IV, printed among this topic's review statements, says these technologies made "
            "exploration, development, and communication possible in interior regions globally, "
            "which led to increased trade and migration. Evidence of traffic through newly "
            "reached places is evidence about that claim; the rejected records bear on other "
            "statements entirely.",
    ),
    dict(
        q="A student claims that every household in an industrial city saw its purchasing power "
          "rise. Which evidence would most directly weaken that claim?",
        choices=[
            "Records of households in the same city whose earnings bought no more at the end of the period than at the start",
            "Records of the new kinds of goods that appeared in the city's shops",
            "Records of the rail lines built into the city",
            "Records of the newspapers founded in the city",
            "Records of the growth of the city's population"],
        ans=0,
        why="KC-5.1 says industrial capitalism raised standards of living FOR SOME, so a claim "
            "about EVERY household is exactly the claim a counterexample defeats. Unit 5 Learning "
            "Objective K asks for the extent of change, and a single household that gained "
            "nothing settles the question of extent.",
    ),
    dict(
        q="One hypothetical source records that goods of a kind once rare became common and cheap in an "
          "industrial city. A second records that a quarter of that city's households could still "
          "not afford them. Considering both, which statement is best supported?",
        choices=[
            "Goods became more available and affordable, and the gain did not reach every household",
            "Goods became more available and affordable, and every household shared in the gain",
            "Goods became scarcer and dearer during the period",
            "The two records cannot both be true",
            "Neither record bears on the standard of living"],
        ans=0,
        why="KC-5.1 pairs improved manufacturing methods and cheaper, more plentiful consumer "
            "goods with a rise in living standards FOR SOME. Two sources of this kind do not "
            "conflict; together they give the framework's qualified statement in evidence, which "
            "is the relationship this topic's skill asks students to explain.",
    ),
    dict(
        q="Which of the following would best support an argument that something important did NOT "
          "change during this period?",
        choices=[
            "Evidence that a region continued to produce manufactured goods by older methods throughout the period",
            "Evidence that a new rail line was opened in the region",
            "Evidence that a new class of factory owners appeared in the region",
            "Evidence that a telegraph office was built in the region",
            "Evidence that a new nation-state was established in the region"],
        ans=0,
        why="KC-5.1.II.B says that while some regions' share in global manufacturing declined, "
            "those regions CONTINUED to produce manufactured goods, and Unit 5 Learning Objective "
            "K asks for the extent of change, which includes what persisted. Each rejected option "
            "is evidence of change rather than of continuity.",
    ),
    dict(
        q="A hypothetical source records that one industrial district's output of cloth tripled over four "
          "decades. Which claim does that source support as stated?",
        choices=[
            "That cloth output rose in that district over those decades",
            "That cloth output rose everywhere in the world over those decades",
            "That the standard of living rose in that district",
            "That the district's population tripled as well",
            "That the district's workers organized themselves in unions"],
        ans=0,
        why="This topic's suggested skill is reasoning about what pieces of evidence establish, "
            "and a record of one district reaches as far as that district. KC-5.1 attaches living "
            "standards to a separate claim with its own qualification, so output figures alone do "
            "not settle it.",
    ),
    dict(
        q="A student notes that Enlightenment thought spread widely in a region and that a "
          "rebellion against the existing government followed there. Which framework statement "
          "licenses treating the first as related to the second?",
        choices=[
            "The statement that the rise and diffusion of Enlightenment thought often preceded revolutions and rebellions",
            "The statement that railroads and the telegraph opened interior regions",
            "The statement that industrial capitalism raised standards of living for some",
            "The statement that new social classes developed",
            "The statement that rapid urbanization at times brought public health crises"],
        ans=0,
        why="KC-5.3.I, printed among this topic's review statements, connects the diffusion of "
            "Enlightenment thought with revolutions and rebellions against existing governments. "
            "The rejected statements are KC-5.1.IV, KC-5.1, KC-5.1.VI.A and KC-5.1.VI.C, none of "
            "which mentions either half of the student's observation.",
    ),
    dict(
        q="The course framework says the diffusion of Enlightenment thought often preceded "
          "revolutions and rebellions. What does that wording allow a student to conclude in a "
          "single case?",
        choices=[
            "That the sequence was common, not that the thought caused the rebellion in any given case",
            "That the thought caused every rebellion of the period",
            "That no rebellion of the period was connected to that thought",
            "That the rebellion always came first",
            "That the framework dates the diffusion precisely"],
        ans=0,
        why="KC-5.3.I says OFTEN PRECEDED, which reports an order and how frequently it held, not "
            "a mechanism. This topic's skill is reasoning about evidence, and a statement about "
            "what commonly came first cannot by itself settle causation in one instance.",
    ),
    dict(
        q="A student argues that the political map of the world was remade during this period. "
          "Which review statement in this unit most directly supports that argument?",
        choices=[
            "The statement that an intense period of revolution and rebellion led to the establishment of new nation-states around the world",
            "The statement that manufacturing methods continued to improve",
            "The statement that consumer goods became more available and affordable",
            "The statement that railroads and steamships reached interior regions",
            "The statement that middle-class women were increasingly limited to household roles"],
        ans=0,
        why="KC-5.3 is printed among this topic's review statements and it is the one that ends "
            "in new nation-states around the world. The rejected options are KC-5.1, KC-5.1.IV "
            "and KC-5.1.VI.B, which bear on production, transport and social roles rather than on "
            "the map of states.",
    ),
    dict(
        q="Which review statement in this unit would a student cite to argue that a force other "
          "than industrial technology reshaped states during this period?",
        choices=[
            "The statement that nationalism became a major force shaping the historical development of states and empires",
            "The statement that railroads, steamships and the telegraph opened interior regions",
            "The statement that manufacturing methods continued to improve",
            "The statement that consumer goods became more available",
            "The statement that industrial capitalism raised standards of living for some"],
        ans=0,
        why="KC-5.3.II.i is printed among this topic's review statements and names nationalism as "
            "a major force shaping states and empires. Every rejected option comes from KC-5.1 or "
            "KC-5.1.IV, which are about production, goods and technology.",
    ),
    dict(
        q="A source from the period argues that a person's rights exist before any government and "
          "that reason should decide questions once settled by custom. Which review statement does "
          "the source belong to?",
        choices=[
            "The statement that philosophers developed new political ideas about the individual, natural rights and the social contract",
            "The statement that railroads and the telegraph opened interior regions",
            "The statement that industrial capitalism raised standards of living for some",
            "The statement that nationalism shaped the development of states and empires",
            "The statement that manufacturing methods continued to improve"],
        ans=0,
        why="KC-5.3.I.A, printed among this topic's review statements, names new political ideas "
            "about the individual, natural rights, and the social contract, and emphasizes the "
            "importance of reason. The source is illustrative and unattributed, and the key rests "
            "on what it argues rather than on who wrote it.",
    ),
    dict(
        q="Two sources describe the same industrial town. One reports well-built new streets and "
          "rising wages; the other reports crowded courts and fouled water. What is the best "
          "reasoning about the two?",
        choices=[
            "Both may be accurate of different parts of the same town, and the extent of improvement is what has to be argued",
            "One of the two must be a forgery",
            "The later of the two must be the accurate one",
            "Neither can be used as evidence about the town",
            "The two together prove that conditions were unchanged"],
        ans=0,
        why="KC-5.1 says living standards rose FOR SOME and KC-5.1.VI.C says rapid urbanization "
            "AT TIMES brought pollution and housing shortages. Both qualifications allow the two "
            "reports to stand together, and Unit 5 Learning Objective K makes the extent of "
            "improvement the question at issue.",
    ),
    dict(
        q="This topic's suggested skill asks students to use historical reasoning to explain "
          "relationships among pieces of historical evidence. Which of the following is that "
          "skill being exercised?",
        choices=[
            "Showing how two records of the same development bear on one another and on the claim being argued",
            "Listing the records in the order in which they were written",
            "Counting how many records survive from the period",
            "Choosing the record that is easiest to read",
            "Summarizing each record without comparing them"],
        ans=0,
        why="The CED assigns skill 6.C to this topic and describes it as using historical "
            "reasoning to explain relationships among pieces of historical evidence, in service "
            "of Unit 5 Learning Objective K. Listing, counting and summarizing leave the "
            "relationship unexplained.",
    ),
    dict(
        q="The table below reports hypothetical index figures for four regions in one illustrative "
          "sample. Which conclusion does the table support?",
        table=_T_REGIONS,
        choices=[
            "Output rose in every region, but by amounts so different that a claim of uniform transformation is not supported",
            "Output rose by about the same amount in every region",
            "Output fell in every region across the period",
            "Output rose in some regions and fell in others",
            "Output was unchanged in every region"],
        ans=0,
        why="Unit 5 Learning Objective K asks for the extent of change, and the table gives an "
            "answer with two halves in it: every region's index is higher at the end, and the "
            "increases differ by several times over. Both halves are read from the two columns "
            "rather than recalled.",
    ),
    dict(
        q="The table below records hypothetical shares for four illustrative districts. Which "
          "conclusion does the table support?",
        table=_T_DISTRICTS,
        choices=[
            "Factory production predominates in some districts while household production still predominates in others",
            "Factory production predominates in every district",
            "Household production predominates in every district",
            "The two shares are equal in every district",
            "Household production has disappeared from every district"],
        ans=0,
        why="KC-5.1.II.B describes regions that CONTINUED to produce manufactured goods even as "
            "the new methods spread, and Unit 5 Learning Objective K asks how far change went. "
            "The table is read district by district, with the two shares in each row accounting "
            "for all of that district's cloth.",
    ),
    dict(
        q="The table below reports hypothetical figures for one illustrative region across four "
          "decades. Which conclusion does the table support?",
        table=_T_INLAND,
        choices=[
            "The tonnage carried inland and the number of people migrating inland both rise in every decade",
            "Both figures fall in every decade",
            "The tonnage rises while the number of people migrating falls",
            "The number of people migrating rises while the tonnage falls",
            "Neither figure changes across the four decades"],
        ans=0,
        why="KC-5.1.IV says the new transport and communication led to increased trade and "
            "migration, and the table shows two columns moving in the directions that statement "
            "pairs. The conclusion keyed is about the figures themselves, which is all a table of "
            "this kind can establish.",
    ),
    dict(
        q="Suppose a table showed both inland trade and inland migration rising across four "
          "decades. Which of the following would that table alone NOT establish?",
        choices=[
            "That the railroads and the telegraph were the cause of the two increases",
            "That inland trade rose across the decades covered",
            "That inland migration rose across the decades covered",
            "That the two rose during the same decades",
            "That both figures stood higher at the end than at the start"],
        ans=0,
        why="KC-5.1.IV supplies the causal claim, and a table of two rising columns supplies only "
            "the two rising columns. Skill 6.C asks students to reason about what pieces of "
            "evidence do and do not establish, and this is the distinction it turns on most often.",
    ),
    dict(
        q="Combining the statement that new transport reached interior regions with the statement "
          "that this led to increased trade and migration, which claim is best supported?",
        choices=[
            "The reach of the new transport and the growth of inland traffic belong to one connected development",
            "Inland traffic grew before any new transport reached the interior",
            "The new transport reached the interior but inland traffic did not change",
            "The two statements describe unrelated developments",
            "Inland traffic grew only on the coasts"],
        ans=0,
        why="KC-5.1.IV is a single sentence in which railroads, steamships and the telegraph make "
            "exploration, development and communication possible in interior regions globally, "
            "WHICH LED TO increased trade and migration. Explaining that relationship is skill "
            "6.C, and the rejected options break the sentence or reverse it.",
    ),
    dict(
        q="A student writes that industrialization transformed every society it touched, "
          "completely and at the same pace. Which criticism of that claim rests on the course "
          "framework rather than on outside knowledge?",
        choices=[
            "The framework's own statements are qualified, saying that living standards rose for some and that urbanization at times brought difficulties",
            "The framework says industrialization had no effects at all",
            "The framework says industrialization affected only one country",
            "The framework gives an exact pace for the change in each society",
            "The framework denies that manufacturing methods improved"],
        ans=0,
        why="KC-5.1 says FOR SOME and KC-5.1.VI.C says AT TIMES. Those qualifications are printed "
            "in the framework, so an objection built on them is an objection from the course "
            "content rather than from an author's opinion, which is what Unit 5 Learning "
            "Objective K asks for.",
    ),
    dict(
        q="Two students argue from the same evidence, that a district's factories multiplied while "
          "its household weavers continued at work. Whose claim does the evidence better support?",
        choices=[
            "The one who argues that factory production grew alongside older methods that persisted",
            "The one who argues that factory production replaced older methods entirely",
            "The one who argues that older methods replaced factory production",
            "The one who argues that neither form of production existed in the district",
            "The one who argues that the evidence bears on nothing about production"],
        ans=0,
        why="The evidence contains both halves, so the claim that matches it contains both halves "
            "too. KC-5.1.II.B describes exactly that combination, regions continuing to produce "
            "manufactured goods while new methods spread, and Unit 5 Learning Objective K asks "
            "how far the change went.",
    ),
    dict(
        q="The course framework states that its developments are not constrained by the dates of a "
          "period and may begin before or continue after it. What does that statement require of "
          "an argument about this unit?",
        choices=[
            "That the argument not rest on a development having started or stopped exactly at a boundary year",
            "That the argument name the exact year each development began",
            "That the argument treat every development as confined to the years given",
            "That the argument avoid any development lasting more than a decade",
            "That the argument use only sources written within the period"],
        ans=0,
        why="Unit 5 Learning Objective K asks about change from 1750 to 1900, and the CED itself "
            "loosens those boundaries in the sentence quoted in the stem. An argument keyed to a "
            "boundary year would therefore contradict the framework's own statement about its "
            "periods.",
    ),
    dict(
        q="An illustrative and unattributed memoir written late in the period recalls that the "
          "writer's grandparents spun at home while the writer's children work in a mill. Which "
          "relationship does the memoir most directly evidence?",
        choices=[
            "A change in where and how goods were produced across three generations",
            "A change in the political boundaries of the writer's state",
            "A change in the writer's religious beliefs",
            "A change in the price of imported grain",
            "A change in the number of newspapers printed"],
        ans=0,
        why="KC-5.1 describes continued improvement in manufacturing methods and KC-5.1.VI.A the "
            "growth of an industrial working class, and a household that spun at home giving way "
            "to children in a mill is that shift in one family. Unit 5 Learning Objective K asks "
            "how far such change went.",
    ),
    dict(
        q="Taking the same memoir, what would a careful argument NOT claim on its evidence alone?",
        choices=[
            "That the same change occurred at the same time everywhere else",
            "That the writer's family's work changed across the generations described",
            "That members of the writer's family were employed in a mill",
            "That spinning had once been done in the writer's household",
            "That the memoir was written late in the period"],
        ans=0,
        why="Skill 6.C asks students to reason about what evidence establishes, and one family's "
            "memoir reaches as far as that family. KC-5.1.II.B shows why the wider claim needs "
            "separate support: regions differed, and some continued producing by older methods "
            "while others changed.",
    ),
    dict(
        q="A student has one record of a new rail line reaching an inland town and wishes to argue "
          "that trade there increased. What would most strengthen the argument?",
        choices=[
            "A second record, independent of the first, of goods moving through the town before and after the line opened",
            "A second copy of the same record",
            "A list of the names of the line's directors",
            "A description of the locomotive used on the line",
            "The date on which the line's builders were incorporated"],
        ans=0,
        why="KC-5.1.IV connects the arrival of such transport with increased trade, but the "
            "student's single record shows only the arrival. Skill 6.C is about the relationship "
            "between pieces of evidence, and an independent record of the traffic itself is what "
            "supplies the missing half.",
    ),
    dict(
        q="Two developments in a region rose together across the same decades. What does that "
          "alone establish about them?",
        choices=[
            "That they moved together, which is not by itself evidence that one produced the other",
            "That the earlier one caused the later one",
            "That the later one caused the earlier one",
            "That neither is connected to anything else in the period",
            "That the two are the same development under different names"],
        ans=0,
        why="The framework itself distinguishes the two relations: KC-5.1.VI.C says rapid "
            "urbanization ACCOMPANIED global capitalism, while KC-5.1.IV says the new transport "
            "LED TO increased trade and migration. Skill 6.C asks students to tell those apart in "
            "the evidence rather than to assume the stronger one.",
    ),
    dict(
        q="A student argues that industrialization's effects were uneven across the world. Which "
          "evidence would most directly support that argument?",
        choices=[
            "Records of manufacturing output rising steeply in some regions and barely at all in others over the same decades",
            "Records of manufacturing output rising by the same amount in every region",
            "A list of the machines in use in one factory",
            "The text of a treaty between two states",
            "The number of philosophers writing in one decade"],
        ans=0,
        why="KC-5.1.II.B describes a period in which some regions' share of global manufacturing "
            "grew while others' declined even as they continued to produce, and Unit 5 Learning "
            "Objective K asks for the extent of change. A comparison across regions is what a "
            "claim about unevenness requires.",
    ),
    dict(
        q="Which of the following is a claim about continuity rather than about change?",
        choices=[
            "That some regions went on producing manufactured goods by the methods they had long used",
            "That new social classes developed in industrializing societies",
            "That railroads and the telegraph reached interior regions for the first time",
            "That new nation-states were established around the world",
            "That new methods appeared in the production of steel and chemicals"],
        ans=0,
        why="KC-5.1.II.B says those regions CONTINUED to produce manufactured goods, which is the "
            "framework's own statement of persistence. The rejected options come from "
            "KC-5.1.VI.A, KC-5.1.IV, KC-5.3 and KC-5.1.I.E, and each of them asserts something "
            "new rather than something continuing.",
    ),
    dict(
        q="Taking the unit's statements together, which judgement about the extent of change from "
          "1750 to 1900 do they best support?",
        choices=[
            "Change was wide and real, and the framework's own qualifications keep it from being uniform or universal",
            "Change was complete and uniform everywhere it reached",
            "Nothing of importance changed during the period",
            "Change was confined to a single region",
            "The framework offers no basis for judging the extent of change"],
        ans=0,
        why="KC-5.1, KC-5.1.IV and KC-5.3 each assert a substantial change, while for some, at "
            "times and continued to produce qualify how far those changes reached. Unit 5 "
            "Learning Objective K asks precisely for that judgement of extent.",
    ),
    dict(
        q="Which single statement best describes what this final topic of the unit asks students "
          "to do?",
        choices=[
            "Draw on the unit's key concepts as evidence and reason about how the pieces of that evidence bear on a claim about the extent of change",
            "Memorize the year in which each development of the unit began",
            "Choose one key concept and set the others aside",
            "Describe each key concept without relating any of them to another",
            "Judge each source by the reputation of the person who wrote it"],
        ans=0,
        why="The CED introduces this topic by saying it focuses on argumentation and gives "
            "students an opportunity to draw on the key concepts of the unit, using evidence "
            "relevant to them. Unit 5 Learning Objective K supplies the claim at issue and skill "
            "6.C supplies the reasoning about how the evidence relates.",
    ),
]
