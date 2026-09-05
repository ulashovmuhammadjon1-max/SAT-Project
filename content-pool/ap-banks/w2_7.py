# AP WORLD HISTORY: MODERN 2.7 Comparison of Economic Exchange  (title copied verbatim
# from WORLD_HISTORY_topics.json). Unit 2 Networks of Exchange, c. 1200 to c. 1450.
# Suggested skill 6.B, support an argument using specific and relevant evidence.
#
# THIS IS THE UNIT'S REASONING TOPIC, so it is written as a reasoning set and not as
# fact recall. The CED says of every unit's final topic that it "focuses on the skill
# of argumentation and so provides an opportunity for your students to draw upon the
# key concepts and historical developments they have studied in this unit", and that
# the final topic page "includes key concepts, which summarize the historical
# developments in the unit".
#
# THE SUGGESTED SKILL IS PRINTED WITH TWO SUB-BULLETS, AND THEY ARE DIFFERENT THINGS:
#
#   6.B  Support an argument using specific and relevant evidence.
#        - Describe specific examples of historically relevant evidence.
#        - Explain how specific examples of historically relevant evidence support
#          an argument.
#
# Naming a piece of evidence and showing what it does for a claim are separate
# operations, and about a third of the items below turn on the difference. That is
# also what keeps this module off topic 3.4's ground: 3.4 shares skill 6.B but asks
# chiefly WHICH evidence is relevant, while this module asks HOW a given piece bears on
# a stated argument.
#
# THE REVIEW KEY CONCEPTS PRINTED ON THIS TOPIC PAGE, in the framework's own words:
#
#   LO 2.L  Explain the similarities and differences among the various networks of
#           exchange in the period from c. 1200 to c. 1450.
#   KC-3.1  A deepening and widening of networks of human interaction within and across
#           regions contributed to cultural, technological, and biological diffusion
#           within and between various societies.
#   KC-3.1.I.A.i  Improved commercial practices led to an increased volume of trade and
#           expanded the geographical range of existing trade routes -- including the
#           Silk Roads -- promoting the growth of powerful new trading cities.
#   KC-3.1.I.C.i  The growth of interregional trade in luxury goods was encouraged by
#           innovations in previously existing transportation and commercial
#           technologies, including the caravanserai, forms of credit, and the
#           development of money economies.
#   KC-3.3  Changes in trade networks RESULTED FROM AND STIMULATED increasing productive
#           capacity, with important implications for social and gender structures and
#           environmental processes.
#   KC-3.3.I.B  Demand for luxury goods increased in Afro-Eurasia. Chinese, Persian, and
#           Indian artisans and merchants expanded their production of textiles and
#           porcelains for export; manufacture of iron and steel expanded in China.
#
# THE CLAUSE THIS MODULE LEANS ON HARDEST. KC-3.3 says changes in trade networks
# RESULTED FROM AND STIMULATED increasing productive capacity. It is a two-way relation
# stated in one phrase, and it is the only sentence in this unit that licenses an
# argument running in either direction. Several items are built on it, and the anchors
# for those items carry both halves, because a distractor keeping one half is the
# obvious wrong answer to write.
#
# ON THE SOURCES. This bank cannot show an image. Every stimulus is a table of
# HYPOTHETICAL figures whose keyed conclusion is recoverable from the table alone, or
# an explicitly unattributed illustrative source, or a draft of a student's own
# argument. No quotation is attributed to a real person or document.
#
# ON DATES. Spans are written "c. 1200 to c. 1450". The CED states that events,
# processes, and developments are not constrained by the given dates and may begin
# before, or continue after, the period, so no key turns on a boundary year.
TOPIC = ("2.7", "Comparison of Economic Exchange", 2)

_T_CARGOES = dict(
    headers=["Network (hypothetical)", "Share of recorded cargoes that were luxury goods (percent)",
             "Share of recorded cargoes that were bulk goods (percent)"],
    rows=[["Network One", "70", "30"],
          ["Network Two", "55", "45"],
          ["Network Three", "82", "18"]])

_T_VOLUME = dict(
    headers=["Network (hypothetical)", "Volume index at an earlier date",
             "Volume index at a later date"],
    rows=[["Network One", "100", "260"],
          ["Network Two", "100", "145"],
          ["Network Three", "100", "190"]])

_T_CAPACITY = dict(
    headers=["Period (hypothetical)", "Index of goods produced for exchange",
             "Index of goods carried between regions"],
    rows=[["Earlier", "100", "100"],
          ["Middle", "150", "170"],
          ["Later", "210", "260"]])

QUESTIONS = [
 dict(q=("A student's argument reads: the networks of exchange in this period were alike in what "
         "encouraged them to grow. Which of the following pieces of evidence would support that "
         "argument most directly?"),
      choices=[
        "That the framework attributes the growth of interregional trade on more than one network to innovations in transportation and commercial technologies that were already in use.",
        "That merchants on each network kept written records of what they carried.",
        "That the networks concerned all existed during the same centuries.",
        "That each network passed through territory governed by some authority or other.",
        "That the goods carried on each network had to be moved from one place to another.",
      ], ans=0,
      why=("KC-3.1.I.C.i states that the growth of interregional trade in luxury goods was "
           "encouraged by innovations in previously existing transportation and commercial "
           "technologies, and Learning Objective L asks for the similarities and differences "
           "among the various networks of exchange. The rejected options are true of any trade "
           "anywhere and so distinguish nothing.")),

 dict(q=("Which of the following identifies the difference between the two things suggested skill "
         "6.B asks a student to do?"),
      choices=[
        "The first is to describe a specific example of relevant evidence, and the second is to explain how that example supports an argument, which is a further step and not the same one.",
        "The first is to explain how an example supports an argument, and the second is to describe a specific example, so the two have been stated in the wrong order.",
        "The two are the same operation named twice, so a student who does one has done both.",
        "The first concerns primary sources and the second concerns secondary ones.",
        "Neither can be done without first stating a value judgment about the evidence.",
      ], ans=0,
      why=("Suggested skill 6.B for this topic is printed with two sub-bullets: describe specific "
           "examples of historically relevant evidence, and explain how specific examples of "
           "historically relevant evidence support an argument. Learning Objective L supplies the "
           "arguments the two operations are performed on, about the similarities and differences "
           "among the various networks of exchange.")),

 dict(q=("The table below carries HYPOTHETICAL shares of recorded cargoes on three networks. A "
         "student wants to use it in an argument about similarity and difference between the "
         "networks. Which of the following does the data best support?"),
      table=_T_CARGOES,
      choices=[
        "Luxury goods are more than half of recorded cargoes on every network listed, which supports a claim of similarity, while the shares differ from one network to another, which supports a claim of difference.",
        "Bulk goods are more than half of recorded cargoes on every network listed.",
        "The three networks listed show the same shares as one another.",
        "On one of the networks listed, bulk goods form the larger share.",
        "Luxury goods form more than half of recorded cargoes on only one of the networks listed.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns, distractors included. Learning "
           "Objective L asks for the similarities AND differences among the various networks of "
           "exchange, and KC-3.1.I.C.i and KC-3.3.I.B both make the luxury trade the framework's "
           "own subject. One table can support both halves of the objective.")),

 dict(q=("An unattributed account describes credit extended at one end of a route and discharged "
         "at the other. A student cites it in support of the claim that commercial practice "
         "improved in this period. Which of the following best explains how the evidence supports "
         "the claim?"),
      choices=[
        "It is an instance of the kind of arrangement the framework names as an improvement, so it shows the general claim holding in a particular case.",
        "It proves the general claim, since a single instance establishes what happened everywhere.",
        "It has no bearing on the claim, since a particular case cannot support a general statement.",
        "It supports the claim only if the merchants named in the account can be identified.",
        "It supports the claim by showing that no other arrangement was available.",
      ], ans=0,
      why=("KC-3.1.I.C.i names forms of credit and the development of money economies among the "
           "innovations in previously existing commercial technologies, and suggested skill 6.B "
           "asks students to explain how a specific example supports an argument. An instance "
           "supports a general claim without establishing it.")),

 dict(q=("HYPOTHETICAL volume indexes for three networks at an earlier and a later date are set "
         "out in the table below. Which of the following does the data best support?"),
      table=_T_VOLUME,
      choices=[
        "All three networks carried more at the later date, which supports a claim of common direction, but by different multiples, which supports a claim of differing degree.",
        "All three networks carried more at the later date and by the same multiple.",
        "One of the networks listed carried less at the later date than at the earlier one.",
        "The network whose volume multiplied by the largest factor is the one that grew least.",
        "None of the networks listed more than doubled its volume.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.1 states that a deepening and "
           "widening of networks of human interaction contributed to diffusion within and between "
           "various societies, and Learning Objective L asks for similarities AND differences "
           "among those networks. The anchor carries both clauses because a distractor keeps the "
           "first and denies the second.")),

 dict(q=("Which of the following identifies what KC-3.3 asserts about the relation between trade "
         "networks and productive capacity?"),
      choices=[
        "That changes in trade networks resulted from increasing productive capacity and also stimulated it, so the relation runs in both directions.",
        "That changes in trade networks resulted from increasing productive capacity and had no effect upon it.",
        "That changes in trade networks stimulated increasing productive capacity and owed nothing to it.",
        "That changes in trade networks and productive capacity were unrelated to one another.",
        "That productive capacity was fixed throughout the period and could neither cause nor be caused.",
      ], ans=0,
      why=("KC-3.3 states that changes in trade networks RESULTED FROM AND STIMULATED increasing "
           "productive capacity, with important implications for social and gender structures and "
           "environmental processes. The anchor carries both directions because each of the two "
           "strongest distractors keeps one and drops the other.")),

 dict(q=("The table below carries HYPOTHETICAL indexes for three successive periods. Which of the "
         "following does the data best support?"),
      table=_T_CAPACITY,
      choices=[
        "Production for exchange and carriage between regions both rise at every step, which is consistent with the two moving together rather than one running ahead while the other stands still.",
        "Production for exchange rises while carriage between regions falls.",
        "Carriage between regions rises while production for exchange falls.",
        "Both indexes are unchanged across the three periods listed.",
        "At one of the steps listed, one index rises while the other stays level.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.3 states that changes in trade "
           "networks resulted from and stimulated increasing productive capacity, and two "
           "measures rising together is what a two-way relation looks like in figures. The keyed "
           "wording says consistent with rather than proves, because figures moving together do "
           "not by themselves settle which moved first.")),

 dict(q=("A student writes: the networks of exchange in this period were entirely different from "
         "one another. Which of the following would be the strongest piece of evidence against "
         "that argument?"),
      choices=[
        "That the framework describes the growth of trade on more than one of them in the same terms, naming increased volume and expanded range of routes already in use.",
        "That the networks concerned carried different goods from one another.",
        "That the networks concerned crossed different kinds of country.",
        "That the networks concerned were used by merchants of different regions.",
        "That the networks concerned are described in different sentences of the framework.",
      ], ans=0,
      why=("KC-3.1.I.A.i states that improved commercial practices led to an increased volume of "
           "trade and expanded the geographical range of existing trade routes, and the "
           "framework's parallel sentences say the same of other networks. Learning Objective L "
           "asks for similarities as well as differences.")),

 dict(q=("An unattributed inventory lists goods of high value and small bulk carried a very long "
         "way. A student uses it to support the claim that the trade of this period was chiefly a "
         "luxury trade. Which of the following best explains the limit of that support?"),
      choices=[
        "The inventory is one cargo, so it illustrates the claim without measuring how large a share of all cargoes such goods were.",
        "The inventory is worthless for the claim, since a list of goods says nothing about trade.",
        "The inventory settles the claim, since one cargo is representative of all cargoes.",
        "The inventory bears on the claim only if the merchant who compiled it is named.",
        "The inventory tells against the claim, since valuable goods are rarely traded.",
      ], ans=0,
      why=("Suggested skill 6.B asks students to explain HOW a specific example supports an "
           "argument, and KC-3.1.I.C.i and KC-3.3.I.B make the luxury trade a subject of the "
           "framework. A single cargo illustrates a claim about proportion without establishing "
           "the proportion.")),

 dict(q=("Which of the following identifies what makes a piece of evidence relevant to an "
         "argument, as distinct from merely true?"),
      choices=[
        "That it bears on the particular claim being made, so that accepting it gives a reader a reason to accept or doubt that claim rather than some other.",
        "That it comes from a source written during the period under discussion.",
        "That it can be shown to be accurate by comparison with a second source.",
        "That it concerns the same region as the argument, whatever the argument asserts about it.",
        "That it is drawn from a document rather than from a modern historian.",
      ], ans=0,
      why=("Suggested skill 6.B asks students to support an argument using specific and RELEVANT "
           "evidence, and Learning Objective L supplies the arguments in this unit, about "
           "similarities and differences among the various networks of exchange. Accuracy and "
           "date are separate virtues from bearing.")),

 dict(q=("A student argues that the growth of exchange in this period had effects reaching beyond "
         "commerce. Which of the following would support that argument most directly?"),
      choices=[
        "That the framework attaches to changes in trade networks important implications for social and gender structures and for environmental processes.",
        "That the framework describes the volume of trade as having increased.",
        "That the framework describes the range of existing routes as having expanded.",
        "That the framework describes powerful new trading cities as having grown.",
        "That the framework describes credit and coin as both having been in use.",
      ], ans=0,
      why=("KC-3.3 states that changes in trade networks resulted from and stimulated increasing "
           "productive capacity, WITH IMPORTANT IMPLICATIONS FOR SOCIAL AND GENDER STRUCTURES AND "
           "ENVIRONMENTAL PROCESSES. The four rejected options are commercial facts and do not "
           "reach past commerce.")),

 dict(q=("An unattributed workshop record shows output rising in a district after its goods began "
         "to be carried to distant markets. A student cites it to support the claim that exchange "
         "stimulated production. Which of the following best explains how it supports the claim, "
         "and what it leaves open?"),
      choices=[
        "It shows production rising after the market widened, which fits the claim, but it does not by itself rule out that the district's output had been rising already for reasons of its own.",
        "It settles the claim completely, since a rise after an event proves the event caused it.",
        "It tells against the claim, since production and exchange cannot rise together.",
        "It has no bearing on the claim, since a single district cannot illustrate a general process.",
        "It supports the claim only if the district's rulers are shown to have ordered the increase.",
      ], ans=0,
      why=("KC-3.3 states that changes in trade networks resulted from AND STIMULATED increasing "
           "productive capacity, so the framework itself allows influence in both directions, and "
           "suggested skill 6.B asks students to explain how an example supports an argument. "
           "Saying what a piece of evidence leaves open is part of that explanation.")),

 dict(q=("Which of the following identifies a similarity among the networks of exchange that the "
         "framework itself supports?"),
      choices=[
        "That a deepening and widening of networks of human interaction contributed to cultural, technological, and biological diffusion within and between various societies.",
        "That every network carried the same goods in the same proportions.",
        "That every network was governed by a single authority along its whole length.",
        "That every network was opened for the first time during this period.",
        "That every network drew its merchants from a single region.",
      ], ans=0,
      why=("KC-3.1 states that a deepening and widening of networks of human interaction within "
           "and across regions contributed to cultural, technological, and biological diffusion "
           "within and between various societies. That is asserted of the networks generally; "
           "none of the four uniformities is asserted anywhere.")),

 dict(q=("A student's draft cites the growth of a trading city as evidence that commercial "
         "practice improved. Which of the following best explains the step the draft is missing?"),
      choices=[
        "It must say why the city's growth would be expected if practice improved, since the framework treats such growth as promoted by increased volume and expanded range rather than as the improvement itself.",
        "It must name the city, since evidence without a name cannot be used.",
        "It must show that the city was the largest in its region, since only the largest case counts.",
        "It must find a second city, since one instance can never be cited.",
        "It must abandon the claim, since city growth has no relation to commercial practice.",
      ], ans=0,
      why=("KC-3.1.I.A.i states that improved commercial practices led to an increased volume of "
           "trade and expanded the geographical range of existing trade routes, PROMOTING the "
           "growth of powerful new trading cities, and suggested skill 6.B asks students to "
           "EXPLAIN HOW an example supports an argument rather than only to name it.")),

 dict(q=("Which of the following claims about the networks of exchange in this period goes beyond "
         "what the unit's key concepts assert?"),
      choices=[
        "That one of the networks carried a greater volume of goods than the others did.",
        "That the volume of trade on existing routes increased.",
        "That the geographical range of existing routes expanded.",
        "That demand for luxury goods increased in Afro-Eurasia.",
        "That innovations in previously existing technologies encouraged the growth of interregional trade.",
      ], ans=0,
      why=("KC-3.1.I.A.i, KC-3.1.I.C.i and KC-3.3.I.B assert increased volume, expanded range, "
           "rising demand and the encouragement given by innovations, but they never compare the "
           "volumes of one network with another. A claim of greater volume adds a comparison of "
           "magnitude the framework does not make.")),

 dict(q=("A student writes that because demand for luxury goods rose, production must have risen "
         "in every region of Afro-Eurasia. Which of the following identifies the overreach?"),
      choices=[
        "The framework names artisans and merchants in three regions as having expanded production for export and says nothing about the rest, so a claim about every region goes past the sentence.",
        "The framework denies that demand for luxury goods rose in this period.",
        "The framework names only one region as having expanded production.",
        "The framework states that production fell as demand rose.",
        "The framework states that demand and production are unconnected.",
      ], ans=0,
      why=("KC-3.3.I.B states that demand for luxury goods increased in Afro-Eurasia and that "
           "Chinese, Persian, and Indian artisans and merchants expanded their production of "
           "textiles and porcelains for export. Three sets of producers are named, and a claim "
           "about every region is broader than the sentence supports.")),

 dict(q=("An unattributed customs record from one port is offered as evidence for a claim about "
         "the trade of a whole ocean. Which of the following best explains what the evidence can "
         "and cannot do for the claim?"),
      choices=[
        "It can show that the pattern the claim describes held at one point on the network, which supports the claim, while establishing the claim for the network as a whole would need evidence from more than one point.",
        "It can establish the claim for the network as a whole, since a port is part of the network.",
        "It can do nothing for the claim, since a record from one port is about that port alone.",
        "It can support the claim only if the port was the busiest on the network.",
        "It can support the claim only if a second record from the same port is found.",
      ], ans=0,
      why=("Suggested skill 6.B asks students to describe specific examples of historically "
           "relevant evidence AND to explain how they support an argument, and Learning Objective "
           "L frames the arguments as claims about the various networks. A point on a network "
           "supports a claim about the network without settling it.")),

 dict(q=("Which of the following pairs an argument with evidence that bears on it rather than "
         "with evidence that merely accompanies it?"),
      choices=[
        "The argument that innovations in existing technologies encouraged trade, paired with a record of an arrangement for shelter and for payment at a distance coming into general use along a route.",
        "The argument that innovations in existing technologies encouraged trade, paired with a record of the weather in the years concerned.",
        "The argument that the volume of trade rose, paired with a record of the names of the merchants involved.",
        "The argument that demand for luxury goods rose, paired with a record of the languages spoken along a route.",
        "The argument that new trading cities grew, paired with a record of the founding date of an older city.",
      ], ans=0,
      why=("KC-3.1.I.C.i names the caravanserai, forms of credit, and the development of money "
           "economies as innovations in previously existing transportation and commercial "
           "technologies that encouraged the growth of interregional trade, and suggested skill "
           "6.B asks for SPECIFIC AND RELEVANT evidence. The rejected pairings attach true facts "
           "that give no reason to accept or doubt the claim.")),

 dict(q=("A student argues that the networks of this period should be studied together rather "
         "than separately. Which of the following supports that argument most directly?"),
      choices=[
        "That the framework describes a deepening and widening of networks of human interaction within AND ACROSS regions, so its own unit of analysis is larger than any single route.",
        "That the routes concerned were all in use during the same centuries.",
        "That merchants on each route carried goods for profit.",
        "That each route ran between two or more regions.",
        "That the framework devotes a separate sentence to each route.",
      ], ans=0,
      why=("KC-3.1 states that a deepening and widening of networks of human interaction WITHIN "
           "AND ACROSS REGIONS contributed to cultural, technological, and biological diffusion "
           "within and between various societies, and Learning Objective L asks for a comparison "
           "AMONG the various networks.")),

 dict(q=("Which of the following identifies why a comparison needs a stated respect in which the "
         "cases are compared?"),
      choices=[
        "Because two networks may be alike in what encouraged them to grow and unlike in what they carried, so a bare claim that they were similar leaves a reader unable to tell what is being asserted.",
        "Because the framework forbids any comparison between two networks.",
        "Because two networks can only be compared if they carried identical goods.",
        "Because a comparison is a value judgment and so needs no evidence.",
        "Because the framework treats all the networks of the period as identical.",
      ], ans=0,
      why=("Learning Objective L asks students to explain the similarities and differences among "
           "the various networks of exchange, and KC-3.1.I.C.i and KC-3.3.I.B describe an "
           "encouragement and a demand that several networks shared while the framework nowhere "
           "asserts that their cargoes matched.")),

 dict(q=("An unattributed account describes women in a producing district taking up weaving for "
         "sale where they had formerly woven only for the household. A student cites it in an "
         "argument about the effects of exchange. Which of the following best explains its "
         "bearing?"),
      choices=[
        "It bears on the framework's claim that changes in trade networks carried important implications for social and gender structures, since it shows who did what work changing as production for market grew.",
        "It bears only on the volume of cloth produced and has no social dimension.",
        "It bears on nothing in the framework, which makes no claim about who did particular work.",
        "It bears on the claim only if the number of women concerned can be counted exactly.",
        "It bears against the framework, which holds that social structures were fixed in this period.",
      ], ans=0,
      why=("KC-3.3 states that changes in trade networks resulted from and stimulated increasing "
           "productive capacity, WITH IMPORTANT IMPLICATIONS FOR SOCIAL AND GENDER STRUCTURES and "
           "environmental processes, and KC-3.3.I.B records artisans and merchants expanding "
           "production of textiles for export.")),

 dict(q=("Which of the following would most weaken an argument that the growth of exchange in "
         "this period was driven entirely by rising demand?"),
      choices=[
        "Evidence that the means of carriage and of payment improved before the rise in demand became general, so that demand alone would have had less to work with.",
        "Evidence that demand for luxury goods rose across Afro-Eurasia.",
        "Evidence that producers in several regions expanded their output.",
        "Evidence that the goods concerned were valuable in proportion to their weight.",
        "Evidence that the routes concerned had been in use before the period.",
      ], ans=0,
      why=("KC-3.3.I.B supplies the demand and KC-3.1.I.C.i the innovations in previously existing "
           "transportation and commercial technologies, which the framework names as a separate "
           "encouragement. Suggested skill 6.B asks how evidence bears on an argument, and "
           "evidence for a second cause is what tells against a single-cause account.")),

 dict(q=("Two students cite the same table of cargo shares. One uses it to argue that the "
         "networks were alike; the other to argue that they differed. Which of the following best "
         "explains how one table can serve both?"),
      choices=[
        "Because the same figures can show a feature common to every case and a variation in its size, and the objective for this topic asks for similarities and differences together.",
        "Because a table can be read to mean whatever a student wishes it to mean.",
        "Because one of the two students must have misread the figures.",
        "Because the table is evidence for neither claim, being merely a list of numbers.",
        "Because similarity and difference are the same claim under two names.",
      ], ans=0,
      why=("Learning Objective L asks students to explain the similarities AND differences among "
           "the various networks of exchange in the period from c. 1200 to c. 1450, and suggested "
           "skill 6.B asks how a specific example supports an argument. A shared feature and a "
           "varying magnitude are two readings of one set of figures.")),

 dict(q=("Which of the following identifies what the framework means by a DEEPENING as well as a "
         "widening of networks of human interaction?"),
      choices=[
        "That the interaction became more intense within the regions already connected as well as reaching across to further ones, so the change is not only a matter of extent.",
        "That the interaction reached further regions while becoming less intense within those already connected.",
        "That the interaction became more intense while reaching no further than before.",
        "That the two words are alternatives, only one of which the framework asserts.",
        "That the framework uses both words to describe a fall in the level of interaction.",
      ], ans=0,
      why=("KC-3.1 states that a DEEPENING AND WIDENING of networks of human interaction within "
           "and across regions contributed to cultural, technological, and biological diffusion "
           "within and between various societies. Two changes are named, and the anchor carries "
           "both because a distractor keeps one and denies the other.")),

 dict(q=("An unattributed register from a region records both a new crop under cultivation and a "
         "new technique in a workshop within the same decade. A student cites it in support of an "
         "argument about the reach of exchange. Which of the following best explains how it "
         "supports the argument?"),
      choices=[
        "It shows two different kinds of thing arriving in one place, which is what the framework describes when it names cultural, technological and biological diffusion together.",
        "It shows one kind of thing arriving, since a crop and a technique are the same category.",
        "It bears on the argument only if the region can be shown to lie on a named route.",
        "It tells against the argument, since a region that receives anything must have produced nothing itself.",
        "It has no bearing on exchange, since cultivation and workshops are internal matters.",
      ], ans=0,
      why=("KC-3.1 states that a deepening and widening of networks of human interaction "
           "contributed to CULTURAL, TECHNOLOGICAL, AND BIOLOGICAL diffusion within and between "
           "various societies. A crop and a technique are two of the three kinds that one "
           "sentence names.")),

 dict(q=("Which of the following identifies what a student should do with evidence that tells "
         "against the argument being made?"),
      choices=[
        "State it and explain why the argument survives it, since an argument that has met the strongest evidence against it is better supported than one that has not.",
        "Omit it, since evidence against an argument weakens the argument by being mentioned.",
        "Abandon the argument, since any evidence against a claim refutes it.",
        "Reclassify it as irrelevant, since only supporting evidence is relevant.",
        "Cite it without comment, since a reader will draw the necessary conclusion.",
      ], ans=0,
      why=("Suggested skill 6.B asks students to support an argument using specific and relevant "
           "evidence and to explain how examples support it, and Learning Objective L's demand "
           "for similarities AND differences means the evidence in this unit rarely points one "
           "way only.")),

 dict(q=("A student's draft asserts that trade in this period changed the environment. Which of "
         "the following would make that assertion an argument the unit's key concepts can "
         "support?"),
      choices=[
        "Naming the environmental processes the framework attaches to changes in trade networks and giving an instance of one, then explaining how the instance bears on the general claim.",
        "Asserting it more strongly, so that a reader is left in no doubt.",
        "Listing every region of Afro-Eurasia by name.",
        "Confining the claim to a single village, so that it may be checked.",
        "Replacing it with a claim about commerce, since environmental claims cannot be argued.",
      ], ans=0,
      why=("KC-3.3 states that changes in trade networks resulted from and stimulated increasing "
           "productive capacity, with important implications for social and gender structures and "
           "ENVIRONMENTAL PROCESSES, and suggested skill 6.B asks students to describe specific "
           "examples of relevant evidence and explain how they support an argument.")),

 dict(q=("Which of the following identifies the difference between an argument and a summary of "
         "what the framework says?"),
      choices=[
        "An argument makes a claim that a reader could dispute and offers evidence for it, while a summary reports assertions without taking a position that evidence must defend.",
        "A summary makes a disputable claim and an argument reports assertions, so the two have been described the wrong way round.",
        "The two are the same, since any statement about the past is an argument.",
        "An argument may use evidence and a summary may not, which is the only difference between them.",
        "A summary concerns the framework and an argument concerns sources, so the two never overlap.",
      ], ans=0,
      why=("Suggested skill 6.B asks students to SUPPORT AN ARGUMENT using specific and relevant "
           "evidence, and Learning Objective L supplies the claims to be argued, about "
           "similarities and differences among the various networks. The anchor carries both "
           "halves in order because the strongest distractor exchanges them.")),

 dict(q=("An unattributed account of one route is the only surviving evidence a student has for a "
         "claim about the whole period. Which of the following best explains how the claim should "
         "be stated?"),
      choices=[
        "In terms the evidence can bear, saying what the account shows about that route and what it suggests about the period, rather than asserting of the period what only one route's record supports.",
        "In the strongest terms available, since a claim is judged by its ambition.",
        "Not at all, since a claim about a period may never be made from one source.",
        "As a claim about the source rather than about the past, since a single source can only describe itself.",
        "As a claim about every route, since routes of the same period must have been alike.",
      ], ans=0,
      why=("Suggested skill 6.B asks students to support an argument using specific and relevant "
           "evidence, and Learning Objective L asks for claims about the VARIOUS networks. Fitting "
           "a claim to what the evidence can carry is what supporting it with that evidence "
           "means.")),

 dict(q=("Taken together, which of the following is the best supported comparative claim a "
         "student could make about the networks of exchange from c. 1200 to c. 1450?"),
      choices=[
        "They were alike in growing through improvements to arrangements already in use and in carrying more than goods between societies, and unlike in the particular routes, technologies and cargoes through which each did so.",
        "They were alike in every particular, so that a description of one describes all of them.",
        "They were unlike in every particular, so that no general statement about them is possible.",
        "They were alike in the goods they carried and unlike in whether they grew at all.",
        "Nothing comparative can be said about them, since the framework describes each separately.",
      ], ans=0,
      why=("KC-3.1 supplies the deepening and widening of networks contributing to cultural, "
           "technological, and biological diffusion, KC-3.1.I.A.i and KC-3.1.I.C.i the improved "
           "practices and the innovations in previously existing technologies, and KC-3.3.I.B the "
           "demand met by producers in several regions. Learning Objective L asks for the "
           "similarities AND differences, which is what the key names and each rejected option "
           "drops.")),
]
