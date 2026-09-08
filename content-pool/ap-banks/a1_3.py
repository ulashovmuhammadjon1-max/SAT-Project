# AP U.S. HISTORY 1.3 European Exploration in the Americas
# (title copied from US_HISTORY_topics.json)
# Unit 1, Period 1: 1491 to 1607. Suggested skill 1.A, identify a historical concept,
# development, or process. Reasoning process printed for this topic: Causation.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 1 Learning Objective C
#       Explain the causes of exploration and conquest of the New World by various
#       European nations.
#
#   KC-1.2.I.A   European nations' efforts to explore and conquer the New World stemmed
#                from a search for new sources of wealth, economic and military
#                competition, and a desire to spread Christianity.
#
#   Read with its parents, which this topic page sits under:
#   KC-1.2       Contact among Europeans, Native Americans, and Africans resulted in the
#                Columbian Exchange and significant social, cultural, and political
#                changes on both sides of the Atlantic Ocean.
#   KC-1.2.I     European expansion into the Western Hemisphere generated intense
#                social, religious, political, and economic competition and changes
#                within European societies.
#
#   THEMATIC FOCUS printed on this topic page, America in the World WOR:
#       Diplomatic, economic, cultural, and military interactions between empires,
#       nations, and peoples shape the development of America and America's
#       increasingly important role in the world.
#
#   Reasoning Process 2, Causation:
#       2.i   Describe causes and/or effects of a specific historical development or
#             process.
#       2.ii  Explain the relationship between causes and effects of a specific
#             historical development or process.
#       2.iii Explain the difference between primary and secondary causes and between
#             short- and long-term effects.
#       2.iv  Explain how a relevant context influenced a specific historical
#             development or process.
#       2.v   Explain the relative historical significance of different causes and/or
#             effects.
#
#   The unit overview's note on periodisation, which the framework prints in its own
#   words: events, processes, and developments are not constrained by the given dates
#   and may begin before, or continue after, the approximate dates assigned to each
#   unit and topic.
#
# WHAT IS NOT KEYED. The Required Course Content for this topic is ONE sentence,
# KC-1.2.I.A, naming three causes. So no key here asserts anything about the Columbian
# Exchange's contents, maritime technology, joint-stock companies, epidemics, the
# encomienda system or the caste system: those are KC-1.2.I.B, KC-1.2.I.C, KC-1.2.II.A,
# KC-1.2.II.B and KC-1.2.II.D, which belong to topics 1.4 and 1.5. Several items appear
# here precisely to test that boundary, and they use those sentences as DISTRACTORS --
# true statements of the framework that are not answers to a question about causes.
# The topic page's optional sources name Columbus, Champlain and Hakluyt; the CED says
# in as many words that none of the exam questions requires students to have studied
# those specific sources, so nothing here rests on them.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=.
# PROSE ONLY: no LaTeX; a span of years is written "1491 to 1607", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("1.3", "European Exploration in the Americas", 1)

_T_MOTIVES = dict(
    headers=["Set of hypothetical documents",
             "Documents in the set",
             "Mentioning a search for new wealth",
             "Mentioning rivalry with another European crown",
             "Mentioning spreading Christianity"],
    rows=[["Set 1", "12", "9", "6", "4"],
          ["Set 2", "12", "7", "8", "3"],
          ["Set 3", "12", "5", "4", "7"]])

_T_ORDER = dict(
    headers=["Statement a student proposes (illustrative)",
             "Does the framework place it among the CAUSES of the efforts, or among the "
             "RESULTS of contact?"],
    rows=[["A search for new sources of wealth", "Cause"],
          ["Economic and military competition among European nations", "Cause"],
          ["The Columbian Exchange", "Result"],
          ["Extensive demographic, economic, and social changes", "Result"]])

QUESTIONS = [

 dict(q="Unit 1's Learning Objective C asks students to explain the causes of what, by "
        "whom?",
      choices=[
        "Exploration and conquest of the New World by various European nations",
        "Migration and settlement across North America by native populations",
        "The Columbian Exchange between the hemispheres",
        "The development of the caste system in the Spanish colonial empire",
        "The growth of English settlement along the Atlantic seaboard"],
      ans=0,
      why="Unit 1 Learning Objective C reads 'Explain the causes of exploration and "
          "conquest of the New World by various European nations.' Native migration is "
          "Learning Objective B's subject, the Columbian Exchange and the caste system "
          "belong to KC-1.2.I.B and KC-1.2.II.D under later objectives of this unit, and "
          "English settlement belongs to Period 2."),

 dict(q="KC-1.2.I.A names three things from which European efforts to explore and conquer "
        "the New World stemmed. Which set names all three?",
      choices=[
        "A search for new sources of wealth, economic and military competition, and a "
        "desire to spread Christianity",
        "A search for new sources of wealth, improvements in maritime technology, and a "
        "desire to spread Christianity",
        "Economic and military competition, population pressure at home, and a desire to "
        "spread Christianity",
        "A search for new sources of wealth, economic and military competition, and the "
        "introduction of new crops",
        "A desire to spread Christianity, the shift from feudalism to capitalism, and "
        "epidemic disease"],
      ans=0,
      why="KC-1.2.I.A states that European nations' efforts to explore and conquer the New "
          "World stemmed from a search for new sources of wealth, economic and military "
          "competition, and a desire to spread Christianity. Maritime technology and the "
          "shift from feudalism to capitalism belong to KC-1.2.I.C and KC-1.2.I.B, new "
          "crops and epidemic disease to KC-1.2.II.A, and population pressure is not in "
          "the framework at all."),

 dict(q="KC-1.2.I.A says the efforts STEMMED FROM those three things. What kind of claim "
        "does that verb make?",
      choices=[
        "A causal claim, that the three named things gave rise to the efforts",
        "A claim about what the efforts produced once they were under way",
        "A claim that the three named things occurred at the same moment as the efforts "
        "and had no bearing on them",
        "A claim about the order in which European nations reached the Americas",
        "A claim that the efforts had no identifiable causes"],
      ans=0,
      why="KC-1.2.I.A puts the three named things behind the efforts rather than after "
          "them, which is a statement of cause, and Unit 1 Learning Objective C asks "
          "students for exactly the causes of exploration and conquest. What the efforts "
          "produced is the subject of KC-1.2 and KC-1.2.II, which describe results, and "
          "nothing in the sentence concerns the sequence of arrivals."),

 dict(q="A hypothetical petition to a crown, its author unnamed, argues that a proposed "
        "voyage should be funded because the lands beyond the ocean are reported to hold "
        "gold and silver in quantity. Which of KC-1.2.I.A's three causes does it "
        "illustrate?",
      choices=[
        "The search for new sources of wealth",
        "Economic and military competition among European nations",
        "The desire to spread Christianity",
        "The improvement of maritime technology",
        "The growth of joint-stock companies"],
      ans=0,
      why="KC-1.2.I.A names a search for new sources of wealth as the first of the three "
          "causes, and a petition resting on reported gold and silver is that search "
          "stated plainly. The petition says nothing about a rival crown or about "
          "religion, which are the sentence's other two causes, and maritime technology "
          "and joint-stock companies belong to KC-1.2.I.C rather than to the causes of "
          "the efforts."),

 dict(q="Suppose an illustrative dispatch, its author unnamed, warns a court that a "
        "neighbouring kingdom is fitting out ships and will claim the coast first unless "
        "the court acts. Which of KC-1.2.I.A's causes does it illustrate?",
      choices=[
        "Economic and military competition among European nations",
        "The search for new sources of wealth",
        "The desire to spread Christianity",
        "The Columbian Exchange between the hemispheres",
        "The shift from feudalism to capitalism"],
      ans=0,
      why="KC-1.2.I.A names economic and military competition as the second of its three "
          "causes, and a warning that a rival kingdom will act first is that competition "
          "in its plainest form. No wealth is named as the object and no religious purpose "
          "is stated, and the Columbian Exchange and the shift from feudalism to "
          "capitalism are KC-1.2's and KC-1.2.I.B's material rather than causes of the "
          "efforts."),

 dict(q="A hypothetical letter to a religious order, its author unnamed, urges that "
        "priests be sent with the next fleet so that the peoples across the ocean may be "
        "brought to the Christian faith. Which of KC-1.2.I.A's causes does it illustrate?",
      choices=[
        "The desire to spread Christianity",
        "The search for new sources of wealth",
        "Economic and military competition among European nations",
        "The desire to record the customs of other peoples",
        "The desire to establish permanent agricultural settlement"],
      ans=0,
      why="KC-1.2.I.A names a desire to spread Christianity as the third of its three "
          "causes, and a request for priests to carry the faith across the ocean is that "
          "desire directly. The letter names no wealth and no rival power, and neither "
          "recording customs nor founding farms appears among the causes the sentence "
          "gives."),

 dict(q="An illustrative royal instruction, its author unnamed, reserves to the crown a "
        "share of any precious metals found and requires that a priest sail with every "
        "ship. Which two of KC-1.2.I.A's three causes does it combine?",
      choices=[
        "The search for new sources of wealth and the desire to spread Christianity",
        "The search for new sources of wealth and economic and military competition",
        "Economic and military competition and the desire to spread Christianity",
        "The desire to spread Christianity and the improvement of maritime technology",
        "Economic and military competition and the introduction of new crops"],
      ans=0,
      why="KC-1.2.I.A's three causes are a search for new sources of wealth, economic and "
          "military competition, and a desire to spread Christianity. Reserving a share of "
          "precious metals is the first and requiring a priest aboard is the third; no "
          "rival power is mentioned, so the competition cause is absent. Maritime "
          "technology and new crops belong to KC-1.2.I.C and KC-1.2.II.A."),

 dict(q="Learning Objective C asks for the causes of exploration AND CONQUEST. What does "
        "including the second word do to the objective's scope?",
      choices=[
        "It extends the question beyond first voyages to the taking of territory and "
        "peoples that followed them",
        "It restricts the question to voyages that turned back without landing",
        "It restricts the question to a single European nation",
        "It makes the objective a question about results rather than about causes",
        "It removes religion from the causes to be considered"],
      ans=0,
      why="Unit 1 Learning Objective C reads 'the causes of exploration and conquest of "
          "the New World by various European nations', so both the voyages and what "
          "followed them fall inside the question, and KC-1.2.I.A uses the same pair of "
          "words for the efforts whose causes it names. The objective says causes rather "
          "than results, it says various nations rather than one, and KC-1.2.I.A keeps "
          "the desire to spread Christianity among the causes."),

 dict(q="What does the phrase VARIOUS EUROPEAN NATIONS, as Learning Objective C uses it, "
        "rule out?",
      choices=[
        "An account that treats exploration and conquest as the work of a single European "
        "power",
        "An account that treats exploration and conquest as having more than one cause",
        "An account that includes religious motives among the causes",
        "An account that mentions competition between European powers",
        "An account that places the efforts before 1607"],
      ans=0,
      why="Unit 1 Learning Objective C asks about exploration and conquest by various "
          "European nations, and KC-1.2.I.A likewise writes of European nations in the "
          "plural, so a one-power account is the one the wording excludes. Multiple causes "
          "and religious motives are what KC-1.2.I.A supplies, competition between powers "
          "requires more than one power rather than fewer, and the objective's own period "
          "runs from 1491 to 1607."),

 dict(q="KC-1.2.I.A names competition of two kinds among the causes. Which two does the "
        "sentence name?",
      choices=[
        "Economic and military",
        "Economic and religious",
        "Military and dynastic",
        "Religious and cultural",
        "Military and legal"],
      ans=0,
      why="KC-1.2.I.A names economic and military competition. Religion enters the "
          "sentence as a separate cause, the desire to spread Christianity, rather than as "
          "a kind of competition, and dynastic, cultural and legal competition appear "
          "nowhere in it. KC-1.2.I does name religious competition, but as something "
          "European expansion generated within European societies rather than as a cause "
          "of the efforts."),

 dict(q="Why does the framework list a search for new sources of wealth separately from "
        "economic competition, when both concern money?",
      choices=[
        "Because one is a pursuit of something not yet held and the other is a contest "
        "with rival powers, and KC-1.2.I.A names them as separate causes",
        "Because the framework treats the search for wealth as a result rather than a "
        "cause",
        "Because economic competition is described as occurring only after 1607",
        "Because the search for wealth is described as a religious motive",
        "Because the framework names economic competition only among native societies"],
      ans=0,
      why="KC-1.2.I.A's list has three items, and a search for new sources of wealth "
          "stands beside economic and military competition rather than inside it, so the "
          "framework distinguishes seeking a new source from contending with a rival for "
          "one. Both are named as causes rather than results, the sentence gives no date "
          "for either, and the competition it names is among European nations."),

 dict(q="Using the table of hypothetical document sets, which conclusion do the counts "
        "support?",
      table=_T_MOTIVES,
      choices=[
        "All three of the motives KC-1.2.I.A names appear in every set, and no single "
        "motive leads in all three sets",
        "Only one of the three motives appears anywhere in these sets",
        "The search for new wealth is mentioned in more documents than either other motive "
        "in every set",
        "Rivalry with another European crown is mentioned in none of the sets",
        "Every document in every set mentions all three motives"],
      ans=0,
      why="Read from the table alone: each of the three motive columns is above zero in "
          "every set, and the leading motive changes from set to set, so no one motive "
          "leads throughout. Those three motives are the three causes KC-1.2.I.A names, "
          "and the sentence itself puts them side by side without ranking them. If every "
          "document mentioned all three, each motive column would equal the documents "
          "column, which none of them does."),

 dict(q="Using the same table of hypothetical document sets, which claim goes BEYOND what "
        "the counts can support?",
      table=_T_MOTIVES,
      choices=[
        "That the crowns funding these voyages judged one motive more important than the "
        "others",
        "That every set contains the same number of documents",
        "That rivalry with another European crown is mentioned in more documents in the "
        "second set than in the third",
        "That spreading Christianity is mentioned in fewer documents than the search for "
        "new wealth in the first set",
        "That no motive is mentioned in more documents than the set contains"],
      ans=0,
      why="The table counts mentions and reports nothing about what anyone judged more "
          "important, so relative importance is the one claim of the five it cannot reach. "
          "The other four are read straight off the rows. KC-1.2.I.A names its three "
          "causes without ranking them either, and the framework's own task of weighing "
          "causes belongs to Reasoning Process 2 rather than to a count of mentions."),

 dict(q="According to KC-1.2.I, where did European expansion into the Western Hemisphere "
        "generate intense competition and change?",
      choices=[
        "Within European societies",
        "Within native societies alone",
        "Within West African societies alone",
        "Nowhere outside the territories that Europeans claimed",
        "Among European monarchs but not within their societies"],
      ans=0,
      why="KC-1.2.I states that European expansion into the Western Hemisphere generated "
          "intense social, religious, political, and economic competition and changes "
          "within European societies, and KC-1.2 makes the same point by placing "
          "significant change on both sides of the Atlantic Ocean. Confining the change to "
          "claimed territory contradicts both sentences, and the framework's word is "
          "societies rather than rulers, which is what makes the change social, religious "
          "and economic as well as political."),

 dict(q="Competition appears both in KC-1.2.I.A and in KC-1.2.I. What is the difference "
        "between the two appearances?",
      choices=[
        "In one it is named among the causes of the efforts to explore and conquer, and in "
        "the other among the things European expansion generated within European societies",
        "In one it is named among the causes of the efforts, and in the other among the "
        "causes of native migration",
        "In one it is described as economic only, and in the other as military only",
        "The two sentences make the same claim in the same words",
        "Neither sentence uses the word competition"],
      ans=0,
      why="KC-1.2.I.A puts economic and military competition behind the efforts to explore "
          "and conquer, while KC-1.2.I puts social, religious, political, and economic "
          "competition among what expansion generated within European societies, so the "
          "same word does duty as a cause in one sentence and as a consequence in the "
          "other. Native migration is KC-1.1's subject, and neither sentence is confined "
          "to one kind of competition."),

 dict(q="Which of the following is NOT among the causes KC-1.2.I.A gives for European "
        "efforts to explore and conquer the New World?",
      choices=[
        "The introduction of crops and animals not found in the Americas",
        "A search for new sources of wealth",
        "Economic competition among European nations",
        "Military competition among European nations",
        "A desire to spread Christianity"],
      ans=0,
      why="KC-1.2.I.A names a search for new sources of wealth, economic and military "
          "competition, and a desire to spread Christianity. The introduction of crops and "
          "animals not found in the Americas belongs to KC-1.2.II.A, which describes what "
          "accompanied and furthered Spanish exploration and conquest rather than what set "
          "the efforts going, so it sits on the other side of the causal relation Unit 1 "
          "Learning Objective C asks about."),

 dict(q="A hypothetical study guide lists the Columbian Exchange among the causes of "
        "European exploration. Which framework sentence shows that ordering to be "
        "reversed?",
      choices=[
        "KC-1.2, which places the Columbian Exchange among the results of contact among "
        "Europeans, Native Americans, and Africans",
        "KC-1.2.I.A, which names a search for new sources of wealth among the causes",
        "KC-1.2.I, which describes competition and changes within European societies",
        "Unit 1 Learning Objective C, which asks for the causes of exploration and conquest",
        "Unit 1 Learning Objective B, which concerns native populations and the natural "
        "environment"],
      ans=0,
      why="KC-1.2 states that contact among Europeans, Native Americans, and Africans "
          "RESULTED IN the Columbian Exchange, so the Exchange follows the voyages rather "
          "than preceding them. The remaining sentences are true but do not settle the "
          "ordering: KC-1.2.I.A and Learning Objective C concern the causes without "
          "mentioning the Exchange, KC-1.2.I concerns changes within Europe, and Learning "
          "Objective B concerns native populations."),

 dict(q="Using the table of proposed statements, which pair does the record place among "
        "the CAUSES of the efforts rather than among the results of contact?",
      table=_T_ORDER,
      choices=[
        "The search for new sources of wealth, and economic and military competition among "
        "European nations",
        "The Columbian Exchange, and extensive demographic, economic, and social changes",
        "The search for new sources of wealth, and the Columbian Exchange",
        "All four statements are placed among the causes",
        "None of the four statements is placed among the causes"],
      ans=0,
      why="Read from the table alone: exactly two rows are marked as causes, and they are "
          "the search for new sources of wealth and the competition among European "
          "nations, which are two of the three things KC-1.2.I.A says the efforts stemmed "
          "from. The two marked as results are the Columbian Exchange and the extensive "
          "demographic, economic, and social changes, which KC-1.2 and KC-1.2.II place "
          "after contact."),

 dict(q="The thematic focus printed on this topic page is America in the World. What does "
        "it state about interactions between empires, nations, and peoples?",
      choices=[
        "That diplomatic, economic, cultural, and military interactions shape the "
        "development of America and its increasingly important role in the world",
        "That such interactions had no bearing on the development of America before 1607",
        "That only military interactions shaped the development of America",
        "That America developed in isolation from other parts of the world",
        "That interactions between peoples are shaped by America but do not shape it"],
      ans=0,
      why="The America in the World thematic focus states that diplomatic, economic, "
          "cultural, and military interactions between empires, nations, and peoples shape "
          "the development of America and America's increasingly important role in the "
          "world, and Unit 1 Learning Objective C asks for the causes of the very "
          "interactions that opened it. KC-1.2.I.A's economic and military competition "
          "among European nations is an interaction of exactly that kind."),

 dict(q="The reasoning process printed for this topic in the unit outline is Causation. "
        "Which task does the framework's first description of that process name?",
      choices=[
        "Describing causes and/or effects of a specific historical development or process",
        "Describing similarities and/or differences between different historical "
        "developments or processes",
        "Describing patterns of continuity and/or change over time",
        "Identifying the evidence used in a source to support an argument",
        "Making a historically defensible claim"],
      ans=0,
      why="The framework's Reasoning Process 2, Causation, opens with describing causes "
          "and effects of a specific historical development or process, and Unit 1 "
          "Learning Objective C asks for exactly that about exploration and conquest. "
          "Similarities belong to Comparison and patterns over time to Continuity and "
          "Change, while the last two are historical thinking skills rather than reasoning "
          "processes."),

 dict(q="The framework's account of Causation distinguishes primary from secondary causes "
        "and short-term from long-term effects. What does that distinction ask a student "
        "to do with KC-1.2.I.A's three causes?",
      choices=[
        "Weigh them against one another rather than simply list them",
        "Discard any cause that cannot be dated precisely",
        "Treat the first cause named in the sentence as the primary one",
        "Treat all three as effects rather than as causes",
        "Choose only the cause that a source mentions most often"],
      ans=0,
      why="Reasoning Process 2 includes explaining the difference between primary and "
          "secondary causes and between short-term and long-term effects, which is a task "
          "of weighing rather than of listing, and KC-1.2.I.A supplies three causes "
          "without weighing them. The framework gives no dating requirement, does not "
          "present its list as a ranking, and calls the three causes rather than effects."),

 dict(q="Reasoning Process 2 also asks for the relative historical significance of "
        "different causes. What does the framework itself supply toward that judgement in "
        "this topic?",
      choices=[
        "The three causes, stated together and left unranked, so the weighing is the "
        "student's work",
        "A ranking of the three causes from most to least important",
        "A statement that the religious cause outweighed the other two",
        "A statement that the economic causes outweighed the religious one",
        "A statement that no cause can be weighed against another"],
      ans=0,
      why="KC-1.2.I.A names a search for new sources of wealth, economic and military "
          "competition, and a desire to spread Christianity in a single list and gives no "
          "order of importance among them, while Reasoning Process 2 makes explaining "
          "relative significance the student's task. Reading a ranking into the sentence, "
          "in either direction, adds something the framework does not say, and the "
          "reasoning process would be empty if no weighing were possible."),

 dict(q="A hypothetical revision guide states that the framework gives a single cause for "
        "European exploration. Why does the framework not support that?",
      choices=[
        "KC-1.2.I.A names three causes and joins them in one sentence",
        "KC-1.2.I.A names no causes at all",
        "KC-1.2.I.A names causes only for Spanish exploration",
        "KC-1.2.I.A treats exploration as having no European causes",
        "KC-1.2.I.A places all its causes after the voyages rather than before them"],
      ans=0,
      why="KC-1.2.I.A states that the efforts stemmed from a search for new sources of "
          "wealth, economic and military competition, and a desire to spread Christianity, "
          "which is three causes rather than one, and Unit 1 Learning Objective C asks "
          "about various European nations rather than about Spain alone. The sentence's "
          "verb places the causes behind the efforts, not after them."),

 dict(q="A hypothetical essay explains European exploration by population pressure at "
        "home, a cause the framework does not name. What is the correct thing to say about "
        "that explanation, from the framework alone?",
      choices=[
        "The framework neither asserts nor denies it, so it cannot be used as an answer "
        "traceable to the course content",
        "The framework names it as a fourth cause alongside the other three",
        "The framework states that it was the most important cause",
        "The framework states that population in Europe was falling",
        "The framework rules it out as a cause of any European development"],
      ans=0,
      why="KC-1.2.I.A names a search for new sources of wealth, economic and military "
          "competition, and a desire to spread Christianity, and says nothing whatever "
          "about population, so the framework neither supports nor contradicts the claim. "
          "Unit 1 Learning Objective C asks students to explain the causes the course "
          "content supplies, and treating an unstated cause as asserted, denied or ranked "
          "would all put words into the sentence."),

 dict(q="What does KC-1.2.I.A's subject, the EFFORTS of European nations to explore and "
        "conquer, tell a reader about what the sentence is a claim about?",
      choices=[
        "It is a claim about why those nations undertook the voyages, not about how the "
        "voyages turned out",
        "It is a claim about how many voyages each nation sent",
        "It is a claim about what the voyages found on arrival",
        "It is a claim about the technology the voyages used",
        "It is a claim about the peoples the voyagers encountered"],
      ans=0,
      why="KC-1.2.I.A puts three motives behind the efforts themselves, so the sentence "
          "concerns the undertaking rather than its outcome, which is what Unit 1 Learning "
          "Objective C means by causes. Numbers of voyages appear nowhere in the sentence; "
          "what was found and whom the voyagers met belong to KC-1.2.II and KC-1.2.III, "
          "and the technology to KC-1.2.I.C."),

 dict(q="The framework prints a note that events, processes, and developments are not "
        "constrained by the given dates. How does that note bear on a question about the "
        "causes of exploration?",
      choices=[
        "The causes may lie before the period's opening date without falling outside the "
        "framework's account",
        "The causes must all be dated within the period's opening and closing years",
        "The note applies only to the results of exploration, never to its causes",
        "The note means the framework assigns no dates to any unit",
        "The note means the causes of exploration cannot be studied at all"],
      ans=0,
      why="The framework states that events, processes, and developments are not "
          "constrained by the given dates and may begin before, or continue after, the "
          "approximate dates assigned to each unit and topic, so a cause of the efforts "
          "KC-1.2.I.A describes may predate 1491 without leaving the account. The note is "
          "general rather than limited to results, and the framework does assign "
          "approximate dates, which is why it calls them approximate."),

 dict(q="How does the desire to spread Christianity sit alongside the two worldly causes "
        "in KC-1.2.I.A's list?",
      choices=[
        "As a third cause of the same standing, so the framework's account of motive is "
        "not purely material",
        "As a consequence of the other two rather than a cause in its own right",
        "As a motive the framework describes as less important than the other two",
        "As a motive the framework confines to a single European nation",
        "As a motive the framework places after conquest rather than before it"],
      ans=0,
      why="KC-1.2.I.A joins a desire to spread Christianity to a search for new sources of "
          "wealth and to economic and military competition in one list of what the efforts "
          "stemmed from, giving no order among them, so the religious motive is a cause "
          "beside the others rather than beneath or after them. Unit 1 Learning Objective C "
          "speaks of various European nations rather than one."),

 dict(q="Which framework sentence would most directly contradict a claim that European "
        "expansion left European societies as they had been?",
      choices=[
        "KC-1.2.I, which says expansion generated intense competition and changes within "
        "European societies",
        "KC-1.2.I.A, which names the causes from which the efforts stemmed",
        "KC-1.2.II, which describes demographic, economic, and social changes following "
        "the Exchange and the Spanish Empire's growth",
        "Unit 1 Learning Objective C, which asks for the causes of exploration and conquest",
        "The America in the World thematic focus, which describes interactions between "
        "peoples"],
      ans=0,
      why="KC-1.2.I locates intense social, religious, political, and economic competition "
          "and changes WITHIN European societies, which is exactly what the claim denies, "
          "and KC-1.2 makes the same point with changes on both sides of the Atlantic "
          "Ocean. KC-1.2.I.A and Learning Objective C concern causes rather than "
          "consequences, and KC-1.2.II's changes are not located inside Europe by that "
          "sentence."),

 dict(q="What would be wrong with treating KC-1.2.I.A's three causes as a sequence in "
        "which one followed another?",
      choices=[
        "The sentence joins them as things the efforts stemmed from together, and asserts "
        "no order among them",
        "The sentence explicitly states that they occurred in the order given",
        "The sentence names only two causes, so no sequence is possible",
        "The sentence places all three causes after the voyages",
        "The sentence attributes each cause to a different European nation"],
      ans=0,
      why="KC-1.2.I.A writes that the efforts stemmed from a search for new sources of "
          "wealth, economic and military competition, and a desire to spread Christianity, "
          "which is a list of three joined together rather than a chronology, and nothing "
          "in it assigns a cause to a particular nation or places any of them after the "
          "voyages. Unit 1 Learning Objective C speaks of various European nations in the "
          "plural throughout."),

 dict(q="Which single sentence states what this topic's Required Course Content says, "
        "without adding to it?",
      choices=[
        "European nations set out to explore and conquer the New World because they sought "
        "new sources of wealth, contended with one another economically and militarily, "
        "and wished to spread Christianity",
        "European nations set out to explore the New World once improvements in maritime "
        "technology made the voyage possible",
        "European nations set out to conquer the New World in order to bring back crops "
        "and animals unknown in Europe",
        "European nations set out to explore the New World in response to epidemics at home",
        "A single European nation set out to explore the New World in search of wealth, and "
        "the others followed"],
      ans=0,
      why="The first is KC-1.2.I.A in the framework's own terms and adds nothing: a search "
          "for new sources of wealth, economic and military competition, and a desire to "
          "spread Christianity. Maritime technology belongs to KC-1.2.I.C and the crops "
          "and animals to KC-1.2.II.A, neither of which the framework gives as a cause; "
          "epidemics appear as an accompaniment of conquest in the Americas rather than as "
          "a European motive, and Unit 1 Learning Objective C speaks of various nations."),
]
