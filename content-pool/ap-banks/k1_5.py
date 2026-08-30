# AP COMPARATIVE GOVERNMENT AND POLITICS 1.5 Sources of Power and Authority
# CED effective Fall 2026, Unit 1 Political Systems, Regimes, and Governments.
# Enduring understanding PAU-1; learning objective PAU-1.D (explain sources of
# power and authority in political systems). Suggested skill 2.B, Country
# Comparison.
#
# The topic rests on a single essential knowledge statement, so every key here is
# traceable to it or to an institutional statement in Unit 2 that fills it out.
#
#   PAU-1.D.1  sources of power and authority include CONSTITUTIONS, RELIGIONS,
#              MILITARY FORCES, POLITICAL PARTIES, LEGISLATURES, and POPULAR
#              SUPPORT; over time the six course countries' regimes have been
#              affected by such sources, represented by:
#     .a the Communist Party's control over China's military, which provided power
#        and authority to maintain regime stability
#     .b the transition of power from dictatorial rule in Iran to a theocracy
#        based on Islamic Sharia law after the 1979 Revolution
#     .c the transition of power in Nigeria and Mexico to multiparty republics
#        following military rule and single-party dominance, RESPECTIVELY
#     .d the political elite's backing of a strong president in Russia, creating a
#        managed democracy with election rules favoring one party
#     .e constitutional reforms in the United Kingdom that devolved power to
#        multiple parliaments, allowing the regime to maintain stability
#
# Institutional statements used to fill out the five illustrations:
#   PAU-3.C.2a China's president is commander in chief, chair of the Military
#              Commission and General Secretary of the Communist Party; changes in
#              top leadership are accomplished behind closed doors
#   PAU-3.C.2b Iran's Supreme Leader sets the political agenda, is commander in
#              chief, and appoints top ministers, the Expediency Council, HALF of
#              the Guardian Council, and the head of the judiciary
#   PAU-3.C.2f the United Kingdom's monarch serves ceremonially as head of state
#              and formally appoints as prime minister the leader of the party or
#              coalition holding the largest number of seats in the Commons
#   PAU-3.E.1a China's constitution recognizes the National People's Congress as
#              the government's most powerful institution
#   PAU-3.F.1a China's Politburo Standing Committee is the ACTUAL center of power
#              in the Chinese state
#   LEG-1.A.1  legitimacy is whether a government's constituents believe it has the
#              right to use power in the way it does
#   LEG-1.B.4  devolution can enhance or weaken legitimacy, with benefits and costs
#              listed in the same statement
#
# The China items keep PAU-3.E.1a and PAU-3.F.1a apart on purpose: the first is a
# statement about the CONSTITUTION and the second about ACTUAL power, and an item
# that blurred them would have no defensible key (AP_COMP_GOV_CED.md note 5).
# Table figures are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("1.5", "Sources of Power and Authority", 1)

_T_SOURCE = dict(
    headers=["Country (hypothetical)", "Named the elected legislature",
             "Named the governing party's leadership body", "Named the armed forces",
             "Named the head of state"],
    rows=[["Country 1", "54", "12", "4", "30"],
          ["Country 2", "9", "61", "18", "12"],
          ["Country 3", "21", "8", "55", "16"]])

_T_DEVO = dict(
    headers=["Region (hypothetical)", "Share of public spending decided by a devolved parliament, 2000",
             "Share of public spending decided by a devolved parliament, 2020"],
    rows=[["Region I", "12 percent", "41 percent"],
          ["Region II", "8 percent", "9 percent"],
          ["Region III", "0 percent", "27 percent"]])

QUESTIONS = [
 dict(q="Which of the following does the framework name as sources of power and authority in political systems?",
   choices=[
     "constitutions, religions, military forces, political parties, legislatures, and popular support",
     "population size, territory, international recognition, and a permanent government",
     "gross domestic product, growth rates, income distribution, and corruption levels",
     "federalism, devolution, unitary structure, and supranational membership",
     "the executive, the legislature, and the judiciary, and nothing besides"], ans=0,
   why="EK PAU-1.D.1 lists exactly these six as sources of power and authority. The rejected lists describe the elements of statehood under EK PAU-1.A.2, the data resources of EK MPA-1.A.8, territorial structure, and the branches of government, none of which is the framework's answer to this question."),
 dict(q="The framework's illustration of how power and authority have been shaped in China is",
   choices=[
     "the Communist Party's control over the military, which provided power and authority to maintain regime stability",
     "the backing of a strong president by the political elite, creating a managed democracy",
     "a transition from dictatorial rule to government under a religious legal code",
     "constitutional reforms that devolved power to multiple regional parliaments",
     "a transition to a multiparty republic following a long period of military rule"], ans=0,
   why="EK PAU-1.D.1.a names the Communist Party's control over China's military as the source that provided power and authority to maintain regime stability. The four rejected descriptions are the framework's own words about Russia, Iran, the United Kingdom and Nigeria."),
 dict(q="The framework presents Iran's 1979 Revolution as an illustration of which source of power and authority reshaping a regime?",
   choices=[
     "religion, since power passed from dictatorial rule to a theocracy based on Islamic Sharia law",
     "military forces, since the armed forces displaced the previous ruler",
     "legislatures, since an elected assembly assumed the previous ruler's powers",
     "constitutions, since a written constitution replaced an unwritten one",
     "popular support, since the new regime introduced universal suffrage"], ans=0,
   why="EK PAU-1.D.1 names religions among the sources of power and authority, and EK PAU-1.D.1.b describes the transition of power from dictatorial rule in Iran to a theocracy based on Islamic Sharia law after the 1979 Revolution. The other five sources are on the same list but are not what this illustration is offered to show."),
 dict(q="Which comparison correctly reports what the framework says about the transitions in Nigeria and Mexico?",
   choices=[
     "Both became multiparty republics, Nigeria following military rule and Mexico following single-party dominance",
     "Both became multiparty republics, Nigeria following single-party dominance and Mexico following military rule",
     "Both became theocracies following revolutions",
     "Both remained one-party states while permitting other parties to exist",
     "Neither changed regime type, since both have always been multiparty republics"], ans=0,
   why="EK PAU-1.D.1.c states the transition of power in Nigeria and Mexico to multiparty republics following military rule and single-party dominance respectively. The framework's 'respectively' fixes the pairing, and reversing it contradicts the sentence."),
 dict(q="The framework describes the political elite's backing of a strong president in Russia as having created",
   choices=[
     "a managed democracy with election rules favoring one party",
     "a theocracy governed under a religious legal code",
     "a multiparty republic following a period of military rule",
     "a unitary state in which regional parliaments hold devolved powers",
     "a one-party state in which only one party may hold governing power"], ans=0,
   why="EK PAU-1.D.1.d states that the political elite's backing of a strong president in Russia created a managed democracy with election rules favoring one party. EK DEM-1.C.5 supplies the matching regime label, a competitive authoritarian regime or illiberal democracy that holds contested elections with limited competitiveness."),
 dict(q="The framework's illustration of the United Kingdom under this topic is constitutional reform that devolved power to multiple parliaments. The effect it attributes to that reform is that it",
   choices=[
     "allowed the regime to maintain stability",
     "converted the United Kingdom from a unitary into a federal state",
     "transferred the appointment of the prime minister to the devolved parliaments",
     "ended the practice of appointing members of the upper chamber",
     "replaced first-past-the-post rules with proportional representation for the Commons"], ans=0,
   why="EK PAU-1.D.1.e states that constitutional reforms in the United Kingdom devolved power to multiple parliaments, allowing the regime to maintain stability. EK PAU-2.A.1 still lists the United Kingdom among the unitary states, so devolution in the framework's account is a redistribution within a unitary state rather than a change of that classification."),
 dict(q="Which pair of the framework's illustrations both describe a regime arriving at a multiparty republic from a different starting point?",
   choices=[
     "Nigeria and Mexico",
     "China and Russia",
     "Iran and the United Kingdom",
     "Russia and the United Kingdom",
     "China and Iran"], ans=0,
   why="EK PAU-1.D.1.c is the only one of the five illustrations that names two countries reaching the same destination, a multiparty republic, from military rule in one case and single-party dominance in the other. The remaining illustrations concern party control of the military, a theocratic transition, elite backing of a strong president, and devolution."),
 dict(q="China's and Russia's illustrations in the framework differ in that China's rests on",
   choices=[
     "a party's control over the armed forces, whereas Russia's rests on the political elite's backing of a strong presidency",
     "the political elite's backing of a strong presidency, whereas Russia's rests on a party's control over the armed forces",
     "a religious legal code, whereas Russia's rests on devolution to regional parliaments",
     "devolution to regional parliaments, whereas Russia's rests on a religious legal code",
     "popular support expressed at competitive elections in both cases"], ans=0,
   why="EK PAU-1.D.1.a names the Communist Party's control over China's military and EK PAU-1.D.1.d names the political elite's backing of a strong president in Russia. Both illustrate a source of power operating outside ordinary electoral competition, but the framework identifies different sources in each."),
 dict(q="Iran's and the United Kingdom's illustrations in the framework are best contrasted as",
   choices=[
     "religion supplying the basis of rule in one case and constitutional reform redistributing power in the other",
     "constitutional reform in one case and military control in the other",
     "military control in one case and single-party dominance in the other",
     "popular support in one case and legislative supremacy in the other",
     "identical processes described in different words"], ans=0,
   why="EK PAU-1.D.1.b describes a transition to a theocracy based on Islamic Sharia law and EK PAU-1.D.1.e describes constitutional reforms devolving power to multiple parliaments. Religions and constitutions are two separate entries on EK PAU-1.D.1's list of sources, and each illustration is offered for one of them."),
 dict(q="A state's founding document establishes which offices exist, how they are filled and what each may do, and disputes about power are settled by reference to it. Which source of power and authority named by the framework does this describe?",
   choices=[
     "constitutions",
     "religions",
     "military forces",
     "popular support",
     "legislatures"], ans=0,
   why="EK PAU-1.D.1 names constitutions first among the sources of power and authority, and a document that both creates offices and settles disputes about their powers is functioning as that source. The remaining named sources operate through belief, force, election and lawmaking rather than through a foundational text."),
 dict(q="In one state the ultimate interpreter of law is a religious authority, and legislation must be found compatible with a body of religious law before it takes effect. Which source of power and authority is most clearly at work?",
   choices=[
     "religions",
     "constitutions",
     "legislatures",
     "military forces",
     "political parties"], ans=0,
   why="EK PAU-1.D.1 names religions among the sources of power and authority and EK PAU-1.D.1.b gives a theocracy based on Islamic Sharia law as the framework's illustration. EK PAU-3.E.1.b adds that Iran's elected legislature acts under supervision to ensure compatibility with Islam and Sharia law, which is this source operating on an ordinary legislative process."),
 dict(q="In one state the officers of the armed forces determine who occupies the highest civil offices and can remove them. Which source of power and authority does this illustrate, and which regime type from the framework's authoritarian list does it produce?",
   choices=[
     "military forces, producing a military regime",
     "constitutions, producing an illiberal democracy",
     "political parties, producing a one-party state",
     "religions, producing a theocracy",
     "popular support, producing a consolidated democracy"], ans=0,
   why="EK PAU-1.D.1 names military forces among the sources of power and authority and EK PAU-1.B.3 names military regimes among the authoritarian types. EK PAU-1.D.1.c refers to Nigeria's transition to a multiparty republic following military rule, which is the framework's own instance of this source having held power."),
 dict(q="A regime in which one organization selects the occupants of every significant state office, sets policy before it reaches the legislature, and controls the armed forces is drawing its power principally from which of the framework's named sources?",
   choices=[
     "political parties",
     "legislatures",
     "constitutions",
     "popular support",
     "religions"], ans=0,
   why="EK PAU-1.D.1 names political parties among the sources of power and authority, and EK PAU-1.D.1.a gives the Communist Party's control over China's military as the illustration. EK PAU-3.F.1.a adds that China's Politburo Standing Committee is the actual center of power in the state, which is a party body rather than a state organ."),
 dict(q="An elected assembly in one state approves all legislation, controls the budget, and may remove ministers by vote. Which source of power and authority named by the framework is most directly at work?",
   choices=[
     "legislatures",
     "military forces",
     "religions",
     "constitutions",
     "political parties"], ans=0,
   why="EK PAU-1.D.1 names legislatures among the sources of power and authority, and the powers described are the lawmaking, budgetary and confirmation powers EK PAU-3.E.1 attributes to the legislative institutions of the course countries. Nothing in the description turns on a founding text, a faith, an army or a party."),
 dict(q="A government that has lost every recent election and whose ministers resign when the electorate turns against them is most directly constrained by which of the framework's named sources of power and authority?",
   choices=[
     "popular support",
     "military forces",
     "religions",
     "constitutions",
     "political parties"], ans=0,
   why="EK PAU-1.D.1 names popular support among the sources of power and authority, and a government that must leave office when support is withdrawn is one whose power depends on it. EK LEG-1.A.1's legitimacy is the related but distinct idea that constituents believe the government has the right to use power as it does."),
 dict(q="Which statement about China's National People's Congress and its Politburo Standing Committee is consistent with the framework?",
   choices=[
     "The constitution recognizes the National People's Congress as the government's most powerful institution, while the Politburo Standing Committee is the actual center of power in the state",
     "The constitution recognizes the Politburo Standing Committee as the government's most powerful institution, while the National People's Congress is the actual center of power",
     "Both bodies are elected directly by voters in single-member districts",
     "Neither body has any role in selecting the head of government",
     "The two are different names for the same institution"], ans=0,
   why="EK PAU-3.E.1.a says the constitution recognizes the National People's Congress as the government's most powerful institution that elects the president, approves the premier and legitimizes executive policies; EK PAU-3.F.1.a says the Politburo Standing Committee is the actual center of power in the Chinese state. Both sentences are the framework's, and they are about different things, the constitutional text and actual power."),
 dict(q="Which of the following powers does the framework assign to Iran's Supreme Leader?",
   choices=[
     "setting the political agenda, serving as commander in chief, and appointing top ministers, the Expediency Council, half of the Guardian Council, and the head of the judiciary",
     "approving all legislation and overseeing the budget",
     "conducting foreign policy and overseeing the civil service after election to a four-year term",
     "appointing the members of an upper chamber on the advice of an independent commission",
     "presiding over the lower chamber of the legislature under certain conditions"], ans=0,
   why="EK PAU-3.C.2.b assigns exactly these powers to the Supreme Leader, and specifies HALF of the Guardian Council rather than all of it. The rejected options describe the Majles under EK PAU-3.E.1.b, Iran's elected president, the United Kingdom's House of Lords and Russia's president."),
 dict(q="The framework says the United Kingdom's monarch formally appoints as prime minister the leader of the party or coalition holding the largest number of seats in the House of Commons. The most accurate description of where the prime minister's authority comes from is that it rests on",
   choices=[
     "command of a majority in the elected chamber, with the monarch's role being formal",
     "the monarch's personal choice among the available party leaders",
     "a direct national election of the prime minister by voters",
     "appointment by the House of Lords after review of the Commons' nominee",
     "selection by the leaders of the civil service"], ans=0,
   why="EK PAU-3.C.2.f states that the monarch serves ceremonially as head of state and FORMALLY appoints as prime minister the leader of the party or coalition holding the largest number of seats in the Commons. The seat count decides the outcome, which is why the framework calls the monarch's part ceremonial."),
 dict(q="The framework says changes in China's top leadership are accomplished behind closed doors. That statement bears most directly on which of its named sources of power and authority?",
   choices=[
     "political parties, since the succession is settled inside the party rather than by an electorate",
     "popular support, since voters choose among candidates for the leadership",
     "constitutions, since the constitution prescribes the method of succession",
     "military forces, since officers select the successor",
     "legislatures, since the legislature debates the succession in open session"], ans=0,
   why="EK PAU-3.C.2.a states that changes in top leadership are accomplished behind closed doors, and EK PAU-1.D.1.a locates China's regime stability in the Communist Party's control. A succession decided outside public institutions is a succession decided by the party, which is the source EK PAU-1.D.1 names."),
 dict(q="The table reports the share of respondents in three hypothetical countries naming each institution as the one that really decides national policy. Which country's pattern is most consistent with the framework's description of a system in which a party's leadership body rather than the elected legislature is the actual center of power?",
   table=_T_SOURCE,
   choices=[
     "Country 2, where the party leadership body is named by 61 percent and the legislature by 9 percent",
     "Country 1, where the legislature is named by 54 percent",
     "Country 3, where the armed forces are named by 55 percent",
     "All three equally, since every country names all four institutions",
     "None, because the framework supplies no survey data for any country"], ans=0,
   why="EK PAU-3.F.1.a describes a party body as the actual center of power in a state whose constitution names a legislature as its most powerful institution, so the pattern to look for is a party leadership body far ahead of the legislature. Only one row shows that gap."),
 dict(q="Using the same table, which country's pattern most suggests that military forces are the principal source of power, in the sense the framework gives that term?",
   table=_T_SOURCE,
   choices=[
     "Country 3, where the armed forces are named by 55 percent, more than every other institution in that country",
     "Country 2, where the armed forces are named by 18 percent",
     "Country 1, where the armed forces are named by 4 percent",
     "None of the three, because the armed forces are named by fewer than half of respondents everywhere",
     "All three, because the armed forces appear in every row"], ans=0,
   why="EK PAU-1.D.1 names military forces among the sources of power and authority, and the row in which the armed forces are named by an outright majority of respondents, ahead of every other institution in that same country, is the one this source fits."),
 dict(q="A student concludes from the same table that the country whose respondents most often name the elected legislature must be a democracy. The strongest objection is that",
   table=_T_SOURCE,
   choices=[
     "the table reports beliefs about where decisions are made, whereas the framework classifies regimes by rule of law, election conduct, media conditions, transparency and participation",
     "the table contains no information about legislatures",
     "beliefs about institutions can never be measured",
     "a country in which most respondents name the legislature cannot hold elections",
     "the framework classifies regimes only by whether they are federal or unitary"], ans=0,
   why="EK PAU-1.B.1 supplies the indicators of the democratic-authoritarian scale and none of them is a survey of opinion about which institution decides. EK LEG-1.A.1 shows the framework does treat what constituents believe as important, but as the source of legitimacy rather than as a test of regime type."),
 dict(q="The table reports hypothetical shares of public spending decided by a devolved parliament in three regions. In which region did a devolved parliament acquire spending authority where it previously had none?",
   table=_T_DEVO,
   choices=[
     "Region III, which moved from 0 percent to 27 percent",
     "Region I, which moved from 12 percent to 41 percent",
     "Region II, which moved from 8 percent to 9 percent",
     "All three regions, since each figure changed",
     "None of the three, since no region reached half"], ans=0,
   why="EK PAU-1.D.1.e describes constitutional reforms that devolved power to multiple parliaments, and a region beginning at zero is the case in which a devolved parliament came into existence rather than merely gaining ground. One region alone starts from nothing in the table."),
 dict(q="Using the same table, the total increase across all three regions in the share of public spending decided by a devolved parliament is",
   table=_T_DEVO,
   choices=[
     "57 percentage points",
     "29 percentage points",
     "68 percentage points",
     "41 percentage points",
     "77 percentage points"], ans=0,
   why="The three regions moved by 29, 1 and 27 percentage points, which sum to 57. Reading only the largest single change, or adding the final column, or adding the two largest final shares, produces each of the figures offered against it."),
 dict(q="Which comparison correctly distinguishes a source of power and authority from political legitimacy as the framework defines them?",
   choices=[
     "A source of power and authority is what a regime's capacity to rule rests on, whereas legitimacy is whether constituents believe the government has the right to use power in the way it does",
     "A source of power and authority is a belief held by citizens, whereas legitimacy is an institution named in a constitution",
     "The two terms mean the same thing and the framework uses them interchangeably",
     "A source of power and authority applies only to authoritarian regimes and legitimacy only to democracies",
     "Legitimacy is measured by the size of a state's armed forces"], ans=0,
   why="EK PAU-1.D.1 lists constitutions, religions, military forces, parties, legislatures and popular support as sources of power and authority, while EK LEG-1.A.1 defines legitimacy as whether a government's constituents believe it has the right to use power as it does. One concerns what a regime rules through, the other what its people accept."),
 dict(q="Which change to a regime would most directly alter the sources of its power and authority in the framework's sense?",
   choices=[
     "The armed forces cease to answer to the governing party and come under the command of an elected civilian government",
     "The legislature moves its sittings to a new building",
     "The governing party adopts a new set of colors and a new logo",
     "The state changes the design of its currency",
     "A ministry is renamed and its offices are relocated to another city"], ans=0,
   why="EK PAU-1.D.1 names military forces and political parties among the sources of power and authority, and EK PAU-1.D.1.a treats one party's control over the military as what supplied a regime with the power to remain stable. Removing that control moves the army from one source to another; symbols, buildings and names touch none of the six."),
 dict(q="One regime's stability is attributed by the framework to a party's command of the armed forces, another's to constitutional reform that redistributed authority to regional parliaments. What does the pairing show about the framework's account of stability?",
   choices=[
     "Stability can be produced by very different sources, so the source a regime rests on cannot be inferred from the fact that it is stable",
     "Only party control of the armed forces can produce stability",
     "Only constitutional reform can produce stability",
     "Stability is unrelated to any of the sources the framework names",
     "Stable regimes are always democratic and unstable ones always authoritarian"], ans=0,
   why="EK PAU-1.D.1.a attributes regime stability in China to the Communist Party's control over the military and EK PAU-1.D.1.e attributes the maintenance of stability in the United Kingdom to devolution by constitutional reform. Both are the framework's own words, so stability cannot identify a single source."),
 dict(q="The framework's devolution statement lists both benefits and costs. Which of the following pairs one of each as the framework does?",
   choices=[
     "Policy can be matched to local needs and central power checked, but policies across regions may contradict one another and interregional inequality may grow",
     "Policy is always made more efficient, and no offsetting costs arise",
     "Policy is always made less efficient, and no offsetting benefits arise",
     "Regional parliaments gain the power to amend the national constitution, and the national government loses its foreign policy powers",
     "Devolution converts a unitary state into a federal one and ends ethnic tension"], ans=0,
   why="EK LEG-1.B.4 lists policy innovation, matching policies to local needs, checking central power and better minority representation alongside contradictory policies, more complicated implementation, interregional inequality, competition for resources and exacerbated ethnic tensions, in a single two-sided statement. Treating devolution as unambiguously good or bad contradicts it."),
 dict(q="A comparativist argues that in one country the written constitution is a poor guide to where power actually lies. Which framework statements, taken together, most directly support the possibility of such a gap?",
   choices=[
     "That a constitution recognizes one body as the government's most powerful institution while a different body is the actual center of power in the state",
     "That constitutions are the only source of power and authority the framework names",
     "That every regime's constitution is amended after each election",
     "That a state must have a written constitution to be recognized internationally",
     "That the powers of a legislature are identical in every course country"], ans=0,
   why="EK PAU-3.E.1.a and EK PAU-3.F.1.a make both claims about the same state, the first about the constitution's recognition and the second about actual power. The framework therefore treats the two as separable questions rather than assuming the text describes the practice."),
 dict(q="What do all five of the framework's illustrations under this topic have in common?",
   choices=[
     "Each shows a regime being affected over time by one or more of the named sources of power and authority",
     "Each describes a regime moving from authoritarian rule to democracy",
     "Each describes a change brought about by an election",
     "Each concerns a country that is federal rather than unitary",
     "Each describes a change that occurred suddenly rather than over time"], ans=0,
   why="EK PAU-1.D.1 introduces the five with the statement that over time course country regimes have been affected by such sources. Two of the five are transitions toward multiparty republics, one is a transition to a theocracy, one describes elite backing of a presidency and one a constitutional reform, so the shared feature is the influence of a source rather than any common direction."),
]
