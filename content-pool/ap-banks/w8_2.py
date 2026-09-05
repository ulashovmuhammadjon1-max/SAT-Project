# AP WORLD HISTORY: MODERN 8.2 The Cold War
# CED effective Fall 2026 (Course Framework V.1), Unit 8 Cold War and
# Decolonization, c. 1900 to the present. Thematic focus: Cultural Developments
# and Interactions (CDI).
#
# Learning Objective: Unit 8 Learning Objective B -- explain the causes and
# effects of the ideological struggle of the Cold War. Suggested skill 2.B,
# explain the point of view, purpose, historical situation, and/or audience of
# a source. This bank leans on that skill deliberately: most items here ask what
# a source was FOR and whom it addressed, which is what distinguishes 8.2 from
# 8.1's contextualization and from 8.3's comparison of superpower methods.
#
# HISTORICAL DEVELOPMENTS this topic prints, and the only sentences the keys
# below rest on:
#   KC-6.2.IV.C.ii  The global balance of economic and political power shifted
#                   during and after World War II and rapidly evolved into the
#                   Cold War. The democracy of the United States and the
#                   authoritarian communist Soviet Union emerged as superpowers,
#                   which led to ideological conflict and a power struggle
#                   between capitalism and communism across the globe.
#   KC-6.2.V.B      Groups and individuals, including the Non-Aligned Movement,
#                   opposed and promoted alternatives to the existing economic,
#                   political, and social orders.
# ILLUSTRATIVE EXAMPLES the CED prints for the Non-Aligned Movement: Sukarno in
# Indonesia; Kwame Nkrumah in Ghana. Illustrative examples are optional in the
# course, so exactly one item below turns on them and it says so in its stem.
#
# SOURCES. Every stimulus is TEXT and none is attributed to a real person or
# document. Each is an explicitly illustrative, unattributed source of the
# period, and every key turns on reasoning about purpose, audience or situation
# rather than on recognising an author. Inventing a speech for a named
# twentieth-century leader would be read by a student as fact.
#
# CONTESTED GROUND. The Cold War invites live political disagreement about who
# was at fault. Nothing here keys a side. The framework's own sentence describes
# two superpowers, an ideological conflict and a movement that opposed both, and
# the keys go no further than that.
#
# DATES. Spans are written "1945 to 1991", never with a hyphen, and no key
# depends on a boundary year: the CED states that events and processes "are not
# constrained by the given dates and may begin before, or continue after, the
# period".
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("8.2", "The Cold War", 8)

_T_ALIGN = dict(
    headers=["Region (hypothetical survey, 1961)", "States represented",
             "States declaring a formal alliance with a superpower"],
    rows=[["Africa", "23", "6"],
          ["Asia", "19", "7"],
          ["Latin America", "9", "4"]])

_T_BROADCAST = dict(
    headers=["Decade (hypothetical estimate)",
             "Weekly hours of foreign-language broadcasting, bloc one",
             "Weekly hours of foreign-language broadcasting, bloc two"],
    rows=[["1940s", "600", "500"],
          ["1950s", "1,400", "1,300"],
          ["1960s", "2,100", "2,200"]])

_T_STUDENTS = dict(
    headers=["Host (hypothetical count)",
             "Students from newly independent states, 1955",
             "Students from newly independent states, 1970"],
    rows=[["Bloc one", "12,000", "41,000"],
          ["Bloc two", "4,000", "33,000"],
          ["Neither bloc", "9,000", "12,000"]])

QUESTIONS = [

 dict(q="A government radio service broadcast a program in 1949 in the language of a rival state, telling listeners there that their own economic system enslaved them while the broadcaster's system left people free to choose their work. Which feature of this source most limits its value as evidence about living standards in either country?",
   choices=[
     "It was produced to persuade an audience inside a rival state, so its claims are advocacy rather than measurement",
     "It was broadcast rather than printed, and spoken sources cannot be used as historical evidence",
     "It dates from 1949, which falls outside the period this course covers",
     "It concerns economics, and economic claims cannot be compared across countries",
     "It was addressed to foreigners, and no government ever addressed foreign audiences in this period"],
   ans=0,
   why="KC-6.2.IV.C.ii describes a power struggle between capitalism and communism carried on across the globe, and a broadcast beamed into a rival state is an instrument of that struggle. Recognising the purpose and audience of a source is the skill this topic practises: the program was made to win listeners, not to measure wages, so its claims about living standards are the least reliable part of it."),

 dict(q="A resolution adopted at a 1961 meeting of recently independent Asian and African states declares that the participants will grant military bases to neither of the two great blocs and will judge each international question on its own merits. The resolution is best used as evidence of",
   choices=[
     "groups and states that opposed the existing economic and political orders and promoted alternatives to them",
     "the formal enlargement of one superpower's alliance system to include Asia and Africa",
     "the disappearance of ideological disagreement from world politics by 1961",
     "the growth of knowledge economies in the regions represented at the meeting",
     "an agreement between the two superpowers to end their competition in Asia and Africa"],
   ans=0,
   why="KC-6.2.V.B states that groups and individuals, including the Non-Aligned Movement, opposed and promoted alternatives to the existing economic, political, and social orders. Refusing bases to both blocs while reserving independent judgement is that stance stated as policy, and it is the opposite of joining either alliance system."),

 dict(q="According to this course, what most directly produced the confrontation between the United States and the Soviet Union after 1945?",
   choices=[
     "A shift in the global balance of economic and political power during and after World War II that rapidly evolved into the Cold War",
     "A dispute over the succession to a European throne that drew in the great powers",
     "Competition between the two states for overseas colonies in Africa and Asia",
     "Disagreement over the causes of climate change and the release of greenhouse gases",
     "A war fought between the two states over their common border"],
   ans=0,
   why="KC-6.2.IV.C.ii states that the global balance of economic and political power shifted during and after World War II and rapidly evolved into the Cold War. The framework names that shift as the origin, not a dynastic quarrel, a colonial race or an environmental dispute."),

 dict(q="Two unattributed pamphlets from the early 1950s are set side by side. Each was published in one of the two superpowers, and each tells its readers that its own country stands for genuine freedom while the other offers only its appearance. What does the pair most reliably establish?",
   choices=[
     "That both sides described the confrontation as a contest between rival ways of organizing society",
     "That the two countries had identical economic systems and disagreed only about words",
     "That readers in both countries believed everything their governments published",
     "That the confrontation was confined to Europe and did not extend to other regions",
     "That neither government made any public argument for its own system"],
   ans=0,
   why="KC-6.2.IV.C.ii states that the emergence of the two superpowers led to ideological conflict and a power struggle between capitalism and communism. Two pamphlets in the same argumentative form establish how the contest was framed by those waging it; what readers privately believed is not something the pamphlets record."),

 dict(q="Which statement best describes what the Non-Aligned Movement, as this course presents it, sought?",
   choices=[
     "An alternative to the existing economic and political orders rather than membership in either bloc",
     "Membership in whichever of the two blocs offered its members the larger subsidy",
     "The restoration of the colonial empires that had governed its members before independence",
     "A single world government administered jointly by the two superpowers",
     "The abolition of trade between its members and the industrialized world"],
   ans=0,
   why="KC-6.2.V.B names the Non-Aligned Movement among groups and individuals that opposed and promoted alternatives to the existing economic, political, and social orders. Promoting an alternative is precisely not choosing between the two orders on offer, which is what each distractor here substitutes for it."),

 dict(q="The table records a hypothetical survey of states represented at a conference of nonaligned countries. Which conclusion does the table alone support?",
   table=_T_ALIGN,
   choices=[
     "In every region listed, fewer than half of the states represented had declared an alliance with a superpower",
     "In every region listed, more than half of the states represented had declared such an alliance",
     "The region sending the fewest states was also the region with the most declared alliances",
     "The number of states declaring an alliance was the same in all three regions",
     "Latin America was the only region in which no state had declared an alliance"],
   ans=0,
   why="KC-6.2.V.B describes groups and states promoting an alternative to the existing orders, and a conference whose participants have overwhelmingly declined formal alliance is one measure of that. The survey is hypothetical and the keyed proportion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="A 1948 government memorandum in a European country argues that its people must choose one of two protectors because no third arrangement is available. Identifying the historical situation of this memorandum most requires knowing that",
   choices=[
     "the war had left two states preeminent and the ideological struggle between them was already under way",
     "the country's own borders had been unchanged for several centuries",
     "the country had recently acquired overseas colonies in Africa",
     "the world was then debating the environmental consequences of industrial production",
     "international trade agreements had abolished tariffs across the continent"],
   ans=0,
   why="KC-6.2.IV.C.ii places the emergence of the two superpowers and the beginning of the ideological struggle in the years during and after World War II. A memorandum insisting that only two options exist is intelligible only against that situation, which is what identifying a source's historical situation means."),

 dict(q="This course offers two national leaders as illustrative examples of the Non-Aligned Movement. They are",
   choices=[
     "Sukarno in Indonesia and Kwame Nkrumah in Ghana",
     "Mohandas Gandhi in India and Martin Luther King Jr. in the United States",
     "Augusto Pinochet in Chile and Francisco Franco in Spain",
     "Deng Xiaoping in China and Margaret Thatcher in Britain",
     "Mengistu Haile Mariam in Ethiopia and Idi Amin in Uganda"],
   ans=0,
   why="The CED prints Sukarno in Indonesia and Kwame Nkrumah in Ghana as the illustrative examples accompanying KC-6.2.V.B and the Non-Aligned Movement. The other four pairs are illustrative examples the framework attaches to different statements, on nonviolence, on responses that intensified conflict and on free-market policies."),

 dict(q="An official history published in one superpower in 1960 recounts the origins of the confrontation entirely as a series of provocations by the other side. A historian reading it should treat the account primarily as",
   choices=[
     "evidence of how that government wished the confrontation to be understood",
     "a settled account of how the confrontation began, since it is an official publication",
     "proof that the other superpower bore no responsibility for the confrontation",
     "a source with no bearing on the Cold War, because it was published in 1960",
     "an impartial record, because official histories are written by trained scholars"],
   ans=0,
   why="KC-6.2.IV.C.ii describes an ideological conflict in which each side argued its case globally, and an official history is one of the instruments of that argument. Reading a source for the purpose it served, rather than for the facts it asserts about its opponent, is the skill this topic practises."),

 dict(q="A speech delivered in 1957 to an audience of factory workers in one bloc, and a diplomatic note sent the same month by the same government to a neutral state, present the confrontation in noticeably different terms. The difference is best explained by",
   choices=[
     "the different audiences the two sources address and the different purposes each was meant to serve",
     "the impossibility of a government holding any consistent position at all",
     "the fact that one of the two documents must be a forgery",
     "a change in the international situation between the beginning and the end of the month",
     "the rule that diplomatic notes are always more truthful than speeches"],
   ans=0,
   why="Explaining a source by its audience and purpose is this topic's suggested skill, and KC-6.2.IV.C.ii supplies the reason a government had both audiences to address: the struggle between capitalism and communism was carried on across the globe, before domestic publics and neutral states alike."),

 dict(q="Which statement about the geographic extent of the Cold War does this course support?",
   choices=[
     "The power struggle between capitalism and communism was carried on across the globe",
     "The power struggle was confined to Europe and to the two superpowers themselves",
     "The power struggle was fought only in states that had never been colonized",
     "The power struggle took place only in the Western Hemisphere",
     "The power struggle involved no state outside the two blocs at any point"],
   ans=0,
   why="KC-6.2.IV.C.ii states that the ideological conflict led to a power struggle between capitalism and communism across the globe. KC-6.2.V.B adds states outside both blocs to the picture, which is a further reason none of the narrower descriptions holds."),

 dict(q="The table gives a hypothetical estimate of foreign-language radio broadcasting by the two blocs. Which conclusion does the table alone support?",
   table=_T_BROADCAST,
   choices=[
     "Both blocs increased their broadcasting in every decade recorded, and the second overtook the first in the last of them",
     "Only one of the two blocs increased its broadcasting over the period recorded",
     "The first bloc broadcast more hours than the second in every decade recorded",
     "Both blocs broadcast fewer hours in the 1960s than they had in the 1940s",
     "The two blocs broadcast an identical number of hours in every decade recorded"],
   ans=0,
   why="KC-6.2.IV.C.ii describes an ideological conflict waged across the globe, and broadcasting into other countries is one form that argument took. The estimate is hypothetical and both halves of the keyed conclusion, together with the falsity of each distractor, are recomputed from the table alone in the verifier."),

 dict(q="A leaflet distributed in a newly independent African state in 1962 warns readers that accepting weapons from either great power will make their country a field on which someone else's argument is settled. The leaflet's argument aligns most closely with",
   choices=[
     "the position of groups that opposed the existing orders and promoted alternatives to both blocs",
     "the position of a state that had formally joined one of the two alliance systems",
     "an argument that the ideological struggle had already ended by 1962",
     "an argument for the restoration of colonial administration in the state concerned",
     "an argument that industrial production should be relocated to Asia and Latin America"],
   ans=0,
   why="KC-6.2.V.B states that groups and individuals, including the Non-Aligned Movement, opposed and promoted alternatives to the existing economic, political, and social orders. Refusing arms from both sides on the ground that they carry someone else's quarrel is that position argued from the receiving end."),

 dict(q="In this course's terms, the word superpower distinguishes the United States and the Soviet Union after 1945 chiefly because",
   choices=[
     "each had emerged from the war with economic and political weight that set it apart from every other state",
     "each governed a larger overseas empire in 1945 than it had governed in 1939",
     "each had a population larger than that of all other states combined",
     "each was recognized as such by a treaty signed at the war's end",
     "each had been neutral during the war and so was undamaged by it"],
   ans=0,
   why="KC-6.2.IV.C.ii ties the term to the shift in the global balance of economic and political power during and after World War II, out of which the two emerged as superpowers. The framework rests the distinction on weight relative to other states, not on empire, population, treaty recognition or neutrality."),

 dict(q="A student argues that because a 1950 propaganda poster from one bloc is one-sided, it is worthless to a historian. The best objection to this argument is that",
   choices=[
     "a one-sided source is strong evidence of the argument its makers wanted the public to accept",
     "propaganda posters were never produced in this period and the source must be misdated",
     "one-sidedness cannot be detected in a source without a written text to compare it with",
     "historians are required to treat every source as equally reliable on every question",
     "a source produced by a government is automatically accurate about its own country"],
   ans=0,
   why="KC-6.2.IV.C.ii describes an ideological conflict, and the case each side made is itself the object of study. A source's point of view limits what it can show about its opponent while making it excellent evidence of its own maker's purpose, which is the distinction this topic's skill turns on."),

 dict(q="Which pair of developments does this course place in a causal relationship?",
   choices=[
     "The postwar shift in the global balance of power, which rapidly evolved into the Cold War",
     "The Cold War, which produced the shift in the global balance of power that preceded it",
     "The Non-Aligned Movement, which created the two superpowers it later criticized",
     "The dissolution of the Soviet Union, which caused World War II a half century earlier",
     "The growth of consumer culture, which caused the ideological struggle of the 1940s"],
   ans=0,
   why="KC-6.2.IV.C.ii states that the balance of economic and political power shifted during and after World War II and rapidly evolved into the Cold War, fixing the shift as prior and the Cold War as what it became. Reversing that order, or making a later development the cause of an earlier one, is what every distractor here does."),

 dict(q="A newspaper published in a nonaligned state in 1965 runs an editorial criticizing both superpowers in the same column. Which inference about the newspaper is best supported?",
   choices=[
     "It addressed readers for whom neither bloc's account of the world was authoritative",
     "It was secretly financed by whichever superpower it criticized more gently",
     "Its editors had no opinion about international affairs of any kind",
     "It was published in a state that had joined one of the two alliance systems",
     "Its readers were unaware that a confrontation between the superpowers existed"],
   ans=0,
   why="KC-6.2.V.B places groups and states outside both orders, opposing them and promoting alternatives, which is the readership an editorial of this kind assumes. A claim about secret financing is not something the editorial's content can establish."),

 dict(q="The table gives a hypothetical count of students from newly independent states studying abroad. Which conclusion does the table alone support?",
   table=_T_STUDENTS,
   choices=[
     "The two blocs together more than tripled their intake, while the number hosted by neither bloc rose by a third",
     "Bloc two hosted more students than bloc one in both of the years recorded",
     "The number of students hosted by neither bloc fell over the period recorded",
     "Bloc one's intake grew by a larger multiple than bloc two's over the period",
     "All three hosts recorded the same number of students in 1970"],
   ans=0,
   why="KC-6.2.IV.C.ii describes a struggle between capitalism and communism carried on across the globe, and competition for the training of a newly independent state's graduates is one arena of it. The count is hypothetical and both halves of the keyed conclusion, with the falsity of each distractor, are recomputed from the table alone in the verifier."),

 dict(q="Which of the following is the weakest use of a 1953 speech by a superpower's leader broadcast to a domestic audience?",
   choices=[
     "Using it as a reliable description of conditions inside the rival superpower",
     "Using it as evidence of how the government wished its own citizens to understand the world",
     "Using it as evidence of the terms in which the confrontation was publicly framed",
     "Using it alongside a source from the other bloc to compare how each argued its case",
     "Using it as evidence that an ideological argument was being conducted in public"],
   ans=0,
   why="KC-6.2.IV.C.ii makes each side an interested party in a global ideological conflict, so a speech is authoritative about its own maker's framing and weak about the opponent it describes. Distinguishing what a source can and cannot support is the skill this topic practises."),

 dict(q="A hypothetical memoir written in the 1990s by a former official of a nonaligned government recalls the pressures the two blocs applied in the 1960s. Compared with a government document written in 1962, this memoir is",
   choices=[
     "written with knowledge of how the confrontation ended, which shapes what it treats as important",
     "necessarily more accurate, because the writer had time to reflect on the events",
     "necessarily less accurate, because all memoirs are written to flatter their authors",
     "unusable, because sources written after the events they describe are not evidence",
     "identical in value to the 1962 document, since both concern the same period"],
   ans=0,
   why="KC-6.2.V.B places nonaligned governments under pressure from both existing orders, which is what both sources describe; the difference between them is the situation each was written in. A later source knows the outcome, and that knowledge selects what it records, which is neither an automatic virtue nor an automatic fault."),

 dict(q="Which statement about the causes of the ideological struggle is NOT supported by this course?",
   choices=[
     "The struggle arose from a competition between the two superpowers for overseas colonies",
     "The struggle followed a shift in the global balance of economic and political power",
     "The struggle set an authoritarian communist state against a democracy",
     "The struggle was conducted between capitalism and communism as rival systems",
     "The struggle extended well beyond the two superpowers themselves"],
   ans=0,
   why="KC-6.2.IV.C.ii traces the confrontation to the postwar shift in the balance of economic and political power and describes it as a struggle between capitalism and communism, not as a colonial competition between the two states. The other four restate that sentence and KC-6.2.V.B."),

 dict(q="A trade union in a neutral country publishes a statement in 1959 rejecting both the private ownership of major industry and the single-party control of unions. This statement is best classified as",
   choices=[
     "an argument for an alternative to both of the existing orders",
     "an endorsement of the economic system of one of the two superpowers",
     "a claim that the two superpowers had already merged their systems",
     "a demand for the restoration of colonial rule in neutral countries",
     "a description of the union's own membership figures for that year"],
   ans=0,
   why="KC-6.2.V.B states that groups and individuals opposed and promoted alternatives to the existing economic, political, and social orders. Rejecting the characteristic arrangement of each bloc in a single statement is exactly the promotion of an alternative rather than a choice between them."),

 dict(q="Suppose a historian wishes to explain why the confrontation after 1945 took an ideological form rather than a purely territorial one. Which consideration does this course make most relevant?",
   choices=[
     "The two states that emerged preeminent were organized on rival principles, a democracy and an authoritarian communist state",
     "The two states shared a long land border over which they had quarrelled for centuries",
     "The two states each claimed the same overseas colonies at the war's end",
     "The two states had been founded in the same decade and had similar constitutions",
     "The two states depended on each other for food and could not risk a rupture"],
   ans=0,
   why="KC-6.2.IV.C.ii states that the democracy of the United States and the authoritarian communist Soviet Union emerged as superpowers, which led to ideological conflict and a power struggle between capitalism and communism. The rival principles on which the two were organized are what the framework makes the ideological form of the struggle rest on."),

 dict(q="In a hypothetical study, an anthropologist collects oral testimony in 2005 from villagers in a formerly nonaligned state about how the confrontation of the 1960s reached them. The chief strength of this evidence is that",
   choices=[
     "it records the experience of people whose governments' documents rarely mention them",
     "it is contemporaneous with the events and therefore free of hindsight",
     "it removes the need to consult any written source about the period",
     "spoken testimony is generally more accurate than written testimony",
     "it can establish the intentions of the two superpowers' governments directly"],
   ans=0,
   why="KC-6.2.IV.C.ii describes a struggle carried on across the globe, which means it reached populations far from either capital, and KC-6.2.V.B places whole societies outside both orders. Testimony gathered decades later is not contemporaneous and cannot report the superpowers' intentions, but it reaches people the official record leaves out."),

 dict(q="Which description of the relationship between the Non-Aligned Movement and the two superpowers does this course support?",
   choices=[
     "The movement opposed the existing orders that the superpowers led and promoted alternatives to them",
     "The movement was a third alliance formally allied to one of the two superpowers",
     "The movement was created by the two superpowers to manage their competition",
     "The movement supported whichever superpower held the greater nuclear arsenal",
     "The movement existed only within the borders of the two superpowers themselves"],
   ans=0,
   why="KC-6.2.V.B names the Non-Aligned Movement among the groups and individuals that opposed and promoted alternatives to the existing economic, political, and social orders. Opposing both orders is incompatible with being an alliance of, a creation of, or a supporter of either superpower."),

 dict(q="A ministry of education in one bloc revises its school textbooks in 1955 so that the chapter on the other bloc is rewritten. Considered as a source, the revision is most useful for studying",
   choices=[
     "how a government sought to shape its own population's understanding of the confrontation",
     "the actual conditions of daily life inside the bloc the chapter describes",
     "the private opinions of the schoolteachers who used the revised books",
     "the military capabilities each bloc possessed in the middle of the 1950s",
     "the level of literacy among adults in the country that made the revision"],
   ans=0,
   why="KC-6.2.IV.C.ii describes an ideological conflict in which each side argued its case, and a state textbook is one of the most deliberate forms that argument took. Reading the source for its purpose rather than for the accuracy of its description of the opponent is what this topic's skill requires."),

 dict(q="Two sources from 1962 describe the same international crisis. One is a public statement issued by a superpower's foreign ministry; the other is an internal briefing note circulated within that ministry. A historian would most reasonably expect",
   choices=[
     "the public statement to be shaped by the need to persuade audiences abroad and at home",
     "the internal note to be less candid than the public statement, since it was official",
     "the two to be identical, since they came from the same institution in the same month",
     "the public statement to contain the ministry's private assessment of its own weaknesses",
     "the internal note to have been written for a foreign audience"],
   ans=0,
   why="Distinguishing a source by its intended audience is the skill this topic practises, and KC-6.2.IV.C.ii supplies the reason a foreign ministry had audiences at home and abroad to persuade in a global ideological struggle. A document written for internal use faces no such requirement."),

 dict(q="Which of the following would count as the strongest single piece of evidence that the ideological struggle had effects outside Europe?",
   choices=[
     "Records showing both superpowers competing for influence in states that had recently become independent",
     "A list of the treaties signed between European states in the 1950s",
     "A survey of European newspaper coverage of the two superpowers",
     "The text of a debate held in one superpower's own legislature",
     "A catalogue of European art produced during the 1950s"],
   ans=0,
   why="KC-6.2.IV.C.ii states that the struggle between capitalism and communism was carried on across the globe. Evidence of competition inside newly independent states outside Europe tests that claim directly, whereas every distractor is drawn from Europe or from one superpower's internal affairs."),

 dict(q="A student writes that because a nonaligned state accepted development aid from one superpower, it must in fact have belonged to that bloc. The best correction to this reasoning is that",
   choices=[
     "accepting aid from one side is consistent with refusing alliance with either, which is the position the movement took",
     "no nonaligned state ever accepted aid from either superpower at any point",
     "development aid was offered only by states that had no interest in influence",
     "the two superpowers did not offer development aid to other countries",
     "a state's alignment can be determined only from the size of its armed forces"],
   ans=0,
   why="KC-6.2.V.B describes opposition to the existing orders and the promotion of alternatives, which is a stance toward alliance rather than a refusal of all contact. Treating any receipt of aid as membership would empty the framework's category of states that opposed both orders."),

 dict(q="Taking the topic as a whole, which single sentence best states the causes and effects of the ideological struggle as this course presents them?",
   choices=[
     "A postwar shift in economic and political power left two states preeminent on rival principles, and their struggle was carried across the globe while other groups pressed alternatives to both",
     "A quarrel over the boundaries of Europe was settled by treaty within a decade and had no effect elsewhere",
     "Two states with identical systems competed for the same colonies until one abandoned the contest",
     "The world's states divided evenly into two blocs, and no group anywhere argued for any other arrangement",
     "The struggle began as an argument about the environment and only later took an economic form"],
   ans=0,
   why="KC-6.2.IV.C.ii supplies the shift, the two superpowers organized on rival principles and the global reach of the struggle, and KC-6.2.V.B supplies the groups that opposed both orders and promoted alternatives. The key is the conjunction of those two sentences, and each distractor contradicts at least one of them."),
]
