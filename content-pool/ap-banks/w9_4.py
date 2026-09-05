# AP WORLD HISTORY: MODERN 9.4 Economics in the Global Age
# CED effective Fall 2026 (Course Framework V.1), Unit 9 Globalization,
# c. 1900 to the present. Thematic focus: Economics Systems (ECN).
# Reasoning process: Continuity and Change.
#
# Learning Objective: Unit 9 Learning Objective D -- explain the continuities and
# changes in the global economy from 1900 to present. Suggested skill 2.C,
# explain the significance of a source's point of view, purpose, historical
# situation, and/or audience, including how these might limit the use(s) of a
# source.
#
# DEDUPE NOTE, AND IT MATTERS MORE HERE THAN ANYWHERE ELSE IN THIS TERRITORY.
# Topic 8.4, Spread of Communism After 1900, is also an ECN topic and ALSO carries
# suggested skill 2.C. Two banks written the same way would be two banks of the
# same questions with the nouns changed. So the division is deliberate:
#   * 8.4 has the state DIRECTING an economy, land and resource redistribution,
#     and the Chinese case. Its items lean on 2.C in its narrow form -- what a
#     source cannot show, what limits its use, who its audience was.
#   * 9.4 has the state WITHDRAWING from direction, and the reasoning process the
#     CED prints beside it is continuity and change, so most items here ask what
#     altered and what persisted across the century. Where 2.C is used it is used
#     in its other half, the SIGNIFICANCE of a point of view: whose economy a
#     source speaks from, and what that position lets it see.
# Free-market liberalization, trade agreements and multinational corporations are
# this module's content and appear in 8.4 only as distractors; state direction of
# the economy is 8.4's and appears here only as the continuity against which the
# change is measured.
#
# HISTORICAL DEVELOPMENTS this topic prints, and the only sentences the keys
# below rest on:
#   KC-6.3.I.D   In a trend accelerated by the end of the Cold War, many
#                governments encouraged free-market economic policies and
#                promoted economic liberalization in the late 20th century.
#   KC-6.3.I.E   In the late 20th century, revolutions in information and
#                communications technology led to the growth of knowledge
#                economies in some regions, while industrial production and
#                manufacturing were increasingly situated in Asia and Latin
#                America.
#   KC-6.3.II.B  Changing economic institutions, multinational corporations, and
#                regional trade agreements reflected the spread of principles and
#                practices associated with free-market economics throughout the
#                world.
#
# THREE PIECES OF WORDING CARRY THE TOPIC, and each is a place a bank goes wrong:
#   * "In a trend ACCELERATED BY the end of the Cold War" -- the end of the Cold
#     War sped up a trend already running; it did not begin it. Items 6 and 19
#     hold that.
#   * "knowledge economies IN SOME REGIONS" -- not everywhere, and the survey in
#     item 13 exists to make that countable.
#   * "REFLECTED the spread of principles and practices" -- institutions,
#     corporations and trade agreements are described as reflecting the spread,
#     not as causing it. Items 9 and 24 hold that verb where the framework put
#     it.
#
# ILLUSTRATIVE EXAMPLES the CED prints on this page, in six lists:
#   Governments' increased encouragement of free-market policies: the United
#     States under Ronald Reagan; Britain under Margaret Thatcher; China under
#     Deng Xiaoping; Chile under Augusto Pinochet.
#   Knowledge economies: Finland; Japan; the U.S.
#   Asian production and manufacturing economies: Vietnam; Bangladesh.
#   Latin American production and manufacturing economies: Mexico; Honduras.
#   Economic institutions and regional trade agreements: the World Trade
#     Organization; NAFTA; ASEAN.
#   Multinational corporations: Nestle; Nissan; Mahindra and Mahindra.
# The CED spells the first corporation with an accented character; the notation
# gate bans non-ASCII, so it is written "Nestle" here. That is a transliteration
# of the CED's own spelling and not a different company.
# Illustrative examples are optional course content, so exactly TWO items turn on
# them and both stems say the course prints them as such.
#
# CONTESTED GROUND. Whether free-market policies were good for the countries
# that adopted them is a live political argument, and the CED's own illustrative
# list names four governments about which people disagree sharply. NO key here
# says those policies succeeded or failed, helped or harmed, or that any of the
# four governments was right or wrong. The framework says many governments
# encouraged such policies and that institutions and firms reflected their
# spread; that is what is keyed. Topic 9.5 covers the movements that protested
# the consequences of global integration and 9.7 the responses to globalization,
# so the objections have their own place in the course and are not smuggled in
# or out here.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT and none is attributed to a real person or document.
# TABLES are hypothetical, each states a whole and its parts, and every keyed
# conclusion is recomputed from the table alone. DATES are written "1980 to
# 2000", never with a hyphen.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("9.4", "Economics in the Global Age", 9)

_T_MANUFACTURING = dict(
    headers=["Period (hypothetical index of world manufacturing output, first period = 100)",
             "Total output",
             "Of that, produced in Asia and Latin America",
             "Of that, produced elsewhere"],
    rows=[["1970", "100", "22", "78"],
          ["1985", "165", "58", "107"],
          ["2000", "260", "130", "130"]])

_T_AGREEMENTS = dict(
    headers=["Decade (hypothetical record of trade agreements in force at the decade's end)",
             "Agreements in force",
             "Of those, joining states of more than one region",
             "Of those, joining states of a single region"],
    rows=[["1960s", "18", "4", "14"],
          ["1980s", "41", "12", "29"],
          ["2000s", "96", "38", "58"]])

_T_SECTORS = dict(
    headers=["Economy (hypothetical employment survey, thousands of workers)",
             "Workers recorded",
             "Of those, in information and communications services",
             "Of those, in other sectors"],
    rows=[["Economy one", "900", "315", "585"],
          ["Economy two", "1,200", "240", "960"],
          ["Economy three", "800", "96", "704"]])

QUESTIONS = [

 dict(q="A finance ministry's budget statement of 1987 announces the sale of state-owned firms to private buyers, the removal of price controls and the reduction of tariffs. According to this course, the statement belongs to which development?",
   choices=[
     "Governments encouraging free-market economic policies and promoting economic liberalization in the late twentieth century",
     "Governments taking a strong role in guiding economic life to promote development",
     "Governments redistributing land and resources within their own borders",
     "Governments controlling the national economy through state-directed campaigns",
     "Governments transferring economic planning to an international organization"],
   ans=0,
   why="KC-6.3.I.D states that in a trend accelerated by the end of the Cold War, many governments encouraged free-market economic policies and promoted economic liberalization in the late twentieth century. Selling state firms, ending price controls and cutting tariffs are that encouragement in a budget document, and each distractor describes the state doing more rather than less."),

 dict(q="A company report of 1994 explains that the firm designs its products in one country, has them assembled in a second and sells them in forty others. According to this course, a firm of this kind is one of the",
   choices=[
     "multinational corporations that reflected the spread of principles and practices associated with free-market economics",
     "state enterprises through which governments directed their national economies",
     "international organizations formed to maintain world peace and cooperation",
     "regional movements that challenged inherited imperial boundaries",
     "nationalist parties that sought independence from imperial rule"],
   ans=0,
   why="KC-6.3.II.B states that changing economic institutions, multinational corporations, and regional trade agreements reflected the spread of principles and practices associated with free-market economics throughout the world. A firm designing in one country, assembling in a second and selling in forty is that corporation as the framework describes it."),

 dict(q="A hypothetical index divides world manufacturing output into two parts in each period. Which conclusion does the table alone support?",
   table=_T_MANUFACTURING,
   choices=[
     "Total output rose in each period, and the share produced in Asia and Latin America rose with it",
     "Total output fell in each period after the first one recorded",
     "The share produced in Asia and Latin America fell across the record",
     "Output produced elsewhere fell in each period recorded",
     "Asia and Latin America produced more than half of the total in every period recorded"],
   ans=0,
   why="KC-6.3.I.E states that in the late twentieth century industrial production and manufacturing were increasingly situated in Asia and Latin America. A rising share of a rising total is what increasingly situated means when it is counted, and the index is hypothetical, with the key and the falsity of each distractor recomputed from the table alone in the verifier."),

 dict(q="According to this course, what did revolutions in information and communications technology lead to in the late twentieth century?",
   choices=[
     "The growth of knowledge economies in some regions",
     "The growth of knowledge economies in every region of the world",
     "The disappearance of industrial production from every region",
     "The end of trade between states in different regions",
     "The return of economic planning to state ministries everywhere"],
   ans=0,
   why="KC-6.3.I.E states that in the late twentieth century, revolutions in information and communications technology led to the growth of knowledge economies IN SOME REGIONS. The qualifier is the framework's own, and the same sentence pairs that growth with manufacturing moving to Asia and Latin America rather than with its disappearance."),

 dict(q="A trade minister's speech to an assembly of manufacturers in 1996 argues for joining a regional agreement, while a speech by the same minister to farmers the same month stresses what the agreement will protect. What is the significance of the two audiences for a historian reading both?",
   choices=[
     "Each speech selects the aspects of the agreement that matter to the audience in front of it, so the two together show more than either alone",
     "The speech to manufacturers must be the minister's real view because industry matters more",
     "The speech to farmers must be the minister's real view because farmers are more numerous",
     "The two speeches cancel each other out and neither can be used as evidence",
     "The existence of two speeches proves the agreement was never signed"],
   ans=0,
   why="Skill 2.C asks for the significance of a source's point of view, purpose, historical situation and audience. KC-6.3.II.B places regional trade agreements among the things that reflected the spread of free-market principles, and a minister arguing for one before two different audiences is selecting from the same case rather than holding two views, which is what the pair lets a historian see."),

 dict(q="This course describes the encouragement of free-market policies as a trend that stood in a particular relation to the end of the Cold War. What was that relation?",
   choices=[
     "The end of the Cold War accelerated a trend that was already under way",
     "The end of the Cold War began a trend that had not existed before it",
     "The end of the Cold War halted a trend that had been under way",
     "The trend ended the Cold War rather than being affected by it",
     "The framework states no relation between the trend and the end of the Cold War"],
   ans=0,
   why="KC-6.3.I.D states that IN A TREND ACCELERATED BY the end of the Cold War, many governments encouraged free-market economic policies. Accelerated presupposes something already moving, so the framework describes a change of pace rather than a beginning, and that distinction is what the key states."),

 dict(q="A hypothetical record divides the trade agreements in force at each decade's end into two groups. Which conclusion does the table alone support?",
   table=_T_AGREEMENTS,
   choices=[
     "The number in force rose in each decade, and agreements joining states of a single region outnumbered the rest in every decade",
     "The number in force fell in each decade after the first one recorded",
     "Agreements joining states of more than one region outnumbered single-region agreements in every decade",
     "No agreement in force at the end of the 1960s joined states of more than one region",
     "The three decades recorded the same number of agreements in force as one another"],
   ans=0,
   why="KC-6.3.II.B states that regional trade agreements reflected the spread of principles and practices associated with free-market economics throughout the world, and a rising count in which regional agreements predominate is that spread counted. The record is hypothetical and the key, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="An industrial survey of 1998 finds that a country which had exported raw materials for most of the century now exports finished goods assembled in its own factories, while a country that had been the world's leading manufacturer now earns more from services and software. Which of this course's statements does the pair illustrate?",
   choices=[
     "That manufacturing was increasingly situated in Asia and Latin America while knowledge economies grew in some regions",
     "That knowledge economies grew in Asia and Latin America while manufacturing moved elsewhere",
     "That manufacturing disappeared from every region during the late twentieth century",
     "That knowledge economies replaced manufacturing in every region simultaneously",
     "That neither manufacturing nor services changed their location during this period"],
   ans=0,
   why="KC-6.3.I.E states that revolutions in information and communications technology led to the growth of knowledge economies in some regions, WHILE industrial production and manufacturing were increasingly situated in Asia and Latin America. The framework puts the two movements in one sentence and in that pairing, so a distractor exchanging them is the error the item is built to catch."),

 dict(q="How does this course describe the relation between multinational corporations and the spread of free-market principles?",
   choices=[
     "The corporations reflected that spread rather than being named as its cause",
     "The corporations caused that spread and the framework names no other factor",
     "The corporations opposed that spread wherever they operated",
     "The corporations and the spread are treated as belonging to different centuries",
     "The framework states no relation between the corporations and the spread"],
   ans=0,
   why="KC-6.3.II.B states that changing economic institutions, multinational corporations, and regional trade agreements REFLECTED the spread of principles and practices associated with free-market economics throughout the world. Reflected is the framework's own verb and it is weaker than caused, so a key naming the corporations as the cause would go past the sentence."),

 dict(q="This course prints certain governments as illustrative examples of the increased encouragement of free-market policies. Which list is the one the course prints?",
   choices=[
     "The United States under Ronald Reagan, Britain under Margaret Thatcher, China under Deng Xiaoping, and Chile under Augusto Pinochet",
     "Egypt under Gamal Abdel Nasser, India under Indira Gandhi, Tanzania under Julius Nyerere, and Sri Lanka under Sirimavo Bandaranaike",
     "Finland, Japan, and the United States as knowledge economies",
     "The World Trade Organization, NAFTA, and ASEAN",
     "Nestle, Nissan, and Mahindra and Mahindra"],
   ans=0,
   why="The CED prints these four beside KC-6.3.I.D as illustrative examples of governments' increased encouragement of free-market policies. The second list is printed beside KC-6.3.I.C in Topic 8.6 for governments guiding economic life, and the others are this page's separate lists for knowledge economies, for institutions and trade agreements, and for multinational corporations. The item asks which list the course prints and nothing about whether the policies succeeded."),

 dict(q="An unattributed editorial published in 1991 argues that the political changes of the preceding two years have removed the main objection to opening its country's economy. Read within this course's framework, the editorial is an instance of",
   choices=[
     "the acceleration of the trend toward economic liberalization that followed the end of the Cold War",
     "the beginning of state direction of the economy in newly independent states",
     "the redistribution of land and resources within states in three world regions",
     "the growth of institutions of global association early in the century",
     "the dissolution of empires and the restructuring of states after World War II"],
   ans=0,
   why="KC-6.3.I.D states that in a trend accelerated by the end of the Cold War, many governments encouraged free-market economic policies and promoted economic liberalization in the late twentieth century. An editorial dating its argument to the political changes of the preceding two years is that acceleration argued from inside the moment."),

 dict(q="A garment manufacturer's prospectus of 1993 invites investment in factories it is opening in two Asian countries and one Central American country, and states that its buyers are in Europe and North America. Which of this course's statements does the prospectus illustrate?",
   choices=[
     "That industrial production and manufacturing were increasingly situated in Asia and Latin America",
     "That industrial production and manufacturing were increasingly situated in Europe and North America",
     "That knowledge economies grew in every region during the late twentieth century",
     "That governments took an increasing role in directing their national economies",
     "That regional trade agreements ceased to be made in the late twentieth century"],
   ans=0,
   why="KC-6.3.I.E states that in the late twentieth century industrial production and manufacturing were increasingly situated in Asia and Latin America. Factories opening in those regions to supply buyers elsewhere is that relocation described by the firm making it, and a distractor reverses the two ends of it."),

 dict(q="A hypothetical employment survey divides each economy's recorded workers into two groups. Which conclusion does the table alone support?",
   table=_T_SECTORS,
   choices=[
     "In no economy surveyed do information and communications services employ a majority, and the share differs between the three",
     "Information and communications services employ a majority in every economy surveyed",
     "No worker in economy three is recorded in information and communications services",
     "Economy three records more workers than economy two records",
     "The share employed in information and communications services is the same in all three economies"],
   ans=0,
   why="KC-6.3.I.E states that revolutions in information and communications technology led to the growth of knowledge economies IN SOME REGIONS, which is a claim about unevenness rather than about universality. A survey in which the share differs markedly and nowhere reaches a majority is that word some made countable, and the figures are hypothetical, with the key recomputed from the table alone in the verifier."),

 dict(q="Which pairing best states a continuity and a change in the global economy as this course presents the century?",
   choices=[
     "Manufacturing continued to be central to the world economy, while the places where it was carried on changed",
     "Manufacturing ceased entirely, while the places where it had been carried on stayed the same",
     "Governments continued to direct their economies, while free-market policies disappeared",
     "Trade between regions ceased, while economic institutions multiplied",
     "Neither the scale nor the location of manufacturing altered during the century"],
   ans=0,
   why="KC-6.3.I.E states that industrial production and manufacturing were increasingly situated in Asia and Latin America, which is a change of location within a continuing activity. Unit 9 Learning Objective D asks for the continuities AND changes in the global economy, and this pair is one of them stated in the framework's own terms."),

 dict(q="An unattributed pamphlet issued by a trade association in 1999 praises a new regional agreement, and a pamphlet issued the same year by a group of its members' employees criticizes it. What is the significance of the difference for a historian?",
   choices=[
     "The two speak from different positions within the same economy, and each shows what that position made visible",
     "The association's pamphlet is authoritative because associations represent whole industries",
     "The employees' pamphlet is authoritative because it comes from those most affected",
     "The disagreement shows that the agreement was never actually concluded",
     "Neither pamphlet can be used, because both were written by interested parties"],
   ans=0,
   why="Skill 2.C asks for the SIGNIFICANCE of a source's point of view and situation, which means asking what a position lets a source see rather than ranking positions for reliability. KC-6.3.II.B places regional trade agreements among the developments reflecting the spread of free-market principles, and both pamphlets are evidence about how that spread was experienced from different places inside it."),

 dict(q="Which statement about the global economy in the late twentieth century is NOT supported by this course?",
   choices=[
     "Knowledge economies grew at the same rate in every region of the world",
     "Many governments encouraged free-market economic policies in this period",
     "Industrial production was increasingly situated in Asia and Latin America",
     "Multinational corporations reflected the spread of free-market principles",
     "Regional trade agreements reflected the spread of free-market principles"],
   ans=0,
   why="KC-6.3.I.E states that revolutions in information and communications technology led to the growth of knowledge economies IN SOME REGIONS, so uniform growth everywhere is the claim the framework does not support. The item asks which statement is NOT supported, so the key is deliberately the false one; the other four restate KC-6.3.I.D, KC-6.3.I.E and KC-6.3.II.B."),

 dict(q="This course prints certain bodies as illustrative examples of economic institutions and regional trade agreements. Which list is the one the course prints?",
   choices=[
     "The World Trade Organization, NAFTA, and ASEAN",
     "Nestle, Nissan, and Mahindra and Mahindra",
     "Finland, Japan, and the United States",
     "Vietnam, Bangladesh, Mexico, and Honduras",
     "Greenpeace and the World Fair Trade Organization"],
   ans=0,
   why="The CED prints the World Trade Organization, NAFTA and ASEAN beside KC-6.3.II.B as illustrative examples of economic institutions and regional trade agreements. The other lists are this page's separate examples of multinational corporations, of knowledge economies, and of Asian and Latin American production economies, or belong to Topic 9.5."),

 dict(q="A historian argues that the economic changes of the late twentieth century were less a break with the past than a change of pace. Which of this course's statements would most directly support that reading?",
   choices=[
     "That the encouragement of free-market policies was a trend accelerated by the end of the Cold War",
     "That the encouragement of free-market policies began only after the end of the Cold War",
     "That governments abandoned all economic policy after the end of the Cold War",
     "That the end of the Cold War had no bearing on economic policy anywhere",
     "That free-market policies were confined to a single country in this period"],
   ans=0,
   why="KC-6.3.I.D states that in a trend ACCELERATED BY the end of the Cold War, many governments encouraged free-market economic policies and promoted economic liberalization. Acceleration is a change of pace in something already moving, which is exactly the historian's reading, and the reasoning process the CED prints beside this topic is continuity and change."),

 dict(q="An unattributed consultancy report of 1997 advises a government that its future lies in software and research rather than in heavy industry. According to this course, the report's advice reflects",
   choices=[
     "the growth of knowledge economies that followed revolutions in information and communications technology",
     "the movement of industrial production and manufacturing toward Asia and Latin America",
     "the strong role governments took in guiding economic life after independence",
     "the redistribution of land and resources within states",
     "the formation of international organizations to maintain world peace"],
   ans=0,
   why="KC-6.3.I.E states that in the late twentieth century, revolutions in information and communications technology led to the growth of knowledge economies in some regions. Advice to move from heavy industry into software and research is that growth recommended as policy, and it is the other half of the sentence from the relocation of manufacturing."),

 dict(q="Two documents describe the same privatization: a government prospectus offering shares to the public and a departmental minute recording the reserve price. What does the difference in purpose between them mean for their use?",
   choices=[
     "The prospectus is written to attract buyers and the minute to record a decision, so each supports different kinds of claim",
     "The prospectus is more reliable because it was published and the minute was not",
     "The minute is more reliable because it was internal and the prospectus was public",
     "The two documents contradict each other and neither can be used",
     "Both documents serve the same purpose and either may stand for the other"],
   ans=0,
   why="Skill 2.C asks for the significance of a source's purpose and audience, including how these might limit its uses. KC-6.3.I.D places privatization among the free-market policies many governments encouraged, and a prospectus and an internal minute about the same sale are produced for different ends, so each can establish something the other cannot."),

 dict(q="According to this course, where were industrial production and manufacturing increasingly situated in the late twentieth century?",
   choices=[
     "In Asia and Latin America",
     "In Europe and North America",
     "In Africa and Oceania",
     "In no region in particular, since the framework names none",
     "In the same regions in which they had been situated in 1900"],
   ans=0,
   why="KC-6.3.I.E states that in the late twentieth century industrial production and manufacturing were increasingly situated in Asia and Latin America. The framework names those two regions in that sentence, and the CED prints Vietnam and Bangladesh, and Mexico and Honduras, as its illustrative examples of them."),

 dict(q="A government's own account of 1989 presents its liberalization programme as a success in its first year. What does this course's suggested skill direct a student to notice about this source?",
   choices=[
     "That it is the programme's author reporting on its own work, which bears on what the account can establish",
     "That it was written in 1989, which places it outside the period the framework covers",
     "That it concerns economics, a subject on which sources are never preserved",
     "That it is a government account, which makes it the only admissible source",
     "That it describes one year, which makes it useless for any purpose"],
   ans=0,
   why="Skill 2.C asks for the significance of a source's point of view and purpose, including how these might limit its uses. KC-6.3.I.D places such programmes among the free-market policies many governments encouraged, and a government reporting on its own programme in its first year has both an interest and a very short run of evidence."),

 dict(q="Which of the following does this course treat as reflecting the spread of principles and practices associated with free-market economics?",
   choices=[
     "Changing economic institutions, multinational corporations, and regional trade agreements",
     "State-owned industries, national development plans, and land redistribution programmes",
     "Military alliances, nuclear proliferation, and proxy wars",
     "Vaccines, antibiotics, and modern methods of birth control",
     "Deforestation, desertification, and declining air quality"],
   ans=0,
   why="KC-6.3.II.B names exactly those three as reflecting the spread of principles and practices associated with free-market economics throughout the world. Each distractor lists developments the framework states in other sentences of this course, which is the cross-sentence error a list item is built to catch."),

 dict(q="A student writes that this course identifies multinational corporations as the cause of economic liberalization. What is the best correction?",
   choices=[
     "The framework says such corporations reflected the spread of free-market principles rather than naming them as its cause",
     "The framework says such corporations opposed the spread of free-market principles",
     "The framework does not mention multinational corporations at any point",
     "The framework says such corporations existed only before the twentieth century",
     "The framework says such corporations caused the end of the Cold War"],
   ans=0,
   why="KC-6.3.II.B states that changing economic institutions, multinational corporations, and regional trade agreements REFLECTED the spread of principles and practices associated with free-market economics. Reflected is the framework's own verb, and the correction has to restore it rather than substituting a different relation."),

 dict(q="A comparison is drawn between a newly independent government of the 1960s directing its economy through state industries and a government of the 1990s selling those industries to private buyers. What does this course's framework let a student say about the pair?",
   choices=[
     "The framework records both, the first as a strong state role after independence and the second as the later encouragement of free-market policies",
     "The framework records only the first and treats the second as never having occurred",
     "The framework records only the second and treats the first as never having occurred",
     "The framework treats the two as having occurred simultaneously in the same states",
     "The framework treats the two as unrelated to the global economy"],
   ans=0,
   why="KC-6.3.I.C in Topic 8.6 records that governments of newly independent states after World War II often took a strong role in guiding economic life, and KC-6.3.I.D here records that in a trend accelerated by the end of the Cold War many governments encouraged free-market policies in the late twentieth century. Unit 9 Learning Objective D asks for continuities and changes, and the pair is the framework's own sequence."),

 dict(q="An unattributed shipping agent's circular of 1995 notes that the goods it forwards now originate in different countries from those of twenty years earlier, though the ports receiving them are much the same. The circular records",
   choices=[
     "a change in where manufacturing was carried on alongside a continuity in where its products were sold",
     "a change in where products were sold alongside a continuity in where they were made",
     "a change in both where goods were made and where they were sold",
     "a continuity in both where goods were made and where they were sold",
     "the disappearance of long-distance trade in manufactured goods"],
   ans=0,
   why="KC-6.3.I.E states that industrial production and manufacturing were increasingly situated in Asia and Latin America in the late twentieth century, which is a change in the origin of goods rather than in their destination. The reasoning process the CED prints beside this topic is continuity and change, and the circular records one of each, so the key names both."),

 dict(q="A researcher wants to test the claim that a country's economy became a knowledge economy in the late twentieth century. Which evidence would bear most directly on the claim?",
   choices=[
     "The share of the country's workers and output in information and communications activities over those years",
     "The number of political parties contesting the country's elections",
     "The country's total land area and the length of its coastline",
     "The number of international conferences the country hosted",
     "The number of colonies the country had governed before 1945"],
   ans=0,
   why="KC-6.3.I.E states that revolutions in information and communications technology led to the growth of knowledge economies in some regions, so the share of workers and output in those activities is the direct measure. The other records bear on developments the framework treats in other topics."),

 dict(q="A history of the world economy argues that the century's most important economic story is one of things moving rather than of things stopping. Which pair of this course's statements best supports that reading?",
   choices=[
     "That manufacturing shifted toward Asia and Latin America, and that free-market principles and practices spread throughout the world",
     "That manufacturing ceased in every region, and that trade between regions came to an end",
     "That governments abandoned economic policy, and that corporations ceased to operate across borders",
     "That knowledge economies replaced every other kind, and that no manufacturing remained anywhere",
     "That economic institutions disappeared, and that regional trade agreements were never concluded"],
   ans=0,
   why="KC-6.3.I.E states that industrial production and manufacturing were increasingly situated in Asia and Latin America, and KC-6.3.II.B that changing economic institutions, multinational corporations, and regional trade agreements reflected the spread of free-market principles and practices throughout the world. Both are movements rather than cessations, which is the reading the historian proposes."),

 dict(q="Considered across this topic, what changed and what carried on in the global economy of the late twentieth century?",
   choices=[
     "The direction of economic policy in many governments changed and manufacturing moved, while production, trade and the search for markets carried on",
     "Every element of economic life changed and nothing at all carried on",
     "Nothing changed, and the economy of 1990 was that of 1900 in every respect",
     "Governments everywhere increased their direction of the economy and manufacturing stayed where it had been",
     "Trade between regions ended and each economy became self-sufficient"],
   ans=0,
   why="KC-6.3.I.D supplies the change in the direction of policy, KC-6.3.I.E the movement of manufacturing and the growth of knowledge economies in some regions, and KC-6.3.II.B the spread of free-market principles through institutions, corporations and trade agreements, all of which presuppose production and trade continuing. Unit 9 Learning Objective D asks for continuities and changes together."),

 dict(q="Taking the topic as a whole, which single sentence best states what this course says about the global economy from 1900 to the present?",
   choices=[
     "Many governments turned toward free-market policies in a trend the end of the Cold War accelerated, knowledge economies grew in some regions while manufacturing moved toward Asia and Latin America, and institutions, firms and trade agreements reflected free-market principles spreading through the world",
     "Governments everywhere increased their direction of the economy, manufacturing stayed where it had always been, and no principles spread anywhere",
     "The world economy ceased to exist as trade between regions ended in the late twentieth century",
     "Knowledge economies grew in every region at once and manufacturing disappeared from the world",
     "Economic policy was identical in every state throughout the century and nothing about it altered"],
   ans=0,
   why="KC-6.3.I.D supplies the turn toward free-market policies and the acceleration by the end of the Cold War, KC-6.3.I.E the knowledge economies in some regions and the relocation of manufacturing, and KC-6.3.II.B the institutions, corporations and trade agreements reflecting the spread. The key is the conjunction of the three with every qualifier intact, and each distractor contradicts at least one."),
]
