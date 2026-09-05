# AP WORLD HISTORY: MODERN 6.5 Economic Imperialism from 1750 to 1900
# CED effective Fall 2026, Unit 6 Consequences of Industrialization, c. 1750 to
# c. 1900. Thematic focus ECN, Economics Systems: "As societies develop, they
# affect and are affected by the ways that they produce, exchange, and consume
# goods and services."
#
# Unit 6 Learning Objective E: "Explain how various economic factors contributed to
# the development of the global economy from 1750 to 1900."
# Reasoning process: Causation. Suggested skill 4.B, explain how a specific
# historical development or process is situated within a broader historical context.
#
# The historical developments this topic prints, in the framework's own words:
#   KC-5.2.I.E   Industrialized states and businesses within those states practiced
#                economic imperialism primarily in Asia and Latin America.
#   KC-5.1.II.C  Trade in some commodities was organized in a way that gave
#                merchants and companies based in Europe and the U.S. a distinct
#                economic advantage.
#
# Illustrative examples the CED prints for this topic, under its own two headings.
# These are the only named places, commodities and events in this module:
#   Industrialized states practicing economic imperialism: Britain and France
#     expanding their influence in China through the Opium Wars; the construction
#     of the Port of Buenos Aires with the support of British firms.
#   Commodities that contributed to European and American economic advantage:
#     opium produced in the Middle East or South Asia and exported to China; cotton
#     grown in South Asia and Egypt and exported to Great Britain and other
#     European countries; palm oil produced in sub-Saharan Africa and exported to
#     European countries; copper extracted in Chile.
#
# TWO THINGS THIS MODULE IS CAREFUL ABOUT.
#   1. The regional claim belongs to KC-5.2.I.E and to nothing else: economic
#      imperialism was practiced PRIMARILY in Asia and Latin America. The commodity
#      list under KC-5.1.II.C is a different statement and includes a sub-Saharan
#      African product. Items 2 and 12 turn on keeping those two apart, because
#      merging them is the easiest wrong key in this topic.
#   2. Every commodity example carries a DIRECTION -- produced in one place,
#      exported to another. Reversing a direction is the classic near-miss
#      distractor, so wherever one is offered the anchor carries both clauses.
#
# REPAIR, recorded because the module shipped ungated. The author of this module was
# stopped before writing verify_w6_5.py, so items 14 to 16 reached the tree with no
# check on them. Item 15 asked for "the single shipment arranged by a firm based in
# the region where the good was produced" and the hypothetical record has TWO such
# rows -- Record 5 (Latin America to Latin America) and Record 4 (Western Europe to
# Western Europe) -- so the item had two defensible answers. Item 15 now names the
# second condition that makes Record 5 unique, item 14 has been rewritten to a
# question the record settles on its own rather than one needing a student to supply
# which regions were industrialized, and item 16's key now says "at least one"
# because two rows satisfy it. verify_w6_5.py asserts the UNIQUENESS of each of
# those keys, which is the check whose absence let the defect through.
#
# The CED names the Opium Wars and the Port of Buenos Aires and describes neither.
# No item asks what happened in a war, when it happened, who signed what, or what
# any of it cost. Every source is UNATTRIBUTED and labelled illustrative, and
# tables are labelled hypothetical with every keyed conclusion recomputable from
# the table alone.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md. Dates are written "1750 to 1900".
TOPIC = ("6.5", "Economic Imperialism from 1750 to 1900", 6)

_T_SHIPMENTS = dict(
    headers=["Shipment record (hypothetical)", "Region where the good was produced",
             "Region to which it was shipped", "Home base of the firm arranging the shipment"],
    rows=[["Record 1", "South Asia", "Western Europe", "Western Europe"],
          ["Record 2", "Latin America", "North America", "North America"],
          ["Record 3", "Sub-Saharan Africa", "Western Europe", "Western Europe"],
          ["Record 4", "Western Europe", "Latin America", "Western Europe"],
          ["Record 5", "Latin America", "Western Europe", "Latin America"]])

_T_ADVANTAGE = dict(
    headers=["Service required to move one hypothetical commodity to market",
             "Share provided by firms based in Europe or North America (hypothetical, percent)"],
    rows=[["Ocean shipping", "88"],
          ["Marine insurance", "91"],
          ["Trade finance and credit", "84"],
          ["Warehousing at the port of shipment", "35"],
          ["Growing and harvesting the crop", "2"]])

QUESTIONS = [
 dict(q="According to the course framework, who practiced economic imperialism in this period?",
   choices=[
     "Industrialized states and businesses based within those states",
     "Industrialized states acting alone, with no part played by private businesses",
     "Private businesses acting alone, with no part played by any state",
     "The governments of the territories in which the commodities were produced",
     "Chartered companies that had been abolished before the period began"], ans=0,
   why="KC-5.2.I.E states that industrialized states AND businesses within those states practiced economic imperialism. Both actors are named in that sentence, which is why each option confining the practice to one of them, or moving it to producing-country governments or to abolished companies, is wrong."),
 dict(q="In which regions does the framework say economic imperialism was practiced primarily?",
   choices=[
     "Asia and Latin America",
     "Africa and Australia",
     "Northern and Western Europe",
     "North America and the Arctic",
     "Central Asia and the Pacific islands only"], ans=0,
   why="KC-5.2.I.E states that industrialized states and businesses within those states practiced economic imperialism primarily in Asia and Latin America. The word primarily is the framework's own, and the regions it names are those two."),
 dict(q="The framework states that trade in some commodities was organized in a particular way. What did that organization produce?",
   choices=[
     "A distinct economic advantage for merchants and companies based in Europe and the United States",
     "A distinct economic advantage for merchants based in the producing regions",
     "An equal division of the gains between producing and consuming regions",
     "The end of long-distance trade in those commodities",
     "A prohibition on the sale of those commodities outside their region of origin"], ans=0,
   why="KC-5.1.II.C states that trade in some commodities was organized in a way that gave merchants and companies based in Europe and the U.S. a distinct economic advantage. The reversal, an advantage to the producing regions, is offered as a distractor and is the opposite of what the framework says."),
 dict(q="One of the commodities the framework lists as contributing to European and American economic advantage moved in which direction?",
   choices=[
     "Opium produced in the Middle East or South Asia and exported to China",
     "Opium produced in China and exported to the Middle East and South Asia",
     "Opium produced in Western Europe and exported to South Asia",
     "Opium produced in Latin America and exported to Western Europe",
     "Opium produced in China and consumed entirely within China"], ans=0,
   why="The CED lists opium produced in the Middle East or South Asia and exported to China among the commodities that contributed to European and American economic advantage, under KC-5.1.II.C. The direction is the whole content of the example, and the reversal is offered as a distractor."),
 dict(q="How does the framework describe the cotton trade among the commodities that gave European and American merchants an advantage?",
   choices=[
     "Cotton grown in South Asia and Egypt and exported to Great Britain and other European countries",
     "Cotton grown in Great Britain and exported to South Asia and Egypt",
     "Cotton grown in Latin America and exported to sub-Saharan Africa",
     "Cotton grown in China and exported to the Middle East",
     "Cotton grown in South Asia and consumed entirely within South Asia"], ans=0,
   why="The CED lists cotton grown in South Asia and Egypt and exported to Great Britain and other European countries among the commodities under KC-5.1.II.C. Both clauses of the key are needed, since the reversed direction is offered and would describe the opposite trade."),
 dict(q="Which commodity does the framework list as produced in sub-Saharan Africa and exported to European countries?",
   choices=[
     "Palm oil",
     "Opium",
     "Copper",
     "Cotton grown in South Asia",
     "Manufactured cloth"], ans=0,
   why="The CED lists palm oil produced in sub-Saharan Africa and exported to European countries among the commodities that contributed to European and American economic advantage. Opium moves to China, copper is extracted in Chile, South Asian cotton goes to Europe from South Asia, and manufactured cloth is a finished good rather than one of the commodities listed under KC-5.1.II.C."),
 dict(q="The framework's list of commodities that contributed to European and American economic advantage includes a metal. Where does it say that metal was extracted?",
   choices=[
     "Chile",
     "Egypt",
     "China",
     "West Africa",
     "South Asia"], ans=0,
   why="The CED lists copper extracted in Chile among the commodities that contributed to European and American economic advantage under KC-5.1.II.C. Egypt and South Asia appear in the cotton example, China as the destination of opium, and West Africa in the palm oil example of the previous topic's illustrative list."),
 dict(q="The framework gives the expansion of British and French influence in China through the Opium Wars as an illustration of",
   choices=[
     "industrialized states practicing economic imperialism",
     "the establishment of a settler colony",
     "the creation of a new state on the periphery of an empire",
     "a rebellion influenced by religious ideas",
     "the migration of indentured labourers between continents"], ans=0,
   why="The CED prints Britain and France expanding their influence in China through the Opium Wars under its heading for industrialized states practicing economic imperialism, the statement of KC-5.2.I.E. Settler colonies, new states, rebellions and labour migration are the subject of other statements in this unit."),
 dict(q="The framework gives the construction of the Port of Buenos Aires with the support of British firms as an illustration of",
   choices=[
     "businesses within an industrialized state practicing economic imperialism in Latin America",
     "an industrialized state annexing a Latin American territory as a colony",
     "a Latin American state acquiring territory in Europe",
     "the creation of an ethnic enclave by returning migrants",
     "the transfer of a colony from a chartered company to a government"], ans=0,
   why="The CED prints the construction of the Port of Buenos Aires with the support of British firms under its heading for industrialized states practicing economic imperialism, and KC-5.2.I.E names businesses within those states alongside the states themselves and places the practice primarily in Asia and Latin America. The example involves firms and a port, not annexation, enclaves or a colonial transfer."),
 dict(q="An illustrative loan agreement of the period provides that a foreign syndicate will finance and build a railway to a mining district, will operate it for a fixed term, and will take a share of the freight revenue. Situated in the broader context of this topic, the agreement illustrates",
   choices=[
     "businesses of an industrialized state obtaining a lasting economic position in another country",
     "an industrialized state annexing another country as a colony",
     "a producing country obtaining an economic advantage over industrialized states",
     "a rebellion against an imperial administration",
     "the conversion of an export economy into a manufacturing economy"], ans=0,
   why="KC-5.2.I.E names businesses within industrialized states, alongside those states, as the practitioners of economic imperialism, and KC-5.1.II.C describes an organization of trade that gave such firms a distinct economic advantage. A financed, operated and revenue-sharing railway is an economic position of exactly that kind, and involves no annexation, no rebellion and no shift into manufacturing."),
 dict(q="Which statement best expresses what the framework means when it says the trade in some commodities was organized in a particular way?",
   choices=[
     "How the trade was arranged, and not only what was traded, determined who gained most from it",
     "The commodities themselves determined the gains, whatever arrangements were made",
     "The trade was arranged by the producing regions to their own advantage",
     "No arrangement of the trade could affect who gained from it",
     "The organization of the trade was fixed by treaty among the producing regions"], ans=0,
   why="KC-5.1.II.C attributes the distinct economic advantage of merchants and companies based in Europe and the U.S. to the way trade in some commodities was ORGANIZED. That locates the advantage in the arrangements rather than in the goods, and it assigns the advantage to those merchants rather than to the producing regions."),
 dict(q="A student writes that, according to the framework, economic imperialism was practiced primarily in sub-Saharan Africa because palm oil from that region is on the framework's commodity list. The error in this reasoning is that",
   choices=[
     "the regional claim belongs to the statement about economic imperialism, while the palm oil example belongs to a separate statement about commodities and advantage",
     "palm oil is not among the commodities the framework lists at all",
     "the framework names no regions in connection with economic imperialism",
     "the framework says economic imperialism was practiced primarily in Europe",
     "the framework denies that sub-Saharan Africa exported anything in this period"], ans=0,
   why="KC-5.2.I.E is the statement that places economic imperialism primarily in Asia and Latin America; KC-5.1.II.C is a different statement, about trade organized to give European and American merchants an advantage, and the palm oil example is printed under it. Reading one statement's region into the other is the error, not any doubt about palm oil."),
 dict(q="The record below lists five hypothetical shipments, with the region where each good was produced, the region it was shipped to, and the home base of the firm that arranged the shipment. In how many of the shipments is the arranging firm based in Europe or North America?",
   choices=[
     "Four of the five shipments",
     "Two of the five shipments",
     "Three of the five shipments",
     "Five of the five shipments",
     "One of the five shipments"], ans=0,
   table=_T_SHIPMENTS,
   why="Read from the record alone: the arranging firm is based in Western Europe in Records 1, 3 and 4 and in North America in Record 2, which is four; only Record 5's firm is based in Latin America. That concentration is what KC-5.1.II.C means by an advantage held by merchants and companies based in Europe and the U.S."),
 dict(q="Using the same hypothetical shipment record, which is the only shipment in which Western Europe is the region where the good was produced rather than a region receiving it?",
   choices=[
     "Record 4",
     "Record 1",
     "Record 2",
     "Record 3",
     "Record 5"], ans=0,
   table=_T_SHIPMENTS,
   why="Read from the record alone: Western Europe is the destination in Records 1, 3 and 5, and Record 4 is the only row in which Western Europe is the region of production. The other four rows carry goods from South Asia, Latin America or sub-Saharan Africa toward Western Europe or North America, so Record 4 is the one shipment running against the direction KC-5.1.II.C describes."),
 dict(q="In the same hypothetical shipment record, which shipment carries a good produced outside Europe and North America and arranged by a firm based in the region that produced it?",
   choices=[
     "Record 5",
     "Record 1",
     "Record 2",
     "Record 3",
     "Record 4"], ans=0,
   table=_T_SHIPMENTS,
   why="Read from the record alone: Record 5's good is produced in Latin America and the arranging firm is based in Latin America, and Latin America lies outside Europe and North America. Record 4 also has its firm based in its own region of production, but that region is Western Europe, so the stem's two conditions are met by Record 5 alone; in Records 1, 2 and 3 the arranging firm sits in the destination region instead, which is the concentration KC-5.1.II.C describes."),
 dict(q="A student concludes from the same hypothetical record that firms based in producing regions never arranged shipments at all. The record refutes this because",
   choices=[
     "at least one shipment is arranged by a firm based in the region that produced the good",
     "the record does not name the commodities being shipped",
     "the record does not give the value of any shipment",
     "the record covers five shipments rather than fifty",
     "the record does not state the year of any shipment"], ans=0,
   table=_T_SHIPMENTS,
   why="The refutation has to come from the data the student is using, and two rows have the arranging firm based in the region of production: Record 5 in Latin America and Record 4 in Western Europe. The four rejected statements are true of the record but leave the claim standing, and KC-5.1.II.C claims an advantage rather than a monopoly."),
 dict(q="The table below breaks a hypothetical commodity's journey to market into the services it required. Which conclusion is best supported?",
   choices=[
     "Firms based in Europe or North America supplied most of the services that moved the crop, but almost none of the labour that grew it",
     "Firms based in Europe or North America supplied most of the labour that grew the crop and few of the services that moved it",
     "The services were divided evenly between firms based in Europe or North America and firms based elsewhere",
     "Firms based in Europe or North America supplied every service listed in full",
     "The table shows no service in which firms based in Europe or North America held a majority share"], ans=0,
   table=_T_ADVANTAGE,
   why="Read from the table alone: shipping at 88, insurance at 91 and finance at 84 are majority shares, warehousing at 35 is not, and growing and harvesting stands at 2. That pattern is a large share of the moving services and almost none of the growing, which is what KC-5.1.II.C means by an advantage arising from the way a trade is organized, and it rules out an even division, a complete monopoly and an absence of majorities."),
 dict(q="Using the same hypothetical breakdown of services, which figure most directly supports the framework's statement that the ORGANIZATION of a trade could confer an advantage?",
   choices=[
     "The high shares held in shipping, insurance and finance, which are the arrangements by which goods reach a market",
     "The low share held in growing and harvesting, which shows where the crop came from",
     "The share held in warehousing, which is the smallest majority in the table",
     "The number of services the table lists",
     "The fact that the shares are given as percentages"], ans=0,
   table=_T_ADVANTAGE,
   why="KC-5.1.II.C locates the advantage in the way trade was organized. Shipping, insurance and finance are the organizing services, and the table gives their shares as 88, 91 and 84; the growing share reports production rather than organization, warehousing at 35 is not a majority at all, and the row count and units carry no claim."),
 dict(q="An illustrative circular issued to shareholders describes a firm's new operations in a distant country as 'a secure field for capital, with the government there favourably disposed'. Considering its purpose, the circular is best used as evidence of",
   choices=[
     "how the venture was presented to the people being asked to invest in it",
     "the actual profits the venture later earned",
     "the opinions of the distant country's population about the venture",
     "the wages the venture paid to its workers",
     "the volume of goods the venture eventually shipped"], ans=0,
   why="A circular to shareholders is written to reassure and attract capital, so it is direct evidence of the case made to investors. Profits, local opinion, wages and shipping volumes are matters it is not written to report, and KC-5.2.I.E's claim about businesses practicing economic imperialism is not established by any single firm's own prospectus."),
 dict(q="Why does the framework describe the advantage held by European and American merchants as arising from the way trade was organized rather than from the commodities themselves?",
   choices=[
     "Because the same commodity could be traded on different terms, and the terms decided who gained",
     "Because the commodities were of no value to anyone in the producing regions",
     "Because the commodities were manufactured in Europe and the United States",
     "Because no commodity was traded across more than one border",
     "Because the producing regions set the terms of every sale"], ans=0,
   why="KC-5.1.II.C attributes a distinct economic advantage to merchants and companies based in Europe and the U.S. and grounds it in how trade in some commodities WAS ORGANIZED. That is a claim about terms rather than about goods; the commodities are the raw materials of KC-5.1.II.A and were produced outside Europe and the United States."),
 dict(q="How is economic imperialism as this topic describes it related to the state expansion described earlier in the unit?",
   choices=[
     "Both are ways in which industrialized states extended their reach, one through control of territory and one through economic position",
     "Both describe the same process, so the framework's two statements are interchangeable",
     "Economic imperialism replaced state expansion entirely once industrialization began",
     "State expansion occurred only in regions where economic imperialism was absent by rule",
     "Neither is described by the framework as involving industrialized states"], ans=0,
   why="KC-5.2.I.A to KC-5.2.I.D describe shifts in control over territory, while KC-5.2.I.E describes economic imperialism practiced by industrialized states and businesses within them. Both are printed under KC-5.2, the statement that as states industrialized they expanded existing empires and established new colonies and transoceanic relationships, so they are two forms of extended reach rather than one process or two unrelated ones."),
 dict(q="A student claims that the framework treats economic imperialism as the work of governments only. Which part of the framework's wording refutes the claim most directly?",
   choices=[
     "The naming of businesses within industrialized states alongside the states themselves",
     "The naming of Asia and Latin America as the principal regions",
     "The description of the trade in some commodities as organized",
     "The listing of copper among the commodities",
     "The placing of the statement in a unit about industrialization"], ans=0,
   why="KC-5.2.I.E reads that industrialized states AND businesses within those states practiced economic imperialism, so the phrase naming businesses is the refutation. The regions, the organization of trade, the commodity list and the unit's placement are all true of the framework but say nothing about who practiced it."),
 dict(q="An illustrative account reports that a foreign bank's branch in a port city came to handle most of the credit on which the local export trade depended. Within this topic's framework, the account is evidence of",
   choices=[
     "a firm based abroad occupying a position in the organization of a trade",
     "the annexation of the port city by a foreign state",
     "the migration of bank employees between continents",
     "the conversion of the port city into a settler colony",
     "the extraction of a natural resource from the port city"], ans=0,
   why="KC-5.1.II.C attributes the advantage of European and American merchants and companies to the way trade in some commodities was organized, and credit is part of that organization. The account describes no annexation, no migration, no settlement and no extraction."),
 dict(q="Which pair of statements about this topic is consistent with the framework?",
   choices=[
     "Economic imperialism was practiced primarily in Asia and Latin America, and the commodities that gave European and American merchants an advantage came from several regions including Africa",
     "Economic imperialism was practiced primarily in Africa, and every commodity on the framework's list came from Asia",
     "Economic imperialism was practiced primarily in Europe, and the commodities came only from Latin America",
     "Economic imperialism was practiced in no identified region, and the framework lists no commodities",
     "Economic imperialism and the commodity trade were confined to the same single region"], ans=0,
   why="KC-5.2.I.E places economic imperialism primarily in Asia and Latin America; the CED's commodity list under KC-5.1.II.C runs from the Middle East and South Asia to Egypt, sub-Saharan Africa and Chile. Holding the two statements apart is what makes the key correct and every alternative pairing false."),
 dict(q="Learning objective E asks how economic factors contributed to the development of the global economy. Which of the following is an economic factor as this topic presents them?",
   choices=[
     "The terms on which a commodity trade was financed and shipped",
     "The religious beliefs of the population in a producing region",
     "The rank of an imperial state among its rivals",
     "The number of officials an administration posted to a colony",
     "The date on which a colony's borders were fixed"], ans=0,
   why="KC-5.1.II.C makes the organization of trade, including who handled it, the source of a distinct economic advantage, and KC-5.2.I.E names states and businesses as the practitioners of economic imperialism. Beliefs, national rank, staffing levels and boundary dates belong to the cultural and governance statements of this unit rather than to its economic ones."),
 dict(q="Two illustrative sources describe the same commodity trade: an exporting firm's freight and insurance accounts, and a petition from growers complaining of the prices they receive. Read together, the two sources are most useful for",
   choices=[
     "showing how the returns from one trade were divided between those who moved it and those who produced it",
     "establishing which of the two documents was written first",
     "proving that one of the two documents must be a forgery",
     "determining the total population of the producing district",
     "identifying the religion of the firm's directors"], ans=0,
   why="The two documents report the two ends of one trade, which is what makes reading them together informative about the division of the returns; KC-5.1.II.C is a claim about exactly that division. Priority of composition, forgery, population and religion are not questions either document is fitted to answer."),
 dict(q="An illustrative treaty clause obliges one state to admit another state's merchants on fixed terms and to charge them no more than a stated duty. Situated in this topic's context, the clause is best understood as",
   choices=[
     "an arrangement securing favourable terms of trade for merchants of the second state",
     "an arrangement transferring the first state's territory to the second state",
     "an arrangement by which the first state acquires a colony overseas",
     "an arrangement ending all trade between the two states",
     "an arrangement for the migration of workers from one state to the other"], ans=0,
   why="KC-5.1.II.C attributes the advantage of European and American merchants and companies to the way trade was organized, and terms of admission and duty are terms of trade. The clause transfers no territory, creates no colony, ends no trade and moves no workers."),
 dict(q="Why is the framework's claim about economic imperialism placed in a unit about the consequences of industrialization?",
   choices=[
     "Because it is industrialized states and their businesses that the framework names as practicing it",
     "Because industrialization is said to have ended the trade in raw materials",
     "Because the framework treats industrialization as a consequence of economic imperialism rather than a condition of it",
     "Because the unit concerns only the internal history of industrial states",
     "Because economic imperialism is said to have preceded industrialization everywhere"], ans=0,
   why="KC-5.2.I.E names industrialized states and businesses within those states as the practitioners, which is what ties the statement to this unit. KC-5.1.II.A in the same unit has the raw material trade growing rather than ending, and the unit's title places these developments as consequences of industrialization."),
 dict(q="Which question about economic imperialism can be answered from the framework, and which cannot?",
   choices=[
     "Which regions the framework identifies as its principal setting can be answered; how much profit any single firm made cannot",
     "How much profit any single firm made can be answered; which regions the framework identifies cannot",
     "Neither the regions nor the identity of the practitioners can be answered",
     "Both the regions and the terms of every commercial treaty of the period can be answered",
     "Only the year in which the practice began can be answered"], ans=0,
   why="KC-5.2.I.E names the practitioners and places the practice primarily in Asia and Latin America, so those are answerable. Profits, treaty terms and starting dates appear nowhere in this topic, whose examples are printed as illustrations without figures. The anchor carries both clauses because the exact reversal is offered."),
 dict(q="Taking this topic's two statements together, what account of the global economy do they give?",
   choices=[
     "Industrialized states and their businesses extended their economic position abroad, and the way particular trades were organized left the gains concentrated in Europe and the United States",
     "Producing regions extended their economic position abroad, and the way trades were organized left the gains concentrated among them",
     "The gains from trade were divided equally, and no state or firm held any advantage",
     "Long-distance trade in raw materials ceased during the period",
     "The framework identifies neither who practiced economic imperialism nor who gained from the commodity trades"], ans=0,
   why="KC-5.2.I.E gives the practitioners and the principal regions, and KC-5.1.II.C gives the distinct economic advantage held by merchants and companies based in Europe and the U.S. Together those are the key's two clauses; the reversal, an equal division, a cessation of trade and a claim of silence are each contradicted by one or both statements."),
]
