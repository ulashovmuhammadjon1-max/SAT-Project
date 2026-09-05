# AP WORLD HISTORY: MODERN 4.4 Maritime Empires Established
# CED effective Fall 2024/2026, Unit 4 Transoceanic Interconnections, c. 1450 to
# c. 1750. Title copied verbatim from WORLD_HISTORY_topics.json.
#
# Unit 4: Learning Objective E -- explain the process of state building and
# expansion among various empires and states in the period from 1450 to 1750.
# Unit 4: Learning Objective F -- explain the continuities and changes in
# economic systems and labor systems from 1450 to 1750.
# Unit 4: Learning Objective G -- explain changes and continuities in systems of
# slavery in the period from 1450 to 1750.
# Suggested skill 2.A, identify a source's point of view, purpose, historical
# situation, and/or audience. Reasoning process: continuity and change.
# Thematic focuses: Governance, Economic Systems, and Social Interactions and
# Organization.
#
# Historical developments this module keys to, in the framework's own words:
#   KC-4.3.II.A.i    Europeans established new trading posts in Africa and Asia,
#                    which proved profitable for the rulers and merchants
#                    involved in new global trade networks. Some Asian states
#                    sought to limit the disruptive economic and cultural effects
#                    of European-dominated long-distance trade by adopting
#                    restrictive or isolationist trade policies.
#   KC-4.3.II.C      Driven largely by political, religious, and economic
#                    rivalries, European states established new maritime empires,
#                    including the Portuguese, Spanish, Dutch, French, and
#                    British.
#   KC-4.3.II.A.ii   The expansion of maritime trading networks fostered the
#                    growth of states in Africa, including the Asante and the
#                    Kingdom of the Kongo, whose participation in trading
#                    networks led to an increase in their influence.
#   KC-4.3.II.A.iii  Despite some disruption and restructuring due to the arrival
#                    of Portuguese, Spanish, and Dutch merchants, existing trade
#                    networks in the Indian Ocean continued to flourish and
#                    included intra-Asian trade and Asian merchants.
#   KC-4.2.II.D      Newly developed colonial economies in the Americas largely
#                    depended on agriculture, utilized existing labor systems,
#                    including the Incan mit'a, and introduced new labor systems
#                    including chattel slavery, indentured servitude, and
#                    encomienda and hacienda systems.
#   KC-4.2.II.B      Enslavement in Africa continued in its traditional forms,
#                    including incorporation of enslaved persons into households
#                    and the export of enslaved persons to the Mediterranean and
#                    the Indian Ocean regions.
#   KC-4.2.II.C      The growth of the plantation economy increased the demand
#                    for enslaved labor in the Americas, leading to significant
#                    demographic, social, and cultural changes.
#
# Illustrative examples printed beside the topic, under two headings:
#   Asian states that adopted restrictive or isolationist trade policies: Ming
#     China; Tokugawa Japan.
#   Indian Ocean Asian merchants: Swahili Arabs; Omanis; Gujaratis; Javanese.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT. The framework gives no date for
# any policy, empire or post, names no ruler, and does not say which maritime
# empire was largest or first. It does not say the Indian Ocean networks were
# destroyed -- its word is "flourish", after "some disruption and restructuring",
# and two items turn on that exact balance. It does not say enslavement in Africa
# ended or was replaced; KC-4.2.II.B says it CONTINUED in its traditional forms
# alongside the growth of the plantation economy in the Americas, and keying the
# two as a replacement would invert the topic's own continuity-and-change frame.
#
# Dates are written "1450 to 1750". Five choices A-E per HISTORY_BRIEF.md. Every
# stimulus is hypothetical or unattributed; no quotation is put in a real
# person's mouth.
TOPIC = ("4.4", "Maritime Empires Established", 4)

_T_MERCHANTS = dict(
    headers=["Group of merchants in a hypothetical port register",
             "Voyages recorded in an early year", "Voyages recorded in a later year"],
    rows=[["Gujarati merchants", "120", "141"],
          ["Javanese merchants", "64", "70"],
          ["Omani merchants", "48", "55"],
          ["Newly arrived European merchants", "0", "37"]])

_T_LABOR = dict(
    headers=["Labor system in a hypothetical colonial account",
             "What the account records about it"],
    rows=[["The Incan mit'a", "In use in the region before the colonial economy was built"],
          ["Chattel slavery", "Introduced with the colonial economy"],
          ["Indentured servitude", "Introduced with the colonial economy"],
          ["The encomienda", "Introduced with the colonial economy"]])

_T_PLANTATION = dict(
    headers=["Decade of a hypothetical estate record",
             "Land under plantation crops (units)",
             "Enslaved laborers recorded on the estates"],
    rows=[["First decade", "200", "90"],
          ["Second decade", "340", "160"],
          ["Third decade", "610", "300"],
          ["Fourth decade", "900", "470"]])

QUESTIONS = [
 dict(
  q=("Where does the framework say Europeans established new trading posts in this period?"),
  choices=[
   "In Africa and Asia",
   "In the interior of the Americas only",
   "In Northern Europe and the Baltic only",
   "In Central Asia along the overland routes",
   "In the Arctic and the far south Atlantic"],
  ans=0,
  why=("KC-4.3.II.A.i states that Europeans established new trading posts in Africa and Asia, "
       "which proved profitable for the rulers and merchants involved in new global trade "
       "networks. The framework places these posts in no other region.")),
 dict(
  q=("The framework says the new trading posts proved profitable. For whom?"),
  choices=[
   "The rulers and merchants involved in new global trade networks",
   "The enslaved laborers working on plantations",
   "The peasant cultivators of inland provinces",
   "The soldiers garrisoning the land empires",
   "The pilgrims travelling the overland routes"],
  ans=0,
  why=("KC-4.3.II.A.i says the new trading posts in Africa and Asia proved profitable for the "
       "rulers and merchants involved in new global trade networks. The framework attributes "
       "that profit to no other group in this statement.")),
 dict(
  q=("According to the framework, what were some Asian states seeking to limit when they changed "
     "their trade policies in this period?"),
  choices=[
   "The disruptive economic and cultural effects of European-dominated long-distance trade",
   "The spread of gunpowder weaponry among their own armies",
   "The movement of pilgrims across their borders",
   "The growth of agriculture in their own provinces",
   "The collection of tribute by their own officials"],
  ans=0,
  why=("KC-4.3.II.A.i says some Asian states sought to limit the disruptive economic and cultural "
       "effects of European-dominated long-distance trade. Gunpowder, pilgrimage, agriculture and "
       "tribute belong to KC-4.3.II, KC-4.1.VI, KC-4.2.II.A and KC-4.3.I.D and are not what those "
       "policies addressed.")),
 dict(
  q=("What kind of policies does the framework say some Asian states adopted in response to "
     "European-dominated long-distance trade?"),
  choices=[
   "Restrictive or isolationist trade policies",
   "Free trade treaties with every European state",
   "The abolition of all customs duties",
   "The chartering of joint-stock companies of their own",
   "The transfer of their ports to European administration"],
  ans=0,
  why=("KC-4.3.II.A.i names restrictive or isolationist trade policies as the response of some "
       "Asian states. Joint-stock companies are KC-4.1.IV.C and belong to European rulers and "
       "merchants there, and the framework records no free trade treaty, abolished duty or "
       "transferred port anywhere in this topic.")),
 dict(
  q=("Which states are printed among the framework's illustrative examples of Asian states that "
     "adopted restrictive or isolationist trade policies?"),
  choices=[
   "Ming China and Tokugawa Japan",
   "The Mughal and Safavid empires",
   "The Asante and the Kingdom of the Kongo",
   "The Ottoman and Manchu empires",
   "The Portuguese and Dutch states"],
  ans=0,
  why=("The illustrative examples beside Unit 4: Learning Objective E print Ming China and "
       "Tokugawa Japan under the heading of Asian states that adopted restrictive or isolationist "
       "trade policies, which is the second half of KC-4.3.II.A.i. The Asante and the Kongo "
       "appear in KC-4.3.II.A.ii as African states whose influence grew through trade.")),
 dict(
  q=("What does the framework say drove European states to establish new maritime empires?"),
  choices=[
   "Political, religious, and economic rivalries",
   "A shortage of farmland in Europe alone",
   "An agreement among European rulers to divide the oceans",
   "The exhaustion of European timber supplies",
   "A common religious mission agreed between them"],
  ans=0,
  why=("KC-4.3.II.C says that, driven largely by political, religious, and economic rivalries, "
       "European states established new maritime empires. Rivalry is the framework's own word, "
       "which is what makes an agreement or a common mission between those states a "
       "contradiction of the sentence rather than an addition to it.")),
 dict(
  q=("Which maritime empires does the framework name as established by European states in this "
     "period?"),
  choices=[
   "The Portuguese, Spanish, Dutch, French, and British",
   "The Ottoman, Safavid, Mughal, and Manchu",
   "The Asante, Kongo, Songhai, and Swahili",
   "The Russian, Swedish, Danish, and Polish",
   "The Venetian, Genoese, Aragonese, and Castilian"],
  ans=0,
  why=("KC-4.3.II.C names the Portuguese, Spanish, Dutch, French, and British maritime empires. "
       "The four land empires of KC-4.3.II.B and the African states of KC-4.3.II.A.ii are named "
       "elsewhere in the framework and are not among the maritime empires listed here.")),
 dict(
  q=("The framework says the expansion of maritime trading networks fostered the growth of states "
     "in one region. Which states does it name?"),
  choices=[
   "The Asante and the Kingdom of the Kongo, in Africa",
   "Ming China and Tokugawa Japan, in Asia",
   "The Mughal and Safavid empires, in South and Central Asia",
   "The Incan and Mexica states, in the Americas",
   "The Venetian and Genoese republics, in Europe"],
  ans=0,
  why=("KC-4.3.II.A.ii states that the expansion of maritime trading networks fostered the growth "
       "of states in Africa, including the Asante and the Kingdom of the Kongo. Ming China and "
       "Tokugawa Japan appear in KC-4.3.II.A.i as states that restricted trade, which is the "
       "opposite response to the same networks.")),
 dict(
  q=("What does the framework say followed from the Asante's and the Kongo's participation in "
     "trading networks?"),
  choices=[
   "An increase in their influence",
   "The loss of their independence to a European empire",
   "A decision to close their ports to all foreign ships",
   "The abandonment of agriculture in their territories",
   "Their absorption into a neighbouring land empire"],
  ans=0,
  why=("KC-4.3.II.A.ii says the growth of these African states was fostered by the expansion of "
       "maritime trading networks, and that their participation in those networks led to an "
       "increase in their influence. The framework records no loss of independence, closure of "
       "ports or absorption for either state.")),
 dict(
  q=("The framework describes what happened to the trade networks of the Indian Ocean after "
     "European merchants arrived. What does it say?"),
  choices=[
   "They continued to flourish, despite some disruption and restructuring",
   "They collapsed entirely and were replaced by European networks",
   "They were unaffected in any way by the arrival of European merchants",
   "They moved wholesale into the Atlantic",
   "They were closed by agreement between the Asian states"],
  ans=0,
  why=("KC-4.3.II.A.iii says that despite some disruption and restructuring due to the arrival of "
       "Portuguese, Spanish, and Dutch merchants, existing trade networks in the Indian Ocean "
       "continued to flourish. The sentence asserts both the disruption and the flourishing, so "
       "the collapse and the no-effect readings each drop half of it.")),
 dict(
  q=("Whose arrival does the framework name as the source of the disruption and restructuring in "
     "the Indian Ocean?"),
  choices=[
   "Portuguese, Spanish, and Dutch merchants",
   "English, French, and Danish merchants",
   "Ottoman and Safavid merchants",
   "Manchu and Mughal officials",
   "Asante and Kongo traders"],
  ans=0,
  why=("KC-4.3.II.A.iii names the arrival of Portuguese, Spanish, and Dutch merchants as the "
       "source of some disruption and restructuring in the Indian Ocean. The English and French "
       "appear among the maritime empires of KC-4.3.II.C but not in this sentence.")),
 dict(
  q=("What does the framework say the surviving Indian Ocean trade networks included?"),
  choices=[
   "Intra-Asian trade and Asian merchants",
   "Only European merchants operating from new posts",
   "Only the overland caravan routes of Central Asia",
   "Only the transatlantic shipment of cash crops",
   "Only trade conducted under Portuguese licence"],
  ans=0,
  why=("KC-4.3.II.A.iii says the existing trade networks in the Indian Ocean continued to "
       "flourish and included intra-Asian trade and Asian merchants. Each rejected option removes "
       "the Asian participation that the sentence exists to assert.")),
 dict(
  q=("Which merchants are printed among the framework's illustrative examples of Indian Ocean "
     "Asian merchants?"),
  choices=[
   "Swahili Arabs, Omanis, Gujaratis, and Javanese",
   "Venetians, Genoese, Catalans, and Flemings",
   "Asante, Kongo, Songhai, and Hausa traders",
   "Portuguese, Spanish, Dutch, and French factors",
   "Mexica, Incan, Maya, and Pueblo traders"],
  ans=0,
  why=("The illustrative examples for this topic print Swahili Arabs, Omanis, Gujaratis and "
       "Javanese under the heading of Indian Ocean Asian merchants, which is what KC-4.3.II.A.iii "
       "means when it says the networks included intra-Asian trade and Asian merchants.")),
 dict(
  q=("On what does the framework say the newly developed colonial economies in the Americas "
     "largely depended?"),
  choices=[
   "Agriculture",
   "The mining of silver alone",
   "Manufacturing for export to Asia",
   "Fishing and whaling",
   "The carrying trade between European ports"],
  ans=0,
  why=("KC-4.2.II.D states that newly developed colonial economies in the Americas largely "
       "depended on agriculture. Silver appears at KC-4.1.IV as part of the global circulation of "
       "goods rather than as the base of the colonial economies, and the other activities are "
       "named nowhere in this statement.")),
 dict(
  q=("The framework says the colonial economies of the Americas used a labor system that already "
     "existed in the region. Which one does it name?"),
  choices=[
   "The Incan mit'a",
   "Chattel slavery",
   "Indentured servitude",
   "The encomienda",
   "The hacienda"],
  ans=0,
  why=("KC-4.2.II.D says the colonial economies utilized existing labor systems, including the "
       "Incan mit'a, and introduced new labor systems including chattel slavery, indentured "
       "servitude, and encomienda and hacienda systems. The four rejected options are all on the "
       "introduced side of that same sentence.")),
 dict(
  q=("Which labor systems does the framework describe as newly introduced in the colonial "
     "economies of the Americas?"),
  choices=[
   "Chattel slavery, indentured servitude, and encomienda and hacienda systems",
   "The Incan mit'a alone",
   "Tribute collection and tax farming",
   "Peasant agriculture and artisan labor",
   "Household enslavement in Africa"],
  ans=0,
  why=("KC-4.2.II.D names chattel slavery, indentured servitude, and encomienda and hacienda "
       "systems as introduced, against the Incan mit'a as an existing system utilized. Tribute "
       "and tax farming are KC-4.3.I.D, peasant and artisan labor KC-4.2.II.A, and household "
       "enslavement in Africa KC-4.2.II.B.")),
 dict(
  q=("What does the framework say about enslavement within Africa in this period?"),
  choices=[
   "It continued in its traditional forms, including incorporation into households and export to the Mediterranean and the Indian Ocean regions",
   "It ended as the Atlantic trade in enslaved persons grew",
   "It began only after European merchants arrived",
   "It was confined to the Atlantic coast",
   "It was replaced entirely by indentured servitude"],
  ans=0,
  why=("KC-4.2.II.B states that enslavement in Africa continued in its traditional forms, "
       "including incorporation of enslaved persons into households and the export of enslaved "
       "persons to the Mediterranean and the Indian Ocean regions. Continuity is what the "
       "sentence asserts, so an ending, a beginning or a replacement all contradict it.")),
 dict(
  q=("To which regions does the framework say enslaved persons continued to be exported from "
     "Africa in the traditional forms of enslavement there?"),
  choices=[
   "The Mediterranean and the Indian Ocean regions",
   "The Baltic and the North Sea regions",
   "The Andes and Mesoamerica",
   "Central Asia and Siberia",
   "The Pacific islands and Australia"],
  ans=0,
  why=("KC-4.2.II.B says enslavement in Africa continued in its traditional forms, including "
       "incorporation of enslaved persons into households and the export of enslaved persons to "
       "the Mediterranean and the Indian Ocean regions. The framework names no other destination "
       "for that continuing export, and the Americas belong to KC-4.2.II.C's separate account of "
       "the plantation economy.")),
 dict(
  q=("What does the framework identify as the consequence of the growth of the plantation "
     "economy?"),
  choices=[
   "An increased demand for enslaved labor in the Americas, leading to significant demographic, social, and cultural changes",
   "A fall in the demand for labor of every kind in the Americas",
   "The end of agriculture as the base of the colonial economies",
   "The closing of the trading posts established in Africa and Asia",
   "The withdrawal of European merchants from the Indian Ocean"],
  ans=0,
  why=("KC-4.2.II.C says the growth of the plantation economy increased the demand for enslaved "
       "labor in the Americas, leading to significant demographic, social, and cultural changes. "
       "Each rejected option contradicts that sentence or one of KC-4.2.II.D, KC-4.3.II.A.i and "
       "KC-4.3.II.A.iii.")),
 dict(
  q=("A student is sorting the states of this topic by how they responded to the new long-distance "
     "trade. Which sorting follows the framework?"),
  choices=[
   "Ming China and Tokugawa Japan adopted restrictive policies, while the Asante and the Kingdom of the Kongo grew in influence through participation",
   "The Asante and the Kingdom of the Kongo adopted restrictive policies, while Ming China and Tokugawa Japan grew in influence through participation",
   "All four adopted restrictive or isolationist trade policies",
   "All four grew in influence through participation in trading networks",
   "None of the four is described by the framework as responding to long-distance trade at all"],
  ans=0,
  why=("The illustrative examples print Ming China and Tokugawa Japan as Asian states that "
       "adopted restrictive or isolationist trade policies under KC-4.3.II.A.i, while "
       "KC-4.3.II.A.ii names the Asante and the Kingdom of the Kongo as African states whose "
       "participation in trading networks led to an increase in their influence. The rejected "
       "sortings exchange the two responses or flatten them into one.")),
 dict(
  q=("Which statement about the Indian Ocean in this period would a reader of the framework "
     "recognise as an error, even though it uses the framework's own terms?"),
  choices=[
   "The arrival of European merchants ended the existing trade networks rather than disrupting and restructuring them",
   "The arrival of European merchants caused some disruption and restructuring",
   "The existing networks continued to flourish",
   "The networks included intra-Asian trade and Asian merchants",
   "Portuguese, Spanish, and Dutch merchants were the arrivals in question"],
  ans=0,
  why=("KC-4.3.II.A.iii holds both halves together: despite some disruption and restructuring due "
       "to the arrival of Portuguese, Spanish, and Dutch merchants, the existing networks "
       "continued to flourish and included intra-Asian trade and Asian merchants. Replacing "
       "disruption with an ending drops the flourishing the same sentence asserts, while the "
       "other four options are that sentence in pieces.")),
 dict(
  q=("A hypothetical company report describes a walled post on a distant coast, its warehouse, "
     "the local ruler who takes a share of the duties, and the season's profit on goods bought "
     "there and shipped home.\n\n"
     "Which statement of the framework does the report most directly illustrate?"),
  choices=[
   "That new trading posts in Africa and Asia proved profitable for the rulers and merchants involved",
   "That some Asian states adopted restrictive or isolationist trade policies",
   "That colonial economies in the Americas largely depended on agriculture",
   "That enslavement in Africa continued in its traditional forms",
   "That existing trade networks in the Indian Ocean included Asian merchants"],
  ans=0,
  why=("KC-4.3.II.A.i says Europeans established new trading posts in Africa and Asia which proved "
       "profitable for the rulers and merchants involved in new global trade networks, and a post "
       "returning a profit shared with a local ruler is that statement in a document. The rejected "
       "options are KC-4.3.II.A.i's second half, KC-4.2.II.D, KC-4.2.II.B and KC-4.3.II.A.iii.")),
 dict(
  q=("A hypothetical order issued by an Asian government limits the number of foreign ships "
     "admitted to a single port each year and forbids foreign merchants to travel inland.\n\n"
     "Which of the framework's developments does the order represent?"),
  choices=[
   "A restrictive or isolationist trade policy adopted to limit the effects of European-dominated trade",
   "The establishment of a European trading post",
   "The growth of an African state through participation in trading networks",
   "The introduction of a new labor system in the Americas",
   "The chartering of a joint-stock company by a European ruler"],
  ans=0,
  why=("KC-4.3.II.A.i says some Asian states sought to limit the disruptive economic and cultural "
       "effects of European-dominated long-distance trade by adopting restrictive or isolationist "
       "trade policies, and capping foreign shipping at one port is such a policy. The rejected "
       "options are KC-4.3.II.A.i's first half, KC-4.3.II.A.ii, KC-4.2.II.D and KC-4.1.IV.C.")),
 dict(
  q=("A hypothetical port register records the voyages made by four groups of merchants in an "
     "early and a later year, as set out in the table below.\n\n"
     "Which conclusion is best supported by the table alone?"),
  table=_T_MERCHANTS,
  choices=[
   "The Asian merchant groups recorded more voyages in the later year even as European merchants entered the register",
   "The Asian merchant groups recorded fewer voyages in the later year as European merchants entered the register",
   "No European merchants appear in the register in either year",
   "Only one of the Asian merchant groups appears in the later year",
   "The four groups recorded the same number of voyages as one another in the later year"],
  ans=0,
  why=("KC-4.3.II.A.iii says existing trade networks in the Indian Ocean continued to flourish "
       "and included intra-Asian trade and Asian merchants despite the arrival of European "
       "merchants, and a register of this shape is what that continuation looks like. The "
       "verifier recomputes every group's two figures.")),
 dict(
  q=("A hypothetical colonial account records four labor systems and what it says about each, as "
     "set out in the table below.\n\n"
     "Which conclusion is best supported by the table?"),
  table=_T_LABOR,
  choices=[
   "One of the listed systems was already in use in the region and three were introduced with the colonial economy",
   "All four of the listed systems were already in use in the region",
   "All four of the listed systems were introduced with the colonial economy",
   "Two of the listed systems were already in use and two were introduced",
   "None of the listed systems is recorded as introduced with the colonial economy"],
  ans=0,
  why=("KC-4.2.II.D says the colonial economies utilized existing labor systems, including the "
       "Incan mit'a, and introduced new labor systems including chattel slavery, indentured "
       "servitude, and encomienda and hacienda systems, which is the split the account records. "
       "The verifier recomputes how many rows fall on each side.")),
 dict(
  q=("A hypothetical estate record covering four decades appears in the table below.\n\n"
     "Which statement about the recorded figures is accurate?"),
  table=_T_PLANTATION,
  choices=[
   "Both the land under plantation crops and the number of enslaved laborers rise in every decade",
   "The land under plantation crops rises while the number of enslaved laborers falls",
   "The number of enslaved laborers rises while the land under plantation crops falls",
   "Both figures fall after the second decade",
   "Neither figure changes across the four decades"],
  ans=0,
  why=("KC-4.2.II.C says the growth of the plantation economy increased the demand for enslaved "
       "labor in the Americas, and a record in which both columns rise together is what that "
       "relation looks like in an estate's books. The verifier recomputes both columns at every "
       "step and confirms that the two swapped readings are false.")),
 dict(
  q=("Suggested skill 2.A asks a student to identify a source's point of view, purpose, "
     "historical situation, or audience. A hypothetical trading company's own report on the "
     "profits of its posts is being read. Which observation is about the source's purpose?"),
  choices=[
   "That the report was written to justify the company's costs to those who financed it",
   "That the report is written on paper",
   "That the report contains numbers as well as prose",
   "That the report survives in more than one copy",
   "That the report is longer than the previous year's"],
  ans=0,
  why=("Suggested skill 2.A distinguishes point of view, purpose, historical situation and "
       "audience, and the reason a document was produced is its purpose. KC-4.3.II.A.i supplies "
       "the situation the report sits in, the profitability of new trading posts in Africa and "
       "Asia. Length, material, copies and the presence of figures are features of the object "
       "rather than statements about why it was made.")),
 dict(
  q=("This topic's reasoning process is continuity and change. Which pairing of a continuity with "
     "a change is supported by the framework?"),
  choices=[
   "Indian Ocean trade networks continued to flourish, while European states established new maritime empires",
   "Indian Ocean trade networks were replaced, while European states withdrew from the oceans",
   "Enslavement in Africa ceased, while colonial economies abandoned agriculture",
   "Trading posts in Africa and Asia were abandoned, while restrictive policies were dropped",
   "Nothing continued and nothing changed in the period"],
  ans=0,
  why=("KC-4.3.II.A.iii gives the continuity, existing Indian Ocean networks flourishing and "
       "including intra-Asian trade and Asian merchants, and KC-4.3.II.C gives the change, "
       "European states establishing new maritime empires driven by political, religious, and "
       "economic rivalries. Each rejected pairing contradicts a statement of the framework.")),
 dict(
  q=("Which of the following claims about this topic would require evidence from outside the "
     "framework's own statements?"),
  choices=[
   "That one of the new maritime empires was larger than the others",
   "That European states established new maritime empires driven largely by rivalries",
   "That Europeans established new trading posts in Africa and Asia",
   "That the expansion of maritime trading networks fostered the growth of states in Africa",
   "That colonial economies in the Americas introduced new labor systems"],
  ans=0,
  why=("The four rejected statements are KC-4.3.II.C, KC-4.3.II.A.i, KC-4.3.II.A.ii and "
       "KC-4.2.II.D almost verbatim. The framework lists the maritime empires without ranking "
       "them by size, date or importance, so a comparison of that kind would have to be defended "
       "from another source.")),
 dict(
  q=("A summary sentence for this topic is being drafted for students. Which version stays within "
     "what the framework asserts about the period 1450 to 1750?"),
  choices=[
   "European states built new maritime empires out of their rivalries and set up profitable trading posts in Africa and Asia, some Asian states answered with restrictive policies while African states such as the Asante gained influence through trade, Indian Ocean networks went on flourishing with Asian merchants in them, and colonial economies in the Americas rested on agriculture worked by old and new labor systems",
   "European states built no empires in this period, and the trading posts of Africa and Asia returned no profit to anyone",
   "Every Asian state welcomed European trade without restriction, and the Indian Ocean networks disappeared",
   "African states lost all influence through trade, while Ming China and Tokugawa Japan expanded their own maritime empires",
   "Colonial economies in the Americas depended on manufacturing and used no labor system that had existed in the region before"],
  ans=0,
  why=("The keyed sentence joins KC-4.3.II.C, KC-4.3.II.A.i, KC-4.3.II.A.ii, KC-4.3.II.A.iii and "
       "KC-4.2.II.D in turn. Each rejected version denies the empires, denies the profit, denies "
       "the restrictive policies, exchanges the African and Asian responses, or contradicts the "
       "agricultural base and the existing labor systems the framework records.")),
]
