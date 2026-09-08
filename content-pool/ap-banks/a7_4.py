# AP U.S. HISTORY 7.4 The Progressives  (title copied from US_HISTORY_topics.json)
# Unit 7, Period 7: 1890 to 1945. TWO thematic focuses and TWO learning objectives are
# printed on this topic's pages: Politics and Power (PCE) with Unit 7 Learning Objective D,
# and Geography and the Environment (GEO) with Unit 7 Learning Objective E. Reasoning
# process: comparison. Suggested skill 2.C, explain the significance of a source's point of
# view, purpose, historical situation, and/or audience, including how these might limit
# the use(s) of a source.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 7 Learning Objective D
#       Compare the goals and effects of the Progressive reform movement.
#   Unit 7 Learning Objective E
#       Compare attitudes toward the use of natural resources from 1890 to 1945.
#
#   KC-7.1.II   In the Progressive Era of the early 20th century, Progressives responded
#               to political corruption, economic instability, and social concerns by
#               calling for greater government action and other political and social
#               measures.  (the concept the lettered points below sit under)
#   KC-7.1.II.A Some Progressive Era journalists attacked what they saw as political
#               corruption, social injustice, and economic inequality, while reformers,
#               often from the middle and upper classes and including many women, worked
#               to effect social changes in cities and among immigrant populations.
#   KC-7.1.II.B On the national level, Progressives sought federal legislation that they
#               believed would effectively regulate the economy, expand democracy, and
#               generate moral reform. Progressive amendments to the Constitution dealt
#               with issues such as prohibition and women's suffrage.
#   KC-7.1.II.C Preservationists and conservationists both supported the establishment of
#               national parks while advocating different government responses to the
#               overuse of natural resources.
#   KC-7.1.II.D The Progressives were divided over many issues. Some Progressives
#               supported Southern segregation, while others ignored its presence. Some
#               Progressives advocated expanding popular participation in government,
#               while others called for greater reliance on professional and technical
#               experts to make government more efficient. Progressives also disagreed
#               about immigration restriction.
#
# THE COMPARISONS THIS TOPIC IS BUILT ON, and why comparison is its reasoning process:
#   * SCALE. KC-7.1.II.A puts reformers to work in cities and among immigrant populations;
#     KC-7.1.II.B opens "On the national level". Items 6, 14 and 21 turn on that pair.
#   * DIVISION. KC-7.1.II.D says in its own first words that the Progressives were divided
#     over many issues, and then gives three of them. Items 8 through 12, 27 and 28 rest
#     on it, and the module never treats "the Progressives" as holding one view.
#   * AGREEMENT INSIDE DISAGREEMENT. KC-7.1.II.C has preservationists and conservationists
#     BOTH supporting national parks WHILE advocating different government responses to
#     overuse. Items 17, 18 and 19 carry both halves, because keeping either alone
#     misreports the sentence.
#
# TWO PLACES WHERE THE FRAMEWORK'S EXACT WORDS MATTER AND A NEAR MISS WOULD BE WRONG:
#   1. KC-7.1.II.D says some Progressives SUPPORTED Southern segregation "while others
#      IGNORED its presence". It does not say any Progressives opposed it. Item 9 keys
#      that pair as the CED states it and item 12 keys the absence; nothing here asserts
#      an opposition the framework does not record.
#   2. KC-7.1.II.B says Progressives sought legislation "that THEY BELIEVED WOULD
#      effectively regulate the economy" -- a report of what they believed, not a finding
#      that the legislation worked. Item 16 keys that distinction.
#
# WHAT IS DELIBERATELY NOT KEYED: no named Progressive, journalist, reformer, statute,
# amendment number, park, agency or court case. The CED names none of those on this page,
# and the works and figures printed under OPTIONAL SOURCES are, in its own words, not
# required course content. The response to the Great Depression is KC-7.1.III on later
# pages of this unit; item 29 keys that boundary rather than crossing it.
#
# SOURCES. The bank cannot show images, so every stimulus is an explicitly hypothetical
# textual source or a table of explicitly illustrative data whose keyed conclusion is
# recoverable from the table alone. PROSE ONLY, no LaTeX, spans written with "to".
TOPIC = ("7.4", "The Progressives", 7)

_T_DIVIDED = dict(
    headers=["Hypothetical group of Progressives (illustrative)",
             "Position on expanding popular participation in government",
             "Position on greater reliance on professional and technical experts",
             "Position on restricting immigration"],
    rows=[["Group 1", "Favours", "Opposes", "Opposes"],
          ["Group 2", "Opposes", "Favours", "Favours"],
          ["Group 3", "Favours", "Opposes", "Favours"],
          ["Group 4", "Opposes", "Favours", "Opposes"]])

_T_CONVENTION = dict(
    headers=["Proposal put to a hypothetical reform convention",
             "Delegates recorded in favour",
             "Delegates recorded against"],
    rows=[["Proposal 1", "62", "38"],
          ["Proposal 2", "55", "45"],
          ["Proposal 3", "41", "59"]])

QUESTIONS = [

 dict(q="Unit 7's Learning Objective D, printed on this topic's first page, asks students to "
        "do what?",
      choices=[
        "Compare the goals and effects of the Progressive reform movement",
        "Explain the causes of the Great Depression and its effects on the economy",
        "Explain the effects of the Spanish-American War",
        "Compare attitudes toward the use of natural resources from 1890 to 1945",
        "Explain the causes and effects of internal migration patterns over time"],
      ans=0,
      why="Unit 7 Learning Objective D reads 'Compare the goals and effects of the "
          "Progressive reform movement', and KC-7.1.II.A, KC-7.1.II.B and KC-7.1.II.D are "
          "printed under it. The fourth option is Unit 7 Learning Objective E, printed on "
          "this topic's second page with KC-7.1.II.C, and the others belong to later topics."),

 dict(q="Unit 7's Learning Objective E, printed on this topic's second page, asks students to "
        "do what?",
      choices=[
        "Compare attitudes toward the use of natural resources from 1890 to 1945",
        "Compare the goals and effects of the Progressive reform movement",
        "Compare the relative significance of the major events of the first half of the 20th "
        "century",
        "Explain how the Great Depression and the New Deal impacted American life over time",
        "Explain the similarities and differences in attitudes about the nation's proper role "
        "in the world"],
      ans=0,
      why="Unit 7 Learning Objective E reads 'Compare attitudes toward the use of natural "
          "resources from 1890 to 1945', and KC-7.1.II.C, on preservationists and "
          "conservationists, is the historical development printed under it. Unit 7 Learning "
          "Objective D is this topic's other objective, and the remaining three belong to "
          "other topics of the unit."),

 dict(q="KC-7.1.II is the key concept the lettered points on this topic's pages sit under. "
        "What does it state?",
      choices=[
        "That Progressives responded to political corruption, economic instability, and "
        "social concerns by calling for greater government action and other measures",
        "That Progressives agreed on a single programme of reform",
        "That Progressives sought to remove government from economic life",
        "That Progressive reform was confined to the national level",
        "That Progressive reform belongs to the 1930s rather than the early 20th century"],
      ans=0,
      why="KC-7.1.II states that in the Progressive Era of the early 20th century, "
          "Progressives responded to political corruption, economic instability, and social "
          "concerns by calling for greater government action and other political and social "
          "measures. KC-7.1.II.D denies the agreement in the second option, KC-7.1.II.A puts "
          "reformers to work in cities as well as nationally, and KC-7.1.III is where the "
          "framework places the 1930s."),

 dict(q="What does KC-7.1.II.A say Progressive Era journalists attacked?",
      choices=[
        "What they saw as political corruption, social injustice, and economic inequality",
        "What they saw as excessive federal regulation of business",
        "What they saw as the overuse of natural resources in the national parks",
        "What they saw as the failure of the armed forces overseas",
        "What they saw as the growth of mass culture and its effects on morals"],
      ans=0,
      why="KC-7.1.II.A states that some Progressive Era journalists attacked what they saw as "
          "political corruption, social injustice, and economic inequality. Federal "
          "regulation is what KC-7.1.II.B says Progressives SOUGHT, the overuse of natural "
          "resources belongs to KC-7.1.II.C, and mass culture to KC-7.2.I on a later topic's "
          "page."),

 dict(q="How does KC-7.1.II.A describe the reformers it names alongside those journalists?",
      choices=[
        "As often from the middle and upper classes, and as including many women",
        "As drawn almost entirely from the industrial workforce",
        "As officials appointed by the federal government",
        "As recruited from among recent immigrants themselves",
        "As a body from which women were excluded"],
      ans=0,
      why="KC-7.1.II.A describes reformers as often from the middle and upper classes and "
          "including many women. The sentence does not describe them as workers, as federal "
          "appointees or as immigrants, and 'including many women' is the opposite of "
          "excluding them."),

 dict(q="Where does KC-7.1.II.A say those reformers worked to effect social changes?",
      choices=[
        "In cities and among immigrant populations",
        "In the federal departments in Washington",
        "In rural districts and among farming families",
        "In the national parks and forest reserves",
        "In the courts, through litigation alone"],
      ans=0,
      why="KC-7.1.II.A states that reformers worked to effect social changes in cities and "
          "among immigrant populations. KC-7.1.II.B is the sentence that turns to the "
          "national level, KC-7.1.II.C to the parks, and neither rural districts nor "
          "litigation appears in KC-7.1.II.A at all."),

 dict(q="KC-7.1.II.A describes two kinds of activity in one sentence. Which pair does it "
        "describe?",
      choices=[
        "Journalists attacking what they saw as wrongs, and reformers working to effect "
        "social changes",
        "Journalists attacking wrongs, and legislators passing federal statutes",
        "Reformers working in cities, and courts striking down state laws",
        "Journalists reporting on the parks, and conservationists managing them",
        "Reformers working in cities, and immigrants organising their own associations"],
      ans=0,
      why="KC-7.1.II.A pairs journalists who attacked what they saw as political corruption, "
          "social injustice, and economic inequality with reformers who worked to effect "
          "social changes in cities and among immigrant populations. Federal legislation "
          "belongs to KC-7.1.II.B, the parks to KC-7.1.II.C, and the sentence assigns no "
          "activity to courts or to immigrant associations."),

 dict(q="How does KC-7.1.II.D open its account of the Progressives?",
      choices=[
        "By stating that the Progressives were divided over many issues",
        "By stating that the Progressives agreed on their central aims",
        "By stating that the Progressives were a single organised party",
        "By stating that Progressive divisions concerned one question only",
        "By stating that the Progressives left no record of their disagreements"],
      ans=0,
      why="KC-7.1.II.D opens 'The Progressives were divided over many issues' and then gives "
          "three of those issues: Southern segregation, popular participation against "
          "reliance on experts, and immigration restriction. Agreement, a single party, a "
          "single question and an absent record each contradict that opening or the list that "
          "follows it."),

 dict(q="What does KC-7.1.II.D state about Progressives and Southern segregation?",
      choices=[
        "That some supported it, while others ignored its presence",
        "That some supported it, while others campaigned against it",
        "That all Progressives opposed it",
        "That all Progressives supported it",
        "That the framework does not raise the question"],
      ans=0,
      why="KC-7.1.II.D states that some Progressives supported Southern segregation, while "
          "others ignored its presence. Those are the two positions the framework records; a "
          "campaign against it is not among them, and neither a uniform opposition nor a "
          "uniform support matches a sentence built on the word 'some'."),

 dict(q="Which disagreement about the machinery of government does KC-7.1.II.D record among "
        "Progressives?",
      choices=[
        "Between expanding popular participation and relying more on professional and "
        "technical experts",
        "Between expanding popular participation and abolishing elections altogether",
        "Between relying on experts and transferring government to private companies",
        "Between strengthening the states and abolishing the federal government",
        "Between reforming the courts and reforming the armed forces"],
      ans=0,
      why="KC-7.1.II.D states that some Progressives advocated expanding popular "
          "participation in government, while others called for greater reliance on "
          "professional and technical experts to make government more efficient. Abolishing "
          "elections, transferring government to companies, abolishing the federal government "
          "and reforming the armed forces are none of them in that sentence."),

 dict(q="What third disagreement does KC-7.1.II.D name among Progressives?",
      choices=[
        "Immigration restriction",
        "The establishment of national parks",
        "The declaration of war on a European power",
        "The abolition of the federal income tax",
        "The regulation of the railways"],
      ans=0,
      why="KC-7.1.II.D ends 'Progressives also disagreed about immigration restriction'. "
          "National parks are the subject of KC-7.1.II.C, where preservationists and "
          "conservationists BOTH supported them, and war, the income tax and railway "
          "regulation are not named in KC-7.1.II.D."),

 dict(q="A student writes that KC-7.1.II.D shows most Progressives worked against Southern "
        "segregation. Why does the sentence not support that?",
      choices=[
        "Because the two positions it records are supporting segregation and ignoring its "
        "presence",
        "Because it says nothing about segregation at all",
        "Because it says all Progressives supported segregation",
        "Because it places the question outside the Progressive Era",
        "Because it treats segregation as a question for the courts alone"],
      ans=0,
      why="KC-7.1.II.D records exactly two positions among Progressives on Southern "
          "segregation: some supported it, and others ignored its presence. Working against "
          "it is not one of them, so the claim adds to the framework rather than reading it. "
          "The sentence does raise the question, does not make the support universal, and "
          "sits inside KC-7.1.II's Progressive Era."),

 dict(q="According to KC-7.1.II.B, what did Progressives believe the federal legislation they "
        "sought would do?",
      choices=[
        "Effectively regulate the economy, expand democracy, and generate moral reform",
        "Reduce the role of the federal government in the economy",
        "Settle the disagreement among Progressives about immigration",
        "Establish national parks and manage the use of natural resources",
        "Prepare the country for a war in Europe"],
      ans=0,
      why="KC-7.1.II.B states that on the national level, Progressives sought federal "
          "legislation that they believed would effectively regulate the economy, expand "
          "democracy, and generate moral reform. Reducing the federal role reverses that; "
          "immigration restriction is a disagreement in KC-7.1.II.D, the parks belong to "
          "KC-7.1.II.C, and war preparation appears in neither."),

 dict(q="KC-7.1.II.B opens with the words ON THE NATIONAL LEVEL. What comparison does that "
        "phrase set up with KC-7.1.II.A?",
      choices=[
        "It marks off national legislation from the work KC-7.1.II.A places in cities and "
        "among immigrant populations",
        "It marks off national legislation from the work of journalists alone",
        "It shows that Progressive reform happened only at the national level",
        "It shows that city reform came after the federal legislation",
        "It shows that the two sentences describe the same activity twice"],
      ans=0,
      why="KC-7.1.II.A places reformers' work in cities and among immigrant populations and "
          "KC-7.1.II.B turns to what Progressives sought on the national level, so the two "
          "sentences describe reform at two scales rather than one, and neither is said to "
          "follow the other in time. Unit 7 Learning Objective D asks students to compare the "
          "goals and effects of the movement, and this is one of the comparisons available."),

 dict(q="What does KC-7.1.II.B say the Progressive amendments to the Constitution dealt with?",
      choices=[
        "Issues such as prohibition and women's suffrage",
        "Issues such as the direct regulation of the railways and the tariff",
        "Issues such as immigration restriction and Southern segregation",
        "Issues such as the establishment of national parks",
        "Issues such as the conduct of foreign policy"],
      ans=0,
      why="KC-7.1.II.B states that Progressive amendments to the Constitution dealt with "
          "issues such as prohibition and women's suffrage. Immigration restriction and "
          "Southern segregation are the disagreements of KC-7.1.II.D, the parks belong to "
          "KC-7.1.II.C, and neither the tariff nor foreign policy appears in KC-7.1.II.B."),

 dict(q="KC-7.1.II.B says Progressives sought legislation THAT THEY BELIEVED WOULD "
        "effectively regulate the economy. What does that wording report?",
      choices=[
        "What the Progressives expected of the legislation, rather than a finding that it "
        "worked",
        "A finding by the framework that the legislation regulated the economy effectively",
        "A finding by the framework that the legislation failed",
        "That the Progressives were indifferent to whether the legislation worked",
        "That the legislation was never enacted"],
      ans=0,
      why="KC-7.1.II.B attributes the expectation to the Progressives themselves with the "
          "words 'that they believed would', so the sentence reports their aim rather than "
          "grading the outcome. Reading either a success or a failure into it adds a "
          "judgement the framework does not make, and Unit 7 Learning Objective D asks "
          "students to compare goals AND effects precisely because the two are not the same."),

 dict(q="On what did preservationists and conservationists agree, according to KC-7.1.II.C?",
      choices=[
        "Both supported the establishment of national parks",
        "Both opposed the establishment of national parks",
        "Both supported leaving the use of resources to private owners",
        "Both supported the same government response to the overuse of natural resources",
        "The framework records no agreement between them"],
      ans=0,
      why="KC-7.1.II.C states that preservationists and conservationists BOTH supported the "
          "establishment of national parks while advocating different government responses to "
          "the overuse of natural resources. The parks are the agreement and the responses "
          "are the difference, so an option that makes them agree on the responses, or "
          "records no agreement at all, misstates the sentence."),

 dict(q="On what did preservationists and conservationists differ, according to KC-7.1.II.C?",
      choices=[
        "On the government response to the overuse of natural resources",
        "On whether national parks should be established at all",
        "On whether natural resources were being overused",
        "On whether the federal government existed to act in such matters",
        "On the boundaries of the parks already established"],
      ans=0,
      why="KC-7.1.II.C states that preservationists and conservationists supported the "
          "establishment of national parks WHILE ADVOCATING DIFFERENT GOVERNMENT RESPONSES to "
          "the overuse of natural resources, so the difference lies in the response. The "
          "parks are what they agreed on, and the sentence raises neither the existence of "
          "the overuse nor park boundaries as points at issue."),

 dict(q="What does KC-7.1.II.C leave a reader unable to say about preservationists and "
        "conservationists?",
      choices=[
        "What each group's preferred government response actually was",
        "Whether either group supported the establishment of national parks",
        "Whether the two groups differed at all",
        "Whether the overuse of natural resources was at issue between them",
        "Whether both groups belong to the period this unit covers"],
      ans=0,
      why="KC-7.1.II.C says the two groups advocated DIFFERENT government responses to the "
          "overuse of natural resources without stating what either response was, so that is "
          "the question the sentence leaves open. It does say both supported the "
          "establishment of national parks, that they differed, and that the overuse of "
          "resources was the subject, and Unit 7 Learning Objective E places the comparison "
          "in the years 1890 to 1945."),

 dict(q="Unit 7's Learning Objective E gives a span of years for the attitudes it asks "
        "students to compare. Which span is it?",
      choices=[
        "1890 to 1945",
        "1890 to 1920",
        "1900 to 1932",
        "1877 to 1900",
        "1945 to 1980"],
      ans=0,
      why="Unit 7 Learning Objective E reads 'Compare attitudes toward the use of natural "
          "resources from 1890 to 1945', which is the whole span of Period 7 rather than the "
          "Progressive Era alone, even though the historical development printed under it, "
          "KC-7.1.II.C, sits inside KC-7.1.II's account of that era."),

 dict(q="Which pairing correctly matches a scale of Progressive activity with the framework "
        "sentence that describes it?",
      choices=[
        "Work in cities and among immigrant populations with KC-7.1.II.A, and federal "
        "legislation with KC-7.1.II.B",
        "Work in cities and among immigrant populations with KC-7.1.II.B, and federal "
        "legislation with KC-7.1.II.A",
        "Work in cities with KC-7.1.II.C, and federal legislation with KC-7.1.II.D",
        "Both scales with KC-7.1.II.A alone",
        "Neither scale is described in the framework's sentences"],
      ans=0,
      why="KC-7.1.II.A places reformers' work in cities and among immigrant populations and "
          "KC-7.1.II.B opens 'On the national level' before naming the federal legislation "
          "Progressives sought. Reversing the pair puts each sentence's content under the "
          "other, KC-7.1.II.C concerns the parks and KC-7.1.II.D the movement's divisions."),

 dict(q="This topic's suggested skill is printed on its page. Which statement is it?",
      choices=[
        "Explain the significance of a source's point of view, purpose, historical situation, "
        "and audience, including how these might limit the uses of a source",
        "Explain the point of view, purpose, historical situation, and audience of a source",
        "Explain how a specific historical development or process is situated within a "
        "broader historical context",
        "Explain a historical concept, development, or process",
        "Explain how a historical development or process relates to another historical "
        "development or process"],
      ans=0,
      why="The suggested skill printed on this topic page is 2.C, explain the significance of "
          "a source's point of view, purpose, historical situation, and audience, including "
          "how these might limit the uses of a source. Skill 2.B, the shorter statement, is "
          "printed on topics 7.3 and 7.14; the rest are skills 4.B, 1.B and 5.B. Unit 7 "
          "Learning Objective D is the objective this skill is practised on here."),

 dict(q="Which reasoning process does the CED print on this topic's page, and what in the "
        "required content calls for it?",
      choices=[
        "Comparison, because the objectives ask students to compare goals with effects and "
        "one attitude to natural resources with another",
        "Causation, because the required content traces one chain of causes",
        "Continuity and change, because the required content follows one policy over time",
        "Contextualization, because the required content previews the whole unit",
        "Periodization, because the required content divides the era into phases"],
      ans=0,
      why="Comparison is the reasoning process printed on this topic page, and both "
          "objectives are comparative: Unit 7 Learning Objective D compares the goals and "
          "effects of the Progressive reform movement, and Unit 7 Learning Objective E "
          "compares attitudes toward the use of natural resources. KC-7.1.II.D's divisions "
          "and KC-7.1.II.C's two groups are what there is to compare."),

 dict(q="Which two thematic focuses does the CED print across this topic's pages?",
      choices=[
        "Politics and Power, and Geography and the Environment",
        "Politics and Power, and America in the World",
        "Work, Exchange, and Technology, and Social Structures",
        "Migration and Settlement, and American and Regional Culture",
        "Geography and the Environment, and America in the World"],
      ans=0,
      why="This topic's first page prints Politics and Power beside Unit 7 Learning Objective "
          "D and KC-7.1.II.A, KC-7.1.II.B and KC-7.1.II.D, and its second page prints "
          "Geography and the Environment beside Unit 7 Learning Objective E and KC-7.1.II.C. "
          "America in the World is printed on topics 7.2, 7.3, 7.5, 7.11, 7.13 and 7.14."),

 dict(q="A hypothetical unattributed report by a settlement worker, invented for this "
        "question, describes classes organised for newly arrived families in a crowded "
        "district. Which part of the framework does it most directly illustrate?",
      choices=[
        "KC-7.1.II.A's reformers working to effect social changes in cities and among "
        "immigrant populations",
        "KC-7.1.II.B's federal legislation sought on the national level",
        "KC-7.1.II.C's establishment of national parks",
        "KC-7.1.II.D's disagreement about immigration restriction",
        "KC-7.1.II's account of political corruption"],
      ans=0,
      why="KC-7.1.II.A states that reformers, often from the middle and upper classes and "
          "including many women, worked to effect social changes in cities and among "
          "immigrant populations, which is what a description of classes for newly arrived "
          "families in a crowded district shows. Federal legislation, the parks and the "
          "disagreement over restriction belong to the other three sentences."),

 dict(q="A hypothetical magazine article, offered as an illustration only, sets out at length "
        "what its writer says are corrupt dealings between a city government and a contractor. "
        "Which part of the framework does it most directly illustrate?",
      choices=[
        "KC-7.1.II.A's journalists attacking what they saw as political corruption",
        "KC-7.1.II.B's amendments dealing with prohibition and women's suffrage",
        "KC-7.1.II.C's difference between preservationists and conservationists",
        "KC-7.1.II.D's division over reliance on professional and technical experts",
        "Unit 7 Learning Objective E's comparison of attitudes to natural resources"],
      ans=0,
      why="KC-7.1.II.A states that some Progressive Era journalists attacked what they saw as "
          "political corruption, social injustice, and economic inequality, and a written "
          "attack on corrupt dealings in a city is that activity. The amendments, the two "
          "resource groups and the expert question belong to KC-7.1.II.B, KC-7.1.II.C and "
          "KC-7.1.II.D."),

 dict(q="Using the table of hypothetical Progressive groups, which conclusion does the record "
        "support?",
      table=_T_DIVIDED,
      choices=[
        "On every issue recorded, groups are found on both sides of the question",
        "The groups recorded agree on every issue",
        "The groups recorded differ on one issue only",
        "Every group recorded favours expanding popular participation in government",
        "No group recorded favours restricting immigration"],
      ans=0,
      why="Read from the table alone: each of the three issue columns carries both a Favours "
          "and an Opposes among the four groups, so no issue finds them united. That is what "
          "KC-7.1.II.D means by stating that the Progressives were divided over many issues "
          "before naming three of them."),

 dict(q="Using the table of a hypothetical reform convention, which reading matches "
        "KC-7.1.II.D?",
      table=_T_CONVENTION,
      choices=[
        "Every proposal drew both support and opposition, and the delegates did not carry "
        "them all",
        "Every proposal was carried by the delegates",
        "No proposal drew any recorded opposition",
        "The delegates divided on one proposal only",
        "Every proposal drew exactly the same division of delegates"],
      ans=0,
      why="Read from the table alone: all three proposals record delegates on both sides, the "
          "divisions are of different sizes, and one proposal draws more delegates against "
          "than for. A body divided in that way is what KC-7.1.II.D describes when it says "
          "the Progressives were divided over many issues."),

 dict(q="Which statement belongs to a LATER topic of this unit rather than to the Progressive "
        "reform this topic covers?",
      choices=[
        "Policymakers responded to the mass unemployment of the Great Depression by "
        "transforming the nation into a limited welfare state",
        "Progressives sought federal legislation on the national level",
        "Some Progressive Era journalists attacked what they saw as economic inequality",
        "Preservationists and conservationists both supported the establishment of national "
        "parks",
        "The Progressives were divided over many issues"],
      ans=0,
      why="The response to mass unemployment and the transformation into a limited welfare "
          "state is KC-7.1.III, which the CED prints on the later topics of this unit dealing "
          "with the Great Depression and the New Deal. The other four statements are "
          "KC-7.1.II.B, KC-7.1.II.A, KC-7.1.II.C and KC-7.1.II.D, all printed on this topic's "
          "pages."),

 dict(q="Taken together, what do KC-7.1.II.A through KC-7.1.II.D establish about the "
        "Progressive reform movement?",
      choices=[
        "It worked at more than one scale, sought several different ends, and was divided "
        "among itself over several questions",
        "It worked at one scale only and agreed on a single end",
        "It agreed on its ends and differed only over the means to them",
        "It confined itself to the national level and to legislation",
        "It is described by the framework without any goals being stated"],
      ans=0,
      why="KC-7.1.II.A puts journalists and reformers to work in cities and among immigrant "
          "populations, KC-7.1.II.B turns to federal legislation on the national level, "
          "KC-7.1.II.C sets preservationists beside conservationists, and KC-7.1.II.D opens "
          "by stating that the Progressives were divided over many issues. That is more than "
          "one scale, more than one end, and disagreement among themselves, which is why Unit "
          "7 Learning Objective D asks for a comparison rather than a description."),
]
