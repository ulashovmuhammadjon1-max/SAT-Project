# AP WORLD HISTORY: MODERN 4.1 Technological Innovations from 1450 to 1750
# CED effective Fall 2024/2026, Unit 4 Transoceanic Interconnections, c. 1450 to
# c. 1750. The topic title in WORLD_HISTORY_topics.json is the string the CED's
# two-column topic page yields; it is copied verbatim and must not be retyped.
#
# Unit 4: Learning Objective A -- explain how cross-cultural interactions
# resulted in the diffusion of technology and facilitated changes in patterns of
# trade and travel from 1450 to 1750. Suggested skill 4.A, identify and describe
# a historical context for a specific historical development or process.
# Reasoning process: causation. Thematic focus: Technology and Innovation.
#
# Historical developments this module keys to, in the framework's own words:
#   KC-4.1.II    Knowledge, scientific learning, and technology from the
#                Classical, Islamic, and Asian worlds spread, facilitating
#                European technological developments and innovation.
#   KC-4.1.II.A  The developments included the production of new tools,
#                innovations in ship designs, and an improved understanding of
#                regional wind and currents patterns -- all of which made
#                transoceanic travel and trade possible.
#
# The illustrative examples are printed beside the topic under two headings, and
# the heading is itself framework content:
#   Innovations in ship design: caravel; carrack; fluyt.
#   European technological developments influenced by cross-cultural
#     interactions with the Classical, Islamic, and Asian worlds: lateen sail;
#     compass; astronomical charts.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT. The framework does not date any
# of these devices, name their inventors, describe how any of them worked, or
# say which was most important. It does not say that Europeans were the only
# people navigating oceans, and no item here implies it. The DIRECTION of the
# diffusion is the framework's own and is what several items turn on:
# knowledge, learning and technology travelled FROM the Classical, Islamic, and
# Asian worlds and facilitated European developments.
#
# Dates are written "1450 to 1750". Five choices A-E per HISTORY_BRIEF.md. Every
# stimulus is hypothetical or unattributed; no quotation is put in a real
# person's mouth.
TOPIC = ("4.1", "Technological Innovations from 1450 to 1750", 4)

_T_EXAMPLES = dict(
    headers=["Item named in the framework", "Heading it is printed under"],
    rows=[["Caravel", "Innovations in ship design"],
          ["Fluyt", "Innovations in ship design"],
          ["Compass", "European developments influenced by cross-cultural interactions"],
          ["Astronomical charts", "European developments influenced by cross-cultural interactions"]])

_T_CROSSINGS = dict(
    headers=["Period of a hypothetical shipping record", "Crossings attempted",
             "Crossings completed"],
    rows=[["Before the new charts were in use", "40", "22"],
          ["First years of their use", "60", "45"],
          ["Later years of their use", "90", "80"]])

_T_DEVELOPMENTS = dict(
    headers=["Development recorded", "What it consisted of"],
    rows=[["Development 1", "A new tool built for measuring position at sea"],
          ["Development 2", "A hull and rig designed to sail closer to the wind"],
          ["Development 3", "A written record of the winds and currents of one ocean region"],
          ["Development 4", "A new style of roofing tile used on houses inland"]])

QUESTIONS = [
 dict(
  q=("According to the framework, knowledge, scientific learning, and technology spread from "
     "which worlds, facilitating European technological developments and innovation?"),
  choices=[
   "The Classical, Islamic, and Asian worlds",
   "The Andean, Mesoamerican, and Caribbean worlds",
   "The Arctic, Siberian, and Pacific Island worlds",
   "The Australian, Melanesian, and Polynesian worlds",
   "The Saharan, Sahelian, and Kalahari worlds"],
  ans=0,
  why=("KC-4.1.II names the Classical, Islamic, and Asian worlds as the sources from which "
       "knowledge, scientific learning, and technology spread, facilitating European "
       "technological developments and innovation. The framework names no other set of sources "
       "for this diffusion.")),
 dict(
  q=("The framework lists the developments that made transoceanic travel and trade possible. "
     "Which of the following is that list?"),
  choices=[
   "New tools, innovations in ship designs, and an improved understanding of regional wind and currents patterns",
   "Standing navies, chartered companies, and fortified ports",
   "Gunpowder, cannons, and armed trade",
   "Tribute collection, tax farming, and innovative tax-collection systems",
   "Plantations, indentured servitude, and encomienda"],
  ans=0,
  why=("KC-4.1.II.A names new tools, innovations in ship designs, and an improved understanding "
       "of regional wind and currents patterns, and says all of these made transoceanic travel "
       "and trade possible. The rejected lists are KC-4.3.II, KC-4.3.I.D and KC-4.2.II.D, which "
       "concern expansion, revenue and labor rather than technology.")),
 dict(
  q=("A student writes that European technological innovation in this period developed in "
     "isolation from other societies. What is the most accurate correction from the framework?"),
  choices=[
   "Knowledge and technology from other worlds spread and facilitated those European developments",
   "European societies produced no technological developments in the period",
   "Technology spread only from Europe outward to other regions",
   "The framework treats technology as unrelated to travel and trade",
   "The framework confines all innovation to the period after 1750"],
  ans=0,
  why=("KC-4.1.II states that knowledge, scientific learning, and technology from the "
       "Classical, Islamic, and Asian worlds spread, facilitating European technological "
       "developments and innovation, so isolation is exactly what the framework denies. The "
       "third option reverses the direction the sentence gives.")),
 dict(
  q=("Which item is printed among the framework's illustrative examples of innovations in ship "
     "design for this topic?"),
  choices=[
   "The caravel",
   "The compass",
   "Astronomical charts",
   "The joint-stock company",
   "The encomienda"],
  ans=0,
  why=("The illustrative examples beside Unit 4: Learning Objective A print the caravel, the "
       "carrack and the fluyt under innovations in ship design, while the compass and "
       "astronomical charts appear under a separate heading. Joint-stock companies are "
       "KC-4.1.IV.C and the encomienda KC-4.2.II.D.")),
 dict(
  q=("The lateen sail, the compass, and astronomical charts are printed together as illustrative "
     "examples. What does the heading above them say about them?"),
  choices=[
   "They are European developments influenced by cross-cultural interactions with the Classical, Islamic, and Asian worlds",
   "They are labor systems introduced in the colonial Americas",
   "They are methods rulers used to legitimize their rule",
   "They are restrictive trade policies adopted by Asian states",
   "They are diseases transferred between hemispheres"],
  ans=0,
  why=("That heading is printed in the framework's own illustrative examples for this topic and "
       "matches KC-4.1.II, which has knowledge, scientific learning, and technology from those "
       "worlds facilitating European developments. The rejected descriptions belong to "
       "KC-4.2.II.D, KC-4.3.I.A, KC-4.3.II.A.i and KC-4.1.V.A.")),
 dict(
  q=("A hypothetical shipwright's notebook from the period describes a hull and rig that let a "
     "vessel hold a course closer to the wind than older vessels could.\n\n"
     "Which of the framework's developments does the notebook record?"),
  choices=[
   "An innovation in ship design",
   "An innovative tax-collection system",
   "A syncretic belief system",
   "A restrictive trade policy",
   "A new labor system on a plantation"],
  ans=0,
  why=("KC-4.1.II.A names innovations in ship designs among the developments that made "
       "transoceanic travel and trade possible, and the illustrative examples print the "
       "caravel, carrack and fluyt as instances. The rejected terms belong to KC-4.3.I.D, "
       "KC-4.1.VI, KC-4.3.II.A.i and KC-4.2.II.D.")),
 dict(
  q=("A hypothetical pilot's book from the period sets out, season by season, the winds and "
     "currents a ship will meet on one ocean route.\n\n"
     "Which framework development does the book represent?"),
  choices=[
   "An improved understanding of regional wind and currents patterns",
   "The production of a new tool",
   "An innovation in ship design",
   "The chartering of a monopoly company",
   "The recruitment of a bureaucratic elite"],
  ans=0,
  why=("KC-4.1.II.A names an improved understanding of regional wind and currents patterns as "
       "one of the three developments that made transoceanic travel and trade possible, and a "
       "seasonal record of winds and currents on a route is that understanding written down. "
       "Tools and ship design are the other two items in the same sentence.")),
 dict(
  q=("The framework says the developments of this topic made something possible. What?"),
  choices=[
   "Transoceanic travel and trade",
   "The abolition of coerced labor in the Americas",
   "The unification of the world's religions",
   "The end of warfare between states",
   "The disappearance of regional markets in Afro-Eurasia"],
  ans=0,
  why=("KC-4.1.II.A ends by saying that new tools, ship designs, and an improved understanding "
       "of regional wind and currents patterns all made transoceanic travel and trade possible. "
       "KC-4.2.II.C, KC-4.1.VI, KC-4.3.III.i and KC-4.1.IV each contradict one of the rejected "
       "options.")),
 dict(
  q=("Suggested skill 4.A asks a student to identify and describe a historical context for a "
     "specific development. Which of the following supplies a context for European advances in "
     "navigation in this period?"),
  choices=[
   "The spread of knowledge and technology from the Classical, Islamic, and Asian worlds",
   "The rainfall recorded in one European valley in a single year",
   "The number of shipwrights living in one port town",
   "The colour used to paint a particular vessel's hull",
   "The name given to a single ship by its owner"],
  ans=0,
  why=("KC-4.1.II identifies exactly that diffusion as what facilitated European technological "
       "developments and innovation, which is the surrounding development a context has to "
       "name. A year's rainfall, a headcount, a paint colour and a ship's name are details "
       "rather than a context.")),
 dict(
  q=("Why does the framework treat improvements in navigation as a cause of changes in trade "
     "rather than as an unrelated development?"),
  choices=[
   "Because it says these developments made transoceanic travel and trade possible",
   "Because it says trade declined once navigation improved",
   "Because it says navigation and trade were unconnected",
   "Because it says trade routes were fixed by treaty",
   "Because it says only inland trade grew in the period"],
  ans=0,
  why=("KC-4.1.II.A states that new tools, innovations in ship designs and an improved "
       "understanding of regional wind and currents patterns all made transoceanic travel and "
       "trade possible, which is a causal link stated in the framework's own words. Each "
       "rejected option denies or reverses it.")),
 dict(
  q=("The table below lists four items the framework prints as illustrative examples for this "
     "topic, with the heading each appears under.\n\n"
     "Which conclusion is supported by the table?"),
  table=_T_EXAMPLES,
  choices=[
   "Two of the listed items are ship designs and two are developments influenced by cross-cultural interaction",
   "All four listed items are ship designs",
   "All four listed items are developments influenced by cross-cultural interaction",
   "None of the listed items concerns navigation or shipping",
   "The four items are printed under four different headings"],
  ans=0,
  why=("The framework prints the caravel, carrack and fluyt under innovations in ship design, "
       "and the lateen sail, compass and astronomical charts under European developments "
       "influenced by cross-cultural interactions, which is the split KC-4.1.II and KC-4.1.II.A "
       "describe. The verifier recomputes the counts from the table.")),
 dict(
  q=("The table below reports a hypothetical shipping record for one ocean route across three "
     "periods.\n\n"
     "Which conclusion is best supported by the table alone?"),
  table=_T_CROSSINGS,
  choices=[
   "Both the number of crossings attempted and the share completed rose across the three periods",
   "The number of crossings attempted rose while the share completed fell",
   "The number of crossings attempted fell while the share completed rose",
   "Neither figure changed across the three periods",
   "Every crossing attempted was completed in every period"],
  ans=0,
  why=("KC-4.1.II.A ties an improved understanding of regional wind and currents patterns to "
       "making transoceanic travel and trade possible, and the record shows more voyages and a "
       "higher completion rate together. The verifier recomputes both columns and confirms that "
       "no period completed every crossing attempted.")),
 dict(
  q=("Four developments are described in the table below.\n\n"
     "Which of them fall within the framework's list of the developments that made transoceanic "
     "travel and trade possible?"),
  table=_T_DEVELOPMENTS,
  choices=[
   "The first three developments only",
   "The first development only",
   "The second and the fourth developments only",
   "The third and the fourth developments only",
   "All four developments"],
  ans=0,
  why=("KC-4.1.II.A names new tools, innovations in ship designs, and an improved understanding "
       "of regional wind and currents patterns. The verifier recomputes that the first three "
       "rows are one of each and that the roofing tile is none of them.")),
 dict(
  q=("Which of the following would be the strongest evidence that a European navigational "
     "advance drew on learning from elsewhere?"),
  choices=[
   "An instrument maker's manual in Europe that follows methods set out in earlier works from another world",
   "A record of the number of ships built in a European port",
   "A list of the crew aboard one European vessel",
   "A tally of the timber used to build one hull",
   "An account of the weather on one voyage"],
  ans=0,
  why=("KC-4.1.II claims that knowledge, scientific learning, and technology from the Classical, "
       "Islamic, and Asian worlds spread and facilitated European developments, so evidence for "
       "it must show a European work depending on earlier learning from elsewhere. Ship counts, "
       "crew lists, timber tallies and weather reports show no such dependence.")),
 dict(
  q=("A hypothetical merchant's account describes cargoes now reaching a European port directly "
     "by sea from another ocean, where before they had come overland through several hands.\n\n"
     "Which framework claim does the account best illustrate?"),
  choices=[
   "That the period's technological developments changed patterns of trade and travel",
   "That regional markets in Afro-Eurasia ceased to operate",
   "That European rulers abandoned mercantilist policies",
   "That land empires stopped using gunpowder weaponry",
   "That the exchange of crops between hemispheres ended"],
  ans=0,
  why=("Unit 4: Learning Objective A asks how cross-cultural interactions resulted in the "
       "diffusion of technology and facilitated changes in patterns of trade and travel, and "
       "KC-4.1.II.A says the resulting developments made transoceanic travel and trade "
       "possible. KC-4.1.IV has regional markets continuing to flourish, which the second "
       "option denies.")),
 dict(
  q=("Which statement best describes the direction of technological diffusion in the "
     "framework's account of this period?"),
  choices=[
   "Learning from the Classical, Islamic, and Asian worlds spread and facilitated European innovation",
   "European learning spread and facilitated Classical, Islamic, and Asian innovation",
   "No learning crossed between regions in the period",
   "Learning spread only within Europe and nowhere else",
   "Learning spread only between the two American hemispheres"],
  ans=0,
  why=("KC-4.1.II gives the direction explicitly: knowledge, scientific learning, and technology "
       "from the Classical, Islamic, and Asian worlds spread, facilitating European "
       "technological developments and innovation. The second option is the exact reversal, "
       "which is the easiest error to make and to miss here.")),
 dict(
  q=("A student is asked why an improved understanding of winds and currents mattered as much as "
     "a better hull. Which answer follows the framework?"),
  choices=[
   "Because the framework lists it beside new tools and ship designs as making ocean travel possible",
   "Because the framework says hull design had no effect on voyages",
   "Because the framework says wind patterns were unchanging and therefore unimportant",
   "Because the framework says navigation mattered only in coastal waters",
   "Because the framework says understanding the winds replaced the need for ships"],
  ans=0,
  why=("KC-4.1.II.A places an improved understanding of regional wind and currents patterns in "
       "the same list as new tools and innovations in ship designs, and says all of them made "
       "transoceanic travel and trade possible. Each rejected option contradicts part of that "
       "same sentence.")),
 dict(
  q=("Which of the following is the best example of a historical context, as suggested skill 4.A "
     "uses the term, for the appearance of new sailing vessels in this period?"),
  choices=[
   "A long exchange of technical knowledge among societies around the Mediterranean and the Indian Ocean",
   "The precise day on which one vessel was launched",
   "The number of nails used in one vessel's construction",
   "The personal preferences of a single shipowner",
   "The modern museum in which a model of the vessel is displayed"],
  ans=0,
  why=("Suggested skill 4.A asks students to identify and describe a historical context for a "
       "specific development, and KC-4.1.II supplies one: the spread of knowledge, scientific "
       "learning, and technology from the Classical, Islamic, and Asian worlds. A launch date, "
       "a nail count, one owner's taste and a modern display are not contexts.")),
 dict(
  q=("A hypothetical inventory from a European port in the period lists instruments for taking "
     "bearings and measuring position, alongside charts of distant coasts.\n\n"
     "Which two of the framework's three named developments does the inventory document?"),
  choices=[
   "The production of new tools, and an improved understanding of regional wind and currents patterns",
   "The production of new tools, and the growth of plantation agriculture",
   "Innovations in ship design, and the spread of syncretic religion",
   "The chartering of monopoly companies, and the collection of tribute",
   "The recruitment of officials, and the building of monuments"],
  ans=0,
  why=("KC-4.1.II.A names new tools, innovations in ship designs, and an improved understanding "
       "of regional wind and currents patterns; instruments are tools and charts record what is "
       "known of a region's waters. Plantations are KC-4.2.II.C, syncretism KC-4.1.VI, "
       "companies KC-4.1.IV.C and officials KC-4.3.I.C.")),
 dict(
  q=("Why is the framework's account of this topic placed under the theme of technology and "
     "innovation rather than under governance?"),
  choices=[
   "Because it concerns human adaptation and innovation and the consequences of technological advance",
   "Because it concerns how governments obtain and retain power",
   "Because it concerns how societies group their members",
   "Because it concerns the exchange of plants and animals",
   "Because it concerns the beliefs societies hold about themselves"],
  ans=0,
  why=("The thematic focus printed with this topic states that human adaptation and innovation "
       "have resulted in increased efficiency, comfort, and security and that technological "
       "advances have shaped human development and interactions with both intended and "
       "unintended consequences, which is what KC-4.1.II and KC-4.1.II.A describe.")),
 dict(
  q=("A historian argues that the technological changes of this period had consequences their "
     "makers did not intend. Which part of the framework most directly supports treating "
     "unintended consequences as part of the subject?"),
  choices=[
   "The thematic focus, which names both intended and unintended consequences of technological advance",
   "The statement that rulers used religious ideas to legitimize rule",
   "The statement that land empires included the Manchu and the Mughal",
   "The statement that peasant labor intensified as demand grew",
   "The statement that enslaved persons challenged existing authorities"],
  ans=0,
  why=("The technology and innovation thematic focus printed with this topic says technological "
       "advances have shaped human development and interactions with both intended and "
       "unintended consequences. The rejected statements are KC-4.3.I.A, KC-4.3.II.B, "
       "KC-4.2.II.A and KC-5.3.III.C.")),
 dict(
  q=("Two students disagree about whether a new instrument or a new hull mattered more for ocean "
     "voyaging in this period. What does the framework allow them to conclude?"),
  choices=[
   "That both belong to one list of developments the framework does not rank",
   "That the framework ranks the instrument above the hull",
   "That the framework ranks the hull above the instrument",
   "That the framework mentions neither",
   "That the framework treats both as irrelevant to voyaging"],
  ans=0,
  why=("KC-4.1.II.A names new tools and innovations in ship designs in a single list and says "
       "all of the listed developments made transoceanic travel and trade possible, without "
       "ordering them. Asserting a rank in either direction goes beyond what the sentence "
       "says.")),
 dict(
  q=("A hypothetical treatise written in a European port cites star tables compiled elsewhere "
     "and adapts them for use on a new route.\n\n"
     "Which framework claim does the treatise most directly evidence?"),
  choices=[
   "That scientific learning from other worlds facilitated European technological developments",
   "That European learning was unaffected by contact with other societies",
   "That astronomical knowledge played no part in navigation",
   "That the framework locates all innovation in the Americas",
   "That transoceanic travel had become impossible"],
  ans=0,
  why=("KC-4.1.II states that knowledge, scientific learning, and technology from the Classical, "
       "Islamic, and Asian worlds spread, facilitating European technological developments and "
       "innovation, and adapting tables compiled elsewhere is that facilitation. The "
       "illustrative examples name astronomical charts among the developments so influenced.")),
 dict(
  q=("Which of the following claims about this period would require evidence from outside the "
     "framework's own statements?"),
  choices=[
   "That one particular vessel design was faster than every other",
   "That knowledge and technology spread from the Classical, Islamic, and Asian worlds",
   "That new tools were among the developments of the period",
   "That an improved understanding of winds and currents developed",
   "That these developments made transoceanic travel and trade possible"],
  ans=0,
  why=("The four rejected statements are KC-4.1.II and KC-4.1.II.A almost verbatim. The "
       "framework compares no two vessel designs for speed, so that claim would have to be "
       "defended from somewhere else.")),
 dict(
  q=("A hypothetical royal instruction of the period orders pilots to record the winds they meet "
     "on each voyage and to deposit the record with the port authority on return.\n\n"
     "What does the instruction show about the framework's third development?"),
  choices=[
   "That an improved understanding of regional wind patterns was built up from accumulated observation",
   "That wind patterns were understood fully before any voyage was made",
   "That pilots were forbidden to keep any records",
   "That the winds of every ocean were identical",
   "That understanding the winds made ships unnecessary"],
  ans=0,
  why=("KC-4.1.II.A speaks of an IMPROVED understanding of regional wind and currents patterns, "
       "which is a process rather than a starting condition, and collecting pilots' "
       "observations is how such an improvement accumulates. The word regional also tells "
       "against treating every ocean as identical.")),
 dict(
  q=("An essay claims that technology alone explains the growth of transoceanic trade in this "
     "period. Which consideration from this unit most complicates the claim?"),
  choices=[
   "The framework also credits state sponsorship of exploration and the policies of rulers",
   "The framework denies that any technological change occurred",
   "The framework says trade did not grow in the period",
   "The framework says ships were not used for trade",
   "The framework says no state took an interest in exploration"],
  ans=0,
  why=("KC-4.1.III says new state-supported transoceanic maritime exploration occurred in this "
       "period and KC-4.1.IV.C adds mercantilist policies and joint-stock companies, so "
       "technology sits alongside state action in the framework's account. Each rejected option "
       "denies something the unit states outright.")),
 dict(
  q=("Which comparison between the technologies of this topic and the weapons of unit 3 is "
     "supported by the framework?"),
  choices=[
   "Both are technologies the framework connects to a wider process, one to expansion and one to ocean travel",
   "Both are treated by the framework as having no consequences",
   "Both are said by the framework to have been invented in the Americas",
   "Both are described as unavailable before 1750",
   "Both are said to have made trade impossible"],
  ans=0,
  why=("KC-4.3.II connects gunpowder, cannons, and armed trade to imperial expansion, while "
       "KC-4.1.II.A connects new tools, ship designs and knowledge of winds and currents to "
       "transoceanic travel and trade. Each rejected option contradicts one or both of those "
       "statements.")),
 dict(
  q=("A student asks whether the framework treats the spread of technology as a one-time event. "
     "What is the best answer from the text?"),
  choices=[
   "It describes a spread of knowledge that facilitated further developments and innovation",
   "It describes a single invention made in a single year",
   "It describes a spread that ended before 1450",
   "It describes technology as unchanged throughout the period",
   "It describes innovation as confined to one port"],
  ans=0,
  why=("KC-4.1.II has knowledge, scientific learning, and technology spreading and facilitating "
       "European technological developments and innovation, and KC-4.1.II.A then lists several "
       "developments that followed, so the framework describes a process rather than an "
       "event.")),
 dict(
  q=("Which piece of evidence would best support the claim that changes in travel followed the "
     "technological developments this topic describes?"),
  choices=[
   "Records of routes sailed before and after the developments came into use",
   "Records of the number of taverns in a port city",
   "Records of the price of bread in an inland town",
   "Records of the height of a cathedral spire",
   "Records of the number of students at a university"],
  ans=0,
  why=("Unit 4: Learning Objective A asks how the diffusion of technology facilitated changes in "
       "patterns of trade and travel, so evidence for it must compare travel before and after. "
       "Taverns, bread prices, spires and enrolments bear on none of that.")),
 dict(
  q=("A summary sentence for this topic is being drafted. Which version stays within what the "
     "framework asserts about the period 1450 to 1750?"),
  choices=[
   "Learning and technology from the Classical, Islamic, and Asian worlds spread and helped produce new tools, better ships, and a fuller grasp of winds and currents, making ocean travel and trade possible",
   "European societies invented ocean navigation without any contact with other regions, and trade patterns were unchanged",
   "No new tools or ship designs appeared, and ocean travel remained impossible throughout the period",
   "Technology spread outward from Europe alone, and other regions contributed nothing",
   "Understanding of winds and currents was complete before the period began, so no improvement occurred"],
  ans=0,
  why=("The keyed sentence joins KC-4.1.II on the spread of knowledge, scientific learning, and "
       "technology to KC-4.1.II.A on new tools, innovations in ship designs, and an improved "
       "understanding of regional wind and currents patterns making transoceanic travel and "
       "trade possible. Each rejected version contradicts one of those two statements.")),
]
