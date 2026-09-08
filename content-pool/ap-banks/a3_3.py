# AP U.S. HISTORY 3.3 Taxation Without Representation
# Title copied verbatim from US_HISTORY_topics.json.
# Unit 3, Period 3: 1754 to 1800. Suggested skill 2.A, identify a source's point of view,
# purpose, historical situation, and/or audience. Reasoning process printed for this
# topic: Causation.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 3: Learning Objective C
#       Explain how British colonial policies regarding North America led to the
#       Revolutionary War.
#
#   THEMATIC FOCUS: America in the World (WOR)
#       Diplomatic, economic, cultural, and military interactions between empires, nations,
#       and peoples shape the development of America and America's increasingly important
#       role in the world.
#
#   KC-3.1.II.A  The imperial struggles of the mid-18th century, as well as new British
#                efforts to collect taxes without direct colonial representation or consent
#                and to assert imperial authority in the colonies, began to unite the
#                colonists against perceived and real constraints on their economic
#                activities and political rights.
#   KC-3.1.II.B  Colonial leaders based their calls for resistance to Britain on arguments
#                about the rights of British subjects, the rights of the individual, local
#                traditions of self-rule, and the ideas of the Enlightenment.
#   KC-3.1.II.C  The effort for American independence was energized by colonial leaders
#                such as Benjamin Franklin, as well as by popular movements that included
#                the political activism of laborers, artisans, and women.
#   KC-3.1.II.D  In the face of economic shortages and the British military occupation of
#                some regions, men and women mobilized in large numbers to provide financial
#                and material support to the Patriot movement.
#
# WHAT IS NOT KEYED, DELIBERATELY. This topic page also carries an OPTIONAL SOURCES list
# (a Stamp Act cartoon, a Revere print, the Declaration and Resolves, the Declaratory Act,
# the Declaration of Rights and Grievances, committee minutes, essays and speeches by
# Adams, Dickinson, Hancock, Henry and Warren, and material on Abigail Adams, Crispus
# Attucks, the Daughters of Liberty, the Edenton tea party, the Green Mountain Boys and the
# Sons of Liberty). The CED says of that list, in its own words, that these "are not
# required AP course content" and that "None of the AP Exam questions require students to
# have studied these specific sources." So no key here turns on any of them; the verifier
# asserts it. Benjamin Franklin and the Patriot movement ARE keyed, because KC-3.1.II.C and
# KC-3.1.II.D name them in the required content itself.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table= and
# every figure in them is explicitly hypothetical, since the CED prints no data here.
# PROSE ONLY: no LaTeX; a span of years is written "1754 to 1800", never with a hyphen.
# FIVE choices (A-E). Every invented source is marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("3.3", "Taxation Without Representation", 3)

_T_SOURCING = dict(
    headers=["Observation about a hypothetical pamphlet",
             "Sourcing question the observation answers"],
    rows=[["Its writer sat in a colonial assembly and had spoken there against the new duties",
           "Point of view"],
          ["It was printed in order to persuade readers to refuse the new duties",
           "Purpose"],
          ["It appeared in the months just after the new duties were announced",
           "Historical situation"],
          ["It was sold cheaply in a port town where sailors and dockworkers gathered",
           "Audience"]])

_T_GROUNDS = dict(
    headers=["Ground appealed to (hypothetical tally)", "Pamphlets in which it appears"],
    rows=[["Rights of British subjects", "31"],
          ["Local traditions of self-rule", "24"],
          ["Rights of the individual", "19"],
          ["Ideas of the Enlightenment", "12"]])

_T_SUPPORT = dict(
    headers=["Group in a hypothetical district return", "Households contributing money",
             "Households contributing goods"],
    rows=[["Laborers", "120", "150"],
          ["Artisans", "90", "70"],
          ["Households headed by women", "60", "110"],
          ["Merchants", "30", "25"]])

QUESTIONS = [

 dict(q="Unit 3's Learning Objective C states what students should be able to explain about "
        "British colonial policies. Which statement is it?",
      choices=[
        "Explain how British colonial policies regarding North America led to the "
        "Revolutionary War",
        "Explain how colonial resistance changed British policy toward North America",
        "Describe the taxes Parliament imposed on the colonies in the order they were passed",
        "Compare British colonial policy in North America with French colonial policy",
        "Explain how the colonies financed their own government before the war"],
      ans=0,
      why="Unit 3: Learning Objective C reads 'Explain how British colonial policies regarding "
          "North America led to the Revolutionary War.' The objective runs from policy to war, "
          "so an objective running the other way reverses it, and the framework asks for "
          "explanation rather than a list of statutes or a comparison of empires."),

 dict(q="Which skill statement is printed beside this topic's title as the one students should "
        "practise here?",
      choices=[
        "Identify a source's point of view, purpose, historical situation, and audience",
        "Explain a historical concept, development, or process",
        "Identify and describe a claim or argument in a source",
        "Support an argument using specific and relevant evidence",
        "Identify patterns among or connections between historical developments and processes"],
      ans=0,
      why="Skill 2.A, identify a source's point of view, purpose, historical situation, and "
          "audience, is printed on this topic page. It is a sourcing skill rather than an "
          "argument skill, which is why the four alternatives, skills 1.B, 3.A, 6.B and 5.A "
          "from other pages of this unit, do not fit a topic whose learning objective is "
          "Unit 3: Learning Objective C on how British policy led to war."),

 dict(q="The unit's topic table assigns each topic a reasoning process. Which does it assign "
        "here?",
      choices=[
        "Causation",
        "Comparison",
        "Continuity and Change",
        "Contextualization",
        "Sourcing and Situation"],
      ans=0,
      why="The unit's topic table assigns Causation to this topic, which matches Unit 3: "
          "Learning Objective C asking how British colonial policies LED TO the Revolutionary "
          "War and matches KC-3.1.II.A, which traces what began to unite the colonists. "
          "Comparison and Continuity and Change are assigned to other topics of this unit, "
          "while Contextualization and Sourcing and Situation are skill categories."),

 dict(q="KC-3.1.II.A names more than one thing that began to unite the colonists. Which set "
        "does the framework name?",
      choices=[
        "The imperial struggles of the mid-18th century, new British efforts to collect taxes "
        "without direct colonial representation or consent, and efforts to assert imperial "
        "authority in the colonies",
        "New British efforts to collect taxes, and nothing besides",
        "The imperial struggles of the mid-18th century, and a decision to grant the colonies "
        "seats in Parliament",
        "Efforts to assert imperial authority, and a British withdrawal from colonial trade "
        "regulation",
        "A colonial demand for new taxes, and Parliament's refusal to impose them"],
      ans=0,
      why="KC-3.1.II.A names three things together: the imperial struggles of the mid-18th "
          "century, AS WELL AS new British efforts to collect taxes without direct colonial "
          "representation or consent AND to assert imperial authority in the colonies. "
          "Reducing the list to taxation alone drops two of the three, and the remaining "
          "options substitute a grant of seats, a withdrawal or a colonial demand that the "
          "sentence does not contain."),

 dict(q="KC-3.1.II.A qualifies the new British efforts to collect taxes with a phrase about "
        "how they were imposed. What is that phrase?",
      choices=[
        "Without direct colonial representation or consent",
        "With the consent of the colonial assemblies but without representation in Parliament",
        "With direct colonial representation but without consent",
        "After a vote of the colonists themselves",
        "Only in the colonies that had asked to be taxed"],
      ans=0,
      why="KC-3.1.II.A describes new British efforts to collect taxes WITHOUT DIRECT COLONIAL "
          "REPRESENTATION OR CONSENT. Both terms are denied by that phrase, so a version "
          "granting either representation or consent keeps one half of what the sentence "
          "withholds, and the framework records no colonial vote or request."),

 dict(q="According to KC-3.1.II.A, what were the colonists beginning to unite against?",
      choices=[
        "Perceived and real constraints on their economic activities and political rights",
        "Constraints on their economic activities alone, since political rights were not yet "
        "at issue",
        "Constraints they believed in but which did not in fact exist",
        "Constraints imposed by the colonial assemblies rather than by Britain",
        "Constraints on religious worship imposed from London"],
      ans=0,
      why="KC-3.1.II.A ends with the colonists uniting against perceived AND REAL constraints "
          "on their ECONOMIC ACTIVITIES AND POLITICAL RIGHTS. The sentence carries two pairs "
          "at once, so an option dropping political rights, or reading 'perceived' as though "
          "it excluded 'real', keeps half of each; the constraints are British and the "
          "subjects named are economic and political rather than religious."),

 dict(q="KC-3.1.II.A says the colonists BEGAN TO UNITE rather than that they were united. What "
        "does that wording establish?",
      choices=[
        "That the framework describes a process getting under way in this period rather than a "
        "unity already achieved",
        "That the colonists never united at any point",
        "That unity was complete before the new British efforts began",
        "That unity was confined to a single colony",
        "That the framework treats colonial unity as unimportant"],
      ans=0,
      why="KC-3.1.II.A's phrase 'began to unite the colonists' marks the start of a process, "
          "which is why the sentence sits under Unit 3: Learning Objective C on how British "
          "policies LED TO war. A unity already complete would leave the sentence nothing to "
          "begin, and the framework treats the process as consequential rather than confining "
          "it to one colony or dismissing it."),

 dict(q="KC-3.1.II.B lists the arguments colonial leaders based their calls for resistance on. "
        "Which set gives all of them?",
      choices=[
        "The rights of British subjects, the rights of the individual, local traditions of "
        "self-rule, and the ideas of the Enlightenment",
        "The rights of British subjects, the rights of the individual, and the authority of "
        "the Crown",
        "Local traditions of self-rule, the ideas of the Enlightenment, and the precedents of "
        "Roman law",
        "The rights of the individual and the ideas of the Enlightenment alone",
        "The rights of British subjects and a claim to seats in Parliament"],
      ans=0,
      why="KC-3.1.II.B names exactly four grounds: arguments about the rights of British "
          "subjects, the rights of the individual, local traditions of self-rule, and the "
          "ideas of the Enlightenment. The authority of the Crown, Roman law and a claim to "
          "seats in Parliament are not among them, and two of the options drop grounds the "
          "sentence includes."),

 dict(q="Two of the grounds KC-3.1.II.B names are easily run together. What distinguishes the "
        "rights of British subjects from the rights of the individual?",
      choices=[
        "The first is a claim to what any subject of the British constitution was owed; the "
        "second is a claim about persons as such, which the framework lists separately",
        "They are the same claim, stated twice in the sentence for emphasis",
        "The first is a claim about persons as such and the second a claim about subjects of "
        "the British constitution",
        "The first belongs to the Enlightenment and the second to local tradition",
        "Neither is a ground the framework names"],
      ans=0,
      why="KC-3.1.II.B lists the rights of British subjects and the rights of the individual as "
          "two of its four grounds, in that order, so the framework treats them as distinct "
          "rather than as one claim repeated. The anchor carries both halves because one "
          "distractor is this same distinction with the two terms exchanged, and the sentence "
          "keeps the Enlightenment and local traditions of self-rule as separate grounds again."),

 dict(q="One of KC-3.1.II.B's grounds appeals to colonial practice rather than to a theory of "
        "rights. Which is it?",
      choices=[
        "Local traditions of self-rule",
        "The ideas of the Enlightenment",
        "The rights of the individual",
        "The rights of British subjects",
        "The authority of Parliament over colonial trade"],
      ans=0,
      why="Of the four grounds KC-3.1.II.B names, local traditions of self-rule is the one that "
          "appeals to what colonists had actually been doing rather than to a doctrine about "
          "what is owed. The Enlightenment and the two kinds of rights are the other three "
          "grounds in the same sentence, and parliamentary authority over trade is not among "
          "them at all."),

 dict(q="KC-3.1.II.B names an eighteenth-century body of thought among the grounds for "
        "resistance. Which does the framework name, and what does naming it establish?",
      choices=[
        "The ideas of the Enlightenment, which places the colonial arguments alongside a body "
        "of thought developing outside the colonies as well as within them",
        "The ideas of the Enlightenment, which the framework treats as the only ground "
        "colonial leaders used",
        "The doctrines of the medieval church, which supplied the language of resistance",
        "The writings of classical antiquity, which the framework names in place of any "
        "contemporary thought",
        "No body of thought at all, since the framework confines the arguments to local "
        "practice"],
      ans=0,
      why="KC-3.1.II.B names the ideas of the Enlightenment as one of four grounds, so it is "
          "present but not alone; the other three are the rights of British subjects, the "
          "rights of the individual, and local traditions of self-rule. Medieval doctrine and "
          "classical antiquity are absent from the sentence, and the sentence plainly does "
          "name a body of thought."),

 dict(q="KC-3.1.II.C describes what energized the effort for American independence. Which "
        "statement matches the framework?",
      choices=[
        "It was energized by colonial leaders and also by popular movements",
        "It was energized by colonial leaders alone, with no popular involvement",
        "It was energized by popular movements alone, with no leadership",
        "It was energized by British officials sympathetic to the colonial cause",
        "It was energized by the colonial assemblies acting without any wider participation"],
      ans=0,
      why="KC-3.1.II.C states that the effort for American independence was energized by "
          "colonial leaders such as Benjamin Franklin, AS WELL AS by popular movements that "
          "included the political activism of laborers, artisans, and women. The sentence "
          "holds both together, so keeping only one side of it drops half; British officials "
          "and the assemblies acting alone are not what it names."),

 dict(q="KC-3.1.II.C names the people whose political activism the popular movements included. "
        "Which set does it name?",
      choices=[
        "Laborers, artisans, and women",
        "Laborers, merchants, and clergy",
        "Artisans, women, and colonial governors",
        "Merchants, planters, and lawyers",
        "Soldiers of the regular army and their officers"],
      ans=0,
      why="KC-3.1.II.C names popular movements that included the political activism of "
          "laborers, artisans, and women. Merchants, clergy, governors, planters, lawyers and "
          "regular soldiers are not in that list, and two of the wrong options keep one or two "
          "of the framework's three names while replacing the rest."),

 dict(q="KC-3.1.II.C names one colonial leader as an example. Which leader does the framework "
        "name there, and how does it introduce him?",
      choices=[
        "Benjamin Franklin, introduced with the words 'such as', so he stands as an example "
        "rather than as the only leader",
        "Benjamin Franklin, introduced as the sole leader of the independence effort",
        "A leader whose name the framework deliberately withholds",
        "Several leaders named together, of whom Benjamin Franklin is the last",
        "No leader at all, since the sentence names only popular movements"],
      ans=0,
      why="KC-3.1.II.C reads that the effort was energized by colonial leaders SUCH AS Benjamin "
          "Franklin, as well as by popular movements. The phrase 'such as' makes him an "
          "instance of a larger group rather than the whole of it, so both the sole-leader and "
          "the no-leader readings misstate the sentence."),

 dict(q="KC-3.1.II.D names the conditions in which men and women mobilized. Which pair does "
        "the framework name?",
      choices=[
        "Economic shortages, and the British military occupation of some regions",
        "Economic prosperity, and the withdrawal of British forces from every region",
        "Economic shortages, and a British offer of representation in Parliament",
        "The British military occupation of every region, and a famine across the colonies",
        "A dispute among the colonies themselves, with no British presence involved"],
      ans=0,
      why="KC-3.1.II.D opens 'In the face of economic shortages and the British military "
          "occupation of some regions'. The framework says SOME regions rather than every "
          "region, and names shortages rather than prosperity, so each alternative alters one "
          "of the two conditions the sentence states."),

 dict(q="How many people does KC-3.1.II.D say mobilized, and who were they?",
      choices=[
        "Men and women, mobilizing in large numbers",
        "A small circle of leaders, acting on behalf of the rest",
        "Men only, since the framework treats mobilization as a military matter",
        "Women only, since the framework assigns the men to the army",
        "The colonial assemblies, acting in their official capacity"],
      ans=0,
      why="KC-3.1.II.D states that men and women mobilized IN LARGE NUMBERS to provide "
          "financial and material support to the Patriot movement. The sentence names both "
          "sexes and a large scale, which is what rules out a small circle, a single sex, or "
          "action confined to the assemblies; KC-3.1.II.C makes the same point by naming "
          "popular movements alongside leaders."),

 dict(q="What kind of support does KC-3.1.II.D say the mobilization provided, and to whom?",
      choices=[
        "Financial and material support, provided to the Patriot movement",
        "Financial support only, provided to the Patriot movement",
        "Material support only, provided to the British forces in occupied regions",
        "Political support in the assemblies, rather than support of any material kind",
        "Support to whichever side held the region at the time"],
      ans=0,
      why="KC-3.1.II.D says men and women mobilized to provide FINANCIAL AND MATERIAL support "
          "to the PATRIOT MOVEMENT. The anchor carries both the kind of support and its "
          "recipient, because the distractors each keep one and alter the other."),

 dict(q="A hypothetical pamphlet, its author unnamed, argues that a duty laid on a colony "
        "without the consent of its own assembly is unlawful because the colonists have "
        "governed themselves in this way for generations. Which of KC-3.1.II.B's grounds is "
        "the pamphlet using?",
      choices=[
        "Local traditions of self-rule",
        "The ideas of the Enlightenment",
        "The rights of the individual considered apart from any community",
        "The authority of the Crown over its overseas possessions",
        "The precedents of Roman law"],
      ans=0,
      why="KC-3.1.II.B names local traditions of self-rule among the four grounds colonial "
          "leaders used, and an argument resting on generations of governing themselves is "
          "that ground rather than a claim about individuals as such or a doctrine drawn from "
          "outside. The Crown's authority and Roman law are not grounds the sentence names."),

 dict(q="Applying the sourcing skill this topic practises, which observation about a "
        "hypothetical broadside answers the question of PURPOSE rather than of point of view?",
      choices=[
        "It was printed and distributed in order to persuade readers to stop buying certain "
        "imported goods",
        "Its writer was a merchant whose own trade had been damaged by the new duties",
        "Its writer had been imprisoned once before for a similar publication",
        "Its writer belonged to a family that had held colonial office for two generations",
        "Its writer had studied in London and admired the British constitution"],
      ans=0,
      why="Skill 2.A distinguishes a source's purpose, which is the objective its creator "
          "pursued, from its point of view, which is what about the creator's own background "
          "shaped what they said. Persuading readers to stop buying goods states an objective; "
          "the other four state facts about the writer. KC-3.1.II.B is the content such a "
          "broadside would illustrate, since it names the grounds on which calls for "
          "resistance were based."),

 dict(q="Still applying the sourcing skill, which observation about a hypothetical circular "
        "letter answers the question of HISTORICAL SITUATION?",
      choices=[
        "It was written in the weeks after new duties were announced and while troops were "
        "quartered in the town",
        "It was addressed to the freeholders of the county",
        "Its writer had sat in the assembly for ten years",
        "It was written in order to secure signatures for a non-importation agreement",
        "It was printed on a press that its writer owned"],
      ans=0,
      why="Skill 2.A separates historical situation, meaning what was happening at the time and "
          "in the place the source was created, from audience, point of view and purpose. The "
          "arrival of new duties and the quartering of troops describe that setting; the other "
          "four observations name a recipient, the writer's background, an objective, and a "
          "physical detail. KC-3.1.II.A supplies the setting itself, in the new efforts to "
          "collect taxes and to assert imperial authority."),

 dict(q="Using the table of observations about a hypothetical pamphlet, which observation is "
        "the one about AUDIENCE?",
      table=_T_SOURCING,
      choices=[
        "The observation about where and how cheaply the pamphlet was sold",
        "The observation about the writer having spoken against the duties in an assembly",
        "The observation about the pamphlet being printed to persuade readers",
        "The observation about when the pamphlet appeared",
        "None of the observations concerns audience"],
      ans=0,
      why="Read from the table alone: exactly one row is marked as answering the question of "
          "audience, and it is the row about where and how cheaply the pamphlet was sold, "
          "since who could buy it is who it was aimed at. The other three rows are marked "
          "point of view, purpose and historical situation, which are the remaining categories "
          "of skill 2.A as printed on this topic page beside Unit 3: Learning Objective C. A "
          "pamphlet of this kind would carry the calls for resistance KC-3.1.II.B describes."),

 dict(q="Using the table of hypothetical pamphlet tallies, what does the record show about the "
        "grounds of colonial argument?",
      table=_T_GROUNDS,
      choices=[
        "All four of the grounds the framework names appear, though in unequal numbers",
        "Only one of the four grounds appears at all",
        "The four grounds appear in equal numbers",
        "The ground appealed to least often is local traditions of self-rule",
        "Enlightenment ideas appear more often than any other ground"],
      ans=0,
      why="Read from the table alone: four grounds are tallied, every tally is above zero, and "
          "no two tallies are equal, so all four appear in unequal numbers; the smallest tally "
          "belongs to Enlightenment ideas rather than to local traditions of self-rule, and it "
          "is the smallest rather than the largest. Those four grounds are exactly the ones "
          "KC-3.1.II.B names as the basis of colonial leaders' calls for resistance."),

 dict(q="Using the table of hypothetical district returns, which conclusion does the record "
        "support?",
      table=_T_SUPPORT,
      choices=[
        "Every group listed contributed in both forms, so support was neither confined to one "
        "group nor of a single kind",
        "Only one group contributed anything at all",
        "Every group contributed money but none contributed goods",
        "Merchants contributed more than any other group in both forms",
        "Contributions of goods exceeded contributions of money in every group"],
      ans=0,
      why="Read from the table alone: every row records contributions under both headings, no "
          "row is empty, and the largest totals do not belong to the merchants, while in two "
          "of the four rows the money column exceeds the goods column. KC-3.1.II.D describes "
          "men and women mobilizing in large numbers to provide FINANCIAL AND MATERIAL support "
          "to the Patriot movement, and KC-3.1.II.C names laborers, artisans, and women among "
          "those active."),

 dict(q="This topic sits under the thematic focus the framework calls America in the World. "
        "What does that focus statement assert?",
      choices=[
        "Diplomatic, economic, cultural, and military interactions between empires, nations, "
        "and peoples shape the development of America and its role in the world",
        "Debates about the role of government shape policy, institutions, parties, and the "
        "rights of citizens",
        "Social categories, roles, and practices are created, maintained, challenged, and "
        "transformed throughout American history",
        "Push and pull factors shape immigration to and migration within America",
        "Creative expression, demographic change, philosophy, and religious beliefs shape "
        "national, regional, and group cultures"],
      ans=0,
      why="The America in the World thematic focus printed on this topic page states that "
          "diplomatic, economic, cultural, and military interactions between empires, nations, "
          "and peoples shape the development of America and America's increasingly important "
          "role in the world. KC-3.1.II.A's imperial struggles and new British efforts are an "
          "interaction of exactly that kind. The other four are the framework's thematic "
          "focuses for politics and power, social structures, migration and regional culture, "
          "printed on other topic pages of this unit."),

 dict(q="How do the framework's sentences connect British policy to the war Unit 3's Learning "
        "Objective C names?",
      choices=[
        "New efforts to tax without representation or consent and to assert imperial authority "
        "began to unite colonists against constraints, and colonial leaders and popular "
        "movements then energized the effort for independence",
        "The war began before any new British efforts to collect taxes, so policy followed the "
        "fighting rather than preceding it",
        "The colonists united first and British policy was framed in response to them",
        "The framework treats British policy and the war as unconnected developments",
        "British policy united the colonists but no movement for independence followed from it"],
      ans=0,
      why="KC-3.1.II.A supplies the first link, with new British efforts beginning to unite the "
          "colonists against perceived and real constraints, and KC-3.1.II.C supplies the "
          "second, with leaders and popular movements energizing the effort for American "
          "independence. That chain is what Unit 3: Learning Objective C means by British "
          "policies leading to the Revolutionary War, so reversing the order or breaking the "
          "chain contradicts it."),

 dict(q="Which of the following does the framework NOT assert about the resistance to British "
        "policy?",
      choices=[
        "That colonial leaders confined their arguments to a single ground",
        "That colonial leaders argued from the rights of British subjects",
        "That the effort for independence was energized by popular movements as well as by "
        "leaders",
        "That men and women mobilized in large numbers",
        "That the arguments included the ideas of the Enlightenment"],
      ans=0,
      why="KC-3.1.II.B names four grounds together, so confinement to a single ground is the "
          "one claim of the five the framework contradicts. The rights of British subjects and "
          "the ideas of the Enlightenment are two of those four grounds, KC-3.1.II.C names "
          "popular movements alongside leaders, and KC-3.1.II.D reports mobilization in large "
          "numbers."),

 dict(q="What is the difference between what KC-3.1.II.C describes and what KC-3.1.II.D "
        "describes?",
      choices=[
        "The first names who energized the effort for independence, while the second names "
        "what people did to sustain it under shortage and occupation",
        "The first names what people did under shortage and occupation, while the second names "
        "who energized the effort for independence",
        "Both sentences describe the arguments used to justify resistance",
        "Both sentences describe decisions taken by the colonial assemblies",
        "The first concerns British policy and the second concerns colonial trade"],
      ans=0,
      why="KC-3.1.II.C is about who energized the effort, naming colonial leaders such as "
          "Benjamin Franklin alongside popular movements of laborers, artisans, and women; "
          "KC-3.1.II.D is about what men and women did in the face of economic shortages and "
          "British military occupation, providing financial and material support to the "
          "Patriot movement. The anchor carries both clauses because the leading distractor is "
          "this same distinction with the two sentences exchanged."),

 dict(q="KC-3.1.II.A calls the constraints PERCEIVED AND REAL. What does that pairing do for "
        "the framework's account?",
      choices=[
        "It allows both that some constraints existed and that colonists also acted on "
        "constraints they believed in, without deciding every case one way",
        "It says the constraints were imaginary throughout",
        "It says every constraint the colonists named was in force",
        "It restricts the account to constraints on trade",
        "It removes the constraints from the explanation of what united the colonists"],
      ans=0,
      why="KC-3.1.II.A says the colonists began to unite against perceived AND REAL constraints "
          "on their economic activities and political rights. Holding both words keeps the "
          "sentence from claiming that every grievance was well founded and from claiming that "
          "none was, and the constraints remain the thing united against rather than being "
          "dropped from the explanation; the same clause names political rights as well as "
          "economic activity."),

 dict(q="A hypothetical resolution of a town meeting, its author unnamed, declares that the "
        "townsmen will buy no imported goods until a duty is repealed, and asks neighbouring "
        "towns to do the same. Which framework claim does an action of this kind illustrate?",
      choices=[
        "That new British efforts to collect taxes began to unite the colonists against "
        "constraints on their economic activities",
        "That colonial leaders argued from the precedents of Roman law",
        "That the British military occupation had ended in every region",
        "That the colonists had been granted direct representation in Parliament",
        "That popular movements played no part in the effort for independence"],
      ans=0,
      why="KC-3.1.II.A states that new British efforts to collect taxes without direct colonial "
          "representation or consent began to unite the colonists against perceived and real "
          "constraints on their economic activities and political rights, and a town agreeing "
          "with its neighbours to refuse imported goods is that uniting in action. KC-3.1.II.C "
          "says popular movements did play a part, and neither Roman law, an end to "
          "occupation, nor a grant of representation appears in the required content."),

 dict(q="Taken together, what do this topic's four sentences establish about how resistance "
        "took shape?",
      choices=[
        "Imperial struggles and new taxes imposed without representation or consent began to "
        "unite colonists, who argued from four distinct grounds, and both leaders and ordinary "
        "people then sustained the effort",
        "A single tax united the colonists at once, and the argument against it rested on one "
        "ground alone",
        "Resistance was organised by leaders without any wider participation, and rested "
        "wholly on Enlightenment ideas",
        "Resistance was a popular movement with no leaders, and rested wholly on local "
        "traditions of self-rule",
        "Resistance began only after the fighting had started, so no argument preceded it"],
      ans=0,
      why="KC-3.1.II.A gives the imperial struggles and the new taxes and says they BEGAN to "
          "unite the colonists, KC-3.1.II.B gives four grounds rather than one, and "
          "KC-3.1.II.C and KC-3.1.II.D give both leaders and ordinary men and women. Each "
          "rejected option collapses one of those three sentences into a single cause, a "
          "single ground, or a single kind of participant."),
]
