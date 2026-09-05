# AP WORLD HISTORY: MODERN 8.1 Setting the Stage for the Cold War and Decolonization
# CED effective Fall 2026 (Course Framework V.1), Unit 8 Cold War and
# Decolonization, c. 1900 to the present.
#
# Learning Objective: Unit 8 Learning Objective A -- explain the historical
# context of the Cold War after 1945. Suggested skill 4.B, explain how a
# specific historical development or process is situated within a broader
# historical context.
#
# HISTORICAL DEVELOPMENTS this topic prints, and the only sentences the keys
# below rest on:
#   KC-6.2.II       Hopes for greater self-government were largely unfulfilled
#                   following World War I; however, in the years following World
#                   War II, increasing anti-imperialist sentiment contributed to
#                   the dissolution of empires and the restructuring of states.
#   KC-6.2.IV.C.i   Technological and economic gains experienced during World
#                   War II by the victorious nations shifted the global balance
#                   of power.
# Two further sentences are quoted from the adjacent topic pages ONLY where a
# question needs to name what the shifting balance turned into, because this
# topic is the context for them:
#   KC-6.2.IV.C.ii  The global balance of economic and political power shifted
#                   during and after World War II and rapidly evolved into the
#                   Cold War. The democracy of the United States and the
#                   authoritarian communist Soviet Union emerged as superpowers,
#                   which led to ideological conflict and a power struggle
#                   between capitalism and communism across the globe.
#
# SOURCES. AP World History Section I is stimulus-based and this bank cannot
# display an image, so every stimulus here is TEXT. No quotation is attributed
# to a real person or document: each is an explicitly illustrative, unattributed
# source of the period ("a pamphlet circulated in a West African colony in
# 1947"), and every key turns on reasoning from the source to a CED sentence
# rather than on recognising who wrote it. Fabricating a speech by a named
# twentieth-century figure would be read by a student as fact.
#
# TABLES. Every figure in a table= here is labelled HYPOTHETICAL in the stem and
# every keyed conclusion is recoverable from the table alone, recomputed in
# verify_w8_1.py. Nothing asks a student to remember a number.
#
# DATES. Spans are written "1939 to 1945", never with a hyphen. The CED states
# that "events, processes, and developments are not constrained by the given
# dates and may begin before, or continue after, the period", so no key here
# depends on a boundary year.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("8.1", "Setting the Stage for the Cold War and Decolonization", 8)

_T_OUTPUT = dict(
    headers=["State (hypothetical)",
             "Share of world manufacturing output, 1938 (percent)",
             "Share of world manufacturing output, 1948 (percent)"],
    rows=[["State W", "32", "48"],
          ["State X", "10", "12"],
          ["State Y", "14", "5"],
          ["State Z", "9", "4"]])

_T_MEMBERS = dict(
    headers=["Year (hypothetical record)", "Sovereign states holding membership"],
    rows=[["1945", "51"],
          ["1955", "76"],
          ["1965", "117"],
          ["1975", "144"]])

_T_TROOPS = dict(
    headers=["Imperial power (hypothetical)",
             "Colonial subjects serving in its armed forces, 1939 to 1945 (thousands)",
             "Colonies still administered by it in 1960"],
    rows=[["Power P", "2,500", "3"],
          ["Power Q", "1,100", "7"],
          ["Power R", "400", "11"]])

QUESTIONS = [

 dict(q="In a hypothetical case, a nationalist association in an Asian colony submitted a petition to the imperial capital in 1919 asking for a fixed timetable toward self-government. In 1946 the same association published a statement recalling that no such timetable had ever been granted. Taken together, the two documents are best used as evidence for which broader development?",
   choices=[
     "Hopes for greater self-government were largely unfulfilled in the years following World War I",
     "Imperial powers granted self-government to most of their Asian possessions in the years following World War I",
     "Anti-imperialist sentiment disappeared from colonial societies during the interwar decades",
     "Imperial governments abolished nationalist associations throughout Asia after World War I",
     "Self-government was extended to African colonies first and to Asian colonies only much later"],
   ans=0,
   why="KC-6.2.II states that hopes for greater self-government were largely unfulfilled following World War I. The pair of documents brackets exactly that gap between a demand made in 1919 and an outcome still absent in 1946, and nothing in the pair shows self-government actually being granted."),

 dict(q="A pamphlet circulated in a West African colony in 1947 argues that the recent world war drained the imperial treasury, exposed the limits of the imperial army, and obliged the empire to promise freedom to peoples abroad while withholding it from its own subjects. The pamphlet is best read as an expression of",
   choices=[
     "the increasing anti-imperialist sentiment that followed World War II and contributed to the dissolution of empires",
     "the largely unfulfilled hopes for self-government that followed World War I",
     "the movement of industrial production and manufacturing toward Asia and Latin America late in the twentieth century",
     "the formation of new military alliances binding European states to one or another superpower",
     "the encouragement of free-market economic policies by governments after the Cold War"],
   ans=0,
   why="KC-6.2.II states that in the years following World War II increasing anti-imperialist sentiment contributed to the dissolution of empires and the restructuring of states. The pamphlet's date and its argument that the war itself weakened the imperial claim place it inside that sentence rather than in the interwar one."),

 dict(q="A hypothetical economic survey written in 1946 observes that the states which ended the recent war on the winning side emerged with enlarged industrial plant, technologies developed under wartime pressure, and large credits owed to them abroad, while much of the industrial capacity of the defeated and occupied states lay in ruins. This observation most directly helps explain",
   choices=[
     "why technological and economic gains made during World War II by the victorious nations shifted the global balance of power",
     "why hopes for greater self-government went unfulfilled in the years after World War I",
     "why regional trade agreements spread free-market principles late in the twentieth century",
     "why diseases associated with poverty persisted throughout the twentieth century",
     "why the victorious nations dissolved their own overseas empires in the first year after the war"],
   ans=0,
   why="KC-6.2.IV.C.i states that technological and economic gains experienced during World War II by the victorious nations shifted the global balance of power. The survey describes precisely those gains and the corresponding ruin of the losing side, which is the mechanism of the shift."),

 dict(q="A political science textbook published in the early 1950s describes an international system that had been reduced, within a few years of the war's end, from several roughly comparable great powers to two states of an altogether different order of magnitude. As this course frames the period, those two states are best characterized as",
   choices=[
     "a democracy, the United States, and an authoritarian communist state, the Soviet Union",
     "an authoritarian communist state, the United States, and a democracy, the Soviet Union",
     "two democracies whose disagreement with each other was economic rather than ideological",
     "two authoritarian communist states competing for the leadership of a single bloc",
     "two overseas empires that emerged from the war with their colonial possessions enlarged"],
   ans=0,
   why="KC-6.2.IV.C.ii states that the democracy of the United States and the authoritarian communist Soviet Union emerged as superpowers. The reversed pairing is the tempting error here, so the key names each state with its own regime type rather than naming the pair alone."),

 dict(q="Which statement best compares the outcome of colonial demands for greater self-government after World War I with the outcome of such demands after World War II?",
   choices=[
     "After World War I those hopes were largely unfulfilled, while after World War II anti-imperialist sentiment contributed to the dissolution of empires",
     "After World War I anti-imperialist sentiment dissolved the empires, while after World War II those hopes were largely unfulfilled",
     "Both wars were followed within a year by the dissolution of the empires that had fought them",
     "Neither war changed the standing of colonial peoples' demands for self-government in any way",
     "Both wars were followed by imperial powers extending full self-government to their colonies within a decade"],
   ans=0,
   why="KC-6.2.II sets the two outcomes in that order: hopes largely unfulfilled following World War I, and increasing anti-imperialist sentiment after World War II contributing to the dissolution of empires. The reversal of the two halves is the error the comparison is built to catch, so the key states both halves in the framework's own order."),

 dict(q="The table gives hypothetical figures for four states, two of which ended the war of 1939 to 1945 among the victors and two among the defeated. Which conclusion does the table alone support?",
   table=_T_OUTPUT,
   choices=[
     "Two of the four states increased their share, while the other two lost more than half of theirs",
     "Every state in the table held a larger share in 1948 than it had held in 1938",
     "The state with the largest share in 1938 held the smallest share in 1948",
     "The two states that lost share held more between them in 1948 than the largest state held alone",
     "The four states together held exactly the same share in 1948 as they had held in 1938"],
   ans=0,
   why="KC-6.2.IV.C.i states that economic gains by the victorious nations shifted the global balance of power, and a redistribution of manufacturing share is one form that shift takes. The figures are hypothetical and the keyed conclusion is recomputed from the table alone in the verifier, so no outside knowledge of any real state is required or invited."),

 dict(q="A memorandum written by a colonial administrator in 1949 predicts that within a generation sovereign states will stand where imperial provinces now do, and that the imperial power's own government will have to be reorganized around a much smaller role in the world. The process the memorandum predicts is described in this course as",
   choices=[
     "the dissolution of empires and the restructuring of states",
     "the proliferation of nuclear weapons among newly independent states",
     "the growth of knowledge economies in some regions of the world",
     "the spread of a globalized consumer culture across national borders",
     "the persistence of diseases associated with poverty in poorer regions"],
   ans=0,
   why="KC-6.2.II names the outcome of rising anti-imperialist sentiment as the dissolution of empires and the restructuring of states. The memorandum describes both halves of that outcome, the disappearance of the imperial units and the remaking of the metropole's own state."),

 dict(q="An editorial published in a neutral European country in 1950 observes that local political quarrels in almost every region are now being described by outsiders as episodes in a single global argument about how economies ought to be owned and directed. The editorial identifies a feature of the period that this course describes as",
   choices=[
     "a power struggle between capitalism and communism carried on across the globe",
     "a competition among several roughly equal European empires for overseas colonies",
     "a dispute confined to Europe that had little effect on other regions",
     "a contest over religious doctrine between two organized faiths",
     "a debate about the nature and causes of climate change"],
   ans=0,
   why="KC-6.2.IV.C.ii states that the emergence of the two superpowers led to ideological conflict and a power struggle between capitalism and communism across the globe. The editorial's observation that local quarrels were being read as episodes of one argument is that struggle seen from a third country."),

 dict(q="A student is asked to situate a 1948 speech by a colonial nationalist within a broader historical context. Which approach would best accomplish that task?",
   choices=[
     "Relating the speech to rising anti-imperialist sentiment after World War II and to the shifting global balance of power",
     "Summarizing the speech's argument sentence by sentence in the order it was delivered",
     "Counting how often the speech uses the word independence and reporting the total",
     "Describing the speaker's vocabulary and judging whether the prose is persuasive today",
     "Listing every other speech delivered anywhere in the world during the same month"],
   ans=0,
   why="Situating a development in a broader context, the skill this topic practices, means connecting it to the larger processes running through the period. KC-6.2.II supplies the relevant process for a 1948 nationalist speech, and KC-6.2.IV.C.i supplies the change in the balance of power that made the moment possible; summary, word counts and style judgements do none of that."),

 dict(q="An imperial government's white paper of 1946 asserts that its colonial subjects are content with imperial rule and desire no change. Which additional body of evidence would be most useful in testing that assertion?",
   choices=[
     "Statements issued in the same years by nationalist organizations within those colonies",
     "Budget records showing how much the imperial government spent on its navy",
     "Manufacturing output figures for the defeated states of the recent war",
     "Membership rolls of political parties in the imperial capital itself",
     "Accounts of the imperial government's negotiations with its wartime allies"],
   ans=0,
   why="KC-6.2.II identifies rising anti-imperialist sentiment within the colonies as the development at issue after World War II, so the claim is about colonial opinion and must be tested against sources produced by colonial subjects. The other bodies of evidence report on the imperial state rather than on the people whose contentment is asserted."),

 dict(q="Which sequence of developments is consistent with the way this course orders the period?",
   choices=[
     "Hopes for self-government largely unfulfilled after World War I, then rising anti-imperialist sentiment after World War II, then the dissolution of empires",
     "The dissolution of empires, then rising anti-imperialist sentiment, then unfulfilled hopes for self-government",
     "Rising anti-imperialist sentiment after World War I, then the dissolution of empires, then World War II",
     "The dissolution of empires after World War I, then World War II, then renewed imperial expansion",
     "Unfulfilled hopes for self-government after World War II, then World War I, then the dissolution of empires"],
   ans=0,
   why="KC-6.2.II states the order explicitly: hopes largely unfulfilled following World War I, then in the years following World War II increasing anti-imperialist sentiment contributing to the dissolution of empires. Every distractor moves at least one of those three stages out of that order."),

 dict(q="In the framework of this course, what is the relationship between anti-imperialist sentiment and the dissolution of empires after World War II?",
   choices=[
     "Rising anti-imperialist sentiment contributed to the dissolution of empires",
     "The dissolution of empires produced anti-imperialist sentiment where none had existed",
     "The two developments occurred in different centuries and are unrelated",
     "Anti-imperialist sentiment delayed the dissolution of empires by dividing colonial opinion",
     "Neither development is treated as having any bearing on the other"],
   ans=0,
   why="KC-6.2.II states that increasing anti-imperialist sentiment contributed to the dissolution of empires and the restructuring of states, making the sentiment a contributing cause and the dissolution its outcome. Reversing the two is the characteristic error, so the key names the direction as well as the pair."),

 dict(q="The table records a hypothetical count of the sovereign states holding membership in an international organization founded in 1945. Which conclusion does the table alone support?",
   table=_T_MEMBERS,
   choices=[
     "The number of member states nearly tripled over the thirty years recorded",
     "The number of member states fell in at least one of the recorded decades",
     "The largest single increase occurred in the decade beginning in 1965",
     "The membership was unchanged between 1945 and 1955",
     "More than half of the states listed for 1975 had already joined by 1945"],
   ans=0,
   why="KC-6.2.II describes the dissolution of empires and the restructuring of states, and a rising count of sovereign states is one visible form of that restructuring. The figures are a hypothetical record and the keyed arithmetic is recomputed from the table alone in the verifier."),

 dict(q="A veterans' association formed in an African colony in 1946 petitions the imperial government, noting that its members fought in the recent war and asking why men trusted with the empire's defense are not trusted with the government of their own country. The petition is best understood as",
   choices=[
     "evidence of the anti-imperialist sentiment that increased in the colonies after World War II",
     "evidence that colonial subjects were excluded from service in the imperial armed forces",
     "evidence that the imperial government had already conceded self-government before 1946",
     "evidence of the growth of knowledge economies in the second half of the century",
     "evidence that the war left the victorious states economically weaker than the defeated ones"],
   ans=0,
   why="KC-6.2.II identifies increasing anti-imperialist sentiment in the years following World War II as the development to which such a petition belongs. The petition's own premise, that its members served, contradicts the exclusion reading, and KC-6.2.IV.C.i places the economic gains with the victorious rather than the defeated states."),

 dict(q="Two unattributed sources are set side by side. Text 1, from 1919, promises colonial subjects that their loyalty during the war will be remembered when the empire considers its future arrangements. Text 2, from 1947, tells the same colony's readers that promises of that kind were made once before and kept only on paper. The most defensible use of the pair is to argue that",
   choices=[
     "the unfulfilled expectations left by the first war shaped the political language of the second postwar moment",
     "colonial subjects had no expectations of self-government at any point before 1947",
     "the imperial government fulfilled its 1919 promise within a decade of making it",
     "the two texts were written by the same author and express a single continuous argument",
     "expectations of self-government arose for the first time only after World War II"],
   ans=0,
   why="KC-6.2.II states that hopes for greater self-government were largely unfulfilled following World War I and that anti-imperialist sentiment increased after World War II. Text 2 is legible as a reply to the disappointment Text 1 set up, which is the connection between the two moments the key states; the pair cannot establish authorship."),

 dict(q="Which statement about the world's empires in the years immediately after 1945 is best supported by this course's framework?",
   choices=[
     "Anti-imperialist sentiment was increasing, and it contributed to the eventual dissolution of empires",
     "Empires dissolved everywhere within a single year of the war's end",
     "Imperial authority in Asia and Africa was stronger in 1950 than it had been in 1930",
     "No empire underwent any change in its territorial extent during the twentieth century",
     "Anti-imperialist sentiment was falling, and imperial rule was becoming more popular"],
   ans=0,
   why="KC-6.2.II states that increasing anti-imperialist sentiment contributed to the dissolution of empires and the restructuring of states. The framework describes a contributing process, not a single-year collapse, and it describes sentiment rising rather than falling."),

 dict(q="A 1947 report to an imperial cabinet argues that holding the empire's remaining possessions would now cost more than the possessions return, because the war has left the treasury depleted and the armed forces overstretched. The report is best used as evidence about",
   choices=[
     "the weakened position from which imperial powers faced rising demands for independence",
     "the technological gains that the defeated states made during the war",
     "the growth of multinational corporations in the late twentieth century",
     "the spread of chemically and genetically modified forms of agriculture",
     "the emergence of new epidemic diseases in the second half of the century"],
   ans=0,
   why="KC-6.2.IV.C.i places the war's economic and technological gains with the victorious nations and thereby marks the war as a redistribution of capacity, while KC-6.2.II places rising anti-imperialist demands in the same years. A report on depleted imperial means speaks to the meeting of those two, not to later economic or medical developments."),

 dict(q="Considered as evidence, what is the principal limitation of a single 1948 pamphlet by a colonial nationalist party for a historian studying anti-imperialist sentiment across a whole colony?",
   choices=[
     "It states the position of one organized party and cannot by itself measure how widely that position was held",
     "It was written after 1945 and so falls outside the period in which such sentiment existed",
     "It concerns politics rather than economics and so bears on no course development",
     "Pamphlets were not produced in colonies during this period and the source must be misdated",
     "It names a colony rather than an empire and so cannot be compared with any other source"],
   ans=0,
   why="KC-6.2.II describes sentiment across colonial societies, a claim about breadth that one party's pamphlet cannot settle on its own. The pamphlet is squarely inside the period the same statement describes, so the objections about dating and relevance fail."),

 dict(q="A historian writes that the Cold War is unintelligible without the war that preceded it. Which piece of supporting evidence draws most directly on this course's account of that connection?",
   choices=[
     "The wartime gains of the victorious nations shifted the global balance of power, and that shifted balance evolved into the Cold War",
     "The Cold War began with a formal declaration of war issued by one bloc against the other",
     "The two superpowers had been each other's principal enemies throughout the war of 1939 to 1945",
     "The Cold War was fought entirely within Europe and left the rest of the world untouched",
     "Empires expanded their overseas holdings during the war and defended them afterward"],
   ans=0,
   why="KC-6.2.IV.C.i states that the victorious nations' wartime gains shifted the global balance of power, and KC-6.2.IV.C.ii states that the shifted balance of economic and political power rapidly evolved into the Cold War. That two-step is the connection the historian's claim rests on."),

 dict(q="The table gives hypothetical figures for three imperial powers. Which conclusion does the table alone support?",
   table=_T_TROOPS,
   choices=[
     "The power that drew the most colonial servicemen retained the fewest colonies in 1960",
     "The power that drew the fewest colonial servicemen retained the fewest colonies in 1960",
     "Every power in the table retained more than ten colonies in 1960",
     "The three powers together drew fewer than two million colonial servicemen",
     "The number of colonies retained rises as the number of servicemen drawn rises"],
   ans=0,
   why="KC-6.2.II makes rising anti-imperialist sentiment after World War II a contributing cause of the dissolution of empires, and wartime service is one of the experiences such sentiment drew on. The figures are hypothetical, and the verifier recomputes the ordering the key asserts from the table alone; the table shows an association and, as with any three cases, settles no cause."),

 dict(q="Which of the following would be the strongest evidence that the global balance of power had shifted by the late 1940s?",
   choices=[
     "Two states had acquired economic and military capacities that no other state could approach",
     "Several European states retained overseas colonies that they had held before the war",
     "A treaty had been signed ending hostilities between the belligerents",
     "The population of the world had grown over the preceding decade",
     "Newspapers in many countries reported on international affairs daily"],
   ans=0,
   why="KC-6.2.IV.C.i speaks of a shift in the global balance of power, and KC-6.2.IV.C.ii identifies its result as the emergence of two superpowers. A balance shifts when capacity is redistributed, so evidence of two states holding capacity no other can approach is the direct evidence; treaties, population and press coverage are not measures of relative power."),

 dict(q="An economics lecture given in 1949 argues that a state's weight in world affairs now depends less on the extent of its territory than on its industrial capacity and its command of new technologies. Applied to the period, this argument best explains why",
   choices=[
     "states holding large overseas empires could nonetheless lose standing relative to the war's victors",
     "the dissolution of empires had no effect on the states that had governed them",
     "colonial subjects lost interest in self-government during the 1940s",
     "the defeated states of the war retained their prewar share of world influence",
     "industrial capacity ceased to matter to international standing after 1945"],
   ans=0,
   why="KC-6.2.IV.C.i attributes the shift in the global balance of power to technological and economic gains rather than to territorial extent, which is why an empire could be large and still lose ground. KC-6.2.II then places the dissolution of those empires in the same years."),

 dict(q="A 1950 school textbook from a newly independent country opens its final chapter by saying that the country's history since 1919 is the history of a promise deferred and then seized. Which pair of course developments does that sentence compress?",
   choices=[
     "Unfulfilled hopes for self-government after the first war, and independence won amid rising anti-imperialist sentiment after the second",
     "Independence won after the first war, and the loss of that independence after the second",
     "The expansion of empires after the first war, and their further expansion after the second",
     "A shift of manufacturing toward Asia, and the growth of knowledge economies elsewhere",
     "The founding of new military alliances, and the proliferation of nuclear weapons"],
   ans=0,
   why="KC-6.2.II supplies both halves in that order: hopes largely unfulfilled following World War I, then increasing anti-imperialist sentiment after World War II contributing to the dissolution of empires. Deferred and then seized is that sequence stated in the textbook's own terms."),

 dict(q="Which question about a 1946 colonial petition would a historian practising contextualization most likely ask?",
   choices=[
     "What larger postwar developments make a petition of this kind appear in this year rather than earlier",
     "How many words the petition contains and whether its grammar is correct",
     "Whether the paper the petition was printed on was manufactured locally",
     "Which of the petition's sentences is the longest and which the shortest",
     "Whether a modern reader finds the petition's tone agreeable"],
   ans=0,
   why="Contextualization, the skill this topic practises, asks what broader process a specific development sits inside; KC-6.2.II names the process for a 1946 colonial petition. Counting words, examining paper stock and judging tone describe the artefact without situating it."),

 dict(q="A commentator in 1947 writes that the world's political argument has changed subject: where the great powers once disputed which of them should hold which territories, they now dispute how societies everywhere should be organized. According to this course, that change of subject is best explained by",
   choices=[
     "the emergence of two superpowers whose rivalry was ideological as well as territorial",
     "the disappearance of all disagreement about territory anywhere in the world",
     "the founding of new colonies by the victorious states after the war",
     "the growth of a globalized consumer culture in the second half of the century",
     "the spread of debates about greenhouse gases and climate change"],
   ans=0,
   why="KC-6.2.IV.C.ii states that the United States and the Soviet Union emerged as superpowers, which led to ideological conflict and a power struggle between capitalism and communism across the globe. An argument about how societies should be organized is that ideological conflict described from outside it."),

 dict(q="Which statement about the years from 1945 to 1949 is NOT supported by this course's framework?",
   choices=[
     "The victorious nations of the war emerged economically weaker than the states they had defeated",
     "The global balance of power had shifted by the end of the war",
     "Anti-imperialist sentiment was increasing in colonized regions",
     "Two states had emerged with capacities that set them apart from the rest",
     "The war's technological gains accrued substantially to its victors"],
   ans=0,
   why="KC-6.2.IV.C.i places the technological and economic gains of the war with the victorious nations, so the claim that those nations emerged weaker than the defeated reverses the framework's sentence. The other four restate KC-6.2.IV.C.i, KC-6.2.II and KC-6.2.IV.C.ii."),

 dict(q="A newly formed political party in a colony announces in 1948 that it will seek independence rather than a larger share of seats in the colonial legislature. Its choice is best situated within",
   choices=[
     "the postwar rise of anti-imperialist sentiment that pressed beyond reform toward the end of imperial rule",
     "the interwar decades in which such demands were granted as a matter of course",
     "a period in which colonial parties uniformly preferred reform within the empire to independence",
     "the late twentieth century turn toward free-market economic policies",
     "a period in which imperial powers were expanding their territorial holdings"],
   ans=0,
   why="KC-6.2.II describes anti-imperialist sentiment increasing after World War II and contributing to the dissolution of empires, which is a demand that goes past reform of colonial institutions. The same sentence records that the earlier, more modest hopes had been left unfulfilled rather than granted."),

 dict(q="A researcher wants to explain why demands for independence produced results after 1945 that similar demands had not produced after 1919. Which pair of considerations does this course make most relevant?",
   choices=[
     "The greater strength of postwar anti-imperialist sentiment together with the war's redistribution of economic and technological capacity",
     "The invention of the printing press together with the founding of the first universities",
     "The globalization of consumer culture together with the growth of online commerce",
     "The spread of vaccines and antibiotics together with the rise of chronic disease",
     "The signing of regional trade agreements together with the growth of multinational corporations"],
   ans=0,
   why="KC-6.2.II supplies the first consideration, increasing anti-imperialist sentiment after World War II, and KC-6.2.IV.C.i supplies the second, the wartime shift of technological and economic capacity that left the imperial powers differently placed. The other pairs belong to developments the framework dates to the later twentieth century."),

 dict(q="An unattributed dispatch from 1946 reports that in the imperial capital officials speak of the colonies as a burden to be managed, whereas thirty years earlier the same offices spoke of them as the foundation of national greatness. The change in official language is best explained by",
   choices=[
     "the altered economic position of the imperial state after a war that shifted the balance of power",
     "a decline in the population of the colonies over the same thirty years",
     "the abolition of the colonial administration by international agreement",
     "the imperial state's acquisition of additional colonies during the war",
     "the disappearance of nationalist movements from the colonies"],
   ans=0,
   why="KC-6.2.IV.C.i states that wartime technological and economic gains by the victorious nations shifted the global balance of power, which changed what an empire was worth to the state holding it. KC-6.2.II records nationalist sentiment increasing rather than disappearing over the same years."),

 dict(q="Considering the whole of this topic, which single sentence best states the historical context in which the Cold War began?",
   choices=[
     "A war that redistributed economic and technological capacity left two states preeminent while anti-imperialist sentiment rose in the colonies of the older powers",
     "A long peace among the great powers ended when two states discovered that their economies were identical",
     "The empires of Europe emerged from the war strengthened and extended their rule for another century",
     "Colonial peoples had already secured self-government before the war began and played no part afterward",
     "The world's political argument after 1945 concerned climate and resources rather than economic systems"],
   ans=0,
   why="KC-6.2.IV.C.i gives the redistribution of capacity, KC-6.2.IV.C.ii gives the two preeminent states and the ideological struggle that followed, and KC-6.2.II gives the rising anti-imperialist sentiment in the same years. The key is the conjunction of those three; each distractor contradicts at least one of them."),
]
