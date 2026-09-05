# AP WORLD HISTORY: MODERN 3.3 Empires: Belief Systems
# CED effective Fall 2024/2026, Unit 3 Land-Based Empires, c. 1450 to c. 1750.
# Unit 3: Learning Objective C -- explain continuity and change within the
# various belief systems during the period from 1450 to 1750. Suggested skill
# 2.B, explain the point of view, purpose, historical situation, and/or audience
# of a source. Reasoning process: continuity and change.
#
# Historical developments this module keys to, in the framework's own words:
#   KC-4.1.VI.i    The Protestant Reformation marked a break with existing
#                  Christian traditions and both the Protestant and Catholic
#                  reformations contributed to the growth of Christianity.
#   KC-4.1.VI.ii   Political rivalries between the Ottoman and Safavid empires
#                  intensified the split within Islam between Sunni and Shi'a.
#   KC-4.1.VI.iii  Sikhism developed in South Asia in a context of interactions
#                  between Hinduism and Islam.
# Their parent statement, printed with topics 3.4 and 4.5:
#   KC-4.1.VI      In some cases, the increase and intensification of
#                  interactions between newly connected hemispheres expanded the
#                  reach and furthered development of existing religions, and
#                  contributed to religious conflicts and the development of
#                  syncretic belief systems and practices.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT. KC-4.1.VI.ii says the Ottoman
# and Safavid rivalry intensified the Sunni and Shi'a split; it does NOT say
# which empire stood on which side, so no item here keys that. The framework
# names no founder and no date for Sikhism, no reformer by name, and no council
# or doctrine of the Catholic reformation, so no item keys any of those either.
# Sample activity 3 for this topic uses an excerpt from Martin Luther's 95
# Theses; because the bank must never put words in a real person's mouth, the
# sourcing items here use explicitly hypothetical, unattributed documents and
# turn on the reasoning rather than on who wrote them.
#
# Dates are written "1450 to 1750". Five choices A-E per HISTORY_BRIEF.md.
TOPIC = ("3.3", "Empires: Belief Systems", 3)

_T_SOURCING = dict(
    headers=["Question a student asks of a source", "What the question is asking about"],
    rows=[["Question 1", "Who the writer was and where the writer stood in the dispute"],
          ["Question 2", "What the writer was trying to accomplish by writing"],
          ["Question 3", "Who the writer expected to read the document"],
          ["Question 4", "What was happening at the time the document was written"]])

_T_HOUSES = dict(
    headers=["Decade", "Houses of worship of the older tradition",
             "Houses of worship of the newer tradition"],
    rows=[["First decade", "400", "0"],
          ["Second decade", "410", "40"],
          ["Third decade", "430", "150"],
          ["Fourth decade", "460", "320"]])

_T_TRADITIONS = dict(
    headers=["Development described", "Where the framework locates it"],
    rows=[["Development 1", "A break with existing Christian traditions, followed by growth in Christianity overall"],
          ["Development 2", "A split within Islam deepened by the rivalry of two empires"],
          ["Development 3", "A tradition developing amid interactions between Hinduism and Islam in South Asia"]])

QUESTIONS = [
 dict(
  q=("According to the framework, what did the Protestant Reformation mark?"),
  choices=[
   "A break with existing Christian traditions",
   "The end of Christianity as a growing religion",
   "The beginning of Islam's split into Sunni and Shi'a",
   "The founding of Sikhism in South Asia",
   "The abandonment of religious ideas as a basis for rule"],
  ans=0,
  why=("KC-4.1.VI.i states that the Protestant Reformation marked a break with existing "
       "Christian traditions. The same statement says both the Protestant and Catholic "
       "reformations contributed to the growth of Christianity, so an end to growth "
       "contradicts it; the Sunni and Shi'a split is KC-4.1.VI.ii and Sikhism KC-4.1.VI.iii.")),
 dict(
  q=("The framework makes a claim about the effect of the Protestant and Catholic reformations "
     "taken together. What is that claim?"),
  choices=[
   "Both contributed to the growth of Christianity",
   "Both reduced the number of Christians worldwide",
   "Both were confined to South Asia",
   "Both ended the use of religious ideas by rulers",
   "Both produced a single unified church"],
  ans=0,
  why=("KC-4.1.VI.i states that both the Protestant and Catholic reformations contributed to "
       "the growth of Christianity. The rejected options reverse that claim, relocate it, or "
       "assert a unification the framework never describes; KC-4.3.I.A meanwhile has rulers "
       "continuing to use religious ideas.")),
 dict(
  q=("Which pair of empires does the framework connect with the deepening of the split within "
     "Islam between Sunni and Shi'a in this period?"),
  choices=[
   "The Ottoman and Safavid empires",
   "The Mughal and Manchu empires",
   "The Ottoman and Manchu empires",
   "The Safavid and Songhai empires",
   "The Mughal and Ottoman empires"],
  ans=0,
  why=("KC-4.1.VI.ii states that political rivalries between the Ottoman and Safavid empires "
       "intensified the split within Islam between Sunni and Shi'a. The other pairs join "
       "empires the framework names elsewhere, at KC-4.3.II.B, without connecting them to this "
       "development.")),
 dict(
  q=("According to the framework, what kind of rivalry between the Ottoman and Safavid empires "
     "intensified the split within Islam?"),
  choices=[
   "Political rivalry",
   "A dispute over shipping in the Atlantic",
   "A quarrel over the succession to a European throne",
   "Competition for colonies in the Americas",
   "A disagreement over the price of silver in China"],
  ans=0,
  why=("KC-4.1.VI.ii names political rivalries between the Ottoman and Safavid empires as what "
       "intensified the Sunni and Shi'a split. Atlantic shipping, American colonies and the "
       "silver trade belong to unit 4's KC-4.1.III and KC-4.1.IV and are not offered as causes "
       "here.")),
 dict(
  q=("The framework says that a religious tradition developed in South Asia in this period in a "
     "particular context. Which tradition and which context?"),
  choices=[
   "Sikhism, amid interactions between Hinduism and Islam",
   "Sikhism, amid interactions between Christianity and Buddhism",
   "Protestantism, amid interactions between Hinduism and Islam",
   "Shi'a Islam, amid interactions between Christianity and Judaism",
   "Catholicism, amid interactions between Buddhism and Daoism"],
  ans=0,
  why=("KC-4.1.VI.iii states that Sikhism developed in South Asia in a context of interactions "
       "between Hinduism and Islam. Each rejected option keeps one half of that statement and "
       "changes the other, which is the near-miss this subject invites.")),
 dict(
  q=("A hypothetical letter written during the period argues that the writer's congregation "
     "must worship in its own way, and denounces the practices of the church the writer's "
     "family had belonged to.\n\n"
     "Which of the framework's developments does the letter most directly illustrate?"),
  choices=[
   "A break with existing Christian traditions",
   "The intensification of the split within Islam",
   "The development of Sikhism in South Asia",
   "The adoption of restrictive trade policies by Asian states",
   "The recruitment of bureaucratic elites by rulers"],
  ans=0,
  why=("KC-4.1.VI.i describes the Protestant Reformation as marking a break with existing "
       "Christian traditions, and a congregation separating from the church it had belonged to "
       "is that break. The other options are KC-4.1.VI.ii, KC-4.1.VI.iii, KC-4.3.II.A.i and "
       "KC-4.3.I.C.")),
 dict(
  q=("A student is asked to explain the point of view of a document written during a religious "
     "dispute. Which of the following does that task require?"),
  choices=[
   "Identifying who the writer was and where the writer stood in the dispute",
   "Counting how many words the document contains",
   "Establishing the price of paper in the year it was written",
   "Listing every other document written in the same decade",
   "Translating the document into a modern language"],
  ans=0,
  why=("Suggested skill 2.B asks students to explain the point of view, purpose, historical "
       "situation, and/or audience of a source, and point of view is the writer's own position "
       "in relation to the subject. Word counts, paper prices, bibliographies and translation "
       "answer different questions about the same object.")),
 dict(
  q=("A hypothetical pamphlet from the period urges readers to petition their ruler in favour "
     "of one side of a religious dispute. A student is asked for the pamphlet's purpose. Which "
     "answer addresses that question?"),
  choices=[
   "To persuade readers to act on behalf of one side of the dispute",
   "To record the writer's date of birth for posterity",
   "To describe the geography of the region for travellers",
   "To settle a boundary between two provinces",
   "To list the goods available in a nearby market"],
  ans=0,
  why=("Suggested skill 2.B names purpose as one of the elements to be explained, and a "
       "pamphlet urging readers to petition is written to persuade them to act. The rejected "
       "options describe purposes no petitioning pamphlet would have.")),
 dict(
  q=("A hypothetical sermon from the period was preached to an assembly of village farmers. A "
     "student asked to explain the source's audience should say which of the following?"),
  choices=[
   "The audience was the assembled villagers to whom the sermon was preached",
   "The audience was the ruler of a distant empire",
   "The audience was a council of foreign merchants",
   "The audience cannot be discussed for any source",
   "The audience is the same as the purpose in every source"],
  ans=0,
  why=("Suggested skill 2.B names audience among the elements a student must explain, and the "
       "audience of a sermon is those to whom it was preached. Audience and purpose are "
       "distinct elements in that skill, so treating them as identical misapplies it.")),
 dict(
  q=("Explaining the historical situation of a source written during a religious conflict "
     "requires attention to which of the following?"),
  choices=[
   "The circumstances in the writer's world at the time the source was produced",
   "The number of copies of the source that survive today",
   "The modern reader's own opinion of the dispute",
   "The alphabet in which the source happens to be written",
   "The physical weight of the volume in which it is bound"],
  ans=0,
  why=("Suggested skill 2.B names historical situation among the elements to be explained, and "
       "a situation is the set of circumstances surrounding the source's production. Survival "
       "rates, a modern opinion, a script and a binding are facts about the object or the "
       "reader rather than about the moment of writing.")),
 dict(
  q=("Which conclusion about religion in the period 1450 to 1750 is best supported by the "
     "framework's statement about the Protestant and Catholic reformations?"),
  choices=[
   "A break within a religion was compatible with that religion's overall growth",
   "A break within a religion necessarily reduced the number of its adherents",
   "A break within a religion always ended in the reunion of the two sides",
   "Religious change in this period was confined to South Asia",
   "Religious change in this period had no political consequences"],
  ans=0,
  why=("KC-4.1.VI.i says the Protestant Reformation marked a break with existing Christian "
       "traditions and that both reformations contributed to the growth of Christianity, so "
       "division and growth occurred together. KC-4.1.VI adds that interactions contributed to "
       "religious conflicts, so political consequences are asserted rather than denied.")),
 dict(
  q=("The framework's parent statement on belief systems in this period names several results "
     "of intensified interaction between newly connected hemispheres. Which is one of them?"),
  choices=[
   "The development of syncretic belief systems and practices",
   "The disappearance of all existing religions",
   "The end of religious conflict everywhere",
   "The confinement of every religion to its region of origin",
   "The replacement of belief by state ceremony"],
  ans=0,
  why=("KC-4.1.VI states that the increase and intensification of interactions expanded the "
       "reach and furthered development of existing religions, and contributed to religious "
       "conflicts and the development of syncretic belief systems and practices. Each rejected "
       "option asserts the opposite of one clause of that sentence.")),
 dict(
  q=("A hypothetical account describes a community whose worship combines practices its members "
     "trace to two different traditions their region had long contained.\n\n"
     "Which term from the framework best describes what the account records?"),
  choices=[
   "A syncretic belief system",
   "A restrictive trade policy",
   "An innovative tax-collection system",
   "A form of armed trade",
   "A bureaucratic elite"],
  ans=0,
  why=("KC-4.1.VI names the development of syncretic belief systems and practices among the "
       "results of intensified interaction, and a community combining practices from two "
       "traditions is that development. The rejected terms belong to KC-4.3.II.A.i, KC-4.3.I.D, "
       "KC-4.3.II and KC-4.3.I.C.")),
 dict(
  q=("Why does the framework treat the period's religious history under continuity and change "
     "rather than under change alone?"),
  choices=[
   "Because existing religions continued and grew even as breaks and splits occurred within them",
   "Because no religious change occurred anywhere in the period",
   "Because every religion of the period was newly founded",
   "Because religious belief ceased to matter to rulers",
   "Because the framework treats all belief systems as identical"],
  ans=0,
  why=("KC-4.1.VI.i has Christianity growing through a period of division, KC-4.1.VI has "
       "existing religions expanding their reach, and KC-4.1.VI.ii and KC-4.1.VI.iii describe "
       "splits and new development within long-standing traditions. Learning Objective C asks "
       "precisely for continuity and change within the various belief systems.")),
 dict(
  q=("The table below lists four questions a student might ask of a written source from this "
     "period.\n\n"
     "Which question is asking about the source's point of view?"),
  table=_T_SOURCING,
  choices=[
   "Question 1",
   "Question 2",
   "Question 3",
   "Question 4",
   "None of the four"],
  ans=0,
  why=("Suggested skill 2.B distinguishes point of view, purpose, historical situation, and "
       "audience. The verifier recomputes that exactly one row asks who the writer was and "
       "where the writer stood, which is point of view; the others ask about aim, readership "
       "and circumstances.")),
 dict(
  q=("Using the same list of questions, which one is asking about the source's audience?"),
  table=_T_SOURCING,
  choices=[
   "Question 3",
   "Question 1",
   "Question 2",
   "Question 4",
   "All four ask about audience"],
  ans=0,
  why=("Suggested skill 2.B names audience as a separate element from purpose and situation, "
       "and the verifier recomputes that exactly one row asks who the writer expected to read "
       "the document. Treating all four as audience questions collapses a distinction the "
       "skill draws.")),
 dict(
  q=("The table below reports hypothetical counts of houses of worship in one region across "
     "four decades in the period 1450 to 1750.\n\n"
     "Which conclusion is best supported by the table alone?"),
  table=_T_HOUSES,
  choices=[
   "Both traditions gained houses of worship over the four decades",
   "The older tradition lost houses of worship in every decade",
   "The newer tradition gained nothing after its first appearance",
   "The two traditions had equal numbers in every decade",
   "Neither tradition changed across the four decades"],
  ans=0,
  why=("KC-4.1.VI.i states that both the Protestant and Catholic reformations contributed to "
       "the growth of Christianity, so growth on both sides of a division is what the framework "
       "leads a student to expect. The verifier recomputes that both columns rise across the "
       "four decades and that the two are never equal.")),
 dict(
  q=("Three developments are described in the table below.\n\n"
     "Which development is the one the framework locates in South Asia?"),
  table=_T_TRADITIONS,
  choices=[
   "Development 3",
   "Development 1",
   "Development 2",
   "The first and the second developments together",
   "None of the three"],
  ans=0,
  why=("KC-4.1.VI.iii states that Sikhism developed in South Asia in a context of interactions "
       "between Hinduism and Islam, and the verifier recomputes that exactly one row names "
       "South Asia and those two traditions. The others describe KC-4.1.VI.i and KC-4.1.VI.ii.")),
 dict(
  q=("A student writes that the split between Sunni and Shi'a began in the period 1450 to 1750 "
     "because of the Ottoman and Safavid rivalry. What is the most accurate correction?"),
  choices=[
   "The framework says the rivalry intensified a split, not that it created one",
   "The framework says the rivalry ended the split entirely",
   "The framework says the split concerned Christianity rather than Islam",
   "The framework says the two empires were allies throughout the period",
   "The framework makes no mention of either empire"],
  ans=0,
  why=("KC-4.1.VI.ii says political rivalries between the Ottoman and Safavid empires "
       "intensified the split within Islam between Sunni and Shi'a, and to intensify something "
       "is to deepen what already exists. Each rejected correction denies something the same "
       "sentence states.")),
 dict(
  q=("Which piece of evidence would most directly support the framework's claim that both "
     "reformations contributed to the growth of Christianity?"),
  choices=[
   "Records showing the number of Christian congregations rising on both sides of the division",
   "Records showing the tonnage of goods shipped from a single port",
   "Records showing the number of soldiers in an imperial garrison",
   "Records showing the rainfall of a single growing season",
   "Records showing the wages paid to builders of a palace"],
  ans=0,
  why=("KC-4.1.VI.i attaches growth in Christianity to both the Protestant and the Catholic "
       "reformations, so evidence bearing on it has to count Christian communities on both "
       "sides. Shipping, garrisons, rainfall and wages document other things entirely.")),
 dict(
  q=("A hypothetical decree from a ruler of this period orders that a religious dispute within "
     "his territory be settled in favour of one side, and warns that the other side's teachers "
     "will lose the ruler's protection.\n\n"
     "Which of the framework's claims does the decree best support?"),
  choices=[
   "Interactions between belief systems in this period contributed to religious conflicts",
   "Religious belief had no bearing on the exercise of state power in this period",
   "Rulers of this period abandoned the use of religious ideas",
   "Religious disputes never crossed the boundary between states",
   "The period saw the end of all religious diversity within empires"],
  ans=0,
  why=("KC-4.1.VI says intensified interaction contributed to religious conflicts, and "
       "KC-4.3.III.i adds that religious disputes led to rivalries and conflict between states, "
       "so a ruler taking a side is that process. KC-4.3.I.A has rulers continuing to use "
       "religious ideas, and KC-4.3.I.B records states accommodating diversity as well as "
       "suppressing it.")),
 dict(
  q=("Two students are comparing religious change in Europe and in South Asia in this period. "
     "Which comparison is supported by the framework?"),
  choices=[
   "A division within one religion in Europe, alongside a tradition developing amid two religions in South Asia",
   "A division within one religion in South Asia, alongside a tradition developing amid two religions in Europe",
   "The disappearance of Christianity in Europe, alongside the disappearance of Islam in South Asia",
   "The unification of all European churches, alongside the unification of all South Asian traditions",
   "The absence of any religious change in either region"],
  ans=0,
  why=("KC-4.1.VI.i places the break with existing Christian traditions in the European "
       "reformations while KC-4.1.VI.iii places Sikhism's development in South Asia amid "
       "interactions between Hinduism and Islam. The first rejected option is the swap of those "
       "two regions, and the rest contradict both statements.")),
 dict(
  q=("A hypothetical treatise from the period was written by a court theologian and addressed "
     "to the ruler's council. Which combination of sourcing elements does that description "
     "supply?"),
  choices=[
   "The writer's position, and the readers the writer addressed",
   "The writer's position, and the number of surviving copies",
   "The readers addressed, and the modern reader's own view",
   "The date of the binding, and the language of translation",
   "The purpose, and nothing else about the source"],
  ans=0,
  why=("Suggested skill 2.B lists point of view and audience among the elements to be "
       "explained, and a court theologian writing for the ruler's council supplies exactly "
       "those two. Survival counts, modern opinions, bindings and translations are not "
       "elements of that skill.")),
 dict(
  q=("Why is the point of view of a polemical religious source from this period worth "
     "establishing before using it as evidence?"),
  choices=[
   "Because the writer's own position in the dispute shapes what the source reports and how",
   "Because a source with a point of view can carry no information at all",
   "Because point of view determines how many copies survive",
   "Because only anonymous sources are usable as evidence",
   "Because the framework forbids the use of religious sources"],
  ans=0,
  why=("Suggested skill 2.B makes point of view an element to be explained precisely because it "
       "bears on how a source presents its subject. Nothing in the skill makes a partisan "
       "source unusable, ties survival to viewpoint, or restricts students to anonymous "
       "documents.")),
 dict(
  q=("Which statement about Sikhism is supported by the framework as it is written?"),
  choices=[
   "It developed in a context of interactions between two existing traditions",
   "It developed in Europe during the Protestant Reformation",
   "It developed without contact with any other tradition",
   "It developed as a branch of Christianity",
   "It developed after the period 1450 to 1750 had ended"],
  ans=0,
  why=("KC-4.1.VI.iii states that Sikhism developed in South Asia in a context of interactions "
       "between Hinduism and Islam, which is a claim about context and about place. The "
       "framework says nothing that would support a European origin, an absence of contact, a "
       "Christian derivation, or a later date.")),
 dict(
  q=("A historian argues that religious change in this period cannot be separated from imperial "
     "politics. Which framework statement most directly supports that argument?"),
  choices=[
   "Political rivalries between two empires intensified a split within Islam",
   "Colonial economies in the Americas depended largely on agriculture",
   "American food crops improved nutrition in Afro-Eurasia",
   "Existing Indian Ocean trade networks continued to flourish",
   "New tools and ship designs made transoceanic travel possible"],
  ans=0,
  why=("KC-4.1.VI.ii ties a religious development directly to the political rivalry of two "
       "empires, which is what the argument claims. The rejected statements are KC-4.2.II.D, "
       "KC-4.1.V.D, KC-4.3.II.A.iii and KC-4.1.II.A, none of which concerns religion.")),
 dict(
  q=("A hypothetical chronicle records that after a long war between two empires, preachers on "
     "each side described the other side's version of their shared faith as false.\n\n"
     "Which framework statement does the chronicle illustrate?"),
  choices=[
   "A political rivalry intensifying a split within a religion",
   "A break with existing Christian traditions",
   "The development of a new tradition amid two others",
   "The expansion of maritime trading networks in Africa",
   "The unintentional transfer of disease vectors"],
  ans=0,
  why=("KC-4.1.VI.ii states that political rivalries between the Ottoman and Safavid empires "
       "intensified the split within Islam between Sunni and Shi'a, and preaching that follows "
       "a war between two empires is that intensification. The other options are KC-4.1.VI.i, "
       "KC-4.1.VI.iii, KC-4.3.II.A.ii and KC-4.1.V.A.")),
 dict(
  q=("Which of the following would best show continuity, rather than change, in a religious "
     "tradition during the period 1450 to 1750?"),
  choices=[
   "Evidence that the tradition kept growing and kept its established observances",
   "Evidence that a group separated from the tradition over doctrine",
   "Evidence that a new tradition formed from two older ones",
   "Evidence that two empires quarrelled over which version was correct",
   "Evidence that a ruler withdrew protection from one side of a dispute"],
  ans=0,
  why=("Learning Objective C asks for continuity and change within the various belief systems, "
       "and continuity is a tradition persisting. KC-4.1.VI.i's break, KC-4.1.VI.iii's new "
       "development and KC-4.1.VI.ii's intensified split are all instances of change rather "
       "than of continuity.")),
 dict(
  q=("Two hypothetical sources describe the same religious dispute: one is a public sermon and "
     "the other a private letter between two officials. Why might a student expect them to "
     "differ?"),
  choices=[
   "Because their audiences differ, and a source is shaped by whom it addresses",
   "Because a sermon can contain no information about a dispute",
   "Because private letters are always more accurate than public speech",
   "Because only one of the two can have a purpose",
   "Because the historical situation of two sources from one dispute must differ"],
  ans=0,
  why=("Suggested skill 2.B names audience among the elements that must be explained about a "
       "source, and a public congregation and a fellow official are different audiences. "
       "Nothing in the skill ranks private sources above public ones or denies a purpose to "
       "either, and two sources from one dispute may share a historical situation.")),
 dict(
  q=("A summary sentence about this topic is being drafted for students. Which version stays "
     "within what the framework asserts about belief systems from 1450 to 1750?"),
  choices=[
   "A reformation broke with existing Christian traditions while Christianity grew, imperial rivalry deepened a split within Islam, and Sikhism developed amid Hinduism and Islam in South Asia",
   "Christianity shrank as it divided, Islam was unified by imperial rivalry, and no new tradition appeared anywhere",
   "Religious belief ceased to interest rulers, and no religion changed in the period",
   "Every religion of the period was newly founded, and none had earlier roots",
   "Religious change occurred only in South Asia, and Europe saw none at all"],
  ans=0,
  why=("The keyed sentence joins KC-4.1.VI.i on the break and the growth of Christianity, "
       "KC-4.1.VI.ii on the intensified Sunni and Shi'a split, and KC-4.1.VI.iii on Sikhism's "
       "development in South Asia. Each rejected version contradicts at least one of those "
       "three statements.")),
]
