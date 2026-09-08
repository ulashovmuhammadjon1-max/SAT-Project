# AP U.S. HISTORY 1.5 Labor, Slavery, and Caste in the Spanish Colonial System
# (title copied from US_HISTORY_topics.json -- this is one of the fifteen titles the
#  extraction repaired, and it matches the topic page's own heading)
# Unit 1, Period 1: 1491 to 1607. Suggested skill 5.A, identify patterns among or
# connections between historical developments and processes. Reasoning process printed
# for this topic: Causation.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 1 Learning Objective E
#       Explain how the growth of the Spanish Empire in North America shaped the
#       development of social and economic structures over time.
#
#   KC-1.2.II.B  In the encomienda system, Spanish colonial economies marshaled Native
#                American labor to support plantation-based agriculture and extract
#                precious metals and other resources.
#   KC-1.2.II.C  European traders partnered with some West African groups who practiced
#                slavery to forcibly extract enslaved laborers for the Americas. The
#                Spanish imported enslaved Africans to labor in plantation agriculture
#                and mining.
#   KC-1.2.II.D  The Spanish developed a caste system that incorporated, and carefully
#                defined the status of, the diverse population of Europeans, Africans,
#                and Native Americans in their empire.
#
#   Read with its parent, which this topic page sits under:
#   KC-1.2.II    The Columbian Exchange and development of the Spanish Empire in the
#                Western Hemisphere resulted in extensive demographic, economic, and
#                social changes.
#
#   THEMATIC FOCUS printed on this topic page, Social Structures SOC:
#       Social categories, roles, and practices are created, maintained, challenged, and
#       transformed throughout American history, shaping government policy, economic
#       systems, culture, and the lives of citizens.
#
# THE TWO LABOR SENTENCES ARE THE SWAP RISK, and most of this module is built to hold
# them apart. KC-1.2.II.B is about NATIVE AMERICAN labor under the encomienda system;
# KC-1.2.II.C is about ENSLAVED AFRICANS imported by the Spanish. Their purposes
# overlap -- plantation agriculture appears in both, and metals or mining in both -- so
# a distractor that keeps the purpose and exchanges the people reads perfectly well and
# is wrong. Every anchor on those items carries the labor source AND the arrangement.
#
# KC-1.2.II.C ALSO HAS TWO SENTENCES, and the framework's qualifiers in the first one
# are load-bearing: it says European traders PARTNERED with SOME West African groups
# WHO PRACTICED SLAVERY, to FORCIBLY EXTRACT enslaved laborers for the Americas. Items
# here key those words, and nothing here asserts anything the sentence does not.
#
# WHAT IS NOT KEYED. Divergent worldviews, mutual misunderstandings and native
# resistance are KC-1.2.III and its sub-points, printed on topic 1.6. They appear here
# only as distractors. Nothing here rests on the topic page's optional sources, which
# the CED itself says no exam question requires.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=.
# PROSE ONLY: no LaTeX; a span of years is written "1491 to 1607", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("1.5", "Labor, Slavery, and Caste in the Spanish Colonial System", 1)

_T_LABOR = dict(
    headers=["Arrangement the framework describes (illustrative arrangement)",
             "Whose labor does the framework describe it drawing on?"],
    rows=[["The encomienda system supporting plantation-based agriculture",
           "Native American labor"],
          ["The encomienda system extracting precious metals and other resources",
           "Native American labor"],
          ["Importation by the Spanish to labor in plantation agriculture",
           "Enslaved African labor"],
          ["Importation by the Spanish to labor in mining",
           "Enslaved African labor"]])

_T_ACTIVITY = dict(
    headers=["Activity described (illustrative)",
             "Workers recorded under the encomienda system",
             "Enslaved African workers recorded"],
    rows=[["Plantation agriculture", "300", "180"],
          ["Mining of precious metals", "220", "140"],
          ["Other resource extraction", "150", "0"]])

QUESTIONS = [

 dict(q="Unit 1's Learning Objective E asks students to explain how the growth of the "
        "Spanish Empire in North America shaped what?",
      choices=[
        "The development of social and economic structures over time",
        "The development of religious doctrine in Europe over time",
        "The migration routes of native populations before contact",
        "The improvement of maritime technology across the Atlantic",
        "The pattern of English settlement along the Atlantic seaboard"],
      ans=0,
      why="Unit 1 Learning Objective E reads 'Explain how the growth of the Spanish Empire "
          "in North America shaped the development of social and economic structures over "
          "time.' Native migration belongs to Learning Objective B, maritime technology to "
          "KC-1.2.I.C under Learning Objective D, and English settlement to Period 2."),

 dict(q="According to KC-1.2.II.B, whose labor did Spanish colonial economies marshal in "
        "the encomienda system?",
      choices=[
        "Native American labor",
        "Enslaved African labor",
        "The labor of European indentured servants",
        "The labor of West African traders",
        "The labor of migrants from other European empires"],
      ans=0,
      why="KC-1.2.II.B states that in the encomienda system, Spanish colonial economies "
          "marshaled Native American labor to support plantation-based agriculture and "
          "extract precious metals and other resources. Enslaved Africans appear in "
          "KC-1.2.II.C, under a different arrangement, and the framework's account of "
          "this period names neither European indentured servants nor migrants from other "
          "empires in the Spanish colonies."),

 dict(q="KC-1.2.II.B names the purposes for which that labor was marshaled. Which set "
        "names them as the framework does?",
      choices=[
        "To support plantation-based agriculture and to extract precious metals and other "
        "resources",
        "To support plantation-based agriculture and to build fortifications",
        "To extract precious metals and to serve in colonial militias",
        "To support plantation-based agriculture and to carry goods across the Atlantic",
        "To extract precious metals and to staff colonial courts"],
      ans=0,
      why="KC-1.2.II.B gives two purposes together: to support plantation-based "
          "agriculture and extract precious metals and other resources. Fortifications, "
          "militias, Atlantic carriage and colonial courts appear nowhere in that "
          "sentence, and the framework does not add purposes to the ones it names."),

 dict(q="What does the first sentence of KC-1.2.II.C say European traders did, and with "
        "whom?",
      choices=[
        "They partnered with some West African groups who practiced slavery, to forcibly "
        "extract enslaved laborers for the Americas",
        "They partnered with every West African group, to forcibly extract enslaved "
        "laborers for the Americas",
        "They partnered with some West African groups who practiced slavery, to open "
        "markets for European manufactures",
        "They partnered with Spanish colonial officials, to recruit Native American labor "
        "for the mines",
        "They partnered with some West African groups, to settle European migrants along "
        "the coast"],
      ans=0,
      why="KC-1.2.II.C states that European traders partnered with some West African "
          "groups who practiced slavery to forcibly extract enslaved laborers for the "
          "Americas. The sentence says some rather than every, names the extraction of "
          "enslaved laborers rather than a market for manufactures or a settlement scheme, "
          "and its partners are West African groups rather than Spanish officials."),

 dict(q="What does the word SOME do in KC-1.2.II.C's phrase about West African groups?",
      choices=[
        "It limits the claim to particular groups rather than extending it to all of West "
        "Africa",
        "It extends the claim to every group in West Africa",
        "It makes the claim about European groups rather than West African ones",
        "It places the partnership after the period this unit covers",
        "It removes the reference to slavery from the sentence"],
      ans=0,
      why="KC-1.2.II.C writes that European traders partnered with SOME West African "
          "groups who practiced slavery, so the sentence describes particular partners "
          "rather than the whole region, in the same way KC-1.1.I.C's 'some societies' "
          "limits a claim to part of a named area. The qualifier changes neither the "
          "sentence's subject nor its period nor its reference to slavery."),

 dict(q="The second sentence of KC-1.2.II.C names two kinds of work. Which pair does the "
        "framework name for the enslaved Africans the Spanish imported?",
      choices=[
        "Plantation agriculture and mining",
        "Plantation agriculture and household service",
        "Mining and shipbuilding",
        "Plantation agriculture and the carrying trade",
        "Mining and the construction of missions"],
      ans=0,
      why="KC-1.2.II.C states that the Spanish imported enslaved Africans to labor in "
          "plantation agriculture and mining. Household service, shipbuilding, the "
          "carrying trade and mission construction are not named in that sentence, and "
          "the framework does not extend its own list."),

 dict(q="KC-1.2.II.D describes a caste system the Spanish developed. What does the "
        "sentence say that system did?",
      choices=[
        "It incorporated, and carefully defined the status of, the diverse population of "
        "the empire",
        "It excluded from the empire's population everyone who was not European",
        "It left the status of the empire's population undefined",
        "It replaced the encomienda system as a way of organizing labor",
        "It applied only to Europeans within the empire"],
      ans=0,
      why="KC-1.2.II.D states that the Spanish developed a caste system that incorporated, "
          "and carefully defined the status of, the diverse population of Europeans, "
          "Africans, and Native Americans in their empire. Incorporation is the opposite "
          "of exclusion and careful definition the opposite of leaving status open; the "
          "sentence describes a system of status rather than of labor, which is "
          "KC-1.2.II.B's subject."),

 dict(q="Which three groups does KC-1.2.II.D name as making up the diverse population the "
        "caste system defined?",
      choices=[
        "Europeans, Africans, and Native Americans",
        "Europeans, Africans, and Asians",
        "Spaniards, Portuguese, and Native Americans",
        "Europeans and Native Americans only",
        "Africans, Native Americans, and West African traders"],
      ans=0,
      why="KC-1.2.II.D names the diverse population of Europeans, Africans, and Native "
          "Americans in the Spanish empire. Substituting Asians, narrowing Europeans to "
          "two nationalities, dropping Africans, or adding traders from West Africa each "
          "changes the framework's own list, which is the same trio KC-1.2 names as the "
          "groups whose contact produced the Columbian Exchange."),

 dict(q="Which pairing of a labor arrangement with the people whose labor it drew on is "
        "the one the framework states?",
      choices=[
        "The encomienda system with Native American labor, and Spanish importation with "
        "enslaved African labor",
        "The encomienda system with enslaved African labor, and Spanish importation with "
        "Native American labor",
        "The encomienda system with European indentured labor, and Spanish importation "
        "with Native American labor",
        "The caste system with Native American labor, and the encomienda system with "
        "enslaved African labor",
        "Spanish importation with European migrant labor, and the encomienda system with "
        "enslaved African labor"],
      ans=0,
      why="KC-1.2.II.B places Native American labor in the encomienda system and "
          "KC-1.2.II.C has the Spanish import enslaved Africans to labor in plantation "
          "agriculture and mining. Exchanging the two peoples keeps both arrangements and "
          "still misreports both sentences, which is why the pairing has to be read as a "
          "whole; the caste system of KC-1.2.II.D is a system of status rather than a "
          "labor arrangement."),

 dict(q="KC-1.2.II.D uses two verbs together, INCORPORATED and CAREFULLY DEFINED THE "
        "STATUS OF. What do they claim when taken together?",
      choices=[
        "That the system brought the empire's whole population within it and assigned each "
        "part of that population a stated position",
        "That the system brought the population within it while leaving positions "
        "unstated",
        "That the system assigned stated positions to some people and expelled the rest",
        "That the system was a description of the population rather than an arrangement "
        "applied to it",
        "That the system applied to labor rather than to status"],
      ans=0,
      why="KC-1.2.II.D says the caste system incorporated, and carefully defined the "
          "status of, the diverse population of Europeans, Africans, and Native Americans "
          "in the Spanish empire, so it both took the whole population in and fixed each "
          "part's position. Dropping either verb leaves half the sentence, and the "
          "Social Structures thematic focus treats such categories as created and "
          "maintained rather than merely observed."),

 dict(q="The thematic focus printed on this topic page is Social Structures. What does it "
        "say about social categories, roles, and practices?",
      choices=[
        "That they are created, maintained, challenged, and transformed, shaping "
        "government policy, economic systems, culture, and the lives of citizens",
        "That they are fixed once established and are not afterwards challenged",
        "That they are shaped by economic systems but shape nothing in turn",
        "That they concern culture alone and not government policy",
        "That they arise only after a colonial period has ended"],
      ans=0,
      why="The Social Structures thematic focus states that social categories, roles, and "
          "practices are created, maintained, challenged, and transformed throughout "
          "American history, shaping government policy, economic systems, culture, and the "
          "lives of citizens. KC-1.2.II.D's caste system is such a category being created "
          "and defined, and Unit 1 Learning Objective E asks how the empire's growth "
          "shaped social and economic structures alike."),

 dict(q="The suggested skill printed on this topic page is 5.A. How does the framework "
        "state that skill?",
      choices=[
        "Identify patterns among or connections between historical developments and "
        "processes",
        "Explain how a historical development or process relates to another historical "
        "development or process",
        "Identify and describe a claim and/or argument in a text-based or non-text-based "
        "source",
        "Identify a historical concept, development, or process",
        "Support an argument using specific and relevant evidence"],
      ans=0,
      why="Skill 5.A as printed on this topic page reads 'Identify patterns among or "
          "connections between historical developments and processes', and it is what "
          "Unit 1 Learning Objective E asks of students who must connect the encomienda "
          "system, the importation of enslaved Africans and the caste system. The other "
          "four are skills 5.B, 3.A, 1.A and 6.B from other topic pages of this course."),

 dict(q="A hypothetical grant document, its author unnamed, assigns a settler the labor of "
        "the people of a named district and requires him to set them to the fields and the "
        "mine. Which framework statement does it illustrate?",
      choices=[
        "KC-1.2.II.B, on the encomienda system marshaling Native American labor for "
        "agriculture and extraction",
        "KC-1.2.II.C, on the Spanish importing enslaved Africans to labor in plantation "
        "agriculture and mining",
        "KC-1.2.II.D, on the caste system defining the status of the empire's population",
        "KC-1.2.I.C, on more organized methods for conducting international trade",
        "KC-1.2.III, on divergent worldviews asserted in interaction"],
      ans=0,
      why="KC-1.2.II.B describes the encomienda system as the arrangement in which Spanish "
          "colonial economies marshaled Native American labor to support plantation-based "
          "agriculture and extract precious metals and other resources, which is what a "
          "grant of a district's labor for fields and mine would be. KC-1.2.II.C's "
          "arrangement rests on importation from across the Atlantic rather than on a "
          "grant of local labor."),

 dict(q="Suppose an illustrative ledger, its author unnamed, records a European trading "
        "post buying captives from a neighbouring ruler and shipping them westward across "
        "the ocean. Which framework statement does it illustrate?",
      choices=[
        "KC-1.2.II.C, on European traders partnering with some West African groups to "
        "forcibly extract enslaved laborers for the Americas",
        "KC-1.2.II.B, on the encomienda system marshaling Native American labor",
        "KC-1.2.II.D, on the caste system defining the status of the empire's population",
        "KC-1.2.I.B, on new crops and mineral wealth reaching Europe",
        "KC-1.2.II, on extensive demographic, economic, and social changes"],
      ans=0,
      why="KC-1.2.II.C's first sentence describes European traders partnering with some "
          "West African groups who practiced slavery to forcibly extract enslaved laborers "
          "for the Americas, which is the transaction and the destination the ledger "
          "records. The encomienda system of KC-1.2.II.B draws on labor already in the "
          "Americas, and KC-1.2.II.D concerns status rather than transport."),

 dict(q="An illustrative colonial register, its author unnamed, sorts the inhabitants of a "
        "town into named categories by descent and attaches a different set of "
        "obligations to each. Which framework statement does it illustrate?",
      choices=[
        "KC-1.2.II.D, on the caste system that incorporated and carefully defined the "
        "status of the empire's diverse population",
        "KC-1.2.II.B, on Native American labor marshaled for agriculture and extraction",
        "KC-1.2.II.C, on enslaved Africans imported to labor in plantation agriculture and "
        "mining",
        "KC-1.2.I.C, on improvements in maritime technology",
        "KC-1.1.I.A, on the spread of maize cultivation"],
      ans=0,
      why="KC-1.2.II.D describes a caste system that incorporated, and carefully defined "
          "the status of, the diverse population of Europeans, Africans, and Native "
          "Americans, which is what a register sorting inhabitants by descent and fixing "
          "each category's obligations records. The two labor sentences describe who "
          "worked at what rather than how status was assigned."),

 dict(q="Using the table of arrangements, which pairing does the record give?",
      table=_T_LABOR,
      choices=[
        "The two encomienda rows draw on Native American labor, and the two importation "
        "rows on enslaved African labor",
        "The two encomienda rows draw on enslaved African labor, and the two importation "
        "rows on Native American labor",
        "All four rows draw on Native American labor",
        "All four rows draw on enslaved African labor",
        "Each of the four rows draws on a different source of labor"],
      ans=0,
      why="Read from the table alone: two rows name the encomienda system and both are "
          "marked as drawing on Native American labor, while two name importation by the "
          "Spanish and both are marked as drawing on enslaved African labor. That is what "
          "KC-1.2.II.B and KC-1.2.II.C say, and exchanging the two sources would keep "
          "every arrangement while misreporting both sentences."),

 dict(q="Using the table of illustrative activity figures, which conclusion do the columns "
        "support?",
      table=_T_ACTIVITY,
      choices=[
        "Both columns record workers in plantation agriculture and in mining, while only "
        "the encomienda column records workers in other resource extraction",
        "Enslaved African workers are recorded in every activity listed",
        "The encomienda column records no workers in one of the activities",
        "More enslaved African workers than encomienda workers are recorded in every "
        "activity",
        "Only one of the three activities records any workers at all"],
      ans=0,
      why="Read from the table alone: the encomienda column is above zero in all three "
          "rows and the enslaved African column in the first two only. That matches the "
          "framework's own lists, since KC-1.2.II.B names plantation-based agriculture and "
          "the extraction of precious metals AND OTHER RESOURCES while KC-1.2.II.C names "
          "plantation agriculture and mining, and the extra category belongs to the "
          "encomienda sentence alone."),

 dict(q="Using the same table of illustrative activity figures, which claim goes BEYOND "
        "what the columns can support?",
      table=_T_ACTIVITY,
      choices=[
        "That one of the two labor systems was more profitable to the Spanish than the "
        "other",
        "That the encomienda column records more workers than the enslaved African column "
        "in every activity",
        "That plantation agriculture records more workers in both columns than mining does",
        "That one activity records workers in one column only",
        "That every activity records at least one worker in the encomienda column"],
      ans=0,
      why="The table counts workers and reports nothing about returns, so relative profit "
          "is the one claim of the five it cannot reach. The other four are read straight "
          "off the rows. KC-1.2.II.B and KC-1.2.II.C describe what the labor was used for "
          "and where it came from, and neither sentence weighs one arrangement's yield "
          "against the other's."),

 dict(q="Learning Objective E asks how the Spanish Empire's growth shaped structures OVER "
        "TIME. What does that phrase ask a student to attend to?",
      choices=[
        "How the structures developed across the period rather than at a single moment",
        "How the structures appeared fully formed at the empire's founding",
        "How the structures were confined to a single year of the period",
        "How the structures ceased to change once the caste system was defined",
        "How the structures resembled those of other empires"],
      ans=0,
      why="Unit 1 Learning Objective E asks how the growth of the Spanish Empire in North "
          "America shaped the development of social and economic structures over time, so "
          "development across the period is what the objective is about. The Social "
          "Structures thematic focus makes the same point by calling categories created, "
          "maintained, challenged, and transformed rather than settled once."),

 dict(q="Learning Objective E names two kinds of structure. What follows from its naming "
        "both?",
      choices=[
        "An answer must reach the arrangement of society as well as the organization of "
        "production",
        "An answer may treat the economic arrangements alone",
        "An answer may treat the social arrangements alone",
        "An answer must confine itself to the caste system",
        "An answer must confine itself to the encomienda system"],
      ans=0,
      why="Unit 1 Learning Objective E asks about the development of social AND economic "
          "structures, and the topic's three sentences supply both: KC-1.2.II.B and "
          "KC-1.2.II.C describe how production was organized and by whose labor, while "
          "KC-1.2.II.D describes how status was assigned. Taking either half alone answers "
          "half the objective."),

 dict(q="Applying suggested skill 5.A, what connects KC-1.2.II.B with the second sentence "
        "of KC-1.2.II.C?",
      choices=[
        "Both describe labor directed to plantation agriculture and to the working of "
        "metals in the Spanish colonies",
        "Both describe labor drawn from the same population",
        "Both describe systems of status rather than of labor",
        "Both describe arrangements the framework places in Europe",
        "Both describe voluntary migration to the Spanish colonies"],
      ans=0,
      why="KC-1.2.II.B has Native American labor supporting plantation-based agriculture "
          "and extracting precious metals, and KC-1.2.II.C has enslaved Africans imported "
          "to labor in plantation agriculture and mining, so the two sentences share their "
          "purposes while differing in whose labor they describe. Skill 5.A asks for "
          "exactly such connections between developments, and neither sentence describes "
          "status, Europe or voluntary migration."),

 dict(q="What most clearly distinguishes KC-1.2.II.B's arrangement from the one described "
        "in the second sentence of KC-1.2.II.C?",
      choices=[
        "One marshals the labor of people already in the Americas, while the other rests "
        "on people the Spanish imported across the Atlantic",
        "One concerns agriculture and the other concerns mining, with no overlap between "
        "them",
        "One is described as occurring in Europe and the other in the Americas",
        "One is described as a system of status and the other as a system of labor",
        "One is placed before 1492 and the other after it"],
      ans=0,
      why="KC-1.2.II.B describes Spanish colonial economies marshaling Native American "
          "labor within the Americas, while KC-1.2.II.C describes the Spanish importing "
          "enslaved Africans. Their purposes overlap rather than divide, since plantation "
          "agriculture and the working of metals appear in both, and both are placed in "
          "the Americas during the period Unit 1 Learning Objective E covers."),

 dict(q="KC-1.2.II, the key concept under which this topic sits, attributes three kinds of "
        "change to the Columbian Exchange and the development of the Spanish Empire. Which "
        "three?",
      choices=[
        "Demographic, economic, and social",
        "Demographic, military, and religious",
        "Political, legal, and economic",
        "Social, cultural, and political",
        "Economic, technological, and military"],
      ans=0,
      why="KC-1.2.II states that the Columbian Exchange and development of the Spanish "
          "Empire in the Western Hemisphere resulted in extensive demographic, economic, "
          "and social changes, and this topic's three sentences are where the economic and "
          "social ones are set out. The triple beginning with social belongs to KC-1.2, "
          "which describes changes on both sides of the Atlantic Ocean, and mistaking one "
          "list for the other is the likeliest confusion here."),

 dict(q="Why is it a mistake to describe KC-1.2.II.D's caste system as a way of organizing "
        "labor?",
      choices=[
        "The sentence describes it as incorporating and defining the status of the "
        "population, while labor is the subject of the two sentences before it",
        "The sentence describes it as a system of trade rather than of status",
        "The sentence describes it as applying only outside the Spanish empire",
        "The sentence does not describe any system at all",
        "The sentence describes it as replacing the importation of enslaved Africans"],
      ans=0,
      why="KC-1.2.II.D says the Spanish developed a caste system that incorporated, and "
          "carefully defined the status of, the diverse population of Europeans, Africans, "
          "and Native Americans in their empire, which is a statement about position "
          "rather than about work; KC-1.2.II.B and KC-1.2.II.C are the sentences that "
          "describe labor. The system is placed inside the empire and is not said to "
          "replace anything."),

 dict(q="A hypothetical seminar handout states that KC-1.2.II.C describes slavery as "
        "unknown in West Africa before European traders arrived. What does the sentence "
        "actually say?",
      choices=[
        "That the traders partnered with some West African groups who practiced slavery",
        "That the traders introduced the practice of slavery to every West African group",
        "That the traders partnered with West African groups who did not practise slavery",
        "That the traders had no West African partners of any kind",
        "That the partnership took place in the Americas rather than in West Africa"],
      ans=0,
      why="KC-1.2.II.C states that European traders partnered with some West African groups "
          "who practiced slavery to forcibly extract enslaved laborers for the Americas, "
          "so the sentence describes existing practice among particular partners rather "
          "than an introduction, and it says some groups rather than all. Reading either "
          "an introduction or a universal claim into it adds something the framework does "
          "not say."),

 dict(q="KC-1.2.II.C says enslaved laborers were FORCIBLY extracted. What does that word "
        "make explicit?",
      choices=[
        "That the people taken did not go by their own choice",
        "That the extraction was carried out without any partner in West Africa",
        "That the laborers were taken to Europe rather than to the Americas",
        "That the partnership between traders and groups was involuntary on the traders' "
        "side",
        "That the practice ended within the period this unit covers"],
      ans=0,
      why="KC-1.2.II.C's adverb attaches to the extraction of enslaved laborers for the "
          "Americas and states that it was done by force, which settles that the people "
          "taken did not consent. The same sentence names West African partners and names "
          "the Americas as the destination, and it reports no ending; KC-1.2.II.C's second "
          "sentence continues with the Spanish importing enslaved Africans."),

 dict(q="How does the Social Structures thematic focus bear on KC-1.2.II.D's carefully "
        "defined statuses?",
      choices=[
        "It treats such categories as made and maintained by people rather than as simply "
        "given, and as shaping policy, economy, culture and lives",
        "It treats such categories as natural facts that history does not touch",
        "It treats such categories as effects of the economy that shape nothing themselves",
        "It restricts such categories to the period after the colonial era",
        "It treats such categories as matters of culture with no bearing on economic "
        "systems"],
      ans=0,
      why="The Social Structures thematic focus states that social categories, roles, and "
          "practices are created, maintained, challenged, and transformed throughout "
          "American history, shaping government policy, economic systems, culture, and the "
          "lives of citizens, and KC-1.2.II.D's verb DEVELOPED says the Spanish made the "
          "caste system rather than found it. Unit 1 Learning Objective E joins the social "
          "structures to the economic ones."),

 dict(q="Which of the following belongs to a different topic of this unit rather than to "
        "the Spanish colonial system described here?",
      choices=[
        "Mutual misunderstandings between Europeans and Native Americans as each sought to "
        "make sense of the other",
        "The marshalling of Native American labor under the encomienda system",
        "The importation of enslaved Africans to labor in plantation agriculture and mining",
        "The partnership of European traders with some West African groups",
        "The caste system that defined the status of the empire's diverse population"],
      ans=0,
      why="Mutual misunderstandings between Europeans and Native Americans are KC-1.2.III.A, "
          "printed on the topic about cultural interactions rather than here. The other "
          "four are KC-1.2.II.B, KC-1.2.II.C in both its sentences, and KC-1.2.II.D, which "
          "together are the whole of this topic's Required Course Content under Unit 1 "
          "Learning Objective E."),

 dict(q="KC-1.2.II.B names precious metals AND OTHER RESOURCES among what the encomienda "
        "system was used to extract. What does the second phrase add to the sentence?",
      choices=[
        "It carries the extraction past precious metals to resources the sentence does not "
        "list one by one",
        "It restricts the extraction to precious metals alone",
        "It names the crops the Columbian Exchange carried to Europe",
        "It transfers the extraction to the enslaved Africans the Spanish imported",
        "It limits the extraction to resources found outside the Spanish empire"],
      ans=0,
      why="KC-1.2.II.B says the encomienda system marshaled Native American labor to "
          "support plantation-based agriculture and extract precious metals and other "
          "resources, so the phrase widens what was extracted without enumerating it, and "
          "it is the one purpose in this topic that KC-1.2.II.C's plantation agriculture "
          "and mining do not match. Crops carried to Europe belong to KC-1.2.I.B, and the "
          "labor in this sentence is Native American rather than imported."),

 dict(q="Which statement collects this topic's Required Course Content without adding to "
        "it?",
      choices=[
        "Spanish colonial economies marshaled Native American labor under the encomienda "
        "system, the Spanish imported enslaved Africans obtained through partnerships with "
        "some West African groups who practiced slavery, and a caste system incorporated "
        "and defined the status of Europeans, Africans, and Native Americans in the empire",
        "Spanish colonial economies relied on European indentured servants, and a caste "
        "system defined the status of Europeans alone",
        "Spanish colonial economies marshaled Native American labor, and no other source "
        "of labor is described for the empire",
        "The Spanish imported enslaved Africans, and no labor was drawn from populations "
        "already in the Americas",
        "A caste system defined the status of the empire's population, and the framework "
        "describes no labor arrangements at all"],
      ans=0,
      why="The first collects KC-1.2.II.B, KC-1.2.II.C and KC-1.2.II.D in the framework's "
          "own terms and adds nothing to them. European indentured servants appear nowhere "
          "in this unit, the caste system is said to incorporate Europeans, Africans, and "
          "Native Americans rather than Europeans alone, and each remaining option drops "
          "one of the three sentences Unit 1 Learning Objective E rests on."),
]
