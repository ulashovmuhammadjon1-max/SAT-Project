# AP WORLD HISTORY: MODERN 4.5 Maritime Empires Maintained and Developed
# CED effective Fall 2024/2026, Unit 4 Transoceanic Interconnections, c. 1450 to
# c. 1750. Title copied verbatim from WORLD_HISTORY_topics.json.
#
# Unit 4: Learning Objective H -- explain how rulers employed economic strategies
# to consolidate and maintain power throughout the period from 1450 to 1750.
# Unit 4: Learning Objective I -- explain the continuities and changes in
# networks of exchange from 1450 to 1750.
# Unit 4: Learning Objective J -- explain how political, economic, and cultural
# factors affected society from 1450 to 1750.
# Unit 4: Learning Objective K -- explain the similarities and differences in how
# various belief systems affected societies from 1450 to 1750.
# Suggested skill 3.A, identify and describe a claim and/or argument in a
# text-based or non-text-based source. Reasoning process: continuity and change.
# Thematic focuses: Governance; Economic Systems; Social Interactions and
# Organization; Cultural Developments and Interactions.
#
# Historical developments this module keys to, in the framework's own words:
#   KC-4.1.IV.C     Mercantilist policies and practices were used by European
#                   rulers to expand and control their economies and claim
#                   overseas territories. Joint-stock companies, influenced by
#                   these mercantilist principles, were used by rulers and
#                   merchants to finance exploration and were used by rulers to
#                   compete against one another in global trade.
#   KC-4.3.III.ii   Economic disputes led to rivalries and conflict between
#                   states.
#   KC-4.1.IV.D.i   The Atlantic trading system involved the movement of goods,
#                   wealth, and labor, including enslaved persons.
#   KC-4.1.IV       The new global circulation of goods was facilitated by
#                   chartered European monopoly companies and the global flow of
#                   silver, especially from Spanish colonies in the Americas,
#                   which was used to purchase Asian goods for the Atlantic
#                   markets and satisfy Chinese demand for silver. Regional
#                   markets continued to flourish in Afro-Eurasia by using
#                   established commercial practices and new transoceanic and
#                   regional shipping services developed by European merchants.
#   KC-4.2.II.A     Peasant and artisan labor continued and intensified in many
#                   regions as the demand for food and consumer goods increased.
#   KC-4.2.III.C    Some notable gender and family restructuring occurred,
#                   including demographic changes in Africa that resulted from
#                   the trade of enslaved persons.
#   KC-4.1.IV.D.ii  The Atlantic trading system involved the movement of labor,
#                   including enslaved persons, and the mixing of African,
#                   American, and European cultures and peoples, with all parties
#                   contributing to this cultural synthesis.
#   KC-4.1.VI       In some cases, the increase and intensification of
#                   interactions between newly connected hemispheres expanded the
#                   reach and furthered development of existing religions, and
#                   contributed to religious conflicts and the development of
#                   syncretic belief systems and practices.
#
# Illustrative examples printed beside the topic, under two headings:
#   Competition over trade routes: Muslim and European rivalry in the Indian
#     Ocean; Moroccan conflict with the Songhai Empire.
#   Increased peasant and artisan labor: Western Europe, wool and linen; India,
#     cotton; China, silk.
#
# NOTE ON AN OVERLAP WITH TOPIC 3.1, so nobody reads it as a contradiction. The
# Songhai Empire's conflict with Morocco is printed TWICE in this CED: beside
# topic 3.1 under the heading "State rivalries", illustrating KC-4.3.III.i's
# political and religious disputes, and beside this topic under the heading
# "Competition over trade routes", illustrating KC-4.3.III.ii's economic
# disputes. `w3_1.py` keys the first heading. This module keys only the second,
# and says so in its `why`.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT. The framework gives no dates,
# no quantities of silver, no ruler and no company by name. KC-4.1.VI opens with
# "In some cases", and that qualifier is kept in every item that touches it: the
# framework does not say interactions ALWAYS expanded a religion's reach, nor
# that syncretism happened everywhere. And KC-4.1.IV asserts BOTH that European
# merchants developed new shipping services AND that Afro-Eurasian regional
# markets continued to flourish using established commercial practices; nothing
# here keys one of those halves as displacing the other.
#
# Dates are written "1450 to 1750". Five choices A-E per HISTORY_BRIEF.md. Every
# stimulus is hypothetical or unattributed; no quotation is put in a real
# person's mouth.
TOPIC = ("4.5", "Maritime Empires Maintained and Developed", 4)

_T_SILVER = dict(
    headers=["Consignment in a hypothetical ledger", "Where the silver was mined",
             "What the ledger records it buying"],
    rows=[["Consignment 1", "A Spanish colony in the Americas",
           "Asian goods for the Atlantic markets"],
          ["Consignment 2", "A Spanish colony in the Americas",
           "Asian goods for the Atlantic markets"],
          ["Consignment 3", "A Spanish colony in the Americas",
           "Goods in China, where demand for silver was high"],
          ["Consignment 4", "A mine within Europe", "Grain within Europe"]])

_T_WORKSHOPS = dict(
    headers=["Workshop district in a hypothetical survey", "Output in an early year",
             "Output in a later year"],
    rows=[["A woollen district", "1,200", "1,850"],
          ["A linen district", "800", "1,150"],
          ["A cotton district", "2,400", "3,600"],
          ["A silk district", "950", "1,400"]])

_T_ATLANTIC = dict(
    headers=["Entry in a hypothetical Atlantic manifest", "What the entry records moving"],
    rows=[["Entry 1", "Goods"],
          ["Entry 2", "Wealth in coin"],
          ["Entry 3", "Labor, in the form of enslaved persons"],
          ["Entry 4", "A private letter between two families"]])

QUESTIONS = [
 dict(
  q=("The framework says European rulers used mercantilist policies and practices. To what end?"),
  choices=[
   "To expand and control their economies and claim overseas territories",
   "To abolish customs duties across Europe",
   "To transfer their overseas claims to rival rulers",
   "To withdraw their merchants from global trade",
   "To fix a single price for goods across the world"],
  ans=0,
  why=("KC-4.1.IV.C states that mercantilist policies and practices were used by European rulers "
       "to expand and control their economies and claim overseas territories. Abolition, "
       "transfer, withdrawal and a single world price are each the opposite of one part of that "
       "sentence.")),
 dict(
  q=("According to the framework, what were joint-stock companies used for?"),
  choices=[
   "To finance exploration, and by rulers to compete against one another in global trade",
   "To finance exploration, and by rulers to end competition between themselves",
   "To collect tribute within the land empires",
   "To administer the labor systems of the colonial Americas",
   "To restrict the movement of merchants inside Europe"],
  ans=0,
  why=("KC-4.1.IV.C says joint-stock companies were used by rulers and merchants to finance "
       "exploration and were used by rulers to compete against one another in global trade. "
       "Ending competition reverses the second half of that sentence; tribute is KC-4.3.I.D and "
       "the colonial labor systems are KC-4.2.II.D.")),
 dict(
  q=("The framework says joint-stock companies were influenced by a particular set of principles. "
     "Which ones?"),
  choices=[
   "Mercantilist principles",
   "The principles of free trade",
   "The principles of a syncretic belief system",
   "The principles of isolationist policy",
   "The principles of tribute collection"],
  ans=0,
  why=("KC-4.1.IV.C describes joint-stock companies as influenced by mercantilist principles, the "
       "same principles behind the policies European rulers used to expand and control their "
       "economies. Isolationist policy is KC-4.3.II.A.i and belongs to some Asian states, and "
       "tribute collection is KC-4.3.I.D.")),
 dict(
  q=("What does the framework say economic disputes led to in this period?"),
  choices=[
   "Rivalries and conflict between states",
   "A permanent settlement of borders between states",
   "The abandonment of long-distance trade",
   "The merger of rival states into one empire",
   "The disappearance of competition over trade routes"],
  ans=0,
  why=("KC-4.3.III.ii states that economic disputes led to rivalries and conflict between states, "
       "which sits beside KC-4.3.III.i on political and religious disputes as a second cause of "
       "the same outcome. Settlement, abandonment, merger and the end of competition are each "
       "the opposite of what the sentence says.")),
 dict(
  q=("Which conflicts are printed among the framework's illustrative examples of competition over "
     "trade routes for this topic?"),
  choices=[
   "Muslim and European rivalry in the Indian Ocean, and the Moroccan conflict with the Songhai Empire",
   "The Safavid conflict with the Mughal Empire, and the Manchu conflict with the Ottoman Empire",
   "The Asante conflict with the Kingdom of the Kongo",
   "Rivalry between Ming China and Tokugawa Japan over Pacific routes",
   "Rivalry between the Incan and Mexica states over Andean routes"],
  ans=0,
  why=("The illustrative examples beside Unit 4: Learning Objective H print Muslim and European "
       "rivalry in the Indian Ocean and the Moroccan conflict with the Songhai Empire under the "
       "heading of competition over trade routes, which is what KC-4.3.III.ii means by economic "
       "disputes leading to rivalries and conflict. The same Moroccan conflict is printed again "
       "beside topic 3.1 under state rivalries, where it illustrates KC-4.3.III.i instead.")),
 dict(
  q=("The framework names two things that facilitated the new global circulation of goods. Which "
     "pair does it name?"),
  choices=[
   "Chartered European monopoly companies and the global flow of silver",
   "Overland caravan routes and pilgrimage networks",
   "Restrictive trade policies and isolationist decrees",
   "Tribute collection and tax farming",
   "The mit'a and the encomienda"],
  ans=0,
  why=("KC-4.1.IV says the new global circulation of goods was facilitated by chartered European "
       "monopoly companies and the global flow of silver. Restrictive policies are KC-4.3.II.A.i, "
       "revenue methods are KC-4.3.I.D, and the labor systems are KC-4.2.II.D.")),
 dict(
  q=("From where does the framework say the silver in the global flow especially came?"),
  choices=[
   "Spanish colonies in the Americas",
   "Mines in Central Asia",
   "Mines in Southern Africa",
   "Mines in the Japanese islands",
   "Mines in Northern Europe"],
  ans=0,
  why=("KC-4.1.IV says the global flow of silver came especially from Spanish colonies in the "
       "Americas. The framework names no other source of silver anywhere in this unit.")),
 dict(
  q=("According to the framework, what was the silver in the global flow used for?"),
  choices=[
   "To purchase Asian goods for the Atlantic markets and to satisfy Chinese demand for silver",
   "To purchase Atlantic goods for the Asian markets and to satisfy European demand for silver",
   "To pay the wages of peasant laborers in Western Europe",
   "To finance the construction of monumental architecture in the land empires",
   "To replace coined money with barter across Afro-Eurasia"],
  ans=0,
  why=("KC-4.1.IV says the silver was used to purchase Asian goods for the Atlantic markets and "
       "satisfy Chinese demand for silver. The second option exchanges both halves of that "
       "sentence, which reads perfectly well and is the reverse of what the framework states.")),
 dict(
  q=("What does the framework say happened to regional markets in Afro-Eurasia in this period?"),
  choices=[
   "They continued to flourish, using established commercial practices and new shipping services developed by European merchants",
   "They were replaced entirely by European monopoly companies",
   "They closed as the global flow of silver grew",
   "They abandoned their established commercial practices",
   "They traded only with one another and never with European merchants"],
  ans=0,
  why=("KC-4.1.IV says regional markets continued to flourish in Afro-Eurasia by using "
       "established commercial practices and new transoceanic and regional shipping services "
       "developed by European merchants. The sentence asserts the old practices and the new "
       "services together, so a reading that drops either half misreports it.")),
 dict(
  q=("What does the framework say the Atlantic trading system involved the movement of?"),
  choices=[
   "Goods, wealth, and labor, including enslaved persons",
   "Goods alone, with no movement of people",
   "Silver alone, with no movement of goods",
   "Pilgrims travelling between shrines",
   "Soldiers moving between land empires"],
  ans=0,
  why=("KC-4.1.IV.D.i states that the Atlantic trading system involved the movement of goods, "
       "wealth, and labor, including enslaved persons. Each rejected option removes one or more "
       "of the three things the sentence names.")),
 dict(
  q=("The framework describes a cultural synthesis arising from the Atlantic trading system. "
     "Whose cultures and peoples does it say mixed?"),
  choices=[
   "African, American, and European, with all parties contributing",
   "African and European only, with the Americas contributing nothing",
   "American and European only, with Africa contributing nothing",
   "Asian and European only",
   "No cultures mixed, according to the framework"],
  ans=0,
  why=("KC-4.1.IV.D.ii says the Atlantic trading system involved the movement of labor, including "
       "enslaved persons, and the mixing of African, American, and European cultures and peoples, "
       "with all parties contributing to this cultural synthesis. The phrase all parties is the "
       "framework's own, and each rejected option removes a contributor it names.")),
 dict(
  q=("What does the framework say happened to peasant and artisan labor in this period?"),
  choices=[
   "It continued and intensified in many regions as demand for food and consumer goods increased",
   "It disappeared as plantation labor replaced it everywhere",
   "It declined as demand for food and consumer goods fell",
   "It was confined to the Americas",
   "It was replaced by wage labor across Afro-Eurasia"],
  ans=0,
  why=("KC-4.2.II.A states that peasant and artisan labor continued and intensified in many "
       "regions as the demand for food and consumer goods increased. Continuity together with "
       "intensification is what the sentence asserts, so disappearance, decline and replacement "
       "each contradict it.")),
 dict(
  q=("Which pairings of a region with a product are printed among the framework's illustrative "
     "examples of increased peasant and artisan labor?"),
  choices=[
   "Western Europe with wool and linen, India with cotton, and China with silk",
   "Western Europe with silk, India with wool and linen, and China with cotton",
   "Western Europe with cotton, India with silk, and China with wool and linen",
   "Western Europe with sugar, India with tobacco, and China with coffee",
   "Western Europe with silver, India with gold, and China with copper"],
  ans=0,
  why=("The illustrative examples beside Unit 4: Learning Objective I print Western Europe with "
       "wool and linen, India with cotton, and China with silk under the heading of increased "
       "peasant and artisan labor, which is KC-4.2.II.A's intensification. The rejected options "
       "rotate the same three products between the same three regions or replace them "
       "altogether.")),
 dict(
  q=("What does the framework say about gender and family structures in this period?"),
  choices=[
   "Some notable restructuring occurred, including demographic changes in Africa resulting from the trade of enslaved persons",
   "No restructuring of any kind occurred in the period",
   "Restructuring occurred only in Europe and left Africa untouched",
   "Restructuring resulted entirely from the spread of new religions",
   "Restructuring occurred only after 1750"],
  ans=0,
  why=("KC-4.2.III.C says some notable gender and family restructuring occurred, including "
       "demographic changes in Africa that resulted from the trade of enslaved persons. The word "
       "some is the framework's own and the African demographic change is the example it gives, "
       "so a denial and a relocation both misreport it.")),
 dict(
  q=("The framework describes what happened to religions as interactions between newly connected "
     "hemispheres increased. Which statement follows it?"),
  choices=[
   "In some cases the reach of existing religions expanded, and religious conflicts and syncretic belief systems also developed",
   "In every case the reach of existing religions expanded, and no conflict followed",
   "Existing religions everywhere disappeared and were replaced by new ones",
   "Religious practice was unaffected by the increase in interactions",
   "The framework records only conflict and no development of new practices"],
  ans=0,
  why=("KC-4.1.VI says that in some cases the increase and intensification of interactions "
       "between newly connected hemispheres expanded the reach and furthered development of "
       "existing religions, and contributed to religious conflicts and the development of "
       "syncretic belief systems and practices. The qualifier in some cases and the joint mention "
       "of conflict and syncretism are both the framework's own.")),
 dict(
  q=("Which statement about the flow of silver would a reader of the framework recognise as an "
     "error, even though every term in it appears in the same sentence?"),
  choices=[
   "Silver flowed from Asian mines to satisfy European demand and to buy Atlantic goods for Asian markets",
   "Silver came especially from Spanish colonies in the Americas",
   "Silver was used to purchase Asian goods for the Atlantic markets",
   "Silver satisfied Chinese demand for silver",
   "The global flow of silver facilitated the new global circulation of goods"],
  ans=0,
  why=("KC-4.1.IV has silver coming especially from Spanish colonies in the Americas, buying "
       "Asian goods for the Atlantic markets and satisfying Chinese demand, so the reversal of "
       "both the source and the destination is the error. The other four options are that "
       "sentence in pieces.")),
 dict(
  q=("A student attributes mercantilist policies to Asian rulers and restrictive trade policies to "
     "European rulers. What is the correction from the framework?"),
  choices=[
   "Mercantilist policies were used by European rulers, and restrictive or isolationist policies were adopted by some Asian states",
   "Both mercantilist and restrictive policies were used by European rulers alone",
   "Both mercantilist and restrictive policies were adopted by Asian states alone",
   "Neither kind of policy is described by the framework for this period",
   "Mercantilist policies were adopted only after the restrictive policies were dropped"],
  ans=0,
  why=("KC-4.1.IV.C says mercantilist policies and practices were used by European rulers, while "
       "KC-4.3.II.A.i says some Asian states adopted restrictive or isolationist trade policies to "
       "limit the effects of European-dominated long-distance trade. The student has exchanged "
       "the two, which is the error this item is built to catch.")),
 dict(
  q=("A hypothetical royal ordinance of the period requires that goods from the crown's overseas "
     "territories travel only in ships of the crown's own subjects, and that they be landed first "
     "in a home port.\n\n"
     "Which of the framework's developments does the ordinance represent?"),
  choices=[
   "A mercantilist policy used to expand and control an economy and claim overseas territories",
   "A restrictive policy adopted by an Asian state to limit European trade",
   "The chartering of a joint-stock company to finance exploration",
   "The collection of tribute to generate revenue for a land empire",
   "The introduction of a new labor system in a colonial economy"],
  ans=0,
  why=("KC-4.1.IV.C says mercantilist policies and practices were used by European rulers to "
       "expand and control their economies and claim overseas territories, and an order reserving "
       "colonial carriage to the ruler's own subjects is such a policy. The rejected options are "
       "KC-4.3.II.A.i, the second half of KC-4.1.IV.C, KC-4.3.I.D and KC-4.2.II.D.")),
 dict(
  q=("A hypothetical charter grants a company the sole right to trade on one route, invites "
     "investors to buy shares in its voyages, and reserves a share of the profit to the ruler who "
     "granted it.\n\n"
     "Which statement of the framework does the charter most directly illustrate?"),
  choices=[
   "That joint-stock companies were used by rulers and merchants to finance exploration and to compete in global trade",
   "That regional markets in Afro-Eurasia continued to flourish",
   "That peasant and artisan labor intensified as demand increased",
   "That economic disputes led to rivalries and conflict between states",
   "That the Atlantic trading system moved goods, wealth, and labor"],
  ans=0,
  why=("KC-4.1.IV.C says joint-stock companies, influenced by mercantilist principles, were used "
       "by rulers and merchants to finance exploration and were used by rulers to compete against "
       "one another in global trade, and a chartered monopoly funded by shareholders with a "
       "royal share of the profit is that arrangement. The rejected options are KC-4.1.IV, "
       "KC-4.2.II.A, KC-4.3.III.ii and KC-4.1.IV.D.i.")),
 dict(
  q=("Four consignments of silver appear in a hypothetical ledger, as set out in the table "
     "below.\n\n"
     "Which conclusion is best supported by the table alone?"),
  table=_T_SILVER,
  choices=[
   "Three of the four consignments were mined in a Spanish colony in the Americas and spent on Asian goods or in China",
   "Every consignment in the ledger was mined within Europe",
   "Every consignment in the ledger was spent within Europe",
   "No consignment in the ledger was spent on Asian goods",
   "The consignments were divided evenly between American and European mines"],
  ans=0,
  why=("KC-4.1.IV says the global flow of silver came especially from Spanish colonies in the "
       "Americas and was used to purchase Asian goods for the Atlantic markets and satisfy "
       "Chinese demand for silver, which is the pattern three of these four rows record. The "
       "verifier recomputes the origin and the destination of every consignment.")),
 dict(
  q=("A hypothetical survey of four workshop districts records the output of each in an early and "
     "a later year, as set out in the table below.\n\n"
     "Which statement about the recorded figures is accurate?"),
  table=_T_WORKSHOPS,
  choices=[
   "Output rose in every district between the early year and the later year",
   "Output fell in every district between the early year and the later year",
   "Output rose in the woollen district and fell in the other three",
   "Output was the same in every district in the later year",
   "Output did not change in any district between the two years"],
  ans=0,
  why=("KC-4.2.II.A says peasant and artisan labor continued and intensified in many regions as "
       "the demand for food and consumer goods increased, and the illustrative examples name wool "
       "and linen, cotton and silk as the goods concerned. The verifier recomputes each "
       "district's two figures.")),
 dict(
  q=("A hypothetical Atlantic manifest records four entries, as set out in the table below.\n\n"
     "How many of the entries record something the framework says the Atlantic trading system "
     "moved?"),
  table=_T_ATLANTIC,
  choices=[
   "Three of the four entries, since the framework names goods, wealth, and labor",
   "One of the four entries, since the framework names only goods",
   "Two of the four entries, since the framework names only goods and wealth",
   "All four entries, since the framework names every kind of movement",
   "None of the entries, since the framework describes no movement at all"],
  ans=0,
  why=("KC-4.1.IV.D.i says the Atlantic trading system involved the movement of goods, wealth, "
       "and labor, including enslaved persons, which covers three of the four entries and not the "
       "private letter. The verifier recomputes which entries fall inside that list.")),
 dict(
  q=("Suggested skill 3.A asks a student to identify and describe the claim or argument a source "
     "is making. A hypothetical pamphlet of the period urges a ruler to keep colonial trade in "
     "the hands of the ruler's own subjects. What is its claim?"),
  choices=[
   "That the ruler's power is served by controlling the economy and its overseas trade",
   "That the pamphlet was printed in a particular year",
   "That the pamphlet is addressed to a ruler",
   "That the pamphlet is shorter than other pamphlets of its kind",
   "That the pamphlet uses figures as well as prose"],
  ans=0,
  why=("Under suggested skill 3.A the claim is what the source argues for, and KC-4.1.IV.C "
       "supplies the position argued: mercantilist policies and practices were used by European "
       "rulers to expand and control their economies and claim overseas territories. A printing "
       "date, an addressee, a length and a use of figures are features of the document rather "
       "than its argument.")),
 dict(
  q=("Continuity and change is the reasoning process printed beside this topic. Which pairing of "
     "a continuity with a change does the framework support?"),
  choices=[
   "Regional markets went on using established commercial practices, while European merchants developed new transoceanic and regional shipping services",
   "Regional markets abandoned their established practices, while European merchants withdrew their shipping services",
   "Peasant labor disappeared, while joint-stock companies ceased to finance exploration",
   "Silver stopped flowing, while mercantilist policies were abandoned",
   "Nothing continued and nothing changed in the networks of exchange"],
  ans=0,
  why=("KC-4.1.IV holds both in a single sentence: regional markets continued to flourish in "
       "Afro-Eurasia by using established commercial practices AND new transoceanic and regional "
       "shipping services developed by European merchants. Each rejected pairing contradicts that "
       "sentence or one of KC-4.2.II.A and KC-4.1.IV.C.")),
 dict(
  q=("Unit 4: Learning Objective H asks how rulers employed economic strategies to consolidate and "
     "maintain power. Which pair of strategies does the framework attribute to European rulers?"),
  choices=[
   "Mercantilist policies, and the use of joint-stock companies to compete in global trade",
   "Tribute collection, and the recruitment of bureaucratic elites",
   "Restrictive trade policies, and the closing of ports to foreign merchants",
   "The abolition of monopolies, and the opening of trade to all comers",
   "The export of enslaved persons to the Mediterranean, and household enslavement"],
  ans=0,
  why=("KC-4.1.IV.C names both: mercantilist policies and practices used by European rulers to "
       "expand and control their economies, and joint-stock companies used by rulers to compete "
       "against one another in global trade. Tribute and bureaucratic elites are KC-4.3.I.D and "
       "KC-4.3.I.C, restrictive policies are KC-4.3.II.A.i, and the African export trade is "
       "KC-4.2.II.B.")),
 dict(
  q=("Which piece of evidence would best support the framework's claim that the trade of enslaved "
     "persons produced demographic change in Africa?"),
  choices=[
   "Records showing a changed balance of ages and sexes in the populations of affected African regions",
   "Records of the tonnage of silver leaving a Spanish colony",
   "Records of the wool woven in a Western European district",
   "Records of the shares sold by a chartered monopoly company",
   "Records of the ships built in a northern European port"],
  ans=0,
  why=("KC-4.2.III.C says some notable gender and family restructuring occurred, including "
       "demographic changes in Africa that resulted from the trade of enslaved persons, so "
       "evidence for it has to be about the composition of those populations. Silver, weaving, "
       "company shares and shipbuilding bear on KC-4.1.IV, KC-4.2.II.A and KC-4.1.IV.C "
       "instead.")),
 dict(
  q=("Which claim about this topic would send a student outside the framework in search of "
     "evidence for it?"),
  choices=[
   "That one European ruler's mercantilist policy was more successful than another's",
   "That mercantilist policies were used by European rulers to control their economies",
   "That the global flow of silver came especially from Spanish colonies in the Americas",
   "That regional markets in Afro-Eurasia continued to flourish",
   "That the Atlantic trading system moved goods, wealth, and labor"],
  ans=0,
  why=("The four rejected statements are KC-4.1.IV.C, KC-4.1.IV and KC-4.1.IV.D.i almost verbatim. "
       "The framework compares no two rulers' policies for success, so a ranking of that kind "
       "would have to be defended from another source.")),
 dict(
  q=("A historian argues that religious change in this period cannot be summed up as growth alone. "
     "Which part of the framework most directly supports that argument?"),
  choices=[
   "The statement that interactions contributed to religious conflicts and to syncretic belief systems as well as expanding the reach of existing religions",
   "The statement that peasant and artisan labor intensified",
   "The statement that silver satisfied Chinese demand",
   "The statement that joint-stock companies financed exploration",
   "The statement that colonial economies depended on agriculture"],
  ans=0,
  why=("KC-4.1.VI says that in some cases the increase and intensification of interactions "
       "expanded the reach and furthered development of existing religions, and contributed to "
       "religious conflicts and the development of syncretic belief systems and practices, so "
       "growth is only one of the outcomes it names. The rejected statements are KC-4.2.II.A, "
       "KC-4.1.IV, KC-4.1.IV.C and KC-4.2.II.D.")),
 dict(
  q=("A student writes that European merchants took over the trade of Afro-Eurasia in this period. "
     "What is the most accurate correction from the framework?"),
  choices=[
   "Regional markets continued to flourish using established practices, alongside the new shipping services European merchants developed",
   "European merchants withdrew from Afro-Eurasian trade entirely",
   "Regional markets ceased trading and European companies replaced them",
   "European merchants developed no new shipping services in the period",
   "The framework says nothing about regional markets in this period"],
  ans=0,
  why=("KC-4.1.IV says regional markets continued to flourish in Afro-Eurasia by using "
       "established commercial practices and new transoceanic and regional shipping services "
       "developed by European merchants, and KC-4.3.II.A.iii says the same of the Indian Ocean "
       "networks. The correction has to keep both the continuation and the new services, and each "
       "rejected option drops one of them.")),
 dict(
  q=("A study guide is condensing this topic into one sentence. Which version stays within what "
     "the framework asserts about the period 1450 to 1750?"),
  choices=[
   "European rulers used mercantilist policies and chartered companies to build and compete for wealth, American silver bought Asian goods and met Chinese demand while Afro-Eurasian regional markets kept flourishing, the Atlantic system moved goods, wealth and enslaved labor and mixed three continents' cultures, and economic disputes set states against one another",
   "European rulers abandoned control of their economies, and no company was chartered in the period",
   "Silver flowed from Asia to the Americas, and Afro-Eurasian regional markets closed as European companies replaced them",
   "The Atlantic system moved goods but no people, and no cultural mixing followed from it",
   "Economic disputes produced no rivalry between states, and peasant labor fell away as demand declined"],
  ans=0,
  why=("The keyed sentence joins KC-4.1.IV.C, KC-4.1.IV, KC-4.1.IV.D.i, KC-4.1.IV.D.ii and "
       "KC-4.3.III.ii in turn. Each rejected version denies the policies and companies, reverses "
       "the direction of the silver, denies the movement of labor and the cultural synthesis, or "
       "contradicts KC-4.3.III.ii and KC-4.2.II.A.")),
]
