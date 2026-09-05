# AP WORLD HISTORY: MODERN 5.6 Industrialization: Government's Role from 1750 to 1900
# CED effective Fall 2024, Unit 5 Revolutions, c. 1750 to c. 1900.
# Thematic focus: Governance (GOV). Reasoning process: Causation.
# Suggested skill 5.A, identify patterns among or connections between historical
# developments and processes.
#
# ON THE TITLE. WORLD_HISTORY_topics.json prints this topic as
# "Industrialization: Government's Role from 1750 to 1900" with a CURLY
# apostrophe (U+2019) in "Government's". The CED's topic page splits the title
# across three lines of a narrow column -- "Industrialization:" / "Government's
# Role" / "from 1750 to 1900" -- which is what produced the earlier truncation to
# "Industrialization:". The JSON is right and TOPIC below is copied from it
# verbatim, curly apostrophe included. Nothing in the QUESTIONS text is non-ASCII;
# es_check.style forbids that, and it does not read TOPIC.
#
# Learning objective:
#   Unit 5 LO G  Explain the causes and effects of economic strategies of
#                different states and empires.
#
# Historical developments relied on, in the framework's own words:
#   KC-5.1.V.C  As the influence of the Industrial Revolution grew, a small number
#               of states and governments promoted their own state-sponsored
#               visions of industrialization.
#   KC-5.2.II.A The expansion of U.S. and European influence in Asia led to
#               internal reform in Japan that supported industrialization and led
#               to the growing regional power of Japan in the Meiji Era.
#
# Illustrative example printed on this topic's page, under "State-sponsored
# visions of industrialization":
#   Muhammad Ali's development of a cotton textile industry in Egypt.
#
# THE THREE HEDGES THAT CARRY THIS TOPIC. KC-5.1.V.C is one sentence and every
# word of it is doing work.
#   1. "a SMALL NUMBER of states and governments" -- not all of them, and the
#      framework gives no count. Items 2, 15, 25 and 26 turn on that, and item 20
#      makes the invented count the claim that goes beyond the CED.
#   2. "THEIR OWN state-sponsored visions" -- each government's own program, not
#      one shared model. Item 3.
#   3. "AS the influence of the Industrial Revolution GREW" -- the growing
#      influence is the setting in which those governments acted, and item 21
#      carries the reversal as a distractor.
#
# ON THE DIRECTION OF KC-5.2.II.A. That sentence is a chain with three links, and
# every one of them is easy to state backwards: the expansion of U.S. and European
# influence in Asia LED TO internal reform in Japan, that reform SUPPORTED
# industrialization, and it LED TO the growing regional power of Japan in the
# Meiji Era. Items 9, 19, 24 and 27 carry a reversed link as a distractor and
# their anchors carry BOTH clauses, so an anchor cannot match the swap.
#
# WHAT IS NOT KEYED. The framework names no Japanese official, no date for any
# reform, no count of the states with programs of their own, and nothing about
# what Egypt's textile industry produced or how long it lasted. None of that is
# asserted here. The reasons a region's share of manufacturing fell belong to
# KC-5.1.II.B, which is topic 5.4; workers' responses belong to KC-5.1.V.A, which
# is topic 5.8; the reforms of the Ottoman Empire and Qing China belong to
# KC-5.1.V.B, also topic 5.8. Those appear here only as distractors.
#
# ON SOURCES AND FIGURES. Section I is stimulus based and this bank cannot display
# images, so every stimulus is a TEXT or a table. No quotation is attributed to a
# real person or document: each source is explicitly illustrative and unattributed.
# Table figures are HYPOTHETICAL and the stems say so; the CED prints no data.
TOPIC = ("5.6", "Industrialization: Government’s Role from 1750 to 1900", 5)

_T_STATES = dict(
    headers=["Illustrative state", "Government program of industrialization recorded",
             "Index of manufacturing output in the later decade"],
    rows=[["State 1", "Yes", "210"],
          ["State 2", "No", "104"],
          ["State 3", "No", "98"],
          ["State 4", "Yes", "185"],
          ["State 5", "No", "101"]])

_T_MILLS = dict(
    headers=["Decade of the illustrative sample",
             "Mechanized mills operating under the government program",
             "Share of cloth that was imported (percent)"],
    rows=[["First decade", "4", "82"],
          ["Second decade", "19", "61"],
          ["Third decade", "47", "38"],
          ["Fourth decade", "96", "19"]])

_T_AIMS = dict(
    headers=["Illustrative state", "Stated aim of the government"],
    rows=[["State 1", "The government funds and directs new mills of its own"],
          ["State 2", "The government reforms internal institutions so that industry may grow"],
          ["State 3", "The government promotes an industrial program of its own design"],
          ["State 4", "The government takes no part and leaves all industry to private merchants"]])

QUESTIONS = [
    dict(
        q="What does the course framework say a small number of states and governments did as "
          "the influence of the Industrial Revolution grew?",
        choices=[
            "They promoted their own state-sponsored visions of industrialization",
            "They agreed on a single shared model of industrialization and adopted it together",
            "They withdrew from economic life and left industry entirely to private merchants",
            "They prohibited the use of industrial machinery within their borders",
            "They abandoned manufacturing in favor of agricultural exports"],
        ans=0,
        why="KC-5.1.V.C states it in one sentence: as the influence of the Industrial Revolution "
            "grew, a small number of states and governments promoted their own state-sponsored "
            "visions of industrialization. The rejected options each contradict that sentence "
            "rather than qualifying it.",
    ),
    dict(
        q="The course framework introduces the state programs of this topic with the phrase a "
          "small number of states and governments. What does that phrase establish?",
        choices=[
            "That only a few states and governments took this path, not that most did",
            "That every industrializing state and government took this path",
            "That no state or government took this path during the period",
            "That the framework gives the exact number of such states",
            "That the states involved were all located in western Europe"],
        ans=0,
        why="KC-5.1.V.C says a small number, which is a limit and not a count. The framework "
            "neither claims that most states did this nor supplies a figure, so a key resting on "
            "either would be asserting something the CED does not print.",
    ),
    dict(
        q="The framework says these governments promoted their own visions of industrialization. "
          "What does that wording indicate about the programs?",
        choices=[
            "Each government promoted a program of its own rather than one common program imposed on all",
            "Each government copied one identical program written elsewhere",
            "The programs were designed by private merchants rather than by governments",
            "The programs were the same in every state that adopted one",
            "The framework describes the programs as belonging to no government in particular"],
        ans=0,
        why="KC-5.1.V.C says these states promoted THEIR OWN state-sponsored visions of "
            "industrialization. The possessive is the framework's own word and it points to "
            "programs held separately by each government, which is why no shared or imposed model "
            "can be keyed here.",
    ),
    dict(
        q="Which example does this topic's page in the course framework print under the heading "
          "state-sponsored visions of industrialization?",
        choices=[
            "Muhammad Ali's development of a cotton textile industry in Egypt",
            "The construction of the Port of Buenos Aires with the support of British firms",
            "The Hong Kong and Shanghai Banking Corporation",
            "Rubber extraction in the Amazon and the Congo basin",
            "The guano industries of Peru and Chile"],
        ans=0,
        why="KC-5.1.V.C is the statement this topic's illustrative example is attached to, and "
            "the CED prints exactly one example beside it. The rejected options are illustrative "
            "examples the CED prints on other topics' pages, beside KC-5.2.I.E, KC-5.1.III.B and "
            "KC-5.1.II.A.",
    ),
    dict(
        q="In the framework's printed example of a state-sponsored vision of industrialization in "
          "Egypt, which industry is named?",
        choices=[
            "A cotton textile industry",
            "An iron and steel industry",
            "A shipbuilding industry",
            "A chemical dye industry",
            "A railway equipment industry"],
        ans=0,
        why="The illustrative example the CED prints beside KC-5.1.V.C names the development of a "
            "cotton textile industry in Egypt and no other sector. The framework says nothing "
            "about what else that state produced, so nothing else can be keyed.",
    ),
    dict(
        q="According to the course framework, what led to internal reform in Japan?",
        choices=[
            "The expansion of U.S. and European influence in Asia",
            "The collapse of trade among Asian states",
            "A famine that reduced the population of the Japanese islands",
            "The abolition of serfdom in eastern Europe",
            "The spread of labor unions across industrialized states"],
        ans=0,
        why="KC-5.2.II.A opens with that cause: the expansion of U.S. and European influence in "
            "Asia led to internal reform in Japan. The framework names no other cause for the "
            "reform, and the rejected options belong to other statements or to nothing in the CED "
            "at all.",
    ),
    dict(
        q="The course framework says the internal reform in Japan supported which development?",
        choices=[
            "Industrialization",
            "A return to agricultural self-sufficiency",
            "The organization of workers into labor unions",
            "The expansion of European influence inside Japan",
            "The abandonment of manufacturing for resource export"],
        ans=0,
        why="KC-5.2.II.A says the expansion of outside influence led to internal reform in Japan "
            "THAT SUPPORTED INDUSTRIALIZATION. The middle link of that chain is the framework's "
            "own, and the rejected options substitute developments the sentence does not name.",
    ),
    dict(
        q="What does the course framework name as the outcome of Japan's internal reform in the "
          "Meiji Era?",
        choices=[
            "The growing regional power of Japan",
            "The decline of Japan's power within its region",
            "The unification of Asia under a single government",
            "The end of industrial production in Japan",
            "The withdrawal of Japan from the affairs of its region"],
        ans=0,
        why="KC-5.2.II.A closes with the outcome: the reform supported industrialization and led "
            "to the growing regional power of Japan in the Meiji Era. Two of the rejected options "
            "reverse the direction of that change and the others replace it entirely.",
    ),
    dict(
        q="A student writes that internal reform in Japan caused the expansion of U.S. and "
          "European influence in Asia. How does the course framework order the two?",
        choices=[
            "The expansion of U.S. and European influence in Asia led to internal reform in Japan",
            "Internal reform in Japan led to the expansion of U.S. and European influence in Asia",
            "The framework treats the two as unconnected developments",
            "The framework denies that any internal reform took place in Japan",
            "The framework places both after the Meiji Era had ended"],
        ans=0,
        why="KC-5.2.II.A runs in one direction and the reasoning process for this topic is "
            "causation, so the order of the sentence is the answer: the expansion of influence "
            "comes first and the reform follows it. The anchor for this item carries both clauses "
            "because one distractor exchanges them.",
    ),
    dict(
        q="Which era does the course framework name when it describes Japan's growing regional "
          "power?",
        choices=[
            "The Meiji Era",
            "The era of the first Industrial Revolution in Britain",
            "The era of the Enlightenment",
            "The era of the Atlantic revolutions",
            "The era of the second industrial revolution"],
        ans=0,
        why="KC-5.2.II.A names it: the growing regional power of Japan in the Meiji Era. The "
            "rejected options are periods the framework names in other statements of this unit, "
            "none of which is attached to Japan's reform.",
    ),
    dict(
        q="How does the course framework characterize the scale of Japan's growing power in the "
          "period it describes?",
        choices=[
            "As regional power rather than global power",
            "As global supremacy over every industrialized state",
            "As power confined to a single Japanese province",
            "As power exercised only over European trading companies",
            "As authority over the whole of the Americas"],
        ans=0,
        why="KC-5.2.II.A says the growing REGIONAL power of Japan. The framework's adjective is "
            "regional and it makes no claim beyond that, so a key asserting worldwide power would "
            "be supplying something the CED does not print.",
    ),
    dict(
        q="This topic's learning objective concerns the economic strategies of states and "
          "empires. Which question is best matched to it?",
        choices=[
            "What caused different states and empires to adopt the economic strategies they did, and what followed from them",
            "How workers organized themselves to improve conditions in industrial states",
            "How Enlightenment philosophers reexamined the role of religion in public life",
            "How rapid urbanization produced public health crises in industrial cities",
            "How new social classes developed in industrial societies"],
        ans=0,
        why="Unit 5 Learning Objective G asks students to explain the causes and effects of "
            "economic strategies of different states and empires. The rejected questions belong "
            "to the objectives behind KC-5.1.V.A, KC-5.3.I.A, KC-5.1.VI.C and KC-5.1.VI.A.",
    ),
    dict(
        q="The reasoning process assigned to this topic is causation. An argument that a state's "
          "program of industrialization produced its later manufacturing growth is strongest when "
          "it also does what?",
        choices=[
            "Accounts for other developments that could have produced the same growth",
            "Lists every official who served in the government during the period",
            "Describes the architecture of the buildings the program erected",
            "Names the largest city in each neighboring state",
            "Repeats the program's own stated aims as though they were results"],
        ans=0,
        why="Unit 5 Learning Objective G asks for the causes and effects of a state's economic "
            "strategy, and KC-5.1.V.C states only that such programs were promoted, not that they "
            "were the sole cause of anything. An argument that leaves rival causes unaddressed "
            "therefore claims more than the framework supports.",
    ),
    dict(
        q="This topic's suggested skill asks students to identify connections between historical "
          "developments. What connects the Egyptian cotton textile industry and the internal "
          "reform in Japan as this topic presents them?",
        choices=[
            "Both are cases in which government action, rather than private enterprise alone, supported industrial development",
            "Both are cases in which workers organized in unions to raise their wages",
            "Both are cases in which a government prohibited the use of industrial machinery",
            "Both are cases in which a European power governed the territory directly",
            "Both are cases in which industrial production was abandoned for agriculture"],
        ans=0,
        why="KC-5.1.V.C describes governments promoting industrial visions of their own and "
            "KC-5.2.II.A describes internal reform in Japan that supported industrialization. The "
            "CED prints both on this topic's page, which is the pattern the suggested skill for "
            "the topic asks students to identify.",
    ),
    dict(
        q="The table below reports hypothetical figures for five illustrative states. Which "
          "conclusion does the table support?",
        table=_T_STATES,
        choices=[
            "A government program is recorded in a minority of the states, and both states with one show a higher output index than any state without one",
            "A government program is recorded in a majority of the states in the sample",
            "The states without a government program show the highest output indexes",
            "Every state in the sample records a government program",
            "No state in the sample records a government program"],
        ans=0,
        why="KC-5.1.V.C says a small number of states and governments promoted programs of their "
            "own, and the sample is built to sit with that: the program column is read from the "
            "table and the output indexes are compared from the table, with nothing recalled.",
    ),
    dict(
        q="The table below reports hypothetical figures for one illustrative state across four "
          "decades of a government program. Which conclusion does the table support?",
        table=_T_MILLS,
        choices=[
            "The number of mills rises in every decade while the share of cloth imported falls in every decade",
            "The number of mills and the share of cloth imported both rise in every decade",
            "The number of mills falls while the share of cloth imported rises",
            "Neither figure changes across the four decades",
            "The share of cloth imported reaches zero by the fourth decade"],
        ans=0,
        why="KC-5.1.V.C describes a government promoting an industrial vision of its own, and the "
            "table shows what such a program would look like in figures: both columns are read "
            "from the table, and the import share is still above zero in the last row.",
    ),
    dict(
        q="The table below records the stated aim of a government in each of four illustrative "
          "states. Which state's aim falls outside the framework's account of state-sponsored "
          "visions of industrialization?",
        table=_T_AIMS,
        choices=[
            "State 4",
            "State 1",
            "State 2",
            "State 3",
            "None of the four falls outside that account"],
        ans=0,
        why="KC-5.1.V.C describes governments that PROMOTED industrial visions of their own, and "
            "KC-5.2.II.A describes a government reforming internal institutions in a way that "
            "supported industrialization. A government that takes no part at all is the one aim "
            "in the table that neither statement covers.",
    ),
    dict(
        q="An illustrative and unattributed circular from a government of the period announces "
          "that the treasury will fund new mills, supply them with machinery bought abroad, and "
          "place them under an official of the state. Which framework statement does the circular "
          "illustrate?",
        choices=[
            "That a small number of states and governments promoted industrial programs of their own",
            "That western European countries began abandoning mercantilism and adopting free trade policies",
            "That many workers organized themselves in labor unions to improve working conditions",
            "That railroads, steamships and the telegraph opened interior regions to trade",
            "That new social classes, including the middle class, developed"],
        ans=0,
        why="KC-5.1.V.C is the statement about governments promoting industrialization as a "
            "program of their own, and a treasury funding mills under a state official is that "
            "arrangement. The rejected options are KC-5.1.III.A, KC-5.1.V.A, KC-5.1.IV and "
            "KC-5.1.VI.A, none of which describes a government founding industry.",
    ),
    dict(
        q="An illustrative and unattributed memorandum written in an Asian state records the "
          "arrival of foreign warships and merchants, and urges that the country's institutions "
          "be remade so that it can build industry of its own. Which framework statement does the "
          "memorandum most closely match?",
        choices=[
            "That the expansion of outside influence in Asia led to internal reform that supported industrialization",
            "That internal reform in Asia led to the expansion of outside influence in the region",
            "That workers in Asia organized in unions to shorten the working day",
            "That Asian states abandoned mercantilism in favor of free trade",
            "That rapid urbanization in Asia produced housing shortages"],
        ans=0,
        why="KC-5.2.II.A states that the expansion of U.S. and European influence in Asia led to "
            "internal reform in Japan that supported industrialization. The memorandum is written "
            "as an unattributed illustration of that order of events, and the anchor carries both "
            "clauses because one distractor exchanges them.",
    ),
    dict(
        q="Which of the following claims goes beyond what the course framework states about "
          "government and industrialization in this period?",
        choices=[
            "That a named minister designed the industrial program of every state that had one",
            "That a small number of states and governments promoted industrial visions of their own",
            "That the expansion of U.S. and European influence in Asia led to internal reform in Japan",
            "That the reform in Japan supported industrialization",
            "That Japan's regional power grew in the era the framework names"],
        ans=0,
        why="KC-5.1.V.C and KC-5.2.II.A state the other four claims and name no minister, no "
            "official and no designer of any program. Supplying one would be filling a silence in "
            "the CED from outside it, which HISTORY_BRIEF.md forbids.",
    ),
    dict(
        q="A student writes that the programs of these governments produced the Industrial "
          "Revolution itself. How does the course framework order the two?",
        choices=[
            "The framework makes the growing influence of the Industrial Revolution the setting in which those governments acted",
            "The framework makes the government programs the cause of the Industrial Revolution",
            "The framework treats the two as unconnected developments",
            "The framework denies that any government promoted industrialization",
            "The framework places both outside the period covered by this unit"],
        ans=0,
        why="KC-5.1.V.C opens AS THE INFLUENCE OF THE INDUSTRIAL REVOLUTION GREW and only then "
            "describes what a small number of states and governments did. The growing influence "
            "is the circumstance of the sentence, not its result, and the anchor carries both "
            "halves because a distractor reverses them.",
    ),
    dict(
        q="Which of the following does the course framework present as a government's own "
          "economic strategy rather than as a response by workers?",
        choices=[
            "The promotion of a state-sponsored vision of industrialization",
            "The organization of workers into labor unions",
            "A movement to limit the hours of the working day",
            "A campaign to gain higher wages",
            "The emergence of workers' political parties"],
        ans=0,
        why="KC-5.1.V.C attaches the promotion of industrial visions to states and governments, "
            "while KC-5.1.V.A attaches organizing, shorter hours, higher wages and workers' "
            "parties to the workers themselves. The two statements sit on different topic pages "
            "and the distinction between them is what this item turns on.",
    ),
    dict(
        q="An illustrative and unattributed account describes a ruler who ordered cultivators to "
          "grow a fibre crop and built spinning and weaving works to process it under state "
          "direction. Which of the framework's printed examples does the account most resemble?",
        choices=[
            "Muhammad Ali's cotton textile industry in Egypt",
            "The Hong Kong and Shanghai Banking Corporation",
            "Unilever operating in British West Africa",
            "The guano industries of Peru and Chile",
            "The Port of Buenos Aires built with British support"],
        ans=0,
        why="The illustrative example printed beside KC-5.1.V.C is the development of a cotton "
            "textile industry in Egypt, and cotton grown to supply state-directed spinning and "
            "weaving works is that arrangement. The rejected examples are printed beside "
            "KC-5.1.III.B, KC-5.1.II.A and KC-5.2.I.E on other topics' pages.",
    ),
    dict(
        q="Which pattern does the framework's account of Japan in this period illustrate?",
        choices=[
            "Pressure from outside a state producing reform inside it",
            "Reform inside a state producing pressure from outside it",
            "A state's industry collapsing as soon as outside influence arrives",
            "A state closing itself to outside contact and industrializing in isolation",
            "Outside powers governing a state directly and building its industry for it"],
        ans=0,
        why="KC-5.2.II.A begins with the expansion of U.S. and European influence in Asia and "
            "makes internal reform in Japan the consequence. The suggested skill for this topic "
            "is identifying patterns among developments, and the anchor carries both clauses "
            "because one distractor exchanges the outside pressure and the internal reform.",
    ),
    dict(
        q="Which of the following does the course framework NOT supply in its account of "
          "state-sponsored industrialization?",
        choices=[
            "A count of exactly how many states promoted such a program",
            "A statement that only a small number of states did so",
            "An example of such a program in Egypt",
            "A statement connecting these programs to the growing influence of the Industrial Revolution",
            "A statement that these governments promoted visions of their own"],
        ans=0,
        why="KC-5.1.V.C supplies the limit, the connection to the Industrial Revolution's growing "
            "influence and the possessive, and the CED prints the Egyptian example beside it. It "
            "gives no figure anywhere, so a count is the one item on this list the framework does "
            "not provide.",
    ),
    dict(
        q="An illustrative and unattributed report from a state with no government industrial "
          "program describes mills founded and financed entirely by private merchants. What does "
          "the report show about the framework's statement on state-sponsored visions of "
          "industrialization?",
        choices=[
            "It is consistent with it, because the framework says only a small number of states promoted such programs",
            "It contradicts it, because the framework says every state promoted such a program",
            "It contradicts it, because the framework denies that private merchants founded mills",
            "It is unrelated, because the framework makes no claim about how many states promoted such programs",
            "It shows that the framework's statement applies only after the period of this unit"],
        ans=0,
        why="KC-5.1.V.C limits the claim to a small number of states and governments, so a state "
            "without such a program is exactly what that limit allows for. The framework neither "
            "universalizes the claim nor denies private enterprise, which is why the other "
            "readings fail.",
    ),
    dict(
        q="According to the course framework, what was the relationship between the internal "
          "reform in Japan and Japanese industrialization?",
        choices=[
            "The reform supported industrialization",
            "The reform replaced industrialization with agricultural production",
            "Industrialization preceded the reform and produced it",
            "The framework describes the two as unrelated",
            "The reform ended industrial production in Japan"],
        ans=0,
        why="KC-5.2.II.A places the reform first and industrialization after it, in the phrase "
            "internal reform in Japan THAT SUPPORTED industrialization. One distractor reverses "
            "that order, so the anchor carries the reform and the industrialization together "
            "rather than either alone.",
    ),
    dict(
        q="Which statement about the framework's treatment of governments and industrialization "
          "is accurate?",
        choices=[
            "It names both a government program in Egypt and internal reform in Japan on this topic's page",
            "It names a government program in Egypt but no case anywhere in Asia",
            "It names a case in Japan but no example of a government program anywhere else",
            "It names no examples at all and speaks only in general terms",
            "It names examples drawn only from western Europe"],
        ans=0,
        why="KC-5.1.V.C carries the illustrative example of a cotton textile industry in Egypt "
            "and KC-5.2.II.A carries the internal reform in Japan, and the CED prints both "
            "statements on this one topic page. The rejected options each deny one half of what "
            "the page contains.",
    ),
    dict(
        q="Which claim about Japan in this period goes beyond what the course framework asserts?",
        choices=[
            "That Japan's growing power extended beyond its own region",
            "That the expansion of U.S. and European influence in Asia led to internal reform in Japan",
            "That the internal reform supported industrialization",
            "That Japan's regional power grew during the era the framework names",
            "That the framework names the era in which that power grew"],
        ans=0,
        why="KC-5.2.II.A says regional power and stops there. Extending the claim past the region "
            "adds a reach the sentence does not give it, while the other four options restate "
            "parts of that same sentence.",
    ),
    dict(
        q="Which single statement best summarizes what this topic asks students to understand "
          "about government and industrialization?",
        choices=[
            "A small number of governments promoted industrial programs of their own, and in Japan outside pressure produced internal reform that supported industrialization and growing regional power",
            "Every government of the period ran an identical industrial program",
            "Governments played no part in industrialization anywhere during the period",
            "Industrialization spread only where governments prohibited private enterprise",
            "The framework treats government policy as unrelated to industrial development"],
        ans=0,
        why="The summary joins KC-5.1.V.C and KC-5.2.II.A, which are the two statements this "
            "topic prints, and it keeps both hedges: a small number of governments, and power "
            "that is regional. Each rejected option contradicts one of those two sentences.",
    ),
]
