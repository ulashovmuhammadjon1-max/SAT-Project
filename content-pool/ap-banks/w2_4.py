# AP WORLD HISTORY: MODERN 2.4 Trans-Saharan Trade Routes  (title copied verbatim from
# WORLD_HISTORY_topics.json). Unit 2 Networks of Exchange, c. 1200 to c. 1450.
# Suggested skill 1.B, explain a historical concept, development, or process.
#
# THE CED CONTENT OF THIS TOPIC, in the framework's own words. The page carries two
# thematic focus blocks and two learning objectives:
#
#   Thematic focus TEC: human adaptation and innovation have resulted in increased
#           efficiency, comfort, and security, and technological advances have shaped
#           human development and interactions with both intended and unintended
#           consequences.
#   LO 2.H  Explain the causes and effects of the growth of trans-Saharan trade.
#   KC-3.1.II.A.ii  The growth of interregional trade was encouraged by innovations in
#           existing transportation technologies.
#   KC-3.1.I.A.iv  Improved transportation technologies and commercial practices led to
#           an increased volume of trade and expanded the geographical range of
#           existing trade routes, including the trans-Saharan trade network.
#
#   Thematic focus GOV: a variety of internal and external factors contribute to state
#           formation, expansion, and decline. Governments maintain order through a
#           variety of administrative institutions, policies, and procedures, and
#           governments obtain, retain, and exercise power in different ways and for
#           different purposes.
#   LO 2.I  Explain how the expansion of empires influenced trade and communication
#           over time.
#   KC-3.1.I.E.ii  The expansion of empires -- including Mali in West Africa --
#           facilitated Afro-Eurasian trade and communication as new people were drawn
#           into the economies and trade networks.
#
#   Illustrative examples printed on this topic page: technologies encouraging
#           interregional trade -- the camel saddle, caravans. The CED states that
#           illustrative examples "do not in any way constitute additional, preferred,
#           or required information", so no key here turns on one.
#
# A DIFFERENCE BETWEEN TWO NEARLY IDENTICAL SENTENCES, WHICH IS REAL AND CHECKABLE.
# KC-3.1.I.E.i, on which topic 2.2 rests, says new people were drawn into THEIR
# CONQUERORS' economies and trade networks. KC-3.1.I.E.ii, this topic's sentence, says
# they were drawn into THE economies and trade networks -- no possessive, no
# conquerors. The framework says the same thing of imperial expansion in both places
# and assigns ownership in only one of them. q13 turns on that and on nothing else,
# and the difference was read off the CED text rather than assumed from memory.
#
# THE SUGGESTED SKILL SHAPES THE BANK. Skill 1.B is to EXPLAIN a concept, development
# or process, so these items ask which account explains something rather than which
# observation evidences it. Topic 1.5 shares this skill, so the stems here are built
# around sources and situations rather than around the bare imperative that module
# uses, and no item repeats one of its question shapes.
#
# ON THE SOURCES. This bank cannot show an image. Every stimulus is a table of
# HYPOTHETICAL figures whose keyed conclusion is recoverable from the table alone, or
# an explicitly unattributed illustrative source. Mali is named only where the CED
# names it, in KC-3.1.I.E.ii, and no key asserts anything further about it.
#
# ON DATES. Spans are written "c. 1200 to c. 1450". The CED states that events,
# processes, and developments are not constrained by the given dates and may begin
# before, or continue after, the period, so no key turns on a boundary year.
TOPIC = ("2.4", "Trans-Saharan Trade Routes", 2)

_T_LOADS = dict(
    headers=["Carrying arrangement (hypothetical)", "Load carried per animal in units",
             "Days the animal can travel between waterings"],
    rows=[["Arrangement One", "60", "3"],
          ["Arrangement Two", "130", "8"],
          ["Arrangement Three", "95", "5"]])

_T_EMPIRE = dict(
    headers=["Period (hypothetical)", "Districts within the empire",
             "Communities recorded trading into the network"],
    rows=[["Earliest", "8", "12"],
          ["Middle", "15", "25"],
          ["Latest", "26", "48"]])

_T_CARAVANS = dict(
    headers=["Caravan (hypothetical)", "Animals travelling in the caravan",
             "Guards recorded travelling with it"],
    rows=[["Caravan One", "200", "12"],
          ["Caravan Two", "450", "27"],
          ["Caravan Three", "80", "8"]])

QUESTIONS = [
 dict(q=("An unattributed manual for merchants describes a fitting for the back of a pack animal "
         "that allows a heavier load to be carried without injuring the beast, and notes that "
         "companies of such animals now travel together under one guide. Which of the following "
         "best explains how arrangements of this kind bore on interregional trade?"),
      choices=[
        "They are innovations in transportation technologies already in use, and the framework treats such innovations as encouragements to the growth of interregional trade.",
        "They are commercial rather than transportation arrangements, and the framework treats only commercial arrangements as bearing on trade.",
        "They are inventions without precedent, and the framework treats only wholly new technologies as bearing on trade.",
        "They have no bearing on trade, which the framework explains by demand alone.",
        "They discouraged interregional trade by raising the cost of moving goods.",
      ], ans=0,
      why=("KC-3.1.II.A.ii states that the growth of interregional trade was encouraged by "
           "innovations in EXISTING transportation technologies, and the topic page names the "
           "camel saddle and caravans as its illustrative instances. The word existing is what "
           "rules out the option about inventions with no precedent.")),

 dict(q=("Which of the following best explains why the framework describes the trans-Saharan "
         "network as a route whose range was expanded rather than as one that was newly opened?"),
      choices=[
        "Because it names the trans-Saharan network among EXISTING trade routes whose geographical range improved transportation technologies and commercial practices expanded.",
        "Because it states that the network was first established during this period.",
        "Because it states that the network fell out of use during this period.",
        "Because it states that the network's extent was unchanged throughout the period.",
        "Because it makes no statement about the extent of the network at any point.",
      ], ans=0,
      why=("KC-3.1.I.A.iv states that improved transportation technologies and commercial "
           "practices led to an increased volume of trade and expanded the geographical range of "
           "existing trade routes, INCLUDING THE TRANS-SAHARAN TRADE NETWORK. The sentence puts "
           "the network among routes already in use.")),

 dict(q=("The table below carries HYPOTHETICAL figures for three ways of loading a pack animal, "
         "giving the load each can carry and the days it can travel between waterings. Which "
         "conclusion do these numbers support?"),
      table=_T_LOADS,
      choices=[
        "Load carried and days between waterings rise together across the arrangements listed, so an improvement in one is not paid for by a loss in the other.",
        "Load carried and days between waterings move in opposite directions across the arrangements listed.",
        "The arrangement carrying the most per animal travels the fewest days between waterings.",
        "Every arrangement listed allows the same number of days between waterings.",
        "The arrangement carrying the least per animal travels the most days between waterings.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns, distractors included. KC-3.1.II.A.ii "
           "states that the growth of interregional trade was encouraged by innovations in "
           "existing transportation technologies, and the Technology thematic focus says human "
           "adaptation and innovation have resulted in increased efficiency. Two measures "
           "improving together is what such an innovation looks like in figures.")),

 dict(q=("Which of the following best explains why a desert crossing places a heavier demand on "
         "transportation technology than a journey of the same length through settled country?"),
      choices=[
        "Because the stages at which water and provisions may be taken up are fewer and further apart, so what a party can carry between them sets the limit on the journey.",
        "Because goods lose their value in proportion to the distance they are carried.",
        "Because trade across a desert is conducted without any commercial arrangements.",
        "Because a desert crossing requires no knowledge of the route to be undertaken.",
        "Because settled country offers no opportunity to exchange goods along the way.",
      ], ans=0,
      why=("KC-3.1.II.A.ii states that the growth of interregional trade was encouraged by "
           "innovations in existing transportation technologies, and the Technology thematic "
           "focus states that human adaptation and innovation have resulted in increased "
           "efficiency, comfort, and security. What a party can carry between stages is the "
           "constraint such innovations relieve.")),

 dict(q=("HYPOTHETICAL counts for one expanding empire are set out in the table below, giving the "
         "districts within it and the communities recorded trading into the network, at three "
         "successive periods. Which conclusion does the data best support?"),
      table=_T_EMPIRE,
      choices=[
        "Both counts rise at every step, and at each step the communities trading into the network rise by more than the districts do.",
        "Both counts rise at every step, and at each step the districts rise by more than the trading communities do.",
        "The districts rise while the communities trading into the network fall.",
        "Both counts are unchanged across the three periods listed.",
        "The communities trading into the network rise while the districts fall.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.1.I.E.ii states that the "
           "expansion of empires, including Mali in West Africa, facilitated Afro-Eurasian trade "
           "and communication as new people were drawn into the economies and trade networks. The "
           "anchor carries both clauses because the strongest distractor exchanges the two "
           "columns.")),

 dict(q=("An unattributed account of a caravan describes a company of many animals travelling "
         "together with a guide who knows the wells, guards hired in common, and merchants who "
         "have agreed in advance how the cost of the guide and the guards is to be shared. Which "
         "of the following best explains why such a company travels together rather than "
         "separately?"),
      choices=[
        "Because travelling in company spreads the cost of guidance and protection and reduces the risk each merchant runs, which is how an arrangement of this kind increases the security of a journey.",
        "Because a single merchant is forbidden by the framework's account to undertake a journey.",
        "Because the goods carried can only be sold if they arrive together in one lot.",
        "Because travelling in company shortens the distance that has to be covered.",
        "Because the animals cannot be induced to walk unless many are gathered.",
      ], ans=0,
      why=("The Technology thematic focus states that human adaptation and innovation have "
           "resulted in increased efficiency, comfort, and SECURITY, and KC-3.1.II.A.ii names "
           "innovations in existing transportation technologies as an encouragement to "
           "interregional trade, with caravans as this page's illustrative instance.")),

 dict(q=("The table below carries HYPOTHETICAL figures for three caravans, giving the animals "
         "travelling in each and the guards recorded with it. Which statement is best supported?"),
      table=_T_CARAVANS,
      choices=[
        "The caravan with the most guards in total is not the caravan carrying the most guards for each hundred animals.",
        "The caravan with the most animals also carries the most guards for each hundred animals.",
        "The smallest caravan listed travels without any guards at all.",
        "Every caravan listed carries the same number of guards for each hundred animals.",
        "The caravan with the fewest animals carries the most guards in total.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.1.II.A.ii names innovations in "
           "existing transportation technologies as an encouragement to interregional trade, with "
           "caravans among this page's illustrative instances, and the Technology thematic focus "
           "names increased security among the results of human adaptation. A total and a rate "
           "that point to different caravans is the distinction such figures allow a student to "
           "draw.")),

 dict(q=("Which of the following best explains the framework's claim that the expansion of "
         "empires facilitated trade and communication?"),
      choices=[
        "Because peoples not previously part of a network were drawn into the economies and trade networks as an empire extended over them.",
        "Because an empire's expansion emptied the territory it crossed of merchants.",
        "Because trade and communication caused imperial expansion rather than following from it.",
        "Because an empire's expansion confined trade to its own original territory.",
        "Because expansion made no difference to trade, which followed the same routes regardless.",
      ], ans=0,
      why=("KC-3.1.I.E.ii states that the expansion of empires, including Mali in West Africa, "
           "facilitated Afro-Eurasian trade and communication as new people were drawn into the "
           "economies and trade networks. Expansion comes first in that sentence and facilitation "
           "follows, which is what the reversed option gets wrong.")),

 dict(q=("An unattributed toll register from a desert-edge town records dues taken on salt "
         "arriving from one direction and on other goods leaving in the other, together with the "
         "names of the officers who took them. Which of the following best explains what a "
         "register of this kind shows about the relation between a state and a trade route?"),
      choices=[
        "That a government could turn traffic passing through its territory into revenue, which is one of the ways power is exercised and one of the reasons a state takes an interest in a route.",
        "That a government's only interest in a route was to close it to traffic.",
        "That the traffic on the route was carried on without any government's knowledge.",
        "That the officers named were merchants rather than servants of any state.",
        "That the goods recorded were produced in the town where the dues were taken.",
      ], ans=0,
      why=("The Governance thematic focus states that governments obtain, retain, and exercise "
           "power in different ways and for different purposes and maintain order through "
           "administrative institutions, policies, and procedures, and KC-3.1.I.E.ii ties "
           "imperial expansion to the facilitation of trade and communication.")),

 dict(q=("Which of the following best explains why the framework counts the growth of "
         "trans-Saharan trade as having causes on more than one side?"),
      choices=[
        "Because it names innovations in existing transportation technologies, improved commercial practices and the expansion of empires in separate sentences about the same growth.",
        "Because it names a single cause and treats every other factor as a consequence of it.",
        "Because it treats the growth as having occurred without any cause that can be identified.",
        "Because it treats the growth as caused entirely by the demand of one region.",
        "Because it treats the growth as caused by a change in the desert itself.",
      ], ans=0,
      why=("KC-3.1.II.A.ii names innovations in existing transportation technologies, "
           "KC-3.1.I.A.iv names improved transportation technologies and commercial practices, "
           "and KC-3.1.I.E.ii names the expansion of empires. Learning Objective H asks for the "
           "causes and effects of the growth of trans-Saharan trade.")),

 dict(q=("A student writes that the technologies encouraging trans-Saharan trade were all "
         "invented in this period. Which of the following best explains the error?"),
      choices=[
        "The framework speaks of innovations in EXISTING transportation technologies, which describes the improvement and spread of arrangements already in use.",
        "The framework speaks of technologies that had been abandoned before this period and were revived in it.",
        "The framework speaks of technologies used only outside the desert regions.",
        "The framework speaks of no technologies at all in connection with this trade.",
        "The framework speaks of technologies that were reserved to rulers and denied to merchants.",
      ], ans=0,
      why=("KC-3.1.II.A.ii states that the growth of interregional trade was encouraged by "
           "innovations in EXISTING transportation technologies, and KC-3.1.I.A.iv likewise "
           "speaks of expanding the range of EXISTING trade routes. Both adjectives are the "
           "framework's own.")),

 dict(q=("Which of the following best explains the Technology thematic focus's remark that "
         "technological advances have both intended and unintended consequences?"),
      choices=[
        "That a device adopted to solve one problem may also change things nobody adopting it had in view, so its effects are not exhausted by its purpose.",
        "That a device adopted to solve one problem always fails to solve it.",
        "That every consequence of a technological advance is foreseen by those who adopt it.",
        "That technological advances have consequences only for those who use them directly.",
        "That the consequences of a technological advance are confined to the period in which it appears.",
      ], ans=0,
      why=("The Technology thematic focus states that technological advances have shaped human "
           "development and interactions WITH BOTH INTENDED AND UNINTENDED CONSEQUENCES, and the "
           "phrase is the framework's own. KC-3.1.II.A.ii supplies the case in this topic, since "
           "an innovation in an existing transportation technology encouraged a growth of trade "
           "that reached well past the journeys it was adopted to ease.")),

 dict(q=("The framework says of imperial expansion in one place that new people were drawn into "
         "their conquerors' economies, and in another place that they were drawn into the "
         "economies and trade networks. Which of the following best explains what a careful "
         "student should take from that difference?"),
      choices=[
        "That the sentence naming conquerors assigns the networks an owner while the other does not, so a claim about whose networks these were should rest on the sentence that says so.",
        "That the sentence naming conquerors assigns no owner while the other does, so the two have been described the wrong way round.",
        "That the two sentences are identical, so no difference of any kind arises.",
        "That the framework denies in one place what it asserts in the other, so one of the two must be disregarded.",
        "That neither sentence says anything about people being drawn into a network.",
      ], ans=0,
      why=("KC-3.1.I.E.i states that new people were drawn into THEIR CONQUERORS' economies and "
           "trade networks, while KC-3.1.I.E.ii, this topic's sentence, states that they were "
           "drawn into THE economies and trade networks. The anchor carries both halves in order "
           "because the strongest distractor exchanges them.")),

 dict(q=("An unattributed traveller's account describes a ruler receiving merchants at his court, "
         "confirming the safety of the roads through his territory, and settling in his own "
         "presence a dispute between traders of two different regions. Which of the following "
         "best explains the connection between such conduct and the growth of trade?"),
      choices=[
        "A ruler who makes passage and redress dependable lowers what a merchant must risk, and the framework treats the expansion of such authority as facilitating trade and communication.",
        "A ruler who receives merchants thereby ceases to govern his own subjects.",
        "A ruler's interest in trade is evidence that his state had no other source of revenue.",
        "A ruler settling a dispute between foreigners is acting outside any authority he holds.",
        "A ruler's protection of a road has no effect on the traffic that uses it.",
      ], ans=0,
      why=("KC-3.1.I.E.ii states that the expansion of empires, including Mali in West Africa, "
           "facilitated Afro-Eurasian trade and communication, and the Governance thematic focus "
           "states that governments maintain order through a variety of administrative "
           "institutions, policies, and procedures.")),

 dict(q=("Which of the following claims about trans-Saharan trade does the framework NOT support?"),
      choices=[
        "That the trade began only after an empire had been established across the whole of the route.",
        "That the growth of interregional trade was encouraged by innovations in existing transportation technologies.",
        "That improved transportation technologies and commercial practices increased the volume of trade.",
        "That the geographical range of existing routes was expanded, the trans-Saharan network among them.",
        "That the expansion of empires facilitated Afro-Eurasian trade and communication.",
      ], ans=0,
      why=("KC-3.1.II.A.ii, KC-3.1.I.A.iv and KC-3.1.I.E.ii between them assert the "
           "encouragement given by innovations in existing technologies, the increase in volume "
           "and range, and the facilitation by imperial expansion. None of them makes an empire a "
           "precondition of the trade's existence, and KC-3.1.I.A.iv calls the network an "
           "existing route.")),

 dict(q=("Which of the following best explains why a state astride a trade route may grow "
         "stronger as the traffic on that route grows?"),
      choices=[
        "Because the traffic supplies it with dues, with goods it can direct, and with a reason for other powers to deal with it, all of which are means by which authority is obtained and retained.",
        "Because a state's strength is fixed by the extent of its territory alone and traffic is irrelevant to it.",
        "Because traffic passing through a territory weakens the authority governing it.",
        "Because a state that taxes traffic thereby loses the allegiance of its own subjects.",
        "Because trade and government were kept entirely separate in this period.",
      ], ans=0,
      why=("The Governance thematic focus states that governments obtain, retain, and exercise "
           "power in different ways and for different purposes, and KC-3.1.I.E.ii links the "
           "expansion of empires to the facilitation of Afro-Eurasian trade and communication as "
           "new people were drawn into the economies and trade networks.")),

 dict(q=("An unattributed letter describes a merchant sending goods south with an agent, "
         "receiving in return goods brought north, and settling the difference at a later "
         "meeting rather than at the moment of exchange. Which of the following best explains "
         "what this arrangement contributed to the trade?"),
      choices=[
        "It is an improved commercial practice, and the framework names such practices beside transportation technologies as causes of an increased volume of trade.",
        "It is an improved transportation technology, since the goods moved further as a result.",
        "It shows that no exchange took place, since nothing was settled at the meeting.",
        "It shows that the merchant had withdrawn from long-distance trade.",
        "It shows that goods in this trade were exchanged only for coin paid at once.",
      ], ans=0,
      why=("KC-3.1.I.A.iv states that improved transportation technologies AND COMMERCIAL "
           "PRACTICES led to an increased volume of trade and expanded the geographical range of "
           "existing trade routes, including the trans-Saharan trade network. Deferred settlement "
           "between partners is a commercial practice rather than a transport technology.")),

 dict(q=("Which of the following best explains why the framework's phrase increased efficiency "
         "is not the same claim as increased trade?"),
      choices=[
        "Because efficiency describes what a given effort can accomplish, while an increase in trade describes how much is actually carried, and the first is one of the conditions of the second rather than the second itself.",
        "Because efficiency describes how much is carried and trade describes what a given effort can accomplish.",
        "Because the two are the same claim expressed in different words.",
        "Because efficiency bears on commercial practice and can have no bearing on transport.",
        "Because an increase in trade must always be accompanied by a fall in efficiency.",
      ], ans=0,
      why=("The Technology thematic focus states that human adaptation and innovation have "
           "resulted in increased efficiency, comfort, and security, while KC-3.1.I.A.iv states "
           "that improved technologies and practices led to an increased VOLUME OF TRADE. The "
           "anchor carries both halves in order because the strongest distractor exchanges "
           "them.")),

 dict(q=("A historian argues that the trans-Saharan trade should be studied as part of "
         "Afro-Eurasian exchange rather than as a separate West African subject. Which of the "
         "following best supports that argument from this topic?"),
      choices=[
        "That the framework describes the expansion of empires including Mali as facilitating AFRO-EURASIAN trade and communication, placing the West African case inside a wider network.",
        "That the framework describes the trans-Saharan network as unconnected to any other route.",
        "That the framework describes West Africa as outside the scope of the period.",
        "That the framework describes the trade as confined to goods produced within the desert itself.",
        "That the framework describes the trade as having no participants beyond a single empire.",
      ], ans=0,
      why=("KC-3.1.I.E.ii states that the expansion of empires, including Mali in West Africa, "
           "facilitated Afro-Eurasian trade and communication as new people were drawn into the "
           "economies and trade networks. The adjective Afro-Eurasian is the framework's own.")),

 dict(q=("Which of the following best explains the difference between what KC-3.1.II.A.ii "
         "asserts and what KC-3.1.I.A.iv asserts?"),
      choices=[
        "The first says innovations in existing transportation technologies encouraged the growth of interregional trade, while the second adds commercial practices and names the volume and range that grew.",
        "The first names the volume and range that grew, while the second says innovations in existing transportation technologies encouraged the growth of trade.",
        "The two assert the same thing in the same words, so no difference arises.",
        "The first concerns maritime routes and the second overland ones.",
        "Neither sentence makes any assertion about transportation technologies.",
      ], ans=0,
      why=("KC-3.1.II.A.ii states that the growth of interregional trade was encouraged by "
           "innovations in existing transportation technologies, and KC-3.1.I.A.iv states that "
           "improved transportation technologies AND COMMERCIAL PRACTICES led to an increased "
           "volume of trade and expanded the geographical range of existing trade routes. The "
           "anchor carries both halves in order because the strongest distractor exchanges "
           "them.")),

 dict(q=("An unattributed record from a town at the desert's southern edge notes that its "
         "population has grown, that quarters have been built for merchants who winter there, and "
         "that its market now deals in goods from beyond the desert as well as from its own "
         "country. Which of the following best explains this growth?"),
      choices=[
        "That an increased volume of traffic on a route made the places where it halted into centres of exchange in their own right.",
        "That the town's growth was caused by the desert becoming easier to cross for people who never traded.",
        "That the town grew because its own country ceased to produce anything for sale.",
        "That the town grew because merchants were forbidden to travel beyond it.",
        "That the town's growth had no relation to the traffic passing through it.",
      ], ans=0,
      why=("KC-3.1.I.A.iv states that improved transportation technologies and commercial "
           "practices led to an increased volume of trade and expanded the geographical range of "
           "existing trade routes, including the trans-Saharan trade network, promoting the "
           "growth of powerful new trading cities.")),

 dict(q=("Which of the following best explains why the framework treats being drawn into a trade "
         "network as an effect of imperial expansion rather than as a coincidence of it?"),
      choices=[
        "Because the sentence makes the drawing in the consequence of the expansion, joining the two with the word as rather than setting them side by side.",
        "Because the sentence names the drawing in first and the expansion afterwards.",
        "Because the sentence denies that any empire expanded during the period.",
        "Because the sentence treats trade networks as older than any empire and therefore unaffected.",
        "Because the sentence describes the two as occurring in different centuries.",
      ], ans=0,
      why=("KC-3.1.I.E.ii states that the expansion of empires, including Mali in West Africa, "
           "facilitated Afro-Eurasian trade and communication AS new people were drawn into the "
           "economies and trade networks. The connective is the framework's own and it makes the "
           "second clause a consequence of the first.")),

 dict(q=("Which of the following best explains a limit on what this topic's key concepts allow a "
         "student to claim?"),
      choices=[
        "They state that innovations in existing transportation technologies encouraged the growth of trade without naming which innovation mattered most.",
        "They state precisely which innovation mattered most and in what degree.",
        "They state that no innovation in transportation technology bore on the trade.",
        "They state that transportation technologies were the only cause of the trade's growth.",
        "They state that the trade grew without any encouragement of any kind.",
      ], ans=0,
      why=("KC-3.1.II.A.ii states only that the growth of interregional trade was encouraged by "
           "innovations in existing transportation technologies, and the topic's illustrative "
           "list names the camel saddle and caravans without ranking them. The CED adds that "
           "illustrative examples do not constitute required information.")),

 dict(q=("Two students describe the same journey. One says the merchants crossed a barrier; the "
         "other says they used a route. Which of the following best explains how both "
         "descriptions can be accurate?"),
      choices=[
        "A desert is an obstacle that particular technologies and knowledge made passable, so the same ground is a barrier to those without them and a route to those with them.",
        "A desert is either a barrier or a route and cannot be both, so one student is simply mistaken.",
        "A desert ceased to be an obstacle during this period and became ordinary country.",
        "A route in the framework's sense is always a stretch of settled country and never a desert.",
        "The framework treats the difficulty of the ground as having no bearing on the traffic.",
      ], ans=0,
      why=("KC-3.1.II.A.ii states that the growth of interregional trade was encouraged by "
           "innovations in existing transportation technologies, and the Technology thematic "
           "focus states that human adaptation and innovation have resulted in increased "
           "efficiency, comfort, and security. What technology relieves is exactly the "
           "difficulty of the ground.")),

 dict(q=("Which of the following would most weaken a claim that the growth of trans-Saharan trade "
         "in this period owed nothing to political conditions?"),
      choices=[
        "Records showing communities entering the network in the years after an expanding empire brought their territory under its authority.",
        "Records showing that the goods carried across the desert were valuable in proportion to their weight.",
        "Records showing that the route had been used before the period as well as during it.",
        "Records showing that merchants travelled in companies rather than singly.",
        "Records showing that the animals used were suited to the ground they crossed.",
      ], ans=0,
      why=("KC-3.1.I.E.ii states that the expansion of empires, including Mali in West Africa, "
           "facilitated Afro-Eurasian trade and communication AS NEW PEOPLE WERE DRAWN INTO the "
           "economies and trade networks. New entrants following incorporation is the framework's "
           "own mechanism, and it is a political condition.")),

 dict(q=("An unattributed account describes a company crossing the desert with a guide who had "
         "made the passage many times and who chose the halting places by the season. Which of "
         "the following best explains the part such knowledge played?"),
      choices=[
        "It is knowledge of the ground and its conditions, without which the technologies of carriage would not by themselves have made the crossing dependable.",
        "It is a commercial practice, since the guide was paid for his service.",
        "It replaced the need for any technology of carriage at all.",
        "It shows that the crossing could be made at any season without difference.",
        "It shows that the company was not engaged in trade but in exploration.",
      ], ans=0,
      why=("KC-3.1.II.A.ii names innovations in existing transportation technologies as an "
           "encouragement to the growth of interregional trade, and the Technology thematic focus "
           "names increased security among the results of human adaptation. Knowing where the "
           "water lies is the adaptation on which the carriage depends.")),

 dict(q=("Which of the following best explains why an increase in the volume of trade and an "
         "expansion of a route's geographical range are two claims rather than one?"),
      choices=[
        "Because more may be carried over the same ground, or the same amount carried over more ground, and the framework asserts both of the routes it names.",
        "Because volume and range are two words for the distance a route covers.",
        "Because volume concerns the range of a route and range concerns the amount carried.",
        "Because the framework asserts only one of the two and a student must choose between them.",
        "Because an increase in volume must always accompany a reduction in range.",
      ], ans=0,
      why=("KC-3.1.I.A.iv states that improved transportation technologies and commercial "
           "practices led to an increased volume of trade AND expanded the geographical range of "
           "existing trade routes. Two effects are named, and the anchor carries both because the "
           "strongest distractor exchanges the definitions.")),

 dict(q=("A student wishes to explain why the same technologies could matter more in one region "
         "than in another. Which of the following best supports such an explanation from this "
         "topic?"),
      choices=[
        "That a technology relieves a particular difficulty, so its effect is largest where that difficulty is greatest, which is why arrangements for carriage and water bear especially on a desert route.",
        "That a technology has the same effect wherever it is adopted, so no regional difference can arise.",
        "That the framework assigns each technology to one region and forbids its use elsewhere.",
        "That a technology has no effect at all unless a government requires its use.",
        "That regional differences in this period were determined by demand alone.",
      ], ans=0,
      why=("The Technology thematic focus states that human adaptation and innovation have "
           "resulted in increased efficiency, comfort, and security, and KC-3.1.II.A.ii ties "
           "innovations in existing transportation technologies to the growth of interregional "
           "trade. An adaptation answers a condition, which is why conditions differ in what they "
           "reward.")),

 dict(q=("An unattributed report states that after a route's traffic increased, the settlements "
         "along it began to draw their grain from further away because their own fields could no "
         "longer feed the people gathered there. Which of the following best explains what this "
         "illustrates about a technological and commercial change?"),
      choices=[
        "That its consequences reached beyond what anyone adopting it intended, which is what the framework means by advances having both intended and unintended consequences.",
        "That its consequences were confined entirely to the merchants who adopted it.",
        "That the change had no consequences of any kind for the settlements concerned.",
        "That every consequence of the change was foreseen by those who brought it about.",
        "That the change reduced the number of people living along the route.",
      ], ans=0,
      why=("The Technology thematic focus states that technological advances have shaped human "
           "development and interactions WITH BOTH INTENDED AND UNINTENDED CONSEQUENCES, and "
           "KC-3.1.I.A.iv ties improved technologies and practices to an increased volume of "
           "trade on the trans-Saharan network among others.")),

 dict(q=("Which of the following statements about trans-Saharan trade is supported by this "
         "topic's key concepts taken together?"),
      choices=[
        "Improvements to arrangements for carriage that were already in use, together with better commercial practice, raised the volume carried and extended the reach of a route already in existence, while the expansion of empires drew further peoples into the exchange.",
        "Wholly new technologies opened a route that had not existed before, while the expansion of empires closed the exchange to peoples outside it.",
        "The volume carried fell across the period, the route contracted, and no empire had any bearing on the exchange.",
        "The volume carried rose, but no commercial practice altered and no people was drawn into the network who had not been in it before.",
        "Nothing can be said about this trade, since the framework makes no assertion about it.",
      ], ans=0,
      why=("KC-3.1.II.A.ii supplies the innovations in existing transportation technologies, "
           "KC-3.1.I.A.iv the improved commercial practices with the increased volume and "
           "expanded range of existing routes including the trans-Saharan network, and "
           "KC-3.1.I.E.ii the facilitation by imperial expansion as new people were drawn into "
           "the economies and trade networks. Each rejected option contradicts at least one.")),
]
