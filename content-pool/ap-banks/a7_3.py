# AP U.S. HISTORY 7.3 The Spanish-American War  (title copied from US_HISTORY_topics.json,
# where it is printed with the CED's en dash; the TOPIC tuple below carries that character
# verbatim and every mention inside a question uses an ASCII hyphen, because the bank is
# not typeset and es_check refuses non-ASCII in question text.)
# Unit 7, Period 7: 1890 to 1945. Thematic focus: America in the World (WOR). Reasoning
# process: causation. Suggested skill 2.B, explain the point of view, purpose, historical
# situation, and/or audience of a source.
#
# THE CED SENTENCE EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 7 Learning Objective C
#       Explain the effects of the Spanish-American War.
#
#   KC-7.3.I.C  The American victory in the Spanish-American War led to the U.S.
#               acquisition of island territories in the Caribbean and the Pacific, an
#               increase in involvement in Asia, and the suppression of a nationalist
#               movement in the Philippines.
#
#   KC-7.3.I    In the late 19th century and early 20th century, new U.S. territorial
#               ambitions and acquisitions in the Western Hemisphere and the Pacific
#               accompanied heightened public debates over America's role in the world.
#               (the concept KC-7.3.I.C sits under)
#
# THE WHOLE TOPIC IS ONE SENTENCE, so the discipline here is to key what that sentence
# says and to key, deliberately, what it does not. It names THREE effects and attributes
# them to the American victory. It gives no date, no battle, no campaign, no commander, no
# casualty figure, no account of the war's causes and no judgement of it. Items 9, 11, 22,
# 23 and 25 exist to hold that line; every one of them is answered by reading KC-7.3.I.C
# and finding the claim absent.
#
# SENSITIVE MATERIAL, handled as the framework handles it. KC-7.3.I.C states "the
# suppression of a nationalist movement in the Philippines" and nothing further. This bank
# repeats that and adds nothing: no invented detail of how the suppression was carried
# out, no figure, no episode. Item 22 keys precisely the gap -- that the framework asserts
# the suppression without describing it -- rather than filling it.
#
# BOUNDARIES. The ARGUMENTS for and against expansion are KC-7.3.I.A and KC-7.3.I.B, on
# topic 7.2's page; the debates of the First World War and after are KC-7.3.II, on topics
# 7.5 and 7.11. Items 13 and 24 key those boundaries rather than crossing them.
#
# SOURCES. The bank cannot show images, so every stimulus is an explicitly hypothetical
# textual source or a table of explicitly illustrative data whose keyed conclusion is
# recoverable from the table alone. Nothing is attributed to a real person or document.
# PROSE ONLY, no LaTeX, and a span of years is written with "to", never a hyphen.
TOPIC = ("7.3", "The Spanish–American War", 7)

_T_TERRITORIES = dict(
    headers=["Territory in the illustrative record",
             "Region recorded",
             "Recorded as acquired by the United States after the American victory"],
    rows=[["Territory Q", "Caribbean", "Yes"],
          ["Territory R", "Pacific", "Yes"],
          ["Territory S", "Mediterranean", "No"],
          ["Territory T", "Pacific", "Yes"]])

_T_ASIA = dict(
    headers=["Stretch of years (illustrative)",
             "U.S. merchant vessels recorded calling at Asian ports",
             "U.S. officials recorded posted to Asian ports"],
    rows=[["Stretch 1", "140", "18"],
          ["Stretch 2", "215", "29"],
          ["Stretch 3", "330", "44"]])

QUESTIONS = [

 dict(q="Unit 7's Learning Objective C, which this topic serves, asks students to explain "
        "what?",
      choices=[
        "The effects of the Spanish-American War",
        "The causes of the Spanish-American War",
        "The similarities and differences in attitudes about the nation's proper role in the "
        "world",
        "The causes and consequences of U.S. involvement in the First World War",
        "The consequences of U.S. involvement in the Second World War"],
      ans=0,
      why="Unit 7 Learning Objective C reads 'Explain the effects of the Spanish-American "
          "War', and KC-7.3.I.C, the single historical development printed under it, is a "
          "sentence about what the American victory led to. The comparison of attitudes is "
          "Unit 7 Learning Objective B's, and the two world wars belong to later objectives "
          "of this unit."),

 dict(q="Which set names the three effects KC-7.3.I.C attributes to the American victory?",
      choices=[
        "The acquisition of island territories, an increase in involvement in Asia, and the "
        "suppression of a nationalist movement in the Philippines",
        "The acquisition of island territories, the annexation of territory in Europe, and a "
        "withdrawal from Asia",
        "An increase in involvement in Asia, the reform of the tariff, and the growth of mass "
        "culture",
        "The suppression of a nationalist movement, the settlement of the western frontier, "
        "and the reduction of the navy",
        "The acquisition of island territories, an increase in migration from Asia, and the "
        "end of public debate over expansion"],
      ans=0,
      why="KC-7.3.I.C states that the American victory in the Spanish-American War led to the "
          "U.S. acquisition of island territories in the Caribbean and the Pacific, an "
          "increase in involvement in Asia, and the suppression of a nationalist movement in "
          "the Philippines. European annexation, a withdrawal from Asia, tariff reform, mass "
          "culture, frontier settlement, naval reduction, Asian migration and an end to "
          "debate are none of them in that sentence."),

 dict(q="In which regions does KC-7.3.I.C place the island territories the United States "
        "acquired?",
      choices=[
        "The Caribbean and the Pacific",
        "The Caribbean only",
        "The Pacific only",
        "The Mediterranean and the Pacific",
        "The Caribbean and the Indian Ocean"],
      ans=0,
      why="KC-7.3.I.C names the acquisition of island territories in the Caribbean AND the "
          "Pacific, so keeping only one of the two regions drops half of what the sentence "
          "says, and the Mediterranean and the Indian Ocean appear nowhere in it. KC-7.3.I "
          "makes the same pairing when it speaks of acquisitions in the Western Hemisphere "
          "and the Pacific."),

 dict(q="What does KC-7.3.I.C say happened to U.S. involvement in Asia?",
      choices=[
        "It increased",
        "It ended",
        "It was transferred to European powers",
        "It was confined to trade in a single port",
        "It stayed as it had been before the war"],
      ans=0,
      why="KC-7.3.I.C names an increase in involvement in Asia among the effects of the "
          "American victory. An end to involvement, a transfer of it, a single-port limit or "
          "no change each contradicts the direction the sentence gives, and the framework "
          "sets no limit on where in Asia that involvement grew."),

 dict(q="What does KC-7.3.I.C say happened to the nationalist movement in the Philippines?",
      choices=[
        "It was suppressed",
        "It was recognised as the government of the islands",
        "It disbanded before the American victory",
        "It was supported by the United States against Spain alone",
        "It is not mentioned by the framework"],
      ans=0,
      why="KC-7.3.I.C names the suppression of a nationalist movement in the Philippines among "
          "the effects of the American victory. The sentence neither recognises the movement "
          "as a government nor places its end before the victory, and it plainly does mention "
          "it, which is why the last option fails as well."),

 dict(q="Which way round does KC-7.3.I.C run the causation?",
      choices=[
        "The American victory led to the three effects the sentence names",
        "The three effects the sentence names brought about the American victory",
        "The victory and the effects are described as unrelated",
        "The effects are said to have preceded the war",
        "The sentence describes an intention rather than an outcome"],
      ans=0,
      why="KC-7.3.I.C opens 'The American victory in the Spanish-American War LED TO' and "
          "then lists three consequences, so the victory is the cause and the acquisitions, "
          "the increased involvement in Asia and the suppression are the effects. Unit 7 "
          "Learning Objective C asks for the EFFECTS of that war, which is the same "
          "direction."),

 dict(q="Which reasoning process does the CED print on this topic's page?",
      choices=[
        "Causation",
        "Comparison",
        "Continuity and change",
        "Contextualization",
        "Periodization"],
      ans=0,
      why="The reasoning process printed on this topic page is causation, which matches "
          "KC-7.3.I.C's structure, an American victory that LED TO three named effects, and "
          "Unit 7 Learning Objective C's demand for the effects of the war. Comparison is the "
          "process printed on topics 7.2, 7.4 and 7.11, and contextualization on topic 7.1."),

 dict(q="This topic's suggested skill is printed on its own page. Which statement is it?",
      choices=[
        "Explain the point of view, purpose, historical situation, and audience of a source",
        "Explain the significance of a source's point of view, purpose, historical situation, "
        "and audience, including how these might limit the uses of a source",
        "Explain how a historical development or process relates to another historical "
        "development or process",
        "Explain how a specific historical development or process is situated within a "
        "broader historical context",
        "Use historical reasoning to explain relationships among pieces of historical evidence"],
      ans=0,
      why="The suggested skill printed on this topic page is 2.B, explain the point of view, "
          "purpose, historical situation, and audience of a source. Skill 2.C, which adds the "
          "significance of those things and the limits they place on a source's use, is "
          "printed on topics 7.2, 7.4 and 7.5; the remaining three are skills 5.B, 4.B and "
          "6.C. Unit 7 Learning Objective C is the objective this skill is practised on."),

 dict(q="A student asks which battles KC-7.3.I.C says the American victory turned on. What is "
        "the answer?",
      choices=[
        "The sentence names no battle at all; it states a victory and three effects",
        "It names one battle in the Caribbean and one in the Pacific",
        "It names a single decisive naval battle",
        "It names the battles but not the year in which they were fought",
        "It says the war was decided without fighting"],
      ans=0,
      why="KC-7.3.I.C states that the American victory in the Spanish-American War led to the "
          "acquisition of island territories in the Caribbean and the Pacific, an increase in "
          "involvement in Asia, and the suppression of a nationalist movement in the "
          "Philippines, and it names no engagement, no commander and no date. Reading battles "
          "into it adds material the framework does not supply."),

 dict(q="A student writes that KC-7.3.I.C shows U.S. involvement in Asia began with the "
        "American victory. Why does the sentence not support that?",
      choices=[
        "Because it reports an INCREASE in involvement, which describes a change of degree "
        "rather than a beginning",
        "Because it reports a decrease in involvement in Asia",
        "Because it places U.S. involvement in Asia after 1945",
        "Because it says nothing about Asia at all",
        "Because it treats Asia as part of the Caribbean"],
      ans=0,
      why="KC-7.3.I.C names 'an increase in involvement in Asia' among the effects of the "
          "victory, and an increase is a change in how much, not a statement that there was "
          "none before. The sentence does mention Asia, does not reverse the direction and "
          "keeps Asia distinct from the Caribbean and Pacific islands it names separately."),

 dict(q="Which of the following is NOT among the effects KC-7.3.I.C names?",
      choices=[
        "The acquisition of territory on the European continent",
        "The acquisition of island territories in the Caribbean",
        "The acquisition of island territories in the Pacific",
        "An increase in involvement in Asia",
        "The suppression of a nationalist movement in the Philippines"],
      ans=0,
      why="KC-7.3.I.C names island territories in the Caribbean and the Pacific, an increase "
          "in involvement in Asia, and the suppression of a nationalist movement in the "
          "Philippines. Territory on the European continent is in neither that sentence nor "
          "KC-7.3.I, which places the period's new ambitions and acquisitions in the Western "
          "Hemisphere and the Pacific."),

 dict(q="Under which key concept does the CED print KC-7.3.I.C, and what does that placement "
        "tell a student?",
      choices=[
        "Under KC-7.3.I, so the acquisitions belong to a period of heightened public debate "
        "over America's role in the world",
        "Under KC-7.3.II, so the acquisitions belong to the First World War and its aftermath",
        "Under KC-7.1.I, so the acquisitions belong to the transition to an industrial economy",
        "Under KC-7.2.II, so the acquisitions belong to the history of migration",
        "Under no key concept, because it stands on its own"],
      ans=0,
      why="KC-7.3.I.C is a lettered sub-point of KC-7.3.I, which states that new U.S. "
          "territorial ambitions and acquisitions in the Western Hemisphere and the Pacific "
          "accompanied heightened public debates over America's role in the world. KC-7.3.II "
          "is the First World War concept, KC-7.1.I the economic transition and KC-7.2.II the "
          "migration one."),

 dict(q="Which topic of this unit, rather than this one, carries the ARGUMENTS Americans made "
        "for and against extending territory overseas?",
      choices=[
        "The topic built on KC-7.3.I.A and KC-7.3.I.B, on imperialist and anti-imperialist "
        "argument",
        "The topic built on KC-7.3.II.A, on entry into the First World War",
        "The topic built on KC-7.1.III.A, on the response to the Great Depression",
        "The topic built on KC-7.2.I.A, on new forms of mass media",
        "No topic in the unit covers those arguments"],
      ans=0,
      why="KC-7.3.I.A gives the imperialist case and KC-7.3.I.B the anti-imperialist one, and "
          "the CED prints both on the preceding topic's page, while this page carries "
          "KC-7.3.I.C and the EFFECTS of the victory that Unit 7 Learning Objective C asks "
          "about. The other options name concepts printed on later pages of the unit."),

 dict(q="A hypothetical unattributed dispatch, invented for this question, describes a new "
        "coaling station established on an island in the Pacific shortly after the American "
        "victory. Which effect named in KC-7.3.I.C does it most directly illustrate?",
      choices=[
        "The acquisition of island territories in the Pacific",
        "The suppression of a nationalist movement in the Philippines",
        "The increase in involvement in Asia, since a coaling station is an Asian port",
        "The acquisition of island territories in the Caribbean",
        "None of the effects, because the framework names no islands in the Pacific"],
      ans=0,
      why="KC-7.3.I.C names the acquisition of island territories in the Caribbean and the "
          "Pacific among the effects of the American victory, and a station on a Pacific "
          "island falls under that effect rather than under the suppression, which the "
          "sentence places in the Philippines, or the Caribbean, which is the other region "
          "named."),

 dict(q="A hypothetical petition, its author unnamed, is written by residents of an island "
        "acquired after the war and asks that they govern themselves. What does suggested "
        "skill 2.B ask a student to explain about it first?",
      choices=[
        "Its point of view, purpose, historical situation, and audience",
        "Whether the framework judges the petition to have been justified",
        "How many residents of the island signed it",
        "Which battles of the war preceded it",
        "How the petition compares with sources from the 1930s"],
      ans=0,
      why="Suggested skill 2.B, printed on this topic page, is to explain the point of view, "
          "purpose, historical situation, and audience of a source, and those four are what a "
          "student is asked to establish about any source here. KC-7.3.I.C reports the "
          "suppression of a nationalist movement in the Philippines without passing judgement, "
          "names no battle and gives no figures."),

 dict(q="A hypothetical unattributed letter to a newspaper, written to persuade readers that "
        "the new island territories should be kept, is being read for its PURPOSE. Which "
        "statement describes that purpose?",
      choices=[
        "To persuade a reading public to support retaining the territories",
        "To record for officials how many vessels called at Asian ports",
        "To report the terms on which the war ended",
        "To petition for self-government in the islands",
        "To instruct soldiers in their duties"],
      ans=0,
      why="Suggested skill 2.B asks for the purpose of a source, and a letter written to "
          "persuade readers to keep the territories has persuasion as its purpose rather than "
          "record-keeping, reporting, petitioning or instruction. KC-7.3.I.C supplies the "
          "development the letter argues about, the acquisition of island territories in the "
          "Caribbean and the Pacific."),

 dict(q="Two hypothetical sources, both invented for this question, argue for keeping the new "
        "island territories: one is a speech to a chamber of commerce, the other a sermon to a "
        "congregation. What does the difference in AUDIENCE most reasonably tell a student?",
      choices=[
        "Each was shaped for the people who would hear it, so the arguments each selects may "
        "differ even though the position is the same",
        "The two sources must make identical arguments, since their position is the same",
        "Neither source can be used, because their audiences differ",
        "The audience of a source has no bearing on the argument it makes",
        "The sermon must be the more reliable of the two"],
      ans=0,
      why="Suggested skill 2.B asks a student to explain the audience of a source, and an "
          "audience is worth explaining only because it shapes what a source says. KC-7.3.I.C "
          "gives the outcome both hypothetical sources argue about, and the framework offers "
          "no rule ranking one kind of source above another."),

 dict(q="A hypothetical unattributed report, offered as an illustration only, is dated shortly "
        "after the American victory and lists ports newly open to U.S. shipping. Which "
        "historical situation does a student place it in, using the framework?",
      choices=[
        "The increase in U.S. involvement in Asia that followed the victory",
        "The debates between imperialists and anti-imperialists before any acquisition",
        "The mobilization of American society for a world war",
        "The transformation of the nation into a limited welfare state",
        "The peak of European migration before the First World War"],
      ans=0,
      why="KC-7.3.I.C names an increase in involvement in Asia among the effects of the "
          "American victory, which is the situation a document about newly opened ports "
          "belongs to. The imperialist and anti-imperialist debates are KC-7.3.I.A and "
          "KC-7.3.I.B, and the remaining options belong to KC-7.3.III, KC-7.1.III and "
          "KC-7.2.II.A.i on other pages of the unit."),

 dict(q="Using the table of illustrative territories, which conclusion matches KC-7.3.I.C?",
      table=_T_TERRITORIES,
      choices=[
        "Every territory recorded as acquired lies in the Caribbean or the Pacific",
        "Every territory in the record was acquired by the United States",
        "The territories recorded as acquired all lie in one region",
        "One territory recorded as acquired lies outside the Caribbean and the Pacific",
        "No territory in the Pacific is recorded as acquired"],
      ans=0,
      why="Read from the table alone: three territories are marked as acquired and each of "
          "them is recorded in the Caribbean or the Pacific, while the one marked as not "
          "acquired is the one outside those regions. That is the pattern KC-7.3.I.C states "
          "when it names island territories in the Caribbean and the Pacific, and KC-7.3.I "
          "places the period's acquisitions in the Western Hemisphere and the Pacific."),

 dict(q="Using the same table of illustrative territories, which claim goes BEYOND what the "
        "record can support?",
      table=_T_TERRITORIES,
      choices=[
        "That the inhabitants of the acquired territories welcomed the change",
        "That three of the four territories are recorded as acquired",
        "That two of the recorded territories lie in the Pacific",
        "That one recorded territory lies in the Caribbean and is recorded as acquired",
        "That the territory recorded outside the Caribbean and the Pacific is not recorded as "
        "acquired"],
      ans=0,
      why="The table records a region and an acquisition mark for each territory and nothing "
          "about the people living in them, so their view is the one claim of the five it "
          "cannot reach; the other four are read directly off the rows. KC-7.3.I.C likewise "
          "reports the acquisitions and the suppression of a nationalist movement in the "
          "Philippines without reporting opinion in the territories."),

 dict(q="Using the table of illustrative Asian port records, which reading matches the effect "
        "KC-7.3.I.C names?",
      table=_T_ASIA,
      choices=[
        "Both recorded measures rise across the stretches, which is the increase in "
        "involvement the framework describes",
        "Both recorded measures fall across the stretches",
        "The vessels rise while the officials posted fall away",
        "Only vessels are recorded, and nothing about officials",
        "Neither measure changes across the stretches recorded"],
      ans=0,
      why="Read from the table alone: the recorded vessels and the recorded officials both "
          "rise at every step, and both are recorded in every stretch. Rising activity of "
          "both kinds is what KC-7.3.I.C means by an increase in involvement in Asia "
          "following the American victory."),

 dict(q="KC-7.3.I.C states the suppression of a nationalist movement in the Philippines. What "
        "does the framework supply about it, and what does it leave out?",
      choices=[
        "It states that the suppression occurred as an effect of the victory and does not "
        "describe how it was carried out",
        "It describes how the suppression was carried out and gives its duration",
        "It states that the movement was not suppressed but negotiated with",
        "It places the suppression before the American victory",
        "It attributes the suppression to a European power"],
      ans=0,
      why="KC-7.3.I.C names the suppression of a nationalist movement in the Philippines as "
          "one of three things the American victory led to, and says nothing more: no method, "
          "no duration, no episode. Reading a description into the sentence, or moving the "
          "suppression before the victory, or assigning it elsewhere, all go past what the "
          "framework states."),

 dict(q="A student concludes from KC-7.3.I.C that the framework calls the island acquisitions "
        "temporary. Why does the sentence not support that?",
      choices=[
        "Because it reports the acquisition and says nothing about how long the territories "
        "were held",
        "Because it says the territories were returned within a year",
        "Because it says the acquisitions were permanent",
        "Because it describes no acquisition at all",
        "Because it places the acquisitions in the 1930s"],
      ans=0,
      why="KC-7.3.I.C states that the American victory led to the U.S. acquisition of island "
          "territories in the Caribbean and the Pacific and gives no term for that holding, so "
          "both 'temporary' and 'permanent' add to the sentence. It plainly does describe an "
          "acquisition, and KC-7.3.I places these developments in the late 19th century and "
          "early 20th century rather than the 1930s."),

 dict(q="How do this topic's required content and the preceding topic's differ, in the "
        "framework's own terms?",
      choices=[
        "The preceding topic states what each side ARGUED, and this one states what the "
        "victory LED TO",
        "The preceding topic states what the victory led to, and this one states what each "
        "side argued",
        "Both topics state what each side argued, in different words",
        "Both topics state what the victory led to, in different words",
        "Neither topic states anything about the debate over expansion"],
      ans=0,
      why="KC-7.3.I.A and KC-7.3.I.B, on the preceding page, report what imperialists and "
          "anti-imperialists cited and argued, while KC-7.3.I.C, on this page, reports what "
          "the American victory led to. Unit 7 Learning Objective B asks for a comparison of "
          "attitudes and Unit 7 Learning Objective C for the effects of the war, so the two "
          "pages ask different questions of the same episode."),

 dict(q="A hypothetical examination question, invented for this item, asks students to explain "
        "why the war with Spain broke out. Why does that fall outside this topic's required "
        "content?",
      choices=[
        "Because Unit 7 Learning Objective C asks for the EFFECTS of the war, and KC-7.3.I.C "
        "states only what the victory led to",
        "Because the framework never mentions a war with Spain",
        "Because the causes of the war belong to Period 6 rather than Period 7",
        "Because the framework treats the war as having no effects worth study",
        "Because the question would require comparing two regions"],
      ans=0,
      why="Unit 7 Learning Objective C reads 'Explain the effects of the Spanish-American "
          "War', and the single historical development printed under it, KC-7.3.I.C, is a "
          "sentence about what the American victory led to. The framework does name the war, "
          "does place it in this unit, and gives it three effects, so the other options are "
          "false on their own terms."),

 dict(q="What does KC-7.3.I.C identify as the cause of the three developments it lists?",
      choices=[
        "The American victory in the Spanish-American War",
        "The perception that the western frontier was closed",
        "The heightened public debates over America's role in the world",
        "The transition to an urban, industrial economy",
        "The increase in involvement in Asia"],
      ans=0,
      why="KC-7.3.I.C names the American victory in the Spanish-American War as what led to "
          "the acquisitions, the increased involvement in Asia and the suppression. The "
          "closed frontier is an imperialist argument in KC-7.3.I.A, the debates are the "
          "setting KC-7.3.I describes, the economic transition is KC-7.1.I, and the increase "
          "in involvement in Asia is one of the effects rather than their cause."),

 dict(q="Which thematic focus does the CED print on this topic's page?",
      choices=[
        "America in the World, concerning interactions between empires, nations, and peoples",
        "Work, Exchange, and Technology, concerning markets, labor, and technology",
        "Politics and Power, concerning debates about the role of government",
        "American and Regional Culture, concerning creative expression and social mores",
        "Geography and the Environment, concerning competition over natural resources"],
      ans=0,
      why="The thematic focus printed on this topic page is America in the World, glossed by "
          "the CED as the diplomatic, economic, cultural, and military interactions between "
          "empires, nations, and peoples that shape America's increasingly important role in "
          "the world. KC-7.3.I.C's acquisitions and increased involvement in Asia belong to "
          "that theme; the other four are printed on other pages of this unit."),

 dict(q="A hypothetical unattributed memoir claims that the war with Spain left U.S. policy "
        "towards Asia exactly as it had been. Which framework sentence most directly "
        "contradicts it?",
      choices=[
        "KC-7.3.I.C, which names an increase in involvement in Asia among the war's effects",
        "KC-7.3.I.A, which lists what imperialists cited",
        "KC-7.3.I.B, which lists what anti-imperialists cited",
        "KC-7.3.I, which places the period's acquisitions in two regions",
        "Unit 7 Learning Objective C, which asks for the effects of the war"],
      ans=0,
      why="KC-7.3.I.C names an increase in involvement in Asia as one of the three things the "
          "American victory led to, which is exactly what a claim of no change denies. "
          "KC-7.3.I.A and KC-7.3.I.B report arguments rather than outcomes, KC-7.3.I describes "
          "the setting, and the objective states the task rather than the outcome."),

 dict(q="Which pairing correctly matches an effect in KC-7.3.I.C with the place the sentence "
        "attaches it to?",
      choices=[
        "The suppression of a nationalist movement with the Philippines, and the acquisition "
        "of island territories with the Caribbean and the Pacific",
        "The suppression of a nationalist movement with the Caribbean, and the acquisition of "
        "island territories with the Philippines",
        "The increase in involvement with the Caribbean, and the acquisitions with Asia",
        "The suppression of a nationalist movement with Asia, and the increase in involvement "
        "with the Philippines",
        "All three effects with the Pacific alone"],
      ans=0,
      why="KC-7.3.I.C attaches the acquisition of island territories to the Caribbean and the "
          "Pacific, the increase in involvement to Asia, and the suppression of a nationalist "
          "movement to the Philippines. Each of the other options moves an effect to a place "
          "the sentence attaches to a different one."),

 dict(q="Taken together, what does KC-7.3.I.C establish about the American victory?",
      choices=[
        "That a single military outcome produced consequences of more than one kind, in more "
        "than one region",
        "That a single military outcome produced consequences of one kind only",
        "That the consequences of the victory were confined to the Caribbean",
        "That the victory produced consequences only for other countries and none for the "
        "United States",
        "That the framework treats the victory as having consequences it declines to name"],
      ans=0,
      why="KC-7.3.I.C attributes three different kinds of consequence to one victory: the "
          "acquisition of island territories in the Caribbean and the Pacific, an increase in "
          "involvement in Asia, and the suppression of a nationalist movement in the "
          "Philippines. That range is why Unit 7 Learning Objective C asks for the effects in "
          "the plural, and it rules out a single kind, a single region, or an unnamed set."),
]
