# AP WORLD HISTORY: MODERN 9.5 Calls for Reform and Responses After 1900
# CED effective Fall 2026 (Course Framework V.1), Unit 9 Globalization,
# c. 1900 to the present. Thematic focus: Social Interactions and Organization
# (SIO). Reasoning process: Continuity and Change.
#
# TITLE. WORLD_HISTORY_topics.json gives this topic as "Calls for Reform and
# Responses After 1900", and that is what is used here. The authoring brief
# records this as one of four titles in this territory reassembled by hand from
# CED pages whose columns interleave, and the JSON is the authority. It matches
# the CED page read in full.
#
# Learning Objective: Unit 9 Learning Objective E -- explain how social
# categories, roles, and practices have been maintained and challenged over time.
# BOTH VERBS ARE IN THE OBJECTIVE. Suggested skill 4.B, explain how a specific
# historical development or process is situated within a broader historical
# context, so most items put a particular local development in front of the
# student and ask which broader process it belongs inside.
#
# HISTORICAL DEVELOPMENTS this topic prints, and the only sentences the keys
# below rest on:
#   KC-6.3.III.i   Rights-based discourses challenged old assumptions about race,
#                  class, gender, and religion.
#   KC-6.3.III.ii  In much of the world, access to education as well as
#                  participation in new political and professional roles became
#                  more inclusive in terms of race, class, gender, and religion.
#   KC-6.3.II.C    Movements throughout the world protested the inequality of the
#                  environmental and economic consequences of global integration.
#
# "IN MUCH OF THE WORLD" IS LOAD-BEARING. KC-6.3.III.ii does not say everywhere,
# and a bank that flattened it into a universal would teach the opposite of the
# framework's own sentence in a topic where the temptation to write a story of
# uniform progress is strong. Items 9, 17 and 26 hold the qualifier open, and
# Learning Objective E's pairing of MAINTAINED with CHALLENGED does the same work
# at the level of the whole topic: items 5, 14, 22 and 29 turn on the fact that
# the objective asks for both.
#
# ILLUSTRATIVE EXAMPLES the CED prints on this page, in four lists:
#   Challenges to assumptions about race, class, gender, and religion: the U.N.
#     Universal Declaration of Human Rights, especially as it sought to protect
#     the rights of children, women, and refugees; global feminism movements; the
#     Negritude movement; liberation theology in Latin America.
#   Increased access to education and political and professional roles: the right
#     to vote and/or to hold public office granted to women in the United States,
#     Brazil, Turkey, Japan, India and Morocco; the rising rate of female
#     literacy and the increasing numbers of women in higher education, in most
#     parts of the world; the U.S. Civil Rights Act; the end of apartheid; caste
#     reservation in India.
#   Environmental movements: Greenpeace; Professor Wangari Maathai's Green Belt
#     Movement in Kenya.
#   Economic movements: the World Fair Trade Organization.
# Illustrative examples are optional course content, so exactly TWO items turn on
# them and both stems say the course prints them as such.
#
# ONE DATE IN THE CED IS NOT KEYED HERE, DELIBERATELY. The CED's second list
# prints "The U.S. Civil Rights Act of 1965". The Civil Rights Act is of 1964 and
# the Voting Rights Act is of 1965, so the CED's year does not match the statute
# its own words name. This bank does not resolve that: NO item keys that date, or
# any date from that list, and the second list is not the one either
# illustrative-example item uses. Keying a year that may be an error in the
# source would teach the error, and the rule in HISTORY_BRIEF.md is that an
# uncertain question is cut rather than guessed.
#
# CONTESTED GROUND, AND THE CARE THIS TOPIC NEEDS MOST. This page is about race,
# class, gender and religion, and about apartheid and caste. Every key here is
# limited to what the framework's three sentences state. NO key evaluates any
# group, belief or religion; NO key states that any particular reform was
# sufficient, insufficient, too fast or too slow; NO key assigns a motive to any
# group of people; and NO key describes any social category as natural or as
# deserved. The framework's own claims are that rights-based discourses
# challenged old assumptions, that access became more inclusive in much of the
# world, and that movements protested the inequality of certain consequences.
# Those are what is keyed.
#
# DEDUPE NOTE. Topic 9.3 covers the environmental changes themselves; the
# environmental MOVEMENTS belong here under KC-6.3.II.C and appear in 9.3 only as
# distractors. Topic 9.7 covers responses to globalization under KC-6.3.IV.iv,
# which is a wider sentence about responses taking a variety of forms; this
# module stays on KC-6.3.II.C's narrower claim about protesting the INEQUALITY of
# environmental and economic consequences. Topic 8.7 covers reactions to power
# structures in the age of the Cold War.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT and none is attributed to a real person or document.
# TABLES are hypothetical, each states a whole and its parts, and every keyed
# conclusion is recomputed from the table alone. DATES are written "1950 to
# 1990", never with a hyphen.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("9.5", "Calls for Reform and Responses After 1900", 9)

_T_UNIVERSITY = dict(
    headers=["Period (hypothetical record of one country's university entrants, thousands)",
             "Entrants recorded",
             "Of those, women",
             "Of those, men"],
    rows=[["1950", "20", "3", "17"],
          ["1970", "60", "18", "42"],
          ["1990", "140", "63", "77"]])

_T_LEGISLATURE = dict(
    headers=["Period (hypothetical record of one national legislature)",
             "Seats in the legislature",
             "Of those, held by women",
             "Of those, held by men"],
    rows=[["1950", "200", "4", "196"],
          ["1975", "200", "22", "178"],
          ["2000", "240", "72", "168"]])

_T_PROTESTS = dict(
    headers=["Decade (hypothetical record of organized protests about global integration)",
             "Protests recorded",
             "Of those, whose stated grievance was chiefly environmental",
             "Of those, whose stated grievance was chiefly economic"],
    rows=[["1970s", "60", "22", "38"],
          ["1980s", "95", "40", "55"],
          ["1990s", "160", "74", "86"]])

QUESTIONS = [

 dict(q="A declaration adopted by an international body in 1948 states that certain entitlements belong to every person without distinction, and it is cited over the following decades by campaigners in many countries who had been told their claims were matters of custom rather than of right. This course would situate the declaration within",
   choices=[
     "the rights-based discourses that challenged old assumptions about race, class, gender, and religion",
     "the movements that protested the inequality of the consequences of global integration",
     "the growth of knowledge economies in some regions of the world",
     "the redrawing of political boundaries after the withdrawal of colonial authorities",
     "the reduction of the problem of geographic distance by new technologies"],
   ans=0,
   why="KC-6.3.III.i states that rights-based discourses challenged old assumptions about race, class, gender, and religion, and the CED prints the U.N. Universal Declaration of Human Rights among its illustrative examples of exactly that. A document asserting entitlements without distinction, taken up by campaigners against arguments from custom, is that discourse in its characteristic use."),

 dict(q="According to this course, in what terms did access to education and participation in new political and professional roles become more inclusive?",
   choices=[
     "In terms of race, class, gender, and religion",
     "In terms of age and place of birth only",
     "In terms of language and citizenship only",
     "In terms of wealth alone, with no other distinction affected",
     "In no terms that the framework identifies"],
   ans=0,
   why="KC-6.3.III.ii states that in much of the world, access to education as well as participation in new political and professional roles became more inclusive IN TERMS OF RACE, CLASS, GENDER, AND RELIGION. Those four are the framework's own list, and they are the same four that KC-6.3.III.i names as the subjects of the old assumptions rights-based discourses challenged."),

 dict(q="A hypothetical record divides one country's university entrants into two groups in each period. Which conclusion does the table alone support?",
   table=_T_UNIVERSITY,
   choices=[
     "The number of entrants rose in each period, and the share of them who were women rose with it",
     "The number of entrants fell in each period after the first one recorded",
     "The share of entrants who were women fell across the record",
     "Women were a majority of entrants in every period recorded",
     "The number of men entering fell in each period recorded"],
   ans=0,
   why="KC-6.3.III.ii states that in much of the world access to education became more inclusive in terms of race, class, gender, and religion, and the CED prints the increasing numbers of women in higher education among its illustrative examples. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="This course states that movements throughout the world protested something in particular about global integration. What was it?",
   choices=[
     "The inequality of its environmental and economic consequences",
     "The speed at which its technologies were adopted",
     "The languages in which its agreements were written",
     "The number of states that took part in it",
     "The absence of any consequences at all"],
   ans=0,
   why="KC-6.3.II.C states that movements throughout the world protested the INEQUALITY OF THE ENVIRONMENTAL AND ECONOMIC CONSEQUENCES of global integration. The framework names the inequality of two specific kinds of consequence as the object of the protest, and the key states both kinds because the sentence does."),

 dict(q="A social historian argues that a category can be challenged and maintained at the same time. Which pairing from this course's framework best illustrates that possibility?",
   choices=[
     "Rights-based discourses challenged old assumptions, while access became more inclusive in much of the world rather than in all of it",
     "Rights-based discourses challenged old assumptions, and every old assumption ceased to be held anywhere",
     "Access became more inclusive everywhere, and no assumption was ever challenged",
     "Neither the assumptions nor the access altered at any point in the century",
     "Old assumptions were maintained everywhere and no discourse challenged them"],
   ans=0,
   why="KC-6.3.III.i states that rights-based discourses challenged old assumptions and KC-6.3.III.ii that access became more inclusive IN MUCH OF THE WORLD. Unit 9 Learning Objective E asks how social categories, roles and practices were both MAINTAINED and CHALLENGED, and a challenge that reached much of the world rather than all of it is both at once."),

 dict(q="An unattributed university prospectus of 1975 announces that places will henceforth be awarded on examination results alone, and notes that this reverses a rule under which certain applicants had not been eligible. Within this course's framework, the change belongs to",
   choices=[
     "access to education becoming more inclusive in terms of race, class, gender, and religion",
     "the growth of knowledge economies following revolutions in communications technology",
     "the movements protesting the inequality of the consequences of global integration",
     "the strong role governments took in guiding economic life after independence",
     "the encouragement of free-market economic policies in the late twentieth century"],
   ans=0,
   why="KC-6.3.III.ii states that in much of the world, access to education as well as participation in new political and professional roles became more inclusive in terms of race, class, gender, and religion. A rule of eligibility replaced by open examination is that widening of access in one institution, and skill 4.B asks a student to situate the specific change inside the broader process."),

 dict(q="This course prints certain developments as illustrative examples of challenges to old assumptions about race, class, gender, and religion. Which list is the one the course prints?",
   choices=[
     "The U.N. Universal Declaration of Human Rights, global feminism movements, the Negritude movement, and liberation theology in Latin America",
     "Greenpeace, the Green Belt Movement in Kenya, and the World Fair Trade Organization",
     "The World Trade Organization, NAFTA, and ASEAN",
     "Shining Path and Al-Qaeda",
     "The Indian National Congress and the Muslim League in British India"],
   ans=0,
   why="The CED prints these four beside KC-6.3.III.i as illustrative examples of challenges to assumptions about race, class, gender, and religion. The second list is this page's separate examples of environmental and economic movements, and the rest are printed beside statements in other topics, on regional trade agreements, on movements that used violence and on nationalist parties."),

 dict(q="A hypothetical record divides the seats of one national legislature into two groups in each period. Which conclusion does the table alone support?",
   table=_T_LEGISLATURE,
   choices=[
     "The number of seats held by women rose at every point recorded, and by the last period they held more than a quarter of the seats",
     "Women held no seats at all in the earliest period recorded",
     "The share of seats held by women fell across the record",
     "Women held a majority of the seats in the last period recorded",
     "The legislature had the same number of seats in every period recorded"],
   ans=0,
   why="KC-6.3.III.ii states that in much of the world participation in new political roles became more inclusive in terms of race, class, gender, and religion, and the CED prints the granting of the right to vote and to hold public office to women among its illustrative examples. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="A student writes that this course says access to education became more inclusive everywhere in the world. What is the best correction?",
   choices=[
     "The framework says this happened in much of the world, which is not the same as everywhere",
     "The framework says this happened nowhere in the world during this period",
     "The framework says access to education became less inclusive during this period",
     "The framework says access changed only in terms of religion and in no other terms",
     "The framework says access to education is not a subject it treats"],
   ans=0,
   why="KC-6.3.III.ii states that IN MUCH OF THE WORLD, access to education as well as participation in new political and professional roles became more inclusive in terms of race, class, gender, and religion. Much of the world is the framework's own qualifier and it rules out the universal claim as well as the opposite absolute, so the correction has to preserve the middle position."),

 dict(q="An unattributed leaflet distributed at a port in 1994 argues that the benefits of a new trade route have gone to distant shareholders while the fishing grounds it disturbed belonged to the people who live there. This course would situate the leaflet within",
   choices=[
     "the movements that protested the inequality of the environmental and economic consequences of global integration",
     "the rights-based discourses that challenged old assumptions about race and religion",
     "the growth of knowledge economies in some regions of the world",
     "the nationalist parties that sought independence from imperial rule",
     "the international organizations formed to maintain world peace"],
   ans=0,
   why="KC-6.3.II.C states that movements throughout the world protested the inequality of the environmental and economic consequences of global integration. A leaflet contrasting distant beneficiaries with local costs to a fishery joins the environmental and the economic grievance in the framework's own pairing."),

 dict(q="How does this course describe what rights-based discourses did?",
   choices=[
     "They challenged old assumptions about race, class, gender, and religion",
     "They confirmed old assumptions about race, class, gender, and religion",
     "They replaced discussion of race and religion with discussion of trade",
     "They were confined to a single region and to a single decade",
     "They had no bearing on assumptions of any kind"],
   ans=0,
   why="KC-6.3.III.i states that rights-based discourses CHALLENGED old assumptions about race, class, gender, and religion. Challenged is the framework's own verb and the four categories are its own list, so a key confirming those assumptions would reverse the sentence."),

 dict(q="A hypothetical record divides the organized protests of each decade into two groups by their stated grievance. Which conclusion does the table alone support?",
   table=_T_PROTESTS,
   choices=[
     "The number of protests rose in each decade, and grievances of both kinds are recorded in every decade",
     "Only grievances that were chiefly economic are recorded in the table",
     "Only grievances that were chiefly environmental are recorded in the table",
     "The number of protests fell in each decade after the first one recorded",
     "Grievances that were chiefly environmental outnumbered the chiefly economic in every decade"],
   ans=0,
   why="KC-6.3.II.C states that movements throughout the world protested the inequality of the ENVIRONMENTAL AND ECONOMIC consequences of global integration, naming both kinds of grievance. A record in which both appear in every decade is that pairing counted, and the figures are hypothetical, with the key recomputed from the table alone in the verifier."),

 dict(q="An unattributed memoir of 1988 recalls that the writer was the first person in her family permitted to sit a professional examination, and that within twenty years such candidates were unremarkable. Within this course's framework, her experience belongs to",
   choices=[
     "participation in new professional roles becoming more inclusive during this period",
     "the protest against the inequality of the consequences of global integration",
     "the growth of multinational corporations in the late twentieth century",
     "the migration of former colonial subjects to imperial metropoles",
     "the reduction of the problem of geographic distance by new technologies"],
   ans=0,
   why="KC-6.3.III.ii states that in much of the world, participation in new political and professional roles became more inclusive in terms of race, class, gender, and religion. A first admission to a professional examination followed by its becoming unremarkable is that widening across one working life, which skill 4.B asks a student to situate in the broader process."),

 dict(q="Which pair does Unit 9 Learning Objective E ask a student to explain about social categories, roles, and practices?",
   choices=[
     "How they have been maintained and how they have been challenged over time",
     "How they were created and how they were abolished within a single decade",
     "How they were measured and how they were recorded in official statistics",
     "How they were exported from one region to another by trade",
     "How they were replaced by economic categories during the twentieth century"],
   ans=0,
   why="Unit 9 Learning Objective E, printed on this topic's page, is to explain how social categories, roles, and practices have been MAINTAINED AND CHALLENGED over time. Both verbs are in the objective, which is why a bank that told only a story of change would be answering half of it."),

 dict(q="Two unattributed pamphlets of 1969 argue for the same reform, one from the premise that it is owed as a matter of right and one from the premise that it will raise the country's output. According to this course, the first belongs to",
   choices=[
     "the rights-based discourses the framework names as challenging old assumptions",
     "the free-market economic policies many governments encouraged",
     "the state direction of economic life in newly independent countries",
     "the movements protesting the consequences of global integration",
     "the international organizations formed to maintain world peace"],
   ans=0,
   why="KC-6.3.III.i states that rights-based discourses challenged old assumptions about race, class, gender, and religion, and an argument from what is owed as of right is that kind of discourse by its own premise. The second pamphlet argues from output rather than from entitlement, which is what distinguishes the two."),

 dict(q="This course prints certain organizations as illustrative examples of environmental and economic movements. Which list is the one the course prints?",
   choices=[
     "Greenpeace, the Green Belt Movement in Kenya, and the World Fair Trade Organization",
     "The U.N. Universal Declaration of Human Rights and liberation theology in Latin America",
     "Nestle, Nissan, and Mahindra and Mahindra",
     "The World Trade Organization, NAFTA, and ASEAN",
     "The Non-Aligned Movement and the Warsaw Pact"],
   ans=0,
   why="The CED prints Greenpeace and Professor Wangari Maathai's Green Belt Movement in Kenya as its environmental movements, and the World Fair Trade Organization as its economic movement, beside KC-6.3.II.C. The second option is this page's separate list of challenges to old assumptions, and the rest are printed beside statements in other topics."),

 dict(q="A comparative study of 1995 finds that in some countries a professional qualification is now open to applicants it once excluded, while in others the same exclusions remain in force. How does this course's framework accommodate both findings?",
   choices=[
     "It states that access became more inclusive in much of the world, which allows for places where it did not",
     "It states that access became more inclusive everywhere, so the second finding must be an error",
     "It states that access became less inclusive everywhere, so the first finding must be an error",
     "It states that access to professional roles is not a subject the framework treats",
     "It states that exclusions of this kind existed only before 1900"],
   ans=0,
   why="KC-6.3.III.ii states that IN MUCH OF THE WORLD access to education and participation in new political and professional roles became more inclusive. The qualifier is what makes room for both findings at once, and a framework asserting a universal change could not accommodate the second."),

 dict(q="An unattributed conference resolution of 1992 argues that the costs of a new industrial zone fall on the districts nearest it while its earnings leave the region entirely. Which of this course's statements does the resolution match?",
   choices=[
     "That movements protested the inequality of the environmental and economic consequences of global integration",
     "That rights-based discourses challenged old assumptions about race and class",
     "That access to education became more inclusive in much of the world",
     "That governments encouraged free-market policies in the late twentieth century",
     "That industrial production was increasingly situated in Asia and Latin America"],
   ans=0,
   why="KC-6.3.II.C states that movements throughout the world protested the inequality of the environmental and economic consequences of global integration. Costs falling locally while earnings leave the region is that inequality stated in both of the framework's two registers at once, the environmental and the economic."),

 dict(q="Which statement about reform in this period is NOT supported by this course?",
   choices=[
     "Access to education and to political roles became equally inclusive in every part of the world",
     "Rights-based discourses challenged old assumptions about race, class, gender, and religion",
     "Access to education became more inclusive in much of the world",
     "Participation in new political and professional roles became more inclusive in much of the world",
     "Movements protested the inequality of the consequences of global integration"],
   ans=0,
   why="KC-6.3.III.ii says IN MUCH OF THE WORLD, so equal inclusiveness in every part of the world is the claim the framework does not support. The item asks which statement is NOT supported, so the key is deliberately the false one; the other four restate KC-6.3.III.i, KC-6.3.III.ii and KC-6.3.II.C."),

 dict(q="A researcher wants to test the claim that participation in political roles became more inclusive in a particular country. Which evidence would bear most directly on the claim?",
   choices=[
     "Records over time of who was eligible to vote and to hold office, and of who actually did so",
     "Records of the country's total exports over the same years",
     "Records of the number of newspapers published in the country",
     "Records of the country's rainfall over the same period",
     "Records of the languages spoken in neighbouring countries"],
   ans=0,
   why="KC-6.3.III.ii states that in much of the world participation in new political roles became more inclusive in terms of race, class, gender, and religion, so eligibility and actual participation over time are the direct measures. The other records bear on developments the framework treats in other topics."),

 dict(q="An unattributed address to a students' association in 1966 argues that a people's own art and thought should be valued on their own terms rather than measured against another's. Within this course's framework, the address belongs among",
   choices=[
     "the challenges to old assumptions about race that this course places among rights-based discourses",
     "the protests against the inequality of the economic consequences of global integration",
     "the campaigns for the redistribution of land and resources within states",
     "the movements that sought independence from imperial rule after 1900",
     "the international organizations formed to facilitate cooperation among states"],
   ans=0,
   why="KC-6.3.III.i states that rights-based discourses challenged old assumptions about race, class, gender, and religion, and the CED prints the Negritude movement among its illustrative examples of such challenges. An argument that a people's art and thought be valued on their own terms is a challenge to an assumption about race in the framework's sense, and the key describes the argument without evaluating it."),

 dict(q="A historian writes that in this period some social practices altered greatly while others held firm. How does this course's framework bear on that observation?",
   choices=[
     "It supports it, since the objective for this topic asks about categories both maintained and challenged",
     "It contradicts it, since the framework states that every social practice altered",
     "It contradicts it, since the framework states that no social practice altered",
     "It is silent, since the framework does not treat social practices at all",
     "It supports it only for the years before 1900"],
   ans=0,
   why="Unit 9 Learning Objective E asks a student to explain how social categories, roles, and practices have been MAINTAINED AND CHALLENGED over time, which is exactly the mixture the historian describes. KC-6.3.III.ii's qualifier, in much of the world, supplies the same mixture inside a single sentence."),

 dict(q="An unattributed campaign circular of 1971 asks readers in wealthy countries to pay more for goods so that the people who grow them receive more. Within this course's framework, the circular belongs to",
   choices=[
     "the movements protesting the inequality of the economic consequences of global integration",
     "the rights-based discourses challenging old assumptions about gender and religion",
     "the growth of knowledge economies in some regions of the world",
     "the encouragement of free-market policies by governments in the late twentieth century",
     "the reduction of the problem of geographic distance by new modes of transport"],
   ans=0,
   why="KC-6.3.II.C states that movements throughout the world protested the inequality of the environmental and economic consequences of global integration, and the CED prints the World Fair Trade Organization among its illustrative examples of economic movements. A campaign to change what growers receive is that protest expressed as a proposal."),

 dict(q="Which of the following did this course's framework identify as becoming more inclusive in much of the world?",
   choices=[
     "Access to education, and participation in new political and professional roles",
     "Access to education alone, with political and professional roles unchanged",
     "Participation in political roles alone, with education unchanged",
     "Membership of international organizations, and nothing else",
     "Ownership of multinational corporations, and nothing else"],
   ans=0,
   why="KC-6.3.III.ii names two things together: access to education AS WELL AS participation in new political and professional roles. A key confined to one of the two would report half of the framework's sentence, which is why the anchor carries both."),

 dict(q="An examination candidate must situate a 1980 campaign for equal admission to a profession within a broader historical context. Which approach best does that?",
   choices=[
     "Relating the campaign to the period's rights-based discourses and to the widening of access in much of the world",
     "Counting how many signatures the campaign's petition collected and reporting the total",
     "Describing the typeface in which the campaign's literature was printed",
     "Listing every other campaign that took place anywhere in 1980",
     "Judging whether the campaign's language would suit a modern reader"],
   ans=0,
   why="KC-6.3.III.i supplies the rights-based discourses that challenged old assumptions and KC-6.3.III.ii the widening of access in much of the world, which are the broader processes a 1980 admission campaign sits inside. Skill 4.B, the suggested skill for this topic, asks a student to situate a specific development within a broader context, which counts and typefaces do not do."),

 dict(q="Two developments are set side by side: rights-based arguments made in public, and changes in who could enter schools and hold office. What relation does this course draw between them?",
   choices=[
     "The framework states both, the first as a challenge to old assumptions and the second as a widening of access in much of the world",
     "The framework states the first and denies that the second occurred",
     "The framework states the second and denies that the first occurred",
     "The framework treats the two as belonging to different centuries",
     "The framework treats the two as having no bearing on social categories"],
   ans=0,
   why="KC-6.3.III.i states that rights-based discourses challenged old assumptions about race, class, gender, and religion, and KC-6.3.III.ii that in much of the world access to education and participation in new political and professional roles became more inclusive in those same four terms. The framework asserts both and the key states each with its own description."),

 dict(q="A district council's minute of 1983 records a decision to plant trees on common land, taken after residents argued that the loss of woodland had fallen hardest on the households with least. This course would situate the decision within",
   choices=[
     "the movements protesting the inequality of the environmental consequences of global integration",
     "the rights-based discourses challenging old assumptions about class and religion",
     "the widening of access to education in much of the world",
     "the growth of multinational corporations in the late twentieth century",
     "the reduction of the problem of geographic distance by new communications"],
   ans=0,
   why="KC-6.3.II.C states that movements throughout the world protested the INEQUALITY of the environmental and economic consequences of global integration, and the CED prints the Green Belt Movement in Kenya among its illustrative examples of environmental movements. Residents arguing that a loss fell hardest on the poorest is that inequality stated as the ground of the protest."),

 dict(q="Considered across this topic, what does this course say about the four categories of race, class, gender, and religion?",
   choices=[
     "Old assumptions about all four were challenged, and access widened in terms of all four in much of the world",
     "Old assumptions about all four were confirmed, and access narrowed in terms of all four",
     "Only assumptions about class were challenged, and the other three were untouched",
     "The four categories ceased to exist in any society during the twentieth century",
     "The framework treats the four categories as unconnected with education or office"],
   ans=0,
   why="KC-6.3.III.i names race, class, gender, and religion as the subjects of the old assumptions rights-based discourses challenged, and KC-6.3.III.ii names the same four as the terms in which access became more inclusive in much of the world. The framework uses one list twice, which is what the key reports, and it does not say the categories disappeared."),

 dict(q="An unattributed pastoral letter circulated in a Latin American diocese in 1974 argues that the condition of the poorest of its parishioners is a matter its faith obliges it to address rather than a fact to be accepted. This course would situate the letter within",
   choices=[
     "the rights-based discourses that challenged old assumptions about class and religion",
     "the movements that protested the inequality of the environmental consequences of global integration",
     "the widening of access to education and professional roles in much of the world",
     "the encouragement of free-market economic policies by governments late in the century",
     "the growth of knowledge economies following revolutions in communications technology"],
   ans=0,
   why="KC-6.3.III.i states that rights-based discourses challenged old assumptions about race, class, gender, and religion, and the CED prints liberation theology in Latin America among its illustrative examples of such challenges. A letter treating the condition of the poorest as an obligation rather than a given challenges an assumption about class from within a religious tradition, which is both of the framework's categories at once; the key describes the argument and does not evaluate the faith it is made in."),

 dict(q="Taking the topic as a whole, which single sentence best states what this course says about calls for reform after 1900?",
   choices=[
     "Arguments framed as rights unsettled long-held assumptions about race, class, gender and religion, schooling and public and professional office opened to more people across much of the world, and movements objected that the gains and costs of global integration fell unevenly",
     "Long-held assumptions about race, class, gender and religion went unchallenged, and nothing about who could enter schools or hold office altered",
     "Access to education and office became equally open in every country in the world, and no one objected to anything about global integration",
     "The century's reforms concerned trade and taxation alone and left social categories untouched",
     "Movements objected to global integration on grounds the framework does not identify, and no reform of any kind followed"],
   ans=0,
   why="KC-6.3.III.i supplies the rights-based challenge to old assumptions about the four categories, KC-6.3.III.ii the widening of access to education and to political and professional roles in much of the world, and KC-6.3.II.C the movements protesting the inequality of the environmental and economic consequences of global integration. The key is the conjunction of the three with the qualifier intact, and each distractor contradicts at least one."),
]
