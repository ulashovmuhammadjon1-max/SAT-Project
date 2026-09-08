# AP U.S. HISTORY 3.4 Philosophical Foundations of the American Revolution
# Title copied verbatim from US_HISTORY_topics.json. (The brief records that an earlier
# extraction produced "Philosophical American Revolution" here, because the CED prints the
# title across three lines of a narrow column with the skill statement beside it. The JSON
# has been repaired; this module trusts the JSON.)
# Unit 3, Period 3: 1754 to 1800. Suggested skill 2.B, explain the point of view, purpose,
# historical situation, and/or audience of a source. Reasoning process printed for this
# topic: Continuity and Change.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 3: Learning Objective D
#       Explain how and why colonial attitudes about government and the individual changed
#       in the years leading up to the American Revolution.
#
#   THEMATIC FOCUS: American and National Identity (NAT)
#       The development of and debates about democracy, freedom, citizenship, diversity,
#       and individualism shape American national identity, cultural values, and beliefs
#       about American exceptionalism, and in turn, these ideas shape political institutions
#       and society. Throughout American history, notions of national identity and culture
#       have coexisted with varying degrees of regional and group identities.
#
#   KC-3.2.I.A  Enlightenment ideas and philosophy inspired many American political thinkers
#               to emphasize individual talent over hereditary privilege, while religion
#               strengthened Americans' view of themselves as a people blessed with liberty.
#   KC-3.2.I.B  The colonists' belief in the superiority of republican forms of government
#               based on the natural rights of the people found expression in Thomas Paine's
#               Common Sense and the Declaration of Independence. The ideas in these
#               documents resonated throughout American history, shaping Americans'
#               understanding of the ideals on which the nation was based.
#
#   And the sentence these two sit beneath, printed in the unit's preview:
#   KC-3.2.I    The ideals that inspired the revolutionary cause reflected new beliefs about
#               politics, religion, and society that had been developing over the course of
#               the 18th century.
#
# NO INVENTED QUOTATION, AND NOT ONE LINE OF EITHER DOCUMENT. KC-3.2.I.B names Thomas
# Paine's Common Sense and the Declaration of Independence, so this module may name them --
# but HISTORY_BRIEF.md's rule bites hardest here, because a fabricated line of either would
# be read by a student as fact. Nothing in this module is presented as a quotation from
# them, or from anyone. Every source-bearing stem is an explicitly hypothetical text.
#
# WHAT IS NOT KEYED. The topic page's OPTIONAL SOURCES (a Sarah Osborn memoir, a Phillis
# Wheatley poem) are, in the CED's own words, "not required AP course content", and "None
# of the AP Exam questions require students to have studied these specific sources." No key
# here rests on either; the verifier asserts it.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table= and
# every figure in them is explicitly hypothetical, since the CED prints no data here.
# PROSE ONLY: no LaTeX; a span of years is written "1754 to 1800", never with a hyphen.
# FIVE choices (A-E).
TOPIC = ("3.4", "Philosophical Foundations of the American Revolution", 3)

_T_STRANDS = dict(
    headers=["Text in a hypothetical collection", "Draws on Enlightenment philosophy",
             "Draws on religious language"],
    rows=[["Text 1", "Yes", "No"],
          ["Text 2", "Yes", "Yes"],
          ["Text 3", "No", "Yes"],
          ["Text 4", "Yes", "Yes"]])

_T_ARGUMENTS = dict(
    headers=["Argument made in a hypothetical set of essays", "Essays in which it appears"],
    rows=[["Office should follow individual talent", "28"],
          ["Office should follow hereditary rank", "5"],
          ["Government rests on the natural rights of the people", "22"],
          ["Government rests on a ruler's inherited claim", "4"]])

_T_RESONANCE = dict(
    headers=["Later period in a hypothetical survey",
             "Public addresses invoking the ideals of the founding documents"],
    rows=[["First later period", "40"],
          ["Second later period", "55"],
          ["Third later period", "72"]])

QUESTIONS = [

 dict(q="Unit 3's Learning Objective D names two things whose treatment by colonists changed "
        "before the Revolution. Which statement gives the objective?",
      choices=[
        "Explain how and why colonial attitudes about government and the individual changed in "
        "the years leading up to the American Revolution",
        "Explain how colonial attitudes about government stayed the same across the whole "
        "colonial period",
        "Describe the philosophical writings colonists read, in the order they were published",
        "Explain how European attitudes about government changed because of the American "
        "Revolution",
        "Explain how colonial attitudes about trade and taxation changed after the Revolution"],
      ans=0,
      why="Unit 3: Learning Objective D reads 'Explain how and why colonial attitudes about "
          "government and the individual changed in the years leading up to the American "
          "Revolution.' Both subjects, government AND the individual, are in it, the direction "
          "is change rather than sameness, the attitudes are colonial rather than European, "
          "and the years are those before the Revolution rather than after it."),

 dict(q="Which skill statement is printed beside this topic's title as the one students should "
        "practise here?",
      choices=[
        "Explain the point of view, purpose, historical situation, and audience of a source",
        "Identify a source's point of view, purpose, historical situation, and audience",
        "Identify and describe a claim or argument in a source",
        "Identify the evidence used in a source to support an argument",
        "Support an argument using specific and relevant evidence"],
      ans=0,
      why="Skill 2.B, explain the point of view, purpose, historical situation, and audience of "
          "a source, is printed on this topic page beside Unit 3: Learning Objective D. Skill "
          "2.A, which asks the student only to IDENTIFY those things, is printed on a "
          "different topic of this unit, and the remaining three are skills 3.A, 3.B and 6.B."),

 dict(q="Two topics of this unit practise sourcing skills that differ by one verb. What is the "
        "difference between the skill printed here and the one printed on the taxation topic?",
      choices=[
        "This topic asks the student to EXPLAIN a source's point of view, purpose, historical "
        "situation, or audience, where the other asks only that they be IDENTIFIED",
        "This topic asks the student to IDENTIFY them, where the other asks that they be "
        "EXPLAINED",
        "The two skills name different sourcing questions from one another",
        "This topic's skill concerns arguments rather than sources",
        "The two topics print the same skill statement word for word"],
      ans=0,
      why="Skill 2.B, printed here beside Unit 3: Learning Objective D, opens with EXPLAIN, "
          "while skill 2.A, printed on the taxation topic, opens with IDENTIFY; the four "
          "sourcing questions named afterwards are the same in both. The anchor carries both "
          "halves because the leading distractor is this same distinction with the two verbs "
          "exchanged."),

 dict(q="The unit's topic table assigns each topic a reasoning process. Which does it assign "
        "here?",
      choices=[
        "Continuity and Change",
        "Causation",
        "Comparison",
        "Argumentation",
        "Sourcing and Situation"],
      ans=0,
      why="The unit's topic table assigns Continuity and Change to this topic, which matches "
          "Unit 3: Learning Objective D asking how and why colonial attitudes CHANGED, and "
          "matches KC-3.2.I's description of beliefs that had been DEVELOPING over the course "
          "of the 18th century. Causation and Comparison are assigned to other topics of this "
          "unit; the remaining two are skill categories."),

 dict(q="This topic sits under the thematic focus the framework calls American and National "
        "Identity. What does the first sentence of that focus assert?",
      choices=[
        "Debates about democracy, freedom, citizenship, diversity, and individualism shape "
        "national identity and cultural values, and those ideas in turn shape political "
        "institutions and society",
        "National identity is shaped by military and diplomatic contact with other empires and "
        "peoples",
        "National identity is shaped by the movement of people into and within America",
        "National identity is a fixed inheritance that debate does not affect",
        "Political institutions shape ideas, but ideas never shape institutions"],
      ans=0,
      why="The American and National Identity thematic focus printed on this topic page states "
          "that the development of and debates about democracy, freedom, citizenship, "
          "diversity, and individualism shape American national identity, cultural values, and "
          "beliefs about American exceptionalism, and that in turn these ideas shape political "
          "institutions and society. The influence therefore runs both ways, which is why the "
          "last two options fail, and the first two alternatives are the framework's focuses "
          "for America in the World and for migration. KC-3.2.I.A is an instance of the "
          "focus's first half, since Enlightenment ideas and religion together reshaped how "
          "colonists regarded government and the individual."),

 dict(q="The same thematic focus adds a second sentence about how national identity has stood "
        "in relation to other identities. What does it say?",
      choices=[
        "Notions of national identity and culture have coexisted with varying degrees of "
        "regional and group identities throughout American history",
        "National identity replaced regional and group identities once independence was won",
        "Regional and group identities prevented any national identity from forming",
        "National identity and regional identity have always been held in the same proportion "
        "everywhere",
        "The framework treats regional and group identities as belonging to a later period"],
      ans=0,
      why="The second sentence of the American and National Identity thematic focus reads that "
          "throughout American history, notions of national identity and culture have "
          "COEXISTED with VARYING DEGREES of regional and group identities. Coexistence rules "
          "out both replacement and prevention, and the word varying rules out a fixed "
          "proportion; the sentence covers the whole of American history rather than a later "
          "period, and Unit 3: Learning Objective D's years before the Revolution are one "
          "stretch inside that longer run."),

 dict(q="KC-3.2.I.A says Enlightenment ideas and philosophy inspired many American political "
        "thinkers to emphasize one thing over another. Which does the framework state?",
      choices=[
        "Individual talent over hereditary privilege",
        "Hereditary privilege over individual talent",
        "Established religion over private conscience",
        "Commercial wealth over landed property",
        "Military service over civil office"],
      ans=0,
      why="KC-3.2.I.A states that Enlightenment ideas and philosophy inspired many American "
          "political thinkers to emphasize individual talent OVER hereditary privilege. The "
          "anchor carries both terms in that order because the leading distractor is the same "
          "pair reversed, which is the way this clause is most easily misremembered; the other "
          "three pairs appear nowhere in the sentence."),

 dict(q="A hypothetical essay, its author unnamed, argues that offices should go to whoever "
        "can best discharge them and that the accident of a man's birth tells nothing about "
        "his fitness. Which framework claim does the essay illustrate?",
      choices=[
        "That Enlightenment ideas inspired many American political thinkers to emphasize "
        "individual talent over hereditary privilege",
        "That religion strengthened Americans' view of themselves as a people blessed with "
        "liberty",
        "That colonists believed republican government rests on the ruler's inherited claim",
        "That American political thinkers preferred hereditary privilege to individual talent",
        "That Enlightenment ideas had no effect on American political thought"],
      ans=0,
      why="KC-3.2.I.A names exactly this emphasis, individual talent over hereditary privilege, "
          "as what Enlightenment ideas and philosophy inspired in many American political "
          "thinkers. The religious strand is the OTHER half of the same sentence and concerns "
          "how Americans viewed themselves rather than how offices should be filled, and "
          "KC-3.2.I.B bases republican government on the natural rights of the people rather "
          "than on inheritance."),

 dict(q="KC-3.2.I.A gives religion a contribution of its own. What does the framework say "
        "religion did?",
      choices=[
        "It strengthened Americans' view of themselves as a people blessed with liberty",
        "It supplied the argument that individual talent should outweigh hereditary privilege",
        "It discouraged Americans from thinking of themselves as a distinct people",
        "It replaced Enlightenment philosophy in American political thought",
        "It confined American political thought to questions of church government"],
      ans=0,
      why="KC-3.2.I.A's second clause reads that religion strengthened Americans' view of "
          "themselves as a people blessed with liberty. The talent-over-privilege emphasis "
          "belongs to the sentence's FIRST clause and is credited to Enlightenment ideas, so "
          "assigning it to religion swaps the halves; the sentence has religion strengthening "
          "rather than discouraging that self-understanding, and running alongside "
          "Enlightenment philosophy rather than replacing it."),

 dict(q="How many strands of thought does KC-3.2.I.A credit with shaping colonial attitudes, "
        "and how do they stand to one another?",
      choices=[
        "Two, Enlightenment philosophy and religion, presented as working alongside each other "
        "in the same sentence",
        "One, Enlightenment philosophy, with religion mentioned only to be dismissed",
        "One, religion, with Enlightenment philosophy belonging to a later period",
        "Two, which the framework presents as alternatives, so that a thinker drew on one or "
        "the other",
        "Three, of which the framework names only two"],
      ans=0,
      why="KC-3.2.I.A joins its two clauses with WHILE: Enlightenment ideas and philosophy "
          "inspired many American political thinkers to emphasize individual talent over "
          "hereditary privilege, WHILE religion strengthened Americans' view of themselves as "
          "a people blessed with liberty. Both are asserted, neither is dismissed or deferred, "
          "and the sentence sets no bar to a thinker drawing on both."),

 dict(q="KC-3.2.I.A says Enlightenment ideas inspired MANY American political thinkers. What "
        "does that word do for the claim?",
      choices=[
        "It attributes the emphasis to a large number of thinkers without claiming every "
        "thinker held it",
        "It attributes the emphasis to every American political thinker without exception",
        "It attributes the emphasis to a handful of thinkers whose influence was slight",
        "It restricts the claim to thinkers outside the colonies",
        "It makes the number of thinkers the framework's main assertion"],
      ans=0,
      why="KC-3.2.I.A says Enlightenment ideas and philosophy inspired MANY American political "
          "thinkers, which is a claim about a large number rather than about all of them or "
          "about a slight few. The thinkers are American, and the sentence's assertion is what "
          "they emphasized, individual talent over hereditary privilege, rather than how many "
          "they were."),

 dict(q="KC-3.2.I.B describes a belief the colonists held about a form of government. What "
        "belief does the framework name?",
      choices=[
        "A belief in the superiority of republican forms of government",
        "A belief in the superiority of hereditary monarchy properly restrained",
        "A belief that no form of government is better than any other",
        "A belief that government should be conducted by the churches",
        "A belief that the colonies should be governed directly from London"],
      ans=0,
      why="KC-3.2.I.B opens with the colonists' belief in the SUPERIORITY OF REPUBLICAN FORMS "
          "OF GOVERNMENT based on the natural rights of the people. Restrained monarchy, "
          "indifference among forms, church government and direct rule from London are each "
          "incompatible with that opening clause."),

 dict(q="On what does KC-3.2.I.B say that belief in republican government was based?",
      choices=[
        "The natural rights of the people",
        "The inherited claim of a ruling family",
        "The commercial advantage of the colonies",
        "The military necessity of the moment",
        "The precedents of the colonial courts"],
      ans=0,
      why="KC-3.2.I.B specifies republican forms of government BASED ON THE NATURAL RIGHTS OF "
          "THE PEOPLE. An inherited claim is what KC-3.2.I.A's emphasis on individual talent "
          "over hereditary privilege works against, and commercial advantage, military "
          "necessity and court precedent appear nowhere in the sentence."),

 dict(q="KC-3.2.I.B names the writings in which that belief found expression. Which does the "
        "framework name?",
      choices=[
        "Thomas Paine's Common Sense and the Declaration of Independence",
        "Thomas Paine's Common Sense alone",
        "The Declaration of Independence alone",
        "A body of writing the framework leaves unnamed",
        "The state constitutions written after independence"],
      ans=0,
      why="KC-3.2.I.B says the colonists' belief found expression in Thomas Paine's Common "
          "Sense AND the Declaration of Independence, naming both together. The anchor carries "
          "both because two distractors keep one and drop the other, and the framework does "
          "name them rather than leaving the writings unspecified."),

 dict(q="KC-3.2.I.B makes a claim about how far the ideas in those documents reached in time. "
        "What does it claim?",
      choices=[
        "The ideas resonated throughout American history",
        "The ideas were confined to the years of the Revolution itself",
        "The ideas were forgotten once independence had been secured",
        "The ideas reached only the states in which the documents were printed",
        "The ideas were revived for the first time in the twentieth century"],
      ans=0,
      why="KC-3.2.I.B states that the ideas in these documents RESONATED THROUGHOUT AMERICAN "
          "HISTORY, shaping Americans' understanding of the ideals on which the nation was "
          "based. That reach in time is what rules out confinement to the Revolution, "
          "forgetting, a regional limit, or a first revival long afterwards."),

 dict(q="What does KC-3.2.I.B say the ideas in those documents did to Americans' understanding?",
      choices=[
        "They shaped Americans' understanding of the ideals on which the nation was based",
        "They shaped Americans' understanding of the boundaries the nation should claim",
        "They settled the question of who would hold office in the new governments",
        "They replaced every earlier idea about government held in the colonies",
        "They had no effect beyond the documents in which they were written"],
      ans=0,
      why="KC-3.2.I.B ends 'shaping Americans' understanding of the ideals on which the nation "
          "was based'. The sentence concerns ideals rather than boundaries or officeholding, "
          "and it describes shaping rather than wholesale replacement or no effect at all."),

 dict(q="KC-3.2.I, the sentence beneath which this topic's content sits, describes when the "
        "beliefs behind the revolutionary cause arose. What does it say?",
      choices=[
        "They were new beliefs that had been developing over the course of the 18th century",
        "They were beliefs that appeared for the first time in the year independence was "
        "declared",
        "They were unchanged inheritances in which nothing was new",
        "They were beliefs that developed only after the fighting had ended",
        "They were beliefs about military organisation rather than about politics or religion"],
      ans=0,
      why="KC-3.2.I states that the ideals that inspired the revolutionary cause reflected NEW "
          "beliefs about politics, religion, and society that HAD BEEN DEVELOPING over the "
          "course of the 18th century. Holding both words is what makes this topic's reasoning "
          "process Continuity and Change rather than causation alone, and it is why Unit 3: "
          "Learning Objective D asks about the years LEADING UP TO the Revolution."),

 dict(q="Applying the sourcing skill printed on this topic page, which statement about a "
        "hypothetical sermon explains its PURPOSE rather than its historical situation?",
      choices=[
        "It was preached in order to persuade the congregation that their liberties were a "
        "trust to be defended",
        "It was preached in a town where troops had recently been quartered",
        "It was preached in the same month that a new duty took effect",
        "It was preached during a season of poor harvests",
        "It was preached in a colony whose assembly had lately been dissolved"],
      ans=0,
      why="Skill 2.B asks the student to EXPLAIN a source's purpose, meaning the objective its "
          "creator pursued, as distinct from its historical situation, meaning what was "
          "happening at the time and place it was made. Only the first statement gives an "
          "objective; the other four describe surrounding circumstances. KC-3.2.I.A is the "
          "content such a sermon would carry, since it credits religion with strengthening "
          "Americans' view of themselves as a people blessed with liberty."),

 dict(q="Still applying that skill, which statement about a hypothetical pamphlet explains its "
        "AUDIENCE?",
      choices=[
        "It was written in plain language and sold at a price a labourer could afford",
        "Its writer had studied natural philosophy for many years",
        "It was written in the weeks after an assembly was dissolved",
        "Its writer intended to convince readers that hereditary rank was no qualification for "
        "office",
        "It was printed on a press the writer owned"],
      ans=0,
      why="Skill 2.B separates audience, meaning who the source was made for, from point of "
          "view, historical situation and purpose. Plain language at a low price identifies "
          "the readers aimed at; the other four statements give the writer's background, the "
          "moment of writing, the objective pursued, and a physical detail. KC-3.2.I.A "
          "supplies the argument such a pamphlet would be making, individual talent over "
          "hereditary privilege."),

 dict(q="A hypothetical letter, its author unnamed, tells a friend that the writer once "
        "thought rank the natural order of things and now believes it an accident of birth. "
        "Which framework claim does the change of mind illustrate?",
      choices=[
        "That colonial attitudes about government and the individual changed in the years "
        "leading up to the Revolution",
        "That colonial attitudes about government were unchanged across the century",
        "That religion discouraged Americans from thinking of themselves as a free people",
        "That the change in colonial attitudes occurred only after independence was declared",
        "That Enlightenment philosophy reached the colonies only through the state "
        "constitutions"],
      ans=0,
      why="Unit 3: Learning Objective D asks students to explain how and why colonial attitudes "
          "about government and the individual CHANGED in the years leading up to the American "
          "Revolution, and a writer abandoning rank for talent is that change in one person. "
          "KC-3.2.I.A credits Enlightenment ideas with that emphasis and religion with "
          "strengthening rather than discouraging a sense of liberty, and KC-3.2.I places the "
          "development across the 18th century rather than after independence."),

 dict(q="Using the table of texts in a hypothetical collection, what does the record show about "
        "the two strands of thought?",
      table=_T_STRANDS,
      choices=[
        "Both strands appear across the collection, and some texts draw on both at once, so "
        "they are not alternatives",
        "Every text draws on Enlightenment philosophy and none on religious language",
        "Every text draws on religious language and none on Enlightenment philosophy",
        "No text draws on both strands at once",
        "Only one text in the collection draws on either strand"],
      ans=0,
      why="Read from the table alone: both columns carry entries, neither is empty, and more "
          "than one row records both marks together. That is the arrangement KC-3.2.I.A "
          "describes, with Enlightenment ideas inspiring an emphasis on individual talent over "
          "hereditary privilege WHILE religion strengthened Americans' view of themselves as a "
          "people blessed with liberty."),

 dict(q="Using the table of arguments made in a hypothetical set of essays, which conclusion "
        "does the record support?",
      table=_T_ARGUMENTS,
      choices=[
        "Arguments from individual talent and from the natural rights of the people each "
        "appear far more often than their inherited counterparts",
        "Arguments from hereditary rank appear more often than arguments from individual talent",
        "The four arguments appear about equally often",
        "Only arguments about officeholding appear, and none about the basis of government",
        "Arguments from a ruler's inherited claim are the most common of the four"],
      ans=0,
      why="Read from the table alone: the talent tally far exceeds the hereditary-rank tally "
          "and the natural-rights tally far exceeds the inherited-claim tally, so the four are "
          "neither equal nor led by an inherited claim, and both subjects are represented. "
          "KC-3.2.I.A supplies the first pairing, individual talent over hereditary privilege, "
          "and KC-3.2.I.B the second, republican government based on the natural rights of the "
          "people."),

 dict(q="Using the table from a hypothetical survey of later periods, what does the record "
        "support about the ideals of the founding documents?",
      table=_T_RESONANCE,
      choices=[
        "They continue to be invoked in every later period recorded, and increasingly so",
        "They cease to be invoked after the first later period recorded",
        "They are invoked in only one of the later periods recorded",
        "They are invoked less often in each later period than in the one before",
        "They are invoked only in the period in which they were written"],
      ans=0,
      why="Read from the table alone: every later period records invocations, none records "
          "zero, and the counts rise at each step, so invocation neither ceases nor declines "
          "nor is confined to one period. KC-3.2.I.B says the ideas in Thomas Paine's Common "
          "Sense and the Declaration of Independence RESONATED THROUGHOUT AMERICAN HISTORY, "
          "shaping Americans' understanding of the ideals on which the nation was based, and a "
          "record of that shape is what such resonance looks like."),

 dict(q="Why does KC-3.2.I.B name particular writings rather than describing the belief alone?",
      choices=[
        "Because the framework says the belief FOUND EXPRESSION in them, which is a claim "
        "about where the belief was set down and made public",
        "Because the framework says the writings created the belief for the first time",
        "Because the framework treats the writings as the only place the belief was ever held",
        "Because the framework is describing the legal force the writings carried",
        "Because the framework needs an example of a source for the sourcing skill"],
      ans=0,
      why="KC-3.2.I.B says the colonists' belief in the superiority of republican forms of "
          "government based on the natural rights of the people FOUND EXPRESSION in Thomas "
          "Paine's Common Sense and the Declaration of Independence. Expression presupposes a "
          "belief already held, so the writings neither create it nor exhaust it, and the "
          "sentence says nothing about legal force."),

 dict(q="Which of the following does the framework NOT assert about the philosophical "
        "foundations of the Revolution?",
      choices=[
        "That religion and Enlightenment philosophy worked against one another in colonial "
        "thought",
        "That Enlightenment ideas inspired many American political thinkers",
        "That religion strengthened Americans' view of themselves as a people blessed with "
        "liberty",
        "That colonists believed republican government superior",
        "That the ideas of the founding documents resonated throughout American history"],
      ans=0,
      why="KC-3.2.I.A places Enlightenment philosophy and religion in one sentence joined by "
          "WHILE, describing two contributions running together rather than opposed, so "
          "opposition is the one claim of the five the framework does not make. The other four "
          "are stated directly in KC-3.2.I.A and KC-3.2.I.B."),

 dict(q="What did the emphasis KC-3.2.I.A describes work against, and what does that tell a "
        "student about colonial attitudes?",
      choices=[
        "It worked against hereditary privilege, so the change concerned who deserves standing "
        "as much as who should govern",
        "It worked against religious belief, so the change concerned church attendance",
        "It worked against commercial activity, so the change concerned trade",
        "It worked against local self-rule, so the change concerned the assemblies",
        "It worked against nothing in particular, since the framework names no contrast"],
      ans=0,
      why="KC-3.2.I.A sets individual talent OVER hereditary privilege, so privilege by birth "
          "is what the emphasis displaces, and the question at issue is who deserves standing "
          "and office. The same sentence credits religion with strengthening a sense of "
          "liberty rather than being opposed, and Unit 3: Learning Objective D names attitudes "
          "about government AND THE INDIVIDUAL together, which is why the contrast reaches "
          "beyond the form of government."),

 dict(q="A hypothetical almanac preface, its author unnamed, tells readers that a people who "
        "have been granted liberty hold it in trust and must prove worthy of it. Which "
        "framework claim does this best illustrate?",
      choices=[
        "That religion strengthened Americans' view of themselves as a people blessed with "
        "liberty",
        "That Enlightenment philosophy inspired an emphasis on individual talent over "
        "hereditary privilege",
        "That the colonists believed republican forms of government rest on the natural rights "
        "of the people",
        "That colonial attitudes about government did not change before the Revolution",
        "That national identity displaced every regional and group identity"],
      ans=0,
      why="KC-3.2.I.A's second clause says religion strengthened Americans' view of themselves "
          "as a people BLESSED WITH LIBERTY, and a text telling readers that their liberty is "
          "a trust to be proved worthy of is that self-understanding in religious language. "
          "The talent emphasis and the natural-rights basis are the other two claims of "
          "KC-3.2.I.A and KC-3.2.I.B, and the thematic focus on this page says national "
          "identity has coexisted with regional and group identities rather than displacing "
          "them."),

 dict(q="How does the reach KC-3.2.I.B claims for these ideas bear on the span this unit "
        "covers?",
      choices=[
        "The ideas are said to have resonated throughout American history, so their effect is "
        "not contained within 1754 to 1800",
        "The ideas are said to have been exhausted by the end of the period the unit covers",
        "The ideas are said to belong to the period after 1800 rather than to this one",
        "The ideas are said to have had no effect outside the documents themselves",
        "The framework makes no claim about how long the ideas lasted"],
      ans=0,
      why="KC-3.2.I.B says the ideas in Thomas Paine's Common Sense and the Declaration of "
          "Independence resonated THROUGHOUT AMERICAN HISTORY, shaping Americans' "
          "understanding of the ideals on which the nation was based, so their effect runs "
          "past the close of Unit 3 rather than being exhausted inside it, and the framework "
          "plainly does make a claim about their duration."),

 dict(q="Which single statement holds both halves of KC-3.2.I.A together as the framework does?",
      choices=[
        "Enlightenment philosophy pressed the claim of talent against inherited rank, while "
        "religion strengthened a sense of a people blessed with liberty",
        "Enlightenment philosophy strengthened a sense of a people blessed with liberty, while "
        "religion pressed the claim of talent against inherited rank",
        "Enlightenment philosophy and religion both pressed the claim of talent against "
        "inherited rank",
        "Enlightenment philosophy and religion both strengthened a sense of a people blessed "
        "with liberty",
        "Neither Enlightenment philosophy nor religion is credited with any effect on colonial "
        "attitudes"],
      ans=0,
      why="KC-3.2.I.A assigns the emphasis on individual talent over hereditary privilege to "
          "Enlightenment ideas and philosophy, and the strengthened view of Americans as a "
          "people blessed with liberty to religion. The anchor carries both clauses because "
          "the leading distractor is the same sentence with the two contributions exchanged, "
          "and the middle options collapse two different contributions into one."),

 dict(q="Taken together, what do this topic's sentences establish about the years before the "
        "Revolution?",
      choices=[
        "Two strands of thought, one philosophical and one religious, changed how colonists "
        "regarded government and the individual, and a belief in republican government resting "
        "on natural rights found expression in writings whose ideas outlasted the period",
        "A single philosophical school produced a belief in republican government that was "
        "forgotten once independence was won",
        "Colonial attitudes about government were settled long before this period and did not "
        "change during it",
        "Religion alone shaped colonial attitudes, and the Enlightenment reached America only "
        "afterwards",
        "The framework describes the writings of the period but makes no claim about the "
        "beliefs behind them"],
      ans=0,
      why="KC-3.2.I.A supplies the two strands and their different contributions, KC-3.2.I.B "
          "supplies the belief in republican government based on the natural rights of the "
          "people and the documents in which it found expression, and the same sentence says "
          "the ideas resonated throughout American history. Unit 3: Learning Objective D asks "
          "precisely for that change, so an account with no change, one strand, or no beliefs "
          "at all contradicts the required content."),
]
