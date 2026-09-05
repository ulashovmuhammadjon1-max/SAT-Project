# AP WORLD HISTORY: MODERN 5.4 Industrialization Spreads in the Period from 1750 to 1900
# CED effective Fall 2024, Unit 5 Revolutions, c. 1750 to c. 1900.
# Thematic focus: Technology and Innovation (TEC). Reasoning process: Continuity
# and Change. Suggested skill 5.A, identify patterns among or connections between
# historical developments and processes.
#
# Learning objective:
#   Unit 5 LO E  Explain how different modes and locations of production have
#                developed and changed over time.
#
# Historical developments relied on, in the framework's own words:
#   KC-5.1.II.B  The rapid development of steam-powered industrial production in
#                European countries and the U.S. contributed to the increase in
#                these regions' share of global manufacturing during the first
#                Industrial Revolution. While Middle Eastern and Asian countries
#                CONTINUED to produce manufactured goods, these regions' SHARE in
#                global manufacturing declined.
#   KC-5.1.I.D   As new methods of industrial production became more common in
#                parts of northwestern Europe, they spread to other parts of
#                Europe and the United States, Russia, and Japan.
#
# Illustrative examples printed on this topic's page, under "Decline of Middle
# Eastern and Asian share in global manufacturing": shipbuilding in India and
# Southeast Asia; iron works in India; textile production in India and Egypt.
#
# THE DEFECT THIS TOPIC INVITES, AND WHAT IS DONE ABOUT IT. KC-5.1.II.B says the
# SHARE declined and, in the same sentence, that these countries CONTINUED to
# produce manufactured goods. A share can fall while output rises, and the easiest
# wrong key in this whole unit is one that reads the falling share as a collapse
# in production. Items 1, 5, 11, 14, 19 and 26 turn on that distinction, and the
# table in item 5 is built so that a region's output rises and its share falls in
# the same two columns -- recomputed in verify_w5_4.py from the figures alone.
#
# WHAT IS NOT KEYED. The framework gives no reason here for the decline in the
# Middle Eastern and Asian share, no date for any country's industrialization, and
# no ranking among the places named in KC-5.1.I.D. None of those is asserted. The
# reasons Japan industrialized belong to KC-5.2.II.A, which is topic 5.6, and the
# consequences of industrialization for empire belong to unit 6.
#
# The figures in the tables are HYPOTHETICAL and the stems say so; the CED prints
# no manufacturing data.
TOPIC = ("5.4", "Industrialization Spreads in the Period from 1750 to 1900", 5)

_T_SHARES = dict(
    headers=["Region (hypothetical)", "Manufacturing output, earlier year (index)",
             "Manufacturing output, later year (index)",
             "Share of global manufacturing, earlier year (percent)",
             "Share of global manufacturing, later year (percent)"],
    rows=[["Region A", "100", "480", "35", "58"],
          ["Region B", "120", "150", "42", "18"],
          ["Region C", "65", "200", "23", "24"]])

_T_EXAMPLES = dict(
    headers=["Industry named by the framework", "Location named beside it"],
    rows=[["Shipbuilding", "India and Southeast Asia"],
          ["Iron works", "India"],
          ["Textile production", "India and Egypt"]])

QUESTIONS = [
    dict(
        q="According to the course framework, what happened to manufacturing in Middle Eastern "
          "and Asian countries during the first Industrial Revolution?",
        choices=[
            "These countries continued to produce manufactured goods while their share of global manufacturing declined",
            "These countries ceased to produce manufactured goods and their share therefore fell to nothing",
            "These countries increased their share of global manufacturing while output fell",
            "These countries neither produced manufactured goods nor traded in them",
            "These countries held a constant share of global manufacturing throughout"],
        ans=0,
        why="KC-5.1.II.B states both halves in one sentence: while Middle Eastern and Asian "
            "countries continued to produce manufactured goods, these regions' share in global "
            "manufacturing declined. A falling share is not the same as a halt in production, "
            "and the framework says so directly.",
    ),
    dict(
        q="To what does the course framework attribute the increase in the European and United "
          "States share of global manufacturing during the first Industrial Revolution?",
        choices=[
            "The rapid development of steam-powered industrial production",
            "The rapid growth of laboratory chemistry and precision machinery",
            "The reform of the Ottoman and Qing militaries",
            "The organization of workers into labor unions",
            "The abolition of serfdom and the expansion of suffrage"],
        ans=0,
        why="KC-5.1.II.B names the cause explicitly: the rapid development of steam-powered "
            "industrial production in European countries and the U.S. contributed to the "
            "increase in these regions' share of global manufacturing. Chemicals and precision "
            "machinery belong to the second industrial revolution in KC-5.1.I.E.",
    ),
    dict(
        q="According to the course framework, where did new methods of industrial production "
          "become more common before spreading further?",
        choices=[
            "In parts of northwestern Europe",
            "In the interior of the Russian Empire",
            "In the port cities of Southeast Asia",
            "In the cotton districts of Egypt",
            "In the Japanese home islands"],
        ans=0,
        why="KC-5.1.I.D opens by stating that as new methods of industrial production became "
            "more common in parts of northwestern Europe, they spread elsewhere. Russia and "
            "Japan appear in the same sentence as places the methods spread TO, not as the "
            "starting point.",
    ),
    dict(
        q="According to the course framework, to which of the following did new methods of "
          "industrial production spread from parts of northwestern Europe?",
        choices=[
            "Other parts of Europe and the United States, Russia, and Japan",
            "The Ottoman Empire, Qing China, and the Latin American republics",
            "Southeast Asia, West Africa, and the Caribbean",
            "Egypt, India, and the Balkan states",
            "Australia, New Zealand, and the Pacific islands"],
        ans=0,
        why="KC-5.1.I.D names exactly those destinations: other parts of Europe and the United "
            "States, Russia, and Japan. The rejected lists name regions the framework treats "
            "under reform in KC-5.1.V.B, under the declining share in KC-5.1.II.B, or under the "
            "nationalisms of KC-5.3.II.iii.",
    ),
    dict(
        q="The table below reports hypothetical figures for three regions in an earlier and a "
          "later year. Which conclusion does the table support?",
        table=_T_SHARES,
        choices=[
            "One region's output rises between the two years while its share of global manufacturing falls",
            "Every region whose share falls also produces less than it did before",
            "Every region's share of global manufacturing rises between the two years",
            "The region with the largest later share had the largest earlier share as well",
            "No region's output changes between the earlier and the later year"],
        ans=0,
        why="KC-5.1.II.B describes exactly this combination, countries continuing to produce "
            "manufactured goods while their share declined, and the table shows it in figures: "
            "one region's output index rises while its share falls. A share is a proportion of a "
            "growing whole, so the two can move in opposite directions.",
    ),
    dict(
        q="The course framework names an industry in India and Southeast Asia among its "
          "illustrative examples of the decline in the Middle Eastern and Asian share of global "
          "manufacturing. Which industry is it?",
        choices=[
            "Shipbuilding",
            "Steelmaking",
            "Coal mining",
            "Railway construction",
            "Precision machinery"],
        ans=0,
        why="The illustrative examples printed beside KC-5.1.II.B name shipbuilding in India "
            "and Southeast Asia. Steel and precision machinery belong to the second industrial "
            "revolution of KC-5.1.I.E, and railways to KC-5.1.IV, so none of those is on this "
            "list.",
    ),
    dict(
        q="Besides shipbuilding and textiles, the course framework names one further industry in "
          "India among its illustrative examples of a declining share of global manufacturing. "
          "Which industry is it?",
        choices=[
            "Iron works",
            "Shipbuilding",
            "Textile production",
            "Chemical manufacture",
            "Electrical equipment"],
        ans=0,
        why="The illustrative examples printed beside KC-5.1.II.B name iron works in India "
            "alongside shipbuilding and textile production. Chemicals and electrical equipment "
            "are second industrial revolution products under KC-5.1.I.E and are not on this "
            "list.",
    ),
    dict(
        q="The table below lists the industries the course framework names among its "
          "illustrative examples of a declining share of global manufacturing. Which industry "
          "does the framework name in Egypt?",
        table=_T_EXAMPLES,
        choices=[
            "Textile production",
            "Shipbuilding",
            "Iron works",
            "Steam locomotive building",
            "Chemical manufacture"],
        ans=0,
        why="The illustrative examples printed beside KC-5.1.II.B name textile production in "
            "India and Egypt, and the table reproduces the framework's own pairing of industry "
            "with location. Egypt appears beside textiles and beside nothing else on that list.",
    ),
    dict(
        q="The course framework locates the change in regional shares of global manufacturing "
          "within a period it names. Which period is it?",
        choices=[
            "The first Industrial Revolution",
            "The second industrial revolution",
            "The age of the Meiji reforms",
            "The period of transoceanic exploration",
            "The era of decolonization"],
        ans=0,
        why="KC-5.1.II.B places the increase in the European and United States share during the "
            "first Industrial Revolution. The framework names a second industrial revolution "
            "separately in KC-5.1.I.E, and the other options are periods it treats in other "
            "units.",
    ),
    dict(
        q="A student concludes from the course framework that manufacturing in Asia stopped "
          "during the first Industrial Revolution. Which correction does the framework support?",
        choices=[
            "Asian countries continued to produce manufactured goods even as their share of the global total declined",
            "Asian countries stopped producing manufactured goods but regained their share later",
            "Asian countries never produced manufactured goods in any period",
            "Asian countries increased their share while ceasing to produce",
            "The framework makes no statement about Asian manufacturing in this period"],
        ans=0,
        why="KC-5.1.II.B says while Middle Eastern and Asian countries continued to produce "
            "manufactured goods, these regions' share in global manufacturing declined. The "
            "word continued is the framework's own, and it is what a reading of collapse "
            "discards.",
    ),
    dict(
        q="Using the reasoning process assigned to this topic, continuity and change, which "
          "pairing best describes Middle Eastern and Asian manufacturing as the course framework "
          "presents it?",
        choices=[
            "Continuity in the production of manufactured goods, change in the share of the global total",
            "Change in the production of manufactured goods, continuity in the share of the global total",
            "Continuity in both production and share",
            "Change in both, with production and share falling to nothing",
            "Neither continuity nor change, since the framework describes no movement"],
        ans=0,
        why="KC-5.1.II.B supplies one of each: production continued, the share declined. Sorting "
            "which of the two moved is exactly the work the reasoning process for this topic "
            "asks for, and reversing the pair misreads the sentence.",
    ),
    dict(
        q="An illustrative account describes a shipyard in a coastal Asian region still "
          "launching vessels in the later part of the period, though it now supplies a smaller "
          "fraction of the world's new tonnage. Which framework statement does the account "
          "illustrate?",
        choices=[
            "That production continued in these regions while their share of global manufacturing declined",
            "That production in these regions ended and their share therefore reached zero",
            "That new methods of industrial production originated in Southeast Asia",
            "That steam-powered production raised the Asian share of global manufacturing",
            "That shipbuilding was unaffected by any change in this period"],
        ans=0,
        why="KC-5.1.II.B pairs continued production with a declining share, and the framework's "
            "illustrative examples name shipbuilding in India and Southeast Asia among the cases "
            "of that decline. A yard still launching ships with a smaller fraction of the total "
            "is that pairing in a single scene.",
    ),
    dict(
        q="This topic's learning objective concerns modes and locations of production. Which "
          "question is best matched to it?",
        choices=[
            "Where industrial production was carried on, and how the way it was organized changed",
            "Which philosophers wrote about natural rights and the social contract",
            "How governments harnessed a sense of commonality to foster unity",
            "Which reform movements contributed to the expansion of rights",
            "How rapid urbanization affected public health in industrial cities"],
        ans=0,
        why="Unit 5 Learning Objective E asks students to explain how different modes and "
            "locations of production have developed and changed over time. The rejected "
            "questions belong to the objectives behind KC-5.3.I.A, KC-5.3.II.ii, KC-5.3.I.C and "
            "KC-5.1.VI.C.",
    ),
    dict(
        q="Two illustrative regions each doubled their manufacturing output over the same "
          "decades, but one raised its share of global manufacturing and the other lost share. "
          "What must have been true?",
        choices=[
            "Global manufacturing as a whole grew faster than the region that lost share",
            "The region that lost share must have reduced its output",
            "The two regions must have produced identical goods",
            "Global manufacturing as a whole must have shrunk",
            "A share cannot change unless output changes"],
        ans=0,
        why="A share is a proportion of a total, which is why KC-5.1.II.B can state that Middle "
            "Eastern and Asian countries continued to produce manufactured goods while their "
            "share declined. A region growing more slowly than the world total loses share "
            "without producing less.",
    ),
    dict(
        q="Which of the following best describes the pattern the course framework identifies in "
          "the spread of new methods of industrial production?",
        choices=[
            "The methods became common in one part of Europe and then spread to further regions",
            "The methods appeared simultaneously and independently in every region named",
            "The methods spread only within the borders of the country where they first appeared",
            "The methods spread from Japan and Russia into northwestern Europe",
            "The methods were confined to shipbuilding and textile production"],
        ans=0,
        why="KC-5.1.I.D describes a sequence: as new methods became more common in parts of "
            "northwestern Europe, they spread to other parts of Europe and the United States, "
            "Russia, and Japan. Suggested skill 5.A for this topic is identifying that kind of "
            "connection between developments.",
    ),
    dict(
        q="A student writes that the course framework describes new methods of industrial "
          "production spreading from Russia and Japan into northwestern Europe. Which correction "
          "does the framework support?",
        choices=[
            "The methods became common in northwestern Europe and spread from there to Russia and Japan",
            "The methods became common in Russia and Japan and spread from there to northwestern Europe",
            "The framework names no direction of spread at all",
            "The framework names Russia and Japan as the only places the methods reached",
            "The framework denies that the methods spread beyond a single country"],
        ans=0,
        why="KC-5.1.I.D runs in one direction: methods becoming more common in parts of "
            "northwestern Europe spread to other parts of Europe and the United States, Russia, "
            "and Japan. The student has reversed the origin and the destinations named in the "
            "same sentence.",
    ),
    dict(
        q="An illustrative report from a textile district in a region whose share was declining "
          "notes that its looms still work but that cloth from abroad now fills much of the "
          "local market. Which illustrative example named by the course framework does this "
          "district correspond to?",
        choices=[
            "Textile production in India and Egypt",
            "Iron works in India",
            "Shipbuilding in India and Southeast Asia",
            "Steel production in the second industrial revolution",
            "Railway construction in interior regions"],
        ans=0,
        why="The illustrative examples printed beside KC-5.1.II.B name textile production in "
            "India and Egypt among the cases of a declining Middle Eastern and Asian share. The "
            "rejected options name other entries on that list or developments the framework "
            "places under KC-5.1.I.E and KC-5.1.IV.",
    ),
    dict(
        q="Which of the following pairs a mode of production with the location the course "
          "framework associates with its spread in this period?",
        choices=[
            "Steam-powered industrial production, spreading from northwestern Europe to the United States, Russia, and Japan",
            "Steam-powered industrial production, spreading from Egypt to northwestern Europe",
            "Household handloom weaving, spreading from the United States to Asia",
            "Precision machinery production, spreading from India to Europe",
            "Shipbuilding by traditional methods, spreading from Europe into Southeast Asia"],
        ans=0,
        why="KC-5.1.II.B names steam-powered industrial production in European countries and the "
            "U.S., and KC-5.1.I.D names the spread of new methods from parts of northwestern "
            "Europe to other parts of Europe and the United States, Russia, and Japan. The "
            "rejected pairs invert one of those two statements.",
    ),
    dict(
        q="An economist argues that because a region's share of global manufacturing fell by "
          "half, its factories must have closed. Which framework statement most directly "
          "undermines the argument?",
        choices=[
            "That these countries continued to produce manufactured goods while their share declined",
            "That new methods of production spread to Russia and Japan",
            "That the factory system concentrated production in a single location",
            "That railroads and steamships increased trade and migration",
            "That some governments promoted state sponsored visions of industrialization"],
        ans=0,
        why="KC-5.1.II.B holds continued production and a falling share together in one "
            "sentence, so the inference from a falling share to closed works is exactly what "
            "that statement rules out. The rejected options are true framework statements that "
            "say nothing about this inference.",
    ),
    dict(
        q="According to the course framework, which of the following regions saw its share of "
          "global manufacturing increase during the first Industrial Revolution?",
        choices=[
            "European countries and the United States",
            "The Middle East and South Asia",
            "Southeast Asia and East Africa",
            "Egypt and the Ottoman Empire",
            "Latin America and the Caribbean"],
        ans=0,
        why="KC-5.1.II.B attributes the increase in share to European countries and the U.S., "
            "where steam-powered industrial production developed rapidly. The same sentence "
            "places the Middle East and Asia on the declining side, and the framework names no "
            "share for the other regions listed.",
    ),
    dict(
        q="An illustrative survey of one country finds new methods of industrial production in "
          "use decades after they were common in northwestern Europe. What does the course "
          "framework's account of the spread of those methods suggest about this finding?",
        choices=[
            "That the methods spread outward over time rather than appearing everywhere at once",
            "That the methods were invented independently in every country that used them",
            "That the methods were unknown outside northwestern Europe throughout the period",
            "That a later adoption shows the methods were abandoned in Europe",
            "That the framework treats the timing of adoption as identical everywhere"],
        ans=0,
        why="KC-5.1.I.D describes methods becoming more common in parts of northwestern Europe "
            "and then spreading to other parts of Europe and the United States, Russia, and "
            "Japan. Spread of that kind takes time, which is what a later date of adoption "
            "records.",
    ),
    dict(
        q="Which statement about the framework's list of places to which industrial methods "
          "spread is accurate?",
        choices=[
            "It includes places in Europe, in North America and in Asia",
            "It is confined to countries in western Europe",
            "It includes no country outside Europe",
            "It names only countries that had already industrialized",
            "It names only regions whose share of global manufacturing declined"],
        ans=0,
        why="KC-5.1.I.D names other parts of Europe, the United States, Russia and Japan, which "
            "spans three of those areas. The rejected options each shrink or misdescribe the "
            "list the framework prints in that single sentence.",
    ),
    dict(
        q="An illustrative pair of accounts describes the same commodity being made by hand in "
          "one place and by steam-driven machinery in another during the same decades. Which "
          "framework idea does the pair best support?",
        choices=[
            "That different modes of production existed alongside one another as new methods spread",
            "That every producer adopted new methods at the same moment",
            "That handwork ceased everywhere once machinery appeared",
            "That machinery was confined to the region where it was invented",
            "That the framework recognizes only one mode of production in this period"],
        ans=0,
        why="KC-5.1.I.D describes methods spreading gradually from parts of northwestern Europe, "
            "and KC-5.1.II.B has Middle Eastern and Asian countries still producing manufactured "
            "goods throughout. Unit 5 Learning Objective E asks about modes and locations of "
            "production, and coexistence is what a spread in progress looks like.",
    ),
    dict(
        q="A historian wants to test whether a region's manufacturing declined in absolute terms "
          "or only in relative terms. Which evidence would settle the question?",
        choices=[
            "The quantity the region produced in each year, set beside the world total for the same years",
            "The number of ports the region maintained",
            "The titles of the region's trade guilds",
            "The number of languages spoken in the region",
            "The date the region's first steam engine was installed"],
        ans=0,
        why="KC-5.1.II.B distinguishes continued production from a declining share, and only the "
            "region's own output measured against the world total separates the two. The "
            "rejected options gather facts that leave the absolute and relative readings equally "
            "open.",
    ),
    dict(
        q="Which of the following is the best statement of the connection the course framework "
          "draws between steam-powered production and the shares of global manufacturing?",
        choices=[
            "Rapid development of steam-powered production contributed to a rising share for the regions that adopted it",
            "A rising share of global manufacturing caused the development of steam-powered production",
            "Steam-powered production and shares of global manufacturing were unrelated",
            "Steam-powered production lowered the share of every region that adopted it",
            "Shares of global manufacturing were fixed and could not change"],
        ans=0,
        why="KC-5.1.II.B states that the rapid development of steam-powered industrial production "
            "in European countries and the U.S. CONTRIBUTED TO the increase in these regions' "
            "share. The framework puts the technology on the causal side, which the reversed "
            "reading discards.",
    ),
    dict(
        q="An illustrative table of world output shows a region's manufacturing rising by a "
          "fifth while its share of the world total is halved. What does this combination "
          "indicate?",
        choices=[
            "The rest of the world's manufacturing grew far faster than that region's did",
            "The region must have miscounted its own output",
            "The world total must have fallen over the same years",
            "The region's output must in fact have fallen",
            "A share and an output cannot be compared at all"],
        ans=0,
        why="KC-5.1.II.B rests on exactly this arithmetic when it reports continued production "
            "alongside a declining share. A share falls when the denominator grows faster than "
            "the numerator, and nothing about that requires an error or a fall in output.",
    ),
    dict(
        q="According to the course framework, which of the following is true of the United "
          "States in this period?",
        choices=[
            "It is named both among the regions whose share rose and among the places new methods spread to",
            "It is named only among the regions whose share of global manufacturing declined",
            "It is named as the place where new methods of industrial production first became common",
            "It is not named in the framework's account of industrial production",
            "It is named only as a source of raw materials for European works"],
        ans=0,
        why="KC-5.1.II.B places the U.S. with European countries among the regions whose share "
            "of global manufacturing increased, and KC-5.1.I.D names the United States among the "
            "places new methods spread to from parts of northwestern Europe. Both sentences name "
            "it, in different roles.",
    ),
    dict(
        q="A student is asked to identify a pattern connecting the framework's two statements "
          "about this topic. Which pattern is best supported?",
        choices=[
            "Where new methods spread, the share of global manufacturing tended to rise, and where they did not, it tended to fall",
            "Where new methods spread, manufacturing ceased altogether",
            "The share of global manufacturing rose in every region named by the framework",
            "New methods spread only to regions whose share was already falling",
            "The framework's two statements describe unrelated developments"],
        ans=0,
        why="KC-5.1.I.D names the places new methods reached and KC-5.1.II.B names the regions "
            "whose share rose and fell, and the two lists line up. Suggested skill 5.A for this "
            "topic is identifying exactly this kind of connection between developments.",
    ),
    dict(
        q="Which limitation should a student observe when using the course framework's account "
          "of the declining Middle Eastern and Asian share of global manufacturing?",
        choices=[
            "The framework reports the decline without assigning it a cause in this statement",
            "The framework assigns the decline entirely to a shortage of raw materials",
            "The framework assigns the decline entirely to a lack of skilled workers",
            "The framework denies that the decline occurred",
            "The framework dates the decline to the second half of the twentieth century"],
        ans=0,
        why="KC-5.1.II.B records continued production and a declining share and stops there; the "
            "cause it does name belongs to the other half of the sentence, the rapid development "
            "of steam-powered production elsewhere. Supplying a further cause from outside the "
            "CED is what HISTORY_BRIEF.md forbids.",
    ),
    dict(
        q="Which single statement best summarizes what this topic asks students to understand "
          "about the spread of industrialization?",
        choices=[
            "New methods spread outward from northwestern Europe, raising some regions' share of global manufacturing while others kept producing with a smaller share",
            "Industrial methods appeared in every region at once and left shares of manufacturing unchanged",
            "Industrial methods stayed within northwestern Europe for the whole period",
            "Manufacturing outside Europe ended entirely during the first Industrial Revolution",
            "The framework treats the location of production as unchanged throughout the period"],
        ans=0,
        why="The summary joins KC-5.1.I.D's outward spread from parts of northwestern Europe "
            "with KC-5.1.II.B's rising and falling shares and its statement that production "
            "continued. Each rejected option contradicts one of those two sentences.",
    ),
]
