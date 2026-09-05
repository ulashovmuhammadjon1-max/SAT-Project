# AP WORLD HISTORY: MODERN 4.2 Exploration: Causes and Events from 1450 to 1750
# CED effective Fall 2024/2026, Unit 4 Transoceanic Interconnections, c. 1450 to
# c. 1750. Title copied verbatim from WORLD_HISTORY_topics.json.
#
# Unit 4: Learning Objective B -- describe the role of states in the expansion of
# maritime exploration from 1450 to 1750.
# Unit 4: Learning Objective C -- explain the economic causes and effects of
# maritime exploration by the various European states.
# Suggested skill 5.B, explain how a historical development or process relates to
# another historical development or process. Reasoning process: causation.
# Thematic focuses: Governance, and Economic Systems.
#
# Historical developments this module keys to, in the framework's own words:
#   KC-4.1.III    New state-supported transoceanic maritime exploration occurred
#                 in this period.
#   KC-4.1.III.A  Portuguese development of maritime technology and navigational
#                 skills led to increased travel to and trade with Africa and
#                 Asia and resulted in the construction of a global trading-post
#                 empire.
#   KC-4.1.III.B  Spanish sponsorship of the voyages of Columbus and subsequent
#                 voyages across the Atlantic and Pacific dramatically increased
#                 European interest in transoceanic travel and trade.
#   KC-4.1.III.C  Northern Atlantic crossings were undertaken under English,
#                 French, and Dutch sponsorship, often with the goal of finding
#                 alternative sailing routes to Asia.
#
# The framework prints NO illustrative examples beside this topic. That is worth
# recording, because it means every concrete detail in this module has to come
# out of the four statements above or out of an explicitly hypothetical stimulus.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT. The framework gives no dates for
# any voyage, names no ruler, no captain and no ship other than in the phrase
# "the voyages of Columbus", ranks no state's exploration above another's, and
# says nothing about what any expedition found. It does not say the Portuguese
# reached Asia first, nor that the northern crossings succeeded in finding the
# routes they sought -- "often with the goal of" is a statement about aims, not
# outcomes, and several items turn on that distinction.
#
# Dates are written "1450 to 1750". Five choices A-E per HISTORY_BRIEF.md. Every
# stimulus is hypothetical or unattributed; no quotation is put in a real
# person's mouth.
TOPIC = ("4.2", "Exploration: Causes and Events from 1450 to 1750", 4)

_T_SPONSORS = dict(
    headers=["Voyage in a hypothetical register", "Who paid for the voyage",
             "Where the voyage was sent"],
    rows=[["Voyage 1", "A royal treasury", "Around Africa toward Asia"],
          ["Voyage 2", "A royal treasury", "West across the Atlantic"],
          ["Voyage 3", "A royal treasury", "North and west across the Atlantic"],
          ["Voyage 4", "A single merchant house", "A short coastal run inside Europe"]])

_T_BACKING = dict(
    headers=["Decade of a hypothetical register",
             "Voyages beyond European waters with royal backing",
             "Voyages beyond European waters without royal backing"],
    rows=[["First decade", "4", "6"],
          ["Second decade", "11", "7"],
          ["Third decade", "24", "9"],
          ["Fourth decade", "41", "10"]])

_T_GOALS = dict(
    headers=["Expedition in a hypothetical register", "Stated purpose recorded for it"],
    rows=[["Expedition 1", "To reach the trading ports of Asia by sailing around Africa"],
          ["Expedition 2", "To reach Asia by sailing west across the Atlantic"],
          ["Expedition 3", "To find another sailing route to Asia through northern waters"],
          ["Expedition 4", "To survey a river mouth inside the sponsor's own kingdom"]])

QUESTIONS = [
 dict(
  q=("The framework opens its account of exploration in this period with a single sentence "
     "about what was new. What does that sentence say occurred?"),
  choices=[
   "New state-supported transoceanic maritime exploration",
   "New privately financed exploration undertaken against the wishes of rulers",
   "The abandonment of ocean voyaging by every European state",
   "The first crossing of any ocean by any society",
   "The replacement of sea routes by overland routes to Asia"],
  ans=0,
  why=("KC-4.1.III states that new state-supported transoceanic maritime exploration occurred "
       "in this period, which makes state support and ocean crossing the two features the "
       "framework picks out. It does not say voyaging was abandoned, that this was the first "
       "ocean crossing by anyone, or that sea routes gave way to overland ones.")),
 dict(
  q=("Unit 4: Learning Objective B asks students to describe the role of a particular kind of "
     "actor in the expansion of maritime exploration from 1450 to 1750. Which actor?"),
  choices=[
   "States",
   "Monastic orders",
   "Universities",
   "Guilds of shipwrights",
   "Village councils"],
  ans=0,
  why=("Unit 4: Learning Objective B names the role of states, and KC-4.1.III describes the "
       "exploration of the period as state-supported. The framework nowhere assigns the "
       "sponsorship of transoceanic exploration in this period to monasteries, universities, "
       "guilds or village councils.")),
 dict(
  q=("According to the framework, Portuguese development of maritime technology and "
     "navigational skills resulted in the construction of what?"),
  choices=[
   "A global trading-post empire",
   "A settler empire covering the interior of the Americas",
   "A land empire stretching across Central Asia",
   "A confederation of independent Atlantic republics",
   "A network of monasteries along the African coast"],
  ans=0,
  why=("KC-4.1.III.A says Portuguese development of maritime technology and navigational skills "
       "led to increased travel to and trade with Africa and Asia and resulted in the "
       "construction of a global trading-post empire. The framework attributes no interior "
       "settler empire, land empire, republican confederation or monastic network to that "
       "development.")),
 dict(
  q=("The framework says Portuguese maritime technology and navigational skills led to increased "
     "travel to and trade with which regions?"),
  choices=[
   "Africa and Asia",
   "The Americas and the Caribbean",
   "Northern Europe and the Baltic",
   "Australia and the Pacific islands",
   "Central Asia and Siberia"],
  ans=0,
  why=("KC-4.1.III.A names increased travel to and trade with Africa and Asia as what followed "
       "from Portuguese development of maritime technology and navigational skills. The other "
       "regions are not named in that statement, and the transatlantic voyages belong to "
       "KC-4.1.III.B instead.")),
 dict(
  q=("What effect does the framework attribute to Spanish sponsorship of the voyages of Columbus "
     "and the voyages that followed them?"),
  choices=[
   "A dramatic increase in European interest in transoceanic travel and trade",
   "A dramatic fall in European interest in ocean voyaging",
   "The immediate abandonment of the route around Africa",
   "The construction of a global trading-post empire",
   "The end of state sponsorship of exploration"],
  ans=0,
  why=("KC-4.1.III.B says Spanish sponsorship of the voyages of Columbus and subsequent voyages "
       "across the Atlantic and Pacific dramatically increased European interest in transoceanic "
       "travel and trade. The trading-post empire is what KC-4.1.III.A attributes to the "
       "Portuguese, so that option is a real statement of the framework attached to the wrong "
       "sponsor.")),
 dict(
  q=("Across which waters does the framework place the Spanish-sponsored voyages of Columbus and "
     "the voyages that came after them?"),
  choices=[
   "The Atlantic and the Pacific",
   "The Indian Ocean and the Red Sea",
   "The Baltic and the North Sea",
   "The Mediterranean alone",
   "The Arctic Ocean alone"],
  ans=0,
  why=("KC-4.1.III.B places Spanish sponsorship of the voyages of Columbus and subsequent "
       "voyages across the Atlantic and Pacific. No other body of water is named in that "
       "statement, and the northern crossings of KC-4.1.III.C are Atlantic rather than Arctic in "
       "the framework's wording.")),
 dict(
  q=("Under whose sponsorship does the framework say the northern Atlantic crossings were "
     "undertaken?"),
  choices=[
   "English, French, and Dutch",
   "Portuguese and Spanish",
   "Ottoman and Safavid",
   "Mughal and Manchu",
   "Swedish and Danish"],
  ans=0,
  why=("KC-4.1.III.C states that northern Atlantic crossings were undertaken under English, "
       "French, and Dutch sponsorship. Portuguese and Spanish sponsorship belong to KC-4.1.III.A "
       "and KC-4.1.III.B, and the land empires of KC-4.3.II.B are not given any role in "
       "transoceanic sponsorship here.")),
 dict(
  q=("The framework gives a goal that the northern Atlantic crossings were often undertaken to "
     "achieve. What was it?"),
  choices=[
   "Finding alternative sailing routes to Asia",
   "Establishing plantations in the Caribbean",
   "Mapping the coasts of the Mediterranean",
   "Escorting pilgrims to a shrine",
   "Blockading the ports of a rival land empire"],
  ans=0,
  why=("KC-4.1.III.C says the northern Atlantic crossings were undertaken often with the goal of "
       "finding alternative sailing routes to Asia. Plantations belong to KC-4.2.II.C, and the "
       "remaining options name purposes the framework attaches to no voyage in this topic.")),
 dict(
  q=("A student is matching each sponsor named in this topic to what the framework attributes to "
     "it. Which pairing is the framework's own?"),
  choices=[
   "Portuguese sponsorship with a global trading-post empire, and Spanish sponsorship with a sharp rise in European interest in transoceanic travel",
   "Portuguese sponsorship with a sharp rise in European interest in transoceanic travel, and Spanish sponsorship with a global trading-post empire",
   "English sponsorship with a global trading-post empire, and Dutch sponsorship with the voyages of Columbus",
   "Spanish sponsorship with the northern Atlantic crossings, and French sponsorship with trade around Africa",
   "Dutch sponsorship with a global trading-post empire, and Portuguese sponsorship with the northern Atlantic crossings"],
  ans=0,
  why=("KC-4.1.III.A gives the trading-post empire to the Portuguese development of maritime "
       "technology, and KC-4.1.III.B gives the dramatic increase in European interest to Spanish "
       "sponsorship of the voyages of Columbus. The rejected pairings exchange those two "
       "attributions or hand one of them to the English, French or Dutch sponsors of "
       "KC-4.1.III.C.")),
 dict(
  q=("Which statement about the sponsorship of exploration in this period would a reader of the "
     "framework recognise as an error, even though every state named in it appears in the "
     "topic?"),
  choices=[
   "The northern Atlantic crossings were undertaken under Portuguese and Spanish sponsorship rather than English, French, and Dutch",
   "The northern Atlantic crossings were undertaken under English, French, and Dutch sponsorship",
   "Spanish sponsorship carried the voyages of Columbus across the Atlantic",
   "Portuguese maritime technology led to increased trade with Africa and Asia",
   "New state-supported transoceanic maritime exploration occurred in this period"],
  ans=0,
  why=("KC-4.1.III.C assigns the northern Atlantic crossings to English, French, and Dutch "
       "sponsorship, so moving them to the Portuguese and Spanish is the error. The other four "
       "statements are KC-4.1.III, KC-4.1.III.A, KC-4.1.III.B and KC-4.1.III.C almost verbatim, "
       "which is what makes the mistaken one hard to see.")),
 dict(
  q=("A hypothetical charter of the period, granted by a ruler and copied into a port's records, "
     "sets aside money from the treasury to fit out three ships for a voyage beyond any water "
     "the kingdom's vessels had sailed before.\n\n"
     "Which development of the period does the charter best illustrate?"),
  choices=[
   "State-supported transoceanic maritime exploration",
   "The recruitment of bureaucratic elites to hold a population under central control",
   "The adoption of a restrictive trade policy by an Asian state",
   "The use of religious ideas to legitimize a ruler's authority",
   "The intensification of peasant labor to meet rising demand"],
  ans=0,
  why=("KC-4.1.III describes new state-supported transoceanic maritime exploration in this "
       "period, and a ruler paying out of the treasury to send ships across an unfamiliar ocean "
       "is that development exactly. The rejected options are KC-4.3.I.C, KC-4.3.II.A.i, "
       "KC-4.3.I.A and KC-4.2.II.A.")),
 dict(
  q=("A hypothetical letter from an agent stationed overseas describes a chain of fortified "
     "posts, each holding a small garrison and a warehouse, strung along the coasts of two "
     "continents and used to buy and sell rather than to settle the interior.\n\n"
     "Which of the framework's outcomes does the letter describe?"),
  choices=[
   "A global trading-post empire",
   "A colonial economy in the Americas resting on plantation agriculture",
   "A land empire built by gunpowder weaponry",
   "A syncretic belief system formed by contact between religions",
   "An isolationist trade policy adopted to limit foreign contact"],
  ans=0,
  why=("KC-4.1.III.A names the construction of a global trading-post empire as the result of "
       "Portuguese development of maritime technology and navigational skills, and posts held for "
       "trade rather than settlement along distant coasts are what that phrase describes. The "
       "rejected options are KC-4.2.II.D, KC-4.3.II, KC-4.1.VI and KC-4.3.II.A.i.")),
 dict(
  q=("The table below records four voyages in a hypothetical register, with who paid for each "
     "and where each was sent.\n\n"
     "Which conclusion is best supported by the table alone?"),
  table=_T_SPONSORS,
  choices=[
   "Every voyage in the register that crossed an ocean was paid for out of a royal treasury",
   "Every voyage in the register was paid for by a merchant house",
   "The only voyage paid for out of a royal treasury stayed within European waters",
   "No voyage in the register was sent beyond European waters",
   "Every voyage in the register was sent in the same direction"],
  ans=0,
  why=("KC-4.1.III describes the exploration of this period as state-supported, and the register "
       "shows the three ocean crossings paid for from a treasury while the one privately funded "
       "voyage stays on the European coast. The verifier recomputes which rows crossed an ocean "
       "and who paid for each.")),
 dict(
  q=("A hypothetical register of voyages sent beyond European waters over four decades is "
     "summarised in the table below.\n\n"
     "Which statement about the table is accurate?"),
  table=_T_BACKING,
  choices=[
   "Voyages with royal backing grow from a minority of the total to a majority of it",
   "Voyages without royal backing grow from a minority of the total to a majority of it",
   "Voyages with royal backing fall in every decade shown",
   "Neither column changes across the four decades",
   "The two columns are equal in every decade shown"],
  ans=0,
  why=("KC-4.1.III singles out state-supported exploration as what was new in this period, and "
       "the register shows royally backed voyages beginning as the smaller share and ending as "
       "the larger one. The verifier recomputes both columns and the share in each decade, and "
       "confirms that the reversed reading is false.")),
 dict(
  q=("Four expeditions and the purpose recorded for each appear in a hypothetical register "
     "below.\n\n"
     "Which recorded purpose matches what the framework says the northern Atlantic crossings "
     "were often undertaken to find?"),
  table=_T_GOALS,
  choices=[
   "The expedition seeking another sailing route to Asia through northern waters",
   "The expedition seeking Asia by sailing around Africa",
   "The expedition seeking Asia by sailing west across the Atlantic",
   "The expedition surveying a river mouth within its sponsor's own kingdom",
   "None of the recorded purposes concerns reaching Asia at all"],
  ans=0,
  why=("KC-4.1.III.C says the northern Atlantic crossings were undertaken often with the goal of "
       "finding alternative sailing routes to Asia, so the match is the northern expedition "
       "rather than the two that seek Asia by the routes already in use. The verifier recomputes "
       "which recorded purposes name Asia and which name northern waters.")),
 dict(
  q=("Suggested skill 5.B asks a student to explain how one historical development relates to "
     "another. Which pairing of developments from this unit does the framework itself connect?"),
  choices=[
   "The spread of knowledge and technology into Europe, and the state-supported ocean voyaging of this period",
   "The spread of knowledge and technology into Europe, and the collection of tribute by land empires",
   "The northern Atlantic crossings, and the recruitment of bureaucratic elites",
   "Portuguese navigational skill, and the practice of tax farming",
   "Spanish sponsorship of Columbus, and the use of monumental architecture to legitimize rule"],
  ans=0,
  why=("KC-4.1.II and KC-4.1.II.A have knowledge and technology spreading into Europe and "
       "producing tools, ship designs and an understanding of winds and currents that made "
       "transoceanic travel possible, and KC-4.1.III then reports the state-supported ocean "
       "voyaging of the period. Tribute, bureaucratic elites, tax farming and monumental "
       "architecture belong to KC-4.3.I and are not connected to exploration there.")),
 dict(
  q=("Unit 4: Learning Objective C asks for the economic causes and effects of maritime "
     "exploration by the various European states. Which of the following does the framework "
     "offer as an economic effect?"),
  choices=[
   "Increased travel to and trade with Africa and Asia",
   "The disappearance of long-distance trade from the Indian Ocean",
   "The closing of every European port to foreign goods",
   "The replacement of coined money by barter across Europe",
   "The end of commercial contact between Europe and Asia"],
  ans=0,
  why=("KC-4.1.III.A gives increased travel to and trade with Africa and Asia as what followed "
       "from Portuguese development of maritime technology and navigational skills, which is an "
       "economic effect in the framework's own words. Each rejected option asserts a contraction "
       "of trade that the framework nowhere records for this period.")),
 dict(
  q=("Why does the framework place this topic under the theme of governance as well as under "
     "economic systems?"),
  choices=[
   "Because the exploration it describes was supported by states, and governance concerns how governments exercise power",
   "Because governance concerns how societies group their members into classes",
   "Because governance concerns the exchange of plants and animals between hemispheres",
   "Because governance concerns the beliefs a society holds about itself",
   "Because governance concerns the ways a society produces and consumes goods"],
  ans=0,
  why=("The governance thematic focus printed with this topic says governments obtain, retain, "
       "and exercise power in different ways and for different purposes, and KC-4.1.III makes "
       "the exploration of the period state-supported. The rejected descriptions are the Social "
       "Interactions, Humans and the Environment, Cultural Developments and Economic Systems "
       "thematic focuses.")),
 dict(
  q=("Which of the following claims about the exploration of this period would require evidence "
     "from outside the framework's own statements?"),
  choices=[
   "That one state's expeditions were better navigated than another's",
   "That state-supported transoceanic maritime exploration was new in this period",
   "That Portuguese navigational skill led to increased trade with Africa and Asia",
   "That Spanish sponsorship carried voyages across the Atlantic and the Pacific",
   "That the northern Atlantic crossings often sought other sailing routes to Asia"],
  ans=0,
  why=("The four rejected statements are KC-4.1.III, KC-4.1.III.A, KC-4.1.III.B and KC-4.1.III.C "
       "almost verbatim. The framework compares no two states' expeditions for quality of "
       "navigation, so a claim of that kind would have to be defended from another source.")),
 dict(
  q=("A hypothetical petition to a ruler asks that the crown pay for a voyage the petitioners "
     "cannot fund themselves, and promises the crown a share of whatever trade follows.\n\n"
     "What does the petition show about exploration in this period?"),
  choices=[
   "That ocean voyaging depended on state support and was expected to bring commercial return",
   "That ocean voyaging was funded entirely without reference to rulers",
   "That rulers forbade their subjects to undertake ocean voyages",
   "That commercial motives played no part in the voyages of the period",
   "That voyages were undertaken only after trade routes were already secure"],
  ans=0,
  why=("KC-4.1.III describes the exploration of the period as state-supported, and Unit 4: "
       "Learning Objective C asks for its economic causes and effects, which together are what "
       "the petition joins. Each rejected option removes either the state or the commercial "
       "motive that those two statements supply.")),
 dict(
  q=("A historian argues that the exploration of this period cannot be explained without the "
     "actions of governments. Which evidence would most directly support that argument as the "
     "framework frames it?"),
  choices=[
   "Records of treasuries paying to fit out voyages beyond European waters",
   "Records of the number of taverns in a port town",
   "Records of the grain harvested in an inland province",
   "Records of the fees charged by a river ferry",
   "Records of the names given to newly built ships"],
  ans=0,
  why=("KC-4.1.III makes state support the distinguishing feature of the period's transoceanic "
       "exploration, so evidence bearing on that claim has to connect a government's money to a "
       "voyage. Taverns, harvests, ferry fees and ships' names document other things and leave "
       "the claim untested.")),
 dict(
  q=("Two students disagree about whether the framework says the northern Atlantic crossings "
     "found the routes they were looking for. What does the text allow them to conclude?"),
  choices=[
   "Only that the crossings were often undertaken with the goal of finding alternative routes",
   "That the crossings are said to have found a northern route to Asia",
   "That the crossings are said to have failed in every case",
   "That the framework gives no purpose for the crossings at all",
   "That the crossings are said to have been abandoned before any ship sailed"],
  ans=0,
  why=("KC-4.1.III.C states that northern Atlantic crossings were undertaken under English, "
       "French, and Dutch sponsorship, often with the goal of finding alternative sailing routes "
       "to Asia. That is a statement about the aim of the voyages and says nothing about the "
       "outcome, so success and failure alike go beyond it.")),
 dict(
  q=("A comparison is being drawn between the Portuguese and the Spanish sponsorship described "
     "in this topic. Which comparison is supported by the framework?"),
  choices=[
   "Both are state involvements in ocean voyaging, but the framework ties one to trade with Africa and Asia and the other to a rise in European interest in transoceanic travel",
   "Both are described as private ventures undertaken without any state involvement",
   "Both are said to have been directed at the northern Atlantic",
   "Both are said by the framework to have produced no economic effect",
   "Both are described as attempts to reach Asia by an overland route"],
  ans=0,
  why=("KC-4.1.III.A ties Portuguese maritime technology to increased travel to and trade with "
       "Africa and Asia, while KC-4.1.III.B ties Spanish sponsorship of the voyages of Columbus "
       "to a dramatic increase in European interest in transoceanic travel and trade, and "
       "KC-4.1.III makes both state-supported. Each rejected comparison contradicts one of those "
       "statements.")),
 dict(
  q=("A textbook chapter on this topic needs a title. Which one stays within what the framework "
     "asserts about the period 1450 to 1750?"),
  choices=[
   "Crowns, Treasuries, and the Opening of Ocean Routes",
   "Private Fortunes Alone: Exploration Without the State",
   "Turning Inward: Why European States Abandoned the Sea",
   "The Overland Road: How Europe Reached Asia by Land",
   "One Sponsor, One Ocean: A Single State's Voyages"],
  ans=0,
  why=("KC-4.1.III makes the exploration of the period state-supported and transoceanic, which is "
       "what the keyed title states. Exploration without the state and a turn away from the sea "
       "contradict that sentence, an overland road contradicts KC-4.1.III.C's search for sailing "
       "routes, and KC-4.1.III.A to KC-4.1.III.C name several sponsors rather than one.")),
 dict(
  q=("A hypothetical pilot's report describes weeks spent probing the inlets of a cold northern "
     "coast for a passage westward, and the decision to turn back before the ice closed in.\n\n"
     "Which of the framework's statements does the report most directly illustrate?"),
  choices=[
   "That crossings in the northern Atlantic were often made in search of another route to Asia",
   "That Portuguese navigation opened trade with Africa and Asia",
   "That Spanish sponsorship carried voyages across the Atlantic and the Pacific",
   "That European states adopted restrictive trade policies to limit contact",
   "That colonial economies in the Americas rested on coerced labor"],
  ans=0,
  why=("KC-4.1.III.C says northern Atlantic crossings were undertaken often with the goal of "
       "finding alternative sailing routes to Asia, and a search for a westward passage along a "
       "cold northern coast is that search. The rejected options are KC-4.1.III.A, KC-4.1.III.B, "
       "KC-4.3.II.A.i and KC-4.2.II.D.")),
 dict(
  q=("How does the framework connect the technology of the previous topic to the voyages of this "
     "one?"),
  choices=[
   "Tools, ship designs and knowledge of winds and currents made ocean travel possible, and states then supported voyages across the oceans",
   "The voyages came first and the technology was developed afterwards to explain them",
   "The framework treats the technology and the voyages as unconnected",
   "The framework says the technology made ocean travel harder rather than easier",
   "The framework says the voyages required no technology of any kind"],
  ans=0,
  why=("KC-4.1.II.A says new tools, innovations in ship designs, and an improved understanding of "
       "regional wind and currents patterns all made transoceanic travel and trade possible, and "
       "KC-4.1.III reports the new state-supported transoceanic exploration of the period. "
       "Suggested skill 5.B asks for exactly this kind of relation between two developments.")),
 dict(
  q=("An essay claims that European states sponsored ocean voyages for reasons that had nothing "
     "to do with commerce. Which part of the framework most directly complicates the claim?"),
  choices=[
   "The learning objective asking for the economic causes and effects of maritime exploration",
   "The statement that rulers used art and monumental architecture to legitimize rule",
   "The statement that land empires included the Ottoman and the Safavid",
   "The statement that enslaved persons challenged existing authorities in the Americas",
   "The statement that peasant labor continued and intensified in many regions"],
  ans=0,
  why=("Unit 4: Learning Objective C asks students to explain the economic causes and effects of "
       "maritime exploration by the various European states, and KC-4.1.III.A and KC-4.1.III.B "
       "both describe trade as an outcome. The rejected statements are KC-4.3.I.A, KC-4.3.II.B, "
       "KC-5.3.III.C and KC-4.2.II.A, none of which bears on the motive for a voyage.")),
 dict(
  q=("Which of the following best explains why the framework calls the exploration of this period "
     "new, given that ocean voyages had been made before 1450?"),
  choices=[
   "Because what it identifies as new is state-supported transoceanic exploration, not sea travel itself",
   "Because it claims no ship had ever left sight of land before this period",
   "Because it claims the oceans themselves were unknown before this period",
   "Because it claims no society outside Europe had ever sailed at all",
   "Because it claims voyaging began only after 1750"],
  ans=0,
  why=("KC-4.1.III says new state-supported transoceanic maritime exploration occurred in this "
       "period, so the novelty the framework asserts is the combination of state support with "
       "ocean crossing. The rejected readings make the sentence claim that ocean travel itself "
       "was unknown, which it does not say and which the CED's own note that developments are "
       "not constrained by the given dates tells against.")),
 dict(
  q=("Which piece of evidence would best support the claim that interest in transoceanic travel "
     "rose sharply among Europeans in this period?"),
  choices=[
   "A run of records showing more ocean voyages fitted out year after year across several states",
   "A record of the wages paid to a single ship's carpenter",
   "A record of one harbour's depth at low tide",
   "A record of the cloth used for one vessel's sails",
   "A record of one captain's date of birth"],
  ans=0,
  why=("KC-4.1.III.B says Spanish sponsorship of the voyages of Columbus and subsequent voyages "
       "dramatically increased European interest in transoceanic travel and trade, and a claim "
       "about rising interest across Europe needs evidence spanning several states and several "
       "years. A wage, a depth, a bolt of cloth and a birth date bear on none of it.")),
 dict(
  q=("A one-sentence summary of this topic is being written for a revision guide. Which version "
     "stays within what the framework asserts about the period 1450 to 1750?"),
  choices=[
   "States paid for new ocean voyages in this period, Portuguese navigation opened trade with Africa and Asia and built a trading-post empire, Spanish sponsorship of transatlantic voyaging raised European interest sharply, and English, French, and Dutch crossings of the northern Atlantic sought other routes to Asia",
   "Private merchants paid for every voyage of the period, and no ruler took any interest in the oceans",
   "European states explored the oceans but gained no trade from doing so, and interest in voyaging declined",
   "Portuguese sponsorship carried the voyages of Columbus, and Spanish navigation built a trading-post empire in Africa and Asia",
   "The northern Atlantic crossings were made to reach the Americas and had no connection to any route to Asia"],
  ans=0,
  why=("The keyed sentence joins KC-4.1.III, KC-4.1.III.A, KC-4.1.III.B and KC-4.1.III.C in the "
       "order the framework prints them. The rejected versions remove the state, deny the trade, "
       "exchange the Portuguese and Spanish attributions, or strip the northern crossings of the "
       "goal KC-4.1.III.C gives them.")),
]
