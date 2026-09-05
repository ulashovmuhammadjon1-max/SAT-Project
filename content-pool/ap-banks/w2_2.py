# AP WORLD HISTORY: MODERN 2.2 The Mongol Empire and the Making of the Modern World
# (title copied verbatim from WORLD_HISTORY_topics.json). Unit 2 Networks of Exchange,
# c. 1200 to c. 1450. Suggested skill 5.A, identify patterns among or connections
# between historical developments and processes.
#
# THE CED CONTENT OF THIS TOPIC, in the framework's own words. The page carries three
# thematic focus blocks and three learning objectives, one historical development each:
#
#   Thematic focus GOV: a variety of internal and external factors contribute to state
#           formation, expansion, and decline. Governments maintain order through a
#           variety of administrative institutions, policies, and procedures, and
#           governments obtain, retain, and exercise power in different ways and for
#           different purposes.
#   LO 2.B  Explain the process of state building and decline in Eurasia over time.
#   KC-3.2.I.B.iii  Empires collapsed in different regions of the world and in some
#           areas were replaced by new imperial states, including the Mongol khanates.
#
#   Thematic focus ECN: as societies develop, they affect and are affected by the ways
#           that they produce, exchange, and consume goods and services.
#   LO 2.C  Explain how the expansion of empires influenced trade and communication
#           over time.
#   KC-3.1.I.E.i  The expansion of empires -- including the Mongols -- facilitated
#           Afro-Eurasian trade and communication as new people were drawn into their
#           conquerors' economies and trade networks.
#
#   Thematic focus CDI: the development of ideas, beliefs, and religions illustrates
#           how groups in society view themselves, and the interactions of societies
#           and their beliefs often have political, social, and cultural implications.
#   LO 2.D  Explain the significance of the Mongol Empire in larger patterns of
#           continuity and change.
#   KC-3.2.II.A.ii  Interregional contacts and conflicts between states and empires,
#           including the Mongols, encouraged significant technological and cultural
#           transfers.
#
#   Illustrative examples printed on this topic page: technological and cultural
#           transfers -- transfer of Greco-Islamic medical knowledge to western Europe,
#           transfer of numbering systems to Europe, adoption of Uyghur script. The CED
#           states that illustrative examples "do not in any way constitute additional,
#           preferred, or required information", so no key turns on one.
#
# THE THREE WORDS THIS TOPIC TURNS ON, and the reason it is easy to get wrong. The
# framework says empires collapsed and IN SOME AREAS were replaced -- not everywhere.
# It says expansion facilitated trade as new people were drawn into THEIR CONQUERORS'
# economies -- a direction, not a merger of equals. And it says contacts AND CONFLICTS
# encouraged transfers -- so conquest and exchange are not opposites in this account.
# A great deal else is commonly said about the Mongols; none of it is keyed here,
# because the framework does not assert it and no later reader could check it.
#
# THE SUGGESTED SKILL SHAPES THE BANK. Skill 5.A is to identify PATTERNS AMONG OR
# CONNECTIONS BETWEEN developments, so the recurring shape here is two developments and
# four candidate relations between them, of which one is the connection the framework
# draws and the others are coincidence, reversal, or a restatement of one development.
#
# ON THE SOURCES. This bank cannot show an image. Every stimulus is a table of
# HYPOTHETICAL figures whose keyed conclusion is recoverable from the table alone, or
# an explicitly unattributed illustrative source. No quotation is attributed to a real
# person or document.
#
# ON DATES. Spans are written "c. 1200 to c. 1450". The CED states that events,
# processes, and developments are not constrained by the given dates and may begin
# before, or continue after, the period, so no key turns on a boundary year.
TOPIC = ("2.2", "The Mongol Empire and the Making of the Modern World", 2)

_T_MESSAGES = dict(
    headers=["Route (hypothetical)", "Messages recorded before the empire's expansion",
             "Messages recorded after the empire's expansion"],
    rows=[["Route One", "20", "85"],
          ["Route Two", "45", "60"],
          ["Route Three", "10", "70"]])

_T_TRANSFERS = dict(
    headers=["Kind of transfer (hypothetical)",
             "Regions in which it is recorded before the contact",
             "Regions in which it is recorded after the contact"],
    rows=[["Medical knowledge", "2", "6"],
          ["Numbering and calculation", "1", "5"],
          ["Script and writing", "3", "4"]])

_T_STATES = dict(
    headers=["Region (hypothetical)", "Imperial states recorded as having collapsed",
             "New imperial states recorded as established"],
    rows=[["Region One", "1", "1"],
          ["Region Two", "1", "0"],
          ["Region Three", "0", "1"]])

QUESTIONS = [
 dict(q=("Which of the following states the connection the framework draws between the expansion "
         "of empires in this period and the movement of goods and news across Afro-Eurasia?"),
      choices=[
        "Expansion facilitated trade and communication, because peoples newly brought under an empire were drawn into the economies and trade networks of those who had conquered them.",
        "Expansion ended trade and communication, because a conquered people had nothing left to exchange.",
        "Expansion had no bearing on trade or communication, the two being separate matters.",
        "Trade and communication caused the expansion of empires rather than following from it.",
        "Expansion facilitated trade only within the conqueror's original territory and not beyond it.",
      ], ans=0,
      why=("KC-3.1.I.E.i states that the expansion of empires, including the Mongols, facilitated "
           "Afro-Eurasian trade and communication as new people were drawn into their conquerors' "
           "economies and trade networks. The direction of the relation is expansion first, "
           "facilitation after, which is what the reversed option gets wrong.")),

 dict(q=("A student writes that every empire that collapsed in this period was succeeded by a new "
         "imperial state. Which of the following identifies the error?"),
      choices=[
        "The framework says empires collapsed in different regions and that in SOME areas they were replaced by new imperial states, which does not assert replacement everywhere.",
        "The framework says no empire collapsed anywhere in this period.",
        "The framework says no new imperial state was established anywhere in this period.",
        "The framework says collapse and replacement were simultaneous in every case.",
        "The framework says replacement occurred only where no collapse had happened.",
      ], ans=0,
      why=("KC-3.2.I.B.iii states that empires collapsed in different regions of the world and IN "
           "SOME AREAS were replaced by new imperial states, including the Mongol khanates. The "
           "qualifier is the framework's own and it is exactly what a universal claim overshoots.")),

 dict(q=("The table below carries HYPOTHETICAL counts of messages recorded on three routes before "
         "and after an empire's expansion across them. Which conclusion does the data best "
         "support?"),
      table=_T_MESSAGES,
      choices=[
        "Every route listed carried more messages after the expansion, and the route carrying fewest before multiplied its traffic by the largest factor.",
        "Every route listed carried fewer messages after the expansion.",
        "The route carrying the most messages before the expansion multiplied its traffic by the largest factor.",
        "One of the routes listed carried the same number of messages before and after.",
        "The route carrying fewest messages before the expansion multiplied its traffic by the smallest factor.",
      ], ans=0,
      why=("Recomputed in the verifier from the table alone, distractors included. KC-3.1.I.E.i "
           "states that the expansion of empires facilitated Afro-Eurasian trade and "
           "communication, and a rise on every route with the largest gain where the traffic had "
           "been thinnest is what facilitation looks like in figures.")),

 dict(q=("An unattributed account describes a merchant travelling for many weeks under a single "
         "authority, presenting the same warrant at each post and finding the same weights in use "
         "at each market. Which of the following identifies the pattern this illustrates?"),
      choices=[
        "The expansion of an empire facilitating trade and communication across territories that had previously been under separate authorities.",
        "The collapse of an empire leaving each district to set its own terms of passage.",
        "The withdrawal of an empire from the regulation of trade within its own territory.",
        "The confinement of trade to the district in which a merchant was born.",
        "The replacement of trade in goods by the carriage of official messages alone.",
      ], ans=0,
      why=("KC-3.1.I.E.i states that the expansion of empires, including the Mongols, facilitated "
           "Afro-Eurasian trade and communication, and the Governance thematic focus states that "
           "governments maintain order through a variety of administrative institutions, "
           "policies, and procedures. A single warrant honoured along a route is that "
           "facilitation in operation.")),

 dict(q=("Which of the following identifies what the framework asserts about the relationship "
         "between conflict and cultural transfer in this period?"),
      choices=[
        "Contacts AND conflicts between states and empires both encouraged significant technological and cultural transfers, so the two are not opposed in the framework's account.",
        "Only peaceful contact encouraged transfers, conflict having prevented them.",
        "Only conflict encouraged transfers, peaceful contact having produced none.",
        "Neither contact nor conflict encouraged transfers, which occurred independently of both.",
        "Transfers encouraged conflict rather than following from it.",
      ], ans=0,
      why=("KC-3.2.II.A.ii states that interregional contacts AND CONFLICTS between states and "
           "empires, including the Mongols, encouraged significant technological and cultural "
           "transfers. Both nouns are in the sentence, which is what the first two rejected "
           "options each halve.")),

 dict(q=("HYPOTHETICAL counts of the regions in which three kinds of knowledge are recorded, "
         "before and after a period of contact, are given in the table below. Which statement is "
         "best supported by that data alone?"),
      table=_T_TRANSFERS,
      choices=[
        "Every kind listed is recorded in more regions after the contact, and the kind recorded in fewest regions beforehand is not the kind recorded in most regions afterwards.",
        "Every kind listed is recorded in more regions after the contact, and the kind recorded in fewest regions beforehand is the kind recorded in most regions afterwards.",
        "One of the kinds listed is recorded in fewer regions after the contact than before it.",
        "One of the kinds listed is recorded in the same number of regions before and after.",
        "The kind recorded in most regions beforehand is also recorded in most regions afterwards.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.2.II.A.ii states that "
           "interregional contacts and conflicts between states and empires encouraged "
           "significant technological and cultural transfers, and knowledge reaching further "
           "than it had before is what such a transfer looks like in a record. The framework "
           "orders no race between them, which is why the anchor carries both clauses: the "
           "strongest distractor changes only which kind ends up furthest spread.")),

 dict(q=("Which of the following identifies the connection between the collapse of empires and "
         "the appearance of the Mongol khanates as the framework presents it?"),
      choices=[
        "The khanates are named as an instance of the new imperial states that replaced collapsed empires in some areas, so they belong to a pattern rather than standing outside one.",
        "The khanates are named as the only imperial states in existence anywhere in this period.",
        "The khanates are described as having prevented any empire from collapsing.",
        "The khanates are described as having existed before any empire collapsed.",
        "The khanates are described as the cause of every imperial collapse recorded in the period.",
      ], ans=0,
      why=("KC-3.2.I.B.iii states that empires collapsed in different regions of the world and in "
           "some areas were replaced by new imperial states, INCLUDING THE MONGOL KHANATES. The "
           "word including makes them an instance of the pattern the sentence describes.")),

 dict(q=("The table below carries HYPOTHETICAL counts, for three regions, of imperial states "
         "recorded as having collapsed and new imperial states recorded as established. Which "
         "conclusion does the data best support?"),
      table=_T_STATES,
      choices=[
        "One region listed records a collapse with no new imperial state, and another records a new imperial state with no collapse, so the two are not always found together.",
        "Every region listed that records a collapse also records a new imperial state.",
        "No region listed records a new imperial state at all.",
        "Every region listed records both a collapse and a new imperial state.",
        "No region listed records a collapse at all.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.2.I.B.iii says empires "
           "collapsed in different regions and IN SOME AREAS were replaced by new imperial "
           "states, and a pattern in which the two do not always accompany each other is what "
           "that qualifier describes.")),

 dict(q=("An unattributed chronicle records that after a conquest the new rulers kept the "
         "existing tax registers, appointed men from among the conquered to administer them, and "
         "added a levy of their own. Which of the following identifies the pattern this belongs "
         "to?"),
      choices=[
        "State building in which an incoming imperial state carries forward the arrangements it finds and adds to them, so decline in one state and building in another can occur in the same place.",
        "State building in which every arrangement of the displaced state is abolished at once.",
        "The collapse of state authority altogether, since two levies were now in force.",
        "The withdrawal of the incoming rulers from the administration of the territory.",
        "The transfer of administration from the incoming rulers to a neighbouring empire.",
      ], ans=0,
      why=("Learning Objective B of this unit asks students to explain the process of state "
           "building AND decline in Eurasia over time, and KC-3.2.I.B.iii pairs collapse with "
           "replacement by new imperial states. The Governance thematic focus names "
           "administrative institutions and procedures as how order is maintained.")),

 dict(q=("Which of the following would be the strongest evidence that the expansion of an empire, "
         "rather than a change in demand, accounts for a rise in exchange across a region?"),
      choices=[
        "That communities which had not previously traded into the network begin to appear in its records after they are brought under the empire's authority.",
        "That the goods traded across the region were valuable in proportion to their weight.",
        "That merchants in the region kept written accounts of what they were owed.",
        "That the region's population is recorded as having grown during the same years.",
        "That the goods traded had also been traded in the region before the expansion.",
      ], ans=0,
      why=("KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and "
           "communication AS NEW PEOPLE WERE DRAWN INTO their conquerors' economies and trade "
           "networks. New participants appearing after incorporation is the mechanism that "
           "sentence names, which is why it distinguishes expansion from a demand-side "
           "explanation.")),

 dict(q=("A student claims that the Mongol Empire is significant only because it was large. Which "
         "of the following identifies the strongest objection from this topic?"),
      choices=[
        "The framework attaches to it a place in larger patterns of continuity and change, naming it in one sentence about imperial replacement and in another about the transfers that contacts and conflicts encouraged.",
        "The framework describes it as the smallest of the imperial states of the period.",
        "The framework treats size as the only respect in which any empire may be significant.",
        "The framework denies that the empire existed on the scale usually claimed for it.",
        "The framework treats significance as a matter of value on which no evidence bears.",
      ], ans=0,
      why=("Learning Objective D asks students to explain the significance of the Mongol Empire "
           "in LARGER PATTERNS of continuity and change, and the empire is named in KC-3.2.I.B.iii "
           "among new imperial states and in KC-3.2.II.A.ii among the parties whose contacts and "
           "conflicts encouraged technological and cultural transfers.")),

 dict(q=("An unattributed source reports that physicians in one region began to use a body of "
         "medical writing that had been compiled far to the east of them, the texts having "
         "reached them through the movement of scholars along routes newly opened to travel. "
         "Which of the following identifies the pattern this illustrates?"),
      choices=[
        "Interregional contact encouraging a technological or cultural transfer, which the framework treats as a characteristic consequence of contacts and conflicts between states and empires.",
        "The invention of a body of medical knowledge in the region that received it.",
        "The disappearance of medical knowledge from the region in which it was compiled.",
        "The confinement of learning to the region in which it was first written down.",
        "The replacement of a region's own scholarship by an imperial administration.",
      ], ans=0,
      why=("KC-3.2.II.A.ii states that interregional contacts and conflicts between states and "
           "empires, including the Mongols, encouraged significant technological and cultural "
           "transfers, and the topic's illustrative list names the transfer of Greco-Islamic "
           "medical knowledge to western Europe as one such case.")),

 dict(q=("Which of the following identifies a connection the framework draws between two "
         "different learning objectives of this topic?"),
      choices=[
        "The same imperial expansion that drew new peoples into a conqueror's trade networks is also named among the contacts and conflicts that encouraged technological and cultural transfers.",
        "The expansion of empires is named as a cause of trade but is excluded by the framework from any bearing on cultural transfer.",
        "Cultural transfer is named as a cause of imperial expansion rather than as a consequence of contact.",
        "The framework treats trade, communication and cultural transfer as three processes with no relation to one another.",
        "The framework treats imperial expansion as a consequence of cultural transfer between regions.",
      ], ans=0,
      why=("KC-3.1.I.E.i names the expansion of empires including the Mongols as facilitating "
           "Afro-Eurasian trade and communication, while KC-3.2.II.A.ii names interregional "
           "contacts and conflicts between states and empires including the Mongols as "
           "encouraging significant technological and cultural transfers. Suggested skill 5.A "
           "asks for exactly such connections between processes.")),

 dict(q=("Which of the following identifies what the phrase drawn into their conquerors' "
         "economies asserts about the direction of the relation?"),
      choices=[
        "That the newly incorporated peoples entered networks belonging to those who had conquered them, rather than the conquerors entering theirs.",
        "That the conquerors entered the networks of the peoples they had conquered, rather than the reverse.",
        "That the two sets of networks were merged into a single one belonging to neither party.",
        "That the newly incorporated peoples were excluded from all trade networks.",
        "That the conquerors abandoned their own networks upon conquering.",
      ], ans=0,
      why=("KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and "
           "communication as new people were drawn into THEIR CONQUERORS' economies and trade "
           "networks. The possessive fixes the direction, and the anchor carries both parties in "
           "order because the strongest distractor exchanges them.")),

 dict(q=("A historian argues that the period's imperial history in Eurasia should be described as "
         "building and decline together rather than as one or the other. Which of the following "
         "best supports that description?"),
      choices=[
        "That the framework's single sentence on the subject records collapse in different regions and replacement by new imperial states in some areas at once.",
        "That the framework records collapse in this period but records no new imperial state.",
        "That the framework records new imperial states in this period but records no collapse.",
        "That the framework treats building and decline as belonging to different centuries.",
        "That the framework denies that any imperial state in Eurasia changed during the period.",
      ], ans=0,
      why=("KC-3.2.I.B.iii states that empires collapsed in different regions of the world and in "
           "some areas were replaced by new imperial states, including the Mongol khanates, and "
           "Learning Objective B asks for the process of state building AND decline in Eurasia "
           "over time. One sentence carries both halves.")),

 dict(q=("An unattributed record from a conquered city notes that its craftsmen were required to "
         "supply the new authority with goods of a kind they had made before, and that their work "
         "now travelled to markets they had never supplied. Which of the following identifies the "
         "pattern?"),
      choices=[
        "A people newly brought under an empire being drawn into a wider network of exchange than the one it had belonged to before.",
        "A people newly brought under an empire being excluded from exchange beyond its own city.",
        "A people newly brought under an empire abandoning the crafts it had practised before.",
        "An empire withdrawing its demands upon the cities it had conquered.",
        "An empire confining the movement of goods to its own original territory.",
      ], ans=0,
      why=("KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and "
           "communication as new people were drawn into their conquerors' economies and trade "
           "networks, and the Economics thematic focus says societies affect and are affected by "
           "the ways they produce, exchange, and consume goods and services.")),

 dict(q=("Which of the following claims about this topic does the framework NOT support?"),
      choices=[
        "That the Mongol khanates were the only new imperial states established anywhere in the period.",
        "That empires collapsed in different regions of the world during the period.",
        "That new imperial states replaced collapsed empires in some areas.",
        "That the expansion of empires facilitated Afro-Eurasian trade and communication.",
        "That interregional contacts and conflicts encouraged significant technological and cultural transfers.",
      ], ans=0,
      why=("KC-3.2.I.B.iii names the Mongol khanates with the word INCLUDING, which presents them "
           "as an instance rather than as the whole class. The other four options restate "
           "KC-3.2.I.B.iii, KC-3.1.I.E.i and KC-3.2.II.A.ii as they stand.")),

 dict(q=("Two developments are given: an empire extends its authority across several regions, and "
         "a technique known in one of those regions comes into use in another. Which of the "
         "following states the connection the framework would draw between them?"),
      choices=[
        "The first creates the contact within which the second becomes possible, since the framework treats interregional contact as an encouragement to technological transfer.",
        "The second creates the conditions for the first, since a shared technique is what allows an empire to extend its authority.",
        "The two are unrelated, since the framework treats political and technical history separately.",
        "The first prevents the second, since an empire restricts the movement of knowledge across its internal boundaries.",
        "The two are the same development described twice, since extending authority is itself a transfer of technique.",
      ], ans=0,
      why=("KC-3.2.II.A.ii states that interregional contacts and conflicts between states and "
           "empires encouraged significant technological and cultural transfers, and KC-3.1.I.E.i "
           "records imperial expansion facilitating communication. Suggested skill 5.A asks for "
           "the connection between two processes, which here runs from contact to transfer.")),

 dict(q=("Which of the following identifies why the adoption of a script by an imperial "
         "administration counts as a cultural transfer in the framework's sense?"),
      choices=[
        "Because a practice belonging to one people comes into use among another through the contact between them, which is what the framework's phrase technological and cultural transfers describes.",
        "Because it is a change in government rather than in culture, and the framework treats the two as one subject.",
        "Because a script is a trade good, and the framework treats transfers as a form of commerce.",
        "Because the adopting people abandoned every practice of its own at the same time.",
        "Because the framework treats writing as the only cultural practice capable of being transferred.",
      ], ans=0,
      why=("KC-3.2.II.A.ii states that interregional contacts and conflicts between states and "
           "empires, including the Mongols, encouraged significant technological and cultural "
           "transfers, and the adoption of Uyghur script is the topic page's own illustrative "
           "instance. The Cultural Developments thematic focus supplies the wider point that "
           "interactions of societies carry political and cultural implications.")),

 dict(q=("A student asks why the framework discusses the Mongol Empire under continuity as well "
         "as change. Which of the following is the best answer from this topic?"),
      choices=[
        "Because the learning objective asks for its significance in larger patterns of continuity and change, and the framework places it inside a pattern of imperial collapse and replacement that was older than the empire itself.",
        "Because the framework holds that nothing about Eurasia changed during the empire's existence.",
        "Because the framework holds that the empire changed everything and continued nothing.",
        "Because the framework treats continuity and change as two names for the same process.",
        "Because the framework treats the empire as belonging to a period other than this one.",
      ], ans=0,
      why=("Learning Objective D asks students to explain the significance of the Mongol Empire "
           "in larger patterns of continuity and change, and KC-3.2.I.B.iii places the khanates "
           "among new imperial states replacing collapsed empires, a pattern the sentence "
           "describes as occurring in different regions of the world.")),

 dict(q=("An unattributed report from a frontier district states that after its incorporation the "
         "same goods continued to be produced there, but that officials now recorded their "
         "movement and levied a share. Which of the following identifies the pattern?"),
      choices=[
        "Continuity in what a district produced together with change in the network and the authority through which it moved, which is how incorporation can alter exchange without altering production.",
        "Change in what a district produced together with continuity in the authority over it.",
        "The cessation of production in the district upon its incorporation.",
        "The withdrawal of any authority from the district following its incorporation.",
        "The removal of the district's goods from every trade network.",
      ], ans=0,
      why=("KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and "
           "communication as new people were drawn into their conquerors' economies and trade "
           "networks, and Learning Objective D asks for the Mongol Empire's place in larger "
           "patterns of CONTINUITY AND CHANGE. The anchor carries both halves because the "
           "strongest distractor exchanges them.")),

 dict(q=("Which of the following would most weaken a claim that imperial expansion in this period "
         "made no difference to the volume of long-distance exchange?"),
      choices=[
        "Records showing communities entering a trade network for the first time in the years following their incorporation into an expanding empire.",
        "Records showing that long-distance exchange existed before the expansion as well as after it.",
        "Records showing that the goods exchanged were the same before and after the expansion.",
        "Records showing that merchants continued to face dangers on the roads after the expansion.",
        "Records showing that the empire concerned collected dues on the traffic it protected.",
      ], ans=0,
      why=("KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and "
           "communication AS NEW PEOPLE WERE DRAWN INTO their conquerors' economies and trade "
           "networks. New entrants are the framework's own mechanism, so evidence of them bears "
           "directly on a claim that expansion made no difference.")),

 dict(q=("Which of the following identifies a limit on what this topic's key concepts allow a "
         "student to claim about cultural transfers?"),
      choices=[
        "They state that contacts and conflicts encouraged significant transfers without stating which party in any exchange gained more by it.",
        "They state that no cultural transfer occurred in this period.",
        "They state that transfers moved in one direction only.",
        "They state that transfers were confined to technology and never touched culture.",
        "They state precisely how many transfers took place in the period.",
      ], ans=0,
      why=("KC-3.2.II.A.ii states that interregional contacts and conflicts between states and "
           "empires, including the Mongols, encouraged significant technological AND CULTURAL "
           "transfers. It names no direction, no magnitude and no beneficiary, so a claim about "
           "who gained more would go beyond the sentence.")),

 dict(q=("An unattributed account of a court describes envoys of several distant rulers waiting "
         "together for audience, each having travelled by roads under one authority for the "
         "greater part of the journey. Which of the following identifies the pattern?"),
      choices=[
        "Imperial expansion facilitating communication between regions that had had little occasion to send word to one another before.",
        "Imperial expansion severing communication between regions previously in contact.",
        "The collapse of an empire leaving each region to communicate for itself.",
        "The confinement of diplomacy to rulers whose territories adjoined one another.",
        "The replacement of envoys by merchants as the only travellers between regions.",
      ], ans=0,
      why=("KC-3.1.I.E.i states that the expansion of empires, including the Mongols, facilitated "
           "Afro-Eurasian trade AND COMMUNICATION. Envoys able to travel a long road under one "
           "authority are the communication half of that sentence.")),

 dict(q=("Which of the following best identifies the difference between the framework's claim "
         "about trade and its claim about transfers of knowledge in this topic?"),
      choices=[
        "The first attributes the facilitation to the expansion of empires, and the second attributes the encouragement to the contacts and conflicts between them, so the two sentences name different agents.",
        "The first attributes the facilitation to contacts and conflicts, and the second attributes the encouragement to the expansion of empires.",
        "Both attribute their effect to the expansion of empires, so no difference is being drawn.",
        "Both attribute their effect to contacts and conflicts, so no difference is being drawn.",
        "Neither sentence attributes its effect to anything, so no comparison is possible.",
      ], ans=0,
      why=("KC-3.1.I.E.i names the expansion of empires as what facilitated Afro-Eurasian trade "
           "and communication, while KC-3.2.II.A.ii names interregional contacts and conflicts "
           "between states and empires as what encouraged technological and cultural transfers. "
           "The anchor carries both attributions in order because the strongest distractor "
           "exchanges them.")),

 dict(q=("A student wishes to argue that an empire's effect on exchange outlasted the empire "
         "itself. Which of the following would the framework allow as a starting point?"),
      choices=[
        "That the framework says its own dates are approximate and that developments may continue after the period in which they are studied.",
        "That the framework fixes the end of every consequence at the end of the state that produced it.",
        "That the framework denies that empires in this period had any effect on exchange.",
        "That the framework treats every effect as beginning and ending in the same year.",
        "That the framework treats exchange as unaffected by political authority of any kind.",
      ], ans=0,
      why=("The CED states that events, processes, and developments are not constrained by the "
           "given dates and may begin before, or continue after, the period, and KC-3.1.I.E.i "
           "asserts that imperial expansion facilitated Afro-Eurasian trade and communication. "
           "The first sentence is what licenses a claim reaching past the period's end.")),

 dict(q=("Which of the following pairs a development from this topic with a genuine consequence "
         "of it rather than with a coincidence?"),
      choices=[
        "Peoples brought under an expanding empire, paired with their appearance in trade networks that had not previously reached them.",
        "Peoples brought under an expanding empire, paired with the fact that trade existed somewhere in Afro-Eurasia at the same time.",
        "The collapse of an empire, paired with the fact that some empires had existed for a long time.",
        "A transfer of knowledge between regions, paired with the fact that knowledge had been written down in both.",
        "The establishment of a new imperial state, paired with the fact that the region concerned had a name.",
      ], ans=0,
      why=("KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and "
           "communication as new people were drawn into their conquerors' economies and trade "
           "networks, which is a consequence the framework asserts. Suggested skill 5.A asks for "
           "connections between developments, and the four rejected pairings connect a "
           "development to a circumstance that would hold anyway.")),

 dict(q=("Which of the following identifies the sense in which the framework calls the transfers "
         "of this period significant?"),
      choices=[
        "That they carried techniques and practices from one region into use in another, so their consequence was not confined to the encounter that produced them.",
        "That they were more numerous than the transfers of any other period.",
        "That they were approved of by the rulers of the regions concerned.",
        "That they were recorded in writing by those who witnessed them.",
        "That they were confined to the courts of the empires that produced them.",
      ], ans=0,
      why=("KC-3.2.II.A.ii states that interregional contacts and conflicts between states and "
           "empires encouraged SIGNIFICANT technological and cultural transfers, and the topic's "
           "illustrative list gives instances in which a body of knowledge or a script came into "
           "use in a region other than its own. The framework makes no comparison with other "
           "periods.")),

 dict(q=("An unattributed set of instructions for officials of an empire directs that merchants "
         "of any origin be given passage and that their disputes be heard by the same procedure "
         "wherever they arise. Which of the following identifies the connection between this and "
         "the growth of exchange?"),
      choices=[
        "A government exercising its power in a way that lowered the cost of moving and dealing across its territory, which is one route by which imperial expansion facilitated trade.",
        "A government withdrawing from the regulation of trade, which left merchants to arrange matters among themselves.",
        "A government confining trade to merchants born within its own territory.",
        "A government substituting official carriage for private trade altogether.",
        "A government treating the movement of merchants as unconnected with its own interests.",
      ], ans=0,
      why=("KC-3.1.I.E.i states that the expansion of empires facilitated Afro-Eurasian trade and "
           "communication, and the Governance thematic focus states that governments maintain "
           "order through a variety of administrative institutions, policies, and procedures and "
           "exercise power in different ways and for different purposes.")),

 dict(q=("Which of the following statements about this topic is supported by all three of its "
         "historical developments taken together?"),
      choices=[
        "An empire could arise where another had collapsed, draw the peoples it conquered into its own networks of exchange, and by the contacts and conflicts that followed encourage techniques and practices to move between regions.",
        "An empire could arise only where no other had existed, kept the peoples it conquered out of its networks, and prevented techniques from moving between regions.",
        "Empires in this period neither collapsed nor were replaced, and exchange between regions was unaffected by them.",
        "Empires in this period expanded, but no people was drawn into a new network and no technique moved anywhere.",
        "Nothing can be said about empires in this period, since the framework makes no assertion about them.",
      ], ans=0,
      why=("KC-3.2.I.B.iii supplies collapse and replacement by new imperial states including the "
           "Mongol khanates, KC-3.1.I.E.i the drawing of new peoples into their conquerors' "
           "economies and trade networks, and KC-3.2.II.A.ii the transfers encouraged by "
           "interregional contacts and conflicts. The key states all three; each rejected option "
           "contradicts at least one.")),
]
