# AP WORLD HISTORY: MODERN 6.3 Indigenous Responses to State Expansion from 1750 to 1900
# CED effective Fall 2026, Unit 6 Consequences of Industrialization, c. 1750 to
# c. 1900. Thematic focus GOV, Governance: "A variety of internal and external
# factors contribute to state formation, expansion, and decline. Governments
# maintain order through a variety of administrative institutions, policies, and
# procedures, and governments obtain, retain, and exercise power in different ways
# and for different purposes."
#
# Unit 6 Learning Objective C: "Explain how and why internal and external factors
# have influenced the process of state building from 1750 to 1900."
# Reasoning process: Causation. Suggested skill 2.C, explain the significance of a
# source's point of view, purpose, historical situation, and/or audience, including
# how these might limit the use(s) of a source.
#
# The historical developments this topic prints, in the framework's own words:
#   KC-5.3.III.D  Increasing questions about political authority and growing
#                 nationalism contributed to anticolonial movements.
#   KC-5.2.II.C   Anti-imperial resistance took various forms, including direct
#                 resistance within empires and the creation of new states on the
#                 peripheries.
#   KC-5.3.III.E  Increasing discontent with imperial rule led to rebellions, some
#                 of which were influenced by religious ideas.
#
# Illustrative examples the CED prints for this topic, under its own three
# headings. These are the only proper names used in this module:
#   Direct resistance: the Yaa Asantewaa War in West Africa; the 1857 rebellion in
#     India. (The CED's list also names two leaders whose names carry accented
#     characters; the notation gate in es_check.py refuses non-ASCII text, and
#     respelling a person's name to satisfy a checker is not acceptable, so those
#     two examples are not used here.)
#   New states: the establishment of independent states in the Balkans; the Sokoto
#     Caliphate in modern-day Nigeria; the Cherokee Nation; the Zulu Kingdom.
#   Rebellions: the Ghost Dance in the U.S.; the Xhosa Cattle-Killing Movement in
#     Southern Africa; the Mahdist wars in Sudan.
#
# WHAT THIS BANK DOES NOT DO. The CED names these episodes and describes none of
# them. No item asks what any of them did, when it happened, who led it or how it
# ended; items ask only what the framework itself asserts, which is the heading an
# example is listed under and the general statements above. Every source is
# UNATTRIBUTED and labelled illustrative. Tables are labelled hypothetical and
# every keyed conclusion is recomputable from the table alone.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md. Dates are written "1750 to 1900".
TOPIC = ("6.3", "Indigenous Responses to State Expansion from 1750 to 1900", 6)

_T_EPISODES = dict(
    headers=["Episode (hypothetical)", "Form the episode took",
             "Religious ideas invoked by participants"],
    rows=[["Episode 1", "Armed resistance inside an existing empire", "Yes"],
          ["Episode 2", "Creation of a new state on the periphery of an empire", "No"],
          ["Episode 3", "Armed resistance inside an existing empire", "No"],
          ["Episode 4", "Armed resistance inside an existing empire", "Yes"],
          ["Episode 5", "Creation of a new state on the periphery of an empire", "Yes"]])

_T_PETITIONS = dict(
    headers=["Decade of the record (hypothetical)",
             "Petitions against the administration received",
             "Armed episodes recorded by officials"],
    rows=[["First decade", "14", "1"],
          ["Second decade", "31", "2"],
          ["Third decade", "58", "4"],
          ["Fourth decade", "96", "9"]])

QUESTIONS = [
 dict(q="According to the course framework, anti-imperial resistance in this period took various forms. Which pair of forms does the framework name?",
   choices=[
     "Direct resistance within empires, and the creation of new states on the peripheries",
     "Direct resistance within empires, and the purchase of colonies from rival empires",
     "The creation of new states on the peripheries, and the emigration of imperial officials",
     "Petitions to European parliaments, and the founding of chartered trading companies",
     "Refusal to trade with any imperial state, and the abolition of local monarchies"], ans=0,
   why="KC-5.2.II.C states that anti-imperial resistance took various forms, including direct resistance within empires and the creation of new states on the peripheries. Those two are the framework's named forms; purchase, emigration, petitions to parliaments, company founding, trade refusal and the abolition of monarchies are not asserted there."),
 dict(q="Which of the following does the framework list as a new state created on the periphery of an empire rather than as a rebellion?",
   choices=[
     "The Sokoto Caliphate in modern-day Nigeria",
     "The Ghost Dance in the United States",
     "The Xhosa Cattle-Killing Movement in Southern Africa",
     "The Mahdist wars in Sudan",
     "The 1857 rebellion in India"], ans=0,
   why="The CED lists the Sokoto Caliphate in modern-day Nigeria under new states, and lists the Ghost Dance, the Xhosa Cattle-Killing Movement and the Mahdist wars under rebellions, with the 1857 rebellion in India under direct resistance. KC-5.2.II.C is the general statement that new states on the peripheries are one form anti-imperial resistance took."),
 dict(q="The framework's example concerning the Balkans in this topic illustrates",
   choices=[
     "the establishment of independent states on the periphery of an empire",
     "a rebellion influenced by religious ideas",
     "direct armed resistance that left the empire's borders unchanged",
     "the transfer of a colony from a chartered company to a government",
     "the founding of a settler colony by an industrialized state"], ans=0,
   why="The CED lists the establishment of independent states in the Balkans under new states, the heading that answers to KC-5.2.II.C's creation of new states on the peripheries. The other four options belong to other statements in this unit or to none of them."),
 dict(q="Under which of the framework's headings does the 1857 rebellion in India appear?",
   choices=[
     "Direct resistance within an empire",
     "The creation of a new state on a periphery",
     "The establishment of a settler colony",
     "The transfer of colonial control from a company to a government",
     "Economic imperialism practiced by an industrialized state"], ans=0,
   why="The CED lists the 1857 rebellion in India among its examples of direct resistance, which is the first of the two forms KC-5.2.II.C names for anti-imperial resistance. Settler colonies, company transfers and economic imperialism are the subject matter of other topics in this unit."),
 dict(q="The framework groups the Ghost Dance, the Xhosa Cattle-Killing Movement and the Mahdist wars together. The statement that accounts for that grouping is that",
   choices=[
     "discontent with imperial rule led to rebellions, some of which were influenced by religious ideas",
     "industrialized states practiced economic imperialism primarily in Asia and Latin America",
     "Europeans established settler colonies in some parts of their empires",
     "migrants often created ethnic enclaves that transplanted their culture into new environments",
     "states with existing colonies assumed direct control over colonies held by non-state entities"], ans=0,
   why="KC-5.3.III.E states that increasing discontent with imperial rule led to rebellions, some of which were influenced by religious ideas, and the CED lists these three episodes under its heading for rebellions. The four other statements are printed in this unit under different topics and account for none of these three."),
 dict(q="Which two developments does the framework identify as contributing to anticolonial movements?",
   choices=[
     "Increasing questions about political authority, and growing nationalism",
     "Increasing questions about political authority, and declining populations in the colonies",
     "Growing nationalism, and the withdrawal of imperial garrisons",
     "The spread of settler colonies, and the abolition of chartered companies",
     "Falling commodity prices, and the closing of mission schools"], ans=0,
   why="KC-5.3.III.D states that increasing questions about political authority and growing nationalism contributed to anticolonial movements. Those two are the named contributors; population decline, garrison withdrawal, settler colonies, company abolition, prices and schools are not asserted there."),
 dict(q="According to the framework, what led to the rebellions of this period?",
   choices=[
     "Increasing discontent with imperial rule",
     "The refusal of imperial states to acquire further territory",
     "An agreement among European states to withdraw from Africa",
     "The abolition of all taxation in the colonies",
     "The absence of any religious ideas among the population"], ans=0,
   why="KC-5.3.III.E states that increasing discontent with imperial rule led to rebellions, some of which were influenced by religious ideas. The framework names discontent as the cause and religion as an influence on some of the rebellions, so an absence of religious ideas is the opposite of what it says."),
 dict(q="Which two of the framework's illustrative examples are listed among new states rather than among rebellions or direct resistance?",
   choices=[
     "The Cherokee Nation and the Zulu Kingdom",
     "The Ghost Dance and the Mahdist wars",
     "The 1857 rebellion in India and the Yaa Asantewaa War",
     "The Xhosa Cattle-Killing Movement and the Ghost Dance",
     "The Yaa Asantewaa War and the Mahdist wars"], ans=0,
   why="The CED lists the Cherokee Nation and the Zulu Kingdom under new states, alongside the Balkans and the Sokoto Caliphate. The 1857 rebellion in India and the Yaa Asantewaa War are listed under direct resistance, and the Ghost Dance, the Xhosa Cattle-Killing Movement and the Mahdist wars under rebellions."),
 dict(q="The framework's West African example of direct resistance to state expansion is",
   choices=[
     "the Yaa Asantewaa War",
     "the Xhosa Cattle-Killing Movement",
     "the establishment of independent states in the Balkans",
     "the Ghost Dance",
     "the Mahdist wars in Sudan"], ans=0,
   why="The CED lists the Yaa Asantewaa War in West Africa among its examples of direct resistance, the first of the two forms of anti-imperial resistance named in KC-5.2.II.C. The Xhosa Cattle-Killing Movement, the Ghost Dance and the Mahdist wars are listed under rebellions, and the Balkans under new states."),
 dict(q="An illustrative report on a rising within a colony was written by the imperial official who commanded the troops that suppressed it. Which limitation on the report's use as evidence of the rebels' aims is most important?",
   choices=[
     "Its author had an interest in how his own conduct was judged, and he reports the rebels' aims only at second hand",
     "Its author was present during the events, so he cannot describe them accurately",
     "It was written in the imperial state's language, so its contents cannot be understood",
     "It was written after the rising ended, so it cannot report anything that happened during it",
     "It concerns a colony rather than the imperial state, so it is not a historical source"], ans=0,
   why="Suggested skill 2.C asks students to explain how a source's point of view, purpose and situation may limit its use. A commander reporting on his own operations has a stake in the judgement of them, and his account of the rebels' purposes is not their own statement of those purposes. Presence at the events, the language of composition and a later date of writing are not by themselves disqualifications."),
 dict(q="An illustrative proclamation issued by the leaders of a rebellion calls on villagers to join them and lists the burdens the administration has imposed. The proclamation is best used as evidence of",
   choices=[
     "the grievances its authors expected would persuade others to join",
     "the private calculations its authors made before issuing it",
     "the number of villagers who actually joined the movement",
     "the imperial administration's own account of its policies",
     "the religious ideas held by the administration's officials"], ans=0,
   why="Suggested skill 2.C makes a source's purpose central to its use. A recruiting proclamation is written to persuade, so what it contains is what its authors thought would move an audience; it is not a record of private reasoning, of how many responded, of official policy or of officials' beliefs."),
 dict(q="Two illustrative documents survive from the same movement: a petition addressed to the imperial government and a leaflet addressed to the movement's own supporters. A historian should expect that",
   choices=[
     "each stresses whatever its own audience was most likely to accept, so the two together show more than either alone",
     "the petition is truthful and the leaflet is not, because governments demand accuracy",
     "the leaflet is truthful and the petition is not, because supporters demand accuracy",
     "the two documents must contain the same arguments, since they come from one movement",
     "neither document can be used, because both were written to persuade"], ans=0,
   why="Suggested skill 2.C makes audience one of the features that shapes a source. Documents aimed at different audiences emphasize different things, which is a reason to read them together rather than a reason to rank one as honest and the other as false or to discard both."),
 dict(q="An illustrative memoir of a rising was written forty years after the events by one of the participants. The historical situation of that source matters most because",
   choices=[
     "the account was shaped by what had happened in the years between the events and the writing",
     "an account written long after the events must be entirely invented",
     "a participant can never describe events in which he took part",
     "a memoir is a private document and so was never intended to be read",
     "the passage of forty years makes the events themselves less important"], ans=0,
   why="Suggested skill 2.C names a source's historical situation among the features whose significance students must explain. Distance in time places the writer in a later situation, with later knowledge and later purposes, which shapes the account without making it worthless or the events less important."),
 dict(q="An illustrative petition to an imperial governor complains of new taxes and of the removal of a local authority. Used carefully, the petition is evidence for which of the framework's statements?",
   choices=[
     "That increasing discontent with imperial rule was present among the governed",
     "That the rebellion which followed was influenced by religious ideas",
     "That a new state was created on the periphery of the empire",
     "That the imperial state assumed direct control from a chartered company",
     "That migrants created an ethnic enclave in the territory"], ans=0,
   why="KC-5.3.III.E names increasing discontent with imperial rule as what led to rebellions, and a petition complaining of taxation and of a removed local authority is a direct expression of such discontent. It is not evidence of religious influence, of a new state, of a company transfer or of migration, none of which it mentions."),
 dict(q="A student uses a single official dispatch as proof that a colony's population was uniformly loyal. The strongest objection is that",
   choices=[
     "one official's dispatch reports what that official saw and chose to report, not the views of a whole population",
     "official dispatches were never preserved and so cannot be consulted",
     "loyalty is a religious idea and therefore cannot be studied historically",
     "a dispatch written in the colony cannot describe events in the colony",
     "the framework forbids the use of government sources of any kind"], ans=0,
   why="Suggested skill 2.C asks how point of view and purpose limit a source's use. A single dispatch is one vantage point with its own purposes, and a claim about a whole population's views needs evidence about that population. The framework places no ban on government sources and offers no reason to doubt that dispatches survive."),
 dict(q="The register below records five hypothetical episodes of resistance, the form each took and whether participants invoked religious ideas. How many of the episodes took a form the framework names as anti-imperial resistance?",
   choices=[
     "All five episodes",
     "Four of the five episodes",
     "Three of the five episodes",
     "Two of the five episodes",
     "None of the episodes, because the forms are not among those the framework names"], ans=0,
   table=_T_EPISODES,
   why="KC-5.2.II.C names direct resistance within empires and the creation of new states on the peripheries. Every row of the register records one or the other of those two forms, three of them armed resistance inside an existing empire and two of them the creation of a new state on a periphery, so all five fall within the framework's named forms."),
 dict(q="In the same hypothetical register, which episode combines the creation of a new state on a periphery with the invoking of religious ideas?",
   choices=[
     "Episode 5",
     "Episode 1",
     "Episode 2",
     "Episode 3",
     "Episode 4"], ans=0,
   table=_T_EPISODES,
   why="Read from the register alone: Episode 5 is the only row whose form column records the creation of a new state on a periphery and whose religion column records that religious ideas were invoked. Episode 2 is the other new state and records no religious ideas; Episodes 1 and 4 invoke religious ideas but are armed resistance inside an empire."),
 dict(q="Counting the same hypothetical register, in how many episodes did participants invoke religious ideas?",
   choices=[
     "Three of the five episodes",
     "One of the five episodes",
     "Two of the five episodes",
     "Four of the five episodes",
     "All five episodes"], ans=0,
   table=_T_EPISODES,
   why="The register records religious ideas in Episodes 1, 4 and 5 and not in Episodes 2 and 3, which is three of five. KC-5.3.III.E says only that SOME rebellions were influenced by religious ideas, so a register in which some rows record religion and others do not is what the framework leads a student to expect."),
 dict(q="A student concludes from the same hypothetical register that religious ideas caused every episode it records. The register refutes this because",
   choices=[
     "two of the five episodes record no religious ideas at all",
     "the register does not name the empire in which each episode occurred",
     "the register does not record how long each episode lasted",
     "the register records forms of resistance rather than dates",
     "the register was compiled by officials rather than by participants"], ans=0,
   table=_T_EPISODES,
   why="The refutation has to come from the data the student is using, and the register's religion column reads No for Episodes 2 and 3. The other four statements are true of the register but leave the claim standing, and KC-5.3.III.E itself says religious ideas influenced only some rebellions."),
 dict(q="The record below reports, for four hypothetical decades in one colony, the petitions received against the administration and the armed episodes officials recorded. Which conclusion is supported?",
   choices=[
     "Both the petitions and the armed episodes rise in every decade recorded",
     "The petitions rise while the armed episodes fall in every decade recorded",
     "The armed episodes rise while the petitions fall in every decade recorded",
     "Both figures remain unchanged across the four decades",
     "The final decade records fewer petitions than the first"], ans=0,
   table=_T_PETITIONS,
   why="Read from the record alone: petitions run 14, 31, 58 and 96 and armed episodes run 1, 2, 4 and 9, so both columns rise at every step. Each of the four rejected statements contradicts one or both of those sequences."),
 dict(q="A historian argues that the record of those four hypothetical decades shows increasing discontent with the administration. Which objection to that reading is the most serious?",
   choices=[
     "The record counts what officials received and wrote down, which may itself have changed over the four decades",
     "The record covers four decades rather than five",
     "The record does not state the name of the colony",
     "The record gives whole numbers rather than percentages",
     "The record lists petitions before armed episodes"], ans=0,
   table=_T_PETITIONS,
   why="Suggested skill 2.C asks how a source's purpose and situation limit its use, and these are administrative counts: a rise in recorded episodes may reflect a change in what was recorded as well as a change in what occurred. The length of the record, the missing name, the units and the column order do not bear on whether the counts measure discontent."),
 dict(q="Learning objective C asks how internal and external factors influenced state building. Which of the following pairs an internal factor with an external one as the topic presents them?",
   choices=[
     "Growing nationalism within a society, and rule imposed on it by an outside empire",
     "Growing nationalism within a society, and religious ideas held within that same society",
     "An imperial administration's tax policy, and that same administration's army",
     "A rebellion's leadership, and the same rebellion's supporters",
     "A colony's harvest, and the same colony's weather"], ans=0,
   why="KC-5.3.III.D names growing nationalism and questions about political authority as arising within societies, while imperial rule is imposed from outside, which is the pairing the learning objective asks students to explain. Each rejected option puts both items on the same side of that line."),
 dict(q="Why does the framework treat the creation of a new state on a periphery as a form of anti-imperial resistance rather than as something separate from it?",
   choices=[
     "Because establishing a state outside imperial control is itself a refusal of that control",
     "Because every new state of the period was founded by an imperial government",
     "Because new states were always created before any empire reached the region",
     "Because the framework defines resistance as any change of government anywhere",
     "Because new states on peripheries were required to pay tribute to the empire"], ans=0,
   why="KC-5.2.II.C names the creation of new states on the peripheries as one of the forms anti-imperial resistance took, so the framework's own classification treats it as resistance. Nothing in the statement makes such states imperial foundations, prior to empire, tributary, or turns every change of government into resistance."),
 dict(q="An illustrative account describes a movement that took up arms against an imperial administration while remaining inside the empire's borders. Within the framework's classification this is",
   choices=[
     "direct resistance within an empire",
     "the creation of a new state on a periphery",
     "an ethnic enclave created by migrants",
     "a settler colony established by an imperial state",
     "an example of economic imperialism"], ans=0,
   why="KC-5.2.II.C names direct resistance within empires as one of the two forms anti-imperial resistance took, and a movement that fights the administration without leaving the empire's borders is that form. Enclaves, settler colonies and economic imperialism belong to other statements in this unit."),
 dict(q="A student writes that religious ideas explain all anticolonial activity in this period. The framework's own wording corrects this because it says that",
   choices=[
     "some of the rebellions were influenced by religious ideas, not all of them",
     "no rebellion of the period was influenced by religious ideas",
     "religious ideas influenced only movements outside empires",
     "religious ideas were confined to the imperial states themselves",
     "every anticolonial movement was founded on a religious doctrine"], ans=0,
   why="KC-5.3.III.E reads that increasing discontent with imperial rule led to rebellions, some of which were influenced by religious ideas. The word some is the correction: the framework asserts religious influence on part of the phenomenon and separately names questions about political authority and growing nationalism in KC-5.3.III.D."),
 dict(q="How are the two statements about anticolonial movements and about rebellions related as the framework presents them?",
   choices=[
     "Both name causes arising from the experience of imperial rule, one in political questions and nationalism and the other in discontent",
     "Both name causes arising outside the societies concerned, in the policies of rival empires",
     "The first names a cause and the second denies that any cause can be identified",
     "The two statements describe the same episodes under different names",
     "Neither statement concerns the period from 1750 to 1900"], ans=0,
   why="KC-5.3.III.D attributes anticolonial movements to increasing questions about political authority and growing nationalism, and KC-5.3.III.E attributes rebellions to increasing discontent with imperial rule. Both locate the cause in how imperial rule was experienced by the governed, and both are printed under this unit, whose span is c. 1750 to c. 1900."),
 dict(q="Which question about a rebellion in this period can be answered from the framework's statements, and which cannot?",
   choices=[
     "Whether the framework attributes rebellions to discontent with imperial rule can be answered; how many people took part in any particular rebellion cannot",
     "How many people took part in any particular rebellion can be answered; whether the framework attributes rebellions to discontent cannot",
     "Neither the framework's stated cause nor its named forms of resistance can be answered",
     "Both the framework's stated cause and the casualty figures of each rebellion can be answered",
     "Only the year in which each rebellion began can be answered"], ans=0,
   why="KC-5.3.III.E states the cause the framework attributes to rebellions and KC-5.2.II.C names the forms resistance took, so those are answerable from the framework. Participant numbers, casualties and dates for particular episodes are not printed anywhere in this topic; the CED lists the episodes as illustrative examples without describing them."),
 dict(q="An illustrative source records that a movement's leaders justified their rising by appealing both to a religious prophecy and to the removal of a ruler the population had recognized. The source is best used as evidence that",
   choices=[
     "religious ideas and questions about political authority could operate together in one movement",
     "religious ideas and questions about political authority were never present in the same movement",
     "the movement was created by the imperial administration itself",
     "the movement sought to establish a chartered trading company",
     "the movement had no connection to imperial rule of any kind"], ans=0,
   why="KC-5.3.III.E names religious ideas as an influence on some rebellions and KC-5.3.III.D names increasing questions about political authority as a contributor to anticolonial movements. A source containing both appeals shows the two working in one episode, which is consistent with the framework's separate statements rather than a contradiction of them."),
 dict(q="Why is the framework's list of resistance episodes described as illustrative rather than exhaustive?",
   choices=[
     "Because the statements it illustrates are general claims about forms and causes, not a complete inventory of episodes",
     "Because the episodes listed are the only ones that occurred in the period",
     "Because the framework treats each listed episode as more significant than any unlisted one",
     "Because students are required to memorize the listed episodes and no others exist",
     "Because the list was compiled from a single colony's records"], ans=0,
   why="The CED prints these episodes under the heading of illustrative examples beside general statements: KC-5.2.II.C on the forms anti-imperial resistance took and KC-5.3.III.E on the rebellions discontent produced. An example illustrates a general claim and does not exhaust the cases falling under it."),
 dict(q="Taking the topic as a whole, what does it add to the account of state expansion given in the preceding topic?",
   choices=[
     "That the populations on the receiving end of expansion acted in ways that shaped what followed",
     "That expansion produced no response of any kind from the populations affected",
     "That expansion was carried out entirely without the use of force",
     "That imperial states abandoned every territory they had acquired",
     "That state building in this period involved no external factors at all"], ans=0,
   why="KC-5.2.II.C, KC-5.3.III.D and KC-5.3.III.E together describe resistance, anticolonial movements and rebellions arising among the governed, and learning objective C asks how internal and external factors influenced state building. That is a claim about action by the governed, not about its absence, and the previous topic's warfare in Africa already shows force in use."),
]
