# AP U.S. HISTORY 5.1 Contextualizing Period 5  (title copied from US_HISTORY_topics.json)
# Unit 5, Period 5: 1844 to 1877. Reasoning process printed beside this topic in the
# Unit 5 outline: Continuity and Change. Suggested skill 4.B, explain how a specific
# historical development or process is situated within a broader historical context.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 5 Learning Objective A
#       Explain the context in which sectional conflict emerged from 1844 to 1877.
#
#   KC-5.1       The United States became more connected with the world, pursued an
#                expansionist foreign policy in the Western Hemisphere, and emerged as
#                the destination for many migrants from other countries.
#   KC-5.1.I     Popular enthusiasm for U.S. expansion, bolstered by economic and
#                security interests, resulted in the acquisition of new territories,
#                substantial migration westward, and new overseas initiatives.
#   KC-5.1.II    In the 1840s and 1850s, Americans continued to debate questions about
#                rights and citizenship for various groups of U.S. inhabitants.
#   KC-5.2       Intensified by expansion and deepening regional divisions, debates over
#                slavery and other economic, cultural, and political issues led the
#                nation into civil war.
#   KC-5.2.I     Ideological and economic differences over slavery produced an array of
#                diverging responses from Americans in the North and the South.
#   KC-5.2.II    Debates over slavery came to dominate political discussion in the
#                1850s, culminating in the bitter election of 1860 and the secession of
#                Southern states.
#   KC-5.3       The Union victory in the Civil War and the contested reconstruction of
#                the South settled the issues of slavery and secession, but left
#                unresolved many questions about the power of the federal government and
#                citizenship rights.
#   KC-5.3.I     The North's greater manpower and industrial resources, the leadership
#                of Abraham Lincoln and others, and the decision to emancipate enslaved
#                people eventually led to the Union military victory over the
#                Confederacy in the devastating Civil War.
#   KC-5.3.II.i  Reconstruction and the Civil War ended slavery, altered relationships
#                between the states and the federal government, and led to debates over
#                new definitions of citizenship, particularly regarding the rights of
#                African Americans, women, and other minorities.
#
#   The topic page's own instruction on what context is: students could examine "Change
#   from and/or continuity with preceding historical developments" and "Similarities
#   and/or differences with contemporaneous historical developments in different regions
#   or geographical areas."
#
#   The framework's NOTE ABOUT PERIODIZATION, printed in the course framework's front
#   matter, is the source for the three data items: it states that several of the periods
#   show some degree of overlap, that Period 4 emphasises antebellum reform and social
#   change with 1848 as an ending point, that Period 5 focuses on how expansion led to
#   debates over slavery and spans the Civil War and Reconstruction, that the emphasis in
#   Period 6 on economic development begins with the end of the Civil War in 1865, and
#   that Period 7 uses 1890 as the starting date for America's rise to global power. The
#   spans themselves are the course outline's.
#
# WHAT IS NOT KEYED, DELIBERATELY. This is a CONTEXTUALIZING topic and its Required
# Course Content is printed under the heading PREVIEW, so it is the unit's key concepts
# rather than the detail behind them. The lettered sub-points -- KC-5.1.I.A through
# KC-5.3.II.E -- belong to topics 5.2 through 5.11, which have their own pages. No key
# here names a campaign, a statute, a court decision, a treaty or a party. Abraham
# Lincoln, the Confederacy and Reconstruction ARE named, because the framework names
# them in the previewed sentences themselves; that is the line, and `no_period_detail`
# in the verifier draws it.
#
# SENSITIVE MATERIAL. Slavery, the Civil War and Reconstruction are handled here in the
# framework's own terms and no further: the module states what the CED states about
# them, invents no detail, and keys nothing that the framework leaves contested. Where
# the CED itself records a dispute -- the reconstruction it calls CONTESTED, the
# questions it says were LEFT UNRESOLVED -- the questions ask what the framework says
# about the dispute rather than settling it.
#
# NO FIGURES: the bank cannot display images, so the data items carry a table=.
# PROSE ONLY: no LaTeX; a span of years is written "1844 to 1877", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("5.1", "Contextualizing Period 5", 5)

_T_PERIODS = dict(
    headers=["Period of the course framework",
             "Span given in the course outline",
             "Emphasis the framework states for the period"],
    rows=[["Period 4", "1800 to 1848", "Antebellum reform and social change"],
          ["Period 5", "1844 to 1877", "How expansion led to debates over slavery"],
          ["Period 6", "1865 to 1898", "Economic development"],
          ["Period 7", "1890 to 1945", "America's rise to global power"]])

_T_APPROACH = dict(
    headers=["Statement a student offers as context (illustrative)",
             "Which of the topic page's two approaches it uses"],
    rows=[["A development already under way before 1844 that continued into the period",
           "Preceding developments"],
          ["A development in a different region of the world during the same years",
           "Contemporaneous developments elsewhere"],
          ["A development that had run its course before 1844",
           "Preceding developments"],
          ["A development in a different geographical area at the same time",
           "Contemporaneous developments elsewhere"]])

_T_TALLY = dict(
    headers=["Broad development proposed as context (illustrative tally)",
             "Number of groups proposing it"],
    rows=[["Westward expansion", "9"],
          ["Regional differences", "7"],
          ["Political controversies and compromises", "5"],
          ["Other proposals", "3"]])

QUESTIONS = [

 dict(q="Unit 5's Learning Objective A asks students to explain the context in which "
        "sectional conflict emerged across a stated span of years. Which span does the "
        "framework give?",
      choices=[
        "1844 to 1877",
        "1800 to 1848",
        "1865 to 1898",
        "1848 to 1877",
        "1844 to 1865"],
      ans=0,
      why="Unit 5 Learning Objective A reads 'Explain the context in which sectional "
          "conflict emerged from 1844 to 1877.' The span 1800 to 1848 is Period 4's and "
          "1865 to 1898 is Period 6's; the remaining two shorten the period at one end or "
          "the other and appear nowhere in the framework's periodisation."),

 dict(q="Learning Objective A for this unit names the development whose context students "
        "are asked to explain. Which development is it?",
      choices=[
        "The emergence of sectional conflict",
        "The rise of industrial capitalism in the United States",
        "European encounters in the Americas",
        "America's growth into its role as a world power",
        "The founding of the first permanent English settlements"],
      ans=0,
      why="Unit 5 Learning Objective A asks students to explain the context in which "
          "sectional conflict emerged from 1844 to 1877. The rise of industrial capitalism "
          "is Unit 6's Learning Objective A, European encounters are Unit 1's, and America "
          "growing into a world power is Unit 7's; the last belongs to an earlier period "
          "still and is not a Learning Objective of this course's Unit 5."),

 dict(q="KC-5.1 states three things about the United States in this period. Which set "
        "names all three?",
      choices=[
        "It became more connected with the world, pursued an expansionist foreign policy in "
        "the Western Hemisphere, and emerged as the destination for many migrants from "
        "other countries",
        "It withdrew from contact with other nations, avoided foreign commitments, and "
        "discouraged arrivals from abroad",
        "It became more connected with the world, pursued an expansionist foreign policy in "
        "the Western Hemisphere, and became a source of emigrants to other countries",
        "It reorganised its economy around large firms, opened new markets, and consolidated "
        "its businesses",
        "It became more connected with the world, settled its internal divisions, and turned "
        "away from expansion"],
      ans=0,
      why="KC-5.1 states that the United States became more connected with the world, "
          "pursued an expansionist foreign policy in the Western Hemisphere, and emerged as "
          "the destination for many migrants from other countries. One option reverses the "
          "direction of migration, making the country a source rather than a destination; "
          "another describes the industrial consolidation the framework places in Unit 6; "
          "and the remaining two contradict KC-5.1's connection with the world and KC-5.2's "
          "deepening regional divisions."),

 dict(q="According to KC-5.1.I, popular enthusiasm for U.S. expansion resulted in three "
        "things. Which set names them?",
      choices=[
        "The acquisition of new territories, substantial migration westward, and new "
        "overseas initiatives",
        "The acquisition of new territories, the end of slavery, and the growth of cities",
        "Substantial migration westward, the growth of manufacturing, and the founding of "
        "colleges",
        "New overseas initiatives, the reduction of tariffs, and the enlargement of the navy",
        "The acquisition of new territories, substantial migration eastward, and new "
        "domestic initiatives"],
      ans=0,
      why="KC-5.1.I states that popular enthusiasm for U.S. expansion, bolstered by economic "
          "and security interests, resulted in the acquisition of new territories, "
          "substantial migration westward, and new overseas initiatives. One option reverses "
          "the direction of the migration and turns the initiatives inward; the others "
          "import results the framework attributes elsewhere, and KC-5.3.II.i rather than "
          "KC-5.1.I is where the ending of slavery appears."),

 dict(q="KC-5.1.I names two interests that bolstered popular enthusiasm for U.S. expansion. "
        "Which pair does the framework give?",
      choices=[
        "Economic and security interests",
        "Religious and dynastic interests",
        "Economic and cultural interests",
        "Security and diplomatic interests",
        "Scientific and military interests"],
      ans=0,
      why="KC-5.1.I says popular enthusiasm for U.S. expansion was bolstered by economic and "
          "security interests. Each of the other pairs keeps one of the framework's two "
          "words or neither, and substituting a term the sentence does not use changes what "
          "the framework claims drove the enthusiasm."),

 dict(q="KC-5.1.II says that in the 1840s and 1850s Americans continued to debate questions "
        "about a particular subject. Which subject does the framework name?",
      choices=[
        "Rights and citizenship for various groups of U.S. inhabitants",
        "The proper relationship between business and government",
        "The moral obligation of the wealthy to help the less fortunate",
        "The extent to which federal courts should review the laws of the states",
        "The place of religion in public schooling"],
      ans=0,
      why="KC-5.1.II states that in the 1840s and 1850s, Americans continued to debate "
          "questions about rights and citizenship for various groups of U.S. inhabitants. "
          "The relationship between business and government and the obligations of the "
          "wealthy are debates the framework places in Unit 6 under KC-6.3.II and KC-6.3.I, "
          "and the last two subjects are not what this sentence names."),

 dict(q="KC-5.1.II says Americans CONTINUED to debate those questions in the 1840s and "
        "1850s. What does that word establish about the debate?",
      choices=[
        "That it was already under way before the period this unit covers",
        "That it began with the 1840s and had no earlier history",
        "That it had been settled earlier and was reopened only afterwards",
        "That it was confined to a single region of the country",
        "That it concerned only inhabitants who arrived after 1840"],
      ans=0,
      why="KC-5.1.II's word 'continued' places the debate before the decades it names, which "
          "is why the sentence belongs to a topic about context: the reasoning process the "
          "framework prints beside this topic is continuity and change, and the topic page "
          "asks students to examine continuity with PRECEDING developments. The sentence "
          "also says 'various groups of U.S. inhabitants', which rules out a single region "
          "and a single date of arrival."),

 dict(q="KC-5.2 names two things that intensified the debates that led the nation into civil "
        "war. Which pair does the framework give?",
      choices=[
        "Expansion and deepening regional divisions",
        "Foreign intervention and financial panic",
        "Expansion and the enlargement of the federal courts",
        "Deepening regional divisions and the arrival of migrants from abroad",
        "Industrial consolidation and the growth of cities"],
      ans=0,
      why="KC-5.2 opens 'Intensified by expansion and deepening regional divisions, debates "
          "over slavery and other economic, cultural, and political issues led the nation "
          "into civil war.' Each of the other pairs keeps at most one of the framework's two "
          "terms, and industrial consolidation and urban growth are what KC-6.1 and KC-6.2 "
          "describe in the following period."),

 dict(q="KC-5.2 says the debates that led the nation into civil war were over slavery and a "
        "further set of issues. Which set does the framework name?",
      choices=[
        "Economic, cultural, and political issues",
        "Religious, legal, and military issues",
        "Economic, military, and diplomatic issues",
        "Cultural, scientific, and educational issues",
        "Political, legal, and technological issues"],
      ans=0,
      why="KC-5.2 names debates over slavery and other economic, cultural, and political "
          "issues. Military, diplomatic, legal, scientific, educational and technological "
          "issues are not in that list, and reading the sentence as being about slavery "
          "alone drops the words 'and other' that the framework prints."),

 dict(q="A hypothetical study guide summarises KC-5.2.I by saying that the North held one "
        "view of slavery and the South held another. What does KC-5.2.I say that the "
        "summary gets wrong?",
      choices=[
        "The framework describes an array of diverging responses, not a single position held "
        "on each side",
        "The framework locates the differences in ideology and economics",
        "The framework names Americans in the North and the South as those who responded",
        "The framework makes slavery the subject of the differences",
        "The framework places these differences before the civil war it goes on to describe"],
      ans=0,
      why="KC-5.2.I states that ideological and economic differences over slavery produced an "
          "ARRAY OF DIVERGING RESPONSES from Americans in the North and the South, which is "
          "a description of many responses rather than one position on each side. The other "
          "four options restate things the sentence does say, so a summary cannot get them "
          "wrong by leaving the array out."),

 dict(q="According to KC-5.2.II, in which decade did debates over slavery come to dominate "
        "political discussion?",
      choices=[
        "The 1850s",
        "The 1820s",
        "The 1830s",
        "The 1870s",
        "The 1890s"],
      ans=0,
      why="KC-5.2.II states that debates over slavery came to dominate political discussion "
          "in the 1850s, culminating in the bitter election of 1860 and the secession of "
          "Southern states. KC-5.1.II names the 1840s and 1850s as the decades of debate "
          "over rights and citizenship, and no sentence of the Unit 5 preview assigns this "
          "domination to any of the other decades listed."),

 dict(q="KC-5.2.II says the debates of the 1850s culminated in two things. Which pair does "
        "the framework name?",
      choices=[
        "The bitter election of 1860 and the secession of Southern states",
        "The bitter election of 1860 and the outbreak of a war with a foreign power",
        "The secession of Southern states and the ending of slavery",
        "A convention called to revise the Constitution and the secession of Southern states",
        "The bitter election of 1860 and the admission of several new states"],
      ans=0,
      why="KC-5.2.II ends by naming the bitter election of 1860 and the secession of Southern "
          "states as what the debates culminated in. The ending of slavery is placed later, "
          "in KC-5.3.II.i, and the framework's Unit 5 preview names neither a foreign war "
          "nor a constitutional convention nor the admission of new states at this point."),

 dict(q="KC-5.3 states what the Union victory and the contested reconstruction of the South "
        "settled and what they left unresolved. Which statement gives both correctly?",
      choices=[
        "They settled the issues of slavery and secession, but left unresolved many questions "
        "about the power of the federal government and citizenship rights",
        "They settled many questions about the power of the federal government and "
        "citizenship rights, but left the issues of slavery and secession unresolved",
        "They settled the issues of slavery and of secession and left nothing unresolved",
        "They left the issues of slavery and secession and the questions about federal power "
        "equally unresolved",
        "They settled the questions about citizenship rights and nothing else"],
      ans=0,
      why="KC-5.3 states that the Union victory in the Civil War and the contested "
          "reconstruction of the South settled the issues of slavery and secession, but left "
          "unresolved many questions about the power of the federal government and "
          "citizenship rights. One option exchanges the settled half with the unresolved "
          "half, which is the likeliest misreading of the sentence and the reason both "
          "clauses have to be carried together."),

 dict(q="KC-5.3 calls the reconstruction of the South CONTESTED. Which reading does that word "
        "support?",
      choices=[
        "That the reconstruction was disputed rather than settled by agreement",
        "That the reconstruction was carried through without opposition",
        "That the reconstruction was abandoned before it began",
        "That the reconstruction concerned the North rather than the South",
        "That the reconstruction is the only part of the period the framework treats"],
      ans=0,
      why="KC-5.3's adjective 'contested', applied to the reconstruction of the South, states "
          "that it was disputed; the same sentence goes on to say that many questions were "
          "LEFT UNRESOLVED, which is what a dispute leaves behind. The framework locates the "
          "reconstruction in the South, describes it as taking place rather than being "
          "abandoned, and devotes KC-5.1 and KC-5.2 to other subjects."),

 dict(q="KC-5.3.I names three things that eventually led to the Union military victory over "
        "the Confederacy. Which set names all three?",
      choices=[
        "The North's greater manpower and industrial resources, the leadership of Abraham "
        "Lincoln and others, and the decision to emancipate enslaved people",
        "The North's greater manpower and industrial resources, intervention by a foreign "
        "power, and superior naval technology",
        "The leadership of Abraham Lincoln and others, the support of European governments, "
        "and shorter lines of supply",
        "The decision to emancipate enslaved people, the collapse of Southern agriculture, "
        "and the capture of the Southern capital",
        "The North's greater manpower and industrial resources, the leadership of Abraham "
        "Lincoln and others, and the refusal to emancipate enslaved people"],
      ans=0,
      why="KC-5.3.I names the North's greater manpower and industrial resources, the "
          "leadership of Abraham Lincoln and others, and the decision to emancipate enslaved "
          "people as what eventually led to the Union military victory over the Confederacy "
          "in the devastating Civil War. One option inverts the third of the three into a "
          "refusal, and the rest substitute foreign intervention, naval technology, supply "
          "lines and a captured capital, none of which the sentence names."),

 dict(q="KC-5.3.I credits the leadership of Abraham Lincoln AND OTHERS. What do those two "
        "added words do to the framework's claim?",
      choices=[
        "They decline to attribute the leadership to one person alone",
        "They name the other leaders individually",
        "They remove Lincoln from the framework's account of the victory",
        "They restrict the leadership in question to military commanders",
        "They make leadership the only cause the sentence gives"],
      ans=0,
      why="KC-5.3.I says 'the leadership of Abraham Lincoln and others', which widens the "
          "credit beyond one person without naming who the others were. The sentence keeps "
          "Lincoln in the account, does not say the others were commanders, and lists "
          "leadership alongside the North's greater manpower and industrial resources and "
          "the decision to emancipate enslaved people, so it is not the only cause given."),

 dict(q="KC-5.3.I says that the advantages it names EVENTUALLY led to the Union military "
        "victory. What does that word qualify?",
      choices=[
        "That the victory did not follow at once from the advantages the sentence names",
        "That the advantages themselves were in doubt",
        "That the victory was never in fact achieved",
        "That the advantages belonged to the Confederacy rather than to the Union",
        "That the sentence is describing the years after the war"],
      ans=0,
      why="KC-5.3.I's word 'eventually' sits between the advantages and the outcome, so it "
          "qualifies the timing rather than the fact: the same sentence states the victory "
          "was won and calls the war devastating. The advantages are attributed to the North "
          "and the outcome to the Union, and the sentence describes the war rather than what "
          "came after it, which is KC-5.3.II.i's subject."),

 dict(q="KC-5.3.II.i says the debates over new definitions of citizenship concerned the "
        "rights of particular groups. Which groups does the framework name?",
      choices=[
        "African Americans, women, and other minorities",
        "African Americans and recent arrivals from abroad only",
        "Women and holders of property",
        "Southern landowners and Northern manufacturers",
        "Federal officeholders and members of the state legislatures"],
      ans=0,
      why="KC-5.3.II.i states that the debates over new definitions of citizenship arose "
          "'particularly regarding the rights of African Americans, women, and other "
          "minorities'. Narrowing the list to two of the three, or replacing it with groups "
          "defined by property, region or office, changes whose rights the framework says "
          "were at issue."),

 dict(q="KC-5.3.II.i names three things Reconstruction and the Civil War did. Which set names "
        "all three?",
      choices=[
        "They ended slavery, altered relationships between the states and the federal "
        "government, and led to debates over new definitions of citizenship",
        "They ended slavery, restored the prewar relationship between the states and the "
        "federal government, and closed the debate over citizenship",
        "They ended slavery, enlarged the nation's territory, and settled the meaning of "
        "citizenship",
        "They ended the fighting, altered relationships between the states and the federal "
        "government, and led to debates over citizenship",
        "They ended slavery, altered relationships among the states themselves, and led to "
        "debates over new definitions of sovereignty"],
      ans=0,
      why="KC-5.3.II.i states that Reconstruction and the Civil War ended slavery, altered "
          "relationships between the states and the federal government, and led to debates "
          "over new definitions of citizenship. Two options close or settle the debate the "
          "sentence says was opened, one moves the altered relationship to one among the "
          "states alone and changes citizenship to sovereignty, and one drops the ending of "
          "slavery in favour of the ending of the fighting."),

 dict(q="The suggested skill printed on this topic's page is stated in the framework as which "
        "of the following?",
      choices=[
        "Explain how a specific historical development or process is situated within a "
        "broader historical context",
        "Identify and describe a historical context for a specific historical development or "
        "process",
        "Explain a historical concept, development, or process",
        "Compare the arguments or main ideas of two sources",
        "Use historical reasoning to explain relationships among pieces of historical "
        "evidence"],
      ans=0,
      why="The skill printed beside this topic is 4.B, explain how a specific historical "
          "development or process is situated within a broader historical context, and it is "
          "what Unit 5 Learning Objective A asks students to do when they explain the "
          "context in which sectional conflict emerged. The others are skills 4.A, 1.B, 3.C "
          "and 6.C, each printed beside other topics of this same unit."),

 dict(q="The topic page tells students that to understand context they could examine change "
        "from or continuity with PRECEDING historical developments, and similarities or "
        "differences with CONTEMPORANEOUS historical developments in different regions. "
        "Which statement describes the second of those two approaches?",
      choices=[
        "Setting a development beside something happening at the same time in a different "
        "region or geographical area",
        "Setting a development beside something that came before it",
        "Setting a development beside something that followed it",
        "Setting a development beside a later interpretation of it",
        "Setting a development beside a measurement taken in the same region"],
      ans=0,
      why="The topic page's second bullet reads 'Similarities and/or differences with "
          "contemporaneous historical developments in different regions or geographical "
          "areas', so the second approach is the simultaneous, different-place one; the "
          "first bullet is the preceding-development one. Unit 5 Learning Objective A asks "
          "for the context in which sectional conflict emerged, and both bullets are ways of "
          "supplying it."),

 dict(q="A hypothetical revision guide claims that this topic's Required Course Content "
        "supplies the detail of the war's campaigns and of the laws passed during "
        "Reconstruction. What is wrong with that claim?",
      choices=[
        "This topic's Required Course Content is printed as a PREVIEW of the unit's key "
        "concepts, and the detail belongs to the unit's later topics",
        "The framework does not treat the Civil War anywhere in Unit 5",
        "Those subjects belong to Period 6 rather than to Period 5",
        "The Required Course Content for this topic lists no key concepts at all",
        "The framework treats the Civil War as context rather than as course content"],
      ans=0,
      why="The topic page prints the unit's key concepts under the heading PREVIEW and tells "
          "the teacher to select one or two for which students most need context, so the "
          "lettered detail sits in topics 5.2 through 5.11 rather than here. KC-5.3 and "
          "KC-5.3.I name the Civil War and KC-5.3.II.i names Reconstruction, so Unit 5 does "
          "cover both and neither is deferred to the following period; and the preview does "
          "list key concepts."),

 dict(q="Which reasoning process does the framework's Unit 5 outline print beside this topic?",
      choices=[
        "Continuity and change",
        "Causation",
        "Comparison",
        "Periodisation",
        "Argumentation"],
      ans=0,
      why="The Unit 5 outline prints Continuity and Change as the reasoning process for this "
          "topic, Causation beside topics 5.2, 5.3, 5.6 and 5.7, and Comparison beside 5.4, "
          "5.5, 5.8 and 5.12; argumentation is the skill category of 5.12 rather than a "
          "reasoning process. Unit 5 Learning Objective A asks for the context in which "
          "sectional conflict emerged, and continuity with what preceded 1844 is one of the "
          "two approaches the topic page names."),

 dict(q="Using the table of course periods, what does the record show about the spans the "
        "framework gives to consecutive periods?",
      table=_T_PERIODS,
      choices=[
        "Consecutive periods overlap, because each later span begins before the one before it "
        "ends",
        "Consecutive periods are separated by a gap of several years",
        "Consecutive periods meet exactly, with neither a gap nor an overlap",
        "Only the first two of the four periods overlap",
        "Each successive span is shorter than the one before it"],
      ans=0,
      why="Read from the table alone: Period 5 begins in 1844 while Period 4 runs to 1848, "
          "Period 6 begins in 1865 while Period 5 runs to 1877, and Period 7 begins in 1890 "
          "while Period 6 runs to 1898, so all three consecutive pairs overlap and none is "
          "separated by a gap or meets exactly. The spans do not shorten in order. The "
          "framework says as much in its note about periodisation, and Unit 5 Learning "
          "Objective A asks for a context that a boundary drawn at one year could not supply."),

 dict(q="Using the same table of course periods, which claim goes BEYOND what the record can "
        "support?",
      table=_T_PERIODS,
      choices=[
        "That the framework regards the earlier of two overlapping periods as the more "
        "important",
        "That the span given for Period 5 begins before the span given for Period 4 ends",
        "That the span given for Period 6 begins before the span given for Period 5 ends",
        "That a different emphasis is recorded for each of the four periods",
        "That the span given for Period 7 is the longest of the four"],
      ans=0,
      why="The table records a span and an emphasis for each period and nothing that ranks "
          "one period above another, so relative importance is a claim it cannot reach. The "
          "other four are read off the rows: 1844 falls before 1848, 1865 falls before 1877, "
          "the four emphases differ, and Period 7's span is the longest. Unit 5 Learning "
          "Objective A asks for context rather than for a ranking of periods, and the "
          "framework's note about periodisation offers the overlaps as a caution against "
          "treating the boundaries as hard."),

 dict(q="Using the table of illustrative context statements, which two rows use the topic "
        "page's approach of examining preceding historical developments?",
      table=_T_APPROACH,
      choices=[
        "The row about a development already under way before 1844 and the row about a "
        "development that had run its course before 1844",
        "The two rows about developments in another region during the same years",
        "The row about a development already under way before 1844 and one of the rows about "
        "another region",
        "All four of the rows",
        "None of the four rows"],
      ans=0,
      why="Read from the table alone: exactly two rows are marked as using preceding "
          "developments, and they are the two whose statements sit before 1844, while the "
          "two marked as contemporaneous describe another region during the same years. That "
          "is the topic page's own pair of approaches, and Unit 5 Learning Objective A is "
          "what both are being used to supply."),

 dict(q="A hypothetical class proposes broad developments as context for the emergence of "
        "sectional conflict, and the tally of proposals is illustrative. Using the table, "
        "which statement is supported?",
      table=_T_TALLY,
      choices=[
        "Westward expansion was proposed by more groups than regional differences was",
        "Regional differences was proposed by more groups than westward expansion was",
        "Every group proposed the same development",
        "Political controversies and compromises was the most frequently proposed development",
        "The three named developments together were proposed by fewer groups than the "
        "unnamed proposals were"],
      ans=0,
      why="Read from the table alone: nine groups against seven, so the comparison runs one "
          "way and its reverse is false; the counts differ, so the proposals were not all "
          "the same; five is not the largest count; and the three named developments together "
          "outnumber the other proposals. KC-5.1.I's substantial migration westward and "
          "KC-5.2's deepening regional divisions are both previewed for this unit, which is "
          "why either could be offered as context under Learning Objective A."),

 dict(q="Which statement belongs to KC-5.3's account of what the war and the reconstruction "
        "left unresolved rather than to KC-5.1's account of the nation's connection with the "
        "world?",
      choices=[
        "Many questions about the power of the federal government and citizenship rights "
        "remained open",
        "The United States became more connected with the world",
        "The United States pursued an expansionist foreign policy in the Western Hemisphere",
        "The United States emerged as the destination for many migrants from other countries",
        "Popular enthusiasm for expansion resulted in new overseas initiatives"],
      ans=0,
      why="Only the first belongs to KC-5.3, which says the Union victory and the contested "
          "reconstruction left unresolved many questions about the power of the federal "
          "government and citizenship rights. The other four are KC-5.1 and KC-5.1.I, which "
          "describe the nation's growing connection with the world, its expansionist foreign "
          "policy, its emergence as a destination for migrants, and the overseas initiatives "
          "that expansion produced."),

 dict(q="Which single sentence best states the whole of what the framework previews for Unit "
        "5, without adding to it?",
      choices=[
        "Expansion connected the country with the world and brought migrants to it; expansion "
        "and deepening regional divisions carried debates over slavery into civil war; and "
        "the Union victory and a contested reconstruction settled slavery and secession while "
        "leaving questions of federal power and citizenship open",
        "The country fought a civil war over the tariff and afterwards rebuilt its economy",
        "Debates over slavery began in 1860 and were closed by the end of the fighting",
        "The period is best understood as a single sectional quarrel with no other content",
        "Expansion, industrial growth, and the rise of large firms are what define the period"],
      ans=0,
      why="The first collects KC-5.1, KC-5.2 and KC-5.3 in the order the framework prints "
          "them and adds nothing. The tariff is not what KC-5.2 names; KC-5.2.II dates the "
          "domination of political discussion to the 1850s and KC-5.3 says questions were "
          "left unresolved rather than closed; KC-5.1 gives the period content beyond the "
          "sectional quarrel; and industrial growth and large firms are KC-6.1's subject."),

 dict(q="Taken together, what does the framework's Unit 5 preview establish about the "
        "relationship between expansion and sectional conflict?",
      choices=[
        "Expansion is presented as one of the things that intensified the debates that led "
        "the nation into civil war",
        "Expansion is presented as unrelated to the debates that led the nation into civil war",
        "Expansion is presented as a consequence of the war rather than as anything preceding "
        "it",
        "Expansion is presented as having ended before the debates over slavery began",
        "Expansion is presented as the only subject the unit covers"],
      ans=0,
      why="KC-5.2 says the debates that led the nation into civil war were 'intensified by "
          "expansion and deepening regional divisions', which makes expansion one "
          "intensifying cause among others rather than the whole story or none of it. KC-5.1 "
          "and KC-5.1.I place expansion across the period rather than after the war, and "
          "KC-5.3 and KC-5.3.II.i give the unit subjects beyond expansion."),
]
