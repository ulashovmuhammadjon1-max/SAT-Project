# AP WORLD HISTORY: MODERN 6.6 Causes of Migration in an Interconnected World
# CED effective Fall 2026, Unit 6 Consequences of Industrialization, c. 1750 to
# c. 1900. This topic prints TWO thematic focuses and two learning objectives, and
# the module keeps them apart because they are the topic's own division:
#   ENV, Humans and the Environments: "The environment shapes human societies, and
#     as populations grow and change, these populations in turn shape their
#     environments."  -- Unit 6 Learning Objective F: "Explain how various
#     environmental factors contributed to the development of varied patterns of
#     migration from 1750 to 1900."
#   ECN, Economics Systems: "As societies develop, they affect and are affected by
#     the ways that they produce, exchange, and consume goods and services."
#     -- Unit 6 Learning Objective G: "Explain how various economic factors
#     contributed to the development of varied patterns of migration from 1750 to
#     1900."
# Reasoning process: Causation. Suggested skill 5.B, explain how a historical
# development or process relates to another historical development or process.
#
# The historical developments this topic prints, in the framework's own words:
#   KC-5.4.I     Migration in many cases was influenced by changes in demographics
#                in both industrialized and unindustrialized societies that
#                presented challenges to existing patterns of living.
#   KC-5.4.I.B   Because of the nature of new modes of transportation, both internal
#                and external migrants increasingly relocated to cities. This
#                pattern contributed to the significant global urbanization of the
#                19th century. The new methods of transportation also allowed for
#                many migrants to return, periodically or permanently, to their home
#                societies.
#   KC-5.4.II.A  Many individuals chose freely to relocate, often in search of work.
#   KC-5.4.II.B  The new global capitalist economy continued to rely on coerced and
#                semicoerced labor migration, including enslavement Chinese and
#                Indian indentured servitude, and convict labor.
#
# A NOTE ON KC-5.4.II.B AS THE CED PRINTS IT. The extracted text reads "including
# enslavement Chinese and Indian indentured servitude, and convict labor" -- a comma
# is missing after "enslavement" in the source PDF, and the list is plainly the
# three items enslavement, Chinese and Indian indentured servitude, and convict
# labor. No item in this module keys on the NUMBER of forms listed, because that is
# the one reading the missing comma could disturb; items key only on whether a named
# form appears in that sentence, which the punctuation cannot change.
#
# Illustrative examples the CED prints for this topic, under its own two headings.
# These are the only named groups in this module, and every item that uses one asks
# which HEADING the framework prints it under, never what any group did:
#   Return of migrants: Japanese agricultural workers in the Pacific; Lebanese
#     merchants in the Americas; Italian industrial workers in Argentina.
#   Migrants: Irish to the United States; British engineers and geologists to South
#     Asia and Africa.
#
# WHAT THIS BANK DOES NOT DO. The CED gives no number of migrants, no date, no
# route, no wage and no law for any of these groups, so no item asks for one. Every
# source is UNATTRIBUTED and labelled illustrative; tables are labelled hypothetical
# and every keyed conclusion is recomputable from the table alone.
#
# DIRECTION IS THE DEFECT THIS TOPIC INVITES. KC-5.4.I.B runs transportation to
# cities to urbanization; KC-5.4.I runs demographic change to migration; the
# illustrative examples run from a named origin to a named destination. Reversing
# any of those reads perfectly well, so wherever a reversal is offered as a
# distractor the anchor in verify_w6_6.py carries BOTH clauses.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md. Dates are written "1750 to 1900".
TOPIC = ("6.6", "Causes of Migration in an Interconnected World", 6)

_T_STREAMS = dict(
    headers=["Migration stream (hypothetical)",
             "People leaving in one decade (thousands)",
             "People returning to the home society in the same decade (thousands)"],
    rows=[["Stream 1", "120", "44"],
          ["Stream 2", "90", "31"],
          ["Stream 3", "60", "9"],
          ["Stream 4", "200", "86"]])

_T_SETTLE = dict(
    headers=["Kind of place in which one hypothetical stream of migrants settled",
             "Migrants settling there (thousands)"],
    rows=[["Cities of more than one hundred thousand people", "148"],
          ["Towns smaller than that", "42"],
          ["Rural districts", "26"]])

_T_REGISTER = dict(
    headers=["Category recorded in one hypothetical port register",
             "Departures recorded in one year (thousands)"],
    rows=[["People travelling at their own expense in search of work", "121"],
          ["People travelling under contracts of indenture", "58"],
          ["People transported under sentence of a court", "17"],
          ["People moved under conditions of enslavement", "9"]])

_T_ARRIVALS = dict(
    headers=["Origin of migrants arriving in one hypothetical city",
             "Arrivals in one decade (thousands)"],
    rows=[["Rural districts of the same country", "96"],
          ["Other regions of the same country", "38"],
          ["Countries overseas", "71"]])

QUESTIONS = [
 dict(q="According to the course framework, migration in many cases was influenced by changes in demographics. In which societies?",
   choices=[
     "In both industrialized and unindustrialized societies",
     "In industrialized societies only",
     "In unindustrialized societies only",
     "In societies that had abolished coerced labour only",
     "In no society that the framework identifies"], ans=0,
   why="KC-5.4.I states that migration in many cases was influenced by changes in demographics in BOTH industrialized and unindustrialized societies. Confining the demographic change to one side of that pair, or to societies defined by their labour law, is what each rejected option does."),
 dict(q="The framework says those demographic changes did something to the way people were already living. What does it say they presented?",
   choices=[
     "Challenges to existing patterns of living",
     "An end to migration of every kind",
     "A uniform improvement in living standards everywhere",
     "A prohibition on movement between countries",
     "A return of every migrant to the society of origin"], ans=0,
   why="KC-5.4.I's own wording is that changes in demographics presented challenges to existing patterns of living. The framework does not say those changes ended migration, improved living standards uniformly, prohibited movement or returned every migrant, and the last option confuses this statement with KC-5.4.I.B's account of return."),
 dict(q="KC-5.4.I.B connects a technical development to where migrants went. Which statement gives that connection as the framework gives it?",
   choices=[
     "New modes of transportation led both internal and external migrants increasingly to relocate to cities",
     "The growth of cities led to the development of new modes of transportation",
     "New modes of transportation led migrants increasingly to leave cities for rural districts",
     "New modes of transportation ended the movement of internal migrants altogether",
     "The growth of cities ended the movement of external migrants altogether"], ans=0,
   why="KC-5.4.I.B reads that because of the nature of new modes of transportation, both internal and external migrants increasingly relocated to cities. The cause and the effect are reversed in one of the rejected options and the direction of the move is reversed in another, so both clauses of the key have to be read together."),
 dict(q="The framework says the pattern of migrants relocating to cities contributed to something larger. To what?",
   choices=[
     "The significant global urbanization of the 19th century",
     "The depopulation of cities across the 19th century",
     "The end of long-distance travel in the 19th century",
     "The abolition of coerced labour migration in the 19th century",
     "The equalization of population between countryside and city"], ans=0,
   why="KC-5.4.I.B states that this pattern contributed to the significant global urbanization of the 19th century. Depopulation is its opposite, and the end of travel, the abolition of coerced labour and an equalization of population are asserted nowhere in that statement."),
 dict(q="What else does the framework say the new methods of transportation made possible?",
   choices=[
     "They allowed many migrants to return, periodically or permanently, to their home societies",
     "They made a migrant's return to the home society impossible",
     "They required every migrant to return to the home society within a fixed term",
     "They allowed migrants to travel only within their own country",
     "They allowed only merchants, and no other migrants, to travel"], ans=0,
   why="KC-5.4.I.B's closing sentence is that the new methods of transportation also allowed for many migrants to return, periodically or permanently, to their home societies. Allowing a return is not requiring one and is the opposite of preventing one, and the statement places no limit on who could travel."),
 dict(q="The framework makes a statement about individuals who moved by their own decision. What does it say about them?",
   choices=[
     "Many individuals chose freely to relocate, often in search of work",
     "Few individuals had any choice about relocating in this period",
     "Individuals who relocated freely were seeking religious instruction rather than work",
     "Individuals relocated freely only within the borders of their own country",
     "Individuals who relocated freely did so without regard to where work could be found"], ans=0,
   why="KC-5.4.II.A states that many individuals chose freely to relocate, often in search of work. The search for work is part of that sentence, so an option removing the work motive or replacing it with another contradicts it, as does an option denying that free choice was common."),
 dict(q="The framework describes what the new global capitalist economy continued to rely on in the movement of labour. What was it?",
   choices=[
     "Coerced and semicoerced labour migration",
     "Freely chosen labour migration alone",
     "The end of all long-distance labour migration",
     "Labour migration organized entirely by the societies that sent the workers",
     "Labour migration confined to the country in which each worker was born"], ans=0,
   why="KC-5.4.II.B states that the new global capitalist economy continued to rely on coerced and semicoerced labor migration. The word continued matters: the framework is describing a reliance that persisted, which is the opposite of the ending or the confinement each rejected option describes."),
 dict(q="Which of the following is NOT among the forms of coerced or semicoerced labour migration that the framework names in this topic?",
   choices=[
     "Conscription of soldiers for service in overseas garrisons",
     "Enslavement",
     "Chinese indentured servitude",
     "Indian indentured servitude",
     "Convict labour"], ans=0,
   why="KC-5.4.II.B names enslavement, Chinese and Indian indentured servitude, and convict labor as the forms the new global capitalist economy continued to rely on. Military conscription for overseas garrisons appears nowhere in that sentence or in this topic, which is what makes it the item the framework does not name."),
 dict(q="Under which of the framework's two illustrative headings does it print Japanese agricultural workers in the Pacific?",
   choices=[
     "The heading Return of migrants",
     "The heading Migrants",
     "The heading Migrant ethnic enclaves",
     "The heading Regulation of immigrants",
     "The heading Resource export economies"], ans=0,
   why="The CED prints Japanese agricultural workers in the Pacific under the heading Return of migrants in topic 6.6, alongside Lebanese merchants in the Americas and Italian industrial workers in Argentina. The CED prints that heading on the topic 6.6 page beside KC-5.4.I.B, the statement that new methods of transportation allowed many migrants to return. Migrant ethnic enclaves and the regulation of immigrants are headings in topic 6.7, and resource export economies is a heading in topic 6.4."),
 dict(q="The framework's illustrative list of returning migrants includes merchants from the eastern Mediterranean. To which region does it say they went?",
   choices=[
     "The Americas",
     "South Asia",
     "West Africa",
     "The Pacific",
     "Australia"], ans=0,
   why="The CED prints Lebanese merchants in the Americas under its heading Return of migrants for topic 6.6. That list is printed beside KC-5.4.I.B, the statement about return. The Pacific belongs to the Japanese agricultural workers in the same list, and South Asia, West Africa and Australia appear in other topics of this unit rather than in this example."),
 dict(q="Italian industrial workers in Argentina appear in this topic's illustrative examples. What does the framework use them to illustrate?",
   choices=[
     "The return of migrants to their home societies",
     "The creation of an ethnic enclave in a receiving society",
     "The regulation of immigrants by a receiving state",
     "The growth of a resource export economy",
     "The practice of economic imperialism by an industrialized state"], ans=0,
   why="The CED prints Italian industrial workers in Argentina under the heading Return of migrants in topic 6.6, and KC-5.4.I.B is the statement that new methods of transportation allowed many migrants to return periodically or permanently. Enclaves and immigration regulation are topic 6.7's headings, export economies belong to topic 6.4 and economic imperialism to topic 6.5."),
 dict(q="One of this topic's illustrative examples of migrants concerns engineers and geologists. How does the framework describe their movement?",
   choices=[
     "British engineers and geologists going to South Asia and Africa",
     "South Asian and African engineers and geologists going to Britain",
     "British engineers and geologists going to the Americas",
     "South Asian engineers and geologists going to Africa",
     "African engineers and geologists going to South Asia"], ans=0,
   why="The CED prints British engineers and geologists to South Asia and Africa under its heading Migrants for topic 6.6, beside KC-5.4.II.A and KC-5.4.II.B. Origin and destination are the whole content of the example and the reversal is offered as a distractor, so both clauses of the key are needed to settle it."),
 dict(q="Where does the framework place the Irish who went to the United States in its illustrative lists for this topic?",
   choices=[
     "Among migrants",
     "Among returning migrants",
     "Among migrant ethnic enclaves",
     "Among states regulating immigration",
     "Among resource export economies"], ans=0,
   why="The CED prints Irish to the United States under the heading Migrants in topic 6.6, while its Return of migrants heading names the Japanese, Lebanese and Italian examples. That heading is printed beside KC-5.4.II.A, the statement that many individuals chose freely to relocate in search of work. The Irish in North America are printed again in topic 6.7 under migrant ethnic enclaves, which is a different topic's list and a different claim."),
 dict(q="An illustrative letter sent home by an emigrant, quoted here without attribution, reports that 'wages at the works here are three times what they were at home, and a man may choose his employer'. Within this topic's framework, the letter best illustrates",
   choices=[
     "an individual choosing freely to relocate in search of work",
     "an individual moved under a contract of indenture",
     "an individual transported under sentence of a court",
     "an individual relocating for reasons unconnected with employment",
     "a state directing the movement of its population"], ans=0,
   why="KC-5.4.II.A states that many individuals chose freely to relocate, often in search of work, and a letter reporting higher wages and a choice of employer describes exactly that motive. Indenture and transportation under sentence belong to the coerced and semicoerced forms of KC-5.4.II.B, and neither the absence of a work motive nor state direction fits what the letter says."),
 dict(q="An illustrative contract of the period binds a labourer to work for a single employer overseas for a term of years, the cost of the passage being advanced and recovered from wages. Within this topic's framework, the contract belongs to",
   choices=[
     "the coerced and semicoerced labour migration the framework says the global capitalist economy relied on",
     "the free relocation in search of work the framework describes separately",
     "the return migration the framework attributes to new methods of transportation",
     "the demographic change the framework says presented challenges to existing patterns of living",
     "the urbanization the framework attributes to migrants relocating to cities"], ans=0,
   why="KC-5.4.II.B states that the new global capitalist economy continued to rely on coerced and semicoerced labor migration, including indentured servitude, and a term bound to one employer with the passage recovered from wages is an arrangement of that kind. KC-5.4.II.A's free relocation, KC-5.4.I.B's return and urbanization and KC-5.4.I's demographic change are each a different statement."),
 dict(q="An illustrative shipping advertisement of the period offers a fare out and a fare home at a reduced combined rate, and notes that the crossing now takes a fraction of the time it once did. This source most directly supports which of the framework's claims?",
   choices=[
     "That new methods of transportation allowed many migrants to return to their home societies",
     "That new methods of transportation prevented migrants from ever returning",
     "That migrants were compelled by law to purchase a return passage",
     "That demographic change presented challenges to existing patterns of living",
     "That the global capitalist economy relied on coerced labour migration"], ans=0,
   why="KC-5.4.I.B states that the new methods of transportation allowed for many migrants to return, periodically or permanently, to their home societies, and a cheaper, faster round passage is the practical form of that possibility. The advertisement shows no compulsion, and demographic change and coerced labour are separate statements it does not speak to."),
 dict(q="An illustrative parish register from a rural district records that holdings are being divided among more heirs each generation and that most young adults leave the district on reaching working age. Within this topic's framework, the register best illustrates",
   choices=[
     "a change in demographics presenting a challenge to an existing pattern of living",
     "a state regulating the flow of people across its borders",
     "an economy relying on convict labour",
     "the creation of an ethnic enclave in a receiving society",
     "the return of migrants to their home society"], ans=0,
   why="KC-5.4.I states that migration in many cases was influenced by changes in demographics that presented challenges to existing patterns of living, and a district whose holdings will no longer support its rising generation is such a challenge. Border regulation and enclaves belong to topic 6.7, convict labour to KC-5.4.II.B and return to KC-5.4.I.B."),
 dict(q="An illustrative court record of the period orders that a convicted person be transported overseas and set to labour there for a term. Which of the framework's statements does this source illustrate?",
   choices=[
     "That the global capitalist economy continued to rely on convict labour among other coerced forms",
     "That many individuals chose freely to relocate in search of work",
     "That new methods of transportation allowed migrants to return home",
     "That migrants increasingly relocated to cities",
     "That receiving societies always welcomed the migrants who arrived"], ans=0,
   why="KC-5.4.II.B names convict labor among the coerced and semicoerced forms of labour migration that the new global capitalist economy continued to rely on, and a sentence of transportation to labour is that form exactly. Free relocation, return and urbanization are separate statements, and the last option is contradicted by KC-5.4.III.C in the next topic."),
 dict(q="The record below reports, for four hypothetical migration streams, how many people left in one decade and how many returned to the home society in the same decade. Which stream returned the largest share of those who left?",
   choices=[
     "Stream 4",
     "Stream 1",
     "Stream 2",
     "Stream 3",
     "The record does not allow the shares to be compared"], ans=0,
   table=_T_STREAMS,
   why="Read from the record alone: Stream 4 returns 86 of the 200 who left, which is above two in five, while Stream 1 returns 44 of 120, Stream 2 returns 31 of 90 and Stream 3 returns 9 of 60. Both columns are given for every stream, so the shares can be compared, and KC-5.4.I.B is the statement about return that the record illustrates."),
 dict(q="Using the same hypothetical record of four migration streams, which conclusion is supported?",
   choices=[
     "Every stream recorded some return migration, and the share returning differed from stream to stream",
     "No stream recorded any return migration",
     "Every stream returned more people than it sent",
     "The stream that sent the most people returned the smallest share of them",
     "The share returning was the same in every stream"], ans=0,
   table=_T_STREAMS,
   why="Read from the record alone: all four streams show returns, and the shares run from 9 of 60 up to 86 of 200, so they are neither absent, nor equal, nor larger than the outward flow. The stream sending the most also returns the largest share, which is what makes that reading false, and KC-5.4.I.B says the new methods of transportation allowed many migrants to return rather than all or none."),
 dict(q="The table below records where the migrants in one hypothetical stream settled. Which conclusion does it support?",
   choices=[
     "Close to seven in every ten of these migrants settled in the largest cities",
     "Close to seven in every ten of these migrants settled in rural districts",
     "These migrants divided themselves evenly among the three kinds of place",
     "Fewer than half of these migrants settled in the largest cities",
     "The record shows no migrant settling outside a city"], ans=0,
   table=_T_SETTLE,
   why="Read from the table alone: 148 of the 216 thousand settlers went to cities of more than one hundred thousand people, which is close to seven in ten, against 42 in smaller towns and 26 in rural districts. That is the pattern KC-5.4.I.B describes when it says migrants increasingly relocated to cities and that this contributed to significant global urbanization."),
 dict(q="Which conclusion about the same hypothetical settlement record is NOT supported?",
   choices=[
     "Rural districts received more of these migrants than the largest cities did",
     "The largest cities received more than half of these migrants",
     "Rural districts received the smallest number of the three kinds of place",
     "The record distinguishes three kinds of place",
     "Smaller towns received more of these migrants than rural districts did"], ans=0,
   table=_T_SETTLE,
   why="The largest cities take 148 thousand against 26 thousand in rural districts, so the keyed statement is the one the record contradicts, while each rejected statement reads directly off the same column: cities above half the total, rural districts the smallest entry, three kinds of place listed, and towns at 42 above rural at 26. KC-5.4.I.B is the statement about relocation to cities that the record illustrates."),
 dict(q="The register below records the categories under which departures from one hypothetical port were entered in a single year. Which conclusion is best supported?",
   choices=[
     "The register records both people relocating freely in search of work and people moving under coerced or semicoerced arrangements, with the freely travelling group the largest single category",
     "The register records only people relocating freely in search of work",
     "The register records only people moving under coerced or semicoerced arrangements",
     "The register records the same number of departures in each of its categories",
     "The register records no departures at all in the year it covers"], ans=0,
   table=_T_REGISTER,
   why="Read from the register alone: 121 thousand travel at their own expense in search of work, which is the largest single entry, while indenture at 58, court sentence at 17 and enslavement at 9 are coerced or semicoerced arrangements. KC-5.4.II.A and KC-5.4.II.B are both statements of this topic, and the register shows the two side by side rather than one to the exclusion of the other."),
 dict(q="A student reading the same hypothetical port register concludes that coerced and semicoerced arrangements had disappeared by the year it covers. Which feature of the register refutes that conclusion?",
   choices=[
     "Three of its four categories describe coerced or semicoerced arrangements, and together they account for 84 thousand departures",
     "The register lists four categories in all",
     "The largest single category is people travelling at their own expense",
     "The register does not name the destination of any departure",
     "The register gives its figures in thousands"], ans=0,
   table=_T_REGISTER,
   why="The refutation has to come from the data the student is using: indenture at 58, court sentence at 17 and enslavement at 9 come to 84 thousand departures, which is not a disappearance. The four rejected statements are true of the register and leave the claim standing, and KC-5.4.II.B says the new global capitalist economy CONTINUED to rely on these forms."),
 dict(q="The table below records where the migrants arriving in one hypothetical city during a decade had come from. Which conclusion does it support?",
   choices=[
     "The city drew migrants both from within its own country and from overseas, with roughly one in three arriving from overseas",
     "The city drew migrants both from within its own country and from overseas, with roughly one in three arriving from within its own country",
     "The city drew migrants only from within its own country",
     "The city drew migrants only from countries overseas",
     "The city recorded no arrivals from any origin during the decade"], ans=0,
   table=_T_ARRIVALS,
   why="Read from the table alone: 96 and 38 thousand arrive from within the same country and 71 thousand from overseas, so of 205 thousand arrivals roughly one in three comes from abroad and two in three from within. KC-5.4.I.B says that BOTH internal and external migrants increasingly relocated to cities, and the reversed proportion is offered as a distractor, so both clauses of the key are needed."),
 dict(q="Learning objective F asks about environmental factors and learning objective G about economic factors. What does the pairing of the two tell a student about this topic?",
   choices=[
     "That the framework treats patterns of migration in this period as arising from more than one kind of cause",
     "That the framework treats environmental causes as the only real causes of migration",
     "That the framework treats economic causes as the only real causes of migration",
     "That the framework treats the two kinds of cause as describing different periods",
     "That the framework denies that migration in this period had any identifiable cause"], ans=0,
   why="The CED prints two learning objectives for topic 6.6: Learning Objective F, how various environmental factors, and Learning Objective G, how various economic factors contributed to the development of varied patterns of migration from 1750 to 1900. Printing both is what shows the framework treating the causes as plural rather than assigning them to one kind, one period or none."),
 dict(q="The reasoning process for this topic is causation, and the suggested skill asks how one historical development relates to another. Applied to KC-5.4.I.B, that reasoning asks a student to explain",
   choices=[
     "how a change in transportation bore on where migrants settled and on whether they could go home",
     "only where migrants settled, since the means of travel is not a historical development",
     "only the means of travel, since where migrants settled belongs to a different topic",
     "the exact year in which each new mode of transportation came into use",
     "which of two migration streams mattered more to the receiving society"], ans=0,
   why="KC-5.4.I.B links new modes of transportation to relocation to cities, to global urbanization and to the possibility of return, and suggested skill 5.B asks how one historical development relates to another. Attending to one end of that link alone is not the relation, and the framework prints no dates for the modes of transportation and no ranking of streams."),
 dict(q="The unit review states that migration patterns changed dramatically and the numbers of migrants increased significantly. What does the framework give as the setting for that change?",
   choices=[
     "The emergence of transoceanic empires and of a global capitalist economy",
     "The disappearance of transoceanic empires and the closing of world markets",
     "A general fall in the population of every industrialized society",
     "The prohibition of long-distance travel by most states",
     "A decision by receiving societies to admit migrants without restriction"], ans=0,
   why="KC-5.4, printed in this unit's review, reads that as a result of the emergence of transoceanic empires and a global capitalist economy, migration patterns changed dramatically and the numbers of migrants increased significantly. Each rejected option asserts the opposite of one clause of that sentence, and the last is contradicted by KC-5.4.III.C in the next topic."),
 dict(q="Which question about migration in this period can be answered from the framework, and which cannot?",
   choices=[
     "Which kinds of cause the framework identifies can be answered; how many people left any particular society cannot",
     "How many people left any particular society can be answered; which kinds of cause the framework identifies cannot",
     "Neither the kinds of cause nor the forms of coerced labour migration can be answered",
     "Both the kinds of cause and the year each migration stream began can be answered",
     "Only the numbers of migrants can be answered, and nothing about their reasons"], ans=0,
   why="KC-5.4.I, KC-5.4.I.B, KC-5.4.II.A and KC-5.4.II.B between them name demographic change, transportation, the search for work and coercion as causes, so the kinds of cause are answerable. The framework prints no figure, no route and no starting date for any stream, and the anchor carries both clauses because the exact reversal is offered."),
 dict(q="Taking this topic's statements together, what account of the causes of migration do they give?",
   choices=[
     "Demographic change and the search for work moved people, new transportation shaped where they went and whether they returned, and coercion continued to move others against their will",
     "Coercion alone moved people, and no individual in this period relocated by choice",
     "Choice alone moved people, and coerced labour migration had ended before the period began",
     "New transportation was the only cause of migration, demographic and economic conditions playing no part",
     "The framework identifies the effects of migration but none of its causes"], ans=0,
   why="KC-5.4.I gives demographic change, KC-5.4.II.A gives free relocation often in search of work, KC-5.4.I.B gives transportation shaping destination and return, and KC-5.4.II.B gives the continued reliance on coerced and semicoerced labour migration. The key holds all four together, and each rejected option deletes one or more of them."),
]
