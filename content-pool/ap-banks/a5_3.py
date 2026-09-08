# AP U.S. HISTORY 5.3 The Mexican-American War  (title in TOPIC copied verbatim from
# US_HISTORY_topics.json, which carries the CED's en dash; this comment uses a plain
# hyphen because the module text is ASCII throughout.)
# Unit 5, Period 5: 1844 to 1877. Thematic focus: America in the World WOR. Reasoning
# process printed beside this topic: Causation. Suggested skill 3.C, compare the
# arguments or main ideas of two sources.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 5 Learning Objective C
#       Explain the causes and effects of the Mexican-American War.
#
#   KC-5.1.I.C   The United States added large territories in the West through victory in
#                the Mexican-American War and diplomatic negotiations, raising questions
#                about the status of slavery, American Indians, and Mexicans in the newly
#                acquired lands.
#   KC-5.1.II.C  U.S. government interaction and conflict with Mexican Americans and
#                American Indians increased in regions newly taken from American Indians
#                and Mexico, altering these groups' economic self-sufficiency and
#                cultures.
#
#   Thematic focus WOR, printed on this page: "Diplomatic, economic, cultural, and
#   military interactions between empires, nations, and peoples shape the development of
#   America and America's increasingly important role in the world."
#
# WHAT IS NOT KEYED, DELIBERATELY. This topic's page also prints an OPTIONAL SOURCES
# list of named documents, of which the CED says "not required AP course content...
# None of the AP Exam questions require students to have studied these specific
# sources." No key here names one of them, and no key asks a student who wrote what.
#
# SENSITIVE MATERIAL. This topic covers a war, a conquest and the dispossession that
# followed. It is handled in the framework's own words and no further. The CED writes
# "regions newly taken from American Indians and Mexico" and "altering these groups'
# economic self-sufficiency and cultures", and this module writes the same. Nothing here
# quantifies a loss, describes violence, or keys a judgement the framework does not make.
# In particular, item 19 keys the NEUTRAL reading of the word ALTERED, because the CED
# states that the self-sufficiency and cultures were altered and does not state a
# direction; a question keying a direction would be putting words in the framework's
# mouth about people it is describing.
#
# NO FIGURES: the bank cannot display images, so the data items carry a table=.
# PROSE ONLY: no LaTeX; a span of years is written "1844 to 1877", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("5.3", "The Mexican–American War", 5)

_T_PETITIONS = dict(
    headers=["Hypothetical petition to a territorial convention, its author unnamed",
             "Question it raises"],
    rows=[["Petition 1", "Whether persons may be held as slaves in the newly acquired lands"],
          ["Petition 2",
           "Whether American Indians in the newly acquired lands are to keep their lands"],
          ["Petition 3",
           "Whether Mexicans living in the newly acquired lands are to be citizens"],
          ["Petition 4", "Whether the duty charged on imported wool is to be raised"]])

_T_SOURCES = dict(
    headers=["Hypothetical unattributed source", "Main idea it advances"],
    rows=[["Source 1",
           "The territory gained by the war settled every question about who would live "
           "there and under what status"],
          ["Source 2",
           "The territory gained by the war left open the question of who would live there "
           "and under what status"]])

_T_COMMUNITIES = dict(
    headers=["Hypothetical description recorded for a community in a region newly taken",
             "What the description reports"],
    rows=[["Community A", "Its customary way of making a living was disrupted"],
          ["Community B", "Its observances and its language came under pressure"],
          ["Community C",
           "Both its way of making a living and its observances were affected"],
          ["Community D", "A new road was surveyed some miles away"]])

QUESTIONS = [

 dict(q="Unit 5's Learning Objective C names what students are to explain about this war. "
        "Which does the framework give?",
      choices=[
        "The causes and effects of the Mexican-American War",
        "The causes of the Mexican-American War, leaving its effects aside",
        "The similarities and differences between this war and the Civil War",
        "The point of view and purpose of sources written during the war",
        "The effects of the war on the economy of the North alone"],
      ans=0,
      why="Unit 5 Learning Objective C reads 'Explain the causes and effects of the "
          "Mexican-American War', so both halves are the framework's own. Comparison with "
          "another war, the analysis of a source's purpose and a restriction to one region "
          "are not what this objective asks, and KC-5.1.I.C and KC-5.1.II.C between them "
          "supply effects reaching well beyond the North."),

 dict(q="According to KC-5.1.I.C, what did the United States add in the West?",
      choices=[
        "Large territories",
        "A single territory of modest extent",
        "A network of trading posts carrying no territory with it",
        "A protectorate over lands it did not govern",
        "Nothing beyond what it already held"],
      ans=0,
      why="KC-5.1.I.C opens by stating that the United States added large territories in the "
          "West. A single modest territory, trading posts, a protectorate and no addition at "
          "all each understate or replace what the sentence says was added."),

 dict(q="KC-5.1.I.C names two means by which the United States added those territories. Which "
        "pair does the framework give?",
      choices=[
        "Victory in the Mexican-American War and diplomatic negotiations",
        "Victory in the Mexican-American War and nothing besides",
        "Diplomatic negotiations and the purchase of land from settlers already there",
        "Victory in the Mexican-American War and the westward movement of settlers",
        "Diplomatic negotiations and a grant made by a European power"],
      ans=0,
      why="KC-5.1.I.C says the territories were added 'through victory in the Mexican-"
          "American War and diplomatic negotiations', naming both means in one clause. "
          "Dropping the negotiations, or replacing either means with a purchase from "
          "settlers, a movement of settlers or a European grant, changes how the framework "
          "says the territories came to be held."),

 dict(q="KC-5.1.I.C names diplomatic negotiations alongside victory in the war. What does "
        "including both establish?",
      choices=[
        "That not all of the added territory came through military victory alone",
        "That the war produced no territorial change at all",
        "That the negotiations were concluded before any fighting began",
        "That the territories were added without the agreement of any other government",
        "That the framework treats the two means as one and the same"],
      ans=0,
      why="KC-5.1.I.C attributes the addition to victory in the war AND diplomatic "
          "negotiations, so the sentence gives two routes rather than one. It does credit "
          "the victory with territory, gives no order between the two, and negotiation is by "
          "definition agreement with another government, so the remaining readings all "
          "contradict the clause."),

 dict(q="KC-5.1.I.C says the acquisition raised questions about the status of three things. "
        "Which set names them?",
      choices=[
        "Slavery, American Indians, and Mexicans in the newly acquired lands",
        "Slavery, import duties, and land surveys in the newly acquired lands",
        "American Indians, Mexicans, and European settlers in the newly acquired lands",
        "Slavery, American Indians, and the federal courts in the newly acquired lands",
        "Mexicans, railroads, and mineral claims in the newly acquired lands"],
      ans=0,
      why="KC-5.1.I.C closes by naming questions about the status of slavery, American "
          "Indians, and Mexicans in the newly acquired lands. Import duties, land surveys, "
          "European settlers, the federal courts, railroads and mineral claims are not in "
          "that list, and each substitution drops one of the three the framework names."),

 dict(q="KC-5.1.I.C locates the questions about status in a particular place. Which does the "
        "framework give?",
      choices=[
        "The newly acquired lands",
        "The states of the eastern seaboard",
        "The territories the United States had held before the war",
        "The ports on the far side of the Pacific",
        "Every state and territory of the Union equally"],
      ans=0,
      why="KC-5.1.I.C says the questions concerned the status of slavery, American Indians, "
          "and Mexicans IN THE NEWLY ACQUIRED LANDS. The sentence is about the lands just "
          "added, so the eastern seaboard, the territories held beforehand, ports abroad and "
          "the Union as a whole are each somewhere the sentence does not place them."),

 dict(q="KC-5.1.I.C presents the questions about status by saying the acquisition RAISED "
        "them. What does that word settle about the order of events?",
      choices=[
        "That the questions followed from the acquisition rather than preceding it",
        "That the questions had been answered before the acquisition took place",
        "That the acquisition followed from the questions",
        "That the questions and the acquisition were unconnected",
        "That the questions arose only after 1877"],
      ans=0,
      why="KC-5.1.I.C makes the acquisition the thing that RAISED the questions, so the "
          "acquisition comes first and the questions follow, which is the direction of "
          "causation Unit 5 Learning Objective C asks students to explain. Reversing the "
          "order, separating the two, or dating the questions outside the period all depart "
          "from the sentence."),

 dict(q="According to KC-5.1.II.C, what increased in the regions newly taken from American "
        "Indians and Mexico?",
      choices=[
        "U.S. government interaction and conflict with Mexican Americans and American Indians",
        "U.S. government interaction with the governments of Europe",
        "Trade between the United States and Asia",
        "Migration out of those regions and into the eastern states",
        "The economic self-sufficiency of the groups already living there"],
      ans=0,
      why="KC-5.1.II.C states that U.S. government interaction and conflict with Mexican "
          "Americans and American Indians increased in regions newly taken from American "
          "Indians and Mexico. The same sentence says these groups' economic self-sufficiency "
          "was ALTERED rather than increased, and European governments, Asian trade and "
          "eastward migration belong to other sentences of the framework or to none."),

 dict(q="KC-5.1.II.C locates that increase in particular regions. Which does the framework "
        "name?",
      choices=[
        "Regions newly taken from American Indians and Mexico",
        "Regions along the Atlantic coast",
        "Regions the United States had held since its founding",
        "Regions ceded to the United States by a European power",
        "Regions in which no government had claimed authority"],
      ans=0,
      why="KC-5.1.II.C names regions newly taken from American Indians and Mexico. That "
          "phrase places the increase where KC-5.1.I.C has just said territory was added, "
          "which is what joins the two sentences; the Atlantic coast, long-held regions, a "
          "European cession and unclaimed regions are each somewhere else."),

 dict(q="KC-5.1.II.C names two things that were altered for these groups. Which pair does the "
        "framework give?",
      choices=[
        "Their economic self-sufficiency and their cultures",
        "Their economic self-sufficiency and their numbers",
        "Their cultures and their military strength",
        "Their languages and their forms of worship",
        "Their landholdings and their trade with Europe"],
      ans=0,
      why="KC-5.1.II.C ends by saying the increase altered these groups' economic "
          "self-sufficiency and cultures. Numbers, military strength, landholdings and trade "
          "with Europe are not named there, and language and worship are parts of what the "
          "word cultures covers rather than the pair the framework prints."),

 dict(q="KC-5.1.II.C says U.S. government INTERACTION AND CONFLICT increased. What does "
        "naming both establish?",
      choices=[
        "That the framework records dealings of more than one kind, not conflict only",
        "That the framework records conflict and nothing else",
        "That interaction and conflict are being treated as the same thing",
        "That interaction decreased as conflict increased",
        "That the framework records neither in the regions newly taken"],
      ans=0,
      why="KC-5.1.II.C names interaction AND conflict together, so the sentence covers "
          "dealings that were not all violent as well as those that were; if the two were "
          "the same word the framework would not need both. The sentence says both "
          "increased, so neither a decrease nor an absence is what it reports."),

 dict(q="Which statement belongs to KC-5.1.I.C's account of the acquisition of territory "
        "rather than to KC-5.1.II.C's account of what followed for the groups living there?",
      choices=[
        "Large territories in the West were added through victory in war and through "
        "diplomatic negotiations",
        "Government interaction and conflict with Mexican Americans increased",
        "Government interaction and conflict with American Indians increased",
        "The economic self-sufficiency of these groups was altered",
        "The cultures of these groups were altered"],
      ans=0,
      why="Only the first is KC-5.1.I.C, which states that the United States added large "
          "territories in the West through victory in the Mexican-American War and "
          "diplomatic negotiations. The other four are KC-5.1.II.C, which describes the "
          "increased interaction and conflict in the regions newly taken and the alteration "
          "of these groups' economic self-sufficiency and cultures."),

 dict(q="The suggested skill printed beside this topic is stated in the framework as which of "
        "the following?",
      choices=[
        "Compare the arguments or main ideas of two sources",
        "Explain a historical concept, development, or process",
        "Explain how a specific historical development or process is situated within a "
        "broader historical context",
        "Explain the point of view, purpose, historical situation, and/or audience of a source",
        "Explain how claims or evidence support, modify, or refute a source's argument"],
      ans=0,
      why="Skill 3.C, compare the arguments or main ideas of two sources, is printed beside "
          "this topic, which is why several items here set two accounts side by side under "
          "Unit 5 Learning Objective C. The others are skills 1.B, 4.B, 2.B and 3.D, printed "
          "beside topics 5.2, 5.4, 5.5 and 5.10 of this same unit."),

 dict(q="KC-5.1.I.C and KC-5.1.II.C both concern people already living in the lands the "
        "United States acquired. What do the two sentences together establish about the "
        "framework's treatment of them?",
      choices=[
        "That it raises a question about their status and then reports that their economic "
        "self-sufficiency and cultures were altered",
        "That it raises a question about their status and reports that the question was "
        "answered at once",
        "That it reports changes to their cultures without raising any question about their "
        "status",
        "That it treats them as inhabitants of Mexico rather than of the newly acquired lands",
        "That it says nothing about how they supported themselves"],
      ans=0,
      why="KC-5.1.I.C raises questions about the status of American Indians and Mexicans in "
          "the newly acquired lands, and KC-5.1.II.C then reports that interaction and "
          "conflict increased in the regions newly taken, altering these groups' economic "
          "self-sufficiency and cultures. Neither sentence records an answer to the question "
          "of status, both place the groups in the acquired lands, and the second names "
          "economic self-sufficiency explicitly."),

 dict(q="The thematic focus printed on this topic's page is America in the World. Which "
        "statement gives that focus as the framework states it?",
      choices=[
        "Diplomatic, economic, cultural, and military interactions between empires, nations, "
        "and peoples shape the development of America and America's increasingly important "
        "role in the world",
        "Geographic and environmental factors, including competition over and debates about "
        "natural resources, shape the development of America",
        "Push and pull factors shape immigration to and migration within America",
        "The interplay between markets, private enterprise, labor, technology, and government "
        "policy shape the American economy",
        "Social categories, roles, and practices are created, maintained, challenged, and "
        "transformed throughout American history"],
      ans=0,
      why="The America in the World focus statement names diplomatic, economic, cultural and "
          "military interactions between empires, nations and peoples, which is why it heads "
          "a topic resting on KC-5.1.I.C's pairing of military victory with diplomatic "
          "negotiations. The other four are the framework's Geography, Migration, Work, and "
          "Social Structures statements, printed at the head of other topics."),

 dict(q="A hypothetical dispatch, its author unnamed, records that a boundary in the West was "
        "fixed by agreement between two governments rather than by fighting. Which part of "
        "KC-5.1.I.C does the dispatch illustrate?",
      choices=[
        "The diplomatic negotiations the sentence names alongside victory in the war",
        "The victory in the Mexican-American War the sentence names",
        "The question about the status of slavery the sentence names",
        "The question about the status of American Indians the sentence names",
        "Nothing in the sentence, which names military means only"],
      ans=0,
      why="KC-5.1.I.C says the territories were added through victory in the Mexican-American "
          "War AND diplomatic negotiations, so a boundary fixed by agreement between "
          "governments is the second of the two means. The sentence does name military "
          "victory as well, which is why the last option is false, and its questions about "
          "status concern what followed the acquisition rather than how it was made."),

 dict(q="Two hypothetical unattributed accounts from a region newly taken are summarised. The "
        "first reports that a community's customary way of supporting itself was disrupted; "
        "the second reports that its observances and language came under pressure. Which "
        "statement compares their main ideas as KC-5.1.II.C would have a student do?",
      choices=[
        "Each reports one of the two alterations the framework names, economic "
        "self-sufficiency in the first and culture in the second",
        "Both report the same alteration, and the framework names only one",
        "Neither reports an alteration the framework names",
        "The first reports a cultural alteration and the second an economic one",
        "Both report an increase in these groups' economic self-sufficiency"],
      ans=0,
      why="KC-5.1.II.C names economic self-sufficiency and cultures as the two things "
          "altered, and a disrupted way of supporting a community is the first while pressure "
          "on its observances and language is the second. Exchanging the two misreads both "
          "accounts, the framework names two alterations rather than one, and it reports "
          "alteration rather than increase."),

 dict(q="A hypothetical petition to a territorial legislature, its author unnamed, asks "
        "whether persons may be held as slaves in lands the United States has newly acquired. "
        "Which sentence of the framework does the petition illustrate?",
      choices=[
        "KC-5.1.I.C, which says the acquisition raised questions about the status of slavery",
        "KC-5.1.II.C, which concerns interaction and conflict in the regions newly taken",
        "Neither sentence, since this topic's page does not mention slavery",
        "Both sentences equally, since each concerns the newly acquired lands",
        "KC-5.1.II.C alone, since the petition concerns a group's economic self-sufficiency"],
      ans=0,
      why="KC-5.1.I.C names the status of slavery in the newly acquired lands as one of the "
          "questions the acquisition raised, and a petition asking whether persons may be "
          "held as slaves there is exactly that question. KC-5.1.II.C concerns increased "
          "interaction and conflict and the alteration of economic self-sufficiency and "
          "cultures, neither of which the petition raises."),

 dict(q="KC-5.1.II.C says these groups' economic self-sufficiency was ALTERED. Which reading "
        "does the framework's word support?",
      choices=[
        "That the way these groups supported themselves was changed",
        "That these groups became more self-sufficient than they had been",
        "That the framework records no change in how these groups supported themselves",
        "That the change reached their cultures and left their livelihoods untouched",
        "That the change occurred before the regions were newly taken"],
      ans=0,
      why="KC-5.1.II.C says the increase in interaction and conflict altered these groups' "
          "economic self-sufficiency and cultures, and 'altered' states that a change "
          "occurred without stating a direction, so a reading that supplies one goes beyond "
          "the sentence. The sentence does record a change, names both livelihoods and "
          "cultures, and places the change in regions newly taken rather than before they "
          "were taken."),

 dict(q="Which of the following does the framework NOT state in this topic?",
      choices=[
        "That the questions of status the acquisition raised were resolved within the period",
        "That the United States added large territories in the West",
        "That the acquisition raised a question about the status of American Indians",
        "That U.S. government interaction and conflict with American Indians increased",
        "That these groups' cultures were altered"],
      ans=0,
      why="KC-5.1.I.C says the acquisition RAISED questions about the status of slavery, "
          "American Indians, and Mexicans and stops there, recording no resolution, so a "
          "resolution is the claim this topic does not make. The other four restate "
          "KC-5.1.I.C and KC-5.1.II.C directly."),

 dict(q="Which pairing states a cause and its effect as KC-5.1.II.C gives them?",
      choices=[
        "Increased U.S. government interaction and conflict as the cause, and the alteration "
        "of these groups' economic self-sufficiency and cultures as the effect",
        "The alteration of these groups' economic self-sufficiency and cultures as the cause, "
        "and increased U.S. government interaction and conflict as the effect",
        "Diplomatic negotiations as the cause, and increased interaction and conflict as the "
        "effect",
        "The alteration of cultures as the cause, and the addition of large territories as "
        "the effect",
        "Enlarged trade with Asia as the cause, and the alteration of these groups' cultures "
        "as the effect"],
      ans=0,
      why="KC-5.1.II.C states that interaction and conflict increased in regions newly taken, "
          "ALTERING these groups' economic self-sufficiency and cultures, so the increase is "
          "the cause and the alteration the effect. Exchanging the two inverts the sentence, "
          "and the remaining pairs join terms the framework keeps apart: KC-5.1.I.C's "
          "negotiations and territories, and trade with Asia, which belongs to another topic."),

 dict(q="Using the table of hypothetical petitions, which three raise a question of the kind "
        "KC-5.1.I.C names?",
      table=_T_PETITIONS,
      choices=[
        "The petitions about slavery, about American Indians, and about Mexicans",
        "The petitions about slavery, about American Indians, and about the duty on wool",
        "The petitions about American Indians, about Mexicans, and about the duty on wool",
        "All four of the petitions in the table",
        "Only the petition about slavery"],
      ans=0,
      why="KC-5.1.I.C names questions about the status of slavery, American Indians, and "
          "Mexicans in the newly acquired lands. Read from the table alone, exactly three of "
          "the four petitions raise one of those three, and the fourth asks about a duty on "
          "an imported good, which is not a question of status at all."),

 dict(q="Using the same table of hypothetical petitions, which claim goes BEYOND what the "
        "record can support?",
      table=_T_PETITIONS,
      choices=[
        "That the convention answered the questions the petitions raised",
        "That three of the four petitions raise a question of status",
        "That one petition concerns a duty rather than a question of status",
        "That one petition asks whether persons may be held as slaves",
        "That no petition concerns the status of a European power"],
      ans=0,
      why="The table records what each petition asks and nothing about what became of it, so "
          "whether the convention answered them is a claim it cannot reach; KC-5.1.I.C "
          "likewise says the questions were raised without recording an answer. The other "
          "four are read directly off the rows."),

 dict(q="Using the table of two hypothetical sources, which comparison of their main ideas "
        "matches KC-5.1.I.C?",
      table=_T_SOURCES,
      choices=[
        "The second matches the framework, which says the acquisition raised questions about "
        "status, while the first denies that it did",
        "The first matches the framework, while the second denies that any territory was "
        "gained",
        "Both sources match the framework equally well",
        "Neither source addresses the status of anyone in the lands gained",
        "The two sources differ only about the extent of the territory gained"],
      ans=0,
      why="KC-5.1.I.C says the acquisition raised questions about the status of slavery, "
          "American Indians, and Mexicans in the newly acquired lands. Read from the table "
          "alone, one source says the gain left that question open and the other says it "
          "settled every such question, so only the first of those two matches the framework "
          "and both do address status; each records that territory was gained, and neither "
          "mentions its extent."),

 dict(q="Using the table of hypothetical descriptions, which community's description reports "
        "both of the alterations KC-5.1.II.C names?",
      table=_T_COMMUNITIES,
      choices=[
        "The community whose way of making a living and whose observances were both affected",
        "The community whose customary way of making a living was disrupted",
        "The community whose observances and language came under pressure",
        "The community near which a new road was surveyed",
        "None of the four communities in the table"],
      ans=0,
      why="KC-5.1.II.C names economic self-sufficiency and cultures as the two things "
          "altered. Read from the table alone, exactly one description reports both a way of "
          "making a living and observances; two others report one of the pair each, and the "
          "fourth reports a road, which is neither."),

 dict(q="A hypothetical council record, its author unnamed, states that a community in a "
        "region newly taken found its customary trade disrupted and its observances under "
        "pressure. Which sentence of the framework does the record illustrate?",
      choices=[
        "KC-5.1.II.C, which names economic self-sufficiency and cultures as what was altered",
        "KC-5.1.I.C, which names the addition of large territories in the West",
        "Neither of this topic's two sentences",
        "KC-5.1.I.C, which raises the question of the status of slavery",
        "Both sentences equally, since each concerns the same groups of people"],
      ans=0,
      why="KC-5.1.II.C says the increased interaction and conflict in regions newly taken "
          "altered these groups' economic self-sufficiency and cultures, and a disrupted "
          "trade with observances under pressure is one of each. KC-5.1.I.C concerns how the "
          "territories were added and what questions of status that raised, neither of which "
          "the record describes."),

 dict(q="KC-5.1.I.C raises questions about the status of three subjects in a single sentence. "
        "What does treating them together indicate about the framework's account?",
      choices=[
        "That it presents them as questions the same acquisition raised, rather than as "
        "unrelated matters",
        "That it treats the three as one and the same question",
        "That it ranks the question about slavery above the other two",
        "That it places the three questions in different periods",
        "That it answers all three within the same sentence"],
      ans=0,
      why="KC-5.1.I.C attributes all three questions to one acquisition, which is what "
          "putting them in a single clause does; the sentence keeps them as three distinct "
          "questions, gives no ranking among them, dates them all to the same acquisition, "
          "and records no answer to any of them."),

 dict(q="How does KC-5.1.I.C serve Unit 5's Learning Objective C?",
      choices=[
        "It supplies effects of the war, since the added territories and the questions of "
        "status both follow from the victory the sentence names",
        "It supplies causes of the war and no effects",
        "It concerns a different war from the one the Learning Objective names",
        "It concerns the years after 1877 rather than the war",
        "It states that the war produced no effects the framework records"],
      ans=0,
      why="Unit 5 Learning Objective C asks for the causes and effects of the Mexican-"
          "American War, and KC-5.1.I.C places the addition of large territories and the "
          "questions of status raised in the newly acquired lands after the victory, which "
          "makes them effects. The sentence names that same war and belongs to a period the "
          "framework ends in 1877."),

 dict(q="Which single sentence best collects what this topic's two historical developments "
        "state, without adding to them?",
      choices=[
        "Victory in the war and diplomatic negotiations added large territories in the West "
        "and raised questions about the status of slavery, American Indians and Mexicans "
        "there, while government interaction and conflict increased in the regions newly "
        "taken and altered these groups' economic self-sufficiency and cultures",
        "The war added no territory and left the questions of the period untouched",
        "The territories were added by purchase alone and raised no question about anyone's "
        "status",
        "The only effect of the war the framework records is an enlargement of trade with Asia",
        "The framework treats the war as the cause of industrial growth in the following "
        "period"],
      ans=0,
      why="The first collects KC-5.1.I.C and KC-5.1.II.C in the order this topic's page "
          "prints them and adds nothing. KC-5.1.I.C states that large territories were added "
          "through victory and negotiations rather than by purchase alone, and that questions "
          "of status were raised; trade with Asia and industrial growth belong to other "
          "topics of the framework."),

 dict(q="Taken together, what do this topic's two sentences establish about the relationship "
        "between the acquisition of territory and the people already living in it?",
      choices=[
        "The acquisition brought their status into question and was followed by increased "
        "government interaction and conflict that altered how they lived",
        "The acquisition left the people already living there unaffected",
        "The acquisition is presented as a consequence of the changes to those communities",
        "The framework records the acquisition without naming anyone living in the lands "
        "acquired",
        "The framework places the changes to those communities before the acquisition"],
      ans=0,
      why="KC-5.1.I.C raises questions about the status of American Indians and Mexicans in "
          "the newly acquired lands, and KC-5.1.II.C reports increased interaction and "
          "conflict in the regions newly taken, altering these groups' economic "
          "self-sufficiency and cultures. Both sentences name those people, both place the "
          "changes after the taking, and neither makes the acquisition follow from them."),
]
