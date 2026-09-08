# AP U.S. HISTORY 4.5 Market Revolution: Industrialization
# (title copied from US_HISTORY_topics.json)
# Unit 4, Period 4: 1800 to 1848. Thematic focus Work, Exchange, and Technology (WXT).
# Suggested skill 6.B, support an argument using specific and relevant evidence.
# Reasoning process for this topic: Causation.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 4 Learning Objective E
#       Explain the causes and effects of the innovations in technology, agriculture, and
#       commerce over time.
#
#   KC-4.2.I.A    Entrepreneurs helped to create a market revolution in production and
#                 commerce, in which market relationships between producers and consumers
#                 came to prevail as the manufacture of goods became more organized.
#   KC-4.2.I.B    Innovations including textile machinery, steam engines, interchangeable
#                 parts, the telegraph, and agricultural inventions increased the
#                 efficiency of production methods.
#   KC-4.2.I.C    Legislation and judicial systems supported the development of roads,
#                 canals, and railroads, which extended and enlarged markets and helped
#                 foster regional interdependence. Transportation networks linked the
#                 North and Midwest more closely than they linked regions in the South.
#   KC-4.2.III.B  Increasing Southern cotton production and the related growth of Northern
#                 manufacturing, banking, and shipping industries promoted the development
#                 of national and international commercial ties.
#
#   Parent concepts printed in the unit's preview and reviewed at 4.14:
#   KC-4.2.I      New transportation systems and technologies dramatically expanded
#                 manufacturing and agricultural production.
#   KC-4.2        Innovations in technology, agriculture, and commerce powerfully
#                 accelerated the American economy, precipitating profound changes to U.S.
#                 society and to national and regional identities.
#
#   Thematic focus WXT, Work, Exchange, and Technology: "The interplay between markets,
#   private enterprise, labor, technology, and government policy shape the American
#   economy. In turn, economic activity shapes society and government policy and drives
#   technological innovation."
#
#   Skill 6.B: support an argument using specific and relevant evidence, printed with two
#   sub-points -- "Describe specific examples of historically relevant evidence" and
#   "Explain how specific examples of historically relevant evidence support an argument."
#
#   Reasoning process Causation: 2.i describe causes and/or effects; 2.ii explain the
#   relationship between causes and effects; 2.iii explain the difference between primary
#   and secondary causes and between short and long term effects; 2.iv explain how a
#   relevant context influenced a development; 2.v explain the relative historical
#   significance of different causes and effects.
#
# WHAT IS NOT ASSERTED. KC-4.2.I.B names five kinds of innovation without naming an
# inventor, a firm, a place or a date, and KC-4.2.I.C names three kinds of route without
# naming one. Neither does this module. The effects of the market revolution on workers,
# households and social structure are KC-4.2.II's material and belong to topic 4.6.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=,
# and every table and every source is marked hypothetical in its stem.
# PROSE ONLY: no LaTeX; a span of years is written "1800 to 1848", never with a hyphen.
TOPIC = ("4.5", "Market Revolution: Industrialization", 4)

_T_EFFICIENCY = dict(
    headers=["Workshop (hypothetical figures)",
             "Pieces finished per worker in a week before the new machinery",
             "Pieces finished per worker in a week after the new machinery"],
    rows=[["Workshop 1", "18", "44"],
          ["Workshop 2", "22", "51"],
          ["Workshop 3", "15", "39"],
          ["Workshop 4", "26", "58"]])

_T_LINKS = dict(
    headers=["Decade (hypothetical figures)",
             "Tons of freight carried between the North and the Midwest",
             "Tons of freight carried between the North and the South"],
    rows=[["1810 to 1820", "40", "31"],
          ["1820 to 1830", "95", "38"],
          ["1830 to 1840", "180", "44"],
          ["1840 to 1848", "310", "49"]])

_T_TIES = dict(
    headers=["Decade (hypothetical index figures)",
             "Southern cotton production",
             "Northern manufacturing, banking, and shipping"],
    rows=[["1810 to 1820", "20", "25"],
          ["1820 to 1830", "46", "48"],
          ["1830 to 1840", "88", "83"],
          ["1840 to 1848", "150", "141"]])

QUESTIONS = [

 dict(q="Unit 4's Learning Objective E states what students should be able to explain about "
        "innovation. Which is it?",
      choices=[
        "The causes and effects of the innovations in technology, agriculture, and commerce "
        "over time",
        "The similarities and differences between Northern and Southern industry",
        "The causes of the Second Great Awakening",
        "How and why a new national culture developed from 1800 to 1848",
        "The continuities and changes in the experience of African Americans"],
      ans=0,
      why="Unit 4 Learning Objective E reads 'Explain the causes and effects of the "
          "innovations in technology, agriculture, and commerce over time', which is why "
          "Causation is the reasoning process printed beside this topic. The remaining "
          "options are Unit 4 Learning Objectives J, I and L and a comparison this objective "
          "does not name."),

 dict(q="KC-4.2.I.A names the actors who helped bring the market revolution about. Whom does "
        "the framework name?",
      choices=[
        "Entrepreneurs",
        "State legislatures",
        "Federal judges",
        "Foreign investors",
        "Voluntary associations"],
      ans=0,
      why="KC-4.2.I.A states that entrepreneurs helped to create a market revolution in "
          "production and commerce. Legislation and judicial systems appear in KC-4.2.I.C in "
          "a supporting role for transport rather than as the creators of the revolution, and "
          "foreign investors and voluntary associations are named in neither sentence."),

 dict(q="According to KC-4.2.I.A, what came to prevail in the market revolution it describes?",
      choices=[
        "Market relationships between producers and consumers",
        "Household production for the household's own use",
        "Barter between neighbouring farms",
        "Direct purchase of goods by the federal government",
        "Guild control of prices and entry to trades"],
      ans=0,
      why="KC-4.2.I.A states that market relationships between producers and consumers came to "
          "prevail. Household production for its own use is what such relationships displace, "
          "and barter, federal purchasing and guild control appear nowhere in the sentence."),

 dict(q="KC-4.2.I.A pairs the prevailing of market relationships with a change in how goods "
        "were made. What does the framework say happened to the manufacture of goods?",
      choices=[
        "It became more organized",
        "It became less organized",
        "It was taken over by the government",
        "It moved out of workshops and back into households",
        "It ceased in favour of imported goods"],
      ans=0,
      why="KC-4.2.I.A says market relationships came to prevail AS THE MANUFACTURE OF GOODS "
          "BECAME MORE ORGANIZED, so the two changes are joined in one sentence. Becoming "
          "less organized is its negation, and a government takeover, a return to the "
          "household and a turn to imports are not in the sentence."),

 dict(q="KC-4.2.I.B lists the innovations that increased the efficiency of production methods. "
        "Which set does the framework name?",
      choices=[
        "Textile machinery, steam engines, interchangeable parts, the telegraph, and "
        "agricultural inventions",
        "Textile machinery, steam engines, the electric motor, the telegraph, and the reaper "
        "alone",
        "Steam engines, interchangeable parts, the sewing machine, and refrigeration",
        "Textile machinery, canals, banking houses, and joint stock companies",
        "Interchangeable parts, the telegraph, the photograph, and the steam turbine"],
      ans=0,
      why="KC-4.2.I.B names innovations including textile machinery, steam engines, "
          "interchangeable parts, the telegraph, and agricultural inventions. Electric motors, "
          "sewing machines, refrigeration, photography and steam turbines are not in that "
          "list, and canals, banking houses and joint stock companies belong to KC-4.2.I.C "
          "and KC-4.2.III.B rather than to this one."),

 dict(q="What does KC-4.2.I.B say those innovations increased?",
      choices=[
        "The efficiency of production methods",
        "The number of hours worked in a day",
        "The price of manufactured goods",
        "The share of goods made in households",
        "The independence of each region from the others"],
      ans=0,
      why="KC-4.2.I.B states that the innovations it names increased the EFFICIENCY OF "
          "PRODUCTION METHODS. Hours, prices and household production are not in the "
          "sentence, and KC-4.2.I.C describes transport fostering regional INTERDEPENDENCE "
          "rather than independence."),

 dict(q="KC-4.2.I.B ends its list with agricultural inventions. What does including them "
        "establish about the innovation the framework describes?",
      choices=[
        "It reached farming as well as manufacturing",
        "It was confined to manufacturing",
        "It was confined to communication",
        "It reached farming but not manufacturing",
        "It concerned only the movement of goods"],
      ans=0,
      why="KC-4.2.I.B's list runs from textile machinery and steam engines through the "
          "telegraph to agricultural inventions, so it spans manufacture, communication and "
          "farming together, and Unit 4 Learning Objective E names technology, agriculture "
          "and commerce for the same reason. Each rejected option keeps one part of the list "
          "and drops the rest."),

 dict(q="KC-4.2.I.C names what supported the development of roads, canals, and railroads. "
        "Which does the framework name?",
      choices=[
        "Legislation and judicial systems",
        "Foreign loans and royal charters",
        "Voluntary associations and churches",
        "Military engineers acting alone",
        "The market relationships described in the previous sentence"],
      ans=0,
      why="KC-4.2.I.C states that legislation and judicial systems supported the development "
          "of roads, canals, and railroads. Loans, charters, churches and military engineers "
          "are named nowhere in the sentence, and the market relationships of KC-4.2.I.A are "
          "a separate development rather than the support this sentence describes."),

 dict(q="According to KC-4.2.I.C, what did the development of roads, canals, and railroads do?",
      choices=[
        "It extended and enlarged markets and helped foster regional interdependence",
        "It extended and enlarged markets while leaving the regions independent of one another",
        "It reduced the size of markets while binding the regions together",
        "It affected the movement of people but not of goods",
        "It concerned only the region in which each route was built"],
      ans=0,
      why="KC-4.2.I.C states that roads, canals, and railroads extended and enlarged markets "
          "AND helped foster regional interdependence, so both results belong to the "
          "sentence. The next two options each keep one half and reverse the other, and the "
          "last two contradict the enlargement of markets the sentence asserts."),

 dict(q="KC-4.2.I.C's second sentence compares how closely transportation networks tied the "
        "regions together. What does the framework say?",
      choices=[
        "Networks linked the North and Midwest more closely than they linked regions in the "
        "South",
        "Networks linked the North and the South more closely than they linked the Midwest",
        "Networks linked the South and Midwest more closely than they linked the North",
        "Networks linked all three regions equally closely",
        "Networks did not link the regions to one another at all"],
      ans=0,
      why="KC-4.2.I.C's second sentence reads that transportation networks linked the North "
          "and Midwest more closely than they linked regions in the South. The next two "
          "options exchange which regions were most closely tied, and equal linkage or no "
          "linkage contradicts a sentence that draws exactly this comparison."),

 dict(q="What does KC-4.2.I.C's second sentence add to its first?",
      choices=[
        "That the interdependence the routes fostered was uneven between the regions",
        "That the routes fostered no interdependence at all",
        "That legislation played no part in building the routes",
        "That markets were enlarged only in the South",
        "That the routes were built in a single decade"],
      ans=0,
      why="KC-4.2.I.C's first sentence has roads, canals, and railroads fostering regional "
          "interdependence, and its second says the networks linked the North and Midwest "
          "more closely than they linked regions in the South, so the added claim is that the "
          "interdependence was unevenly distributed. Denying the interdependence, denying "
          "legislation's part or confining enlargement to the South each contradict the first "
          "sentence, and no date is given."),

 dict(q="KC-4.2.III.B pairs a Southern development with Northern ones. Which pair does the "
        "framework name?",
      choices=[
        "Increasing Southern cotton production and the growth of Northern manufacturing, "
        "banking, and shipping industries",
        "Increasing Southern manufacturing and the growth of Northern cotton production",
        "Increasing Southern shipping and the growth of Northern agriculture",
        "Declining Southern cotton production and the growth of Northern industry",
        "Increasing Southern cotton production and the decline of Northern banking"],
      ans=0,
      why="KC-4.2.III.B names increasing Southern cotton production and the related growth of "
          "Northern manufacturing, banking, and shipping industries. The second option "
          "exchanges the two regions' activities, and the remaining three reverse the "
          "direction of change in one half of the pair."),

 dict(q="What does KC-4.2.III.B say those developments promoted?",
      choices=[
        "The development of national and international commercial ties",
        "The development of national commercial ties alone",
        "The development of international commercial ties alone",
        "The separation of the Northern and Southern economies",
        "A decline in commerce between the United States and other nations"],
      ans=0,
      why="KC-4.2.III.B states that they promoted the development of NATIONAL AND "
          "INTERNATIONAL commercial ties, so restricting the outcome to either scale drops "
          "half the sentence. Separation and decline are the opposite of promoting ties, and "
          "KC-4.2.III has economic development helping to unify the nation."),

 dict(q="KC-4.2.III.B calls the growth of Northern industries RELATED to increasing Southern "
        "cotton production. What does that word assert?",
      choices=[
        "That the two regions' growth was connected rather than independent",
        "That the two regions' growth happened at the same time but for unconnected reasons",
        "That Northern growth caused Southern cotton production to fall",
        "That Southern cotton production was carried on by Northern firms",
        "That the two regions traded only with other nations and not with one another"],
      ans=0,
      why="KC-4.2.III.B calls the Northern growth RELATED to increasing Southern cotton "
          "production and has the two together promoting national and international "
          "commercial ties, which is a claim of connection rather than coincidence. The "
          "sentence describes both as increasing, so no fall is asserted, and it says nothing "
          "about who owned Southern production or about trade being external only."),

 dict(q="KC-4.2.I, the concept printed above this topic's sub-points, credits new "
        "transportation systems and technologies with a dramatic expansion. Of what?",
      choices=[
        "Manufacturing and agricultural production",
        "Government revenue and public employment",
        "Household production for the household's own use",
        "Foreign shipping alone",
        "The population of the Southern states"],
      ans=0,
      why="KC-4.2.I states that new transportation systems and technologies dramatically "
          "expanded manufacturing and agricultural production, which is the general claim "
          "beneath which KC-4.2.I.A, KC-4.2.I.B and KC-4.2.I.C sit. Revenue, employment, "
          "household production, shipping alone and population are not what that sentence "
          "names."),

 dict(q="The Work, Exchange, and Technology thematic focus printed on this topic's page names "
        "five things whose interplay shapes the American economy. Which set does it give?",
      choices=[
        "Markets, private enterprise, labor, technology, and government policy",
        "Markets, private enterprise, migration, religion, and government policy",
        "Labor, technology, climate, geography, and foreign policy",
        "Markets, banking, education, technology, and the courts",
        "Private enterprise, labor, warfare, technology, and the press"],
      ans=0,
      why="The Work, Exchange, and Technology thematic focus reads that the interplay between "
          "markets, private enterprise, labor, technology, and government policy shape the "
          "American economy, which is the interplay Unit 4 Learning Objective E asks students "
          "to trace. Migration, religion, climate, geography, foreign policy, banking, "
          "education, the courts, warfare and the press are not in that list."),

 dict(q="The same thematic focus adds a second sentence running the other way. What does it "
        "say economic activity does?",
      choices=[
        "It shapes society and government policy and drives technological innovation",
        "It is shaped by society and government policy but shapes nothing in return",
        "It drives technological innovation but has no effect on society",
        "It shapes society but not government policy",
        "It operates independently of society, government and technology alike"],
      ans=0,
      why="The Work, Exchange, and Technology thematic focus reads 'In turn, economic activity "
          "shapes society and government policy and drives technological innovation', so the "
          "influence runs in both directions and reaches all three, which is the interplay Unit 4 "
          "Learning Objective E asks students to explain in both directions. Each rejected option "
          "removes one or more of the three, and the first removes the return direction "
          "entirely, which is what the words IN TURN establish."),

 dict(q="Which statement is the suggested skill printed beside this topic's title?",
      choices=[
        "Support an argument using specific and relevant evidence",
        "Identify the evidence used in a source to support an argument",
        "Explain how claims or evidence support, modify, or refute a source's argument",
        "Make a historically defensible claim",
        "Use historical reasoning to explain relationships among pieces of historical evidence"],
      ans=0,
      why="Skill 6.B, support an argument using specific and relevant evidence, is printed "
          "beside this topic's title in service of Unit 4 Learning Objective E. The remaining "
          "options are skills 3.B, 3.D, 6.A and 6.C, printed beside topics 4.11, 4.8 and 4.14 "
          "or elsewhere in the course."),

 dict(q="Skill 6.B is printed with two sub-points. Which pair does the framework give?",
      choices=[
        "Describe specific examples of historically relevant evidence, and explain how "
        "specific examples support an argument",
        "Describe specific examples of historically relevant evidence, and rank them by "
        "reliability",
        "Identify the audience of a source, and explain its purpose",
        "Compare two sources, and explain which is the more persuasive",
        "Make a defensible claim, and modify it using alternative evidence"],
      ans=0,
      why="Skill 6.B carries two sub-points in the framework: describe specific examples of "
          "historically relevant evidence, and explain how specific examples of historically "
          "relevant evidence support an argument. Ranking by reliability is not one of them, "
          "audience and purpose belong to skills 2.A and 2.B, comparison of sources to skill "
          "3.C, and modifying a claim with alternative evidence to skill 6.D. Unit 4 Learning "
          "Objective E is what 6.B is applied to here."),

 dict(q="A student argues that innovation in this period raised how much a given worker could "
        "produce. Applying skill 6.B, which piece of evidence would most directly support that "
        "argument?",
      choices=[
        "A comparison of output per worker in the same workshops before and after new "
        "machinery was installed",
        "A list of the routes opened between two regions in the same years",
        "The number of banks chartered in the Northern states",
        "The total tonnage of cotton exported from Southern ports",
        "The number of voluntary associations founded in the same decade"],
      ans=0,
      why="Skill 6.B asks students to support an argument with specific and relevant evidence, "
          "and an argument about output per worker is settled by figures for output per "
          "worker. KC-4.2.I.B is the sentence the argument restates, that innovations "
          "including textile machinery and steam engines increased the efficiency of "
          "production methods. Routes, banks, exports and associations bear on KC-4.2.I.C, "
          "KC-4.2.III.B and KC-4.1.III.A instead."),

 dict(q="Another student argues that the routes built in this period tied some regions "
        "together more tightly than others. Under skill 6.B, which evidence would most "
        "directly support that argument?",
      choices=[
        "A comparison of the freight carried between the North and the Midwest with the "
        "freight carried between the North and the South",
        "The total mileage of route built across the whole country",
        "The number of patents issued for agricultural inventions",
        "The output per worker of a single Northern workshop",
        "The value of cotton sold to other nations"],
      ans=0,
      why="KC-4.2.I.C's second sentence makes a comparative claim, that transportation networks "
          "linked the North and Midwest more closely than they linked regions in the South, "
          "so the evidence that bears on it must itself compare two links. Skill 6.B requires "
          "evidence that is relevant as well as specific: a national total, a patent count, "
          "one workshop's output and a cotton value are each specific without speaking to the "
          "comparison."),

 dict(q="A third student argues that Southern and Northern economic growth were connected. "
        "Under skill 6.B, which of the following is specific but NOT relevant to that "
        "argument?",
      choices=[
        "The number of voluntary associations founded in Northern towns in the same decade",
        "Figures for Southern cotton production alongside figures for Northern shipping",
        "The share of Southern cotton handled by Northern merchants",
        "The value of goods carried between Southern ports and Northern ones",
        "Figures for Northern banking alongside figures for Southern cotton exports"],
      ans=0,
      why="Skill 6.B requires evidence to be relevant as well as specific, and KC-4.2.III.B's "
          "claim is about increasing Southern cotton production and the RELATED growth of "
          "Northern manufacturing, banking, and shipping industries. Counts of voluntary "
          "associations belong to KC-4.1.III.A and bear on no economic connection; the other "
          "four each put a Southern quantity beside a Northern one, which is what the "
          "argument needs."),

 dict(q="The reasoning process printed beside this topic asks students to trace what produced "
        "the innovations and what followed from them. Which process is it?",
      choices=[
        "Causation",
        "Comparison",
        "Continuity and Change",
        "Argumentation",
        "Sourcing and Situation"],
      ans=0,
      why="The unit's own table prints Causation as this topic's reasoning process, matching "
          "Unit 4 Learning Objective E's demand for the causes and effects of the innovations "
          "in technology, agriculture, and commerce. Comparison and Continuity and Change are "
          "the other two reasoning processes; argumentation and sourcing are historical "
          "thinking skills."),

 dict(q="One aspect of the Causation reasoning process separates effects by how long they take "
        "to appear. What does the framework ask students to explain?",
      choices=[
        "The difference between primary and secondary causes and between short-term and "
        "long-term effects",
        "The difference between causes that are stated and causes that are not",
        "The difference between similarities and differences",
        "The difference between a source's purpose and its audience",
        "The difference between a claim and the evidence for it"],
      ans=0,
      why="Aspect 2.iii of the Causation reasoning process asks students to explain the "
          "difference between primary and secondary causes and between short and long term "
          "effects, which is the distinction Unit 4 Learning Objective E requires when "
          "innovations are traced over time. Similarities and differences belong to "
          "Comparison, purpose and audience to skill 2.B, and claims and evidence to skill "
          "6.A and skill 6.B."),

 dict(q="What part does government play in the account of industrialisation these sentences "
        "give?",
      choices=[
        "Legislation and judicial systems supported the development of roads, canals, and "
        "railroads",
        "Government built and owned the manufacturing enterprises of the period",
        "Government stood outside the economy of the period entirely",
        "Government set the prices at which manufactured goods were sold",
        "Government created the market relationships between producers and consumers"],
      ans=0,
      why="KC-4.2.I.C gives government its role in these sentences: legislation and judicial "
          "systems supported the development of roads, canals, and railroads. The Work, "
          "Exchange, and Technology thematic focus names government policy among the five "
          "things whose interplay shapes the economy, which rules out standing outside it, "
          "and KC-4.2.I.A credits entrepreneurs rather than government with creating the "
          "market relationships."),

 dict(q="A hypothetical class summary states that the new routes bound every region of the "
        "country together to the same degree. Which sentence contradicts it most directly?",
      choices=[
        "KC-4.2.I.C, which says the networks linked the North and Midwest more closely than "
        "regions in the South",
        "KC-4.2.I.A, which describes market relationships coming to prevail",
        "KC-4.2.I.B, which names innovations increasing efficiency",
        "KC-4.2.III.B, which describes cotton production and Northern industry growing "
        "together",
        "KC-4.2.I, which describes expanded manufacturing and agricultural production"],
      ans=0,
      why="KC-4.2.I.C's second sentence is the direct denial of even integration, since it "
          "states that transportation networks linked the North and Midwest more closely than "
          "they linked regions in the South. The other four sentences concern market "
          "relationships, efficiency, commercial ties and the expansion of production, none "
          "of which speaks to how evenly the routes tied the regions."),

 dict(q="A hypothetical record sets output per worker in four workshops before the new "
        "machinery was installed against output per worker after it. What does the record "
        "support?",
      table=_T_EFFICIENCY,
      choices=[
        "Output per worker is higher after the new machinery in every workshop recorded",
        "Output per worker is lower after the new machinery in every workshop recorded",
        "Output per worker is unchanged in two of the workshops recorded",
        "Output per worker rises in only one of the workshops recorded",
        "The workshop with the lowest output before has the highest output after"],
      ans=0,
      why="Read from the table alone: the second figure exceeds the first in all four rows, so "
          "output rises everywhere rather than falling, holding steady or rising once, and "
          "the workshop lowest before is not the highest after. That is the change KC-4.2.I.B "
          "describes when it says innovations including textile machinery and steam engines "
          "increased the efficiency of production methods."),

 dict(q="Four decades of hypothetical figures set the freight carried between the North and "
        "the Midwest beside the freight carried between the North and the South. Which reading "
        "do the figures support?",
      table=_T_LINKS,
      choices=[
        "Traffic between the North and the Midwest grows much faster than traffic between the "
        "North and the South",
        "Traffic between the North and the South grows much faster than traffic between the "
        "North and the Midwest",
        "Traffic between the North and the South declines across the four decades",
        "The two columns grow at the same rate across the four decades",
        "Traffic between the North and the Midwest is the smaller figure in every decade "
        "recorded"],
      ans=0,
      why="Read from the table alone: the first column rises from a smaller multiple to more "
          "than seven times its opening figure while the second rises by about half, so the "
          "first grows far faster, the second does not decline, the rates differ, and the "
          "first column is the larger in every row. KC-4.2.I.C states that transportation "
          "networks linked the North and Midwest more closely than they linked regions in the "
          "South."),

 dict(q="Suppose a table of index figures sets Southern cotton production beside Northern "
        "manufacturing, banking, and shipping across four decades. What does it support?",
      table=_T_TIES,
      choices=[
        "Both indexes rise together across the four decades recorded",
        "Southern cotton production rises while the Northern index falls",
        "The Northern index rises while Southern cotton production falls",
        "Neither index changes across the four decades recorded",
        "The Northern index is the larger in every decade recorded"],
      ans=0,
      why="Read from the table alone: both columns rise at every step, so neither falls and "
          "neither is unchanged, and the Northern index leads in the first two rows while the "
          "Southern leads in the last two. Growth in step is what KC-4.2.III.B describes when "
          "it calls the growth of Northern manufacturing, banking, and shipping industries "
          "RELATED to increasing Southern cotton production."),

 dict(q="Taking this topic's four historical developments together, which statement best "
        "collects what the framework asserts?",
      choices=[
        "Entrepreneurs helped create a market revolution as manufacture became more organized, "
        "innovations from textile machinery to agricultural inventions raised efficiency, "
        "legislation and courts supported routes that enlarged markets unevenly across the "
        "regions, and Southern cotton grew alongside Northern industry to build commercial "
        "ties at home and abroad",
        "Government built the routes and the factories alike, while entrepreneurs and the "
        "courts played no part",
        "Innovation was confined to manufacturing, and the routes tied every region together "
        "to the same degree",
        "Southern and Northern growth proceeded independently of one another and produced no "
        "commercial ties",
        "Market relationships gave way to household production as the manufacture of goods "
        "became less organized"],
      ans=0,
      why="The first collects KC-4.2.I.A, KC-4.2.I.B, KC-4.2.I.C and KC-4.2.III.B in the order "
          "the topic page prints them and adds nothing. The second contradicts KC-4.2.I.A and "
          "KC-4.2.I.C, the third contradicts KC-4.2.I.B's agricultural inventions and "
          "KC-4.2.I.C's second sentence, the fourth contradicts KC-4.2.III.B's word RELATED, "
          "and the fifth reverses KC-4.2.I.A outright."),
]
