# AP WORLD HISTORY: MODERN 8.5 Decolonization After 1900
# CED effective Fall 2026 (Course Framework V.1), Unit 8 Cold War and
# Decolonization, c. 1900 to the present. Thematic focus: Governance (GOV).
# Reasoning process: Comparison.
#
# Learning Objective: Unit 8 Learning Objective F -- compare the processes by
# which various peoples pursued independence after 1900. Suggested skill 5.B,
# explain how a historical development or process relates to another historical
# development or process. Comparison is therefore the shape of this bank: most
# items set two cases, two aims or two routes beside each other and ask what the
# framework says the difference between them is.
#
# HISTORICAL DEVELOPMENTS this topic prints, and the only sentences the keys
# below rest on:
#   KC-6.2.II.A  Nationalist leaders and parties in Asia and Africa sought
#                varying degrees of autonomy within or independence from
#                imperial rule.
#   KC-6.2.I.C   After the end of World War II, some colonies negotiated their
#                independence, while others achieved independence through armed
#                struggle.
#   KC-6.2.II.B  Regional, religious, and ethnic movements challenged colonial
#                rule and inherited imperial boundaries. Some of these movements
#                advocated for autonomy.
#
# ILLUSTRATIVE EXAMPLES the CED prints on this page, in four lists:
#   Nationalist leaders and parties: Indian National Congress; Ho Chi Minh in
#     French Indochina (Vietnam); Kwame Nkrumah in British Gold Coast (Ghana);
#     Gamal Abdel Nasser in Egypt.
#   Negotiated independence: India from the British Empire; the Gold Coast from
#     the British Empire; French West Africa.
#   Independence through armed struggle: Algeria from the French empire; Angola
#     from the Portuguese empire; Vietnam from the French empire.
#   Regional, religious, and ethnic movements: Muslim League in British India;
#     Quebecois separatist movement in Canada; Biafra secessionist movement in
#     Nigeria.
# Illustrative examples are optional course content, so exactly TWO items turn
# on them and both stems say that the course prints them as such. The CED
# spells the Canadian movement with accented characters; the notation gate bans
# non-ASCII, so it is written "Quebecois" here. That is a transliteration of the
# CED's own spelling and not a different movement.
#
# THE WORD "VARYING" IS LOAD-BEARING, and it is the error this topic invites.
# KC-6.2.II.A says nationalist leaders and parties sought VARYING DEGREES of
# autonomy within OR independence from imperial rule. A bank that keyed every
# nationalist party as demanding outright independence from the start would
# teach the opposite of the framework's own sentence, in a topic whose title
# makes that reading tempting. Items 1, 5, 11, 17 and 21 hold the range open.
# KC-6.2.I.C's "some ... while others" does the same work for the two routes,
# and KC-6.2.II.B's "some of these movements" for the third statement.
#
# WHAT IS DELIBERATELY NOT KEYED. The framework says some colonies negotiated
# independence and others achieved it through armed struggle. It does not say
# which route was more common, which was quicker, or which produced better
# outcomes, and no key here supplies any of those. Nor does any key assign
# rightness to an imperial power or to a movement; the two data questions that
# count cases are labelled hypothetical in their stems for exactly that reason.
#
# DEDUPE NOTE. Topic 8.6 takes up what newly independent states then did, and
# the redrawing of boundaries into new states belongs there; this module stays
# on the PROCESSES by which independence was pursued. Topic 8.7 takes up
# nonviolence and violence as reactions to power structures in general, so
# armed struggle appears here only as one of the two routes KC-6.2.I.C names,
# never as a general claim about political violence.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT and none is attributed to a real person or document.
# Each is an explicitly illustrative, unattributed source, and every key turns on
# reasoning from the source to a CED sentence rather than on recognising an
# author. TABLES are hypothetical and every keyed conclusion is recomputed from
# the table alone. DATES are written "1945 to 1960", never with a hyphen; the
# CED states that events and processes are not constrained by its given dates,
# so no key here depends on a boundary year.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("8.5", "Decolonization After 1900", 8)

# EACH TABLE STATES A WHOLE AND ITS TWO PARTS, and that is deliberate. A table
# giving only the two parts can be checked for "both are present", but the
# corruption used by the negative control only ever makes a number LARGER, so a
# check of that shape can never fail and proves nothing about the table it
# claims to read. Giving the total as well lets the verifier recompute that the
# parts sum to the whole, which every cell participates in. The first draft of
# this module caught 1 of 12 corrupted cells in the second table; it now catches
# all of them.
_T_DEGREES = dict(
    headers=["Region (hypothetical survey of nationalist party programmes)",
             "Programmes surveyed",
             "Of those, seeking greater autonomy within imperial rule",
             "Of those, seeking full independence from imperial rule"],
    rows=[["Asia", "45", "18", "27"],
          ["Africa", "47", "21", "26"]])

_T_PATHS = dict(
    headers=["Decade (hypothetical record)",
             "Colonies becoming independent",
             "Of those, independence negotiated",
             "Of those, independence following armed struggle"],
    rows=[["1940s", "7", "5", "2"],
          ["1950s", "13", "9", "4"],
          ["1960s", "27", "21", "6"],
          ["1970s", "11", "6", "5"]])

_T_MOVEMENTS = dict(
    headers=["Movement type (hypothetical survey, 1900 to 1990)",
             "Movements recorded",
             "Of those, stated aim was autonomy",
             "Of those, stated aim was a separate state"],
    rows=[["Regional", "16", "7", "9"],
          ["Religious", "11", "5", "6"],
          ["Ethnic", "14", "6", "8"]])

QUESTIONS = [

 dict(q="Two party programmes circulate in the same Asian colony in 1932. The first asks that the colony's legislature be given an elected majority while the colony remains part of the empire. The second asks that the colony leave the empire altogether. The pair is best used as evidence for which course development?",
   choices=[
     "Nationalist parties sought varying degrees of autonomy within, or independence from, imperial rule",
     "Nationalist parties across Asia and Africa converged on a single identical demand",
     "Nationalist parties appeared in Africa but not in Asia during this period",
     "Nationalist demands of every kind were abandoned in the decades before 1945",
     "Imperial rule in Asia went unchallenged by organized parties before World War II"],
   ans=0,
   why="KC-6.2.II.A states that nationalist leaders and parties in Asia and Africa sought varying degrees of autonomy within or independence from imperial rule. Two programmes in one colony asking for different amounts of self-rule are that range of degrees visible in a single place, which is what the word varying names."),

 dict(q="Two accounts describe the end of imperial rule in two different territories in the years after 1945. The first records a series of conferences, a published timetable and a transfer ceremony. The second records several years of fighting between an armed movement and the imperial army before the imperial government withdrew. Together the two accounts illustrate which statement from this course?",
   choices=[
     "Some colonies negotiated their independence, while others achieved independence through armed struggle",
     "Some colonies achieved independence through armed struggle, while no colony ever negotiated its independence",
     "Every colony that became independent after 1945 did so by negotiation with the imperial power",
     "Every colony that became independent after 1945 did so through a war of independence",
     "No territory became independent of an imperial power in the decades after 1945"],
   ans=0,
   why="KC-6.2.I.C states that after the end of World War II, some colonies negotiated their independence, while others achieved independence through armed struggle. The framework asserts that both routes occurred, so the key has to carry both halves; each distractor collapses the pair into a single route or denies the outcome altogether."),

 dict(q="A manifesto issued in 1965 by a movement inside a state that had become independent five years earlier argues that the state's frontiers were drawn in a European capital and cut through the territory of the people the movement speaks for. The manifesto is best understood as an example of",
   choices=[
     "a movement challenging the imperial boundaries a new state had inherited",
     "a movement demanding the restoration of direct imperial administration",
     "a movement seeking to enlarge the empire that had drawn the frontiers",
     "a movement organized by the imperial power to prevent independence",
     "a movement concerned only with the price of agricultural exports"],
   ans=0,
   why="KC-6.2.II.B states that regional, religious, and ethnic movements challenged colonial rule and inherited imperial boundaries. A frontier drawn by a departed empire and still in force after independence is precisely an inherited imperial boundary, and challenging it is the second of the two targets the framework names."),

 dict(q="A hypothetical survey places each nationalist party programme it records under exactly one of two stated aims. Which conclusion does the table alone support?",
   table=_T_DEGREES,
   choices=[
     "In each region surveyed, some programmes sought autonomy within imperial rule and others sought full independence",
     "In each region surveyed, every programme recorded sought full independence from imperial rule",
     "No programme recorded in Africa sought greater autonomy within imperial rule",
     "Africa recorded more programmes seeking full independence than Asia recorded",
     "The two regions surveyed the same number of programmes as one another"],
   ans=0,
   why="KC-6.2.II.A states that nationalist leaders and parties in Asia and Africa sought varying degrees of autonomy within or independence from imperial rule. A survey in which both aims appear in both regions is that variation made countable. The figures are hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="A colonial administrator's memorandum of 1955 divides the colony's politicians into those who want a larger share in the government of the colony and those who want the colony out of the empire. The distinction the memorandum draws corresponds most closely to",
   choices=[
     "the varying degrees of autonomy within, or independence from, imperial rule that nationalist parties sought",
     "the difference between negotiated independence and independence through armed struggle",
     "the difference between regional movements and religious movements",
     "the difference between an imperial metropole and its overseas possessions",
     "the difference between a military alliance and a trade agreement"],
   ans=0,
   why="KC-6.2.II.A distinguishes autonomy WITHIN imperial rule from independence FROM it and says nationalist parties sought varying degrees along that range, which is the distinction the memorandum reports. KC-6.2.I.C's distinction between negotiated and armed routes concerns how independence was reached, not how much self-rule was asked for."),

 dict(q="This course prints certain cases as illustrative examples of the two processes by which colonies became independent after World War II. Which pairing matches an example to the process it illustrates as the course prints them?",
   choices=[
     "India from the British Empire illustrates negotiated independence, and Algeria from the French empire illustrates independence through armed struggle",
     "India from the British Empire illustrates independence through armed struggle, and Algeria from the French empire illustrates negotiated independence",
     "Angola from the Portuguese empire and French West Africa both illustrate negotiated independence",
     "The Gold Coast from the British Empire and Vietnam from the French empire both illustrate independence through armed struggle",
     "Ho Chi Minh and Kwame Nkrumah are printed as illustrative examples of redrawn political boundaries"],
   ans=0,
   why="The CED prints India from the British Empire, the Gold Coast from the British Empire and French West Africa as illustrative examples of negotiated independence, and Algeria from the French empire, Angola from the Portuguese empire and Vietnam from the French empire as illustrative examples of independence through armed struggle, all beside KC-6.2.I.C. The exchanged pairing is the tempting error, so the key names each case together with its own process."),

 dict(q="A hypothetical petition submitted in 1953 by a regional association asks that its district be given a self-governing assembly within the colony rather than be separated from it. According to this course, such a movement",
   choices=[
     "is one of the regional movements that advocated for autonomy rather than a separate state",
     "cannot be counted as a movement at all, because it did not demand separation",
     "must be classified as a nationalist party seeking independence for the whole colony",
     "shows that regional movements never challenged colonial rule in any form",
     "shows that colonial administrations had already granted self-government everywhere"],
   ans=0,
   why="KC-6.2.II.B states that regional, religious, and ethnic movements challenged colonial rule and inherited imperial boundaries, and that some of these movements advocated for autonomy. The word some makes autonomy one of the aims such movements held rather than a disqualification from the category."),

 dict(q="A nationalist party founded in 1919 asked in its first programme for elected representation inside the colonial system. Its 1947 programme demands complete independence and nothing less. The change between the two programmes is best described as",
   choices=[
     "a movement along the range of degrees, from autonomy within imperial rule to independence from it",
     "a movement from independence from imperial rule back toward autonomy within it",
     "a change of subject from imperial politics to the regulation of trade",
     "evidence that the party had been dissolved and replaced by an unrelated organization",
     "evidence that the party had abandoned political aims in favour of cultural ones"],
   ans=0,
   why="KC-6.2.II.A places autonomy within imperial rule and independence from imperial rule at two ends of a range of varying degrees that nationalist parties sought. The two programmes are the same party at two points on that range, and the direction matters, so the key names the starting point and the end point rather than the pair alone."),

 dict(q="A hypothetical record places each colony's independence under exactly one of the two processes that produced it. Which conclusion does the table alone support?",
   table=_T_PATHS,
   choices=[
     "Both processes are recorded in every decade the table covers",
     "In at least one decade, more independences followed armed struggle than were negotiated",
     "Negotiated independence ceased to be recorded after the 1950s",
     "The decade recording the most negotiated independences also recorded the fewest following armed struggle",
     "The four decades together record more independences following armed struggle than negotiated ones"],
   ans=0,
   why="KC-6.2.I.C states that some colonies negotiated their independence while others achieved independence through armed struggle, which is an assertion that both processes occurred rather than a claim about which was more frequent. The figures are hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="An imperial government's published statement of 1946 announces a constitutional conference with a colony's elected leaders and a date by which power will pass to them. The process the statement describes is the one this course calls",
   choices=[
     "negotiated independence, as distinct from independence achieved through armed struggle",
     "independence achieved through armed struggle, as distinct from negotiated independence",
     "the redrawing of political boundaries by an international organization",
     "the migration of former colonial subjects to the imperial metropole",
     "the strong role newly independent governments took in guiding economic life"],
   ans=0,
   why="KC-6.2.I.C names two processes after the end of World War II, colonies that negotiated their independence and colonies that achieved independence through armed struggle. A conference with elected leaders and an announced transfer date is the first of those, so the key names it together with the process it is distinct from, because the reversed reading is the error the item is built to catch."),

 dict(q="A student writes that nationalist parties in Asia and Africa all demanded complete independence from the moment they were founded. What is the best correction?",
   choices=[
     "The framework says such parties sought varying degrees of autonomy within or independence from imperial rule, so some asked for less than independence",
     "The framework says such parties never asked for independence from imperial rule at all",
     "The framework says such parties existed only in Asia and never in Africa",
     "The framework says such parties were organized by the imperial governments themselves",
     "The framework says such parties confined themselves to religious questions"],
   ans=0,
   why="KC-6.2.II.A states that nationalist leaders and parties in Asia and Africa sought varying degrees of autonomy within or independence from imperial rule. Varying degrees rules out the claim that every party demanded the maximum, and it equally rules out the opposite absolute, so the correction has to preserve the range rather than replace one absolute with another."),

 dict(q="A hypothetical survey groups movements by type and places each under exactly one of two stated aims. Which conclusion does the table alone support?",
   table=_T_MOVEMENTS,
   choices=[
     "In every type recorded, some movements sought autonomy and others sought a separate state",
     "In every type recorded, every movement sought autonomy rather than a separate state",
     "No religious movement in the survey stated autonomy as its aim",
     "Regional movements are the only type in which a majority stated autonomy as the aim",
     "The three types recorded the same number of movements as one another"],
   ans=0,
   why="KC-6.2.II.B states that regional, religious, and ethnic movements challenged colonial rule and inherited imperial boundaries, and that SOME of these movements advocated for autonomy. A survey in which autonomy is one aim among others in every type is that word some made countable, and the figures are hypothetical, with the key recomputed from the table alone in the verifier."),

 dict(q="An ethnic association campaigned against the colonial administration in 1950 and, after independence, campaigned in 1968 against the successor state's refusal to redraw a frontier the empire had fixed. The two campaigns together show that such movements",
   choices=[
     "challenged colonial rule and also challenged the imperial boundaries that independent states inherited",
     "challenged colonial rule but dissolved as soon as the imperial power withdrew",
     "arose only after independence and never during the colonial period",
     "were concerned with imperial boundaries but never with colonial rule itself",
     "were created by the successor state to justify its existing frontiers"],
   ans=0,
   why="KC-6.2.II.B states that regional, religious, and ethnic movements challenged colonial rule and inherited imperial boundaries, naming both targets in one sentence. The association's two campaigns are the two targets in sequence, so the key carries both rather than either alone."),

 dict(q="Where does this course locate the nationalist leaders and parties that sought autonomy or independence from imperial rule?",
   choices=[
     "In Asia and in Africa",
     "In Asia only, with none recorded in Africa",
     "In Africa only, with none recorded in Asia",
     "In Europe and North America only",
     "In no particular region, since the framework names none"],
   ans=0,
   why="KC-6.2.II.A states that nationalist leaders and parties in Asia and Africa sought varying degrees of autonomy within or independence from imperial rule. The framework names both regions in that sentence, and a key naming one of the two would drop half of what it asserts."),

 dict(q="A communique issued in 1957 by an anti-colonial front reports that its units have been fighting the imperial army for three years and will continue until the imperial government leaves. The process this source describes is",
   choices=[
     "independence achieved through armed struggle, one of the two routes the course names",
     "negotiated independence, the other of the two routes the course names",
     "the granting of autonomy within imperial rule by constitutional reform",
     "the formation of an international organization to supervise a transfer of power",
     "the migration of colonial subjects toward the imperial capital"],
   ans=0,
   why="KC-6.2.I.C states that after the end of World War II some colonies negotiated their independence while others achieved independence through armed struggle. A front reporting years of fighting until the imperial government withdraws describes the second route, and the key names which of the two it is so that the reversed reading cannot match."),

 dict(q="In a hypothetical case, a religious association in a colony petitions in 1948 for a separate political unit in which its community would govern itself. This course would classify the association among",
   choices=[
     "the regional, religious, and ethnic movements that challenged colonial rule and inherited imperial boundaries",
     "the nationalist parties that spoke for the colony as a single undivided people",
     "the international organizations formed to maintain world peace",
     "the imperial administrations that governed colonies before independence",
     "the multinational corporations that spread free-market practices"],
   ans=0,
   why="KC-6.2.II.B names regional, religious, and ethnic movements as a category of their own, distinct from the nationalist parties of KC-6.2.II.A, and says they challenged colonial rule and inherited imperial boundaries. A community asking for a political unit of its own inside a colony is that category rather than a party speaking for the whole colony."),

 dict(q="Which statement about the pursuit of independence after 1900 is NOT supported by this course?",
   choices=[
     "Every colony that became independent after World War II reached that outcome by the same process",
     "Some colonies negotiated their independence after the end of World War II",
     "Some colonies achieved independence through armed struggle after the end of World War II",
     "Nationalist parties in Asia and Africa sought varying degrees of autonomy or independence",
     "Regional, religious, and ethnic movements challenged colonial rule"],
   ans=0,
   why="KC-6.2.I.C states that after the end of World War II some colonies negotiated their independence while others achieved independence through armed struggle, which is an assertion that the processes differed. A single common process is therefore the statement the framework does not support; the other four restate KC-6.2.I.C, KC-6.2.II.A and KC-6.2.II.B."),

 dict(q="This topic's learning objective asks students to compare something. What is it?",
   choices=[
     "The processes by which various peoples pursued independence after 1900",
     "The military capabilities of the two Cold War superpowers",
     "The economic policies of newly independent governments",
     "The causes of the collapse of the Soviet Union",
     "The forms taken by responses to cultural globalization"],
   ans=0,
   why="Unit 8 Learning Objective F is to compare the processes by which various peoples pursued independence after 1900, and the reasoning process printed beside this topic is comparison. The other options name the learning objectives of other topics in this course rather than this one."),

 dict(q="A 1938 party congress resolution offers to accept a status inside the empire carrying its own parliament and control of internal affairs, provided the status is granted within five years. According to this course, the resolution is best described as",
   choices=[
     "a nationalist demand for a degree of autonomy within imperial rule rather than for independence from it",
     "a nationalist demand for full independence from imperial rule expressed in indirect language",
     "a rejection of nationalism in favour of continued direct imperial administration",
     "a demand that the empire enlarge itself by acquiring further territories",
     "a proposal that a foreign power replace the existing imperial administration"],
   ans=0,
   why="KC-6.2.II.A says nationalist leaders and parties sought varying degrees of autonomy WITHIN or independence FROM imperial rule, so a demand for internal self-government inside the empire is one of the degrees the sentence covers. Reading it as a disguised demand for independence would erase the distinction the framework's own wording draws."),

 dict(q="A colonial-era party newspaper and the party's post-independence official history describe the same transfer of power, the first as a concession extracted from a weakened empire and the second as a victory won by the party. What does this course's framework let a historian conclude from the disagreement?",
   choices=[
     "Both descriptions concern the same process by which independence was pursued, and each reflects the position of the moment in which it was written",
     "One of the two accounts must be a fabrication, since a transfer of power has only one description",
     "The disagreement shows that no transfer of power took place in that territory",
     "The later account is automatically more reliable, because it was written with hindsight",
     "The earlier account is automatically more reliable, because it was written at the time"],
   ans=0,
   why="Unit 8 Learning Objective F asks for a comparison of the processes by which peoples pursued independence, and KC-6.2.I.C establishes that those processes differed from case to case. Two accounts of one process written in different situations can both report it while framing it differently, which is what skill 5.B's relating of one development to another requires a student to hold."),

 dict(q="Two colonies became independent in the same year. In the first, an elected assembly and the imperial government agreed a constitution over three years of talks. In the second, an armed movement fought the imperial army for eight years before the imperial government withdrew. Which comparison does this course support?",
   choices=[
     "The outcome was the same in both cases, while the process by which it was reached differed",
     "The process was the same in both cases, while the outcome differed",
     "Neither case counts as independence, because the framework recognizes only one route",
     "The first case is independence and the second is a civil war unrelated to imperial rule",
     "The two cases cannot be compared, because comparison requires identical processes"],
   ans=0,
   why="KC-6.2.I.C states that after the end of World War II some colonies negotiated their independence while others achieved independence through armed struggle, which places a common outcome at the end of two different processes. Unit 8 Learning Objective F asks for exactly that comparison, so the key separates the shared outcome from the differing process."),

 dict(q="An imperial government's file note of 1950 predicts that granting an elected majority to a colonial legislature will satisfy the colony's politicians permanently. A historian using this course's framework would most reasonably respond that",
   choices=[
     "nationalist parties sought varying degrees, so an elected majority might satisfy some of them and not others",
     "nationalist parties all sought identical terms, so the concession would satisfy all of them or none",
     "nationalist parties had no stated aims that a concession could be measured against",
     "no colonial legislature anywhere was ever given an elected majority",
     "the concession would be irrelevant, since imperial rule ended everywhere in 1950"],
   ans=0,
   why="KC-6.2.II.A states that nationalist leaders and parties sought varying degrees of autonomy within or independence from imperial rule. Where the aims vary, a single concession sits at one point on the range and cannot by itself meet the demands sitting further along it, which is what makes the file note's prediction a claim the framework does not support."),

 dict(q="This course prints certain leaders and organizations as illustrative examples of the nationalist leaders and parties described in this topic. Which list is the one the course prints?",
   choices=[
     "The Indian National Congress, Ho Chi Minh in French Indochina, Kwame Nkrumah in the British Gold Coast, and Gamal Abdel Nasser in Egypt",
     "The Muslim League in British India, the Quebecois separatist movement in Canada, and the Biafra secessionist movement in Nigeria",
     "Israel, Cambodia, and Pakistan as states created by the redrawing of political boundaries",
     "The United States under Ronald Reagan, Britain under Margaret Thatcher, and China under Deng Xiaoping",
     "The Korean War, the Angolan Civil War, and the Sandinista and Contras conflict in Nicaragua"],
   ans=0,
   why="The CED prints these four beside KC-6.2.II.A as illustrative examples of nationalist leaders and parties. The second list is the illustrative examples the same page prints for the regional, religious, and ethnic movements of KC-6.2.II.B, and the remaining lists are printed beside statements in other topics, on redrawn boundaries, on free-market policies and on proxy wars."),

 dict(q="Which statement about regional, religious, and ethnic movements is NOT supported by this course?",
   choices=[
     "Such movements challenged colonial rule but never questioned the boundaries independent states inherited",
     "Such movements mounted challenges to colonial rule",
     "Such movements contested the imperial boundaries that were inherited",
     "Some such movements advocated for autonomy",
     "Such movements are described as regional, religious, and ethnic in character"],
   ans=0,
   why="KC-6.2.II.B states that regional, religious, and ethnic movements challenged colonial rule AND inherited imperial boundaries, so a statement that they never questioned inherited boundaries strikes out half of the framework's sentence. The other four restate parts of that same sentence."),

 dict(q="A researcher wants to compare how two peoples pursued independence after 1900. Which pair of features would make the comparison most relevant to this topic?",
   choices=[
     "The degree of self-rule each movement demanded, and the process by which independence was eventually reached",
     "The average rainfall of the two territories, and the crops each exported",
     "The names of the two imperial capitals, and the distance between them",
     "The number of pages in each movement's founding document, and the paper it was printed on",
     "The current populations of the two territories, and their present-day currencies"],
   ans=0,
   why="KC-6.2.II.A supplies the first feature, the varying degrees of autonomy or independence that nationalist leaders and parties sought, and KC-6.2.I.C supplies the second, the difference between negotiated independence and independence through armed struggle. Unit 8 Learning Objective F asks for a comparison of processes, which is what those two features between them describe."),

 dict(q="Which relationship between the developments in this topic does the framework support?",
   choices=[
     "Nationalist parties pressed varying demands on imperial rule, and independence when it came was reached through negotiation in some cases and armed struggle in others",
     "Nationalist parties pressed identical demands, and independence was reached the same way everywhere",
     "Independence was reached before any nationalist parties had formed anywhere",
     "Nationalist parties formed only after independence had already been achieved",
     "Nationalist parties and independence movements are described by the framework as unrelated to one another"],
   ans=0,
   why="KC-6.2.II.A describes the varying demands nationalist leaders and parties made of imperial rule, and KC-6.2.I.C describes the two processes by which independence was reached after the end of World War II. Skill 5.B asks how one development relates to another, and the key states the two together in the order the framework sets them."),

 dict(q="An unattributed pamphlet published in a colony in 1954 argues that its people should press for independence at once rather than accept the stages of self-government the imperial government has proposed. The disagreement the pamphlet joins is best described as one about",
   choices=[
     "how much self-rule to demand and how quickly, within the range the course describes",
     "whether the colony had ever been governed by an imperial power at all",
     "which foreign state should replace the current imperial administration",
     "whether the imperial power should acquire additional colonies elsewhere",
     "which international organization should administer the colony permanently"],
   ans=0,
   why="KC-6.2.II.A states that nationalist leaders and parties sought varying degrees of autonomy within or independence from imperial rule, which is a range along which a demand for immediate independence and a staged transfer sit at different points. The pamphlet takes a position on that range rather than disputing whether imperial rule existed."),

 dict(q="A newly independent state's first census, taken in 1962, records several communities whose leaders had petitioned before independence for frontiers different from the ones the state now has. Those petitions are best related to which course statement?",
   choices=[
     "Regional, religious, and ethnic movements challenged colonial rule and inherited imperial boundaries",
     "Nationalist leaders and parties in Asia and Africa sought varying degrees of autonomy from imperial rule",
     "Some colonies negotiated their independence while others fought for it",
     "Governments of newly independent states took a strong role in guiding economic life",
     "New international organizations formed with the goal of maintaining world peace"],
   ans=0,
   why="KC-6.2.II.B states that regional, religious, and ethnic movements challenged colonial rule and inherited imperial boundaries, which is what a petition for frontiers other than the ones an empire drew amounts to. KC-6.2.II.A concerns the degree of self-rule a nationalist party sought for a whole colony rather than where its borders should lie."),

 dict(q="Considered across the cases this topic covers, what varied most between one people's pursuit of independence and another's?",
   choices=[
     "The degree of self-rule demanded and the process by which independence was reached",
     "Whether the territory concerned had ever been under imperial rule",
     "Whether the imperial power was located in another part of the world",
     "Whether independence, once reached, produced a sovereign state",
     "Whether any organized political movement existed in the territory"],
   ans=0,
   why="KC-6.2.II.A records varying degrees of autonomy or independence sought, and KC-6.2.I.C records negotiated independence alongside independence through armed struggle, so the framework's own two axes of variation are the demand and the process. It does not describe variation in whether the territories were under imperial rule or whether independence produced a state."),

 dict(q="Taking the topic as a whole, which single sentence best states what this course says about decolonization after 1900?",
   choices=[
     "Nationalist leaders and parties in Asia and Africa asked for varying amounts of self-rule, independence after 1945 came by negotiation in some places and by armed struggle in others, and regional, religious and ethnic movements contested both colonial rule and the frontiers empires left behind",
     "Every colony followed one identical path to independence, demanded by one identical kind of movement, and no frontier was ever disputed afterward",
     "Imperial rule in Asia and Africa was unchallenged until it ended by agreement among the imperial powers themselves",
     "Independence movements existed only in Europe, and the empires of the twentieth century were never contested in the territories they governed",
     "Decolonization consisted entirely of the redrawing of frontiers and involved no political movements of any kind"],
   ans=0,
   why="KC-6.2.II.A supplies the varying degrees of autonomy or independence sought in Asia and Africa, KC-6.2.I.C the two processes after the end of World War II, and KC-6.2.II.B the regional, religious, and ethnic movements challenging colonial rule and inherited imperial boundaries. The key is the conjunction of those three sentences and each distractor contradicts at least one of them."),
]
