# AP U.S. HISTORY 3.1 Contextualizing Period 3  (title copied from US_HISTORY_topics.json)
# Unit 3, Period 3: 1754 to 1800. Suggested skill 4.A, identify and describe a historical
# context for a specific historical development or process. Reasoning process printed for
# this topic in UNIT AT A GLANCE: Continuity and Change.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words. The
# text below was read off the topic page and the unit's PREVIEW tables; where the two
# column layout ran words together in the extraction the spacing has been restored and
# nothing else.
#
#   Unit 3: Learning Objective A
#       Explain the context in which America gained independence and developed a sense of
#       national identity.
#
#   PREVIEW: UNIT 3 KEY CONCEPTS  (printed under that heading on this topic's page)
#
#   KC-3.1        British attempts to assert tighter control over its North American
#                 colonies and the colonial resolve to pursue self-government led to a
#                 colonial independence movement and the Revolutionary War.
#   KC-3.1.I      The competition among the British, French, and American Indians for
#                 economic and political advantage in North America culminated in the
#                 Seven Years' War (the French and Indian War), in which Britain defeated
#                 France and allied American Indians.
#   KC-3.1.II     The desire of many colonists to assert ideals of self-government in the
#                 face of renewed British imperial efforts led to a colonial independence
#                 movement and war with Britain.
#   KC-3.2        The American Revolution's democratic and republican ideals inspired new
#                 experiments with different forms of government.
#   KC-3.2.I      The ideals that inspired the revolutionary cause reflected new beliefs
#                 about politics, religion, and society that had been developing over the
#                 course of the 18th century.
#   KC-3.2.II     After declaring independence, American political leaders created new
#                 constitutions and declarations of rights that articulated the role of the
#                 state and federal governments while protecting individual liberties and
#                 limiting both centralized power and excessive popular influence.
#   KC-3.2.III.i  New forms of national culture and political institutions developed in the
#                 United States alongside continued regional variations and differences over
#                 economic, political, social, and foreign policy issues.
#   KC-3.3        Migration within North America and competition over resources, boundaries,
#                 and trade intensified conflicts among peoples and nations.
#   KC-3.3.I      In the decades after American independence, interactions among different
#                 groups resulted in competition for resources, shifting alliances, and
#                 cultural blending.
#   KC-3.3.II     The continued presence of European powers in North America challenged the
#                 United States to find ways to safeguard its borders, maintain neutral
#                 trading rights, and promote its economic interests.
#
#   The topic page's own instruction, in its own words: "Spend a class period helping
#   students understand some contexts for this unit. Considering this unit's key concepts
#   (previewed below), select one or two for which your students will most need context."
#   And on what context is: students could examine "Change from and/or continuity with
#   preceding historical developments" and "Similarities and/or differences with
#   contemporaneous historical developments in different regions or geographical areas."
#
#   The optional activity printed on this same page: it tells the teacher to note that
#   "the two main historical developments that will be covered in this unit are the
#   American Revolution and the creation of the U.S. Constitution", and to show students
#   AP European History's Unit 4 and AP World History's Unit 5 while highlighting that
#   the Enlightenment is a key topic in all three courses.
#
# WHAT IS NOT KEYED, DELIBERATELY. 3.1 is a CONTEXTUALIZING topic and its Required Course
# Content is a PREVIEW of the unit's key concepts, not the detail behind them. The lettered
# sub-points -- KC-3.1.I.A through KC-3.3.II.C -- are printed on the pages of topics 3.2
# through 3.12, which own them. So no key here names a tax, an act, a battle, a convention,
# a political party, a founder or a treaty. What the preview itself names is fair: the
# Seven Years' War, the Revolutionary War, Britain, France and American Indians all appear
# in KC-3.1 and KC-3.1.I, so they are preview content rather than a reach into 3.2.
# `no_period_detail` in the verifier enforces exactly that boundary, and several items
# exist to test it.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=.
# PROSE ONLY: no LaTeX; a span of years is written "1754 to 1800", never with a hyphen.
# FIVE choices (A-E). Any invented source is marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("3.1", "Contextualizing Period 3", 3)

_T_PREVIEW = dict(
    headers=["Previewed key concept",
             "Roman-numeral sub-points printed beneath it in the preview"],
    rows=[["KC-3.1", "2"],
          ["KC-3.2", "3"],
          ["KC-3.3", "2"]])

_T_APPROACH = dict(
    headers=["Statement offered as context for this unit (illustrative)",
             "Where it stands in relation to Period 3"],
    rows=[["Colonial traditions of self-government had been forming before 1754",
           "Preceding"],
          ["Enlightenment ideas were being argued over in Europe during these same decades",
           "Contemporaneous, in a different region"],
          ["New states were admitted west of the mountains long after 1848",
           "Later than the period"],
          ["British and French rivalry in North America had begun well before 1754",
           "Preceding"]])

_T_SPAN = dict(
    headers=["Period as the framework numbers it", "First year of the span",
             "Last year of the span"],
    rows=[["Period 2", "1607", "1754"],
          ["Period 3", "1754", "1800"],
          ["Period 4", "1800", "1848"]])

QUESTIONS = [

 dict(q="Unit 3's Learning Objective A asks students to explain the context for one thing "
        "in particular. Which of the following does the framework name?",
      choices=[
        "The context in which America gained independence and developed a sense of national "
        "identity",
        "The causes and effects of the Seven Years' War",
        "The differing ideological positions on the structure and function of the federal "
        "government",
        "The continuities and changes in American culture from 1754 to 1800",
        "How and why migration and immigration to and within North America caused competition "
        "and conflict over time"],
      ans=0,
      why="Unit 3: Learning Objective A reads 'Explain the context in which America gained "
          "independence and developed a sense of national identity.' The other four are real "
          "learning objectives of this same unit, printed on the pages of later topics, which "
          "is what makes them the tempting wrong answers rather than obviously false ones."),

 dict(q="The framework gives Period 3 a span of years, printed at the head of every page of "
        "the unit. Which span is it?",
      choices=[
        "1754 to 1800",
        "1607 to 1754",
        "1800 to 1848",
        "1763 to 1789",
        "1775 to 1783"],
      ans=0,
      why="The unit is titled Period 3: 1754 to 1800, and Unit 3: Learning Objective A asks "
          "for the context of the independence and national identity that develop inside it. "
          "1607 to 1754 is Period 2 and 1800 to 1848 is Period 4; the remaining two spans are "
          "not part of the framework's periodisation at all."),

 dict(q="According to KC-3.1, which two things together led to a colonial independence "
        "movement and the Revolutionary War?",
      choices=[
        "British attempts to assert tighter control over the North American colonies, and the "
        "colonial resolve to pursue self-government",
        "British withdrawal from North America, and colonial indifference to imperial policy",
        "A settled agreement between Britain and the colonies over taxation, and a shared "
        "imperial defence policy",
        "The collapse of colonial assemblies, and the transfer of colonial trade to France",
        "Colonial demands for closer union with Britain, and imperial reluctance to grant it"],
      ans=0,
      why="KC-3.1 states that British attempts to assert tighter control over its North "
          "American colonies AND the colonial resolve to pursue self-government led to a "
          "colonial independence movement and the Revolutionary War. The sentence names a "
          "push from one side and a resolve from the other; withdrawal, indifference, "
          "agreement, collapse and a demand for closer union each contradict one half of it."),

 dict(q="KC-3.1.I names the parties whose competition culminated in the Seven Years' War. "
        "Which group does the framework name, and over what?",
      choices=[
        "The British, the French and American Indians, competing for economic and political "
        "advantage in North America",
        "The British, the Spanish and the Dutch, competing for control of the Atlantic fisheries",
        "The French, the Spanish and American Indians, competing for religious authority in "
        "the interior",
        "The British and the French alone, competing over the terms of a European succession",
        "The British, the French and the Spanish, competing for naval supremacy in the "
        "Caribbean"],
      ans=0,
      why="KC-3.1.I states that the competition among the British, French, and American "
          "Indians for economic and political advantage in North America culminated in the "
          "Seven Years' War. Substituting the Spanish or the Dutch for American Indians, or "
          "reducing the contest to two European powers, changes the framework's own list, and "
          "no other object of the competition is named in that sentence."),

 dict(q="KC-3.1.I states an outcome for the Seven Years' War. Which statement matches it?",
      choices=[
        "Britain defeated France and allied American Indians",
        "France defeated Britain and allied American Indians",
        "The war ended without a victor, leaving the previous boundaries in place",
        "American Indian nations defeated both European powers and expelled them from the "
        "interior",
        "Britain and France divided North America between them by prior agreement"],
      ans=0,
      why="KC-3.1.I ends with the words 'in which Britain defeated France and allied American "
          "Indians'. The reversed version keeps every noun and swaps the victor, which is the "
          "likeliest way to misremember the sentence; a drawn war, an American Indian victory "
          "and a prior partition are each contradicted by it."),

 dict(q="What does KC-3.1.II give as the desire that led to a colonial independence movement "
        "and war with Britain?",
      choices=[
        "The desire of many colonists to assert ideals of self-government in the face of "
        "renewed British imperial efforts",
        "The desire of British ministers to be rid of colonies they judged unprofitable",
        "The desire of the colonies to join the French empire in North America",
        "The desire of colonial merchants to end all trade across the Atlantic",
        "The desire of a small group of colonists to restore hereditary rule in America"],
      ans=0,
      why="KC-3.1.II states that the desire of many colonists to assert ideals of "
          "self-government in the face of renewed British imperial efforts led to a colonial "
          "independence movement and war with Britain. The framework attributes the desire to "
          "colonists and describes it as a response to renewed imperial effort, so a desire "
          "located in London, in an alternative empire, in ending trade or in hereditary rule "
          "is not the sentence's claim."),

 dict(q="KC-3.2 connects the American Revolution's ideals to something that followed from "
        "them. Which connection does the framework make?",
      choices=[
        "Its democratic and republican ideals inspired new experiments with different forms of "
        "government",
        "Its ideals were set aside once the fighting ended, leaving colonial forms of "
        "government untouched",
        "Its ideals produced a single form of government adopted uniformly everywhere",
        "Its ideals were confined to military organisation and had no effect on civil "
        "institutions",
        "Its ideals were imported from the states and had no source in the Revolution itself"],
      ans=0,
      why="KC-3.2 reads that the American Revolution's democratic and republican ideals "
          "inspired new experiments with different forms of government. The word EXPERIMENTS, "
          "in the plural, and the phrase DIFFERENT FORMS are what rule out both a single "
          "uniform outcome and an absence of effect, and the sentence makes the ideals the "
          "source rather than the borrowing."),

 dict(q="KC-3.2.I says something about where the ideals that inspired the revolutionary cause "
        "came from. What does it say?",
      choices=[
        "They reflected new beliefs about politics, religion, and society that had been "
        "developing over the course of the 18th century",
        "They appeared suddenly in the year independence was declared and had no earlier history",
        "They were beliefs about military discipline rather than about politics or religion",
        "They were unchanged inheritances from the previous century, with nothing new in them",
        "They were beliefs held only by those who wrote the new constitutions"],
      ans=0,
      why="KC-3.2.I states that the ideals that inspired the revolutionary cause reflected new "
          "beliefs about politics, religion, and society that had been developing over the "
          "course of the 18th century. The sentence calls the beliefs NEW and also says they "
          "had been DEVELOPING, so neither a sudden appearance nor an unchanged inheritance "
          "matches it, and the three subjects it names are not military."),

 dict(q="KC-3.2.II describes what the new constitutions and declarations of rights did. Which "
        "pair of limits does the framework say they imposed?",
      choices=[
        "They limited both centralized power and excessive popular influence",
        "They limited centralized power while placing no limit on popular influence",
        "They limited popular influence while placing no limit on centralized power",
        "They removed limits of every kind in order to speed the conduct of the war",
        "They limited the authority of the states while leaving the federal government "
        "unrestrained"],
      ans=0,
      why="KC-3.2.II states that the new constitutions and declarations of rights articulated "
          "the role of the state and federal governments while protecting individual liberties "
          "and limiting BOTH centralized power AND excessive popular influence. A student who "
          "keeps only one of the two limits has half the sentence, which is why the two "
          "one-sided readings are offered; the sentence removes no limits and does not confine "
          "its restraint to the states."),

 dict(q="According to KC-3.2.III.i, what accompanied the development of new forms of national "
        "culture and political institutions in the United States?",
      choices=[
        "Continued regional variations and differences over economic, political, social, and "
        "foreign policy issues",
        "The disappearance of regional differences as national institutions took hold",
        "Agreement on foreign policy, with disagreement confined to economic questions",
        "A single national culture that replaced every earlier regional culture",
        "The absence of any national political institutions at all in this period"],
      ans=0,
      why="KC-3.2.III.i states that new forms of national culture and political institutions "
          "developed in the United States ALONGSIDE continued regional variations and "
          "differences over economic, political, social, and foreign policy issues. The word "
          "alongside makes the two simultaneous rather than sequential, and the sentence lists "
          "foreign policy among the matters in dispute."),

 dict(q="KC-3.3 identifies what intensified conflicts among peoples and nations. Which "
        "statement gives the framework's answer?",
      choices=[
        "Migration within North America, together with competition over resources, boundaries, "
        "and trade",
        "Migration into North America from Europe alone, with no internal movement involved",
        "Competition over religious authority, which the framework treats as the sole cause",
        "The withdrawal of European powers, which left rival claims unresolved",
        "A decline in trade, which reduced the value of the contested territory"],
      ans=0,
      why="KC-3.3 states that migration WITHIN North America and competition over resources, "
          "boundaries, and trade intensified conflicts among peoples and nations. The sentence "
          "names internal movement rather than transatlantic arrival, names three objects of "
          "competition rather than religious authority, and describes competition intensifying "
          "rather than trade declining. KC-3.3.II says European powers continued to be present."),

 dict(q="KC-3.3.I says that interactions among different groups produced three results. Which "
        "set names all three?",
      choices=[
        "Competition for resources, shifting alliances, and cultural blending",
        "Competition for resources, permanent alliances, and cultural separation",
        "Religious conversion, population decline, and the end of trade",
        "Shifting alliances, uniform law, and the disappearance of frontier settlement",
        "Cultural blending, fixed boundaries, and an end to competition"],
      ans=0,
      why="KC-3.3.I states that in the decades after American independence, interactions among "
          "different groups resulted in competition for resources, shifting alliances, and "
          "cultural blending. Cultural blending is the item a student is likeliest to drop, "
          "and alliances that SHIFT are the opposite of permanent ones, so the alternatives "
          "each replace a term of the framework's own triple."),

 dict(q="KC-3.3.II names three things the continued presence of European powers challenged the "
        "United States to do. Which set names them?",
      choices=[
        "Safeguard its borders, maintain neutral trading rights, and promote its economic "
        "interests",
        "Safeguard its borders, raise a standing army, and establish a state church",
        "Maintain neutral trading rights, abolish the states, and close its western lands",
        "Promote its economic interests, join a European alliance, and end its own trade",
        "Safeguard its borders, and nothing further, since trade was not yet a national concern"],
      ans=0,
      why="KC-3.3.II states that the continued presence of European powers in North America "
          "challenged the United States to find ways to safeguard its borders, maintain "
          "neutral trading rights, and promote its economic interests. A standing army, a "
          "state church, abolishing the states, closing western lands and joining a European "
          "alliance are not in that sentence, and the framework names trade explicitly."),

 dict(q="This topic page prints a suggested skill for students to practise. Which skill "
        "statement is it?",
      choices=[
        "Identify and describe a historical context for a specific historical development or "
        "process",
        "Explain a historical concept, development, or process",
        "Identify a source's point of view, purpose, historical situation, and audience",
        "Identify patterns among or connections between historical developments and processes",
        "Support an argument using specific and relevant evidence"],
      ans=0,
      why="The suggested skill printed beside this topic's title is 4.A, identify and describe "
          "a historical context for a specific historical development or process, and it is "
          "the skill Unit 3: Learning Objective A asks students to apply. The other four are "
          "skills 1.B, 2.A, 5.A and 6.B, each printed on other topic pages of this same unit."),

 dict(q="In the unit's own table of topics, each topic is assigned a reasoning process. Which "
        "one is assigned to this topic?",
      choices=[
        "Continuity and Change",
        "Causation",
        "Comparison",
        "Contextualization",
        "Argumentation"],
      ans=0,
      why="The unit's topic table assigns Continuity and Change to this topic, which fits "
          "Unit 3: Learning Objective A asking for the context in which America gained "
          "independence. Causation and Comparison are the reasoning processes assigned to "
          "other topics of this unit, while Contextualization and Argumentation are skill "
          "categories rather than reasoning processes."),

 dict(q="The page tells students two ways they could examine context. Which pair does it give?",
      choices=[
        "Change from or continuity with preceding historical developments, and similarities or "
        "differences with contemporaneous historical developments in different regions or "
        "geographical areas",
        "The intentions of the people involved, and the consequences that followed for them",
        "The reliability of a source, and the audience for which it was written",
        "The order in which events occurred, and the length of time between them",
        "The number of people affected, and the territory over which the effects were felt"],
      ans=0,
      why="The topic page lists exactly two approaches under its instruction on context: "
          "change from and/or continuity with preceding historical developments, and "
          "similarities and/or differences with contemporaneous historical developments in "
          "different regions or geographical areas. Unit 3: Learning Objective A is what those "
          "two approaches are meant to serve. Intention, reliability, sequence and scale are "
          "historical questions the page does not put under this heading."),

 dict(q="This page directs the teacher to do something specific with the previewed key "
        "concepts rather than to cover all of them. What is the direction?",
      choices=[
        "Select one or two of the previewed key concepts for which students will most need "
        "context",
        "Teach every previewed key concept in full before the unit begins",
        "Postpone all of the previewed key concepts until the end of the unit",
        "Replace the previewed key concepts with material drawn from another course",
        "Assign the previewed key concepts as reading without discussing any of them"],
      ans=0,
      why="The topic page reads: considering this unit's key concepts, previewed below, select "
          "one or two for which your students will most need context. That direction is what "
          "makes this a contextualizing topic rather than a survey of the unit, and it is why "
          "the detail behind Unit 3: Learning Objective A's key concepts belongs to the later "
          "topics that own the lettered sub-points."),

 dict(q="The activity printed on this page names the two main historical developments the unit "
        "will cover. Which pair does it name?",
      choices=[
        "The American Revolution and the creation of the U.S. Constitution",
        "The Seven Years' War and the settlement of the western interior",
        "The Columbian Exchange and the growth of the Atlantic trade",
        "The American Revolution and the abolition of slavery throughout the United States",
        "The creation of the U.S. Constitution and the opening of the Pacific coast"],
      ans=0,
      why="The optional activity on this topic page tells the teacher to note that the two "
          "main historical developments covered in this unit are the American Revolution and "
          "the creation of the U.S. Constitution, which is the pair Unit 3: Learning Objective "
          "A asks students to contextualise. The remaining options each substitute a "
          "development the page does not name in that sentence."),

 dict(q="The same activity has the teacher show students two other AP courses' unit outlines. "
        "What point is that comparison meant to establish?",
      choices=[
        "That the Enlightenment is a key topic in this course and in two other AP history "
        "courses at the same time",
        "That the American Revolution is studied only in this course",
        "That the other courses cover the same period under a different number",
        "That the Enlightenment belongs to the century after Period 3",
        "That the three courses disagree about when the period begins"],
      ans=0,
      why="The activity directs the teacher to display the outlines of AP European History's "
          "Unit 4 and AP World History's Unit 5 and to highlight that the Enlightenment is a "
          "key topic in all three courses. That is the topic page's own illustration of the "
          "second approach to context it names, contemporaneous developments in different "
          "regions, in the service of Unit 3: Learning Objective A."),

 dict(q="Using the table of previewed key concepts, which statement is supported by the record "
        "shown?",
      table=_T_PREVIEW,
      choices=[
        "One of the three previewed key concepts carries more sub-points than the other two, "
        "which carry the same number as each other",
        "All three previewed key concepts carry the same number of sub-points",
        "Each previewed key concept carries a different number of sub-points from the others",
        "One previewed key concept carries no sub-points at all",
        "The three previewed key concepts carry nine sub-points between them"],
      ans=0,
      why="Read from the table alone: the counts are two, three and two, so one concept "
          "carries more than the others and the remaining two are equal, and the three "
          "together carry seven rather than nine. KC-3.2 is the concept with three "
          "sub-points, and none of the three is without sub-points, so the framework's "
          "preview of Unit 3: Learning Objective A's key concepts is uneven rather than "
          "uniform."),

 dict(q="Using the table of proposed context statements, which row falls outside both of the "
        "approaches this topic page names?",
      table=_T_APPROACH,
      choices=[
        "The row marked as later than the period",
        "The row about Enlightenment argument in Europe",
        "The row about colonial traditions of self-government",
        "The row about British and French rivalry",
        "No row falls outside the two approaches"],
      ans=0,
      why="The topic page names preceding developments and contemporaneous developments in "
          "different regions. Read from the table alone, three rows are marked preceding or "
          "contemporaneous and exactly one is marked later than the period, so that row is the "
          "one neither approach reaches. Unit 3: Learning Objective A asks for the context IN "
          "WHICH the period's developments happened, which a later development cannot supply."),

 dict(q="Using the table of periods and years, what does the record show about how the "
        "framework marks off Period 3?",
      table=_T_SPAN,
      choices=[
        "It opens in the year the preceding period closes and closes in the year the following "
        "period opens, so the spans meet rather than leaving a gap",
        "It is separated from the preceding period by several years in which nothing is "
        "assigned",
        "It overlaps the preceding period by several years",
        "It is longer than the preceding period and shorter than the following one",
        "It shares no boundary year with either neighbouring period"],
      ans=0,
      why="Read from the table alone: the preceding period closes in the year this one opens "
          "and this one closes in the year the following period opens, so the spans abut. That "
          "is why the context Unit 3: Learning Objective A asks for reaches back into the "
          "preceding period rather than into an unassigned gap. The table also shows this "
          "period is the shortest of the three, so the length option fails on the same rows."),

 dict(q="A hypothetical revision guide states that this topic's Required Course Content "
        "supplies the detail of the debates over ratifying the Constitution. What is wrong "
        "with that statement?",
      choices=[
        "This topic's Required Course Content is printed as a PREVIEW of the unit's key "
        "concepts, and the detail belongs to the later topics of the unit",
        "The framework does not cover those debates anywhere in Unit 3",
        "Those debates belong to Period 4 rather than to Period 3",
        "The Required Course Content for this topic lists no key concepts at all",
        "The framework treats those debates as context rather than as content"],
      ans=0,
      why="This topic's Required Course Content sits under the heading PREVIEW: UNIT 3 KEY "
          "CONCEPTS and the page tells the teacher to select one or two of them for context, "
          "so the lettered detail is carried by the later topics that own it. KC-3.2.II is "
          "previewed here and does concern the new constitutions, so the unit certainly covers "
          "the material and does not defer it to another period, and the preview plainly lists "
          "key concepts."),

 dict(q="Of the previewed key concepts, which one is about movement and rival claims rather "
        "than about forms of government?",
      choices=[
        "KC-3.3, on migration within North America and competition over resources, boundaries, "
        "and trade",
        "KC-3.2, on democratic and republican ideals inspiring experiments in government",
        "KC-3.2.II, on new constitutions and declarations of rights",
        "KC-3.2.I, on beliefs about politics, religion, and society",
        "KC-3.1.II, on colonists asserting ideals of self-government"],
      ans=0,
      why="KC-3.3 is the previewed concept about migration and competition over resources, "
          "boundaries, and trade. The other four are all about ideals or about the forms of "
          "government they produced: KC-3.2 names the experiments, KC-3.2.II the new "
          "constitutions and declarations of rights, KC-3.2.I the beliefs behind the "
          "revolutionary cause and KC-3.1.II the assertion of self-government."),

 dict(q="Suppose a summary of KC-3.2.II says only that the new constitutions limited "
        "centralized power. Which half of the framework's sentence has it dropped?",
      choices=[
        "The limit on excessive popular influence, which the sentence places beside the limit "
        "on centralized power",
        "The protection of individual liberties, which the sentence does not mention",
        "The role of foreign governments, which the sentence assigns to the states",
        "The claim that the constitutions were written before independence was declared",
        "The claim that only the federal government was given a defined role"],
      ans=0,
      why="KC-3.2.II limits BOTH centralized power AND excessive popular influence, so a "
          "summary keeping only the first drops the second. The sentence does mention "
          "protecting individual liberties, does articulate the role of the state AND federal "
          "governments, and places all of this AFTER declaring independence, so the remaining "
          "options misdescribe the sentence rather than name what the summary lost."),

 dict(q="KC-3.3.I opens by locating its interactions in time. Where does the framework place "
        "them?",
      choices=[
        "In the decades after American independence",
        "In the decades before the Seven Years' War",
        "During the Revolutionary War itself and at no other time",
        "Across the whole of the 17th century",
        "Only after the period covered by this unit had ended"],
      ans=0,
      why="KC-3.3.I begins 'In the decades after American independence', which places the "
          "competition for resources, shifting alliances, and cultural blending it describes "
          "inside the later part of Period 3 rather than before the Seven Years' War, during "
          "the war alone, in the previous century, or beyond the period entirely."),

 dict(q="What does the word ALONGSIDE do in KC-3.2.III.i's account of national culture and "
        "regional variation?",
      choices=[
        "It makes the new national forms and the continuing regional variations simultaneous, "
        "so the first did not displace the second",
        "It makes the regional variations a consequence of the new national forms",
        "It makes the new national forms a later replacement for the regional variations",
        "It restricts the sentence to cultural matters and excludes political institutions",
        "It confines the differences it names to economic questions"],
      ans=0,
      why="KC-3.2.III.i says new forms of national culture and political institutions "
          "developed ALONGSIDE continued regional variations, which puts the two at the same "
          "time and denies displacement in either direction. The sentence names political "
          "institutions as well as culture, and lists economic, political, social, and foreign "
          "policy issues rather than economic ones alone."),

 dict(q="In KC-3.1.I, American Indians appear twice over. What are the two roles the sentence "
        "gives them?",
      choices=[
        "As competitors for advantage in their own right, and as allies defeated alongside "
        "France",
        "As competitors for advantage in their own right, and as the victors of the war",
        "As allies of Britain, and as the party that gained territory by the outcome",
        "As bystanders to the competition, and as parties to the peace that ended it",
        "As allies of France only, with no interest of their own in the competition"],
      ans=0,
      why="KC-3.1.I names the competition among the British, FRENCH, AND AMERICAN INDIANS for "
          "economic and political advantage, which makes American Indians one of the competing "
          "parties, and then ends 'in which Britain defeated France and allied American "
          "Indians', which makes them allies on the losing side. Holding only one of the two "
          "roles, or reversing the alliance or the outcome, misreads the same sentence."),

 dict(q="Which pairing correctly matches a previewed Unit 3 key concept with its subject?",
      choices=[
        "KC-3.1 with tighter British control and colonial self-government, and KC-3.3 with "
        "migration and competition over resources",
        "KC-3.1 with migration and competition over resources, and KC-3.3 with tighter British "
        "control and colonial self-government",
        "KC-3.1 with revolutionary ideals and new forms of government, and KC-3.2 with the "
        "continued presence of European powers",
        "KC-3.2 with migration within North America, and KC-3.3 with democratic and republican "
        "ideals",
        "All three previewed key concepts have the same subject, stated three times"],
      ans=0,
      why="KC-3.1 concerns British attempts at tighter control and the colonial resolve to "
          "pursue self-government; KC-3.3 concerns migration within North America and "
          "competition over resources, boundaries, and trade; KC-3.2 concerns the Revolution's "
          "ideals and the experiments in government they inspired. Every other pairing swaps "
          "two of those three subjects, and the preview states three distinct claims rather "
          "than one repeated."),

 dict(q="Which single sentence states the whole of what the framework previews for Unit 3 "
        "without adding to it?",
      choices=[
        "Tighter British control met colonial resolve to govern themselves and produced "
        "independence and war; the Revolution's ideals inspired experiments with different "
        "forms of government; and migration and competition over resources intensified "
        "conflicts among peoples and nations",
        "Britain lost a war in North America and the colonies afterwards adopted a single "
        "settled form of government that ended every regional difference",
        "Colonists objected to taxation, fought a war, and then returned to the arrangements "
        "that had governed them before it",
        "The Revolution's ideals were confined to the United States and had no effect on the "
        "movement of people or on relations with European powers",
        "The period is about migration and competition alone, since the framework treats the "
        "war and the new governments as belonging to the previous period"],
      ans=0,
      why="The first collects KC-3.1, KC-3.2 and KC-3.3 in the order the preview prints them "
          "and adds nothing. The second contradicts KC-3.2.III.i's continued regional "
          "variations; the third denies the new experiments of KC-3.2; the fourth denies both "
          "KC-3.3 and KC-3.3.II; and the fifth drops two of the three previewed concepts, all "
          "of which Unit 3: Learning Objective A asks students to contextualise together."),
]
