# AP WORLD HISTORY: MODERN 2.3 Exchange in the Indian Ocean  (title copied verbatim
# from WORLD_HISTORY_topics.json). Unit 2 Networks of Exchange, c. 1200 to c. 1450.
# Suggested skill 5.A, identify patterns among or connections between historical
# developments and processes.
#
# THE CED CONTENT OF THIS TOPIC, in the framework's own words. The page carries three
# thematic focus blocks and three learning objectives:
#
#   Thematic focus ECN: as societies develop, they affect and are affected by the ways
#           that they produce, exchange, and consume goods and services.
#   LO 2.E  Explain the causes of the growth of networks of exchange after 1200.
#   KC-3.1.I.A.ii  Improved transportation technologies and commercial practices led
#           to an increased volume of trade and expanded the geographical range of
#           existing trade routes, including the Indian Ocean, promoting the growth of
#           powerful new trading cities.
#   KC-3.1.I.C.ii  The growth of interregional trade in luxury goods was encouraged by
#           significant innovations in previously existing transportation and
#           commercial technologies, including the use of the compass, the astrolabe,
#           and larger ship designs.
#   KC-3.1.I.A.iii  The Indian Ocean trading network fostered the growth of states.
#
#   Thematic focus CDI: the development of ideas, beliefs, and religions illustrates
#           how groups in society view themselves, and the interactions of societies
#           and their beliefs often have political, social, and cultural implications.
#   LO 2.F  Explain the effects of the growth of networks of exchange after 1200.
#   KC-3.1.III.B  In key places along important trade routes, merchants set up
#           diasporic communities where they introduced their own cultural traditions
#           into the indigenous cultures and, IN TURN, indigenous cultures influenced
#           merchant cultures.
#   KC-3.2.II.A.iii  Interregional contacts and conflicts between states and empires
#           encouraged significant technological and cultural transfers, including
#           during Chinese maritime activity led by Ming Admiral Zheng He.
#
#   Thematic focus ENV: the environment shapes human societies, and as populations grow
#           and change, these populations in turn shape their environments.
#   LO 2.G  Explain the role of environmental factors in the development of networks of
#           exchange in the period from c. 1200 to c. 1450.
#   KC-3.1.II.A.i  The expansion and intensification of long-distance trade routes
#           often depended on environmental knowledge, including advanced knowledge of
#           the monsoon winds.
#
#   Illustrative examples printed on this topic page: growth of states -- city-states
#           of the Swahili Coast, Gujarat, the Sultanate of Malacca; diasporic
#           communities -- Arab and Persian communities in East Africa, Chinese
#           merchant communities in Southeast Asia, Malay communities in the Indian
#           Ocean basin. The CED states that illustrative examples "do not in any way
#           constitute additional, preferred, or required information", so no key here
#           turns on one.
#
# WHAT DISTINGUISHES THIS TOPIC FROM 2.1, and why it matters that the two were written
# to differ. KC-3.1.I.A.ii is nearly word for word KC-3.1.I.A.i, which topic 2.1 rests
# on, but it adds IMPROVED TRANSPORTATION TECHNOLOGIES to the commercial practices the
# Silk Roads sentence names alone, and this topic adds three things 2.1 does not have
# at all: the network FOSTERING THE GROWTH OF STATES, diasporic communities whose
# influence runs BOTH WAYS, and a dependence on ENVIRONMENTAL KNOWLEDGE. The weight of
# this module is on those three, and only q2 and q5 touch the shared sentence -- one of
# them precisely on the difference between the two.
#
# ON THE SOURCES. This bank cannot show an image. Every stimulus is a table of
# HYPOTHETICAL figures whose keyed conclusion is recoverable from the table alone, or
# an explicitly unattributed illustrative source. Zheng He is named only where the CED
# names him, in KC-3.2.II.A.iii, and no words are put in his mouth or anyone else's.
#
# ON DATES. Spans are written "c. 1200 to c. 1450". The CED states that events,
# processes, and developments are not constrained by the given dates and may begin
# before, or continue after, the period, so no key turns on a boundary year.
TOPIC = ("2.3", "Exchange in the Indian Ocean", 2)

_T_SEASONS = dict(
    headers=["Port (hypothetical)", "Departures recorded in the season of one wind",
             "Departures recorded in the season of the opposing wind"],
    rows=[["Port One", "60", "58"],
          ["Port Two", "45", "47"],
          ["Port Three", "30", "29"]])

_T_DIASPORA = dict(
    headers=["Port (hypothetical)", "Practices recorded as introduced by resident merchants",
             "Practices recorded as taken up by resident merchants from the host society"],
    rows=[["Port One", "7", "5"],
          ["Port Two", "4", "9"],
          ["Port Three", "6", "6"]])

_T_PORTS = dict(
    headers=["Coastal settlement (hypothetical)", "Ships calling in a year",
             "Offices recorded in its administration"],
    rows=[["Settlement One", "12", "2"],
          ["Settlement Two", "40", "6"],
          ["Settlement Three", "75", "11"]])

QUESTIONS = [
 dict(q=("An unattributed sailing directory of the period tells a master when to leave a western "
         "port for the east and when to expect a passage back, adding that a ship which misses "
         "the season must wait for the wind to turn. Which of the following identifies the "
         "connection between such knowledge and the growth of long-distance exchange?"),
      choices=[
        "The expansion and intensification of long-distance routes often depended on environmental knowledge, so knowing when a wind reverses is part of what made a regular long voyage possible.",
        "Environmental knowledge had no bearing on long-distance routes, which depended on shipbuilding alone.",
        "Long-distance routes were used only by masters who ignored the seasons entirely.",
        "The reversal of a wind prevented long-distance exchange rather than enabling it.",
        "Knowledge of the seasons was useful only for voyages within sight of a coast.",
      ], ans=0,
      why=("KC-3.1.II.A.i states that the expansion and intensification of long-distance trade "
           "routes often depended on environmental knowledge, including advanced knowledge of the "
           "monsoon winds, and the Humans and the Environments thematic focus states that the "
           "environment shapes human societies.")),

 dict(q=("The framework's sentence on the Silk Roads names improved commercial practices as the "
         "cause of increased volume and expanded range; its sentence on the Indian Ocean names "
         "something in addition. Which of the following identifies that addition?"),
      choices=[
        "Improved transportation technologies, which the Indian Ocean sentence names alongside commercial practices.",
        "Improved commercial practices, which the Indian Ocean sentence names and the Silk Roads sentence omits.",
        "The growth of powerful new trading cities, which appears only in the Indian Ocean sentence.",
        "The expansion of the geographical range of existing routes, which appears only in the Indian Ocean sentence.",
        "An increased volume of trade, which appears only in the Indian Ocean sentence.",
      ], ans=0,
      why=("KC-3.1.I.A.i attributes the change to improved commercial practices, while "
           "KC-3.1.I.A.ii attributes it to improved TRANSPORTATION TECHNOLOGIES AND commercial "
           "practices. Increased volume, expanded range and the growth of powerful new trading "
           "cities appear in both sentences, so only the transportation clause is an addition.")),

 dict(q=("Which of the following identifies what the framework asserts about the relationship "
         "between the Indian Ocean trading network and the states along it?"),
      choices=[
        "The network fostered the growth of states, so political development in the region is treated as an effect of the exchange and not merely as its setting.",
        "States along the network prevented its growth by taxing what passed through them.",
        "The network had no bearing on the states along it, which developed independently of it.",
        "States created the network, which had no existence before they established it.",
        "The network fostered the growth of states only outside the Indian Ocean basin.",
      ], ans=0,
      why=("KC-3.1.I.A.iii states in one sentence that the Indian Ocean trading network fostered "
           "the growth of states. The framework makes the network the agent and the growth of "
           "states the effect, which is what the reversed and the null options each deny.")),

 dict(q=("The table below carries HYPOTHETICAL counts of departures recorded at three ports in "
         "the season of one wind and in the season of the opposing wind. Which conclusion does "
         "the data best support?"),
      table=_T_SEASONS,
      choices=[
        "Every port listed sends ships out in both seasons, and at none of them does either season account for much more than half the departures.",
        "Every port listed sends its ships out in one season only.",
        "At one of the ports listed, one season accounts for more than twice the departures of the other.",
        "Departures at every port listed are confined to the season of the same wind.",
        "The port with the most departures in the first season has the fewest in the second.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns, distractors included. KC-3.1.II.A.i "
           "states that the expansion and intensification of long-distance trade routes often "
           "depended on environmental knowledge, including advanced knowledge of the monsoon "
           "winds, and traffic balanced between two opposing seasons is what sailing to a wind "
           "that reverses looks like in a port's records.")),

 dict(q=("An unattributed harbour record notes that a settlement which had received a few coasting "
         "vessels a generation earlier now receives ships from several distant regions, and that "
         "its ruler has appointed officers to weigh goods, to hear merchants' disputes and to "
         "collect a due on every cargo. Which of the following identifies the pattern?"),
      choices=[
        "A trading network fostering the growth of a state, since the traffic came first and the apparatus of government followed it.",
        "A state fostering the growth of a trading network, since the officers were appointed before the ships arrived.",
        "A trading network and a state developing without any relation between them.",
        "A state withdrawing from the regulation of trade as the traffic increased.",
        "A trading network declining as the state that governed it grew stronger.",
      ], ans=0,
      why=("KC-3.1.I.A.iii states that the Indian Ocean trading network fostered the growth of "
           "states, and the Governance thematic focus is not invoked here because the framework's "
           "own sentence already fixes the direction. The anchor carries both the network and the "
           "state in order because the strongest distractor exchanges them.")),

 dict(q=("Which of the following identifies what KC-3.1.III.B asserts about the cultural effect "
         "of merchant communities settled along trade routes?"),
      choices=[
        "That the merchants introduced their own traditions into the indigenous cultures and that the indigenous cultures in turn influenced the merchants' own.",
        "That the merchants introduced their own traditions into the indigenous cultures and were themselves unaffected.",
        "That the indigenous cultures influenced the merchants while the merchants introduced nothing of their own.",
        "That neither party affected the other, each keeping to its own quarter of the port.",
        "That the merchants abandoned their own traditions entirely on settling.",
      ], ans=0,
      why=("KC-3.1.III.B states that in key places along important trade routes merchants set up "
           "diasporic communities where they introduced their own cultural traditions into the "
           "indigenous cultures AND, IN TURN, indigenous cultures influenced merchant cultures. "
           "The anchor carries both directions because each of the first two rejected options "
           "keeps one and drops the other.")),

 dict(q=("HYPOTHETICAL counts of practices recorded at three ports are set out in the table "
         "below. Which conclusion is best supported by that data alone?"),
      table=_T_DIASPORA,
      choices=[
        "Practices of both kinds are recorded at every port listed, and the direction in which more practices moved is not the same at all three.",
        "Only practices introduced by resident merchants are recorded at the ports listed.",
        "Only practices taken up by merchants from their host societies are recorded at the ports listed.",
        "The direction in which more practices moved is the same at every port listed.",
        "The port recording the most practices introduced by merchants also records the most taken up by them.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.1.III.B describes influence "
           "running in both directions between merchant communities and the societies they "
           "settled among, and figures in which neither direction predominates everywhere are "
           "what such a two-way relation looks like in a record.")),

 dict(q=("Which of the following identifies why the compass and the astrolabe are grouped by the "
         "framework with larger ship designs rather than with commercial practices?"),
      choices=[
        "Because all three bear on how a vessel is navigated and loaded, which is the transportation side of the pair of technologies the framework names.",
        "Because all three bear on how payment and obligation are arranged between merchants.",
        "Because all three were invented during this period without any earlier precedent.",
        "Because all three were confined to the Indian Ocean and used on no other route.",
        "Because all three were restricted by rulers to the use of official fleets.",
      ], ans=0,
      why=("KC-3.1.I.C.ii states that the growth of interregional trade in luxury goods was "
           "encouraged by significant innovations in PREVIOUSLY EXISTING transportation and "
           "commercial technologies, including the use of the compass, the astrolabe, and larger "
           "ship designs. All three instances the sentence gives belong to the transportation "
           "half, and the word previously rules out invention within the period.")),

 dict(q=("The table below carries HYPOTHETICAL figures for three coastal settlements, giving the "
         "ships calling in a year and the offices recorded in each settlement's administration. "
         "Which conclusion does the data best support?"),
      table=_T_PORTS,
      choices=[
        "The settlements rank in the same order by ships calling as by offices recorded, a pattern consistent with a trading network fostering the growth of states.",
        "The settlements rank in the reverse order by ships calling from their order by offices recorded.",
        "The settlement with the most ships calling has the fewest offices recorded.",
        "Every settlement listed records the same number of offices.",
        "Offices are recorded at only one of the settlements listed.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.1.I.A.iii states that the "
           "Indian Ocean trading network fostered the growth of states, and two measures that "
           "rank the same settlements alike is a pattern consistent with that claim. The keyed "
           "wording says consistent with rather than proves, because a ranking cannot establish "
           "a direction on its own.")),

 dict(q=("An unattributed account describes a quarter of a coastal city inhabited by merchants "
         "from a distant region who keep their own observances, marry into local families, and "
         "whose children speak the language of the port as well as that of their fathers. Which "
         "of the following identifies the pattern?"),
      choices=[
        "A diasporic community formed along a trade route, in which the settlers' traditions enter the host society and the host society's enter theirs.",
        "A diasporic community formed along a trade route, in which the settlers remain wholly separate from the society around them.",
        "A conquest, in which one society replaces the institutions of another by force.",
        "A temporary market, in which no settlement of any kind takes place.",
        "A withdrawal of merchants from a port, leaving no trace of their presence.",
      ], ans=0,
      why=("KC-3.1.III.B states that in key places along important trade routes, merchants set up "
           "diasporic communities where they introduced their own cultural traditions into the "
           "indigenous cultures and, in turn, indigenous cultures influenced merchant cultures. "
           "The account shows both halves of that sentence at once.")),

 dict(q=("Which of the following identifies the role the framework assigns to environmental "
         "knowledge in the growth of long-distance exchange?"),
      choices=[
        "It is named as something the expansion and intensification of long-distance routes often depended on, so it is treated as a condition of the growth rather than a consequence of it.",
        "It is named as a consequence of the growth of long-distance routes rather than a condition of it.",
        "It is named as irrelevant to long-distance routes, which depended on political authority alone.",
        "It is named as a substitute for transportation technology rather than a complement to it.",
        "It is named only in connection with overland routes and not with maritime ones.",
      ], ans=0,
      why=("KC-3.1.II.A.i states that the expansion and intensification of long-distance trade "
           "routes often DEPENDED ON environmental knowledge, including advanced knowledge of the "
           "monsoon winds. Depending on something makes it a condition, and the monsoon is a "
           "maritime instance.")),

 dict(q=("Which of the following claims about the Indian Ocean network does the framework NOT "
         "support?"),
      choices=[
        "That the network's growth was directed by a single state that controlled the whole of it.",
        "That improved transportation technologies and commercial practices increased the volume of trade on it.",
        "That the network fostered the growth of states.",
        "That merchants formed communities in key places along it.",
        "That its expansion often depended on knowledge of the monsoon winds.",
      ], ans=0,
      why=("KC-3.1.I.A.ii, KC-3.1.I.A.iii, KC-3.1.III.B and KC-3.1.II.A.i between them assert "
           "increased volume, the fostering of states, diasporic merchant communities and a "
           "dependence on environmental knowledge. A single controlling state appears in none of "
           "them.")),

 dict(q=("An unattributed inventory from a vessel of the period lists a far larger cargo than "
         "such ships had carried a century earlier, together with instruments for taking a "
         "bearing and for measuring the height of a star. Which of the following identifies what "
         "the inventory illustrates?"),
      choices=[
        "Innovations in transportation technologies already in use, which the framework names among the encouragements to the growth of interregional trade in luxury goods.",
        "Innovations in commercial practice, since a larger cargo implies a larger sum at risk.",
        "The abandonment of long-distance sailing in favour of coasting voyages.",
        "The invention of navigation itself during this period.",
        "The confinement of trade to goods that could be carried by a single traveller.",
      ], ans=0,
      why=("KC-3.1.I.C.ii states that the growth of interregional trade in luxury goods was "
           "encouraged by significant innovations in previously existing transportation and "
           "commercial technologies, including the use of the compass, the astrolabe, and larger "
           "ship designs. All three of the inventory's features belong to that clause.")),

 dict(q=("Which of the following states the connection the framework draws between the maritime "
         "activity it names under Ming Admiral Zheng He and the wider pattern of the period?"),
      choices=[
        "It is offered as an instance of the interregional contacts and conflicts between states and empires that encouraged significant technological and cultural transfers.",
        "It is offered as the only occasion on which any technological or cultural transfer occurred in the period.",
        "It is offered as an instance of a state withdrawing from contact with other regions.",
        "It is offered as the cause of the Indian Ocean network rather than an episode within it.",
        "It is offered as evidence that maritime activity produced no transfers of any kind.",
      ], ans=0,
      why=("KC-3.2.II.A.iii states that interregional contacts and conflicts between states and "
           "empires encouraged significant technological and cultural transfers, INCLUDING during "
           "Chinese maritime activity led by Ming Admiral Zheng He. The word including makes the "
           "voyages an instance of the pattern rather than the whole of it.")),

 dict(q=("A student argues that the growth of Indian Ocean exchange had political consequences as "
         "well as economic ones. Which of the following best supports that argument from this "
         "topic's key concepts?"),
      choices=[
        "That the framework says the network fostered the growth of states, which is a political effect asserted in the same set of sentences as the commercial ones.",
        "That the framework says the network carried goods of high value in small bulk.",
        "That the framework says merchants used instruments for navigation.",
        "That the framework says the routes concerned already existed before the period.",
        "That the framework says the growth of trade depended on knowledge of the winds.",
      ], ans=0,
      why=("KC-3.1.I.A.iii states that the Indian Ocean trading network fostered the growth of "
           "states, which stands beside KC-3.1.I.A.ii's account of volume and range. The other "
           "four options are true of the framework but bear on the commerce or the navigation "
           "rather than on the politics.")),

 dict(q=("Which of the following identifies the difference between a diasporic community as the "
         "framework describes it and a party of merchants passing through a port?"),
      choices=[
        "The first is settled in the place, which is what allows traditions to pass in both directions between it and the society around it.",
        "The first is passing through, and the second is settled, so the two have been described the wrong way round.",
        "The two are the same thing under different names, since any merchant in a port is a settler.",
        "The first carries goods and the second does not, which is the only difference the framework draws.",
        "The first is confined to one region of the world and the second is found everywhere.",
      ], ans=0,
      why=("KC-3.1.III.B states that in key places along important trade routes MERCHANTS SET UP "
           "DIASPORIC COMMUNITIES where they introduced their own cultural traditions into the "
           "indigenous cultures and, in turn, indigenous cultures influenced merchant cultures. "
           "Settlement is what the sentence describes and what its two-way influence requires. "
           "The anchor carries both the settlement and its consequence because one distractor "
           "exchanges the two descriptions.")),

 dict(q=("An unattributed report from a coastal town states that the men who handle its shipping "
         "keep accounts in a script the town did not formerly use, and that its own weavers have "
         "begun to work patterns brought by those same men. Which of the following identifies the "
         "pattern?"),
      choices=[
        "Cultural traditions introduced by a settled merchant community entering the practice of the host society.",
        "Cultural traditions of the host society entering the practice of a settled merchant community.",
        "The extinction of the host society's own practices upon the merchants' arrival.",
        "The exclusion of the merchants from any dealing with the host society.",
        "The replacement of trade by cultural exchange as the merchants' business.",
      ], ans=0,
      why=("KC-3.1.III.B states that merchants introduced their own cultural traditions into the "
           "indigenous cultures and that indigenous cultures in turn influenced merchant "
           "cultures. Here the movement described runs from the merchants into the town, and the "
           "anchor names the direction because the strongest distractor reverses it.")),

 dict(q=("Which of the following would be the strongest evidence that environmental knowledge, "
         "rather than shipbuilding alone, accounts for the regularity of voyages on a maritime "
         "route?"),
      choices=[
        "That sailings cluster in the same two parts of the year across many ports and many decades, in a rhythm no change of vessel would produce.",
        "That the vessels used on the route grew larger across the period.",
        "That the goods carried on the route were valuable in proportion to their weight.",
        "That the ports on the route grew in population during the period.",
        "That instruments for taking a bearing were carried aboard the vessels.",
      ], ans=0,
      why=("KC-3.1.II.A.i states that the expansion and intensification of long-distance trade "
           "routes often depended on environmental knowledge, INCLUDING ADVANCED KNOWLEDGE OF THE "
           "MONSOON WINDS. A seasonal rhythm in the sailings is the signature of that knowledge; "
           "larger ships and better instruments belong to KC-3.1.I.C.ii's technological clause "
           "instead.")),

 dict(q=("A student writes that the merchants who settled in foreign ports changed those places "
         "without being changed themselves. Which of the following identifies the error?"),
      choices=[
        "The framework says indigenous cultures influenced merchant cultures in turn, so the effect it describes runs in both directions.",
        "The framework says the merchants changed nothing in the places where they settled.",
        "The framework says the merchants never settled in foreign ports at all.",
        "The framework says the merchants were changed while the host societies were not.",
        "The framework says the two parties never came into contact in the ports concerned.",
      ], ans=0,
      why=("KC-3.1.III.B states that merchants introduced their own cultural traditions into the "
           "indigenous cultures AND, IN TURN, indigenous cultures influenced merchant cultures. "
           "The phrase in turn is the framework's own and it is what a one-way account leaves "
           "out.")),

 dict(q=("Which of the following pairs a cause named in this topic with the effect the framework "
         "attaches to it?"),
      choices=[
        "Improved transportation technologies and commercial practices, paired with an increased volume of trade and an extended range for routes already in use.",
        "Improved transportation technologies and commercial practices, paired with the diffusion of religions into regions that had not known them.",
        "Knowledge of the monsoon winds, paired with the establishment of diasporic communities in inland cities.",
        "The growth of states along the network, paired with the invention of the compass.",
        "The settlement of merchant communities, paired with a fall in the volume of trade.",
      ], ans=0,
      why=("KC-3.1.I.A.ii states that improved transportation technologies and commercial "
           "practices led to an increased volume of trade and expanded the geographical range of "
           "existing trade routes, including the Indian Ocean. That is the pairing the sentence "
           "itself makes; the others join a cause to an effect the framework does not attach to "
           "it.")),

 dict(q=("Which of the following identifies a limit on what this topic's key concepts allow a "
         "student to claim about diasporic communities?"),
      choices=[
        "They assert that influence ran in both directions without stating which direction carried more in any particular place.",
        "They assert that influence ran in one direction only.",
        "They assert that no such communities existed along the routes of this period.",
        "They assert precisely how many such communities were established.",
        "They assert that such communities were confined to inland routes.",
      ], ans=0,
      why=("KC-3.1.III.B states that merchants introduced their own cultural traditions into the "
           "indigenous cultures and that indigenous cultures in turn influenced merchant "
           "cultures. It supplies no magnitude on either side and names no place, so a claim "
           "about which way the balance fell would go past the sentence.")),

 dict(q=("An unattributed account of a maritime state describes its ruler fixing the dues payable "
         "on cargo, keeping a fleet to clear the approaches to his harbour, and inviting "
         "merchants of several regions to settle under his protection. Which of the following "
         "identifies the connection between the state's actions and the network?"),
      choices=[
        "The state's growth and the network's traffic reinforce one another, which is consistent with the framework's claim that the network fostered the growth of states.",
        "The state's actions show that the network could only exist where a state had created it.",
        "The state's actions show that rulers of the period withdrew from any dealing with merchants.",
        "The state's actions show that trade and government were kept strictly separate in this period.",
        "The state's actions show that the network declined wherever a state took an interest in it.",
      ], ans=0,
      why=("KC-3.1.I.A.iii states that the Indian Ocean trading network fostered the growth of "
           "states, and KC-3.1.III.B records merchants settling in key places along important "
           "trade routes. A ruler protecting and taxing that traffic is the state side of the "
           "same relation.")),

 dict(q=("Which of the following identifies why the framework calls the innovations of this topic "
         "innovations in previously existing technologies?"),
      choices=[
        "Because vessels, instruments and commercial arrangements were already in use and what changed was their improvement and spread, not their first appearance.",
        "Because the technologies concerned were abandoned during this period and revived later.",
        "Because the technologies concerned were used only in regions that had never traded before.",
        "Because the framework treats every technology of the period as having been invented within it.",
        "Because the technologies concerned were the property of rulers rather than of merchants.",
      ], ans=0,
      why=("KC-3.1.I.C.ii states that the growth of interregional trade in luxury goods was "
           "encouraged by significant innovations in PREVIOUSLY EXISTING transportation and "
           "commercial technologies, including the use of the compass, the astrolabe, and larger "
           "ship designs. The adjective is the framework's own.")),

 dict(q=("A historian wishes to show that exchange in this period shaped the societies of the "
         "coasts and not only the fortunes of merchants. Which of the following would be the most "
         "direct evidence?"),
      choices=[
        "That practices belonging to settled merchant communities came into ordinary use among the people of the ports, and practices of the ports among the merchants.",
        "That the volume of goods passing through the ports rose across the period.",
        "That the vessels calling at the ports grew larger across the period.",
        "That the ports lay on a route whose extent had been enlarged.",
        "That merchants kept written records of the cargoes they shipped.",
      ], ans=0,
      why=("KC-3.1.III.B states that merchants introduced their own cultural traditions into the "
           "indigenous cultures and, in turn, indigenous cultures influenced merchant cultures, "
           "and the Cultural Developments thematic focus states that the interactions of "
           "societies and their beliefs often have political, social, and cultural implications.")),

 dict(q=("Which of the following identifies what the Humans and the Environments thematic focus "
         "adds to this topic's account of exchange?"),
      choices=[
        "That the relation runs both ways, the environment shaping the societies that trade and those populations in turn shaping their environments.",
        "That the environment shapes societies while remaining itself unaffected by them.",
        "That societies shape their environments while remaining themselves unaffected.",
        "That the environment and human societies have no bearing on one another.",
        "That environmental factors bear on agriculture but not on exchange.",
      ], ans=0,
      why=("The Humans and the Environments thematic focus states that the environment shapes "
           "human societies, and as populations grow and change, these populations IN TURN shape "
           "their environments, while KC-3.1.II.A.i makes environmental knowledge a condition of "
           "the expansion of long-distance routes. The anchor carries both directions because two "
           "distractors keep one and drop the other.")),

 dict(q=("Two students describe the same port. One calls it a place where goods change hands; the "
         "other calls it a place where societies meet. Which of the following identifies how the "
         "framework allows both descriptions?"),
      choices=[
        "It treats the same routes as carrying an increased volume of trade and as the places where merchants settled and cultural traditions passed between communities.",
        "It treats commercial and cultural effects as belonging to different routes, so the two students are describing different places.",
        "It treats the cultural description as a figure of speech with no historical content.",
        "It treats the commercial description as false, since the ports existed for cultural exchange alone.",
        "It treats the two descriptions as contradictory, so one of the students must be mistaken.",
      ], ans=0,
      why=("KC-3.1.I.A.ii supplies the increased volume of trade on existing routes including the "
           "Indian Ocean, and KC-3.1.III.B supplies the diasporic communities in key places along "
           "important trade routes where traditions moved in both directions. The framework "
           "asserts both of the same routes.")),

 dict(q=("Which of the following would most weaken a claim that the growth of states along the "
         "Indian Ocean had nothing to do with the trade passing them?"),
      choices=[
        "Evidence that the apparatus of government at a coastal settlement was built up in the same years as its shipping traffic multiplied.",
        "Evidence that the settlement's rulers claimed descent from an earlier line.",
        "Evidence that the settlement lay on a coast with a natural harbour.",
        "Evidence that the settlement's population spoke more than one language.",
        "Evidence that the settlement had existed before the period began.",
      ], ans=0,
      why=("KC-3.1.I.A.iii states that the Indian Ocean trading network fostered the growth of "
           "states. Government and traffic growing together is the pattern that sentence "
           "predicts, so evidence of it bears directly on a claim that the two were unconnected.")),

 dict(q=("A student asks why environmental knowledge belongs in a topic about trade rather than "
         "in one about agriculture. Which of the following is the best answer from this topic?"),
      choices=[
        "Because the framework makes the expansion and intensification of long-distance trade routes depend on such knowledge, so it is part of the account of the trade itself.",
        "Because the framework treats agriculture as having no environmental dimension.",
        "Because the framework treats environmental knowledge as a kind of commercial practice.",
        "Because the framework treats trade routes as unaffected by conditions of any kind.",
        "Because the framework assigns environmental knowledge to no topic in particular.",
      ], ans=0,
      why=("KC-3.1.II.A.i states that the expansion and intensification of long-distance trade "
           "routes often depended on environmental knowledge, including advanced knowledge of the "
           "monsoon winds, and Learning Objective G of this unit asks for the role of "
           "environmental factors in the development of networks of exchange.")),

 dict(q=("An unattributed letter from a merchant settled far from his birthplace mentions the "
         "festival his community keeps, the local partner with whom he holds a share in a "
         "consignment, and the local court before which their agreement was witnessed. Which of "
         "the following identifies the pattern?"),
      choices=[
        "A settled merchant community woven into the institutions of its host society while keeping observances of its own, which is the two-sided relation the framework describes.",
        "A settled merchant community entirely absorbed into its host society and retaining nothing of its own.",
        "A settled merchant community entirely separate from its host society and dealing with no one in it.",
        "A merchant travelling through a port without forming any connection there.",
        "A host society adopting a merchant community's institutions while giving nothing in return.",
      ], ans=0,
      why=("KC-3.1.III.B states that merchants set up diasporic communities where they introduced "
           "their own cultural traditions into the indigenous cultures and, in turn, indigenous "
           "cultures influenced merchant cultures. Keeping an observance while using a local "
           "court is both halves of that sentence in one life.")),

 dict(q=("Which of the following statements about exchange in the Indian Ocean is supported by "
         "this topic's key concepts taken together?"),
      choices=[
        "Improvements in ships and in commercial arrangements raised the volume carried on a route already in use, the traffic fostered the growth of states along it, merchants settled in its ports and influenced and were influenced by the societies there, and the whole depended on knowing when the winds would turn.",
        "The route was opened for the first time in this period, carried a falling volume of goods, produced no state along it, and required no knowledge of local conditions.",
        "Improvements in ships raised the volume carried, but no state grew along the route and no merchant settled anywhere on it.",
        "Merchants settled along the route and influenced its societies, but the volume of trade was unchanged and no environmental knowledge was involved.",
        "Nothing can be said about the Indian Ocean in this period, since the framework makes no assertion about it.",
      ], ans=0,
      why=("KC-3.1.I.A.ii supplies the improved transportation technologies and commercial "
           "practices and the increased volume on existing routes, KC-3.1.I.A.iii the fostering "
           "of states, KC-3.1.III.B the diasporic communities and their two-way influence, and "
           "KC-3.1.II.A.i the dependence on environmental knowledge including the monsoon winds. "
           "Each rejected option contradicts at least one.")),
]
