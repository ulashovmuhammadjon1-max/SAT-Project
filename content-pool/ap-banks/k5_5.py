# AP COMPARATIVE GOVERNMENT AND POLITICS 5.5 International and Supranational
# Organizations
# CED effective Fall 2026, Unit 5 Political and Economic Changes and Development.
# Enduring understanding LEG-3 (a government bolsters regime stability by adapting
# its policies to environmental, political, economic, and cultural conditions);
# learning objective LEG-3.A (explain how international and supranational
# organizations influence domestic policymakers and national sovereignty).
# Suggested skill 4.B, Source Analysis.
#
# Essential knowledge relied on:
#   LEG-3.A.1  INTERNATIONAL ORGANIZATIONS like the INTERNATIONAL MONETARY FUND and
#              the WORLD BANK EXERT GREAT INFLUENCE THROUGH PRECONDITIONS FOR
#              FINANCIAL ASSISTANCE; countries that receive IMF assistance OFTEN MUST
#              AGREE TO STRUCTURAL ADJUSTMENT PROGRAMS REQUIRING PRIVATIZATION OF
#              STATE-OWNED COMPANIES, REDUCED TARIFFS, and REDUCED GOVERNMENTAL
#              SUBSIDIES OF DOMESTIC INDUSTRIES
#   LEG-3.A.2  TO BOLSTER THEIR OWN DEVELOPING INDUSTRIES, some countries pass IMPORT
#              SUBSTITUTION INDUSTRIALIZATION (ISI) POLICIES AIMED AT REDUCING FOREIGN
#              DEPENDENCY by RAISING TARIFFS and ENCOURAGING LOCAL PRODUCTION OF
#              INDUSTRIALIZED PRODUCTS
#   LEG-3.A.3  SUPRANATIONAL ORGANIZATIONS such as the ECONOMIC COMMUNITY OF WEST
#              AFRICAN STATES, the EUROPEAN UNION and the WORLD TRADE ORGANIZATION
#              HAVE SOVEREIGN POWERS OVER THE NATIONAL GOVERNMENTS THAT ARE MEMBER
#              STATES and CAN APPLY PRESSURE ON POLICYMAKERS TO REDUCE TARIFFS AND
#              OTHERWISE LIBERALIZE TRADE
#   DEM-1.A.5  the UNITED KINGDOM HAS USED REFERENDA to decide questions including
#              THEIR WITHDRAWAL FROM THE EUROPEAN UNION
#
# THE TARIFF GOES BOTH WAYS, AND THAT IS THE TOPIC. Structural adjustment requires
# REDUCED tariffs (LEG-3.A.1); supranational organizations press to REDUCE tariffs
# (LEG-3.A.3); import substitution industrialization RAISES them (LEG-3.A.2). Two
# of the framework's three statements push a government one way and the third
# pushes it the other, for a reason the framework also states -- reducing foreign
# dependency. Items 10, 17 and 24-27 all turn on that opposition, and a student
# who has filed "international organizations mean free trade" has no way to place
# ISI.
#
# THE TWO MECHANISMS ARE NOT THE SAME. An international organization exerts
# influence through PRECONDITIONS FOR FINANCIAL ASSISTANCE -- a government that
# wants the money accepts the terms, and one that does not want the money is not
# bound. A supranational organization has SOVEREIGN POWERS OVER the national
# governments that are its member states, which is authority rather than leverage.
# Items 11, 18 and 28-29 key that distinction, and it is the reason the learning
# objective mentions national sovereignty at all.
#
# WHAT IS DELIBERATELY NOT ASSERTED: no course country is placed in any named
# organization except where the framework itself does so. The one membership claim
# in the module is DEM-1.A.5's, that the United Kingdom used a referendum to decide
# its withdrawal from the European Union, which the CED states and which is a
# settled past event rather than a moving condition. No loan, programme, tariff
# schedule or negotiation of any real country is asserted anywhere. Every table
# figure is HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("5.5", "International and Supranational Organizations", 5)

_T_SAP = dict(
    headers=["Condition attached to financial assistance",
             "Borrowing governments accepting it, of 40 receiving assistance (hypothetical)"],
    rows=[["Privatization of state-owned companies", "35"],
          ["Reduced tariffs", "18"],
          ["Reduced governmental subsidies of domestic industries", "29"]])

_T_TARIFF = dict(
    headers=["Programme (hypothetical)", "Average tariff before the programme (percent)",
             "Average tariff after the programme (percent)", "Stated aim of the programme"],
    rows=[["Programme 1", "24", "9", "To meet the conditions attached to external financial assistance"],
          ["Programme 2", "11", "27", "To reduce dependence on foreign goods by building up local production"]])

_T_ORG = dict(
    headers=["Organization (hypothetical)", "How it acts on the governments it deals with"],
    rows=[["Organization 1", "Attaches conditions to the financial assistance it agrees to provide"],
          ["Organization 2", "Holds sovereign powers over the national governments that are its member states"]])

QUESTIONS = [
 dict(q="Through what does the framework say international organizations such as the International Monetary Fund and the World Bank exert great influence?",
   choices=[
     "preconditions for financial assistance",
     "the deployment of peacekeeping forces",
     "the power to annul a member state's legislation",
     "the appointment of ministers in borrowing countries",
     "the setting of exchange rates by treaty"], ans=0,
   why="EK LEG-3.A.1 states that international organizations like the International Monetary Fund and the World Bank exert great influence through preconditions for financial assistance, so the leverage lies in the terms attached to money a government wants."),
 dict(q="What does the framework say countries receiving assistance from the International Monetary Fund often must agree to?",
   choices=[
     "structural adjustment programs",
     "membership in a supranational organization",
     "import substitution industrialization policies",
     "the transfer of their natural resources to foreign owners",
     "the holding of a referendum on the loan"], ans=0,
   why="EK LEG-3.A.1 states that countries that receive assistance from the International Monetary Fund often must agree to structural adjustment programs, which is the vehicle the preconditions travel in."),
 dict(q="Which requirements does the framework say structural adjustment programs impose?",
   choices=[
     "privatization of state-owned companies, reduced tariffs, and reduced governmental subsidies of domestic industries",
     "nationalization of key industries, higher tariffs, and larger subsidies",
     "the adoption of a written constitution and competitive elections",
     "the creation of special economic zones and joint ventures",
     "the imposition of limits on foreign investment"], ans=0,
   why="EK LEG-3.A.1 names privatization of state-owned companies, reduced tariffs, and reduced governmental subsidies of domestic industries as the requirements of structural adjustment programs."),
 dict(q="What does the framework say import substitution industrialization policies are aimed at?",
   choices=[
     "reducing foreign dependency",
     "meeting the conditions attached to external loans",
     "joining a supranational organization",
     "increasing the flow of imported manufactured goods",
     "transferring state industries to private owners"], ans=0,
   why="EK LEG-3.A.2 states that some countries pass import substitution industrialization policies aimed at reducing foreign dependency, which is the purpose the framework attaches to the policy."),
 dict(q="By which two means does the framework say import substitution industrialization pursues that aim?",
   choices=[
     "raising tariffs and encouraging local production of industrialized products",
     "lowering tariffs and privatizing state-owned companies",
     "borrowing abroad and reducing subsidies",
     "joining a customs union and adopting a common currency",
     "opening special economic zones and inviting foreign investment"], ans=0,
   why="EK LEG-3.A.2 states that import substitution industrialization policies work by raising tariffs and encouraging local production of industrialized products, so the barrier and the domestic build-up operate together."),
 dict(q="Whose industries does the framework say import substitution industrialization is meant to bolster?",
   choices=[
     "the passing country's own developing industries",
     "the industries of the country's principal trading partner",
     "industries owned by multinational corporations",
     "industries within a supranational organization's member states",
     "industries designated by an international lender"], ans=0,
   why="EK LEG-3.A.2 opens by stating that these policies are passed to bolster the country's own developing industries, which is why they raise barriers against goods produced elsewhere."),
 dict(q="Which organizations does the framework give as examples of supranational organizations?",
   choices=[
     "the Economic Community of West African States, the European Union, and the World Trade Organization",
     "the International Monetary Fund, the World Bank, and the United Nations",
     "the World Health Organization, the International Labour Organization, and the African Union",
     "the International Court of Justice, the United Nations, and the World Bank",
     "the International Monetary Fund, the European Union, and the World Health Organization"], ans=0,
   why="EK LEG-3.A.3 names the Economic Community of West African States, the European Union, and the World Trade Organization as supranational organizations, and EK LEG-3.A.1 treats the International Monetary Fund and the World Bank separately as international organizations acting through loan conditions."),
 dict(q="What does the framework say supranational organizations hold over the national governments that are their member states?",
   choices=[
     "sovereign powers",
     "a right of military intervention",
     "the power to appoint their heads of government",
     "ownership of their natural resources",
     "no authority of any kind"], ans=0,
   why="EK LEG-3.A.3 states that supranational organizations have sovereign powers over the national governments that are member states, which is authority over the member rather than leverage exercised through an offer."),
 dict(q="What pressure does the framework say supranational organizations apply to policymakers?",
   choices=[
     "to reduce tariffs and otherwise liberalize trade",
     "to raise tariffs and restrict imports",
     "to nationalize their energy industries",
     "to withdraw from international financial organizations",
     "to increase subsidies for domestic producers"], ans=0,
   why="EK LEG-3.A.3 states that supranational organizations can apply pressure on policymakers to reduce tariffs and otherwise liberalize trade, which runs in the same direction as the conditions in EK LEG-3.A.1."),
 dict(q="How do import substitution industrialization policies stand in relation to what structural adjustment programs and supranational organizations press for on tariffs?",
   choices=[
     "they move tariffs in the opposite direction, since they raise them while the others press for reductions",
     "they move tariffs in the same direction, since all three reduce them",
     "they move tariffs in the same direction, since all three raise them",
     "they leave tariffs unchanged while the others alter them",
     "they concern subsidies rather than tariffs"], ans=0,
   why="EK LEG-3.A.1 requires reduced tariffs and EK LEG-3.A.3 has supranational organizations pressing to reduce tariffs, while EK LEG-3.A.2 states that import substitution industrialization works by raising them."),
 dict(q="How does the influence the framework attributes to the International Monetary Fund differ from the powers it attributes to a supranational organization?",
   choices=[
     "one operates through conditions a government accepts in order to receive assistance, while the other is a sovereign power held over a government that is a member state",
     "one operates through military force and the other through diplomacy",
     "one applies only to democracies and the other only to authoritarian regimes",
     "one concerns trade and the other concerns human rights",
     "there is no difference, since both are treaty organizations"], ans=0,
   why="EK LEG-3.A.1 describes influence exerted through preconditions for financial assistance while EK LEG-3.A.3 states that supranational organizations have sovereign powers over the national governments that are member states, so one is leverage over a request and the other is authority over a member."),
 dict(q="Which course country does the framework record as having used a referendum to decide a question about membership of a supranational organization?",
   choices=[
     "the United Kingdom",
     "Nigeria",
     "Mexico",
     "China",
     "Iran"], ans=0,
   why="EK DEM-1.A.5 states that the United Kingdom has used referenda to decide questions including their withdrawal from the European Union, and EK LEG-3.A.3 names the European Union among the supranational organizations with sovereign powers over member states."),
 dict(q="A government raises duties on imported manufactured goods and funds a programme to expand domestic factories making the same goods. Which framework policy does this describe?",
   choices=[
     "import substitution industrialization",
     "a structural adjustment program",
     "accession to a supranational organization",
     "a special economic zone",
     "a joint venture with a foreign firm"], ans=0,
   why="EK LEG-3.A.2 states that import substitution industrialization policies aim at reducing foreign dependency by raising tariffs and encouraging local production of industrialized products, and the scenario contains both instruments."),
 dict(q="In exchange for financial assistance, a government agrees to sell several state-owned firms, cut import duties, and end its support payments to domestic producers. Which framework policy does this describe?",
   choices=[
     "a structural adjustment program required as a precondition for assistance",
     "an import substitution industrialization programme",
     "the exercise of sovereign powers by a supranational organization",
     "the creation of a special economic zone",
     "the re-nationalization of an energy industry"], ans=0,
   why="EK LEG-3.A.1 states that countries receiving assistance from the International Monetary Fund often must agree to structural adjustment programs requiring privatization of state-owned companies, reduced tariffs, and reduced governmental subsidies of domestic industries, and the scenario contains all three."),
 dict(q="A writer argues that when a lender can set the terms on which a country obtains funds it needs, elected ministers end up implementing decisions they did not take. Which framework claim does this argument rest on?",
   choices=[
     "that international organizations exert great influence through preconditions for financial assistance",
     "that supranational organizations hold sovereign powers over member states",
     "that import substitution policies reduce foreign dependency",
     "that governments raise tariffs to protect developing industries",
     "that multinational corporations dominate global markets"], ans=0,
   why="EK LEG-3.A.1 states that international organizations exert great influence through preconditions for financial assistance, which is the mechanism the argument describes, whereas sovereign powers under EK LEG-3.A.3 would not require the country to be seeking funds."),
 dict(q="Another writer argues that a poor country should accept higher prices at home for a period in order to build factories of its own rather than buy manufactured goods abroad. Which framework policy does this argument defend?",
   choices=[
     "import substitution industrialization",
     "a structural adjustment program",
     "membership in a supranational organization",
     "the reduction of tariffs to liberalize trade",
     "the privatization of state-owned companies"], ans=0,
   why="EK LEG-3.A.2 states that import substitution industrialization policies aim at reducing foreign dependency by raising tariffs and encouraging local production of industrialized products, which is the trade-off the argument accepts."),
 dict(q="Why can the framework's three statements leave a single government facing pressures that point in opposite directions?",
   choices=[
     "because a loan condition and a supranational organization both press tariffs down while a policy meant to reduce foreign dependency presses them up",
     "because international organizations require higher tariffs and supranational organizations require lower ones",
     "because supranational organizations have no view about trade",
     "because import substitution and structural adjustment are the same policy",
     "because the framework describes only one of these pressures at a time"], ans=0,
   why="EK LEG-3.A.1 requires reduced tariffs as a condition of assistance and EK LEG-3.A.3 has supranational organizations pressing to reduce tariffs and otherwise liberalize trade, while EK LEG-3.A.2's import substitution industrialization raises tariffs to reduce foreign dependency."),
 dict(q="What does the framework's phrase about supranational organizations holding sovereign powers over member states most directly imply for national sovereignty?",
   choices=[
     "that on the matters covered, a member government's decisions are subject to an authority above it",
     "that member governments cease to exist as states",
     "that member governments may ignore the organization's decisions at will",
     "that the organization takes ownership of the member's territory",
     "that membership has no bearing on what a government may decide"], ans=0,
   why="EK LEG-3.A.3 states that supranational organizations have sovereign powers over the national governments that are member states, and the learning objective for EK LEG-3.A is to explain how such organizations influence domestic policymakers and national sovereignty."),
 dict(q="Which finding would most strongly support a claim that a government had entered a structural adjustment program of the kind the framework describes?",
   choices=[
     "In the year it obtained external financial assistance, it transferred state-owned companies to private owners, lowered import duties, and withdrew subsidies from domestic producers",
     "In the year it obtained assistance, it raised import duties and expanded subsidies to domestic producers",
     "It joined a supranational organization and adopted its trade rules",
     "It nationalized its energy industry and limited foreign investment",
     "It held a referendum on membership of a regional body"], ans=0,
   why="EK LEG-3.A.1 names privatization of state-owned companies, reduced tariffs, and reduced governmental subsidies of domestic industries as the requirements of a structural adjustment program, so the supporting finding has to show all three alongside the assistance."),
 dict(q="A commentator claims that international and supranational organizations have no real bearing on what a national government does. Which reply is best supported by the framework?",
   choices=[
     "The framework says international organizations exert great influence through preconditions for assistance and that supranational organizations hold sovereign powers over member states and press policymakers on tariffs",
     "The framework says these organizations act only on countries that are not sovereign",
     "The framework says these organizations may only make recommendations",
     "The framework says these organizations act only through military means",
     "The framework says national governments always refuse their conditions"], ans=0,
   why="EK LEG-3.A.1 attributes great influence to preconditions for financial assistance and EK LEG-3.A.3 attributes sovereign powers over member states together with pressure to reduce tariffs and otherwise liberalize trade."),
 dict(q="The table records how many of forty hypothetical borrowing governments accepted each condition attached to financial assistance. Which condition was accepted by the most?",
   table=_T_SAP,
   choices=[
     "privatization of state-owned companies, accepted by 35",
     "reduced governmental subsidies of domestic industries, accepted by 29",
     "reduced tariffs, accepted by 18",
     "none of them, since the framework names no such conditions",
     "all three equally"], ans=0,
   why="EK LEG-3.A.1 names privatization of state-owned companies, reduced tariffs, and reduced governmental subsidies of domestic industries as the requirements of structural adjustment programs, so the table's three rows are the framework's own three conditions."),
 dict(q="According to the same table, the total number of acceptances recorded across the three conditions is",
   table=_T_SAP,
   choices=[
     "82",
     "64",
     "53",
     "47",
     "35"], ans=0,
   why="Adding the column across the three rows gives the total. The alternatives are the total with the smallest row omitted, the largest and smallest rows added, the total with the largest row omitted, and the largest single row."),
 dict(q="Using the same table, how many more governments accepted the most widely accepted condition than accepted the least widely accepted one?",
   table=_T_SAP,
   choices=[
     "17",
     "6",
     "11",
     "35",
     "18"], ans=0,
   why="Subtracting the smallest row from the largest gives the difference. The alternatives are the other two gaps within the same column and the two extreme rows read as though they were differences."),
 dict(q="The table describes two hypothetical tariff programmes. Which one matches the framework's account of import substitution industrialization?",
   table=_T_TARIFF,
   choices=[
     "the programme that raised the average tariff and was aimed at building up local production",
     "the programme that lowered the average tariff to meet external conditions",
     "both, since each changed the average tariff",
     "neither, since import substitution does not involve tariffs",
     "the programme with the lower tariff after it was carried out"], ans=0,
   why="EK LEG-3.A.2 states that import substitution industrialization aims at reducing foreign dependency by raising tariffs and encouraging local production of industrialized products, so the matching programme must both raise the tariff and state that aim."),
 dict(q="Using the same table of programmes, which one matches the framework's account of a structural adjustment program?",
   table=_T_TARIFF,
   choices=[
     "the programme that lowered the average tariff in order to meet the conditions attached to external financial assistance",
     "the programme that raised the average tariff to build up local production",
     "both, since each was carried out by a government",
     "neither, since structural adjustment does not concern tariffs",
     "the programme with the higher tariff after it was carried out"], ans=0,
   why="EK LEG-3.A.1 names reduced tariffs among the requirements of structural adjustment programs and states that those requirements arrive as preconditions for financial assistance, so the matching programme must lower the tariff and give that reason."),
 dict(q="According to the same table of programmes, the fall in the average tariff under the first programme is",
   table=_T_TARIFF,
   choices=[
     "15 percentage points",
     "16 percentage points",
     "24 percentage points",
     "9 percentage points",
     "27 percentage points"], ans=0,
   why="Subtracting the later average tariff from the earlier one in that row gives the fall. The alternatives are the change recorded in the other row and the individual figures in the table read as though they were changes."),
 dict(q="Using the same table of programmes, the rise in the average tariff under the second programme is",
   table=_T_TARIFF,
   choices=[
     "16 percentage points",
     "15 percentage points",
     "11 percentage points",
     "27 percentage points",
     "24 percentage points"], ans=0,
   why="Subtracting the earlier average tariff from the later one in that row gives the rise. The alternatives are the change recorded in the other row and the individual figures in the table read as though they were changes."),
 dict(q="The table describes two hypothetical organizations. Which one acts in the way the framework attributes to the International Monetary Fund and the World Bank?",
   table=_T_ORG,
   choices=[
     "the one that attaches conditions to the financial assistance it agrees to provide",
     "the one that holds sovereign powers over the national governments that are its member states",
     "both, since each deals with national governments",
     "neither, since the framework describes no such organizations",
     "the one whose decisions bind a government whether or not it seeks assistance"], ans=0,
   why="EK LEG-3.A.1 states that international organizations like the International Monetary Fund and the World Bank exert great influence through preconditions for financial assistance, which is leverage over a government seeking funds rather than authority over a member."),
 dict(q="Using the same table of organizations, which one acts in the way the framework attributes to a supranational organization?",
   table=_T_ORG,
   choices=[
     "the one that holds sovereign powers over the national governments that are its member states",
     "the one that attaches conditions to the assistance it provides",
     "both, since each influences policy",
     "neither, since supranational organizations have no powers",
     "the one whose influence depends on a government wanting money"], ans=0,
   why="EK LEG-3.A.3 states that supranational organizations such as the Economic Community of West African States, the European Union, and the World Trade Organization have sovereign powers over the national governments that are member states."),
 dict(q="Taking EK LEG-3.A as a whole, which summary is most accurate?",
   choices=[
     "International lenders shape policy through the conditions they attach to assistance, supranational bodies hold sovereign powers over their member states and press for lower tariffs, and a country seeking to reduce its dependence on foreign goods may raise tariffs instead, so a government can face pressures pointing opposite ways",
     "All the organizations the framework names press governments in the same direction",
     "These organizations affect trade policy but never bear on national sovereignty",
     "Only supranational organizations influence domestic policymakers",
     "Import substitution and structural adjustment are two names for the same programme"], ans=0,
   why="EK LEG-3.A.1 supplies the conditionality mechanism and its three requirements, EK LEG-3.A.3 the sovereign powers and the pressure to liberalize trade, and EK LEG-3.A.2 the raising of tariffs to reduce foreign dependency, which runs against the other two."),
]
