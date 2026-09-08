# AP U.S. HISTORY 8.1 Contextualizing Period 8  (title copied from US_HISTORY_topics.json)
# Unit 8, Period 8: 1945 to 1980. Suggested skill 4.B, explain how a specific historical
# development or process is situated within a broader historical context.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 8 Learning Objective A
#       Explain the context for societal change from 1945 to 1980.
#
#   KC-8.1      The United States responded to an uncertain and unstable postwar world by
#               asserting and working to maintain a position of global leadership, with
#               far-reaching domestic and international consequences.
#   KC-8.1.I    United States policymakers engaged in a cold war with the authoritarian
#               Soviet Union, seeking to limit the growth of Communist military power and
#               ideological influence, create a free-market global economy, and build an
#               international security system.
#   KC-8.1.II   Cold War policies led to public debates over the power of the federal
#               government and acceptable means for pursuing international and domestic
#               goals while protecting civil liberties.
#   KC-8.2      New movements for civil rights and liberal efforts to expand the role of
#               government generated a range of political and cultural responses.
#   KC-8.2.I    Seeking to fulfill Reconstruction-era promises, civil rights activists and
#               political leaders achieved some legal and political successes in ending
#               segregation, although progress toward racial equality was slow.
#   KC-8.2.II   Responding to social conditions and the African American civil rights
#               movement, a variety of movements emerged that focused on issues of
#               identity, social justice, and the environment.
#   KC-8.2.III  Liberalism influenced postwar politics and court decisions, but it came
#               under increasing attack from the left as well as from a resurgent
#               conservative movement.
#   KC-8.3      Postwar economic and demographic changes had far-reaching consequences for
#               American society, politics, and culture.
#   KC-8.3.I    Rapid economic and social changes in American society fostered a sense of
#               optimism in the postwar years.
#   KC-8.3.II   New demographic and social developments, along with anxieties over the Cold
#               War, changed U.S. culture and led to significant political and moral
#               debates that sharply divided the nation.
#
#   The topic page's own instruction on what context is: students could examine "change
#   from and/or continuity with preceding historical developments" and "similarities
#   and/or differences with contemporaneous historical developments in different regions
#   or geographical areas."
#
# WHAT IS NOT KEYED, DELIBERATELY. This is a CONTEXTUALIZING topic and its Required
# Course Content is printed under the heading PREVIEW: UNIT 8 KEY CONCEPTS. The lettered
# sub-points -- KC-8.1.I.A through KC-8.3.II.C -- are printed on the pages of topics 8.2
# through 8.14, not here. So no key in this module names a president, a war, a statute, a
# court case, a region or a named movement of the period. Every key rests on the ten
# previewed sentences above and on what the skill of contextualization is.
# `no_period_detail` in verify_a8_1.py asserts that, and several items exist to test the
# boundary rather than to reward recall.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=, and
# every figure in them is labelled hypothetical in the stem.
# PROSE ONLY: no LaTeX; a span of years is written "1945 to 1980", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("8.1", "Contextualizing Period 8", 8)

_T_GROWTH = dict(
    headers=["Year (hypothetical record)",
             "Index of real output per person (1945 equals 100)",
             "Households holding a given durable good (percent)"],
    rows=[["1945", "100", "12"],
          ["1955", "128", "60"],
          ["1965", "152", "85"],
          ["1975", "171", "95"]])

_T_MOVEMENTS = dict(
    headers=["Movement recorded in a hypothetical survey",
             "Issue the survey records it as focusing on"],
    rows=[["Movement 1", "Identity"],
          ["Movement 2", "Social justice"],
          ["Movement 3", "The environment"],
          ["Movement 4", "Reducing the power of the federal government"]])

_T_MOOD = dict(
    headers=["Year (hypothetical poll)",
             "Respondents expressing optimism about their own future (percent)",
             "Respondents expressing anxiety about international dangers (percent)"],
    rows=[["1948", "68", "71"],
          ["1953", "72", "74"],
          ["1958", "70", "69"],
          ["1963", "74", "66"]])

QUESTIONS = [

 dict(q="Unit 8 Learning Objective A asks students to explain the context for something across "
        "a stated span of years. What does the framework name?",
      choices=[
        "Societal change from 1945 to 1980",
        "Cold War diplomacy from 1945 to 1991",
        "Economic growth from 1945 to 1960",
        "The expansion of civil rights from 1960 to 1980",
        "Constitutional revision from 1945 to 1980"],
      ans=0,
      why="Unit 8 Learning Objective A reads 'Explain the context for societal change from 1945 "
          "to 1980.' The span belongs to the whole of Period 8, and the object of the sentence "
          "is societal change rather than any single strand of it, so narrowing it to diplomacy, "
          "growth, civil rights or constitutional revision replaces the framework's own subject."),

 dict(q="According to KC-8.1, how does the framework describe the postwar world, and what does "
        "it say the United States did in response?",
      choices=[
        "An uncertain and unstable postwar world, to which the United States responded by "
        "asserting and working to maintain a position of global leadership",
        "A settled and predictable postwar world, in which the United States gave up a position "
        "of global leadership",
        "An uncertain and unstable postwar world, from which the United States withdrew into "
        "isolation",
        "A settled and predictable postwar world, in which the United States asserted a position "
        "of global leadership",
        "An uncertain and unstable postwar world, in which the United States left global "
        "leadership to international organizations"],
      ans=0,
      why="KC-8.1 states that the United States responded to an uncertain and unstable postwar "
          "world by asserting and working to maintain a position of global leadership. Both "
          "halves matter and each is separately contradicted here: calling the world settled "
          "denies the first, and withdrawal, isolation or delegation to other bodies denies the "
          "second."),

 dict(q="KC-8.1 ends by describing the consequences of the position the United States took. "
        "Which reading does that clause support?",
      choices=[
        "The consequences were far-reaching and were both domestic and international",
        "The consequences were confined to the conduct of foreign policy",
        "The consequences were felt at home but not abroad",
        "The consequences were slight in both spheres",
        "The framework does not say where the consequences were felt"],
      ans=0,
      why="KC-8.1 says the assertion of global leadership carried 'far-reaching domestic and "
          "international consequences', which names both spheres and calls them far-reaching. "
          "Confining them to foreign policy or to the home front drops half the clause, calling "
          "them slight contradicts 'far-reaching', and the sentence plainly does locate them."),

 dict(q="KC-8.1.I lists what United States policymakers were seeking when they engaged in a cold "
        "war with the Soviet Union. Which option gives the framework's own list?",
      choices=[
        "To limit the growth of Communist military power and ideological influence, create a "
        "free-market global economy, and build an international security system",
        "To limit the growth of Communist military power, abolish free markets abroad, and avoid "
        "permanent commitments overseas",
        "To create a free-market global economy, enlarge the colonial holdings of allied states, "
        "and disarm",
        "To build an international security system, restrict trade with every other nation, and "
        "leave Europe to settle its own affairs",
        "To limit Communist ideological influence, bring American industry under public "
        "ownership, and reduce federal spending"],
      ans=0,
      why="KC-8.1.I states that policymakers engaged in a cold war with the authoritarian Soviet "
          "Union 'seeking to limit the growth of Communist military power and ideological "
          "influence, create a free-market global economy, and build an international security "
          "system'. Each rejected option keeps one item from that list and substitutes aims the "
          "sentence does not contain, several of which reverse it."),

 dict(q="How does KC-8.1.I characterize the state with which United States policymakers engaged "
        "in a cold war?",
      choices=[
        "As the authoritarian Soviet Union",
        "As a Soviet Union then moving toward democracy",
        "As a coalition of newly independent nations",
        "As a wartime ally that continued to share American economic aims",
        "As a state the framework deliberately declines to characterize"],
      ans=0,
      why="KC-8.1.I names 'the authoritarian Soviet Union', so the framework does supply a "
          "characterization and that characterization is authoritarian. A move toward democracy, "
          "a coalition of new nations and a continuing partner in American aims are each "
          "incompatible with the adjective the sentence chooses."),

 dict(q="KC-8.1.II says Cold War policies led to public debates. What does the framework say "
        "those debates were about?",
      choices=[
        "The power of the federal government, and acceptable means for pursuing international "
        "and domestic goals while protecting civil liberties",
        "The power of state governments to conduct foreign policy of their own",
        "Whether elections should be held at all during a period of international tension",
        "The proper size of the federal judiciary and nothing beyond it",
        "Whether a free-market global economy was worth having"],
      ans=0,
      why="KC-8.1.II states that Cold War policies led to public debates over the power of the "
          "federal government and acceptable means for pursuing international and domestic goals "
          "while protecting civil liberties. The sentence names two subjects together, and none "
          "of the rejected options is either of them."),

 dict(q="The last clause of KC-8.1.II is 'while protecting civil liberties'. What does including "
        "it show about the debates that sentence describes?",
      choices=[
        "That what was at issue was how to pursue international and domestic goals without "
        "sacrificing civil liberties",
        "That civil liberties were not seriously at issue in the period",
        "That the framework treats civil liberties as an international question only",
        "That the debates were carried on in the courts rather than in public",
        "That the debates ceased once the goals had been achieved"],
      ans=0,
      why="KC-8.1.II ties acceptable means for pursuing international and domestic goals to the "
          "protection of civil liberties in a single clause, so the tension between the two is "
          "the subject of the debate. The same sentence calls the debates public, applies them to "
          "domestic as well as international goals, and reports no point at which they stopped."),

 dict(q="KC-8.2 names two developments that together generated a range of political and cultural "
        "responses. Which pair does the framework give?",
      choices=[
        "New movements for civil rights, and liberal efforts to expand the role of government",
        "New movements for civil rights, and efforts to reduce the role of government",
        "Cold War policies abroad, and liberal efforts to expand the role of government",
        "Postwar economic growth, and new movements for civil rights",
        "Demographic change, and the building of an international security system"],
      ans=0,
      why="KC-8.2 states that new movements for civil rights and liberal efforts to expand the "
          "role of government generated a range of political and cultural responses. Reversing "
          "expansion into reduction, or swapping either half for Cold War policy, growth or "
          "demographic change, replaces one of the framework's two terms with material it "
          "assigns to KC-8.1 or KC-8.3."),

 dict(q="KC-8.2 says the developments it names generated a RANGE of political and cultural "
        "responses. Which reading does that word exclude?",
      choices=[
        "That the responses were uniform and ran in a single direction",
        "That some of the responses were political",
        "That some of the responses were cultural",
        "That both of the developments named drew responses",
        "That the framework treats the responses as part of the period's history"],
      ans=0,
      why="A range is by definition varied, so KC-8.2's wording rules out a single uniform "
          "reaction; that is the whole force of the word in the sentence. The other four are "
          "things the sentence asserts rather than excludes, since it names political and "
          "cultural responses and attributes them to both developments it lists."),

 dict(q="Which statement matches what KC-8.2.I says civil rights activists and political leaders "
        "were seeking and what they achieved?",
      choices=[
        "Seeking to fulfill Reconstruction-era promises, they achieved some legal and political "
        "successes in ending segregation, although progress toward racial equality was slow",
        "Seeking to fulfill Reconstruction-era promises, they achieved complete racial equality "
        "within the period",
        "Seeking goals unconnected to any earlier period, they achieved some legal and political "
        "successes in ending segregation",
        "Seeking to fulfill Reconstruction-era promises, they achieved no legal or political "
        "success of any kind",
        "Seeking an end to segregation, they found that progress toward racial equality was "
        "rapid and largely uncontested"],
      ans=0,
      why="KC-8.2.I states that, seeking to fulfill Reconstruction-era promises, civil rights "
          "activists and political leaders achieved some legal and political successes in ending "
          "segregation, although progress toward racial equality was slow. The sentence is "
          "carefully balanced, and each rejected option breaks the balance in one direction or "
          "the other, or cuts the tie to the earlier era."),

 dict(q="The phrase 'Reconstruction-era promises' in KC-8.2.I links Period 8 to an earlier "
        "period. Under the topic page's own account of context, what kind of link is that?",
      choices=[
        "Continuity with a preceding historical development",
        "A difference with a contemporaneous development in another region",
        "A prediction about a period still to come",
        "A comparison between two regions of the United States",
        "A statement that the earlier period has no bearing on this one"],
      ans=0,
      why="The topic page offers two ways into context, one of them 'change from and/or "
          "continuity with preceding historical developments'. KC-8.2.I places the activists of "
          "this period in pursuit of promises made in an earlier era, so the link is that "
          "continuity. The page's second approach concerns contemporaneous developments in "
          "different regions, which is not what a link backward in time is."),

 dict(q="KC-8.2.II says a variety of movements emerged in response to two things and focused on "
        "three issues. Which option states both correctly?",
      choices=[
        "They responded to social conditions and to the African American civil rights movement, "
        "and focused on identity, social justice, and the environment",
        "They responded to social conditions alone, and focused on identity, social justice, and "
        "the environment",
        "They responded to social conditions and to the African American civil rights movement, "
        "and focused on tariffs, currency, and territorial expansion",
        "They responded to Cold War policies alone, and focused on identity, social justice, and "
        "the environment",
        "They responded to the African American civil rights movement alone, and focused on the "
        "power of the courts"],
      ans=0,
      why="KC-8.2.II states that, responding to social conditions and the African American civil "
          "rights movement, a variety of movements emerged that focused on issues of identity, "
          "social justice, and the environment. Dropping either half of the cause, or replacing "
          "the three issues, departs from the sentence in a way a prepared student can check "
          "against it."),

 dict(q="Which statement matches KC-8.2.III on the influence liberalism had and the opposition "
        "it met?",
      choices=[
        "Liberalism influenced postwar politics and court decisions, but came under increasing "
        "attack from the left as well as from a resurgent conservative movement",
        "Liberalism influenced postwar politics and court decisions, and came under attack only "
        "from a resurgent conservative movement",
        "Liberalism influenced postwar politics and court decisions, and came under attack only "
        "from the left",
        "Liberalism left court decisions untouched, though it was attacked from two directions",
        "Liberalism met no organized opposition during the postwar decades"],
      ans=0,
      why="KC-8.2.III states that liberalism influenced postwar politics and court decisions but "
          "came under increasing attack from the left as well as from a resurgent conservative "
          "movement. The phrase 'as well as' makes the opposition two-sided, so an account that "
          "keeps only one side of it, or denies the influence on courts, or denies opposition "
          "altogether, is not what the sentence says."),

 dict(q="According to KC-8.3, what kind of postwar changes had far-reaching consequences, and "
        "for what?",
      choices=[
        "Economic and demographic changes, with consequences for American society, politics, and "
        "culture",
        "Military and diplomatic changes, with consequences for American society, politics, and "
        "culture",
        "Economic and demographic changes, with consequences confined to the economy itself",
        "Legal and constitutional changes, with consequences for the courts alone",
        "Economic and demographic changes, with consequences felt only outside the United States"],
      ans=0,
      why="KC-8.3 states that postwar economic and demographic changes had far-reaching "
          "consequences for American society, politics, and culture. Substituting military and "
          "diplomatic change for the causes, or narrowing the consequences to the economy, the "
          "courts or other countries, alters one end of the sentence or the other."),

 dict(q="KC-8.3.I connects rapid economic and social changes in American society to a particular "
        "postwar mood. Which does the framework name?",
      choices=[
        "A sense of optimism in the postwar years",
        "A settled resignation about the nation's prospects",
        "A general indifference to public affairs",
        "A widespread hostility to economic growth",
        "A conviction that further change had become impossible"],
      ans=0,
      why="KC-8.3.I states that rapid economic and social changes in American society fostered a "
          "sense of optimism in the postwar years. Resignation, indifference, hostility to growth "
          "and a belief that change had stopped are each incompatible with the noun the framework "
          "chooses, and none appears in the preview."),

 dict(q="KC-8.3.II names what changed U.S. culture and what followed from it. Which option gives "
        "both as the framework does?",
      choices=[
        "New demographic and social developments together with anxieties over the Cold War "
        "changed U.S. culture, and led to significant political and moral debates that sharply "
        "divided the nation",
        "New demographic and social developments alone changed U.S. culture, and led to a broad "
        "political consensus",
        "Anxieties over the Cold War were the sole cause of cultural change, and they led to "
        "significant political and moral debates that sharply divided the nation",
        "New demographic and social developments together with anxieties over the Cold War "
        "changed U.S. culture, and brought the nation's political disagreements to an end",
        "New demographic and social developments changed the economy rather than the culture, "
        "and left political debate untouched"],
      ans=0,
      why="KC-8.3.II states that new demographic and social developments, along with anxieties "
          "over the Cold War, changed U.S. culture and led to significant political and moral "
          "debates that sharply divided the nation. Both the compound cause and the divisive "
          "outcome are the framework's, and each rejected option cuts one of the two causes or "
          "reverses the outcome."),

 dict(q="KC-8.3.I and KC-8.3.II stand side by side in the unit preview. Taken together, what do "
        "they establish about postwar American society?",
      choices=[
        "That a sense of optimism and debates that sharply divided the nation both belong to the "
        "same period",
        "That optimism gave way to division only once the period's debates had been settled",
        "That division came before the period's rapid economic changes",
        "That the framework records optimism but no serious disagreement",
        "That the framework records disagreement but no optimism"],
      ans=0,
      why="KC-8.3.I records a sense of optimism fostered by rapid economic and social change, "
          "and KC-8.3.II records debates that sharply divided the nation. Both are printed as "
          "part of the same preview for the same period, so the framework asserts each without "
          "ranking one after the other, which is what the rejected orderings and the two "
          "one-sided readings all do."),

 dict(q="The suggested skill printed on this topic page is 4.B. How does the framework state it?",
      choices=[
        "Explain how a specific historical development or process is situated within a broader "
        "historical context",
        "Identify and describe a historical context for a specific historical development or "
        "process",
        "Explain how a historical development or process relates to another historical "
        "development or process",
        "Explain a historical concept, development, or process",
        "Compare the arguments or main ideas of two sources"],
      ans=0,
      why="Skill 4.B, printed beside this topic and cited by Unit 8 Learning Objective A, reads "
          "'Explain how a specific historical development or process is situated within a broader "
          "historical context.' The others are skills 4.A, 5.B, 1.B and 3.C, each printed beside "
          "other topics of this course, and 4.A is the near neighbour a student is likeliest to "
          "take for this one."),

 dict(q="This topic's page tells students they could examine change from or continuity with "
        "PRECEDING developments, and similarities or differences with CONTEMPORANEOUS "
        "developments in different regions. Which pair illustrates those two approaches in that "
        "order?",
      choices=[
        "Civil rights activists were pursuing promises made in an earlier era; other societies "
        "were passing through postwar economic changes of their own at the same time",
        "Other societies were passing through postwar economic changes of their own at the same "
        "time; civil rights activists were pursuing promises made in an earlier era",
        "Both statements describe developments that came before the period",
        "Both statements describe developments inside the United States",
        "Neither statement is of the kind the topic page describes"],
      ans=0,
      why="The topic page names preceding developments first and contemporaneous developments in "
          "different regions second. KC-8.2.I's Reconstruction-era promises supply the first, and "
          "postwar change elsewhere supplies the second. Reversing the pair, or calling both "
          "preceding or both domestic, misapplies the page's own distinction."),

 dict(q="A hypothetical course outline states that the Required Course Content printed for this "
        "topic supplies the period's major legislation and military engagements. What is wrong "
        "with that?",
      choices=[
        "The content here is printed as a PREVIEW of the unit's key concepts, and that detail "
        "belongs to the unit's later topics",
        "The framework does not treat legislation or military engagements anywhere in the unit",
        "The preview lists no key concepts at all",
        "Detail of that kind belongs to Period 9 rather than to Period 8",
        "The framework treats the period's legislation as context rather than as content"],
      ans=0,
      why="The heading over this topic's Required Course Content reads PREVIEW: UNIT 8 KEY "
          "CONCEPTS, and the page tells the teacher to select one or two of those concepts for "
          "which students most need context. The lettered sub-points beneath KC-8.1, KC-8.2 and "
          "KC-8.3 carry that detail and are printed on the later topic pages of the same unit, "
          "so the unit does cover them and does not defer them to another period."),

 dict(q="Which of the following statements belongs to the unit's first key concept rather than "
        "to KC-8.2 or KC-8.3?",
      choices=[
        "The United States responded to an unstable postwar world by asserting a position of "
        "global leadership",
        "New movements for civil rights generated a range of political and cultural responses",
        "Postwar economic and demographic changes had far-reaching consequences for American "
        "culture",
        "Liberalism came under increasing attack from the left as well as from a resurgent "
        "conservative movement",
        "Rapid economic and social changes fostered a sense of optimism in the postwar years"],
      ans=0,
      why="KC-8.1 is the unit's first key concept and concerns the American response to an "
          "uncertain and unstable postwar world. The second and fourth statements are KC-8.2 and "
          "KC-8.2.III, and the third and fifth are KC-8.3 and KC-8.3.I, so all four belong to the "
          "other two key concepts of the preview."),

 dict(q="Which statement belongs to KC-8.3's account of economic and demographic change rather "
        "than to KC-8.2's account of movements and responses?",
      choices=[
        "New demographic and social developments changed U.S. culture and led to significant "
        "political and moral debates",
        "Civil rights activists and political leaders achieved some legal and political successes "
        "in ending segregation",
        "A variety of movements emerged that focused on issues of identity, social justice, and "
        "the environment",
        "Liberalism influenced postwar politics and court decisions",
        "Liberal efforts to expand the role of government generated a range of responses"],
      ans=0,
      why="Only the first is drawn from KC-8.3, whose sub-point KC-8.3.II describes new "
          "demographic and social developments changing U.S. culture and producing divisive "
          "political and moral debates. The remaining four are KC-8.2.I, KC-8.2.II, KC-8.2.III "
          "and KC-8.2, all of which sit under the key concept about movements and responses."),

 dict(q="A hypothetical policy memorandum written in 1949 argues that the United States cannot "
        "return to its prewar habits because the world left by the war is neither settled nor "
        "safe. Which previewed key concept does it most directly illustrate?",
      choices=[
        "KC-8.1, on the American response to an uncertain and unstable postwar world",
        "KC-8.2, on movements for civil rights and the responses they generated",
        "KC-8.3, on postwar economic and demographic change",
        "KC-8.2.III, on attacks upon liberalism from the left and from conservatives",
        "KC-8.3.II, on debates that sharply divided the nation"],
      ans=0,
      why="KC-8.1 is the sentence that describes an uncertain and unstable postwar world and the "
          "United States responding by asserting and working to maintain global leadership, which "
          "is the argument the memorandum makes. The other four previewed sentences concern "
          "movements and responses, economic and demographic change, opposition to liberalism, "
          "and cultural division, none of which is the memorandum's subject."),

 dict(q="A hypothetical letter to a newspaper editor in 1952 complains that measures adopted to "
        "pursue the nation's aims abroad are being used at home in ways that endanger ordinary "
        "people's rights. The letter is best used as evidence for which previewed statement?",
      choices=[
        "KC-8.1.II, on public debates over acceptable means for pursuing goals while protecting "
        "civil liberties",
        "KC-8.2.I, on legal and political successes in ending segregation",
        "KC-8.3.I, on rapid economic change and a sense of optimism",
        "KC-8.2.II, on movements focused on identity, social justice, and the environment",
        "KC-8.3, on the far-reaching consequences of economic and demographic change"],
      ans=0,
      why="KC-8.1.II states that Cold War policies led to public debates over the power of the "
          "federal government and acceptable means for pursuing international and domestic goals "
          "while protecting civil liberties, which is exactly the complaint the letter makes. "
          "None of the other previewed sentences concerns the means used to pursue foreign aims "
          "or their effect on liberties at home."),

 dict(q="The table records hypothetical figures for the postwar decades. Which conclusion does "
        "the table alone support?",
      table=_T_GROWTH,
      choices=[
        "Both recorded measures rise at every reading, and the durable good spreads from fewer "
        "than one household in five to nearly all",
        "The index of output per person falls in one of the decades recorded",
        "The durable good was already held by more than half of households in the first year "
        "recorded",
        "The index of output per person more than doubles across the record",
        "The two recorded measures move in opposite directions"],
      ans=0,
      why="KC-8.3.I attributes a sense of optimism to rapid economic and social changes in "
          "American society, and a record in which output per person and household holdings both "
          "rise is one form such change takes. The figures are hypothetical and the keyed "
          "conclusion, with the falsity of all four rejected readings, is recomputed from the "
          "table alone in the verifier."),

 dict(q="KC-8.2.II names three issues on which the movements it describes focused. Using the "
        "hypothetical survey table, which row records an issue that is NOT one of those three?",
      table=_T_MOVEMENTS,
      choices=[
        "The row recording a movement focused on reducing the power of the federal government",
        "The row recording a movement focused on identity",
        "The row recording a movement focused on social justice",
        "The row recording a movement focused on the environment",
        "Every row records one of the three issues the framework names"],
      ans=0,
      why="KC-8.2.II names identity, social justice, and the environment as the issues on which "
          "the variety of movements focused. Three rows of the table match those three issues and "
          "the fourth does not, so the fourth is the one outside the sentence; the reduction of "
          "federal power belongs instead to KC-8.2.III's account of the resurgent conservative "
          "movement that attacked liberalism."),

 dict(q="Using the hypothetical poll table, which statement does the record support about the "
        "years it covers?",
      table=_T_MOOD,
      choices=[
        "In every year recorded a majority expressed optimism about their own future, and in "
        "every year a majority also expressed anxiety about international dangers",
        "In no year recorded did a majority hold both attitudes at once",
        "Anxiety about international dangers falls below half in the last year recorded",
        "Optimism about respondents' own future declines at every reading",
        "The two recorded shares are equal in every year"],
      ans=0,
      why="KC-8.3.I records a sense of optimism in the postwar years and KC-8.3.II records "
          "anxieties over the Cold War, and the framework prints both for the same period rather "
          "than in sequence. The figures are hypothetical and the verifier recomputes from the "
          "table alone that both shares exceed half in every recorded year and that each rejected "
          "reading is false."),

 dict(q="Which of the following is NOT stated anywhere in the Unit 8 preview?",
      choices=[
        "That the federal government withdrew from economic life in the postwar years",
        "That Cold War policies led to public debates over the power of the federal government",
        "That a variety of movements emerged focused on identity, social justice, and the "
        "environment",
        "That rapid economic and social changes fostered a sense of optimism",
        "That liberalism influenced postwar politics and court decisions"],
      ans=0,
      why="The four rejected statements are KC-8.1.II, KC-8.2.II, KC-8.3.I and KC-8.2.III, each "
          "printed in the preview in nearly those words. Nothing in the preview says the federal "
          "government withdrew from economic life; KC-8.2 describes liberal efforts to EXPAND the "
          "role of government, which is the opposite claim."),

 dict(q="Which single sentence best collects what the framework previews for Unit 8 without "
        "adding to it?",
      choices=[
        "The United States asserted global leadership in an unstable postwar world, new movements "
        "and liberal efforts to expand government drew a range of responses, and economic and "
        "demographic change reshaped society, politics, and culture",
        "The United States withdrew from world affairs while its domestic politics grew calmer "
        "and more united",
        "Postwar economic growth is the whole of what this period covers",
        "Movements for civil rights met no organized opposition, and liberalism had no critics",
        "The nation's policies abroad and its changes at home had nothing to do with one another"],
      ans=0,
      why="The first collects KC-8.1, KC-8.2 and KC-8.3 in the order the preview prints them and "
          "adds nothing to any of the three. The second reverses KC-8.1 and KC-8.3.II, the third "
          "reduces the preview to part of KC-8.3, the fourth contradicts KC-8.2 and KC-8.2.III, "
          "and the fifth denies the link KC-8.1 draws between global leadership and domestic "
          "consequences."),

 dict(q="Taken together, what do the three previewed key concepts establish about the context "
        "Unit 8 asks students to explain?",
      choices=[
        "That change at home and the nation's position abroad are treated as parts of one "
        "context rather than as separate stories",
        "That the framework treats foreign policy as the only source of change in the period",
        "That the framework treats change at home as untouched by international events",
        "That the period's changes produced agreement rather than debate",
        "That the context for the period lies entirely outside the United States"],
      ans=0,
      why="KC-8.1 gives the assertion of global leadership far-reaching DOMESTIC as well as "
          "international consequences, KC-8.1.II makes Cold War policies the source of debates at "
          "home, and KC-8.3.II names anxieties over the Cold War among the causes of cultural "
          "change, so the framework joins the two rather than separating them. KC-8.2 and "
          "KC-8.3.II also record debate rather than agreement."),
]
