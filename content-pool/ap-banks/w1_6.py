# AP WORLD HISTORY: MODERN 1.6 Developments in Europe from c. 1200 to c. 1450
# (title copied verbatim from WORLD_HISTORY_topics.json -- this is one of the twelve
# titles corrected after the truncation bug, and the JSON is trusted over anything
# reconstructed from the CED dump, whose topic pages print a title split across three
# lines of a narrow column). Unit 1 The Global Tapestry, c. 1200 to c. 1450.
# Suggested skill 1.A, identify a historical concept, development, or process.
#
# THE CED CONTENT OF THIS TOPIC, IN FULL. The page carries three thematic focus
# blocks and three learning objectives, each with one historical development:
#
#   Thematic focus CDI: the development of ideas, beliefs, and religions illustrates
#           how groups in society view themselves, and the interactions of societies
#           and their beliefs often have political, social, and cultural implications.
#   LO 1.K  Explain how the beliefs and practices of the predominant religions in
#           Europe affected European society.
#   KC-3.1.III.D.v  Christianity, Judaism, Islam, and the core beliefs and practices
#           of these religions continued to shape societies in Europe.
#
#   Thematic focus GOV: a variety of internal and external factors contribute to state
#           formation, expansion, and decline. Governments maintain order through a
#           variety of administrative institutions, policies, and procedures, and
#           governments obtain, retain, and exercise power in different ways and for
#           different purposes.
#   LO 1.L  Explain the causes and consequences of political decentralization in
#           Europe from c. 1200 to c. 1450.
#   KC-3.2.I.B.ii  Europe was politically fragmented and characterized by decentralized
#           monarchies, feudalism, and the manorial system.
#
#   Thematic focus SIO: the process by which societies group their members and the
#           norms that govern the interactions between these groups and between
#           individuals influence political, economic, and cultural institutions and
#           organization.
#   LO 1.M  Explain the effects of agriculture on social organization in Europe from
#           c. 1200 to c. 1450.
#   KC-3.3.III.C  Europe was largely an agricultural society dependent on free and
#           coerced labor, including serfdom.
#
# THIS TOPIC PAGE PRINTS NO ILLUSTRATIVE EXAMPLES AT ALL -- checked in the framework
# text, not assumed. So there is not even a named instance to lean on, and every key
# below rests on one of those three sentences or on a thematic focus statement. A
# great deal is known about Europe in these centuries that the CED does not assert;
# none of it is keyed here, because a key resting on it could not be checked by anyone
# reading this bank later.
#
# THE SUGGESTED SKILL SHAPES THE BANK. Skill 1.A is to IDENTIFY a concept,
# development or process, so these items put a source or a situation in front of the
# student and ask which development it is an instance of -- deliberately a different
# shape from topic 1.5, whose skill is 1.B and whose items ask for an explanation, and
# from topic 1.7, whose skill is 6.A and whose items ask which claim is defensible.
#
# ON THE SOURCES. Section I of this exam is stimulus based and this bank cannot show
# an image, so every stimulus here is either a table of HYPOTHETICAL figures whose
# keyed conclusion is recoverable from the table alone, or an explicitly unattributed
# illustrative source. Nothing is put into a real person's mouth.
#
# ON DATES. Spans are written "c. 1200 to c. 1450". The CED states that events,
# processes, and developments are not constrained by the given dates and may begin
# before, or continue after, the period, so no key here turns on a boundary year.
TOPIC = ("1.6", "Developments in Europe from c. 1200 to c. 1450", 1)

_T_MANOR = dict(
    headers=["Manor (hypothetical)", "Households owing labor service on the lord's own fields",
             "Households holding their land for a money rent"],
    rows=[["Manor One", "40", "10"],
          ["Manor Two", "25", "25"],
          ["Manor Three", "12", "48"]])

_T_DUES = dict(
    headers=["Region (hypothetical)", "Districts where the monarch's officers collected dues directly",
             "Districts where a lord collected the dues and forwarded a share"],
    rows=[["Region One", "3", "12"],
          ["Region Two", "5", "10"],
          ["Region Three", "2", "18"]])

_T_VILLAGE = dict(
    headers=["Village (hypothetical)", "Households whose main work is cultivation (percent)",
             "Households whose main work is a craft (percent)"],
    rows=[["Village One", "90", "10"],
          ["Village Two", "85", "15"],
          ["Village Three", "78", "22"]])

QUESTIONS = [
 dict(q=("An unattributed survey of a lordship, written for the use of its steward, records "
         "that a stretch of country is held of the king by a count, that the count has granted "
         "portions of it to knights who owe him service for what they hold, and that each "
         "portion is worked by tenants of the estate to which it belongs. Which of the "
         "following identifies the development this survey records?"),
      choices=[
        "A politically fragmented Europe characterized by decentralized monarchies, by holding land in return for service, and by the estate as the unit of cultivation.",
        "A single centralized monarchy that administered every district directly through salaried officers of its own.",
        "A commercial order in which land was held only by purchase and sale and carried no obligation of service.",
        "An arrangement in which religious institutions held all land and no lay lord held any.",
        "A territory in which the monarch held no land and exercised no authority of any kind.",
      ], ans=0,
      why=("KC-3.2.I.B.ii states that Europe was politically fragmented and characterized by "
           "decentralized monarchies, feudalism, and the manorial system. The survey shows all "
           "three at once: a king above a count, land held for service, and an estate worked by "
           "its tenants. Each rejected option denies the sentence's own terms.")),

 dict(q=("Which of the following identifies what the term political fragmentation names when it "
         "is applied to Europe in this period?"),
      choices=[
        "A condition in which authority over territory was divided among many holders rather than gathered into one hand.",
        "A condition in which a territory was governed by no authority whatever.",
        "A condition in which one ruler governed several distant territories at the same time.",
        "A condition in which authority over territory was exercised by religious institutions alone.",
        "A condition in which every district was governed by an assembly chosen by those who lived in it.",
      ], ans=0,
      why=("KC-3.2.I.B.ii calls Europe politically fragmented and characterizes it by "
           "decentralized monarchies, and Learning Objective L asks for the causes and "
           "consequences of political DECENTRALIZATION. Division of authority is what the two "
           "words share; absence of authority is a different claim the framework does not make.")),

 dict(q=("An unattributed record of a European town in this period lists a church served by its "
         "clergy, a Jewish community whose members settle disputes among themselves before their "
         "own elders, and merchants of the Muslim faith who trade in the market on stated days. "
         "Which of the following identifies the development the record illustrates?"),
      choices=[
        "Christianity, Judaism and Islam, and the core beliefs and practices of those religions, continued to shape societies in Europe.",
        "Christianity alone shaped European societies in this period, the others being absent from Europe.",
        "The three traditions had each reached Europe for the first time during this period.",
        "European society in this period was organized without reference to any religious tradition.",
        "The three traditions were practiced in Europe only by people who held no property there.",
      ], ans=0,
      why=("KC-3.1.III.D.v names Christianity, Judaism, Islam and the core beliefs and practices "
           "of these religions as continuing to shape societies in Europe. All three are named "
           "in that sentence, and the word CONTINUED rules out a first arrival within the "
           "period.")),

 dict(q=("An unattributed statement of the customs of an estate says that certain households "
         "hold their land in return for a fixed number of days of work each year on the lord's "
         "own fields and may not depart without his licence, while other households on the same "
         "estate pay a money rent and are free to go. Which of the following identifies the "
         "development the statement records?"),
      choices=[
        "An agricultural society that depended on free and on coerced labor together, serfdom being among the coerced forms.",
        "An agricultural society whose labor was entirely coerced, no free arrangement existing anywhere.",
        "An agricultural society whose labor was entirely free, no coerced arrangement existing anywhere.",
        "A society in which cultivation had ceased to be the principal work of the population.",
        "A society in which land was worked only by people hired for a season and holding nothing.",
      ], ans=0,
      why=("KC-3.3.III.C states that Europe was largely an agricultural society dependent on "
           "free and coerced labor, including serfdom. Both kinds appear on the one estate in "
           "the statement, which is exactly the pairing the sentence makes; the first two "
           "rejected options each delete one half of it.")),

 dict(q=("Learning Objective L asks for the causes and the consequences of political "
         "decentralization in Europe. Which of the following would be a CONSEQUENCE of "
         "decentralization rather than a cause of it?"),
      choices=[
        "That a person seeking judgment in a dispute might have to seek it from the lord of his district rather than from the monarch.",
        "That the monarch lacked the officers and the revenue to administer distant districts himself.",
        "That grants of land for service were the means by which rulers secured armed followers.",
        "That the difficulty of moving men and messages across country limited what a center could supervise.",
        "That an inheritance divided among heirs left authority in more hands than before.",
      ], ans=0,
      why=("Learning Objective L distinguishes causes from consequences, and KC-3.2.I.B.ii "
           "states that Europe was politically fragmented and characterized by decentralized "
           "monarchies and feudalism. Where a subject must go for justice follows from that "
           "division of authority; the other four options are conditions that produce it.")),

 dict(q=("A student writes that a decentralized monarchy is a monarchy that has ceased to exist. "
         "Which of the following identifies the error?"),
      choices=[
        "Decentralization describes how far authority is dispersed within a monarchy, so a monarchy may be decentralized and still be a monarchy.",
        "Decentralization describes the size of a monarchy's territory, so a decentralized monarchy is simply a small one.",
        "Decentralization describes the religion of a monarchy, so the student has confused two different subjects.",
        "Decentralization describes the length of a monarch's reign, so the term has no bearing on authority at all.",
        "Decentralization is the framework's term for a territory that has no monarch, so the student is correct.",
      ], ans=0,
      why=("KC-3.2.I.B.ii speaks of DECENTRALIZED MONARCHIES, a phrase that would be "
           "self-contradictory if decentralization meant the end of monarchy. The Governance "
           "thematic focus likewise treats how power is exercised as separate from whether a "
           "government exists.")),

 dict(q=("The table below carries HYPOTHETICAL figures for three estates, giving the number of "
         "households that owe labor service on the lord's own fields and the number that hold "
         "their land for a money rent. Which conclusion do these numbers support?"),
      table=_T_MANOR,
      choices=[
        "Each estate listed records households of both kinds, and the share owing labor service falls from the first estate to the third.",
        "Each estate listed records households of one kind only.",
        "The share of households owing labor service rises from the first estate to the third.",
        "On every estate listed, households paying a money rent outnumber those owing labor service.",
        "The estate with the most households owing labor service also has the most paying a money rent.",
      ], ans=0,
      why=("Recomputed in the verifier from the table alone, distractors included. KC-3.3.III.C "
           "states that Europe was largely an agricultural society dependent on free AND coerced "
           "labor, and two arrangements present together in differing proportions is what such a "
           "dependence looks like in figures. The numbers are hypothetical and the stem says so.")),

 dict(q=("HYPOTHETICAL counts for three regions of one kingdom are set out in the table below, "
         "giving the districts in which the monarch's own officers collected dues directly and "
         "the districts in which a lord collected them and forwarded a share. Which conclusion "
         "does the data best support?"),
      table=_T_DUES,
      choices=[
        "In every region listed the districts collected through a lord outnumber those collected directly, and the gap between the two is widest in the third region.",
        "In every region listed the districts collected directly outnumber those collected through a lord.",
        "In one of the regions listed the two kinds of district are equal in number.",
        "The gap between the two kinds of district is widest in the first region listed.",
        "The region with the most directly collected districts also has the most collected through a lord.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.2.I.B.ii characterizes Europe "
           "by decentralized monarchies, and revenue reaching a monarch mostly through "
           "intermediaries rather than through his own officers is what decentralization looks "
           "like in an administrative record. The anchor carries both clauses of the key.")),

 dict(q=("For three villages the table below gives HYPOTHETICAL shares of households by their "
         "main work. Which statement is best supported by that data?"),
      table=_T_VILLAGE,
      choices=[
        "Cultivation is the main work of more than three quarters of households in every village listed.",
        "In one of the villages listed, fewer than half the households have cultivation as their main work.",
        "In the village with the largest craft share, craft households outnumber cultivating households.",
        "The three villages listed have the same share of households in cultivation.",
        "The village with the largest craft share also has the largest cultivating share.",
      ], ans=0,
      why=("Recomputed in the verifier from the table alone. KC-3.3.III.C states that Europe was "
           "LARGELY an agricultural society, and a large majority of households in cultivation "
           "with a smaller craft population is what the word largely describes.")),

 dict(q=("Which of the following identifies a claim about Europe in this period that KC-3.1.III.D.v "
         "does NOT make?"),
      choices=[
        "That the three religious traditions it names were equal in the number of their adherents in Europe.",
        "That Christianity continued to shape societies in Europe.",
        "That Judaism continued to shape societies in Europe.",
        "That Islam continued to shape societies in Europe.",
        "That the core beliefs and practices of those traditions, and not their names alone, shaped European societies.",
      ], ans=0,
      why=("KC-3.1.III.D.v states that Christianity, Judaism, Islam, and the core beliefs and "
           "practices of these religions continued to shape societies in Europe. It names three "
           "traditions and their practices; it says nothing whatever about their relative "
           "numbers, so a key resting on numbers would rest on something the CED does not assert.")),

 dict(q=("An unattributed account of a dispute over a mill records that the case was heard in the "
         "court of the lord on whose land the mill stood, that his officers summoned the parties, "
         "and that his judgment was enforced by his own men. Which of the following identifies "
         "what the account shows about government in this period?"),
      choices=[
        "That the institutions through which order was maintained could belong to a lord rather than to the monarch, which is what decentralized authority means in practice.",
        "That the monarch personally heard every dispute that arose within his kingdom.",
        "That disputes in this period were settled without any institution or procedure at all.",
        "That the enforcement of judgments was reserved to religious institutions.",
        "That a lord holding a court was thereby acting against the monarch's authority.",
      ], ans=0,
      why=("The Governance thematic focus states that governments maintain order through a "
           "variety of administrative institutions, policies, and procedures, and KC-3.2.I.B.ii "
           "characterizes Europe by decentralized monarchies and feudalism. A lord's court is one "
           "of that variety; the framework does not describe it as a rebellion against the crown.")),

 dict(q=("Which of the following identifies the relationship the framework asserts between "
         "agriculture and social organization in Europe in this period?"),
      choices=[
        "That the work of cultivation, and the free and coerced arrangements under which it was done, shaped how the society grouped its members.",
        "That social organization in Europe was settled independently of how the land was worked.",
        "That agriculture in Europe was carried on by a single class holding a single kind of obligation.",
        "That the arrangements under which land was worked were the same everywhere in Europe.",
        "That social organization determined the crops that were grown and nothing else.",
      ], ans=0,
      why=("Learning Objective M asks for the effects of agriculture on social organization in "
           "Europe, KC-3.3.III.C states that Europe was largely an agricultural society dependent "
           "on free and coerced labor including serfdom, and the Social Interactions thematic "
           "focus says the way a society groups its members influences its institutions.")),

 dict(q=("A traveler's notebook of the period, its author unnamed, remarks that a journey of a "
         "few days took the writer through the lands of four different lords, each with his own "
         "custom for the tolls charged on the road. Which of the following identifies the "
         "development the remark illustrates?"),
      choices=[
        "Political fragmentation, since authority over the road was divided among several holders rather than exercised by one.",
        "The absence of any authority over the road, since tolls were charged without any right to charge them.",
        "The consolidation of authority in a single monarchy, since the tolls were of the same kind throughout.",
        "The transfer of authority over roads from lay lords to religious institutions.",
        "The extension of a single custom across the whole of Europe.",
      ], ans=0,
      why=("KC-3.2.I.B.ii states that Europe was politically fragmented and characterized by "
           "decentralized monarchies. Several holders each exercising authority over a stretch of "
           "one road, on their own terms, is that fragmentation in miniature.")),

 dict(q=("A student claims that because Europe was politically fragmented, it had no governments "
         "in this period. Which of the following identifies the strongest objection?"),
      choices=[
        "That fragmentation describes how authority was distributed, and the framework describes governments in Europe maintaining order through institutions and procedures throughout.",
        "That the framework denies that Europe was politically fragmented in this period.",
        "That fragmentation and centralization are the same condition under two names.",
        "That governments existed only in those parts of Europe that were not fragmented.",
        "That the question cannot be settled because no records of government survive from the period.",
      ], ans=0,
      why=("KC-3.2.I.B.ii asserts fragmentation and decentralized MONARCHIES in the same clause, "
           "and the Governance thematic focus states that governments maintain order through a "
           "variety of administrative institutions, policies, and procedures. Fragmentation is a "
           "description of distribution, not of absence.")),

 dict(q=("An unattributed charter grants a holding to a man and to his heirs, to be held of the "
         "grantor, in return for attendance with arms when summoned. Which of the following "
         "identifies the concept the charter exemplifies?"),
      choices=[
        "Land held on condition of service owed to the grantor, which is the arrangement the framework names as part of Europe's political character.",
        "Land sold outright for a price, carrying no continuing obligation to anyone.",
        "Land held by a religious institution in return for prayers said for the grantor.",
        "Land taken by force and held without any grant or title.",
        "Land held directly of the monarch by every person who cultivated it.",
      ], ans=0,
      why=("KC-3.2.I.B.ii names feudalism among the characteristics of a politically fragmented "
           "Europe. A grant of land held OF a grantor in return for armed service is the "
           "conditional tenure that term denotes; an outright sale carries no such condition.")),

 dict(q=("Which of the following identifies the difference between the two labor arrangements "
         "the framework pairs in describing European agriculture?"),
      choices=[
        "The one leaves the worker able to withhold his labor or depart, and the other binds him to render it, both being found in the same agricultural society.",
        "The one is found in agriculture and the other only in the towns, so the two never appear together.",
        "The one belongs to the earlier part of the period and the other to the later, so the two never coexisted.",
        "The one applies to men and the other to women, so the pair describes a division by sex rather than by obligation.",
        "The two are the same arrangement described in different words, so no difference is being asserted.",
      ], ans=0,
      why=("KC-3.3.III.C states that Europe was largely an agricultural society dependent on free "
           "AND coerced labor, including serfdom. The sentence pairs the two within one "
           "agricultural society, so neither a separation by place nor a separation in time nor "
           "an identity between them follows from it.")),

 dict(q=("An unattributed set of household instructions from a European community of this period "
         "sets the days on which no work is to be done, the fasts that are to be kept, and the "
         "occasions on which the household is to give to the poor. Which of the following "
         "identifies what such a text shows?"),
      choices=[
        "That the core beliefs and practices of a religion ordered ordinary conduct and not only formal worship, which is how a belief system shapes a society.",
        "That religious practice in this period was confined to those in religious orders.",
        "That the household concerned was governed by the monarch rather than by any lord.",
        "That religious traditions in Europe left the arrangement of daily life untouched.",
        "That instructions of this kind were addressed only to those who could read.",
      ], ans=0,
      why=("KC-3.1.III.D.v names the core beliefs AND PRACTICES of Christianity, Judaism and "
           "Islam as continuing to shape societies in Europe, and the Cultural Developments "
           "thematic focus states that beliefs illustrate how groups view themselves and carry "
           "social implications. Days of rest, fasts and almsgiving are practices ordering "
           "conduct.")),

 dict(q=("Which of the following identifies a question about Europe in this period that could be "
         "settled by evidence rather than by a judgment of value?"),
      choices=[
        "Whether the households of a given estate owed days of work as well as a money rent.",
        "Whether it was just that some households owed days of work to a lord.",
        "Whether a decentralized monarchy is a better form of government than a centralized one.",
        "Whether the obligations of a tenant to his lord were deserved.",
        "Whether one religious tradition in Europe taught a truer doctrine than another.",
      ], ans=0,
      why=("KC-3.3.III.C asserts matters of fact about the arrangements under which land was "
           "worked in Europe, and Learning Objective M asks for the effects of agriculture on "
           "social organization. What a household owed can be checked against a record; justice, "
           "superiority, desert and doctrinal truth cannot be settled by observation.")),

 dict(q=("A historian argues that European political decentralization in this period had more "
         "than one cause. Which of the following would most strengthen that argument?"),
      choices=[
        "Evidence that the limits on a center's revenue, the difficulty of communication across country, and the practice of granting land for service each contributed, and that removing any one leaves the pattern unexplained.",
        "Evidence that one particular kingdom was more fragmented than its neighbors.",
        "Evidence that fragmentation was recorded in the writings of contemporaries.",
        "Evidence that the process can be dated to a single decade.",
        "Evidence that a single lord held more land than the monarch did.",
      ], ans=0,
      why=("The Governance thematic focus states that a VARIETY of internal and external factors "
           "contribute to state formation, expansion, and decline, and Learning Objective L asks "
           "for the causes of political decentralization in Europe. A multi-cause account is "
           "strengthened by evidence about the causes, not by a fact about one case.")),

 dict(q=("Which of the following identifies what makes an estate rather than a kingdom the unit "
         "of description in an account of European cultivation in this period?"),
      choices=[
        "That the obligations under which land was worked were fixed by the custom of the estate on which it lay, so the estate is where those obligations can be observed.",
        "That kingdoms in this period contained only one estate each, so the two units are the same.",
        "That cultivation in this period was directed centrally from each kingdom's capital.",
        "That the estate was a religious rather than an agricultural institution.",
        "That the framework describes European agriculture without reference to any unit of organization.",
      ], ans=0,
      why=("KC-3.2.I.B.ii names the manorial system among the characteristics of Europe in this "
           "period and KC-3.3.III.C describes an agricultural society dependent on free and "
           "coerced labor. The estate is the unit those two sentences meet in; the framework "
           "nowhere describes cultivation as centrally directed.")),

 dict(q=("An unattributed chronicle of a European kingdom notes that when the monarch wished to "
         "raise a force, he sent to his greater men, and each came with such followers as he "
         "could bring. Which of the following identifies what this shows about how power was "
         "exercised?"),
      choices=[
        "That the monarch's capacity to act depended on intermediaries who brought their own followings, rather than on a force he raised and paid directly.",
        "That the monarch had no capacity to raise a force under any circumstances.",
        "That the greater men were officers appointed by the monarch and removable at his word.",
        "That military service in this period was owed by every inhabitant directly to the monarch.",
        "That the monarch's forces were supplied by religious institutions.",
      ], ans=0,
      why=("KC-3.2.I.B.ii characterizes Europe by decentralized monarchies and feudalism, and the "
           "Governance thematic focus states that governments obtain, retain, and exercise power "
           "in different ways. Acting through men who bring their own followings is one of those "
           "ways and is what decentralization means for a monarch's reach.")),

 dict(q=("Which of the following identifies a continuity that the framework asserts about "
         "religion in Europe in this period?"),
      choices=[
        "That the traditions it names had been shaping European societies before this period and went on doing so within it.",
        "That the traditions it names entered Europe during this period and had no earlier presence.",
        "That the traditions it names ceased to shape European societies during this period.",
        "That the traditions it names were practiced without any change in their beliefs or practices ever.",
        "That the traditions it names were confined to a single region of Europe.",
      ], ans=0,
      why=("KC-3.1.III.D.v says that Christianity, Judaism, Islam and their core beliefs and "
           "practices CONTINUED to shape societies in Europe, and the CED states that "
           "developments are not constrained by the given dates and may begin before the period. "
           "Continuing is not the same as never changing, which is the fourth option's error.")),

 dict(q=("Two students describe the same estate. One says its tenants were unfree; the other says "
         "some of its tenants were free. Which of the following identifies how the framework "
         "allows both statements to be about the same society?"),
      choices=[
        "The framework describes a society dependent on free and coerced labor together, so an estate may hold households of both conditions at once.",
        "The framework describes a society whose labor was wholly coerced, so the second student is describing a different period.",
        "The framework describes a society whose labor was wholly free, so the first student is describing a different region.",
        "The framework treats free and coerced labor as two names for one condition, so the students are not disagreeing.",
        "The framework makes no statement about labor in Europe, so neither student can be assessed.",
      ], ans=0,
      why=("KC-3.3.III.C states that Europe was largely an agricultural society dependent on free "
           "and coerced labor, including serfdom. The sentence joins the two conditions within "
           "one society, which is what allows both descriptions to hold of the same estate.")),

 dict(q=("Which of the following identifies the sense in which the framework calls Europe in this "
         "period largely an agricultural society?"),
      choices=[
        "That cultivation was the work of most of its people, without the claim that no other work was done.",
        "That cultivation was the only work done anywhere in Europe in this period.",
        "That Europe produced more food than any other region of the world.",
        "That agriculture in Europe was organized by a single authority across the continent.",
        "That agriculture had only recently become the principal work of Europeans.",
      ], ans=0,
      why=("KC-3.3.III.C uses the word LARGELY, which asserts predominance and not exclusivity, "
           "and Learning Objective M asks for the effects of agriculture on social organization "
           "rather than for a comparison of regions by output. The other four options each add a "
           "claim the sentence does not make.")),

 dict(q=("An unattributed petition asks a lord to confirm that the customs of an estate are as "
         "they were in his father's time. Which of the following identifies what the petition "
         "reveals about how obligations on such an estate were understood?"),
      choices=[
        "That they were held to rest on established custom, which is why an appeal to how things had been done was worth making.",
        "That they were fixed by a statute of the monarch applying uniformly across the kingdom.",
        "That they were settled anew by each lord on his accession with no reference to what preceded.",
        "That they were regarded as matters of no importance to those who owed them.",
        "That they were determined by the tenants themselves without reference to the lord.",
      ], ans=0,
      why=("KC-3.2.I.B.ii names the manorial system as a characteristic of Europe in this period "
           "and the Governance thematic focus names policies and procedures among the means by "
           "which order is maintained. An appeal to what was done before is an appeal to custom "
           "as the ground of an obligation.")),

 dict(q=("Which of the following identifies a difference between the situation KC-3.2.I.B.ii "
         "describes for Europe and the situation KC-3.2.I.A describes for the Song Dynasty of "
         "China?"),
      choices=[
        "Europe is described as politically fragmented, while the Song are described as maintaining rule through an imperial bureaucracy.",
        "Europe is described as maintaining rule through an imperial bureaucracy, while the Song are described as politically fragmented.",
        "Both are described as politically fragmented, so no difference is asserted between them.",
        "Both are described as governed through an imperial bureaucracy, so no difference is asserted between them.",
        "Neither is described in terms of how its government was organized.",
      ], ans=0,
      why=("KC-3.2.I.B.ii states that Europe was politically fragmented and characterized by "
           "decentralized monarchies, feudalism, and the manorial system, while KC-3.2.I.A states "
           "that the Song utilized traditional methods of Confucianism and an imperial "
           "bureaucracy to maintain and justify its rule. The anchor carries both halves because "
           "the strongest distractor is the same pair exchanged.")),

 dict(q=("A historian wishes to show that religious traditions in Europe had political as well as "
         "private effects. Which of the following would be the most direct evidence?"),
      choices=[
        "A record of a religious institution holding land and exercising over it the same kind of authority a lay lord exercised over his.",
        "A record of the number of copies made of a devotional text.",
        "A record of the days on which a market was held in a town.",
        "A record of a household observing a fast.",
        "A record of the crops sown on an estate in a given year.",
      ], ans=0,
      why=("The Cultural Developments thematic focus states that the interactions of societies "
           "and their beliefs often have political, social, and cultural implications, "
           "KC-3.1.III.D.v names the religions shaping European societies, and KC-3.2.I.B.ii "
           "makes lordship over land the political question of the period.")),

 dict(q=("Which of the following identifies the reason a claim about Europe in this period cannot "
         "be established simply by finding one estate where it holds?"),
      choices=[
        "Because the framework's statements are about European society at large, and a single estate may be unrepresentative of it.",
        "Because records of individual estates from this period are always unreliable.",
        "Because the framework's statements concern only the towns and not the countryside.",
        "Because a claim about a society can never be supported by evidence from any particular place.",
        "Because the framework treats every estate in Europe as identical to every other.",
      ], ans=0,
      why=("KC-3.3.III.C and KC-3.2.I.B.ii both make general statements about Europe, and the "
           "Social Interactions thematic focus concerns how a society groups its members. A "
           "general claim is supported by particular evidence but is not established by one "
           "instance, which is a matter of scale rather than of the record's reliability.")),

 dict(q=("An unattributed account of a European community records that its members were subject "
         "in some matters to the authority of their own tradition's law and in others to the lord "
         "of the place where they lived. Which of the following identifies what this shows?"),
      choices=[
        "That a person could stand under more than one authority at once, which is consistent both with religious traditions shaping European society and with authority over territory being divided.",
        "That religious authority and lordship over territory were exercised by the same person in every case.",
        "That no authority of any kind reached the community described.",
        "That the community was outside the territory of any lord.",
        "That the framework treats religious tradition and territorial lordship as alternatives, only one of which could apply.",
      ], ans=0,
      why=("KC-3.1.III.D.v states that Christianity, Judaism, Islam and their core beliefs and "
           "practices continued to shape societies in Europe, and KC-3.2.I.B.ii describes a "
           "politically fragmented Europe. Overlapping authority is what those two sentences "
           "together describe; the framework nowhere makes them exclusive.")),

 dict(q=("Taken together, what generalization about Europe from c. 1200 to c. 1450 do the "
         "developments of this topic best support?"),
      choices=[
        "Authority over territory was divided rather than concentrated, most people worked the land under obligations that were free in some cases and coerced in others, and several religious traditions went on shaping how the society understood itself.",
        "Authority was concentrated in a single center, cultivation was carried on under one uniform obligation, and one religious tradition alone was present.",
        "Authority was divided, but the population was chiefly employed outside agriculture and no religious tradition affected social life.",
        "Authority was concentrated, cultivation rested on free labor alone, and religious traditions had political effects only.",
        "None of the three subjects can be described for Europe in this period, since the framework makes no assertion about them.",
      ], ans=0,
      why=("The three historical developments of this topic are KC-3.2.I.B.ii on political "
           "fragmentation, decentralized monarchies, feudalism and the manorial system, "
           "KC-3.3.III.C on an agricultural society dependent on free and coerced labor including "
           "serfdom, and KC-3.1.III.D.v on Christianity, Judaism and Islam continuing to shape "
           "societies in Europe. The key states all three and each rejected option contradicts at "
           "least one.")),
]
