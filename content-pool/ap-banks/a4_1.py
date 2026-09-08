# AP U.S. HISTORY 4.1 Contextualizing Period 4  (title copied from US_HISTORY_topics.json)
# Unit 4, Period 4: 1800 to 1848. Suggested skill 4.A, identify and describe a historical
# context for a specific historical development or process. Reasoning process for this
# topic: Continuity and Change.
#
# NOTE ON THE SOURCE FILE, worth keeping for the next agent. When this module was
# written `ced-source/US_HISTORY_ced.txt.gz` was not yet in the repository (the setup
# commit added the topic list and the extractor but not the dump; commit 9069f8c landed
# it afterwards), so every sentence quoted below was read from the coordinator's
# pdftotext output at /tmp/ced/US_HISTORY.txt.
#
# DO NOT `zcat ... > /tmp/apush.txt` and read that path. Sibling agents share this
# container and share /tmp, so the same command run by two agents truncates the file
# under the other one -- observed here, as a 26,553-line file that `wc -c` reported as 0
# bytes. Unzip to your own scratch directory instead.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 4 Learning Objective A
#       Explain the context in which the republic developed from 1800 to 1848.
#
#   KC-4.1     The United States began to develop a modern democracy and celebrated a
#              new national culture, while Americans sought to define the nation's
#              democratic ideals and change their society and institutions to match them.
#   KC-4.1.I   The nation's transition to a more participatory democracy was achieved by
#              expanding suffrage from a system based on property ownership to one based
#              on voting by all adult white men, and it was accompanied by the growth of
#              political parties.
#   KC-4.1.II  While Americans embraced a new national culture, various groups developed
#              distinctive cultures of their own.
#   KC-4.1.III Increasing numbers of Americans, many inspired by new religious and
#              intellectual movements, worked primarily outside of government
#              institutions to advance their ideals.
#   KC-4.2     Innovations in technology, agriculture, and commerce powerfully
#              accelerated the American economy, precipitating profound changes to U.S.
#              society and to national and regional identities.
#   KC-4.2.I   New transportation systems and technologies dramatically expanded
#              manufacturing and agricultural production.
#   KC-4.2.II  The changes caused by the market revolution had significant effects on
#              U.S. society, workers' lives, and gender and family relations.
#   KC-4.2.III Economic development shaped settlement and trade patterns, helping to
#              unify the nation while also encouraging the growth of different regions.
#   KC-4.3     The U.S. interest in increasing foreign trade and expanding its national
#              borders shaped the nation's foreign policy and spurred government and
#              private initiatives.
#   KC-4.3.I   Struggling to create an independent global presence, the United States
#              sought to claim territory throughout the North American continent and
#              promote foreign trade.
#   KC-4.3.II  The United States' acquisition of lands in the West gave rise to contests
#              over the extension of slavery into new territories.
#
#   The topic page's own instruction on what context is: students could examine "change
#   from and/or continuity with preceding historical developments" and "similarities
#   and/or differences with contemporaneous historical developments in different regions
#   or geographical areas."
#
#   The framework's periodisation note: "Events, processes, and developments are not
#   constrained by the given dates and may begin before, or continue after, the period."
#
# WHAT IS NOT KEYED, DELIBERATELY. This is a CONTEXTUALIZING topic and its Required
# Course Content is printed under the heading PREVIEW: UNIT 4 KEY CONCEPTS. The lettered
# sub-points -- KC-4.1.I.A through KC-4.3.II.C -- are printed on the pages of topics 4.2
# through 4.13, not here. So no key in this module names a party, a leader, a court
# decision, a compromise, a purchase, a machine, a route or a convention. Every key rests
# on the previewed sentences above, on the topic page's definition of context, and on the
# skill and reasoning process printed beside the title. `no_period_detail` in the verifier
# asserts that, and several items exist precisely to test the boundary.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=, and
# every table is marked hypothetical in its stem.
# PROSE ONLY: no LaTeX; a span of years is written "1800 to 1848", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("4.1", "Contextualizing Period 4", 4)

_T_SUFFRAGE = dict(
    headers=["State (hypothetical figures)",
             "Adult white men able to vote while a property test applied",
             "Adult white men able to vote after the property test was dropped"],
    rows=[["State 1", "3,100", "8,400"],
          ["State 2", "2,700", "9,100"],
          ["State 3", "4,500", "7,900"],
          ["State 4", "1,800", "6,200"]])

_T_MARKET = dict(
    headers=["Decade (hypothetical figures)",
             "Value of goods sent beyond the district where they were made",
             "Value of goods consumed in the district where they were made"],
    rows=[["1800 to 1810", "40", "160"],
          ["1810 to 1820", "70", "150"],
          ["1820 to 1830", "120", "130"],
          ["1830 to 1840", "210", "110"]])

_T_ASSOC = dict(
    headers=["Decade (hypothetical figures)",
             "Associations founded outside government institutions",
             "Bodies founded by state or federal government"],
    rows=[["1800 to 1810", "12", "9"],
          ["1810 to 1820", "31", "10"],
          ["1820 to 1830", "68", "11"],
          ["1830 to 1840", "140", "12"]])

QUESTIONS = [

 dict(q="Unit 4's Learning Objective A asks students to explain the context in which the "
        "republic developed across a stated span of years. Which span does the framework "
        "give?",
      choices=[
        "1800 to 1848",
        "1754 to 1800",
        "1844 to 1877",
        "1789 to 1840",
        "1815 to 1850"],
      ans=0,
      why="Unit 4 Learning Objective A reads 'Explain the context in which the republic "
          "developed from 1800 to 1848.' The span 1754 to 1800 is Period 3's and 1844 to "
          "1877 is Period 5's; the remaining two appear nowhere in the framework's "
          "periodisation."),

 dict(q="KC-4.1 opens the unit by naming two things the United States began to do in this "
        "period. Which pair does the framework state?",
      choices=[
        "It began to develop a modern democracy and celebrated a new national culture",
        "It began to develop a modern democracy and abandoned any distinct national culture",
        "It restricted political participation and celebrated a new national culture",
        "It replaced its constitution and adopted a single official religion",
        "It withdrew from foreign trade and concentrated on internal settlement"],
      ans=0,
      why="KC-4.1 states that the United States began to develop a modern democracy and "
          "celebrated a new national culture. Nothing in that sentence describes abandoning "
          "a national culture, restricting participation, replacing the constitution or "
          "withdrawing from trade, and KC-4.3 says the opposite of the last by naming U.S. "
          "interest in increasing foreign trade."),

 dict(q="Beyond describing what the United States began to develop, KC-4.1 adds a clause "
        "about what Americans themselves sought to do. Which is it?",
      choices=[
        "They sought to define the nation's democratic ideals and to change their society "
        "and institutions to match them",
        "They sought to define the nation's democratic ideals and to leave society and "
        "institutions as they found them",
        "They sought to adopt the institutions of other nations without alteration",
        "They sought to settle the meaning of the ideals by leaving it to the courts alone",
        "They sought to postpone any statement of national ideals until the period ended"],
      ans=0,
      why="KC-4.1 says Americans sought to define the nation's democratic ideals AND change "
          "their society and institutions to match them, so both halves belong to the "
          "sentence. Leaving institutions unaltered is the negation of the second half, and "
          "copying other nations, deferring to courts alone and postponing the ideals appear "
          "nowhere in the previewed key concepts."),

 dict(q="KC-4.1.I describes the basis on which the right to vote rested before and after the "
        "transition it names. Which direction of change does the framework state?",
      choices=[
        "From a system based on property ownership to one based on voting by all adult "
        "white men",
        "From a system based on voting by all adult white men to one based on property "
        "ownership",
        "From a system based on property ownership to one based on voting by all adult "
        "residents",
        "From a system based on religious membership to one based on property ownership",
        "From a system based on military service to one based on payment of taxes"],
      ans=0,
      why="KC-4.1.I states that the transition to a more participatory democracy was achieved "
          "by expanding suffrage from a system based on property ownership to one based on "
          "voting by all adult white men. The second option reverses the framework's own "
          "direction, and religious membership, military service and tax payment are not the "
          "bases the sentence names."),

 dict(q="According to KC-4.1.I, what accompanied the nation's transition to a more "
        "participatory democracy?",
      choices=[
        "It was accompanied by the growth of political parties",
        "It was accompanied by the disappearance of organised political competition",
        "It was accompanied by the transfer of elections to the federal courts",
        "It was accompanied by a decline in the number of offices filled by election",
        "It was accompanied by the abolition of state governments"],
      ans=0,
      why="KC-4.1.I ends by saying the transition was accompanied by the growth of political "
          "parties. Growth is the opposite of disappearance and of decline, and the sentence "
          "says nothing about courts running elections or about state governments being "
          "abolished."),

 dict(q="KC-4.1.II sets a national culture beside something else. What relationship between "
        "the two does the framework assert?",
      choices=[
        "Americans embraced a new national culture while various groups developed "
        "distinctive cultures of their own",
        "Americans embraced a new national culture that replaced every distinctive group "
        "culture",
        "Various groups developed distinctive cultures while no national culture emerged",
        "The national culture was imported whole from abroad and adopted without change",
        "Group cultures and the national culture were identical to one another"],
      ans=0,
      why="KC-4.1.II reads that WHILE Americans embraced a new national culture, various "
          "groups developed distinctive cultures of their own, so the sentence holds both at "
          "once. Replacement, the absence of a national culture and identity between the two "
          "each drop one half of it, and KC-4.1.II makes no claim that the national culture "
          "was imported whole."),

 dict(q="KC-4.1.III describes where increasing numbers of Americans did their work of "
        "advancing their ideals. Where does the framework place it?",
      choices=[
        "Primarily outside of government institutions",
        "Primarily inside state legislatures",
        "Primarily inside the federal executive departments",
        "Primarily within the courts",
        "Primarily within the armed forces"],
      ans=0,
      why="KC-4.1.III states that increasing numbers of Americans worked primarily outside of "
          "government institutions to advance their ideals. Legislatures, executive "
          "departments, courts and the armed forces are all government institutions, which "
          "is what the sentence's word 'outside' excludes."),

 dict(q="KC-4.1.III names a source of inspiration for many of the Americans it describes. "
        "Which does the framework give?",
      choices=[
        "New religious and intellectual movements",
        "New military and diplomatic successes",
        "New commercial partnerships with European states",
        "New scientific societies founded by the federal government",
        "New restrictions placed on voluntary association"],
      ans=0,
      why="KC-4.1.III says increasing numbers of Americans were many of them inspired by new "
          "religious and intellectual movements. Military success, commercial partnership, "
          "federally founded societies and restrictions on association are not in that "
          "sentence, and the last contradicts its account of Americans working outside "
          "government institutions."),

 dict(q="KC-4.2 names three fields in which innovation powerfully accelerated the American "
        "economy. Which set names all three?",
      choices=[
        "Technology, agriculture, and commerce",
        "Technology, warfare, and finance",
        "Agriculture, education, and law",
        "Commerce, medicine, and shipbuilding",
        "Technology, agriculture, and diplomacy"],
      ans=0,
      why="KC-4.2 states that innovations in technology, agriculture, and commerce powerfully "
          "accelerated the American economy. Warfare, finance, education, law, medicine, "
          "shipbuilding and diplomacy are not among the three fields that sentence names."),

 dict(q="What does KC-4.2 say the acceleration of the American economy precipitated?",
      choices=[
        "Profound changes to U.S. society and to national and regional identities",
        "Profound changes to U.S. society while identities remained fixed",
        "A uniform national identity that displaced every regional one",
        "Changes confined to the households of merchants",
        "A slowing of change in society and in identity alike"],
      ans=0,
      why="KC-4.2 says the innovations precipitated profound changes to U.S. society and to "
          "national AND regional identities, so identity is among the things changed rather "
          "than a thing left fixed, and both scales of identity are named. Confining the "
          "change to merchants or calling it a slowing contradicts the word 'profound'."),

 dict(q="KC-4.2.I attributes a dramatic expansion to new transportation systems and "
        "technologies. What does the framework say expanded?",
      choices=[
        "Manufacturing and agricultural production together",
        "Manufacturing, while agricultural production contracted",
        "Agricultural production, while manufacturing contracted",
        "Government revenue, rather than production of any kind",
        "The export trade alone, with production unchanged"],
      ans=0,
      why="KC-4.2.I states that new transportation systems and technologies dramatically "
          "expanded manufacturing and agricultural production, naming the two together. The "
          "two middle options each keep one half of the sentence and reverse the other, which "
          "is the likeliest error here, and neither government revenue nor an unchanged level "
          "of production appears in the sentence."),

 dict(q="On what does KC-4.2.II say the changes caused by the market revolution had "
        "significant effects?",
      choices=[
        "U.S. society, workers' lives, and gender and family relations",
        "U.S. society and workers' lives, but not family relations",
        "Foreign policy, military strength, and territorial claims",
        "Church membership, schooling, and the size of the electorate",
        "Regional identity alone, leaving households untouched"],
      ans=0,
      why="KC-4.2.II names significant effects on U.S. society, workers' lives, and gender and "
          "family relations. Excluding family relations drops the last item of the "
          "framework's own list; foreign policy and territorial claims belong to KC-4.3, and "
          "church membership, schooling and the electorate are not in KC-4.2.II."),

 dict(q="KC-4.2.III describes what economic development did to settlement and trade patterns. "
        "Which two-sided outcome does the framework state?",
      choices=[
        "It helped to unify the nation while also encouraging the growth of different regions",
        "It unified the nation and erased the differences between its regions",
        "It divided the nation without producing any national ties",
        "It left settlement and trade patterns as they had been",
        "It shaped trade patterns but had no effect on where people settled"],
      ans=0,
      why="KC-4.2.III says economic development shaped settlement and trade patterns, helping "
          "to unify the nation WHILE ALSO encouraging the growth of different regions, so "
          "both results are asserted at once. Erasing regional difference keeps only the "
          "first half, producing no national ties keeps only the second, and the last two "
          "deny that the sentence's subject changed anything."),

 dict(q="KC-4.3 says the nation's interest in foreign trade and in expanding its borders "
        "spurred initiatives. Whose initiatives does the framework name?",
      choices=[
        "Government and private initiatives",
        "Government initiatives only",
        "Private initiatives only",
        "Initiatives of foreign states acting in North America",
        "Initiatives of the courts interpreting treaties"],
      ans=0,
      why="KC-4.3 states that the U.S. interest in increasing foreign trade and expanding its "
          "national borders shaped the nation's foreign policy and spurred government AND "
          "private initiatives, so restricting it to either one alone drops half the "
          "sentence. Foreign states and courts are not the actors it names."),

 dict(q="KC-4.3.I opens with the phrase 'Struggling to create an independent global "
        "presence'. What does the framework say the United States sought to do?",
      choices=[
        "Claim territory throughout the North American continent and promote foreign trade",
        "Claim territory throughout the North American continent while withdrawing from "
        "foreign trade",
        "Promote foreign trade while making no territorial claims",
        "Join an existing alliance of European powers",
        "Confine its activity to the territory it already held"],
      ans=0,
      why="KC-4.3.I states that the United States sought to claim territory throughout the "
          "North American continent AND promote foreign trade, and the two middle options "
          "each keep one of those and deny the other. KC-4.3 confirms the trade half by "
          "naming U.S. interest in increasing foreign trade, so withdrawal and confinement "
          "are both excluded."),

 dict(q="KC-4.3.II names a consequence of the United States' acquisition of lands in the "
        "West. Which does the framework give?",
      choices=[
        "It gave rise to contests over the extension of slavery into new territories",
        "It settled the question of slavery for the remainder of the period",
        "It ended the nation's interest in further territorial expansion",
        "It transferred authority over new territories to foreign governments",
        "It removed the western lands from national politics"],
      ans=0,
      why="KC-4.3.II states that the acquisition of lands in the West gave rise to contests "
          "over the extension of slavery into new territories, so the question was opened "
          "rather than settled or removed from politics. KC-4.3 describes a continuing "
          "interest in expanding national borders, which rules out the third option, and no "
          "previewed sentence transfers authority to foreign governments."),

 dict(q="The topic page tells students that context can be examined in two ways. Which pair "
        "states them?",
      choices=[
        "Change from or continuity with preceding developments, and similarities or "
        "differences with contemporaneous developments in different regions",
        "Change from or continuity with later developments, and similarities or differences "
        "with developments in the same region",
        "The point of view of a source, and the audience for which it was written",
        "The relative significance of two causes, and the difference between short-term and "
        "long-term effects",
        "The evidence used in a source, and the argument that evidence supports"],
      ans=0,
      why="The topic page for Unit 4 Learning Objective A tells students they could examine "
          "change from and continuity with PRECEDING historical developments, and "
          "similarities and differences with CONTEMPORANEOUS developments in DIFFERENT "
          "regions. Later developments and the same region invert both halves; the remaining "
          "options describe skills 2.A and 2.B, the causation reasoning process, and skill "
          "3.B, none of which is the definition of context."),

 dict(q="Which statement is the suggested skill printed beside this topic's title?",
      choices=[
        "Identify and describe a historical context for a specific historical development or "
        "process",
        "Explain how a specific historical development or process is situated within a "
        "broader historical context",
        "Explain a historical concept, development, or process",
        "Explain how a historical development or process relates to another historical "
        "development or process",
        "Use historical reasoning to explain relationships among pieces of historical evidence"],
      ans=0,
      why="Skill 4.A is printed beside this topic's title, and it is the skill Unit 4 Learning "
          "Objective A asks students to apply when they explain the context in which the "
          "republic developed from 1800 to 1848. The other four are skills 4.B, 1.B, 5.B and "
          "6.C, each printed beside a different topic of this same unit."),

 dict(q="Which reasoning process does the framework print beside this topic, and what does "
        "that process ask students to do?",
      choices=[
        "Continuity and Change, which asks students to describe and explain patterns of "
        "continuity and change over time",
        "Causation, which asks students to describe causes and effects of a development",
        "Comparison, which asks students to describe similarities and differences between "
        "developments",
        "Argumentation, which asks students to develop a defensible claim",
        "Sourcing and Situation, which asks students to analyse a source's audience"],
      ans=0,
      why="The unit's own table prints Continuity and Change as the reasoning process for "
          "this topic, which Unit 4 Learning Objective A asks students to apply to the span "
          "1800 to 1848, and the framework defines that process as describing and "
          "explaining patterns of continuity and change over time. Causation and Comparison "
          "are the other two reasoning processes and belong to other topics of Unit 4; "
          "argumentation and sourcing are historical thinking skills rather than reasoning "
          "processes."),

 dict(q="The framework prints a note about the dates attached to each period. What does that "
        "note say?",
      choices=[
        "Events, processes, and developments are not constrained by the given dates and may "
        "begin before, or continue after, the period",
        "Events must be placed strictly inside the years the period names",
        "A development that begins earlier belongs to the earlier period alone",
        "The dates are fixed by law and may not be revised",
        "Only political events are bounded by the given dates"],
      ans=0,
      why="The framework's own note reads that events, processes, and developments are not "
          "constrained by the given dates and may begin before, or continue after, the "
          "period. That is the opposite of a strict boundary, and it is stated for all "
          "developments rather than for political events alone; Unit 4 Learning Objective A "
          "still gives 1800 to 1848 as the span whose context is to be explained."),

 dict(q="A hypothetical revision guide states that the Required Course Content on this topic's "
        "page supplies the detail of the period's party politics and court decisions. What is "
        "wrong with the claim?",
      choices=[
        "This page prints the unit's key concepts as a PREVIEW, and the lettered detail "
        "belongs to the later topics of the unit",
        "The framework does not cover party politics anywhere in Unit 4",
        "Party politics belongs to Period 3 rather than to Period 4",
        "The page lists no key concepts at all",
        "The framework treats party politics as context rather than as content"],
      ans=0,
      why="The heading over this topic's Required Course Content reads PREVIEW: UNIT 4 KEY "
          "CONCEPTS, and the page directs the teacher to select one or two of those concepts "
          "for which students most need context, so the lettered sub-points sit on the pages "
          "of topics 4.2 through 4.13. KC-4.1.I names the growth of political parties, so "
          "Unit 4 does cover party politics and does not defer it to Period 3, and the "
          "preview does list key concepts."),

 dict(q="Which of the following belongs to KC-4.2's account of the economy rather than to "
        "KC-4.1's account of democracy and culture?",
      choices=[
        "Innovation powerfully accelerated the American economy",
        "Suffrage was expanded from a basis in property ownership",
        "Various groups developed distinctive cultures of their own",
        "Increasing numbers of Americans worked outside government institutions",
        "The nation celebrated a new national culture"],
      ans=0,
      why="Only the first is KC-4.2, which states that innovations in technology, agriculture, "
          "and commerce powerfully accelerated the American economy. The other four are "
          "KC-4.1, KC-4.1.I, KC-4.1.II and KC-4.1.III, which concern suffrage, group cultures "
          "and work carried on outside government institutions."),

 dict(q="Which of the following belongs to KC-4.3 rather than to KC-4.1 or KC-4.2?",
      choices=[
        "An interest in increasing foreign trade and expanding national borders",
        "An expansion of manufacturing and agricultural production",
        "A transition to a more participatory democracy",
        "Significant effects on gender and family relations",
        "The growth of different regions within the nation"],
      ans=0,
      why="KC-4.3 is the key concept about the U.S. interest in increasing foreign trade and "
          "expanding its national borders. The other four come from KC-4.2.I, KC-4.1.I, "
          "KC-4.2.II and KC-4.2.III, all of which concern the domestic economy, the franchise "
          "or society rather than foreign policy and borders."),

 dict(q="A hypothetical student offers as context for this period the statement that American "
        "politics and the American economy were both settled and unchanging in these years. "
        "Why do the previewed key concepts not support it?",
      choices=[
        "Suffrage was being expanded and parties were growing, while innovation was "
        "accelerating the economy",
        "The framework says nothing about politics before 1848",
        "The framework confines all change in the period to foreign policy",
        "The framework treats the economy as unchanging but politics as changing",
        "The framework treats politics as unchanging but the economy as changing"],
      ans=0,
      why="KC-4.1.I describes suffrage expanding and political parties growing, and KC-4.2 "
          "describes innovation powerfully accelerating the American economy, so the "
          "framework asserts change in both at once. That rules out the two options that "
          "freeze one of them, and the previewed concepts cover far more than foreign "
          "policy."),

 dict(q="KC-4.1 says Americans sought to change their society and institutions to MATCH their "
        "democratic ideals. What relationship between ideals and institutions does that "
        "wording assert?",
      choices=[
        "The ideals were treated as a standard that existing society and institutions did "
        "not yet meet",
        "The ideals were drawn from institutions that already embodied them fully",
        "The ideals and the institutions were held to be one and the same thing",
        "The ideals were abandoned because institutions could not be altered",
        "The institutions were left to develop without reference to any ideal"],
      ans=0,
      why="KC-4.1 has Americans seeking to define the nation's democratic ideals and then "
          "change society and institutions TO MATCH them, which only makes sense if the "
          "institutions did not already match. Deriving the ideals from institutions that "
          "already embodied them, identifying the two, abandoning the ideals, or detaching "
          "institutions from ideals each contradict that order."),

 dict(q="KC-4.1.I describes the new basis for the franchise as voting by all adult white men. "
        "What does that phrase establish about the expansion the sentence reports?",
      choices=[
        "The wider franchise still rested on a category that excluded those who were not "
        "adult white men",
        "The wider franchise rested on no category at all",
        "The wider franchise extended to every adult resident of a state",
        "The wider franchise was narrower than the property test it replaced",
        "The wider franchise applied only to holders of property"],
      ans=0,
      why="KC-4.1.I states the new system was based on voting by all adult white men, which is "
          "a stated category rather than the whole population, so the expansion it reports "
          "had a limit written into its own definition. The framework calls the change an "
          "expansion of suffrage, which rules out its being narrower than the property test "
          "or still confined to property holders."),

 dict(q="A hypothetical register records, for four states, how many adult white men could vote "
        "while a property test applied and how many could vote after it was dropped. Which "
        "conclusion does the record support?",
      table=_T_SUFFRAGE,
      choices=[
        "The number able to vote is higher after the property test was dropped in every "
        "state recorded",
        "The number able to vote is lower after the property test was dropped in every state "
        "recorded",
        "The number able to vote is unchanged in two of the states recorded",
        "The number able to vote rises in only one of the states recorded",
        "The record shows the property test applying in only one state"],
      ans=0,
      why="Read from the table alone: in each of the four rows the second figure exceeds the "
          "first, so the count rises everywhere rather than falling, holding steady or rising "
          "once. That is the direction KC-4.1.I describes when it says suffrage was expanded "
          "from a system based on property ownership to one based on voting by all adult "
          "white men, and every row records the test applying."),

 dict(q="Four decades of hypothetical figures record the value of goods sent beyond the "
        "district where they were made against the value consumed in that same district. What "
        "do the figures support?",
      table=_T_MARKET,
      choices=[
        "The share of output leaving its own district rises in every decade recorded",
        "The share of output leaving its own district falls in every decade recorded",
        "Both columns move in the same direction across the four decades",
        "The value consumed locally exceeds the value sent away in every decade recorded",
        "Neither column changes across the four decades"],
      ans=0,
      why="Read from the table alone: the value sent away rises at every step while the value "
          "consumed locally falls at every step, so the share leaving its district rises in "
          "each decade and the two columns move in opposite directions. In the final decade "
          "the value sent away is the larger of the two. KC-4.2.III describes economic "
          "development shaping settlement and trade patterns, and KC-4.2 calls the "
          "acceleration of the economy profound."),

 dict(q="A hypothetical count sets associations founded outside government institutions "
        "against bodies founded by state or federal government across four decades. Which "
        "reading does the count support?",
      table=_T_ASSOC,
      choices=[
        "Associations founded outside government grow far faster than bodies founded by "
        "government",
        "Bodies founded by government grow far faster than associations founded outside it",
        "Associations founded outside government decline across the four decades",
        "Bodies founded by government outnumber the others in every decade recorded",
        "The two columns hold the same figure in every decade recorded"],
      ans=0,
      why="Read from the table alone: the first column rises more than tenfold across the four "
          "rows while the second rises by three, so growth outside government far outpaces "
          "growth within it, neither column declines, and the government column is the "
          "smaller in every row. KC-4.1.III states that increasing numbers of Americans "
          "worked primarily outside of government institutions to advance their ideals."),

 dict(q="Which single sentence states the whole of what the framework previews for Unit 4 "
        "without adding to it?",
      choices=[
        "A more participatory democracy and a new national culture developed alongside "
        "distinctive group cultures, innovation accelerated the economy and reshaped society "
        "and regional identity, and an interest in trade and borders shaped foreign policy "
        "and opened contests over slavery in new territory",
        "A settled political order presided over an economy that changed slowly while the "
        "nation kept clear of foreign trade",
        "Innovation in technology and commerce transformed the economy, which is the whole of "
        "what the period covers",
        "A single national culture displaced every regional and group culture as democracy "
        "widened",
        "Territorial expansion abroad proceeded without any consequence for politics or "
        "society at home"],
      ans=0,
      why="The first collects KC-4.1, KC-4.1.I, KC-4.1.II, KC-4.2, KC-4.2.III, KC-4.3 and "
          "KC-4.3.II in the order the framework prints them and adds nothing. The second "
          "contradicts KC-4.1.I and KC-4.2; the third reduces the preview to KC-4.2 alone; "
          "the fourth contradicts KC-4.1.II's distinctive group cultures; and the fifth "
          "contradicts KC-4.3.II, which makes western acquisition the origin of contests over "
          "slavery."),
]
