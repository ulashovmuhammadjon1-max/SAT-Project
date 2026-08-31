# AP COMPARATIVE GOVERNMENT AND POLITICS 5.6 Adaptation of Social Policies
# CED effective Fall 2026, Unit 5 Political and Economic Changes and Development.
# Enduring understanding LEG-3 (a government bolsters regime stability by adapting
# its policies to environmental, political, economic, and cultural conditions);
# learning objective LEG-3.B (explain how governments adapt social policies to
# address political, cultural, and economic changes). Suggested skill 2.B, Country
# Comparison.
#
# Essential knowledge relied on:
#   LEG-3.B.1  IN RESPONSE TO POLITICAL, CULTURAL, AND ECONOMIC CHANGES, governments
#              CREATE NEW SOCIAL POLICIES, including GENDER EQUITY, HEALTH CARE, and
#              EDUCATION POLICIES, as represented by:
#     .a GENDER EQUITY RULES IN IRAN with VOTING, the ELECTION OF MAJLES, and
#        APPOINTMENT TO CABINET POSITIONS
#     .b DISPUTES IN IRAN about FEMALE ACCESS TO CERTAIN UNIVERSITY DEGREE PROGRAMS
#        and ATTENDANCE AT AND PARTICIPATION IN SPORTING EVENTS
#     .c VARIED ABORTION POLICIES IN MEXICO'S LOCAL AND STATE GOVERNMENTS
#     .d GENDER QUOTAS IN MEXICO
#     .e UNEQUAL GENDER ACCESS TO EDUCATION IN THE NORTH AND SOUTH OF NIGERIA
#   LEG-3.B.2  governments IMPLEMENT SOCIAL WELFARE POLICIES to REDUCE POVERTY,
#              INCREASE LITERACY, and IMPROVE PUBLIC HEALTH, BOTH TO IMPROVE
#              CITIZENS' LIVES AND TO MAINTAIN OR BOLSTER POLITICAL LEGITIMACY
#
# LEG-3.B.2 HAS TWO PURPOSES IN ONE SENTENCE, and that is the item this topic
# turns on. Social welfare policy is stated as serving citizens AND as serving the
# regime, and the framework joins them with "both ... and" rather than offering
# them as alternatives. A student who reads welfare policy as purely humanitarian
# cannot answer an item that asks why an authoritarian government would expand a
# literacy programme. Items 9, 14, 15, 19 and 20 all key the second purpose, and
# EK LEG-1.A.1's definition of legitimacy as what constituents believe is what
# makes it intelligible.
#
# THE FIVE EXAMPLES ARE NOT FIVE COUNTRIES. Two are Iranian, two Mexican and one
# Nigerian, and they differ in KIND as well as in country: .a is a set of rules
# about holding office, .b a set of disputes about access, .c a variation ACROSS
# LEVELS OF GOVERNMENT inside one country, .d a nomination rule, .e a variation
# ACROSS REGIONS inside one country. Items 10, 11, 12 and 13 key those
# differences, because "which country" is the easy half and "which kind of policy
# question" is the half the exam actually asks.
#
# WHAT IS DELIBERATELY NOT ASSERTED: no outcome, statistic, court ruling, election
# or current condition of any real country. Each of the five examples is keyed to
# exactly what its own sentence says and no further -- in particular the module
# says only that abortion policies VARY across Mexico's local and state
# governments, which is the framework's whole claim, and it attributes no content
# to any of those policies. Every table figure is HYPOTHETICAL, labelled so, and
# attached to an unnamed country.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("5.6", "Adaptation of Social Policies", 5)

_T_QUOTA = dict(
    headers=["Legislature (hypothetical)", "Seats held by women before the rules (percent)",
             "Seats held by women after the rules (percent)", "Nomination quota rules in force"],
    rows=[["Legislature 1", "12", "43", "Yes"],
          ["Legislature 2", "17", "19", "No"],
          ["Legislature 3", "9", "38", "Yes"]])

_T_WELFARE = dict(
    headers=["Stated aim of the programme", "Share of one government's social welfare budget (percent, hypothetical)"],
    rows=[["Reducing poverty", "46"],
          ["Increasing literacy", "21"],
          ["Improving public health", "33"]])

_T_REGION = dict(
    headers=["Region of one country (hypothetical)", "Boys completing secondary school (percent)",
             "Girls completing secondary school (percent)"],
    rows=[["Northern region", "54", "28"],
          ["Southern region", "71", "66"]])

QUESTIONS = [
 dict(q="In response to what does the framework say governments create new social policies?",
   choices=[
     "political, cultural, and economic changes",
     "instructions issued by supranational organizations",
     "the demands of multinational corporations alone",
     "changes in the boundaries between states",
     "rulings of international courts"], ans=0,
   why="EK LEG-3.B.1 states that in response to political, cultural, and economic changes governments create new social policies, so the framework locates the prompt in conditions rather than in an external instruction."),
 dict(q="Which three kinds of social policy does the framework name?",
   choices=[
     "gender equity, health care, and education policies",
     "taxation, tariff, and subsidy policies",
     "defense, foreign affairs, and treaty policies",
     "party registration, campaign finance, and districting policies",
     "immigration, citizenship, and border policies"], ans=0,
   why="EK LEG-3.B.1 names gender equity, health care, and education policies as the social policies governments create in response to political, cultural, and economic changes."),
 dict(q="With which three matters does the framework associate Iran's gender equity rules?",
   choices=[
     "voting, the election of the Majles, and appointment to cabinet positions",
     "military service, taxation, and property ownership",
     "school attendance, marriage, and inheritance",
     "party registration, campaign finance, and ballot access",
     "trade, investment, and employment"], ans=0,
   why="EK LEG-3.B.1.a associates gender equity rules in Iran with voting, the election of the Majles, and appointment to cabinet positions, so all three concern participation in choosing or holding office."),
 dict(q="What subjects of dispute in Iran does the framework record?",
   choices=[
     "female access to certain university degree programs and attendance at and participation in sporting events",
     "the length of the president's term and the powers of the Guardian Council",
     "the ownership of the oil industry and the level of subsidies",
     "the boundaries of electoral districts and the registration of parties",
     "the level of tariffs and the terms of foreign investment"], ans=0,
   why="EK LEG-3.B.1.b records disputes in Iran about female access to certain university degree programs and about attendance at and participation in sporting events, which are questions of access rather than of office."),
 dict(q="What does the framework record about abortion policy in Mexico?",
   choices=[
     "that it varies across local and state governments",
     "that it is set uniformly by the national government",
     "that it is determined by a supranational organization",
     "that it is decided by referendum in every state",
     "that the framework records nothing on the subject"], ans=0,
   why="EK LEG-3.B.1.c records varied abortion policies in Mexico's local and state governments, so what the framework states is the variation across levels of government rather than the content of any policy."),
 dict(q="Which gender equity measure does the framework record in Mexico?",
   choices=[
     "gender quotas",
     "rules governing appointment to cabinet positions",
     "disputes about access to university degree programs",
     "unequal access to education between regions",
     "restrictions on attendance at sporting events"], ans=0,
   why="EK LEG-3.B.1.d names gender quotas in Mexico. The rejected measures are the framework's Iranian and Nigerian examples."),
 dict(q="What does the framework record about education in Nigeria?",
   choices=[
     "unequal gender access to education in the north and south of the country",
     "uniform gender access to education across the country",
     "the abolition of secondary education outside the capital",
     "the transfer of education policy to a supranational organization",
     "the introduction of gender quotas in universities"], ans=0,
   why="EK LEG-3.B.1.e records unequal gender access to education in the north and south of Nigeria, which makes it a claim about variation between regions of one country."),
 dict(q="Which aims does the framework give for governments' social welfare policies?",
   choices=[
     "reducing poverty, increasing literacy, and improving public health",
     "raising tariffs, cutting subsidies, and privatizing industry",
     "expanding the armed forces and the intelligence services",
     "increasing the number of registered political parties",
     "extending the terms of legislators and judges"], ans=0,
   why="EK LEG-3.B.2 states that governments implement social welfare policies to reduce poverty, increase literacy, and improve public health."),
 dict(q="For what two reasons does the framework say governments implement social welfare policies?",
   choices=[
     "both to improve citizens' lives and to maintain or bolster political legitimacy",
     "to improve citizens' lives, and for no other reason",
     "to maintain political legitimacy, and for no other reason",
     "to satisfy the conditions attached to foreign loans and to raise tariffs",
     "to extend national influence abroad and to reduce trade deficits"], ans=0,
   why="EK LEG-3.B.2 joins the two purposes with both and and, stating that governments implement these policies both to improve citizens' lives and to maintain or bolster political legitimacy, so neither purpose is offered as an alternative to the other."),
 dict(q="Which of the framework's five examples concerns a policy that differs between levels of government inside one country?",
   choices=[
     "varied abortion policies in Mexico's local and state governments",
     "gender equity rules in Iran concerning voting and cabinet appointment",
     "disputes in Iran about access to university degree programs",
     "gender quotas in Mexico",
     "unequal gender access to education in the north and south of Nigeria"], ans=0,
   why="EK LEG-3.B.1.c is the only one of the five examples to locate the variation in local and state governments, which places the difference between levels of government rather than between regions or countries."),
 dict(q="Which of the framework's five examples concerns a difference between regions of one country?",
   choices=[
     "unequal gender access to education in the north and south of Nigeria",
     "gender quotas in Mexico",
     "gender equity rules in Iran concerning the election of the Majles",
     "disputes in Iran about attendance at sporting events",
     "varied abortion policies across Mexico's local and state governments"], ans=0,
   why="EK LEG-3.B.1.e states that gender access to education is unequal in the north and south of Nigeria, which is a comparison between two regions of a single country."),
 dict(q="Which comparison of the framework's Iranian and Mexican gender examples is accurate?",
   choices=[
     "The Iranian examples concern rules about holding office and disputes about access, while the Mexican ones concern a nomination quota and policies that differ across levels of government",
     "Both countries' examples concern nomination quotas alone",
     "Both countries' examples concern access to university programs",
     "Neither country's gender policies are described by the framework",
     "Both countries' examples concern differences between northern and southern regions"], ans=0,
   why="EK LEG-3.B.1.a and EK LEG-3.B.1.b give Iran rules about voting, the Majles and cabinet appointment together with disputes about university access and sporting events, while EK LEG-3.B.1.d gives Mexico gender quotas and EK LEG-3.B.1.c varied policies across its local and state governments."),
 dict(q="A student says all five of the framework's examples are the same kind of policy question. Why is that wrong?",
   choices=[
     "because they range across rules for holding office, disputes over access, variation between levels of government, a nomination requirement, and a gap between regions",
     "because they all concern education",
     "because they all concern one country",
     "because they all concern health care",
     "because none of them concerns gender"], ans=0,
   why="EK LEG-3.B.1's five examples differ in kind: .a states rules about office, .b disputes about access, .c variation across levels of government, .d a nomination quota, and .e a gap between two regions."),
 dict(q="Why is it consistent with the framework for a government to expand social welfare provision partly for reasons of its own standing?",
   choices=[
     "because the framework states that such policies are implemented both to improve citizens' lives and to maintain or bolster political legitimacy, and legitimacy is a matter of what constituents believe",
     "because the framework states that welfare policies have no effect on citizens' lives",
     "because the framework states that only authoritarian regimes implement welfare policies",
     "because the framework states that welfare policy is required by international lenders",
     "because the framework states that legitimacy depends on a country's borders"], ans=0,
   why="EK LEG-3.B.2 names both purposes in one sentence and EK LEG-1.A.1 defines legitimacy as whether constituents believe a government has the right to use power as it does, which is why a visible improvement in provision bears on it."),
 dict(q="A government announces a large expansion of adult literacy classes and its ministers argue publicly that it shows the government is delivering for ordinary people. Which framework claim does this best illustrate?",
   choices=[
     "that social welfare policies are implemented both to improve citizens' lives and to maintain or bolster political legitimacy",
     "that governments create social policies only in response to economic change",
     "that education policy is set by supranational organizations",
     "that welfare policy is a condition of external financial assistance",
     "that literacy programmes have no bearing on a government's standing"], ans=0,
   why="EK LEG-3.B.2 states that governments implement social welfare policies to increase literacy among other aims, both to improve citizens' lives and to maintain or bolster political legitimacy, and the announcement pursues both at once."),
 dict(q="A country adopts a rule requiring every party to nominate candidates of each gender in fixed proportions. Which of the framework's examples does this match?",
   choices=[
     "gender quotas of the kind the framework records in Mexico",
     "gender equity rules concerning appointment to cabinet positions",
     "disputes about female access to university degree programs",
     "unequal gender access to education between regions",
     "varied policies across local and state governments"], ans=0,
   why="EK LEG-3.B.1.d names gender quotas in Mexico, and a requirement that parties nominate candidates of each gender in fixed proportions is what such a quota does."),
 dict(q="A public argument breaks out over which university degree programs women may enrol in. Which of the framework's examples does this match?",
   choices=[
     "disputes about female access to certain university degree programs",
     "gender quotas applied to party nominations",
     "gender equity rules about voting and the election of a legislature",
     "unequal gender access to education between a country's regions",
     "varied policies across local and state governments"], ans=0,
   why="EK LEG-3.B.1.b records disputes in Iran about female access to certain university degree programs, which is exactly the question in the scenario."),
 dict(q="How does the topic's enduring understanding frame the making of social policy?",
   choices=[
     "as a way a government bolsters regime stability by adapting its policies to environmental, political, economic, and cultural conditions",
     "as a set of obligations imposed by international financial organizations",
     "as a matter settled once when a constitution is written",
     "as the exclusive concern of democratic regimes",
     "as an activity unrelated to a government's stability"], ans=0,
   why="Enduring understanding LEG-3 states that a government bolsters regime stability by adapting its policies to environmental, political, economic, and cultural conditions, which is why EK LEG-3.B.1 begins from changes and EK LEG-3.B.2 ends at legitimacy."),
 dict(q="Which finding would most strongly support a claim that a government's social welfare programme serves its standing as well as its citizens?",
   choices=[
     "The programme measurably reduced poverty and the government made its delivery the centerpiece of its case for public support",
     "The programme was funded entirely from external assistance",
     "The programme was administered by an international organization",
     "The programme was never mentioned in public by any minister",
     "The programme reduced poverty in a country with no elections"], ans=0,
   why="EK LEG-3.B.2 states both purposes together, so evidence for the pair must show the improvement in citizens' lives and the government's use of it, and EK LEG-1.A.1 makes legitimacy turn on what constituents believe about the government's right to use power."),
 dict(q="A commentator argues that social welfare policy is purely humanitarian and has nothing to do with a regime's position. Which reply is best supported by the framework?",
   choices=[
     "The framework states in one sentence that these policies are implemented both to improve citizens' lives and to maintain or bolster political legitimacy",
     "The framework states that welfare policy never improves citizens' lives",
     "The framework states that only unstable regimes provide welfare",
     "The framework states that welfare policy is decided abroad",
     "The framework states that legitimacy is unaffected by anything a government does"], ans=0,
   why="EK LEG-3.B.2 joins the two purposes with both and and rather than presenting them as alternatives, so the humanitarian reading captures one half of the framework's own statement."),
 dict(q="The table reports hypothetical figures on women's representation in three legislatures. Which conclusion does it support?",
   table=_T_QUOTA,
   choices=[
     "The two legislatures with nomination quota rules in force saw much larger increases than the one without them",
     "The legislature without quota rules saw the largest increase",
     "All three legislatures saw increases of similar size",
     "Only the legislature without quota rules saw any increase",
     "Every legislature ended with the same share of seats held by women"], ans=0,
   why="EK LEG-3.B.1.d names gender quotas among the social policies governments create in response to political, cultural, and economic changes, and the two rows with quotas in force rise by far more than the row without them."),
 dict(q="According to the same table, the largest increase in the share of seats held by women is",
   table=_T_QUOTA,
   choices=[
     "31 percentage points",
     "29 percentage points",
     "2 percentage points",
     "43 percentage points",
     "26 percentage points"], ans=0,
   why="Subtracting each row's earlier share from its later one and taking the largest result gives the answer. The alternatives are the increases in the other two rows, a final share read as an increase, and a difference taken across two different rows."),
 dict(q="Using the same table, the gap between the highest and lowest shares of seats held by women after the rules is",
   table=_T_QUOTA,
   choices=[
     "24 percentage points",
     "34 percentage points",
     "31 percentage points",
     "19 percentage points",
     "43 percentage points"], ans=0,
   why="Subtracting the smallest figure in the later column from the largest gives the gap. The alternatives are a difference taken across the two columns, the largest single increase, and the two extreme values of the later column read as gaps."),
 dict(q="The table reports how one hypothetical government divides its social welfare budget. Which aim receives the largest share, and does the framework name it?",
   table=_T_WELFARE,
   choices=[
     "reducing poverty, at 46 percent, and the framework names it as one of three aims of social welfare policy",
     "improving public health, at 33 percent, and the framework names no aims",
     "increasing literacy, at 21 percent, and the framework names it as the only aim",
     "none of them, since the framework names no aims for social welfare policy",
     "all three equally, since each receives a share"], ans=0,
   why="EK LEG-3.B.2 names reducing poverty, increasing literacy, and improving public health as the aims of social welfare policies, so the table's three rows are the framework's own three aims and one of them takes the largest share."),
 dict(q="According to the same table of budget shares, the three shares add to",
   table=_T_WELFARE,
   choices=[
     "100",
     "79",
     "67",
     "54",
     "46"], ans=0,
   why="Adding the column across the three rows gives the sum. The alternatives are the sum with each of the three rows omitted in turn, and the largest single row."),
 dict(q="Using the same table of budget shares, the difference between the largest and smallest shares is",
   table=_T_WELFARE,
   choices=[
     "25 percentage points",
     "13 percentage points",
     "12 percentage points",
     "46 percentage points",
     "21 percentage points"], ans=0,
   why="Subtracting the smallest share from the largest gives the difference. The alternatives are the other two gaps within the same column and the two extreme shares read as though they were differences."),
 dict(q="The table reports hypothetical school completion figures for two regions of one country. Which conclusion does it support?",
   table=_T_REGION,
   choices=[
     "The gap between boys and girls completing secondary school is far wider in the northern region than in the southern one",
     "The gap between boys and girls is far wider in the southern region",
     "There is no gap between boys and girls in either region",
     "Girls complete secondary school more often than boys in both regions",
     "The two regions record identical completion figures"], ans=0,
   why="EK LEG-3.B.1.e records unequal gender access to education in the north and south of Nigeria, which is a claim about a gap differing between two regions of one country, and the table shows exactly that shape."),
 dict(q="According to the same table of completion figures, the gap between boys and girls in the northern region is",
   table=_T_REGION,
   choices=[
     "26 percentage points",
     "5 percentage points",
     "21 percentage points",
     "54 percentage points",
     "28 percentage points"], ans=0,
   why="Subtracting the girls' figure from the boys' figure in that row gives the gap. The alternatives are the gap in the other region, the difference between the two gaps, and that row's own two figures read as gaps."),
 dict(q="Using the same table of completion figures, the two regions' gaps between boys and girls differ by",
   table=_T_REGION,
   choices=[
     "21 percentage points",
     "26 percentage points",
     "5 percentage points",
     "17 percentage points",
     "38 percentage points"], ans=0,
   why="Working out each region's gap and subtracting the smaller from the larger gives the answer. The alternatives are the two gaps themselves and the differences between the two regions' boys' figures and girls' figures."),
 dict(q="Taking EK LEG-3.B as a whole, which summary is most accurate?",
   choices=[
     "Governments answer political, cultural and economic change with new gender equity, health care and education policies that differ in kind and in the level of government that sets them, and they run welfare programmes both to improve citizens' lives and to shore up their own legitimacy",
     "Governments create social policies only where an international organization requires them",
     "Social policy is uniform across the course countries",
     "Social welfare policy serves citizens and has no bearing on a regime's position",
     "Gender policy is the only kind of social policy the framework treats"], ans=0,
   why="EK LEG-3.B.1 supplies the prompt, the three policy areas and five examples differing in kind and in level of government, and EK LEG-3.B.2 supplies the three welfare aims together with both of the purposes the framework states for them."),
]
