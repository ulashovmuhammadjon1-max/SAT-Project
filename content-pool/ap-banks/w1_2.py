# AP WORLD HISTORY: MODERN 1.2  (title copied verbatim from WORLD_HISTORY_topics.json.)
#
# THIS MODULE FOUND A REAL DEFECT AND THE NOTE IS KEPT BECAUSE OF IT. The JSON
# originally held "Developments in c. 1200 to c. 1450" -- the Course at a Glance
# table sets three units side by side, so this title's middle lines landed in a
# neighbouring column and were dropped, leaving something shorter but still
# grammatical. 1.1 was truncated to the SAME string. This module followed the
# brief and copied the JSON, while recording that the CED page read
# "Developments in Dar al-Islam from c. 1200 to c. 1450" -- which is what made
# the conflict visible. Twelve titles were wrong; extract_topics.py now refuses
# any list in which two topics share a title.
# Unit 1 The Global Tapestry. Suggested skill 1.A, identify and describe a historical
# concept, development, or process.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON:
#
#   LO 1.D  Explain how systems of belief and their practices affected society in the
#           period from c. 1200 to c. 1450.
#   KC-3.1.III.D.iii  Islam, Judaism, Christianity, and the core beliefs and practices
#           of these religions continued to shape societies in Africa and Asia.
#   LO 1.E  Explain the causes and effects of the rise of Islamic states over time.
#   KC-3.2.I  As the Abbasid Caliphate fragmented, new Islamic political entities
#           emerged, most of which were dominated by Turkic peoples. These states
#           demonstrated continuity, innovation, and diversity.
#   KC-3.1.III.A  Muslim rule continued to expand to many parts of Afro-Eurasia due to
#           military expansion, and Islam subsequently expanded through the activities
#           of merchants, missionaries, and Sufis.
#   LO 1.F  Explain the effects of intellectual innovation in Dar al-Islam.
#   KC-3.2.II.A.i  Muslim states and empires encouraged significant intellectual
#           innovations and transfers.
#
#   Thematic focus CDI: the development of ideas, beliefs, and religions illustrates
#           how groups in society view themselves, and the interactions of societies
#           and their beliefs often have political, social, and cultural implications.
#   Thematic focus GOV: governments obtain, retain, and exercise power in different
#           ways and for different purposes.
#   Thematic focus TEC: human adaptation and innovation have resulted in increased
#           efficiency, comfort, and security, and technological advances have shaped
#           human development and interactions with both intended and unintended
#           consequences.
#
#   Illustrative examples on this topic page: new Islamic political entities -- the
#   Seljuk Empire, the Mamluk sultanate of Egypt, the Delhi sultanates; innovations --
#   advances in mathematics, in literature and in medicine; transfers -- preservation
#   and commentaries on Greek moral and natural philosophy, the House of Wisdom in
#   Abbasid Bagdad, scholarly and cultural transfers in Muslim and Christian Spain.
#
# THE ORDER IN KC-3.1.III.A IS PART OF THE STATEMENT. Rule expanded by military means
# and Islam SUBSEQUENTLY expanded through merchants, missionaries and Sufis. A
# distractor that reverses those two halves is right about both processes and wrong
# only about their relation, which is the most dangerous shape a distractor takes in
# this subject -- so the anchors for those items carry both clauses.
#
# Stimuli are unattributed and illustrative, or HYPOTHETICAL tables whose keyed
# conclusion is recomputed from the table alone. No quotation is put in a real
# person's mouth.
TOPIC = ("1.2", "Developments in Dar al-Islam from c. 1200 to c. 1450", 1)

_T_LIBRARY = dict(
    headers=["Field of learning (hypothetical)", "Works in an earlier inventory",
             "Works in a later inventory"],
    rows=[["Mathematics", "40", "110"],
          ["Medicine", "30", "95"],
          ["Poetry", "60", "70"]])

_T_ARRIVALS = dict(
    headers=["Route (hypothetical)", "Merchants recorded in an earlier year",
             "Merchants recorded in a later year"],
    rows=[["Overland route", "120", "150"],
          ["Sea route", "80", "240"]])

_T_OFFICIALS = dict(
    headers=["State (hypothetical label)", "Years of rule recorded in one chronicle",
             "Officials of Turkic military background, per hundred named"],
    rows=[["State One", "95", "70"],
          ["State Two", "140", "55"],
          ["State Three", "60", "80"]])

QUESTIONS = [
 dict(q=("An unattributed chronicle from the period reports that the caliph continued to be "
         "named in the Friday prayer and on the coinage, while the commander of the garrison "
         "collected the revenues, appointed the governors and led the army on campaign. Which "
         "development does the chronicle best illustrate?"),
      choices=[
        "The fragmentation of the Abbasid Caliphate, out of which new Islamic political entities emerged holding real authority under a caliph who retained the older titles.",
        "The abolition of the caliphal office and its replacement by an assembly of merchants.",
        "The unification of all Islamic lands under a single administration for the first time.",
        "The transfer of political authority in Islamic lands to Christian rulers from Europe.",
        "The withdrawal of Islamic states from every region outside the Arabian peninsula.",
      ], ans=0,
      why=("KC-3.2.I states that as the Abbasid Caliphate fragmented, new Islamic political "
           "entities emerged, most of which were dominated by Turkic peoples. A caliph keeping "
           "the titles while another power holds the revenue and the army is that fragmentation; "
           "the CED asserts none of the four alternatives.")),

 dict(q=("Two students describe how Islam came to be practiced across much of Afro-Eurasia in "
         "this period. One says conquest did all the work; the other says trade and preaching "
         "did all of it. Which statement best corrects both of them?"),
      choices=[
        "Muslim rule continued to expand by military means, and Islam then spread further through the activities of merchants, missionaries and Sufis, so the two processes are successive rather than rival.",
        "Islam spread first through merchants and missionaries, and only afterward did any expansion of Muslim rule by military means occur.",
        "Neither military expansion nor the movement of merchants had any part in the spread of Islam in this period.",
        "Military expansion and preaching were carried out by the same personnel, so no distinction between them can be drawn.",
        "The spread of Islam in this period was confined to the lands already ruled by the Abbasid Caliphate.",
      ], ans=0,
      why=("KC-3.1.III.A states that Muslim rule continued to expand to many parts of "
           "Afro-Eurasia due to military expansion and that Islam SUBSEQUENTLY expanded through "
           "the activities of merchants, missionaries, and Sufis. The order in that sentence is "
           "what the second option reverses.")),

 dict(q=("A historian argues that the Islamic states which emerged in this period should not be "
         "treated as copies of one another. Which of the following, drawn from the framework's "
         "own characterization of those states, most directly supports the argument?"),
      choices=[
        "They demonstrated continuity, innovation and diversity, so shared inheritance and local difference are both part of their description.",
        "They were governed by a single administration operating from one capital.",
        "They adopted identical institutions because they emerged from the same caliphate.",
        "They were each founded in the same decade and lasted for the same span of years.",
        "They differed in name only, since their systems of rule were indistinguishable.",
      ], ans=0,
      why=("KC-3.2.I states that the new Islamic political entities demonstrated continuity, "
           "innovation, and diversity. Diversity is asserted in the same sentence that asserts "
           "continuity, so the four uniformity claims contradict the framework.")),

 dict(q=("Which of the following best states what the framework claims about religion in Africa "
         "and Asia during this period?"),
      choices=[
        "Islam, Judaism and Christianity, together with the core beliefs and practices of each, continued to shape societies there.",
        "Islam alone shaped societies there, the other traditions having disappeared from both regions.",
        "Religious belief ceased to influence society in these regions once new states emerged.",
        "Only rulers and their households retained any religious practice in these regions.",
        "The religions of these regions were newly introduced in this period and had no earlier presence.",
      ], ans=0,
      why=("KC-3.1.III.D.iii names Islam, Judaism, and Christianity together and says the core "
           "beliefs and practices of these religions continued to shape societies in Africa and "
           "Asia. Naming three traditions is exactly what the single-tradition option denies.")),

 dict(q=("A ruler in this period endows a college of learning, pays salaries to its teachers, "
         "and equips a library of copied manuscripts. Which of the following best describes what "
         "such patronage represents?"),
      choices=[
        "A Muslim state encouraging intellectual innovation and the transfer of learning, which the framework treats as an effect of state support rather than an accident.",
        "A religious prohibition on the study of subjects not contained in scripture.",
        "A commercial venture whose purpose was to sell manuscripts abroad at a profit.",
        "A military measure designed to garrison a frontier province.",
        "An arrangement by which scholarship was removed from the reach of the state.",
      ], ans=0,
      why=("KC-3.2.II.A.i states that Muslim states and empires encouraged significant "
           "intellectual innovations and transfers, and Learning Objective F asks for the "
           "effects of intellectual innovation in Dar al-Islam. Endowment, salary and library "
           "are that encouragement in concrete form.")),

 dict(q=("Scholars in this period copied older Greek works on moral and natural philosophy, "
         "wrote commentaries on them, and taught from both. A student who called this activity "
         "a transfer rather than an invention would be making which point?"),
      choices=[
        "That learning already produced elsewhere was preserved, interpreted and carried into new settings, which is a distinct achievement from originating it.",
        "That the scholars concerned contributed nothing beyond mechanical copying and added no interpretation.",
        "That the older works were composed in this period and only appeared to be older.",
        "That transferred learning is by definition less useful than newly invented learning.",
        "That no original work of any kind was produced in these societies during the period.",
      ], ans=0,
      why=("KC-3.2.II.A.i pairs intellectual innovations WITH transfers, and this topic's "
           "illustrative list names preservation and commentaries on Greek moral and natural "
           "philosophy as an example of a transfer. Commentary is interpretation, so the "
           "copying-only option misstates it.")),

 dict(q=("In the Iberian peninsula during this period, Muslim and Christian rulers held "
         "territory in proximity and scholars moved between their courts and schools. Which "
         "process does that situation best exemplify?"),
      choices=[
        "Scholarly and cultural transfer occurring where societies of different faiths were in sustained contact.",
        "The complete isolation of each religious community from the learning of the others.",
        "The replacement of all local learning by texts imported from a single distant capital.",
        "The prohibition of translation between languages by both sets of rulers.",
        "The confinement of scholarship in this period to communities with no political frontier near them.",
      ], ans=0,
      why=("KC-3.2.II.A.i states that Muslim states and empires encouraged significant "
           "intellectual innovations and transfers, and the topic's illustrative list names "
           "scholarly and cultural transfers in Muslim and Christian Spain as an instance. "
           "Contact is the condition the example points to.")),

 dict(q=("The framework treats advances in mathematics, in medicine and in literature during "
         "this period as belonging together. What do they have in common that justifies "
         "grouping them?"),
      choices=[
        "Each is an intellectual innovation of the kind Muslim states and empires are said to have encouraged.",
        "Each was produced by a single scholar working without any institutional support.",
        "Each was a military technology adopted for use on campaign.",
        "Each was a commercial practice devised for use by merchants in long-distance trade.",
        "Each was a form of administration by which revenue was assessed and collected.",
      ], ans=0,
      why=("KC-3.2.II.A.i states that Muslim states and empires encouraged significant "
           "intellectual innovations and transfers; the topic's illustrative list groups "
           "advances in mathematics, literature and medicine under exactly that heading. The "
           "other four categories belong to different key concepts.")),

 dict(q=("Sufis are named by the framework alongside merchants and missionaries as agents of "
         "the spread of Islam. What does including them in that list indicate about how "
         "religious change occurred?"),
      choices=[
        "That it proceeded partly through teaching and personal devotion carried by travelers, and not only through the extension of a state's rule.",
        "That it proceeded only where an army had first established a garrison in the district.",
        "That it was directed entirely by officials appointed for the purpose by the caliph.",
        "That it required the prior conversion of a ruler before any ordinary person could adopt the faith.",
        "That it occurred without any movement of people between regions.",
      ], ans=0,
      why=("KC-3.1.III.A names merchants, missionaries, and Sufis as the activities through "
           "which Islam subsequently expanded, distinguishing that expansion from the military "
           "expansion of Muslim rule in the same sentence. Teaching carried by travelers is what "
           "the second half describes.")),

 dict(q=("Which of the following would be the best evidence that the fragmentation of a large "
         "state need not mean the decline of the civilization it governed?"),
      choices=[
        "That the successor states which emerged continued established practices, added innovations of their own, and encouraged learning.",
        "That the successor states each ruled a smaller territory than the state they replaced.",
        "That the ruler of the older state kept his title after losing control of the revenue.",
        "That the number of separate rulers in the region increased.",
        "That the frontiers between the successor states were frequently disputed.",
      ], ans=0,
      why=("KC-3.2.I states that the entities emerging from the Abbasid fragmentation "
           "demonstrated continuity, innovation, and diversity, and KC-3.2.II.A.i credits Muslim "
           "states with encouraging intellectual innovations and transfers. Smaller territory "
           "and more rulers describe the fragmentation, not its consequences for learning.")),

 dict(q=("The table below sets out HYPOTHETICAL holdings of one library, by field of learning, "
         "at an earlier and a later inventory. Which conclusion do these numbers best support?"),
      table=_T_LIBRARY,
      choices=[
        "Holdings rose in every field listed, and mathematics and medicine each more than doubled while poetry did not.",
        "Holdings in poetry fell between the two inventories.",
        "Every field listed more than doubled its holdings between the two inventories.",
        "The field with the largest holdings at the earlier inventory grew by the largest multiple.",
        "Holdings in medicine were larger than holdings in mathematics at both inventories.",
      ], ans=0,
      why=("Recomputed in the verifier from the table alone; every alternative is false on the "
           "same numbers. KC-3.2.II.A.i is the process such a pattern would illustrate, since "
           "the framework credits Muslim states with encouraging intellectual innovation and "
           "the transfer of learning.")),

 dict(q=("HYPOTHETICAL counts of merchants arriving at one city by two routes, in an earlier "
         "and a later year, are given in the table below. Which statement is best supported by "
         "that data?"),
      table=_T_ARRIVALS,
      choices=[
        "Arrivals rose on both routes, and the sea route tripled while the overland route grew by a quarter.",
        "Arrivals on the overland route fell between the two years.",
        "The overland route carried more merchants than the sea route in the later year.",
        "Both routes grew by the same multiple between the two years.",
        "Arrivals on the sea route were higher than those on the overland route in both years.",
      ], ans=0,
      why=("Recomputed in the verifier: the sea route moves from eighty to two hundred and "
           "forty and the overland route from one hundred and twenty to one hundred and fifty. "
           "KC-3.1.III.A names merchants among the agents by which Islam expanded, which is why "
           "such movement matters to this topic.")),

 dict(q=("For three states of the period, the table below gives HYPOTHETICAL figures: the "
         "length of rule recorded in one chronicle, and the number of named officials of Turkic "
         "military background per hundred named. Which conclusion is best supported?"),
      table=_T_OFFICIALS,
      choices=[
        "A majority of the named officials in each state listed came from a Turkic military background, and the share differed from state to state.",
        "The same share of officials came from a Turkic military background in each state listed.",
        "In at least one state listed, officials of Turkic military background were a minority of those named.",
        "The state with the longest recorded rule had the largest share of such officials.",
        "The share of such officials rose as the recorded length of rule rose.",
      ], ans=0,
      why=("Recomputed in the verifier: the three shares are all above half and all differ. "
           "KC-3.2.I says the new Islamic political entities were MOST OF WHICH dominated by "
           "Turkic peoples and demonstrated diversity, so predominance with variation is the "
           "pattern the framework describes.")),

 dict(q=("A student is asked to identify a historical process rather than a single event in "
         "the material of this topic. Which of the following is a process?"),
      choices=[
        "The gradual expansion of Islam through the activities of merchants, missionaries and Sufis across many regions and generations.",
        "The naming of a particular caliph in the Friday prayer of a particular year.",
        "The appointment of one governor to one province.",
        "The completion of a single manuscript by a single copyist.",
        "The arrival of one merchant caravan at one city.",
      ], ans=0,
      why=("Suggested skill 1.A for this topic asks students to identify and describe a "
           "historical concept, development, or process, and KC-3.1.III.A describes the "
           "expansion of Islam as an extended development. The other four options are single "
           "datable acts.")),

 dict(q=("Why is it a mistake to treat the weakening of one caliphate as evidence that Islamic "
         "political life as a whole was weakening in this period?"),
      choices=[
        "Because new Islamic political entities emerged from that fragmentation and themselves demonstrated continuity, innovation and diversity.",
        "Because the caliphate in question did not in fact weaken at any point in the period.",
        "Because political life and religious life in this period had no bearing on one another.",
        "Because no new state anywhere in Afro-Eurasia was founded during this period.",
        "Because the framework treats every change in this period as an improvement.",
      ], ans=0,
      why=("KC-3.2.I puts the fragmentation and the emergence of new entities in one sentence "
           "and then credits those entities with continuity, innovation, and diversity. The "
           "decline of one state is therefore not the decline of the political world it "
           "belonged to.")),

 dict(q=("The framework says that most of the new Islamic political entities were dominated by "
         "Turkic peoples. Which of the following inferences does that wording license?"),
      choices=[
        "That Turkic domination was the prevailing pattern without being universal, so an entity outside that pattern would not contradict the statement.",
        "That every one of the new entities was ruled by a Turkic dynasty without exception.",
        "That Turkic peoples were a small minority among the rulers of the new entities.",
        "That the new entities were governed jointly by Turkic and Abbasid officials in equal numbers.",
        "That Turkic domination applied only to entities founded after 1400.",
      ], ans=0,
      why=("KC-3.2.I says MOST OF WHICH were dominated by Turkic peoples. The quantifier is the "
           "point: it asserts a prevailing pattern and stops short of a universal claim, and the "
           "CED's dates are approximate so no threshold year is implied.")),

 dict(q=("An unattributed traveler's report describes a market town far from any Muslim capital "
         "in which a group of resident traders keeps its own prayer hall and observes its own "
         "law among themselves. As evidence, this report bears most directly on which claim?"),
      choices=[
        "That the movement of merchants carried religious practice into places that no army had brought under Muslim rule.",
        "That religious practice in this period existed only under the direct authority of a Muslim state.",
        "That merchants in this period abandoned their own observances when trading abroad.",
        "That trade and religion in this period were carried on by entirely separate groups of people.",
        "That no community of foreign traders was permitted to settle outside its home region.",
      ], ans=0,
      why=("KC-3.1.III.A distinguishes the expansion of Muslim RULE by military means from the "
           "subsequent expansion of ISLAM through merchants, missionaries and Sufis. A trading "
           "community observing its faith beyond any Muslim state is the second process without "
           "the first.")),

 dict(q=("A comparison is drawn between the Song Dynasty of China and the Islamic states of "
         "this period. Which similarity is asserted by the framework about both?"),
      choices=[
        "Each is described as demonstrating continuity, innovation and diversity rather than as either static or wholly new.",
        "Each recruited its officials by a written examination on a shared body of classical texts.",
        "Each was ruled by a hereditary military elite drawn from beyond its own frontiers.",
        "Each governed a territory of the same extent and population.",
        "Each abandoned its inherited methods of rule during the course of the period.",
      ], ans=0,
      why=("KC-3.2.I.A uses the phrase continuity, innovation, and diversity of states in "
           "Afro-Eurasia and the Americas including the Song, and KC-3.2.I uses the same phrase "
           "of the new Islamic entities. The examination system is asserted of the Song alone.")),

 dict(q=("Which of the following questions about this topic could be settled by historical "
         "evidence rather than by a judgment of value?"),
      choices=[
        "Whether rulers in the period endowed institutions of learning and paid the scholars who taught in them.",
        "Whether rulers in the period were right to spend revenue on learning rather than on other things.",
        "Whether one religious tradition of the period offered a better account of the world than another.",
        "Whether the deference expected within households of the period was deserved.",
        "Whether conquest is ever a legitimate means of extending a state.",
      ], ans=0,
      why=("KC-3.2.II.A.i asserts that Muslim states and empires encouraged intellectual "
           "innovations and transfers, which is a matter of what was done and can be checked "
           "against evidence. The other four ask what was right, better or deserved.")),

 dict(q=("Considered as an effect rather than a cause, the growth of scholarship in Dar "
         "al-Islam in this period is best explained by which of the following?"),
      choices=[
        "The encouragement given by states and empires, which supported innovation and the transfer of learning from elsewhere.",
        "The absence of any state authority, which left scholars entirely to their own resources.",
        "The prohibition of contact with the learning of other societies, which forced originality.",
        "The concentration of all scholarship in a single city from which nothing circulated.",
        "The replacement of written transmission by memorization alone.",
      ], ans=0,
      why=("KC-3.2.II.A.i names Muslim states and empires as the agent that encouraged "
           "significant intellectual innovations and transfers, and Learning Objective F asks "
           "for the effects of that innovation. The alternatives each deny the support the "
           "framework credits.")),

 dict(q=("A student writes that belief systems in this period had consequences beyond private "
         "conduct. Which of the following would best support that sentence?"),
      choices=[
        "That the core beliefs and practices of Islam, Judaism and Christianity continued to shape whole societies in Africa and Asia, not only the conduct of individuals within them.",
        "That individual believers in these regions performed daily observances at home.",
        "That religious texts of the period were copied and preserved in libraries.",
        "That travelers in the period carried religious books with them on their journeys.",
        "That several religious traditions were present in the same region at the same time.",
      ], ans=0,
      why=("KC-3.1.III.D.iii says these religions continued to SHAPE SOCIETIES in Africa and "
           "Asia, and the Cultural Developments thematic focus says beliefs often have "
           "political, social and cultural implications. Society, not the individual, is the "
           "unit in that sentence.")),

 dict(q=("Which statement best captures what the framework means by calling the new Islamic "
         "entities continuous as well as innovative?"),
      choices=[
        "They carried forward inherited institutions and religious authority while also adopting arrangements their predecessors had not used.",
        "They preserved everything they inherited and adopted nothing new.",
        "They discarded everything they inherited and began from arrangements of their own devising.",
        "They alternated between periods of pure preservation and periods of pure novelty.",
        "They were continuous in religion and innovative in nothing else.",
      ], ans=0,
      why=("KC-3.2.I says the new entities demonstrated continuity, innovation, and diversity, "
           "listing the three together rather than in alternation. Holding all three at once is "
           "the framework's characterization, and each rejected option drops one of them.")),

 dict(q=("A historian claims that innovation in this period had consequences its makers did not "
         "intend. Which of the following best explains why such a claim is compatible with the "
         "framework's treatment of technology and innovation?"),
      choices=[
        "Because the framework states that technological advances have shaped human development and interactions with both intended and unintended consequences.",
        "Because the framework holds that innovation in this period had no consequences at all.",
        "Because the framework treats every consequence of an innovation as foreseen by those who made it.",
        "Because the framework confines the study of innovation to the period after 1450.",
        "Because the framework treats innovation as a purely religious activity.",
      ], ans=0,
      why=("The Technology and Innovation thematic focus states in terms that advances have "
           "shaped human development and interactions with both intended and unintended "
           "consequences, and KC-3.2.II.A.i places significant innovation in this period rather "
           "than after it.")),

 dict(q=("Suppose a source records that a ruler's armies took a province and that, a century "
         "later, most of its inhabitants observed Islam although few of them had ever seen a "
         "soldier. What does that sequence best illustrate?"),
      choices=[
        "That the expansion of Muslim rule and the later spread of the faith among a population were distinct processes working on different timescales.",
        "That conquest and religious change always occurred simultaneously and cannot be separated.",
        "That religious change in this period preceded and caused the movement of armies.",
        "That a population's religion changed only where soldiers were permanently stationed.",
        "That the framework treats religious change as unrelated to any historical process.",
      ], ans=0,
      why=("KC-3.1.III.A separates military expansion of Muslim rule from the subsequent "
           "expansion of Islam through merchants, missionaries and Sufis. The anchor for this "
           "item carries both halves because the third option is the same pair of processes with "
           "their order reversed.")),

 dict(q=("Which of the following best describes the relation between political power and "
         "learning in Dar al-Islam as the framework presents it?"),
      choices=[
        "States and empires were an active source of encouragement for innovation and for the transfer of learning, rather than bystanders to it.",
        "States and empires suppressed learning wherever it appeared within their territories.",
        "Learning flourished only in the intervals when no state exercised authority.",
        "Learning and political power were maintained by separate populations that had no contact.",
        "States collected learning already produced elsewhere but never supported its production.",
      ], ans=0,
      why=("KC-3.2.II.A.i states that Muslim states and empires ENCOURAGED significant "
           "intellectual innovations and transfers. Encouragement of both production and "
           "transfer is what the sentence asserts, and the last option keeps only half of it.")),

 dict(q=("A textbook lists the Seljuk Empire, the Mamluk sultanate of Egypt and the Delhi "
         "sultanates together. On the framework's terms, what is the point of that grouping?"),
      choices=[
        "They are instances of the new Islamic political entities that emerged as the Abbasid Caliphate fragmented.",
        "They are instances of states that rejected Islam as a basis of rule.",
        "They are instances of maritime empires established after 1450.",
        "They are instances of states in the Americas that expanded in scope and reach.",
        "They are the only three states of any kind that existed in Afro-Eurasia in this period.",
      ], ans=0,
      why=("KC-3.2.I describes the emergence of new Islamic political entities as the Abbasid "
           "Caliphate fragmented, and this topic's illustrative list names those three as "
           "examples of exactly that category. Maritime empires belong to a later unit.")),

 dict(q=("What would most weaken a claim that intellectual life in this period depended "
         "entirely on contact with other societies?"),
      choices=[
        "Evidence of original advances made within these societies in mathematics, medicine and literature alongside the transfers received from elsewhere.",
        "Evidence that Greek works were preserved and provided with commentaries.",
        "Evidence that scholars moved between Muslim and Christian courts in the Iberian peninsula.",
        "Evidence that a library's holdings included works translated from other languages.",
        "Evidence that rulers sent for manuscripts held in distant cities.",
      ], ans=0,
      why=("KC-3.2.II.A.i names innovations AND transfers as two things Muslim states "
           "encouraged, and this topic's illustrative list separates innovations in mathematics, "
           "literature and medicine from the transfers beside them. The rejected options are all "
           "instances of transfer.")),

 dict(q=("A student asks whether the processes studied in this topic stopped at the end of the "
         "period. Which answer is most consistent with the framework's own statement about its "
         "dates?"),
      choices=[
        "Processes such as the spread of a religion and the movement of learning may begin before the period and continue after it, since the given dates are approximate.",
        "Every process studied began and ended within the stated dates.",
        "A process that continued after 1450 is by that fact excluded from this period's subject matter.",
        "The dates given are legal boundaries that rulers of the period themselves recognized.",
        "The framework forbids describing any process as continuing across the end of a period.",
      ], ans=0,
      why=("The CED states that events, processes, and developments are not constrained by the "
           "given dates and may begin before, or continue after, the period; KC-3.1.III.D.iii's "
           "word CONTINUED, used of three religions, is itself an instance of a process older "
           "than the period.")),

 dict(q=("Which of the following pairs a cause with an effect in the way Learning Objective E "
         "asks students to do for the rise of Islamic states?"),
      choices=[
        "The fragmentation of a large caliphate, followed by the emergence of new political entities that governed its former territories.",
        "The emergence of new political entities, followed by the founding of the caliphate they replaced.",
        "The copying of manuscripts, followed by the collapse of the states that paid for it.",
        "The arrival of merchants in a city, followed by the disappearance of its markets.",
        "The endowment of a college, followed by the prohibition of teaching within it.",
      ], ans=0,
      why=("Learning Objective E asks for the causes and effects of the rise of Islamic states, "
           "and KC-3.2.I supplies the pair directly: as the Abbasid Caliphate fragmented, new "
           "Islamic political entities emerged. The second option reverses that order.")),

 dict(q=("Taken together, the developments studied in this topic best support which "
         "generalization about the period from c. 1200 to c. 1450?"),
      choices=[
        "Political division and cultural vitality occurred together, since states that emerged from a fragmenting caliphate encouraged learning and religious traditions continued to shape whole societies.",
        "Political division and cultural vitality are incompatible, so the period saw a decline in both.",
        "Cultural vitality in the period depended on the survival of a single unified state.",
        "Religious traditions in the period ceased to influence society once political authority divided.",
        "The period saw no innovation in learning and no change in political authority.",
      ], ans=0,
      why=("KC-3.2.I, KC-3.2.II.A.i and KC-3.1.III.D.iii assert respectively that new entities "
           "emerged from fragmentation, that Muslim states encouraged intellectual innovation "
           "and transfers, and that three religions continued to shape societies in Africa and "
           "Asia. All three hold in the same period.")),
]
