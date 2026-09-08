# AP U.S. HISTORY 8.4 Economy after 1945  (title copied from US_HISTORY_topics.json)
# Unit 8, Period 8: 1945 to 1980. Thematic focuses WXT, Work, Exchange, and Technology,
# and MIG, Migration and Settlement. Reasoning process: causation. Suggested skill 2.C,
# explain the significance of a source's point of view, purpose, historical situation,
# and/or audience, including how these might limit the use or uses of a source.
#
# THE REQUIRED COURSE CONTENT OF THIS TOPIC, in the framework's own words. This topic
# prints TWO Learning Objectives under two thematic focuses, and one historical
# development beneath each:
#
#   Unit 8 Learning Objective D
#       Explain the causes of economic growth in the years after World War II.
#   KC-8.3.I.A   A burgeoning private sector, federal spending, the baby boom, and
#                technological developments helped spur economic growth.
#
#   Unit 8 Learning Objective E
#       Explain the causes and effects of the migration of various groups of Americans
#       after 1945.
#   KC-8.3.I.B   As higher education opportunities and new technologies rapidly expanded,
#                increasing social mobility encouraged the migration of the middle class
#                to the suburbs and of many Americans to the South and West. The Sun Belt
#                region emerged as a significant political and economic force.
#
#   Their parent, printed in the Unit 8 preview at topic 8.1 and cited here only where an
#   item needs the frame these two sit inside:
#   KC-8.3.I     Rapid economic and social changes in American society fostered a sense of
#                optimism in the postwar years.
#
# WHAT IS DELIBERATELY NOT KEYED. KC-8.3.I.A names four contributors to growth and says
# they "helped spur" it; it does not rank them, quantify any of them, or say that they
# were the only ones. So no key here ranks the four, and the one item that asks about
# relative size asks it of a hypothetical table and is recomputed from that table alone.
# Nor does any key name a statute, an agency, a company, a highway programme or a
# mortgage scheme: the framework names none of those, and this topic's OPTIONAL SOURCES
# page is explicitly not required content.
#
# NO FIGURES: the three data items carry a table= and every figure in them is labelled
# hypothetical in the stem. PROSE ONLY; spans are written "1945 to 1980".
# FIVE choices (A-E). Invented sources are marked hypothetical.
TOPIC = ("8.4", "Economy after 1945", 8)

_T_MEASURES = dict(
    headers=["Measure in a hypothetical record",
             "Index in 1948 (1948 equals 100)",
             "Index in 1968"],
    rows=[["Private sector output", "100", "196"],
          ["Federal spending", "100", "172"],
          ["Patents granted", "100", "158"],
          ["Births per year", "100", "134"]])

_T_REGION = dict(
    headers=["Grouping of regions in a hypothetical record",
             "Population in 1950 (millions)",
             "Population in 1970 (millions)"],
    rows=[["South and West together", "58", "89"],
          ["Northeast and Midwest together", "93", "111"]])

_T_MOVE = dict(
    headers=["Household in a hypothetical survey",
             "Reason the survey records for moving",
             "Destination the survey records"],
    rows=[["Household 1", "A new job in a growing industry",
           "A suburb of the same metropolitan area"],
          ["Household 2", "Completion of a course of higher education",
           "A city in the South"],
          ["Household 3", "A new job in a growing industry",
           "A city in the West"],
          ["Household 4", "Completion of a course of higher education",
           "A suburb of the same metropolitan area"]])

QUESTIONS = [

 dict(q="Unit 8 Learning Objective D states what students should be able to explain about the "
        "postwar economy. What does the framework ask for?",
      choices=[
        "The causes of economic growth in the years after World War II",
        "The effects of economic growth on American foreign policy",
        "The causes and effects of the migration of various groups of Americans after 1945",
        "The continuities and changes in Cold War policies from 1945 to 1980",
        "The causes and effects of the Red Scare after World War II"],
      ans=0,
      why="Unit 8 Learning Objective D reads 'Explain the causes of economic growth in the years "
          "after World War II.' Learning Objective E, printed beneath the second thematic focus "
          "on the same page, is the migration objective, and the last two are Learning "
          "Objectives B and C from other topics of this unit."),

 dict(q="This topic prints a second Learning Objective beneath its migration thematic focus. "
        "What does Unit 8 Learning Objective E ask students to explain?",
      choices=[
        "The causes and effects of the migration of various groups of Americans after 1945",
        "The causes of economic growth in the years after World War II",
        "The reasons the middle class remained in the cities after 1945",
        "The effects of immigration from outside the United States after 1945",
        "The continuities and changes in immigration patterns over time"],
      ans=0,
      why="Unit 8 Learning Objective E reads 'Explain the causes and effects of the migration of "
          "various groups of Americans after 1945.' Learning Objective D is the growth objective "
          "printed above it, and Learning Objective K, about continuities and changes in "
          "immigration patterns, is printed on the page of a later topic in this unit."),

 dict(q="KC-8.3.I.A names four things that helped spur economic growth. Which set gives all "
        "four?",
      choices=[
        "A burgeoning private sector, federal spending, the baby boom, and technological "
        "developments",
        "A burgeoning private sector, foreign aid, the baby boom, and railway building",
        "Federal spending, technological developments, tariffs, and the growth of trade unions",
        "The baby boom, technological developments, immigration, and the export of capital",
        "A burgeoning private sector, federal spending, higher education, and the Sun Belt"],
      ans=0,
      why="KC-8.3.I.A names 'a burgeoning private sector, federal spending, the baby boom, and "
          "technological developments'. Each rejected option keeps some of that list and "
          "substitutes causes from elsewhere; higher education and the Sun Belt belong to "
          "KC-8.3.I.B, which is a sentence about migration rather than about the causes of "
          "growth."),

 dict(q="KC-8.3.I.A says the four things it names HELPED SPUR economic growth. What does that "
        "wording establish?",
      choices=[
        "That each contributed to growth without the sentence claiming any one of them produced "
        "it alone",
        "That each was sufficient by itself to produce the growth described",
        "That the four are ranked in the order the sentence lists them",
        "That growth would have occurred at the same rate without any of them",
        "That the framework treats the causes of growth as unknown"],
      ans=0,
      why="'Helped spur' attributes contribution rather than sufficiency, and KC-8.3.I.A gives "
          "its four items as a list without ranking or weighting them. The sentence therefore "
          "neither makes any one of them decisive nor denies that they mattered, and it plainly "
          "does offer an account of the causes Learning Objective D asks about."),

 dict(q="KC-8.3.I.B opens with two things expanding rapidly. Which pair does the framework name?",
      choices=[
        "Higher education opportunities and new technologies",
        "Higher education opportunities and federal spending",
        "New technologies and the size of the armed forces",
        "Home ownership and foreign trade",
        "The private sector and the birth rate"],
      ans=0,
      why="KC-8.3.I.B opens 'As higher education opportunities and new technologies rapidly "
          "expanded'. Federal spending, the private sector and the birth rate belong to "
          "KC-8.3.I.A's list of contributors to growth, and the armed forces, home ownership and "
          "foreign trade appear in neither sentence of this topic."),

 dict(q="According to KC-8.3.I.B, what did increasing social mobility encourage?",
      choices=[
        "The migration of the middle class to the suburbs and of many Americans to the South and "
        "West",
        "The migration of the middle class to the South and West and of many Americans to the "
        "suburbs",
        "The migration of most Americans out of the South and West",
        "The return of the middle class from the suburbs to the central cities",
        "The migration of Americans to other countries in search of work"],
      ans=0,
      why="KC-8.3.I.B states that increasing social mobility encouraged 'the migration of the "
          "middle class to the suburbs and of many Americans to the South and West'. The "
          "sentence attaches each group to its own destination, so exchanging them misreports it, "
          "and the remaining options reverse the direction of movement the framework describes."),

 dict(q="KC-8.3.I.B ends with a claim about the Sun Belt. What does the framework say about it?",
      choices=[
        "That the region emerged as a significant political and economic force",
        "That the region emerged as a significant economic force but not a political one",
        "That the region emerged as a significant political force but not an economic one",
        "That the region lost population to the Northeast and Midwest",
        "That the region's emergence lay outside the period this unit covers"],
      ans=0,
      why="KC-8.3.I.B states that 'the Sun Belt region emerged as a significant political and "
          "economic force', naming both kinds of significance together. Dropping either one is "
          "the likeliest error here, and the sentence places the emergence inside the same "
          "movement of population toward the South and West that it has just described."),

 dict(q="Which sequence best states the causal chain KC-8.3.I.B sets out?",
      choices=[
        "Higher education opportunities and new technologies expanded, social mobility increased, "
        "and migration to the suburbs and to the South and West followed",
        "Migration to the suburbs came first, which expanded higher education opportunities and "
        "new technologies",
        "Social mobility fell, which drove Americans toward the South and West",
        "The Sun Belt emerged first, which caused higher education opportunities to expand",
        "The framework describes the developments without linking them"],
      ans=0,
      why="KC-8.3.I.B is built as a chain: as higher education opportunities and new technologies "
          "rapidly expanded, INCREASING social mobility ENCOURAGED the two migrations, and the "
          "Sun Belt then emerged. Reversing any link inverts the sentence, and it plainly does "
          "link the developments rather than merely listing them, which is what Learning "
          "Objective E asks students to explain."),

 dict(q="Which of the following does KC-8.3.I.A NOT name among the things that helped spur "
        "economic growth?",
      choices=[
        "A reduction in the amount the federal government spent",
        "A burgeoning private sector",
        "The baby boom",
        "Technological developments",
        "Federal spending"],
      ans=0,
      why="KC-8.3.I.A names federal SPENDING among the contributors, so a reduction in what the "
          "federal government spent is not only absent from the sentence but the reverse of what "
          "appears there. The other three options are the remaining items on the framework's own "
          "list."),

 dict(q="The suggested skill printed beside this topic is 2.C. What does it ask students to do?",
      choices=[
        "Explain the significance of a source's point of view, purpose, historical situation, and "
        "audience, including how these might limit the use or uses of a source",
        "Explain the point of view, purpose, historical situation, or audience of a source",
        "Explain how a specific historical development or process is situated within a broader "
        "historical context",
        "Explain a historical concept, development, or process",
        "Identify patterns among or connections between historical developments and processes"],
      ans=0,
      why="Skill 2.C is printed beside this topic as the skill students practise in meeting Unit "
          "8 Learning Objective D and Learning Objective E, and it carries the further step that skill 2.B, the "
          "near-neighbour distractor, does not: explaining how a source's features might limit "
          "its use. The remaining options are skills 4.B, 1.B and 5.A."),

 dict(q="A hypothetical advertisement of 1954, placed by the builder of a new housing "
        "development outside a large city, promises quiet streets and new schools. Applying "
        "skill 2.C, what does its purpose tell a reader about its use as evidence?",
      choices=[
        "It was made to sell houses, so it is strong evidence of what buyers were being offered "
        "and weak evidence of what life in such a development was like",
        "It was made to sell houses, so it is strong evidence of what life in such a development "
        "was like",
        "It was made by a private firm, so it can tell a reader nothing about migration",
        "Its purpose cannot be recovered from an advertisement",
        "Its purpose makes it useful only for the history of advertising"],
      ans=0,
      why="KC-8.3.I.B records the migration of the middle class to the suburbs, and an "
          "advertisement aimed at prospective buyers is direct evidence of the inducements held "
          "out to them. Skill 2.C asks how purpose limits use: a document written to sell reports "
          "its makers' appeal reliably and the conditions it describes much less so, which is why "
          "both halves of the key have to be held together."),

 dict(q="A hypothetical university bulletin of 1958 lists new degree programmes and the numbers "
        "admitted to each. Which development named in this topic does it most directly bear on?",
      choices=[
        "The rapid expansion of higher education opportunities that KC-8.3.I.B places before "
        "increasing social mobility",
        "The baby boom that KC-8.3.I.A names among the contributors to economic growth",
        "The emergence of the Sun Belt as a political and economic force",
        "The burgeoning private sector named in KC-8.3.I.A",
        "The migration of the middle class to the suburbs"],
      ans=0,
      why="KC-8.3.I.B opens with higher education opportunities and new technologies rapidly "
          "expanding, and a record of new degree programmes and rising admissions is evidence of "
          "the first of those. The other options name real content of this topic that a list of "
          "degree programmes does not directly measure."),

 dict(q="A hypothetical chamber of commerce report of 1966 urges firms in the Northeast to open "
        "plants in a southern state, citing its growing population. Which claim of KC-8.3.I.B "
        "does the report most directly illustrate?",
      choices=[
        "That the Sun Belt region emerged as a significant political and economic force",
        "That higher education opportunities rapidly expanded",
        "That new technologies rapidly expanded",
        "That the middle class migrated to the suburbs",
        "That federal spending helped spur economic growth"],
      ans=0,
      why="KC-8.3.I.B closes by stating that the Sun Belt region emerged as a significant "
          "political and economic force, and an appeal to move production toward a growing "
          "southern state is an instance of that economic weight being felt. Federal spending "
          "belongs to KC-8.3.I.A, and the other options name parts of KC-8.3.I.B that the report "
          "does not address."),

 dict(q="The table records four hypothetical measures twenty years apart. Which conclusion does "
        "the table alone support?",
      table=_T_MEASURES,
      choices=[
        "All four measures stand higher in the later year without any of them doubling, and "
        "private sector output rises by the most",
        "One of the four measures stands lower in the later year",
        "Federal spending rises by the most of the four measures",
        "Every measure recorded more than doubles between the two years",
        "The four measures stand at the same level as each other in the later year"],
      ans=0,
      why="KC-8.3.I.A names a burgeoning private sector, federal spending, the baby boom, and "
          "technological developments together as having helped spur economic growth, and a "
          "record in which four such measures all rise is the shape that sentence describes. The "
          "figures are hypothetical, the sentence itself ranks nothing, and every reading offered "
          "is recomputed from the table alone in the verifier."),

 dict(q="Using the hypothetical population record, which conclusion does the table support?",
      table=_T_REGION,
      choices=[
        "Both groupings gain population, but the South and West gain by a larger share of their "
        "own starting population",
        "Both groupings gain population, but the Northeast and Midwest gain by a larger share of "
        "their own starting population",
        "The South and West lose population across the record",
        "The South and West hold a larger population than the Northeast and Midwest in the later "
        "year",
        "The two groupings are recorded at the same population in the later year"],
      ans=0,
      why="KC-8.3.I.B records the migration of many Americans to the South and West and the "
          "emergence of the Sun Belt as a significant political and economic force, and a faster "
          "proportional gain in those regions is one form that shift takes. The figures are "
          "hypothetical and both the direction of each change and the comparison between the two "
          "rates are recomputed from the table alone."),

 dict(q="Using the hypothetical household survey, which statement does the record support?",
      table=_T_MOVE,
      choices=[
        "Every recorded destination is either a suburb or a place in the South or West, which are "
        "the directions of movement this topic names",
        "Every household is recorded as moving to a suburb",
        "One household is recorded as moving to the Northeast",
        "Every household records the same reason for moving",
        "No household is recorded as moving to the South or West"],
      ans=0,
      why="KC-8.3.I.B names two directions of movement, the middle class to the suburbs and many "
          "Americans to the South and West, and every destination in the record falls under one "
          "of them. The households are hypothetical and the presence of both kinds of "
          "destination, along with the falsity of each rejected reading, is recomputed from the "
          "table alone."),

 dict(q="A hypothetical household account book kept between 1949 and 1959 records a family's "
        "purchases of new domestic machinery. Applying skill 2.C, what limits its use as evidence "
        "about the postwar economy as a whole?",
      choices=[
        "It records one household, so it cannot by itself show how widely such purchases were "
        "made",
        "It was kept during the period, which disqualifies it as evidence",
        "It records purchases rather than opinions, so it cannot be evidence of anything",
        "It was kept privately, so nothing in it can be true",
        "It concerns domestic machinery, which this topic does not discuss"],
      ans=0,
      why="KC-8.3.I.A names technological developments among the contributors to economic growth "
          "and a burgeoning private sector alongside them, so the subject is squarely within the "
          "topic. Skill 2.C asks how a source's features limit its use, and the limit here is "
          "breadth: one household is evidence about that household, and a claim about the economy "
          "as a whole needs many."),

 dict(q="A hypothetical firm's prospectus of 1955 tells shareholders that demand for its goods "
        "will grow because there are more children in the country than before. Which contributor "
        "named in KC-8.3.I.A is the prospectus appealing to?",
      choices=[
        "The baby boom",
        "Federal spending",
        "Technological developments",
        "The expansion of higher education opportunities",
        "The emergence of the Sun Belt"],
      ans=0,
      why="KC-8.3.I.A names the baby boom among the things that helped spur economic growth, and "
          "an argument from a larger number of children is an appeal to exactly that. Higher "
          "education and the Sun Belt belong to KC-8.3.I.B, and neither federal spending nor "
          "technological development is what the prospectus cites."),

 dict(q="A hypothetical study argues that postwar economic growth is fully explained by "
        "government outlays. Which sentence of this topic most directly qualifies that argument?",
      choices=[
        "KC-8.3.I.A, which names federal spending as one of four contributors that helped spur "
        "growth",
        "KC-8.3.I.B, which describes the migration of the middle class to the suburbs",
        "KC-8.3.I.B's statement that the Sun Belt emerged as a political and economic force",
        "Unit 8 Learning Objective E, which concerns migration rather than growth",
        "The framework offers nothing that bears on the argument"],
      ans=0,
      why="KC-8.3.I.A places federal spending in a list with a burgeoning private sector, the "
          "baby boom, and technological developments, and says the four together helped spur "
          "growth, so the framework treats government outlays as one contributor among several. "
          "The migration sentence and its Learning Objective concern a different question."),

 dict(q="How are this topic's two required sentences related to each other?",
      choices=[
        "KC-8.3.I.A gives contributors to economic growth and KC-8.3.I.B gives movements of "
        "population that accompanied it, and both sit beneath the same key concept about postwar "
        "change",
        "KC-8.3.I.A and KC-8.3.I.B describe the same development in different words",
        "KC-8.3.I.B contradicts KC-8.3.I.A",
        "KC-8.3.I.A belongs to this unit and KC-8.3.I.B to a later one",
        "The two sentences concern different centuries"],
      ans=0,
      why="Both are lettered sub-points of KC-8.3.I, which states that rapid economic and social "
          "changes in American society fostered a sense of optimism in the postwar years. "
          "KC-8.3.I.A supplies the economic side and KC-8.3.I.B the social and geographic side, "
          "so they are complementary parts of one account rather than a repetition or a "
          "contradiction."),

 dict(q="A hypothetical letter written in 1961 by a worker who has moved from a northern city to "
        "a southern one explains that he followed his employer's new plant. Applying skill 2.C, "
        "what does the source's point of view contribute?",
      choices=[
        "It reports a move from the inside, giving one migrant's reason rather than a measure of "
        "how common that reason was",
        "It reports a move from the inside, which makes it a measure of how common such moves "
        "were",
        "It was written by a worker, so it cannot bear on economic questions",
        "It was written during the period, so it is less reliable than a later account",
        "Its point of view cannot be recovered from a letter"],
      ans=0,
      why="KC-8.3.I.B records the migration of many Americans to the South and West, and a "
          "participant's letter is direct evidence of one such move and of the reason he gives "
          "for it. Skill 2.C asks how point of view bears on use: an insider's account is "
          "strongest about the particular case and cannot by itself establish a pattern, which "
          "is the distinction the two similar options are built to separate."),

 dict(q="Which of the following would be the strongest evidence for the claim that increasing "
        "social mobility encouraged migration, as KC-8.3.I.B describes?",
      choices=[
        "Records linking households' education or occupation to whether and where they moved",
        "A count of the total population of the United States in each year",
        "A list of the goods sold by one manufacturer",
        "A record of federal spending on defence",
        "A summary of United States policy toward the Soviet Union"],
      ans=0,
      why="KC-8.3.I.B makes increasing social mobility the link between the expansion of higher "
          "education and new technologies on one side and migration on the other, so evidence for "
          "it has to connect a household's position to its movement. A national population total, "
          "one firm's sales, defence outlays and foreign policy each bear on something else."),

 dict(q="A hypothetical planning report of 1963 predicts that a metropolitan area's central city "
        "will lose households to the districts around it. Which development named in this topic "
        "does the prediction concern?",
      choices=[
        "The migration of the middle class to the suburbs",
        "The migration of many Americans to the South and West",
        "The rapid expansion of new technologies",
        "The baby boom",
        "The burgeoning private sector"],
      ans=0,
      why="KC-8.3.I.B names the migration of the middle class to the suburbs as one of the two "
          "movements increasing social mobility encouraged, and a shift of households from a "
          "central city to the districts around it is that movement. The move toward the South "
          "and West is the sentence's other direction and is not what a single metropolitan area's "
          "internal shift describes."),

 dict(q="Why does KC-8.3.I.B's phrase 'various groups of Americans' matter for the way Learning "
        "Objective E is stated?",
      choices=[
        "Because the objective asks about several movements of population rather than one, and "
        "the sentence names two with different groups and destinations",
        "Because the objective is confined to the middle class",
        "Because the objective concerns arrivals from outside the United States",
        "Because the objective treats all migrants as moving for the same reason",
        "Because the objective concerns a period before 1945"],
      ans=0,
      why="Unit 8 Learning Objective E asks for the causes and effects of the migration of "
          "various groups of Americans after 1945, and KC-8.3.I.B supplies two distinct "
          "movements: the middle class to the suburbs, and many Americans to the South and West. "
          "The objective is neither confined to one group nor about immigration from abroad, "
          "which is the subject of a different objective in this unit."),

 dict(q="A hypothetical survey of 1970 reports that a majority of respondents in a southern city "
        "were born in another state. Which claim does the survey most directly support?",
      choices=[
        "That people had been moving into the South, which KC-8.3.I.B names as one direction of "
        "postwar migration",
        "That the middle class had been moving to the suburbs",
        "That higher education opportunities had expanded",
        "That federal spending had helped spur economic growth",
        "That new technologies had expanded rapidly"],
      ans=0,
      why="KC-8.3.I.B states that increasing social mobility encouraged the migration of many "
          "Americans to the South and West, and a population largely born elsewhere is evidence "
          "of arrivals. The suburban movement is the sentence's other direction, and the "
          "remaining options name causes rather than the movement itself."),

 dict(q="Which statement about the causes of postwar growth is NOT supported by this topic's "
        "required content?",
      choices=[
        "Technological developments played no part in postwar economic growth",
        "A burgeoning private sector helped spur economic growth",
        "Federal spending helped spur economic growth",
        "The baby boom helped spur economic growth",
        "Several different factors together helped spur economic growth"],
      ans=0,
      why="KC-8.3.I.A names technological developments among the four things that helped spur "
          "economic growth, so denying their part contradicts the sentence directly. The four "
          "rejected statements restate the same sentence, item by item and then as a whole."),

 dict(q="A hypothetical trade journal of 1957 describes machinery that allows a factory to "
        "produce more goods with the same workforce. Which contributor named in KC-8.3.I.A does "
        "the description illustrate?",
      choices=[
        "Technological developments",
        "The baby boom",
        "Federal spending",
        "The expansion of higher education opportunities",
        "The emergence of the Sun Belt as a political force"],
      ans=0,
      why="KC-8.3.I.A names technological developments among the things that helped spur economic "
          "growth, and machinery that raises output per worker is such a development. The baby "
          "boom and federal spending are the sentence's other contributors, and higher education "
          "and the Sun Belt belong to KC-8.3.I.B."),

 dict(q="What does the framework identify as an effect of the migrations KC-8.3.I.B describes?",
      choices=[
        "The emergence of the Sun Belt region as a significant political and economic force",
        "A decline in higher education opportunities",
        "The end of technological change",
        "A fall in the population of the United States",
        "The return of the middle class to the central cities"],
      ans=0,
      why="KC-8.3.I.B closes by stating that the Sun Belt region emerged as a significant "
          "political and economic force, which is the effect the sentence records and which Unit "
          "8 Learning Objective E asks students to explain alongside the causes. None of the "
          "rejected options appears in the sentence, and several reverse it."),

 dict(q="A hypothetical account written in 1980 recalls that the writer's family moved twice "
        "after 1945, first to a suburb and then to a western state. Applying skill 2.C, what does "
        "its historical situation contribute and what does it limit?",
      choices=[
        "It is recalled from the end of the period, so it can trace a whole sequence of moves but "
        "reports them through what the writer knew later",
        "It is recalled from the end of the period, so it reports each move exactly as it was "
        "understood at the time",
        "It concerns one family, so it cannot bear on migration at all",
        "It was written in 1980, so it lies outside this period entirely",
        "Its historical situation cannot be recovered from an account of this kind"],
      ans=0,
      why="KC-8.3.I.B names both a move to the suburbs and a move to the South and West, so a "
          "single family recalling both is evidence about the two movements together. Skill 2.C "
          "asks what a source's situation contributes and what it limits: distance allows the "
          "sequence to be seen whole and colours how each step is remembered, which is why the "
          "key holds the two clauses together."),

 dict(q="Taken together, what do this topic's two required sentences establish about the years "
        "after 1945?",
      choices=[
        "That several forces together spurred economic growth, and that the mobility accompanying "
        "it moved Americans toward the suburbs and toward the South and West",
        "That a single cause produced economic growth, and that Americans stayed where they were",
        "That economic growth and migration were unrelated developments",
        "That migration occurred while the economy contracted",
        "That the framework describes the period's economy but not its movements of population"],
      ans=0,
      why="KC-8.3.I.A gives four contributors that together helped spur growth and KC-8.3.I.B "
          "gives the mobility and the two migrations that accompanied it, with the Sun Belt "
          "emerging as a result. Both are sub-points of KC-8.3.I, on rapid economic and social "
          "changes in American society, so the framework treats them as parts of one postwar "
          "change rather than as separate or opposed ones."),
]
