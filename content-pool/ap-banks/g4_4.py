# AP HUMAN GEOGRAPHY 4.4 Defining Political Boundaries -- 30 questions
# CED (2020 framework), Unit 4, enduring understanding IMP-4: political
# boundaries and divisions of governance reflect balances of power that have
# been negotiated or imposed.
#
# Learning objective IMP-4.A: define types of political boundaries used by
# geographers.
# Essential knowledge:
#   IMP-4.A.1  Types of political boundaries include relict, superimposed,
#              subsequent, antecedent, geometric, and consequent boundaries.
#
# The list is closed and it is the whole content of the topic, so the module is
# built on the one distinction that actually decides every case: WHEN the line
# was drawn relative to the settlement of the area, and WHO drew it. Antecedent
# precedes settlement; subsequent follows and adjusts to it; consequent is the
# subsequent case where the line was drawn TO match a cultural division;
# superimposed is drawn by an outside power in disregard of that division; relict
# no longer functions but is still legible on the landscape; geometric describes
# the SHAPE of a line rather than its history, which is why a boundary can be
# geometric and superimposed at once (items 9, 18, 26).
#
# The CED's own sample question 2 keys the Berlin Conference and the 1947
# partition of India to SUPERIMPOSED boundaries, and item 12 below follows that
# key rather than a different reading.
#
# Suggested skill 1.D, describe a relevant concept in a specified context:
# items 15, 24 and 29 carry real data tables.
#
# FIVE choices (A-E), matching the real AP Human Geography exam.
TOPIC = ("4.4", "Defining Political Boundaries", 4)
QUESTIONS = [
 dict(q="A boundary was surveyed across a forested interior before farmers or towns arrived, and settlement later filled in on both sides. This boundary is", choices=[
   "antecedent",
   "subsequent",
   "consequent",
   "relict",
   "superimposed"], ans=0,
   why="An antecedent boundary is one drawn before the cultural landscape developed around it, which is exactly the sequence described: line first, settlement afterward. Every other type on the list requires an existing settled landscape for the line to respond to, ignore, or outlive."),
 dict(q="A boundary between two provinces was adjusted over several centuries as villages grew, farmland spread, and communities negotiated where one jurisdiction ended. The boundary is", choices=[
   "subsequent",
   "antecedent",
   "geometric",
   "relict",
   "superimposed"], ans=0,
   why="A subsequent boundary develops after settlement and shifts as the cultural landscape changes, which is what centuries of negotiated adjustment describe. An antecedent line would have been fixed before the villages existed, and would not have moved with them."),
 dict(q="After a war, an outside coalition drew a boundary across a region without consulting the peoples living there, splitting several of them between two new states. The boundary is best classified as", choices=[
   "superimposed",
   "consequent",
   "subsequent",
   "antecedent",
   "relict"], ans=0,
   why="A superimposed boundary is imposed by an external power over an existing cultural landscape it disregards, and splitting resident peoples is the diagnostic consequence. A consequent line would have been placed to follow those same cultural divisions rather than to cut across them."),
 dict(q="A boundary was drawn along the line separating two language communities so that each new administrative unit would contain one of them. This is a", choices=[
   "consequent boundary",
   "superimposed boundary",
   "antecedent boundary",
   "relict boundary",
   "geometric boundary"], ans=0,
   why="A consequent boundary is drawn to accommodate an existing cultural division rather than in spite of one, so a line placed along a language divide is the standard case. It is a kind of subsequent boundary, since the culture had to exist first, distinguished by the intent to match it."),
 dict(q="A line of ruined watchtowers and a disused customs house mark where an old frontier ran, although the states on either side merged decades ago. Geographers call this a", choices=[
   "relict boundary",
   "consequent boundary",
   "geometric boundary",
   "antecedent boundary",
   "subsequent boundary"], ans=0,
   why="A relict boundary no longer functions politically but remains visible in the landscape, which is what abandoned towers and a disused customs post are. The visibility is the point: it is the traces, not the legal line, that make the category."),
 dict(q="A boundary runs due north along a line of longitude for 1,600 kilometers, ignoring rivers, ridges, and settlement. On the criterion of SHAPE alone this boundary is", choices=[
   "geometric",
   "antecedent",
   "consequent",
   "relict",
   "subsequent"], ans=0,
   why="Geometric describes the form of the line -- a straight segment following a meridian, parallel, or arc -- and says nothing about when or by whom it was drawn. That is why the question restricts itself to shape: the same line will also belong to one of the history-based categories."),
 dict(q="Which pair of boundary types is distinguished by WHEN the line was drawn relative to settlement, rather than by who drew it or what shape it takes?", choices=[
   "Antecedent and subsequent",
   "Geometric and relict",
   "Superimposed and geometric",
   "Consequent and geometric",
   "Relict and superimposed"], ans=0,
   why="Antecedent means before the cultural landscape formed and subsequent means after it, so the two differ purely in timing. Geometric is a statement about shape, relict about whether the line still functions, and superimposed about who imposed it over whom."),
 dict(q="The border between two states follows the crest of a mountain range that was uninhabited when the line was agreed, and villages later grew on both slopes. Two labels fit this boundary at once:", choices=[
   "antecedent, because it preceded settlement, and physical, because it follows a landform",
   "subsequent, because settlement came later, and geometric, because ridges are straight",
   "superimposed, because mountains impose themselves, and relict, because ranges are old",
   "consequent, because it separates two slopes, and antecedent, because mountains are ancient",
   "relict, because the range is eroding, and subsequent, because villages arrived"], ans=0,
   why="The classification tracks the human sequence, not the age of the landform: settlement arrived after the line, which makes it antecedent, and the line's course follows a physical feature. Calling a mountain range 'ancient' confuses the geology with the boundary's political history."),
 dict(q="A boundary in a desert region is a perfectly straight line drawn by a colonial administration that never surveyed the peoples living there. The most complete classification is", choices=[
   "geometric in shape and superimposed in origin",
   "geometric in shape and antecedent in origin",
   "consequent in shape and relict in origin",
   "subsequent in shape and consequent in origin",
   "relict in shape and geometric in origin"], ans=0,
   why="Shape and history are independent axes: the straightness makes it geometric, and an outside administration drawing it over an inhabited landscape it disregarded makes it superimposed. Requiring one label per boundary is the mistake this item is built to expose."),
 dict(q="Which observation would be the strongest evidence that a boundary is relict rather than merely quiet?", choices=[
   "Fortifications, border markers, or a cleared strip survive on the ground although no jurisdiction changes there",
   "Few people cross it because the terrain is difficult",
   "It is not shown on recent road maps",
   "It separates two provinces of the same country",
   "It was drawn as a straight line"], ans=0,
   why="A relict boundary must be both defunct and legible -- traces on the landscape are what distinguish it from a line that has simply been forgotten. Low traffic, cartographic omission, an internal position, and straightness say nothing about whether physical evidence remains."),
 dict(q="A newly independent state keeps the exact borders it had as a colony, including segments that divide a single ethnic group between it and its neighbor. Those segments remain", choices=[
   "superimposed, because their origin lies in an outside power's disregard for the cultural landscape",
   "consequent, because they now separate two independent states",
   "antecedent, because independence came after them",
   "relict, because the colonial administration no longer exists",
   "geometric, because independence made them straight"], ans=0,
   why="Classification follows a boundary's origin, and independence changes who administers the line, not who drew it or why. The relict reading fails because the line is still a functioning international border, which is precisely what a relict boundary is not."),
 dict(q="The boundaries produced by the Berlin Conference of 1884-1885 and by the 1947 partition of India are grouped together in this course as examples of", choices=[
   "superimposed boundaries",
   "relict boundaries",
   "antecedent boundaries",
   "consequent boundaries",
   "subsequent boundaries"], ans=0,
   why="In both cases an outside authority drew lines across long-settled regions without regard for the peoples they divided, which is the definition of a superimposed boundary. The lasting difficulties both created -- divided nations on either side -- follow directly from that disregard."),
 dict(q="Which of these would most likely become a consequent boundary?", choices=[
   "A line negotiated between two communities so that each governs the area where its own religion predominates",
   "A line drawn along a parallel of latitude by a distant treaty",
   "A line surveyed across empty grassland before anyone settled it",
   "A line marked only by ruined fortifications",
   "A line imposed by a victorious army across an inhabited valley"], ans=0,
   why="Consequent means the line was placed to correspond with an existing cultural division, so a negotiated religious boundary is the case. A parallel of latitude, an unsettled survey, ruins, and an imposed military line each match a different category on the list."),
 dict(q="A geographer says that a boundary type describes a PROCESS while another describes a FORM. The pairing that best illustrates this contrast is", choices=[
   "antecedent, which records when the line appeared, and geometric, which records what the line looks like",
   "relict, which records what the line looks like, and geometric, which records when it appeared",
   "consequent and subsequent, both of which record only shape",
   "superimposed and antecedent, both of which record only shape",
   "geometric and consequent, both of which record only timing"], ans=0,
   why="Antecedent, subsequent, consequent, superimposed, and relict all say something about a boundary's history; geometric alone describes its geometry. Keeping the two axes apart is what allows a line to be both geometric and superimposed."),
 dict(table=dict(headers=["Boundary", "Drawn before local settlement", "Drawn by an outside power", "Still administered today"],
   rows=[["Boundary 1", "Yes", "No", "Yes"], ["Boundary 2", "No", "Yes", "Yes"],
         ["Boundary 3", "No", "No", "No"], ["Boundary 4", "No", "No", "Yes"]]),
   q="Using the accompanying record of four boundaries, which is best classified as relict?", choices=[
   "Boundary 3, because it is no longer administered",
   "Boundary 1, because it preceded settlement",
   "Boundary 2, because an outside power drew it",
   "Boundary 4, because it is still administered",
   "None of them, because the record does not report boundary shape"], ans=0,
   why="A relict boundary is one that has ceased to function, and only one row records that the line is no longer administered. Preceding settlement makes a boundary antecedent and an outside origin makes it superimposed, so those rows answer different questions."),
 dict(q="Two states agree that their common boundary shall run down the deepest channel of a river. Some years later the river shifts its course. The classification problem this creates is that", choices=[
   "the boundary's position may now differ from the physical feature it was defined by",
   "the boundary automatically becomes relict",
   "the boundary automatically becomes geometric",
   "the boundary becomes antecedent to the river",
   "the boundary ceases to be a political boundary"], ans=0,
   why="A boundary defined by a moving feature raises the question of whether the line follows the feature or stays where the feature used to be, which is why such treaties specify one or the other. Nothing about a channel shift ends the boundary's function or changes its shape to a straight line."),
 dict(q="A state's internal provincial boundaries were drawn after settlement and adjusted as populations grew, while its international boundary was drawn by a treaty before any of that settlement occurred. The correct pair of labels is", choices=[
   "subsequent for the provincial lines and antecedent for the international line",
   "antecedent for the provincial lines and subsequent for the international line",
   "relict for the provincial lines and consequent for the international line",
   "geometric for both, since all boundaries have a shape",
   "superimposed for both, since a government drew them"], ans=0,
   why="The provincial lines followed and responded to settlement, which is subsequent, while the treaty line preceded it, which is antecedent. A government drawing its own internal lines is not an outside power, so superimposed does not apply."),
 dict(q="Why can a boundary be described as geometric and superimposed simultaneously without contradiction?", choices=[
   "Geometric describes the line's shape and superimposed describes who drew it and over what",
   "Both terms describe the same property using different words",
   "Geometric boundaries are always drawn before settlement",
   "Superimposed boundaries are always curved",
   "The two terms apply at different scales of analysis"], ans=0,
   why="The categories answer different questions, so a single line can have an answer to each: a straight segment drawn by a colonial power across an inhabited region is geometric in form and superimposed in origin. They are not synonyms and neither implies a particular timing."),
 dict(q="An old defensive wall now runs through the middle of a single country's territory and is preserved as a monument. In boundary terms the wall is", choices=[
   "the trace of a relict boundary",
   "an active superimposed boundary",
   "a consequent boundary between two cultures",
   "an antecedent boundary awaiting settlement",
   "a geometric boundary because it is straight"], ans=0,
   why="The wall no longer divides jurisdictions but remains legible on the landscape, which is exactly what makes a boundary relict. Preservation as a monument is evidence of the visibility the category requires, not evidence that the line still functions."),
 dict(q="Which classification error does a student make by calling every straight-line boundary in Africa 'geometric' and stopping there?", choices=[
   "The label describes only shape and omits that most were imposed from outside on settled regions",
   "The label describes only origin and omits the shape",
   "The label wrongly implies the lines were drawn after settlement",
   "The label wrongly implies the lines no longer function",
   "The label applies only to internal boundaries"], ans=0,
   why="Geometric is accurate but incomplete: it captures the form while leaving out the history that explains why so many African boundaries divide peoples. The omission is what makes the description uninformative about the consequences."),
 dict(q="A boundary between two countries follows a line agreed in a treaty that was never surveyed or marked on the ground. Using the standard sequence for establishing a boundary, this line has been", choices=[
   "defined and delimited but not demarcated",
   "demarcated but not defined",
   "administered but not defined",
   "demarcated and administered but not delimited",
   "neither defined nor delimited"], ans=0,
   why="Defining sets the boundary in a legal document, delimiting draws it on a map, and demarcating marks it on the ground; a treaty line never physically marked has completed the first two steps only. The sequence matters because unmarked boundaries are the ones most often disputed on the ground."),
 dict(q="Two neighboring states have a boundary that was drawn to place each of two nations wholly within one state. Fifty years of migration has left large minorities on both sides. The boundary", choices=[
   "was consequent when drawn, even though the population no longer matches it",
   "has become antecedent because the migration came later",
   "has become geometric because it has not moved",
   "has become superimposed because it now divides peoples",
   "has become relict because it no longer matches the population"], ans=0,
   why="Classification records the circumstances at the time the line was drawn, and this one was drawn to match a cultural division. Superimposed would require an outside power to have imposed it against the cultural map, and relict would require the boundary to have stopped functioning, neither of which has happened."),
 dict(q="Which of the following best explains why antecedent boundaries tend to generate fewer disputes over divided communities than superimposed ones?", choices=[
   "An antecedent line existed before communities formed, so communities grew up on one side or the other rather than being cut apart",
   "Antecedent boundaries are always drawn along rivers",
   "Antecedent boundaries are never straight",
   "Superimposed boundaries are always internal to a state",
   "Superimposed boundaries are drawn before settlement"], ans=0,
   why="The timing does the work: a line that precedes settlement cannot split an existing community, whereas one imposed on an inhabited region routinely does. The final option restates the antecedent definition and misapplies it to the superimposed case."),
 dict(table=dict(headers=["Boundary segment", "Length (km)", "Follows a straight survey line"],
   rows=[["Segment 1", "420", "Yes"], ["Segment 2", "180", "No"],
         ["Segment 3", "300", "Yes"], ["Segment 4", "100", "No"]]),
   q="Using the accompanying segment data, what percentage of the total boundary length follows a straight survey line?", choices=[
   "72 percent",
   "50 percent",
   "28 percent",
   "62 percent",
   "84 percent"], ans=0,
   why="The straight segments total 720 km of a 1,000 km boundary, which is 72 percent. Counting segments instead of length would give 50 percent, and that mismatch is the reason the question specifies length."),
 dict(q="A boundary drawn by an outside power in 1900 is still the international border today, and it still divides an ethnic group. A student calls it relict. The correction is that", choices=[
   "it is superimposed and active, since a relict boundary must have stopped functioning",
   "it is antecedent, since it was drawn long ago",
   "it is consequent, since it separates two groups",
   "it is geometric, since colonial lines are straight",
   "the student is right, since the colonial power is gone"], ans=0,
   why="Relict is about whether the line still does political work, not about the age of the decision or the survival of the authority that made it. A border that governments still administer is active by definition, whatever its origin."),
 dict(q="Which of these is the best reason geographers keep 'geometric' as a category even though it says nothing about a boundary's history?", choices=[
   "Shape has its own consequences, since a line that ignores terrain and settlement is harder to police and more likely to cut across communities",
   "Shape determines which state is sovereign over the boundary",
   "Shape indicates when the boundary was drawn",
   "Shape determines whether the boundary is internal or international",
   "Shape indicates whether the boundary is still administered"], ans=0,
   why="A straight line laid across a landscape without reference to rivers, ridges, or settlement produces practical problems of its own, independent of who drew it, so the shape is worth recording separately. It carries no information about timing, sovereignty, status, or function."),
 dict(q="A treaty establishes a boundary along a line of latitude across territory that European surveyors had mapped but where indigenous nations had long lived. The most accurate description is", choices=[
   "geometric in shape and superimposed in origin, because the line disregards the peoples already there",
   "geometric in shape and antecedent in origin, because surveyors mapped it first",
   "consequent in origin, because the line follows a cultural division",
   "relict in origin, because the treaty is old",
   "subsequent in origin, because settlers arrived after the treaty"], ans=0,
   why="Prior mapping by outsiders is not prior settlement; the region was inhabited, so a line drawn across it by an outside treaty is superimposed. Treating a survey as evidence that the land was empty is the assumption the antecedent reading depends on, and it is false here."),
 dict(q="At the scale of a single village divided by a superimposed international boundary, the most likely everyday consequence is that", choices=[
   "residents on the two sides face different laws, currencies, and services despite belonging to one community",
   "the village becomes a relict boundary",
   "the boundary becomes consequent over time",
   "the two sides automatically merge into one state",
   "the boundary's shape changes from geometric to physical"], ans=0,
   why="A boundary is a difference in jurisdiction, so a line through a settled community delivers two sets of rules to one social unit. That mismatch is the local expression of the disregard that made the boundary superimposed in the first place."),
 dict(table=dict(headers=["Boundary", "Year line fixed", "Year first permanent settlement"],
   rows=[["Boundary V", "1846", "1871"], ["Boundary W", "1919", "1650"],
         ["Boundary X", "1885", "1400"], ["Boundary Y", "1902", "1930"]]),
   q="Using the accompanying dates, how many of the four boundaries are antecedent?", choices=[
   "Two, because in two cases the line was fixed before permanent settlement",
   "One, because only the earliest line qualifies",
   "Three, because most lines precede settlement",
   "Four, because all boundaries precede some settlement",
   "None, because settlement always precedes a boundary"], ans=0,
   why="An antecedent boundary is fixed before the area was settled, and comparing the two columns row by row shows the line preceding settlement in two of the four cases. The other two were fixed centuries after settlement, which makes them subsequent or superimposed rather than antecedent."),
 dict(q="Comparing two boundaries of identical length, one following a winding river and one running straight across a plateau, a geographer would expect the straight one to be", choices=[
   "cheaper to survey but more likely to divide settlements and land holdings",
   "cheaper to survey and less likely to divide settlements",
   "harder to survey and less likely to divide settlements",
   "identical in every practical respect, since length is the same",
   "automatically classified as antecedent"], ans=0,
   why="A straight line is trivial to define and mark, which is why administrations drawing lines from a distance favored them, but it takes no account of where fields, villages, and routes already are. Those two consequences -- ease of survey and disregard for the landscape -- are the same property seen from two sides."),
]
