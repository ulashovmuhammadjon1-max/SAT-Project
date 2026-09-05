# AP WORLD HISTORY: MODERN 1.5 State Building in Africa  (title copied verbatim from
# WORLD_HISTORY_topics.json). Unit 1 The Global Tapestry, c. 1200 to c. 1450.
# Suggested skill 1.B, explain a historical concept, development, or process.
#
# THE CED CONTENT OF THIS TOPIC, IN FULL -- one learning objective, one key concept
# sentence and one thematic focus block, which is what the topic page carries:
#
#   LO 1.J  Explain how and why states in Africa developed and changed over time.
#   KC-3.2.I.D.ii  In Africa, as in Eurasia and the Americas, state systems
#           demonstrated continuity, innovation, and diversity and expanded in scope
#           and reach.
#
#   Thematic focus GOV: a variety of internal and external factors contribute to state
#           formation, expansion, and decline. Governments maintain order through a
#           variety of administrative institutions, policies, and procedures, and
#           governments obtain, retain, and exercise power in different ways and for
#           different purposes.
#
#   Illustrative examples: state systems in Africa -- Great Zimbabwe, Ethiopia, the
#           Hausa kingdoms.
#
# Two further CED sentences are cited where they bear on Africa specifically:
#   KC-3.1.III.D.iii  Islam, Judaism, Christianity, and the core beliefs and practices
#           of these religions continued to shape societies in AFRICA and Asia.
#   KC-3.1.I.E.ii (Unit 2)  the expansion of empires, including Mali in West Africa,
#           facilitated Afro-Eurasian trade and communication. It is cited only as
#           context; the trade routes themselves belong to topic 2.4 and are not
#           examined here.
#
# THE SUGGESTED SKILL SHAPES THE BANK. Skill 1.B is to EXPLAIN a concept,
# development or process, so these items ask which account explains something rather
# than which observation evidences it -- deliberately a different question shape from
# topic 1.4, whose skill is 3.B and whose items ask what the evidence is. The two
# topics carry nearly the same key concept sentence, one clause apart, and writing
# them the same way would have produced two interchangeable banks.
#
# No key asserts a fact about Great Zimbabwe, Ethiopia or the Hausa kingdoms beyond
# their being named as illustrative examples, because the framework asserts none. The
# stimuli are unattributed and written for the item; nothing is put in a real author's
# mouth.
TOPIC = ("1.5", "State Building in Africa", 1)

_T_WALLS = dict(
    headers=["Settlement (hypothetical)", "Enclosure wall length in paces",
             "Cattle pens recorded"],
    rows=[["Settlement One", "900", "12"],
          ["Settlement Two", "400", "20"],
          ["Settlement Three", "650", "6"]])

_T_DISTRICTS = dict(
    headers=["Kingdom (hypothetical)", "Districts governed at an earlier date",
             "Districts governed at a later date"],
    rows=[["Kingdom One", "5", "9"],
          ["Kingdom Two", "8", "8"],
          ["Kingdom Three", "3", "6"]])

_T_OFFICES = dict(
    headers=["Office (hypothetical)", "Holders recorded in an earlier reign",
             "Holders recorded in a later reign"],
    rows=[["Office of the treasury", "2", "6"],
          ["Office of the court", "4", "5"],
          ["Office of the frontier", "3", "3"]])

QUESTIONS = [
 dict(q=("Which statement best expresses what the framework asserts about state systems in "
         "Africa between c. 1200 and c. 1450?"),
      choices=[
        "They showed continuity, innovation and diversity and grew in what they did and in how far their authority ran, as state systems elsewhere did.",
        "They were uniform in organization and unchanging in extent throughout the period.",
        "They were smaller versions of state systems found in Eurasia and had no features of their own.",
        "They contracted throughout the period and lost the functions they had held earlier.",
        "They developed in ways for which no comparison with other regions is possible.",
      ], ans=0,
      why=("KC-3.2.I.D.ii states that in Africa, as in Eurasia and the Americas, state systems "
           "demonstrated continuity, innovation, and diversity and expanded in scope and reach. "
           "Each clause of the key comes from that sentence and each rejected option denies one "
           "of them.")),

 dict(q=("The framework describes state systems in Africa with the same three terms it uses for "
         "Eurasia and for the Americas. Explain what follows from that choice of wording."),
      choices=[
        "The same analytic vocabulary is being applied to all three regions, so African state building is treated as an instance of a general process rather than as an exception to it.",
        "The state systems of the three regions are being described as having been in contact with one another.",
        "The state systems of the three regions are being described as identical in size and organization.",
        "African state systems are being described as derived from those of the other two regions.",
        "The framework is signalling that African state systems require terms that do not apply elsewhere.",
      ], ans=0,
      why=("KC-3.2.I.D.ii opens with the phrase as in Eurasia and the Americas, and KC-3.2.I.A "
           "and KC-3.2.I.D.i apply the same three terms to those regions. Shared vocabulary is a "
           "claim about how to analyze the cases, not about contact, descent or identity.")),

 dict(q=("A student writes two paragraphs about a kingdom in Africa. The first lists the rulers "
         "in order with the year of each accession. The second sets out how the kingdom came to "
         "govern districts it had not governed before, and by what means. Which paragraph "
         "explains a historical process, and why?"),
      choices=[
        "The second, because it gives an account of how a change came about rather than recording that events occurred in a sequence.",
        "The first, because a list of rulers in order is what a process consists of.",
        "Both equally, since any statement about the past explains a process.",
        "Neither, because a process can only be described for a region and never for a single kingdom.",
        "The first, because the second concerns government rather than chronology.",
      ], ans=0,
      why=("Suggested skill 1.B for this topic is to explain a historical concept, development, "
           "or process, and Learning Objective J asks how and WHY states in Africa developed and "
           "changed. An explanation gives the means by which a change occurred; a chronology "
           "does not.")),

 dict(q=("A kingdom that once collected only occasional gifts begins to assess a fixed render "
         "from each district, appoint officers to gather it, and hear disputes about it. Explain "
         "what this change amounts to on the framework's terms."),
      choices=[
        "An expansion in the scope of the state, since it has taken on functions it did not previously perform.",
        "An expansion in the reach of the state, since its authority now extends over more territory.",
        "A contraction of the state, since fixed obligations replace voluntary ones.",
        "A change of no significance for the state, since gifts and renders are the same thing.",
        "A change in the state's religion rather than in its government.",
      ], ans=0,
      why=("KC-3.2.I.D.ii says state systems expanded in scope AND reach, two different things, "
           "and the Governance thematic focus describes governments maintaining order through "
           "administrative institutions, policies and procedures. New functions are scope; more "
           "territory would be reach.")),

 dict(q=("Explain why the framework's claim that African state systems were diverse cannot be "
         "settled by studying one kingdom alone."),
      choices=[
        "Because diversity is a claim about variation between cases, so it can only be assessed by comparing more than one.",
        "Because a single kingdom cannot be studied with the evidence available.",
        "Because the framework treats every individual kingdom as identical to every other.",
        "Because diversity in the framework refers only to religion and not to government.",
        "Because a claim about variation is settled by choosing the largest case available.",
      ], ans=0,
      why=("KC-3.2.I.D.ii asserts diversity among state systems in Africa, and the Governance "
           "thematic focus says governments obtain, retain, and exercise power in different ways "
           "and for different purposes. A statement about difference between cases requires more "
           "than one case.")),

 dict(q=("An unattributed account describes a settlement enclosed by stone walls, whose leading "
         "families own most of the cattle in the district and whose smiths work metal brought "
         "from some distance away. Explain how such a settlement might come to dominate its "
         "neighbors."),
      choices=[
        "Control of wealth in herds and of skilled production gives its leading families the means to attract followers and to reward them, which is one way authority is built.",
        "Its stone walls prevent any contact with neighboring districts, which leaves it dominant by default.",
        "Metal brought from a distance shows that the settlement had no authority of its own.",
        "Ownership of cattle by a few families is evidence that no authority existed there.",
        "A settlement can dominate its neighbors only if it holds a written record of its claims.",
      ], ans=0,
      why=("The Governance thematic focus states that governments obtain, retain, and exercise "
           "power in different ways and for different purposes, and KC-3.2.I.D.ii asserts "
           "diversity among African state systems. Wealth converted into followers is one of "
           "those ways; the rejected options each assert something the framework denies or "
           "does not support.")),

 dict(q=("A ruler replaces district heads drawn from local ruling families with officers "
         "appointed from his own household and removable at his word. Explain the significance "
         "of the change."),
      choices=[
        "It is an innovation in administration that makes the districts answerable to the ruler rather than to their own inherited leadership.",
        "It is a continuity in administration, since districts continue to have heads.",
        "It removes the state's authority from the districts altogether.",
        "It concerns the ruler's household and has no bearing on how the state is governed.",
        "It shows that the state had ceased to expand in scope or reach.",
      ], ans=0,
      why=("KC-3.2.I.D.ii names innovation alongside continuity in African state systems, and "
           "the Governance thematic focus names administrative institutions and procedures as "
           "how governments maintain order. Learning Objective J asks how and why states "
           "developed and changed.")),

 dict(q=("Explain why a state that draws revenue from traffic passing through its territory may "
         "have an interest in the security of routes far beyond its own borders."),
      choices=[
        "Because its revenue depends on traffic that must survive the whole journey, so disorder anywhere along the route reduces what reaches its own markets.",
        "Because a state is obliged to govern every region its merchants visit.",
        "Because revenue from traffic is collected at the far end of the route rather than at home.",
        "Because states in this period could tax only goods produced outside their own territory.",
        "Because the security of a route has no effect on the volume of traffic along it.",
      ], ans=0,
      why=("The Governance thematic focus states that a variety of internal and EXTERNAL factors "
           "contribute to state formation, expansion, and decline, and KC-3.1.I.E.ii records "
           "that the expansion of empires, including Mali in West Africa, facilitated trade and "
           "communication.")),

 dict(q=("Which of the following is an internal factor in the expansion or decline of a state, "
         "as the framework distinguishes internal from external?"),
      choices=[
        "A quarrel among the state's own leading families over who is to succeed the ruler.",
        "The rise of a stronger neighbor on the state's frontier.",
        "A shift in the route taken by merchants from another region.",
        "A demand for tribute pressed by an outside power.",
        "The conversion of a neighboring people to a new faith.",
      ], ans=0,
      why=("The Governance thematic focus states that a variety of internal and external factors "
           "contribute to state formation, expansion, and decline. A succession quarrel arises "
           "within the state itself; each rejected option originates outside it. KC-3.2.I.D.ii "
           "is the content those factors operate on.")),

 dict(q=("Explain why the survival of an older title alongside a newly created office is "
         "described by the framework as continuity and innovation together rather than as one or "
         "the other."),
      choices=[
        "Because the inherited title carries forward an existing claim to authority while the new office does something that was not being done before, and both are in use at once.",
        "Because an older title cannot exist alongside a newer office, so one of the two must be a later invention.",
        "Because continuity and innovation are the same term used of different periods.",
        "Because the framework treats any change as a break with everything that preceded it.",
        "Because a state can be described as continuous only after it has ceased to innovate.",
      ], ans=0,
      why=("KC-3.2.I.D.ii lists continuity, innovation, and diversity together as properties of "
           "the same state systems, not as stages following one another. Learning Objective J "
           "asks how states developed and changed over time.")),

 dict(q=("The table below carries HYPOTHETICAL records for three settlements, giving the length "
         "of each enclosure wall and the number of cattle pens recorded. Which conclusion do "
         "these numbers support?"),
      table=_T_WALLS,
      choices=[
        "The settlement with the longest wall does not have the most pens, so ranking by wall length and by pens gives different orders.",
        "Ranking the settlements by wall length gives the same order as ranking them by pens.",
        "The settlement with the shortest wall has the fewest pens.",
        "Every settlement listed has more pens than the one with the longest wall.",
        "Wall length and the number of pens are equal at every settlement listed.",
      ], ans=0,
      why=("Recomputed in the verifier from the table alone. KC-3.2.I.D.ii asserts diversity "
           "among African state systems, and two measures that rank the same settlements "
           "differently is what variation looks like in data.")),

 dict(q=("HYPOTHETICAL counts of the districts governed by three kingdoms, at an earlier and a "
         "later date, are set out in the table below. What is best supported by that data?"),
      table=_T_DISTRICTS,
      choices=[
        "Two of the three kingdoms governed more districts at the later date while one governed the same number, and the kingdom that exactly doubled was the smallest at the earlier date.",
        "All three kingdoms governed more districts at the later date.",
        "The kingdom governing the most districts at the earlier date grew by the largest multiple.",
        "At least one kingdom governed fewer districts at the later date than at the earlier one.",
        "The kingdom that exactly doubled was the largest at the earlier date.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns, distractors included. KC-3.2.I.D.ii "
           "says African state systems expanded in scope and reach and were diverse, and growth "
           "in some cases but not all is what such a claim predicts.")),

 dict(q=("For three offices of one kingdom, the table below gives HYPOTHETICAL counts of the "
         "holders recorded in an earlier and a later reign. Which statement is best supported?"),
      table=_T_OFFICES,
      choices=[
        "The number of holders rose for two of the three offices listed, and the office of the treasury tripled while the others did not.",
        "The number of holders rose for every office listed.",
        "The office of the frontier recorded more holders in the later reign than in the earlier one.",
        "The office of the court more than doubled its holders between the two reigns.",
        "Every office listed recorded fewer holders in the later reign.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. The Governance thematic focus names "
           "administrative institutions as how governments maintain order, and KC-3.2.I.D.ii's "
           "expansion in scope is what a growing establishment in some offices and not others "
           "would illustrate.")),

 dict(q=("Explain why the framework speaks of state systems rather than simply of states."),
      choices=[
        "Because it is describing the arrangements by which authority was organized, which may take in more than one center and may not correspond to a single named kingdom.",
        "Because it is describing states that possessed written constitutions.",
        "Because system is the term used for states that existed before 1200 only.",
        "Because it wishes to exclude any polity that governed more than one district.",
        "Because a system in the framework's usage means a state that never changed.",
      ], ans=0,
      why=("KC-3.2.I.D.ii uses the phrase state systems of Africa and KC-3.2.I.D.i uses it of the "
           "Americas, in both cases alongside diversity; the Governance thematic focus describes "
           "governments maintaining order through a VARIETY of institutions, policies and "
           "procedures.")),

 dict(q=("A historian sets out to explain why a kingdom in Africa grew during this period and "
         "offers a single cause. What is the strongest general objection to that approach?"),
      choices=[
        "That the framework treats a variety of internal and external factors as contributing to formation, expansion and decline, so an account resting on one cause is likely to be incomplete.",
        "That growth in this period cannot be explained at all, since no evidence survives.",
        "That an explanation with one cause is easier to check and therefore preferable.",
        "That only external factors may be cited in explaining expansion.",
        "That only internal factors may be cited in explaining expansion.",
      ], ans=0,
      why=("The Governance thematic focus states that a VARIETY of internal and external factors "
           "contribute to state formation, expansion, and decline, and Learning Objective J asks "
           "how and why states in Africa developed and changed over time.")),

 dict(q=("An unattributed account reports that a kingdom's ruler was accompanied at court by "
         "scholars of a faith practiced widely beyond his own territory, and that his officials "
         "used that faith's written language for their records. Explain what this indicates."),
      choices=[
        "That a religious tradition present across a wider region could supply a state with learning and a written medium for its administration.",
        "That the kingdom's administration must have been directed by rulers from outside the region.",
        "That religious traditions in Africa in this period had no connection with government.",
        "That written records in this period were kept only where no religious tradition was present.",
        "That the ruler's own subjects were forbidden to practice any faith.",
      ], ans=0,
      why=("KC-3.1.III.D.iii states that Islam, Judaism, Christianity and their core beliefs and "
           "practices continued to shape societies in AFRICA and Asia, and the Governance "
           "thematic focus names administrative institutions and procedures as how governments "
           "maintain order.")),

 dict(q=("Explain how a state may extend its reach without occupying the territory concerned."),
      choices=[
        "By obliging neighboring communities to render goods or service while leaving their own leadership in place, so that authority runs further than administration does.",
        "By moving its own capital into the neighboring territory and governing from there.",
        "By ceasing to collect anything from the neighboring communities at all.",
        "By declaring that the neighboring territory does not exist.",
        "By exchanging its own territory for the neighboring one.",
      ], ans=0,
      why=("KC-3.2.I.D.ii says state systems expanded in scope and REACH, and the Governance "
           "thematic focus says governments obtain, retain and exercise power in different ways "
           "and for different purposes. Obligation without occupation is one of those ways.")),

 dict(q=("Which of the following questions about states in Africa in this period is answerable "
         "from evidence rather than by a judgment of value?"),
      choices=[
        "Whether a kingdom governed more districts at the end of a reign than at its beginning.",
        "Whether a kingdom was right to bring those districts under its authority.",
        "Whether the obligations owed by those districts were fair.",
        "Whether one kingdom's arrangements were superior to another's.",
        "Whether a ruler deserved the loyalty his officials gave him.",
      ], ans=0,
      why=("KC-3.2.I.D.ii asserts matters of fact about state systems expanding in scope and "
           "reach, and Learning Objective J asks how and why they developed. A count of "
           "districts can be checked; rightness, fairness, superiority and desert cannot be "
           "settled by observation.")),

 dict(q=("Explain why the decline of one center in a region does not by itself establish that "
         "state building in that region had ended."),
      choices=[
        "Because the framework describes state systems in the region as diverse, so other centers may continue or expand while one declines.",
        "Because the framework denies that any center in the region declined during the period.",
        "Because a center that declines has necessarily been absorbed by a larger one.",
        "Because the framework treats decline and expansion as the same process under two names.",
        "Because the framework treats every region as containing exactly one center at a time.",
      ], ans=0,
      why=("KC-3.2.I.D.ii asserts diversity among African state systems, and the Governance "
           "thematic focus names formation, expansion AND decline as parts of one subject. A "
           "claim about one center is not a claim about a region.")),

 dict(q=("What would count as evidence that a state in Africa had innovated rather than simply "
         "inherited its arrangements?"),
      choices=[
        "A record of an office or procedure in use under one ruler that no earlier ruler of that state had employed.",
        "A record showing that a ruler took the same title as his predecessor.",
        "A record showing that the state's capital remained where it had always been.",
        "A record showing that the state's boundaries were unchanged over a reign.",
        "A record showing that a ruler claimed descent from the founder of the state.",
      ], ans=0,
      why=("KC-3.2.I.D.ii joins innovation to continuity in one sentence about African state "
           "systems, so an arrangement without a precedent in that state is evidence of the "
           "innovation half. Each rejected record evidences continuity instead.")),

 dict(q=("A source says a kingdom in Africa was founded in a particular year. Explain why the "
         "framework's periodization does not require that its history be studied only from that "
         "year onward."),
      choices=[
        "Because the framework states that developments are not constrained by the given dates and may begin before or continue after the period.",
        "Because the framework treats founding dates recorded in sources as always inaccurate.",
        "Because the framework holds that no state in Africa was founded during this period.",
        "Because the framework requires every state to be studied from 1200 exactly.",
        "Because the framework treats a founding as the only event worth studying about a state.",
      ], ans=0,
      why=("The CED states that events, processes, and developments are not constrained by the "
           "given dates and may begin before, or continue after, the period, and KC-3.2.I.D.ii's "
           "word continuity presupposes arrangements older than the period's opening.")),

 dict(q=("An unattributed record lists the goods a district owed each year, the officer to whom "
         "they were owed, and the penalty for failing to render them. Explain what such a "
         "document shows about the state that produced it."),
      choices=[
        "That its authority was exercised through a standing procedure with named responsibility and a consequence attached, rather than through demands made as occasion arose.",
        "That its authority extended only as far as the officer named could travel in a day.",
        "That it had no means of enforcing what it demanded.",
        "That the district concerned governed itself without reference to any wider authority.",
        "That obligations of this kind were owed only in years when the ruler was present.",
      ], ans=0,
      why=("The Governance thematic focus states that governments maintain order through a "
           "variety of administrative institutions, policies, and procedures, and KC-3.2.I.D.ii "
           "credits African state systems with expansion in scope. A schedule with an "
           "enforcement clause is a procedure.")),

 dict(q=("Explain the difference between saying that a state in Africa grew larger and saying "
         "that it grew stronger."),
      choices=[
        "The first is a claim about the extent it covered and the second about what it was able to do within that extent, and a state may change in one without changing in the other.",
        "The first is a claim about what it was able to do and the second about the extent it covered.",
        "The two claims are equivalent, since a larger state is necessarily a stronger one.",
        "The first concerns government and the second concerns religion.",
        "Neither claim can be assessed from historical evidence.",
      ], ans=0,
      why=("KC-3.2.I.D.ii names expansion in scope and expansion in reach as two things, and the "
           "Governance thematic focus separates how power is exercised from the extent over "
           "which it runs. The anchor carries both halves in order because one distractor "
           "exchanges them.")),

 dict(q=("Two kingdoms in Africa are described as maintaining order in different ways, one "
         "through a council of elders in each district and the other through officers appointed "
         "by the ruler. Explain what the framework says about such a difference."),
      choices=[
        "That governments maintain order through a variety of institutions and procedures, so more than one arrangement is consistent with an effective state.",
        "That only one of the two can have maintained order, since the framework recognizes one method.",
        "That the difference indicates that one of the two was not a state at all.",
        "That the framework treats such differences as too small to be worth recording.",
        "That both arrangements must have been adopted from a common source outside Africa.",
      ], ans=0,
      why=("The Governance thematic focus states that governments maintain order through a "
           "variety of administrative institutions, policies, and procedures, and KC-3.2.I.D.ii "
           "asserts diversity among the state systems of Africa.")),

 dict(q=("Explain why a historian would treat an account written by a visitor to an African "
         "kingdom differently from a record produced by that kingdom's own administration."),
      choices=[
        "Because the two were made for different purposes and by people with different access, so each is strong where the other is weak.",
        "Because a visitor's account is always false and an administrative record is always true.",
        "Because administrative records were not produced anywhere in Africa in this period.",
        "Because a visitor's account concerns religion and an administrative record concerns trade.",
        "Because only one of the two kinds of source may be used in a historical argument.",
      ], ans=0,
      why=("Learning Objective J asks students to explain how and why states in Africa developed "
           "and changed, which requires weighing sources rather than ranking them by type; the "
           "Governance thematic focus is the content, since administrative records are the "
           "product of the institutions it names.")),

 dict(q=("A kingdom's authority is said to have grown deeper as well as wider. Explain what "
         "deeper would mean here."),
      choices=[
        "That the state came to regulate more aspects of life within the territory it already held, rather than adding new territory.",
        "That the state added new territory rather than regulating more within its existing territory.",
        "That the state's rulers reigned for longer than their predecessors.",
        "That the state's records were kept in a greater number of copies.",
        "That the state's capital was rebuilt on a larger scale.",
      ], ans=0,
      why=("KC-3.2.I.D.ii pairs expansion in scope with expansion in reach, and the Governance "
           "thematic focus describes governments maintaining order through institutions and "
           "procedures. The anchor carries both halves because the strongest distractor is the "
           "same pair exchanged.")),

 dict(q=("An unattributed chronicle says that a district which had rendered tribute for two "
         "generations ceased to do so after a disputed succession at the center. Explain what "
         "this suggests about the basis of the state's authority there."),
      choices=[
        "That obedience in the district depended in part on the center's ability to act, so a crisis at the center could interrupt obligations at a distance.",
        "That the district had never rendered tribute at any point.",
        "That the succession dispute occurred because the district ceased to render tribute.",
        "That tribute in this period was owed to districts by centers rather than the reverse.",
        "That authority once established could not be interrupted by any event.",
      ], ans=0,
      why=("The Governance thematic focus names internal factors among those contributing to "
           "state expansion and decline, and KC-3.2.I.D.ii speaks of reach. The anchor carries "
           "the direction of the relation, because one distractor reverses cause and effect.")),

 dict(q=("Explain why the same three terms, continuity, innovation and diversity, can be applied "
         "to state systems that differ greatly from one another."),
      choices=[
        "Because the terms describe how state systems change and vary rather than naming any particular institution, so they fit cases whose institutions are unalike.",
        "Because the terms are so vague that they can be applied to anything whatever.",
        "Because the state systems concerned were in fact alike in their institutions.",
        "Because the terms apply only to states that share a common origin.",
        "Because the framework applies the terms to Africa alone and not to other regions.",
      ], ans=0,
      why=("KC-3.2.I.D.ii applies the three terms to Africa as KC-3.2.I.D.i does to the Americas "
           "and KC-3.2.I.A to Afro-Eurasia. They describe patterns of change and variation, "
           "which is why one vocabulary covers institutionally unlike cases.")),

 dict(q=("A student claims that state building in Africa in this period can be explained "
         "entirely by influences arriving from outside the continent. Explain the strongest "
         "objection."),
      choices=[
        "That the framework names internal as well as external factors in state formation, and describes African state systems as showing continuity, which points to arrangements already in place.",
        "That the framework denies that any influence from outside reached Africa in this period.",
        "That the framework treats external influence as the only factor worth considering.",
        "That the framework holds that no state building occurred in Africa in this period.",
        "That the framework treats continuity as evidence of external influence.",
      ], ans=0,
      why=("The Governance thematic focus states that a variety of INTERNAL and external factors "
           "contribute to state formation, expansion, and decline, and KC-3.2.I.D.ii asserts "
           "continuity among African state systems, which is a claim about inherited "
           "arrangements.")),

 dict(q=("Taken together, what generalization about Africa between c. 1200 and c. 1450 do the "
         "developments of this topic best support?"),
      choices=[
        "Its state systems varied in form, carried inherited arrangements forward while adopting new ones, and grew both in what they did and in how far their authority ran.",
        "Its state systems were uniform in form and fixed in extent across the period.",
        "Its state systems declined continuously throughout the period.",
        "Its state systems can be described only in terms that apply nowhere else.",
        "Its state systems existed only in a single region of the continent.",
      ], ans=0,
      why=("KC-3.2.I.D.ii is a single sentence carrying every element of the key: continuity, "
           "innovation, diversity and expansion in scope and reach, in Africa as in Eurasia and "
           "the Americas. Learning Objective J asks how and why these states developed and "
           "changed.")),
]
