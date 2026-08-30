# AP COMPARATIVE GOVERNMENT AND POLITICS 1.9 Sustaining Legitimacy
# CED effective Fall 2026, Unit 1 Political Systems, Regimes, and Governments.
# Enduring understanding LEG-1; learning objective LEG-1.B (explain how
# governments maintain legitimacy). Suggested skill 1.E, Concept Application.
#
# Essential knowledge relied on:
#   LEG-1.B.1  governments maintain legitimacy through processes or factors
#              including POLICY EFFECTIVENESS, POLITICAL EFFICACY, TRADITION,
#              CHARISMATIC LEADERSHIP, and INSTITUTIONALIZED LAWS
#   LEG-1.B.2  PEACEFUL RESOLUTION OF CONFLICTS, PEACEFUL TRANSFER OF POWER,
#              REDUCED GOVERNMENTAL CORRUPTION, and ECONOMIC DEVELOPMENT can
#              reinforce legitimacy
#   LEG-1.B.3  an INCREASE IN CORRUPTION, REDUCED ELECTORAL COMPETITION, and
#              SERIOUS PROBLEMS (such as a poor economy or social conflicts) can
#              all undermine legitimacy
#   LEG-1.B.4  devolution and delegation of power to regional governments can
#              ENHANCE OR WEAKEN legitimacy, creating both opportunities and
#              obstacles, by
#     .a promoting policy innovation, matching policies to local needs, improving
#        policies through competition, increasing political participation,
#        checking central power, and allowing better representation of
#        religious/ethnic/minority groups
#     .b creating contradictory policies, making implementation more complicated
#        and inefficient, allowing inequality between regions, increasing
#        competition for resources, and exacerbating ethnic and local tensions
#   LEG-1.B.5  questions about the INTEGRITY OF ELECTION RESULTS across the course
#              countries can lead to PROTESTS that may weaken legitimacy AND any
#              ongoing democratization processes
#
# POLITICAL EFFICACY is named by LEG-1.B.1 and not defined in the framework text.
# It IS defined in the CED's own scoring guidelines for sample free-response
# question 2, which accept "citizens have faith and trust in government and
# believe that they can influence politics" and "citizens believe that one's vote
# can influence political affairs." Items 2 and 3 key that wording and nothing
# beyond it. The same scoring guidelines supply item 28: authoritarian regimes
# often allow citizens to participate in order to develop and maintain a sense of
# political legitimacy.
#
# Supporting statements: LEG-1.A.1 (legitimacy as belief), PAU-1.C.3 (corruption
# inhibits democratization; independent judiciaries reduce it), PAU-1.C.4
# (democratization can stall or be reversed), PAU-4.A.3 and DEM-2.B.4.a (measures
# that reduce electoral competition), PAU-3.C.2.f (the ceremonial monarch),
# MPA-1.A.3 (causation cannot be isolated).
#
# Table figures are HYPOTHETICAL and labelled so in every stem.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("1.9", "Sustaining Legitimacy", 1)

_T_CORR = dict(
    headers=["Country (hypothetical)", "Corruption score, 2010 (0 = highly corrupt, 100 = very clean)",
             "Corruption score, 2020 (0 = highly corrupt, 100 = very clean)",
             "Share saying they trust the national government, 2020"],
    rows=[["Country R", "31", "52", "64"],
          ["Country S", "58", "44", "39"],
          ["Country T", "47", "46", "51"]])

_T_PROTEST = dict(
    headers=["Election (hypothetical)", "Share of citizens saying the count was accurate",
             "Protest events recorded in the following month",
             "Change in the share saying the government has the right to rule, in percentage points"],
    rows=[["Election 1", "81", "4", "2"],
          ["Election 2", "57", "46", "-9"],
          ["Election 3", "34", "112", "-18"]])

QUESTIONS = [
 dict(q="Which set of processes or factors does the framework name as ways governments maintain legitimacy?",
   choices=[
     "policy effectiveness, political efficacy, tradition, charismatic leadership, and institutionalized laws",
     "territory, population, governing institutions, and international recognition",
     "federalism, devolution, and supranational membership",
     "the number of registered parties and the length of the electoral term",
     "gross domestic product, growth rates, and income distribution"], ans=0,
   why="EK LEG-1.B.1 lists exactly these five. The rejected sets are the elements of statehood under EK PAU-1.A.2, territorial structure, electoral arithmetic and the data resources of EK MPA-1.A.8, none of which the framework offers under this heading."),
 dict(q="The College Board's own scoring guidance describes political efficacy as",
   choices=[
     "citizens having faith and trust in government and believing that they can influence politics",
     "a government's ability to implement the policies it announces",
     "the share of eligible citizens who cast a ballot",
     "the legal authority of a state over its territory",
     "the endorsement of a government by a dominant political party"], ans=0,
   why="The scoring guidelines for the CED's sample free-response question on political efficacy accept 'citizens have faith and trust in government and believe that they can influence politics' and 'citizens believe that one's vote can influence political affairs'. EK LEG-1.B.1 names political efficacy without defining it, so this is the framework's own gloss."),
 dict(q="In one country, most citizens say they believe their vote can influence political affairs and that raising a concern with officials is worth doing. Which of the framework's routes to sustaining legitimacy does this most directly describe?",
   choices=[
     "political efficacy",
     "charismatic leadership",
     "institutionalized laws",
     "tradition",
     "peaceful transfer of power"], ans=0,
   why="EK LEG-1.B.1 names political efficacy among the factors through which governments maintain legitimacy, and the CED's scoring guidance describes it as citizens believing that one's vote can influence political affairs. The other listed factors concern a leader's personal appeal, a body of law, continuity, and the manner of a succession."),
 dict(q="A government's authority rests heavily on the personal appeal of a leader whose supporters follow the leader rather than the office. Which factor from the framework's list is at work?",
   choices=[
     "charismatic leadership",
     "institutionalized laws",
     "policy effectiveness",
     "political efficacy",
     "economic development"], ans=0,
   why="EK LEG-1.B.1 names charismatic leadership among the factors through which governments maintain legitimacy. Authority attached to a person rather than to an office or a rule is that factor; institutionalized laws are the framework's contrasting item on the same list."),
 dict(q="In a second country, authority is accepted because offices, procedures and limits are set out in law that outlasts any particular officeholder. Which factor from the framework's list is at work?",
   choices=[
     "institutionalized laws",
     "charismatic leadership",
     "political efficacy",
     "economic development",
     "peaceful resolution of conflicts"], ans=0,
   why="EK LEG-1.B.1 names institutionalized laws among the factors through which governments maintain legitimacy, and EK PAU-1.A.2 makes rules that endure from government to government the regime rather than the officeholder. Authority attaching to the office rather than the person is the contrast with charismatic leadership."),
 dict(q="Which comparison of policy effectiveness and political efficacy is most accurate on the framework's account?",
   choices=[
     "Policy effectiveness concerns how well the government's policies work, whereas political efficacy concerns whether citizens believe they can influence politics",
     "Policy effectiveness concerns whether citizens believe they can influence politics, whereas political efficacy concerns how well policies work",
     "The two terms mean the same thing and the framework lists both for emphasis",
     "Policy effectiveness applies only to democracies and political efficacy only to authoritarian regimes",
     "Neither is among the factors the framework says maintain legitimacy"], ans=0,
   why="EK LEG-1.B.1 lists both separately, and the CED's scoring guidance glosses political efficacy as citizens' faith, trust and belief that they can influence politics. One is a property of what government does and the other of what citizens believe, which is why a government can be effective without producing efficacy."),
 dict(q="Which set of developments does the framework say can reinforce legitimacy?",
   choices=[
     "peaceful resolution of conflicts, peaceful transfer of power, reduced governmental corruption, and economic development",
     "an increase in corruption, reduced electoral competition, and a poor economy",
     "the suspension of a constitution and the cancellation of elections",
     "the appointment of a legislature's members by the executive",
     "the transfer of regulatory authority to a supranational body"], ans=0,
   why="EK LEG-1.B.2 names exactly these four as reinforcing legitimacy. The first rejected option is EK LEG-1.B.3's list of what undermines it, and the others are institutional changes the framework treats under different statements."),
 dict(q="A country's governing party loses an election and hands office to its opponents without incident, for the third consecutive alternation. On the framework's account this most directly",
   choices=[
     "reinforces legitimacy, since a peaceful transfer of power is named among the things that do so",
     "undermines legitimacy, since a change of government shows instability",
     "has no bearing on legitimacy, which depends only on economic performance",
     "converts the country from an authoritarian regime into a democratic one automatically",
     "reduces the country's sovereignty by weakening the incumbent government"], ans=0,
   why="EK LEG-1.B.2 names peaceful transfer of power among the things that reinforce legitimacy, and EK PAU-1.D.4 describes elections as the relatively peaceful route by which governments change. A transfer that goes off without incident demonstrates that the rules are accepted by those who lose under them."),
 dict(q="A state establishes an independent judiciary that convicts senior officials of taking bribes, and the perceived level of official corruption falls. On the framework's account this most directly",
   choices=[
     "reinforces legitimacy, since reduced governmental corruption is named among the things that do so",
     "undermines legitimacy, since prosecutions publicize wrongdoing",
     "has no bearing on legitimacy, which depends only on election results",
     "converts a unitary state into a federal one",
     "reduces the independence of the judiciary by involving it in politics"], ans=0,
   why="EK LEG-1.B.2 names reduced governmental corruption among the things that reinforce legitimacy, and EK PAU-1.C.3 states that independent judiciaries can reduce corruption while protecting individual liberties and civil rights. The two statements point the same way."),
 dict(q="Over two decades a country's incomes, life expectancy and school enrolment all rise substantially. On the framework's account this most directly",
   choices=[
     "reinforces legitimacy, since economic development is named among the things that do so",
     "undermines legitimacy by raising citizens' expectations beyond what any government can meet",
     "has no bearing on legitimacy, which is a purely legal matter",
     "guarantees that the country will democratize",
     "shows that the country must be a consolidated democracy"], ans=0,
   why="EK LEG-1.B.2 names economic development among the things that can reinforce legitimacy, and EK LEG-1.A.2 names economic growth among the sources of legitimacy. Neither statement makes development sufficient for democratization, which EK PAU-1.C.1 defines separately."),
 dict(q="Which set of developments does the framework say can undermine legitimacy?",
   choices=[
     "an increase in corruption, reduced electoral competition, and serious problems such as a poor economy or social conflicts",
     "peaceful transfer of power, reduced corruption, and economic development",
     "the establishment of an independent election commission",
     "the extension of the franchise to all adult citizens",
     "the publication of the reasoning behind ministerial decisions"], ans=0,
   why="EK LEG-1.B.3 names exactly these three. The first rejected option is EK LEG-1.B.2's list of what reinforces legitimacy, and the remaining three are institutional changes the framework treats as aims or instruments of democratization under EK PAU-1.C."),
 dict(q="A government raises the registration requirements facing rival parties, raises the threshold for ballot access, and disqualifies several opposition candidates. On the framework's account of legitimacy, the most direct consequence is that",
   choices=[
     "legitimacy is undermined, since reduced electoral competition is named among the things that undermine it",
     "legitimacy is reinforced, since fewer parties makes government more decisive",
     "legitimacy is unaffected, since elections are still being held",
     "sovereignty is transferred to the electoral commission",
     "the country automatically becomes a federal state"], ans=0,
   why="EK LEG-1.B.3 names reduced electoral competition among the things that can undermine legitimacy, EK PAU-4.A.3 lists registration and threshold rules among the devices that entrench one party, and EK DEM-2.B.4.a describes candidate exclusion reducing competition and representation. The continued holding of elections does not answer the objection."),
 dict(q="Reports of officials demanding payments for routine public services multiply, and audits confirm the pattern. Which pair of framework claims does this most directly engage?",
   choices=[
     "that an increase in corruption can undermine legitimacy, and that political corruption inhibits democratization",
     "that peaceful transfer of power reinforces legitimacy, and that devolution can weaken it",
     "that economic development reinforces legitimacy, and that tradition sustains it",
     "that reduced electoral competition undermines legitimacy, and that charismatic leadership sustains it",
     "that legitimacy is conferred by other states, and that sovereignty depends on recognition"], ans=0,
   why="EK LEG-1.B.3 names an increase in corruption among the things that can undermine legitimacy and EK PAU-1.C.3 states that political corruption inhibits democratization. The framework therefore treats rising corruption as damaging on two fronts at once."),
 dict(q="The framework's examples of the 'serious problems' that can undermine legitimacy are",
   choices=[
     "a poor economy and social conflicts",
     "a rising population and a large territory",
     "membership of supranational organizations",
     "the existence of more than one political party",
     "the separation of powers among branches of government"], ans=0,
   why="EK LEG-1.B.3 gives a poor economy and social conflicts as its examples of the serious problems that can undermine legitimacy. Population, territory, treaty membership, party competition and separated powers appear elsewhere in the framework and not under this heading."),
 dict(q="Which statement most accurately reports what the framework says about devolving power to regional governments?",
   choices=[
     "It can enhance or weaken legitimacy, creating both opportunities for and obstacles to resolving social, political and economic issues",
     "It always enhances legitimacy by bringing government closer to citizens",
     "It always weakens legitimacy by fragmenting national authority",
     "It has no bearing on legitimacy, which is determined at the national level only",
     "It converts a unitary state into a federal state and thereby settles the question"], ans=0,
   why="EK LEG-1.B.4 states that devolution and delegation of power to regional governments can enhance or weaken legitimacy, creating both opportunities and obstacles, and then lists benefits and costs in the same statement. A one-sided reading contradicts the sentence in either direction."),
 dict(q="Which of the following appears on the framework's list of what devolution can do FOR legitimacy?",
   choices=[
     "promoting policy innovation and improving policies through competition among regions",
     "creating contradictory policies across regions",
     "increasing competition for resources between regions",
     "allowing inequality between regions to grow",
     "making policy implementation more complicated and inefficient"], ans=0,
   why="EK LEG-1.B.4.a lists promoting policy innovation, matching policies to local needs, improving policies through competition, increasing political participation, checking central power and better representation of religious, ethnic and minority groups. Each rejected option is drawn from EK LEG-1.B.4.b, the costs half of the same statement."),
 dict(q="Among the costs the framework attributes to devolving and delegating power to regional governments is",
   choices=[
     "exacerbating ethnic and local tensions",
     "increasing political participation",
     "checking central power",
     "matching policies to local needs",
     "allowing better representation of minority groups"], ans=0,
   why="EK LEG-1.B.4.b lists creating contradictory policies, complicating and slowing implementation, allowing inequality between regions, increasing competition for resources and exacerbating ethnic and local tensions. Each rejected option is drawn from EK LEG-1.B.4.a, the benefits half of the same statement."),
 dict(q="A state devolves health and education policy to its regions. Within a decade, regions have adopted different approaches, two have produced improvements that others then copy, and turnout at regional elections has risen. On the framework's account this outcome shows devolution",
   choices=[
     "enhancing legitimacy through policy innovation, improvement by competition, and increased political participation",
     "weakening legitimacy through contradictory policies and interregional inequality",
     "having no effect on legitimacy, since national institutions are unchanged",
     "converting the state from unitary to federal",
     "reducing the state's sovereignty by dividing its authority"], ans=0,
   why="EK LEG-1.B.4.a names promoting policy innovation, improving policies through competition and increasing political participation among devolution's benefits, and all three appear in the scenario. EK PAU-2.A.2 allows the degree of centralization to change without altering the constitutional classification."),
 dict(q="In a second state, devolution has produced sharply different entitlements across regions, disputes over the distribution of national revenue, and worsening relations between two regional communities. On the framework's account this outcome shows devolution",
   choices=[
     "weakening legitimacy through inequality between regions, competition for resources, and exacerbated ethnic and local tensions",
     "enhancing legitimacy through better representation of minority groups",
     "having no effect on legitimacy, since each region chose its own policy",
     "converting the state from federal to unitary",
     "establishing that devolution is always harmful"], ans=0,
   why="EK LEG-1.B.4.b names allowing inequality between regions, increasing competition for resources and exacerbating ethnic and local tensions among devolution's costs, and all three appear in the scenario. EK LEG-1.B.4's opening clause is why this does not establish a general verdict on devolution."),
 dict(q="What does the framework say questions about the integrity of election results can lead to?",
   choices=[
     "protests that may weaken legitimacy and any ongoing democratization processes",
     "the automatic annulment of the election by an international body",
     "an immediate change of regime in every case",
     "an increase in legitimacy, since disputes show that citizens are engaged",
     "the transfer of the count to the armed forces"], ans=0,
   why="EK LEG-1.B.5 states that questions about the integrity of election results across the course countries can lead to protests that may weaken legitimacy and any ongoing democratization processes. The statement names two casualties, not one, and hedges with 'may'."),
 dict(q="The framework's statement about disputed election results is best described as applying to",
   choices=[
     "the course countries generally, rather than to authoritarian regimes alone",
     "authoritarian regimes only",
     "democratic regimes only",
     "federal states only",
     "states that belong to supranational organizations only"], ans=0,
   why="EK LEG-1.B.5 refers to questions about the integrity of election results ACROSS THE COURSE COUNTRIES, which is the framework's phrase for the whole set of six. This matches EK DEM-1.C.2's and EK DEM-1.B.3's pattern of assigning a phenomenon to both regime types and differing in degree."),
 dict(q="The table reports hypothetical corruption scores and trust figures for three countries. Which country's record best matches the framework's claim that reduced governmental corruption can reinforce legitimacy?",
   table=_T_CORR,
   choices=[
     "Country R, whose corruption score rose 21 points toward the clean end of the scale and which reports the highest trust figure",
     "Country S, whose corruption score fell 14 points",
     "Country T, whose corruption score changed by 1 point",
     "All three equally, since each score changed",
     "None of the three, because corruption cannot be measured"], ans=0,
   why="EK LEG-1.B.2 names reduced governmental corruption among the things that reinforce legitimacy, and the header states that a higher score means cleaner, so a rise is a reduction in corruption. Only one row pairs a large rise with the highest trust figure in the table."),
 dict(q="Using the same table, which country's record best matches the framework's claim that an increase in corruption can undermine legitimacy?",
   table=_T_CORR,
   choices=[
     "Country S, whose corruption score fell 14 points and which reports the lowest trust figure",
     "Country R, whose corruption score rose 21 points",
     "Country T, whose score barely moved",
     "All three, since every country's trust figure is below 70",
     "None, since the table reports no information about corruption"], ans=0,
   why="EK LEG-1.B.3 names an increase in corruption among the things that can undermine legitimacy, and on this scale a falling score means rising corruption. Only one row pairs a substantial fall with the lowest trust figure in the table."),
 dict(q="A student wants to use the third country in the table as evidence for one of the framework's two claims about corruption and legitimacy. The best response is that",
   table=_T_CORR,
   choices=[
     "its corruption score barely moved over the decade, so it supports neither the claim about reduced corruption nor the claim about increased corruption",
     "it supports the claim about reduced corruption, since its 2020 score is cleaner than the second country's",
     "it supports the claim about increased corruption, since its trust figure is not the highest",
     "it supports both claims equally well",
     "it cannot be used because its trust figure is missing"], ans=0,
   why="EK LEG-1.B.2 and EK LEG-1.B.3 are both claims about CHANGE in corruption, so a country whose score is effectively flat provides no movement for either claim to attach to. A level reading and a rank in trust are different quantities from a change over time."),
 dict(q="The table reports hypothetical figures for three elections. Which conclusion does it support?",
   table=_T_PROTEST,
   choices=[
     "The lower the share of citizens accepting the count, the more protest followed and the larger the fall in the share saying the government has the right to rule",
     "Protest was heaviest after the election whose count was most widely accepted",
     "The share saying the government has the right to rule rose after every election",
     "Acceptance of the count was unrelated to the number of protest events",
     "Every election in the table was followed by a fall in the share saying the government has the right to rule"], ans=0,
   why="EK LEG-1.B.5 states that questions about the integrity of election results can lead to protests that may weaken legitimacy. Reading the three rows in order of the acceptance column, protest counts rise and the change in the right-to-rule share becomes more negative, which is that statement in numbers."),
 dict(q="According to the same table, the total number of protest events recorded across the three elections is",
   table=_T_PROTEST,
   choices=[
     "162",
     "158",
     "116",
     "50",
     "112"], ans=0,
   why="Adding the three figures in the protest column gives the total; the alternatives arise from dropping the smallest row, dropping the largest, adding only the first two, or reading the largest single row as though it were the total."),
 dict(q="Which row of the same table best illustrates the framework's hedge that such protests MAY weaken legitimacy rather than must?",
   table=_T_PROTEST,
   choices=[
     "Election 1, where a large majority accepted the count, few protest events followed, and the right-to-rule share rose rather than fell",
     "Election 2, where a bare majority accepted the count",
     "Election 3, where the fewest citizens accepted the count",
     "No row, since the framework says protests always weaken legitimacy",
     "All three rows equally, since each was followed by some protest"], ans=0,
   why="EK LEG-1.B.5 says protests MAY weaken legitimacy and any ongoing democratization processes, so an election followed by little protest and no loss of the right-to-rule share is what the hedge leaves room for. The rows with heavy protest illustrate the other half of the statement."),
 dict(q="The CED's scoring guidance explains high turnout in an authoritarian regime partly by noting that such regimes often allow citizens to participate in order to",
   choices=[
     "develop and maintain a sense of political legitimacy",
     "identify which citizens oppose the government so they can be prosecuted",
     "satisfy a requirement imposed by a supranational organization",
     "transfer the selection of the executive to the electorate",
     "guarantee that opposition parties win a share of the seats"], ans=0,
   why="The scoring guidelines for the CED's sample free-response question on turnout accept that authoritarian regimes often allow citizens to participate to develop and maintain a sense of political legitimacy, which matches EK DEM-1.A.4's statement that formal participation can be encouraged across regime types to enhance legitimacy."),
 dict(q="Which finding would most strongly indicate that a government's legitimacy is being reinforced in the framework's sense?",
   choices=[
     "Power has passed peacefully between rival parties, measured corruption has fallen, and a growing share of citizens say the government has the right to make the decisions it makes",
     "The governing party has increased its majority in the legislature",
     "The government has signed several new trade agreements",
     "The national legislature has moved to a larger building",
     "The government has announced a new set of policy targets"], ans=0,
   why="EK LEG-1.B.2 names peaceful transfer of power and reduced governmental corruption among the things that reinforce legitimacy, and EK LEG-1.A.1 makes the belief of constituents the thing being reinforced. The keyed finding reports two named causes and the belief itself; the rejected findings report none of them."),
 dict(q="Taking the framework's statements on sustaining legitimacy together, which summary is most accurate?",
   choices=[
     "Legitimacy is maintained through several named processes, reinforced by peaceful politics, cleaner government and development, undermined by corruption, narrowed competition and serious problems, and affected in either direction by devolution and by disputes over election results",
     "Legitimacy is maintained only by economic growth and lost only in recessions",
     "Legitimacy once established cannot be undermined by anything a government does",
     "Legitimacy depends entirely on whether other states recognize the government",
     "Legitimacy is enhanced by devolution in every case and by nothing else"], ans=0,
   why="EK LEG-1.B.1 supplies the processes, EK LEG-1.B.2 the reinforcing developments, EK LEG-1.B.3 the undermining ones, EK LEG-1.B.4 the two-sided effect of devolution and EK LEG-1.B.5 the effect of disputed election results. The summary keeps all five rather than reducing them to one mechanism."),
]
