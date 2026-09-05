# AP WORLD HISTORY: MODERN 1.4 State Building in the Americas  (title copied verbatim
# from WORLD_HISTORY_topics.json). Unit 1 The Global Tapestry, c. 1200 to c. 1450.
# Suggested skill 3.B, identify the evidence used in a source to support an argument.
#
# THE CED CONTENT OF THIS TOPIC, IN FULL. It is one learning objective and one key
# concept sentence, and that is not a truncated reading -- the topic page carries a
# single THEMATIC FOCUS block:
#
#   LO 1.I  Explain how and why states in the Americas developed and changed over time.
#   KC-3.2.I.D.i  In the Americas, as in Afro-Eurasia, state systems demonstrated
#           continuity, innovation, and diversity, and expanded in scope and reach.
#
#   Thematic focus GOV: a variety of internal and external factors contribute to state
#           formation, expansion, and decline. Governments maintain order through a
#           variety of administrative institutions, policies, and procedures, and
#           governments obtain, retain, and exercise power in different ways and for
#           different purposes.
#
#   Illustrative examples: state systems in the Americas -- Maya city-states, Mexica,
#           Inca, Chaco, Mesa Verde, Cahokia.
#
# HOW THIRTY QUESTIONS ARE WRITTEN FROM ONE SENTENCE, HONESTLY. The suggested skill
# here is 3.B, identify the EVIDENCE a source uses to support an argument, so most of
# this bank gives an unattributed account, states the argument someone draws from it,
# and asks which observation does the supporting work. The key to such an item is
# recoverable from the text printed in the stem; KC-3.2.I.D.i and the Governance
# thematic focus supply the content the item sits in. That is the alternative to
# padding the bank with facts about the Mexica or the Inca that the CED does not
# assert -- HISTORY_BRIEF.md's rule is that a key traces to a CED sentence and not to
# what the author happens to know, and the framework here is deliberately spare.
#
# Nothing is attributed to a real author. The CED's own sample activity for this topic
# points teachers at a sixteenth-century Spanish description of Tenochtitlan; that text
# is not quoted or paraphrased here, because a stimulus invented and then signed with a
# real name is fabrication.
TOPIC = ("1.4", "State Building in the Americas", 1)

_T_TRIBUTE = dict(
    headers=["Province (hypothetical)", "Loads of cloth rendered",
             "Distance from the capital in days of travel"],
    rows=[["Province One", "400", "4"],
          ["Province Two", "250", "9"],
          ["Province Three", "300", "6"]])

_T_SETTLE = dict(
    headers=["Settlement (hypothetical)", "Households in an earlier survey",
             "Households in a later survey"],
    rows=[["Settlement One", "900", "1,400"],
          ["Settlement Two", "1,200", "1,100"],
          ["Settlement Three", "300", "900"]])

_T_STORE = dict(
    headers=["Storehouse group (hypothetical)", "Capacity in units",
             "Days of travel from the nearest town"],
    rows=[["Group A", "500", "1"],
          ["Group B", "800", "2"],
          ["Group C", "200", "5"]])

QUESTIONS = [
 dict(q=("Which of the following best states what the framework claims about state systems in "
         "the Americas in the period from c. 1200 to c. 1450?"),
      choices=[
        "They demonstrated continuity, innovation and diversity and expanded in scope and reach, as state systems in Afro-Eurasia did.",
        "They remained unchanged in extent and in method throughout the period.",
        "They followed a single pattern shared by every state in the hemisphere.",
        "They contracted steadily in territory across the period.",
        "They developed along lines with no counterpart anywhere in Afro-Eurasia.",
      ], ans=0,
      why=("KC-3.2.I.D.i states that in the Americas, as in Afro-Eurasia, state systems "
           "demonstrated continuity, innovation, and diversity, and expanded in scope and reach. "
           "Every clause of the key is in that sentence and each distractor contradicts one of "
           "them.")),

 dict(q=("The framework introduces its statement about state systems in the Americas with the "
         "words as in Afro-Eurasia. What does that phrasing do?"),
      choices=[
        "It treats the Americas as showing the same general pattern of state formation as the rest of the world rather than as an exception to it.",
        "It claims that American and Afro-Eurasian states were in contact with one another during the period.",
        "It claims that states in the Americas were founded by settlers from Afro-Eurasia.",
        "It restricts the study of American states to those resembling Afro-Eurasian ones.",
        "It asserts that the two regions produced states of identical size and organization.",
      ], ans=0,
      why=("KC-3.2.I.D.i opens with the comparative phrase and then applies to the Americas the "
           "same terms KC-3.2.I.A applies to Afro-Eurasia: continuity, innovation, and "
           "diversity. A shared pattern is not contact, descent or identity.")),

 dict(q=("A state expands in scope and a state expands in reach. Which of the following best "
         "distinguishes the two as the framework pairs them?"),
      choices=[
        "Scope concerns how much a state undertakes to do, while reach concerns how far its authority extends, so a state can grow in one without growing in the other.",
        "Scope and reach are two words for the same growth in territory.",
        "Scope concerns the age of a state and reach concerns its wealth.",
        "Scope applies only to states in the Americas and reach only to states in Afro-Eurasia.",
        "Scope and reach both refer to the number of people a state governs.",
      ], ans=0,
      why=("KC-3.2.I.D.i says state systems expanded in scope AND reach, naming two things "
           "rather than one. The Governance thematic focus supplies the distinction by treating "
           "what governments do, through institutions and procedures, separately from the extent "
           "over which they do it.")),

 dict(q=("An unattributed account of a city in the Americas argues that its people were governed "
         "by an organized authority. The account reports that the streets meet at right angles, "
         "that a canal carries water into the center, that the market opens and closes at fixed "
         "hours, and that the writer found the place beautiful. Which of these is evidence for "
         "the argument?"),
      choices=[
        "That the market opens and closes at fixed hours, which implies a rule enforced on many people at once.",
        "That the writer found the place beautiful, which shows the effect it had on a visitor.",
        "That the streets meet at right angles, which is a matter of taste in building.",
        "That a canal carries water, which is a fact about the landscape rather than about people.",
        "That the account was written at all, which shows the city was worth describing.",
      ], ans=0,
      why=("Suggested skill 3.B asks students to identify the EVIDENCE a source uses to support "
           "an argument. A fixed opening hour is a rule obeyed by many, which bears on the claim "
           "of organized authority; KC-3.2.I.D.i and the Governance thematic focus supply the "
           "content, since maintaining order through procedures is what governments do.")),

 dict(q=("A historian argues that a state of the Americas exercised authority far beyond its "
         "central district. Which of the following observations would be the strongest evidence "
         "for that argument?"),
      choices=[
        "Records of goods rendered to the center by settlements many days of travel away.",
        "Records of the center's own population in a single year.",
        "Records of the materials from which the center's largest building was made.",
        "Records of a festival held annually in the central district.",
        "Records of the names of the center's rulers in order.",
      ], ans=0,
      why=("KC-3.2.I.D.i says state systems in the Americas expanded in scope and REACH, and "
           "suggested skill 3.B asks which observation supports the argument. Obligations "
           "rendered from a distance are evidence about reach; the other four concern the center "
           "alone.")),

 dict(q=("An unattributed report describes a highland state whose officials keep records of the "
         "households in each valley, move labor between valleys for building work, and store "
         "grain against a poor season. A student who cites this report as evidence that the "
         "state possessed administrative institutions would be pointing to which feature?"),
      choices=[
        "That households were recorded, labor was directed and stores were kept, since each requires a standing procedure rather than a single decision.",
        "That the valleys concerned lay in the highlands rather than on the coast.",
        "That the report describes more than one valley.",
        "That the state in question is described as a state by the report's author.",
        "That building work was carried out at all.",
      ], ans=0,
      why=("The Governance thematic focus states that governments maintain order through a "
           "variety of administrative institutions, policies, and procedures, and KC-3.2.I.D.i "
           "credits state systems in the Americas with continuity, innovation, and diversity. "
           "Skill 3.B asks which detail carries the argument.")),

 dict(q=("Which of the following would best support an argument that state systems in the "
         "Americas were diverse rather than uniform?"),
      choices=[
        "Evidence that different states in the hemisphere maintained order by different arrangements, some through a network of cities and others through a single dominant center.",
        "Evidence that every state in the hemisphere collected tribute in the same commodity.",
        "Evidence that the states of the hemisphere all reached their greatest extent in the same decade.",
        "Evidence that one state governed a larger territory than any other.",
        "Evidence that the states of the hemisphere shared a single language of administration.",
      ], ans=0,
      why=("KC-3.2.I.D.i asserts diversity among state systems in the Americas alongside "
           "continuity and innovation, and the Governance thematic focus says governments obtain, "
           "retain and exercise power in different ways and for different purposes. Uniformity "
           "in commodity, timing or language would tell the other way.")),

 dict(q=("An argument holds that a settlement was the center of a wider system rather than an "
         "isolated town. Which observation would count as evidence for that argument?"),
      choices=[
        "That goods found there were made in districts at a considerable distance from it.",
        "That its buildings were larger than those of nearby settlements.",
        "That its population was recorded as growing over several generations.",
        "That it was situated where two rivers meet.",
        "That its inhabitants worked the fields immediately around it.",
      ], ans=0,
      why=("Suggested skill 3.B asks students to identify the evidence used to support an "
           "argument; goods from distant districts show connection to other places, which is "
           "what a claim about a wider system requires. KC-3.2.I.D.i's phrase scope and reach is "
           "the framework context.")),

 dict(q=("A source describes a state of the Americas in which a governing council of several "
         "families decides matters jointly, and another in which a single ruler decides alone. "
         "Both are described as effective. What does this comparison best illustrate?"),
      choices=[
        "That governments in the period obtained, retained and exercised power in different ways, so effectiveness did not depend on one form of rule.",
        "That only one of the two arrangements can have been effective, whatever the source says.",
        "That the arrangements described must have been adopted from a single common source.",
        "That the form of a government has no bearing on how it exercises power.",
        "That councils are found only in the Americas and single rulers only in Afro-Eurasia.",
      ], ans=0,
      why=("The Governance thematic focus states that governments obtain, retain, and exercise "
           "power in different ways and for different purposes, and KC-3.2.I.D.i asserts "
           "diversity among the state systems of the Americas.")),

 dict(q=("Which of the following best explains why the framework speaks of state systems in the "
         "Americas developing and CHANGING over time rather than simply existing?"),
      choices=[
        "Because it treats these systems as carrying forward inherited arrangements while also adopting new ones and extending their authority.",
        "Because it treats them as replaced entirely at regular intervals throughout the period.",
        "Because it treats them as fixed from their foundation until the end of the period.",
        "Because it treats change in these systems as caused solely by forces outside the hemisphere.",
        "Because it treats every change in these systems as a decline.",
      ], ans=0,
      why=("Learning Objective I asks how and why states in the Americas developed and changed "
           "over time, and KC-3.2.I.D.i names continuity, innovation, and diversity together "
           "with expansion in scope and reach. Change resting on continuity is the framework's "
           "combination.")),

 dict(q=("The table below sets out HYPOTHETICAL records for three provinces of one state: the "
         "loads of cloth each rendered to the capital and its distance from that capital. Which "
         "conclusion is best supported by that data alone?"),
      table=_T_TRIBUTE,
      choices=[
        "Across the three provinces listed, the cloth rendered falls as the distance from the capital rises, though the data alone cannot say why.",
        "The most distant province listed rendered the most cloth.",
        "The three provinces listed rendered equal quantities of cloth.",
        "The data shows that distance from the capital caused the difference in cloth rendered.",
        "The province nearest the capital rendered the least cloth of the three.",
      ], ans=0,
      why=("Recomputed in the verifier from the table alone. KC-3.2.I.D.i's phrase scope and "
           "reach is the framework context for obligations rendered across distances, and the "
           "causal option overreaches what three observations can establish.")),

 dict(q=("HYPOTHETICAL household counts for three settlements, taken at an earlier and a later "
         "survey, are set out in the table below. Which statement do these numbers support?"),
      table=_T_SETTLE,
      choices=[
        "The settlement that was smallest at the earlier survey grew by the largest multiple, while one of the three declined.",
        "All three settlements listed grew between the two surveys.",
        "The settlement that was largest at the earlier survey grew by the largest multiple.",
        "The settlement that declined was the smallest at the earlier survey.",
        "None of the settlements listed declined between the two surveys.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns, distractors included. KC-3.2.I.D.i "
           "credits state systems in the Americas with diversity as well as expansion, and "
           "settlements moving in different directions at once is what such data shows.")),

 dict(q=("For three groups of storehouses, the table below gives HYPOTHETICAL capacities and "
         "the distance of each group from the nearest town. What do these numbers show?"),
      table=_T_STORE,
      choices=[
        "The group with the largest capacity is not the one closest to a town, so capacity and distance do not vary together in one direction.",
        "Capacity falls as distance from the nearest town rises, across all three groups listed.",
        "The group closest to a town has the largest capacity of the three.",
        "The three groups listed have equal capacities.",
        "The most distant group listed has the largest capacity.",
      ], ans=0,
      why=("Recomputed in the verifier: the largest capacity belongs to the middle group by "
           "distance. The Governance thematic focus treats storage and provisioning as "
           "administrative arrangements, and KC-3.2.I.D.i's diversity is what an irregular "
           "pattern illustrates.")),

 dict(q=("A student is asked to separate an argument from the evidence offered for it in a "
         "source. Which of the following is an argument rather than evidence?"),
      choices=[
        "That the state described was able to command labor from many districts at once.",
        "That two thousand workers were recorded on the site in one season.",
        "That the workers came from named districts lying at different distances.",
        "That the work was completed within a stated number of years.",
        "That the materials used were carried from a quarry some days away.",
      ], ans=0,
      why=("Suggested skill 3.B for this topic asks students to identify the evidence a source "
           "uses to support an argument, which requires telling the two apart. The first option "
           "is the conclusion the other four would be offered to establish; Learning Objective I "
           "is the content.")),

 dict(q=("What would most weaken an argument that a particular center in the Americas governed "
         "the settlements around it?"),
      choices=[
        "Evidence that the surrounding settlements rendered nothing to the center and took no direction from it.",
        "Evidence that the center was larger than the settlements around it.",
        "Evidence that the center and the settlements used similar pottery.",
        "Evidence that the center stood at the middle of the district.",
        "Evidence that the center was founded before the settlements around it.",
      ], ans=0,
      why=("The Governance thematic focus describes governments as maintaining order through "
           "institutions, policies and procedures, and KC-3.2.I.D.i speaks of reach. Absence of "
           "any obligation or direction is the observation that bears on whether authority was "
           "exercised; size, pottery, position and age do not.")),

 dict(q=("Suppose two neighboring states in the Americas both expanded during this period, one "
         "by taking territory and the other by drawing nearby settlements into rendering tribute "
         "without occupying them. How should this be described?"),
      choices=[
        "As two different means to expansion, which is consistent with the framework's claim that state systems there were diverse and expanded in scope and reach.",
        "As evidence that only one of the two states expanded at all.",
        "As evidence that expansion in the Americas always took a single form.",
        "As evidence that neither state exercised authority beyond its own center.",
        "As evidence that tribute and territory are the same thing under two names.",
      ], ans=0,
      why=("KC-3.2.I.D.i asserts diversity among state systems in the Americas and says they "
           "expanded in scope and reach; the Governance thematic focus says power is obtained "
           "and exercised in different ways. Two routes to expansion is that pair of statements "
           "applied.")),

 dict(q=("An unattributed account records that a ruler in the Americas ordered a causeway built "
         "across marshland, that labor for it was supplied in turn by several districts, and "
         "that the work took many seasons. Which argument does the account best support?"),
      choices=[
        "That the state could organize labor drawn from more than one district over a long period, which requires administration rather than a single command.",
        "That the state possessed no means of directing work beyond its own center.",
        "That the districts concerned acted independently of any central direction.",
        "That the work was carried out by people from a single settlement.",
        "That building projects of this period were completed within one season.",
      ], ans=0,
      why=("The Governance thematic focus names administrative institutions, policies, and "
           "procedures as how governments maintain order, and KC-3.2.I.D.i credits state systems "
           "in the Americas with expansion in scope and reach. Skill 3.B asks which detail "
           "carries the argument.")),

 dict(q=("Which of the following questions about states in the Americas in this period could be "
         "settled by evidence rather than by a judgment of value?"),
      choices=[
        "Whether settlements at a distance from a center rendered goods to it.",
        "Whether the obligations imposed on those settlements were just.",
        "Whether one state's arrangements were better than another's.",
        "Whether a ruler deserved the authority he exercised.",
        "Whether the labor demanded for public works was excessive.",
      ], ans=0,
      why=("KC-3.2.I.D.i asserts matters of fact about state systems expanding in scope and "
           "reach, and skill 3.B concerns evidence. Whether goods were rendered can be checked; "
           "justice, betterness, desert and excess are standards of value that observation does "
           "not settle.")),

 dict(q=("A historian claims that continuity and innovation can be observed in the same state at "
         "the same time. Which evidence from the Americas would support that claim?"),
      choices=[
        "That a state retained an inherited form of ceremonial authority while introducing new arrangements for recording and moving labor.",
        "That a state retained an inherited form of ceremonial authority and introduced nothing new.",
        "That a state abandoned its inherited ceremonial authority when it introduced new arrangements.",
        "That a state neither retained inherited forms nor introduced new arrangements.",
        "That a state's inherited forms and new arrangements were adopted in different centuries.",
      ], ans=0,
      why=("KC-3.2.I.D.i states that state systems in the Americas demonstrated continuity, "
           "innovation, and diversity, listing the terms together rather than in sequence. "
           "Holding two of them at once in one state is exactly what the sentence permits.")),

 dict(q=("An unattributed source argues that a city of the Americas held a large population, and "
         "offers as support that its market drew traders from many districts, that its "
         "storehouses were numerous, and that the author counted many hundreds of dwellings in "
         "one quarter alone. Which of these best supports the argument as stated?"),
      choices=[
        "The count of dwellings in one quarter, since population is a count of people and dwellings stand in for them.",
        "The presence of traders from many districts, since visitors are not residents.",
        "The number of storehouses, since storage capacity concerns goods rather than people.",
        "The author's decision to write the account, since that shows the city impressed him.",
        "The fact that the city had quarters at all, since every city is divided into parts.",
      ], ans=0,
      why=("Suggested skill 3.B asks which observation supports the argument actually made. The "
           "argument concerns population, so a count standing in for residents supports it "
           "while visitors and stored goods do not. KC-3.2.I.D.i is the content context.")),

 dict(q=("The framework names internal and external factors as contributing to state formation, "
         "expansion and decline. Which of the following is an internal factor?"),
      choices=[
        "A dispute over succession among the ruling families of the state itself.",
        "An invasion mounted by a neighboring state.",
        "The arrival of traders from a distant region.",
        "A change in the practices of a neighboring people.",
        "A demand for tribute made by a stronger state nearby.",
      ], ans=0,
      why=("The Governance thematic focus states that a variety of internal and external factors "
           "contribute to state formation, expansion, and decline. A succession dispute arises "
           "within the state; the other four originate outside it. KC-3.2.I.D.i is the content "
           "these factors operate on.")),

 dict(q=("Why is a source's own description of a state as powerful weaker evidence than a record "
         "of what that state actually required of its subjects?"),
      choices=[
        "Because the description states a conclusion while the record reports observable acts from which a reader can judge the conclusion independently.",
        "Because descriptions written at the time are always false and records are always true.",
        "Because a record of requirements is easier to read than a description.",
        "Because the framework accepts only numerical evidence about states.",
        "Because a description of power concerns religion rather than government.",
      ], ans=0,
      why=("Suggested skill 3.B asks students to identify the evidence a source uses to support "
           "an argument, which presupposes that a stated conclusion is not itself the evidence "
           "for it. Learning Objective I supplies the content, how states developed and changed.")),

 dict(q=("A state in the Americas is described as having grown from governing one valley to "
         "governing several. Which further observation would best show that its scope, and not "
         "only its reach, had grown?"),
      choices=[
        "That it now maintained storehouses, directed labor and settled disputes, functions it had not previously performed anywhere.",
        "That the valleys it governed were further apart than before.",
        "That its rulers travelled more widely than before.",
        "That the distance from its center to its furthest boundary had increased.",
        "That it had more subjects than before.",
      ], ans=0,
      why=("KC-3.2.I.D.i names expansion in scope AND reach as two things, and the Governance "
           "thematic focus describes what governments do through institutions and procedures. "
           "New functions are scope; greater distance and more subjects are reach.")),

 dict(q=("Which of the following best explains why the framework's dates for this period should "
         "not be treated as the beginning and end of state building in the Americas?"),
      choices=[
        "Because the framework states that developments are not constrained by the given dates and may begin before or continue after the period.",
        "Because the framework treats state building in the Americas as having no history before 1200.",
        "Because the framework holds that all state systems in the Americas ended in 1450.",
        "Because the framework regards its dates as fixed by the states themselves.",
        "Because the framework forbids the study of any period before 1200.",
      ], ans=0,
      why=("The CED states that events, processes, and developments are not constrained by the "
           "given dates and may begin before, or continue after, the period, and KC-3.2.I.D.i's "
           "word CONTINUITY presupposes arrangements inherited from before it.")),

 dict(q=("An unattributed account reports that a state of the Americas kept its records by a "
         "method unlike writing as the author knew it, and that officials were nonetheless able "
         "to state the obligations of each district exactly. What does the account best support?"),
      choices=[
        "That an administration can keep accurate records by means an outside observer does not recognize, so the absence of a familiar method is not the absence of administration.",
        "That the state in question kept no records of any kind.",
        "That record keeping is possible only where writing in the observer's sense exists.",
        "That the officials described were unable to state obligations accurately.",
        "That the account's author invented the officials he describes.",
      ], ans=0,
      why=("The Governance thematic focus states that governments maintain order through a "
           "variety of administrative institutions, policies, and procedures, and KC-3.2.I.D.i "
           "asserts innovation and diversity among the state systems of the Americas. Variety in "
           "method is what those words allow for.")),

 dict(q=("A historian wishes to compare a state of the Americas with a state of Afro-Eurasia. "
         "On the framework's terms, what makes such a comparison legitimate?"),
      choices=[
        "That the framework describes both as showing continuity, innovation and diversity, so the same analytic terms apply to each.",
        "That the two regions were in regular contact throughout the period.",
        "That the two regions produced states of the same size and duration.",
        "That the framework treats the Americas as a special case requiring separate terms.",
        "That the states of both regions kept records by identical methods.",
      ], ans=0,
      why=("KC-3.2.I.D.i says in the Americas, AS IN AFRO-EURASIA, state systems demonstrated "
           "continuity, innovation, and diversity, and KC-3.2.I.A applies those terms to "
           "Afro-Eurasia. The comparison is licensed by the shared vocabulary, not by contact.")),

 dict(q=("An argument holds that a decline in one center does not amount to the collapse of a "
         "region's political life. Which observation would most support that argument?"),
      choices=[
        "That while one center was abandoned, others in the same region continued to govern their districts and to grow.",
        "That the abandoned center had been the largest in the region.",
        "That the abandonment took place over several generations rather than at once.",
        "That the reasons for the abandonment are not recorded.",
        "That the center had been founded long before it was abandoned.",
      ], ans=0,
      why=("The Governance thematic focus names formation, expansion AND decline as parts of the "
           "same subject, and KC-3.2.I.D.i asserts diversity among the state systems of the "
           "Americas. Other centers continuing is what distinguishes one decline from a general "
           "collapse.")),

 dict(q=("What is the difference between saying that a state grew and saying that a state's "
         "institutions grew more capable?"),
      choices=[
        "The first is a claim about extent and the second about what the state could do, and evidence for one is not automatically evidence for the other.",
        "The two statements are equivalent, since a larger state is necessarily more capable.",
        "The first concerns religion and the second concerns warfare.",
        "The second is a claim about extent and the first about capability.",
        "Neither statement can be supported by any historical evidence.",
      ], ans=0,
      why=("KC-3.2.I.D.i pairs expansion in scope with expansion in reach as separate terms, and "
           "the Governance thematic focus separates the ways power is exercised from the extent "
           "over which it is exercised. The anchor names both halves in order because one "
           "distractor is the same pair exchanged.")),

 dict(q=("An unattributed source lists, for each district of a state, the number of workers owed "
         "for public labor and the season in which they were owed. A student cites the list to "
         "argue that obligations were regularized rather than demanded at will. Which feature of "
         "the list is the evidence?"),
      choices=[
        "That the amount and the timing are both stated in advance for every district, which is what distinguishes a standing obligation from an occasional demand.",
        "That the list survives at all, which shows the state valued records.",
        "That the districts are named individually rather than in groups.",
        "That the labor concerned was for public rather than private work.",
        "That the number of workers differs from district to district.",
      ], ans=0,
      why=("Suggested skill 3.B asks which detail supports the argument. A schedule fixed in "
           "advance is the mark of a procedure, which is what the Governance thematic focus "
           "names as a means by which governments maintain order; KC-3.2.I.D.i is the content.")),

 dict(q=("Taken together, what generalization about the Americas between c. 1200 and c. 1450 do "
         "the developments of this topic best support?"),
      choices=[
        "State systems there took more than one form, carried inherited arrangements forward while adding new ones, and extended what they did and how far they did it.",
        "State systems there were uniform in form and static in extent throughout the period.",
        "State systems there existed only in a single region of the hemisphere.",
        "State systems there declined continuously across the whole period.",
        "State systems there can be described only in terms that do not apply anywhere else.",
      ], ans=0,
      why=("KC-3.2.I.D.i is a single sentence containing every element of the key: continuity, "
           "innovation, diversity, and expansion in scope and reach, in the Americas as in "
           "Afro-Eurasia. Learning Objective I asks precisely how and why these states developed "
           "and changed.")),
]
