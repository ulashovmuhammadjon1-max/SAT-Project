# AP COMPARATIVE GOVERNMENT AND POLITICS 1.10 Political Stability
# CED effective Fall 2026, Unit 1 Political Systems, Regimes, and Governments.
# Enduring understanding LEG-1; learning objective LEG-1.C (explain how internal
# actors influence and interact with state authority and either enhance or
# threaten stability). Suggested skill 3.D, Data Analysis.
#
# Essential knowledge relied on:
#   LEG-1.C.1  INTERNAL ACTORS can interact with governments to BOLSTER OR
#              UNDERMINE regime stability and rule of law, represented by:
#     .a contrasting methods to combat POLITICAL CORRUPTION among the six course
#        countries
#     .b state responses to SEPARATIST GROUP VIOLENCE, DRUG TRAFFICKING, and
#        DISCRIMINATION BASED ON GENDER OR RELIGIOUS DIFFERENCES in IRAN, MEXICO
#        and NIGERIA
#     .c VARIED state responses to MASS PROTEST MOVEMENTS that oppose governmental
#        policies or their equal enforcement
#   LEG-1.C.2  state authorities OF DIFFERENT REGIME TYPES attempt to limit the
#              influence of divisive and violent actors in their countries TO
#              ATTRACT MORE PRIVATE CAPITAL AND FOREIGN DIRECT INVESTMENT and to
#              improve economic growth
#   LEG-1.C.3  across the course countries, INTERNAL REFORM PRESSURE from CITIZEN
#              PROTEST GROUPS AND CIVIL SOCIETY can lead to the creation of new
#              political institutions or policies to PROTECT CIVIL LIBERTIES,
#              IMPROVE TRANSPARENCY, ADDRESS ELECTION FAIRNESS AND MEDIA BIAS,
#              LIMIT CORRUPTION, and ENSURE EQUALITY UNDER LAW
#
# Supporting statements, each named in the verifier's claim:
#   LEG-2.B.2b state responses to cleavages range from BRUTE REPRESSION to
#              recognition of ethnic/religious minorities and the creation of
#              autonomous regions and/or representation in governmental
#              institutions
#   LEG-2.B.4a separatist movements have emerged in CHINA, IRAN, NIGERIA, RUSSIA
#              and the UNITED KINGDOM
#   LEG-2.B.4b groups demanding AUTONOMY BUT NOT INDEPENDENCE have emerged in
#              MEXICO and the UNITED KINGDOM
#   LEG-2.B.4c ethnicity has played a more significant role in Nigeria than in
#              Mexico because of different colonial histories and greater
#              diversity and politicization of identities in Nigeria
#   LEG-2.B.5  challenges in multinational states: conflicting interests and
#              competition among groups and parties; perceived lack of
#              governmental authority and legitimacy; pressure for
#              autonomy/secession, intergroup conflict, terrorism and civil war;
#              encroachment of neighboring states sensing weakness
#   DEM-1.B.4  authoritarian regimes tolerate mass political protests and movements
#              LESS than democratic regimes, valuing public order more than
#              individual liberties and civil rights
#   PAU-1.C.3  independent judiciaries can reduce corruption
#   MPA-1.A.3  causation cannot be isolated and demonstrated with certainty
#
# NOTE the two lists at LEG-2.B.4: the United Kingdom appears on BOTH, and Mexico
# only on the second. That is not the pairing a student would guess, so items 10
# to 12 key it explicitly (AP_COMP_GOV_CED.md note 14).
#
# Table figures are HYPOTHETICAL and labelled so in every stem.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("1.10", "Political Stability", 1)

_T_STAB = dict(
    headers=["Country (hypothetical)", "Recorded incidents of political violence, 2015",
             "Recorded incidents of political violence, 2020",
             "Net foreign direct investment inflow as a share of GDP, 2020 (percent)"],
    rows=[["Country U", "310", "94", "4.6"],
          ["Country V", "120", "260", "1.1"],
          ["Country W", "45", "41", "3.8"]])

_T_RESP = dict(
    headers=["State response to a mass protest movement (hypothetical sample of episodes)",
             "Number of episodes",
             "Episodes followed within two years by a new institution or policy protecting civil liberties"],
    rows=[["Ban the protest and disperse it", "40", "2"],
          ["Negotiate and concede some demands", "25", "19"],
          ["Ignore the protest", "18", "3"],
          ["Recognize the group and create a consultative body", "17", "14"]])

QUESTIONS = [
 dict(q="What does the framework say about how internal actors interact with governments?",
   choices=[
     "they can bolster or undermine regime stability and the rule of law",
     "they can only undermine regime stability, never strengthen it",
     "they can only strengthen regime stability, never undermine it",
     "they affect the economy but not regime stability",
     "they matter only in authoritarian regimes"], ans=0,
   why="EK LEG-1.C.1 states that internal actors can interact with governments to bolster or undermine regime stability and rule of law. The statement is deliberately two-directional, so a reading that allows only one direction contradicts it."),
 dict(q="One of the framework's three illustrations of internal actors interacting with state authority is",
   choices=[
     "contrasting methods to combat political corruption among the six course countries",
     "the operations of supranational organizations in member states",
     "the encroachment of neighboring states on a weakened government",
     "the allocation of legislative seats by proportional representation",
     "the appointment of judges by a national executive"], ans=0,
   why="EK LEG-1.C.1.a names contrasting methods to combat political corruption among the six course countries as one of the three illustrations. Supranational operations and encroachment by neighbors are external actors, treated at EK PAU-2.A.2 and EK LEG-2.B.5.d."),
 dict(q="Which set of challenges, and which set of countries, does the framework pair in its illustration of state responses to internal actors?",
   choices=[
     "separatist group violence, drug trafficking, and discrimination based on gender or religious differences, in Iran, Mexico, and Nigeria",
     "separatist group violence and drug trafficking, in China, Russia, and the United Kingdom",
     "corruption and media bias, in China, Iran, and Russia",
     "electoral fraud and low turnout, in Mexico, Nigeria, and the United Kingdom",
     "foreign invasion and treaty disputes, in all six course countries"], ans=0,
   why="EK LEG-1.C.1.b names state responses to separatist group violence, drug trafficking, and discrimination based on gender or religious differences in Iran, Mexico and Nigeria. Both halves of the pairing are the framework's, and substituting a different trio of countries loses the statement's support."),
 dict(q="The framework's third illustration under this heading concerns",
   choices=[
     "varied state responses to mass protest movements that oppose governmental policies or their equal enforcement",
     "uniform state responses to mass protest movements across all six countries",
     "the absence of mass protest movements in authoritarian regimes",
     "the role of supranational organizations in resolving protests",
     "the effect of protests on a state's international recognition"], ans=0,
   why="EK LEG-1.C.1.c names varied state responses to mass protest movements that oppose governmental policies or their equal enforcement. The word 'varied' is the framework's, and EK LEG-2.B.2.b describes the range those responses run along."),
 dict(q="According to the framework, why do state authorities attempt to limit the influence of divisive and violent actors?",
   choices=[
     "to attract more private capital and foreign direct investment and to improve economic growth",
     "to satisfy the requirements of a supranational organization they have joined",
     "to increase the number of parties represented in the legislature",
     "to secure international recognition of their statehood",
     "to transfer authority from the national to the regional level"], ans=0,
   why="EK LEG-1.C.2 gives exactly this motive: to attract more private capital and foreign direct investment and to improve economic growth. The framework thus links internal order to an economic objective rather than to an institutional or diplomatic one."),
 dict(q="Which statement about which regimes pursue that objective is consistent with the framework?",
   choices=[
     "State authorities of different regime types pursue it, so the motive is not confined to democracies or to authoritarian regimes",
     "Only democratic regimes pursue it, since only they depend on private investment",
     "Only authoritarian regimes pursue it, since only they can suppress violent actors",
     "No regime pursues it, since investment decisions are outside a state's influence",
     "Only federal states pursue it, since their regions compete for capital"], ans=0,
   why="EK LEG-1.C.2 begins with 'state authorities of different regime types', which places the behavior on both sides of the democratic-authoritarian divide. This follows the framework's recurring pattern, seen also at EK DEM-1.C.2 and EK DEM-1.B.3, of assigning a practice to both types and distinguishing them by degree."),
 dict(q="The framework says internal reform pressure from citizen protest groups and civil society can lead to the creation of new political institutions or policies. Which set of purposes does it name for them?",
   choices=[
     "protecting civil liberties, improving transparency, addressing election fairness and media bias, limiting corruption, and ensuring equality under law",
     "raising economic growth, expanding exports, and attracting foreign investment",
     "redrawing electoral districts and lengthening the terms of officeholders",
     "transferring authority to supranational organizations",
     "increasing the size of the armed forces and the police"], ans=0,
   why="EK LEG-1.C.3 lists exactly these five purposes. The economic objectives belong to EK LEG-1.C.2, which describes what state authorities pursue rather than what reform pressure produces."),
 dict(q="The framework's statement about internal reform pressure applies to",
   choices=[
     "the course countries generally, since the statement opens by saying it holds across them",
     "democratic course countries only",
     "authoritarian course countries only",
     "federal course countries only",
     "no course country, since the statement is purely hypothetical"], ans=0,
   why="EK LEG-1.C.3 opens with 'Across the course countries', the framework's phrase for the whole set of six. EK LEG-1.C.2 uses a parallel construction, 'state authorities of different regime types', so both statements are deliberately general."),
 dict(q="The framework describes a range along which state responses to social cleavages fall. That range runs from",
   choices=[
     "brute repression to recognition of ethnic and religious minorities and the creation of autonomous regions or representation in governmental institutions",
     "brute repression to the expulsion of minority populations",
     "indifference to the transfer of sovereignty to a supranational body",
     "negotiation to the redrawing of international borders",
     "a single response common to all six course countries"], ans=0,
   why="EK LEG-2.B.2.b states that state responses can range from brute repression to recognition of ethnic and religious minorities and the creation of autonomous regions and/or representation of minorities in governmental institutions. Both endpoints are the framework's own words."),
 dict(q="In which course countries does the framework say separatist movements have emerged as a result of social cleavages?",
   choices=[
     "China, Iran, Nigeria, Russia, and the United Kingdom",
     "Iran, Mexico, and Nigeria",
     "China, Russia, and Iran only",
     "Mexico and the United Kingdom",
     "All six course countries"], ans=0,
   why="EK LEG-2.B.4.a names China, Iran, Nigeria, Russia and the United Kingdom. Mexico is absent from this list, which is why the intuitive answer of naming every country, or the trio from EK LEG-1.C.1.b, fails."),
 dict(q="In which course countries does the framework say groups demanding autonomy but not independence have emerged?",
   choices=[
     "Mexico and the United Kingdom",
     "China and Russia",
     "Iran and Nigeria",
     "China, Iran, Nigeria, Russia, and the United Kingdom",
     "None, since every such group demands independence"], ans=0,
   why="EK LEG-2.B.4.b names Mexico and the United Kingdom as the countries where groups demanding autonomy but not independence have emerged. The five-country list belongs to EK LEG-2.B.4.a and concerns separatist movements instead."),
 dict(q="Which country appears on both of the framework's lists, of countries with separatist movements and of countries with groups demanding autonomy but not independence?",
   choices=[
     "the United Kingdom",
     "Mexico",
     "China",
     "Iran",
     "Russia"], ans=0,
   why="EK LEG-2.B.4.a names China, Iran, Nigeria, Russia and the United Kingdom, and EK LEG-2.B.4.b names Mexico and the United Kingdom, so one country stands on both. Mexico appears only on the second list, which is the pairing a student is most likely to get backwards."),
 dict(q="Which comparison of how democratic and authoritarian regimes respond to mass protest is consistent with the framework?",
   choices=[
     "Authoritarian regimes tolerate mass political protests and movements less than democratic regimes, valuing public order more than individual liberties and civil rights",
     "Authoritarian regimes tolerate mass political protests more than democratic regimes, since they are less constrained by public opinion",
     "Both regime types tolerate mass protest to exactly the same degree",
     "Neither regime type tolerates any mass protest",
     "Democratic regimes prohibit all protest that opposes governmental policy"], ans=0,
   why="EK DEM-1.B.4 states that authoritarian regimes tolerate mass political protests and movements less than democratic regimes do, valuing public order more than individual liberties and civil rights. EK DEM-1.B.3 adds that both types regulate formal participation, so the difference the framework draws is one of degree."),
 dict(q="Which set of challenges does the framework say governments face in securing stability in multinational states?",
   choices=[
     "conflicting interests among groups and parties, a perceived lack of governmental authority and legitimacy, pressure for autonomy or secession and intergroup conflict, and encroachment by neighboring states sensing weakness",
     "low turnout, high inflation, and an ageing population",
     "the absence of a written constitution and the lack of a national anthem",
     "membership of supranational organizations and the signing of trade agreements",
     "the separation of powers and the independence of the judiciary"], ans=0,
   why="EK LEG-2.B.5 lists exactly these four challenges. The last of them is the only external actor on the list, which is why the framework can treat stability in multinational states as partly a question of how weakness is perceived from outside."),
 dict(q="A state seeking to combat political corruption strengthens the independence of its courts so that officials can be prosecuted without the executive's approval. Which framework claims does this most directly engage?",
   choices=[
     "that course countries use contrasting methods to combat political corruption, and that independent judiciaries can reduce corruption while protecting liberties and civil rights",
     "that separatist movements have emerged in five of the six course countries",
     "that state authorities limit violent actors to attract foreign direct investment",
     "that authoritarian regimes tolerate mass protest less than democratic regimes",
     "that international recognition is an element of statehood"], ans=0,
   why="EK LEG-1.C.1.a names contrasting methods to combat political corruption among the six course countries as an illustration of internal actors interacting with state authority, and EK PAU-1.C.3 identifies independent judiciaries as able to reduce corruption while protecting individual liberties and civil rights."),
 dict(q="Which of the following describes an internal actor BOLSTERING regime stability in the framework's sense?",
   choices=[
     "A civil society coalition works with officials to design an anticorruption agency, and public confidence in the administration of justice rises",
     "An armed group seizes control of several districts and taxes traffic through them",
     "A neighboring state moves troops to the border after judging the government weak",
     "A supranational body requires the state to change a regulation",
     "A foreign investor withdraws capital after a change in tax law"], ans=0,
   why="EK LEG-1.C.1 says internal actors can interact with governments to bolster or undermine regime stability and rule of law, and EK LEG-1.C.3 describes civil society pressure producing new institutions to limit corruption. The rejected options are either an undermining internal actor or, in three cases, external actors of the kind EK LEG-2.B.5.d and EK PAU-2.A.2 treat separately."),
 dict(q="Which of the following describes an internal actor UNDERMINING regime stability and the rule of law in the framework's sense?",
   choices=[
     "Trafficking organizations establish control over sections of territory and intimidate local officials into ignoring the law",
     "A civil society group publishes an analysis of the national budget",
     "A political party contests an election and loses",
     "A regional assembly passes a law within its devolved competence",
     "A supreme court rules against a government minister"], ans=0,
   why="EK LEG-1.C.1.b names drug trafficking among the challenges to which states respond, and EK LEG-1.C.1 makes such actors capable of undermining regime stability and the rule of law. The rejected options are ordinary politics conducted through institutions, which EK PAU-1.B.1.a treats as the rule of law working rather than failing."),
 dict(q="A government negotiates the disarmament of armed groups operating in a mining region, publicizing the agreement as a signal to investors. Which framework claim does this most directly illustrate?",
   choices=[
     "that state authorities attempt to limit the influence of divisive and violent actors to attract private capital and foreign direct investment and improve growth",
     "that internal reform pressure from civil society creates new institutions protecting civil liberties",
     "that separatist movements have emerged as a result of social cleavages",
     "that authoritarian regimes tolerate mass protest less than democratic regimes",
     "that devolution can enhance or weaken legitimacy"], ans=0,
   why="EK LEG-1.C.2 states that state authorities of different regime types attempt to limit the influence of divisive and violent actors in their countries to attract more private capital and foreign direct investment and to improve economic growth. The investor signal in the scenario is that motive made explicit."),
 dict(q="After sustained campaigning by journalists' associations and civic groups, a state creates an independent body empowered to publish government contracts and audit ministries. Which framework claim does this most directly illustrate?",
   choices=[
     "that internal reform pressure from citizen protest groups and civil society can create new institutions to improve transparency and limit corruption",
     "that state authorities limit violent actors to attract foreign investment",
     "that separatist movements emerge from long-standing social cleavages",
     "that governments change more frequently and easily than regimes",
     "that a state's degree of centralization can change over time"], ans=0,
   why="EK LEG-1.C.3 states that internal reform pressure from citizen protest groups and civil society can lead to the creation of new political institutions or policies to protect civil liberties, improve transparency, address election fairness and media bias, limit corruption and ensure equality under law. Two of those five purposes appear in the scenario."),
 dict(q="The table reports hypothetical figures for three countries. Which country's record best fits the framework's claim that limiting divisive and violent actors is pursued in order to attract capital and investment?",
   table=_T_STAB,
   choices=[
     "Country U, whose recorded incidents fell by 216 over the period and which reports the highest investment share",
     "Country V, whose recorded incidents more than doubled",
     "Country W, whose recorded incidents fell by 4",
     "All three equally, since each country's figures changed",
     "None of the three, because the framework supplies no figures for any country"], ans=0,
   why="EK LEG-1.C.2 pairs limiting the influence of divisive and violent actors with attracting more private capital and foreign direct investment. The row that shows both halves at once, a large fall in violence alongside the largest investment share in the table, is the one the claim fits."),
 dict(q="Using the same table, which country's record moves in the direction the framework associates with weakening stability?",
   table=_T_STAB,
   choices=[
     "Country V, whose recorded incidents rose from 120 to 260 while its investment share is the lowest in the table",
     "Country U, whose recorded incidents fell sharply",
     "Country W, whose recorded incidents were lowest in both years",
     "None of the three, since political violence cannot be counted",
     "All three, since every country recorded some political violence"], ans=0,
   why="EK LEG-1.C.1 makes internal actors capable of undermining regime stability and the rule of law, and EK LEG-1.C.2 links limiting such actors to attracting capital. A row in which violence more than doubles while investment is lowest moves against both halves of that account."),
 dict(q="According to the same table, the fall in recorded incidents in the country with the largest decline was closest to",
   table=_T_STAB,
   choices=[
     "70 percent",
     "30 percent",
     "50 percent",
     "9 percent",
     "216 percent"], ans=0,
   why="Dividing the size of the fall by the earlier year's figure gives the proportional decline, which is what the question asks for. The alternatives arise from computing the remaining share instead of the fall, from halving, from reading a different row, and from mistaking the absolute drop for a percentage."),
 dict(q="The table reports a hypothetical sample of protest episodes classified by the state's response. Which conclusion does it support?",
   table=_T_RESP,
   choices=[
     "Episodes met with negotiation or with recognition of the group were followed by a new protective institution far more often, in proportion, than episodes that were banned or ignored",
     "Episodes met with a ban were followed by a new protective institution more often than episodes met with negotiation",
     "Every episode in the sample was followed by a new protective institution",
     "No episode in the sample was followed by a new protective institution",
     "The state banned fewer episodes than it recognized"], ans=0,
   why="EK LEG-1.C.1.c states that state responses to mass protest movements vary, and EK LEG-1.C.3 says reform pressure can produce new institutions protecting civil liberties. Reading each row as a proportion rather than a count separates the two accommodating responses sharply from the two that are not."),
 dict(q="According to the same table, the share of banned episodes that were followed within two years by a new protective institution or policy is",
   table=_T_RESP,
   choices=[
     "5 percent",
     "2 percent",
     "40 percent",
     "20 percent",
     "76 percent"], ans=0,
   why="Dividing the number of banned episodes followed by a new institution by the number of banned episodes gives the share. The alternatives offer the raw count as though it were a percentage, the row's total, a misplaced decimal, and the corresponding share for a different row."),
 dict(q="A student concludes from the same table that banning a protest causes a state not to adopt new protections. Which objection does the framework most directly support?",
   table=_T_RESP,
   choices=[
     "The table shows an association across four categories of response, and the framework denies that causation can be isolated and demonstrated with certainty from such evidence",
     "The table reports no information about how states responded",
     "An association of this kind establishes causation only in democratic regimes",
     "State responses to protest do not vary, so there is nothing to compare",
     "New institutions protecting civil liberties are never created after protest"], ans=0,
   why="EK MPA-1.A.3 states that numerous variables potentially influence political outcomes with no way to isolate and demonstrate which is producing the change, and EK MPA-1.A.4 calls a co-movement an association. A state willing to ban a protest may also be a state disinclined to adopt protections for independent reasons, which the table cannot separate."),
 dict(q="Why, according to the framework, has ethnicity played a more significant role in Nigeria than in Mexico?",
   choices=[
     "because of different colonial histories and a greater diversity and politicization of ethnic and religious identities in Nigeria",
     "because Mexico is unitary and Nigeria is federal",
     "because Nigeria holds elections and Mexico does not",
     "because Mexico has no ethnic divisions of any kind",
     "because Nigeria belongs to more supranational organizations"], ans=0,
   why="EK LEG-2.B.4.c gives exactly this explanation. EK LEG-2.A.1.c does describe ethnic divisions in Mexico between the indigenous population and whites and mestizos, so the framework's claim is comparative rather than a denial that cleavages exist there."),
 dict(q="Which finding would most strongly support a claim that internal reform pressure has produced institutional change in the framework's sense?",
   choices=[
     "Following a sustained civil society campaign, the state established a body with statutory powers to audit ministries and publish its findings",
     "A governing party increased its majority at a general election",
     "The state signed a trade agreement with a neighbouring country",
     "A ministry announced a target for reducing corruption",
     "The head of government gave a speech condemning corruption"], ans=0,
   why="EK LEG-1.C.3 requires the creation of new political institutions or policies, so a body with statutory powers is the kind of outcome that satisfies it. An election result, a treaty, an announced target and a speech leave the institutional landscape unchanged."),
 dict(q="Which comparison of the framework's two statements about limiting divisive actors and about reform pressure is most accurate?",
   choices=[
     "One describes state authorities acting on society for an economic objective, while the other describes society acting on the state for institutional and rights-based objectives",
     "Both describe state authorities acting on society for economic objectives",
     "Both describe society acting on the state for rights-based objectives",
     "One applies only to democracies and the other only to authoritarian regimes",
     "The two statements describe the same process in different words"], ans=0,
   why="EK LEG-1.C.2 has state authorities limiting divisive and violent actors to attract capital and improve growth, while EK LEG-1.C.3 has citizen protest groups and civil society producing institutions protecting liberties, transparency, election fairness, anticorruption and equality. The direction of pressure and the objective differ in each."),
 dict(q="A state faced with a movement demanding recognition for a linguistic minority creates an autonomous region with authority over language and education, rather than banning the movement. Where does this response fall on the range the framework describes?",
   choices=[
     "at the accommodating end, since creating autonomous regions is the framework's own example of recognition rather than repression",
     "at the repressive end, since the state has redrawn its internal boundaries",
     "outside the range, since the framework describes only repressive responses",
     "outside the range, since the framework describes only accommodating responses",
     "at the midpoint, since autonomy is neither recognition nor repression"], ans=0,
   why="EK LEG-2.B.2.b describes state responses ranging from brute repression to recognition of ethnic and religious minorities and the creation of autonomous regions and/or representation of minorities in governmental institutions. The scenario names the framework's own accommodating endpoint."),
 dict(q="Taking the framework's three statements on political stability together, which summary is most accurate?",
   choices=[
     "Internal actors can either strengthen or threaten stability and the rule of law, states of every regime type try to limit violent actors partly for economic reasons, and pressure from protest groups and civil society can produce new institutions protecting rights and limiting corruption",
     "Internal actors can only threaten stability, and states respond to them only by repression",
     "Stability depends entirely on external actors such as neighboring states and supranational organizations",
     "Only authoritarian regimes attempt to limit the influence of violent actors",
     "Protest movements have no effect on institutions in any course country"], ans=0,
   why="EK LEG-1.C.1 supplies the two-directional influence of internal actors, EK LEG-1.C.2 the cross-regime economic motive for limiting violent actors, and EK LEG-1.C.3 the institutional consequences of reform pressure. The summary keeps all three rather than reducing stability to repression or to outside forces."),
]
