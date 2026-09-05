# AP WORLD HISTORY: MODERN 9.8 Institutions Developing in a Globalized World
# CED effective Fall 2026 (Course Framework V.1), Unit 9 Globalization,
# c. 1900 to the present. Thematic focus: Governance (GOV).
# Reasoning process: Causation.
#
# TITLE. WORLD_HISTORY_topics.json gives this topic as "Institutions Developing
# in a Globalized World", and that is what is used here. The authoring brief
# records this as one of four titles in this territory reassembled by hand from
# CED pages whose columns interleave, and the JSON is the authority. It matches
# the CED page read in full.
#
# Learning Objective: Unit 9 Learning Objective H -- explain how and why
# globalization changed international interactions among states. Suggested skill
# 3.C, COMPARE THE ARGUMENTS OR MAIN IDEAS OF TWO SOURCES.
#
# THE SKILL IS THE SHAPE OF THIS BANK, AND IT IS UNIQUE IN THIS TERRITORY. No
# other topic in units 8 or 9 carries skill 3.C. So a majority of the items below
# set TWO unattributed sources side by side and ask what the comparison shows --
# where the two agree, where they differ, and what each is arguing. That is the
# real Section I question type for this skill and it is what keeps 9.8 from
# reading like a second copy of 9.7's source analysis, which is skill 2.C and
# asks about one source at a time.
#
# HISTORICAL DEVELOPMENT this topic prints -- ONE sentence:
#   KC-6.3.II.A  New international organizations, including the United Nations,
#                formed with the stated goal of maintaining world peace and
#                facilitating international cooperation.
# Where an item needs the wider claim that such bodies kept developing, it cites
# KC-6.3, which the CED reprints in Topic 8.9: the role of the state in the
# domestic economy varied, and NEW INSTITUTIONS OF GLOBAL ASSOCIATION EMERGED AND
# CONTINUED TO DEVELOP THROUGHOUT THE CENTURY. The CED prints no illustrative
# examples on this page, so no item turns on any and none is invented.
#
# THE WORD "STATED" IS THE MOST IMPORTANT WORD ON THE PAGE. KC-6.3.II.A says
# these organizations formed with the STATED GOAL of maintaining world peace and
# facilitating international cooperation. It reports what they declared they were
# for. It does NOT say they achieved it, and whether they did is a live political
# argument that the framework does not enter.
#   * NO key here says any international organization succeeded or failed at
#     keeping the peace, was effective or ineffective, or was worth having.
#   * NO key says any state was right or wrong in its dealings with such a body.
#   * Items 4, 12, 19, 23 and 29 turn on the word stated, keying the difference
#     between what an organization declared and what it accomplished. A student
#     who has read the sentence carefully is rewarded and a student who has read
#     a verdict into it is not.
#
# ALSO NOT KEYED: the framework says "new international organizations, INCLUDING
# the United Nations", so the United Nations is one of several rather than the
# whole of what the sentence describes. Items 7 and 16 hold that open, because
# treating the sentence as being only about one body would narrow it.
#
# DEDUPE NOTE. Topic 9.4 covers economic institutions, multinational corporations
# and regional trade agreements under KC-6.3.II.B, which is a different sentence
# about a different kind of body; those appear here only as distractors. Topic
# 8.3 covers the military alliances of the Cold War under KC-6.2.IV.D. This
# module stays on international organizations formed with a stated goal of peace
# and cooperation.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT. NO source here is attributed to a real person,
# organization or document, and no charter, resolution or treaty is quoted:
# every paired source is explicitly unattributed and illustrative, and each item
# turns on comparing the two arguments rather than on recognising who made them.
# TABLES are hypothetical, each states a whole and its parts, and every keyed
# conclusion is recomputed from the table alone. DATES are written "1945 to
# 1990", never with a hyphen.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("9.8", "Institutions Developing in a Globalized World", 9)

_T_MEMBERSHIP = dict(
    headers=["Year (hypothetical record of one international organization)",
             "Member states",
             "Of those, states already independent in 1945",
             "Of those, states that became independent later"],
    rows=[["1945", "50", "50", "0"],
          ["1965", "115", "50", "65"],
          ["1985", "159", "50", "109"]])

_T_FOUNDED = dict(
    headers=["Decade (hypothetical record of international organizations founded)",
             "Organizations founded",
             "Of those, whose stated purpose was maintaining peace or security",
             "Of those, whose stated purpose was something else"],
    rows=[["1940s", "12", "5", "7"],
          ["1960s", "28", "9", "19"],
          ["1980s", "41", "11", "30"]])

_T_REGISTERED = dict(
    headers=["Decade (hypothetical record of agreements registered with an international body)",
             "Agreements registered",
             "Of those, between two states only",
             "Of those, among three or more states"],
    rows=[["1950s", "400", "320", "80"],
          ["1970s", "900", "630", "270"],
          ["1990s", "1,600", "960", "640"]])

QUESTIONS = [

 dict(q="Two unattributed documents of 1946 are compared. Text 1, a founding charter of a new international body, declares that its members will settle disputes without recourse to arms. Text 2, a commentary in a national newspaper, argues that such declarations have been made before and that this one will be tested by events. Which statement best compares the two?",
   choices=[
     "Both describe the same stated goal, but Text 1 announces it while Text 2 reserves judgement on whether it will be met",
     "Both announce the same stated goal and both express confidence that it will be met",
     "Text 1 denies that the body has any stated goal, while Text 2 supplies one",
     "The two documents concern different organizations and cannot be compared",
     "Text 2 announces the goal and Text 1 reserves judgement on it"],
   ans=0,
   why="KC-6.3.II.A states that new international organizations, including the United Nations, formed with the STATED GOAL of maintaining world peace and facilitating international cooperation. The framework records what such bodies declared, and skill 3.C asks a student to compare two sources' main ideas: here a declaration of the goal and a withholding of judgement about it."),

 dict(q="According to this course, with what stated goal did the new international organizations of this period form?",
   choices=[
     "Maintaining world peace and facilitating international cooperation",
     "Maintaining world peace, with no stated aim of cooperation",
     "Facilitating international cooperation, with no stated aim concerning peace",
     "Regulating the internal economies of their member states",
     "Redrawing the political boundaries of their member states"],
   ans=0,
   why="KC-6.3.II.A states that new international organizations, including the United Nations, formed with the stated goal of MAINTAINING WORLD PEACE AND FACILITATING INTERNATIONAL COOPERATION. Both halves are in the framework's phrase, so a key naming one would report half of it."),

 dict(q="A hypothetical record divides one organization's member states into two groups at each date. Which conclusion does the table alone support?",
   table=_T_MEMBERSHIP,
   choices=[
     "Membership grew at every date recorded, and the growth came from states that became independent after 1945",
     "Membership fell at each date after the first one recorded",
     "The number of members already independent in 1945 fell across the record",
     "States that became independent after 1945 were a majority of members at every date recorded",
     "Membership was unchanged between the second and third dates recorded"],
   ans=0,
   why="KC-6.3.II.A states that new international organizations formed with the stated goal of maintaining world peace and facilitating international cooperation, and KC-6.2.III.A.i in Topic 8.6 records the creation of new states from redrawn boundaries after colonial withdrawals. A membership growing from later-independent states joins those two developments, and the record is hypothetical, with the key recomputed from the table alone in the verifier."),

 dict(q="A historian writes that this course tells us what the new international organizations were for but not whether they achieved it. Is that reading correct?",
   choices=[
     "Yes, because the framework reports their stated goal and does not assess their results",
     "No, because the framework states that they achieved their goal in full",
     "No, because the framework states that they failed to achieve their goal",
     "No, because the framework gives no goal for these organizations",
     "Yes, because the framework denies that these organizations were formed"],
   ans=0,
   why="KC-6.3.II.A says these organizations formed with the STATED GOAL of maintaining world peace and facilitating international cooperation. Stated is the framework's own word: it records the declared purpose and returns no verdict on the outcome, which is a live political argument this course does not enter."),

 dict(q="Two unattributed sources of 1970 are compared. Text 1, a note from a small state's foreign ministry, argues that membership of an international body gives it a hearing it would not otherwise get. Text 2, a note from a large state's ministry, argues that membership constrains what it may do without attracting criticism. What do the two have in common?",
   choices=[
     "Both treat membership as changing how a state can act toward others, though they value the change differently",
     "Both treat membership as leaving a state's conduct entirely unaffected",
     "Both argue that membership benefits large states and disadvantages small ones",
     "Both argue that the body in question has no members at all",
     "Neither expresses any view about the effects of membership"],
   ans=0,
   why="Unit 9 Learning Objective H asks how and why globalization changed international interactions among states, and KC-6.3.II.A supplies the new organizations through which those interactions were conducted. Skill 3.C asks a student to compare two sources' main ideas, and the shared premise here is that membership alters what a state can do, which the two sources then evaluate in opposite ways."),

 dict(q="A student writes that this course's sentence about new international organizations is about the United Nations and nothing else. What is the best correction?",
   choices=[
     "The framework says new international organizations formed, INCLUDING the United Nations, so it names one among several",
     "The framework says the United Nations was the only international organization ever formed",
     "The framework does not mention the United Nations at any point",
     "The framework says the United Nations was formed for a different stated goal from the others",
     "The framework says these organizations formed before the twentieth century"],
   ans=0,
   why="KC-6.3.II.A states that NEW INTERNATIONAL ORGANIZATIONS, INCLUDING the United Nations, formed with the stated goal of maintaining world peace and facilitating international cooperation. The word including makes the United Nations an instance of a wider class, and treating the sentence as being about one body would narrow it."),

 dict(q="A hypothetical record divides the international organizations founded in each decade by their stated purpose. Which conclusion does the table alone support?",
   table=_T_FOUNDED,
   choices=[
     "The number founded rose in each decade, and in every decade most were founded for a stated purpose other than peace or security",
     "In every decade most were founded for the stated purpose of maintaining peace or security",
     "No organization founded in the 1940s had peace or security as its stated purpose",
     "The number founded fell in each decade after the first one recorded",
     "The three decades recorded the same number of organizations founded"],
   ans=0,
   why="KC-6.3.II.A names two stated goals, maintaining world peace AND facilitating international cooperation, so cooperation covers purposes wider than peace and security alone. A record in which most bodies are founded for some other stated purpose is that breadth counted, and the figures are hypothetical, with the key recomputed from the table alone in the verifier."),

 dict(q="Two unattributed sources of 1955 are compared. Text 1 argues that a dispute between two states should go to an international body because a neutral forum will produce a settlement neither could impose. Text 2 argues that the dispute should be settled directly between the two governments because only they can bind themselves. Which best compares their main ideas?",
   choices=[
     "They disagree about where a settlement should be sought, while agreeing that a settlement is needed",
     "They disagree about whether a settlement is needed, while agreeing on where it should be sought",
     "They agree on both where the settlement should be sought and whether one is needed",
     "Neither expresses a view about how the dispute should be resolved",
     "They concern two different disputes and cannot be compared"],
   ans=0,
   why="Skill 3.C asks a student to compare the arguments or main ideas of two sources, which means locating both the shared ground and the point of difference. KC-6.3.II.A supplies the international bodies formed with the stated goal of facilitating international cooperation, and Text 1 proposes to use one where Text 2 prefers direct dealing."),

 dict(q="An unattributed diplomatic memorandum of 1962 observes that its government now deals with other governments in permanent conference halls as often as in each other's capitals. This course would treat the observation as bearing on",
   choices=[
     "how globalization changed international interactions among states",
     "how political changes led to changes in the arts",
     "how diseases associated with poverty persisted through the century",
     "how manufacturing came to be increasingly situated in Asia and Latin America",
     "how consumer culture transcended national borders"],
   ans=0,
   why="Unit 9 Learning Objective H, printed on this topic's page, is to explain how and why globalization changed international interactions among states, and KC-6.3.II.A supplies the new organizations in which those interactions came to be conducted. A shift from bilateral capitals to permanent conference halls is that change described by a participant."),

 dict(q="A hypothetical record divides the agreements registered in each decade by how many states are party to them. Which conclusion does the table alone support?",
   table=_T_REGISTERED,
   choices=[
     "The number registered rose in each decade, and the share among three or more states rose with it",
     "The number registered fell in each decade after the first one recorded",
     "The share among three or more states fell across the record",
     "The number of agreements between two states only fell in each decade recorded",
     "Most agreements were among three or more states in every decade recorded"],
   ans=0,
   why="KC-6.3.II.A states that new international organizations formed with the stated goal of facilitating international cooperation, and a rising proportion of agreements binding three or more states at once is one form such cooperation takes. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="Two unattributed sources of 1948 are compared. Text 1, from a delegation, argues that the new organization's value lies in giving small states a seat at the same table as large ones. Text 2, from a different delegation, argues that its value lies in giving large states a way to consult before acting. Which best compares their arguments?",
   choices=[
     "Both value the organization for facilitating cooperation, but each identifies a different beneficiary",
     "Both value the organization for maintaining peace, and neither mentions cooperation",
     "Text 1 values the organization and Text 2 argues it should be dissolved",
     "Both argue that the organization has no value of any kind",
     "The two texts make the same argument in the same terms"],
   ans=0,
   why="KC-6.3.II.A names facilitating international cooperation among the stated goals of these organizations, and both delegations are describing a form of that cooperation. Skill 3.C asks a student to compare two sources' main ideas, and the shared object with different beneficiaries is what the comparison yields."),

 dict(q="An unattributed report of 1994 assesses whether an international body has met the aims set out at its founding. According to this course, what does the framework itself supply about such a question?",
   choices=[
     "The aims as stated, but no assessment of whether they were met",
     "Both the aims as stated and a full assessment of whether they were met",
     "An assessment of the outcome without any statement of the aims",
     "Neither the aims nor any assessment of the outcome",
     "A ruling that such assessments cannot be made by anyone"],
   ans=0,
   why="KC-6.3.II.A records that these organizations formed with the STATED GOAL of maintaining world peace and facilitating international cooperation. The framework supplies the declared aim and stops there; whether it was met is a matter on which people disagree and on which this course takes no position."),

 dict(q="Two unattributed sources of 1981 are compared. Text 1 argues that an international agency's technical work on health and agriculture is its most valuable activity. Text 2 argues that its most valuable activity is providing a place where hostile governments still have to meet. Which best compares their main ideas?",
   choices=[
     "Both identify a form of international cooperation as valuable, but they identify different forms",
     "Both identify the same form of international cooperation as valuable",
     "Text 1 denies that international cooperation is possible and Text 2 affirms it",
     "Neither text identifies any activity as valuable",
     "Both argue that the agency should confine itself to military matters"],
   ans=0,
   why="KC-6.3.II.A names facilitating international cooperation among the stated goals of the new international organizations, and technical work and a standing forum are two forms cooperation can take. Skill 3.C asks a student to compare two sources' main ideas, and here they agree on the category and differ within it."),

 dict(q="Which statement about international organizations in this period is NOT supported by this course?",
   choices=[
     "This course records that these organizations achieved the goal they were founded for",
     "New international organizations formed during this period",
     "The United Nations is among the organizations the framework names",
     "Their stated goal included maintaining world peace",
     "Their stated goal included facilitating international cooperation"],
   ans=0,
   why="KC-6.3.II.A records the STATED GOAL of these organizations and says nothing about whether it was achieved, so a claim that the course records their achievement is the one the framework does not support. The item asks which statement is NOT supported, so the key is deliberately the false one; the other four restate parts of that sentence."),

 dict(q="Two unattributed sources of 1975 are compared. Text 1, from a recently independent state, argues that international bodies matter because they are where a small state's voice carries beyond its borders. Text 2, from the same state's opposition, argues that they matter because membership commits the government at home to standards it has publicly accepted. Which best compares the two?",
   choices=[
     "Both regard membership as consequential, one for the state's position abroad and one for its conduct at home",
     "Both regard membership as inconsequential in every respect",
     "Both regard membership as mattering only for the state's position abroad",
     "Text 1 argues for membership and Text 2 argues for withdrawal",
     "Neither text takes a position on the effects of membership"],
   ans=0,
   why="Unit 9 Learning Objective H asks how and why globalization changed international interactions among states, and KC-6.3.II.A supplies the organizations through which the change ran. Skill 3.C asks for a comparison of two sources' main ideas, and both here treat membership as consequential while locating the consequence in different places."),

 dict(q="How does this course's framework describe the relationship between the United Nations and the other organizations it refers to in this topic?",
   choices=[
     "The United Nations is named as one of the new international organizations rather than as the only one",
     "The United Nations is named as the only new international organization of the period",
     "The United Nations is described as older than the other organizations named",
     "The United Nations is described as having a different stated goal from the others",
     "The United Nations is not referred to in this topic at all"],
   ans=0,
   why="KC-6.3.II.A states that new international organizations, INCLUDING the United Nations, formed with the stated goal of maintaining world peace and facilitating international cooperation. Including places the United Nations inside a wider class and gives it the same stated goal as the rest of that class."),

 dict(q="Two unattributed sources of 1999 are compared. Text 1 argues that an international body should be judged by the disputes it has settled. Text 2 argues that it should be judged by the disputes that were never allowed to begin. Which best compares their arguments?",
   choices=[
     "They agree that the body should be judged by its effect on disputes but propose different measures of that effect",
     "They agree on the measure to be used but disagree about whether the body should be judged at all",
     "Text 1 proposes a measure and Text 2 argues that no measure is possible",
     "Both propose that the body be judged by the number of its member states",
     "Neither text proposes any basis for judging the body"],
   ans=0,
   why="Skill 3.C asks a student to compare the arguments or main ideas of two sources, locating shared ground and the point of divergence. KC-6.3.II.A gives maintaining world peace as one of these bodies' stated goals, and the two texts propose different measures of the same thing; the framework itself supplies no verdict, so neither text is keyed as correct."),

 dict(q="An unattributed conference record of 1968 shows delegates from more than a hundred states voting on a single text. According to this course, an occasion of this kind is best understood as",
   choices=[
     "an instance of the international cooperation these organizations were formed to facilitate",
     "an instance of the military alliances the Cold War produced",
     "an instance of the regional trade agreements that reflected free-market principles",
     "an instance of the redrawing of political boundaries after colonial withdrawals",
     "an instance of consumer culture transcending national borders"],
   ans=0,
   why="KC-6.3.II.A states that new international organizations formed with the stated goal of maintaining world peace and FACILITATING INTERNATIONAL COOPERATION, and a hundred delegations voting on one text is that facilitation in operation. Military alliances belong to KC-6.2.IV.D and trade agreements to KC-6.3.II.B in other topics."),

 dict(q="A commentator argues that because this course names the stated goal of these organizations, it is endorsing the claim that they kept the peace. What is the best response?",
   choices=[
     "Reporting a goal an organization declared is not the same as endorsing a claim about what it accomplished",
     "The commentator is right, because a framework that reports a goal thereby endorses it",
     "The commentator is right, because the framework says the organizations kept the peace",
     "The commentator is wrong, because the framework says the organizations failed",
     "The commentator is wrong, because the framework names no goal for these organizations"],
   ans=0,
   why="KC-6.3.II.A's word is STATED. The framework records what these bodies declared themselves to be for, which leaves entirely open what they achieved, and a course that reported the declaration is not thereby making the further claim. This is the distinction the whole topic rests on."),

 dict(q="Two unattributed sources of 1952 are compared. Text 1 argues that international organizations work because states are bound by the agreements they sign. Text 2 argues that they work only so far as the strongest members find them convenient. Which best compares the two?",
   choices=[
     "They give different accounts of what makes such organizations effective, one resting on obligation and one on the interests of powerful states",
     "They give the same account of what makes such organizations effective",
     "Text 1 says such organizations exist and Text 2 denies that they exist",
     "Neither text offers any account of how such organizations work",
     "Both argue that such organizations are effective for the same reason"],
   ans=0,
   why="Skill 3.C asks a student to compare the arguments of two sources, and here the two propose different mechanisms for the same phenomenon. KC-6.3.II.A establishes that such organizations were formed with a stated goal, and the framework itself explains neither mechanism, so the key describes the disagreement rather than settling it."),

 dict(q="What does this course say about when institutions of global association developed?",
   choices=[
     "They emerged and continued to develop throughout the century",
     "They emerged at one moment and did not develop afterward",
     "They emerged only in the last decade of the century",
     "They emerged before 1900 and ceased to develop thereafter",
     "The framework gives no indication of when they developed"],
   ans=0,
   why="KC-6.3, which the CED reprints as a review key concept in Topic 8.9, states that the role of the state in the domestic economy varied and that new institutions of global association EMERGED AND CONTINUED TO DEVELOP THROUGHOUT THE CENTURY. Both halves of that phrase are the framework's own, and a key giving only the emergence would report half of it."),

 dict(q="Two unattributed sources of 1986 are compared. Text 1, from a national government, argues that an international body has exceeded the authority its members gave it. Text 2, from that body's secretariat, argues that it has acted within the authority its founding text confers. Which best compares their main ideas?",
   choices=[
     "Both accept that the body's authority comes from its members, and they disagree about how far that authority extends",
     "Both accept that the body's authority is unlimited and disagree about how it should be used",
     "Text 1 accepts the body's authority and Text 2 denies that it has any",
     "Neither text refers to the source of the body's authority",
     "Both agree about how far the body's authority extends"],
   ans=0,
   why="KC-6.3.II.A places these organizations among the institutions through which states dealt with one another, and their authority is what their members confer. Skill 3.C asks a student to compare two sources' main ideas, and here the shared premise about the source of authority frames a disagreement about its extent."),

 dict(q="A researcher wants to test the claim that a state's dealings with other states became more multilateral over the twentieth century. Which evidence would bear most directly on the claim?",
   choices=[
     "Records over time of how many of its agreements bound it to two or more other states at once",
     "Records of its total agricultural output over the same period",
     "Records of the number of newspapers published within its borders",
     "Records of its average rainfall over the same period",
     "Records of the number of films made within its borders"],
   ans=0,
   why="Unit 9 Learning Objective H asks how and why globalization changed international interactions among states, and KC-6.3.II.A supplies the organizations formed to facilitate international cooperation. How many states an agreement binds at once is the direct measure of whether dealings became multilateral; the other records bear on developments the framework treats in other topics."),

 dict(q="Two unattributed sources of 1990 are compared. Text 1 argues that international organizations grew because states found problems they could not solve alone. Text 2 argues that they grew because a few states wished to spread their own arrangements. Which best compares the two?",
   choices=[
     "Both explain the growth of these organizations, but they attribute it to different motives",
     "Both attribute the growth of these organizations to the same motive",
     "Text 1 explains their growth and Text 2 denies that they grew",
     "Neither text attempts to explain why such organizations grew",
     "Both argue that these organizations did not grow during the century"],
   ans=0,
   why="The reasoning process the CED prints beside this topic is causation, and skill 3.C asks a student to compare two sources' arguments. KC-6.3, reprinted in Topic 8.9, records that new institutions of global association emerged and continued to develop throughout the century; the framework supplies the growth and not its motive, so the key describes two accounts of it without endorsing either."),

 dict(q="Which pair of stated goals does this course attach to the new international organizations of this period?",
   choices=[
     "Maintaining world peace, and facilitating international cooperation",
     "Maintaining world peace, and directing the domestic economies of members",
     "Facilitating international cooperation, and redrawing colonial boundaries",
     "Promoting free-market economic policies, and lowering tariffs among members",
     "Protecting national industries, and restricting migration between members"],
   ans=0,
   why="KC-6.3.II.A names exactly those two as the stated goal of the new international organizations formed in this period. Each distractor attaches one of the framework's goals to a development stated in a different sentence of this course, which is the cross-sentence error a pairing item is built to catch."),

 dict(q="Two unattributed sources of 1958 are compared. Text 1 argues that an international body's usefulness is proved by the number of states willing to join it. Text 2 argues that it is proved by whether members change their conduct after joining. Which best compares their arguments?",
   choices=[
     "Both accept that the body's usefulness can be tested, and they differ over whether membership or conduct is the test",
     "Both accept that membership is the only possible test of usefulness",
     "Text 1 argues that usefulness can be tested and Text 2 argues that it cannot",
     "Neither text suggests any way of testing the body's usefulness",
     "Both argue that no state was willing to join such a body"],
   ans=0,
   why="Skill 3.C asks a student to compare the arguments or main ideas of two sources, which means naming the common ground and the disagreement. KC-6.3.II.A establishes the organizations and their stated goal, and the framework provides no test of usefulness, so the key reports the two proposed tests rather than choosing between them."),

 dict(q="An unattributed handbook of 1972 lists more than two hundred bodies through which governments meet one another regularly. Within this course's framework, the handbook documents",
   choices=[
     "institutions of global association that emerged and continued to develop through the century",
     "the military alliances the Cold War produced between and within blocs",
     "the multinational corporations that reflected free-market principles",
     "the nationalist parties that sought independence from imperial rule",
     "the movements that used violence against civilians for political aims"],
   ans=0,
   why="KC-6.3, reprinted as a review key concept in Topic 8.9, states that new institutions of global association emerged and continued to develop throughout the century, and KC-6.3.II.A names the international organizations formed with a stated goal of peace and cooperation. Two hundred standing bodies is that development counted; the distractors name developments the framework states in other topics."),

 dict(q="Two unattributed sources of 1965 are compared. Text 1 argues that an international organization changed how its members behave toward one another. Text 2 argues that its members behave as their interests dictate and would have done so in any case. What is the disagreement between them?",
   choices=[
     "Whether the organization made a difference to its members' conduct, which the framework does not settle",
     "Whether the organization exists, which the framework settles in Text 2's favour",
     "Whether the organization had a stated goal, which the framework settles in Text 1's favour",
     "Whether states have interests at all, which the framework settles in Text 1's favour",
     "Nothing, since the two texts make the same claim"],
   ans=0,
   why="KC-6.3.II.A records the STATED GOAL of these organizations and returns no verdict on their effect, so the disagreement between the two texts is exactly the question the framework leaves open. Skill 3.C asks a student to compare two sources' main ideas, and locating an unsettled question is part of that comparison."),

 dict(q="Considered across this topic, what does this course establish about the international organizations of this period?",
   choices=[
     "That new ones formed, that the United Nations is among them, and that their stated goal was world peace and international cooperation",
     "That only one such organization formed and that its goal was never stated",
     "That such organizations formed and that the framework judges them to have succeeded",
     "That such organizations formed and that the framework judges them to have failed",
     "That no such organizations formed during the twentieth century"],
   ans=0,
   why="KC-6.3.II.A is one sentence containing exactly three assertions: that new international organizations formed, that the United Nations is among them, and that their stated goal was maintaining world peace and facilitating international cooperation. The key states all three and each distractor either removes one or adds a verdict the framework withholds."),

 dict(q="Taking the topic as a whole, which single sentence best states what this course says about institutions in a globalized world?",
   choices=[
     "New international organizations, the United Nations among them, were founded declaring that they existed to keep the peace and to make cooperation between states easier, and such institutions went on developing across the century",
     "One international organization was founded, it declared no purpose, and no further institutions of the kind appeared",
     "International organizations were founded and this course records that they achieved the peace they were founded to keep",
     "International organizations were founded and this course records that they failed in the purpose they declared",
     "No institutions of global association existed at any point in the twentieth century"],
   ans=0,
   why="KC-6.3.II.A supplies the new organizations, the United Nations among them, and their stated goal of maintaining world peace and facilitating international cooperation, while KC-6.3 supplies institutions of global association emerging and continuing to develop throughout the century. The key is the conjunction of those, with the declaration reported and no verdict added, and each distractor either contradicts one or supplies a verdict the framework withholds."),
]
