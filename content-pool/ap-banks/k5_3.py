# AP COMPARATIVE GOVERNMENT AND POLITICS 5.3 Challenges from Globalization
# CED effective Fall 2026, Unit 5 Political and Economic Changes and Development.
# Enduring understanding IEF-3; learning objective IEF-3.C (explain how
# globalization creates challenges to regime sovereignty). Suggested skill 1.D,
# Concept Application.
#
# Essential knowledge relied on:
#   IEF-3.C.1  MANY ASPECTS OF GLOBALIZATION CAN CHALLENGE REGIME SOVEREIGNTY,
#              including:
#     .a FOREIGN DIRECT INVESTMENT AND MULTINATIONAL CORPORATIONS FROM ORIGINATING
#        REGIMES can pose a CHALLENGE TO A GOVERNMENT'S FOUNDATIONAL ECONOMIC AND
#        POLITICAL IDEAS AND PRINCIPLES
#     .b CULTURAL INFLUENCES (OFTEN WESTERN) THAT ACCOMPANY INVESTMENT AND TRADE
#        with a given regime CAN PROVOKE A DOMESTIC BACKLASH
#     .c INCREASED ECONOMIC DEVELOPMENT CAN CAUSE ENVIRONMENTAL DEGRADATION AND
#        ACCOMPANYING HEALTH ISSUES THAT ALIENATE CITIZENS
#     .d FOREIGN GOVERNMENTS CAN BRING POLITICAL AND ECONOMIC PRESSURES (including
#        TREATY REVERSALS, PUBLIC CONDEMNATION AT INTERGOVERNMENTAL ORGANIZATIONS
#        LIKE THE UNITED NATIONS, and ECONOMIC SANCTIONS) TO BEAR ON COUNTRIES WHOSE
#        ACTIONS (INCLUDING HUMAN RIGHTS VIOLATIONS) OFFEND THEM
#   IEF-3.C.2  in response to global market forces, GOVERNMENTS FREQUENTLY STRIVE TO
#              RESPOND TO INTERNAL DEMANDS FOR DOMESTIC REFORM; governments ALSO WORK
#              TO CONTROL DOMESTIC POLICY DEBATES and ATTEMPT TO EXTEND THEIR
#              INFLUENCE REGIONALLY TO DEFLECT CRITICISM AND IMPROVE ECONOMIC
#              CONDITIONS
#
# THE FOUR CHALLENGES DO NOT ALL COME FROM OUTSIDE, and that is the item this
# topic is built around. Only IEF-3.C.1.d names foreign governments as the actor.
# IEF-3.C.1.b's backlash is domestic, IEF-3.C.1.c's alienation is domestic, and
# IEF-3.C.1.a's challenge is to the government's OWN foundational ideas rather
# than to its territory. So a student who reads "challenge to sovereignty" as
# "pressure from abroad" gets three of the four wrong. Items 10, 11, 12 and 17 key
# that reading directly.
#
# THE SECOND STRUCTURAL POINT is that IEF-3.C.1.c is the challenge a government
# brings on itself by succeeding. Development produces the degradation, the
# degradation produces the health issues, and the health issues alienate the
# citizens -- a three-step chain inside one sentence. The environment table follows
# exactly those steps, which is why its check requires every column to move.
#
# IEF-3.C.2 IS TWO SENTENCES WITH DIFFERENT SUBJECTS: governments respond to
# internal demands for reform, AND governments work to control the debate and
# extend regional influence to deflect criticism. The second is not a softer
# version of the first; deflecting criticism is not the same as answering it.
# Items 8, 9 and 18 keep them apart.
#
# NOTHING HERE TURNS ON CURRENT EVENTS. No sanction, treaty, dispute or condition
# of any actual country is asserted; the framework's instruments are named as
# instruments. Every table figure is HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("5.3", "Challenges from Globalization", 5)

_T_PRESSURE = dict(
    headers=["Instrument of foreign pressure", "Times used against one country in a decade (hypothetical)"],
    rows=[["Treaty reversal", "4"],
          ["Public condemnation at an intergovernmental organization", "19"],
          ["Economic sanctions", "11"]])

_T_ENV = dict(
    headers=["Year (hypothetical)", "Index of industrial output (first year = 100)",
             "Days on which air quality was rated unhealthy",
             "Hospital admissions for respiratory illness per 100,000 residents",
             "Residents saying the government is not protecting their health (percent)"],
    rows=[["Year 1", "100", "41", "310", "22"],
          ["Year 2", "138", "76", "465", "39"],
          ["Year 3", "187", "119", "640", "58"]])

_T_CASE = dict(
    headers=["Case (hypothetical)", "What happened"],
    rows=[["Case 1", "A foreign-owned firm's terms of operation required changes at odds with the government's stated economic and political principles"],
          ["Case 2", "Goods and entertainment arriving with new trade prompted a public campaign against foreign customs"],
          ["Case 3", "Rapid industrial growth fouled the air and water, and residents blamed the government for the illness that followed"],
          ["Case 4", "Other governments withdrew from a treaty, condemned the country at an international organization, and imposed sanctions"]])

QUESTIONS = [
 dict(q="What does the framework say many aspects of globalization can challenge?",
   choices=[
     "regime sovereignty",
     "the size of a country's population",
     "the number of parties in a legislature",
     "the length of a head of government's term",
     "a country's system of judicial appointment"], ans=0,
   why="EK IEF-3.C.1 opens by stating that many aspects of globalization can challenge regime sovereignty, and the four items it lists are the ways that challenge arrives."),
 dict(q="What does the framework say foreign direct investment and multinational corporations from originating regimes can challenge?",
   choices=[
     "a government's foundational economic and political ideas and principles",
     "a country's international boundaries",
     "the composition of a country's legislature",
     "the length of a country's electoral cycle",
     "a country's membership of a supranational organization"], ans=0,
   why="EK IEF-3.C.1.a states that foreign direct investment and multinational corporations from originating regimes can pose a challenge to a government's foundational economic and political ideas and principles, so what is challenged is the regime's own commitments."),
 dict(q="What does the framework say the cultural influences that accompany investment and trade can provoke?",
   choices=[
     "a domestic backlash",
     "an increase in foreign direct investment",
     "a reversal of a treaty by a foreign government",
     "the imposition of economic sanctions",
     "a rise in hospital admissions"], ans=0,
   why="EK IEF-3.C.1.b states that cultural influences, often Western, that accompany investment and trade with a given regime can provoke a domestic backlash, so the reaction the framework names comes from inside the country."),
 dict(q="According to the framework, what can increased economic development cause that in turn alienates citizens?",
   choices=[
     "environmental degradation and accompanying health issues",
     "the reversal of trade treaties by neighboring states",
     "the arrival of multinational corporations",
     "public condemnation at an intergovernmental organization",
     "a fall in foreign direct investment"], ans=0,
   why="EK IEF-3.C.1.c states that increased economic development can cause environmental degradation and accompanying health issues that alienate citizens, which makes the alienation a consequence of growth rather than of foreign action."),
 dict(q="Which actor does the framework identify as bringing political and economic pressures to bear on a country?",
   choices=[
     "foreign governments",
     "domestic civil society groups",
     "the country's own regional legislatures",
     "multinational corporations headquartered in the country",
     "the country's judiciary"], ans=0,
   why="EK IEF-3.C.1.d states that foreign governments can bring political and economic pressures to bear on countries whose actions offend them, and it is the only one of the four challenges whose actor is another state."),
 dict(q="Which instruments does the framework name as the political and economic pressures foreign governments can apply?",
   choices=[
     "treaty reversals, public condemnation at intergovernmental organizations, and economic sanctions",
     "tariff reductions, currency swaps, and development loans",
     "party registration requirements, thresholds, and district boundaries",
     "special economic zones, joint ventures, and privatization",
     "gender quotas, health care spending, and education policy"], ans=0,
   why="EK IEF-3.C.1.d names treaty reversals, public condemnation at intergovernmental organizations like the United Nations, and economic sanctions as the pressures foreign governments can bring to bear."),
 dict(q="What sort of conduct does the framework say attracts those pressures from foreign governments?",
   choices=[
     "actions that offend them, including human rights violations",
     "any decision to trade with a neighbor",
     "the adoption of a written constitution",
     "the holding of competitive elections",
     "membership in an international financial organization"], ans=0,
   why="EK IEF-3.C.1.d states that foreign governments bring these pressures to bear on countries whose actions, including human rights violations, offend them, so the trigger is conduct another government finds objectionable."),
 dict(q="What does the framework say governments frequently strive to do in response to global market forces?",
   choices=[
     "respond to internal demands for domestic reform",
     "withdraw from every international organization",
     "abolish private ownership of industry",
     "transfer policy making to multinational corporations",
     "suspend their own constitutions"], ans=0,
   why="EK IEF-3.C.2 states that in response to global market forces governments frequently strive to respond to internal demands for domestic reform, which places the demand inside the country and the response with the government."),
 dict(q="Besides responding to internal demands, what else does the framework say governments do in the face of global market forces?",
   choices=[
     "work to control domestic policy debates and attempt to extend their influence regionally to deflect criticism and improve economic conditions",
     "leave domestic debate entirely unmanaged and withdraw from their regions",
     "hand economic policy to an intergovernmental organization",
     "cease all trade with countries that criticize them",
     "abolish the ministries responsible for economic policy"], ans=0,
   why="EK IEF-3.C.2 adds that governments also work to control domestic policy debates and attempt to extend their influence regionally to deflect criticism and improve economic conditions, which is a different response from answering the demands themselves."),
 dict(q="Which of the four challenges in EK IEF-3.C.1 has an actor outside the country as its source?",
   choices=[
     "the pressures applied by foreign governments",
     "the domestic backlash against cultural influences",
     "the alienation of citizens by environmental degradation",
     "the challenge to a government's foundational ideas and principles",
     "all four, since each concerns globalization"], ans=0,
   why="EK IEF-3.C.1.d names foreign governments as the actor, while EK IEF-3.C.1.b's backlash comes from the country's own public, EK IEF-3.C.1.c's alienation from its own citizens, and EK IEF-3.C.1.a's challenge falls on the government's own commitments."),
 dict(q="Which of the four challenges in EK IEF-3.C.1 takes the form of a reaction by a country's own population?",
   choices=[
     "the backlash provoked by the cultural influences that accompany investment and trade",
     "the reversal of treaties by other governments",
     "the imposition of economic sanctions",
     "public condemnation at an intergovernmental organization",
     "the arrival of foreign direct investment"], ans=0,
   why="EK IEF-3.C.1.b states that cultural influences, often Western, that accompany investment and trade can provoke a domestic backlash, and the word domestic places the reaction among the country's own people."),
 dict(q="Which of the four challenges in EK IEF-3.C.1 arises from a country's own economic success rather than from anything done to it?",
   choices=[
     "environmental degradation and health issues caused by increased economic development",
     "public condemnation at an intergovernmental organization",
     "the reversal of a treaty by another government",
     "the imposition of economic sanctions",
     "the arrival of multinational corporations from other regimes"], ans=0,
   why="EK IEF-3.C.1.c states that increased economic development can cause environmental degradation and accompanying health issues that alienate citizens, so the chain begins with the country's own growth."),
 dict(q="A foreign investor will build a plant only if the government abandons a commitment it has long treated as basic to its economic and political order. Which framework challenge does this illustrate?",
   choices=[
     "foreign direct investment posing a challenge to a government's foundational economic and political ideas and principles",
     "cultural influences provoking a domestic backlash",
     "environmental degradation alienating citizens",
     "foreign governments imposing economic sanctions",
     "a government extending its influence regionally"], ans=0,
   why="EK IEF-3.C.1.a states that foreign direct investment and multinational corporations from originating regimes can pose a challenge to a government's foundational economic and political ideas and principles, which is what a condition of investment requiring the abandonment of such a commitment amounts to."),
 dict(q="Imported entertainment and consumer goods spread quickly after a trade opening, and a large public campaign forms to defend traditional practices. Which framework challenge does this illustrate?",
   choices=[
     "cultural influences accompanying investment and trade provoking a domestic backlash",
     "foreign governments bringing political and economic pressures to bear",
     "increased economic development causing environmental degradation",
     "a government responding to internal demands for domestic reform",
     "multinational corporations challenging a government's budget"], ans=0,
   why="EK IEF-3.C.1.b states that cultural influences, often Western, that accompany investment and trade with a given regime can provoke a domestic backlash, and a public campaign in defense of traditional practices is that backlash."),
 dict(q="After two decades of rapid industrial growth, a river system is heavily polluted, respiratory illness rises sharply, and residents say the government has failed them. Which framework challenge does this illustrate?",
   choices=[
     "increased economic development causing environmental degradation and health issues that alienate citizens",
     "cultural influences provoking a domestic backlash",
     "foreign governments imposing sanctions",
     "foreign direct investment challenging a government's principles",
     "a government working to control domestic policy debates"], ans=0,
   why="EK IEF-3.C.1.c states that increased economic development can cause environmental degradation and accompanying health issues that alienate citizens, and the scenario runs through all three steps of that chain."),
 dict(q="Several governments withdraw from an agreement with a country, criticize it at the United Nations, and restrict trade with it after objecting to its treatment of a minority. Which framework challenge does this illustrate?",
   choices=[
     "foreign governments bringing political and economic pressures to bear on countries whose actions offend them",
     "cultural influences provoking a domestic backlash",
     "environmental degradation alienating citizens",
     "foreign direct investment challenging a government's foundational principles",
     "a government striving to respond to internal demands for reform"], ans=0,
   why="EK IEF-3.C.1.d names treaty reversals, public condemnation at intergovernmental organizations like the United Nations, and economic sanctions as pressures foreign governments bring to bear on countries whose actions, including human rights violations, offend them."),
 dict(q="Why does the framework treat these four developments as challenges to sovereignty rather than merely as difficulties?",
   choices=[
     "because each narrows what a government can decide for itself within its own territory, whether the constraint comes from investors, its own public, the consequences of growth, or other states",
     "because each transfers a country's territory to another state",
     "because each requires a country to leave an international organization",
     "because each is imposed by a supranational body with sovereign powers",
     "because each abolishes a country's constitution"], ans=0,
   why="EK IEF-3.C's learning objective is to explain how globalization creates challenges to regime sovereignty, and the four items in EK IEF-3.C.1 each constrain what a government can settle on its own, which is why the framework groups them under that heading."),
 dict(q="EK IEF-3.C.2 says governments attempt to extend their influence regionally in part to deflect criticism. How does deflecting criticism differ from responding to internal demands for reform?",
   choices=[
     "responding to the demands addresses what is being asked for, while deflecting criticism turns attention elsewhere without granting it",
     "the two are the same thing described twice",
     "deflecting criticism means granting every demand at once",
     "responding to demands means suppressing them",
     "deflecting criticism is directed at foreign governments only"], ans=0,
   why="EK IEF-3.C.2 states both separately, first that governments strive to respond to internal demands for domestic reform and then that they also work to control domestic policy debates and extend their influence regionally to deflect criticism, which are different responses to the same pressure."),
 dict(q="EK IEF-3.C.2 and EK IEF-3.B.3 both describe why governments act as they do under market pressure. What do they have in common?",
   choices=[
     "both name managing domestic political debate and extending influence beyond the country's borders among a government's reasons for acting",
     "both state that governments act only to improve economic conditions",
     "both state that governments act only under instruction from international organizations",
     "both deny that governments respond to domestic demands",
     "both concern the treatment of natural resources alone"], ans=0,
   why="EK IEF-3.B.3.c and EK IEF-3.B.3.d name controlling domestic political debates to maintain power and extending national influence regionally and internationally, and EK IEF-3.C.2 names controlling domestic policy debates and extending influence regionally to deflect criticism."),
 dict(q="A commentator argues that globalization challenges the sovereignty only of weak states. Which reply is best supported by the framework?",
   choices=[
     "The framework's challenges include a government's own public reacting against cultural change and its own citizens being alienated by the effects of growth, neither of which depends on a state being weak",
     "The framework states that only states with large economies face these challenges",
     "The framework states that sovereignty cannot be challenged at all",
     "The framework states that these challenges arise only from foreign governments",
     "The framework states that economic development removes every challenge to sovereignty"], ans=0,
   why="EK IEF-3.C.1.b locates a backlash among a country's own public and EK IEF-3.C.1.c locates alienation among its own citizens as a consequence of development, so two of the four challenges arise from within and follow from a country's own growth."),
 dict(q="The table records how often three instruments of foreign pressure were used against one hypothetical country. Which instrument was used most often?",
   table=_T_PRESSURE,
   choices=[
     "public condemnation at an intergovernmental organization, 19 times",
     "economic sanctions, 11 times",
     "treaty reversal, 4 times",
     "none of them, since the framework does not name such instruments",
     "all three equally often"], ans=0,
   why="EK IEF-3.C.1.d names treaty reversals, public condemnation at intergovernmental organizations like the United Nations, and economic sanctions as the pressures foreign governments can bring to bear, so the table's three rows are the framework's own three instruments."),
 dict(q="According to the same table, the total number of times the three instruments were used is",
   table=_T_PRESSURE,
   choices=[
     "34",
     "30",
     "23",
     "19",
     "11"], ans=0,
   why="Adding the column across the three rows gives the total. The alternatives are the total with the smallest row omitted, the largest and smallest rows added, the largest single row, and the middle row."),
 dict(q="Using the same table, the difference between the most and least frequently used instruments is",
   table=_T_PRESSURE,
   choices=[
     "15",
     "8",
     "7",
     "19",
     "4"], ans=0,
   why="Subtracting the smallest row from the largest gives the difference. The alternatives are the other two gaps within the same column and the two extreme rows read as though they were differences."),
 dict(q="The table sets industrial output beside three health and opinion measures for one hypothetical country. Which conclusion does it support?",
   table=_T_ENV,
   choices=[
     "As industrial output rose, unhealthy air days, respiratory admissions, and the share of residents who say the government is not protecting their health all rose with it",
     "As industrial output rose, unhealthy air days and respiratory admissions fell",
     "Industrial output fell while health complaints rose",
     "None of the four columns changed across the three years",
     "Residents' views of the government improved as output rose"], ans=0,
   why="EK IEF-3.C.1.c states that increased economic development can cause environmental degradation and accompanying health issues that alienate citizens, and the table's four columns run through exactly those steps, each rising in every year."),
 dict(q="According to the same table of three years, the increase in the number of days on which air quality was rated unhealthy is",
   table=_T_ENV,
   choices=[
     "78",
     "43",
     "35",
     "119",
     "160"], ans=0,
   why="Subtracting the first year's figure from the third year's gives the increase. The alternatives are the increases across the other pairs of years, the third year's own figure, and the first and third years added instead of subtracted."),
 dict(q="Using the same table of three years, the rise in the share of residents saying the government is not protecting their health is",
   table=_T_ENV,
   choices=[
     "36 percentage points",
     "19 percentage points",
     "17 percentage points",
     "58 percentage points",
     "87 percentage points"], ans=0,
   why="Subtracting the first year's share from the third year's gives the rise. The alternatives are the rises across the other pairs of years, the final share read as a rise, and the change in the output index read as though it were a percentage of residents."),
 dict(q="The table describes four hypothetical cases. Which one matches EK IEF-3.C.1.a?",
   table=_T_CASE,
   choices=[
     "the case in which a foreign-owned firm's terms required changes at odds with the government's stated principles",
     "the case in which new trade prompted a campaign against foreign customs",
     "the case in which industrial growth fouled the air and water",
     "the case in which other governments withdrew from a treaty and imposed sanctions",
     "none of the four, since that statement describes no such situation"], ans=0,
   why="EK IEF-3.C.1.a states that foreign direct investment and multinational corporations from originating regimes can pose a challenge to a government's foundational economic and political ideas and principles, and only one case sets a foreign firm's terms against the government's stated principles."),
 dict(q="Using the same table of cases, which one matches EK IEF-3.C.1.b?",
   table=_T_CASE,
   choices=[
     "the case in which goods and entertainment arriving with new trade prompted a public campaign against foreign customs",
     "the case in which a foreign-owned firm's terms clashed with the government's principles",
     "the case in which industrial growth fouled the air and water",
     "the case in which other governments condemned the country and imposed sanctions",
     "none of the four, since that statement describes no such situation"], ans=0,
   why="EK IEF-3.C.1.b states that cultural influences, often Western, that accompany investment and trade with a given regime can provoke a domestic backlash, and a public campaign against foreign customs following a trade opening is that backlash."),
 dict(q="Using the same table of cases, which one describes a challenge whose source lies outside the country?",
   table=_T_CASE,
   choices=[
     "the case in which other governments withdrew from a treaty, condemned the country at an international organization, and imposed sanctions",
     "the case in which residents blamed the government for illness after industrial growth",
     "the case in which a public campaign formed against foreign customs",
     "the case in which a foreign-owned firm's terms clashed with the government's principles",
     "all four, since each concerns globalization"], ans=0,
   why="EK IEF-3.C.1.d is the only one of the four statements whose actor is another state, and the rejected cases place the reaction with the country's own residents, its own public, or its own government's commitments."),
 dict(q="Taking EK IEF-3.C as a whole, which summary is most accurate?",
   choices=[
     "Globalization narrows what a government can settle for itself in four ways at once, through investors' terms, a public reacting against cultural change, the environmental and health costs of its own growth, and pressure from other states, and governments answer with a mixture of reform, management of the domestic debate, and regional ambition",
     "Globalization challenges sovereignty only through the actions of foreign governments",
     "Globalization poses no challenge to sovereignty, since states remain legally supreme",
     "Governments respond to these challenges only by granting the reforms demanded",
     "Globalization affects economic policy but leaves political debate untouched"], ans=0,
   why="EK IEF-3.C.1 lists four aspects of globalization that can challenge regime sovereignty, two of them arising inside the country, and EK IEF-3.C.2 gives both responses, striving to answer internal demands for reform and working to control the debate while extending regional influence."),
]
