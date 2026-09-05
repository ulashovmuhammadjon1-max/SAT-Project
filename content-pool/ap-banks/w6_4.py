# AP WORLD HISTORY: MODERN 6.4 Global Economic Development from 1750 to 1900
# CED effective Fall 2026, Unit 6 Consequences of Industrialization, c. 1750 to
# c. 1900. Thematic focus ENV, Humans and the Environments: "The environment
# shapes human societies, and as populations grow and change, these populations in
# turn shape their environments."
#
# Unit 6 Learning Objective D: "Explain how various environmental factors
# contributed to the development of the global economy from 1750 to 1900."
# Reasoning process: Continuity and Change. Suggested skill 2.B, explain the point
# of view, purpose, historical situation, and/or audience of a source.
#
# The single historical development this topic prints, in the framework's own words:
#   KC-5.1.II.A  The need for raw materials for factories and increased food
#                supplies for the growing population in urban centers led to the
#                growth of export economies around the world that specialized in
#                commercial extraction of natural resources and the production of
#                food and industrial crops. The profits from these raw materials
#                were used to purchase finished goods.
#
# Illustrative examples the CED prints for this topic, under the heading "Resource
# export economies". These are the only named places and commodities in this module:
#   Cotton production in Egypt; rubber extraction in the Amazon and the Congo
#   basin; the palm oil trade in West Africa; the guano industries in Peru and
#   Chile; meat from Argentina and Uruguay; diamonds from Africa.
#
# WHAT THIS BANK DOES NOT DO. The CED names these export economies and gives no
# tonnage, no price, no date and no company for any of them, so no item asks for
# one. Where an item sorts an example into one of the framework's own two
# categories -- commercial extraction of natural resources, and the production of
# food and industrial crops -- the why states the ground for the sorting, because
# the framework prints the categories and the examples separately and does not
# pair them itself. Every source is UNATTRIBUTED and labelled illustrative, and
# tables are labelled hypothetical with every keyed conclusion recomputable from
# the table alone.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md. Dates are written "1750 to 1900".
TOPIC = ("6.4", "Global Economic Development from", 6)

_T_PORTS = dict(
    headers=["Port economy (hypothetical)", "Leading export by value", "Leading import by value"],
    rows=[["Port economy 1", "Unprocessed fibre", "Woven cloth"],
          ["Port economy 2", "Crude mineral ore", "Machine tools"],
          ["Port economy 3", "Chilled meat", "Manufactured hardware"],
          ["Port economy 4", "Raw gum and latex", "Finished rubber goods"]])

_T_SHARES = dict(
    headers=["Commodity leaving one hypothetical export economy",
             "Share of the economy's export earnings (hypothetical, percent)"],
    rows=[["A single extracted natural resource", "78"],
          ["Foodstuffs", "9"],
          ["Textiles woven in the territory", "6"],
          ["Machinery assembled in the territory", "4"],
          ["All other goods", "3"]])

_T_DECADES = dict(
    headers=["Decade (hypothetical)",
             "Raw fibre exported (thousands of bales)",
             "Finished cloth imported (thousands of bolts)"],
    rows=[["First decade", "40", "22"],
          ["Second decade", "75", "51"],
          ["Third decade", "130", "96"],
          ["Fourth decade", "210", "170"]])

QUESTIONS = [
 dict(q="According to the course framework, which two needs led to the growth of export economies around the world in this period?",
   choices=[
     "The need for raw materials for factories, and the need for increased food supplies for growing urban populations",
     "The need for raw materials for factories, and the need to settle surplus population overseas",
     "The need for increased food supplies, and the need to convert overseas populations to a religion",
     "The need for skilled labour in the colonies, and the need for new sources of tax revenue",
     "The need for military bases overseas, and the need to reduce the size of merchant fleets"], ans=0,
   why="KC-5.1.II.A names exactly two needs: raw materials for factories, and increased food supplies for the growing population in urban centers. Settlement, religious conversion, skilled labour, tax revenue and military bases are not among the causes that statement gives."),
 dict(q="The framework says that the export economies that grew in this period specialized in two kinds of production. They are",
   choices=[
     "commercial extraction of natural resources, and the production of food and industrial crops",
     "the manufacture of machinery, and the refining of imported metals",
     "shipbuilding, and the weaving of cloth for export",
     "the production of finished consumer goods, and their sale in domestic markets",
     "banking services, and the insurance of long-distance cargoes"], ans=0,
   why="KC-5.1.II.A states that export economies grew that specialized in commercial extraction of natural resources and the production of food and industrial crops. Manufacture, refining, shipbuilding, weaving, finished consumer goods, banking and insurance are not what that statement says these economies specialized in."),
 dict(q="The framework describes what was done with the profits earned from these raw materials. It states that",
   choices=[
     "the profits from the raw materials were used to purchase finished goods",
     "the profits from finished goods were used to purchase raw materials",
     "the profits were reinvested entirely in local factory construction",
     "the profits were forbidden by treaty from leaving the territory that earned them",
     "no profits were earned, because the trade was conducted by barter alone"], ans=0,
   why="KC-5.1.II.A's closing sentence reads that the profits from these raw materials were used to purchase finished goods. The reversal is offered as a distractor, and both clauses of the key have to be read together to reject it; the framework says nothing about reinvestment, treaty restrictions or barter."),
 dict(q="An illustrative account describes a district whose farms, once growing a mixture of crops for local consumption, come over several decades to plant almost entirely one crop bound for export. This change is best described as",
   choices=[
     "the growth of an export economy specializing in an industrial crop",
     "the growth of a manufacturing economy specializing in finished goods",
     "the creation of a settler colony on the periphery of an empire",
     "the transfer of a colony from a chartered company to a government",
     "a rebellion against the imperial administration",
     ], ans=0,
   why="KC-5.1.II.A describes the growth of export economies that specialized in the production of food and industrial crops, which is what a district turning from mixed local farming to a single export crop illustrates. Manufacturing, settler colonies, company transfers and rebellions are the subject of other statements in this unit."),
 dict(q="Which of the framework's illustrative resource export economies is an export of food?",
   choices=[
     "Meat from Argentina and Uruguay",
     "Diamonds from Africa",
     "Rubber extraction in the Amazon and the Congo basin",
     "The guano industries in Peru and Chile",
     "Cotton production in Egypt"], ans=0,
   why="KC-5.1.II.A names the production of food among the specializations of these export economies, and of the CED's printed examples meat is the one that is eaten. Diamonds, rubber and guano are extracted natural resources and cotton is grown to be spun rather than consumed as food."),
 dict(q="Which of the framework's illustrative examples belongs to the category of commercial extraction of a natural resource rather than to the production of a crop?",
   choices=[
     "Diamonds from Africa",
     "Cotton production in Egypt",
     "The palm oil trade in West Africa",
     "Meat from Argentina and Uruguay",
     "Grain milled in an imperial capital"], ans=0,
   why="KC-5.1.II.A distinguishes commercial extraction of natural resources from the production of food and industrial crops. Diamonds are dug from the ground rather than grown or raised; cotton and palm oil are crops, meat is a food, and milling in an imperial capital is processing rather than extraction and is not among the CED's examples."),
 dict(q="An illustrative merchant's circular of the period advertises a fertilizer shipped from a Pacific coast to European farms. Within the framework's account of this period, the trade it describes belongs to",
   choices=[
     "the commercial extraction of a natural resource for export",
     "the production of finished goods for export",
     "the transfer of colonial control from a company to a government",
     "the creation of a new state on the periphery of an empire",
     "the migration of labourers between two continents"], ans=0,
   why="KC-5.1.II.A names commercial extraction of natural resources as one of the two specializations of the export economies that grew in this period, and the CED prints the guano industries of Peru and Chile among its examples. Finished goods, colonial transfers, new states and migration are treated in other statements of this unit."),
 dict(q="Why does the framework place the growth of these export economies under the theme of humans and the environment?",
   choices=[
     "Because these economies rested on what particular environments could yield, and reshaped those environments as they grew",
     "Because the framework treats economic history as a branch of physical geography",
     "Because the environment determined which state would govern each territory",
     "Because these economies produced no goods that were traded across borders",
     "Because environmental conditions were identical in every exporting region"], ans=0,
   why="The Humans and the Environments thematic focus states that the environment shapes human societies and that growing and changing populations in turn shape their environments. KC-5.1.II.A describes economies built on extracting natural resources and growing crops, which is that relationship in operation, and learning objective D asks how environmental factors contributed to the global economy."),
 dict(q="The register below records four hypothetical port economies, with the leading export and the leading import of each. What pattern does the register show?",
   choices=[
     "Each economy sends out an unprocessed good and takes in a finished one",
     "Each economy sends out a finished good and takes in an unprocessed one",
     "Each economy sends out and takes in the same kind of good",
     "Two economies export finished goods and two export raw materials",
     "The register records exports but no imports"], ans=0,
   table=_T_PORTS,
   why="Read from the register alone: unprocessed fibre against woven cloth, crude ore against machine tools, chilled meat against manufactured hardware, and raw gum and latex against finished rubber goods. Every row pairs an unprocessed export with a finished import, which is KC-5.1.II.A's closing sentence in a table."),
 dict(q="Using the same hypothetical register of port economies, which conclusion is NOT supported?",
   choices=[
     "At least one of these economies exports goods it has manufactured itself",
     "Every economy listed exports a good in an unprocessed state",
     "Every economy listed imports a good that has been manufactured",
     "The register lists four separate port economies",
     "No economy listed imports an unprocessed good"], ans=0,
   table=_T_PORTS,
   why="Every export in the register is unprocessed and every import is a manufactured good, so no row supports the keyed claim, while each of the four rejected statements can be read directly off the same two columns."),
 dict(q="The table below gives the composition of the export earnings of one hypothetical economy. Which conclusion about that economy is supported?",
   choices=[
     "Its export earnings depend overwhelmingly on a single extracted natural resource",
     "Its export earnings are spread evenly across five kinds of goods",
     "Its export earnings come mainly from textiles woven in the territory",
     "Its export earnings come mainly from machinery assembled in the territory",
     "Its export earnings come mainly from foodstuffs"], ans=0,
   table=_T_SHARES,
   why="Read from the table alone: a single extracted natural resource accounts for 78 percent of export earnings, more than all four other categories combined. That is what KC-5.1.II.A means in calling such economies specialized, and it makes each of the four rejected readings false on the same numbers."),
 dict(q="A student says the same hypothetical economy is a manufacturing economy. Which figure from the table most directly refutes that description?",
   choices=[
     "Textiles and machinery together account for one tenth of export earnings",
     "Foodstuffs account for less than one tenth of export earnings",
     "All other goods account for the smallest share of export earnings",
     "The table lists five categories of export earnings",
     "The shares in the table sum to one hundred percent"], ans=0,
   table=_T_SHARES,
   why="Textiles at 6 percent and machinery at 4 percent are the two manufactured categories in the table, and together they come to 10 percent of export earnings, which is what refutes the description directly. The food share, the residual category, the number of rows and the fact that the shares sum to a whole tell a student nothing about manufacturing."),
 dict(q="The record below reports, for four hypothetical decades in one territory, the raw fibre it exported and the finished cloth it imported. What does the record show?",
   choices=[
     "Both the raw fibre exported and the finished cloth imported rise in every decade",
     "The raw fibre exported rises while the finished cloth imported falls",
     "The finished cloth imported rises while the raw fibre exported falls",
     "Both figures are unchanged across the four decades",
     "The territory imports raw fibre and exports finished cloth"], ans=0,
   table=_T_DECADES,
   why="Read from the record alone: fibre exports run 40, 75, 130 and 210 while cloth imports run 22, 51, 96 and 170, so both columns rise at every step. The record also names fibre as the export and cloth as the import, so the reversed reading is false on the column headings."),
 dict(q="Using the same hypothetical four-decade record, which statement best connects it to the framework's account of export economies?",
   choices=[
     "A territory sending out more raw material over time also took in more finished goods over time",
     "A territory sending out more raw material over time reduced its purchases of finished goods",
     "A territory manufacturing more cloth over time exported less raw fibre",
     "A territory's exports and imports moved in opposite directions throughout",
     "A territory ceased to trade with other economies during the period recorded"], ans=0,
   table=_T_DECADES,
   why="KC-5.1.II.A states that the profits from raw materials were used to purchase finished goods, and the record shows both columns rising together across four decades, which is that relationship over time rather than the opposing movement each rejected option describes."),
 dict(q="An illustrative prospectus written to attract investors describes a territory as offering 'inexhaustible supplies of a raw material for which the mills of Europe are hungry'. Considering its purpose, this source is best used as evidence of",
   choices=[
     "how the territory's resources were presented to people whose money was being sought",
     "the actual quantity of the raw material the territory contained",
     "the wages paid to workers who gathered the raw material",
     "the opinions of the territory's own inhabitants about the trade",
     "the price the raw material eventually fetched in Europe"], ans=0,
   why="Suggested skill 2.B asks students to explain how a source's purpose and audience bear on its interpretation. A prospectus exists to attract investment, so it is direct evidence of the case made to investors and not of quantities, wages, local opinion or later prices, none of which it is written to report."),
 dict(q="Two illustrative sources describe the same export trade: a shipping company's freight ledger and a travel writer's published account of the same port. The most useful way to use them together is to recognize that",
   choices=[
     "the ledger was compiled to keep a commercial record and the published account to interest readers, so each is reliable about different things",
     "the ledger must be false because commercial records are always altered",
     "the published account must be false because it was written for money",
     "the two sources cannot be compared because they were made for different reasons",
     "whichever source is longer is the more reliable of the two"], ans=0,
   why="Suggested skill 2.B makes purpose and audience central to interpretation. A ledger kept for internal commercial use and a narrative written to interest readers answer different questions well, which is a reason to use them for different things rather than to declare either false or to refuse the comparison."),
 dict(q="An illustrative report by an official of the importing country praises an export economy for its 'orderly and rising trade'. What does the report's point of view most importantly limit?",
   choices=[
     "Its usefulness as evidence about how the trade was experienced by the people producing the goods",
     "Its usefulness as evidence that the trade existed at all",
     "Its usefulness as evidence of what the official's own government valued",
     "Its usefulness as a document written during the period it describes",
     "Its usefulness as an indication of which goods were traded"], ans=0,
   why="Suggested skill 2.B asks how a source's point of view affects its interpretation. An official of the country receiving the goods writes from the importing side, so his praise is good evidence of what his government valued and poor evidence of the producers' experience, which he is not reporting."),
 dict(q="The reasoning process for this topic is continuity and change. Applied to a territory that becomes a resource export economy in this period, that reasoning asks a student to identify",
   choices=[
     "what about the territory's production changed and what carried on unchanged",
     "only the changes, since continuities are not part of historical reasoning",
     "only the continuities, since changes belong to a different reasoning process",
     "the exact year in which the change began",
     "which of two territories mattered more to the imperial economy"], ans=0,
   why="The CED names continuity and change as the reasoning process for topic 6.4, and that reasoning is the joint identification of what altered and what persisted. It is not a demand for a precise date, nor a ranking of territories, nor an instruction to attend to one half of the pair alone."),
 dict(q="An illustrative account of a territory reports that its farmers continued to use the same tools and the same field boundaries while the crop they planted changed from food for local sale to a fibre bound for export. Reasoning about continuity and change, a student should conclude that",
   choices=[
     "the technique of cultivation persisted while the destination and purpose of the crop changed",
     "both the technique of cultivation and the destination of the crop changed together",
     "both the technique of cultivation and the destination of the crop stayed the same",
     "the technique of cultivation changed while the destination of the crop persisted",
     "no conclusion about continuity or change can be drawn from an agricultural account"], ans=0,
   why="The account states unchanged tools and boundaries alongside a changed crop and a changed destination, so the continuity is in technique and the change is in what is grown and for whom. The reversed reading is offered as a distractor, and both clauses of the key are needed to reject it. KC-5.1.II.A is the process the account illustrates."),
 dict(q="Why does the framework connect the growth of urban populations to the growth of export economies on the other side of the world?",
   choices=[
     "Because feeding a growing urban population required food supplies that were increasingly obtained from distant export economies",
     "Because urban populations emigrated in large numbers to the exporting territories",
     "Because urban populations financed the construction of factories in the exporting territories",
     "Because exporting territories were governed by the cities that consumed their produce",
     "Because urban populations consumed no food that was grown outside their own region"], ans=0,
   why="KC-5.1.II.A names increased food supplies for the growing population in urban centers as one of the two needs that led to the growth of export economies specializing in food production. Emigration, factory finance and governance are not what that statement asserts, and the last option is the denial of it."),
 dict(q="Which statement most accurately describes what the framework means by calling these economies specialized?",
   choices=[
     "Their production was concentrated on a narrow range of goods sold outside the territory",
     "Their production covered every kind of good the territory's inhabitants required",
     "They produced only goods that were consumed within the territory",
     "They employed only workers trained in a single craft",
     "They traded with only one other territory each"], ans=0,
   why="KC-5.1.II.A speaks of export economies that specialized in commercial extraction of natural resources and the production of food and industrial crops, and pairs that with profits used to purchase finished goods. Concentration on a narrow range of exports, with other goods bought in, is what that pairing describes; the framework says nothing about the training of workers or the number of trading partners."),
 dict(q="A student claims that the growth of export economies in this period was unconnected to industrial production anywhere. The framework contradicts this by stating that",
   choices=[
     "the need for raw materials for factories was one of the causes of their growth",
     "factories were built in each exporting territory before its exports began",
     "industrial production ceased entirely during the period covered by the unit",
     "raw materials were consumed only in the territories that produced them",
     "no finished goods were purchased anywhere with the profits of these exports"], ans=0,
   why="KC-5.1.II.A opens by naming the need for raw materials for factories as one of the two causes of the growth of export economies, which is a direct connection between the two. It does not claim that factories were built in the exporting territories, and it says the opposite of the last two options."),
 dict(q="An illustrative petition from merchants in an exporting territory asks their government to build a railway to the interior so that produce can reach the coast. The petition is evidence of",
   choices=[
     "an effort to move a bulky export more cheaply to the point where it leaves the territory",
     "an effort to establish manufacturing industries in the interior",
     "an effort to prevent the export of the territory's produce",
     "an effort to convert the interior population to the merchants' religion",
     "an effort to establish a new state on the periphery of an empire"], ans=0,
   why="KC-5.1.II.A describes export economies specializing in extraction and in food and industrial crops, and a request for transport from the interior to the coast is aimed at getting such produce out of the territory. The petition asks for no factory, no prohibition, no mission and no new state."),
 dict(q="What did the export economies described in this topic have in common, whether they extracted a mineral, tapped a tree or raised livestock?",
   choices=[
     "Each sold abroad what its environment could yield and bought finished goods with the proceeds",
     "Each manufactured the finished goods that its own population consumed",
     "Each was owned and worked by the government of the importing country",
     "Each traded only with territories on its own continent",
     "Each ceased production before the end of the period"], ans=0,
   why="KC-5.1.II.A groups commercial extraction of natural resources with the production of food and industrial crops as the specializations of these export economies and states that the profits from these raw materials were used to purchase finished goods. Ownership, continental restriction and cessation are not asserted anywhere in that statement."),
 dict(q="Which question about a resource export economy of this period can be answered from the framework, and which cannot?",
   choices=[
     "What kinds of production such economies specialized in can be answered; how many tons any one of them shipped cannot",
     "How many tons any one of them shipped can be answered; what kinds of production they specialized in cannot",
     "Neither the specializations nor the use made of the profits can be answered",
     "Both the specializations and the wages paid in each territory can be answered",
     "Only the year in which each export trade began can be answered"], ans=0,
   why="KC-5.1.II.A names the specializations and states what the profits were used for, so those are answerable from the framework. Tonnages, wages and starting dates are printed nowhere in this topic, whose examples are listed as illustrations without figures. The anchor carries both clauses because the exact reversal is offered."),
 dict(q="An illustrative newspaper item in an importing country reports that the price of a colonial foodstuff has fallen and that consumption of it in the cities has risen. Considering the historical situation of this source, it is most useful as evidence about",
   choices=[
     "conditions in the market where the foodstuff was sold rather than in the territory that produced it",
     "the methods used to produce the foodstuff in the exporting territory",
     "the wages earned by the workers who harvested the foodstuff",
     "the environmental conditions of the exporting territory",
     "the political arrangements governing the exporting territory"], ans=0,
   why="Suggested skill 2.B asks how a source's historical situation bears on its interpretation. This item is written in and about the consuming market, so it reports prices and consumption there; production methods, wages, environment and government in the exporting territory are all outside what it observes."),
 dict(q="How does this topic's account of the global economy relate to the topic on state expansion in the same unit?",
   choices=[
     "It describes the economic activity of the period, while the other describes how state power over territory shifted",
     "It describes the same processes as the other topic under different names",
     "It denies that any state exercised power over an exporting territory",
     "It concerns a period entirely different from the one the other topic covers",
     "It replaces the other topic's account with an economic explanation of every event"], ans=0,
   why="KC-5.1.II.A is a statement about export economies and the purchase of finished goods, while KC-5.2.I and KC-5.2.II are statements about the shifting of state power. Both sit in Unit 6, whose span is c. 1750 to c. 1900, so the two are separate strands of the same period rather than the same claim or a replacement for it."),
 dict(q="An illustrative company report describes a territory's output rising sharply after new land is cleared and planted with a single crop for export. Reasoning from the framework's thematic focus, a student should note that",
   choices=[
     "a growing and changing population reshaped the environment it depended on",
     "the environment was unaffected by anything the population did to it",
     "the population's activities were determined entirely by the environment",
     "clearing land has no connection to the growth of an export economy",
     "the framework treats environmental change as belonging to a later period"], ans=0,
   why="The Humans and the Environments focus states that the environment shapes human societies and that populations as they grow and change in turn shape their environments. Clearing land to plant an export crop is the second half of that sentence, and KC-5.1.II.A is the economic process it serves."),
 dict(q="A historian wishes to test whether a territory's economy became more specialized over a period of decades. Which evidence would serve best?",
   choices=[
     "The share of the territory's export earnings coming from its largest export, measured at several dates",
     "The total value of the territory's exports in a single year",
     "The number of ships calling at the territory's main port in a single year",
     "The population of the territory's largest city at the end of the period",
     "The number of officials the imperial state posted to the territory"], ans=0,
   why="Specialization is a claim about concentration, so testing it requires a measure of concentration compared across time, which is what a repeated share of earnings from the largest export provides. A single year's total, a ship count, a city population and an official headcount measure size or administration rather than concentration."),
 dict(q="Taking KC-5.1.II.A as a whole, what sequence does it describe?",
   choices=[
     "Industrial and urban demand grew, export economies specialized to meet it, and their earnings bought finished goods",
     "Export economies specialized first, and industrial and urban demand grew afterwards in response",
     "Finished goods were exchanged for other finished goods, with raw materials playing no part",
     "Urban populations shrank, and export economies grew because demand at home had disappeared",
     "Industrial demand grew but produced no change in production anywhere outside the industrial states"], ans=0,
   why="KC-5.1.II.A runs in that order: the need for raw materials for factories and increased food supplies for growing urban populations LED TO the growth of specialized export economies, and the profits from those raw materials were then used to purchase finished goods. The reversal of the first two stages is offered as a distractor, and both clauses of the key are needed to reject it."),
]
