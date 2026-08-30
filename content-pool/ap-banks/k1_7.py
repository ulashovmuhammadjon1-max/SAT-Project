# AP COMPARATIVE GOVERNMENT AND POLITICS 1.7 Federal and Unitary Systems
# CED effective Fall 2026, Unit 1 Political Systems, Regimes, and Governments.
# Enduring understanding PAU-2 (distribution of power and authority and the
# influence of internal and external actors affect regime stability); learning
# objective PAU-2.A. Suggested skill 4.B, Source Analysis.
#
# Essential knowledge relied on:
#   PAU-2.A.1  FEDERAL states like MEXICO, NIGERIA and RUSSIA divide power among
#              different levels of government to confer a degree of local autonomy
#              in supplying SOCIAL AND EDUCATIONAL SERVICES, while also reserving
#              powers for the national government. UNITARY states like CHINA, IRAN
#              and the UNITED KINGDOM concentrate power at the national level with
#              more uniform policies and POTENTIALLY more efficient policy making.
#   PAU-2.A.2  the degree to which power is centralized or decentralized CAN CHANGE
#              OVER TIME IN BOTH federal and unitary states, and in many cases
#              reflects a state response to internal and external actors that
#              include ETHNIC CLEAVAGES and operations of SUPRANATIONAL
#              ORGANIZATIONS AND OTHER COUNTRIES
#
# Country statements used, each named in the verifier's claim:
#   PAU-1.D.1e constitutional reforms in the United Kingdom devolved power to
#              multiple parliaments, allowing the regime to maintain stability
#   DEM-2.B.5c Russia's federal districts with presidential envoys, and regional
#              legislatures forgoing elections to appoint a governor from a list
#              approved by the president, reasserted federal power under the
#              president
#   DEM-2.B.3b Nigeria's presidential distribution requirement reflects the federal
#              characteristic of the regime
#   PAU-3.E.1c Mexico's Senate holds the unique power to approve federal
#              intervention in state matters
#   PAU-3.G.1e under Nigeria's system of federalism, Islamic Sharia Courts have
#              been established in the north
#   PAU-3.G.1i the United Kingdom's Supreme Court rules on devolution disputes
#   LEG-1.B.4  devolution's benefits AND costs, listed in one statement
#
# THE TRAP THIS TOPIC EXISTS TO SET: the unitary list holds the course's clearest
# democracy and its clearest one-party state, and the federal list holds two
# multiparty republics and a competitive authoritarian regime. Territorial
# structure therefore does not track regime type, and the framework's own lists
# refute the generalization a student is most likely to bring (see
# AP_COMP_GOV_CED.md note 4). Items 4, 25 and 26 key that.
#
# Table figures are HYPOTHETICAL and labelled so; the framework prints no
# spending shares.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("1.7", "Federal and Unitary Systems", 1)

_T_FED = dict(
    headers=["Country (hypothetical)", "Constitutional structure",
             "Share of public spending decided by subnational governments, 2000",
             "Share of public spending decided by subnational governments, 2020"],
    rows=[["Country H", "federal", "38 percent", "26 percent"],
          ["Country J", "unitary", "11 percent", "24 percent"],
          ["Country K", "federal", "41 percent", "43 percent"]])

_T_SERV = dict(
    headers=["Policy area", "Share of a hypothetical sample of states in which the area is decided nationally",
             "Share in which it is decided subnationally"],
    rows=[["Defense", "100 percent", "0 percent"],
          ["Foreign affairs", "100 percent", "0 percent"],
          ["School curriculum", "45 percent", "55 percent"],
          ["Local social services", "20 percent", "80 percent"]])

QUESTIONS = [
 dict(q="Which grouping of the six course countries by territorial structure does the framework give?",
   choices=[
     "Federal: Mexico, Nigeria, Russia. Unitary: China, Iran, the United Kingdom",
     "Federal: China, Iran, Russia. Unitary: Mexico, Nigeria, the United Kingdom",
     "Federal: Mexico, Nigeria, the United Kingdom. Unitary: China, Iran, Russia",
     "Federal: China, Mexico, Nigeria. Unitary: Iran, Russia, the United Kingdom",
     "All six are unitary, since each has a single national government"], ans=0,
   why="EK PAU-2.A.1 names Mexico, Nigeria and Russia as federal states and China, Iran and the United Kingdom as unitary ones. The United Kingdom remains on the unitary list even though EK PAU-1.D.1.e records constitutional reforms devolving power to multiple parliaments."),
 dict(q="According to the framework, federal states divide power among levels of government in order to",
   choices=[
     "confer a degree of local autonomy in supplying social and educational services, while reserving powers for the national government",
     "transfer all social and educational services to the national government",
     "guarantee that every level of government holds identical powers",
     "eliminate the national government's role in policy making",
     "ensure that policies are uniform in every region"], ans=0,
   why="EK PAU-2.A.1 states that federal states divide power among different levels of government to confer a degree of local autonomy in supplying social and educational services, while also reserving powers for the national government. Uniformity is what the same statement attributes to unitary states."),
 dict(q="According to the framework, unitary states concentrate power at the national level, with what consequences?",
   choices=[
     "more uniform policies and potentially more efficient policy making",
     "greater local autonomy in supplying social and educational services",
     "a constitutional guarantee of regional legislative powers",
     "policy that necessarily matches local needs more closely",
     "the elimination of any subnational administration"], ans=0,
   why="EK PAU-2.A.1 attributes more uniform policies and potentially more efficient policy making to unitary states. Local autonomy in social and educational services is what the same statement attributes to federal states, and concentrating power at the national level does not abolish subnational administration."),
 dict(q="A student proposes that authoritarian regimes are unitary and democratic regimes federal. The framework's own lists refute this because",
   choices=[
     "the unitary group contains both a one-party state and a long-established democracy, and the federal group contains both multiparty republics and a regime the framework calls competitive authoritarian",
     "all six course countries are federal",
     "all six course countries are unitary",
     "the framework does not classify any country as federal or unitary",
     "the framework says federal states are always more democratic than unitary ones"], ans=0,
   why="EK PAU-2.A.1's unitary list holds China and the United Kingdom and its federal list holds Mexico, Nigeria and Russia, while EK DEM-1.C.5 characterizes Russia as a competitive authoritarian regime or illiberal democracy. Territorial structure and regime type are therefore separate classifications that cut across each other."),
 dict(q="What does the framework say about how centralized a state's power is over time?",
   choices=[
     "the degree of centralization or decentralization can change over time in both federal and unitary states",
     "the degree of centralization is fixed by a state's constitution and cannot change",
     "only federal states can become more or less centralized",
     "only unitary states can become more or less centralized",
     "centralization changes only when a state changes regime type"], ans=0,
   why="EK PAU-2.A.2 states that the degree to which power is centralized or decentralized can change over time in both federal and unitary states. The framework's own examples include a unitary state devolving power and a federal state reasserting central control."),
 dict(q="The framework says that changes in the degree of centralization often reflect a state's response to internal and external actors. Which actors does it name?",
   choices=[
     "ethnic cleavages, and the operations of supranational organizations and other countries",
     "political parties and interest groups alone",
     "the armed forces and the judiciary alone",
     "religious authorities and the electoral commission",
     "the media and public opinion polling firms"], ans=0,
   why="EK PAU-2.A.2 names ethnic cleavages and the operations of supranational organizations and other countries as the internal and external actors whose pressure such changes often reflect. One is internal and the others external, which is why the statement pairs them."),
 dict(q="Constitutional reforms in the United Kingdom that devolved power to multiple parliaments are best described in this topic's terms as",
   choices=[
     "a unitary state decentralizing without ceasing to be unitary",
     "a unitary state becoming a federal state",
     "a federal state centralizing power at the national level",
     "a federal state dividing itself into several sovereign states",
     "a change that the framework says had no effect on stability"], ans=0,
   why="EK PAU-2.A.1 still lists the United Kingdom among the unitary states, and EK PAU-1.D.1.e records that the reforms devolved power to multiple parliaments and allowed the regime to maintain stability. EK PAU-2.A.2 makes such a change possible within either structure."),
 dict(q="Russia's creation of federal districts headed by presidential envoys, together with the rule allowing regional legislatures to appoint a governor from a list approved by the president, is best described in this topic's terms as",
   choices=[
     "a federal state centralizing power under the national executive",
     "a federal state decentralizing power to its regions",
     "a unitary state devolving power to regional parliaments",
     "a unitary state abolishing its regional administration",
     "a change with no bearing on the balance between levels of government"], ans=0,
   why="EK DEM-2.B.5.c presents both measures as reasserting federal power under the Russian president, and EK PAU-2.A.1 lists Russia among the federal states. EK PAU-2.A.2 allows the degree of centralization to change within a federal structure, which is what these measures do."),
 dict(q="The framework notes that Islamic Sharia Courts have been established in the north of one course country. It presents this as a consequence of",
   choices=[
     "that country's system of federalism",
     "that country's unitary concentration of power at the national level",
     "a supranational organization's requirement",
     "a constitutional amendment abolishing judicial review",
     "the national executive's power to appoint all judges"], ans=0,
   why="EK PAU-3.G.1.e states that under Nigeria's system of federalism, Islamic Sharia Courts have been established in the north. EK PAU-2.A.1 lists Nigeria among the federal states, and a legal order differing by region is what a division of power among levels of government makes possible."),
 dict(q="Nigeria requires a winning presidential candidate to take at least 25 percent of the vote in two-thirds of the states as well as the most votes nationally. The framework presents this rule as reflecting",
   choices=[
     "the federal characteristic of the regime",
     "the unitary concentration of power at the national level",
     "the influence of a supranational organization",
     "a requirement imposed by the judiciary",
     "the absence of any subnational government"], ans=0,
   why="EK DEM-2.B.3.b states that the distribution requirement reflects the federal characteristic of the Nigerian regime, and EK PAU-2.A.1 lists Nigeria among the federal states. The rule makes the constituent units, not only the national electorate, part of how the presidency is won."),
 dict(q="Which power does the framework assign to Mexico's Senate that bears directly on the relationship between levels of government?",
   choices=[
     "approving federal intervention in state matters",
     "appointing the governors of the states",
     "drawing the boundaries of the states",
     "admitting new states to the federation",
     "levying all taxes collected within the states"], ans=0,
   why="EK PAU-3.E.1.c gives Mexico's Senate the unique power to confirm presidential appointments to the Supreme Court, approve treaties, and approve federal intervention in state matters. The last of these is the point at which the national and state levels meet, which is what makes it a federal power."),
 dict(q="Among the functions the framework assigns to the United Kingdom's Supreme Court is",
   choices=[
     "ruling on devolution disputes",
     "approving federal intervention in the affairs of regional governments",
     "appointing the members of the devolved parliaments",
     "certifying the results of general elections",
     "nominating half the members of the upper chamber"], ans=0,
   why="EK PAU-3.G.1.i names serving as the final court of appeals, protecting human and civil rights and liberties, and ruling on devolution disputes among the Supreme Court's major functions. A unitary state that has devolved power still needs an authority to settle which level may act."),
 dict(q="Which comparison of the United Kingdom and Russia is supported by the framework?",
   choices=[
     "A unitary state has devolved power to regional parliaments while a federal state has reasserted central power over its regions",
     "A federal state has devolved power to regional parliaments while a unitary state has reasserted central power",
     "Both states have moved in the same direction, toward greater decentralization",
     "Both states have moved in the same direction, toward greater centralization",
     "Neither state's balance between levels of government has changed"], ans=0,
   why="EK PAU-2.A.1 classifies the United Kingdom as unitary and Russia as federal, EK PAU-1.D.1.e records devolution to multiple parliaments in the first, and EK DEM-2.B.5.c records the reassertion of federal power under the president in the second. EK PAU-2.A.2 is the statement that allows both movements to occur inside unchanged structures."),
 dict(q="The framework's claim about efficiency in unitary states is best stated as",
   choices=[
     "concentrating power at the national level makes more uniform policies and potentially more efficient policy making possible",
     "concentrating power at the national level always makes policy making more efficient",
     "concentrating power at the national level always makes policy making less efficient",
     "efficiency is unrelated to whether a state is federal or unitary",
     "only federal states can make policy efficiently"], ans=0,
   why="EK PAU-2.A.1 says unitary states concentrate power at the national level with more uniform policies and POTENTIALLY more efficient policy making. The hedge is the framework's own, and dropping it turns a conditional claim into a guarantee the statement does not make."),
 dict(q="A commentator writes that federal systems are simply inefficient and unitary systems simply efficient. Which framework statement most directly complicates that judgement?",
   choices=[
     "that devolution creates both opportunities for and obstacles to resolving social, political, and economic issues, listing benefits and costs together",
     "that all six course countries are unitary",
     "that federal states reserve no powers for the national government",
     "that unitary states never adjust the balance of power between levels",
     "that efficiency is the only criterion by which a territorial structure may be judged"], ans=0,
   why="EK LEG-1.B.4 lists policy innovation, matching policies to local needs, checking central power and better minority representation alongside contradictory policies, complicated implementation, interregional inequality and exacerbated tensions, in a single two-sided statement. EK PAU-2.A.1's own efficiency claim is hedged with 'potentially' for the same reason."),
 dict(q="Which of the following does the framework list among the benefits of devolving and delegating power to regional governments?",
   choices=[
     "matching policies to local needs and allowing better representation of religious, ethnic and minority groups",
     "guaranteeing that policies will be identical across every region",
     "removing the need for a national government",
     "increasing the uniformity of public services across the state",
     "ensuring that every region raises the same amount of revenue"], ans=0,
   why="EK LEG-1.B.4.a lists promoting policy innovation, matching policies to local needs, improving policies through competition, increasing political participation, checking central power and allowing better representation of religious, ethnic and minority groups. Uniformity is what EK PAU-2.A.1 attributes to unitary concentration instead."),
 dict(q="Which of the following does the framework list among the costs of devolving and delegating power to regional governments?",
   choices=[
     "contradictory policies across regions, inequality between regions, and exacerbated ethnic and local tensions",
     "the loss of the national government's foreign policy powers",
     "the automatic conversion of a unitary state into a federal one",
     "the abolition of judicial review",
     "the requirement that every region adopt the same policies"], ans=0,
   why="EK LEG-1.B.4.b lists creating contradictory policies, making implementation more complicated and inefficient, allowing inequality between regions, increasing competition for resources and exacerbating ethnic and local tensions. The framework states these in the same sentence as the benefits, so devolution is two-sided in its account."),
 dict(q="A state adopts a single national curriculum, a single national health service structure, and identical local government powers in every region, all set by the national ministry. This is most characteristic of",
   choices=[
     "a unitary state concentrating power at the national level",
     "a federal state conferring local autonomy on its constituent units",
     "a confederation of sovereign states",
     "a state that has devolved power to multiple parliaments",
     "a state whose regions each maintain their own legal system"], ans=0,
   why="EK PAU-2.A.1 attributes to unitary states the concentration of power at the national level with more uniform policies. Identical curricula, structures and powers set centrally are that uniformity, and they are the opposite of the local autonomy the same statement attributes to federal states."),
 dict(q="In a second state, constituent units set their own school curricula, run their own social services, and may legislate on matters not reserved to the national government. This is most characteristic of",
   choices=[
     "a federal state dividing power among levels of government",
     "a unitary state concentrating power at the national level",
     "a state that has abolished its national government",
     "a state whose policies are uniform across every region",
     "a theocracy in which religious authorities make all policy"], ans=0,
   why="EK PAU-2.A.1 describes federal states dividing power among different levels of government to confer a degree of local autonomy in supplying social and educational services, while reserving powers for the national government. Both halves of that description appear in the scenario."),
 dict(q="The table reports hypothetical subnational spending shares in three states. Which pair of countries together illustrates the framework's statement that the degree of centralization can change over time in both federal and unitary states?",
   table=_T_FED,
   choices=[
     "Country H and Country J, since the federal state's subnational share fell while the unitary state's rose",
     "Country H and Country K, since both are federal",
     "Country J alone, since only a unitary state can change its degree of centralization",
     "Country K alone, since its share changed least",
     "None of them, since a state's degree of centralization is fixed by its constitution"], ans=0,
   why="EK PAU-2.A.2 states that the degree of centralization or decentralization can change over time in BOTH federal and unitary states, so the illustration needs one of each moving. Two rows of the same structure would show only half of the claim."),
 dict(q="Using the same table, the country whose subnational spending share changed least over the period is",
   table=_T_FED,
   choices=[
     "Country K, by 2 percentage points",
     "Country H, by 12 percentage points",
     "Country J, by 13 percentage points",
     "Country K, by 43 percentage points",
     "The table does not permit the comparison"], ans=0,
   why="Subtracting each country's 2000 share from its 2020 share gives changes of twelve, thirteen and two percentage points in some order, and the smallest of those is the answer. The largest figure offered for the same country is its final share rather than its change."),
 dict(q="A student concludes from the same table that the unitary state has become a federal state. The best objection is that",
   table=_T_FED,
   choices=[
     "the table reports how spending is decided, whereas the framework's classification turns on how power is divided constitutionally, and it expressly allows centralization to change within either structure",
     "the table reports no information about subnational government",
     "a unitary state's subnational share can never rise",
     "spending shares are the only evidence the framework accepts for classification",
     "the framework does not classify states as federal or unitary at all"], ans=0,
   why="EK PAU-2.A.1 defines the two structures by how power is divided among levels of government, not by a spending ratio, and EK PAU-2.A.2 says the degree of centralization can change within both. The United Kingdom is the framework's own case of a unitary state that has devolved power and remained unitary."),
 dict(q="The table reports, for a hypothetical sample of states, the share deciding each policy area nationally and subnationally. Which conclusion does it support?",
   table=_T_SERV,
   choices=[
     "The two areas the framework associates with local autonomy are decided subnationally in most of the sample, while defense and foreign affairs are decided nationally throughout it",
     "Every policy area in the table is decided nationally in most of the sample",
     "Every policy area in the table is decided subnationally in most of the sample",
     "Defense is decided subnationally more often than school curriculum is",
     "The sample contains no state in which any area is decided subnationally"], ans=0,
   why="EK PAU-2.A.1 names social and educational services as what federal division of power confers local autonomy over, while reserving powers for the national government. Reading the rows, those two areas are majority subnational and the two classic national functions are unanimously national."),
 dict(q="Using the same table, the policy area with the largest gap between the share deciding it nationally and the share deciding it subnationally, among the areas not decided nationally throughout the sample, is",
   table=_T_SERV,
   choices=[
     "local social services, with a gap of 60 percentage points",
     "school curriculum, with a gap of 10 percentage points",
     "local social services, with a gap of 80 percentage points",
     "school curriculum, with a gap of 55 percentage points",
     "defense, with a gap of 100 percentage points"], ans=0,
   why="The question excludes the areas decided nationally throughout the sample, leaving two rows; subtracting the smaller share from the larger within each of those rows gives the gap. The larger figures offered are single column values rather than differences."),
 dict(q="China and the United Kingdom are both unitary states in the framework's classification, yet they differ sharply in regime type. What follows?",
   choices=[
     "Territorial structure carries no implication about a state's place on the democratic-authoritarian scale",
     "One of the two must have been misclassified by the framework",
     "Unitary structure is evidence of authoritarianism",
     "Unitary structure is evidence of democracy",
     "Regime type and territorial structure are two names for the same classification"], ans=0,
   why="EK PAU-2.A.1 places China, Iran and the United Kingdom in the same unitary group while EK PAU-1.B.1 supplies an entirely separate set of indicators for regime type. Two states can share the first classification and diverge on the second, which is what these two do."),
 dict(q="Mexico, Nigeria and Russia are all federal states in the framework's classification. What does that grouping show?",
   choices=[
     "that a federal division of power is compatible with more than one regime type, since the framework describes two of these states as multiparty republics and the third as a competitive authoritarian regime",
     "that federal states are always democratic",
     "that federal states are always authoritarian",
     "that these three states have identical political institutions",
     "that federalism prevents a national executive from gaining power over the regions"], ans=0,
   why="EK PAU-2.A.1 groups the three as federal, EK PAU-1.D.1.c describes Nigeria and Mexico as multiparty republics, and EK DEM-1.C.5 characterizes Russia as a competitive authoritarian regime or illiberal democracy. EK DEM-2.B.5.c further shows a federal structure accommodating the reassertion of central power."),
 dict(q="A state with a large, territorially concentrated linguistic minority creates a regional assembly with authority over education and cultural policy in that region. Which framework statement best accounts for the change?",
   choices=[
     "that the degree of centralization often reflects a state's response to internal actors including ethnic cleavages",
     "that unitary states concentrate power at the national level with more uniform policies",
     "that governments change more frequently and easily than regimes",
     "that authoritarian regimes prefer secret or closed proceedings",
     "that a state must have international recognition to be sovereign"], ans=0,
   why="EK PAU-2.A.2 states that changes in the degree of centralization in many cases reflect a state response to internal and external actors that include ethnic cleavages. EK LEG-1.B.4.a adds better representation of religious, ethnic and minority groups among devolution's benefits, which is what such an assembly is for."),
 dict(q="A state transfers authority over several areas of regulation to a supranational body it has joined, and at the same time transfers others to its regions. In the framework's terms this is",
   choices=[
     "a change in the degree of centralization reflecting the operations of a supranational organization as well as internal pressure",
     "a change of regime, since the rules of access to power have been replaced",
     "a loss of statehood, since a state cannot share regulatory authority",
     "proof that the state has become federal",
     "unrelated to the framework's account of centralization"], ans=0,
   why="EK PAU-2.A.2 names the operations of supranational organizations and other countries among the external actors whose influence such changes reflect, alongside internal ethnic cleavages. EK PAU-1.A.2's rules of access to power are untouched by a reallocation of regulatory authority, so no regime change is involved."),
 dict(q="Which finding would most strongly support a claim that a federal state has become more centralized?",
   choices=[
     "The national executive has acquired the power to shape who holds regional office, and areas formerly decided by the constituent units are now decided nationally",
     "The number of constituent units in the federation has increased",
     "The national legislature has moved to a new building",
     "A regional government has changed the party in control of its assembly",
     "The state has been admitted to a new international organization"], ans=0,
   why="EK PAU-2.A.2 makes the degree of centralization the thing that changes, and EK DEM-2.B.5.c gives the framework's own instance of it, a national executive shaping who holds regional office. Counting units, relocating a legislature, a regional election result and treaty membership do not by themselves move authority between levels."),
 dict(q="Taking the framework's two statements on territorial structure together, which summary is most accurate?",
   choices=[
     "States are classified as federal or unitary by how power is divided among levels of government, and the degree of centralization within either classification can shift over time in response to internal and external pressures",
     "States are classified as federal or unitary by regime type, and the classification cannot change",
     "Only federal states divide power among levels of government, and only unitary states respond to external pressure",
     "The classification determines a state's degree of democracy and its efficiency",
     "The framework classifies states only by whether their governments are democratic"], ans=0,
   why="EK PAU-2.A.1 supplies the classification and what each structure is for, and EK PAU-2.A.2 supplies the movement within it and the internal and external actors that drive that movement. Keeping both means treating structure as fixed while the degree of centralization is not."),
]
