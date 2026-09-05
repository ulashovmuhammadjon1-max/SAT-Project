# AP WORLD HISTORY: MODERN 7.2 Causes of World War I
# CED effective Fall 2026, Unit 7 Global Conflict, c. 1900 to the present.
# Thematic focus Governance (GOV). Unit 7 Learning Objective B: explain the
# causes and consequences of World War I. Suggested skill 1.B, explain a
# historical concept, development, or process.
#
# THE HISTORICAL DEVELOPMENT THIS TOPIC RESTS ON, in the framework's own words:
#   KC-6.2.IV.B.i  The causes of World War I included imperialist expansion and
#                  competition for resources. In addition, territorial and
#                  regional conflicts combined with a flawed alliance system and
#                  intense nationalism to escalate the tensions into global
#                  conflict.
#
# That single sentence names five things -- imperialist expansion, competition
# for resources, territorial and regional conflicts, a flawed alliance system,
# intense nationalism -- and one relationship: the last three COMBINED to
# escalate tensions into conflict on a global scale. Every key in this module
# is one of those five or that relationship.
#
# CONSEQUENCES. The learning objective covers consequences as well as causes,
# but this topic's own historical development states only causes. Where a
# consequence is keyed, the citation is to the sentence in the framework that
# supplies it: KC-6.2.IV.B.ii, which names the unsustainable peace settlement
# after World War I among the causes of World War II, and KC-6.1.III.C.i, which
# states that new military technology led to increased levels of wartime
# casualties.
#
# WHAT IS DELIBERATELY NOT ASKED. No item keys to a date, an assassination, a
# mobilisation order, a battle, a treaty clause or a named alliance bloc: the
# framework states none of them, and a question resting on them could not be
# checked by a later reader against the CED. No item asks which cause was the
# most important, because the sentence lists them without ranking; the relative
# significance of causes is topic 7.9's business, where the framework does ask
# for it.
#
# SOURCES. The bank cannot show images and the framework prints no document for
# this topic, so every stimulus is either an explicitly unattributed
# illustrative source or a table of illustrative data whose keyed conclusion is
# recoverable from the table alone. Nothing is attributed to a real person or
# document.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md.
TOPIC = ("7.2", "Causes of World War I", 7)

_T_TERRITORY = dict(
    headers=["Power (illustrative)",
             "Overseas territory held in 1880 (thousands of square kilometers)",
             "Overseas territory held in 1910 (thousands of square kilometers)"],
    rows=[["Power A", "2,400", "9,100"],
          ["Power B", "700", "5,600"],
          ["Power C", "150", "2,900"]])

_T_RESOURCE = dict(
    headers=["Power (illustrative)",
             "Share of its rubber consumed that is imported (percent)",
             "Share of its iron ore consumed that is imported (percent)"],
    rows=[["Power A", "100", "38"],
          ["Power B", "100", "61"],
          ["Power C", "100", "22"]])

QUESTIONS = [
 dict(q="An unattributed naval memorandum written before the First World War argues that the state must secure coaling stations along a distant trade route and acquire rubber-producing territory 'before our rivals close it to us.' The memorandum best illustrates which pair of causes named by the framework?",
   choices=[
     "Imperialist expansion together with competition for resources",
     "A flawed alliance system together with intense nationalism",
     "A regional territorial dispute together with an alliance obligation",
     "An economic depression together with the rise of totalitarian regimes",
     "A peace settlement together with the redrawing of borders"], ans=0,
   why="KC-6.2.IV.B.i states that the causes of World War I included imperialist expansion and competition for resources. Acquiring distant territory is expansion and securing a supply of rubber before a rival does is competition for a resource, so the memorandum names one of each."),
 dict(q="Which of the following is NOT among the causes of the First World War that the framework names?",
   choices=[
     "A global economic depression",
     "Imperialist expansion",
     "Competition for resources",
     "A flawed alliance system",
     "Intense nationalism"], ans=0,
   why="KC-6.2.IV.B.i lists imperialist expansion, competition for resources, territorial and regional conflicts, a flawed alliance system and intense nationalism. The framework assigns the global economic crisis engendered by the Great Depression to the causes of the second war, in KC-6.2.IV.B.ii, not to the first."),
 dict(q="According to the framework, which combination escalated existing tensions into a conflict on a global scale?",
   choices=[
     "Territorial and regional conflicts, a flawed alliance system, and intense nationalism",
     "A peace settlement, an economic crisis, and the rise of fascist regimes",
     "Advances in medicine, communication, and transportation acting together",
     "The collapse of the older land-based empires and the communist revolution that followed",
     "Government control of the national economy through a series of five-year plans"], ans=0,
   why="KC-6.2.IV.B.i states that territorial and regional conflicts combined with a flawed alliance system and intense nationalism to escalate the tensions into global conflict. The other combinations belong to KC-6.2.IV.B.ii, KC-6.1, KC-6.2.I.A and KC-6.3.I.A.i, which describe other developments."),
 dict(q="What role does the framework assign to the alliance system among the causes of the war?",
   choices=[
     "The alliances helped escalate regional tensions into a conflict on a global scale",
     "The alliances prevented any regional dispute from becoming a war at all",
     "The alliances were formed only after the fighting had begun",
     "The alliances are described as the sole cause of the war",
     "The alliances concerned trade alone and had no military content"], ans=0,
   why="KC-6.2.IV.B.i calls the alliance system flawed and places it among the things that combined to escalate tensions into global conflict. Escalation is the function the sentence gives it, and the same sentence names other causes beside it, so it cannot be the sole cause."),
 dict(q="An unattributed editorial published shortly before the war praises the writer's nation as superior to all its neighbours and demands the recovery of a province across the border where people speaking the same language live. The editorial best illustrates",
   choices=[
     "Intense nationalism joined to a territorial dispute",
     "Competition for a scarce industrial resource",
     "An alliance obligation binding one state to another",
     "The transfer of a colony under a treaty settlement",
     "A government taking a more active role in economic life"], ans=0,
   why="KC-6.2.IV.B.i names territorial and regional conflicts and intense nationalism among the things that combined to escalate tensions. A claim of national superiority is the first and a demand for a neighbouring province is the second."),
 dict(q="A dispute between two neighbouring states draws in states on several continents within weeks. Which cause named by the framework most directly accounts for that change of scale?",
   choices=[
     "The flawed alliance system, which bound states to one another's quarrels",
     "Competition for rubber and other tropical resources",
     "The spread of new agricultural techniques",
     "Government intervention in the national economy",
     "The redrawing of colonial borders by treaty"], ans=0,
   why="KC-6.2.IV.B.i has the alliance system combining with regional conflict and nationalism to escalate tensions into global conflict. Of the causes it names, the alliance system is the one that links additional states to a quarrel that was not originally theirs."),
 dict(q="The table below reports illustrative holdings of overseas territory for three powers at two dates before the First World War. Which conclusion is best supported by the data as given?",
   table=_T_TERRITORY,
   choices=[
     "All three powers expanded their overseas holdings, and Power C multiplied its holdings by the largest factor",
     "All three powers expanded their overseas holdings, and Power A multiplied its holdings by the largest factor",
     "Only one of the three powers expanded its overseas holdings in this period",
     "The three powers held equal amounts of overseas territory at the later date",
     "Every power's holdings were smaller at the later date than at the earlier one"], ans=0,
   why="Read from the table alone: every power's holding is larger at the later date, and dividing each later value by its earlier one shows that the power with the smallest starting holding grew by the greatest multiple. This is the imperialist expansion that KC-6.2.IV.B.i names among the causes of the war."),
 dict(q="The table below reports illustrative import shares for two industrial materials in three powers. Which conclusion is best supported?",
   table=_T_RESOURCE,
   choices=[
     "Every power depends entirely on imports for one of the two materials, and Power B is the most import-dependent for the other",
     "Every power depends entirely on imports for one of the two materials, and Power C is the most import-dependent for the other",
     "Only one of the three powers imports any of either material",
     "Each power supplies all of its own needs for both materials",
     "The three powers depend on imports to the same degree for both materials"], ans=0,
   why="Read from the table alone: one column is at its maximum for all three powers, and in the other column one power stands above the rest. A state that must import what its industry consumes has an interest in the territory that supplies it, which is the competition for resources KC-6.2.IV.B.i names."),
 dict(q="A student asks what the framework says about the settlement that ended the First World War. The best answer is that",
   choices=[
     "the settlement is itself named among the causes of the next war, as an unsustainable peace",
     "the settlement is described as having removed the causes of further conflict",
     "the framework says nothing at all about the years after the fighting stopped",
     "the settlement is described as a cause of the First World War rather than a consequence",
     "the settlement is described as having dissolved every empire immediately"], ans=0,
   why="KC-6.2.IV.B.ii lists the unsustainable peace settlement after World War I first among the causes of World War II. That is the framework's own statement of a consequence of the first war, and it is the opposite of a settlement that removed the causes of conflict."),
 dict(q="Two industrial states each need a mineral that neither produces in quantity, and each seeks exclusive access to the region where it is found. The framework would classify this situation under which of its named causes?",
   choices=[
     "Competition for resources",
     "A flawed alliance system",
     "Intense nationalism",
     "The rise of totalitarian regimes",
     "The onset of a global economic crisis"], ans=0,
   why="KC-6.2.IV.B.i names competition for resources among the causes of World War I. Two states seeking exclusive access to the same supply is that competition; the other four are either different causes in the same sentence or belong to KC-6.2.IV.B.ii."),
 dict(q="Which research question would a historian working from this topic's learning objective be best placed to answer?",
   choices=[
     "What were the causes and the consequences of the First World War",
     "Which general commanded each army during the First World War",
     "How were rifles manufactured in the years before the First World War",
     "Which languages were spoken in the capitals of the belligerent states",
     "How did the climate of Europe change during the First World War"], ans=0,
   why="Unit 7 Learning Objective B asks students to explain the causes and consequences of World War I, so an inquiry framed as causes and consequences restates the objective. The other four ask about matters the objective does not name."),
 dict(q="An unattributed government circular issued before the war instructs schoolteachers to teach that the nation's people are one family with a single destiny and that neighbouring peoples are its natural rivals. The circular is best used as evidence of",
   choices=[
     "the intense nationalism the framework names among the war's causes",
     "the competition for resources the framework names among the war's causes",
     "an alliance obligation entered into with another state",
     "a government taking a more active role in economic life",
     "the transfer of territory under a treaty settlement"], ans=0,
   why="KC-6.2.IV.B.i names intense nationalism among the things that combined to escalate tensions into global conflict. Instruction in national unity and in the hostility of neighbours is the cultivation of exactly that sentiment; nothing in the circular concerns resources, alliances, the economy or territory transferred by treaty."),
 dict(q="Why is a war that began with a dispute in one region described by the framework as a global conflict?",
   choices=[
     "Because tensions were escalated until states in many parts of the world were at war",
     "Because the original dispute was itself worldwide from the outset",
     "Because the fighting was confined to the colonies rather than to Europe",
     "Because the war was fought entirely at sea and therefore touched every ocean",
     "Because it was the first war in which any state used a written alliance"], ans=0,
   why="KC-6.2.IV.B.i describes territorial and regional conflicts combining with the alliance system and nationalism to escalate the tensions into global conflict. The scale is the product of escalation from a regional starting point rather than a property the dispute had at the start."),
 dict(q="A historian argues that the war can be explained by nationalism alone. Using this topic's historical development, the strongest objection is that",
   choices=[
     "the framework names nationalism as one of several things that combined, not as a cause acting by itself",
     "the framework does not mention nationalism among the war's causes at all",
     "the framework describes nationalism as a consequence of the war rather than a cause",
     "the framework describes nationalism as confined to states outside Europe",
     "the framework treats nationalism as identical to imperialist expansion"], ans=0,
   why="KC-6.2.IV.B.i lists imperialist expansion and competition for resources, then has territorial and regional conflicts combine with a flawed alliance system and intense nationalism. Nationalism appears as one term in a combination, so a single-cause account drops the rest of the sentence."),
 dict(q="Which of the following pieces of evidence would most directly support a claim that imperialist expansion was among the causes of the war?",
   choices=[
     "Records of rival states claiming the same overseas territory in the decades before the war",
     "Records of the number of schools built in each state before the war",
     "Records of the crops grown in each state's home provinces",
     "Records of the number of newspapers published in each capital",
     "Records of the ceremonial titles held by each state's ruler"], ans=0,
   why="KC-6.2.IV.B.i names imperialist expansion among the causes. Evidence that expanding states were claiming the same territory bears directly on that cause, whereas schools, crops, newspapers and titles bear on it only by a chain of inference the framework does not supply."),
 dict(q="An unattributed diplomatic note sent before the war states that if a third state moves against the sender's partner, the sender 'will not stand aside.' The note is best used as evidence about",
   choices=[
     "the alliance system that the framework describes as flawed",
     "the competition for resources between industrial economies",
     "the intensity of national feeling among the sender's population",
     "the sender's plans for expansion into overseas territory",
     "the terms of the settlement that would follow the war"], ans=0,
   why="KC-6.2.IV.B.i names a flawed alliance system among the things that escalated tensions into global conflict. A written undertaking to join a partner's war is that system in operation, and the note says nothing about resources, popular feeling, expansion or a future settlement."),
 dict(q="Which statement best explains why the framework calls the causes of the war multiple rather than single?",
   choices=[
     "The framework's own sentence lists several causes and describes three of them as combining",
     "The framework states that historians have never identified any cause of the war",
     "The framework identifies one cause but says it operated in several regions",
     "The framework treats the war as having no causes that can be studied",
     "The framework states that the causes were the same as those of the second war"], ans=0,
   why="KC-6.2.IV.B.i names imperialist expansion and competition for resources, and then has territorial and regional conflicts combine with a flawed alliance system and intense nationalism. Both the list and the word 'combined' are in the sentence itself."),
 dict(q="A state annexes a neighbouring district inhabited by people it claims as its own, and a rival state objects that its own interests in the region are threatened. This is best classified as",
   choices=[
     "a territorial and regional conflict of the kind the framework names",
     "a resource shortage caused by the failure of a harvest",
     "an economic crisis of the kind that preceded the second war",
     "a peace settlement imposed on a defeated power",
     "an act of government intervention in the national economy"], ans=0,
   why="KC-6.2.IV.B.i names territorial and regional conflicts among the things that combined to escalate tensions into global conflict. A disputed annexation objected to by a neighbouring rival is a conflict about territory in a region, and none of the other four descriptions fits the situation."),
 dict(q="How does the framework relate the causes it names to one another?",
   choices=[
     "It presents them as operating together rather than in isolation",
     "It presents them in a strict order of importance from first to last",
     "It presents each as sufficient on its own to have produced the war",
     "It presents them as alternatives, only one of which can be true",
     "It presents them as causes of the second war rather than the first"], ans=0,
   why="KC-6.2.IV.B.i uses the word 'combined' for three of its causes and adds the other two with 'included' and 'in addition'. The sentence therefore asserts joint operation, and it supplies no ranking, which is why the relative significance of causes is left to Unit 7 Learning Objective I."),
 dict(q="Which consequence of the war does the framework state directly?",
   choices=[
     "New military technology led to increased levels of wartime casualties",
     "Every colonial empire was dissolved before the fighting ended",
     "Industrial production ceased in all of the belligerent states",
     "The alliance system was abolished by agreement among the powers",
     "Competition for resources ended with the signing of the peace"], ans=0,
   why="KC-6.1.III.C.i states that new military technology led to increased levels of wartime casualties, which the framework attaches to the conduct of the First World War in topic 7.3. The other four assert outcomes that appear nowhere in the framework."),
 dict(q="A source produced by a government at war blames the enemy alone for starting it. What is the most significant limitation on the use of that source for studying the war's causes?",
   choices=[
     "Its purpose is to justify the government's own conduct, so it has reason to omit causes that implicate its state",
     "It was written in the period it describes, which makes it unusable",
     "It concerns politics rather than economics, so it cannot bear on causes",
     "It was published rather than kept secret, so its contents cannot be checked",
     "It names a specific enemy, which no source about a war can do"], ans=0,
   why="KC-6.2.IV.B.i names causes, including imperialist expansion and competition for resources, that would implicate more than one state. A belligerent government's account has an interest in leaving those out, which is a limit on the source's use rather than a reason to discard it."),
 dict(q="Two states with no dispute between them find themselves at war with one another. Which of the framework's causes best explains that outcome?",
   choices=[
     "The alliance system drew each into a quarrel that began elsewhere",
     "Each had exhausted its own supply of a strategic resource",
     "Each had annexed territory belonging to the other",
     "Each had experienced a collapse of its own government",
     "Each had signed the peace settlement that followed the war"], ans=0,
   why="KC-6.2.IV.B.i describes a flawed alliance system combining with regional conflict and nationalism to escalate tensions into global conflict. Alliances are what put a state into a war it had no quarrel of its own to fight."),
 dict(q="Which of the following would be the best contextual opening for an essay on why the war became worldwide rather than regional?",
   choices=[
     "A statement that European powers had been expanding into other regions and competing for their resources for decades",
     "A statement that the war's battles were fought in a small number of provinces",
     "A statement that soldiers on both sides used similar rifles",
     "A statement that the war ended with a signed settlement",
     "A statement that the belligerents had similar systems of schooling"], ans=0,
   why="KC-6.2.IV.B.i places imperialist expansion and competition for resources among the causes, and those two operate across regions rather than within one. An essay on the war's global scale is therefore best opened with the process that had already made the powers' interests global."),
 dict(q="Which pairing correctly matches a cause named by the framework with a piece of evidence that would bear on it?",
   choices=[
     "Competition for resources, evidenced by rival claims to the same mineral-bearing territory",
     "Competition for resources, evidenced by the number of alliance treaties signed",
     "Intense nationalism, evidenced by the tonnage of ore imported each year",
     "The alliance system, evidenced by the size of the annual grain harvest",
     "Imperialist expansion, evidenced by the number of newspapers printed in the capital"], ans=0,
   why="KC-6.2.IV.B.i names competition for resources as a cause, and rival claims to a mineral-bearing territory are evidence of exactly that competition. The other four pairings attach evidence to a cause it does not bear on."),
 dict(q="An unattributed pamphlet published during the war argues that the fighting arose because 'the powers had already divided the world between them and could enlarge their share only at one another's expense.' This argument corresponds most closely to which cause named by the framework?",
   choices=[
     "Imperialist expansion",
     "A flawed alliance system",
     "The peace settlement that followed the war",
     "The rise of fascist and totalitarian regimes",
     "Government control of the national economy"], ans=0,
   why="KC-6.2.IV.B.i names imperialist expansion among the causes of World War I. A pamphlet describing powers that can grow only by taking from one another is describing that expansion reaching its limit, not an alliance, a settlement, a regime type or an economic policy."),
 dict(q="Which of the following statements about the framework's account of the war's origins is accurate?",
   choices=[
     "It names causes in more than one domain, including the economic and the political",
     "It names a single economic cause and no political ones",
     "It names a single political cause and no economic ones",
     "It names only causes internal to one state",
     "It declines to identify any cause of the war"], ans=0,
   why="KC-6.2.IV.B.i names competition for resources and imperialist expansion, which are economic as well as political, alongside territorial conflict, alliances and nationalism, which are political. The sentence therefore spans more than one domain."),
 dict(q="A state's leaders believe that acquiring more territory abroad is necessary to secure raw materials for its factories. This belief connects which two of the framework's causes?",
   choices=[
     "Imperialist expansion and competition for resources",
     "The alliance system and intense nationalism",
     "Territorial conflict and the peace settlement",
     "Intense nationalism and government control of the economy",
     "Competition for resources and the rise of totalitarian regimes"], ans=0,
   why="KC-6.2.IV.B.i names imperialist expansion and competition for resources in the same clause. A justification of expansion by the need for raw materials is the point at which the two meet, and neither the alliance system nor nationalism is involved in the reasoning described."),
 dict(q="Suppose evidence showed that no state had any territorial dispute with a neighbour in the years before the war. Which part of the framework's account would be most weakened?",
   choices=[
     "The claim that territorial and regional conflicts were among the things that escalated tensions",
     "The claim that imperialist expansion was a cause of the war",
     "The claim that competition for resources was a cause of the war",
     "The claim that new military technology increased wartime casualties",
     "The claim that the peace settlement was unsustainable"], ans=0,
   why="KC-6.2.IV.B.i lists territorial and regional conflicts first among the three things that combined to escalate tensions. Removing them would remove one term of that combination, while leaving the separate claims about expansion, resources, technology and the settlement untouched."),
 dict(q="Why does this topic's suggested skill, explaining a historical development or process, fit the study of the war's origins particularly well?",
   choices=[
     "Because the framework presents the origins as a process in which several causes combined over time",
     "Because the framework presents the origins as a single event on a single day",
     "Because the framework presents the origins as unknowable",
     "Because the framework presents the origins as identical in every state",
     "Because the framework presents the origins as belonging to the period after 1945"], ans=0,
   why="Suggested skill 1.B asks students to explain a historical concept, development or process, and KC-6.2.IV.B.i describes causes that combined to escalate tensions. A combination unfolding over time is a process rather than an event."),
 dict(q="A student claims that the causes of the two world wars are the same in the framework's account. What is the best correction?",
   choices=[
     "The framework gives the second war its own list of causes, including an unsustainable peace settlement and a global economic crisis",
     "The framework gives the two wars an identical list of causes",
     "The framework gives causes for the first war only and none for the second",
     "The framework gives causes for the second war only and none for the first",
     "The framework denies that either war had causes that can be identified"], ans=0,
   why="KC-6.2.IV.B.i lists the causes of the first war and KC-6.2.IV.B.ii lists those of the second, which include the unsustainable peace settlement after World War I, the global economic crisis engendered by the Great Depression, continued imperialist aspirations and the rise of fascist and totalitarian regimes. The two lists overlap but are not the same."),
]
