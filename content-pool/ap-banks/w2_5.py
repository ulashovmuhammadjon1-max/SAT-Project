# AP WORLD HISTORY: MODERN 2.5 Cultural Consequences of Connectivity  (title copied
# verbatim from WORLD_HISTORY_topics.json). Unit 2 Networks of Exchange, c. 1200 to
# c. 1450. Suggested skill 2.A, identify a source's point of view, purpose, historical
# situation, and/or audience.
#
# THE CED CONTENT OF THIS TOPIC, in the framework's own words:
#
#   Thematic focus CDI: the development of ideas, beliefs, and religions illustrates
#           how groups in society view themselves, and the interactions of societies
#           and their beliefs often have political, social, and cultural implications.
#   LO 2.J  Explain the intellectual and cultural effects of the various networks of
#           exchange in Afro-Eurasia from c. 1200 to c. 1450.
#   KC-3.1.III.D  Increased cross-cultural interactions resulted in the diffusion of
#           literary, artistic, and cultural traditions, as well as scientific and
#           technological innovations.
#   KC-3.3.II  The fate of cities varied greatly, with periods of significant decline
#           and periods of increased urbanization, buoyed by rising productivity and
#           expanding trade networks.
#   KC-3.1.III.C  As exchange networks intensified, an increasing number of travelers
#           within Afro-Eurasia wrote about their travels.
#
#   Illustrative examples printed on this topic page: diffusion of cultural traditions
#           -- the influence of Buddhism in East Asia, the spread of Hinduism and
#           Buddhism into Southeast Asia, the spread of Islam in sub-Saharan Africa and
#           Asia; diffusion of scientific or technological innovations -- gunpowder
#           from China, paper from China; travelers -- Ibn Battuta, Margery Kempe,
#           Marco Polo. The CED states that illustrative examples "do not in any way
#           constitute additional, preferred, or required information", so no key here
#           turns on one.
#
# THE SUGGESTED SKILL IS A SOURCING SKILL, WHICH SHAPES EVERY ITEM. Skill 2.A asks a
# student to identify a source's point of view, purpose, historical situation and
# audience, so most items here put an unattributed source in front of the student and
# ask what may be inferred from WHO WROTE IT, WHY, WHEN AND FOR WHOM -- not what
# happened. That is the question shape the real exam's short-answer primary-source
# prompts use, and it is what this topic page exists to teach.
#
# THE RULE THAT MATTERS MOST IN THIS PARTICULAR TOPIC. KC-3.1.III.C is the framework's
# sentence about travel writers, and the page names three of them. NOT ONE WORD IS PUT
# INTO ANY OF THEIR MOUTHS ANYWHERE IN THIS MODULE. Every source below is explicitly
# unattributed and written for the item, because inventing a passage and signing a real
# traveller's name to it would be a fabrication a student would read as a real
# quotation, and the CED does not print those texts for anyone to check against.
#
# ON DATES. Spans are written "c. 1200 to c. 1450". The CED states that events,
# processes, and developments are not constrained by the given dates and may begin
# before, or continue after, the period, so no key turns on a boundary year.
TOPIC = ("2.5", "Cultural Consequences of Connectivity", 2)

_T_CITIES = dict(
    headers=["City (hypothetical)", "Households recorded at an earlier date",
             "Households recorded at a later date"],
    rows=[["City One", "9,000", "4,000"],
          ["City Two", "5,000", "12,000"],
          ["City Three", "7,000", "7,000"]])

_T_ACCOUNTS = dict(
    headers=["Period (hypothetical)", "Surviving accounts of travel",
             "Recorded long-distance journeys"],
    rows=[["Earlier", "4", "30"],
          ["Middle", "11", "70"],
          ["Later", "26", "150"]])

_T_SPREAD = dict(
    headers=["Practice or innovation (hypothetical)",
             "Regions in which it is recorded in an earlier period",
             "Regions in which it is recorded in a later period"],
    rows=[["Practice One", "2", "5"],
          ["Practice Two", "1", "6"],
          ["Practice Three", "3", "4"]])

QUESTIONS = [
 dict(q=("An unattributed account of a distant city was written by a traveller for readers in "
         "his own country who had never been there. It dwells at length on the customs he found "
         "strange and says little about what resembled what he already knew. Which of the "
         "following best identifies the effect of the intended audience on the account?"),
      choices=[
        "It selects for what would be unfamiliar to that audience, so the account's emphasis reflects what its readers did not know rather than what mattered most in the city described.",
        "It selects for what was most important in the city described, since a traveller records what he judges significant.",
        "It has no effect on the account, since an audience receives a text without shaping it.",
        "It makes the account worthless as evidence, since a text written for readers cannot be used by a historian.",
        "It shows that the traveller had not visited the city at all.",
      ], ans=0,
      why=("Suggested skill 2.A asks students to identify a source's point of view, purpose, "
           "historical situation and AUDIENCE, and KC-3.1.III.C states that as exchange networks "
           "intensified, an increasing number of travelers within Afro-Eurasia wrote about their "
           "travels. An audience that has never seen a place is what makes strangeness worth "
           "reporting.")),

 dict(q=("Which of the following identifies what KC-3.1.III.C asserts about writing and exchange "
         "in this period?"),
      choices=[
        "That as exchange networks intensified, an increasing number of travellers within Afro-Eurasia wrote about their travels.",
        "That travel writing declined as exchange networks intensified.",
        "That travel writing was confined to a single region of Afro-Eurasia.",
        "That travellers wrote only when their journeys had been unsuccessful.",
        "That the number of travellers rose while the number who wrote fell.",
      ], ans=0,
      why=("KC-3.1.III.C states that as exchange networks intensified, an increasing number of "
           "travelers within Afro-Eurasia wrote about their travels. The sentence ties the "
           "quantity of writing to the intensity of exchange, which is what each rejected option "
           "denies.")),

 dict(q=("An unattributed report on a foreign court was written by an envoy to justify to his own "
         "ruler the expense of the journey he had made. Which of the following best identifies "
         "the effect of that purpose on the report?"),
      choices=[
        "It gives the writer a reason to present the journey as having achieved something, so a historian should ask what the report is arguing for as well as what it describes.",
        "It guarantees the report's accuracy, since an envoy answerable to a ruler dare not err.",
        "It makes the report useless, since any document with a purpose is unusable as evidence.",
        "It shows that the envoy never reached the court he describes.",
        "It removes any point of view from the report, since an official document has none.",
      ], ans=0,
      why=("Suggested skill 2.A asks students to identify a source's PURPOSE as well as its point "
           "of view, and KC-3.1.III.C records travellers within Afro-Eurasia writing about their "
           "travels in growing numbers. A document written to justify an expense is arguing as "
           "well as reporting.")),

 dict(q=("Which of the following identifies what the framework asserts about the fate of cities "
         "in this period?"),
      choices=[
        "That it varied greatly, some cities passing through significant decline and others through increased urbanization buoyed by rising productivity and expanding trade.",
        "That cities everywhere grew steadily across the period.",
        "That cities everywhere declined across the period.",
        "That the size of cities was fixed throughout the period.",
        "That cities changed only where a trade route passed through them and nowhere else.",
      ], ans=0,
      why=("KC-3.3.II states that the fate of cities varied greatly, with periods of significant "
           "decline and periods of increased urbanization, buoyed by rising productivity and "
           "expanding trade networks. Variation is the claim, and each rejected option asserts a "
           "uniformity instead.")),

 dict(q=("The table below carries HYPOTHETICAL counts of households recorded in three cities at "
         "an earlier and a later date. Which conclusion does the data best support?"),
      table=_T_CITIES,
      choices=[
        "The three cities moved in different directions, one downward, one upward and one not at all, so no single account of what happened to cities fits all of them.",
        "Every city listed held more households at the later date.",
        "Every city listed held fewer households at the later date.",
        "The city with the most households at the earlier date also had the most at the later date.",
        "All three cities listed held the same number of households at both dates.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns, distractors included. KC-3.3.II "
           "states that the fate of cities varied greatly, with periods of significant decline "
           "and periods of increased urbanization, and figures pointing three ways at once are "
           "what that variation looks like in a record.")),

 dict(q=("An unattributed devotional text written in one region is found, in a later century, "
         "copied and used in another region far away, translated into a language the original "
         "writer did not know. Which of the following identifies what this best illustrates?"),
      choices=[
        "The diffusion of a cultural tradition through cross-cultural interaction, which the framework treats as a result of increased contact between societies.",
        "The invention of a devotional tradition in the region where the copy was found.",
        "The disappearance of the tradition from the region in which the text was written.",
        "The confinement of religious practice to the region in which a text originates.",
        "The replacement of written transmission by oral transmission in this period.",
      ], ans=0,
      why=("KC-3.1.III.D states that increased cross-cultural interactions resulted in the "
           "diffusion of literary, artistic, and cultural traditions, as well as scientific and "
           "technological innovations. A text used far from where it was written, in a new "
           "language, is diffusion in that sense.")),

 dict(q=("HYPOTHETICAL counts for three successive periods are given in the table below, showing "
         "surviving accounts of travel and recorded long-distance journeys. Which conclusion is "
         "best supported by that data alone?"),
      table=_T_ACCOUNTS,
      choices=[
        "Both counts rise across the three periods, and across the whole span the accounts multiply by a larger factor than the journeys do.",
        "Both counts rise across the three periods, and across the whole span the journeys multiply by a larger factor than the accounts do.",
        "The accounts fall across the three periods while the journeys rise.",
        "The journeys fall across the three periods while the accounts rise.",
        "Both counts are unchanged across the three periods listed.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.1.III.C states that as exchange "
           "networks intensified, an INCREASING NUMBER of travelers within Afro-Eurasia wrote "
           "about their travels, so writing growing faster than travel is the pattern that "
           "sentence describes. The anchor carries both clauses because the strongest distractor "
           "exchanges the two columns.")),

 dict(q=("An unattributed chronicle of a city records that its markets emptied over two "
         "generations and that many of its houses fell down, while a chronicle of a "
         "neighbouring city in the same years records new quarters built outside its walls. A "
         "student cites only the first. Which of the following identifies the problem?"),
      choices=[
        "The framework says the fate of cities varied greatly in this period, so a single city's record cannot be made to stand for cities in general.",
        "The framework says all cities declined in this period, so the second chronicle must be a forgery.",
        "The framework says all cities grew in this period, so the first chronicle must be a forgery.",
        "The framework says nothing about cities in this period, so neither chronicle bears on it.",
        "The framework says city records from this period are always unreliable.",
      ], ans=0,
      why=("KC-3.3.II states that the fate of cities VARIED GREATLY, with periods of significant "
           "decline and periods of increased urbanization, buoyed by rising productivity and "
           "expanding trade networks. A claim of variation is not settled by one case on either "
           "side.")),

 dict(q=("HYPOTHETICAL counts of the regions in which three practices are recorded, in an earlier "
         "and a later period, are given in the table below. Which conclusion does the data best "
         "support?"),
      table=_T_SPREAD,
      choices=[
        "Every practice listed is recorded in more regions in the later period, and the practice recorded in fewest regions earlier reaches the most regions later.",
        "Every practice listed is recorded in more regions in the later period, and the practice recorded in most regions earlier reaches the most regions later.",
        "One of the practices listed is recorded in fewer regions in the later period.",
        "The three practices listed are recorded in the same number of regions in the later period.",
        "The practice recorded in fewest regions earlier reaches the fewest regions later.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.1.III.D states that increased "
           "cross-cultural interactions resulted in the diffusion of literary, artistic, and "
           "cultural traditions, as well as scientific and technological innovations, and "
           "spreading unevenly is what diffusion looks like in a record. The anchor carries both "
           "clauses because the strongest distractor exchanges which practice spreads furthest.")),

 dict(q=("An unattributed account of a pilgrimage was written by a person of modest means, in a "
         "language spoken at home rather than in a language of learning. Which of the following "
         "best identifies what a historian may take from that fact about the source?"),
      choices=[
        "That its point of view is that of someone outside the learned and official worlds, so it may record what documents produced by those worlds pass over.",
        "That it is less accurate than a document written in a language of learning.",
        "That it was written for an audience of scholars in distant regions.",
        "That it cannot be used as evidence, since only official documents may be.",
        "That its author had no purpose in writing beyond passing the time.",
      ], ans=0,
      why=("Suggested skill 2.A asks students to identify a source's POINT OF VIEW as well as its "
           "purpose and audience, and KC-3.1.III.C records an increasing number of travelers "
           "within Afro-Eurasia writing about their travels. Who a writer is bears on what the "
           "writing notices.")),

 dict(q=("Which of the following identifies the difference between a source's purpose and its "
         "point of view?"),
      choices=[
        "Purpose is what the writer meant the text to accomplish, and point of view is the position from which the writer saw what is described, and a single text has both.",
        "Point of view is what the writer meant the text to accomplish, and purpose is the position from which the writer saw what is described.",
        "The two are the same thing under different names, so a text has only one of them.",
        "Purpose belongs to official documents and point of view to private ones, so no text has both.",
        "Neither can be identified from a text, so both are matters of speculation.",
      ], ans=0,
      why=("Suggested skill 2.A for this topic names a source's point of view, purpose, "
           "historical situation, and audience as four separable things to identify, and "
           "KC-3.1.III.C supplies the travel accounts on which the skill is practised here. The "
           "anchor carries both definitions in order because the strongest distractor exchanges "
           "them.")),

 dict(q=("An unattributed merchant's memorandum describes a technique for making a substance, "
         "noting that it was learned from craftsmen in a region the writer had visited and that "
         "it is now practised in his own city. Which of the following best identifies what the "
         "memorandum illustrates?"),
      choices=[
        "The diffusion of a technological innovation through the contact that trade created, which the framework treats alongside the diffusion of cultural traditions.",
        "The independent invention of the same technique in two places without any contact between them.",
        "The loss of a technique from the region in which it was first practised.",
        "The confinement of technical knowledge to the region in which it originates.",
        "The replacement of trade in goods by trade in knowledge alone.",
      ], ans=0,
      why=("KC-3.1.III.D states that increased cross-cultural interactions resulted in the "
           "diffusion of literary, artistic, and cultural traditions, AS WELL AS scientific and "
           "technological innovations. The framework puts both kinds of diffusion in one "
           "sentence, which is why a technique and a devotional text are instances of the same "
           "claim.")),

 dict(q=("A student uses a traveller's description of a city as evidence of that city's size. "
         "Which of the following identifies the question a historian would ask first?"),
      choices=[
        "What situation the writer was in when the account was composed, since a description written long afterwards or at second hand bears differently on the question than one written on the spot.",
        "Whether the writer's name is one a modern reader recognizes, since a famous traveller is more reliable than an obscure one.",
        "Whether the account has survived in more than one copy, since a copied text is more accurate than a unique one.",
        "Whether the account is longer than other accounts of the same city, since length is a measure of care.",
        "Nothing, since a traveller's description of a city may be used as it stands.",
      ], ans=0,
      why=("Suggested skill 2.A names a source's HISTORICAL SITUATION among the things a student "
           "must identify, and KC-3.1.III.C records the growing body of travel writing this skill "
           "is practised on. When and under what conditions a text was written bears on what it "
           "can be used to show.")),

 dict(q=("Which of the following claims about the cultural effects of exchange in this period "
         "does the framework NOT support?"),
      choices=[
        "That every society receiving a tradition from outside abandoned its own in exchange.",
        "That increased cross-cultural interactions resulted in the diffusion of cultural traditions.",
        "That increased cross-cultural interactions resulted in the diffusion of scientific and technological innovations.",
        "That an increasing number of travellers within Afro-Eurasia wrote about their travels.",
        "That the fate of cities in the period varied greatly.",
      ], ans=0,
      why=("KC-3.1.III.D asserts diffusion and KC-3.1.III.C the growth of travel writing, while "
           "KC-3.3.II asserts the variation in the fate of cities. Nothing in any of them says a "
           "receiving society gave up its own traditions, which makes that the unsupported "
           "claim.")),

 dict(q=("An unattributed account of a journey was written many years after the journey ended, "
         "from notes the writer had kept and from what he could remember. Which of the following "
         "best identifies what follows for its use as evidence?"),
      choices=[
        "The distance in time between the events and the writing is part of the source's situation, so a historian weighs the account differently from one composed on the road.",
        "The account is worthless, since only a text written at the moment of an event may be used.",
        "The account is more reliable than a contemporaneous one, since the writer had time to reflect.",
        "The delay removes the writer's point of view, since memory is impartial.",
        "The delay shows that the journey never took place.",
      ], ans=0,
      why=("Suggested skill 2.A names a source's historical situation among the things to be "
           "identified, and KC-3.1.III.C records travellers within Afro-Eurasia writing about "
           "their travels in growing numbers as exchange networks intensified. When a text was "
           "written relative to what it describes is part of that situation.")),

 dict(q=("Which of the following identifies the connection the framework draws between the growth "
         "of exchange and the growth of writing about travel?"),
      choices=[
        "The intensification of exchange networks is what the framework makes the growth in travel writing follow from, so more writing is presented as a consequence of more movement.",
        "The growth in travel writing is what the framework makes the intensification of exchange networks follow from, so more writing produced more movement.",
        "The framework presents the two as unrelated processes that happened to coincide.",
        "The framework presents the growth in travel writing as having preceded any exchange network.",
        "The framework presents travel writing as having declined while exchange intensified.",
      ], ans=0,
      why=("KC-3.1.III.C states that AS exchange networks intensified, an increasing number of "
           "travelers within Afro-Eurasia wrote about their travels. The connective makes the "
           "writing follow the exchange, and the anchor carries both halves in order because the "
           "strongest distractor reverses them.")),

 dict(q=("An unattributed letter written by a resident of a city to a kinsman elsewhere describes "
         "the arrival of a new devotional practice in the neighbourhood and the writer's own "
         "unease at it. Which of the following best identifies what the letter is good evidence "
         "for?"),
      choices=[
        "How the arrival of a practice from outside was received by at least one person in the place it reached, which is a question about reception rather than about the practice itself.",
        "The doctrinal content of the practice described, since the writer names it.",
        "The number of people in the city who adopted the practice, since the writer lived there.",
        "The place where the practice originated, since the writer says it came from elsewhere.",
        "Nothing at all, since a private letter cannot be used as historical evidence.",
      ], ans=0,
      why=("KC-3.1.III.D states that increased cross-cultural interactions resulted in the "
           "diffusion of literary, artistic, and cultural traditions, and the Cultural "
           "Developments thematic focus states that the development of ideas, beliefs, and "
           "religions illustrates how groups in society view themselves. Suggested skill 2.A asks "
           "what a particular source's point of view can and cannot establish.")),

 dict(q=("Which of the following identifies what the framework means by saying the fate of cities "
         "was buoyed by rising productivity and expanding trade networks?"),
      choices=[
        "That where cities grew, the framework attaches that growth to more being produced and to wider exchange rather than leaving it unexplained.",
        "That every city in the period grew, since productivity and trade both rose.",
        "That rising productivity and expanding trade were consequences of urban growth rather than supports of it.",
        "That cities in the period were unaffected by what was produced or exchanged around them.",
        "That the framework assigns the growth of cities to political causes alone.",
      ], ans=0,
      why=("KC-3.3.II states that the fate of cities varied greatly, with periods of significant "
           "decline and periods of increased urbanization, BUOYED BY rising productivity and "
           "expanding trade networks. The participle attaches a support to the growth without "
           "asserting that every city grew.")),

 dict(q=("Two unattributed accounts of the same foreign city disagree: one calls its people "
         "generous and the other calls them grasping. Which of the following identifies the "
         "soundest thing for a historian to do?"),
      choices=[
        "Ask what each writer was in a position to see and what each was writing for, since a difference of judgment may follow from a difference of situation rather than from one writer being wrong.",
        "Choose the account written by the better known traveller, since fame is a mark of reliability.",
        "Discard both accounts, since two sources that disagree cancel one another.",
        "Average the two descriptions, since the truth lies between any two accounts.",
        "Accept the harsher account, since a writer has less reason to invent a criticism than a compliment.",
      ], ans=0,
      why=("Suggested skill 2.A asks students to identify a source's point of view, purpose, "
           "historical situation and audience, and KC-3.1.III.C supplies the growing body of "
           "travel accounts on which that skill is exercised. Two situations can produce two "
           "honest and different judgments.")),

 dict(q=("Which of the following identifies a limit on what KC-3.1.III.D allows a student to "
         "claim?"),
      choices=[
        "It states that cross-cultural interaction resulted in diffusion without stating that any particular tradition displaced another.",
        "It states which traditions displaced which others and in what order.",
        "It states that no diffusion of any kind occurred in this period.",
        "It states that diffusion was confined to religious traditions and touched nothing else.",
        "It states that diffusion occurred only between societies that shared a language.",
      ], ans=0,
      why=("KC-3.1.III.D states that increased cross-cultural interactions resulted in the "
           "diffusion of literary, artistic, and cultural traditions, as well as scientific and "
           "technological innovations. It asserts spread, names no displacement and confines "
           "itself to no single category.")),

 dict(q=("An unattributed account of a distant region was written for readers who would use it to "
         "decide whether to send goods there. Which of the following best identifies the effect "
         "of that audience on what the account contains?"),
      choices=[
        "It gives prominence to what such readers would need to know, so prices, dangers and the customs of dealing are likely to be full while other matters are thin.",
        "It gives prominence to whatever the writer found most interesting, since an audience cannot shape a text.",
        "It makes the account a work of imagination rather than of observation.",
        "It shows that the writer had no first-hand knowledge of the region.",
        "It removes the writer's own point of view, since a practical text has none.",
      ], ans=0,
      why=("Suggested skill 2.A names AUDIENCE among the things a student identifies in a source, "
           "and KC-3.1.III.C records travellers writing about their travels in growing numbers as "
           "exchange networks intensified. What readers intend to do with a text shapes what it "
           "is worth including.")),

 dict(q=("Which of the following best identifies why a rising number of travel accounts is "
         "evidence about exchange and not only about literature?"),
      choices=[
        "Because the framework ties the increase in such writing to the intensification of exchange networks, so the writing is a trace of the movement that produced it.",
        "Because travel accounts of this period contain no literary qualities at all.",
        "Because the framework treats literature and exchange as the same subject.",
        "Because travel accounts were written only by merchants and never by anyone else.",
        "Because the number of accounts is the only evidence about exchange that survives.",
      ], ans=0,
      why=("KC-3.1.III.C states that as exchange networks intensified, an increasing number of "
           "travelers within Afro-Eurasia wrote about their travels, and Learning Objective J "
           "asks for the intellectual and cultural effects of the various networks of exchange in "
           "Afro-Eurasia.")),

 dict(q=("An unattributed official register from a city records the trades practised in each "
         "quarter and the tolls each pays. Which of the following best identifies what its "
         "purpose implies about its contents?"),
      choices=[
        "It was compiled to assess and collect, so what it records fully is what bore on assessment, and what fell outside that concern may be absent though it existed.",
        "It was compiled to describe the city completely, so anything absent from it did not exist.",
        "It was compiled for readers in other cities, so it emphasizes what would strike a stranger.",
        "It has no purpose, being a list rather than an argument.",
        "It is unusable as evidence, since a document made by authority serves that authority.",
      ], ans=0,
      why=("Suggested skill 2.A asks students to identify a source's PURPOSE, and KC-3.3.II makes "
           "the fate of cities, which such a register bears on, a subject of this topic. A "
           "document made for one administrative use is complete for that use and not for "
           "others.")),

 dict(q=("Which of the following identifies the relation the framework draws between contact "
         "between societies and change within them?"),
      choices=[
        "It treats increased cross-cultural interaction as producing diffusion, so contact is presented as a cause of change rather than as a mere setting for it.",
        "It treats diffusion as producing cross-cultural interaction, so change is presented as the cause of contact.",
        "It treats contact and change as unconnected, each running its own course.",
        "It treats contact as preventing change by fixing each society in its own practices.",
        "It treats change within societies as occurring only where no contact took place.",
      ], ans=0,
      why=("KC-3.1.III.D states that increased cross-cultural interactions RESULTED IN the "
           "diffusion of literary, artistic, and cultural traditions, as well as scientific and "
           "technological innovations. The verb makes contact the cause, and the anchor carries "
           "both halves in order because the strongest distractor reverses them.")),

 dict(q=("A student writes that because a practice is recorded in two regions, it must have "
         "spread from one to the other. Which of the following identifies the weakness?"),
      choices=[
        "Presence in two places is consistent with diffusion but does not by itself establish it, so evidence of contact or of a route between them is what turns the observation into a claim about spread.",
        "Presence in two places rules out diffusion, since a practice can exist in only one place at a time.",
        "The framework denies that any practice was recorded in more than one region.",
        "The framework treats every similarity between regions as proof of contact.",
        "The student is correct, since two occurrences of anything always share an origin.",
      ], ans=0,
      why=("KC-3.1.III.D attributes diffusion to INCREASED CROSS-CULTURAL INTERACTIONS, which "
           "means the framework's own account of spread runs through contact. Suggested skill 2.A "
           "asks what a source establishes, and a bare coincidence of presence establishes less "
           "than a route does.")),

 dict(q=("An unattributed account praises a ruler at whose court its author was a guest. Which of "
         "the following best identifies how a historian should treat it?"),
      choices=[
        "As a source whose situation gives the writer a reason to praise, so the praise is evidence of the relationship between writer and host as much as of the ruler's qualities.",
        "As a source that must be discarded, since a guest cannot report honestly.",
        "As a source of unusual reliability, since a guest sees a court from within.",
        "As a source with no point of view, since praise is a convention rather than an opinion.",
        "As a source about the writer's own country rather than about the court described.",
      ], ans=0,
      why=("Suggested skill 2.A asks students to identify a source's point of view and historical "
           "situation, and KC-3.1.III.C records the growing body of travel writing in this period. "
           "A writer's position relative to a subject is part of what the text is evidence for.")),

 dict(q=("Which of the following identifies what the Cultural Developments thematic focus adds to "
         "this topic's account of diffusion?"),
      choices=[
        "That beliefs and ideas illustrate how groups in a society view themselves, so the arrival of a tradition from outside bears on how a society understands itself and not only on what it practises.",
        "That beliefs and ideas have no implications beyond the private conduct of individuals.",
        "That the interactions of societies and their beliefs are without political or social consequence.",
        "That a society's view of itself is fixed and unaffected by anything reaching it from outside.",
        "That only material goods and never ideas move along networks of exchange.",
      ], ans=0,
      why=("The Cultural Developments thematic focus states that the development of ideas, "
           "beliefs, and religions illustrates how groups in society view themselves, and that "
           "the interactions of societies and their beliefs often have political, social, and "
           "cultural implications. KC-3.1.III.D supplies the diffusion those interactions "
           "produce.")),

 dict(q=("Which of the following would most weaken a claim that the growth of a city in this "
         "period had nothing to do with the exchange passing through it?"),
      choices=[
        "Evidence that the city's new quarters were built in the same years in which the traffic through its market multiplied.",
        "Evidence that the city had existed for several centuries before the period began.",
        "Evidence that the city's inhabitants spoke more than one language.",
        "Evidence that the city stood on a river.",
        "Evidence that a traveller wrote an account of the city.",
      ], ans=0,
      why=("KC-3.3.II states that the fate of cities varied greatly, with periods of significant "
           "decline and periods of increased urbanization, BUOYED BY rising productivity and "
           "expanding trade networks. Building and traffic growing together is the pattern that "
           "clause describes.")),

 dict(q=("A student asks why this topic is taught through sources rather than through a list of "
         "what spread where. Which of the following is the best answer?"),
      choices=[
        "Because the suggested skill for the topic is to identify a source's point of view, purpose, historical situation and audience, and almost everything known about diffusion in this period reaches us through texts written by people with all four.",
        "Because the framework holds that no diffusion can be described without naming its source.",
        "Because sources from this period are the only ones that survive from any period.",
        "Because the framework treats lists as forbidden in the study of history.",
        "Because point of view and purpose are the only subjects the topic contains.",
      ], ans=0,
      why=("Suggested skill 2.A for this topic is to identify a source's point of view, purpose, "
           "historical situation, and audience, and KC-3.1.III.C states that as exchange networks "
           "intensified, an increasing number of travelers within Afro-Eurasia wrote about their "
           "travels. Those writings are the evidence for the diffusion KC-3.1.III.D asserts.")),

 dict(q=("Which of the following statements about the cultural consequences of connectivity is "
         "supported by this topic's key concepts taken together?"),
      choices=[
        "Increased contact between societies spread traditions and techniques from one to another, the number of people writing accounts of their journeys grew as the networks intensified, and the cities along those networks rose or fell rather than following one course.",
        "Contact between societies spread nothing, travel writing declined as networks intensified, and cities everywhere grew at the same rate.",
        "Contact spread techniques but no traditions, travel writing grew, and every city declined.",
        "Contact spread traditions but no techniques, travel writing was unchanged, and cities were unaffected by trade.",
        "Nothing can be said about the cultural effects of exchange in this period, since the framework makes no assertion about them.",
      ], ans=0,
      why=("KC-3.1.III.D supplies the diffusion of literary, artistic, and cultural traditions as "
           "well as scientific and technological innovations, KC-3.1.III.C the increasing number "
           "of travelers who wrote about their travels as exchange networks intensified, and "
           "KC-3.3.II the varied fate of cities. Each rejected option contradicts at least one.")),
]
