# AP WORLD HISTORY: MODERN 1.3 Developments in South and Southeast Asia from
# c. 1200 to c. 1450  (title copied verbatim from WORLD_HISTORY_topics.json).
# Unit 1 The Global Tapestry. Suggested skill 3.A, identify and describe a claim
# and/or argument in a text-based or non-text-based source.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON:
#
#   LO 1.G  Explain how the various belief systems and practices of South and
#           Southeast Asia affected society over time.
#   KC-3.1.III.D.iv  Hinduism, Islam, and Buddhism, and their core beliefs and
#           practices, continued to shape societies in South and Southeast Asia.
#   LO 1.H  Explain how and why various states of South and Southeast Asia
#           developed and maintained power over time.
#   KC-3.2.I.B.i  State formation and development demonstrated continuity,
#           innovation, and diversity, including the new Hindu and Buddhist states
#           that emerged in South and Southeast Asia.
#
#   Thematic focus CDI: the development of ideas, beliefs, and religions illustrates
#           how groups in society view themselves, and the interactions of societies
#           and their beliefs often have political, social, and cultural implications.
#   Thematic focus GOV: a variety of internal and external factors contribute to state
#           formation, expansion, and decline; governments obtain, retain, and exercise
#           power in different ways and for different purposes.
#
#   Illustrative examples on this topic page: beliefs and practices -- the Bhakti
#   movement, Sufism, Buddhist monasticism; Hindu and Buddhist states -- the
#   Vijayanagara Empire, the Srivijaya Empire, the Rajput kingdoms, the Khmer Empire,
#   Majapahit, the Sukhothai kingdom, the Sinhala dynasties.
#
# BECAUSE THE SUGGESTED SKILL IS 3.A, roughly a third of these items give an
# unattributed source and ask what CLAIM it makes or what would support it. The key
# to such an item is recoverable from the source printed in the stem, which is why
# the sources are written rather than quoted: inventing a quotation and signing a
# real author's name to it would be fabrication, and a student would read it as a
# genuine document. Nothing here is attributed to any real person or text.
#
# Spans are written "c. 1200 to c. 1450". No key turns on a boundary year, since the
# CED states its dates are approximate.
TOPIC = ("1.3", "Developments in South and Southeast Asia from c. 1200 to c. 1450", 1)

_T_GRANTS = dict(
    headers=["Site (hypothetical)", "Land grants recorded in an earlier reign",
             "Land grants recorded in a later reign"],
    rows=[["Site One", "12", "30"],
          ["Site Two", "20", "24"],
          ["Site Three", "8", "8"]])

_T_PORTS = dict(
    headers=["Port (hypothetical)", "Ships recorded in one season",
             "Languages recorded among resident traders"],
    rows=[["Port A", "140", "6"],
          ["Port B", "90", "4"],
          ["Port C", "40", "5"]])

_T_HOUSES = dict(
    headers=["District (hypothetical)", "Monastic communities in an earlier survey",
             "Monastic communities in a later survey"],
    rows=[["District One", "30", "45"],
          ["District Two", "25", "20"],
          ["District Three", "15", "15"]])

QUESTIONS = [
 dict(q=("A devotional poem of the period, its author unrecorded, addresses a deity directly "
         "and declares that neither noble birth nor mastery of the sacred languages brings a "
         "worshipper near, but only love freely given. Which claim is the poem making?"),
      choices=[
        "That personal devotion, rather than rank at birth or scholarly training, is what brings a worshipper close to the divine.",
        "That worship should be conducted only by those who have mastered the sacred languages.",
        "That the divine is unreachable by any human means whatever.",
        "That noble birth confers a religious standing that devotion cannot equal.",
        "That religious practice is a matter for the state to regulate rather than for the individual.",
      ], ans=0,
      why=("Suggested skill 3.A asks students to identify the claim a source makes, and the "
           "poem states its claim in its own words. KC-3.1.III.D.iv is the framework context: "
           "Hinduism and its core beliefs and practices continued to shape societies in South "
           "and Southeast Asia, and the Bhakti movement is the topic's illustrative example.")),

 dict(q=("Which of the following best states what the framework says about religion in South "
         "and Southeast Asia during this period?"),
      choices=[
        "Hinduism, Islam and Buddhism, together with the core beliefs and practices of each, continued to shape societies across these regions.",
        "A single tradition prevailed throughout both regions, the others having no presence there.",
        "Religious belief in these regions was confined to ruling households.",
        "The traditions of these regions were introduced for the first time during this period.",
        "Religious practice in these regions had ceased to affect society by the thirteenth century.",
      ], ans=0,
      why=("KC-3.1.III.D.iv names Hinduism, Islam, and Buddhism together and says their core "
           "beliefs and practices continued to shape societies in South and Southeast Asia. "
           "Naming three traditions is what the single-tradition option denies, and the word "
           "continued is what the first-introduction option denies.")),

 dict(q=("A historian describes the states that arose in South and Southeast Asia in this "
         "period as neither wholly traditional nor wholly novel. Which framework statement does "
         "that description follow?"),
      choices=[
        "That state formation and development demonstrated continuity, innovation and diversity, including new Hindu and Buddhist states that emerged in these regions.",
        "That every state in these regions preserved without alteration the arrangements of its predecessors.",
        "That the states of these regions were founded on principles unknown anywhere before.",
        "That state formation in these regions followed one uniform pattern from beginning to end.",
        "That no new state emerged in these regions during the period.",
      ], ans=0,
      why=("KC-3.2.I.B.i states that state formation and development demonstrated continuity, "
           "innovation, and diversity, including the new Hindu and Buddhist states that emerged "
           "in South and Southeast Asia. All three terms are asserted at once.")),

 dict(q=("An unattributed inscription set up by a ruler of the period records that he endowed a "
         "temple with land, remitted the taxes of the village that served it, and adds that he "
         "did so because a ruler who honors the gods is upheld by them. Which part of the "
         "inscription is a claim rather than a report of an action?"),
      choices=[
        "The statement that a ruler who honors the gods is upheld by them.",
        "The statement that land was endowed to the temple.",
        "The statement that the village's taxes were remitted.",
        "The statement that the inscription was set up by the ruler.",
        "The statement that a village served the temple.",
      ], ans=0,
      why=("Suggested skill 3.A asks students to identify a claim in a source and to distinguish "
           "it from what the source merely reports. Learning Objective H concerns how states "
           "developed and maintained power, and a justification of rule is the argumentative "
           "part of such a text.")),

 dict(q=("Monastic communities in this period supported schools, held land granted to them, and "
         "gave shelter to travelers. A historian who cites these activities to argue that belief "
         "systems affected society would be relying on which reasoning?"),
      choices=[
        "That the institutions a religion sustains carry out social functions, so its influence is visible in ordinary life and not only in doctrine.",
        "That the doctrines of a religion determine its social effects without any institution being needed.",
        "That religious institutions of this period had no dealings with people outside them.",
        "That schools and shelters in this period were maintained exclusively by rulers.",
        "That a religion affects society only when it becomes the official cult of a state.",
      ], ans=0,
      why=("Learning Objective G asks how the belief systems and practices of these regions "
           "affected society over time, and KC-3.1.III.D.iv names practices alongside core "
           "beliefs. Buddhist monasticism is the topic's own illustrative practice.")),

 dict(q=("A teacher of the period is described in an unattributed account as gathering "
         "followers, teaching by example and by song rather than by disputation, and living "
         "among ordinary people rather than at a court. What argument does the account best "
         "support?"),
      choices=[
        "That religious teaching in this period reached society through personal instruction outside formal institutions as well as through them.",
        "That religious teaching in this period took place only under royal supervision.",
        "That song and example were regarded in this period as unfit means of religious instruction.",
        "That teachers of religion in this period were drawn exclusively from courtly households.",
        "That religious instruction in this period had no audience beyond those who could read.",
      ], ans=0,
      why=("KC-3.1.III.D.iv says the core beliefs AND PRACTICES of Hinduism, Islam and Buddhism "
           "continued to shape these societies, and the topic's illustrative list names the "
           "Bhakti movement and Sufism, both of which are practices rather than institutions of "
           "state.")),

 dict(q=("Which of the following best explains why the framework describes the states of these "
         "regions as diverse?"),
      choices=[
        "Because states of more than one religious character emerged there, and their arrangements for holding power differed from one another.",
        "Because every state there shared one religion and one method of rule.",
        "Because no state there survived long enough to develop a distinctive character.",
        "Because the states there were governed from a single capital outside the region.",
        "Because the framework treats diversity as a property of religion alone and never of states.",
      ], ans=0,
      why=("KC-3.2.I.B.i says state formation and development demonstrated continuity, "
           "innovation, and diversity, INCLUDING the new Hindu and Buddhist states that emerged "
           "in South and Southeast Asia. Naming two religious characters inside a claim of "
           "diversity is the point of the sentence.")),

 dict(q=("Consider a claim that religious traditions in these regions were introduced from "
         "outside and remained foreign to the societies that received them. Which observation "
         "would tell most strongly against that claim?"),
      choices=[
        "That the core beliefs and practices of these traditions continued to shape the societies concerned rather than remaining confined to particular communities within them.",
        "That travelers from other regions visited these societies during the period.",
        "That texts of these traditions were written in languages other than the local ones.",
        "That rulers in these regions corresponded with rulers elsewhere.",
        "That merchants from other regions traded in the ports of these societies.",
      ], ans=0,
      why=("KC-3.1.III.D.iv states that Hinduism, Islam, and Buddhism and their core beliefs and "
           "practices continued to SHAPE SOCIETIES in South and Southeast Asia. Shaping a "
           "society is incompatible with remaining foreign to it.")),

 dict(q=("An unattributed chronicle of a maritime kingdom of the period reports that its ruler "
         "controlled a strait through which shipping passed, collected dues from vessels calling "
         "at his harbor, and used the revenue to endow temples and pay retainers. What does the "
         "chronicle suggest about how such a state maintained its power?"),
      choices=[
        "That control of a route and the revenue drawn from it could be converted into religious patronage and armed followers, both of which sustained the ruler's position.",
        "That the state's power rested on agriculture alone and had no connection to shipping.",
        "That religious patronage in this period was funded only by grants from other rulers.",
        "That collecting dues from shipping was incompatible with maintaining armed retainers.",
        "That maritime states of this period exercised no authority over the waters near them.",
      ], ans=0,
      why=("Learning Objective H asks how and why various states of South and Southeast Asia "
           "developed and MAINTAINED power over time, and the Governance thematic focus states "
           "that governments obtain, retain and exercise power in different ways and for "
           "different purposes.")),

 dict(q=("The same phrase, continuity, innovation and diversity, is used by the framework of "
         "states in East Asia, in the Islamic world and in South and Southeast Asia. What does "
         "using one phrase across those cases indicate?"),
      choices=[
        "That the framework treats the combination of inherited practice, new arrangements and regional difference as a general pattern of state formation in this period.",
        "That the states in question were governed in identical ways.",
        "That the framework regards regional differences between these states as unimportant.",
        "That each of these states was founded at the same time and by the same means.",
        "That the phrase applies to religion in these regions and not to their governments.",
      ], ans=0,
      why=("KC-3.2.I.B.i uses the phrase of South and Southeast Asian state formation, "
           "KC-3.2.I.A of states in Afro-Eurasia and the Americas, and KC-3.2.I of the new "
           "Islamic entities. A shared description of a general pattern is not a claim that the "
           "cases are alike in detail.")),

 dict(q=("The table below records HYPOTHETICAL counts of land grants made to three religious "
         "sites, under an earlier and a later reign. Which conclusion is best supported by that "
         "data?"),
      table=_T_GRANTS,
      choices=[
        "Two of the three sites recorded more grants under the later reign and the third recorded no change, so patronage did not move in one direction everywhere.",
        "Every site recorded more grants under the later reign than under the earlier one.",
        "At least one site recorded fewer grants under the later reign than under the earlier one.",
        "The site with the most grants under the earlier reign grew by the largest multiple.",
        "No site recorded any change between the two reigns.",
      ], ans=0,
      why=("Recomputed in the verifier from the table alone, distractors included. Learning "
           "Objective G concerns how belief systems affected society, and patronage that rises "
           "in some places and not others is the uneven pattern the framework's word diversity "
           "in KC-3.2.I.B.i describes.")),

 dict(q=("HYPOTHETICAL data for three ports in one season is set out in the table below, giving "
         "the number of ships recorded and the number of languages recorded among resident "
         "traders. Which statement do these numbers support?"),
      table=_T_PORTS,
      choices=[
        "The port with the most ships also recorded the most languages, but ranking the other two ports by ships and by languages gives different orders.",
        "Ranking the three ports by ships gives the same order as ranking them by languages.",
        "The port with the fewest ships also recorded the fewest languages.",
        "Every port listed recorded more than five languages among resident traders.",
        "The number of languages recorded was the same at every port listed.",
      ], ans=0,
      why=("Recomputed in the verifier: the two orderings agree at the top and disagree below "
           "it. KC-3.1.III.D.iv concerns societies shaped by more than one tradition, and a port "
           "where traders of several languages reside is the setting in which such contact "
           "occurs.")),

 dict(q=("For three districts, the table below gives HYPOTHETICAL counts of monastic "
         "communities recorded in an earlier and a later survey. What do these numbers show?"),
      table=_T_HOUSES,
      choices=[
        "The count rose in one district, fell in another and was unchanged in the third, so no single direction of change describes all three.",
        "The count rose in every district between the two surveys.",
        "The count fell in every district between the two surveys.",
        "The count was unchanged in every district between the two surveys.",
        "The district with the largest earlier count showed the largest decline.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.2.I.B.i's word diversity and "
           "Learning Objective G's phrase OVER TIME both point at variation between places and "
           "across time rather than at one uniform trend.")),

 dict(q=("An unattributed traveler's notebook says of a city that its people are industrious, "
         "that three temples stand on its main street, and that its ruler is the wisest in the "
         "region. Which of these is a statement of fact that could be checked, as opposed to a "
         "judgment?"),
      choices=[
        "That three temples stand on the city's main street.",
        "That the ruler is the wisest in the region.",
        "That the people of the city are industrious.",
        "That the city is worth visiting.",
        "That the city's arrangements are better than those of its neighbors.",
      ], ans=0,
      why=("Suggested skill 3.A asks students to identify a claim in a source, which requires "
           "separating what a source reports from what it argues. The count of buildings is "
           "observable; the remaining statements apply a standard of value. KC-3.1.III.D.iv is "
           "the content context for temples in such a city.")),

 dict(q=("A ruler of the period patronizes both a temple and a community of scholars of a "
         "different tradition. On the framework's terms, what does such patronage best "
         "illustrate?"),
      choices=[
        "That more than one belief system was present in the same society and that rulers dealt with the several traditions among their subjects.",
        "That belief systems in this period never coexisted within one state's territory.",
        "That rulers in this period were required to patronize every tradition equally.",
        "That patronage in this period was a private matter with no political significance.",
        "That a ruler's own observance determined the observance of all his subjects.",
      ], ans=0,
      why=("KC-3.1.III.D.iv names three traditions shaping the societies of these regions in the "
           "same period, and the Cultural Developments thematic focus states that the "
           "interactions of societies and their beliefs often have political implications.")),

 dict(q=("Why would it be an error to say that Buddhism or Hinduism arrived in South and "
         "Southeast Asia during the period from c. 1200 to c. 1450?"),
      choices=[
        "Because the framework says these traditions and their core beliefs CONTINUED to shape societies there, which presupposes that they were already present.",
        "Because the framework says these traditions were absent from these regions throughout the period.",
        "Because the framework treats all religious change as impossible during this period.",
        "Because the framework locates these traditions only in East Asia during this period.",
        "Because the framework denies that any tradition can spread from one region to another.",
      ], ans=0,
      why=("KC-3.1.III.D.iv uses the word continued of Hinduism, Islam, and Buddhism in South "
           "and Southeast Asia, and the CED separately states that developments are not "
           "constrained by the given dates and may begin before the period.")),

 dict(q=("Which of the following would be the strongest evidence that a state of this period "
         "had developed institutions of its own rather than simply inheriting them?"),
      choices=[
        "Records showing offices and procedures in use there that its predecessors had not employed, alongside others carried over unchanged.",
        "Records showing that its rulers claimed descent from earlier rulers of the same region.",
        "Records showing that it used the same religious titles as the state before it.",
        "Records showing that its territory was the same as that of an earlier state.",
        "Records showing that its capital stood on an older site.",
      ], ans=0,
      why=("KC-3.2.I.B.i joins innovation to continuity in one sentence about state formation in "
           "these regions, so evidence of innovation is evidence of something the predecessors "
           "did not have. Each rejected option is evidence of continuity only.")),

 dict(q=("An unattributed account of a court ceremony says that the ruler was seated above the "
         "assembly, that the officials of each district presented their tribute in turn, and "
         "that the ceremony was held annually. A historian arguing that the ceremony helped hold "
         "the state together would be relying on which reading of the account?"),
      choices=[
        "That a regular public occasion at which subordinate officials rendered tribute displayed and renewed their subordination to the ruler.",
        "That the ceremony was purely decorative and had no bearing on how the state was governed.",
        "That the officials attended in order to elect the ruler for a further term.",
        "That tribute was collected at the ceremony because no other means of taxation existed.",
        "That the ruler's seat above the assembly was a matter of comfort rather than of rank.",
      ], ans=0,
      why=("Learning Objective H asks how states of these regions developed and maintained power "
           "over time, and the Governance thematic focus states that governments maintain order "
           "through a variety of administrative institutions, policies, and procedures.")),

 dict(q=("Suppose a source from these regions records a community following a devotional "
         "practice that its neighbors do not share, while both communities acknowledge the same "
         "broad tradition. What does that best illustrate?"),
      choices=[
        "That a tradition can shape a society through a variety of practices rather than through one uniform observance.",
        "That the two communities cannot in fact have belonged to the same tradition.",
        "That devotional practice in this period was fixed by the state and admitted no variety.",
        "That variety in practice indicates that the tradition had ceased to shape the society.",
        "That the neighbors had adopted a tradition from a different region entirely.",
      ], ans=0,
      why=("KC-3.1.III.D.iv names the core beliefs AND PRACTICES of these traditions as what "
           "continued to shape these societies, and the topic's illustrative list prints three "
           "different practices under one heading: the Bhakti movement, Sufism and Buddhist "
           "monasticism.")),

 dict(q=("A student must identify the argument of an unattributed treatise which says that a "
         "kingdom prospers when its ruler protects cultivators, that a ruler who taxes beyond "
         "endurance loses them to his rivals, and that neighboring kingdoms have fallen for that "
         "reason. What is the treatise's argument?"),
      choices=[
        "That a ruler's own interest requires moderate exactions, since cultivators who are driven away take the kingdom's strength with them.",
        "That cultivators should be taxed as heavily as they can bear in order to strengthen the kingdom.",
        "That neighboring kingdoms fell for reasons no one can determine.",
        "That the prosperity of a kingdom is unrelated to the treatment of its cultivators.",
        "That a ruler should abolish taxation on cultivators entirely.",
      ], ans=0,
      why=("Suggested skill 3.A asks students to identify the argument a source makes, and this "
           "one states a claim and gives a reason and an example for it. Learning Objective H "
           "supplies the content context, how states developed and maintained power.")),

 dict(q=("Which of the following questions about South and Southeast Asia in this period could "
         "be settled by evidence rather than by a judgment of value?"),
      choices=[
        "Whether rulers of the period made grants of land to religious institutions.",
        "Whether rulers of the period should have made such grants instead of other expenditures.",
        "Whether one of the region's traditions offers a better guide to life than another.",
        "Whether the tribute owed by a district was fair to those who paid it.",
        "Whether a ruler deserved the obedience his officials rendered him.",
      ], ans=0,
      why=("KC-3.2.I.B.i and KC-3.1.III.D.iv assert matters of fact about state formation and "
           "about religious traditions shaping societies, which evidence can settle. The other "
           "four ask what should have been done, what is better, what is fair and what is "
           "deserved.")),

 dict(q=("How does the framework's account of state formation in these regions bear on the idea "
         "that a period of political change must be a period of cultural loss?"),
      choices=[
        "It tells against that idea, since new states emerged in these regions while the region's religious traditions continued to shape its societies.",
        "It supports that idea, since the framework describes the traditions of these regions as disappearing as new states arose.",
        "It is silent on the question, since the framework describes no state formation in these regions.",
        "It supports that idea, since the framework treats innovation and continuity as mutually exclusive.",
        "It tells against that idea, since the framework denies that any new states emerged in the period.",
      ], ans=0,
      why=("KC-3.2.I.B.i records new Hindu and Buddhist states emerging in these regions and "
           "KC-3.1.III.D.iv records the traditions continuing to shape their societies, in the "
           "same period. Both statements hold at once.")),

 dict(q=("A source describes a market town in which a mosque, a temple and a monastery each "
         "stand within a short distance of one another. As evidence, this description bears most "
         "directly on which framework statement?"),
      choices=[
        "That Hinduism, Islam and Buddhism all continued to shape the societies of South and Southeast Asia in this period.",
        "That only one of these traditions was permitted within any one settlement.",
        "That religious buildings in this period were confined to capital cities.",
        "That trade in this period was conducted only by adherents of a single tradition.",
        "That the traditions of these regions had merged into a single observance.",
      ], ans=0,
      why=("KC-3.1.III.D.iv names Hinduism, Islam, and Buddhism together as continuing to shape "
           "societies in South and Southeast Asia. Three buildings of three traditions in one "
           "town is that sentence in miniature; nothing in it implies a merger.")),

 dict(q=("What distinguishes a claim from evidence in a historical source, as the suggested "
         "skill for this topic asks students to recognize?"),
      choices=[
        "A claim asserts something the source is trying to establish, while evidence is what the source offers in support of it.",
        "A claim is always false and evidence is always true.",
        "A claim appears at the end of a source and evidence at the beginning.",
        "A claim is written by an author and evidence is not.",
        "A claim concerns religion and evidence concerns government.",
      ], ans=0,
      why=("Suggested skill 3.A for this topic is to identify and describe a claim and or "
           "argument in a source, and the following skill in the same sequence is to identify "
           "the evidence used in a source to support an argument. Learning Objective H is the "
           "content these skills are practiced on here.")),

 dict(q=("An argument holds that the states of these regions in this period should be studied "
         "together with their religious institutions rather than separately from them. Which "
         "evidence would most strengthen it?"),
      choices=[
        "Evidence that rulers endowed religious foundations and that those foundations in turn supported the ruler's standing among his subjects.",
        "Evidence that religious foundations kept records in a language rulers did not use.",
        "Evidence that religious foundations were built of the same materials as palaces.",
        "Evidence that rulers and religious teachers lived in the same region.",
        "Evidence that some rulers of the period were literate.",
      ], ans=0,
      why=("Learning Objective H asks how states developed and maintained power, KC-3.2.I.B.i "
           "names the new Hindu and Buddhist states of these regions, and the Cultural "
           "Developments thematic focus states that beliefs often carry political implications.")),

 dict(q=("An unattributed monastic rule from the period sets out how a community is to admit "
         "members, how it is to hold property in common, and how disputes among its members are "
         "to be settled. What does the existence of such a rule indicate?"),
      choices=[
        "That a religious community of this period was an organized body with procedures of its own, and so could act as an institution within society.",
        "That religious communities of this period had no property and no members to admit.",
        "That such communities were administered directly by the officials of the state.",
        "That disputes within such communities were referred to the ruler for settlement.",
        "That the rule was addressed to the general population rather than to the community.",
      ], ans=0,
      why=("Learning Objective G asks how the belief systems AND PRACTICES of these regions "
           "affected society over time; KC-3.1.III.D.iv names practices beside core beliefs, and "
           "Buddhist monasticism is the topic's own illustrative practice.")),

 dict(q=("Which of the following best explains why the framework speaks of states that emerged "
         "in these regions rather than of states that were imposed on them?"),
      choices=[
        "Because it treats state formation there as a development arising within the region, in which inherited practice and new arrangements combined.",
        "Because it holds that no external influence of any kind reached these regions.",
        "Because it treats every state of the period as the creation of a single founder.",
        "Because it regards these states as identical to those of neighboring regions.",
        "Because it denies that these states exercised authority over any territory.",
      ], ans=0,
      why=("KC-3.2.I.B.i says state formation and development demonstrated continuity, "
           "innovation, and diversity, INCLUDING the new Hindu and Buddhist states that emerged "
           "in South and Southeast Asia. Emergence with continuity is the framework's own "
           "wording.")),

 dict(q=("A ruler is recorded as taking a title used by earlier rulers, while also creating a "
         "new body of officials to collect revenue. How should this combination be described?"),
      choices=[
        "As continuity in the claim to legitimacy joined to innovation in the machinery of administration.",
        "As innovation in the claim to legitimacy joined to continuity in the machinery of administration.",
        "As continuity in both the claim to legitimacy and the machinery of administration.",
        "As innovation in both the claim to legitimacy and the machinery of administration.",
        "As evidence that neither legitimacy nor administration mattered to rule in this period.",
      ], ans=0,
      why=("KC-3.2.I.B.i asserts continuity AND innovation together in state formation in these "
           "regions. The anchor for this item names both halves in order, because the "
           "alternatives are the same two terms exchanged, which is the distractor shape this "
           "subject makes easiest to miss.")),

 dict(q=("A student proposes that the influence of a belief system can be measured only by the "
         "number of its adherents. Which consideration most complicates that proposal?"),
      choices=[
        "That a tradition also shapes a society through the institutions it sustains and the practices it prescribes, which affect people beyond its own adherents.",
        "That the number of adherents of a tradition can never be estimated at all.",
        "That belief systems in this period had no institutions attached to them.",
        "That the framework treats the size of a tradition as its only significant feature.",
        "That adherents of a tradition in this period were forbidden to record their numbers.",
      ], ans=0,
      why=("KC-3.1.III.D.iv says the core beliefs and PRACTICES of these traditions continued to "
           "shape societies, and Learning Objective G asks how belief systems and their "
           "practices affected society. Shaping a society is broader than counting its "
           "believers.")),

 dict(q=("Taken together, the developments of this topic best support which generalization about "
         "South and Southeast Asia between c. 1200 and c. 1450?"),
      choices=[
        "New states took shape there while long established religious traditions went on shaping the societies those states governed.",
        "New states took shape there only after the region's religious traditions had disappeared.",
        "The region's religious traditions survived only where no state existed.",
        "Neither new states nor continuing religious traditions can be identified there in this period.",
        "The region's states and its religious traditions developed in complete isolation from one another.",
      ], ans=0,
      why=("KC-3.2.I.B.i records new Hindu and Buddhist states emerging in these regions and "
           "KC-3.1.III.D.iv records Hinduism, Islam and Buddhism continuing to shape their "
           "societies. The two statements describe the same period and the same regions.")),
]
