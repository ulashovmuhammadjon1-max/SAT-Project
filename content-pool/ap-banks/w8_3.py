# AP WORLD HISTORY: MODERN 8.3 Effects of the Cold War
# CED effective Fall 2026 (Course Framework V.1), Unit 8 Cold War and
# Decolonization, c. 1900 to the present. Thematic focus: Governance (GOV).
#
# Learning Objective: Unit 8 Learning Objective C -- compare the ways in which
# the United States and the Soviet Union sought to maintain influence over the
# course of the Cold War. Suggested skill 5.B, explain how a historical
# development or process relates to another historical development or process.
#
# HISTORICAL DEVELOPMENT this topic prints, and the sentence nearly every key
# below rests on:
#   KC-6.2.IV.D  The Cold War produced new military alliances, including NATO
#                and the Warsaw Pact, and led to nuclear proliferation and proxy
#                wars between and within postcolonial states in Latin America,
#                Africa, and Asia.
# Two sentences from adjacent topic pages are used where an item needs to name
# what the two superpowers were:
#   KC-6.2.IV.C.ii  ... the democracy of the United States and the authoritarian
#                communist Soviet Union emerged as superpowers, which led to
#                ideological conflict and a power struggle between capitalism and
#                communism across the globe.
#   KC-6.2.I.C   After the end of World War II, some colonies negotiated their
#                independence, while others achieved independence through armed
#                struggle. (Used only to explain what "postcolonial" names.)
# ILLUSTRATIVE EXAMPLES the CED prints for proxy wars: the Korean War; the
# Angolan Civil War; the Sandinista-Contras conflict in Nicaragua. Illustrative
# examples are optional in the course, so exactly one item turns on them and its
# stem says so.
#
# WHAT IS DELIBERATELY NOT KEYED. The framework states that the Cold War led to
# nuclear proliferation AND to proxy wars. It does NOT assert that proliferation
# caused the superpowers to fight through clients instead of each other, however
# familiar that argument is, and it does not say the two never met in battle. No
# key here supplies either claim. Nor does any key assign blame for a proxy war
# to one superpower: the framework describes the pattern, not the culprit, and
# this is live political ground.
#
# SOURCES are text and unattributed. TABLES are labelled hypothetical in the
# stem and every keyed conclusion is recomputed from the table alone. DATES are
# written "1950 to 1990", never with a hyphen.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("8.3", "Effects of the Cold War", 8)

_T_ALLIANCE = dict(
    headers=["Alliance (hypothetical record)", "Member states, 1955", "Member states, 1975"],
    rows=[["Alliance one", "15", "19"],
          ["Alliance two", "8", "7"]])

_T_NUCLEAR = dict(
    headers=["Decade (hypothetical record)", "States possessing nuclear weapons"],
    rows=[["1940s", "1"],
          ["1950s", "3"],
          ["1960s", "5"],
          ["1970s", "6"]])

_T_PROXY = dict(
    headers=["Region (hypothetical count, 1950 to 1990)",
             "Armed conflicts between states", "Armed conflicts within a single state"],
    rows=[["Africa", "3", "11"],
          ["Asia", "5", "9"],
          ["Latin America", "2", "8"]])

QUESTIONS = [

 dict(q="An unattributed treaty text of the early 1950s provides that an armed attack on any signatory shall be treated as an attack on all of them, and establishes a joint command for the signatories' forces. A treaty of this kind is best understood as an instance of",
   choices=[
     "the new military alliances that the Cold War produced",
     "an agreement to reduce the signatories' armed forces to a common ceiling",
     "a trade agreement setting tariffs among the signatories",
     "a colonial charter granting a European state authority over an overseas territory",
     "a settlement ending a war between two of the signatories"],
   ans=0,
   why="KC-6.2.IV.D states that the Cold War produced new military alliances, including NATO and the Warsaw Pact. A mutual defense pledge with a joint command is the characteristic form of such an alliance and is neither a disarmament measure, a tariff arrangement nor a colonial instrument."),

 dict(q="Two treaty texts of the 1950s are placed side by side, one drawn up by each bloc. Each pledges its signatories to treat an attack on one as an attack on all. What does this comparison most directly show about the two superpowers?",
   choices=[
     "Both answered the confrontation with the same instrument, a standing military alliance",
     "Both had abandoned the search for influence beyond their own borders",
     "Neither was willing to enter into any commitment with other states",
     "Both had agreed to place their forces under a single joint command with each other",
     "Both treaties were signed by every state in the world at the same time"],
   ans=0,
   why="KC-6.2.IV.D states that the Cold War produced new military alliances, including NATO and the Warsaw Pact, which is a pairing: the framework records the same instrument taken up on both sides. Comparing the ways the two superpowers sought to maintain influence is the task this topic sets, and identical instruments is the comparison the framework itself supports."),

 dict(q="In the terms this course uses, a proxy war is best described as",
   choices=[
     "a conflict between or within other states in which the rival superpowers backed opposing sides",
     "a conflict fought directly between the armies of the two superpowers on their own territory",
     "a conflict conducted entirely through diplomatic notes and without armed force",
     "a conflict between two colonial empires over the ownership of a territory",
     "a conflict over trade tariffs settled by an international tribunal"],
   ans=0,
   why="KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states in Latin America, Africa, and Asia. The framework locates such wars in other states rather than in the superpowers themselves, and the phrase between and within covers both interstate and internal conflicts."),

 dict(q="Which three regions does this course name as the setting of the proxy wars the Cold War produced?",
   choices=[
     "Latin America, Africa, and Asia",
     "Western Europe, Scandinavia, and the Arctic",
     "Australia, Antarctica, and the Pacific islands",
     "Central Europe, the Balkans, and the Baltic states",
     "North America, Western Europe, and Japan"],
   ans=0,
   why="KC-6.2.IV.D names proxy wars between and within postcolonial states in Latin America, Africa, and Asia. The regions matter because they identify where the confrontation was fought with arms while the two superpowers themselves were not invaded."),

 dict(q="The phrase between and within postcolonial states, as this course applies it to proxy wars, indicates that such wars",
   choices=[
     "included both wars fought between separate states and armed conflicts inside a single state",
     "were fought only across international borders and never inside one country",
     "were fought only inside single countries and never between separate states",
     "were confined to states that had never been governed by a colonial power",
     "took place only in states that possessed nuclear weapons of their own"],
   ans=0,
   why="KC-6.2.IV.D says proxy wars occurred between and within postcolonial states, a formulation that covers interstate war and internal war alike. Restricting the category to only one of the two contradicts the framework's own wording, and postcolonial means the opposite of never colonized."),

 dict(q="The table gives a hypothetical record of two military alliances. Which conclusion does the table alone support?",
   table=_T_ALLIANCE,
   choices=[
     "One alliance gained members over the period while the other lost members",
     "Both alliances gained members over the period recorded",
     "Both alliances lost members over the period recorded",
     "The two alliances had the same number of members in 1975",
     "The alliance that was smaller in 1955 was the larger of the two in 1975"],
   ans=0,
   why="KC-6.2.IV.D states that the Cold War produced new military alliances, including NATO and the Warsaw Pact, so the membership of such blocs is a measure of the confrontation's shape. The record is hypothetical and the keyed conclusion, together with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="This course offers three armed conflicts as illustrative examples of proxy wars. They are",
   choices=[
     "the Korean War, the Angolan Civil War, and the Sandinista-Contras conflict in Nicaragua",
     "the Napoleonic Wars, the Crimean War, and the Boer War",
     "the Seven Years War, the American Revolution, and the Haitian Revolution",
     "the First World War, the Second World War, and the Russian Civil War",
     "the Opium Wars, the Taiping Rebellion, and the Boxer Rebellion"],
   ans=0,
   why="The CED prints these three as the illustrative examples accompanying KC-6.2.IV.D and its statement about proxy wars. Every distractor lists conflicts the framework places in earlier units and outside the Cold War entirely."),

 dict(q="The table records a hypothetical count of the states possessing nuclear weapons. Which conclusion does the table alone support?",
   table=_T_NUCLEAR,
   choices=[
     "The number rose in every decade recorded and ended more than five times its starting value",
     "The number was unchanged from the 1950s onward",
     "The number fell in at least one of the decades recorded",
     "The largest single increase came in the last decade recorded",
     "The number doubled between the first and last decades recorded"],
   ans=0,
   why="KC-6.2.IV.D states that the Cold War led to nuclear proliferation, and a rising count of states holding such weapons is what proliferation names. The record is hypothetical and both halves of the keyed conclusion, with the falsity of each distractor, are recomputed from the table alone in the verifier."),

 dict(q="In this course's usage, nuclear proliferation refers to",
   choices=[
     "the spread of nuclear weapons to a growing number of states",
     "an agreement among states to destroy the nuclear weapons they already hold",
     "the use of nuclear power to generate electricity for civilian customers",
     "the construction of shelters intended to protect civilians from attack",
     "the transfer of a single state's entire arsenal to an international body"],
   ans=0,
   why="KC-6.2.IV.D names nuclear proliferation among the effects of the Cold War, alongside new military alliances and proxy wars, in a sentence about the confrontation's spread rather than its containment. Proliferation is growth in the number of holders, which is the opposite of the disarmament and transfer options offered."),

 dict(q="A newly independent Asian state's foreign minister writes in 1963 that his country's internal quarrels have acquired sponsors abroad, and that each faction now speaks the language of one great power. His observation describes a development this course identifies as",
   choices=[
     "a proxy war fought within a postcolonial state",
     "the formation of a new military alliance among European states",
     "the negotiated transfer of power from an imperial authority",
     "the spread of a globalized consumer culture across national borders",
     "the redistribution of land within a state that had adopted communism"],
   ans=0,
   why="KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states, and factions inside one newly independent state acquiring rival great-power sponsors is that pattern in its internal form. The other options name developments the framework attaches to different statements."),

 dict(q="A student asks how decolonization and the Cold War are connected. Which answer draws most directly on this course's framework?",
   choices=[
     "The states that emerged from empire in Asia, Africa and Latin America became the ground on which the superpowers' proxy wars were fought",
     "Decolonization ended before the Cold War began and the two processes never overlapped",
     "The superpowers agreed to leave newly independent states entirely outside their competition",
     "Decolonization took place only in Europe, where the Cold War was concentrated",
     "The Cold War prevented any colony from becoming independent until it was over"],
   ans=0,
   why="KC-6.2.IV.D locates proxy wars between and within postcolonial states in Latin America, Africa, and Asia, which is a direct connection between the end of empire and the superpower confrontation. KC-6.2.I.C places the achievement of independence in the same postwar years, so the two processes overlap rather than succeed one another."),

 dict(q="The table gives a hypothetical count of armed conflicts by region. Which conclusion does the table alone support?",
   table=_T_PROXY,
   choices=[
     "In every region listed, conflicts within a single state outnumbered conflicts between states",
     "In every region listed, conflicts between states outnumbered conflicts within a single state",
     "Asia recorded the fewest conflicts of both kinds",
     "The three regions recorded the same number of conflicts within a single state",
     "Africa recorded no armed conflicts between states at all"],
   ans=0,
   why="KC-6.2.IV.D says proxy wars occurred between and within postcolonial states, and the relative weight of the two kinds is exactly what a count of this shape reports. The figures are hypothetical and the keyed comparison, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="Which statement about the effects of the Cold War is NOT supported by this course?",
   choices=[
     "The confrontation reduced the number of states holding nuclear weapons",
     "The confrontation produced new military alliances",
     "The confrontation led to armed conflicts inside postcolonial states",
     "The confrontation reached Latin America, Africa and Asia",
     "The confrontation led to a growth in the number of nuclear-armed states"],
   ans=0,
   why="KC-6.2.IV.D lists nuclear proliferation among the Cold War's effects, so a claim that the confrontation reduced the number of nuclear-armed states reverses the framework's own sentence. The other four restate the alliances, the proxy wars, the regions and the proliferation that sentence names."),

 dict(q="A historian claims that a particular civil war in an African state during the 1970s should be counted as a proxy war. Which evidence would best support that claim?",
   choices=[
     "Records showing each side supplied with arms and advisers by a different superpower",
     "Records showing that the war lasted longer than five years",
     "Records showing that the country had once been governed by a European power",
     "Records showing that the war was reported in newspapers on several continents",
     "Records showing that both sides used weapons manufactured in the same decade"],
   ans=0,
   why="KC-6.2.IV.D describes proxy wars as a product of the Cold War fought within postcolonial states, so what makes a conflict a proxy war is the rival sponsorship rather than its duration, its colonial past or its press coverage. Every postcolonial state satisfies the colonial-past test, which is why that option cannot distinguish one war from another."),

 dict(q="A 1971 appeal from a faction in a newly independent African state asks a superpower for weapons, arguing that its rival is already receiving them from the other side. The appeal is most useful to a historian as evidence of",
   choices=[
     "how superpower rivalry was drawn into a local contest by the local participants themselves",
     "the total quantity of weapons that either superpower actually delivered",
     "the private intentions of the superpower to which the appeal was addressed",
     "the outcome of the contest between the two factions",
     "the level of literacy in the state from which the appeal was sent"],
   ans=0,
   why="KC-6.2.IV.D places proxy wars within postcolonial states, and an appeal of this kind shows one of the mechanisms by which a local contest acquired superpower sponsors. A request records what its author sought, not what was delivered, what the recipient intended, or how the contest ended."),

 dict(q="How does a military alliance of the kind this course describes differ from a proxy war?",
   choices=[
     "An alliance is a standing commitment among states, while a proxy war is armed conflict in which rival sponsors back opposing sides",
     "An alliance involves armed force, while a proxy war is conducted entirely through diplomacy",
     "An alliance is formed only after a proxy war has been concluded",
     "An alliance is confined to postcolonial states, while a proxy war occurs only in Europe",
     "There is no difference; this course treats the two as the same development"],
   ans=0,
   why="KC-6.2.IV.D lists new military alliances and proxy wars as two separate products of the Cold War in a single sentence. The alliances named are standing mutual commitments, while the proxy wars are the fighting itself, located between and within postcolonial states rather than in Europe."),

 dict(q="A pamphlet published in a nonaligned state in 1968 complains that its region has become a place where other people's disputes are settled with local lives. The complaint corresponds most closely to which development named in this course?",
   choices=[
     "Proxy wars fought between and within postcolonial states",
     "The negotiated independence of colonies from their imperial rulers",
     "The formation of new military alliances in Europe",
     "The growth of knowledge economies in the late twentieth century",
     "The migration of former colonial subjects to imperial metropoles"],
   ans=0,
   why="KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states in Latin America, Africa, and Asia. A complaint that outsiders' disputes are being settled locally with local casualties describes that pattern from inside one of those states."),

 dict(q="Considered as a comparison, which statement about the two superpowers' pursuit of influence is best supported by this course?",
   choices=[
     "Each built a military alliance and each backed clients in conflicts outside its own territory",
     "One relied wholly on alliances while the other relied wholly on trade agreements",
     "Neither sought influence in regions that had recently emerged from colonial rule",
     "One acquired nuclear weapons while the other consistently refused to develop them",
     "Both confined their competition to the continent on which each was situated"],
   ans=0,
   why="KC-6.2.IV.D names new military alliances, including NATO and the Warsaw Pact, and proxy wars between and within postcolonial states as products of the Cold War, which places both instruments on both sides. The framework does not describe either superpower abstaining from alliances, from nuclear weapons or from the postcolonial world."),

 dict(q="Which sequence of relationships does this course support?",
   choices=[
     "The Cold War came first, and new military alliances, nuclear proliferation and proxy wars followed from it",
     "New military alliances came first and produced the Cold War as their consequence",
     "Proxy wars came first and produced the Cold War as their consequence",
     "Nuclear proliferation came first and produced both the Cold War and decolonization",
     "The three developments occurred in unrelated centuries and had no bearing on each other"],
   ans=0,
   why="KC-6.2.IV.D makes the Cold War the subject and the alliances, the proliferation and the proxy wars its products: the confrontation produced them rather than being produced by them. Every distractor reverses that direction or denies the relation the sentence asserts."),

 dict(q="A government in a small European state argues in 1955 that joining one of the two alliances is the only way to guarantee its security. Which consideration would a historian add to explain why alliances of this kind existed at all?",
   choices=[
     "The confrontation between the superpowers had produced standing military blocs on both sides",
     "The state in question had recently acquired overseas colonies it needed to defend",
     "The world's states were then negotiating a single agreement to abolish armed forces",
     "The state was seeking membership in a regional free-trade area rather than a bloc",
     "Alliances of this kind had been abolished by international agreement after the war"],
   ans=0,
   why="KC-6.2.IV.D states that the Cold War produced new military alliances, including NATO and the Warsaw Pact, which is the condition that makes joining one an available choice in 1955. The other options describe arrangements the framework does not place in this period."),

 dict(q="Which of the following best explains why this course treats proxy wars as an effect of the Cold War rather than as unrelated local conflicts?",
   choices=[
     "The framework describes them as wars the Cold War led to, fought with rival superpower backing",
     "The framework describes them as conflicts fought by the superpowers' own armies at home",
     "The framework describes them as disputes settled by international courts",
     "The framework describes them as conflicts that occurred only before 1945",
     "The framework describes them as conflicts over trade rules among neighbouring states"],
   ans=0,
   why="KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states, which is a claim about their relation to the confrontation. The framework does not describe them as fought at home by the superpowers, as judicial disputes, as prewar, or as commercial."),

 dict(q="A researcher wishes to measure the extent of nuclear proliferation over the second half of the twentieth century. Which measure fits the framework's use of the term most closely?",
   choices=[
     "The number of separate states that had acquired nuclear weapons by each date",
     "The total electricity generated by nuclear power stations each year",
     "The number of civilians who had participated in air-raid drills",
     "The number of scientific papers published on nuclear physics",
     "The share of a state's budget devoted to its diplomatic service"],
   ans=0,
   why="KC-6.2.IV.D names nuclear proliferation among the Cold War's effects, and proliferation is the spread of the weapons to more holders. Civilian power generation, drills, publications and budgets measure adjacent things rather than the number of states holding the weapons."),

 dict(q="A hypothetical internal report circulated within one superpower in 1966 recommends supporting a faction in a distant civil war on the ground that the rival superpower is supporting the other side. What does this document most directly illustrate?",
   choices=[
     "The reasoning by which a local conflict was absorbed into the superpower confrontation",
     "The formal terms of the military alliance to which the superpower belonged",
     "The number of nuclear weapons the superpower possessed at that date",
     "The economic policy the superpower pursued at home during the 1960s",
     "The process by which colonies negotiated their independence peacefully"],
   ans=0,
   why="KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states, and this document shows the step by which a distant conflict became one: the rival's involvement is itself offered as the reason to intervene. The report is silent on alliances, arsenals, domestic policy and decolonization."),

 dict(q="Which claim about the geography of the Cold War's armed effects does this course support?",
   choices=[
     "The fighting associated with the confrontation fell largely on states outside the two superpowers",
     "The fighting associated with the confrontation fell largely on the two superpowers' own territory",
     "The confrontation produced no armed conflict anywhere in the world",
     "The confrontation produced armed conflict only in states that possessed nuclear weapons",
     "The confrontation produced armed conflict only in Europe"],
   ans=0,
   why="KC-6.2.IV.D places proxy wars between and within postcolonial states in Latin America, Africa, and Asia, which locates the fighting outside the superpowers themselves and outside Europe. The framework records the conflicts rather than denying them."),

 dict(q="Two accounts of the same 1970s civil war are compared. One, written in a superpower capital, describes the war as a contest between two world systems; the other, written locally, describes it as a quarrel over land and office that outsiders later joined. A historian using both would best conclude that",
   choices=[
     "the conflict had local origins and acquired an additional superpower dimension",
     "one of the two accounts must be a deliberate fabrication",
     "the conflict had no local causes and was created entirely from outside",
     "the conflict had no international dimension and the first account is irrelevant",
     "the two accounts describe two different wars in two different countries"],
   ans=0,
   why="KC-6.2.IV.D describes proxy wars as fought within postcolonial states, a formulation that presupposes a conflict located in such a state and a superpower rivalry running through it. Each account reports one of those two layers, and the framework's own phrasing accommodates both."),

 dict(q="Which of the following would be the least useful evidence for studying the alliances the Cold War produced?",
   choices=[
     "A census recording the population of a nonaligned state in the same decade",
     "The text of a mutual defense treaty signed by one bloc",
     "The list of states acceding to such a treaty over time",
     "The record of a joint military exercise conducted by an alliance's members",
     "A government memorandum debating whether to join one of the two blocs"],
   ans=0,
   why="KC-6.2.IV.D identifies the alliances by their character as standing military commitments, so treaty texts, accession lists, joint exercises and accession debates all bear on them directly. A population count for a state outside both blocs speaks to none of that."),

 dict(q="A commentator writes in 1980 that a small state can now be ruined by a quarrel to which it was never a party. Which development named in this course does the remark most directly reflect?",
   choices=[
     "Proxy wars fought in states far from either superpower's own territory",
     "The negotiation of independence between a colony and its imperial ruler",
     "The redrawing of political boundaries after colonial authorities withdrew",
     "The globalization of consumer culture across national borders",
     "The strong role newly independent governments took in guiding economic life"],
   ans=0,
   why="KC-6.2.IV.D states that the Cold War led to proxy wars between and within postcolonial states in Latin America, Africa, and Asia, which is precisely a quarrel between two other powers being fought out on a third party's ground. The other options name developments the framework attaches to different statements."),

 dict(q="Suppose a student claims that the two superpowers pursued influence by entirely different means. What does this course's own account of the period allow that student to say?",
   choices=[
     "Very little, because the framework records the same instruments, alliances and proxy conflicts, on both sides",
     "A great deal, because the framework describes one side as using alliances and the other as using trade",
     "A great deal, because the framework says one side avoided the postcolonial world entirely",
     "Nothing at all, because the framework does not mention either superpower",
     "A great deal, because the framework says only one of the two ever acquired nuclear weapons"],
   ans=0,
   why="KC-6.2.IV.D names new military alliances, including NATO and the Warsaw Pact, together with nuclear proliferation and proxy wars, without assigning any one of those instruments to a single side. A claim of entirely different means therefore runs past what the framework supports, which is what a comparison in this topic has to respect."),

 dict(q="Which statement best describes the relationship between the ideological character of the Cold War and its armed effects?",
   choices=[
     "A struggle framed as one between rival systems was pursued through alliances, arms and wars in other states",
     "A struggle framed as one between rival systems produced no consequences beyond speeches and publications",
     "A struggle over territory alone produced alliances but no ideological argument",
     "A struggle over religious doctrine produced the alliances and proxy wars of the period",
     "A struggle between two identical systems produced a competition over vocabulary"],
   ans=0,
   why="KC-6.2.IV.C.ii describes the confrontation as an ideological conflict and a power struggle between capitalism and communism across the globe, and KC-6.2.IV.D records the alliances, the proliferation and the proxy wars that struggle produced. The key joins the two sentences, and each distractor denies one of them."),

 dict(q="Taking the topic as a whole, which single sentence best states the effects of the Cold War as this course presents them?",
   choices=[
     "The confrontation produced standing military alliances, spread nuclear weapons to more states, and set off wars between and within postcolonial states in Latin America, Africa and Asia",
     "The confrontation was settled by a treaty within five years and left no lasting institutions",
     "The confrontation produced alliances in Europe but had no armed consequences anywhere else",
     "The confrontation reduced the number of armed conflicts in the world to nearly none",
     "The confrontation was carried on entirely within the borders of the two superpowers"],
   ans=0,
   why="KC-6.2.IV.D states all three effects in one sentence: new military alliances including NATO and the Warsaw Pact, nuclear proliferation, and proxy wars between and within postcolonial states in Latin America, Africa, and Asia. Each distractor drops or contradicts at least one of the three."),
]
