# AP WORLD HISTORY: MODERN 2.6 Environmental Consequences of Connectivity  (title
# copied verbatim from WORLD_HISTORY_topics.json -- this is one of the twelve titles
# corrected after the truncation bug, and the JSON is trusted over anything
# reconstructed from the CED dump, whose topic pages print the title split across three
# lines of a narrow column). Unit 2 Networks of Exchange, c. 1200 to c. 1450.
# Suggested skill 5.A, identify patterns among or connections between historical
# developments and processes.
#
# THE CED CONTENT OF THIS TOPIC, IN FULL. This page is one of the thinnest in the
# course: one thematic focus, one learning objective, one historical development, one
# illustrative list.
#
#   Thematic focus ENV: the environment shapes human societies, and as populations grow
#           and change, these populations in turn shape their environments.
#   LO 2.K  Explain the environmental effects of the various networks of exchange in
#           Afro-Eurasia from c. 1200 to c. 1450.
#   KC-3.1.IV  There was continued diffusion of crops and pathogens, with epidemic
#           diseases, including the bubonic plague, along trade routes.
#
#   Illustrative examples printed on this topic page: diffusion of crops -- bananas in
#           Africa, new rice varieties in East Asia, the spread of citrus in the
#           Mediterranean. The CED states that illustrative examples "do not in any way
#           constitute additional, preferred, or required information", so no key here
#           turns on one.
#
# WHAT THE SINGLE SENTENCE ACTUALLY SAYS, CLAUSE BY CLAUSE, because thirty questions
# rest on it and nothing else:
#
#   "continued"        -- the diffusion is older than the period, not begun in it
#   "crops AND pathogens" -- the framework puts the two together in one clause, so the
#                         same movement carries what feeds and what kills
#   "epidemic diseases, including the bubonic plague" -- the plague is named as ONE
#                         instance of a wider class, with the word including
#   "along trade routes" -- the route is named as the path, which is what makes this
#                         an environmental consequence OF CONNECTIVITY rather than a
#                         separate subject
#
# WHAT IS DELIBERATELY ABSENT. No key asserts a mortality figure, a date for any
# outbreak, a mechanism of transmission, a climatic episode, or a demographic
# consequence, because the CED asserts none of them here and a student could not check
# any of them against this framework. A great deal is known about the fourteenth
# century that this page does not say, and HISTORY_BRIEF.md is explicit that a key
# resting on such knowledge is not an AP question.
#
# ON THE SOURCES. This bank cannot show an image. Every stimulus is a table of
# HYPOTHETICAL figures whose keyed conclusion is recoverable from the table alone, or
# an explicitly unattributed illustrative source. Nothing is put into a real person's
# mouth.
#
# ON DATES. Spans are written "c. 1200 to c. 1450". The CED states that events,
# processes, and developments are not constrained by the given dates and may begin
# before, or continue after, the period -- and KC-3.1.IV's own word CONTINUED is an
# instance of that, which is why no key here turns on a boundary year.
TOPIC = ("2.6", "Environmental Consequences of Connectivity", 2)

_T_OUTBREAK = dict(
    headers=["Settlement (hypothetical)", "Days of travel from the nearest trade route",
             "Years after the first record elsewhere that the outbreak is recorded here"],
    rows=[["Settlement One", "1", "3"],
          ["Settlement Two", "4", "9"],
          ["Settlement Three", "9", "17"]])

_T_CROPS = dict(
    headers=["Crop (hypothetical)", "Regions in which it is recorded before this period",
             "Regions in which it is recorded during this period"],
    rows=[["Crop One", "1", "4"],
          ["Crop Two", "2", "3"],
          ["Crop Three", "3", "8"]])

_T_ROUTES = dict(
    headers=["Route (hypothetical)", "Crops recorded as newly present along it",
             "Epidemic outbreaks recorded along it"],
    rows=[["Route One", "5", "2"],
          ["Route Two", "3", "4"],
          ["Route Three", "6", "3"]])

QUESTIONS = [
 dict(q=("Which of the following identifies what KC-3.1.IV asserts about what moved along the "
         "trade routes of this period?"),
      choices=[
        "That the diffusion of crops and of pathogens continued along those routes, epidemic diseases among them.",
        "That crops diffused along those routes while pathogens did not.",
        "That pathogens diffused along those routes while crops did not.",
        "That the diffusion of crops and pathogens began in this period, no such movement having occurred before.",
        "That neither crops nor pathogens moved along trade routes in this period.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens, with "
           "epidemic diseases, including the bubonic plague, along trade routes. Both are in the "
           "one clause, and the word continued rules out an origin inside the period.")),

 dict(q=("A student writes that the movement of crops between regions was something new in this "
         "period. Which of the following identifies the error?"),
      choices=[
        "The framework calls the diffusion CONTINUED, which describes a process already under way rather than one beginning.",
        "The framework calls the diffusion new, so the student has correctly reported it.",
        "The framework says crops did not move between regions in this period.",
        "The framework says crops moved only within the regions where they were first grown.",
        "The framework says the movement of crops ended during this period.",
      ], ans=0,
      why=("KC-3.1.IV states that there was CONTINUED diffusion of crops and pathogens along "
           "trade routes, and the CED separately states that developments are not constrained by "
           "the given dates and may begin before the period. The adjective is the framework's "
           "own.")),

 dict(q=("The table below carries HYPOTHETICAL figures for three settlements, giving each one's "
         "distance from the nearest trade route and how long after the first record elsewhere an "
         "outbreak is recorded there. Which conclusion does the data best support?"),
      table=_T_OUTBREAK,
      choices=[
        "The further a settlement lies from the route, the later the outbreak is recorded there, a pattern consistent with a disease moving along the route.",
        "The further a settlement lies from the route, the earlier the outbreak is recorded there.",
        "Every settlement listed records the outbreak after the same interval.",
        "The settlement nearest the route records the outbreak last of the three.",
        "None of the settlements listed records the outbreak at all.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns, distractors included. KC-3.1.IV "
           "states that there was continued diffusion of crops and pathogens, with epidemic "
           "diseases, including the bubonic plague, ALONG TRADE ROUTES, and a delay that grows "
           "with distance from a route is what movement along that route looks like in figures.")),

 dict(q=("Which of the following identifies the connection the framework draws between exchange "
         "and disease in this period?"),
      choices=[
        "It places the diffusion of pathogens along trade routes, so the same connections that carried goods are treated as the paths disease travelled.",
        "It treats disease as having spread independently of any route, by ways the framework does not describe.",
        "It treats disease as a cause of the trade routes rather than something carried along them.",
        "It treats trade routes as having protected the regions they linked from disease.",
        "It makes no statement connecting disease with exchange in this period.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens, with "
           "epidemic diseases, including the bubonic plague, ALONG TRADE ROUTES. The prepositional "
           "phrase is what makes this an environmental consequence of connectivity rather than a "
           "separate subject.")),

 dict(q=("HYPOTHETICAL counts of the regions in which three crops are recorded, before and during "
         "this period, are given in the table below. Which conclusion is best supported by that "
         "data alone?"),
      table=_T_CROPS,
      choices=[
        "Every crop listed is already recorded somewhere before the period and is recorded in more regions during it, so what the figures show is a spread continuing rather than beginning.",
        "Every crop listed is recorded in no region before the period, so the figures show a spread beginning within it.",
        "Every crop listed is recorded in fewer regions during the period than before it.",
        "The crop recorded in the most regions before the period is recorded in the fewest during it.",
        "All three crops listed are recorded in the same number of regions during the period.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.1.IV states that there was "
           "CONTINUED diffusion of crops and pathogens along trade routes, and a crop already "
           "present somewhere and present in more places later is that continuation in figures. "
           "The anchor carries both clauses because the strongest distractor denies the earlier "
           "presence.")),

 dict(q=("An unattributed account from a coastal district reports that a fruit unknown there a "
         "generation earlier is now grown in its gardens, having been brought by traders from a "
         "region across the sea. Which of the following identifies the pattern this illustrates?"),
      choices=[
        "The diffusion of a crop along a route of exchange, which the framework treats as one of the environmental effects of connectivity.",
        "The independent appearance of the same crop in two regions without any movement between them.",
        "The disappearance of a crop from the region in which it had been grown before.",
        "The confinement of cultivation to the crops native to a district.",
        "The replacement of trade in goods by trade in plants alone.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens along "
           "trade routes, and Learning Objective K asks students to explain the environmental "
           "effects of the various networks of exchange in Afro-Eurasia from c. 1200 to c. 1450.")),

 dict(q=("The table below carries HYPOTHETICAL counts for three routes, giving the crops recorded "
         "as newly present along each and the epidemic outbreaks recorded along it. Which "
         "conclusion does the data best support?"),
      table=_T_ROUTES,
      choices=[
        "Every route listed records both crops and outbreaks, and the route recording the most crops is not the route recording the most outbreaks.",
        "Every route listed records both crops and outbreaks, and the route recording the most crops also records the most outbreaks.",
        "One of the routes listed records crops but no outbreak.",
        "None of the routes listed records any outbreak.",
        "Outbreaks outnumber newly present crops on every route listed.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.1.IV puts the diffusion of "
           "crops and of pathogens in one clause about trade routes, so both appearing along "
           "every route is what the sentence predicts, while the framework nowhere makes their "
           "quantities move together. The anchor carries both clauses because the strongest "
           "distractor asserts that the two maxima coincide.")),

 dict(q=("Which of the following identifies what the word including does in the phrase epidemic "
         "diseases, including the bubonic plague?"),
      choices=[
        "It presents the plague as one instance of a wider class of epidemic diseases rather than as the whole of what the framework asserts.",
        "It presents the plague as the only epidemic disease of the period.",
        "It presents the plague as excluded from the class of epidemic diseases.",
        "It presents epidemic disease as a subdivision of the plague.",
        "It presents the plague as a crop rather than a pathogen.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens, with "
           "epidemic diseases, INCLUDING the bubonic plague, along trade routes. The word marks "
           "an instance of a class, which is the same function it performs in the framework's "
           "other sentences.")),

 dict(q=("Which of the following identifies what the Humans and the Environments thematic focus "
         "adds to a study of exchange?"),
      choices=[
        "That the relation runs both ways, the environment shaping human societies and those societies in turn shaping their environments as they grow and change.",
        "That the environment shapes human societies while remaining unaffected by them.",
        "That human societies shape their environments while remaining unaffected by them.",
        "That the environment and human societies have no bearing on one another.",
        "That environmental factors bear on settlement but never on exchange.",
      ], ans=0,
      why=("The Humans and the Environments thematic focus states that the environment shapes "
           "human societies, and as populations grow and change, these populations IN TURN shape "
           "their environments, while KC-3.1.IV supplies what this topic's environment carries "
           "along its trade routes. The anchor carries both directions because two distractors "
           "keep one and drop the other.")),

 dict(q=("An unattributed chronicle records that a district into which a new grain had been "
         "introduced was able to feed more people than before, and that new ground was broken for "
         "planting where woodland had stood. Which of the following identifies the pattern?"),
      choices=[
        "A crop arriving by exchange changing what a population could do, and that population in turn changing the ground it lived on, which is the two-way relation the framework describes.",
        "A population changing its environment without any change reaching it from outside.",
        "An environment changing a population without any change made by that population.",
        "A district whose environment and population were both unaffected by the arrival.",
        "A crop arriving by exchange and being abandoned without effect.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops along trade routes, and "
           "the Humans and the Environments thematic focus states that the environment shapes "
           "human societies and that as populations grow and change these populations in turn "
           "shape their environments.")),

 dict(q=("Which of the following claims about this topic does the framework NOT support?"),
      choices=[
        "That the diffusion of pathogens along trade routes was confined to a single region of Afro-Eurasia.",
        "That the diffusion of crops along trade routes continued in this period.",
        "That the diffusion of pathogens along trade routes continued in this period.",
        "That epidemic diseases were among the pathogens that diffused.",
        "That the bubonic plague was one of those epidemic diseases.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens, with "
           "epidemic diseases, including the bubonic plague, along trade routes, and Learning "
           "Objective K frames the topic as the environmental effects of the various networks of "
           "exchange IN AFRO-EURASIA. No confinement to one region is asserted anywhere.")),

 dict(q=("A student argues that the benefits and the harms of connectivity in this period cannot "
         "be separated. Which of the following best supports that argument from this topic?"),
      choices=[
        "That the framework names the diffusion of crops and of pathogens in a single clause about the same trade routes, so the routes that carried food carried disease as well.",
        "That the framework names crops in one sentence and pathogens in another about different routes.",
        "That the framework denies that crops moved along trade routes at all.",
        "That the framework denies that pathogens moved along trade routes at all.",
        "That the framework treats the benefits of exchange as belonging to a later period than its harms.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of CROPS AND PATHOGENS, with "
           "epidemic diseases, including the bubonic plague, along trade routes. One clause, one "
           "set of routes, two kinds of cargo.")),

 dict(q=("Which of the following would be the strongest evidence that a disease travelled along "
         "trade routes rather than spreading outward evenly from one place?"),
      choices=[
        "Records showing it appearing first in places connected by traffic and only later in nearer places off the route.",
        "Records showing it appearing in many places within a single year.",
        "Records showing that the places it reached were of different sizes.",
        "Records showing that it reached both coastal and inland places.",
        "Records showing that it was described by writers in more than one language.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens, with "
           "epidemic diseases, including the bubonic plague, ALONG TRADE ROUTES. Order of arrival "
           "following connection rather than distance is what movement along a route would leave "
           "in a record.")),

 dict(q=("An unattributed account describes a port whose ships were turned away for a season "
         "after news arrived of sickness in the places they had come from. Which of the following "
         "identifies what such a measure implies about how the sickness was understood?"),
      choices=[
        "That it was thought to travel with the traffic, which is the connection the framework draws between epidemic disease and trade routes.",
        "That it was thought to arise independently in every place it appeared.",
        "That it was thought to be carried only by people who were already dead.",
        "That it was thought to be unconnected with any movement of people or goods.",
        "That it was thought to be confined to the port itself and incapable of travelling.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens, with "
           "epidemic diseases, including the bubonic plague, along trade routes. A measure aimed "
           "at arriving traffic is a measure aimed at the path the framework names.")),

 dict(q=("Which of the following identifies why the framework treats the movement of a crop as an "
         "ENVIRONMENTAL effect of exchange rather than only an economic one?"),
      choices=[
        "Because a crop taking root in a new region changes what grows there and what the ground is used for, which is a change in the environment itself and not only in what is bought and sold.",
        "Because crops in this period were not bought or sold at all.",
        "Because the framework treats every economic change as environmental by definition.",
        "Because a crop's arrival has no effect on the region that receives it.",
        "Because the framework treats environmental change as confined to disease.",
      ], ans=0,
      why=("Learning Objective K asks students to explain the ENVIRONMENTAL effects of the "
           "various networks of exchange, KC-3.1.IV places the diffusion of crops among them, and "
           "the Humans and the Environments thematic focus states that populations shape their "
           "environments as they grow and change.")),

 dict(q=("Two students disagree about a crop found in two distant regions. One says it must have "
         "been carried between them; the other says it may have appeared in each independently. "
         "Which of the following identifies what would settle the question?"),
      choices=[
        "Evidence of a route joining the two and of the crop's presence at points along it, since the framework's account of diffusion runs through the connections between places.",
        "Evidence that the crop is useful in both regions, since usefulness explains its presence.",
        "Evidence that the two regions have similar soils, since similar ground grows similar plants.",
        "Evidence that the crop is recorded in both regions in the same century, since simultaneity establishes transmission.",
        "Nothing could settle it, since the framework treats the origin of crops as unknowable.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued DIFFUSION of crops and pathogens ALONG "
           "TRADE ROUTES, which makes the route the framework's own mechanism. Suggested skill "
           "5.A asks for connections between developments, and a connection is what "
           "simultaneity by itself does not supply.")),

 dict(q=("Which of the following identifies a limit on what KC-3.1.IV allows a student to claim?"),
      choices=[
        "It states that epidemic diseases diffused along trade routes without stating how many people they killed or in which years they arrived.",
        "It states precisely how many people the epidemic diseases of the period killed.",
        "It states that no epidemic disease diffused in the period.",
        "It states that only one disease diffused and names no class beyond it.",
        "It states that crops diffused while denying that pathogens did.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens, with "
           "epidemic diseases, including the bubonic plague, along trade routes. It supplies no "
           "mortality, no date and no mechanism, so a key resting on any of those would rest on "
           "something outside the framework.")),

 dict(q=("An unattributed record from an inland town notes that its market was closed for a year "
         "and that fields near it went unharvested. Which of the following identifies the "
         "soundest use of such a record in an argument about this topic?"),
      choices=[
        "As one local instance of the kind of disruption an epidemic could produce, supporting a general claim rather than establishing by itself what happened across Afro-Eurasia.",
        "As proof that the same disruption occurred in every town of Afro-Eurasia.",
        "As evidence that no epidemic reached the town, since the record does not name one.",
        "As a substitute for any general claim, since a vivid case argues for itself.",
        "As evidence about the town only if the town can be shown to be typical in every respect.",
      ], ans=0,
      why=("KC-3.1.IV asserts the diffusion of epidemic diseases along trade routes as a general "
           "development, and Learning Objective K asks for the environmental effects of the "
           "various networks of exchange in Afro-Eurasia. One town's record illustrates a general "
           "claim without establishing it and without needing to be typical.")),

 dict(q=("Which of the following pairs a development from this topic with a genuine consequence "
         "rather than a coincidence?"),
      choices=[
        "A trade route in regular use, paired with the appearance along it of a crop that had not grown there before.",
        "A trade route in regular use, paired with the fact that agriculture existed somewhere in Afro-Eurasia at the same time.",
        "An epidemic disease, paired with the fact that people had always been liable to illness.",
        "The diffusion of a crop, paired with the fact that the regions concerned had names.",
        "A closed market, paired with the fact that markets are held on fixed days.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens along "
           "trade routes, which makes a crop's arrival along a route a consequence the framework "
           "asserts. Suggested skill 5.A asks for connections between developments, and the four "
           "rejected pairings attach a development to a circumstance that would hold anyway.")),

 dict(q=("Which of the following identifies the difference between saying a disease was present "
         "in a region and saying it diffused there?"),
      choices=[
        "The first records a state of affairs and the second asserts that it arrived from elsewhere, which is a claim about movement and needs evidence of a path.",
        "The first asserts that it arrived from elsewhere and the second records a state of affairs.",
        "The two are the same claim expressed in different words.",
        "The first concerns crops and the second concerns pathogens.",
        "Neither claim can be made about this period, since the framework is silent about disease.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued DIFFUSION of crops and pathogens, with "
           "epidemic diseases, including the bubonic plague, ALONG TRADE ROUTES. Diffusion is the "
           "framework's word and it is a claim about movement along a path. The anchor carries "
           "both halves in order because the strongest distractor exchanges them.")),

 dict(q=("A historian argues that the environmental effects of exchange in this period should be "
         "studied across Afro-Eurasia rather than region by region. Which of the following best "
         "supports that argument from this topic?"),
      choices=[
        "That the learning objective frames the environmental effects as those of the various networks of exchange IN AFRO-EURASIA, and the routes it names crossed the regions rather than staying within them.",
        "That the framework describes each region's environment as unconnected with every other.",
        "That the framework treats crops as moving only within the region where they originated.",
        "That the framework treats epidemic disease as a purely local phenomenon.",
        "That the framework describes trade routes as ending at the boundary of each region.",
      ], ans=0,
      why=("Learning Objective K asks students to explain the environmental effects of the "
           "various networks of exchange IN AFRO-EURASIA from c. 1200 to c. 1450, and KC-3.1.IV "
           "places the diffusion of crops and pathogens along trade routes, which are what join "
           "the regions.")),

 dict(q=("An unattributed traveller's note records that a plant he had seen only in one country "
         "was now growing beside the road in another, many weeks' journey away, and that nobody "
         "there recalled a time before it. Which of the following identifies what the note is "
         "good evidence for?"),
      choices=[
        "That the plant had spread beyond its earlier range and had been established long enough for its arrival to have passed out of memory, which is what a continuing diffusion looks like from inside.",
        "That the plant had originated in the second country and spread to the first.",
        "That the plant had never grown anywhere but the second country.",
        "That the plant arrived in the second country during the traveller's own visit.",
        "That the two countries had no connection of any kind between them.",
      ], ans=0,
      why=("KC-3.1.IV states that there was CONTINUED diffusion of crops and pathogens along "
           "trade routes, and the CED states that developments are not constrained by the given "
           "dates and may begin before the period. A spread already beyond living memory is that "
           "continuation seen from within.")),

 dict(q=("Which of the following identifies the connection between this topic and the topics on "
         "the routes themselves?"),
      choices=[
        "The routes whose volume and range those topics describe are the paths along which the framework places the diffusion of crops and pathogens, so the same networks carry both subjects.",
        "The routes described in those topics are different routes from the ones along which diffusion occurred.",
        "The framework treats environmental effects as having occurred before any route existed.",
        "The framework treats the routes as having been created by the diffusion of crops.",
        "The framework treats the two subjects as belonging to different periods.",
      ], ans=0,
      why=("KC-3.1.IV places the diffusion of crops and pathogens ALONG TRADE ROUTES, and "
           "KC-3.1.I.A.i, KC-3.1.I.A.ii and KC-3.1.I.A.iv are the sentences describing the volume "
           "and range of those same routes. Suggested skill 5.A asks for exactly such connections "
           "between processes.")),

 dict(q=("Which of the following best explains why an environmental consequence of exchange may "
         "be felt by people who never traded?"),
      choices=[
        "Because what moves along a route does not stop at the people who carry it, so a crop or a pathogen entering a region reaches those who had no part in the traffic.",
        "Because everyone in a region through which a route passes is by definition a merchant.",
        "Because the framework treats environmental effects as reaching only those who travel.",
        "Because a region's inhabitants must all consent before any crop may be introduced.",
        "Because the framework treats trade and environment as unconnected subjects.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens, with "
           "epidemic diseases, including the bubonic plague, along trade routes, and the Humans "
           "and the Environments thematic focus states that the environment shapes human "
           "societies. Neither sentence limits the effect to those who carried the traffic.")),

 dict(q=("A student claims that the environmental consequences of connectivity in this period "
         "were entirely harmful. Which of the following identifies the strongest objection from "
         "this topic?"),
      choices=[
        "The framework's single sentence names the diffusion of crops beside that of pathogens, so the same process it describes carried something a region could eat as well as something that made it ill.",
        "The framework names only pathogens, so the student has understated the harm.",
        "The framework names only crops, so no harm is asserted anywhere.",
        "The framework denies that anything diffused along trade routes in this period.",
        "The framework treats the question of harm as one no evidence could settle.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of CROPS AND PATHOGENS, with "
           "epidemic diseases, including the bubonic plague, along trade routes. Both are named "
           "in the one clause, which is what a wholly negative account leaves out.")),

 dict(q=("An unattributed register from a monastery lists the plants in its garden and marks "
         "several as having been received from a house in another country. Which of the following "
         "identifies what such a document contributes to the study of crop diffusion?"),
      choices=[
        "A record of a particular transfer, which is the kind of evidence a general claim about diffusion is built from and which can also show a path that was not commercial.",
        "A record proving that all crop diffusion in the period passed through religious houses.",
        "A record showing that crops did not move between countries in this period.",
        "A record with no bearing on diffusion, since a garden is not a field.",
        "A record showing that the plants concerned were native to both countries.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens along "
           "trade routes, and Learning Objective K asks for the environmental effects of the "
           "various networks of exchange. A documented transfer is an instance of the diffusion "
           "the sentence asserts, and the framework does not confine such movement to a single "
           "kind of carrier.")),

 dict(q=("Which of the following identifies why the framework's word diffusion is more useful "
         "here than the word spread would be on its own?"),
      choices=[
        "Because diffusion names a movement from somewhere to somewhere along a path, which is what allows the framework to attach it to trade routes.",
        "Because diffusion means the same as spread, so the choice between them is a matter of taste.",
        "Because diffusion refers only to pathogens and spread only to crops.",
        "Because diffusion describes a process with no direction, which is what the framework asserts.",
        "Because diffusion describes a movement confined within a single region.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens, with "
           "epidemic diseases, including the bubonic plague, ALONG TRADE ROUTES. The framework "
           "attaches its noun to a path, which is what makes the topic a consequence of "
           "connectivity.")),

 dict(q=("Which of the following would most weaken a claim that the arrival of a new crop in a "
         "region left that region's way of life unchanged?"),
      choices=[
        "Evidence that land not previously cultivated was brought under the plough in the years after the crop's arrival.",
        "Evidence that the crop was also grown in the region it came from.",
        "Evidence that the crop was carried by merchants rather than by settlers.",
        "Evidence that the region had traded with other regions before the crop arrived.",
        "Evidence that the crop was recorded in writing at the time of its arrival.",
      ], ans=0,
      why=("The Humans and the Environments thematic focus states that the environment shapes "
           "human societies and that as populations grow and change these populations IN TURN "
           "shape their environments, and KC-3.1.IV places the diffusion of crops along trade "
           "routes. New ground broken is the population reshaping its environment.")),

 dict(q=("Which of the following identifies what makes this topic a topic about connectivity "
         "rather than about agriculture or medicine?"),
      choices=[
        "That the framework's claim is about what moved along trade routes, so the subject is the consequence of places being joined rather than the crops or the diseases considered by themselves.",
        "That the framework treats agriculture and medicine as having no history in this period.",
        "That the framework treats crops and pathogens as the same kind of thing.",
        "That the framework denies that any crop was cultivated or any disease treated in this period.",
        "That the framework treats connectivity as a subject with no environmental dimension.",
      ], ans=0,
      why=("KC-3.1.IV states that there was continued diffusion of crops and pathogens, with "
           "epidemic diseases, including the bubonic plague, ALONG TRADE ROUTES, and Learning "
           "Objective K asks for the environmental effects OF THE VARIOUS NETWORKS OF EXCHANGE. "
           "The connection is the subject.")),

 dict(q=("Which of the following statements about the environmental consequences of connectivity "
         "is supported by this topic's content taken as a whole?"),
      choices=[
        "A diffusion already under way before the period carried both crops and pathogens along the routes of exchange, epidemic disease among them, and the regions reached were changed by what arrived and changed their own ground in turn.",
        "A diffusion beginning within the period carried crops but no pathogens, and the regions reached were unchanged by what arrived.",
        "A diffusion already under way carried pathogens but no crops, and no region altered its ground in consequence.",
        "Nothing moved along the routes of exchange except goods, and the environment of every region was unaffected.",
        "Nothing can be said about the environmental effects of exchange in this period, since the framework makes no assertion about them.",
      ], ans=0,
      why=("KC-3.1.IV supplies the continued diffusion of crops and pathogens, with epidemic "
           "diseases including the bubonic plague, along trade routes, and the Humans and the "
           "Environments thematic focus supplies the two-way relation between populations and "
           "their environments. Each rejected option contradicts one or the other.")),
]
