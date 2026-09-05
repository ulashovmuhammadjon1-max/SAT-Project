# AP WORLD HISTORY: MODERN 5.8 Reactions to the Industrial Economy from 1750 to 1900
# CED effective Fall 2024, Unit 5 Revolutions, c. 1750 to c. 1900.
# Thematic focus: Social Interactions and Organization (SIO). Reasoning process:
# Causation. Suggested skill 2.B, explain the point of view, purpose, historical
# situation, and/or audience of a source.
#
# Learning objective:
#   Unit 5 LO I  Explain the causes and effects of calls for changes in industrial
#                societies from 1750 to 1900.
#
# Historical developments relied on, in the framework's own words:
#   KC-5.1.V.D     IN RESPONSE TO the social and economic changes brought about by
#                  industrial capitalism, SOME governments, organizations, and
#                  individuals promoted various types of political, social,
#                  educational, and urban reforms.
#   KC-5.1.V.A     In industrialized states, MANY workers organized themselves,
#                  OFTEN in labor unions, to improve working conditions, limit
#                  hours, and gain higher wages. Workers' movements and political
#                  parties emerged IN DIFFERENT AREAS, promoting alternative
#                  visions of society.
#   KC-5.3.IV.A.ii Discontent with established power structures ENCOURAGED the
#                  development of various ideologies, INCLUDING those espoused by
#                  Karl Marx, and the ideas of socialism and communism.
#   KC-5.1.V.B     IN RESPONSE TO the expansion of industrializing states, SOME
#                  governments in Asia and Africa, INCLUDING the Ottoman Empire and
#                  Qing China, sought to reform and modernize their economies and
#                  militaries. Reform efforts were OFTEN resisted by SOME members
#                  of government or established elite groups.
#
# The CED prints NO illustrative examples on this topic's page. Nothing here names
# a reform act, a union, a party, a strike, a treaty or a date, because the
# framework names none of them for this topic.
#
# THE HEDGES, and the items that turn on each. Every one of these four sentences
# is qualified, and dropping a qualification is how a plausible wrong key ships.
#   "SOME governments, organizations, and individuals"        -- items 2 and 5
#   "MANY workers ... OFTEN in labor unions"                  -- items 6 and 7
#   "IN DIFFERENT AREAS", with no area named                  -- item 9
#   "INCLUDING those espoused by Karl Marx"                    -- item 15
#   "INCLUDING the Ottoman Empire and Qing China"              -- item 21
#   "OFTEN resisted by SOME members of government"            -- items 20 and 26
#
# ON THE DIRECTION OF THE ARROWS. Three of the four statements are responses to
# something, and each reads plausibly backwards: the reforms answered the changes
# industrial capitalism brought, the reform efforts in Asia and Africa answered the
# expansion of industrializing states, and the discontent encouraged the
# ideologies rather than the other way about. Items 4, 16 and 25 carry the
# reversal as a distractor and their anchors carry BOTH clauses.
#
# WHERE THE BORDER WITH TOPIC 5.6 RUNS. KC-5.2.II.A's internal reform in Japan is
# printed on topic 5.6's page, not this one, and KC-5.1.V.B names the Ottoman
# Empire and Qing China. Item 18 turns on that distinction and offers Japan as the
# near miss, because the question asks which states the framework NAMES in this
# statement.
#
# ON SOURCES. This topic's suggested skill is sourcing, so items 23 to 27 ask about
# a source's purpose, point of view, historical situation or audience. Section I is
# stimulus based and the bank cannot display images, so every stimulus is a TEXT or
# a table, and NO quotation is attributed to a real person or document -- each
# source is explicitly illustrative and unattributed. Table figures are
# HYPOTHETICAL and the stems say so; the CED prints no data.
TOPIC = ("5.8", "Reactions to the Industrial Economy from 1750 to 1900", 5)

_T_UNIONS = dict(
    headers=["Decade of the illustrative sample", "Members of labor unions (thousands)",
             "Average hours worked in a week"],
    rows=[["First decade", "12", "72"],
          ["Second decade", "58", "69"],
          ["Third decade", "190", "62"],
          ["Fourth decade", "540", "56"]])

_T_PETITIONS = dict(
    headers=["Illustrative petition", "Demand it makes"],
    rows=[["Petition 1", "That the working day be shortened"],
          ["Petition 2", "That wages be raised"],
          ["Petition 3", "That the workrooms be made safer and better ventilated"],
          ["Petition 4", "That the mill be closed and its machinery destroyed"]])

_T_MEASURES = dict(
    headers=["Illustrative measure", "Type of reform it represents"],
    rows=[["An act extending the vote to more of the population", "Political"],
          ["An act limiting the hours that children may work", "Social"],
          ["An act requiring a school in every district", "Educational"],
          ["An act funding sewers and paving in the growing towns", "Urban"],
          ["An act re-equipping and drilling the standing army", "Military"]])

QUESTIONS = [
    dict(
        q="According to the course framework, what were the political, social, educational and "
          "urban reforms of this period a response to?",
        choices=[
            "The social and economic changes brought about by industrial capitalism",
            "The decline of trade between industrializing states",
            "The abandonment of mercantilism by western European countries",
            "The expansion of the Ottoman Empire into Europe",
            "The growth of state-sponsored visions of industrialization"],
        ans=0,
        why="KC-5.1.V.D opens with the cause: in response to the social and economic changes "
            "brought about by industrial capitalism, some governments, organizations, and "
            "individuals promoted various types of reform. The framework names no other "
            "occasion for them.",
    ),
    dict(
        q="Whom does the course framework name as promoting the reforms it describes in "
          "industrial societies?",
        choices=[
            "Some governments, organizations, and individuals",
            "Every government in the industrializing world",
            "Labor unions and nobody else",
            "Transnational businesses and nobody else",
            "Enlightenment philosophers and nobody else"],
        ans=0,
        why="KC-5.1.V.D names all three together and qualifies them: SOME governments, "
            "organizations, and individuals. The framework neither universalizes the claim nor "
            "confines the reforms to a single kind of promoter.",
    ),
    dict(
        q="Which four kinds of reform does the course framework name in its account of responses "
          "to industrial capitalism?",
        choices=[
            "Political, social, educational, and urban",
            "Military, naval, colonial, and diplomatic",
            "Agricultural, monetary, judicial, and clerical",
            "Religious, artistic, scientific, and literary",
            "Fiscal, commercial, maritime, and industrial"],
        ans=0,
        why="KC-5.1.V.D lists exactly those four types of reform. Military reform appears in the "
            "framework only in KC-5.1.V.B, where it belongs to governments in Asia and Africa "
            "responding to the expansion of industrializing states.",
    ),
    dict(
        q="A student writes that the reform movements of this period brought industrial "
          "capitalism into being. How does the course framework order the two?",
        choices=[
            "Industrial capitalism brought social and economic changes, and the reforms came in response to them",
            "The reforms came first and industrial capitalism followed from them",
            "The framework treats the reforms and industrial capitalism as unconnected",
            "The framework denies that any reforms were promoted in this period",
            "The framework places both outside the period covered by this unit"],
        ans=0,
        why="KC-5.1.V.D begins IN RESPONSE TO the social and economic changes brought about by "
            "industrial capitalism, which puts the changes first and the reforms second. This "
            "topic's reasoning process is causation, and the anchor carries both clauses because "
            "a distractor exchanges them.",
    ),
    dict(
        q="The course framework says some governments, organizations and individuals promoted "
          "these reforms. What does that word some establish?",
        choices=[
            "That part of them did so, and the framework does not claim all of them did",
            "That all of them did so",
            "That none of them did so",
            "That only governments did so",
            "That the framework gives the exact proportion that did so"],
        ans=0,
        why="KC-5.1.V.D writes SOME governments, organizations, and individuals, which limits the "
            "claim without counting anyone. The framework prints no figure, so neither a "
            "universal claim nor a proportion can be keyed here.",
    ),
    dict(
        q="Where does the course framework say many workers organized themselves during this "
          "period?",
        choices=[
            "In industrialized states",
            "In states that had not yet begun to industrialize",
            "Only in the countryside",
            "Only in states with no manufacturing at all",
            "In the Ottoman Empire and Qing China alone"],
        ans=0,
        why="KC-5.1.V.A opens with the setting: in industrialized states, many workers organized "
            "themselves. The framework's account of the Ottoman Empire and Qing China is a "
            "separate statement, KC-5.1.V.B, and it is about governments rather than workers.",
    ),
    dict(
        q="In what form does the course framework say many workers organized themselves?",
        choices=[
            "Often in labor unions",
            "Always in labor unions, without exception",
            "In transnational businesses",
            "In state-sponsored industrial programs",
            "In stock markets and limited-liability corporations"],
        ans=0,
        why="KC-5.1.V.A says many workers organized themselves, OFTEN in labor unions. The "
            "adverb is the framework's own and it stops short of saying always, which is the "
            "difference the two leading options turn on.",
    ),
    dict(
        q="Which three aims does the course framework attach to workers organizing themselves?",
        choices=[
            "To improve working conditions, limit hours, and gain higher wages",
            "To abolish serfdom, expand suffrage, and end slavery",
            "To reform economies and militaries",
            "To promote free trade and reduce duties",
            "To found transnational businesses of their own"],
        ans=0,
        why="KC-5.1.V.A names those three in that order. Suffrage, abolition and the end of "
            "serfdom belong to KC-5.3.I.C, the reform of economies and militaries to KC-5.1.V.B, "
            "and free trade to KC-5.1.III.A, all of which are separate statements.",
    ),
    dict(
        q="The course framework says workers' movements and political parties emerged in "
          "different areas. What does that phrase establish?",
        choices=[
            "That they appeared in more than one place rather than in a single country",
            "That they appeared in every country of the world",
            "That they appeared in only one country",
            "That the framework names the countries in which they appeared",
            "That they appeared only outside industrialized states"],
        ans=0,
        why="KC-5.1.V.A says workers' movements and political parties emerged IN DIFFERENT AREAS "
            "and names none of those areas. The phrase asserts more than one place and nothing "
            "further, so any list of countries would be supplied from outside the CED.",
    ),
    dict(
        q="What does the course framework say the workers' movements and political parties of "
          "this period were promoting?",
        choices=[
            "Alternative visions of society",
            "A return to agricultural production",
            "The expansion of industrializing states into Asia and Africa",
            "The abandonment of mercantilism for free trade",
            "State-sponsored visions of industrialization"],
        ans=0,
        why="KC-5.1.V.A closes with the phrase: workers' movements and political parties emerged "
            "in different areas, promoting alternative visions of society. State-sponsored "
            "visions belong to KC-5.1.V.C and free trade to KC-5.1.III.A.",
    ),
    dict(
        q="The table below reports hypothetical figures for one illustrative industrialized state "
          "across four decades. Which conclusion does the table support?",
        table=_T_UNIONS,
        choices=[
            "Union membership rises in every decade while the average hours worked in a week fall in every decade",
            "Union membership and the average hours worked in a week both rise in every decade",
            "Union membership falls while the average hours worked in a week rise",
            "Neither figure changes across the four decades",
            "The average hours worked in a week fall to zero by the fourth decade"],
        ans=0,
        why="KC-5.1.V.A says many workers organized themselves, often in labor unions, to limit "
            "hours among other aims, and the table's two columns move in the directions that "
            "statement pairs. Both readings come from the table itself; the table shows the "
            "movement of the figures and the framework supplies the aim.",
    ),
    dict(
        q="According to the course framework, what encouraged the development of the various "
          "ideologies of this period?",
        choices=[
            "Discontent with established power structures",
            "Satisfaction with established power structures",
            "The growth of transnational banking practices",
            "The spread of railroads into interior regions",
            "The reform of economies and militaries in Asia and Africa"],
        ans=0,
        why="KC-5.3.IV.A.ii opens with the cause: discontent with established power structures "
            "encouraged the development of various ideologies. One distractor inverts the noun "
            "into its opposite, which is why the anchor carries the discontent itself.",
    ),
    dict(
        q="Whose ideas does the course framework name among the ideologies that discontent "
          "encouraged?",
        choices=[
            "Those espoused by Karl Marx",
            "Those espoused by Adam Smith",
            "Those espoused by the mercantilist writers",
            "Those espoused by the physiocrats",
            "Those espoused by the defenders of established power structures"],
        ans=0,
        why="KC-5.3.IV.A.ii names him: various ideologies, including those espoused by Karl Marx. "
            "Adam Smith is named in KC-5.1.III.A instead, in the framework's account of free "
            "trade and laissez-faire capitalism.",
    ),
    dict(
        q="Which two ideas does the course framework name alongside the ideologies that "
          "discontent encouraged?",
        choices=[
            "Socialism and communism",
            "Mercantilism and protectionism",
            "Laissez-faire capitalism and free markets",
            "Liberalism and constitutional monarchy",
            "Nationalism and imperialism"],
        ans=0,
        why="KC-5.3.IV.A.ii names the ideas of socialism and communism. Democracy and "
            "19th-century liberalism belong to KC-5.3.IV.A.i and laissez-faire capitalism to "
            "KC-5.1.III.A, so neither can be keyed to this statement.",
    ),
    dict(
        q="The course framework introduces the ideologies of this period with the word including. "
          "What does that word establish?",
        choices=[
            "That the ideologies named are examples and the framework does not present them as the only ones",
            "That the ideologies named are the only ones that developed",
            "That no ideologies developed during the period",
            "That the framework gives a complete count of the ideologies",
            "That the ideologies named developed outside the period"],
        ans=0,
        why="KC-5.3.IV.A.ii says various ideologies, INCLUDING those espoused by Karl Marx. The "
            "word various and the word including both leave the list open, so a key treating the "
            "named ideas as exhaustive would claim more than the framework does.",
    ),
    dict(
        q="A student writes that the new ideologies of this period created the discontent with "
          "established power structures. How does the course framework order the two?",
        choices=[
            "Discontent with established power structures encouraged the development of the ideologies",
            "The ideologies encouraged the development of discontent with established power structures",
            "The framework treats the two as unconnected",
            "The framework denies that any new ideologies developed",
            "The framework places both before the beginning of the period"],
        ans=0,
        why="KC-5.3.IV.A.ii puts the discontent first and the ideologies second. The anchor "
            "carries both clauses because the distractor exchanges them, and this topic's "
            "reasoning process is causation, so the order of the sentence is the answer.",
    ),
    dict(
        q="According to the course framework, what were the reform efforts of some governments in "
          "Asia and Africa a response to?",
        choices=[
            "The expansion of industrializing states",
            "The collapse of industrial production in Europe",
            "The organization of workers into labor unions",
            "The growing acceptance of laissez-faire theory",
            "The proliferation of transnational businesses"],
        ans=0,
        why="KC-5.1.V.B opens with it: in response to the expansion of industrializing states, "
            "some governments in Asia and Africa sought to reform and modernize. The framework "
            "names no other occasion for those efforts.",
    ),
    dict(
        q="Which two states does the course framework name in its statement about governments in "
          "Asia and Africa that sought to reform and modernize?",
        choices=[
            "The Ottoman Empire and Qing China",
            "Japan and Russia",
            "Egypt and Argentina",
            "Britain and the Netherlands",
            "Peru and Chile"],
        ans=0,
        why="KC-5.1.V.B names those two and no others. The framework's statement about internal "
            "reform in Japan is KC-5.2.II.A, printed on a different topic's page, which is what "
            "makes the second option a near miss rather than a second correct answer.",
    ),
    dict(
        q="What does the course framework say those governments sought to reform and modernize?",
        choices=[
            "Their economies and militaries",
            "Their economies but not their militaries",
            "Their militaries but not their economies",
            "Their systems of religious instruction",
            "Their systems of land tenure"],
        ans=0,
        why="KC-5.1.V.B names both together: these governments sought to reform and modernize "
            "their economies and militaries. The framework mentions neither religious instruction "
            "nor land tenure anywhere in this statement.",
    ),
    dict(
        q="According to the course framework, what happened to those reform efforts?",
        choices=[
            "They were often resisted by some members of government or established elite groups",
            "They were welcomed without opposition by every group in those states",
            "They were resisted only by workers in the new factories",
            "They were abandoned before any of them began",
            "They were imposed from outside by the industrializing states"],
        ans=0,
        why="KC-5.1.V.B closes with the sentence: reform efforts were often resisted by some "
            "members of government or established elite groups. Both hedges are the framework's "
            "own, and the resistance it names comes from inside those states rather than from "
            "workers or from outside.",
    ),
    dict(
        q="Which of the following claims goes beyond what the course framework states about "
          "reform in Asia and Africa?",
        choices=[
            "That the Ottoman Empire and Qing China were the only governments in Asia and Africa that sought such reform",
            "That some governments in Asia and Africa sought to reform and modernize their economies and militaries",
            "That those efforts were often resisted by some members of government",
            "That the framework names the Ottoman Empire among those governments",
            "That the framework names Qing China among those governments"],
        ans=0,
        why="KC-5.1.V.B says SOME governments in Asia and Africa, INCLUDING the Ottoman Empire "
            "and Qing China. Both words leave the group open, so treating the two named states as "
            "the whole of it asserts something the CED does not print.",
    ),
    dict(
        q="This topic's learning objective concerns calls for change in industrial societies. "
          "Which question is best matched to it?",
        choices=[
            "What caused calls for change in industrial societies and what followed from them",
            "How environmental factors contributed to the beginning of industrial production",
            "How technology shaped economic production over time",
            "How different modes and locations of production changed over time",
            "How the Enlightenment affected societies over time"],
        ans=0,
        why="Unit 5 Learning Objective I asks students to explain the causes and effects of calls "
            "for changes in industrial societies from 1750 to 1900. The rejected questions belong "
            "to the objectives behind KC-5.1.I.A, KC-5.1.I.B, KC-5.1.I.D and KC-5.3.I.A.",
    ),
    dict(
        q="An illustrative and unattributed handbill posted at a mill gate urges the workers there "
          "to combine and to petition together for a shorter day. Considering its purpose and its "
          "intended audience, which framework statement does the handbill belong to?",
        choices=[
            "That many workers organized themselves, often in labor unions, to limit hours",
            "That some governments promoted political, social, educational and urban reforms",
            "That some governments in Asia and Africa sought to reform their economies and militaries",
            "That discontent encouraged the development of new ideologies",
            "That western European countries began adopting free trade policies"],
        ans=0,
        why="KC-5.1.V.A names limiting hours among the aims of workers who organized themselves, "
            "often in labor unions. The handbill's audience is the workers of one mill and its "
            "purpose is to get them to combine, which is that statement rather than any of the "
            "others on the list.",
    ),
    dict(
        q="An illustrative and unattributed circular is addressed by a city council to the "
          "ratepayers of the town, and sets out a plan to drain and pave the poorest streets. "
          "Whose point of view does the circular represent, and which framework statement does it "
          "illustrate?",
        choices=[
            "A government's, illustrating the urban reforms promoted in response to industrial capitalism",
            "A workers' organization's, illustrating the demand for higher wages",
            "A transnational business's, illustrating new practices in banking and finance",
            "An Asian government's, illustrating the reform of economies and militaries",
            "A philosopher's, illustrating the reexamination of religion in public life"],
        ans=0,
        why="KC-5.1.V.D names urban reform among the four types promoted by some governments, "
            "organizations, and individuals in response to the changes industrial capitalism "
            "brought. A council writing to its own ratepayers about drains and paving is a "
            "government promoting exactly that kind of reform.",
    ),
    dict(
        q="An illustrative and unattributed memorial written to a ruler in Asia argues that unless "
          "the army is re-equipped and the state's workshops rebuilt, the country will not hold "
          "its ground against the industrializing powers. Which framework statement does the "
          "memorial's historical situation match?",
        choices=[
            "That some governments in Asia and Africa sought to reform and modernize their economies and militaries in response to the expansion of industrializing states",
            "That the expansion of industrializing states followed from the reform of Asian and African economies",
            "That many workers in Asia organized themselves in labor unions",
            "That discontent with established power structures encouraged socialism and communism",
            "That governments in Europe promoted state-sponsored visions of industrialization"],
        ans=0,
        why="KC-5.1.V.B joins both halves in one sentence: in response to the expansion of "
            "industrializing states, some governments in Asia and Africa sought to reform and "
            "modernize their economies and militaries. The memorial names the workshops and the "
            "army together, and the anchor carries both clauses because a distractor reverses them.",
    ),
    dict(
        q="An illustrative and unattributed minute records senior officials at a court objecting "
          "that a proposed program of workshops and drill would unsettle established ranks. Which "
          "part of the framework's account does the minute illustrate?",
        choices=[
            "That reform efforts were often resisted by some members of government or established elite groups",
            "That reform efforts were welcomed by every group in those states",
            "That reform efforts were resisted only by workers in the new factories",
            "That reform efforts were imposed from outside by industrializing states",
            "That no reform efforts were attempted in Asia or Africa"],
        ans=0,
        why="KC-5.1.V.B says reform efforts were often resisted by some members of government or "
            "established elite groups. Officials of the court objecting that established ranks "
            "would be unsettled are that resistance, coming from inside the government rather "
            "than from workers or from abroad.",
    ),
    dict(
        q="An illustrative and unattributed tract argues that the mills and the land alike should "
          "be held in common, and that the present order rests on the labor of those who own "
          "nothing. Which framework statement does the tract belong to?",
        choices=[
            "That discontent with established power structures encouraged the ideas of socialism and communism",
            "That workers organized in unions to gain higher wages within the existing order",
            "That some governments promoted urban and educational reforms",
            "That western European countries adopted theories of free markets",
            "That some governments in Asia sought to modernize their militaries"],
        ans=0,
        why="KC-5.3.IV.A.ii names the ideas of socialism and communism among the ideologies that "
            "discontent with established power structures encouraged. A tract calling for common "
            "ownership argues against the order itself rather than for terms within it, which is "
            "what separates it from the wage demands of KC-5.1.V.A.",
    ),
    dict(
        q="The table below records the demand made by each of four illustrative petitions. Which "
          "demand falls outside the three aims the course framework attaches to workers "
          "organizing themselves?",
        table=_T_PETITIONS,
        choices=[
            "The demand that the mill be closed and its machinery destroyed",
            "The demand that the working day be shortened",
            "The demand that wages be raised",
            "The demand that the workrooms be made safer and better ventilated",
            "None of the four falls outside those aims"],
        ans=0,
        why="KC-5.1.V.A names three aims: to improve working conditions, limit hours, and gain "
            "higher wages. Three of the petitions in the table match one of those three each, and "
            "the demand to close the mill matches none of them.",
    ),
    dict(
        q="The table below sorts five illustrative measures by the type of reform each represents. "
          "Which type is NOT among those the course framework names in its account of reforms "
          "promoted in industrial societies?",
        table=_T_MEASURES,
        choices=[
            "Military",
            "Political",
            "Social",
            "Educational",
            "Urban"],
        ans=0,
        why="KC-5.1.V.D names political, social, educational, and urban reforms. Military reform "
            "appears in the framework only in KC-5.1.V.B, where governments in Asia and Africa "
            "sought to modernize their economies and militaries, so it is not one of the four "
            "types this statement lists.",
    ),
    dict(
        q="Which single statement best summarizes what this topic asks students to understand "
          "about reactions to the industrial economy?",
        choices=[
            "Workers organized to change their conditions, some governments and individuals promoted reforms, discontent encouraged new ideologies, and some governments in Asia and Africa sought to modernize against resistance",
            "Industrial societies produced no organized response of any kind",
            "Every government of the period resisted all reform without exception",
            "Workers of the period sought only to abolish serfdom and expand suffrage",
            "The framework treats the ideologies of the period as unrelated to discontent"],
        ans=0,
        why="The summary joins KC-5.1.V.A, KC-5.1.V.D, KC-5.3.IV.A.ii and KC-5.1.V.B, the four "
            "statements this topic prints, and it keeps each hedge: some governments, many "
            "workers, and reform often resisted. Each rejected option contradicts one of the four.",
    ),
]
