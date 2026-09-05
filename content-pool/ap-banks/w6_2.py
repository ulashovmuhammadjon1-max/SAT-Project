# AP WORLD HISTORY: MODERN 6.2 State Expansion from 1750 to 1900
# CED effective Fall 2026, Unit 6 Consequences of Industrialization, c. 1750 to
# c. 1900. Thematic focus GOV, Governance: "A variety of internal and external
# factors contribute to state formation, expansion, and decline. Governments
# maintain order through a variety of administrative institutions, policies, and
# procedures, and governments obtain, retain, and exercise power in different ways
# and for different purposes."
#
# Unit 6 Learning Objective B: "Compare processes by which state power shifted in
# various parts of the world from 1750 to 1900."
# Reasoning process: Comparison. Suggested skill 4.B, explain how a specific
# historical development or process is situated within a broader historical context.
#
# The historical developments this topic prints, in the framework's own words:
#   KC-5.2.I.A  Some states with existing colonies strengthened their control over
#               those colonies and in some cases assumed direct control over
#               colonies previously held by non-state entities.
#   KC-5.2.I.B  European states as well as the United States and Japan acquired
#               territories throughout Asia and the Pacific, while Spanish and
#               Portuguese influence declined.
#   KC-5.2.I.C  Many European states used both warfare and diplomacy to expand
#               their empires in Africa.
#   KC-5.2.I.D  Europeans established settler colonies in some parts of their
#               empires.
#   KC-5.2.II.B The United States, Russia, and Japan expanded their land holdings
#               by conquering and settling neighboring territories.
#
# Illustrative examples the CED prints for this topic, and the only proper names
# used in this module:
#   Non-state to state colonial control: the shift from the private ownership of
#     the Congo by King Leopold II to the Belgium government; the shift from the
#     Dutch East India Company to Dutch government control in Indonesia and
#     Southeast Asia.
#   European states that expanded empires in Africa: Britain in West Africa,
#     Belgium in the Congo, French in West Africa.
#   Settler colonies established in empires: New Zealand.
#
# WHAT THIS BANK DOES NOT DO. No item asks for a year, a treaty, a battle, a
# population figure or a person the CED does not print. Every source is
# UNATTRIBUTED and labelled illustrative, because inventing a quotation and
# hanging a real name on it would be read by a student as fact. Tables are
# labelled hypothetical in the stem and every keyed conclusion is recomputable
# from the table alone.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md. Dates are written "1750 to 1900".
TOPIC = ("6.2", "State Expansion from 1750 to 1900", 6)

_T_CONTROL = dict(
    headers=["Territory (hypothetical)",
             "Body exercising control at the start of the period",
             "Body exercising control at the end of the period"],
    rows=[["Territory Q", "A chartered trading company",
           "The government of the same European state"],
          ["Territory R", "A chartered trading company",
           "The same chartered trading company"],
          ["Territory S", "A chartered trading company",
           "The government of a different European state"],
          ["Territory T", "The government of a European state",
           "The government of the same European state"],
          ["Territory U", "An estate privately owned by a European monarch",
           "The government of that monarch's own state"]])

_T_SETTLERS = dict(
    headers=["African territory (hypothetical)",
             "Means by which control was first obtained",
             "Settlers from the imperial state resident at the end of the period (hypothetical)"],
    rows=[["Territory V", "A treaty negotiated with local rulers", "180,000"],
          ["Territory W", "A military campaign", "2,400"],
          ["Territory X", "A military campaign", "95,000"],
          ["Territory Y", "Transfer from a chartered trading company", "600"]])

QUESTIONS = [
 dict(q="An illustrative statute of the period, quoted here without attribution, provides that 'the territories heretofore administered by the Company shall pass to and be governed in the name of the Crown'. The change this statute makes is best described as",
   choices=[
     "a colony passing from a non-state entity to direct control by a state",
     "a colony passing from direct control by a state to a non-state entity",
     "a colony ceasing to be governed from outside altogether",
     "the founding of a colony in territory no empire had claimed",
     "the sale of one state's colony to a neighbouring state"], ans=0,
   why="KC-5.2.I.A states that some states assumed direct control over colonies previously held by non-state entities. A company is such an entity and a Crown is a state, so the statute is that process in a single document. The reversed reading is offered as a distractor and is not what the text says."),
 dict(q="The course framework gives, as an illustration of colonial control shifting from a non-state holder to a state, the case of the Congo. What change does that example describe?",
   choices=[
     "The Congo was privately owned by King Leopold II and control then passed to the Belgian government",
     "The Congo was governed by the Belgian government and control then passed to King Leopold II as private property",
     "The Congo was governed by a chartered trading company and control then passed to local rulers",
     "The Congo was a settler colony that became a self-governing state",
     "The Congo was transferred from one European government to another by treaty"], ans=0,
   why="The CED's illustrative example for topic 6.2 is the shift from the private ownership of the Congo by King Leopold II to the Belgium government, which is exactly the direction the key states. The reversal is offered as a distractor, and the two clauses have to be read together to reject it."),
 dict(q="A second illustration the framework gives of the same process concerns Indonesia and Southeast Asia. That example describes a shift from",
   choices=[
     "the Dutch East India Company to control by the Dutch government",
     "the Dutch government to control by the Dutch East India Company",
     "a Portuguese government to a Dutch chartered company",
     "a settler assembly to a company board of directors",
     "an independent kingdom to a company with no European government involved"], ans=0,
   why="The CED's illustrative example is the shift from the Dutch East India Company to Dutch government control in Indonesia and Southeast Asia, which is the direction the key states and the opposite of the first distractor. KC-5.2.I.A is the general statement these examples illustrate."),
 dict(q="Which statement best describes the acquisition of territory in Asia and the Pacific during this period as the framework presents it?",
   choices=[
     "European states, the United States and Japan acquired territories there while Spanish and Portuguese influence declined",
     "Spanish and Portuguese influence expanded there while other European states, the United States and Japan withdrew",
     "No state outside Europe acquired territory anywhere in the region",
     "Acquisition in the region stopped entirely once industrial production began",
     "Every territory in the region was acquired by purchase rather than by any other means"], ans=0,
   why="KC-5.2.I.B states that European states as well as the United States and Japan acquired territories throughout Asia and the Pacific while Spanish and Portuguese influence declined. Both clauses of the key are needed, because the exact reversal is offered as a distractor."),
 dict(q="Which two states outside Europe does the framework name as acquiring territories throughout Asia and the Pacific in this period?",
   choices=[
     "The United States and Japan",
     "The United States and Brazil",
     "Japan and the Ottoman Empire",
     "Brazil and Argentina",
     "Persia and Siam"], ans=0,
   why="KC-5.2.I.B names European states as well as the United States and Japan as the acquirers of territory throughout Asia and the Pacific. No other state outside Europe is named in that statement, and the framework's claim is about who acquired territory, not about who could have."),
 dict(q="How does the framework describe the means by which many European states expanded their empires in Africa?",
   choices=[
     "By both warfare and diplomacy",
     "By warfare alone, since no agreements were made",
     "By diplomacy alone, since no force was used",
     "By purchase from other European states alone",
     "By the emigration of settlers, with no role for governments"], ans=0,
   why="KC-5.2.I.C states that many European states used both warfare and diplomacy to expand their empires in Africa. The framework names two means and not one, which is what makes each of the single-means options wrong rather than merely incomplete."),
 dict(q="An illustrative agreement of the period records that a local ruler grants a European state exclusive rights in his territory in return for a promise of protection, and that no fighting accompanied the arrangement. This document illustrates",
   choices=[
     "expansion by diplomacy, one of the two means the framework names for Africa",
     "expansion by warfare, the only means the framework names for Africa",
     "the transfer of a colony from a company to a government",
     "the establishment of a settler colony by permanent emigration",
     "the decline of an older empire's influence in the region"], ans=0,
   why="KC-5.2.I.C names warfare and diplomacy as the two means by which many European states expanded their empires in Africa. An agreement concluded without fighting is the second of those. The document reports no company, no settlement and no older empire."),
 dict(q="The framework states that Europeans established settler colonies in some parts of their empires. A settler colony is distinguished from other colonial arrangements by",
   choices=[
     "the permanent settlement of populations from the imperial state in the territory",
     "the absence of any administration answering to the imperial state",
     "the presence of a chartered company in place of a government",
     "the granting of full independence at the moment of acquisition",
     "the prohibition of all trade between the colony and the imperial state"], ans=0,
   why="KC-5.2.I.D states that Europeans established settler colonies in some parts of their empires, and the framework uses the same vocabulary of settlement in KC-5.2.II.B, where states expand by conquering and settling neighboring territories. Settlement is what the term picks out; the other four options describe arrangements the framework does not attach to it."),
 dict(q="Which territory does the course framework give as its illustrative example of a settler colony established within an empire?",
   choices=[
     "New Zealand",
     "The Congo",
     "Indonesia",
     "West Africa",
     "The Ottoman Balkans"], ans=0,
   why="The CED prints New Zealand as its illustrative example of settler colonies established in empires, alongside KC-5.2.I.D. The other four places appear in this unit in other roles: the Congo and Indonesia as transfers from non-state holders, West Africa among the African expansions, and the Balkans in the topic on responses to state expansion."),
 dict(q="One state is named by the framework as expanding its land holdings by conquering and settling neighbouring territories but is not among the states it names as acquiring territories throughout Asia and the Pacific. That state is",
   choices=[
     "Russia",
     "Japan",
     "The United States",
     "Belgium",
     "Portugal"], ans=0,
   why="KC-5.2.II.B names the United States, Russia and Japan as expanding their land holdings by conquering and settling neighboring territories, while KC-5.2.I.B names European states, the United States and Japan as acquiring territories throughout Asia and the Pacific. Russia is the state that appears in the first list and not in the second."),
 dict(q="Two illustrative accounts describe expansions in the same decades. In the first, a state annexes land bordering its own and settles families there; in the second, a state acquires an island group on the far side of an ocean. The most accurate comparison is that",
   choices=[
     "both are expansions of state power, one into neighbouring territory and one overseas",
     "both are expansions of state power, and the framework treats only the overseas kind as expansion",
     "neither is an expansion of state power, since no new government was created",
     "only the annexation of neighbouring land counts as acquiring territory",
     "the two cannot be compared because they occurred in different hemispheres"], ans=0,
   why="KC-5.2.I.B describes acquisition of territories across Asia and the Pacific and KC-5.2.II.B describes expansion by conquering and settling neighboring territories, so the framework treats both as expansions of state holdings. Learning objective B asks precisely for a comparison of such processes, so the difference in geography is what is being compared, not a reason to refuse the comparison."),
 dict(q="Why is the passage of a colony from a chartered company to a government correctly described as a shift in state power rather than as a change of officials?",
   choices=[
     "Power over the territory moved from a private body to a state that had not held it directly before",
     "Power over the territory moved from a state to a private body that had not held it before",
     "The territory ceased to be part of any empire at the moment of the transfer",
     "The change altered the borders of the territory rather than who governed it",
     "The change ended all taxation of the territory's inhabitants"], ans=0,
   why="KC-5.2.I.A describes states assuming direct control over colonies previously held by non-state entities, which is a change in the kind of body exercising power and not merely in its personnel. The reversal is offered as a distractor, and the framework attaches no change of borders, no end of empire and no fiscal consequence to the transfer itself."),
 dict(q="The framework names three European states in its illustrations of empires expanded in Africa. Those illustrations are",
   choices=[
     "Britain in West Africa, Belgium in the Congo, and the French in West Africa",
     "Spain in West Africa, Portugal in the Congo, and the Dutch in East Africa",
     "Russia in North Africa, Japan in West Africa, and the United States in the Congo",
     "Britain in Indonesia, Belgium in New Zealand, and the French in the Pacific",
     "The Ottoman Empire in East Africa, Persia in the Congo, and Belgium in West Africa"], ans=0,
   why="The CED's illustrative examples of European states that expanded empires in Africa are Britain in West Africa, Belgium in the Congo and the French in West Africa, printed alongside KC-5.2.I.C. The other options move those states to regions the framework does not attach to them."),
 dict(q="The register below records, for five hypothetical territories, which body exercised control at each end of the period. In how many of them did control pass from a non-state body to a state?",
   choices=[
     "Three of the five territories",
     "One of the five territories",
     "Two of the five territories",
     "Four of the five territories",
     "All five territories"], ans=0,
   table=_T_CONTROL,
   why="Read from the register alone: Territory Q, Territory S and Territory U each begin under a company or a private estate and end under a government, which is three. Territory R remains with the company throughout and Territory T is under a government at both ends, so neither shows the shift."),
 dict(q="Using the same hypothetical register, which territory shows control passing to a state other than the one whose company had held it?",
   choices=[
     "Territory S",
     "Territory Q",
     "Territory R",
     "Territory T",
     "Territory U"], ans=0,
   table=_T_CONTROL,
   why="The register gives Territory S a chartered trading company at the start and the government of a different European state at the end. Territory Q and Territory U pass to the government of the same state, Territory R does not change hands, and Territory T is under a government at both ends."),
 dict(q="In the same hypothetical register, which two territories are NOT examples of the shift from a non-state holder to direct state control?",
   choices=[
     "Territory R and Territory T",
     "Territory Q and Territory S",
     "Territory S and Territory U",
     "Territory Q and Territory T",
     "Territory R and Territory U"], ans=0,
   table=_T_CONTROL,
   why="Territory R is held by the same chartered company at both ends of the period, so no shift occurs, and Territory T is under a government at both ends, so there is no non-state holder to shift from. The remaining three all begin under a non-state body and end under a government."),
 dict(q="The register below records four hypothetical African territories, the means by which control over each was first obtained, and the number of settlers from the imperial state resident at the end of the period. Which territory is best described as a settler colony?",
   choices=[
     "Territory V",
     "Territory W",
     "Territory X",
     "Territory Y",
     "None of them, because settlement is not recorded"], ans=0,
   table=_T_SETTLERS,
   why="KC-5.2.I.D makes settlement the mark of a settler colony, and the register records 180,000 settlers in Territory V, the largest figure by a wide margin and more than the other three combined. The register does record settlement, so the last option is false on the face of the table."),
 dict(q="Considering the means recorded in the same hypothetical African register, what does the register illustrate about how control over these territories was obtained?",
   choices=[
     "Both warfare and diplomacy appear among the means recorded",
     "Only warfare appears among the means recorded",
     "Only diplomacy appears among the means recorded",
     "Every territory was obtained by transfer from a chartered company",
     "The means of acquisition is not recorded for any territory"], ans=0,
   table=_T_SETTLERS,
   why="KC-5.2.I.C states that many European states used both warfare and diplomacy to expand their empires in Africa, and the register carries a treaty negotiated with local rulers, two military campaigns and a company transfer. Both named means are therefore present, and no single means accounts for all four rows."),
 dict(q="Which conclusion about the four hypothetical African territories is NOT supported by the register?",
   choices=[
     "The territories obtained by military campaign hold fewer settlers than any territory obtained otherwise",
     "The territory obtained by treaty holds more settlers than any other territory listed",
     "One territory holds fewer than a thousand settlers at the end of the period",
     "Two of the four territories were obtained by military campaign",
     "The territory transferred from a chartered company holds the fewest settlers"], ans=0,
   table=_T_SETTLERS,
   why="Territory X was obtained by a military campaign and holds 95,000 settlers, more than the 600 in Territory Y, which was obtained by a company transfer, so the keyed statement fails on the register's own numbers. Each of the other four statements recomputes as true from the same three columns."),
 dict(q="What does a comparison of the Congo case with the Indonesian case show about state power in this period?",
   choices=[
     "In both, a territory held by a non-state holder came under the direct control of a European government",
     "In both, a territory held by a European government was handed to a non-state holder",
     "In both, a territory obtained independence from European control",
     "In both, control passed from one European government to another",
     "In both, a settler population took over the government of the territory"], ans=0,
   why="KC-5.2.I.A states the pattern and the CED prints these two as its illustrations of it: the Congo from private ownership to the Belgium government, and Indonesia and Southeast Asia from the Dutch East India Company to Dutch government control. The reversal is offered as a distractor and is not what either example describes."),
 dict(q="When a colony administered by a chartered company came under direct government administration, what changed and what remained the same?",
   choices=[
     "The body exercising control changed while the territory remained under imperial rule",
     "The territory ceased to be under imperial rule while the body exercising control remained the same",
     "Both the body exercising control and the imperial relationship ended at once",
     "Neither the body exercising control nor the imperial relationship was altered in any way",
     "The territory's population changed while its government did not"], ans=0,
   why="KC-5.2.I.A describes states assuming direct control over colonies previously held by non-state entities. The holder of control changes and the colonial relationship continues, which is why the framework files this under expansion of state power rather than under its end. The reversed reading is offered as a distractor."),
 dict(q="A student asserts that Spain and Portugal were the leading acquirers of new territory in Asia and the Pacific during this period. The framework corrects this by",
   choices=[
     "describing their influence as declining while other states acquired territories in the region",
     "describing their influence as growing faster than that of any other European state",
     "denying that any European state acquired territory in the region",
     "restricting all acquisition in the region to states outside Europe",
     "placing all acquisition in the region after the period closes"], ans=0,
   why="KC-5.2.I.B pairs the acquisitions by European states, the United States and Japan with the decline of Spanish and Portuguese influence in the same sentence, so the framework asserts the opposite of the student's claim about those two states while affirming that acquisition in the region did occur."),
 dict(q="An illustrative dispatch reports that in a colony held for many decades the imperial state has doubled its resident officials, extended its courts into the interior and imposed a direct tax. The dispatch is best used as evidence of",
   choices=[
     "a state strengthening its control over a colony it already held",
     "a state assuming control over a colony previously held by a company",
     "a state establishing a settler colony in newly acquired territory",
     "a colony securing independence from the imperial state",
     "the transfer of a colony from one imperial state to another"], ans=0,
   why="KC-5.2.I.A opens with states that strengthened their control over existing colonies, which is what more officials, a wider court system and a new direct tax describe. The dispatch names no company, no settlement, no independence and no second imperial state."),
 dict(q="KC-5.2.I.A names two related processes. They are",
   choices=[
     "strengthening control over existing colonies, and assuming direct control over colonies previously held by non-state entities",
     "acquiring colonies by purchase, and dividing colonies with rival states by treaty",
     "granting self-government to settler populations, and withdrawing officials from older colonies",
     "founding chartered companies, and transferring colonies from governments to those companies",
     "abolishing taxation in existing colonies, and prohibiting settlement in new ones"], ans=0,
   why="The statement reads that some states with existing colonies strengthened their control over those colonies and in some cases assumed direct control over colonies previously held by non-state entities. Those are the two processes; purchase, division, self-government, company founding and taxation policy are not asserted there."),
 dict(q="An illustrative account describes families emigrating permanently from a European state to a territory in its empire, taking up land there and remaining for generations. The framework's term for a part of an empire developed in this way is",
   choices=[
     "a settler colony",
     "a chartered company territory",
     "an anticolonial movement",
     "an economic sphere of influence",
     "a neighbouring territory acquired by conquest alone"], ans=0,
   why="KC-5.2.I.D states that Europeans established settler colonies in some parts of their empires, and permanent emigration from the imperial state to take up land is what the term picks out. The account describes no company charter, no resistance movement, no commercial sphere and no conquest of adjacent land."),
 dict(q="What do the expansions of the United States, Russia and Japan have in common as the framework describes them?",
   choices=[
     "Each added neighbouring territory by conquest and settlement",
     "Each added distant overseas territory by purchase alone",
     "Each acquired territory only through the transfer of company holdings",
     "Each abandoned territory it had previously held",
     "Each expanded only after the period covered by this unit"], ans=0,
   why="KC-5.2.II.B states that the United States, Russia and Japan expanded their land holdings by conquering and settling neighboring territories. Conquest and settlement of adjacent land is the shared feature; purchase, company transfer and abandonment are not asserted of them there."),
 dict(q="Why does the framework present the Congo and Indonesian transfers as illustrations rather than as isolated events?",
   choices=[
     "Because it states the pattern in general terms and offers these cases as examples of it",
     "Because these were the only two colonies that changed hands anywhere in the period",
     "Because both transfers were carried out by the same European state",
     "Because both territories became independent at the moment of transfer",
     "Because the framework requires students to memorize the date of each transfer"], ans=0,
   why="KC-5.2.I.A is a general statement about states assuming direct control over colonies previously held by non-state entities, and the CED prints the Congo and the Dutch East Indies as illustrative examples beside it. The framework marks such examples as illustrative and asks for no dates."),
 dict(q="An illustrative memorandum reports that officials of two European states have met to fix the boundary between their claims in an African region, and that the local population was not represented. The process the memorandum records is",
   choices=[
     "diplomacy between imperial states, one of the two means the framework names for expansion in Africa",
     "warfare between imperial states, the only means the framework names for expansion in Africa",
     "the transfer of a colony from a chartered company to a government",
     "the establishment of a settler colony by permanent emigration",
     "an anticolonial movement organized by the local population"], ans=0,
   why="KC-5.2.I.C names warfare and diplomacy as the two means by which many European states expanded their empires in Africa, and a negotiated boundary between two states is diplomacy. The memorandum reports no fighting, no company, no settlement and no movement of the local population."),
 dict(q="Which pair of questions about state expansion in this period can and cannot be settled from the framework's statements?",
   choices=[
     "Which states acquired territories in Asia and the Pacific can be settled; whether a particular acquisition was popular at home cannot",
     "Whether a particular acquisition was popular at home can be settled; which states acquired territories in Asia and the Pacific cannot",
     "Neither which states acquired territories nor by what means they expanded in Africa can be settled",
     "Both which states acquired territories and how each colony's population voted can be settled",
     "Only the number of settlers in each colony can be settled"], ans=0,
   why="KC-5.2.I.B names the acquiring states and KC-5.2.I.C names the means used in Africa, so those questions have answers in the framework. Public opinion in the imperial state, colonial voting and settler numbers are not asserted anywhere in this topic, and the reversal of the key is offered as a distractor."),
 dict(q="Learning objective B asks students to compare processes by which state power shifted in various parts of the world. What do the processes named in this topic share?",
   choices=[
     "In each, the holder or the reach of state power over a territory changed",
     "In each, an empire was dissolved and its territories left ungoverned",
     "In each, a chartered company replaced a government",
     "In each, expansion was accomplished without any use of force anywhere",
     "In each, the change was confined to a single continent"], ans=0,
   why="The processes the topic names are strengthened control over existing colonies, direct control assumed from non-state entities, acquisitions in Asia and the Pacific, warfare and diplomacy in Africa, settler colonies, and conquest and settlement of neighbouring territory. Each is a change in who exercises state power or how far it reaches, and they span several continents, use force in some cases and never leave a territory ungoverned."),
]
