# AP U.S. HISTORY 3.2 The Seven Years' War (The French and Indian War)
# Title copied verbatim from US_HISTORY_topics.json, which carries the CED's own curly
# apostrophe in "Years'". Every apostrophe in the QUESTIONS below is a plain ASCII one,
# because es_check refuses non-ASCII anywhere in student-facing text.
# Unit 3, Period 3: 1754 to 1800. Suggested skill 1.B, explain a historical concept,
# development, or process. Reasoning process printed for this topic: Causation.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 3: Learning Objective B
#       Explain the causes and effects of the Seven Years' War (the French and Indian War).
#
#   THEMATIC FOCUS: America in the World (WOR)
#       Diplomatic, economic, cultural, and military interactions between empires, nations,
#       and peoples shape the development of America and America's increasingly important
#       role in the world.
#
#   KC-3.1.I.A  Colonial rivalry intensified between Britain and France in the mid-18th
#               century, as the growing population of the British colonies expanded into
#               the interior of North America, threatening French-Indian trade networks
#               and American Indian autonomy.
#   KC-3.1.I.B  Britain achieved a major expansion of its territorial holdings by defeating
#               the French, but at tremendous expense, setting the stage for imperial
#               efforts to raise revenue and consolidate control over the colonies.
#   KC-3.1.I.C  After the British victory, imperial officials' attempts to prevent colonists
#               from moving westward generated colonial opposition, while native groups
#               sought to both continue trading with Europeans and resist the encroachments
#               of colonists on tribal lands.
#
#   And the sentence these three sit beneath, printed in the unit's preview:
#   KC-3.1.I    The competition among the British, French, and American Indians for economic
#               and political advantage in North America culminated in the Seven Years' War
#               (the French and Indian War), in which Britain defeated France and allied
#               American Indians.
#
# WHAT IS NOT KEYED, DELIBERATELY. The topic page also carries an OPTIONAL SOURCES list
# (the Jumonville Glen skirmish, the Ohio Company instructions, a Galloway letter, the
# Proclamation Line, a Pontiac speech). The CED says of that list, in its own words, that
# these "are not required AP course content" and that "None of the AP Exam questions
# require students to have studied these specific sources." So no key in this module turns
# on any of them, and one item keys that caveat itself. Every key traces to the four
# sentences above, to Learning Objective B, to the WOR thematic focus, or to the skill and
# reasoning process printed on the page.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table= and
# every figure in them is explicitly hypothetical, since the CED prints no data here.
# PROSE ONLY: no LaTeX; a span of years is written "1754 to 1800", never with a hyphen.
# FIVE choices (A-E). Every invented source is marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("3.2", "The Seven Years’ War (The French and Indian War)", 3)

_T_POP = dict(
    headers=["Decade (hypothetical figures)",
             "People in the British mainland colonies (thousands)",
             "People living in the interior districts (thousands)"],
    rows=[["First", "900", "40"],
          ["Second", "1,300", "110"],
          ["Third", "1,800", "260"]])

_T_EXPENSE = dict(
    headers=["Head of account (hypothetical index)", "Before the war", "After the war"],
    rows=[["Cost of maintaining forces in North America", "20", "100"],
          ["Revenue raised in the colonies", "6", "7"],
          ["Mainland territory administered", "30", "95"]])

_T_NATIVE = dict(
    headers=["Group in a hypothetical set of records",
             "Continued trading with Europeans",
             "Contested colonists' settlement on tribal land"],
    rows=[["Group 1", "Yes", "Yes"],
          ["Group 2", "Yes", "Yes"],
          ["Group 3", "Yes", "Yes"],
          ["Group 4", "No", "Yes"]])

QUESTIONS = [

 dict(q="Unit 3's Learning Objective B names one war and asks students to explain two things "
        "about it. Which statement gives the objective?",
      choices=[
        "Explain the causes and effects of the Seven Years' War, also called the French and "
        "Indian War",
        "Explain the causes of the Seven Years' War, without treating its consequences",
        "Describe the battles of the Seven Years' War in the order they were fought",
        "Compare the Seven Years' War with a European war of the same century",
        "Explain how the Seven Years' War was financed by the colonies themselves"],
      ans=0,
      why="Unit 3: Learning Objective B reads 'Explain the causes and effects of the Seven "
          "Years' War (the French and Indian War).' Both halves are in the objective, which "
          "is why an objective confined to causes fails; the framework asks for explanation "
          "rather than narration or comparison, and KC-3.1.I.B says the war was fought at "
          "tremendous expense to Britain rather than financed by the colonies."),

 dict(q="KC-3.1.I.A gives a reason that colonial rivalry between Britain and France "
        "intensified. Which reason does the framework state?",
      choices=[
        "The growing population of the British colonies expanded into the interior of North "
        "America",
        "The French population of North America grew faster than the British and pressed "
        "eastward",
        "Both powers withdrew their settlers from the interior and left it to trade alone",
        "A European treaty transferred the interior to Britain before any settlement occurred",
        "British colonists abandoned the coast and moved their whole population inland"],
      ans=0,
      why="KC-3.1.I.A states that colonial rivalry intensified between Britain and France in "
          "the mid-18th century AS the growing population of the British colonies expanded "
          "into the interior of North America. The framework locates the growth and the "
          "expansion on the British side, so a mirror-image account of French pressure "
          "reverses it, and withdrawal, a prior treaty and a wholesale abandonment of the "
          "coast are each contradicted by the same sentence."),

 dict(q="According to KC-3.1.I.A, that expansion into the interior threatened two things at "
        "once. Which pair does the framework name?",
      choices=[
        "French-Indian trade networks and American Indian autonomy",
        "French-Indian trade networks and the authority of the British Parliament",
        "American Indian autonomy and the profits of the British Atlantic fisheries",
        "Spanish mission settlements and French-Indian trade networks",
        "The autonomy of the colonial assemblies and the French claim to the coast"],
      ans=0,
      why="KC-3.1.I.A ends by naming what the expansion threatened: French-Indian trade "
          "networks AND American Indian autonomy. The anchor carries both because each "
          "distractor keeps one of the two and replaces the other with something the "
          "sentence does not mention."),

 dict(q="In what part of the century does KC-3.1.I.A place the intensifying rivalry between "
        "Britain and France?",
      choices=[
        "The middle of the 18th century",
        "The opening years of the 17th century",
        "The closing years of the 18th century",
        "The middle of the 19th century",
        "The framework gives no time for it at all"],
      ans=0,
      why="KC-3.1.I.A states that colonial rivalry intensified between Britain and France in "
          "the mid-18th century, which sits at the opening of the span 1754 to 1800 that this "
          "unit covers. The other three datings fall in different centuries or at the wrong "
          "end of this one, and the sentence plainly does date the development."),

 dict(q="KC-3.1.I.B describes what Britain gained from the war and what it cost. Which "
        "statement holds both halves together as the framework does?",
      choices=[
        "Britain achieved a major expansion of its territorial holdings by defeating the "
        "French, but at tremendous expense",
        "Britain achieved a major expansion of its territorial holdings at little cost to "
        "itself",
        "Britain gained no territory but bore a tremendous expense",
        "Britain gained territory from Spain rather than from France, and at moderate cost",
        "Britain's gains and its costs were both small enough to leave imperial policy "
        "unchanged"],
      ans=0,
      why="KC-3.1.I.B reads that Britain achieved a major expansion of its territorial "
          "holdings by defeating the French, BUT at tremendous expense. The word but is doing "
          "the work: the sentence asserts the gain and the cost together, so an account "
          "keeping only one of them, or naming Spain as the defeated power, is not the "
          "framework's claim."),

 dict(q="KC-3.1.I.B says the expense of the war set the stage for something. What does the "
        "framework say it set the stage for?",
      choices=[
        "Imperial efforts to raise revenue and consolidate control over the colonies",
        "Imperial efforts to grant the colonies representation in Parliament",
        "A withdrawal of imperial officials from North America to reduce costs",
        "The sale of the newly won territory to another European power",
        "A decision to leave colonial administration exactly as it had been"],
      ans=0,
      why="KC-3.1.I.B ends 'setting the stage for imperial efforts to raise revenue and "
          "consolidate control over the colonies'. Raising revenue and consolidating control "
          "are the two things the sentence names, so granting representation, withdrawing, "
          "selling the territory and leaving administration untouched each contradict it."),

 dict(q="KC-3.1.I.C describes what followed when imperial officials tried to prevent colonists "
        "from moving westward. What does the framework say followed?",
      choices=[
        "The attempts generated colonial opposition",
        "The attempts were welcomed by colonists as a protection against conflict",
        "The attempts succeeded so completely that no colonist crossed the mountains again",
        "The attempts were made by the colonial assemblies rather than by imperial officials",
        "The attempts ended the competition for land in the interior"],
      ans=0,
      why="KC-3.1.I.C states that after the British victory, imperial officials' attempts to "
          "prevent colonists from moving westward GENERATED COLONIAL OPPOSITION. The sentence "
          "attributes the attempts to imperial officials, not to the assemblies, and reports "
          "opposition rather than welcome, complete success or an end to the competition."),

 dict(q="KC-3.1.I.C says native groups sought two things after the British victory. Which "
        "statement gives both?",
      choices=[
        "They sought both to continue trading with Europeans and to resist the encroachments "
        "of colonists on tribal lands",
        "They sought to continue trading with Europeans and accepted colonial settlement on "
        "tribal lands",
        "They sought to resist the encroachments of colonists and ended all trade with "
        "Europeans",
        "They sought neither to trade with Europeans nor to contest colonial settlement",
        "They sought to replace trade with Europeans by trade among themselves alone"],
      ans=0,
      why="KC-3.1.I.C states that native groups sought to BOTH continue trading with Europeans "
          "AND resist the encroachments of colonists on tribal lands. The anchor carries both "
          "halves because each distractor keeps one and denies the other, and the framework "
          "presents them as held together rather than as alternatives."),

 dict(q="The unit's preview sentence for this material names three parties whose competition "
        "culminated in the war. Which set does it name?",
      choices=[
        "The British, the French, and American Indians",
        "The British, the French, and the Spanish",
        "The British, the Dutch, and American Indians",
        "The French, the Spanish, and American Indians",
        "The British and the French, with no third party involved"],
      ans=0,
      why="KC-3.1.I states that the competition among the British, French, and American "
          "Indians for economic and political advantage in North America culminated in the "
          "Seven Years' War. American Indians are one of the three competing parties in that "
          "sentence, so substituting the Spanish or the Dutch, or reducing the contest to two "
          "European powers, drops a party the framework names."),

 dict(q="How does KC-3.1.I state the outcome of the fighting?",
      choices=[
        "Britain defeated France and allied American Indians",
        "France defeated Britain and allied American Indians",
        "The fighting ended in a stalemate that left the interior as it had been",
        "American Indian nations defeated both European powers",
        "Britain defeated Spain and its allies in the interior"],
      ans=0,
      why="KC-3.1.I ends 'in which Britain defeated France and allied American Indians'. The "
          "anchor carries the whole clause because the leading distractor is that same clause "
          "with victor and loser exchanged, which is how the sentence is likeliest to be "
          "misremembered; KC-3.1.I.B independently confirms Britain as the power that gained "
          "territory by defeating the French."),

 dict(q="This topic sits under a thematic focus the framework calls America in the World. What "
        "does that focus statement assert?",
      choices=[
        "Diplomatic, economic, cultural, and military interactions between empires, nations, "
        "and peoples shape the development of America and America's role in the world",
        "American development is shaped by internal migration rather than by contact with "
        "other peoples",
        "American national identity is shaped by debates about democracy, freedom, and "
        "citizenship",
        "Social categories, roles, and practices are created and transformed throughout "
        "American history",
        "Push and pull factors shape immigration to and migration within America"],
      ans=0,
      why="The America in the World thematic focus printed on this topic page reads that "
          "diplomatic, economic, cultural, and military interactions between empires, nations, "
          "and peoples shape the development of America and America's increasingly important "
          "role in the world, which is why KC-3.1.I.A's rivalry between two empires sits under "
          "it. The other four statements are the framework's thematic focuses for national "
          "identity, social structures and migration, printed on other topic pages."),

 dict(q="Which skill statement is printed beside this topic's title as the one students should "
        "practise here?",
      choices=[
        "Explain a historical concept, development, or process",
        "Identify and describe a historical context for a specific historical development or "
        "process",
        "Identify the evidence used in a source to support an argument",
        "Explain the point of view, purpose, historical situation, and audience of a source",
        "Support an argument using specific and relevant evidence"],
      ans=0,
      why="Skill 1.B, explain a historical concept, development, or process, is printed on "
          "this topic page, and it is what Unit 3: Learning Objective B asks for when it says "
          "EXPLAIN the causes and effects of the war. The other four are skills 4.A, 3.B, 2.B "
          "and 6.B, each printed on a different topic page of this unit."),

 dict(q="The unit's topic table assigns a reasoning process to each topic. Which one does it "
        "assign here?",
      choices=[
        "Causation",
        "Comparison",
        "Continuity and Change",
        "Contextualization",
        "Argumentation"],
      ans=0,
      why="The unit's topic table assigns Causation to this topic, which matches Unit 3: "
          "Learning Objective B asking for the CAUSES AND EFFECTS of the war and matches the "
          "shape of KC-3.1.I.A, KC-3.1.I.B and KC-3.1.I.C, each of which links a development "
          "to what produced it or what followed from it. Comparison and Continuity and Change "
          "are assigned to other topics of this unit, and the remaining two are skill "
          "categories rather than reasoning processes."),

 dict(q="A hypothetical set of instructions, its author unnamed, tells an agent of a land "
        "company to travel beyond the mountains, survey ground suitable for farms, and report "
        "which routes traders already use. Which development described in the framework does "
        "an arrangement of this kind belong to?",
      choices=[
        "The expansion of a growing colonial population into the interior, which threatened "
        "existing trade networks and American Indian autonomy",
        "An imperial effort to raise revenue from the settled colonies after a costly war",
        "A native effort to end trade with Europeans and rely on other suppliers",
        "A French plan to move settlers eastward toward the coastal colonies",
        "An agreement between empires to leave the interior unsettled by either side"],
      ans=0,
      why="KC-3.1.I.A describes the growing population of the British colonies expanding into "
          "the interior of North America and threatening French-Indian trade networks and "
          "American Indian autonomy; surveying ground for farms while noting existing trade "
          "routes is that expansion in operation. Revenue-raising belongs to what KC-3.1.I.B "
          "says the war's expense set the stage for, and the remaining options reverse the "
          "direction of movement or assert an agreement the framework does not."),

 dict(q="Using the table of hypothetical population figures, which claim does the record "
        "support?",
      table=_T_POP,
      choices=[
        "Both the colonial total and the number in the interior districts rise at every step, "
        "and the interior grows as a share of the whole",
        "The colonial total rises while the number in the interior districts falls",
        "The number in the interior districts rises while the colonial total is unchanged",
        "The interior districts hold more people than the rest of the colonies by the third "
        "decade",
        "Both figures are unchanged across the three decades shown"],
      ans=0,
      why="Read from the table alone: both columns rise at every step and the interior share "
          "of the total rises as well, while the interior never approaches the size of the "
          "whole. That combination is what KC-3.1.I.A describes when it makes the GROWING "
          "population of the British colonies the thing that expanded into the interior and "
          "threatened French-Indian trade networks and American Indian autonomy."),

 dict(q="Using the table of hypothetical accounts, which reading is supported by the figures "
        "before and after the war?",
      table=_T_EXPENSE,
      choices=[
        "The cost of maintaining forces and the territory administered both rise sharply while "
        "the revenue raised in the colonies barely moves",
        "Revenue raised in the colonies rises faster than the cost of maintaining forces",
        "The territory administered falls while costs rise",
        "All three heads of account rise by about the same proportion",
        "Costs and revenue both fall after the war"],
      ans=0,
      why="Read from the table alone: two heads of account multiply several times over while "
          "the third moves by a small fraction of itself. A gap of that shape is what "
          "KC-3.1.I.B means by a major expansion of territorial holdings won at tremendous "
          "expense, setting the stage for imperial efforts to raise revenue and consolidate "
          "control over the colonies."),

 dict(q="Using the table of hypothetical records of native groups, what does the record show "
        "about trading and contesting settlement?",
      table=_T_NATIVE,
      choices=[
        "Most groups are recorded as doing both at once, so trading with Europeans and "
        "contesting settlement are not alternatives",
        "No group is recorded as doing both at once",
        "Every group is recorded as continuing to trade",
        "Every group is recorded as accepting colonists' settlement",
        "Groups that continued trading are the ones that did not contest settlement"],
      ans=0,
      why="Read from the table alone: three of the four rows record both continued trade and "
          "contested settlement, and the one group not recorded as trading still contested "
          "settlement, so no row supports treating the two as alternatives. That is exactly "
          "KC-3.1.I.C's claim that native groups sought to BOTH continue trading with "
          "Europeans AND resist the encroachments of colonists on tribal lands."),

 dict(q="Sorting the framework's sentences by the reasoning process this topic practises, which "
        "of the following does KC-3.1.I.A supply?",
      choices=[
        "A cause of the intensifying rivalry, namely colonial population growth pressing into "
        "the interior",
        "An effect of the British victory, namely opposition to restrictions on westward "
        "movement",
        "An effect of the war's expense, namely imperial efforts to raise revenue",
        "A description of the terms on which the war was ended",
        "A statement about how national culture developed after the war"],
      ans=0,
      why="KC-3.1.I.A supplies the causal antecedent: rivalry intensified AS the growing "
          "population of the British colonies expanded into the interior. The two effects "
          "named among the distractors belong to KC-3.1.I.C and KC-3.1.I.B respectively, and "
          "neither peace terms nor national culture is the subject of KC-3.1.I.A. Sorting "
          "causes from effects is what Unit 3: Learning Objective B and this topic's assigned "
          "reasoning process ask for."),

 dict(q="What link does the framework draw between the fighting and the imperial policy that "
        "followed it?",
      choices=[
        "The tremendous expense of the victory set the stage for efforts to raise revenue and "
        "consolidate control over the colonies",
        "The territory Britain won paid for the war immediately, so no new policy was needed",
        "The victory persuaded imperial officials to loosen their control over the colonies",
        "The war was paid for by the colonies, so imperial policy afterwards concerned trade "
        "alone",
        "The framework treats the war and later imperial policy as unconnected"],
      ans=0,
      why="KC-3.1.I.B makes the connection in one clause: the expansion of territorial holdings "
          "came at tremendous expense, SETTING THE STAGE FOR imperial efforts to raise revenue "
          "and consolidate control over the colonies. Consolidation is the opposite of "
          "loosening control, and the sentence makes the expense Britain's rather than the "
          "colonies', so the war and the policy are connected rather than separate."),

 dict(q="A hypothetical treasury report, its author unnamed, sets out that a war has been won, "
        "that new territory must now be garrisoned, and that the sums borrowed to pay for it "
        "remain outstanding. Which framework claim does a document of this kind illustrate?",
      choices=[
        "That a major expansion of territorial holdings was achieved at tremendous expense",
        "That the war produced no change in the extent of territory held",
        "That the cost of the war fell mainly on the defeated power",
        "That imperial officials had decided to abandon the newly won territory",
        "That the colonies had already been granted representation in return for taxes"],
      ans=0,
      why="KC-3.1.I.B holds a gain and a cost together: Britain achieved a major expansion of "
          "its territorial holdings by defeating the French, BUT at tremendous expense. A "
          "record of new ground to garrison and debts still outstanding is that pairing. The "
          "framework asserts the expansion, places the expense on the victor, and says the "
          "expense set the stage for revenue efforts rather than for abandonment or for a "
          "grant of representation."),

 dict(q="When does KC-3.1.I.C place the attempts to prevent colonists from moving westward?",
      choices=[
        "After the British victory",
        "Before the rivalry between Britain and France had intensified",
        "During the war itself, as a measure of wartime discipline",
        "After the colonies had declared their independence",
        "The framework does not say when they occurred"],
      ans=0,
      why="KC-3.1.I.C opens with the words 'After the British victory', which places the "
          "attempts, the colonial opposition they generated, and the native groups' twin aims "
          "in the years following the war rather than before the rivalry described in "
          "KC-3.1.I.A, during the fighting, or after independence."),

 dict(q="The British victory produced opposition from two directions at once, according to "
        "KC-3.1.I.C. What were the two, and what did each object to?",
      choices=[
        "Colonists opposed imperial attempts to stop them moving westward, while native groups "
        "resisted colonists' encroachments on tribal lands",
        "Colonists opposed the loss of trade with the French, while native groups objected to "
        "the terms of the peace",
        "Colonists and native groups both objected to the same imperial restriction on "
        "westward movement",
        "Native groups opposed imperial attempts to stop colonists moving westward, while "
        "colonists resisted encroachments on tribal lands",
        "Neither group objected to anything the framework records"],
      ans=0,
      why="KC-3.1.I.C names two objections with different objects: imperial officials' attempts "
          "to prevent westward movement generated COLONIAL opposition, while NATIVE GROUPS "
          "resisted the encroachments of colonists on tribal lands. The anchor carries both "
          "clauses because one distractor exchanges the two parties and another collapses them "
          "into a single shared grievance."),

 dict(q="KC-3.1.I.A names the trade networks that colonial expansion threatened. Whose networks "
        "were they, and whose autonomy was at stake?",
      choices=[
        "French-Indian trade networks, and American Indian autonomy",
        "British-Indian trade networks, and French autonomy in the interior",
        "French-Indian trade networks, and the autonomy of the British colonial assemblies",
        "Spanish trade networks, and American Indian autonomy",
        "British colonial trade networks, and the autonomy of the French crown"],
      ans=0,
      why="KC-3.1.I.A names the threatened networks as French-Indian and the threatened "
          "autonomy as American Indian, in the same clause. The anchor carries both because "
          "each distractor keeps one term and swaps the other, which is the way this sentence "
          "is most often half-remembered."),

 dict(q="A hypothetical trader's account, its author unnamed, records that goods once carried "
        "along one set of paths now move along another because farms have been laid out across "
        "the old route. Which framework claim does this illustrate?",
      choices=[
        "That colonial expansion into the interior threatened existing trade networks",
        "That the colonies had begun to raise their own revenue for imperial defence",
        "That imperial officials had succeeded in preventing colonists from moving westward",
        "That native groups had ended their trade with Europeans",
        "That Britain had lost territory to France in the interior"],
      ans=0,
      why="KC-3.1.I.A states that the growing population of the British colonies expanded into "
          "the interior of North America, threatening French-Indian trade networks and "
          "American Indian autonomy; settlement cutting an established route is that threat in "
          "operation. KC-3.1.I.C says the attempts to prevent westward movement generated "
          "opposition rather than succeeded, and says native groups continued trading; "
          "KC-3.1.I.B says Britain gained territory rather than lost it."),

 dict(q="The framework prints a list of optional sources for this topic and adds a caveat about "
        "them. What does the caveat say?",
      choices=[
        "The listed sources are not required course content, and no exam question requires "
        "students to have studied those particular sources",
        "The listed sources are required reading for every student taking the course",
        "The listed sources replace the key concepts as the content for this topic",
        "The listed sources are the only evidence an exam answer may use",
        "The listed sources are drawn from a period the unit does not cover"],
      ans=0,
      why="The optional-sources paragraph on this topic page states that the sources are not "
          "required AP course content and that none of the AP Exam questions require students "
          "to have studied these specific sources. That is why the content of this topic is "
          "carried by KC-3.1.I.A, KC-3.1.I.B and KC-3.1.I.C together with Unit 3: Learning "
          "Objective B, and not by the source list."),

 dict(q="Which of the following does the framework NOT assert about the war and its outcome?",
      choices=[
        "That Britain won its territorial gains cheaply",
        "That Britain defeated France",
        "That Britain's territorial holdings expanded",
        "That the victory was followed by attempts to prevent westward movement",
        "That the competition preceding the war involved American Indians as well as two "
        "European powers"],
      ans=0,
      why="KC-3.1.I.B says the expansion of territorial holdings came at TREMENDOUS EXPENSE, "
          "so a cheap victory is the one claim among the five the framework contradicts. The "
          "other four are stated directly: KC-3.1.I gives the defeat of France and names the "
          "three competing parties, KC-3.1.I.B gives the expansion, and KC-3.1.I.C gives the "
          "attempts that followed the victory."),

 dict(q="Comparing what the war settled with what it left unsettled, which statement follows "
        "from the framework's account?",
      choices=[
        "It settled which European power held the territory, while leaving the question of who "
        "would settle the interior in dispute",
        "It settled both which European power held the territory and who would settle the "
        "interior",
        "It settled neither question, since the framework describes no change in territorial "
        "holdings",
        "It settled who would settle the interior, while leaving the European claim in dispute",
        "It settled the question of colonial revenue, which had been the cause of the fighting"],
      ans=0,
      why="KC-3.1.I.B gives the settled question, a major expansion of British territorial "
          "holdings achieved by defeating the French, and KC-3.1.I.C gives the unsettled one, "
          "with colonists opposing restrictions on westward movement and native groups "
          "resisting encroachments on tribal lands. The anchor carries both clauses because "
          "one distractor exchanges the settled and unsettled halves. Revenue is what "
          "KC-3.1.I.B says the war's expense set the stage for, not its cause."),

 dict(q="A hypothetical petition, its author unnamed, asks an imperial governor to lift an "
        "order that forbids families from taking up land beyond the mountains. Which framework "
        "claim does such a request illustrate?",
      choices=[
        "That imperial officials' attempts to prevent colonists from moving westward generated "
        "colonial opposition",
        "That colonists welcomed imperial restrictions on westward movement",
        "That native groups petitioned for an end to European trade",
        "That imperial officials encouraged settlement beyond the mountains",
        "That the colonies were content with the revenue measures that followed the war"],
      ans=0,
      why="KC-3.1.I.C states that after the British victory, imperial officials' attempts to "
          "prevent colonists from moving westward generated colonial opposition; a request to "
          "lift such an order is that opposition expressed. The same sentence says native "
          "groups sought to continue trading, and it describes officials preventing rather "
          "than encouraging settlement."),

 dict(q="Which single statement pairs a cause of the war with an effect of it, as Unit 3's "
        "Learning Objective B asks?",
      choices=[
        "Colonial population pressing into the interior helped bring on the fighting, and the "
        "cost of winning it set the stage for imperial efforts to raise revenue",
        "Imperial efforts to raise revenue helped bring on the fighting, and colonial "
        "population growth followed from it",
        "The defeat of France was both the cause and the effect of the fighting",
        "Native resistance to encroachment caused the fighting, and the fighting ended it",
        "The framework names causes for the war but no effects"],
      ans=0,
      why="KC-3.1.I.A supplies the cause, colonial population expanding into the interior as "
          "rivalry intensified, and KC-3.1.I.B supplies the effect, tremendous expense setting "
          "the stage for imperial efforts to raise revenue and consolidate control. The "
          "leading distractor exchanges the two, which is why the anchor carries both clauses; "
          "Unit 3: Learning Objective B asks for causes AND effects, so the last option fails "
          "on the objective itself."),

 dict(q="Taken together, what do the framework's sentences on this topic establish about the "
        "war's place in the period?",
      choices=[
        "A contest among three parties over advantage in North America was resolved in "
        "Britain's favour at great cost, and the settlement it produced left both colonists "
        "and native groups with grievances",
        "A contest between two European powers was resolved cheaply and left no grievances "
        "behind it",
        "A contest that Britain lost, after which French officials tried to restrict colonial "
        "settlement",
        "A contest over colonial revenue that ended when the colonies agreed to pay for their "
        "own defence",
        "A contest whose outcome the framework leaves open"],
      ans=0,
      why="KC-3.1.I names three competing parties and Britain's victory, KC-3.1.I.B gives the "
          "tremendous expense, and KC-3.1.I.C gives the grievances that followed on both "
          "sides, with colonial opposition to restrictions on westward movement and native "
          "resistance to encroachment. A cheap victory, a British defeat, a revenue settlement "
          "and an open outcome each contradict one of those three sentences."),
]
