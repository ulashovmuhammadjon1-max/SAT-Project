# AP U.S. HISTORY 4.2 The Rise of Political Parties and the Era of Jefferson
# (title copied from US_HISTORY_topics.json)
# Unit 4, Period 4: 1800 to 1848. Thematic focus Politics and Power (PCE).
# Suggested skill 2.A, identify a source's point of view, purpose, historical situation,
# and/or audience. Reasoning process for this topic: Causation.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 4 Learning Objective B
#       Explain the causes and effects of policy debates in the early republic.
#
#   KC-4.1.I.A    In the early 1800s, national political parties continued to debate
#                 issues such as the tariff, powers of the federal government, and
#                 relations with European powers.
#   KC-4.1.I.B    Supreme Court decisions established the primacy of the judiciary in
#                 determining the meaning of the Constitution and asserted that federal
#                 laws took precedence over state laws.
#   KC-4.3.I.A.i  Following the Louisiana Purchase, the U.S. government sought influence
#                 and control over North America through a variety of means, including
#                 exploration and diplomatic efforts.
#
#   Parent concepts printed in the unit's preview and reviewed at 4.14:
#   KC-4.1.I      The nation's transition to a more participatory democracy was achieved
#                 by expanding suffrage from a system based on property ownership to one
#                 based on voting by all adult white men, and it was accompanied by the
#                 growth of political parties.
#   KC-4.3.I      Struggling to create an independent global presence, the United States
#                 sought to claim territory throughout the North American continent and
#                 promote foreign trade.
#
#   Thematic focus PCE, Politics and Power: "Debates fostered by social and political
#   groups about the role of government in American social, political, and economic life
#   shape government policy, institutions, political parties, and the rights of citizens."
#
#   Skill 2.A: identify a source's point of view, purpose, historical situation, and/or
#   audience. Skill 2.B, printed on topics 4.3 and 4.4, is the same list under the verb
#   EXPLAIN, and the difference between the two verbs is keyed here deliberately.
#
#   Reasoning process Causation: 2.i describe causes and/or effects of a specific
#   historical development or process; 2.ii explain the relationship between causes and
#   effects; 2.iii explain the difference between primary and secondary causes and
#   between short- and long-term effects; 2.iv explain how a relevant context influenced
#   a specific historical development or process; 2.v explain the relative historical
#   significance of different causes and/or effects.
#
# WHAT IS NOT ASSERTED. The framework names the Louisiana Purchase and Supreme Court
# decisions without naming a seller, a price, a year or a case, so neither does this
# module. Nothing here rests on the author's own knowledge of the early republic; where
# the CED is silent the question is cut rather than filled in.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=,
# and every table and every source is marked hypothetical in its stem.
# PROSE ONLY: no LaTeX; a span of years is written "1800 to 1848", never with a hyphen.
TOPIC = ("4.2", "The Rise of Political Parties and the Era of Jefferson", 4)

_T_DEBATE = dict(
    headers=["Issue debated (hypothetical count of published essays)",
             "Essays published by one national party",
             "Essays published by the other national party"],
    rows=[["The tariff", "41", "37"],
          ["Powers of the federal government", "58", "52"],
          ["Relations with European powers", "33", "44"]])

_T_COURT = dict(
    headers=["Decision (hypothetical)",
             "What the dispute was about",
             "Which law the decision held to prevail"],
    rows=[["Decision 1", "A federal duty and a conflicting state duty", "The federal law"],
          ["Decision 2", "A federal licence and a conflicting state licence", "The federal law"],
          ["Decision 3", "The meaning of a clause of the Constitution", "The federal law"],
          ["Decision 4", "A federal rule and a conflicting state rule", "The federal law"]])

_T_MEANS = dict(
    headers=["Decade (hypothetical figures)",
             "Missions sent to explore the interior",
             "Missions sent to negotiate with other governments"],
    rows=[["1790 to 1800", "1", "2"],
          ["1800 to 1810", "6", "7"],
          ["1810 to 1820", "9", "11"],
          ["1820 to 1830", "14", "16"]])

QUESTIONS = [

 dict(q="Unit 4's Learning Objective B states what students should be able to explain about "
        "the early republic. Which is it?",
      choices=[
        "The causes and effects of policy debates in the early republic",
        "The similarities and differences between the two major parties of the early republic",
        "The point of view of every source produced in the early republic",
        "The extent to which the early republic resembled the colonial period",
        "The continuities in the experience of African Americans in the early republic"],
      ans=0,
      why="Unit 4 Learning Objective B reads 'Explain the causes and effects of policy debates "
          "in the early republic', which is why Causation is the reasoning process printed "
          "beside this topic. Comparison belongs to Unit 4 Learning Objective C, source "
          "analysis is a skill rather than an objective, and the continuities in the "
          "experience of African Americans are Unit 4 Learning Objective L."),

 dict(q="KC-4.1.I.A names the issues national political parties continued to debate in the "
        "early 1800s. Which set does the framework give?",
      choices=[
        "The tariff, powers of the federal government, and relations with European powers",
        "The tariff, the extension of slavery, and the size of the army",
        "Powers of the federal government, public schooling, and immigration",
        "Relations with European powers, the national census, and the postal service",
        "The tariff, powers of the federal government, and the admission of new states"],
      ans=0,
      why="KC-4.1.I.A states that in the early 1800s national political parties continued to "
          "debate issues such as the tariff, powers of the federal government, and relations "
          "with European powers. Slavery's extension is the subject of KC-4.3.II, and the "
          "army, schooling, immigration, the census, the postal service and the admission of "
          "states are not in KC-4.1.I.A's list."),

 dict(q="KC-4.1.I.A says national political parties CONTINUED to debate those issues. What "
        "does that verb establish?",
      choices=[
        "The debates carried on from before the early 1800s rather than beginning then",
        "The debates began in the early 1800s and had no earlier history",
        "The debates were settled during the early 1800s",
        "The debates were conducted only outside the parties",
        "The debates concerned only questions that were new to the republic"],
      ans=0,
      why="KC-4.1.I.A's verb CONTINUED places the debates as ongoing rather than newly begun, "
          "which is also why the framework's periodisation note says developments may begin "
          "before a period. Nothing in the sentence reports the debates being settled, and it "
          "assigns them to the national political parties themselves."),

 dict(q="According to KC-4.1.I.A, who conducted the debates it describes?",
      choices=[
        "National political parties",
        "State legislatures acting alone",
        "The federal courts",
        "Foreign governments represented in the United States",
        "Voluntary associations formed outside government"],
      ans=0,
      why="KC-4.1.I.A names national political parties as the debaters, and KC-4.1.I places "
          "the growth of those parties alongside the expansion of suffrage. Courts are the "
          "subject of KC-4.1.I.B rather than of this sentence, and voluntary associations "
          "outside government belong to KC-4.1.III.A."),

 dict(q="KC-4.1.I.B credits Supreme Court decisions with establishing a primacy. Whose "
        "primacy, and over what question?",
      choices=[
        "The primacy of the judiciary in determining the meaning of the Constitution",
        "The primacy of the legislature in determining the meaning of the Constitution",
        "The primacy of the executive in enforcing the Constitution",
        "The primacy of the states in amending the Constitution",
        "The primacy of the judiciary in collecting federal revenue"],
      ans=0,
      why="KC-4.1.I.B states that Supreme Court decisions established the primacy of the "
          "judiciary in determining the meaning of the Constitution. The sentence assigns "
          "that role to no other branch and no state, and it concerns the meaning of the "
          "Constitution rather than enforcement, amendment or revenue."),

 dict(q="KC-4.1.I.B adds a second assertion about the relationship between two bodies of law. "
        "Which does the framework state?",
      choices=[
        "That federal laws took precedence over state laws",
        "That state laws took precedence over federal laws",
        "That federal and state laws were of equal standing",
        "That federal laws applied only where a state had consented",
        "That state courts settled conflicts between the two"],
      ans=0,
      why="KC-4.1.I.B states that Supreme Court decisions asserted that federal laws took "
          "precedence over state laws. Reversing the two, making them equal, requiring state "
          "consent or transferring the question to state courts each contradict that "
          "sentence, and the same sentence gives the judiciary primacy in determining the "
          "meaning of the Constitution."),

 dict(q="A hypothetical study guide summarises KC-4.1.I.B as a statement about who enforces "
        "the Constitution. What has that summary changed?",
      choices=[
        "The sentence is about determining the Constitution's MEANING, which is "
        "interpretation rather than enforcement",
        "The sentence is about amending the Constitution rather than interpreting it",
        "The sentence concerns state courts rather than the Supreme Court",
        "The sentence concerns the tariff rather than the Constitution",
        "The sentence denies that federal law has any precedence"],
      ans=0,
      why="KC-4.1.I.B speaks of the primacy of the judiciary in DETERMINING THE MEANING of the "
          "Constitution, so the claim is about interpretation; enforcement is a different act "
          "and the sentence does not assign it. The sentence names the Supreme Court, says "
          "nothing about amendment, and asserts rather than denies the precedence of federal "
          "law. The tariff belongs to KC-4.1.I.A."),

 dict(q="KC-4.3.I.A.i describes what the U.S. government sought after a territorial "
        "acquisition. What did it seek, and where?",
      choices=[
        "Influence and control over North America, following the Louisiana Purchase",
        "Influence and control over Europe, following the Louisiana Purchase",
        "Influence and control over North America, before any territorial acquisition",
        "A withdrawal from North American affairs after the acquisition",
        "Control over the Western Hemisphere by military action alone"],
      ans=0,
      why="KC-4.3.I.A.i states that following the Louisiana Purchase the U.S. government "
          "sought influence and control over North America through a variety of means. Europe "
          "is not the object of that sentence, the acquisition precedes rather than follows "
          "the effort, and withdrawal is its negation. Control over the Western Hemisphere "
          "through means including military action is KC-4.3.I.A.ii, the subject of topic "
          "4.4."),

 dict(q="Which means does KC-4.3.I.A.i name among those the U.S. government used to seek "
        "influence and control over North America?",
      choices=[
        "Exploration and diplomatic efforts",
        "Exploration and the sale of public land",
        "Diplomatic efforts and a permanent alliance with a European power",
        "Taxation and the regulation of shipping",
        "The chartering of trading companies alone"],
      ans=0,
      why="KC-4.3.I.A.i says the government sought influence and control over North America "
          "through a variety of means, including exploration and diplomatic efforts. Land "
          "sales, permanent alliances, taxation, shipping regulation and chartered companies "
          "are not among the means that sentence names."),

 dict(q="KC-4.3.I.A.i says the government used a VARIETY of means. What does that phrase rule "
        "out?",
      choices=[
        "That the effort rested on a single instrument of policy",
        "That exploration was among the means used",
        "That diplomatic efforts were among the means used",
        "That the effort followed the Louisiana Purchase",
        "That North America was the region concerned"],
      ans=0,
      why="KC-4.3.I.A.i's phrase 'a variety of means, including exploration and diplomatic "
          "efforts' asserts more than one instrument, so a single-instrument account is what "
          "it excludes. The other four are things the same sentence states rather than "
          "excludes."),

 dict(q="How does KC-4.3.I.A.i relate to KC-4.3.I, the concept printed above it?",
      choices=[
        "KC-4.3.I states the general aim of claiming territory and promoting trade, and "
        "KC-4.3.I.A.i gives one way the government pursued it",
        "KC-4.3.I.A.i states the general aim and KC-4.3.I gives one way it was pursued",
        "The two sentences concern different periods of the course",
        "KC-4.3.I concerns domestic policy while KC-4.3.I.A.i concerns culture",
        "The two sentences make the same claim in different words"],
      ans=0,
      why="KC-4.3.I is the broader statement, that the United States sought to claim territory "
          "throughout the North American continent and promote foreign trade; KC-4.3.I.A.i "
          "sits beneath it and describes the government seeking influence and control over "
          "North America through exploration and diplomatic efforts after the Louisiana "
          "Purchase. Reversing the levels, splitting them across periods or assigning either "
          "to culture misreads the framework's own ordering."),

 dict(q="The Politics and Power thematic focus printed on this topic's page says that debates "
        "about the role of government shape four things. Which set does it name?",
      choices=[
        "Government policy, institutions, political parties, and the rights of citizens",
        "Government policy, foreign alliances, migration, and religious practice",
        "Institutions, the money supply, the census, and the rights of citizens",
        "Political parties, the size of the army, schooling, and government policy",
        "Government policy, institutions, technology, and regional identity"],
      ans=0,
      why="The Politics and Power thematic focus reads that debates fostered by social and "
          "political groups about the role of government in American social, political, and "
          "economic life shape government policy, institutions, political parties, and the "
          "rights of citizens, which is the shaping Unit 4 Learning Objective B asks students "
          "to explain for the early republic. Alliances, migration, religion, the census, "
          "the army, schooling, technology and regional identity are not in that list."),

 dict(q="Which statement is the suggested skill printed beside this topic's title?",
      choices=[
        "Identify a source's point of view, purpose, historical situation, and/or audience",
        "Explain the point of view, purpose, historical situation, and/or audience of a source",
        "Explain the significance of a source's point of view, including how it might limit "
        "the use of a source",
        "Identify the evidence used in a source to support an argument",
        "Compare the arguments or main ideas of two sources"],
      ans=0,
      why="Skill 2.A, identify a source's point of view, purpose, historical situation, and/or "
          "audience, is printed beside this topic's title and serves Unit 4 Learning "
          "Objective B. The other four are skills 2.B, 2.C, 3.B and 3.C; 2.B is printed on "
          "topics 4.3 and 4.4 and 3.B on topic 4.11."),

 dict(q="Skill 2.A and skill 2.B name the same four features of a source. What separates them?",
      choices=[
        "2.A asks the student to IDENTIFY those features and 2.B asks the student to EXPLAIN "
        "them",
        "2.A asks the student to explain those features and 2.B asks the student to identify "
        "them",
        "2.A applies to primary sources and 2.B to secondary sources",
        "2.A concerns the audience only and 2.B concerns the purpose only",
        "2.A belongs to Unit 4 and 2.B belongs to a later unit"],
      ans=0,
      why="The framework prints 2.A as 'Identify a source's point of view, purpose, historical "
          "situation, and/or audience' and 2.B as 'Explain the point of view, purpose, "
          "historical situation, and/or audience of a source', so the verb is the whole of "
          "the difference. Both skills name all four features, neither is restricted by "
          "source type, and both appear within Unit 4, 2.A here and 2.B on topics 4.3 and "
          "4.4, in service of Unit 4 Learning Objective B and its neighbours."),

 dict(q="Suppose an unattributed pamphlet, its author unnamed, argues that the powers of the "
        "federal government should be read narrowly, and addresses itself throughout to the "
        "voters of one state. Applying skill 2.A, which observation identifies the pamphlet's "
        "AUDIENCE?",
      choices=[
        "That it addresses itself to the voters of one state",
        "That it argues for reading federal power narrowly",
        "That it seeks to persuade rather than to record",
        "That it was produced while parties were debating the powers of the federal government",
        "That its author is not named"],
      ans=0,
      why="Skill 2.A distinguishes four features, and the audience is whom the source is "
          "addressed to, which here is the voters of one state. The argument for narrow "
          "federal power is its point of view, persuasion is its purpose, the ongoing party "
          "debate named in KC-4.1.I.A is its historical situation, and an unnamed author is "
          "none of the four."),

 dict(q="A hypothetical letter, its author unnamed, urges merchants to accept a restriction on "
        "trade with a European power while that restriction is in force. Applying skill 2.A, "
        "which observation identifies the letter's PURPOSE?",
      choices=[
        "That it sets out to persuade merchants to accept the restriction",
        "That it is addressed to merchants",
        "That it was written while the restriction was in force",
        "That it takes the side of the government imposing the restriction",
        "That it is a letter rather than a public speech"],
      ans=0,
      why="Under skill 2.A the purpose is what the source sets out to do, which here is to "
          "persuade merchants to accept the restriction. Being addressed to merchants is the "
          "audience, the restriction being in force is the historical situation named in "
          "KC-4.1.I.A's issue of relations with European powers, siding with the government "
          "is the point of view, and the form of the document is none of the four."),

 dict(q="An illustrative petition asks a legislature to lower a duty on imported goods, and it "
        "is submitted while the national parties are debating that duty. Applying skill 2.A, "
        "which observation identifies the petition's HISTORICAL SITUATION?",
      choices=[
        "That it was submitted while the national parties were debating the duty",
        "That it asks for the duty to be lowered",
        "That it is addressed to a legislature",
        "That it sets out to obtain a change in policy",
        "That it comes from people who pay the duty"],
      ans=0,
      why="Under skill 2.A the historical situation is the circumstances in which the source "
          "was produced, and KC-4.1.I.A places the tariff among the issues national political "
          "parties continued to debate in the early 1800s. Asking for a lower duty is the "
          "point of view, the legislature is the audience, obtaining a change is the purpose, "
          "and who the petitioners are is not one of the four features."),

 dict(q="Take an unattributed newspaper essay that praises a decision holding a federal law "
        "superior to a conflicting state law. Applying skill 2.A, which observation identifies "
        "the essay's POINT OF VIEW?",
      choices=[
        "That it approves of federal law prevailing over state law",
        "That it appeared in a newspaper",
        "That it was written after the decision was handed down",
        "That it seeks to build support for the decision",
        "That it is addressed to newspaper readers"],
      ans=0,
      why="Under skill 2.A the point of view is the position the source takes, which here is "
          "approval of the precedence KC-4.1.I.B describes, federal laws taking precedence "
          "over state laws. The form of publication is neither, the date is the historical "
          "situation, building support is the purpose, and the readership is the audience."),

 dict(q="Why does the framework treat identifying a source's point of view as different from "
        "reporting what the source says happened?",
      choices=[
        "A point of view is the position from which the source speaks, which shapes what it "
        "reports",
        "A point of view is the same thing as the source's date",
        "A point of view is the audience the source was written for",
        "A point of view can only be identified for secondary sources",
        "A point of view is whatever a later historian concludes from the source"],
      ans=0,
      why="Skill 2.A lists point of view separately from purpose, historical situation and "
          "audience, and skill 2.C asks students to explain how such features might limit the "
          "uses of a source, which only makes sense if the position a source speaks from "
          "shapes its account. The date is the historical situation and the addressee is the "
          "audience, and the framework applies the skill to primary and secondary sources "
          "alike. Unit 4 Learning Objective B is what the skill is put to work on here, the "
          "causes and effects of policy debates in the early republic."),

 dict(q="The reasoning process printed beside this topic asks students to work with causes and "
        "effects. Which process is it, and what does the framework say it involves?",
      choices=[
        "Causation, which involves describing causes and effects and explaining the "
        "relationship between them",
        "Comparison, which involves describing similarities and differences between "
        "developments",
        "Continuity and Change, which involves describing patterns over time",
        "Argumentation, which involves developing a defensible claim",
        "Contextualization, which involves situating a development in a broader context"],
      ans=0,
      why="The unit's own table prints Causation as this topic's reasoning process, matching "
          "Unit 4 Learning Objective B on the causes and effects of policy debates, and the "
          "framework defines Causation as describing causes and effects of a specific "
          "historical development or process and explaining the relationship between them. "
          "Comparison and Continuity and Change are the other two reasoning processes; "
          "argumentation and contextualization are historical thinking skills."),

 dict(q="One aspect of the Causation reasoning process asks students to draw a distinction "
        "within causes and another within effects. Which pair does the framework state?",
      choices=[
        "Primary against secondary causes, and short-term against long-term effects",
        "Political against economic causes, and domestic against foreign effects",
        "Stated against unstated causes, and intended against unintended effects",
        "Necessary against sufficient causes, and local against national effects",
        "Immediate against remote causes, and material against cultural effects"],
      ans=0,
      why="The framework's aspect 2.iii of the Causation reasoning process reads 'Explain the "
          "difference between primary and secondary causes and between short and long term "
          "effects', which is the distinction Unit 4 Learning Objective B asks students to "
          "apply to policy debates. The other four pairs are plausible distinctions the "
          "framework does not print."),

 dict(q="Another aspect of the Causation process concerns weighing one cause against another. "
        "What does the framework ask students to explain?",
      choices=[
        "The relative historical significance of different causes and effects",
        "That every cause carries the same historical significance",
        "That effects should be weighed but causes should not",
        "That significance is settled by the order in which events occurred",
        "That only causes named in a source may be weighed"],
      ans=0,
      why="Aspect 2.v of the Causation reasoning process reads 'Explain the relative "
          "historical significance of different causes and/or effects', so the framework asks "
          "for a weighing rather than treating all causes alike, and it applies that weighing "
          "to causes and effects together. Neither chronology nor the contents of a single "
          "source is offered as the test, and Unit 4 Learning Objective B asks for causes and "
          "effects of policy debates."),

 dict(q="The Causation process also asks how a relevant context influenced a development. "
        "Which statement matches that aspect as the framework prints it?",
      choices=[
        "Explain how a relevant context influenced a specific historical development or "
        "process",
        "Explain how a specific development influenced its own context",
        "Identify and describe a historical context for a development",
        "Explain how a development relates to another development",
        "Identify patterns among historical developments"],
      ans=0,
      why="Aspect 2.iv of the Causation reasoning process reads 'Explain how a relevant "
          "context influenced a specific historical development or process', with the "
          "influence running from context to development. Identifying and describing a "
          "context is skill 4.A, relating one development to another is skill 5.B, and "
          "identifying patterns is skill 5.A; Unit 4 Learning Objective B is served by the "
          "causation aspect rather than by any of those."),

 dict(q="KC-4.1.I places the growth of political parties beside another development of the "
        "same period. Which one?",
      choices=[
        "The nation's transition to a more participatory democracy through an expanded "
        "suffrage",
        "The nation's withdrawal from foreign trade",
        "The transfer of lawmaking from Congress to the states",
        "The end of debate over the powers of the federal government",
        "The replacement of elections by appointment"],
      ans=0,
      why="KC-4.1.I states that the transition to a more participatory democracy was achieved "
          "by expanding suffrage and that it was accompanied by the growth of political "
          "parties, which is the same growth KC-4.1.I.A describes at work in national policy "
          "debates. KC-4.3 records an interest in increasing foreign trade rather than a "
          "withdrawal, and the remaining options are asserted nowhere in the unit."),

 dict(q="Which of the three historical developments printed on this topic's page belongs to "
        "foreign policy rather than to domestic politics?",
      choices=[
        "The government's pursuit of influence and control over North America after a "
        "territorial acquisition",
        "The debate among national political parties over the tariff",
        "The establishment of the judiciary's primacy in reading the Constitution",
        "The assertion that federal laws took precedence over state laws",
        "The growth of political parties alongside an expanding suffrage"],
      ans=0,
      why="KC-4.3.I.A.i sits under KC-4.3, the key concept about foreign trade and national "
          "borders, and describes the government seeking influence and control over North "
          "America through exploration and diplomatic efforts. The other four come from "
          "KC-4.1.I.A, KC-4.1.I.B and KC-4.1.I, all of which concern politics and law inside "
          "the republic."),

 dict(q="A hypothetical class debate proposes that because the judiciary gained primacy in "
        "reading the Constitution, the parties stopped debating the powers of the federal "
        "government. Why do this topic's sentences not support that conclusion?",
      choices=[
        "KC-4.1.I.A has the parties continuing to debate those powers, so the framework "
        "asserts both at once",
        "KC-4.1.I.B says nothing about the Constitution",
        "The framework denies that federal law had any precedence over state law",
        "The framework places party debate after the period covered by this unit",
        "The framework treats the powers of the federal government as a settled question "
        "throughout"],
      ans=0,
      why="KC-4.1.I.B records the judiciary's primacy in determining the meaning of the "
          "Constitution and KC-4.1.I.A records national political parties continuing to "
          "debate the powers of the federal government, so the framework holds both without "
          "making one end the other. The remaining options each contradict one of those two "
          "sentences."),

 dict(q="A hypothetical count of published essays sets one national party against the other "
        "across three issues. Which conclusion do the figures support?",
      table=_T_DEBATE,
      choices=[
        "Both parties published essays on all three issues",
        "Only one of the three issues drew essays from both parties",
        "One party published no essays on any of the three issues",
        "Relations with European powers drew more essays in total than the other two issues",
        "The same party published more essays than the other on every issue"],
      ans=0,
      why="Read from the table alone: every cell holds a positive figure, so both parties "
          "published on all three issues and neither published none; relations with European "
          "powers total fewer essays than the powers of the federal government; and the "
          "second column leads on the third issue while the first column leads on the other "
          "two. That both parties argued all three is what KC-4.1.I.A describes when it says "
          "national political parties continued to debate the tariff, powers of the federal "
          "government, and relations with European powers."),

 dict(q="Suppose a register of four hypothetical decisions records what each dispute concerned "
        "and which law was held to prevail. What does the register support?",
      table=_T_COURT,
      choices=[
        "In every recorded decision the federal law was held to prevail",
        "In every recorded decision the state law was held to prevail",
        "The recorded decisions divide evenly between federal and state law",
        "Only one of the recorded disputes involved a conflict of laws",
        "Every recorded dispute concerned the same subject"],
      ans=0,
      why="Read from the table alone: the final column reads the same in all four rows and "
          "names the federal law, so the split, the reversal and any even division are false, "
          "and the middle column records four different subjects of which three are conflicts "
          "between a federal and a state measure. KC-4.1.I.B states that Supreme Court "
          "decisions asserted that federal laws took precedence over state laws."),

 dict(q="Four decades of hypothetical figures record missions sent to explore the interior "
        "beside missions sent to negotiate with other governments. Which reading do the "
        "figures support?",
      table=_T_MEANS,
      choices=[
        "Both kinds of mission increase across the four decades recorded",
        "Exploring missions increase while negotiating missions decline",
        "Negotiating missions increase while exploring missions decline",
        "Neither kind of mission changes across the four decades recorded",
        "Exploring missions outnumber negotiating missions in every decade recorded"],
      ans=0,
      why="Read from the table alone: both columns rise at every step, so neither declines and "
          "neither is unchanged, and the negotiating column is the larger in all four rows. "
          "Two kinds of mission rising together is what KC-4.3.I.A.i describes when it says "
          "the government sought influence and control over North America through a variety "
          "of means, including exploration and diplomatic efforts."),

 dict(q="Taking this topic's three historical developments together, which statement best "
        "collects what the framework asserts about the early republic?",
      choices=[
        "National parties went on debating the tariff, federal power and relations with "
        "Europe; court decisions gave the judiciary primacy in reading the Constitution and "
        "put federal law above state law; and after a territorial acquisition the government "
        "pursued influence over North America by exploration and diplomacy",
        "National parties settled their disputes, the courts withdrew from constitutional "
        "questions, and the government confined itself to the territory it already held",
        "The courts took over the debates the parties had been conducting, and foreign policy "
        "was left to the states",
        "Party debate, judicial primacy and territorial ambition each belong to a different "
        "period of the course",
        "The parties debated only foreign policy, while the courts settled every domestic "
        "question"],
      ans=0,
      why="The first collects KC-4.1.I.A, KC-4.1.I.B and KC-4.3.I.A.i in the order the topic "
          "page prints them and adds nothing to any of them. Each rejected version negates "
          "one of those sentences, moves them into other periods, or gives the courts and the "
          "states roles the framework does not."),
]
