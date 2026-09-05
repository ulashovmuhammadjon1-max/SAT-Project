# AP WORLD HISTORY: MODERN 3.4 Comparison in Land-Based Empires
# CED effective Fall 2024/2026, Unit 3 Land-Based Empires, c. 1450 to c. 1750.
# Unit 3: Learning Objective D -- compare the methods by which various empires
# increased their influence from 1450 to 1750. Suggested skill 6.B, support an
# argument using specific and relevant evidence: describe specific examples of
# historically relevant evidence, and explain how specific examples of
# historically relevant evidence support an argument. Reasoning process:
# comparison.
#
# This is the unit's REASONING topic. The CED says so in its own words: the
# final topic in this unit focuses on the skill of argumentation and so provides
# an opportunity for students to draw upon the key concepts and historical
# developments they have studied in this unit. So the items here are argument
# and comparison items, not fact recall, and the fact content they draw on is
# the unit's own review list and nothing beyond it.
#
# REVIEW: UNIT 3 KEY CONCEPTS, as the CED prints them beside this topic:
#   KC-4.1        The interconnection of the Eastern and Western Hemispheres,
#                 made possible by transoceanic voyaging, transformed trade and
#                 had a significant social impact on the world.
#   KC-4.1.VI     In some cases, the increase and intensification of interactions
#                 between newly connected hemispheres expanded the reach and
#                 furthered development of existing religions, and contributed to
#                 religious conflicts and the development of syncretic belief
#                 systems and practices.
#   KC-4.3        Empires achieved increased scope and influence around the
#                 world, shaping and being shaped by the diverse populations they
#                 incorporated.
#   KC-4.3.II     Imperial expansion relied on the increased use of gunpowder,
#                 cannons, and armed trade to establish large empires in both
#                 hemispheres.
#   KC-4.3.II.B   Land empires included the Manchu in Central and East Asia;
#                 Mughal in South and Central Asia; Ottoman in Southern Europe,
#                 the Middle East, and North Africa; and the Safavids in the
#                 Middle East.
#   KC-4.3.III.i  Political and religious disputes led to rivalries and conflict
#                 between states.
# Where an item reaches back to the unit's earlier topics it cites them:
# KC-4.3.I.A, KC-4.3.I.C and KC-4.3.I.D on administration, and KC-4.1.VI.i to
# KC-4.1.VI.iii on belief systems.
#
# Dates are written "1450 to 1750". Five choices A-E per HISTORY_BRIEF.md. Every
# stimulus is hypothetical or unattributed; no quotation is put in a real
# person's mouth.
TOPIC = ("3.4", "Comparison in Land-Based Empires Land-Based Empires", 3)

_T_EVIDENCE = dict(
    headers=["Piece of evidence a student has gathered", "What it records"],
    rows=[["Evidence 1", "The artillery train an empire assembled before annexing a province"],
          ["Evidence 2", "The number of pages in a chronicle describing that annexation"],
          ["Evidence 3", "The duties an empire levied on caravans at a garrisoned frontier post"],
          ["Evidence 4", "The rainfall recorded in the annexed province two centuries later"]])

_T_TWO_EMPIRES = dict(
    headers=["Method recorded", "Empire A", "Empire B"],
    rows=[["Provinces governed by salaried officials of the ruler", "18", "4"],
          ["Provinces whose taxes were farmed to contractors", "2", "16"],
          ["Major religious buildings raised by the ruler", "9", "8"]])

_T_CLAIMS = dict(
    headers=["Draft claim", "What the draft asserts"],
    rows=[["Claim 1", "Both empires expanded, and each used gunpowder weaponry in doing so"],
          ["Claim 2", "Both empires expanded, and neither ever used force of any kind"],
          ["Claim 3", "Both empires expanded, and both lay in the Western Hemisphere"]])

QUESTIONS = [
 dict(
  q=("A student is writing an argument comparing the methods by which two land empires "
     "increased their influence between 1450 and 1750. Which pair of claims sets up a genuine "
     "comparison rather than two unconnected descriptions?"),
  choices=[
   "Both empires expanded by armed force, but they differed in how they raised the revenue to pay for it",
   "One empire lay in Asia, and the other empire had a capital city",
   "One empire had rivers, and the other empire had mountains",
   "One empire existed in the period, and the other empire also existed in the period",
   "One empire produced chronicles, and the other empire produced chronicles as well"],
  ans=0,
  why=("Learning Objective D asks students to compare the methods by which various empires "
       "increased their influence, so a comparison must run along a stated axis of method. The "
       "keyed pair names a similarity from KC-4.3.II and a difference from KC-4.3.I.D; the "
       "rejected pairs place two facts side by side without any axis at all.")),
 dict(
  q=("Suggested skill 6.B asks a student to support an argument using specific and relevant "
     "evidence. What makes a piece of evidence relevant to an argument?"),
  choices=[
   "It bears on the claim the argument actually makes",
   "It is longer than any other piece of evidence available",
   "It comes from the most recently published book",
   "It concerns the same century as the argument, whatever the argument says",
   "It is written in the language the argument is written in"],
  ans=0,
  why=("Suggested skill 6.B is stated in two parts: describe specific examples of historically "
       "relevant evidence, and explain how specific examples of historically relevant evidence "
       "support an argument. Relevance is therefore a relation between the evidence and the "
       "claim, not a property of the source's length, date, or language.")),
 dict(
  q=("A student's thesis reads: the land empires of 1450 to 1750 expanded by similar military "
     "means but governed by different fiscal ones. Which pair of evidence would support both "
     "halves of the thesis?"),
  choices=[
   "Artillery in each empire's campaigns, together with the different ways each raised revenue",
   "Artillery in each empire's campaigns, together with the artillery in a third empire's campaigns",
   "The revenue methods of each empire, together with the revenue methods of a third",
   "The rivers of each empire, together with the mountains of each empire",
   "The chronicles of each empire, together with the paper each was written on"],
  ans=0,
  why=("KC-4.3.II supplies the shared military means and KC-4.3.I.D the differing revenue "
       "methods, so a thesis asserting both needs one piece of evidence for each half. Each "
       "rejected pair evidences one half twice, or neither half.")),
 dict(
  q=("Four pieces of evidence a student has gathered are listed in the table below.\n\n"
     "Which of them bear directly on the claim that an empire increased its influence by armed "
     "force and armed commerce?"),
  table=_T_EVIDENCE,
  choices=[
   "Evidence 1 and Evidence 3",
   "Evidence 1 and Evidence 2",
   "Evidence 2 and Evidence 4",
   "Evidence 3 and Evidence 4",
   "All four pieces"],
  ans=0,
  why=("KC-4.3.II names gunpowder, cannons, and armed trade as the means of imperial expansion, "
       "so the artillery train and the duties levied at a garrisoned post bear on the claim. "
       "The length of a chronicle and the rainfall two centuries later are facts about other "
       "things, which is what suggested skill 6.B means by relevance.")),
 dict(
  q=("Using the same list, why is the rainfall record a poor choice of evidence for an argument "
     "about how an empire increased its influence?"),
  table=_T_EVIDENCE,
  choices=[
   "It records a condition two centuries after the events the argument concerns",
   "It was written down rather than spoken",
   "It concerns a province rather than a capital",
   "It is a number rather than a sentence",
   "It survives in only one copy"],
  ans=0,
  why=("Suggested skill 6.B requires evidence to be historically relevant to the argument it "
       "supports, and a measurement taken two centuries later cannot bear on the methods of "
       "expansion at issue. Being written, numerical, provincial or rare has no bearing on "
       "relevance.")),
 dict(
  q=("The table below records hypothetical figures for two land empires of the period 1450 to "
     "1750.\n\n"
     "Which comparison is best supported by the table alone?"),
  table=_T_TWO_EMPIRES,
  choices=[
   "The two empires differed in how provincial revenue was collected but were similar in the scale of their religious building",
   "The two empires were identical in how provincial revenue was collected",
   "The two empires differed sharply in the scale of their religious building",
   "Neither empire used salaried officials in any province",
   "Neither empire farmed the taxes of any province"],
  ans=0,
  why=("KC-4.3.I.D names tax farming and other collection systems among the revenue methods "
       "and KC-4.3.I.A names monumental architecture among the means of legitimation, so the "
       "table sets a fiscal difference beside a legitimating similarity. The verifier "
       "recomputes both, and confirms every empire used both fiscal methods somewhere.")),
 dict(
  q=("Three draft claims for an essay comparing two land empires are given in the table "
     "below.\n\n"
     "Which draft is both a comparison and consistent with the framework?"),
  table=_T_CLAIMS,
  choices=[
   "Claim 1",
   "Claim 2",
   "Claim 3",
   "The second and the third drafts equally",
   "None of the three"],
  ans=0,
  why=("KC-4.3.II states that imperial expansion relied on the increased use of gunpowder, "
       "cannons, and armed trade, so a claim that neither empire used force contradicts the "
       "framework, and KC-4.3.II.B places the land empires of this unit across Asia, the Middle "
       "East, Southern Europe and North Africa rather than in the Western Hemisphere.")),
 dict(
  q=("A student argues that the land empires of this period were more alike than different. "
     "Which piece of evidence would most weaken that argument as the framework frames it?"),
  choices=[
   "Evidence that they used sharply different methods of raising revenue from their provinces",
   "Evidence that they all used gunpowder weapons in expansion",
   "Evidence that they all raised monumental buildings",
   "Evidence that they all recruited officials to govern provinces",
   "Evidence that they all fought wars with neighbouring states"],
  ans=0,
  why=("KC-4.3.II, KC-4.3.I.A and KC-4.3.I.C describe practices shared across these empires, so "
       "evidence of those supports the argument rather than weakening it. KC-4.3.I.D names "
       "several distinct revenue methods, which is where the framework itself locates variation "
       "between empires.")),
 dict(
  q=("Which of the following best explains how a specific example supports a general argument, "
     "in the sense suggested skill 6.B requires?"),
  choices=[
   "The example is stated, and the reason it bears on the claim is then explained",
   "The example is stated, and the reader is left to see the connection",
   "The claim is restated in different words after the example",
   "The example is described at greater length than the claim",
   "The example is placed at the end of the essay rather than the beginning"],
  ans=0,
  why=("Suggested skill 6.B has two parts, describing specific examples of historically "
       "relevant evidence AND explaining how those examples support an argument, so naming the "
       "example is only half the task. Length, position and restatement do not perform the "
       "second half.")),
 dict(
  q=("Two land empires of the period both expanded into neighbouring territory. A student wants "
     "to compare the causes. Which framing follows the framework's account?"),
  choices=[
   "Comparing the part played in each case by gunpowder weaponry and armed commerce",
   "Comparing the number of letters in each empire's name",
   "Comparing which empire is better known to modern readers",
   "Comparing the number of surviving portraits of each ruler",
   "Comparing the modern national borders that cross each empire's former territory"],
  ans=0,
  why=("KC-4.3.II makes gunpowder, cannons, and armed trade the framework's explanation of "
       "imperial expansion, so that is the axis on which a comparison of causes runs. Modern "
       "renown, modern borders, name lengths and portrait survival are facts about the record "
       "or about the present rather than about the expansion.")),
 dict(
  q=("A student claims that the land empires of 1450 to 1750 all incorporated populations "
     "unlike their rulers. Which framework statement most directly supports the claim?"),
  choices=[
   "Empires achieved increased scope and influence, shaping and being shaped by the diverse populations they incorporated",
   "Imperial expansion relied on gunpowder, cannons, and armed trade",
   "Political and religious disputes led to rivalries and conflict between states",
   "The Protestant Reformation marked a break with existing Christian traditions",
   "New state-supported transoceanic maritime exploration occurred in this period"],
  ans=0,
  why=("KC-4.3 states that empires achieved increased scope and influence around the world, "
       "shaping and being shaped by the diverse populations they incorporated, which is the "
       "diversity the claim asserts. The rejected statements are KC-4.3.II, KC-4.3.III.i, "
       "KC-4.1.VI.i and KC-4.1.III, none of which concerns incorporated populations.")),
 dict(
  q=("Why does the framework's phrase about empires being shaped by the populations they "
     "incorporated matter for a comparison essay?"),
  choices=[
   "Because it makes influence run in both directions, so a comparison can consider effects on the rulers as well",
   "Because it means the incorporated populations had no effect on the empire",
   "Because it means every empire governed a single people",
   "Because it means comparison between empires is impossible",
   "Because it means empires stopped expanding once they incorporated new peoples"],
  ans=0,
  why=("KC-4.3 says empires were shaping and being shaped by the diverse populations they "
       "incorporated, which is a two-way relation. Each rejected reading denies one half of "
       "that phrase or draws a conclusion about expansion the sentence does not support.")),
 dict(
  q=("A student's paragraph names four empires, gives a date for each, and stops. Against "
     "suggested skill 6.B, what is the paragraph missing?"),
  choices=[
   "An explanation of how the named evidence supports the argument being made",
   "A longer list of empires",
   "A translation of each empire's name",
   "A map of each empire's territory",
   "A footnote for every date given"],
  ans=0,
  why=("Suggested skill 6.B requires both describing specific examples of historically relevant "
       "evidence and explaining how those examples support an argument, and a bare list "
       "performs only the first. More names, translations and footnotes leave the same half "
       "undone.")),
 dict(
  q=("Which comparison between the land empires and the belief systems of this period is "
     "supported by the unit's own review statements?"),
  choices=[
   "Imperial rivalry and religious division were connected, since political and religious disputes set states against one another",
   "Imperial rivalry and religious division were unconnected in every case",
   "Religious division occurred only where no empire existed",
   "Imperial rivalry occurred only where all subjects shared one faith",
   "Neither imperial rivalry nor religious division occurred in the period"],
  ans=0,
  why=("KC-4.3.III.i states that political and religious disputes led to rivalries and conflict "
       "between states, and KC-4.1.VI adds that intensified interactions contributed to "
       "religious conflicts. Each rejected option denies a connection both statements assert, "
       "or denies the developments themselves.")),
 dict(
  q=("A student wishes to argue that empires in this period increased their influence by more "
     "than one kind of method. Which set of examples best supports that argument?"),
  choices=[
   "An artillery campaign, a new revenue system, and a programme of monumental building",
   "Three artillery campaigns in three different provinces",
   "Three revenue systems introduced in the same decade",
   "Three monumental buildings raised in the same capital",
   "Three chronicles written about the same campaign"],
  ans=0,
  why=("KC-4.3.II supplies military means, KC-4.3.I.D revenue methods, and KC-4.3.I.A "
       "legitimation through art and monumental architecture, so an argument about more than "
       "one kind of method needs an example from more than one of those statements. Each "
       "rejected set repeats a single kind.")),
 dict(
  q=("Which of the following is a difference between two land empires that the framework "
     "itself records, rather than one a student would have to supply from outside it?"),
  choices=[
   "The regions in which each was situated",
   "The average height of each ruler",
   "The number of poems written at each court",
   "The colour of each empire's official robes",
   "The names each gave to the months of the year"],
  ans=0,
  why=("KC-4.3.II.B assigns each land empire a region: the Manchu in Central and East Asia, the "
       "Mughal in South and Central Asia, the Ottoman in Southern Europe, the Middle East, and "
       "North Africa, and the Safavids in the Middle East. The framework records nothing about "
       "heights, court poetry, robes or calendars.")),
 dict(
  q=("A hypothetical essay opens: two empires of this period both expanded, and both used "
     "cannon. What must the essay add for this to become an argument rather than an "
     "observation?"),
  choices=[
   "A claim about what the similarity shows, supported by the evidence",
   "A second sentence repeating the observation",
   "A list of every empire that existed in the period",
   "The publication date of the sources consulted",
   "A statement that the topic is important"],
  ans=0,
  why=("Suggested skill 6.B asks students to support an argument using specific and relevant "
       "evidence, which presupposes a claim for the evidence to support. Repetition, an "
       "exhaustive list, a publication date and an assertion of importance supply no claim.")),
 dict(
  q=("A student compares an empire that expanded chiefly by conquest with one that expanded "
     "chiefly through armed commerce. What does the framework allow the student to say about "
     "the two?"),
  choices=[
   "Both used means the framework names as the basis of imperial expansion",
   "Only the first used means the framework names",
   "Only the second used means the framework names",
   "Neither used means the framework names",
   "The framework names no means of expansion at all"],
  ans=0,
  why=("KC-4.3.II names gunpowder, cannons, AND armed trade in a single sentence as what "
       "imperial expansion relied on, so conquest and armed commerce are both within its "
       "account. Each rejected option drops one of the three or denies the sentence "
       "entirely.")),
 dict(
  q=("An argument holds that the land empires of this period were creations of military "
     "technology alone. Which consideration most complicates that argument, using this unit's "
     "own content?"),
  choices=[
   "The unit also describes administration, revenue and legitimation as means by which rulers held power",
   "The unit denies that gunpowder weapons existed",
   "The unit places all four empires in the Western Hemisphere",
   "The unit says empires never fought one another",
   "The unit says rulers collected no revenue"],
  ans=0,
  why=("KC-4.3.I.A, KC-4.3.I.C and KC-4.3.I.D describe legitimation, recruited elites and "
       "revenue systems alongside the military means of KC-4.3.II, so technology alone does not "
       "exhaust the unit's account. The rejected options contradict statements the unit makes "
       "outright.")),
 dict(
  q=("Two students disagree. One says the empires of this period are best compared by how they "
     "expanded; the other by how they governed what they had taken. How does the unit's "
     "learning objective bear on the disagreement?"),
  choices=[
   "It asks for a comparison of the methods by which empires increased their influence, which covers both",
   "It asks only about warfare and excludes government",
   "It asks only about government and excludes warfare",
   "It forbids comparison between empires",
   "It restricts comparison to a single empire"],
  ans=0,
  why=("Unit 3: Learning Objective D asks students to compare the methods by which various "
       "empires increased their influence from 1450 to 1750, and the unit supplies both "
       "expansion at KC-4.3.II and administration at KC-4.3.I.A, KC-4.3.I.C and KC-4.3.I.D as "
       "such methods.")),
 dict(
  q=("Which of the following would be the strongest single piece of evidence for the claim that "
     "an empire's expansion and its revenue system were connected?"),
  choices=[
   "A record showing new revenue from a province being spent on the campaigns that took the next one",
   "A record listing the names of an empire's provinces",
   "A record of the weather during one campaign season",
   "A record of the number of scribes employed in the capital",
   "A record of a single tax paid in a single village"],
  ans=0,
  why=("KC-4.3.I.D says rulers used tribute collection, tax farming, and innovative "
       "tax-collection systems to generate revenue in order to forward state power and "
       "expansion, which is exactly the connection the claim asserts. A list, the weather, a "
       "staff count and one village's tax show no such link.")),
 dict(
  q=("A student writes that comparing two empires means listing what each did in turn. What is "
     "the best correction, given the unit's reasoning process?"),
  choices=[
   "A comparison identifies similarities and differences along a stated axis, rather than two separate lists",
   "A comparison must always conclude that the two are identical",
   "A comparison must always conclude that the two are entirely different",
   "A comparison requires at least five empires",
   "A comparison is only possible between empires in the same region"],
  ans=0,
  why=("The reasoning process printed for this topic is comparison, and Learning Objective D "
       "asks students to compare the methods by which various empires increased their "
       "influence, which requires a shared axis. Nothing there fixes the conclusion in advance, "
       "sets a minimum number, or confines comparison to one region.")),
 dict(
  q=("A hypothetical set of court records from two empires shows that each raised a great "
     "religious building in its capital within the same decade. What is the most defensible use "
     "of this evidence in a comparison?"),
  choices=[
   "As evidence of a shared method of legitimizing rule",
   "As evidence that the two empires were allies",
   "As evidence that the two empires shared a religion",
   "As evidence that neither empire used military force",
   "As evidence that the two empires had identical revenue systems"],
  ans=0,
  why=("KC-4.3.I.A states that rulers continued to use religious ideas, art, and monumental "
       "architecture to legitimize their rule, so two such buildings evidence a shared method. "
       "Alliance, shared belief, an absence of force and identical finances are conclusions the "
       "evidence does not reach.")),
 dict(
  q=("Which statement about the land empires of 1450 to 1750 would require evidence from "
     "outside the framework's own assertions to defend?"),
  choices=[
   "That one empire's army was better trained than another's",
   "That imperial expansion relied on gunpowder, cannons, and armed trade",
   "That land empires included the Manchu, the Mughal, the Ottoman and the Safavids",
   "That political and religious disputes led to rivalries between states",
   "That empires were shaped by the diverse populations they incorporated"],
  ans=0,
  why=("The four rejected statements are KC-4.3.II, KC-4.3.II.B, KC-4.3.III.i and KC-4.3 "
       "almost verbatim. The framework makes no comparative judgement about the training of any "
       "army, so that claim would have to be defended from elsewhere.")),
 dict(
  q=("A student wants to show that the empires of this period were connected to developments "
     "beyond their own borders. Which of the unit's review statements supports that?"),
  choices=[
   "The interconnection of the Eastern and Western Hemispheres transformed trade and had a significant social impact",
   "Land empires included the Manchu, the Mughal, the Ottoman and the Safavids",
   "Rulers used tribute collection and tax farming to raise revenue",
   "Rulers recruited bureaucratic elites to hold central control",
   "The Protestant Reformation marked a break with existing Christian traditions"],
  ans=0,
  why=("KC-4.1, printed in this topic's review list, states that the interconnection of the "
       "Eastern and Western Hemispheres, made possible by transoceanic voyaging, transformed "
       "trade and had a significant social impact on the world. The rejected statements concern "
       "the empires or their administration internally.")),
 dict(
  q=("An essay claims that religion and empire reinforced each other in this period. Which two "
     "framework statements together support the claim?"),
  choices=[
   "That rulers used religious ideas to legitimize rule, and that religious disputes led to conflict between states",
   "That rulers used religious ideas to legitimize rule, and that ship design improved",
   "That religious disputes led to conflict between states, and that American crops improved nutrition",
   "That ship design improved, and that American crops improved nutrition",
   "That empires incorporated diverse populations, and that ship design improved"],
  ans=0,
  why=("KC-4.3.I.A has rulers using religious ideas to legitimize their rule and KC-4.3.III.i "
       "has religious disputes leading to rivalries and conflict between states, so the two "
       "together give religion a role inside and between empires. Ship design is KC-4.1.II.A "
       "and American crops KC-4.1.V.D, neither of which concerns religion.")),
 dict(
  q=("Why is a claim that all four named land empires expanded for exactly the same reason hard "
     "to defend from the framework?"),
  choices=[
   "Because the framework names several means of expansion without ranking them for any empire",
   "Because the framework names only one empire",
   "Because the framework denies that any empire expanded",
   "Because the framework says expansion had no causes",
   "Because the framework treats the four empires as one state"],
  ans=0,
  why=("KC-4.3.II names gunpowder, cannons, and armed trade together and KC-4.3.II.B names four "
       "separate empires in four regions, but nothing there assigns a single dominant cause to "
       "any one of them. The rejected options contradict the plain content of both "
       "statements.")),
 dict(
  q=("A student has one strong example and needs to broaden an argument about imperial methods. "
     "What does suggested skill 6.B indicate is the better next step?"),
  choices=[
   "Add a second specific example and explain how it too supports the claim",
   "Repeat the first example in different words",
   "State that many other examples exist without naming any",
   "Replace the example with a general assertion",
   "Move the example to a footnote"],
  ans=0,
  why=("Suggested skill 6.B asks for specific examples of historically relevant evidence and "
       "for an explanation of how they support the argument, so a second worked example "
       "advances both halves. Repetition, an unnamed multitude, a bare assertion and a footnote "
       "advance neither.")),
 dict(
  q=("Which comparison of the land empires with the belief systems of the same period is best "
     "supported by the unit's review statements?"),
  choices=[
   "Both empires and religions grew in reach during the period, and both saw division as well as growth",
   "Empires grew while every religion shrank",
   "Religions grew while every empire shrank",
   "Neither empires nor religions changed in reach",
   "Both empires and religions were confined to one hemisphere"],
  ans=0,
  why=("KC-4.3 has empires achieving increased scope and influence and KC-4.1.VI has "
       "interactions expanding the reach of existing religions while contributing to religious "
       "conflicts; KC-4.1.VI.i and KC-4.1.VI.ii supply the division. KC-4.3.II locates imperial "
       "expansion in both hemispheres.")),
 dict(
  q=("A summary sentence for this topic is being drafted. Which version is both a comparison and "
     "consistent with the unit's review statements?"),
  choices=[
   "The land empires of 1450 to 1750 expanded by shared military and commercial means while differing in how they raised revenue and legitimized rule",
   "The land empires of 1450 to 1750 expanded without force and were identical in every respect",
   "The land empires of 1450 to 1750 governed populations that were the same everywhere",
   "The land empires of 1450 to 1750 lay entirely within the Western Hemisphere",
   "The land empires of 1450 to 1750 had no contact with the world beyond their borders"],
  ans=0,
  why=("The keyed sentence names a similarity from KC-4.3.II and differences drawn from "
       "KC-4.3.I.D and KC-4.3.I.A, which is what Learning Objective D asks for. Each rejected "
       "version contradicts KC-4.3.II, KC-4.3, KC-4.3.II.B or KC-4.1.")),
]
