# AP WORLD HISTORY: MODERN 8.4 Spread of Communism After 1900
# CED effective Fall 2026 (Course Framework V.1), Unit 8 Cold War and
# Decolonization, c. 1900 to the present. Thematic focus: Economic Systems (ECN)
# and Social Interactions and Organization (SIO).
#
# TWO learning objectives share this topic page:
#   Unit 8 Learning Objective D -- explain the causes and consequences of
#     China's adoption of communism.
#   Unit 8 Learning Objective E -- explain the causes and effects of movements
#     to redistribute economic resources.
# Suggested skill 2.C, explain the significance of a source's point of view,
# purpose, historical situation, and/or audience, INCLUDING HOW THESE MIGHT
# LIMIT THE USE(S) OF A SOURCE. That last clause is why so many items here ask
# what a source cannot show as well as what it can.
#
# HISTORICAL DEVELOPMENTS this topic prints, and the only sentences the keys
# below rest on:
#   KC-6.2.I.i     As a result of internal tension and Japanese aggression,
#                  Chinese communists seized power. These changes in China
#                  eventually led to communist revolution.
#   KC-6.3.I.A.ii  In communist China, the government controlled the national
#                  economy through the Great Leap Forward, often implementing
#                  repressive policies, with negative repercussions for the
#                  population.
#   KC-6.2.II.D.i  Movements to redistribute land and resources developed within
#                  states in Africa, Asia, and Latin America, sometimes
#                  advocating communism or socialism.
# ILLUSTRATIVE EXAMPLES the CED prints for land and resource redistribution: the
# Communist Revolution for Vietnamese independence; Mengistu Haile Mariam in
# Ethiopia; land reform in Kerala and other states within India; the White
# Revolution in Iran. Exactly one item turns on them and its stem says so.
#
# THE WORD "SOMETIMES" IS LOAD-BEARING. KC-6.2.II.D.i says redistribution
# movements SOMETIMES advocated communism or socialism. A bank that keyed every
# land reform as communist would teach the opposite of the framework's own
# sentence, and it is an easy error to make in a topic titled Spread of
# Communism. Items 5, 12 and 20 exist to hold that distinction open.
#
# DEDUPE NOTE. Topic 9.4 Economics in the Global Age also concerns economic
# systems. This module stays on redistribution, state direction of the economy
# and the Chinese case; free-market liberalization, trade agreements and
# multinational corporations belong to 9.4 and appear here only as distractors.
#
# SOURCES are text and unattributed; no quotation is put in a real person's
# mouth. TABLES are hypothetical and every keyed conclusion is recomputed from
# the table alone. DATES are written "1945 to 1980", never with a hyphen.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("8.4", "Spread of Communism After 1900", 8)

_T_LAND = dict(
    headers=["Group (hypothetical district survey)",
             "Share of farmland held before the reform (percent)",
             "Share of farmland held after the reform (percent)"],
    rows=[["Largest landholders", "62", "9"],
          ["Middling holders", "25", "34"],
          ["Households holding no land before the reform", "0", "41"],
          ["Village and collective holdings", "13", "16"]])

_T_CAMPAIGN = dict(
    headers=["Year of a state-directed campaign (hypothetical figures)",
             "Grain output (index, first year = 100)",
             "Grain taken by the state (index, first year = 100)"],
    rows=[["Year one", "100", "100"],
          ["Year two", "85", "118"],
          ["Year three", "71", "124"],
          ["Year four", "78", "96"]])

_T_REGION = dict(
    headers=["Region (hypothetical survey, 1945 to 1980)",
             "States adopting a national land redistribution program",
             "Of those, states whose program declared a communist or socialist aim"],
    rows=[["Africa", "14", "6"],
          ["Asia", "12", "5"],
          ["Latin America", "11", "4"]])

QUESTIONS = [

 dict(q="According to this course, which combination of conditions preceded the Chinese communists' seizure of power?",
   choices=[
     "Internal tension within China together with Japanese aggression against it",
     "An invasion of China by the Soviet Union together with a famine in Europe",
     "The withdrawal of a European colonial administration together with a negotiated independence",
     "A dispute with a neighbouring state over trade tariffs together with a currency crisis",
     "The collapse of a global free-market order together with the founding of the United Nations"],
   ans=0,
   why="KC-6.2.I.i states that as a result of internal tension and Japanese aggression, Chinese communists seized power. The framework names those two conditions and no others, and it does not describe China as a colony whose independence was negotiated with a European power."),

 dict(q="This course states that the changes in China that brought the communists to power eventually led to",
   choices=[
     "communist revolution",
     "the restoration of the imperial dynasty",
     "the partition of the country into two colonial spheres",
     "the adoption of free-market economic policies within a decade",
     "the abolition of central government in favour of provincial rule"],
   ans=0,
   why="KC-6.2.I.i states that these changes in China eventually led to communist revolution. The framework treats the seizure of power and the revolution as connected stages of one process rather than as separate or reversed developments."),

 dict(q="In the framework of this course, the Great Leap Forward is described as a means by which",
   choices=[
     "the government of communist China controlled the national economy",
     "China opened its economy to foreign private investment",
     "China transferred economic planning to an international organization",
     "a European empire administered its remaining Asian possessions",
     "a group of newly independent states coordinated their trade policies"],
   ans=0,
   why="KC-6.3.I.A.ii states that in communist China the government controlled the national economy through the Great Leap Forward. The framework presents it as an instrument of state direction, which is the opposite of opening the economy or handing planning to an outside body."),

 dict(q="What does this course say about the effects of the Great Leap Forward on the population of China?",
   choices=[
     "The government often implemented repressive policies, with negative repercussions for the population",
     "The population was left unaffected because the campaign was confined to foreign trade",
     "The campaign raised living standards without any accompanying coercion",
     "The campaign was administered by an international body rather than by the state",
     "The campaign applied only to the country's urban professional classes"],
   ans=0,
   why="KC-6.3.I.A.ii states that the government controlled the national economy through the Great Leap Forward, often implementing repressive policies, with negative repercussions for the population. The framework records both the coercion and the harm, so any answer that reports one without the other or neither departs from it."),

 dict(q="This course states that movements to redistribute land and resources developed within states in Africa, Asia, and Latin America and that they",
   choices=[
     "sometimes advocated communism or socialism, rather than always doing so",
     "always advocated communism, without exception in any region",
     "always opposed communism and socialism in every case",
     "developed only in states that were already governed by communist parties",
     "were confined to Europe and North America during this period"],
   ans=0,
   why="KC-6.2.II.D.i states that movements to redistribute land and resources developed within states in Africa, Asia, and Latin America, sometimes advocating communism or socialism. The word sometimes is the framework's own, and treating every such movement as communist would contradict the sentence the question is drawn from."),

 dict(q="This course offers four cases as illustrative examples of land and resource redistribution. They are",
   choices=[
     "the Communist Revolution for Vietnamese independence, Mengistu Haile Mariam in Ethiopia, land reform in Kerala and other Indian states, and the White Revolution in Iran",
     "the founding of NATO, the founding of the Warsaw Pact, the Korean War, and the Angolan Civil War",
     "the Non-Aligned Movement, the Green Belt Movement, Greenpeace, and the World Fair Trade Organization",
     "the Partition of India, the creation of the state of Israel, the founding of Pakistan, and the founding of Cambodia",
     "the policies of Ronald Reagan, Margaret Thatcher, Deng Xiaoping, and Augusto Pinochet"],
   ans=0,
   why="The CED prints these four as the ILLUSTRATIVE EXAMPLES accompanying KC-6.2.II.D.i on land and resource redistribution. Each distractor lists illustrative examples the framework attaches to other statements, on proxy wars, on movements opposing existing orders, on redrawn boundaries and on free-market policies."),

 dict(q="A district survey gives hypothetical figures for landholding before and after a redistribution. Which conclusion does the table alone support?",
   table=_T_LAND,
   choices=[
     "The group with the largest share before the reform had the smallest share after it",
     "The group with the largest share before the reform also had the largest share after it",
     "Every group's share of farmland fell between the two columns",
     "The shares recorded after the reform total less than half of those recorded before",
     "Households that had held no land before the reform still held none afterward"],
   ans=0,
   why="KC-6.2.II.D.i describes movements to redistribute land and resources, and a transfer of share between holding groups is what redistribution names. The survey is hypothetical and the keyed conclusion, together with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="A provincial official's report of 1959 submitted to his own superiors describes a state-directed economic campaign in his province as an unqualified success. Which consideration most limits the use of this source as evidence about the campaign's results?",
   choices=[
     "It was written for the authority that ordered the campaign, by an official answerable to it",
     "It concerns a province rather than the whole country, so its subject falls outside the period",
     "It was written in 1959, and no document of that year can be used as historical evidence",
     "It reports on economics, and economic reports are never preserved in archives",
     "It was written by an official, and officials are the only trustworthy source on policy"],
   ans=0,
   why="KC-6.3.I.A.ii records repressive policies and negative repercussions for the population under a campaign of state economic control, which is exactly what a subordinate reporting upward has reason not to record. Explaining how a source's purpose and audience limit its uses is the skill this topic practises."),

 dict(q="The table gives hypothetical figures for a state-directed campaign. Which conclusion does the table alone support?",
   table=_T_CAMPAIGN,
   choices=[
     "The year in which output stood lowest was also the year in which the state took the most",
     "Output and the quantity taken by the state moved in the same direction in every year recorded",
     "The quantity taken by the state fell in every year after the first",
     "Output stood higher in the last year recorded than in the first",
     "Output never fell by more than a tenth below its first-year level"],
   ans=0,
   why="KC-6.3.I.A.ii states that the government controlled the national economy through the Great Leap Forward, often implementing repressive policies, with negative repercussions for the population. A state taking the most in the very year production stood lowest is one mechanism by which such repercussions reach a population, and the figures are hypothetical, with the key recomputed from the table alone in the verifier. An earlier wording of this choice spoke of the two years output fell furthest, which was ambiguous between the lowest levels and the sharpest year-on-year drops and was true only on the second reading."),

 dict(q="A peasant association's resolution of 1952 and a landlord's petition of the same year describe the same redistribution in a single district in incompatible terms. A historian using both should conclude that",
   choices=[
     "each source reports the interest of the group that produced it, and the two together show what was at stake",
     "one of the two documents must be a forgery, since both cannot be accurate",
     "neither document can be used, because interested parties produce no usable evidence",
     "the petition is automatically the more reliable, because it was addressed to authority",
     "the resolution is automatically the more reliable, because it represents more people"],
   ans=0,
   why="KC-6.2.II.D.i describes movements to redistribute land and resources within states, which is a conflict between groups with opposed interests in the same land. Reading each source for the position it represents, rather than ranking the two for truthfulness, is what this topic's skill asks."),

 dict(q="The table gives a hypothetical survey of national land redistribution programs. Which conclusion does the table alone support?",
   table=_T_REGION,
   choices=[
     "In every region listed, fewer than half of the programs declared a communist or socialist aim",
     "In every region listed, more than half of the programs declared such an aim",
     "No program in Latin America declared a communist or socialist aim",
     "Asia recorded more redistribution programs than any other region listed",
     "The three regions recorded the same number of redistribution programs"],
   ans=0,
   why="KC-6.2.II.D.i states that redistribution movements developed in Africa, Asia, and Latin America and sometimes advocated communism or socialism. A survey in which such declarations are a minority everywhere is that word sometimes made measurable, and the figures are hypothetical, with the key recomputed from the table alone in the verifier."),

 dict(q="A student writes that every twentieth-century land reform in Asia, Africa and Latin America was a communist program. What is the best correction?",
   choices=[
     "The framework says redistribution movements sometimes advocated communism or socialism, so many did not",
     "The framework says redistribution movements never advocated communism or socialism",
     "The framework says redistribution movements occurred only in Europe",
     "The framework says redistribution movements were confined to states with no agriculture",
     "The framework says redistribution movements always followed a foreign invasion"],
   ans=0,
   why="KC-6.2.II.D.i states that movements to redistribute land and resources developed within states in Africa, Asia, and Latin America, sometimes advocating communism or socialism. Sometimes rules out both always and never, so the correction has to preserve the middle position rather than replace one absolute with another."),

 dict(q="An unattributed party programme published in an Asian colony in 1945 links the demand for national independence to a promise of land for those who farm it. This combination is best understood as showing that",
   choices=[
     "a movement could pursue independence and the redistribution of resources as a single programme",
     "independence movements everywhere rejected any change in the ownership of land",
     "colonial administrations had already redistributed land before independence was demanded",
     "demands for land redistribution arose only after independence had been achieved",
     "the demand for independence and the demand for land were never made by the same movement"],
   ans=0,
   why="KC-6.2.II.D.i places movements to redistribute land and resources within states in Africa, Asia, and Latin America, and the CED's own illustrative example of a communist revolution for Vietnamese independence pairs the two demands. The framework therefore treats the combination as available rather than impossible."),

 dict(q="Which statement about the causes of communism's spread is NOT supported by this course?",
   choices=[
     "Chinese communists took power after a foreign invasion by the Soviet Union",
     "Internal tension in China contributed to the communists' seizure of power",
     "Japanese aggression contributed to the communists' seizure of power",
     "Movements to redistribute resources developed in Africa, Asia and Latin America",
     "Some redistribution movements advocated communism or socialism"],
   ans=0,
   why="KC-6.2.I.i names internal tension and Japanese aggression as the conditions from which the Chinese communists seized power; it names no Soviet invasion, so that statement is the one the framework does not support. The other four restate KC-6.2.I.i and KC-6.2.II.D.i."),

 dict(q="A memoir published abroad in 1985 by a former villager describes hunger during a state-directed campaign of the late 1950s. Which use of this source is best supported?",
   choices=[
     "As testimony about how the campaign was experienced by one person in one place",
     "As a measurement of the campaign's effect on national output as a whole",
     "As evidence of what the government intended when it launched the campaign",
     "As proof that no such campaign was carried out in other provinces",
     "As an official statement of the policy the campaign was meant to implement"],
   ans=0,
   why="KC-6.3.I.A.ii records negative repercussions for the population under the campaign, which is exactly what individual testimony can attest and exactly what a single memoir cannot quantify nationally. Judging what a source's situation permits it to support is the skill this topic practises."),

 dict(q="A poster produced by a redistribution movement in a Latin American country in 1962 shows only slogans and no figures. Its intended audience is best inferred to be",
   choices=[
     "the rural population the movement hoped to recruit to its programme",
     "foreign economists studying agricultural productivity",
     "the officials of an international organization based in another continent",
     "historians writing about the movement several decades afterward",
     "the members of a rival movement in a different country"],
   ans=0,
   why="KC-6.2.II.D.i places redistribution movements within states in Latin America among other regions, and a slogan poster without data is designed to persuade the people whose support the movement needs. Identifying the audience a source addresses is this topic's skill, and specialists reading for figures are not addressed by a source that contains none."),

 dict(q="Which pair of developments does this course place in a causal relationship in the Chinese case?",
   choices=[
     "Internal tension and Japanese aggression, which led to the communists' seizure of power",
     "The communists' seizure of power, which caused the Japanese aggression that preceded it",
     "The Great Leap Forward, which caused the internal tension of the preceding decades",
     "Communist revolution, which caused the internal tension from which it arose",
     "Japanese aggression, which was caused by the communists' economic policies"],
   ans=0,
   why="KC-6.2.I.i states that as a result of internal tension and Japanese aggression, Chinese communists seized power, fixing the two conditions as prior and the seizure as their result. Every distractor makes a later development the cause of an earlier one."),

 dict(q="A national statistical yearbook published by a government during a campaign it is itself conducting reports record harvests. What is the strongest reason for caution?",
   choices=[
     "The figures were compiled and published by the authority whose campaign they assess",
     "Statistical yearbooks were not published anywhere in the world during this period",
     "Numerical evidence cannot be used by historians under any circumstances",
     "The yearbook is a printed source, and printed sources postdate the events they record",
     "The yearbook covers a whole country, and only local sources are ever admissible"],
   ans=0,
   why="KC-6.3.I.A.ii records repressive policies and negative repercussions for the population under a campaign of state economic control, which gives the compiling authority an interest in the figures it publishes. Explaining how a source's producer and purpose limit its uses is the skill this topic practises."),

 dict(q="Considered together, what do the movements described in this topic have in common across Africa, Asia and Latin America?",
   choices=[
     "Each sought to change who held land and resources within its own state",
     "Each was organized by the same international party from a single headquarters",
     "Each was directed at the redistribution of territory between states rather than within them",
     "Each rejected any role for the state in economic life",
     "Each arose only in states that had never experienced colonial rule"],
   ans=0,
   why="KC-6.2.II.D.i states that movements to redistribute land and resources developed WITHIN states in Africa, Asia, and Latin America. The framework describes a common object, the internal distribution of land and resources, without asserting common organization or a common ideology."),

 dict(q="Two land reforms are compared. One is carried out by a communist government that abolishes private holdings; the other is carried out by a monarchy that buys estates and sells them in small lots. According to this course, how should the second be classified?",
   choices=[
     "As a movement to redistribute land and resources that did not advocate communism",
     "As an instance of communism, since any redistribution of land is communist",
     "As unrelated to redistribution, since a monarchy carried it out",
     "As a free-market liberalization of the kind associated with the late twentieth century",
     "As a proxy war of the kind the Cold War produced"],
   ans=0,
   why="KC-6.2.II.D.i states that redistribution movements sometimes advocated communism or socialism, which makes the advocacy a variable feature and the redistribution the defining one. A reform that changes who holds land is redistribution whoever carries it out, and the word sometimes is what forbids the communist reading."),

 dict(q="An unattributed newspaper editorial published in 1958 in a country conducting a state-directed economic campaign praises the campaign in identical language to every other paper in the country. That uniformity is best treated as evidence of",
   choices=[
     "the constraints under which publication took place rather than of the campaign's results",
     "the genuine unanimity of public opinion about the campaign",
     "the accuracy of the campaign's reported production figures",
     "the absence of any government interest in what newspapers printed",
     "the existence of a free market in newsprint and printing services"],
   ans=0,
   why="KC-6.3.I.A.ii records the government controlling the national economy and often implementing repressive policies, which bears directly on what could be printed. Uniform praise across all outlets is evidence about the conditions of publication, and inferring popular opinion from it would mistake a source's situation for its content."),

 dict(q="A researcher wants to test the claim that a particular redistribution programme improved the position of the poorest rural households. Which evidence would be most useful?",
   choices=[
     "Holdings and incomes recorded for those households before and after the programme",
     "The text of the speech in which the programme was announced",
     "The number of officials employed to administer the programme",
     "The programme's coverage in newspapers published in other countries",
     "A list of the countries that had adopted similar programmes elsewhere"],
   ans=0,
   why="KC-6.2.II.D.i describes movements to redistribute land and resources, so a claim about their effects is a claim about who ended up holding what. Announcements, staffing levels and foreign coverage report the programme's intentions or its profile rather than its outcome for the households in question."),

 dict(q="How does this course connect the Chinese case to the wider spread of communism after 1900?",
   choices=[
     "It presents the seizure of power in China as leading to communist revolution there, and treats redistribution movements elsewhere as sometimes advocating communism",
     "It presents China as the only state in which any redistribution of land occurred",
     "It presents the Chinese revolution as caused by land reform in Latin America",
     "It presents every redistribution movement outside China as directed from China",
     "It presents China as having rejected state control of its national economy"],
   ans=0,
   why="KC-6.2.I.i traces the Chinese sequence from internal tension and Japanese aggression to the seizure of power and then to communist revolution, while KC-6.2.II.D.i separately places redistribution movements in Africa, Asia, and Latin America that sometimes advocated communism or socialism. The framework connects the two as parallel developments and does not make one the agent of the other."),

 dict(q="A landowner's letter of 1953 predicts that a redistribution will ruin agriculture, and a government circular of the same year predicts that it will transform it. What can a historian most safely conclude from the pair?",
   choices=[
     "Both documents state expectations, and neither records what actually followed",
     "The government circular must be correct, because it was issued by the state",
     "The landowner's letter must be correct, because he farmed the land in question",
     "The two documents together establish the programme's eventual results",
     "Neither document has any value, because both concern the future"],
   ans=0,
   why="KC-6.2.II.D.i places these movements inside states where interested parties disagreed about them, and a prediction reports its author's expectation and interest. Distinguishing what a source's situation allows it to establish from what it merely asserts is the skill this topic practises."),

 dict(q="Which description of the relationship between state power and the economy in communist China does this course support?",
   choices=[
     "The government directed the national economy through campaigns it designed and enforced",
     "The government withdrew from the economy and left production to private firms",
     "The government transferred economic decisions to elected village assemblies",
     "The government confined its economic role to setting import tariffs",
     "The government left the economy to be managed by foreign investors"],
   ans=0,
   why="KC-6.3.I.A.ii states that in communist China the government controlled the national economy through the Great Leap Forward, often implementing repressive policies. Direction and enforcement by the state is the framework's own description, and each distractor describes a withdrawal of the state that the sentence contradicts."),

 dict(q="Suppose a student wishes to argue that redistribution movements were a response to conditions inside their own countries. What does this course's framework allow?",
   choices=[
     "The argument fits the framework, which places these movements within states in three world regions",
     "The argument fails, because the framework locates every such movement outside the state it changed",
     "The argument fails, because the framework describes no redistribution movements at all",
     "The argument fits only for Europe, the sole region the framework names",
     "The argument fails, because the framework attributes every movement to a single foreign sponsor"],
   ans=0,
   why="KC-6.2.II.D.i states that movements to redistribute land and resources developed within states in Africa, Asia, and Latin America. Within states is the framework's own wording, and it is what the student's argument needs; the framework attributes the movements to no single external sponsor."),

 dict(q="An oral history collected in the 1990s from former officials of a redistribution programme differs sharply from the programme's own contemporary paperwork. The most useful response is to",
   choices=[
     "read each against the other, asking what each was produced for and what each could not say",
     "discard the oral history, because memory is always mistaken about numbers",
     "discard the paperwork, because official records are always falsified",
     "average the two accounts and report the midpoint as the finding",
     "conclude that the programme never took place at all"],
   ans=0,
   why="KC-6.2.II.D.i and KC-6.3.I.A.ii describe programmes conducted by states with an interest in how they were recorded, and testimony gathered later that is free of that interest but subject to memory. Reading each source for its purpose and situation, which is this topic's skill, is what lets the two be used together."),

 dict(q="Which of the following best states the consequences of China's adoption of communism as this course presents them?",
   choices=[
     "The state took control of the national economy and its campaigns brought repression and harm to the population",
     "The state left the economy alone and living standards were unaffected by policy",
     "The state opened the economy to foreign ownership and no coercion occurred",
     "The state redistributed land only outside its own borders",
     "The state confined its policies to foreign affairs and did not touch production"],
   ans=0,
   why="KC-6.3.I.A.ii states that the government controlled the national economy through the Great Leap Forward, often implementing repressive policies, with negative repercussions for the population. The key reports the control, the repression and the harm together, which is what the framework's sentence asserts."),

 dict(q="Which of the following best states the causes of movements to redistribute economic resources as this course presents them?",
   choices=[
     "They arose within states in Africa, Asia and Latin America over the holding of land and resources, sometimes under a communist or socialist banner",
     "They arose only where a foreign army had already installed a government",
     "They arose from disputes between states about the location of their borders",
     "They arose from the growth of multinational corporations late in the century",
     "They arose only in states that had already abolished private property"],
   ans=0,
   why="KC-6.2.II.D.i states that movements to redistribute land and resources developed within states in Africa, Asia, and Latin America, sometimes advocating communism or socialism. The key preserves both the internal origin and the qualifier sometimes; the distractors substitute foreign agency, interstate disputes or a later economic development."),

 dict(q="Taking the topic as a whole, which single sentence best summarizes what this course says about the spread of communism after 1900?",
   choices=[
     "Communists took power in China amid internal tension and foreign aggression and then directed the economy at heavy cost to the population, while movements over land and resources arose across three world regions and only sometimes took a communist form",
     "Communism spread by agreement among governments and left economies and populations unchanged wherever it arrived",
     "Every movement over land and resources in the twentieth century was organized by communists from one centre",
     "Communism appeared only in Europe and had no bearing on Asia, Africa or Latin America",
     "Land redistribution occurred nowhere outside China during the twentieth century"],
   ans=0,
   why="KC-6.2.I.i supplies the Chinese conditions and outcome, KC-6.3.I.A.ii the state direction of the economy with repression and negative repercussions, and KC-6.2.II.D.i the redistribution movements across three regions that sometimes advocated communism or socialism. The key is the conjunction of those three sentences, and each distractor contradicts at least one."),
]
