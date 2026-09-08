# AP U.S. HISTORY 4.3 Politics and Regional Interests
# (title copied from US_HISTORY_topics.json)
# Unit 4, Period 4: 1800 to 1848. Thematic focus Politics and Power (PCE).
# Suggested skill 2.B, explain the point of view, purpose, historical situation, and/or
# audience of a source. Reasoning process for this topic: Comparison.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 4 Learning Objective C
#       Explain how different regional interests affected debates about the role of the
#       federal government in the early republic.
#
#   KC-4.1.I.D    Regional interests often trumped national concerns as the basis for
#                 many political leaders' positions on slavery and economic policy.
#   KC-4.2.III.D  Plans to further unify the U.S. economy, such as the American System,
#                 generated debates over whether such policies would benefit agriculture
#                 or industry, potentially favoring different sections of the country.
#   KC-4.3.II.C   Congressional attempts at political compromise, such as the Missouri
#                 Compromise, only temporarily stemmed growing tensions between opponents
#                 and defenders of slavery.
#
#   Parent concepts printed in the unit's preview and reviewed at 4.14:
#   KC-4.1.I      The nation's transition to a more participatory democracy was achieved
#                 by expanding suffrage from a system based on property ownership to one
#                 based on voting by all adult white men, and it was accompanied by the
#                 growth of political parties.
#   KC-4.2.III    Economic development shaped settlement and trade patterns, helping to
#                 unify the nation while also encouraging the growth of different regions.
#   KC-4.3.II     The United States' acquisition of lands in the West gave rise to
#                 contests over the extension of slavery into new territories.
#
#   Thematic focus PCE, Politics and Power: "Debates fostered by social and political
#   groups about the role of government in American social, political, and economic life
#   shape government policy, institutions, political parties, and the rights of citizens."
#
#   Skill 2.B: explain the point of view, purpose, historical situation, and/or audience
#   of a source. Skill 2.A, printed on topic 4.2, is the same list under IDENTIFY.
#
#   Reasoning process Comparison: 1.i describe similarities and/or differences between
#   different historical developments or processes; 1.ii explain relevant similarities
#   and/or differences between specific historical developments and processes; 1.iii
#   explain the relative historical significance of similarities and/or differences
#   between different historical developments or processes.
#
# SENSITIVE MATERIAL. Slavery is the subject of two of this topic's three sentences. It
# is handled as the CED handles it -- as a matter of political conflict between, in the
# framework's own words, opponents and defenders of slavery, whose tensions a compromise
# stemmed only temporarily. Nothing is added to what the framework states.
#
# WHAT IS NOT ASSERTED. The CED names the American System and the Missouri Compromise as
# EXAMPLES ("such as") without giving their terms, their dates or their authors, so
# neither does this module. Where the framework is silent the question is cut.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=,
# and every table and every source is marked hypothetical in its stem.
# PROSE ONLY: no LaTeX; a span of years is written "1800 to 1848", never with a hyphen.
TOPIC = ("4.3", "Politics and Regional Interests", 4)

_T_SECTIONS = dict(
    headers=["Section of the country (hypothetical figures)",
             "Votes cast for a plan to further unify the economy",
             "Votes cast against that plan"],
    rows=[["Section 1", "34", "6"],
          ["Section 2", "29", "9"],
          ["Section 3", "5", "31"]])

_T_COMPROMISE = dict(
    headers=["Congressional compromise (hypothetical)",
             "Years until tension over slavery rose again",
             "Was the underlying disagreement recorded as resolved?"],
    rows=[["Compromise 1", "8", "No"],
          ["Compromise 2", "6", "No"],
          ["Compromise 3", "4", "No"],
          ["Compromise 4", "3", "No"]])

_T_LEADERS = dict(
    headers=["Leader (hypothetical)",
             "Region represented",
             "Position taken on a proposed economic measure"],
    rows=[["Leader 1", "Region A", "In favour"],
          ["Leader 2", "Region A", "In favour"],
          ["Leader 3", "Region B", "Opposed"],
          ["Leader 4", "Region B", "Opposed"],
          ["Leader 5", "Region C", "Opposed"]])

QUESTIONS = [

 dict(q="Unit 4's Learning Objective C states what students should be able to explain about "
        "regional interests. Which is it?",
      choices=[
        "How different regional interests affected debates about the role of the federal "
        "government in the early republic",
        "How debates about the role of the federal government created the regions of the "
        "early republic",
        "How the federal government resolved every regional disagreement in the early republic",
        "How regional interests shaped the culture of the early republic",
        "How foreign policy divided the regions of the early republic"],
      ans=0,
      why="Unit 4 Learning Objective C reads 'Explain how different regional interests "
          "affected debates about the role of the federal government in the early republic', "
          "with the influence running from regional interests to the debates. The second "
          "option reverses that direction, and culture and foreign policy are the subjects of "
          "Unit 4 Learning Objectives I and D rather than of this one."),

 dict(q="KC-4.1.I.D weighs two kinds of concern against one another as the basis for many "
        "political leaders' positions. Which does the framework say prevailed?",
      choices=[
        "Regional interests often trumped national concerns",
        "National concerns often trumped regional interests",
        "Regional interests and national concerns carried equal weight",
        "Neither regional interests nor national concerns shaped those positions",
        "Party loyalty trumped both regional interests and national concerns"],
      ans=0,
      why="KC-4.1.I.D states that regional interests often trumped national concerns as the "
          "basis for many political leaders' positions. The second option reverses the "
          "framework's own ordering, and equal weight, no influence and the priority of party "
          "loyalty are each claims the sentence does not make."),

 dict(q="On which two subjects does KC-4.1.I.D say political leaders' positions rested on "
        "regional interests?",
      choices=[
        "Slavery and economic policy",
        "Slavery and foreign policy",
        "Economic policy and religious establishment",
        "Territorial expansion and the militia",
        "Public schooling and the postal service"],
      ans=0,
      why="KC-4.1.I.D names positions on slavery and economic policy as the ones for which "
          "regional interests often trumped national concerns. Foreign policy is the subject "
          "of KC-4.3.I.A.ii on topic 4.4, and religious establishment, the militia, schooling "
          "and the postal service are not in this sentence."),

 dict(q="KC-4.1.I.D says regional interests OFTEN trumped national concerns. What does that "
        "word do to the claim?",
      choices=[
        "It reports a frequent pattern rather than a rule without exception",
        "It reports that the pattern held in every case",
        "It reports that the pattern was rare",
        "It reports that the pattern applied only after 1848",
        "It reports that the pattern applied only to economic policy"],
      ans=0,
      why="KC-4.1.I.D's word OFTEN describes a frequent pattern and stops short of a universal "
          "rule, so neither 'every case' nor 'rare' matches it. The same sentence names "
          "slavery alongside economic policy, and Unit 4 Learning Objective C places the "
          "whole claim inside the early republic rather than after 1848."),

 dict(q="Whose positions does KC-4.1.I.D describe?",
      choices=[
        "Many political leaders",
        "Every voter in the republic",
        "The judges of the federal courts",
        "Foreign ministers accredited to the United States",
        "The officers of voluntary associations"],
      ans=0,
      why="KC-4.1.I.D speaks of the basis for MANY POLITICAL LEADERS' positions on slavery and "
          "economic policy, which is narrower than the whole electorate and different from "
          "judges, foreign ministers or the voluntary associations of KC-4.1.III.A. Unit 4 "
          "Learning Objective C asks how regional interests affected the debates those "
          "leaders conducted."),

 dict(q="KC-4.2.III.D describes what plans to further unify the U.S. economy generated. What "
        "does the framework say they produced?",
      choices=[
        "Debates over whether such policies would benefit agriculture or industry",
        "Agreement that such policies would benefit agriculture and industry alike",
        "A settled division of revenue between the sections",
        "An end to sectional disagreement about economic policy",
        "A transfer of economic policy to the state governments"],
      ans=0,
      why="KC-4.2.III.D states that plans to further unify the U.S. economy generated debates "
          "over whether such policies would benefit agriculture or industry. Agreement, a "
          "settled division and an end to disagreement are the opposite of a debate, and "
          "nothing in the sentence transfers economic policy to the states."),

 dict(q="Which example does KC-4.2.III.D give of a plan to further unify the U.S. economy?",
      choices=[
        "The American System",
        "The Missouri Compromise",
        "The Monroe Doctrine",
        "The Louisiana Purchase",
        "The Northwest Ordinance"],
      ans=0,
      why="KC-4.2.III.D names the American System as its example of a plan to further unify "
          "the U.S. economy. The Missouri Compromise is KC-4.3.II.C's example of a "
          "congressional attempt at political compromise, the Monroe Doctrine is named in "
          "KC-4.3.I.A.ii, the Louisiana Purchase in KC-4.3.I.A.i, and the Northwest Ordinance "
          "belongs to an earlier period of the course."),

 dict(q="KC-4.2.III.D ends with the phrase 'potentially favoring different sections of the "
        "country'. What does that clause add to the sentence?",
      choices=[
        "That the debate over agriculture and industry was also a debate between sections",
        "That the plans were designed to favour one section openly",
        "That the sections agreed about which industries to support",
        "That the debate concerned only the section where a plan was proposed",
        "That the plans had no consequences outside the capital"],
      ans=0,
      why="KC-4.2.III.D links the question of whether a policy would benefit agriculture or "
          "industry to its POTENTIALLY FAVORING DIFFERENT SECTIONS of the country, which is "
          "what makes the economic debate a sectional one, and Unit 4 Learning Objective C "
          "asks exactly how regional interests affected such debates. The word 'potentially' "
          "stops short of a designed preference, and agreement, a single-section debate and "
          "an absence of consequences each contradict the clause."),

 dict(q="What is the tension inside KC-4.2.III.D between the aim of the plans it describes and "
        "the response they met?",
      choices=[
        "Plans meant to further UNIFY the economy generated debates that set sections against "
        "one another",
        "Plans meant to divide the economy generated agreement between the sections",
        "Plans meant to unify the economy were adopted without any debate",
        "Plans meant to unify the economy concerned only foreign trade",
        "Plans meant to unify the economy were proposed only after 1848"],
      ans=0,
      why="KC-4.2.III.D calls them plans to FURTHER UNIFY the U.S. economy and then reports "
          "that they generated debates over whom the policies would benefit, potentially "
          "favoring different sections, so the unifying aim and the sectional response sit in "
          "the same sentence. KC-4.2.III makes the same double point about economic "
          "development unifying the nation while encouraging the growth of different regions."),

 dict(q="KC-4.3.II.C describes what congressional attempts at political compromise achieved. "
        "What does the framework say they did?",
      choices=[
        "They only temporarily stemmed growing tensions",
        "They permanently settled the disagreement",
        "They increased tensions immediately in every case",
        "They removed the question from Congress altogether",
        "They had no effect of any kind on the tensions"],
      ans=0,
      why="KC-4.3.II.C states that congressional attempts at political compromise ONLY "
          "TEMPORARILY stemmed growing tensions between opponents and defenders of slavery. "
          "That is neither a permanent settlement nor an absence of effect; the sentence "
          "credits the compromises with stemming the tensions for a time and denies that the "
          "relief lasted."),

 dict(q="Between whom does KC-4.3.II.C say the tensions ran?",
      choices=[
        "Opponents and defenders of slavery",
        "Agricultural and industrial interests",
        "The federal government and the state governments",
        "Established churches and voluntary associations",
        "Frontier settlers and coastal merchants"],
      ans=0,
      why="KC-4.3.II.C names growing tensions between opponents and defenders of slavery. "
          "Agriculture against industry is KC-4.2.III.D's division, the federal and state "
          "governments are the subject of KC-4.1.I.B, and neither churches nor frontier "
          "settlers appear in this sentence."),

 dict(q="Which example does KC-4.3.II.C give of a congressional attempt at political "
        "compromise?",
      choices=[
        "The Missouri Compromise",
        "The American System",
        "A treaty with a European power",
        "A decision of the Supreme Court",
        "A convention called by the states"],
      ans=0,
      why="KC-4.3.II.C names the Missouri Compromise as its example of a congressional attempt "
          "at political compromise. The American System is KC-4.2.III.D's example of a plan "
          "to unify the economy, and a treaty, a court decision and a state convention are "
          "none of them acts of congressional compromise as this sentence describes them."),

 dict(q="KC-4.3.II.C calls the tensions it describes GROWING. What does that word establish "
        "about the period the sentence covers?",
      choices=[
        "The disagreement over slavery was intensifying rather than subsiding",
        "The disagreement over slavery was subsiding across the period",
        "The disagreement over slavery held steady across the period",
        "The disagreement over slavery began only after the compromises",
        "The disagreement over slavery was confined to Congress"],
      ans=0,
      why="KC-4.3.II.C describes GROWING tensions that compromise stemmed only temporarily, "
          "which is an account of intensification rather than of decline or of a steady "
          "state. The tensions precede the attempts at compromise that stem them, and "
          "KC-4.3.II locates the contests in the acquisition of lands in the West rather than "
          "inside Congress alone."),

 dict(q="How does KC-4.3.II.C sit beneath KC-4.3.II, the concept printed above it?",
      choices=[
        "KC-4.3.II says western acquisition gave rise to contests over extending slavery, and "
        "KC-4.3.II.C reports how Congress responded to them",
        "KC-4.3.II reports how Congress responded, and KC-4.3.II.C says western acquisition "
        "gave rise to the contests",
        "The two sentences concern unrelated questions",
        "KC-4.3.II concerns economic policy while KC-4.3.II.C concerns culture",
        "The two sentences describe the same congressional compromise twice"],
      ans=0,
      why="KC-4.3.II states that the United States' acquisition of lands in the West gave rise "
          "to contests over the extension of slavery into new territories, and KC-4.3.II.C "
          "sits beneath it describing congressional attempts at compromise that only "
          "temporarily stemmed those tensions. Exchanging the two levels, separating them or "
          "assigning either to economics or culture misreads the framework's ordering."),

 dict(q="KC-4.2.III says economic development helped to unify the nation while also "
        "encouraging the growth of different regions. Which sentence on this topic's page "
        "shows that double effect at work in politics?",
      choices=[
        "KC-4.2.III.D, in which plans to unify the economy generated debates potentially "
        "favoring different sections",
        "KC-4.1.I.B, in which federal law was held to take precedence over state law",
        "KC-4.3.I.A.i, in which the government sought influence over North America",
        "KC-4.1.II, in which various groups developed distinctive cultures",
        "KC-4.1.III, in which Americans worked outside government institutions"],
      ans=0,
      why="KC-4.2.III.D is the sub-point printed beneath KC-4.2.III on this topic's page, and "
          "it carries the same doubleness: a plan meant to further unify the economy produced "
          "debate that potentially favoured different sections. The other four sentences "
          "belong to topics 4.2, 4.9 and 4.11 and concern law, foreign policy, culture and "
          "voluntary association rather than the unity of the economy."),

 dict(q="The Politics and Power thematic focus printed on this topic's page names what shapes "
        "government policy, institutions, political parties and the rights of citizens. What "
        "does it name?",
      choices=[
        "Debates fostered by social and political groups about the role of government in "
        "American social, political, and economic life",
        "Decisions of the federal courts about the meaning of the Constitution",
        "The distribution of population between the sections of the country",
        "The pace of innovation in technology and commerce",
        "The formation of voluntary associations outside government"],
      ans=0,
      why="The Politics and Power thematic focus reads that debates fostered by social and "
          "political groups about the role of government in American social, political, and "
          "economic life shape government policy, institutions, political parties, and the "
          "rights of citizens. That is the shaping Unit 4 Learning Objective C asks students "
          "to trace from regional interests into debates about the federal government; court "
          "decisions, population, innovation and voluntary associations are the subjects of "
          "other key concepts."),

 dict(q="Which statement is the suggested skill printed beside this topic's title?",
      choices=[
        "Explain the point of view, purpose, historical situation, and/or audience of a source",
        "Identify a source's point of view, purpose, historical situation, and/or audience",
        "Identify and describe a claim or argument in a source",
        "Explain how claims or evidence support, modify, or refute a source's argument",
        "Use historical reasoning to explain relationships among pieces of historical evidence"],
      ans=0,
      why="Skill 2.B, explain the point of view, purpose, historical situation, and/or "
          "audience of a source, is printed beside this topic's title in service of Unit 4 "
          "Learning Objective C. Skill 2.A is the same list under IDENTIFY and is printed on "
          "topic 4.2; the remaining options are skills 3.A, 3.D and 6.C."),

 dict(q="Suppose a hypothetical speech, its author unnamed, urges a legislature to reject a "
        "plan for unifying the economy on the ground that it would benefit manufacturers at "
        "the expense of farmers. Applying skill 2.B, which statement EXPLAINS the speech's "
        "point of view rather than merely naming it?",
      choices=[
        "It speaks for an agricultural interest, which is why it reads a plan of national "
        "improvement as a transfer to industry",
        "It is opposed to the plan",
        "It was delivered to a legislature",
        "It was delivered while the plan was under debate",
        "It is a speech rather than a petition"],
      ans=0,
      why="Skill 2.B asks the student to EXPLAIN a point of view rather than to identify it, "
          "which means saying what the position rests on and what follows from it. "
          "KC-4.2.III.D supplies the ground: plans to further unify the economy generated "
          "debates over whether they would benefit agriculture or industry. Merely reporting "
          "opposition names the point of view without explaining it, and the remaining "
          "options give the audience, the historical situation and the form of the source."),

 dict(q="An illustrative letter, its author unnamed, asks a member of Congress to support a "
        "compromise on the extension of slavery so that the session may proceed to other "
        "business. Applying skill 2.B, which statement explains the letter's PURPOSE?",
      choices=[
        "It seeks to secure a vote for the compromise by presenting it as the price of "
        "getting other work done",
        "It is addressed to a member of Congress",
        "It was written while the extension of slavery was in dispute",
        "It favours compromise over confrontation",
        "It is a letter rather than a published essay"],
      ans=0,
      why="Skill 2.B asks for an explanation of purpose, which is what the source is trying to "
          "achieve and the means it uses. KC-4.3.II.C describes congressional attempts at "
          "political compromise that only temporarily stemmed growing tensions between "
          "opponents and defenders of slavery, which is the setting rather than the purpose. "
          "The remaining options give the audience, the historical situation, the point of "
          "view and the form."),

 dict(q="Consider a hypothetical petition, unattributed, that asks Congress to keep a duty on "
        "imported cloth and is signed by people in a district of textile mills. Applying skill "
        "2.B, which statement explains the petition's AUDIENCE and why it matters?",
      choices=[
        "It is addressed to Congress because Congress is the body that sets the duty, so the "
        "argument is pitched at national lawmakers rather than at neighbours",
        "Congress is its addressee",
        "It comes from a district of textile mills",
        "It supports keeping the duty",
        "It was signed while the duty was under debate"],
      ans=0,
      why="Skill 2.B asks students to explain the audience rather than name it, which means "
          "saying how the addressee shapes the argument. KC-4.2.III.D places debates over "
          "whether a policy benefits agriculture or industry among the sectional questions of "
          "the period, and KC-4.1.I.D has regional interests underlying leaders' positions on "
          "economic policy. Naming the addressee, the signatories, the position or the date "
          "identifies without explaining."),

 dict(q="Why does the framework treat a source's historical situation as worth explaining "
        "rather than only recording?",
      choices=[
        "The circumstances in which a source was produced help account for the argument it "
        "makes",
        "The circumstances fix the date, which is all a reader needs",
        "The circumstances determine who owns the source",
        "The circumstances matter only for secondary sources",
        "The circumstances are the same as the source's audience"],
      ans=0,
      why="Skill 2.B asks students to explain the historical situation of a source, and skill "
          "2.C asks them to explain how such features might limit its uses, which together "
          "treat circumstance as an explanation of the argument rather than a label on it. "
          "KC-4.1.I.D gives the kind of circumstance that matters here, regional interests "
          "underlying a leader's position, and Unit 4 Learning Objective C asks for exactly "
          "that connection. The situation is not the audience, and the framework applies the "
          "skill to sources of every kind."),

 dict(q="The reasoning process printed beside this topic asks students to set developments "
        "side by side. Which process is it, and what does the framework say it involves?",
      choices=[
        "Comparison, which involves describing and explaining similarities and differences "
        "between developments",
        "Causation, which involves describing causes and effects of a development",
        "Continuity and Change, which involves describing patterns over time",
        "Argumentation, which involves developing a defensible claim",
        "Contextualization, which involves situating a development in a broader context"],
      ans=0,
      why="The unit's own table prints Comparison as this topic's reasoning process, matching "
          "Unit 4 Learning Objective C's demand that students explain how DIFFERENT regional "
          "interests affected debates, and the framework defines Comparison as describing and "
          "explaining similarities and differences between historical developments or "
          "processes. Causation and Continuity and Change are the other two reasoning "
          "processes; argumentation and contextualization are skills."),

 dict(q="One aspect of the Comparison reasoning process goes beyond naming a difference. Which "
        "does the framework state?",
      choices=[
        "Explain the relative historical significance of similarities and differences between "
        "developments",
        "Explain the relative historical significance of causes and effects",
        "Describe patterns of continuity and change over time",
        "Explain how a relevant context influenced a development",
        "Identify patterns among or connections between developments"],
      ans=0,
      why="Aspect 1.iii of the Comparison reasoning process asks students to explain the "
          "relative historical significance of similarities and differences between different "
          "historical developments or processes, which is what Unit 4 Learning Objective C "
          "requires when regional interests are weighed against national concerns as "
          "KC-4.1.I.D describes. The weighing of causes and effects is aspect 2.v of "
          "Causation, patterns over time belong to Continuity and Change, context to aspect "
          "2.iv, and identifying patterns to skill 5.A."),

 dict(q="What separates the Comparison reasoning process from the Causation reasoning process "
        "as the framework defines them?",
      choices=[
        "Comparison sets developments beside one another, while Causation traces what "
        "produced a development and what followed from it",
        "Comparison traces what produced a development, while Causation sets developments "
        "beside one another",
        "Comparison applies to sources and Causation applies to events",
        "Comparison belongs to Unit 4 and Causation to later units",
        "The two processes are defined identically in the framework"],
      ans=0,
      why="The framework defines Comparison by similarities and differences between "
          "developments and Causation by causes, effects and the relationship between them, "
          "so the second option exchanges the two definitions. Both processes are applied to "
          "developments rather than being split between sources and events, and both appear "
          "within Unit 4, Comparison here under Unit 4 Learning Objective C and Causation on "
          "topics 4.2, 4.4, 4.5 and others."),

 dict(q="Which of this topic's three historical developments concerns economic policy rather "
        "than the politics of slavery?",
      choices=[
        "Debates over whether plans to unify the economy would benefit agriculture or industry",
        "Congressional attempts at compromise that only temporarily stemmed tensions",
        "Tensions between opponents and defenders of slavery",
        "The contests raised by the acquisition of lands in the West",
        "Positions on slavery resting on regional rather than national interests"],
      ans=0,
      why="KC-4.2.III.D is the economic sentence on this page, concerning plans to further "
          "unify the U.S. economy and the debate over whether they would benefit agriculture "
          "or industry. The others come from KC-4.3.II.C, KC-4.3.II and KC-4.1.I.D and "
          "concern the politics of slavery, although KC-4.1.I.D also names economic policy "
          "alongside it."),

 dict(q="A hypothetical class summary states that once Congress had passed its compromise, the "
        "dispute over slavery was closed. Which sentence on this page contradicts it most "
        "directly?",
      choices=[
        "KC-4.3.II.C, which says such compromises only temporarily stemmed growing tensions",
        "KC-4.2.III.D, which describes debates over agriculture and industry",
        "KC-4.1.I.D, which names economic policy among the subjects of regional division",
        "KC-4.2.III, which describes economic development unifying the nation",
        "KC-4.1.I, which describes an expanding suffrage"],
      ans=0,
      why="KC-4.3.II.C states that congressional attempts at political compromise only "
          "temporarily stemmed growing tensions between opponents and defenders of slavery, "
          "which is precisely the denial that the question was closed. The other sentences "
          "concern economic debate, the franchise and the unifying effects of economic "
          "development, none of which speaks directly to whether a compromise settled the "
          "dispute."),

 dict(q="A hypothetical division list records how three sections voted on a plan to further "
        "unify the economy. Which conclusion do the figures support?",
      table=_T_SECTIONS,
      choices=[
        "The sections divide, with two supporting the plan and one opposing it",
        "All three sections support the plan",
        "All three sections oppose the plan",
        "The sections divide evenly, with votes for and against equal in each",
        "Only one section recorded any votes against the plan"],
      ans=0,
      why="Read from the table alone: the first two rows record far more votes for the plan "
          "than against it and the third records far more against than for, so support is "
          "neither universal nor absent, no row is evenly divided, and all three rows record "
          "some votes against. KC-4.2.III.D describes plans to further unify the U.S. economy "
          "generating debates that potentially favoured different sections of the country."),

 dict(q="Suppose a record of four congressional compromises notes how long each held before "
        "tension over slavery rose again, and whether the underlying disagreement was "
        "resolved. What does the record support?",
      table=_T_COMPROMISE,
      choices=[
        "Every compromise was followed by renewed tension, and none resolved the underlying "
        "disagreement",
        "Every compromise resolved the underlying disagreement",
        "Tension rose again after only one of the four compromises",
        "The interval before tension rose again lengthens with each compromise",
        "The record shows no compromise holding for more than a year"],
      ans=0,
      why="Read from the table alone: the final column reads the same in all four rows and "
          "records no resolution, every row records a positive number of years before tension "
          "rose again, the intervals shorten rather than lengthen, and each is longer than a "
          "year. KC-4.3.II.C states that congressional attempts at political compromise only "
          "temporarily stemmed growing tensions between opponents and defenders of slavery."),

 dict(q="A hypothetical list pairs five leaders with the region each represents and the "
        "position each took on a proposed economic measure. Which reading does the list "
        "support?",
      table=_T_LEADERS,
      choices=[
        "Leaders from the same region take the same position, and the positions differ "
        "between regions",
        "Leaders from the same region take opposing positions",
        "All five leaders take the same position on the measure",
        "Only one region is represented by more than one leader",
        "No two leaders on the list take the same position"],
      ans=0,
      why="Read from the table alone: the two leaders of the first region agree with each "
          "other, the two of the second region agree with each other, the two groups differ, "
          "and both of those regions have more than one leader on the list. That is the "
          "pattern KC-4.1.I.D describes when it says regional interests often trumped "
          "national concerns as the basis for many political leaders' positions on slavery "
          "and economic policy."),

 dict(q="Taking this topic's three historical developments together, which statement best "
        "collects what the framework asserts?",
      choices=[
        "Regional interests often outweighed national concerns in leaders' positions on "
        "slavery and economic policy, plans to unify the economy were argued over as "
        "sectional questions, and congressional compromise stemmed the tensions over slavery "
        "only for a time",
        "National concerns outweighed regional ones, economic plans were adopted without "
        "argument, and congressional compromise settled the question of slavery",
        "Regional interests shaped only economic questions, while slavery was left to the "
        "courts",
        "Economic plans divided the sections, but no compromise on slavery was ever attempted "
        "in Congress",
        "Congress avoided both economic policy and slavery throughout the early republic"],
      ans=0,
      why="The first collects KC-4.1.I.D, KC-4.2.III.D and KC-4.3.II.C in the order the topic "
          "page prints them and adds nothing. The second reverses all three; the third "
          "contradicts KC-4.1.I.D, which names slavery alongside economic policy; the fourth "
          "contradicts KC-4.3.II.C's congressional attempts at compromise; and the fifth "
          "denies all three sentences at once."),
]
