# AP WORLD HISTORY: MODERN 4.8 Continuity and Change from 1450 to 1750
# CED effective Fall 2024/2026, Unit 4 Transoceanic Interconnections, c. 1450 to
# c. 1750. Title copied verbatim from WORLD_HISTORY_topics.json.
#
# THIS IS THE UNIT'S REASONING TOPIC. The CED's own words on the page: "The final
# topic in this unit focuses on the skill of argumentation and so provides an
# opportunity for your students to draw upon the key concepts and historical
# developments they have studied in this unit. Using evidence relevant to this
# unit's key concepts, students should practice the suggested skill for this
# topic." So this module is written as a reasoning set, not as fact recall: most
# items ask what a piece of evidence shows, what relationship two pieces stand
# in, what would strengthen or weaken an argument, and where an argument
# outruns what its evidence can carry.
#
# Unit 4: Learning Objective N -- explain how economic developments from 1450 to
# 1750 affected social structures over time.
# Suggested skill 6.C, use historical reasoning to explain relationships among
# pieces of historical evidence. Reasoning process: continuity and change.
#
# The page prints a REVIEW list rather than new content, and this module keys to
# that list and to nothing outside it. In the framework's own words:
#   KC-4.1        The interconnection of the Eastern and Western Hemispheres,
#                 made possible by transoceanic voyaging, transformed trade and
#                 had a significant social impact on the world.
#   KC-4.1.II     Knowledge, scientific learning, and technology from the
#                 Classical, Islamic, and Asian worlds spread, facilitating
#                 European technological developments and innovation.
#   KC-4.1.II.A   The developments included the production of new tools,
#                 innovations in ship designs, and an improved understanding of
#                 regional wind and currents patterns, all of which made
#                 transoceanic travel and trade possible.
#   KC-4.2        Although the world's productive systems continued to be heavily
#                 centered on agriculture, major changes occurred in agricultural
#                 labor, the systems and locations of manufacturing, gender and
#                 social structures, and environmental processes.
#   KC-4.2.II     The demand for labor intensified as a result of the growing
#                 global demand for raw materials and finished products.
#                 Traditional peasant agriculture increased and changed in
#                 nature, plantations expanded, and the Atlantic slave trade
#                 developed and intensified.
#   KC-4.3        Empires achieved increased scope and influence around the
#                 world, shaping and being shaped by the diverse populations they
#                 incorporated.
#   KC-4.3.III.ii Economic disputes led to rivalries and conflict between states.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT. KC-4.2 is a single sentence
# whose subordinate clause is a CONTINUITY and whose main clause is a set of
# CHANGES: productive systems went on being heavily centered on agriculture,
# ALTHOUGH major changes occurred in agricultural labor, in the systems and
# locations of manufacturing, in gender and social structures, and in
# environmental processes. Nothing here keys the change as displacing the
# continuity, which is the single most tempting error in a topic named
# Continuity and Change. KC-4.3 likewise runs in two directions at once, empires
# shaping AND being shaped by the populations they incorporated, and no item
# keys one direction alone.
#
# Dates are written "1450 to 1750". Five choices A-E per HISTORY_BRIEF.md. Every
# stimulus is hypothetical or unattributed; no quotation is put in a real
# person's mouth.
TOPIC = ("4.8", "Continuity and Change from 1450 to 1750", 4)

_T_EVIDENCE = dict(
    headers=["Piece of evidence in a hypothetical file", "What it records"],
    rows=[["Evidence 1", "Rising exports of a raw material from one region"],
          ["Evidence 2", "More laborers recorded on the plantations of that region"],
          ["Evidence 3", "More enslaved persons landed at that region's ports"],
          ["Evidence 4", "The rebuilding of a cathedral tower in a distant city"]])

_T_WORKFORCE = dict(
    headers=["Period of a hypothetical survey",
             "Share of the recorded workforce in agriculture (percent)",
             "Share of the recorded workforce in manufacturing crafts (percent)"],
    rows=[["First period", "82", "9"],
          ["Second period", "79", "12"],
          ["Third period", "76", "16"],
          ["Fourth period", "73", "20"]])

_T_CLAIMS = dict(
    headers=["Claim in a hypothetical essay", "Evidence the essay offers for it"],
    rows=[["That the demand for labor intensified",
           "Records of more laborers on plantations and more raw material exported"],
          ["That transoceanic voyaging transformed trade",
           "Records of goods arriving by sea that had previously come overland"],
          ["That an empire was shaped by a population it incorporated",
           "Records of a court adopting practices of a newly incorporated group"],
          ["That the climate of the Atlantic changed",
           "Records of more laborers on plantations"]])

QUESTIONS = [
 dict(
  q=("The CED describes what the final topic of this unit is for. According to that description, "
     "what should students be doing here?"),
  choices=[
   "Practising the skill of argumentation using evidence relevant to the unit's key concepts",
   "Memorising a list of dates for the unit's events",
   "Learning a new set of key concepts not studied earlier in the unit",
   "Comparing this unit with a unit they have not yet studied",
   "Reading a set of sources without drawing any conclusion from them"],
  ans=0,
  why=("The CED's page for this topic says the final topic in this unit focuses on the skill of "
       "argumentation and provides an opportunity for students to draw upon the key concepts and "
       "historical developments they have studied in this unit, using evidence relevant to those "
       "key concepts. It introduces no new key concept of its own and prints a review list of "
       "KC-4.1, KC-4.2 and KC-4.3 instead.")),
 dict(
  q=("Suggested skill 6.C names what a student is to do with historical evidence in this topic. "
     "What is it?"),
  choices=[
   "Use historical reasoning to explain relationships among pieces of historical evidence",
   "Identify the author of each piece of evidence",
   "Arrange the pieces of evidence by the date each was written",
   "Count how many pieces of evidence a source contains",
   "Decide which piece of evidence is the longest"],
  ans=0,
  why=("Suggested skill 6.C for this topic is to use historical reasoning to explain "
       "relationships among pieces of historical evidence, and the reasoning process printed with "
       "the topic is continuity and change; the evidence to be reasoned about is the review list, "
       "KC-4.1, KC-4.2 and KC-4.3. Authorship belongs to suggested skill 2.A, and the remaining "
       "options describe handling evidence without reasoning about it.")),
 dict(
  q=("Unit 4: Learning Objective N sets the argument students are to make in this topic. What is "
     "it about?"),
  choices=[
   "How economic developments from 1450 to 1750 affected social structures over time",
   "How social structures determined the geography of the oceans",
   "How religious belief determined the design of ships",
   "How the weather of one year affected a single harvest",
   "How one ruler's household was organised"],
  ans=0,
  why=("Unit 4: Learning Objective N asks students to explain how economic developments from 1450 "
       "to 1750 affected social structures over time, which is why the review list beside it "
       "carries KC-4.1, KC-4.2 and KC-4.3. The rejected options reverse the direction of the "
       "explanation or shrink it to a single household or harvest.")),
 dict(
  q=("The review list opens with a sentence that names both a continuity and a set of changes in "
     "the world's productive systems. Which reading of it is correct?"),
  choices=[
   "Productive systems went on being heavily centered on agriculture, although major changes occurred in agricultural labor, manufacturing, gender and social structures, and environmental processes",
   "Productive systems ceased to be centered on agriculture, and manufacturing took its place",
   "Productive systems went on being centered on agriculture, and nothing about them changed",
   "Productive systems changed in every respect, with no continuity of any kind",
   "The framework describes neither a continuity nor a change in productive systems"],
  ans=0,
  why=("KC-4.2 says that although the world's productive systems continued to be heavily centered "
       "on agriculture, major changes occurred in agricultural labor, the systems and locations of "
       "manufacturing, gender and social structures, and environmental processes. The continuity "
       "and the changes are asserted in the same sentence, so a reading that keeps one and drops "
       "the other misreports it.")),
 dict(
  q=("The review list gives a reason why the demand for labor intensified in this period. What "
     "reason does it give?"),
  choices=[
   "The growing global demand for raw materials and finished products",
   "A fall in the world's population",
   "The abandonment of agriculture as a productive system",
   "A decision by rulers to require labor of every subject",
   "The exhaustion of the world's silver supply"],
  ans=0,
  why=("KC-4.2.II says the demand for labor intensified as a result of the growing global demand "
       "for raw materials and finished products. The framework offers none of the other causes, "
       "and KC-4.2 says productive systems continued to be heavily centered on agriculture rather "
       "than abandoning it.")),
 dict(
  q=("Which three developments does the review list name as accompanying the intensified demand "
     "for labor?"),
  choices=[
   "Traditional peasant agriculture increased and changed in nature, plantations expanded, and the Atlantic slave trade developed and intensified",
   "Peasant agriculture disappeared, plantations contracted, and the Atlantic slave trade ended",
   "New tools appeared, ship designs improved, and knowledge of winds and currents grew",
   "Mercantilist policies were adopted, monopoly companies were chartered, and silver circulated",
   "Empires expanded, disputes multiplied, and rivalries hardened"],
  ans=0,
  why=("KC-4.2.II names exactly these three: traditional peasant agriculture increased and changed "
       "in nature, plantations expanded, and the Atlantic slave trade developed and intensified. "
       "The rejected lists reverse all three, or belong to KC-4.1.II.A, KC-4.1.IV.C and KC-4.3.")),
 dict(
  q=("The review list summarises what the interconnection of the hemispheres did. Which summary "
     "is the framework's?"),
  choices=[
   "It transformed trade and had a significant social impact on the world",
   "It transformed trade but left societies unaffected",
   "It changed societies but left patterns of trade as they were",
   "It affected neither trade nor society",
   "It affected only the societies of the Western Hemisphere"],
  ans=0,
  why=("KC-4.1 says the interconnection of the Eastern and Western Hemispheres, made possible by "
       "transoceanic voyaging, transformed trade and had a significant social impact on the world. "
       "Both consequences are in the one sentence, and each rejected option drops or narrows one "
       "of them.")),
 dict(
  q=("The review list describes the relationship between empires and the populations they took "
     "in. Which description follows it?"),
  choices=[
   "Empires shaped the diverse populations they incorporated and were shaped by them in turn",
   "Empires shaped the populations they incorporated and were not affected by them",
   "Empires were shaped by the populations they incorporated and did not affect them",
   "Empires and the populations they incorporated had no effect on one another",
   "Empires incorporated no diverse populations in this period"],
  ans=0,
  why=("KC-4.3 says empires achieved increased scope and influence around the world, shaping and "
       "being shaped by the diverse populations they incorporated. The two directions are given "
       "together, so keeping one and dropping the other is the error the distractors are built "
       "from.")),
 dict(
  q=("A student has two pieces of evidence: rising exports of a raw material from a region, and a "
     "rising number of laborers recorded working in that region. Using suggested skill 6.C, what "
     "relationship between them does the framework's account make available?"),
  choices=[
   "That growing demand for raw materials intensified the demand for labor",
   "That the rising number of laborers caused the demand for the raw material",
   "That the two are unrelated, since the framework connects trade to no labor system",
   "That both were caused by an improvement in ship design",
   "That both were caused by a change in the climate of the region"],
  ans=0,
  why=("KC-4.2.II states the relationship in that direction: the demand for labor intensified as a "
       "result of the growing global demand for raw materials and finished products. The reversed "
       "reading is not what the sentence says, and the framework connects neither ship design nor "
       "climate to a rising workforce.")),
 dict(
  q=("An essay argues that transoceanic voyaging transformed patterns of trade. Which piece of "
     "evidence would most strengthen that argument?"),
  choices=[
   "A record showing goods that once came overland arriving by sea instead",
   "A record of the number of masons employed on an inland cathedral",
   "A record of the age of a ruler at accession",
   "A record of the rainfall in one province over one summer",
   "A record of the number of books held in a single library"],
  ans=0,
  why=("KC-4.1 says the interconnection of the hemispheres, made possible by transoceanic "
       "voyaging, transformed trade, so evidence for it must show a route or a pattern of trade "
       "changing. Masons, an accession, rainfall and a library bear on none of that and leave the "
       "argument where it stood.")),
 dict(
  q=("An essay argues that the world's productive systems stopped being centered on agriculture in "
     "this period. Which evidence would most directly weaken that argument?"),
  choices=[
   "A survey showing most of the recorded workforce still in agriculture at the end of the period",
   "A survey showing the number of ships entering one port",
   "A survey showing the titles held by a colonial governor",
   "A survey showing the price of one commodity in one market",
   "A survey showing the number of letters sent between two cities"],
  ans=0,
  why=("KC-4.2 says the world's productive systems continued to be heavily centered on agriculture "
       "even as major changes occurred elsewhere in them, so a workforce still concentrated in "
       "agriculture is the direct counter-evidence. Ship counts, titles, one price and a "
       "correspondence bear on the claim not at all.")),
 dict(
  q=("A student is shown a body of evidence about one region across the period and asked to "
     "separate a continuity from a change. Which pairing follows the framework?"),
  choices=[
   "Agriculture remaining the base of production is the continuity, and the expansion of plantations is the change",
   "The expansion of plantations is the continuity, and agriculture remaining the base of production is the change",
   "Both the base of production and the expansion of plantations are continuities",
   "Both are changes, since the framework records no continuity in this period",
   "Neither is described by the framework"],
  ans=0,
  why=("KC-4.2 gives the continuity, productive systems continuing to be heavily centered on "
       "agriculture, and KC-4.2.II gives the change, plantations expanding as the demand for labor "
       "intensified. Exchanging them inverts the sentence, and denying either denies half of it.")),
 dict(
  q=("A student finds that a region's exports and its recorded workforce both rose in the same "
     "years, and concludes that the rise in the workforce caused the rise in exports. What is the "
     "best assessment of that reasoning?"),
  choices=[
   "The evidence shows the two rose together, and the framework puts the causation the other way, from demand for products to demand for labor",
   "The evidence establishes the student's causal direction beyond doubt",
   "The evidence shows the two are unconnected",
   "The evidence shows the exports fell while the workforce rose",
   "The evidence cannot be used in a historical argument at all"],
  ans=0,
  why=("Two series rising together establish that they moved together and not which moved the "
       "other, and KC-4.2.II states the direction the framework gives: the demand for labor "
       "intensified as a result of the growing global demand for raw materials and finished "
       "products. The student has reversed it.")),
 dict(
  q=("A single hypothetical record shows that one port handled more goods at the end of the "
     "period than at the start. Which conclusion does that record alone support?"),
  choices=[
   "That the volume of trade through that port grew",
   "That the whole world's trade grew by the same proportion",
   "That the port's growth was caused by improvements in ship design",
   "That the goods came from the Western Hemisphere",
   "That the port's laborers were enslaved"],
  ans=0,
  why=("One port's totals support a claim about that port and no more; KC-4.1 makes the wider "
       "claim about world trade, and KC-4.1.II.A the claim about ship design, but neither can be "
       "read off a single port's book. Scale is what suggested skill 6.C asks a student to keep "
       "track of when relating pieces of evidence.")),
 dict(
  q=("An essay claims that the Atlantic slave trade began in this period. How does that claim "
     "stand against the framework's own wording?"),
  choices=[
   "It overstates it, since the framework says the Atlantic slave trade developed and intensified",
   "It matches it exactly, since the framework says the trade began in this period",
   "It understates it, since the framework says the trade ended in this period",
   "It is irrelevant, since the framework does not mention the Atlantic slave trade",
   "It is correct, since the framework dates the trade precisely"],
  ans=0,
  why=("KC-4.2.II says the Atlantic slave trade developed and intensified, which describes growth "
       "rather than a beginning, and the CED's own note says events and processes are not "
       "constrained by the given dates and may begin before or continue after the period. A claim "
       "about a beginning goes past the sentence.")),
 dict(
  q=("A hypothetical file of four pieces of evidence about one region appears in the table "
     "below.\n\n"
     "How many of them bear on the framework's claim that the demand for labor intensified as "
     "global demand for raw materials and finished products grew?"),
  table=_T_EVIDENCE,
  choices=[
   "Three of the four, since one records something unconnected to that demand",
   "One of the four, since only a count of laborers can bear on a claim about labor",
   "Two of the four, since exports cannot bear on a claim about labor",
   "All four, since every record from the period bears on every claim about it",
   "None of the four, since a claim about demand cannot be evidenced at all"],
  ans=0,
  why=("KC-4.2.II ties the intensified demand for labor to the growing global demand for raw "
       "materials and finished products, and names the expansion of plantations and the "
       "intensification of the Atlantic slave trade alongside it, so exports, plantation laborers "
       "and arrivals at the ports all bear on the claim while a cathedral tower does not. The "
       "verifier recomputes which rows qualify.")),
 dict(
  q=("A hypothetical survey of one region's recorded workforce across four periods appears in the "
     "table below.\n\n"
     "Which conclusion is best supported by the table alone?"),
  table=_T_WORKFORCE,
  choices=[
   "Agriculture holds the larger share in every period while the manufacturing share rises throughout",
   "Manufacturing overtakes agriculture before the end of the survey",
   "The agricultural share rises while the manufacturing share falls",
   "Neither share changes across the four periods",
   "The two shares are equal in the final period"],
  ans=0,
  why=("KC-4.2 says the world's productive systems continued to be heavily centered on agriculture "
       "although major changes occurred in the systems and locations of manufacturing, and a "
       "survey of this shape is what that combination looks like in one region's figures. The "
       "verifier recomputes both columns in every period.")),
 dict(
  q=("A hypothetical essay's four claims and the evidence offered for each appear in the table "
     "below.\n\n"
     "Which conclusion about the essay's use of evidence is best supported?"),
  table=_T_CLAIMS,
  choices=[
   "Three of the claims are supported by evidence that bears on them, and one is supported by evidence that bears on a different claim",
   "All four claims are supported by evidence that bears on them",
   "None of the claims is supported by evidence that bears on it",
   "Two of the claims are supported by the same piece of evidence, and both correctly",
   "The essay offers no evidence for any of its claims"],
  ans=0,
  why=("Suggested skill 6.C asks a student to explain relationships among pieces of evidence, and "
       "the relationship at issue is whether a piece of evidence bears on the claim it is offered "
       "for. Plantation laborers bear on KC-4.2.II's intensified demand for labor and not on a "
       "claim about the climate. The verifier recomputes which pairings hold.")),
 dict(
  q=("A hypothetical account by a merchant of the period reports that goods once bought through "
     "several intermediaries overland now arrive at the same port directly by sea, and that the "
     "trades of the town have changed accordingly.\n\n"
     "Which relationship among the framework's claims does the account most directly "
     "illustrate?"),
  choices=[
   "That transoceanic voyaging transformed trade and had a social impact",
   "That empires were shaped by the populations they incorporated",
   "That economic disputes led to rivalries and conflict between states",
   "That productive systems continued to be centered on agriculture",
   "That knowledge and technology spread from the Classical, Islamic, and Asian worlds"],
  ans=0,
  why=("KC-4.1 says the interconnection of the Eastern and Western Hemispheres, made possible by "
       "transoceanic voyaging, transformed trade and had a significant social impact on the world, "
       "and an account joining a changed route to changed trades in the town shows both halves at "
       "once. The rejected options are KC-4.3, KC-4.3.III.ii, KC-4.2 and KC-4.1.II.")),
 dict(
  q=("A hypothetical estate survey from the period records that the same fields are still worked, "
     "that more hands work them than before, and that the terms on which those hands work have "
     "changed.\n\n"
     "Which combination does the survey illustrate?"),
  choices=[
   "A continuity in what was produced together with a change in how labor was organised",
   "A change in what was produced together with a continuity in how labor was organised",
   "A continuity in both what was produced and how labor was organised",
   "A change in both what was produced and how labor was organised",
   "Neither a continuity nor a change of any kind"],
  ans=0,
  why=("KC-4.2 says productive systems continued to be heavily centered on agriculture although "
       "major changes occurred in agricultural labor, and KC-4.2.II adds that traditional peasant "
       "agriculture increased and changed in nature. Same fields with more hands on different "
       "terms is exactly that pairing.")),
 dict(
  q=("A hypothetical chronicle records that after a province was taken into an empire, the "
     "empire's court began to keep some of the province's customs, while the province's officials "
     "began to keep the empire's accounts.\n\n"
     "Which statement of the review list does the chronicle illustrate?"),
  choices=[
   "That empires shaped and were shaped by the diverse populations they incorporated",
   "That the demand for labor intensified as global demand grew",
   "That transoceanic voyaging made travel and trade possible",
   "That economic disputes led to conflict between states",
   "That productive systems remained centered on agriculture"],
  ans=0,
  why=("KC-4.3 says empires achieved increased scope and influence around the world, shaping and "
       "being shaped by the diverse populations they incorporated, and a court taking up provincial "
       "customs while the province takes up imperial administration is influence running both ways. "
       "The rejected options are KC-4.2.II, KC-4.1.II.A, KC-4.3.III.ii and KC-4.2.")),
 dict(
  q=("A hypothetical petition from one state's merchants to their ruler complains that another "
     "state's ships are taking the trade of a route their own ships once carried, and asks the "
     "ruler to act.\n\n"
     "Which statement of the review list does the petition illustrate?"),
  choices=[
   "That economic disputes led to rivalries and conflict between states",
   "That political and religious disputes led to rivalries between states",
   "That empires were shaped by the populations they incorporated",
   "That the demand for labor intensified across the period",
   "That productive systems remained heavily centered on agriculture"],
  ans=0,
  why=("KC-4.3.III.ii, printed in this topic's review list, says economic disputes led to "
       "rivalries and conflict between states, and a quarrel over who carries a route's trade is "
       "an economic dispute. Political and religious disputes are KC-4.3.III.i, which belongs to "
       "unit 3 and is not in this review list.")),
 dict(
  q=("Unit 4: Learning Objective N asks how economic developments affected social structures. "
     "Which chain of reasoning follows the framework's own statements?"),
  choices=[
   "Growing global demand for goods intensified the demand for labor, plantations expanded and the Atlantic slave trade intensified, and social structures changed accordingly",
   "Social structures changed first, which then produced a global demand for goods",
   "Growing demand for goods left labor and social structures untouched",
   "Plantations contracted as demand for goods grew, and social structures were unaffected",
   "The framework connects economic developments to no social change at all"],
  ans=0,
  why=("KC-4.2.II runs from the growing global demand for raw materials and finished products to "
       "the intensified demand for labor, the expansion of plantations and the development and "
       "intensification of the Atlantic slave trade, while KC-4.2 names gender and social "
       "structures among the things that changed and KC-4.1 records a significant social impact. "
       "The rejected chains reverse or break that order.")),
 dict(
  q=("A hypothetical file of evidence records rising plantation acreage, a rising number of "
     "enslaved laborers, "
     "and a rising volume of exported cash crops in one colony. Which claim does the file NOT "
     "support on its own?"),
  choices=[
   "That the colony's social structure was unchanged across the period",
   "That the colony's plantations expanded",
   "That the colony's demand for labor intensified",
   "That the colony exported more than before",
   "That the three developments occurred together"],
  ans=0,
  why=("KC-4.2.II ties expanding plantations and an intensifying Atlantic slave trade to the "
       "intensified demand for labor, and KC-4.2 names gender and social structures among the "
       "things that changed in the period, so a claim of an unchanged social structure runs "
       "against the framework rather than following from the file. The other four claims are read "
       "directly off the three series.")),
 dict(
  q=("An argument holds that the interconnection of the hemispheres had social consequences and "
     "not merely commercial ones. Which further evidence would complete it?"),
  choices=[
   "Evidence that the arrangements of work and family in a region changed as its trade changed",
   "Evidence that a ship completed a voyage in fewer days than before",
   "Evidence that a port levied a new duty on one commodity",
   "Evidence that a chart of one coast was redrawn",
   "Evidence that a company issued more shares than the previous year"],
  ans=0,
  why=("KC-4.1 says the interconnection of the hemispheres transformed trade AND had a significant "
       "social impact on the world, and KC-4.2 names gender and social structures among what "
       "changed, so the missing half of the argument is evidence about how people lived and "
       "worked. Faster voyages, a new duty, a redrawn chart and a share issue are all commercial "
       "or technical.")),
 dict(
  q=("Two students each argue that the period changed the world's productive systems. One cites "
     "the expansion of plantations; the other cites a single year's harvest in one village. Whose "
     "evidence better fits the claim, and why?"),
  choices=[
   "The first, because a change in how and where production was organised bears on productive systems, while one harvest does not",
   "The second, because a village harvest is closer to ordinary life",
   "Neither, because the framework records no change in productive systems",
   "Both equally, because any evidence from the period supports any claim about it",
   "The second, because a single year is easier to verify"],
  ans=0,
  why=("KC-4.2 describes major changes in agricultural labor and in the systems and locations of "
       "manufacturing, and KC-4.2.II names the expansion of plantations, so evidence at the level "
       "of how production was organised is what the claim needs. One village's harvest in one year "
       "speaks to weather rather than to a productive system, which is the kind of mismatch "
       "suggested skill 6.C asks students to notice.")),
 dict(
  q=("In a set of evidence showing new crops, new labor systems and new trade routes in one "
     "region, which finding would count as the CONTINUITY the framework leads a student to look "
     "for?"),
  choices=[
   "That production in the region remained centered on agriculture throughout",
   "That the region's trade routes were all new",
   "That the region's labor systems were all new",
   "That the region's crops were all new",
   "That nothing in the region can be described as continuous"],
  ans=0,
  why=("KC-4.2 says the world's productive systems continued to be heavily centered on agriculture "
       "although major changes occurred around them, so in a set of changes the agricultural base "
       "is the continuity the framework points to. Every rejected option names one of the changes "
       "instead.")),
 dict(
  q=("Which of the following claims about this unit would require evidence from outside the "
     "framework's own statements?"),
  choices=[
   "That the changes of this period mattered more to the world than those of the previous period",
   "That the interconnection of the hemispheres transformed trade and had a significant social impact",
   "That the demand for labor intensified as global demand for goods grew",
   "That productive systems continued to be heavily centered on agriculture",
   "That empires shaped and were shaped by the populations they incorporated"],
  ans=0,
  why=("The four rejected statements are KC-4.1, KC-4.2.II, KC-4.2 and KC-4.3 almost verbatim. The "
       "framework weighs no period against another for importance, so a comparison of that kind "
       "would have to be defended from another source.")),
 dict(
  q=("Why does the framework place this topic's reasoning process as continuity and change rather "
     "than as causation alone?"),
  choices=[
   "Because its review list pairs things that continued with things that changed in the same sentences",
   "Because it denies that anything caused anything else in the period",
   "Because it records no change of any kind in the period",
   "Because it records no continuity of any kind in the period",
   "Because it treats the period as too short for either"],
  ans=0,
  why=("KC-4.2 pairs productive systems continuing to be heavily centered on agriculture with "
       "major changes in labor, manufacturing, social structures and environmental processes, and "
       "KC-4.2.II pairs traditional peasant agriculture increasing with its changing in nature. "
       "Causation is the reasoning process of other topics in this unit, including 4.1 and 4.6.")),
 dict(
  q=("A summary argument for this unit is being drafted for students. Which version stays within "
     "what the framework asserts about the period 1450 to 1750?"),
  choices=[
   "Transoceanic voyaging linked the hemispheres and transformed trade with a significant social impact, production stayed centered on agriculture even as labor, manufacturing and social structures changed, demand for labor intensified with global demand for goods, and empires grew while being shaped by the populations they took in",
   "Transoceanic voyaging left trade as it was, and no social impact followed from it",
   "Production ceased to be centered on agriculture, and the demand for labor fell as global demand grew",
   "Empires shaped the populations they incorporated and were entirely unchanged by them",
   "The period saw changes but no continuities of any kind"],
  ans=0,
  why=("The keyed sentence joins KC-4.1, KC-4.2, KC-4.2.II and KC-4.3, which are the review list "
       "printed beside this topic. Each rejected version denies the transformation of trade, "
       "reverses the continuity in productive systems, drops one direction of KC-4.3's two-way "
       "relationship, or denies the continuities that make this a continuity and change topic.")),
]
