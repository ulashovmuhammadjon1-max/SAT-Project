# AP WORLD HISTORY: MODERN 9.3 Technological Advances: Debates About the
# Environment After 1900
# CED effective Fall 2026 (Course Framework V.1), Unit 9 Globalization,
# c. 1900 to the present. Thematic focus: Humans and the Environment (ENV).
# Reasoning process: Causation.
#
# Learning Objective: Unit 9 Learning Objective C -- explain the causes and
# effects of environmental changes in the period from 1900 to present. Suggested
# skill 4.B, explain how a specific historical development or process is situated
# within a broader historical context. That skill is the shape of this bank: most
# items put a particular, local development in front of the student -- a district
# losing its trees, a basin drawing more water, a city's air -- and ask which of
# the framework's broader processes it belongs inside.
#
# HISTORICAL DEVELOPMENTS this topic prints, and the only sentences the keys
# below rest on:
#   KC-6.1.II.A  As human activity contributed to deforestation,
#                desertification, a decline in air quality, and increased
#                consumption of the world's supply of fresh water, humans
#                competed over these and other resources more intensely than
#                ever before.
#   KC-6.1.II.B  The release of greenhouse gases and pollutants into the
#                atmosphere contributed to debates about the nature and causes of
#                climate change.
# The CED prints NO illustrative examples on this page, so no item here turns on
# any, and none is invented to fill the space.
#
# READ KC-6.1.II.B EXACTLY, BECAUSE THIS IS THE MOST CONTESTED SENTENCE IN THE
# WHOLE COURSE. What the framework asserts is that the release of greenhouse
# gases and pollutants CONTRIBUTED TO DEBATES ABOUT the nature and causes of
# climate change. It asserts the releases and it asserts the debates. It does not
# itself settle what the nature or the causes of climate change are, and neither
# does this bank.
#
#   * NO key here states what causes climate change, or that it does not have a
#     cause, or that any particular account of it is correct or incorrect.
#   * NO key assigns responsibility for emissions to any country, industry,
#     government or group, and the emissions table deliberately names no real
#     state.
#   * NO key endorses or rejects any environmental policy.
#   * Items 9, 17, 23 and 28 exist to mark the boundary explicitly: each keys the
#     fact that the framework describes a DEBATE rather than a verdict, so a
#     student who has read the sentence carefully is rewarded and a student who
#     has read a position into it is not.
#
# This is the instruction in HISTORY_BRIEF.md and MISSION.md applied at its
# hardest point: recent history invites both strong general knowledge and live
# political disagreement, so stay on what the framework states and let contested
# questions stay contested rather than keying one side. A bank that keyed a
# position here would be teaching that position under the cover of an exam.
#
# KC-6.1.II.A IS FOUR CHANGES AND ONE CONSEQUENCE. The four are deforestation,
# desertification, a decline in air quality, and increased consumption of the
# world's supply of fresh water. The consequence is that humans competed over
# these and other resources MORE INTENSELY THAN EVER BEFORE. The framework says
# human activity CONTRIBUTED TO the four changes, not that it was their sole
# cause, and items 6, 14 and 21 hold that verb where the framework put it.
#
# DEDUPE NOTE. Topic 9.1 covers the technologies themselves, including energy
# technologies under KC-6.1.I.D and modified agriculture under KC-6.1.I.B; 9.2
# covers disease as an environmental factor; 9.5 covers the movements that
# protested the environmental and economic consequences of global integration
# under KC-6.3.II.C, so environmental MOVEMENTS belong there and appear here only
# as distractors. This module stays on the environmental changes themselves,
# their causes, and the competition and debates they produced.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT and none is attributed to a real person or document.
# TABLES are hypothetical, each states a whole and its parts, and every keyed
# conclusion is recomputed from the table alone. DATES are written "1950 to
# 1990", never with a hyphen.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("9.3", "Technological Advances: Debates About the Environment After 1900", 9)

_T_FOREST = dict(
    headers=["Period (hypothetical land survey of one region, thousands of square kilometres)",
             "Land surveyed",
             "Of that, under forest",
             "Of that, not under forest"],
    rows=[["1950", "800", "380", "420"],
          ["1970", "800", "300", "500"],
          ["1990", "800", "210", "590"]])

_T_WATER = dict(
    headers=["Period (hypothetical record of one river basin, billions of cubic metres)",
             "Fresh water withdrawn",
             "Of that, withdrawn for agriculture",
             "Of that, withdrawn for other uses"],
    rows=[["1950", "40", "30", "10"],
          ["1970", "72", "52", "20"],
          ["1990", "118", "82", "36"]])

_T_RELEASES = dict(
    headers=["Period (hypothetical index of recorded atmospheric releases, first period = 100)",
             "Total recorded releases",
             "Of that, from one group of states",
             "Of that, from all other states"],
    rows=[["1950", "100", "78", "22"],
          ["1970", "210", "140", "70"],
          ["1990", "360", "200", "160"]])

QUESTIONS = [

 dict(q="A district forestry officer's return of 1968 records that woodland cleared for cultivation and for timber over the preceding twenty years now exceeds the woodland remaining. This local record is best situated within which of this course's broader processes?",
   choices=[
     "Human activity contributing to deforestation during this period",
     "Human activity contributing to a decline in air quality during this period",
     "The release of greenhouse gases contributing to debates about climate change",
     "The spread of new modes of communication reducing the problem of distance",
     "The migration of former colonial subjects to imperial metropoles"],
   ans=0,
   why="KC-6.1.II.A states that human activity contributed to deforestation, desertification, a decline in air quality, and increased consumption of the world's supply of fresh water. A district record of woodland cleared for cultivation and timber is the first of those four named changes observed locally, and skill 4.B asks a student to situate a specific development inside the broader process it belongs to."),

 dict(q="According to this course, what did the four environmental changes it names lead humans to do?",
   choices=[
     "Compete over these and other resources more intensely than ever before",
     "Abandon the use of the resources concerned altogether",
     "Divide the world's resources equally among all states by agreement",
     "Cease all agricultural production in the affected regions",
     "Reverse each of the four changes within a single generation"],
   ans=0,
   why="KC-6.1.II.A states that as human activity contributed to deforestation, desertification, a decline in air quality, and increased consumption of the world's supply of fresh water, humans competed over these and other resources MORE INTENSELY THAN EVER BEFORE. Intensified competition is the consequence the framework's own sentence names."),

 dict(q="A hypothetical land survey divides one region's area into two parts in each period. Which conclusion does the table alone support?",
   table=_T_FOREST,
   choices=[
     "The area under forest fell in each period recorded, and the area not under forest rose correspondingly",
     "The area under forest rose in each period recorded",
     "The area not under forest fell in each period recorded",
     "Forest covered more than half of the region's area in every period recorded",
     "No forest remained in the region by the last period recorded"],
   ans=0,
   why="KC-6.1.II.A names deforestation among the changes to which human activity contributed. The survey is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier; the table records a change in land cover and attributes it to no one in particular."),

 dict(q="This course states that the release of greenhouse gases and pollutants into the atmosphere had a particular consequence. What does the framework say that consequence was?",
   choices=[
     "It contributed to debates about the nature and causes of climate change",
     "It settled the question of the nature and causes of climate change",
     "It had no bearing on any discussion of the climate",
     "It caused the deforestation of the world's remaining woodland",
     "It reduced the intensity of competition over the world's resources"],
   ans=0,
   why="KC-6.1.II.B states that the release of greenhouse gases and pollutants into the atmosphere CONTRIBUTED TO DEBATES ABOUT the nature and causes of climate change. The framework records the releases and the debates they contributed to; it does not itself settle what the nature or the causes are, and the key states exactly what the sentence states and no more."),

 dict(q="An agricultural inspector's note of 1975 reports that land at the edge of a dry region, cropped and grazed without rest for two decades, will no longer hold a crop and is turning to bare sand. Within this course's framework, the note documents",
   choices=[
     "desertification, one of the changes to which human activity contributed",
     "deforestation, one of the changes to which human activity contributed",
     "a decline in air quality, one of the changes to which human activity contributed",
     "the release of pollutants that contributed to debates about climate change",
     "the growth of commercial agriculture that sustained a growing population"],
   ans=0,
   why="KC-6.1.II.A names desertification among the four changes to which human activity contributed. Land at a dry margin worked without rest until it will no longer hold a crop is that change described in the field, and the framework distinguishes it from the other three it names in the same sentence."),

 dict(q="How does this course describe the role of human activity in the environmental changes it names?",
   choices=[
     "As having contributed to them, rather than as their only cause",
     "As having been their sole and only cause",
     "As having had no part in them whatever",
     "As having reversed them once they had begun",
     "As having been irrelevant to any change in the environment"],
   ans=0,
   why="KC-6.1.II.A states that human activity CONTRIBUTED TO deforestation, desertification, a decline in air quality, and increased consumption of the world's supply of fresh water. Contributed is the framework's own verb and it is weaker than sole causation and stronger than no part at all, so the key keeps it where the sentence puts it."),

 dict(q="A hypothetical record divides one river basin's withdrawals into two parts in each period. Which conclusion does the table alone support?",
   table=_T_WATER,
   choices=[
     "Total withdrawals rose in each period, and agriculture accounted for the largest part in every period",
     "Total withdrawals fell in each period after the first one recorded",
     "Withdrawals for other uses fell across the record",
     "Agriculture accounted for less than half of withdrawals in every period",
     "Agriculture's share of withdrawals rose across the record"],
   ans=0,
   why="KC-6.1.II.A names increased consumption of the world's supply of fresh water among the changes to which human activity contributed. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier; the last distractor is true of the quantity and false of the share, which is why the verifier separates the two."),

 dict(q="A hypothetical city engineer's report of 1959 attributes a persistent winter haze to the smoke of domestic fires and of the factories in the valley. This local finding sits within which of the framework's named changes?",
   choices=[
     "A decline in air quality, to which human activity contributed",
     "Desertification, to which human activity contributed",
     "Increased consumption of the world's supply of fresh water",
     "The reduction of the problem of geographic distance",
     "The spread of chemically and genetically modified forms of agriculture"],
   ans=0,
   why="KC-6.1.II.A names a decline in air quality among the four changes to which human activity contributed. Smoke from domestic fires and factories producing a persistent haze is that decline observed in one city, and skill 4.B asks a student to place a specific finding inside the broader process."),

 dict(q="A student writes that this course settles the question of what causes climate change. What is the best correction?",
   choices=[
     "The framework records that releases into the atmosphere contributed to debates about the nature and causes of climate change, and leaves those debates open",
     "The framework states the causes of climate change directly and identifies which account is correct",
     "The framework states that climate change has no causes worth investigating",
     "The framework makes no reference to the atmosphere or to climate at any point",
     "The framework states that the debates about climate change ended before 1900"],
   ans=0,
   why="KC-6.1.II.B states that the release of greenhouse gases and pollutants into the atmosphere contributed to DEBATES ABOUT the nature and causes of climate change. The framework's subject is the existence of the debates, not a verdict within them, and this item exists to mark that boundary so a student who reads the sentence carefully is rewarded."),

 dict(q="Which list correctly names the four environmental changes this course states human activity contributed to?",
   choices=[
     "Deforestation, desertification, a decline in air quality, and increased consumption of fresh water",
     "Deforestation, urbanization, the growth of trade, and the spread of railways",
     "Desertification, the decline of empires, migration, and the growth of cities",
     "A decline in air quality, the spread of vaccines, air travel, and nuclear power",
     "Increased consumption of fresh water, falling fertility, longer life, and rising output"],
   ans=0,
   why="KC-6.1.II.A names exactly these four: deforestation, desertification, a decline in air quality, and increased consumption of the world's supply of fresh water. Each distractor mixes in developments the framework states in other sentences of this course, which is the cross-sentence error a list item is built to catch."),

 dict(q="Two neighbouring states each claim the greater share of the flow of a river they share, and each cites the needs of its own farmers. This course would situate their dispute within",
   choices=[
     "the more intense competition over resources that followed the environmental changes of the period",
     "the debates about the nature and causes of climate change",
     "the dissolution of empires and the restructuring of states after World War II",
     "the growth of knowledge economies in some regions late in the century",
     "the spread of a globalized consumer culture across national borders"],
   ans=0,
   why="KC-6.1.II.A states that as human activity contributed to the four changes it names, humans competed over these and other resources more intensely than ever before. Two states disputing the flow of a shared river is that competition in its plainest form, and the framework treats increased consumption of fresh water as one of the changes driving it."),

 dict(q="A hypothetical index divides recorded atmospheric releases into two parts in each period. Which conclusion does the table alone support?",
   table=_T_RELEASES,
   choices=[
     "Total recorded releases rose in each period, while the share coming from the first group of states fell",
     "Total recorded releases fell in each period after the first one recorded",
     "The share coming from the first group of states rose across the record",
     "Releases from all other states fell across the record",
     "The first group of states accounted for less than half of recorded releases in every period"],
   ans=0,
   why="KC-6.1.II.B states that the release of greenhouse gases and pollutants into the atmosphere contributed to debates about the nature and causes of climate change, so the quantity and distribution of releases is course content. The index is hypothetical and names no real state; the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier, and the item asks nothing about responsibility for the releases."),

 dict(q="An unattributed pamphlet of 1980 argues that the environmental strains of its region are without precedent in intensity. Which of this course's statements is closest to that claim?",
   choices=[
     "That humans competed over resources more intensely than ever before",
     "That humans ceased to compete over resources during this period",
     "That environmental change was confined to the years before 1900",
     "That human activity had no part in the environmental changes of the period",
     "That the debates about climate change had been concluded"],
   ans=0,
   why="KC-6.1.II.A ends with the statement that humans competed over these and other resources MORE INTENSELY THAN EVER BEFORE, which is a claim about unprecedented intensity. The pamphlet's claim is the framework's own comparison, and each distractor denies some part of the sentence."),

 dict(q="A commentator writes that the environmental changes of the twentieth century happened entirely without human involvement. How does this course's framework bear on that claim?",
   choices=[
     "It contradicts the claim, stating that human activity contributed to the changes it names",
     "It supports the claim, stating that human activity had no part in those changes",
     "It supports the claim for deforestation but not for the other three changes",
     "It is silent, since the framework names no environmental changes",
     "It contradicts the claim by stating that human activity was the sole cause"],
   ans=0,
   why="KC-6.1.II.A states that human activity CONTRIBUTED TO deforestation, desertification, a decline in air quality, and increased consumption of the world's supply of fresh water. Contributed contradicts no involvement without asserting sole causation, so the key states the framework's verb and not a stronger one."),

 dict(q="A water authority's minute of 1972 records that the wells its district has depended on for generations now have to be sunk far deeper each year to reach water. This local record belongs within which broader process the framework names?",
   choices=[
     "Increased consumption of the world's supply of fresh water",
     "A decline in the quality of the world's air",
     "The deforestation of the world's remaining woodland",
     "The desertification of the world's dry margins",
     "The release of greenhouse gases into the atmosphere"],
   ans=0,
   why="KC-6.1.II.A names increased consumption of the world's supply of fresh water among the four changes to which human activity contributed. Wells needing to be sunk deeper each year is that consumption recorded by the authority that manages it, and skill 4.B asks a student to place the local record inside the broader process."),

 dict(q="Which statement about the environment in this period is NOT supported by this course?",
   choices=[
     "Competition over resources became less intense than it had been before 1900",
     "Human activity contributed to deforestation during this period",
     "Human activity contributed to desertification during this period",
     "Human activity contributed to a decline in air quality during this period",
     "Human activity contributed to increased consumption of fresh water"],
   ans=0,
   why="KC-6.1.II.A states that humans competed over these and other resources MORE INTENSELY THAN EVER BEFORE, so a claim of reduced intensity reverses the framework's sentence. The item asks which statement is NOT supported, so the key is deliberately the false one; the other four restate the four changes the same sentence names."),

 dict(q="Two unattributed articles of 1988 disagree about what is happening to the world's climate and why. According to this course, the existence of that disagreement is",
   choices=[
     "part of what the framework describes, since releases into the atmosphere contributed to debates about the nature and causes of climate change",
     "outside what the framework describes, since the framework records no debates on the subject",
     "evidence that the framework treats one of the two articles as correct",
     "evidence that the framework treats the climate as unchanging",
     "outside what the framework describes, since the framework places all such debates before 1900"],
   ans=0,
   why="KC-6.1.II.B states that the release of greenhouse gases and pollutants into the atmosphere contributed to debates about the nature and causes of climate change. The disagreement between the two articles is one instance of the debates the framework names, and the framework endorses neither side of it, which is what the key says and all it says."),

 dict(q="An unattributed regional plan of 1965 proposes to clear woodland for new farms while acknowledging that the district's rainfall may already be declining. Which broader process does the plan sit inside?",
   choices=[
     "Human activity contributing to deforestation, one of the environmental changes of the period",
     "The reversal of deforestation through the planting of new woodland",
     "The reduction of competition over land through international agreement",
     "The transfer of the district's land to an international administration",
     "The migration of the district's population to a former imperial metropole"],
   ans=0,
   why="KC-6.1.II.A names deforestation first among the changes to which human activity contributed. A plan to clear woodland for farms is a decision that contributes to that change, and skill 4.B asks a student to situate the specific proposal within the broader process rather than to judge the proposal."),

 dict(q="A researcher wants to explain why disputes over a particular resource grew sharper across the twentieth century. Which of this course's statements supplies the framework's own explanation?",
   choices=[
     "That human activity contributed to environmental changes and that humans then competed over those resources more intensely than ever before",
     "That human activity had no bearing on the availability of any resource",
     "That competition over resources was constant across the whole century",
     "That resources ceased to be used once the environmental changes began",
     "That disputes over resources were settled by international agreement in every case"],
   ans=0,
   why="KC-6.1.II.A joins the two in one sentence: as human activity contributed to deforestation, desertification, a decline in air quality, and increased consumption of the world's supply of fresh water, humans competed over these and other resources more intensely than ever before. The reasoning process the CED prints beside this topic is causation, and that sentence is the causal chain."),

 dict(q="A hypothetical city council's record of 1982 shows measurements of the air taken every day for the first time that year. According to this course, the practice of taking such measurements is best situated within",
   choices=[
     "concern about a decline in air quality and about releases into the atmosphere during this period",
     "the reduction of the problem of geographic distance by new transportation",
     "the growth of knowledge economies in some regions of the world",
     "the redrawing of political boundaries after the withdrawal of colonial authorities",
     "the growth of a globalized consumer culture across national borders"],
   ans=0,
   why="KC-6.1.II.A names a decline in air quality among the changes to which human activity contributed, and KC-6.1.II.B names the release of pollutants into the atmosphere and the debates it contributed to. A city beginning to measure its air daily belongs inside those two, which skill 4.B asks a student to identify as the broader context."),

 dict(q="A historian writes that the framework's account of environmental change should not be read as blaming any single generation or country. Is that reading consistent with what this course states?",
   choices=[
     "Yes, because the framework says human activity contributed to the changes and names no particular actor as responsible",
     "No, because the framework names the specific countries responsible for each change",
     "No, because the framework states that a single generation caused all four changes",
     "Yes, because the framework denies that human activity had any part in the changes",
     "No, because the framework assigns responsibility for the changes to agriculture alone"],
   ans=0,
   why="KC-6.1.II.A states that HUMAN ACTIVITY contributed to deforestation, desertification, a decline in air quality, and increased consumption of the world's supply of fresh water. The subject of the sentence is human activity in general and the framework names no country, industry or generation, so a reading that supplies one would go beyond it."),

 dict(q="Which pair does this course present as connected, the first contributing to the second?",
   choices=[
     "The release of greenhouse gases and pollutants into the atmosphere, and debates about the nature and causes of climate change",
     "Debates about the nature and causes of climate change, and the release of greenhouse gases into the atmosphere",
     "The deforestation of woodland, and the reduction of competition over resources",
     "Increased consumption of fresh water, and the disappearance of agriculture",
     "A decline in air quality, and the lengthening of human life"],
   ans=0,
   why="KC-6.1.II.B states that the release of greenhouse gases and pollutants into the atmosphere contributed to debates about the nature and causes of climate change, which fixes the release as prior and the debates as what it contributed to. A distractor reverses the order, so the key names both terms and the direction between them."),

 dict(q="An examination candidate is told to situate a 1970 report on a shrinking lake within a broader historical context. Which approach best does that?",
   choices=[
     "Relating the report to the period's increased consumption of fresh water and the sharper competition over resources that followed",
     "Counting the number of pages the report contains and describing its binding",
     "Listing every other report published anywhere in the world in 1970",
     "Judging whether the report's prose would satisfy a modern reader",
     "Describing the professional qualifications of the report's authors"],
   ans=0,
   why="KC-6.1.II.A names increased consumption of the world's supply of fresh water among the changes to which human activity contributed and states that humans competed over such resources more intensely than ever before. Skill 4.B, the suggested skill for this topic, asks a student to situate a specific development inside a broader process, which page counts and prose judgements do not do."),

 dict(q="Two unattributed government papers of 1990 propose opposite responses to the same set of atmospheric measurements. What does this course's framework allow a student to conclude?",
   choices=[
     "That releases into the atmosphere contributed to debates of exactly this kind, without the framework favouring either proposal",
     "That the framework identifies which of the two proposals is correct",
     "That the framework treats atmospheric measurements as impossible to make",
     "That the framework treats disagreements about policy as belonging to an earlier century",
     "That the framework denies that any releases into the atmosphere occurred"],
   ans=0,
   why="KC-6.1.II.B states that the release of greenhouse gases and pollutants into the atmosphere contributed to debates about the nature and causes of climate change. Two opposed papers responding to the same measurements are an instance of those debates, and the framework describes the debates without taking a side, which is what the key states and all it states."),

 dict(q="According to this course, over what did humans compete more intensely than ever before?",
   choices=[
     "The resources affected by the period's environmental changes, and other resources besides",
     "Only over fresh water, and over no other resource",
     "Only over woodland, and over no other resource",
     "Over no resource, since competition declined during the period",
     "Over resources that the framework does not identify in any way"],
   ans=0,
   why="KC-6.1.II.A states that humans competed over THESE AND OTHER RESOURCES more intensely than ever before, where these are the resources implicated in the four named changes. The framework's phrase reaches past the four to other resources as well, so a key confined to one of them would understate the sentence."),

 dict(q="A commodity broker's circular of 1974 notes that buyers are now bidding against one another for supplies that were freely available a generation earlier. Within this course's framework, the circular is evidence of",
   choices=[
     "the intensified competition over resources that accompanied the period's environmental changes",
     "the reduction of the problem of geographic distance by new transportation",
     "the debates about the nature and causes of climate change",
     "the persistence of diseases associated with poverty",
     "the strong role newly independent governments took in guiding economic life"],
   ans=0,
   why="KC-6.1.II.A states that as human activity contributed to the four named changes, humans competed over these and other resources more intensely than ever before. Buyers bidding against one another for what had been freely available is that intensified competition recorded commercially."),

 dict(q="Which question would this course's framework treat as still open rather than settled?",
   choices=[
     "What the nature and causes of climate change are",
     "Whether human activity contributed to deforestation in this period",
     "Whether human activity contributed to desertification in this period",
     "Whether the world's air quality declined in this period",
     "Whether consumption of the world's fresh water increased in this period"],
   ans=0,
   why="KC-6.1.II.A asserts the four environmental changes and human activity's contribution to them as matters of course content, while KC-6.1.II.B asserts only that releases into the atmosphere contributed to DEBATES ABOUT the nature and causes of climate change. The framework therefore states the four and leaves the content of the debates open, which is the distinction this item is built on."),

 dict(q="A district council in 1985 must decide between clearing more land for cultivation and preserving what remains of its woodland, and the argument turns on which use the district needs more. This course would situate the council's difficulty within",
   choices=[
     "the sharper competition over resources that followed the environmental changes of the period",
     "the debates about the nature and causes of climate change",
     "the growth of commercial agriculture that sustained a growing population",
     "the reduction of the problem of geographic distance",
     "the migration of colonial subjects to imperial metropoles"],
   ans=0,
   why="KC-6.1.II.A states that as human activity contributed to deforestation and the other changes it names, humans competed over these and other resources more intensely than ever before. A council forced to choose between two uses of the same land is that competition inside one jurisdiction, and skill 4.B asks for the broader process a specific decision belongs to."),

 dict(q="Considered across this topic, what does this course say the environmental changes of the period produced?",
   choices=[
     "Sharper competition over resources, and debates about the nature and causes of climate change",
     "The end of all competition over resources, and agreement about the climate",
     "No effect on human societies of any kind during the period",
     "The reversal of every environmental change within the same century",
     "A settled scientific verdict that the framework itself states"],
   ans=0,
   why="KC-6.1.II.A ends in competition over resources more intense than ever before and KC-6.1.II.B ends in debates about the nature and causes of climate change. Those are the two outcomes the topic's two sentences name, and the framework supplies a debate rather than a verdict, which the key preserves."),

 dict(q="Taking the topic as a whole, which single sentence best states what this course says about the environment after 1900?",
   choices=[
     "Human activity contributed to the loss of forests, the spread of deserts, worse air and heavier use of fresh water, competition over such resources grew sharper than ever, and releases into the atmosphere fed debates about the climate that the course does not settle",
     "Human activity had no part in the environmental changes of the century, and no competition over resources followed from them",
     "Human activity caused every environmental change single-handedly, and the course states the settled scientific verdict about the climate",
     "The environmental changes of the century reduced competition over resources and ended all debate about the climate",
     "Environmental change belongs to the years before 1900 and has no place in the history of the twentieth century"],
   ans=0,
   why="KC-6.1.II.A supplies the four changes, human activity's contribution to them, and the competition more intense than ever before; KC-6.1.II.B supplies the releases and the debates about the nature and causes of climate change. The key is the conjunction of those two sentences, keeping contributed rather than caused and a debate rather than a verdict, and each distractor breaks at least one of those."),
]
