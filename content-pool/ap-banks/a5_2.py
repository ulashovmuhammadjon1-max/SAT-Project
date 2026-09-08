# AP U.S. HISTORY 5.2 Manifest Destiny  (title copied from US_HISTORY_topics.json)
# Unit 5, Period 5: 1844 to 1877. Thematic focus: Geography and the Environment GEO.
# Reasoning process printed beside this topic: Causation. Suggested skill 1.B, explain a
# historical concept, development, or process.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 5 Learning Objective B
#       Explain the causes and effects of westward expansion from 1844 to 1877.
#
#   KC-5.1.I.A  The desire for access to natural and mineral resources and the hope of
#               many settlers for economic opportunities or religious refuge led to an
#               increased migration to and settlement in the West.
#   KC-5.1.I.B  Advocates of annexing western lands argued that Manifest Destiny and the
#               superiority of American institutions compelled the United States to
#               expand its borders westward to the Pacific Ocean; however, this
#               frequently provoked competition and violent conflict.
#   KC-5.1.I.D  Westward migration was boosted during and after the Civil War by the
#               passage of new legislation promoting western transportation and economic
#               development.
#   KC-5.1.I.E  U.S. interest in expanding trade led to economic, diplomatic, and
#               cultural initiatives to create more ties with Asia.
#
#   Thematic focus GEO, printed on this page: "Geographic and environmental factors,
#   including competition over and debates about natural resources, shape the development
#   of America and foster regional diversity. The development of America impacts the
#   environment and reshapes geography, which leads to debates about environmental and
#   geographic issues."
#
# WHAT IS NOT KEYED, DELIBERATELY. This topic's page also prints an OPTIONAL SOURCES
# list. The CED says of it, in terms: "The following optional sources and activity are
# not required AP course content... None of the AP Exam questions require students to
# have studied these specific sources." So no key here rests on a named pamphlet, treaty,
# speech or author from that list. Nothing in this module asks a student to know who
# coined a phrase or who signed a treaty; every key traces to one of the four sentences
# above, to the Learning Objective, or to the thematic focus statement.
#
# ATTRIBUTION, and why the verifier enforces it. KC-5.1.I.B does NOT assert that American
# institutions were superior. It reports that ADVOCATES OF ANNEXING WESTERN LANDS ARGUED
# so, and it follows the report with "however, this frequently provoked competition and
# violent conflict". A question that dropped the reporting verb would teach the argument
# as the framework's own finding. `a56_scope.attributed` refuses any stem, choice or why
# that names the superiority of American institutions without an attribution word within
# reach, and item 9 exists to key the distinction itself.
#
# NO FIGURES: the bank cannot display images, so the data items carry a table=.
# PROSE ONLY: no LaTeX; a span of years is written "1844 to 1877", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("5.2", "Manifest Destiny", 5)

_T_MOTIVES = dict(
    headers=["Reason a hypothetical group of migrating households recorded",
             "Number of households recording it"],
    rows=[["Access to natural and mineral resources", "48"],
          ["Hope of economic opportunity", "61"],
          ["Hope of religious refuge", "22"],
          ["Other reasons recorded", "9"]])

_T_PAMPHLETS = dict(
    headers=["Hypothetical annexation pamphlet, its author unnamed",
             "Argument the pamphlet advances"],
    rows=[["Pamphlet 1",
           "Manifest Destiny compels the nation to extend its borders westward to the "
           "Pacific Ocean"],
          ["Pamphlet 2",
           "American institutions are superior to those of their neighbours and ought to "
           "be carried west"],
          ["Pamphlet 3",
           "The duties charged on imported cloth should be lowered at the next session"],
          ["Pamphlet 4",
           "Trade should be enlarged by treaty and by a regular steamship service across "
           "the Pacific"]])

QUESTIONS = [

 dict(q="Unit 5's Learning Objective B asks students to explain something about westward "
        "expansion across a stated span of years. Which does the framework name?",
      choices=[
        "The causes and effects of westward expansion from 1844 to 1877",
        "The causes of westward expansion from 1844 to 1877, leaving its effects aside",
        "The effects of westward expansion from 1865 to 1898",
        "The similarities and differences between westward expansion and industrial growth",
        "The causes and effects of westward expansion from 1800 to 1848"],
      ans=0,
      why="Unit 5 Learning Objective B reads 'Explain the causes and effects of westward "
          "expansion from 1844 to 1877', so both halves and the span are the framework's "
          "own. The span 1865 to 1898 is Period 6's and 1800 to 1848 is Period 4's, and the "
          "reasoning process printed beside this topic is causation rather than comparison."),

 dict(q="According to KC-5.1.I.A, which set names everything that led to an increased "
        "migration to and settlement in the West?",
      choices=[
        "The desire for access to natural and mineral resources, and the hope of many "
        "settlers for economic opportunities or religious refuge",
        "The desire for access to natural and mineral resources, and nothing besides",
        "The hope of many settlers for economic opportunities, and a government wish to "
        "reduce the population of the eastern cities",
        "The desire for access to natural and mineral resources, and the hope of many "
        "settlers for military service or public office",
        "The hope of many settlers for religious refuge, and a wish among merchants to "
        "shorten the route to Europe"],
      ans=0,
      why="KC-5.1.I.A states that the desire for access to natural and mineral resources and "
          "the hope of many settlers for economic opportunities or religious refuge led to "
          "an increased migration to and settlement in the West. Reducing the sentence to "
          "one of its causes, or substituting a government wish, military service, public "
          "office or a route to Europe, changes what the framework says drove the migration."),

 dict(q="KC-5.1.I.A names what those desires and hopes led to. Which does the framework "
        "state?",
      choices=[
        "An increased migration to and settlement in the West",
        "An increased migration to the cities of the East",
        "A decline in the population of the western territories",
        "An increase in the volume of trade carried across the Atlantic",
        "A reduction in competition over natural resources"],
      ans=0,
      why="KC-5.1.I.A ends by naming an increased migration to and settlement in the West as "
          "the effect. Migration eastward and a declining western population reverse it; "
          "KC-5.1.I.E rather than KC-5.1.I.A is where expanding trade appears, and it names "
          "Asia rather than the Atlantic; and KC-5.1.I.B says the expansion frequently "
          "provoked competition rather than reducing it."),

 dict(q="KC-5.1.I.A attributes a hope for economic opportunities or religious refuge to MANY "
        "settlers. What does that word do to the framework's claim?",
      choices=[
        "It attributes the hope to a large number of settlers without attributing it to all "
        "of them",
        "It attributes the hope to every settler who moved west",
        "It attributes the hope to a handful of settlers only",
        "It removes settlers from the framework's account of the migration",
        "It makes the hope a policy of government rather than a motive of settlers"],
      ans=0,
      why="KC-5.1.I.A says 'the hope of many settlers', which is a claim about a large number "
          "and not about all of them or only a few; the sentence keeps settlers at the "
          "centre of the migration it describes and treats the hope as theirs. The "
          "legislation of KC-5.1.I.D is where government action enters this topic, and it "
          "boosts the migration rather than supplying its motive."),

 dict(q="A hypothetical settler's letter, its author unnamed, describes ore deposits reported "
        "in a western valley and the writer's decision to move there. Which cause named in "
        "KC-5.1.I.A does the letter illustrate?",
      choices=[
        "The desire for access to natural and mineral resources",
        "The hope of many settlers for religious refuge",
        "An interest in expanding trade with Asia",
        "The passage of legislation promoting western transportation",
        "The argument that expansion to the Pacific Ocean was compelled"],
      ans=0,
      why="KC-5.1.I.A names the desire for access to natural and mineral resources first "
          "among the causes of increased migration to and settlement in the West, and ore is "
          "a mineral resource. Religious refuge is the sentence's other motive, expanding "
          "trade with Asia belongs to KC-5.1.I.E, transportation legislation to KC-5.1.I.D, "
          "and the compulsion to reach the Pacific is what KC-5.1.I.B reports advocates "
          "arguing."),

 dict(q="A hypothetical family record, its author unnamed, states that the household moved "
        "west so that its members could worship as they chose. Which cause named in "
        "KC-5.1.I.A does the record illustrate?",
      choices=[
        "The hope of many settlers for religious refuge",
        "The desire for access to natural and mineral resources",
        "The hope of many settlers for economic opportunities",
        "An interest in creating more cultural ties with Asia",
        "The argument advocates of annexing western lands made"],
      ans=0,
      why="KC-5.1.I.A names the hope of many settlers for economic opportunities OR "
          "religious refuge, and a move made in order to worship freely is the second of "
          "those two. Mineral resources and economic opportunity are the sentence's other "
          "causes, ties with Asia belong to KC-5.1.I.E, and KC-5.1.I.B reports an argument "
          "for annexation rather than a settler's motive."),

 dict(q="KC-5.1.I.B reports what advocates of annexing western lands argued. Which statement "
        "gives their argument as the framework states it?",
      choices=[
        "That Manifest Destiny and the superiority of American institutions compelled the "
        "United States to expand its borders westward to the Pacific Ocean",
        "That the United States should extend its borders only as far as settlers had "
        "already gone",
        "That Manifest Destiny compelled the United States to extend its borders eastward "
        "across the Atlantic",
        "That American institutions were strong enough to make any further expansion "
        "unnecessary",
        "That expansion should wait until competition and violent conflict had ended"],
      ans=0,
      why="KC-5.1.I.B states that advocates of annexing western lands argued that Manifest "
          "Destiny and the superiority of American institutions compelled the United States "
          "to expand its borders westward to the Pacific Ocean. The framework reports this "
          "as their argument. Reversing the direction, dropping half the argument, or making "
          "expansion conditional all depart from the sentence, whose closing clause says the "
          "expansion frequently provoked competition and violent conflict rather than "
          "waiting for them to end."),

 dict(q="KC-5.1.I.B names the limit to which advocates of annexation argued the borders "
        "should be extended. Which does the framework give?",
      choices=[
        "Westward to the Pacific Ocean",
        "Westward to the crest of the Rocky Mountains",
        "Southward to the Isthmus of Panama",
        "Northward to the Arctic Ocean",
        "As far as the treaties already in force allowed"],
      ans=0,
      why="KC-5.1.I.B says the advocates argued that the United States was compelled to "
          "expand its borders westward to the Pacific Ocean. No other limit appears in that "
          "sentence, and a limit set by treaties already in force would be the opposite of "
          "the compulsion the advocates claimed."),

 dict(q="KC-5.1.I.B mentions the superiority of American institutions. How does the framework "
        "present that claim?",
      choices=[
        "As part of the argument advocates of annexing western lands made, not as the "
        "framework's own assertion",
        "As a finding the framework itself establishes about the institutions of the period",
        "As the reason the framework gives for the outcome of westward migration",
        "As an argument the framework attributes to settlers rather than to advocates of "
        "annexation",
        "As a claim the framework says the advocates of annexation came to reject"],
      ans=0,
      why="KC-5.1.I.B opens 'Advocates of annexing western lands argued that...', so "
          "everything after the verb is reported as their argument rather than asserted by "
          "the framework. The sentence attributes it to those advocates rather than to "
          "settlers, does not say they abandoned it, and gives increased migration in "
          "KC-5.1.I.A a different set of causes altogether."),

 dict(q="KC-5.1.I.B closes with a qualification introduced by the word 'however'. What does "
        "that closing clause state?",
      choices=[
        "That the expansion frequently provoked competition and violent conflict",
        "That the expansion was accomplished without opposition of any kind",
        "That competition and violent conflict occurred only after 1877",
        "That the advocates gave up their argument once conflict began",
        "That competition over resources was settled by treaty in every case"],
      ans=0,
      why="KC-5.1.I.B ends 'however, this frequently provoked competition and violent "
          "conflict', which is the framework's own qualification of the expansion the "
          "advocates urged. The sentence dates nothing to after 1877, says nothing about the "
          "advocates changing their minds, and reports conflict rather than universal "
          "settlement."),

 dict(q="KC-5.1.I.B says the expansion FREQUENTLY provoked competition and violent conflict. "
        "What does that word stop the sentence short of claiming?",
      choices=[
        "That it provoked competition and violent conflict in every instance",
        "That it provoked competition and violent conflict at all",
        "That the competition and the conflict were serious",
        "That advocates of annexing western lands existed",
        "That the borders were extended westward"],
      ans=0,
      why="KC-5.1.I.B's word 'frequently' asserts that the provocation was common while "
          "declining to say it happened every time, and reading the framework's own hedges "
          "is part of using it honestly. The same sentence does assert that conflict "
          "occurred, that advocates existed and that expansion westward was urged, so none "
          "of those is what the word withholds."),

 dict(q="According to KC-5.1.I.D, what boosted westward migration during and after the Civil "
        "War?",
      choices=[
        "The passage of new legislation promoting western transportation and economic "
        "development",
        "The passage of new legislation restricting settlement in the western territories",
        "A finding that the western territories held no mineral resources worth working",
        "A decision by advocates of annexation to give up their argument",
        "The enlargement of trade with Asia"],
      ans=0,
      why="KC-5.1.I.D states that westward migration was boosted during and after the Civil "
          "War by the passage of new legislation promoting western transportation and "
          "economic development. Legislation that restricted settlement would work the other "
          "way; KC-5.1.I.A makes mineral resources a cause of migration rather than an "
          "absence of them; and KC-5.1.I.E treats trade with Asia separately."),

 dict(q="KC-5.1.I.D says westward migration was BOOSTED during and after the Civil War. What "
        "does that word indicate about the migration?",
      choices=[
        "That it was already occurring and was increased rather than begun",
        "That it began only once the legislation had been passed",
        "That it slowed as the legislation took effect",
        "That it was confined to the years of the war itself",
        "That it was carried out by the government rather than by settlers"],
      ans=0,
      why="A boost raises something already in motion, and KC-5.1.I.A has already described "
          "an increased migration to and settlement in the West arising from resources, "
          "opportunity and refuge, so KC-5.1.I.D adds to a migration the framework has "
          "already established. The phrase 'during and after' rules out confinement to the "
          "war years, and the sentence describes legislation promoting migration rather than "
          "government carrying it out."),

 dict(q="KC-5.1.I.D places the boost to westward migration DURING AND AFTER the Civil War. "
        "What does that pairing establish?",
      choices=[
        "That the boost was not confined to the years following the war",
        "That the boost took effect only once the war was over",
        "That the boost took effect only while the war was being fought",
        "That the war had no bearing at all on westward migration",
        "That the legislation had been passed before the war began"],
      ans=0,
      why="KC-5.1.I.D names two stretches of time at once, during the Civil War and after it, "
          "so neither one alone is what the sentence claims; a reader who kept only the "
          "postwar half or only the wartime half would drop what the framework prints. The "
          "sentence ties the boost to legislation passed in those years rather than before "
          "them, and it relates the migration to the war rather than separating them."),

 dict(q="KC-5.1.I.D names two things the new legislation promoted. Which pair does the "
        "framework give?",
      choices=[
        "Western transportation and economic development",
        "Western transportation and religious settlement",
        "Economic development and the extension of the franchise",
        "Military garrisons and the survey of mineral deposits",
        "Public education and the improvement of harbours"],
      ans=0,
      why="KC-5.1.I.D says the new legislation promoted western transportation and economic "
          "development. Religious refuge is a settler's motive in KC-5.1.I.A rather than "
          "something the legislation promoted, and the franchise, garrisons, mineral surveys, "
          "education and harbours are not named in this sentence at all."),

 dict(q="According to KC-5.1.I.E, U.S. interest in expanding trade led to initiatives of "
        "three kinds. Which set names them?",
      choices=[
        "Economic, diplomatic, and cultural initiatives",
        "Economic, military, and religious initiatives",
        "Diplomatic, cultural, and educational initiatives",
        "Economic, diplomatic, and military initiatives",
        "Cultural, scientific, and legal initiatives"],
      ans=0,
      why="KC-5.1.I.E states that U.S. interest in expanding trade led to economic, "
          "diplomatic, and cultural initiatives to create more ties with Asia. Military, "
          "religious, educational, scientific and legal initiatives are not in that list, "
          "and substituting one of them for a term the framework prints changes what the "
          "sentence claims the interest produced."),

 dict(q="KC-5.1.I.E states the part of the world with which those initiatives were meant to "
        "create more ties. Which does the framework name?",
      choices=[
        "Asia",
        "Europe",
        "Africa",
        "The Caribbean",
        "Australia"],
      ans=0,
      why="KC-5.1.I.E says the economic, diplomatic, and cultural initiatives were to create "
          "more ties with Asia. No other region is named in that sentence, and none of the "
          "other three sentences of this topic mentions a region outside North America."),

 dict(q="Which statement belongs to KC-5.1.I.A's account of why settlers moved west rather "
        "than to KC-5.1.I.B's account of what advocates of annexation argued?",
      choices=[
        "The hope of economic opportunities drew many settlers to the West",
        "Expansion as far as the Pacific Ocean was compelled and could not be declined",
        "The superiority of American institutions was urged as a reason to annex western "
        "lands",
        "Annexing the western lands was pressed as a duty the nation could not refuse",
        "Extending the borders westward was said to follow from the nation's destiny"],
      ans=0,
      why="Only the first is KC-5.1.I.A, which names the desire for resources and the hope of "
          "many settlers for economic opportunities or religious refuge as the causes of "
          "increased migration and settlement. The other four restate parts of the argument "
          "KC-5.1.I.B reports advocates of annexing western lands making, which is a claim "
          "about policy rather than an account of why households moved."),

 dict(q="The Unit 5 outline prints a reasoning process beside this topic. Which is it?",
      choices=[
        "Causation",
        "Comparison",
        "Continuity and change",
        "Periodisation",
        "Contextualisation"],
      ans=0,
      why="Causation is printed beside this topic in the Unit 5 outline, and it matches Unit "
          "5 Learning Objective B, which asks for the CAUSES AND EFFECTS of westward "
          "expansion from 1844 to 1877. Comparison is printed beside topics 5.4, 5.5, 5.8 "
          "and 5.12 and continuity and change beside 5.1, 5.9 and 5.11; contextualisation is "
          "a skill category rather than a reasoning process."),

 dict(q="The suggested skill printed beside this topic is stated in the framework as which of "
        "the following?",
      choices=[
        "Explain a historical concept, development, or process",
        "Explain how a specific historical development or process is situated within a "
        "broader historical context",
        "Compare the arguments or main ideas of two sources",
        "Explain the point of view, purpose, historical situation, and/or audience of a "
        "source",
        "Identify patterns among or connections between historical developments and processes"],
      ans=0,
      why="Skill 1.B, explain a historical concept, development, or process, is printed "
          "beside this topic, and Manifest Destiny is exactly the kind of concept it asks "
          "students to explain under Unit 5 Learning Objective B. The others are skills 4.B, "
          "3.C, 2.B and 5.A, printed beside topics 5.4, 5.3, 5.5 and 5.8 of this same unit."),

 dict(q="The thematic focus printed on this topic's page is Geography and the Environment. "
        "Which statement gives that focus as the framework states it?",
      choices=[
        "Geographic and environmental factors, including competition over and debates about "
        "natural resources, shape the development of America and foster regional diversity",
        "Push and pull factors shape immigration to and migration within America, and the "
        "resulting demographic change shapes the migrants, society, and the environment",
        "The interplay between markets, private enterprise, labor, technology, and government "
        "policy shape the American economy",
        "Social categories, roles, and practices are created, maintained, challenged, and "
        "transformed throughout American history",
        "Diplomatic, economic, cultural, and military interactions between empires, nations, "
        "and peoples shape the development of America"],
      ans=0,
      why="The Geography and the Environment focus statement names geographic and "
          "environmental factors, including competition over and debates about natural "
          "resources, as shaping America's development and fostering regional diversity, "
          "which is why it heads a topic resting on KC-5.1.I.A's desire for access to natural "
          "and mineral resources. The other four are the framework's Migration and "
          "Settlement, Work Exchange and Technology, Social Structures, and America in the "
          "World statements, printed at the head of other topics."),

 dict(q="Which pairing states a cause and its effect as KC-5.1.I.A gives them?",
      choices=[
        "The desire for access to natural and mineral resources as the cause, and increased "
        "migration to and settlement in the West as the effect",
        "Increased migration to and settlement in the West as the cause, and the desire for "
        "access to natural and mineral resources as the effect",
        "The passage of legislation promoting transportation as the cause, and the hope of "
        "religious refuge as the effect",
        "The argument of advocates of annexation as the cause, and the finding of mineral "
        "deposits as the effect",
        "Enlarged trade with Asia as the cause, and settlement in the West as the effect"],
      ans=0,
      why="KC-5.1.I.A puts the desire for access to natural and mineral resources on the "
          "cause side and increased migration to and settlement in the West on the effect "
          "side. Exchanging the two inverts the sentence, and the remaining pairs join terms "
          "the framework keeps in separate sentences: KC-5.1.I.D's legislation, KC-5.1.I.B's "
          "argument and KC-5.1.I.E's trade with Asia."),

 dict(q="A hypothetical territorial newspaper report, its author unnamed, notes that a "
        "statute has been passed to aid the building of a road and a telegraph line into a "
        "western territory, and that arrivals have risen since. Which sentence of the "
        "framework does the report illustrate?",
      choices=[
        "KC-5.1.I.D, which says westward migration was boosted by new legislation promoting "
        "western transportation and economic development",
        "KC-5.1.I.A, which names the desire for access to natural and mineral resources",
        "KC-5.1.I.B, which reports the argument advocates of annexing western lands made",
        "KC-5.1.I.E, which concerns initiatives to create more ties with Asia",
        "None of the framework's four sentences about westward expansion in this topic"],
      ans=0,
      why="KC-5.1.I.D ties a rise in westward migration to new legislation promoting western "
          "transportation and economic development, and a road and a telegraph line built "
          "under a new statute are transportation and communication of exactly that kind. "
          "The other sentences concern settlers' motives, the argument for annexation, and "
          "trade with Asia, none of which the report describes."),

 dict(q="A hypothetical merchant's memorandum, its author unnamed, proposes a regular "
        "steamship service and an exchange of envoys with a country across the Pacific in "
        "order to enlarge trade. Which sentence of the framework does the proposal "
        "illustrate?",
      choices=[
        "KC-5.1.I.E, which says U.S. interest in expanding trade led to economic, diplomatic, "
        "and cultural initiatives to create more ties with Asia",
        "KC-5.1.I.A, which names the hope of settlers for economic opportunities or religious "
        "refuge",
        "KC-5.1.I.B, which reports what advocates of annexing western lands argued",
        "KC-5.1.I.D, which concerns legislation promoting western transportation",
        "None of the framework's four sentences about westward expansion in this topic"],
      ans=0,
      why="KC-5.1.I.E states that U.S. interest in expanding trade led to economic, "
          "diplomatic, and cultural initiatives to create more ties with Asia, and a "
          "steamship service with an exchange of envoys is an economic initiative and a "
          "diplomatic one together. The other three sentences concern settlers' motives, the "
          "argument for annexation, and legislation promoting transportation within the "
          "West."),

 dict(q="Using the table of recorded reasons, which statement is supported?",
      table=_T_MOTIVES,
      choices=[
        "More households recorded a hope of economic opportunity than recorded access to "
        "natural and mineral resources",
        "More households recorded access to natural and mineral resources than recorded a "
        "hope of economic opportunity",
        "A hope of religious refuge was the most frequently recorded reason",
        "Every household in the group recorded the same reason",
        "The three reasons the framework names were recorded by fewer households in total "
        "than the remaining reasons were"],
      ans=0,
      why="Read from the table alone: sixty one households against forty eight, so the "
          "comparison runs one way and its reverse is false; twenty two is not the largest "
          "count; the counts differ, so the reasons were not all the same; and the three "
          "named reasons together outnumber the remainder many times over. All three named "
          "reasons are those KC-5.1.I.A gives for increased migration to and settlement in "
          "the West."),

 dict(q="Using the same table of recorded reasons, which claim goes BEYOND what the record "
        "can support?",
      table=_T_MOTIVES,
      choices=[
        "That the households which moved west found the opportunity they had hoped for",
        "That a hope of economic opportunity was recorded more often than a hope of religious "
        "refuge",
        "That access to natural and mineral resources was recorded by more than forty "
        "households",
        "That the reasons recorded include all three of those the framework names",
        "That fewer households recorded a reason outside the three the framework names than "
        "recorded any one of the three"],
      ans=0,
      why="The table records a reason and a count for each row and nothing about what "
          "happened to the households afterwards, so whether the hope was met is a claim it "
          "cannot reach. The other four are read directly off the rows, and the three reasons "
          "named in them are those KC-5.1.I.A gives: access to natural and mineral resources, "
          "and the hope of many settlers for economic opportunities or religious refuge."),

 dict(q="Using the table of hypothetical pamphlets, which two advance the argument KC-5.1.I.B "
        "attributes to advocates of annexing western lands?",
      table=_T_PAMPHLETS,
      choices=[
        "The pamphlet invoking Manifest Destiny and the pamphlet claiming the superiority of "
        "American institutions",
        "The pamphlet about import duties and the pamphlet about trade across the Pacific",
        "The pamphlet invoking Manifest Destiny and the pamphlet about import duties",
        "The pamphlet about trade across the Pacific and the pamphlet claiming the "
        "superiority of American institutions",
        "All four of the pamphlets in the table"],
      ans=0,
      why="KC-5.1.I.B reports advocates of annexing western lands arguing that Manifest "
          "Destiny AND the superiority of American institutions compelled the United States "
          "to expand its borders westward to the Pacific Ocean, so exactly the two pamphlets "
          "advancing those two claims match it. Read from the table alone, the remaining two "
          "concern import duties and the enlargement of trade, and the second of those "
          "belongs with KC-5.1.I.E instead."),

 dict(q="Using the same table of hypothetical pamphlets, which one advances the interest "
        "KC-5.1.I.E describes?",
      table=_T_PAMPHLETS,
      choices=[
        "The pamphlet proposing that trade be enlarged by treaty and by a regular steamship "
        "service",
        "The pamphlet invoking Manifest Destiny",
        "The pamphlet comparing American institutions with those of their neighbours",
        "The pamphlet on the duties charged on imported cloth",
        "None of the four pamphlets in the table"],
      ans=0,
      why="KC-5.1.I.E says U.S. interest in expanding trade led to economic, diplomatic, and "
          "cultural initiatives to create more ties with Asia, and read from the table alone "
          "exactly one pamphlet proposes enlarging trade by treaty and by steamship service "
          "across the Pacific. The others belong with KC-5.1.I.B's argument for annexation or "
          "with a question of import duties that this topic's sentences do not treat."),

 dict(q="Which of the following does the framework NOT state about westward expansion in this "
        "topic?",
      choices=[
        "That the expansion ended competition over natural resources",
        "That a desire for access to natural and mineral resources led to increased migration",
        "That advocates of annexing western lands argued for expansion to the Pacific Ocean",
        "That new legislation promoting western transportation boosted migration",
        "That U.S. interest in expanding trade led to initiatives creating more ties with Asia"],
      ans=0,
      why="KC-5.1.I.B says the expansion FREQUENTLY PROVOKED competition and violent conflict, "
          "which is the opposite of ending competition, so that is the claim the framework "
          "does not make. The other four restate KC-5.1.I.A, KC-5.1.I.B, KC-5.1.I.D and "
          "KC-5.1.I.E in turn."),

 dict(q="Which single sentence best collects what this topic's four historical developments "
        "state, without adding to them?",
      choices=[
        "Resources, opportunity and refuge drew settlers west; advocates argued that "
        "expansion to the Pacific was compelled, though it frequently provoked competition "
        "and violent conflict; new legislation boosted migration during and after the Civil "
        "War; and an interest in trade produced initiatives creating ties with Asia",
        "Settlers moved west for land alone, and the government took no part in the movement "
        "at any stage",
        "Expansion to the Pacific was accomplished peacefully and closed the question of "
        "trade with Asia",
        "The whole of westward expansion in this period followed from legislation passed "
        "after the Civil War",
        "Westward expansion was driven by industrial consolidation and by the growth of large "
        "cities"],
      ans=0,
      why="The first collects KC-5.1.I.A, KC-5.1.I.B, KC-5.1.I.D and KC-5.1.I.E in the order "
          "the page prints them and adds nothing. KC-5.1.I.A names resources, opportunity and "
          "refuge rather than land alone and KC-5.1.I.D gives government a part; KC-5.1.I.B "
          "records frequent competition and violent conflict rather than a peaceful "
          "settlement; the legislation boosted a migration already under way rather than "
          "producing all of it; and industrial consolidation belongs to the following "
          "period."),
]
