# AP WORLD HISTORY: MODERN 5.7 Economic Developments and Innovations in the Industrial Age
# CED effective Fall 2024, Unit 5 Revolutions, c. 1750 to c. 1900.
# Thematic focus: Economics Systems (ECN). Reasoning process: Continuity and
# Change. Suggested skill 5.B, explain how a historical development or process
# relates to another historical development or process.
#
# Learning objective:
#   Unit 5 LO H  Explain the development of economic systems, ideologies, and
#                institutions and how they contributed to change in the period
#                from 1750 to 1900.
#
# Historical developments relied on, in the framework's own words:
#   KC-5.1.III.A  Western European countries BEGAN abandoning mercantilism and
#                 adopting free trade policies, PARTLY in response to the GROWING
#                 acceptance of Adam Smith's theories of laissez-faire capitalism
#                 and free markets.
#   KC-5.1.III.B  The global nature of trade and production CONTRIBUTED TO the
#                 proliferation of large-scale transnational businesses that
#                 RELIED ON new practices in banking and finance.
#   KC-5.1        The development of industrial capitalism led to increased
#                 standards of living FOR SOME, and to continued improvement in
#                 manufacturing methods that increased the availability,
#                 affordability, and variety of consumer goods.
#
# Illustrative examples printed on this topic's page:
#   Transnational businesses: Hong Kong and Shanghai Banking Corporation (HSBC);
#     Unilever based in England and the Netherlands and operating in British West
#     Africa and the Belgian Congo.
#   Financial instruments: Stock markets; Limited-liability corporations.
#
# THE FOUR HEDGES THAT CARRY THIS TOPIC, and the items that turn on each:
#   1. "FOR SOME" in KC-5.1. The framework says industrial capitalism raised
#      standards of living for SOME, and this is the single easiest wrong key in
#      the unit -- a student who half-knows the material will key a general rise.
#      Items 13, 14, 22, 23, 26 and 30 all hold that qualification.
#   2. "BEGAN abandoning" in KC-5.1.III.A. A shift under way, not one completed.
#      Items 4 and 24 turn on it, and the table in 24 leaves protection still in
#      place in the last decade for exactly that reason.
#   3. "PARTLY in response to" in KC-5.1.III.A. Adam Smith's theories are one part
#      of the reason and the framework does not make them the whole of it. Item 3.
#   4. "CONTRIBUTED TO" in KC-5.1.III.B, not caused outright. Items 7 and 18.
#
# ON THE DIRECTION OF THE ARROWS. All three statements are causal and all three
# are easy to state backwards: it is the growing acceptance of the theories that
# helped move the countries off mercantilism, it is the GLOBAL NATURE OF TRADE
# that contributed to the businesses, and it is the IMPROVEMENT IN MANUFACTURING
# METHODS that increased the availability of consumer goods. Items 1, 5, 9, 11 and
# 16 carry the reversal as a distractor and their anchors carry both clauses.
#
# WHAT IS NOT KEYED. The framework prints no date for the repeal of any duty, no
# profit or size figure for any firm, no founder for HSBC or Unilever, and no
# statement about WHO the "some" with rising standards of living were. None of
# that is asserted here. Economic imperialism and the commodity trades belong to
# KC-5.2.I.E and KC-5.1.II.C, which are unit 6; the technologies themselves belong
# to KC-5.1.I.B, KC-5.1.I.E and KC-5.1.IV, which are topic 5.5; workers' responses
# belong to KC-5.1.V.A, which is topic 5.8. Those appear here only as distractors.
#
# ON SOURCES AND FIGURES. Section I is stimulus based and this bank cannot display
# images, so every stimulus is a TEXT or a table. No quotation is attributed to a
# real person or document -- each source is explicitly illustrative and
# unattributed. Table figures are HYPOTHETICAL and the stems say so; the CED
# prints no data.
TOPIC = ("5.7", "Economic Developments and Innovations in the Industrial Age", 5)

_T_INCOME = dict(
    headers=["Group in the illustrative sample", "Index of real income, earlier decade",
             "Index of real income, later decade"],
    rows=[["Group 1", "100", "168"],
          ["Group 2", "100", "141"],
          ["Group 3", "100", "99"],
          ["Group 4", "100", "96"]])

_T_TRADE = dict(
    headers=["Decade of the illustrative sample",
             "Share of imports carrying protective duties (percent)",
             "Treaties in force that reduce duties"],
    rows=[["First decade", "74", "1"],
          ["Second decade", "58", "4"],
          ["Third decade", "39", "9"],
          ["Fourth decade", "21", "15"]])

_T_FIRMS = dict(
    headers=["Illustrative firm", "Countries in which the firm operates",
             "Uses the new banking and finance practices"],
    rows=[["Firm 1", "6", "Yes"],
          ["Firm 2", "9", "Yes"],
          ["Firm 3", "1", "No"],
          ["Firm 4", "7", "Yes"]])

QUESTIONS = [
    dict(
        q="What does the course framework say western European countries began to do in this "
          "period?",
        choices=[
            "Abandon mercantilism and adopt free trade policies",
            "Abandon free trade policies and adopt mercantilism",
            "Abandon manufacturing in favor of resource extraction",
            "Prohibit the export of manufactured goods",
            "Replace private ownership of industry with state ownership"],
        ans=0,
        why="KC-5.1.III.A states the direction of the change: western European countries began "
            "abandoning mercantilism and adopting free trade policies. One distractor exchanges "
            "the two policies, so the anchor for this item carries both halves of the sentence.",
    ),
    dict(
        q="Whose theories does the course framework name in its account of the move toward free "
          "trade?",
        choices=[
            "Adam Smith's theories of laissez-faire capitalism and free markets",
            "Karl Marx's account of class conflict",
            "The mercantilist doctrine of a favorable balance of trade",
            "Enlightenment theories of the social contract",
            "The physiocratic doctrine of the primacy of agriculture"],
        ans=0,
        why="KC-5.1.III.A names them: the growing acceptance of Adam Smith's theories of "
            "laissez-faire capitalism and free markets. Marx belongs to KC-5.3.IV.A.ii and the "
            "social contract to KC-5.3.I.A, both of which sit on other topic pages.",
    ),
    dict(
        q="The course framework says western European countries moved away from mercantilism "
          "partly in response to the growing acceptance of one body of economic theory. What does "
          "the word partly establish?",
        choices=[
            "That the framework treats those theories as one part of the reason and does not present them as the whole of it",
            "That the framework treats those theories as the only reason for the change",
            "That the framework denies the theories had any part in the change",
            "That the change was complete before the theories were written",
            "That the theories were accepted everywhere at the same moment"],
        ans=0,
        why="KC-5.1.III.A says PARTLY in response to the growing acceptance of those theories. "
            "The adverb limits the claim, so a key making the theories the sole cause would "
            "assert more than the framework does.",
    ),
    dict(
        q="The course framework writes that western European countries BEGAN abandoning "
          "mercantilism. What does that verb establish about the shift?",
        choices=[
            "That the shift was under way, not that it was complete",
            "That the shift was finished within a single decade",
            "That the shift never actually started",
            "That mercantilism was abandoned everywhere at the same moment",
            "That free trade replaced mercantilism in every state of the world"],
        ans=0,
        why="KC-5.1.III.A says these countries BEGAN abandoning mercantilism, which describes a "
            "process in motion. The framework never says the process finished, and the CED also "
            "states that its developments may continue after the period given.",
    ),
    dict(
        q="A student writes that free trade policies in western Europe produced the acceptance of "
          "laissez-faire theory rather than the other way around. How does the course framework "
          "state the relationship?",
        choices=[
            "The growing acceptance of those theories is part of what moved those countries away from mercantilism",
            "The move away from mercantilism is what produced the acceptance of those theories",
            "The framework describes the two as unconnected",
            "The framework denies that mercantilism was ever abandoned",
            "The framework places the theories after the end of the period"],
        ans=0,
        why="KC-5.1.III.A makes the policy change the thing explained and the growing acceptance "
            "of the theories part of the explanation. The anchor carries both clauses because a "
            "distractor exchanges them, and the framework's own hedge partly is preserved in the "
            "keyed wording.",
    ),
    dict(
        q="Which countries does the course framework name as beginning to abandon mercantilism "
          "for free trade policies?",
        choices=[
            "Western European countries",
            "Every country in the world",
            "The states of East Asia",
            "The empires of the Middle East",
            "The newly independent states of the Americas"],
        ans=0,
        why="KC-5.1.III.A names western European countries and no others. The framework's other "
            "statements about regions in this unit, such as KC-5.1.I.D and KC-5.1.II.B, belong to "
            "topic 5.4 and make different claims, so nothing wider can be keyed here.",
    ),
    dict(
        q="According to the course framework, what contributed to the proliferation of "
          "large-scale transnational businesses?",
        choices=[
            "The global nature of trade and production",
            "The abandonment of trade between continents",
            "The prohibition of foreign investment by western European states",
            "The concentration of all production within single national markets",
            "The collapse of banking practices during the period"],
        ans=0,
        why="KC-5.1.III.B says the global nature of trade and production contributed to the "
            "proliferation of large-scale transnational businesses. The verb is contributed to, "
            "which the framework uses rather than a claim of sole cause.",
    ),
    dict(
        q="The course framework says the large-scale transnational businesses of this period "
          "relied on what?",
        choices=[
            "New practices in banking and finance",
            "State ownership of all their assets",
            "The prohibition of stock markets",
            "A return to older methods of barter",
            "The abandonment of trade over long distances"],
        ans=0,
        why="KC-5.1.III.B closes with it: transnational businesses that relied on new practices "
            "in banking and finance. The CED prints stock markets and limited-liability "
            "corporations beside that statement as its illustrative financial instruments.",
    ),
    dict(
        q="A historian argues that large-scale transnational businesses created the global "
          "character of trade and production in this period. How does the course framework order "
          "the two?",
        choices=[
            "The global nature of trade and production contributed to the proliferation of those businesses",
            "The proliferation of those businesses contributed to the global nature of trade and production",
            "The framework treats the two as unconnected",
            "The framework denies that such businesses existed in the period",
            "The framework places both after the period covered by this unit"],
        ans=0,
        why="KC-5.1.III.B puts the global nature of trade and production first and the businesses "
            "second. The anchor carries both clauses because the distractor exchanges them, and "
            "the direction of that sentence is the whole of the answer.",
    ),
    dict(
        q="Which of the following does the course framework print as an illustrative example of a "
          "transnational business on this topic's page?",
        choices=[
            "The Hong Kong and Shanghai Banking Corporation",
            "The guano industries of Peru and Chile",
            "Muhammad Ali's cotton textile industry in Egypt",
            "The Port of Buenos Aires",
            "The rubber trade of the Congo basin"],
        ans=0,
        why="The CED prints two transnational businesses beside KC-5.1.III.B and this is one of "
            "them. The rejected options are illustrative examples printed beside KC-5.1.II.A, "
            "KC-5.1.V.C and KC-5.2.I.E on other topics' pages.",
    ),
    dict(
        q="The course framework prints one transnational business as based in two European "
          "countries and operating in two African territories. Which description matches what it "
          "prints?",
        choices=[
            "Based in England and the Netherlands, operating in British West Africa and the Belgian Congo",
            "Based in British West Africa and the Belgian Congo, operating in England and the Netherlands",
            "Based in England and the Netherlands, operating only within Europe",
            "Based in British West Africa alone, operating throughout Europe",
            "Based in the Belgian Congo, operating in England and the Netherlands"],
        ans=0,
        why="The illustrative example the CED prints beside KC-5.1.III.B gives the base and the "
            "field of operation in that order. Three distractors exchange them, so the anchor "
            "carries both clauses rather than the base alone.",
    ),
    dict(
        q="Which pair does the course framework print as illustrative financial instruments on "
          "this topic's page?",
        choices=[
            "Stock markets and limited-liability corporations",
            "Guilds and apprenticeship contracts",
            "Tariffs and navigation acts",
            "Land grants and manorial dues",
            "Guano contracts and rubber concessions"],
        ans=0,
        why="The CED prints exactly that pair under the heading financial instruments beside "
            "KC-5.1.III.B, which is the statement about businesses relying on new practices in "
            "banking and finance. Nothing else on the page is offered as an instrument.",
    ),
    dict(
        q="According to the course framework, what did the development of industrial capitalism "
          "lead to?",
        choices=[
            "Increased standards of living for some, and continued improvement in manufacturing methods",
            "Increased standards of living for everyone in industrial societies",
            "A decline in standards of living for everyone in industrial societies",
            "The end of improvement in manufacturing methods",
            "A fall in the variety of goods available to consumers"],
        ans=0,
        why="KC-5.1 names both consequences in one sentence and qualifies the first of them: "
            "increased standards of living FOR SOME, and continued improvement in manufacturing "
            "methods. Dropping that qualification is the easiest wrong key in this topic.",
    ),
    dict(
        q="The course framework says industrial capitalism led to increased standards of living "
          "for some. What does that qualification establish?",
        choices=[
            "That the framework claims a rise for part of the population and not for all of it",
            "That the framework claims a rise for the whole population",
            "That the framework claims standards of living fell for everyone",
            "That the framework makes no claim about standards of living at all",
            "That the framework confines the rise to the owners of transnational businesses"],
        ans=0,
        why="KC-5.1 says FOR SOME, which limits the claim without saying who benefited. The "
            "framework names no group, so a key identifying one would be supplying something the "
            "CED does not print, and a key generalizing the rise would contradict it.",
    ),
    dict(
        q="What does the course framework say the continued improvement in manufacturing methods "
          "increased?",
        choices=[
            "The availability, affordability, and variety of consumer goods",
            "The price of consumer goods in every market",
            "The number of hours worked in each factory",
            "The share of goods produced by hand in the home",
            "The cost of shipping goods between continents"],
        ans=0,
        why="KC-5.1 names all three together: continued improvement in manufacturing methods that "
            "increased the availability, affordability, and variety of consumer goods. The "
            "framework's list has three items and the key carries all of them.",
    ),
    dict(
        q="A student writes that the growing availability of consumer goods produced the "
          "improvements in manufacturing methods. How does the course framework order the two?",
        choices=[
            "Continued improvement in manufacturing methods increased the availability of consumer goods",
            "The increased availability of consumer goods produced the improvement in manufacturing methods",
            "The framework describes the two as unconnected",
            "The framework denies that manufacturing methods improved",
            "The framework denies that consumer goods became more available"],
        ans=0,
        why="KC-5.1 puts the improvement in methods first and the availability of goods second. "
            "The anchor carries both clauses because a distractor exchanges them, and this "
            "topic's reasoning process asks students to trace exactly such a relationship.",
    ),
    dict(
        q="This topic's learning objective concerns economic systems, ideologies and "
          "institutions. Which question is best matched to it?",
        choices=[
            "How economic systems, ideologies and institutions developed and how they contributed to change in the period",
            "How environmental factors contributed to the beginning of industrial production",
            "How technology shaped economic production over time",
            "How industrialization changed existing social hierarchies",
            "How the causes and effects of the period's revolutions can be explained"],
        ans=0,
        why="Unit 5 Learning Objective H asks for the development of economic systems, "
            "ideologies, and institutions and how they contributed to change in the period from "
            "1750 to 1900. The rejected questions belong to the objectives behind KC-5.1.I.A, "
            "KC-5.1.I.B, KC-5.1.VI.A and KC-5.3.",
    ),
    dict(
        q="This topic's suggested skill asks students to explain how one historical development "
          "relates to another. Which pairing does the course framework itself state on this "
          "topic's page?",
        choices=[
            "The global nature of trade and production, and the spread of large-scale transnational businesses",
            "The organization of workers in unions, and the growth of stock markets",
            "Rapid urbanization, and the abandonment of mercantilism",
            "The development of new social classes, and the acceptance of free market theory",
            "The opening of interior regions by railroads, and the improvement of banking practices"],
        ans=0,
        why="KC-5.1.III.B joins those two developments in one sentence, saying that the first "
            "contributed to the second. The rejected pairings each join a statement from this "
            "page to one from KC-5.1.V.A, KC-5.1.VI.C, KC-5.1.VI.A or KC-5.1.IV, which the "
            "framework nowhere connects.",
    ),
    dict(
        q="An illustrative and unattributed pamphlet from the period argues that duties on "
          "imported grain should be repealed because a trade left to itself enriches both "
          "parties to it. Which framework statement does the pamphlet bear on most directly?",
        choices=[
            "That western European countries began abandoning mercantilism and adopting free trade policies",
            "That the global nature of trade contributed to the spread of transnational businesses",
            "That industrial capitalism raised standards of living for some",
            "That a small number of governments promoted industrial visions of their own",
            "That many workers organized themselves in labor unions"],
        ans=0,
        why="KC-5.1.III.A describes the shift away from mercantilism toward free trade policies, "
            "partly in response to the growing acceptance of theories of free markets. An "
            "argument for repealing a duty on that ground is that shift stated as a claim.",
    ),
    dict(
        q="An illustrative and unattributed prospectus invites subscribers to buy shares in a "
          "company that will trade across three continents, and assures them they can lose no "
          "more than the sum they put in. Which two things named on this topic's page does the "
          "prospectus combine?",
        choices=[
            "A large-scale transnational business and a limited-liability corporation",
            "A state-sponsored industrial program and a labor union",
            "A mercantilist monopoly and a guild charter",
            "A resource export economy and a system of forced labor",
            "A precision machinery works and a chemical plant"],
        ans=0,
        why="KC-5.1.III.B describes large-scale transnational businesses relying on new practices "
            "in banking and finance, and the CED prints stock markets and limited-liability "
            "corporations beside it. Shares sold to subscribers whose loss is capped are those "
            "two things together.",
    ),
    dict(
        q="An illustrative and unattributed shop catalogue from late in the period lists cotton "
          "cloth in a dozen patterns at prices well below those quoted a generation earlier. "
          "Which framework statement does the catalogue illustrate?",
        choices=[
            "That improvement in manufacturing methods increased the availability, affordability and variety of consumer goods",
            "That western European countries adopted free trade policies",
            "That transnational businesses relied on new practices in banking",
            "That workers organized in unions to raise their wages",
            "That governments promoted industrial visions of their own"],
        ans=0,
        why="KC-5.1 ties improved manufacturing methods to the availability, affordability, and "
            "variety of consumer goods, and a catalogue offering more patterns at lower prices "
            "shows all three at once. The rejected options are KC-5.1.III.A, KC-5.1.III.B, "
            "KC-5.1.V.A and KC-5.1.V.C.",
    ),
    dict(
        q="An illustrative and unattributed survey of an industrial district reports that some "
          "households ate better and lived in better rooms than a generation earlier while others "
          "in the same district did not. How does the survey sit with the course framework's "
          "statement about industrial capitalism?",
        choices=[
            "It fits the framework, which says standards of living increased for some",
            "It contradicts the framework, which says standards of living increased for everyone",
            "It contradicts the framework, which says standards of living fell for everyone",
            "It is unrelated, because the framework makes no claim about standards of living",
            "It shows that the framework's statement applies only outside industrial districts"],
        ans=0,
        why="KC-5.1 says the development of industrial capitalism led to increased standards of "
            "living for some. A district in which some households gained and others did not is "
            "precisely what that qualification allows for, so the survey supports rather than "
            "unsettles the statement.",
    ),
    dict(
        q="The table below reports hypothetical index figures for four groups in one illustrative "
          "industrial society. Which conclusion does the table support?",
        table=_T_INCOME,
        choices=[
            "Real income rises for two of the four groups and does not rise for the other two",
            "Real income rises for all four groups",
            "Real income falls for all four groups",
            "Real income is unchanged for every group",
            "Real income rises for three of the four groups"],
        ans=0,
        why="KC-5.1 says industrial capitalism led to increased standards of living for some, and "
            "the sample shows what for some looks like in figures. Both halves of the keyed "
            "conclusion are read from the table, with the earlier and later columns compared row "
            "by row.",
    ),
    dict(
        q="The table below reports hypothetical figures for one illustrative western European "
          "state across four decades. Which conclusion does the table support?",
        table=_T_TRADE,
        choices=[
            "The share of imports carrying protective duties falls in every decade while the number of treaties reducing duties rises, and protection has not disappeared by the last decade",
            "The share of imports carrying protective duties falls to zero by the last decade",
            "The share carrying protective duties rises while the number of such treaties falls",
            "Both figures fall across the four decades",
            "Neither figure changes across the four decades"],
        ans=0,
        why="KC-5.1.III.A says western European countries BEGAN abandoning mercantilism, a shift "
            "under way rather than a completed one, and the table is read the same way: the "
            "protected share falls at every step, the treaties rise at every step, and the share "
            "is still above zero in the final row.",
    ),
    dict(
        q="The table below records hypothetical information for four illustrative firms. Which "
          "conclusion does the table support?",
        table=_T_FIRMS,
        choices=[
            "Every firm operating in more than one country uses the new banking and finance practices, and the one firm confined to a single country does not",
            "Every firm in the sample uses the new banking and finance practices",
            "No firm operating in more than one country uses those practices",
            "The firm operating in the most countries does not use those practices",
            "Every firm in the sample operates in more than one country"],
        ans=0,
        why="KC-5.1.III.B describes large-scale transnational businesses that relied on new "
            "practices in banking and finance, and the sample sorts the same way. The count of "
            "countries and the practice column are both read from the table, with nothing "
            "recalled from outside it.",
    ),
    dict(
        q="Which of the following claims goes beyond what the course framework states about the "
          "economy of this period?",
        choices=[
            "That free trade policies had been adopted by every state in the world by the end of the period",
            "That western European countries began abandoning mercantilism and adopting free trade policies",
            "That the global nature of trade contributed to the spread of large-scale transnational businesses",
            "That those businesses relied on new practices in banking and finance",
            "That industrial capitalism increased standards of living for some"],
        ans=0,
        why="KC-5.1.III.A, KC-5.1.III.B and KC-5.1 state the other four claims. None of them "
            "extends free trade beyond western European countries or says the shift was ever "
            "completed, so a claim of worldwide adoption supplies what the CED does not print.",
    ),
    dict(
        q="Which statement correctly separates the two economic developments the course framework "
          "describes on this topic's page?",
        choices=[
            "One concerns the trade policies of western European states, the other the spread of businesses operating across borders",
            "One concerns the trade policies of western European states, the other the organization of workers into unions",
            "One concerns the growth of cities, the other the spread of businesses operating across borders",
            "Both concern the trade policies of western European states alone",
            "Both concern the spread of businesses operating across borders alone"],
        ans=0,
        why="KC-5.1.III.A is about the trade policies of western European countries and "
            "KC-5.1.III.B is about transnational businesses and the finance they relied on. "
            "Workers' organizations belong to KC-5.1.V.A and urban growth to KC-5.1.VI.C, neither "
            "of which is printed on this page.",
    ),
    dict(
        q="The reasoning process assigned to this topic is continuity and change. Which of the "
          "following would best show that a state's economic institutions had changed across the "
          "period?",
        choices=[
            "A comparison of how businesses were financed at the start and at the end of the period",
            "A list of the state's ambassadors during the period",
            "The names of the largest landholding families in the state",
            "A description of the state's cathedral architecture",
            "The number of soldiers in the state's army in one year"],
        ans=0,
        why="Unit 5 Learning Objective H asks how economic institutions developed and contributed "
            "to change, and KC-5.1.III.B names banking and finance practices as the institutions "
            "in question. A comparison across the period is what a claim of change requires; a "
            "single year cannot show change at all.",
    ),
    dict(
        q="Which of the following does the course framework NOT state about the transnational "
          "businesses it names?",
        choices=[
            "How much profit any of them made",
            "That they were large in scale",
            "That they operated across national borders",
            "That they relied on new practices in banking and finance",
            "That their spread was connected to the global nature of trade and production"],
        ans=0,
        why="KC-5.1.III.B supplies the scale, the cross-border operation, the reliance on new "
            "banking and finance practices and the connection to global trade. It gives no "
            "figure of any kind, so a profit claim would be filling a silence in the CED.",
    ),
    dict(
        q="Which single statement best summarizes what this topic asks students to understand "
          "about economic developments in the industrial age?",
        choices=[
            "Western European trade policy began shifting toward free markets, businesses spread across borders on new financial practices, and industrial capitalism raised living standards for some while making consumer goods more available",
            "Trade policy in western Europe moved toward tighter mercantilist control throughout the period",
            "Businesses of the period remained confined within single national markets",
            "Industrial capitalism raised the standard of living of every person in every society",
            "The framework treats economic ideas as unrelated to economic policy"],
        ans=0,
        why="The summary joins KC-5.1.III.A, KC-5.1.III.B and KC-5.1, and it keeps every hedge "
            "those sentences carry: a shift that began, businesses whose spread was contributed "
            "to rather than caused, and living standards that rose for some. Each rejected option "
            "contradicts one of the three.",
    ),
]
