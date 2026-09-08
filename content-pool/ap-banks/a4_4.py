# AP U.S. HISTORY 4.4 America on the World Stage
# (title copied from US_HISTORY_topics.json; the CED's Unit at a Glance row and its topic
# page both read "America on the World Stage", and the JSON matches them.)
# Unit 4, Period 4: 1800 to 1848. Thematic focus America in the World (WOR).
# Suggested skill 2.B, explain the point of view, purpose, historical situation, and/or
# audience of a source. Reasoning process for this topic: Causation.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 4 Learning Objective D
#       Explain how and why American foreign policy developed and expanded over time.
#
#   KC-4.3.I       Struggling to create an independent global presence, the United States
#                  sought to claim territory throughout the North American continent and
#                  promote foreign trade.
#   KC-4.3.I.A.ii  The U.S. government sought influence and control over the Western
#                  Hemisphere through a variety of means, including military actions,
#                  American Indian removal, and diplomatic efforts such as the Monroe
#                  Doctrine.
#
#   The neighbouring sub-point, printed on topic 4.2's page and used here only for the
#   contrast the framework itself sets up:
#   KC-4.3.I.A.i   Following the Louisiana Purchase, the U.S. government sought influence
#                  and control over North America through a variety of means, including
#                  exploration and diplomatic efforts.
#
#   Parent concept printed in the unit's preview and reviewed at 4.14:
#   KC-4.3         The U.S. interest in increasing foreign trade and expanding its
#                  national borders shaped the nation's foreign policy and spurred
#                  government and private initiatives.
#
#   Thematic focus WOR, America in the World: "Diplomatic, economic, cultural, and
#   military interactions between empires, nations, and peoples shape the development of
#   America and America's increasingly important role in the world."
#
#   Skill 2.B: explain the point of view, purpose, historical situation, and/or audience
#   of a source.
#
#   Reasoning process Causation: 2.i describe causes and/or effects; 2.ii explain the
#   relationship between causes and effects; 2.iii explain the difference between primary
#   and secondary causes and between short and long term effects; 2.iv explain how a
#   relevant context influenced a development; 2.v explain the relative historical
#   significance of different causes and effects.
#
# SENSITIVE MATERIAL. KC-4.3.I.A.ii names American Indian removal as one of the means by
# which the U.S. government sought influence and control over the Western Hemisphere.
# This module states that as the framework states it -- a government policy, listed among
# the instruments of a policy of control -- and adds no detail of its own. KC-4.3.I.B,
# which describes American Indian resistance and the wars and relocations that followed,
# is printed on topic 4.8's page and is that topic's material, not this one's.
#
# WHAT IS NOT ASSERTED. The CED names the Monroe Doctrine as an EXAMPLE of a diplomatic
# effort and gives no text, date or author for it, so neither does this module; no key
# turns on what the Doctrine said.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=,
# and every table and every source is marked hypothetical in its stem.
# PROSE ONLY: no LaTeX; a span of years is written "1800 to 1848", never with a hyphen.
TOPIC = ("4.4", "America on the World Stage", 4)

_T_MEANS = dict(
    headers=["Action recorded (hypothetical)",
             "Kind of means the record assigns it",
             "Where the action was directed"],
    rows=[["Action 1", "Military action", "The Western Hemisphere"],
          ["Action 2", "American Indian removal", "The Western Hemisphere"],
          ["Action 3", "Diplomatic effort", "The Western Hemisphere"],
          ["Action 4", "Diplomatic effort", "The Western Hemisphere"],
          ["Action 5", "Military action", "The Western Hemisphere"]])

_T_TRADE = dict(
    headers=["Decade (hypothetical figures)",
             "Value of goods traded with other nations",
             "Area of territory newly claimed, in thousands of square miles"],
    rows=[["1800 to 1810", "55", "12"],
          ["1810 to 1820", "78", "19"],
          ["1820 to 1830", "104", "26"],
          ["1830 to 1840", "141", "38"]])

_T_INITIATIVE = dict(
    headers=["Decade (hypothetical figures)",
             "Ventures abroad fitted out by the government",
             "Ventures abroad fitted out by private parties"],
    rows=[["1800 to 1810", "7", "18"],
          ["1810 to 1820", "11", "27"],
          ["1820 to 1830", "16", "41"],
          ["1830 to 1840", "23", "60"]])

QUESTIONS = [

 dict(q="Unit 4's Learning Objective D states what students should be able to explain about "
        "American foreign policy. Which is it?",
      choices=[
        "How and why American foreign policy developed and expanded over time",
        "How American foreign policy was fixed at the founding and left unchanged",
        "Why European powers shaped their policy towards the United States",
        "How regional interests affected debates about the federal government",
        "How and why a new national culture developed in the same years"],
      ans=0,
      why="Unit 4 Learning Objective D reads 'Explain how and why American foreign policy "
          "developed and expanded over time'. A policy fixed at the founding is the negation "
          "of development and expansion, European policy is not the objective's subject, and "
          "regional interests and national culture are Unit 4 Learning Objectives C and I."),

 dict(q="KC-4.3.I opens with the participle 'Struggling to create an independent global "
        "presence'. What does that phrase say about the United States in this period?",
      choices=[
        "It was working towards a standing among other nations that it did not yet have",
        "It had already secured a settled standing among other nations",
        "It had abandoned the attempt to act independently abroad",
        "It was content to act through the agency of a European power",
        "It had withdrawn from dealings with other nations altogether"],
      ans=0,
      why="KC-4.3.I's word STRUGGLING describes an effort still under way to create an "
          "INDEPENDENT global presence, so the standing is being sought rather than already "
          "held or given up. Acting through a European power or withdrawing from other "
          "nations would contradict the same sentence, which has the United States promoting "
          "foreign trade and claiming territory."),

 dict(q="KC-4.3.I names two things the United States sought while struggling to create an "
        "independent global presence. Which pair does the framework give?",
      choices=[
        "To claim territory throughout the North American continent and to promote foreign "
        "trade",
        "To claim territory throughout the North American continent and to restrict foreign "
        "trade",
        "To promote foreign trade and to renounce further territorial claims",
        "To settle its boundaries by arbitration and to avoid commerce with Europe",
        "To acquire territory outside the Western Hemisphere and to promote foreign trade"],
      ans=0,
      why="KC-4.3.I states that the United States sought to claim territory throughout the "
          "North American continent AND promote foreign trade. The second and third options "
          "each keep one half and reverse the other, and the framework mentions neither "
          "arbitration nor acquisitions outside the hemisphere; KC-4.3 confirms the interest "
          "in increasing foreign trade and expanding national borders."),

 dict(q="Over which region does KC-4.3.I.A.ii say the U.S. government sought influence and "
        "control?",
      choices=[
        "The Western Hemisphere",
        "North America only",
        "Europe",
        "The Pacific islands",
        "West Africa"],
      ans=0,
      why="KC-4.3.I.A.ii states that the U.S. government sought influence and control over the "
          "Western Hemisphere. North America is the region named in the neighbouring sentence "
          "KC-4.3.I.A.i, printed on topic 4.2's page, and Europe, the Pacific and West Africa "
          "are named in neither."),

 dict(q="KC-4.3.I.A.ii lists the means by which the U.S. government pursued influence and "
        "control over the Western Hemisphere. Which set does the framework name?",
      choices=[
        "Military actions, American Indian removal, and diplomatic efforts",
        "Military actions, foreign loans, and religious missions",
        "American Indian removal, foreign loans, and colonisation societies",
        "Diplomatic efforts, tariffs, and naval blockade",
        "Military actions, exploration, and the sale of public land"],
      ans=0,
      why="KC-4.3.I.A.ii says the government sought influence and control over the Western "
          "Hemisphere through a variety of means, including military actions, American Indian "
          "removal, and diplomatic efforts. Loans, missions, colonisation societies, tariffs, "
          "blockade and land sales are not in that list, and exploration belongs to the "
          "neighbouring sentence about North America."),

 dict(q="KC-4.3.I.A.ii names the Monroe Doctrine. Under which of its listed means does the "
        "framework place it?",
      choices=[
        "Among the diplomatic efforts",
        "Among the military actions",
        "Among the measures of American Indian removal",
        "Among the commercial treaties",
        "Among the acts of exploration"],
      ans=0,
      why="KC-4.3.I.A.ii reads 'diplomatic efforts such as the Monroe Doctrine', so the "
          "framework offers the Doctrine as an example of a diplomatic effort rather than of "
          "a military action or of removal. Commercial treaties and exploration are not "
          "categories in this sentence at all, exploration belonging to KC-4.3.I.A.i."),

 dict(q="KC-4.3.I.A.i and KC-4.3.I.A.ii each describe the U.S. government seeking influence "
        "and control. How do the two sentences differ in the region they name?",
      choices=[
        "The first names North America and the second names the Western Hemisphere",
        "The first names the Western Hemisphere and the second names North America",
        "Both sentences name the Western Hemisphere",
        "Both sentences name North America",
        "Neither sentence names a region"],
      ans=0,
      why="KC-4.3.I.A.i has the government seeking influence and control over North America "
          "following the Louisiana Purchase, and KC-4.3.I.A.ii has it seeking influence and "
          "control over the Western Hemisphere. Reversing the two, or collapsing them into "
          "one region, loses the widening of scope that Unit 4 Learning Objective D asks "
          "students to explain."),

 dict(q="How do the means named in KC-4.3.I.A.i differ from those named in KC-4.3.I.A.ii?",
      choices=[
        "The first names exploration and diplomatic efforts, while the second adds military "
        "actions and American Indian removal",
        "The first names military actions and removal, while the second adds exploration",
        "Both sentences name exactly the same means",
        "The first names only diplomatic efforts and the second only military actions",
        "Neither sentence names any particular means"],
      ans=0,
      why="KC-4.3.I.A.i lists exploration and diplomatic efforts; KC-4.3.I.A.ii lists military "
          "actions, American Indian removal, and diplomatic efforts such as the Monroe "
          "Doctrine. Diplomacy appears in both, which is why the difference lies in what the "
          "second sentence adds, and reversing the two sentences misstates both."),

 dict(q="What do KC-4.3.I.A.i and KC-4.3.I.A.ii assert in common?",
      choices=[
        "That the U.S. government sought influence and control through a variety of means",
        "That the U.S. government relied on a single instrument in each case",
        "That the U.S. government acted only through private parties",
        "That the U.S. government sought trade but not influence",
        "That the U.S. government confined itself to the territory it already held"],
      ans=0,
      why="Both sentences use the same construction: the U.S. government sought influence and "
          "control over a region through A VARIETY OF MEANS, including a named list. A single "
          "instrument is what that phrase excludes, and KC-4.3 has the government spurring "
          "initiatives of its own alongside private ones while KC-4.3.I has it claiming "
          "territory rather than staying put."),

 dict(q="According to KC-4.3, what shaped the nation's foreign policy in this period?",
      choices=[
        "The U.S. interest in increasing foreign trade and expanding its national borders",
        "The U.S. interest in reducing foreign trade and fixing its national borders",
        "The demands of European powers on the United States",
        "The decisions of the federal courts about treaties",
        "The internal debate over the powers of the federal government"],
      ans=0,
      why="KC-4.3 states that the U.S. interest in increasing foreign trade and expanding its "
          "national borders shaped the nation's foreign policy. The second option reverses "
          "both halves; European demands and court decisions are not named in the sentence, "
          "and the debate over federal power belongs to KC-4.1.I.A."),

 dict(q="KC-4.3 says the nation's interest in trade and borders spurred initiatives. Whose "
        "initiatives, and what does naming both matter for?",
      choices=[
        "Government and private initiatives, so foreign policy was not carried on by the "
        "state alone",
        "Government initiatives alone, so private parties had no part in it",
        "Private initiatives alone, so the government had no part in it",
        "The initiatives of other governments acting in North America",
        "The initiatives of the federal courts in interpreting treaties"],
      ans=0,
      why="KC-4.3 names government AND private initiatives, so restricting the effort to "
          "either one alone drops half the sentence, and KC-4.3.I.A.ii separately describes "
          "the government's own means. Other governments and the courts are not the actors "
          "the sentence names."),

 dict(q="The America in the World thematic focus printed on this topic's page names four "
        "kinds of interaction between empires, nations and peoples. Which set does it give?",
      choices=[
        "Diplomatic, economic, cultural, and military",
        "Diplomatic, economic, religious, and legal",
        "Economic, cultural, scientific, and military",
        "Diplomatic, military, demographic, and technological",
        "Economic, military, judicial, and educational"],
      ans=0,
      why="The America in the World thematic focus reads that diplomatic, economic, cultural, "
          "and military interactions between empires, nations, and peoples shape the "
          "development of America. Religious, legal, scientific, demographic, technological, "
          "judicial and educational interactions are not in that list, and Unit 4 Learning "
          "Objective D is the objective the focus serves here."),

 dict(q="The same thematic focus says those interactions shape two things. What is the second, "
        "beside the development of America itself?",
      choices=[
        "America's increasingly important role in the world",
        "America's withdrawal from the affairs of other nations",
        "The internal boundaries between American regions",
        "The powers reserved to the state governments",
        "The character of American religious belief"],
      ans=0,
      why="The America in the World thematic focus says the interactions it names shape the "
          "development of America AND America's increasingly important role in the world, "
          "which is the widening Unit 4 Learning Objective D asks students to explain. "
          "Withdrawal is its negation, and internal boundaries, state powers and religious "
          "belief belong to other themes of the course."),

 dict(q="Which statement is the suggested skill printed beside this topic's title?",
      choices=[
        "Explain the point of view, purpose, historical situation, and/or audience of a source",
        "Identify a source's point of view, purpose, historical situation, and/or audience",
        "Explain how claims or evidence support, modify, or refute a source's argument",
        "Support an argument using specific and relevant evidence",
        "Explain a historical concept, development, or process"],
      ans=0,
      why="Skill 2.B, explain the point of view, purpose, historical situation, and/or "
          "audience of a source, is printed beside this topic's title in service of Unit 4 "
          "Learning Objective D. Skill 2.A is the same list under IDENTIFY, and the remaining "
          "options are skills 3.D, 6.B and 1.B, printed beside topics 4.8, 4.5 and 4.7."),

 dict(q="Suppose a hypothetical dispatch, its author unnamed, informs a minister abroad that "
        "the United States will treat any new colonisation in the hemisphere as unfriendly, "
        "and asks him to say so to the government he is posted to. Applying skill 2.B, which "
        "statement explains the dispatch's PURPOSE?",
      choices=[
        "It sets out to have a position on the hemisphere communicated to another government, "
        "so that the position becomes known before it is tested",
        "It concerns the Western Hemisphere",
        "It is addressed to a minister abroad",
        "It takes the view that new colonisation would be unfriendly",
        "It was written while the United States was seeking influence in the hemisphere"],
      ans=0,
      why="Skill 2.B asks the student to EXPLAIN a purpose, which means saying what the source "
          "is trying to bring about and by what means. KC-4.3.I.A.ii places diplomatic "
          "efforts among the means by which the U.S. government sought influence and control "
          "over the Western Hemisphere. The remaining options give the subject, the audience, "
          "the point of view and the historical situation instead."),

 dict(q="An illustrative memoir, its author unnamed, defends a military action in the "
        "hemisphere as necessary for the security of American commerce. Applying skill 2.B, "
        "which statement explains the memoir's POINT OF VIEW?",
      choices=[
        "It reads security and commerce as a single interest, which is why it treats force as "
        "a commercial instrument",
        "It defends a military action",
        "It was written after the action it defends",
        "It is a memoir rather than an official paper",
        "It seeks to persuade readers that the action was justified"],
      ans=0,
      why="Skill 2.B asks for an explanation of a point of view, which means saying what the "
          "position rests on. KC-4.3.I joins claiming territory to promoting foreign trade in "
          "a single sentence and KC-4.3.I.A.ii names military actions among the means of "
          "seeking influence and control, so treating force and commerce as one interest is "
          "the position explained. Merely reporting the defence names the view, and the "
          "remaining options give the situation, the form and the purpose."),

 dict(q="Consider a hypothetical petition, unattributed, from shipowners asking the government "
        "to protect their trade in distant waters. Applying skill 2.B, which statement "
        "explains the petition's AUDIENCE and why that matters?",
      choices=[
        "It is directed at the government because only the government commands the means of "
        "protection, which is why it asks for action rather than for sympathy",
        "The government is its addressee",
        "It comes from shipowners",
        "It asks for protection of trade",
        "It was submitted while foreign trade was expanding"],
      ans=0,
      why="Skill 2.B asks students to explain an audience rather than name it, which means "
          "saying how the addressee shapes what is asked for. KC-4.3 has the interest in "
          "increasing foreign trade spurring government and private initiatives together, so "
          "a request addressed to the government is a request for the state's own instrument. "
          "Naming the addressee, the petitioners, the request or the date identifies without "
          "explaining."),

 dict(q="Why does the framework ask students to explain a source's historical situation when "
        "the source concerns foreign policy?",
      choices=[
        "What a source urges abroad depends on what the nation was then seeking abroad",
        "The situation supplies the date, which is all that is needed to use the source",
        "The situation determines whether the source is primary or secondary",
        "The situation matters only for sources written by officials",
        "The situation is the same thing as the source's purpose"],
      ans=0,
      why="Skill 2.B asks for an explanation of historical situation, and skill 2.C asks how "
          "such features might limit a source's uses, which together treat circumstance as "
          "part of the argument rather than a label on it. KC-4.3.I gives the circumstance "
          "that matters here, a nation struggling to create an independent global presence "
          "while claiming territory and promoting trade, and Unit 4 Learning Objective D asks "
          "how and why policy developed. A situation is neither a date, a source type nor a "
          "purpose."),

 dict(q="The reasoning process printed beside this topic asks students to trace what produced "
        "a development and what followed from it. Which process is it?",
      choices=[
        "Causation",
        "Comparison",
        "Continuity and Change",
        "Argumentation",
        "Contextualization"],
      ans=0,
      why="The unit's own table prints Causation as this topic's reasoning process, matching "
          "Unit 4 Learning Objective D's demand that students explain HOW AND WHY American "
          "foreign policy developed and expanded. Comparison and Continuity and Change are "
          "the other two reasoning processes; argumentation and contextualization are "
          "historical thinking skills."),

 dict(q="One aspect of the Causation reasoning process concerns the link between a cause and "
        "its effect. What does the framework ask students to do?",
      choices=[
        "Explain the relationship between causes and effects of a specific historical "
        "development or process",
        "List the causes of a development without relating them to its effects",
        "Explain similarities and differences between two developments",
        "Describe patterns of continuity and change over time",
        "Identify and describe a historical context for a development"],
      ans=0,
      why="Aspect 2.ii of the Causation reasoning process reads 'Explain the relationship "
          "between causes and effects of a specific historical development or process', so a "
          "bare list is not what is asked for. Similarities and differences belong to "
          "Comparison, patterns over time to Continuity and Change, and identifying a context "
          "to skill 4.A; Unit 4 Learning Objective D is what the causation aspect is applied "
          "to here."),

 dict(q="Unit 4's Learning Objective D says foreign policy developed and expanded OVER TIME. "
        "What does that phrase ask a student to attend to?",
      choices=[
        "The change in the reach and instruments of policy across the period rather than a "
        "single moment",
        "A single decisive moment at which policy was settled",
        "The policy of other nations towards the United States",
        "The internal debate over the powers of the federal government",
        "The unchanging character of American policy across the period"],
      ans=0,
      why="Unit 4 Learning Objective D asks how and why American foreign policy developed and "
          "expanded OVER TIME, which directs attention to change across the period; the "
          "framework's own pair of sentences shows it, KC-4.3.I.A.i naming North America and "
          "exploration and KC-4.3.I.A.ii naming the Western Hemisphere and a wider set of "
          "means. A single moment and an unchanging character are the two ways of losing that "
          "reading, and the other options change the subject."),

 dict(q="What does KC-4.3.I's word STRUGGLING concede about the effort it describes?",
      choices=[
        "That an independent global presence was not yet established and was hard to obtain",
        "That the effort was abandoned during the period",
        "That the effort succeeded immediately",
        "That other nations offered no resistance to it",
        "That the effort concerned trade but not territory"],
      ans=0,
      why="KC-4.3.I says the United States was STRUGGLING to create an independent global "
          "presence, which concedes difficulty and an outcome not yet reached, without saying "
          "the effort was abandoned or immediately successful. The same sentence names "
          "territory alongside trade, and KC-4.3.I.A.ii's list of means implies effort rather "
          "than an absence of resistance."),

 dict(q="Which of the following does the framework present as an AIM of American policy in "
        "this period rather than as a means of pursuing it?",
      choices=[
        "Creating an independent global presence",
        "American Indian removal",
        "Diplomatic efforts",
        "Military actions",
        "Exploration of the interior"],
      ans=0,
      why="KC-4.3.I makes the independent global presence the thing the United States was "
          "struggling to create, which is the aim; KC-4.3.I.A.ii lists military actions, "
          "American Indian removal and diplomatic efforts as MEANS by which the government "
          "sought influence and control, and KC-4.3.I.A.i adds exploration to the same "
          "category of means."),

 dict(q="A hypothetical class summary states that American policy abroad in this period was "
        "purely commercial. Which sentence contradicts it most directly?",
      choices=[
        "KC-4.3.I.A.ii, which names military actions and American Indian removal among the "
        "means used",
        "KC-4.3, which names an interest in increasing foreign trade",
        "KC-4.3.I, which names the promotion of foreign trade",
        "The thematic focus, which names economic interactions",
        "KC-4.3.I.A.i, which names exploration"],
      ans=0,
      why="KC-4.3.I.A.ii names military actions and American Indian removal alongside "
          "diplomatic efforts, which is what a purely commercial account leaves out. The "
          "other four all name commercial or exploratory activity and so are consistent with "
          "the summary rather than a refutation of it, even though KC-4.3 and KC-4.3.I also "
          "name territorial claims."),

 dict(q="A hypothetical revision note lists the Monroe Doctrine among American military "
        "actions of the period. What is wrong with that placement?",
      choices=[
        "The framework offers it as an example of a diplomatic effort, a separate item in the "
        "same list",
        "The framework does not mention the Monroe Doctrine at all",
        "The framework places it in a later period of the course",
        "The framework treats it as an act of exploration",
        "The framework treats it as a commercial treaty"],
      ans=0,
      why="KC-4.3.I.A.ii reads 'diplomatic efforts such as the Monroe Doctrine', listing "
          "military actions, American Indian removal and diplomatic efforts as separate items "
          "and placing the Doctrine under the third. The Doctrine is therefore named, is named "
          "in this unit, and is classed neither as exploration nor as a commercial treaty."),

 dict(q="How does KC-4.3.I.A.ii sit beneath KC-4.3.I, the concept printed above it?",
      choices=[
        "KC-4.3.I states the aim of territory and trade, and KC-4.3.I.A.ii describes the means "
        "the government used to pursue influence and control",
        "KC-4.3.I.A.ii states the aim, and KC-4.3.I describes the means used to pursue it",
        "The two sentences concern different periods of the course",
        "KC-4.3.I concerns culture while KC-4.3.I.A.ii concerns commerce",
        "The two sentences state the same claim in different words"],
      ans=0,
      why="KC-4.3.I is the broader statement about a nation struggling to create an "
          "independent global presence by claiming territory and promoting trade, and "
          "KC-4.3.I.A.ii sits beneath it naming the means by which the government sought "
          "influence and control over the Western Hemisphere. Exchanging the levels, "
          "separating them by period or assigning either to culture misreads the framework's "
          "own ordering, which Unit 4 Learning Objective D follows."),

 dict(q="A hypothetical register assigns each of five recorded actions to a kind of means and "
        "records where it was directed. What does the register support?",
      table=_T_MEANS,
      choices=[
        "All three of the kinds of means the framework lists appear in the record",
        "Only one kind of means appears in the record",
        "The recorded actions were directed at more than one region",
        "Diplomatic effort is the only kind of means recorded more than once",
        "No military action appears in the record"],
      ans=0,
      why="Read from the table alone: the middle column holds three distinct kinds of means, "
          "military action appears twice and diplomatic effort twice, and every row names the "
          "same single region. That variety is what KC-4.3.I.A.ii describes when it says the "
          "government sought influence and control over the Western Hemisphere through a "
          "variety of means, including military actions, American Indian removal, and "
          "diplomatic efforts."),

 dict(q="Four decades of hypothetical figures set the value of goods traded with other nations "
        "beside the area of territory newly claimed. Which reading do the figures support?",
      table=_T_TRADE,
      choices=[
        "Trade and new territorial claims both grow across the four decades",
        "Trade grows while new territorial claims fall away",
        "New territorial claims grow while trade falls away",
        "Neither column changes across the four decades",
        "New claims exceed the traded value in every decade recorded"],
      ans=0,
      why="Read from the table alone: both columns rise at every step, so neither falls away "
          "and neither is unchanged, and the traded value is the larger figure in every row. "
          "Two lines of effort rising together is what KC-4.3 describes when it says the U.S. "
          "interest in increasing foreign trade AND expanding its national borders shaped the "
          "nation's foreign policy."),

 dict(q="Suppose a record of ventures sent abroad separates those fitted out by the government "
        "from those fitted out by private parties. Which conclusion does the record support?",
      table=_T_INITIATIVE,
      choices=[
        "Both government and private ventures increase, with private ventures the more "
        "numerous throughout",
        "Both government and private ventures increase, with government ventures the more "
        "numerous throughout",
        "Government ventures increase while private ventures decline",
        "Private ventures appear in only one of the decades recorded",
        "The two columns hold the same figure in every decade recorded"],
      ans=0,
      why="Read from the table alone: both columns rise at every step and the private column "
          "is the larger in all four rows, so neither declines, private ventures appear "
          "throughout, and the columns never match. KC-4.3 states that the interest in "
          "increasing foreign trade and expanding national borders spurred government AND "
          "private initiatives."),

 dict(q="Taking this topic's sentences together, which statement best collects what the "
        "framework asserts about American foreign policy in these years?",
      choices=[
        "A nation still struggling for an independent standing abroad pursued territory across "
        "the continent and trade beyond it, and its government sought influence and control "
        "over the Western Hemisphere by military action, American Indian removal and "
        "diplomacy",
        "A nation with a settled standing abroad confined its policy to commerce and made no "
        "territorial claims",
        "A nation that had abandoned foreign trade concentrated on claiming territory by "
        "military action alone",
        "A nation whose government left foreign policy entirely to private parties",
        "A nation whose policy abroad concerned Europe rather than the Western Hemisphere"],
      ans=0,
      why="The first collects KC-4.3.I and KC-4.3.I.A.ii in the order the topic page prints "
          "them, with KC-4.3's government and private initiatives behind them, and adds "
          "nothing. A settled standing contradicts KC-4.3.I's STRUGGLING, abandoning trade "
          "and leaving policy to private parties contradict KC-4.3, and Europe is not the "
          "region either sentence names."),
]
