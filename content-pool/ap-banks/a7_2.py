# AP U.S. HISTORY 7.2 Imperialism: Debates  (title copied from US_HISTORY_topics.json)
# Unit 7, Period 7: 1890 to 1945. Thematic focus: America in the World (WOR). Reasoning
# process: comparison. Suggested skill 2.C, explain the significance of a source's point
# of view, purpose, historical situation, and/or audience, including how these might
# limit the use(s) of a source.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 7 Learning Objective B
#       Explain the similarities and differences in attitudes about the nation's proper
#       role in the world.
#
#   KC-7.3.I    In the late 19th century and early 20th century, new U.S. territorial
#               ambitions and acquisitions in the Western Hemisphere and the Pacific
#               accompanied heightened public debates over America's role in the world.
#   KC-7.3.I.A  Imperialists cited economic opportunities, racial theories, competition
#               with European empires, and the perception in the 1890s that the western
#               frontier was "closed" to argue that Americans were destined to expand
#               their culture and institutions to peoples around the globe.
#   KC-7.3.I.B  Anti-imperialists cited principles of self-determination and invoked both
#               racial theories and the U.S. foreign policy tradition of isolationism to
#               argue that the United States should not extend its territory overseas.
#
# THE COMPARISON THIS TOPIC IS BUILT ON, and the reason the reasoning process is
# comparison: RACIAL THEORIES APPEAR IN BOTH SENTENCES. KC-7.3.I.A lists them among what
# imperialists cited and KC-7.3.I.B says anti-imperialists INVOKED BOTH racial theories
# and the tradition of isolationism. So the shared element is the racial argument and the
# differences sit in what surrounds it -- economic opportunity, competition with European
# empires and the perception of a closed frontier on one side; self-determination and
# isolationism on the other. Items 7, 9, 18, 23 and 30 turn on that, and any item keyed to
# a difference has an anchor carrying both halves, because half an anchor would match the
# side it is being contrasted with.
#
# WHAT IS DELIBERATELY NOT KEYED. Nothing about the SPANISH-AMERICAN WAR or its outcome:
# that is KC-7.3.I.C and belongs to topic 7.3, and item 27 keys that boundary rather than
# crossing it. No named imperialist or anti-imperialist and no quotation from one: the
# CED prints those names only under OPTIONAL SOURCES, which its own page says are not
# required course content and which no exam question may require. Nothing is asserted
# about whether either side was right; the framework reports what each cited.
#
# SOURCES. The bank cannot show images, so every stimulus is an explicitly hypothetical
# textual source or a table of explicitly illustrative data whose keyed conclusion is
# recoverable from the table alone. Nothing is attributed to a real person or document.
# PROSE ONLY, no LaTeX, and a span of years is written with "to", never a hyphen.
TOPIC = ("7.2", "Imperialism: Debates", 7)

_T_PAMPHLETS = dict(
    headers=["Hypothetical pamphlet (illustrative)",
             "Position it argues",
             "Cites economic opportunity",
             "Invokes racial theories",
             "Cites the tradition of isolationism"],
    rows=[["Pamphlet 1", "For extending U.S. territory overseas", "Yes", "Yes", "No"],
          ["Pamphlet 2", "For extending U.S. territory overseas", "Yes", "No", "No"],
          ["Pamphlet 3", "Against extending U.S. territory overseas", "No", "Yes", "Yes"],
          ["Pamphlet 4", "Against extending U.S. territory overseas", "No", "No", "Yes"]])

_T_MEETINGS = dict(
    headers=["Stretch of years (illustrative)",
             "Public meetings recorded arguing for extending U.S. territory overseas",
             "Public meetings recorded arguing against extending U.S. territory overseas"],
    rows=[["Stretch 1", "12", "9"],
          ["Stretch 2", "20", "17"],
          ["Stretch 3", "34", "29"]])

QUESTIONS = [

 dict(q="Unit 7's Learning Objective B, which this topic serves, asks students to explain "
        "what?",
      choices=[
        "The similarities and differences in attitudes about the nation's proper role in the "
        "world",
        "The causes of the transition to an urban, industrial economy",
        "The effects of innovations in communication and technology",
        "The consequences of U.S. involvement in the Second World War",
        "The causes and effects of internal migration patterns over time"],
      ans=0,
      why="Unit 7 Learning Objective B reads 'Explain the similarities and differences in "
          "attitudes about the nation's proper role in the world.' The four other objectives "
          "belong to other topics of this unit, and the objective's pairing of similarities "
          "WITH differences is what makes comparison this topic's reasoning process."),

 dict(q="According to KC-7.3.I.A, which set of things did imperialists cite in their "
        "argument?",
      choices=[
        "Economic opportunities, racial theories, competition with European empires, and the "
        "perception that the western frontier was closed",
        "Economic opportunities, the tradition of isolationism, and principles of "
        "self-determination",
        "Religious revival, the growth of mass culture, and the reform of the tariff",
        "Competition with European empires, the abolition of standing armies, and free trade",
        "Racial theories, the growth of organised labour, and the settlement of the Pacific "
        "coast"],
      ans=0,
      why="KC-7.3.I.A states that imperialists cited economic opportunities, racial theories, "
          "competition with European empires, and the perception in the 1890s that the "
          "western frontier was closed. Isolationism and self-determination belong to "
          "KC-7.3.I.B and the anti-imperialist case, and the remaining lists name things that "
          "sentence does not."),

 dict(q="What conclusion does KC-7.3.I.A say imperialists drew from the things they cited?",
      choices=[
        "That Americans were destined to expand their culture and institutions to peoples "
        "around the globe",
        "That the United States should confine its influence to the Western Hemisphere",
        "That the United States should acquire territory only where no other empire competed",
        "That expansion should wait until the domestic economy had been reformed",
        "That Americans should adopt the institutions of the peoples they encountered"],
      ans=0,
      why="KC-7.3.I.A states that imperialists argued that Americans were destined to expand "
          "their culture and institutions to peoples around the globe. The sentence sets no "
          "regional limit, no condition about competing empires, no domestic precondition, "
          "and it runs in the opposite direction from adopting others' institutions."),

 dict(q="What principles does KC-7.3.I.B say anti-imperialists cited?",
      choices=[
        "Principles of self-determination",
        "Principles of free trade among empires",
        "Principles of religious toleration",
        "Principles of federal supremacy over the states",
        "Principles of scientific management in government"],
      ans=0,
      why="KC-7.3.I.B states that anti-imperialists cited principles of self-determination. "
          "Free trade, religious toleration, federal supremacy and scientific management are "
          "not named in that sentence, and none of them appears in KC-7.3.I.A either."),

 dict(q="KC-7.3.I.B says anti-imperialists INVOKED BOTH of two things alongside the "
        "principles they cited. Which two?",
      choices=[
        "Racial theories and the U.S. foreign policy tradition of isolationism",
        "Racial theories and the perception that the western frontier was closed",
        "The tradition of isolationism and competition with European empires",
        "Economic opportunities and the tradition of isolationism",
        "Racial theories and the economic opportunities of overseas markets"],
      ans=0,
      why="KC-7.3.I.B states that anti-imperialists invoked both racial theories and the U.S. "
          "foreign policy tradition of isolationism. The closed frontier, competition with "
          "European empires and economic opportunities all belong to KC-7.3.I.A's list of "
          "what imperialists cited, so each of the other options pairs one side's material "
          "with the other's."),

 dict(q="What did anti-imperialists argue, according to KC-7.3.I.B?",
      choices=[
        "That the United States should not extend its territory overseas",
        "That the United States should extend its territory only in the Western Hemisphere",
        "That the United States should end all commercial contact with other peoples",
        "That the United States should join a union of European empires",
        "That the United States should surrender the territory it already held"],
      ans=0,
      why="KC-7.3.I.B states that anti-imperialists argued that the United States should not "
          "extend its territory overseas. The sentence sets no regional exception, says "
          "nothing about commerce, names no union of empires, and asks for no surrender of "
          "existing territory."),

 dict(q="Which element appears in the framework's account of BOTH the imperialist and the "
        "anti-imperialist argument?",
      choices=[
        "Racial theories, cited by imperialists and invoked by anti-imperialists alike",
        "The tradition of isolationism, cited by both sides alike",
        "Competition with European empires, cited by both sides alike",
        "Principles of self-determination, cited by both sides alike",
        "No element appears in both accounts"],
      ans=0,
      why="KC-7.3.I.A lists racial theories among what imperialists cited and KC-7.3.I.B says "
          "anti-imperialists invoked BOTH racial theories and the tradition of isolationism, "
          "so the racial argument is the element the two sentences share. Isolationism and "
          "self-determination appear only in KC-7.3.I.B, and competition with European empires "
          "only in KC-7.3.I.A."),

 dict(q="Which of the following is named ONLY in the framework's account of the imperialist "
        "argument?",
      choices=[
        "Competition with European empires",
        "Racial theories",
        "The tradition of isolationism",
        "Principles of self-determination",
        "The nation's proper role in the world"],
      ans=0,
      why="KC-7.3.I.A names competition with European empires and KC-7.3.I.B does not. Racial "
          "theories appear in both sentences, isolationism and self-determination only in "
          "KC-7.3.I.B, and the nation's proper role in the world is the subject of Unit 7 "
          "Learning Objective B, which covers both sides at once."),

 dict(q="Which pair names something found only in the anti-imperialist account and something "
        "found only in the imperialist account, in that order?",
      choices=[
        "Principles of self-determination, and the perception that the western frontier was "
        "closed",
        "The perception that the western frontier was closed, and principles of "
        "self-determination",
        "Racial theories, and the tradition of isolationism",
        "Economic opportunities, and competition with European empires",
        "The tradition of isolationism, and principles of self-determination"],
      ans=0,
      why="KC-7.3.I.B names principles of self-determination and KC-7.3.I.A names the "
          "perception in the 1890s that the western frontier was closed, so that pair runs "
          "anti-imperialist first and imperialist second. Reversing the order, or pairing two "
          "items from the same sentence, or naming racial theories, which both sentences "
          "carry, fails the test the question sets."),

 dict(q="How does KC-7.3.I.A describe the closed western frontier of the 1890s?",
      choices=[
        "As a perception that imperialists cited in argument",
        "As a fact the framework establishes about land settlement",
        "As a policy adopted by the federal government",
        "As an argument used only by anti-imperialists",
        "As a consequence of overseas expansion"],
      ans=0,
      why="KC-7.3.I.A names 'the perception in the 1890s that the western frontier was "
          "closed' among the things imperialists cited, so the framework reports it as a "
          "perception used in argument rather than asserting it as a settled fact, a policy, "
          "or a consequence. KC-7.3.I.B does not mention it at all."),

 dict(q="What does the framework say about which side of the debate was right?",
      choices=[
        "Nothing; KC-7.3.I.A and KC-7.3.I.B report what each side cited and argued",
        "That the imperialist argument was the sounder of the two",
        "That the anti-imperialist argument was the sounder of the two",
        "That both arguments were rejected by the public at the time",
        "That the question was settled before the debates began"],
      ans=0,
      why="KC-7.3.I.A and KC-7.3.I.B each state what a side cited and what it argued, and "
          "neither endorses a side, and KC-7.3.I frames the whole as heightened public "
          "debates over America's role in the world. Unit 7 Learning Objective B asks for "
          "similarities and differences in attitudes, which is a comparison rather than a "
          "verdict."),

 dict(q="According to KC-7.3.I, what accompanied the new U.S. territorial ambitions and "
        "acquisitions of the late 19th century and early 20th century?",
      choices=[
        "Heightened public debates over America's role in the world",
        "A public consensus in favour of expansion",
        "The end of public discussion of foreign policy",
        "A reduction in U.S. involvement in the Pacific",
        "The transfer of foreign policy to the state governments"],
      ans=0,
      why="KC-7.3.I states that new U.S. territorial ambitions and acquisitions in the "
          "Western Hemisphere and the Pacific accompanied heightened public debates over "
          "America's role in the world, and KC-7.3.I.A and KC-7.3.I.B are the two sides of "
          "exactly those debates. A consensus, or an end to discussion, is what heightened "
          "debate rules out."),

 dict(q="A hypothetical unattributed account of a public meeting records a speaker arguing "
        "that the United States must take markets abroad before rival empires close them off. "
        "Which side of the debate does that argument belong to, and on what ground?",
      choices=[
        "The imperialist side, because it joins economic opportunity to competition with "
        "European empires",
        "The anti-imperialist side, because it appeals to self-determination",
        "The anti-imperialist side, because it appeals to the tradition of isolationism",
        "Neither side, because the framework records no economic argument in this debate",
        "Both sides equally, because economic argument was common to them"],
      ans=0,
      why="KC-7.3.I.A names economic opportunities and competition with European empires "
          "among the things imperialists cited, and the hypothetical speaker joins exactly "
          "those two. KC-7.3.I.B's anti-imperialists cited self-determination and invoked "
          "racial theories and isolationism, none of which the speaker uses, and economic "
          "opportunity appears in only one of the two sentences."),

 dict(q="A hypothetical pamphlet, its author unnamed, argues against extending U.S. territory "
        "overseas on the ground that no people should be governed without its own consent. "
        "Which part of the framework does that argument match?",
      choices=[
        "KC-7.3.I.B's principles of self-determination",
        "KC-7.3.I.A's perception of a closed western frontier",
        "KC-7.3.I.A's competition with European empires",
        "KC-7.3.I's account of new territorial acquisitions",
        "Unit 7 Learning Objective B's requirement to compare attitudes"],
      ans=0,
      why="KC-7.3.I.B states that anti-imperialists cited principles of self-determination to "
          "argue that the United States should not extend its territory overseas, and "
          "governing no people without its own consent is that principle. The closed frontier "
          "and competition with European empires are imperialist material in KC-7.3.I.A, and "
          "the remaining two options describe the acquisitions and the objective rather than "
          "an argument."),

 dict(q="A hypothetical pamphlet invokes racial theories. Why is that alone not enough to "
        "identify which side of the debate it argues for?",
      choices=[
        "Because the framework records racial theories as cited by imperialists and invoked by "
        "anti-imperialists as well",
        "Because the framework says racial theories were used by neither side",
        "Because racial theories were used only after the debates had ended",
        "Because the framework treats racial theories as a form of economic argument",
        "Because a pamphlet is never evidence of the argument it makes"],
      ans=0,
      why="KC-7.3.I.A lists racial theories among what imperialists cited and KC-7.3.I.B says "
          "anti-imperialists invoked both racial theories and the tradition of isolationism, "
          "so the same kind of argument appears on both sides and cannot by itself place a "
          "source. Suggested skill 2.C is about reading a source's argument carefully enough "
          "to see what it does and does not settle."),

 dict(q="This topic's suggested skill is printed on its own page. Which statement is it?",
      choices=[
        "Explain the significance of a source's point of view, purpose, historical situation, "
        "and audience, including how these might limit the uses of a source",
        "Explain how a specific historical development or process is situated within a "
        "broader historical context",
        "Explain how a historical development or process relates to another historical "
        "development or process",
        "Explain a historical concept, development, or process",
        "Corroborate, qualify, or modify an argument using diverse and alternative evidence"],
      ans=0,
      why="The suggested skill printed on this topic page is 2.C, explain the significance of "
          "a source's point of view, purpose, historical situation, and audience, including "
          "how these might limit the uses of a source. It is the skill Unit 7 Learning "
          "Objective B's comparison of attitudes calls for; the other four are skills 4.B, "
          "5.B, 1.B and 6.D from other pages of this unit."),

 dict(q="A hypothetical campaign speech, invented for this question, is delivered by a "
        "candidate seeking election in a district whose factories sell abroad. How does that "
        "purpose most reasonably limit the use a historian can make of it?",
      choices=[
        "It shows what an argument for expansion sounded like to a voting audience, but not "
        "how widely that argument was held",
        "It shows nothing about the debate, because a candidate has an interest in the "
        "outcome",
        "It settles the question of how many Americans favoured expansion",
        "It proves that economic opportunity was the only argument used for expansion",
        "It proves that anti-imperialists made no economic argument at all"],
      ans=0,
      why="Suggested skill 2.C asks how a source's purpose and audience limit its uses, and a "
          "speech made to win votes evidences the argument being offered rather than its "
          "reach. KC-7.3.I.A names economic opportunities as one of four things imperialists "
          "cited, not the only one, and KC-7.3.I frames the period as one of heightened "
          "public debates rather than a measured distribution of opinion."),

 dict(q="Using the table of hypothetical pamphlets, which conclusion does the record support?",
      table=_T_PAMPHLETS,
      choices=[
        "Racial theories are invoked by pamphlets arguing on both sides of the question",
        "Racial theories are invoked only by the pamphlets arguing for extending territory",
        "The tradition of isolationism is cited by pamphlets on both sides",
        "Economic opportunity is cited by pamphlets on both sides",
        "Every pamphlet in the record invokes racial theories"],
      ans=0,
      why="Read from the table alone: one pamphlet on each side is marked as invoking racial "
          "theories, while economic opportunity is marked only on the side arguing for "
          "extension and isolationism only on the side arguing against. That is the pattern "
          "KC-7.3.I.A and KC-7.3.I.B state together, since racial theories are the one element "
          "both sentences carry, and two of the four pamphlets do not invoke them at all."),

 dict(q="Using the same table of hypothetical pamphlets, which claim goes BEYOND what the "
        "record can support?",
      table=_T_PAMPHLETS,
      choices=[
        "That the pamphlets arguing for extension were more widely read than those arguing "
        "against",
        "That two of the four pamphlets argue for extending U.S. territory overseas",
        "That economic opportunity is cited only by pamphlets arguing for extension",
        "That isolationism is cited only by pamphlets arguing against extension",
        "That one pamphlet on each side invokes racial theories"],
      ans=0,
      why="The table records the position and the arguments of each pamphlet and nothing "
          "about circulation or readership, so relative reach is the one claim of the five it "
          "cannot reach; the other four are read directly off the rows. KC-7.3.I.A and "
          "KC-7.3.I.B likewise state what each side cited without asserting how widely either "
          "case was received, and suggested skill 2.C is about exactly that limit on a "
          "source's use."),

 dict(q="Using the table of illustrative public meetings, which reading matches KC-7.3.I's "
        "account of the period?",
      table=_T_MEETINGS,
      choices=[
        "Meetings arguing on both sides grow more numerous across the stretches recorded",
        "Meetings arguing for extension grow while meetings arguing against them fall away",
        "Only meetings arguing for extension are recorded",
        "The recorded totals fall across the three stretches",
        "Meetings arguing against extension outnumber those arguing for it in every stretch"],
      ans=0,
      why="Read from the table alone: both columns rise at every step and both are recorded "
          "in every stretch, while the column for extension is the larger throughout. Rising "
          "argument on both sides is what KC-7.3.I means by heightened public debates over "
          "America's role in the world accompanying new territorial ambitions and "
          "acquisitions."),

 dict(q="Unit 7's Learning Objective B asks for similarities AND differences. Which pair of "
        "findings answers both halves for this topic?",
      choices=[
        "Both sides drew on racial theories, while only one side appealed to "
        "self-determination and isolationism",
        "Both sides appealed to self-determination, while only one side drew on racial "
        "theories",
        "Neither side drew on racial theories, and both appealed to economic opportunity",
        "Both sides opposed extending territory overseas, for different reasons",
        "The two sides agreed about the nation's proper role but differed about its timing"],
      ans=0,
      why="KC-7.3.I.A and KC-7.3.I.B share racial theories and differ in that only KC-7.3.I.B "
          "names self-determination and the tradition of isolationism, which answers Unit 7 "
          "Learning Objective B's demand for similarities and differences at once. The other "
          "options reverse the shared element, deny it, or make the two sides agree on the "
          "conclusion KC-7.3.I.A and KC-7.3.I.B place them on opposite sides of."),

 dict(q="A hypothetical unattributed letter argues that expanding overseas would betray the "
        "country's own founding principles. Which framework sentence does the argument most "
        "directly rest on?",
      choices=[
        "KC-7.3.I.B, which has anti-imperialists cite principles of self-determination and "
        "the tradition of isolationism",
        "KC-7.3.I.A, which has imperialists cite economic opportunities",
        "KC-7.3.I.A, which has imperialists cite competition with European empires",
        "KC-7.3.I, which describes new territorial acquisitions",
        "Unit 7 Learning Objective B, which asks for a comparison of attitudes"],
      ans=0,
      why="KC-7.3.I.B states that anti-imperialists cited principles of self-determination "
          "and invoked the U.S. foreign policy tradition of isolationism to argue that the "
          "United States should not extend its territory overseas, and an appeal to the "
          "country's own founding principles against expansion is that case. The KC-7.3.I.A "
          "options are the arguments on the other side, and the last two describe the "
          "acquisitions and the objective rather than an argument."),

 dict(q="A student concludes from KC-7.3.I.B that anti-imperialists rejected racial theories. "
        "Why does the sentence not support that?",
      choices=[
        "Because it says they INVOKED racial theories alongside the tradition of isolationism",
        "Because it says nothing at all about racial theories",
        "Because it says they rejected the tradition of isolationism instead",
        "Because it treats racial theories as an imperialist argument only",
        "Because it places their argument after the debates had ended"],
      ans=0,
      why="KC-7.3.I.B states that anti-imperialists invoked BOTH racial theories and the U.S. "
          "foreign policy tradition of isolationism, so the sentence has them using the "
          "racial argument rather than rejecting it, and KC-7.3.I.A shows the same kind of "
          "argument on the other side. Reading the sentence as a rejection reverses what it "
          "reports."),

 dict(q="Which thematic focus does the CED print on this topic's page?",
      choices=[
        "America in the World, concerning interactions between empires, nations, and peoples",
        "Work, Exchange, and Technology, concerning markets, labor, and technology",
        "Migration and Settlement, concerning push and pull factors",
        "American and Regional Culture, concerning creative expression and social mores",
        "Social Structures, concerning social categories, roles, and practices"],
      ans=0,
      why="The thematic focus printed on this topic page is America in the World, which the "
          "CED glosses as the diplomatic, economic, cultural, and military interactions "
          "between empires, nations, and peoples that shape America's increasingly important "
          "role in the world. That is the theme KC-7.3.I's debates over America's role belong "
          "to; the other four are thematic focuses printed on other pages of this unit."),

 dict(q="What does the word DESTINED do in KC-7.3.I.A's account of the imperialist argument?",
      choices=[
        "It reports the claim imperialists made about expansion rather than a judgement the "
        "framework makes",
        "It states the framework's own conclusion about the period",
        "It restricts the argument to the Western Hemisphere",
        "It shows that imperialists expected expansion to fail",
        "It marks expansion as something anti-imperialists also expected"],
      ans=0,
      why="KC-7.3.I.A says imperialists cited four things TO ARGUE that Americans were "
          "destined to expand their culture and institutions to peoples around the globe, so "
          "the destiny is inside the argument being reported. The sentence sets no regional "
          "limit, reports no expectation of failure, and KC-7.3.I.B puts anti-imperialists on "
          "the other side of the question."),

 dict(q="A student writes that KC-7.3.I.B shows anti-imperialists wanted the United States to "
        "cut its trade with the rest of the world. Why does the sentence not support that?",
      choices=[
        "Because the argument it reports is about extending TERRITORY overseas and says "
        "nothing about trade",
        "Because it reports an argument for extending territory rather than against it",
        "Because it names economic opportunities as an anti-imperialist argument",
        "Because it applies only to the Western Hemisphere",
        "Because it describes a policy the government adopted"],
      ans=0,
      why="KC-7.3.I.B states that anti-imperialists argued the United States should not "
          "extend its territory overseas; commerce is not in the sentence, and reading it in "
          "adds a claim the framework does not make. Economic opportunities belong to "
          "KC-7.3.I.A, the sentence sets no regional limit, and it reports an argument rather "
          "than an adopted policy."),

 dict(q="Which statement belongs to a LATER topic of this unit rather than to the debates "
        "this topic covers?",
      choices=[
        "The American victory in a war with Spain led to the acquisition of island territories "
        "in the Caribbean and the Pacific",
        "Imperialists cited economic opportunities and competition with European empires",
        "Anti-imperialists cited principles of self-determination",
        "Anti-imperialists invoked the U.S. foreign policy tradition of isolationism",
        "New territorial ambitions accompanied heightened public debates over America's role "
        "in the world"],
      ans=0,
      why="The acquisition of island territories following the American victory is KC-7.3.I.C, "
          "which the CED prints on the next topic's page, on the effects of that war. This "
          "topic's Required Course Content is KC-7.3.I.A and KC-7.3.I.B, the two sides of the "
          "argument, set inside KC-7.3.I's account of heightened public debates."),

 dict(q="How does the historical situation of the 1890s bear on the imperialist argument, as "
        "the framework reports it?",
      choices=[
        "The perception that the western frontier was closed was one of the things "
        "imperialists cited",
        "The closing of the frontier is what anti-imperialists cited against expansion",
        "The framework gives no historical situation for either argument",
        "The framework places the imperialist argument entirely after 1920",
        "The framework treats the frontier as still open throughout the period"],
      ans=0,
      why="KC-7.3.I.A names the perception in the 1890s that the western frontier was closed "
          "among the things imperialists cited, which is a historical situation shaping an "
          "argument, exactly what suggested skill 2.C asks a student to explain. KC-7.3.I.B "
          "does not mention the frontier, and KC-7.3.I places these debates in the late 19th "
          "century and early 20th century."),

 dict(q="A hypothetical newspaper report of a debate, offered as an illustration only, "
        "summarises one speaker as arguing that expansion would bring both markets and a duty "
        "to spread American institutions. Which two parts of KC-7.3.I.A does that summary "
        "combine?",
      choices=[
        "The economic opportunities cited, and the argument that Americans were destined to "
        "expand their culture and institutions",
        "The economic opportunities cited, and the tradition of isolationism",
        "The racial theories cited, and principles of self-determination",
        "Competition with European empires, and the argument that territory should not be "
        "extended",
        "The perception of a closed frontier, and the acquisition of island territories"],
      ans=0,
      why="KC-7.3.I.A names economic opportunities among the things imperialists cited and "
          "gives their conclusion as the claim that Americans were destined to expand their "
          "culture and institutions to peoples around the globe, which is the pair the "
          "summary joins. Isolationism and self-determination are KC-7.3.I.B's, and the "
          "acquisition of island territories is KC-7.3.I.C, on the following topic's page."),

 dict(q="Taken together, what do KC-7.3.I.A and KC-7.3.I.B establish about the debate over "
        "America's role in the world?",
      choices=[
        "Two sides drew on an overlapping stock of arguments, including racial theories, and "
        "reached opposite conclusions about extending territory",
        "Two sides drew on entirely separate arguments and reached opposite conclusions",
        "Two sides drew on the same arguments and reached the same conclusion",
        "One side argued while the other left the question alone",
        "The debate concerned the domestic economy rather than the nation's role in the world"],
      ans=0,
      why="KC-7.3.I.A and KC-7.3.I.B share racial theories while differing over economic "
          "opportunity, competition with European empires and the closed frontier on one side "
          "and self-determination and isolationism on the other, and they end in opposite "
          "conclusions about extending territory overseas. KC-7.3.I places the whole inside "
          "heightened public debates over America's role in the world, which is also what "
          "Unit 7 Learning Objective B asks students to compare."),
]
