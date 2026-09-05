# AP U.S. HISTORY 1.1 Contextualizing Period 1  (title copied from US_HISTORY_topics.json)
# Unit 1, Period 1: 1491-1607. Suggested skill 4.A, identify and describe a historical
# context for a specific historical development or process.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 1 Learning Objective A
#       Explain the context for European encounters in the Americas from 1491 to 1607.
#
#   KC-1.1     As native populations migrated and settled across the vast expanse of
#              North America over time, they developed distinct and increasingly complex
#              societies by adapting to and transforming their diverse environments.
#   KC-1.1.I   Different native societies adapted to and transformed their environments
#              through innovations in agriculture, resource use, and social structure.
#   KC-1.2     Contact among Europeans, Native Americans, and Africans resulted in the
#              Columbian Exchange and significant social, cultural, and political changes
#              on both sides of the Atlantic Ocean.
#   KC-1.2.I   European expansion into the Western Hemisphere generated intense social,
#              religious, political, and economic competition and changes within European
#              societies.
#   KC-1.2.II  The Columbian Exchange and development of the Spanish Empire in the
#              Western Hemisphere resulted in extensive demographic, economic, and social
#              changes.
#   KC-1.2.III In their interactions, Europeans and Native Americans asserted divergent
#              worldviews regarding issues such as religion, gender roles, family, land
#              use, and power.
#
#   The topic page's own instruction on what context is: students examine "change from
#   and/or continuity with preceding historical developments" and "similarities and/or
#   differences with contemporaneous historical developments in different regions or
#   geographical areas."
#
# WHAT IS NOT KEYED, DELIBERATELY. This is a CONTEXTUALIZING topic and its Required
# Course Content is a PREVIEW of the unit's key concepts, not the detail behind them.
# So no key here names a people, a place, a crop, a disease, a date, an explorer or a
# colony -- all of that belongs to 1.2 through 1.7, whose pages carry the lettered
# sub-points. Every key rests on the previewed sentences above and on what the skill of
# contextualization is. Several items exist precisely to test that boundary.
#
# NO FIGURES: the bank cannot display images, so the one data item carries a table=.
# PROSE ONLY: no LaTeX; a span of years is written "1491 to 1607", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("1.1", "Contextualizing Period 1", 1)

_T_SETTLEMENT = dict(
    headers=["Region of North America (illustrative)",
             "Principal food source described",
             "Form of settlement described"],
    rows=[["Region 1", "Maize raised on irrigated fields", "Permanent towns"],
          ["Region 2", "Fish and shellfish taken from rivers and the coast", "Permanent villages"],
          ["Region 3", "Bison hunted on foot across grassland", "Camps moved with the herds"],
          ["Region 4", "Nuts, game and berries gathered in woodland", "Villages moved every few years"]])

_T_CONTEXT = dict(
    headers=["Statement a student proposes as context (illustrative)",
             "Does it look before the period, or beside it?"],
    rows=[["Native societies had been migrating and settling across North America over time",
           "Before"],
          ["European societies were competing with one another over religion and trade",
           "Beside"],
          ["Native societies had developed distinct and increasingly complex societies",
           "Before"],
          ["West African societies were in contact with Europeans across the Atlantic",
           "Beside"]])

QUESTIONS = [

 dict(q="Unit 1's Learning Objective A asks students to explain the context for European "
        "encounters in the Americas across a stated span of years. Which span does the "
        "framework give?",
      choices=[
        "1491 to 1607",
        "1450 to 1550",
        "1500 to 1650",
        "1607 to 1754",
        "1492 to 1600"],
      ans=0,
      why="Unit 1 Learning Objective A reads 'Explain the context for European encounters in "
          "the Americas from 1491 to 1607.' The span 1607 to 1754 is Period 2's, and the "
          "other three appear nowhere in the framework's periodisation."),

 dict(q="According to KC-1.1, what did native populations do that produced distinct and "
        "increasingly complex societies?",
      choices=[
        "They migrated and settled across the vast expanse of North America over time, "
        "adapting to and transforming their diverse environments",
        "They were united under a single political authority that spread a common way of life",
        "They abandoned agriculture in favour of hunting as the climate changed",
        "They arrived in one migration and remained where they first landed",
        "They adopted the practices of the first Europeans they encountered"],
      ans=0,
      why="KC-1.1 states that as native populations migrated and settled across the vast "
          "expanse of North America over time, they developed distinct and increasingly "
          "complex societies by adapting to and transforming their diverse environments. "
          "Neither a single authority, an abandonment of agriculture, a single arrival nor "
          "European influence appears in that sentence, and the last is chronologically "
          "impossible for developments the framework places before contact."),

 dict(q="KC-1.1.I names three things through which different native societies adapted to and "
        "transformed their environments. Which set names all three?",
      choices=[
        "Agriculture, resource use, and social structure",
        "Agriculture, warfare, and written record-keeping",
        "Trade, religion, and social structure",
        "Resource use, migration, and monarchy",
        "Agriculture, resource use, and maritime navigation"],
      ans=0,
      why="KC-1.1.I states that different native societies adapted to and transformed their "
          "environments through innovations in agriculture, resource use, and social "
          "structure. Warfare, written record-keeping, trade, religion, monarchy and "
          "maritime navigation are not in that list."),

 dict(q="A student writes that KC-1.1.I shows native societies were shaped by their "
        "environments. What does the sentence say that this summary leaves out?",
      choices=[
        "That the societies TRANSFORMED their environments as well as adapting to them",
        "That the societies were shaped by contact with Europeans",
        "That the innovations were the same in every region",
        "That the environments were uniform across North America",
        "That the framework treats the environment as unimportant"],
      ans=0,
      why="KC-1.1.I says native societies 'adapted to AND TRANSFORMED their environments'. A "
          "summary keeping only the adaptation makes the relationship one-way, which is the "
          "half of the framework's claim that a student is most likely to drop. The "
          "framework says the societies were distinct rather than uniform, calls the "
          "environments diverse in KC-1.1, and places these developments before the contact "
          "described in KC-1.2."),

 dict(q="According to KC-1.2, contact among which three groups resulted in the Columbian "
        "Exchange and significant changes on both sides of the Atlantic Ocean?",
      choices=[
        "Europeans, Native Americans, and Africans",
        "Europeans, Native Americans, and Asians",
        "Europeans and Native Americans only",
        "Spanish, Portuguese, and English settlers",
        "Native Americans, Africans, and Pacific Islanders"],
      ans=0,
      why="KC-1.2 states that contact among Europeans, Native Americans, and Africans "
          "resulted in the Columbian Exchange and significant social, cultural, and "
          "political changes on both sides of the Atlantic Ocean. Dropping Africans, or "
          "substituting Asians or Pacific Islanders, changes the framework's own list; the "
          "three European nationalities are not the grouping KC-1.2 uses."),

 dict(q="KC-1.2 says the changes following contact occurred on BOTH SIDES of the Atlantic "
        "Ocean. Which reading does that phrase rule out?",
      choices=[
        "That the consequences of contact were confined to the Americas",
        "That the Columbian Exchange involved the movement of goods",
        "That Europeans experienced political change in this period",
        "That contact produced social and cultural change as well as political change",
        "That the framework treats contact as significant"],
      ans=0,
      why="KC-1.2's phrase 'on both sides of the Atlantic Ocean' is what makes the "
          "consequences two-directional, so a reading that confines them to the Americas is "
          "the one it excludes. The other four are things KC-1.2 asserts rather than "
          "excludes: it names social, cultural, and political changes, and KC-1.2.I "
          "describes changes within European societies."),

 dict(q="According to KC-1.2.I, what did European expansion into the Western Hemisphere "
        "generate?",
      choices=[
        "Intense social, religious, political, and economic competition and changes within "
        "European societies",
        "A settled agreement among European states over the division of the hemisphere",
        "The end of religious disagreement within Europe",
        "A decline in economic activity across European societies",
        "Changes confined to the territories Europeans claimed"],
      ans=0,
      why="KC-1.2.I states that European expansion into the Western Hemisphere generated "
          "intense social, religious, political, and economic competition and changes within "
          "European societies. Agreement, an end to religious disagreement and a decline in "
          "activity are the opposites of competition and change, and the last option "
          "contradicts the sentence's location of those changes WITHIN European societies."),

 dict(q="KC-1.2.II attributes extensive demographic, economic, and social changes to two "
        "things together. Which pair does the framework name?",
      choices=[
        "The Columbian Exchange and the development of the Spanish Empire in the Western "
        "Hemisphere",
        "The Columbian Exchange and the growth of English settlement",
        "The Spanish Empire and the arrival of Christianity in Europe",
        "European competition and the migration of native populations",
        "The Columbian Exchange and innovations in native agriculture"],
      ans=0,
      why="KC-1.2.II names the Columbian Exchange and the development of the Spanish Empire "
          "in the Western Hemisphere as together resulting in extensive demographic, "
          "economic, and social changes. English settlement belongs to Period 2, and the "
          "other pairings recombine terms the framework keeps apart."),

 dict(q="Which three kinds of change does KC-1.2.II say followed from the Columbian Exchange "
        "and the development of the Spanish Empire?",
      choices=[
        "Demographic, economic, and social",
        "Demographic, military, and religious",
        "Political, legal, and economic",
        "Social, cultural, and political",
        "Economic, technological, and military"],
      ans=0,
      why="KC-1.2.II names extensive demographic, economic, and social changes. 'Social, "
          "cultural, and political' is KC-1.2's list, describing the changes on both sides "
          "of the Atlantic, and mistaking one for the other is the likeliest confusion here; "
          "military, religious, legal and technological change are not in either list."),

 dict(q="According to KC-1.2.III, Europeans and Native Americans asserted divergent "
        "worldviews in their interactions. Which set of issues does the framework name?",
      choices=[
        "Religion, gender roles, family, land use, and power",
        "Religion, language, currency, and law",
        "Land use, taxation, and military service",
        "Family, education, and inheritance",
        "Religion, trade routes, and shipbuilding"],
      ans=0,
      why="KC-1.2.III states that in their interactions, Europeans and Native Americans "
          "asserted divergent worldviews regarding issues such as religion, gender roles, "
          "family, land use, and power. Language, currency, law, taxation, military service, "
          "education, inheritance, trade routes and shipbuilding are not among them."),

 dict(q="KC-1.2.III says the worldviews Europeans and Native Americans asserted were "
        "DIVERGENT. Which of the following best states what that word claims?",
      choices=[
        "That the two sides held differing views and each maintained its own",
        "That one side had a worldview and the other did not",
        "That the two sides gradually came to share a single worldview",
        "That neither side held views about religion or land use",
        "That the differences between them were resolved during the period"],
      ans=0,
      why="KC-1.2.III's word 'asserted', applied to both parties, and 'divergent', applied to "
          "their worldviews, together describe two sides each maintaining differing views. "
          "The sentence does not say one side lacked a worldview, does not describe "
          "convergence, and does not report a resolution; that neither side held such views "
          "is contradicted by the list of issues the sentence gives."),

 dict(q="The topic page tells students that to understand context they could examine change "
        "from or continuity with PRECEDING historical developments, and similarities or "
        "differences with CONTEMPORANEOUS developments in different regions. Which pair of "
        "statements matches those two approaches in that order?",
      choices=[
        "Native societies had been developing across North America before 1491; European "
        "societies were competing with one another at the same time",
        "European societies were competing with one another at the same time; native "
        "societies had been developing across North America before 1491",
        "Both statements describe developments preceding the period",
        "Both statements describe developments in the same region",
        "Neither statement is the kind the topic page describes"],
      ans=0,
      why="The topic page names two ways into context: change from or continuity with "
          "PRECEDING developments, and similarities or differences with CONTEMPORANEOUS "
          "developments in different regions. KC-1.1's account of native migration and "
          "settlement 'over time' is the preceding one; KC-1.2.I's competition within "
          "European societies runs beside the period in a different region. Reversing the "
          "pair, or calling both preceding or both same-region, misapplies the page's own "
          "distinction."),

 dict(q="A hypothetical student essay opens by describing the Columbian Exchange in detail "
        "and then states that this is the context for European encounters in the Americas. "
        "Why does that use of the term not match the topic page's instruction?",
      choices=[
        "The Columbian Exchange is a consequence of the encounters, so it cannot be the "
        "context that preceded or surrounded them",
        "The Columbian Exchange is not mentioned anywhere in Unit 1",
        "Context must always be economic rather than biological",
        "The essay should have described a single region rather than the Atlantic world",
        "Contextualization requires naming a date"],
      ans=0,
      why="The topic page describes context as preceding developments or contemporaneous "
          "developments elsewhere, and KC-1.2 places the Columbian Exchange among the RESULTS "
          "of contact. Using a result as the context inverts the relationship. The Exchange "
          "is named in KC-1.2 and KC-1.2.II, so the second option is false, and the framework "
          "restricts context neither to one kind of subject, nor to one region, nor to a "
          "stated date."),

 dict(q="Skill 4.A, which this topic practises, is stated in the framework as which of the "
        "following?",
      choices=[
        "Identify and describe a historical context for a specific historical development or "
        "process",
        "Explain how a historical development or process relates to another historical "
        "development or process",
        "Identify patterns among or connections between historical developments and processes",
        "Support an argument using specific and relevant evidence",
        "Explain the point of view, purpose, historical situation, and/or audience of a source"],
      ans=0,
      why="The suggested skill printed on this topic page is 4.A, identify and describe a "
          "historical context for a specific historical development or process, and it is "
          "the skill Unit 1 Learning Objective A asks students to apply when they explain "
          "the context for European encounters in the Americas from 1491 to 1607. The other "
          "four are skills 5.B, 5.A, 6.B and 2.B, each printed on other topic pages of this "
          "course."),

 dict(q="Using the table of illustrative regions, what does the record shown support about "
        "native societies before European contact?",
      table=_T_SETTLEMENT,
      choices=[
        "Different food sources are recorded alongside different forms of settlement, which "
        "is the variation KC-1.1 describes",
        "Every region recorded the same food source and the same form of settlement",
        "Only one region is recorded as having a permanent form of settlement",
        "The record shows agriculture in every region",
        "The record shows that settlement did not vary with the food source"],
      ans=0,
      why="Read from the table alone: four regions carry four different principal food "
          "sources and three different forms of settlement, and the two vary together. That "
          "is the distinctness KC-1.1 attributes to societies adapting to diverse "
          "environments, and KC-1.1.I names agriculture and resource use among the "
          "innovations. Two regions record permanent settlement, not one, and only one "
          "records maize agriculture, so 'agriculture in every region' is false."),

 dict(q="Using the same table, which claim goes BEYOND what the record can support?",
      table=_T_SETTLEMENT,
      choices=[
        "That the societies in these regions had no contact with one another",
        "That the recorded food sources differ from region to region",
        "That two of the four regions are recorded with permanent settlement",
        "That one recorded food source is a cultivated crop",
        "That the forms of settlement recorded are not all the same"],
      ans=0,
      why="The table records a food source and a form of settlement for each region and "
          "nothing about relations between regions, so contact is a claim it cannot reach. "
          "The other four are read directly off the rows: the food sources differ, two rows "
          "say permanent, maize is a cultivated crop, and the settlement forms are not "
          "uniform. KC-1.1.I concerns agriculture, resource use and social structure, none of "
          "which is a claim about intergroup contact."),

 dict(q="Using the table of proposed context statements, which pair does the record place "
        "BEFORE the period rather than beside it?",
      table=_T_CONTEXT,
      choices=[
        "The statements about native migration and settlement, and about increasingly complex "
        "native societies",
        "The statements about European competition, and about West African contact across the "
        "Atlantic",
        "The statements about native migration, and about European competition",
        "All four statements are placed before the period",
        "None of the four statements is placed before the period"],
      ans=0,
      why="Read from the table alone: exactly two rows are marked 'Before', and they are the "
          "two describing native migration and settlement and increasingly complex native "
          "societies, which is what KC-1.1 states. The two marked 'Beside' are the European "
          "and West African rows, matching the topic page's second approach, contemporaneous "
          "developments in different regions."),

 dict(q="A hypothetical class discussion asks whether the framework's account of Period 1 "
        "begins with Europeans. What does KC-1.1's placement establish?",
      choices=[
        "The unit's first key concept describes native societies developing over time before "
        "the encounters the Learning Objective asks students to contextualise",
        "The unit's first key concept describes the arrival of Europeans",
        "The framework offers no account of the Americas before 1491",
        "The framework treats native societies only as they appear in European sources",
        "The unit begins with the Columbian Exchange"],
      ans=0,
      why="KC-1.1 is the unit's first key concept and describes native populations migrating "
          "and settling over time and developing distinct and increasingly complex societies; "
          "KC-1.2, which follows it, is where contact appears. Learning Objective A asks for "
          "the CONTEXT for European encounters, and the framework supplies that context in "
          "KC-1.1 before the encounters themselves."),

 dict(q="Which statement belongs to KC-1.2's account of what followed contact rather than to "
        "KC-1.1's account of what preceded it?",
      choices=[
        "Significant social, cultural, and political changes occurred on both sides of the "
        "Atlantic Ocean",
        "Native populations migrated and settled across the vast expanse of North America",
        "Native societies developed distinct and increasingly complex societies",
        "Different native societies made innovations in agriculture and resource use",
        "Native societies adapted to and transformed their diverse environments"],
      ans=0,
      why="Only the first belongs to KC-1.2, which describes what contact among Europeans, "
          "Native Americans, and Africans resulted in. The other four are KC-1.1 and "
          "KC-1.1.I, describing the migration, settlement, complexity and environmental "
          "innovation the framework places before the encounters."),

 dict(q="A hypothetical textbook passage states that European expansion changed the Americas "
        "and left Europe as it was. Which framework sentence most directly contradicts it?",
      choices=[
        "KC-1.2.I, which says expansion generated competition and changes WITHIN European "
        "societies",
        "KC-1.1.I, which names innovations in agriculture, resource use, and social structure",
        "KC-1.2.III, which describes divergent worldviews regarding religion and land use",
        "KC-1.1, which describes native migration across North America",
        "Learning Objective A, which states the span 1491 to 1607"],
      ans=0,
      why="KC-1.2.I locates intense social, religious, political, and economic competition "
          "and changes WITHIN European societies, which is exactly what the passage denies; "
          "KC-1.2 makes the same point with 'on both sides of the Atlantic Ocean'. The other "
          "sentences concern native societies, worldviews in interaction, and the period's "
          "span, none of which speaks to whether Europe changed."),

 dict(q="What does the framework's word 'diverse', used of environments in KC-1.1, do for the "
        "claim that native societies were distinct?",
      choices=[
        "It supplies the reason the societies differed, since they adapted to and transformed "
        "environments that were not alike",
        "It establishes that the societies were unaware of one another",
        "It shows that the environments were unchanged by the societies living in them",
        "It restricts the claim to agricultural societies",
        "It places the developments after European contact"],
      ans=0,
      why="KC-1.1 links distinct and increasingly complex societies to adapting to and "
          "transforming DIVERSE environments, so the diversity of the environments is what "
          "the sentence offers as the reason the societies differed. The same sentence says "
          "the societies transformed those environments, which rules out 'unchanged'; it "
          "makes no claim about mutual awareness, is not restricted to agriculture, and "
          "describes developments over time before the contact of KC-1.2."),

 dict(q="A hypothetical student proposes as context for the encounters: 'Native societies "
        "were static until Europeans arrived.' Why does the framework not support it?",
      choices=[
        "KC-1.1 describes native societies developing over time and becoming increasingly "
        "complex before contact",
        "The framework does not discuss native societies before 1491",
        "The framework says native societies changed only in their agriculture",
        "The framework attributes all change in the Americas to the Columbian Exchange",
        "The framework says native societies were identical to one another"],
      ans=0,
      why="KC-1.1 states that native populations migrated and settled OVER TIME and developed "
          "increasingly complex societies, which is a description of change rather than "
          "stasis, and KC-1.1.I names innovations in agriculture, resource use AND social "
          "structure. The framework does discuss the period before contact, does not confine "
          "change to agriculture, and calls the societies distinct rather than identical."),

 dict(q="Which of the following is NOT among the changes KC-1.2 attributes to contact?",
      choices=[
        "Technological",
        "Social",
        "Cultural",
        "Political",
        "The Columbian Exchange"],
      ans=0,
      why="KC-1.2 names the Columbian Exchange and significant social, cultural, and "
          "political changes. Technological change is not in that sentence. The Columbian "
          "Exchange is named in it, which is why it belongs among the four that are."),

 dict(q="A hypothetical seminar handout lists four statements and asks which could serve as "
        "context for European encounters under the topic page's own definition. Which "
        "statement fails that test?",
      choices=[
        "A description of an event that occurred in the Americas in the 1660s",
        "A description of native societies before 1491",
        "A description of competition within European societies during the period",
        "A description of West African societies during the period",
        "A description of long-run native migration across North America"],
      ans=0,
      why="The topic page defines context as preceding developments or contemporaneous "
          "developments in different regions. An event of the 1660s is later than the span "
          "1491 to 1607 that Learning Objective A gives, so it is neither. The other four are "
          "either preceding, as in KC-1.1, or contemporaneous elsewhere, as with the European "
          "competition of KC-1.2.I and the African societies named among KC-1.2's three "
          "groups in contact."),

 dict(q="KC-1.2.III names 'power' among the issues over which worldviews diverged. What does "
        "including it alongside religion, gender roles, family and land use indicate about "
        "the framework's account?",
      choices=[
        "That the divergence extended to political relations as well as to belief and daily "
        "life",
        "That the framework treats power as the only real issue between the two sides",
        "That religion and family were not genuinely at issue",
        "That the divergence concerned material questions only",
        "That the two sides agreed about everything except power"],
      ans=0,
      why="KC-1.2.III's list runs from religion and family through land use to power, so it "
          "spans belief, daily life and political relations together; the sentence gives no "
          "ranking among them, which rules out treating power as the only real issue or the "
          "sole point of disagreement. Religion and family are in the list, and religion is "
          "not a material question, so neither of the remaining options holds."),

 dict(q="The framework says the changes in KC-1.2.II were EXTENSIVE. Which of the following "
        "does that word support, given the rest of the sentence?",
      choices=[
        "That demographic, economic, and social change following the Exchange and the Spanish "
        "Empire's development was wide-reaching",
        "That the changes were confined to the Spanish Empire's own territories",
        "That the changes were principally military",
        "That the changes were slow enough to be unnoticed",
        "That the changes affected only the Western Hemisphere"],
      ans=0,
      why="KC-1.2.II describes extensive demographic, economic, and social changes, so "
          "'extensive' qualifies exactly those three and makes them wide-reaching. Confining "
          "them to Spanish territory or to the Western Hemisphere contradicts KC-1.2's 'both "
          "sides of the Atlantic Ocean'; the sentence names no military change and says "
          "nothing about the pace at which the changes occurred."),

 dict(q="Which pairing correctly matches a Unit 1 key concept with what it is about?",
      choices=[
        "KC-1.1 with native societies before contact, and KC-1.2 with the consequences of "
        "contact",
        "KC-1.1 with the consequences of contact, and KC-1.2 with native societies before "
        "contact",
        "KC-1.1 with European competition, and KC-1.2 with native agriculture",
        "KC-1.1 with the Columbian Exchange, and KC-1.2 with divergent worldviews only",
        "KC-1.1 and KC-1.2 with the same subject, stated twice"],
      ans=0,
      why="KC-1.1 concerns native populations migrating, settling and developing distinct and "
          "increasingly complex societies; KC-1.2 concerns what contact among Europeans, "
          "Native Americans, and Africans resulted in. Reversing them, or assigning European "
          "competition and native agriculture the other way round, misstates both. Divergent "
          "worldviews are KC-1.2.III, one part of KC-1.2 rather than the whole of it."),

 dict(q="A hypothetical revision guide claims that Unit 1's Required Course Content for this "
        "topic supplies the detail of Spanish exploration and conquest. What is wrong with "
        "that claim?",
      choices=[
        "This topic's Required Course Content is a PREVIEW of the unit's key concepts, and "
        "the detail belongs to the later topics of the unit",
        "The framework does not cover Spanish exploration anywhere in Unit 1",
        "Spanish exploration belongs to Period 2 rather than Period 1",
        "The Required Course Content for this topic lists no key concepts at all",
        "The framework treats Spanish exploration as context rather than content"],
      ans=0,
      why="The topic page prints the unit's key concepts under the heading PREVIEW and tells "
          "the teacher to select one or two for which students most need context, so the "
          "detail sits in the later topics rather than here. KC-1.2.II names the development "
          "of the Spanish Empire, so Unit 1 does cover it and it is not deferred to Period 2, "
          "and the preview does list key concepts."),

 dict(q="Which single sentence best states the whole of what the framework previews for "
        "Unit 1, without adding to it?",
      choices=[
        "Native societies developed distinctly across North America by adapting to and "
        "transforming diverse environments, and then contact among Europeans, Native "
        "Americans, and Africans brought the Columbian Exchange and change on both sides of "
        "the Atlantic",
        "Europeans arrived in the Americas and imposed their institutions on societies that "
        "had not changed for centuries",
        "The Columbian Exchange moved crops and animals between hemispheres, which is the "
        "whole of what Period 1 covers",
        "Native societies and European societies developed along identical lines until they "
        "met",
        "Spanish, Portuguese and English colonies competed for territory across North America"],
      ans=0,
      why="The first collects KC-1.1, KC-1.1.I and KC-1.2 in the order the framework gives "
          "them and adds nothing. The second contradicts KC-1.1's account of societies "
          "developing over time; the third reduces KC-1.2 to one part of itself and omits "
          "KC-1.1 entirely; the fourth contradicts 'distinct'; and the fifth describes "
          "colonial competition that Period 1's key concepts do not state."),

 dict(q="Taken together, what does the framework's Unit 1 preview establish about the two "
        "sides of the encounters it asks students to contextualise?",
      choices=[
        "Each already had developed societies of its own, and each was changed by the contact "
        "between them",
        "One side had developed societies and the other was changed by the encounter",
        "Neither side changed as a result of the encounters",
        "Both sides changed, but only in their religious beliefs",
        "Change on both sides was confined to the years after 1607"],
      ans=0,
      why="KC-1.1 gives native societies their own long development, KC-1.2.I gives European "
          "societies competition and change of their own, and KC-1.2 places significant "
          "change on BOTH sides of the Atlantic, which together make the encounter one "
          "between two already-developed sides that both changed. KC-1.2 names social, "
          "cultural and political change rather than religious change alone, and Learning "
          "Objective A places the period at 1491 to 1607."),
]
