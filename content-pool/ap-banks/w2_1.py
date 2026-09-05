# AP WORLD HISTORY: MODERN 2.1 The Silk Roads  (title copied verbatim from
# WORLD_HISTORY_topics.json). Unit 2 Networks of Exchange, c. 1200 to c. 1450.
# Suggested skill 4.A, identify and describe a historical context for a specific
# historical development or process.
#
# THE CED CONTENT OF THIS TOPIC, in the framework's own words:
#
#   Thematic focus ECN: as societies develop, they affect and are affected by the ways
#           that they produce, exchange, and consume goods and services.
#   LO 2.A  Explain the causes and effects of growth of networks of exchange after 1200.
#   KC-3.1.I.A.i  Improved commercial practices led to an increased volume of trade and
#           expanded the geographical range of existing trade routes -- including the
#           Silk Roads -- promoting the growth of powerful new trading cities.
#   KC-3.1.I.C.i  The growth of interregional trade in luxury goods was encouraged by
#           innovations in previously existing transportation and commercial
#           technologies, including the caravanserai, forms of credit, and the
#           development of money economies.
#   KC-3.3.I.B  Demand for luxury goods increased in Afro-Eurasia. Chinese, Persian,
#           and Indian artisans and merchants expanded their production of textiles and
#           porcelains for export; manufacture of iron and steel expanded in China.
#
#   Illustrative examples printed on this topic page: trading cities -- Kashgar,
#           Samarkand; new forms of credit and money economies -- bills of exchange,
#           banking houses, use of paper money. The CED states that illustrative
#           examples "are intended as examples and do not in any way constitute
#           additional, preferred, or required information", so no key turns on one.
#
# THE TWO WORDS THIS TOPIC TURNS ON. KC-3.1.I.A.i says the routes' geographical range
# was EXPANDED and KC-3.1.I.C.i says the technologies innovated upon were PREVIOUSLY
# EXISTING. Both are claims about improvement of something already there rather than
# about invention from nothing, and several items below are built on exactly that,
# because it is the distinction a prepared student is most likely to get wrong.
#
# THE SUGGESTED SKILL SHAPES THE BANK. Skill 4.A is to identify and describe a
# historical CONTEXT for a development, so a recurring shape here is a source or a
# development followed by four candidate settings, of which one is the circumstance in
# which the development occurred and the others restate or exemplify the development
# itself. That is the error the skill exists to catch.
#
# ON THE SOURCES. This bank cannot show an image. Every stimulus is a table of
# HYPOTHETICAL figures whose keyed conclusion is recoverable from the table alone, or
# an explicitly unattributed illustrative source. No quotation is attributed to a real
# person or document.
#
# ON DATES. Spans are written "c. 1200 to c. 1450". The CED states that events,
# processes, and developments are not constrained by the given dates and may begin
# before, or continue after, the period, so no key turns on a boundary year.
TOPIC = ("2.1", "The Silk Roads", 2)

_T_CARAVANS = dict(
    headers=["Stage of the route (hypothetical)", "Caravans recorded in an earlier decade",
             "Caravans recorded in a later decade"],
    rows=[["Stage One", "40", "95"],
          ["Stage Two", "60", "140"],
          ["Stage Three", "25", "30"]])

_T_SETTLEMENT = dict(
    headers=["Market (hypothetical)", "Transactions settled in coin",
             "Transactions settled by a written instrument"],
    rows=[["Market One", "800", "200"],
          ["Market Two", "500", "500"],
          ["Market Three", "300", "700"]])

_T_GOODS = dict(
    headers=["Good (hypothetical)", "Units carried westward in an earlier period",
             "Units carried westward in a later period"],
    rows=[["Silk textiles", "300", "900"],
          ["Porcelain", "120", "480"],
          ["Worked iron", "60", "90"]])

QUESTIONS = [
 dict(q=("An unattributed merchant's handbook of the period sets out where along an overland "
         "route a traveller may find shelter for his animals, how a debt contracted at one city "
         "may be discharged at another, and which coins are accepted at each stage. A student "
         "asked to describe the context in which the volume of overland trade grew should "
         "identify which of the following?"),
      choices=[
        "That innovations in transportation and commercial technologies already in use, among them shelter for caravans, forms of credit and the spread of money economies, encouraged the growth of interregional trade in luxury goods.",
        "That the overland route was opened for the first time in this period, no earlier traffic having used it.",
        "That merchants of the period travelled without goods and carried only messages.",
        "That trade along the route was conducted entirely by barter, no coin or credit being available.",
        "That the growth of trade was confined to a single city and did not extend along the route.",
      ], ans=0,
      why=("KC-3.1.I.C.i states that the growth of interregional trade in luxury goods was "
           "encouraged by innovations in previously existing transportation and commercial "
           "technologies, including the caravanserai, forms of credit, and the development of "
           "money economies. The handbook describes all three, and each rejected option denies "
           "something the sentence asserts.")),

 dict(q=("Which of the following best states what KC-3.1.I.A.i claims improved commercial "
         "practices did to the trade routes already in use?"),
      choices=[
        "They increased the volume carried on those routes and expanded the geographical range the routes covered.",
        "They replaced the routes already in use with entirely new ones running elsewhere.",
        "They reduced the volume carried, since practices grew more cautious.",
        "They left the routes unchanged in both volume and extent.",
        "They confined trade to the two ends of each route, with nothing exchanged between.",
      ], ans=0,
      why=("KC-3.1.I.A.i states that improved commercial practices led to an increased volume of "
           "trade and expanded the geographical range of EXISTING trade routes, including the "
           "Silk Roads. Both halves are in the one sentence, and the sentence is about existing "
           "routes rather than new ones.")),

 dict(q=("A student writes that the technologies encouraging interregional trade in this period "
         "were invented from nothing during it. Which of the following identifies the error?"),
      choices=[
        "The framework describes innovations in previously existing transportation and commercial technologies, which is improvement of what was already in use rather than invention from nothing.",
        "The framework describes no technologies bearing on trade in this period at all.",
        "The framework describes the technologies as having been abandoned during this period.",
        "The framework describes the technologies as confined to maritime rather than overland trade.",
        "The framework describes the technologies as available only to rulers and not to merchants.",
      ], ans=0,
      why=("KC-3.1.I.C.i states that the growth of interregional trade in luxury goods was "
           "encouraged by innovations in PREVIOUSLY EXISTING transportation and commercial "
           "technologies. The adjective is the framework's own and it is what the student's "
           "sentence contradicts.")),

 dict(q=("The table below carries HYPOTHETICAL counts of caravans recorded at three stages of one "
         "overland route in an earlier and a later decade. Which conclusion does the data best "
         "support?"),
      table=_T_CARAVANS,
      choices=[
        "Every stage listed recorded more caravans in the later decade, and the stage with the largest increase in number is not the stage whose traffic multiplied by the largest factor.",
        "Every stage listed recorded fewer caravans in the later decade.",
        "The stage with the largest increase in number is also the stage whose traffic multiplied by the largest factor.",
        "One of the stages listed recorded the same number of caravans in both decades.",
        "The stage with the most caravans in the earlier decade had the smallest increase of any stage listed.",
      ], ans=0,
      why=("Recomputed in the verifier from the table alone, distractors included. KC-3.1.I.A.i "
           "states that improved commercial practices led to an increased volume of trade on "
           "existing routes, and a rise at every stage of one route is what an increase in volume "
           "looks like in figures.")),

 dict(q=("An unattributed account of a city on an overland route describes moneychangers seated "
         "in its market, agents who accept a sum in one place against payment in another, and "
         "quarters set aside for merchants from several regions. Which of the following describes "
         "the context in which such a city grew rather than restating that it grew?"),
      choices=[
        "Improved commercial practices raised the volume of trade and extended the range of existing routes, and cities of this kind grew because they stood where that traffic passed.",
        "The city contained a market in which goods were bought and sold.",
        "Merchants of several regions were present in the city at the same time.",
        "The city's moneychangers exchanged one coinage for another.",
        "The city was larger at the end of the period than at its beginning.",
      ], ans=0,
      why=("Suggested skill 4.A asks for the historical CONTEXT of a development rather than a "
           "restatement of it, and KC-3.1.I.A.i supplies that context by saying improved "
           "commercial practices increased the volume of trade and expanded the geographical "
           "range of existing routes, PROMOTING THE GROWTH of powerful new trading cities. The "
           "other four options describe features of the city itself.")),

 dict(q=("HYPOTHETICAL counts of how transactions were settled in three markets are given in the "
         "table below. Which conclusion is best supported by that data alone?"),
      table=_T_SETTLEMENT,
      choices=[
        "Every market listed records settlement of both kinds, and the share settled by a written instrument rises across the three markets.",
        "Every market listed settles more transactions by written instrument than in coin.",
        "The share settled in coin rises across the three markets listed.",
        "One of the markets listed records no transaction settled by a written instrument.",
        "The market recording the most settlements in coin also records the most by written instrument.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.1.I.C.i names forms of credit "
           "and the development of money economies among the innovations that encouraged the "
           "growth of interregional trade in luxury goods, and settlement by written instrument "
           "beside settlement in coin is what such a development looks like in a market's "
           "records.")),

 dict(q=("Which of the following identifies what the framework asserts about demand for luxury "
         "goods in Afro-Eurasia in this period?"),
      choices=[
        "It increased, and artisans and merchants in China, Persia and India expanded their production of goods for export in response.",
        "It fell, and production for export contracted accordingly.",
        "It was unchanged, and production for export was fixed by custom.",
        "It increased in China alone, production elsewhere being unaffected.",
        "It increased, but no producer anywhere altered what was made.",
      ], ans=0,
      why=("KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia and that "
           "Chinese, Persian, and Indian artisans and merchants expanded their production of "
           "textiles and porcelains for export. Three regions of producers are named, not one, "
           "and the demand and the response are asserted together.")),

 dict(q=("The table below carries HYPOTHETICAL quantities of three goods carried westward along "
         "one route in an earlier and a later period. Which statement is best supported?"),
      table=_T_GOODS,
      choices=[
        "All three goods listed moved in larger quantity in the later period, and porcelain multiplied by a larger factor than silk textiles did.",
        "All three goods listed moved in larger quantity in the later period, and silk textiles multiplied by a larger factor than porcelain did.",
        "At least one of the goods listed moved in smaller quantity in the later period.",
        "The three goods listed multiplied by the same factor.",
        "The good moving in the largest quantity in the earlier period multiplied by the largest factor.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.3.I.B states that demand for "
           "luxury goods increased in Afro-Eurasia and that artisans and merchants expanded "
           "production of textiles and porcelains for export. The anchor carries both clauses "
           "because the strongest distractor exchanges the two goods.")),

 dict(q=("A historian argues that the growth of overland trade in this period cannot be explained "
         "by rising demand alone. Which of the following would most strengthen that argument?"),
      choices=[
        "Evidence that the means of carrying and paying for goods improved at the same time, so that a rise in demand could be met rather than merely felt.",
        "Evidence that the goods traded were valuable in proportion to their weight.",
        "Evidence that one particular city on the route grew faster than its neighbours.",
        "Evidence that merchants kept records of the sums they were owed.",
        "Evidence that the route had been in use before this period as well as during it.",
      ], ans=0,
      why=("KC-3.3.I.B supplies the demand side and KC-3.1.I.C.i the supply side, naming "
           "innovations in previously existing transportation and commercial technologies among "
           "the encouragements to interregional trade. An argument for more than one cause is "
           "strengthened by evidence about the other cause.")),

 dict(q=("An unattributed traveller's notebook records that a merchant deposited a sum with a "
         "house in one city and drew the same sum from a correspondent of that house many weeks' "
         "journey away, carrying no coin between. Which of the following describes the "
         "significance of an arrangement of this kind for long-distance trade?"),
      choices=[
        "It is a form of credit, and the framework names forms of credit among the innovations that encouraged the growth of interregional trade in luxury goods.",
        "It is a transportation technology, since the sum travelled the distance in the merchant's place.",
        "It shows that money economies had not yet developed in the region concerned.",
        "It shows that the merchant had abandoned trade in goods for trade in coin.",
        "It has no bearing on trade, being a private arrangement between two houses.",
      ], ans=0,
      why=("KC-3.1.I.C.i names forms of credit and the development of money economies among the "
           "innovations in previously existing commercial technologies that encouraged the growth "
           "of interregional trade in luxury goods. A sum payable at a distance is credit, not "
           "transport.")),

 dict(q=("Which of the following identifies why a shelter provided at intervals along an overland "
         "route counts as a technology of trade in the framework's sense?"),
      choices=[
        "Because it is an improvement to the conditions under which goods and animals move, and the framework groups such improvements with commercial ones as encouragements to interregional trade.",
        "Because it produced the goods that were carried along the route.",
        "Because it replaced the need for merchants to travel at all.",
        "Because it was a form of credit extended to travellers.",
        "Because it fixed the prices at which goods were sold along the route.",
      ], ans=0,
      why=("KC-3.1.I.C.i states that the growth of interregional trade in luxury goods was "
           "encouraged by innovations in previously existing TRANSPORTATION and commercial "
           "technologies, including the caravanserai, and the caravanserai is the CED's own "
           "illustrative instance of the transportation half.")),

 dict(q=("Two students disagree. One says the Silk Roads were created in this period; the other "
         "says they were extended in it. Which of the following resolves the disagreement as the "
         "framework states the matter?"),
      choices=[
        "The framework describes the geographical range of existing routes, the Silk Roads among them, as having been expanded, which is extension of something already in use.",
        "The framework describes the Silk Roads as first opened during this period.",
        "The framework describes the Silk Roads as having fallen out of use during this period.",
        "The framework describes the Silk Roads as unchanged in extent throughout the period.",
        "The framework makes no statement about the extent of any route in this period.",
      ], ans=0,
      why=("KC-3.1.I.A.i states that improved commercial practices expanded the geographical "
           "range of EXISTING trade routes, including the Silk Roads. The word existing settles "
           "the dispute, and the CED elsewhere states that developments may begin before the "
           "period.")),

 dict(q=("An unattributed register kept at a frontier post lists the goods passing outward and "
         "notes that most are light in weight and high in value. Which of the following best "
         "describes the context this detail belongs to?"),
      choices=[
        "The growth of interregional trade in luxury goods, which the framework treats as the kind of trade the period's commercial and transport innovations encouraged.",
        "The growth of trade in bulk foodstuffs, which the framework treats as the characteristic overland traffic of the period.",
        "The decline of interregional trade, since only small quantities were moving.",
        "The confinement of trade to goods produced at the frontier itself.",
        "The replacement of trade in goods by the movement of coin alone.",
      ], ans=0,
      why=("KC-3.1.I.C.i speaks specifically of the growth of interregional trade in LUXURY "
           "GOODS being encouraged by innovations in previously existing transportation and "
           "commercial technologies, and KC-3.3.I.B says demand for luxury goods increased in "
           "Afro-Eurasia. The framework's subject here is the luxury trade.")),

 dict(q=("Which of the following would be the best evidence that a city owed its growth to its "
         "position on a trade route rather than to its own hinterland?"),
      choices=[
        "That the goods handled in its markets were produced far away in both directions and were not consumed in the surrounding country.",
        "That its population rose across the period covered by the records.",
        "That its market was held on fixed days each week.",
        "That it lay within the territory of a state that also held other cities.",
        "That its inhabitants used coined money in daily transactions.",
      ], ans=0,
      why=("KC-3.1.I.A.i states that improved commercial practices increased the volume of trade "
           "and expanded the range of existing routes, PROMOTING THE GROWTH OF POWERFUL NEW "
           "TRADING CITIES. Goods that neither originate nor stop in the district are what "
           "distinguishes a city of passage from a market for its own region.")),

 dict(q=("A student's essay says that the increase in demand for luxury goods in this period was "
         "felt only by those who bought them. Which of the following identifies the strongest "
         "objection?"),
      choices=[
        "The framework attaches to that demand an expansion of production by artisans and merchants in several regions, so the effect reached the places where the goods were made as well.",
        "The framework denies that demand for luxury goods increased in this period.",
        "The framework states that luxury goods were consumed only in the regions that produced them.",
        "The framework states that production in this period was fixed and could not expand.",
        "The framework treats demand and production as unrelated to each other.",
      ], ans=0,
      why=("KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia and that "
           "Chinese, Persian, and Indian artisans and merchants expanded their production of "
           "textiles and porcelains for export, and the Economics thematic focus says societies "
           "affect and are affected by the ways they produce, exchange, and consume goods.")),

 dict(q=("Which of the following pairs a development with the context that best explains it, "
         "rather than with a restatement of it?"),
      choices=[
        "The appearance of powerful new trading cities, set against a rise in the volume of trade and an extension of the routes on which they stood.",
        "The appearance of powerful new trading cities, set against the fact that some cities in the period were powerful and traded.",
        "A rise in the volume of trade, set against the fact that more goods were carried than before.",
        "The use of written instruments in settlement, set against the fact that merchants settled accounts in writing.",
        "An increase in demand for luxury goods, set against the fact that luxury goods were wanted.",
      ], ans=0,
      why=("Suggested skill 4.A asks a student to identify and describe a historical CONTEXT for "
           "a development, which is the circumstance in which it occurred and not the development "
           "restated. KC-3.1.I.A.i supplies exactly such a context for the growth of trading "
           "cities: increased volume and expanded range on existing routes.")),

 dict(q=("An unattributed contract of the period records that two merchants shared the cost of a "
         "consignment and agreed in advance how any loss on the journey should fall between them. "
         "Which of the following identifies what such an arrangement contributed?"),
      choices=[
        "An improvement in commercial practice, which the framework treats as a cause of increased volume of trade and of the extension of existing routes.",
        "An improvement in transportation technology, since the goods travelled more safely as a result.",
        "A reduction in the volume of trade, since two merchants now did the work of one.",
        "A withdrawal from long-distance trade, since risk was being avoided rather than taken.",
        "A change in what was produced rather than in how it was exchanged.",
      ], ans=0,
      why=("KC-3.1.I.A.i states that IMPROVED COMMERCIAL PRACTICES led to an increased volume of "
           "trade and expanded the geographical range of existing trade routes. An agreement "
           "distributing risk is a commercial practice, not a transport technology.")),

 dict(q=("Which of the following claims about this period does the framework NOT support?"),
      choices=[
        "That the volume of overland trade grew because rulers compelled merchants to travel.",
        "That the volume of trade on existing routes increased.",
        "That the geographical range of existing routes expanded.",
        "That powerful new trading cities grew.",
        "That interregional trade in luxury goods was encouraged by innovations in technologies already in use.",
      ], ans=0,
      why=("KC-3.1.I.A.i and KC-3.1.I.C.i between them assert increased volume, expanded range, "
           "the growth of powerful new trading cities and the encouragement given by innovations "
           "in previously existing technologies. Compulsion by rulers appears in neither sentence "
           "and is the one claim with nothing behind it.")),

 dict(q=("A student wishes to argue that exchange in this period changed the societies at both "
         "ends of a route and not only the merchants who travelled it. Which of the following "
         "best supports that argument?"),
      choices=[
        "The framework's statement that societies affect and are affected by the ways they produce, exchange and consume, taken with its account of producers expanding output for distant markets.",
        "The framework's statement that the routes concerned already existed before the period.",
        "The framework's statement that trading cities grew along the routes.",
        "The framework's statement that credit and coin were both in use.",
        "The framework's statement that its own dates are approximate.",
      ], ans=0,
      why=("The Economics thematic focus states that as societies develop, they affect and are "
           "affected by the ways that they produce, exchange, and consume goods and services, and "
           "KC-3.3.I.B records artisans and merchants in three regions expanding production for "
           "export. Together they carry the argument to the producing societies.")),

 dict(q=("Which of the following identifies the difference between the two kinds of innovation "
         "the framework groups together as encouragements to interregional trade?"),
      choices=[
        "One concerns how goods and people are moved and the other how payment and obligation are arranged, and the framework names both as previously existing technologies that were improved.",
        "One concerns how payment is arranged and the other how goods are moved, so the framework's two categories have been stated in the wrong order here.",
        "One belongs to the overland routes and the other to the maritime ones, so the two never operate together.",
        "One is available to merchants and the other only to rulers, so the two serve different people.",
        "The two are the same category described twice, so no difference is being drawn.",
      ], ans=0,
      why=("KC-3.1.I.C.i names innovations in previously existing TRANSPORTATION AND COMMERCIAL "
           "technologies and then gives an instance of each, the caravanserai on one side and "
           "forms of credit and money economies on the other. The anchor carries both halves in "
           "order because the strongest distractor exchanges them.")),

 dict(q=("An unattributed inventory from a workshop lists bolts of woven cloth and fired vessels "
         "packed for carriage to markets many weeks away, in quantities far beyond what the "
         "district could absorb. Which of the following describes the context to which this "
         "belongs?"),
      choices=[
        "Rising demand for luxury goods across Afro-Eurasia, to which artisans and merchants in several producing regions responded by expanding output for export.",
        "A collapse of demand for luxury goods, which left workshops with goods they could not sell.",
        "A prohibition on the export of manufactured goods, which confined production to local use.",
        "A shift from manufacture to agriculture in the districts where such workshops stood.",
        "The confinement of textile and ceramic production to a single region of Afro-Eurasia.",
      ], ans=0,
      why=("KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia and that "
           "Chinese, Persian, and Indian artisans and merchants expanded their production of "
           "textiles and porcelains for export. Output far exceeding local consumption is "
           "production for export in exactly that sense.")),

 dict(q=("Which of the following identifies what makes a trading city powerful in the framework's "
         "account rather than merely populous?"),
      choices=[
        "That it grew with the traffic of an extended route and the increased volume that route carried, so its standing rested on the exchange passing through it.",
        "That its inhabitants outnumbered those of the cities around it.",
        "That it stood within the territory of a large state.",
        "That its buildings were more numerous than those of neighbouring towns.",
        "That it lay at a greater distance from its neighbours than they lay from one another.",
      ], ans=0,
      why=("KC-3.1.I.A.i states that improved commercial practices increased the volume of trade "
           "and expanded the geographical range of existing routes, promoting the growth of "
           "POWERFUL NEW TRADING CITIES. The framework ties the standing of such a city to the "
           "trade rather than to its size alone.")),

 dict(q=("A student asks why the framework treats the growth of exchange after 1200 as having "
         "causes at all, rather than as something that simply happened. Which of the following is "
         "the best answer from this topic?"),
      choices=[
        "Because the learning objective for the topic asks for the causes and effects of the growth of networks of exchange, and the key concepts name improved practices, innovations in existing technologies and rising demand as those causes.",
        "Because the framework holds that every historical development must have exactly one cause.",
        "Because the framework treats trade as the cause of every other development in the period.",
        "Because the framework denies that exchange grew at all after 1200.",
        "Because the framework treats causes as matters of opinion on which no evidence bears.",
      ], ans=0,
      why=("Learning Objective A of this unit asks students to explain the causes and effects of "
           "the growth of networks of exchange after 1200, and KC-3.1.I.A.i, KC-3.1.I.C.i and "
           "KC-3.3.I.B each supply a cause: improved commercial practices, innovations in "
           "previously existing technologies, and increased demand.")),

 dict(q=("Which of the following would count as an EFFECT of the growth of exchange rather than a "
         "cause of it, as this topic's key concepts are arranged?"),
      choices=[
        "The growth of powerful new trading cities along the routes concerned.",
        "The improvement of commercial practices used by merchants.",
        "The innovations made in transportation technologies already in use.",
        "The development of money economies in the regions the routes crossed.",
        "The increase in demand for luxury goods across Afro-Eurasia.",
      ], ans=0,
      why=("KC-3.1.I.A.i puts the growth of powerful new trading cities on the far side of the "
           "sentence from improved commercial practices, which lead to increased volume and "
           "expanded range and thereby PROMOTE that growth. Learning Objective A asks for causes "
           "and effects, and the other four options are named among the causes.")),

 dict(q=("An unattributed letter of the period complains that a debt owed at one market cannot be "
         "collected at another because the two use different weights and different coin. Which of "
         "the following identifies what the complaint shows about commercial practice?"),
      choices=[
        "That the practices making payment transferable between places were an improvement whose absence was felt, which is why the framework treats their spread as a cause of growing trade.",
        "That trade between the two markets was impossible in this period.",
        "That coin was not in use in either of the two markets.",
        "That the merchant concerned had no interest in trade beyond his own city.",
        "That differences of weight and coin were a benefit to long-distance trade.",
      ], ans=0,
      why=("KC-3.1.I.A.i names improved commercial practices as a cause of increased volume of "
           "trade, and KC-3.1.I.C.i names forms of credit and the development of money economies "
           "among the innovations encouraging interregional trade. A complaint about their "
           "absence is evidence of what their presence did.")),

 dict(q=("Which of the following identifies a limit on what this topic's key concepts allow a "
         "student to claim?"),
      choices=[
        "They assert that demand for luxury goods increased in Afro-Eurasia without stating how far it increased or in what proportion between regions.",
        "They assert nothing about demand for luxury goods anywhere.",
        "They assert that demand increased in one named region only.",
        "They assert that the increase in demand was matched exactly by an increase in supply.",
        "They assert that demand for luxury goods fell across the period.",
      ], ans=0,
      why=("KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia and names "
           "Chinese, Persian, and Indian artisans and merchants as expanding production for "
           "export. It gives no magnitude and no comparison between regions, so a claim about how "
           "much would go beyond the sentence.")),

 dict(q=("Two accounts of the same route survive: one kept by a merchant who used it and one by a "
         "ruler's officer who taxed its traffic. Which of the following identifies the soundest "
         "way to use them together?"),
      choices=[
        "As records made for different purposes, so that what each was written to accomplish is part of what the historian must weigh in reading it.",
        "As records of equal value, so that where they disagree the disagreement may be ignored.",
        "As records of which only the official one may be used, since it was made by authority.",
        "As records of which only the merchant's may be used, since he saw the traffic himself.",
        "As records that cannot be used together, since two sources on one subject always conflict.",
      ], ans=0,
      why=("Learning Objective A asks students to explain the causes and effects of the growth of "
           "networks of exchange after 1200, and KC-3.1.I.A.i is a claim about volume and range "
           "that both a merchant's book and a toll register bear on. Weighing purpose is how two "
           "such records are used together rather than ranked.")),

 dict(q=("Which of the following claims about the caravanserai is supported by the framework as it "
         "stands?"),
      choices=[
        "It is offered as an instance of the transportation technologies whose improvement encouraged the growth of interregional trade in luxury goods.",
        "It is the only technology the framework treats as bearing on interregional trade.",
        "It is described by the framework as an invention of this period without earlier precedent.",
        "It is described by the framework as a commercial rather than a transportation technology.",
        "It is described by the framework as having discouraged long-distance trade.",
      ], ans=0,
      why=("KC-3.1.I.C.i names the caravanserai, forms of credit, and the development of money "
           "economies together as innovations in previously existing transportation and "
           "commercial technologies that encouraged the growth of interregional trade in luxury "
           "goods. It is one instance among several, and the sentence's word previously rules out "
           "novelty.")),

 dict(q=("A student claims that because the routes of this period already existed, nothing about "
         "trade on them changed. Which of the following identifies the error?"),
      choices=[
        "The framework says the volume carried on existing routes increased and their geographical range expanded, so continuity of the route is consistent with change in the trade.",
        "The framework says the routes did not exist before this period, so the student's premise is false.",
        "The framework says the volume carried on existing routes fell, so the student has the direction wrong.",
        "The framework says the routes were abandoned in this period, so nothing was carried on them.",
        "The framework says nothing about the volume or range of trade in this period.",
      ], ans=0,
      why=("KC-3.1.I.A.i states that improved commercial practices led to an increased volume of "
           "trade and expanded the geographical range of EXISTING trade routes, including the "
           "Silk Roads. The sentence asserts an old route and a changed trade in the same breath.")),

 dict(q=("Which of the following statements about the Silk Roads in this period is supported by "
         "all three of this topic's key concepts taken together?"),
      choices=[
        "Trade on routes already in use grew in volume and extent, was encouraged by improvements to technologies of carriage and of payment, and was driven by a demand for luxury goods that producers in several regions worked to meet.",
        "Trade on newly opened routes grew, was carried on without credit or coin, and was met by producers in one region only.",
        "Trade on routes already in use declined, technologies of carriage fell out of use, and demand for luxury goods contracted.",
        "Trade on routes already in use grew, but no city along them gained by it and no producer altered output.",
        "Trade in this period cannot be described, since the framework makes no assertion about it.",
      ], ans=0,
      why=("KC-3.1.I.A.i supplies the increased volume and expanded range of existing routes, "
           "KC-3.1.I.C.i the innovations in previously existing transportation and commercial "
           "technologies, and KC-3.3.I.B the increase in demand met by artisans and merchants in "
           "China, Persia and India. The key states all three; each rejected option contradicts "
           "at least one.")),
]
