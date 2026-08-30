# AP HUMAN GEOGRAPHY 4.1 Introduction to Political Geography -- 30 questions
# CED (2020 framework), Unit 4 Political Patterns and Processes.
# Enduring understanding PSO-4: the political organization of space results from
# historical and current processes, events, and ideas.
#
# Learning objective PSO-4.A: for world political maps, (a) define the different
# types of political entities and (b) explain their spatial relationships.
#
# Essential knowledge this module rests on:
#   PSO-4.A.1  Independent states are the primary building blocks of the world
#              political map.
#   PSO-4.A.2  Types of political entities include nations, nation-states,
#              stateless nations, multinational states, multistate nations, and
#              autonomous and semiautonomous regions, such as Native American
#              reservations.
#
# The CED's list in PSO-4.A.2 is a CLOSED list of six entity types, and that is
# what makes this topic testable as application rather than recall: every item
# below hands the student a described territory and asks which of the six it is.
# The four properties of an independent state -- defined territory, permanent
# population, an effective government, and recognized sovereignty -- are treated
# as the content of PSO-4.A.1's word "independent", because the framework names
# independent states as the building blocks without unpacking the adjective.
#
# Suggested skill 4.A, identify the different types of information presented in
# visual sources: items 12, 21 and 28 carry real data tables rather than a prose
# description of one.
#
# FIVE choices (A-E), matching the real AP Human Geography exam.
TOPIC = ("4.1", "Introduction to Political Geography", 4)
QUESTIONS = [
 dict(q="A territory has a permanent population, a clearly bounded area, a government that controls that area, and recognition from most other governments. Which political entity does it satisfy the criteria for?", choices=[
   "An independent state",
   "A nation",
   "A stateless nation",
   "An autonomous region",
   "A multistate nation"], ans=0,
   why="Those four properties -- territory, population, effective government, and recognized sovereignty -- are what make an entity independent, and PSO-4.A.1 names independent states as the primary building blocks of the world political map. The other four entities are defined by culture or by a grant of internal authority, not by sovereignty."),
 dict(q="Kurds live in adjoining parts of Turkey, Iraq, Iran, and Syria, share a language and a sense of common descent, and govern none of those states. Geographers classify the Kurds as", choices=[
   "a stateless nation",
   "a nation-state",
   "a multinational state",
   "an autonomous region",
   "a supranational organization"], ans=0,
   why="A nation is a people with a shared identity and a claim to a territory; the Kurds have that identity but no sovereign state of their own, which is precisely the stateless-nation case in PSO-4.A.2. The territory being split among four states is what rules out the nation-state reading."),
 dict(q="Iceland's population is overwhelmingly of one cultural group, that group's homeland is the island, and the island is a sovereign state. This close match makes Iceland an unusually clear example of", choices=[
   "a nation-state",
   "a multinational state",
   "a stateless nation",
   "a multistate nation",
   "a semiautonomous region"], ans=0,
   why="A nation-state is the case where the territory of a nation and the territory of a state coincide. Iceland is cited because near-perfect coincidence is rare -- most states in PSO-4.A.2's list contain several nations, which is why the multinational category exists at all."),
 dict(q="The Russian Federation contains Tatars, Chechens, Bashkirs, and dozens of other peoples with distinct languages and homelands inside its borders. This makes Russia", choices=[
   "a multinational state",
   "a multistate nation",
   "a nation-state",
   "a stateless nation",
   "an autonomous region"], ans=0,
   why="The prefix attaches to the noun that is plural: many nations inside one state is a multinational state, whereas one nation spread across several states is a multistate nation. Russia has the first pattern, so reversing the terms is the error the question is built to catch."),
 dict(q="Korean identity, language, and historical homeland span both North Korea and South Korea, two separate sovereign states. Koreans are therefore best described as", choices=[
   "a multistate nation",
   "a multinational state",
   "a nation-state",
   "a stateless nation",
   "a semiautonomous region"], ans=0,
   why="One nation whose members are divided among two or more sovereign states is a multistate nation. Koreans are not stateless -- they have two states -- which is what separates this case from the Kurdish one."),
 dict(q="Which situation would give geographers the strongest reason to call a territory a semiautonomous region rather than an independent state?", choices=[
   "It runs its own schools, courts, and police, but the national government controls its foreign policy and defense",
   "It has its own flag, anthem, and national holiday",
   "Its population speaks a language different from the national majority",
   "It is separated from the rest of the country by a mountain range",
   "It sends elected representatives to the national legislature"], ans=0,
   why="Autonomy is a grant of internal self-government; sovereignty is the right to act externally as a state. A region that runs its internal affairs but cannot conduct its own foreign or defense policy has the first without the second. Flags, distinct languages, physical separation, and legislative representation are all common inside ordinary provinces and settle nothing."),
 dict(q="A federally recognized Native American reservation in the United States operates its own tribal government and courts while remaining within United States territory. The CED classifies such a territory as", choices=[
   "an autonomous or semiautonomous region",
   "an independent state",
   "a stateless nation",
   "a multistate nation",
   "a supranational organization"], ans=0,
   why="PSO-4.A.2 names autonomous and semiautonomous regions and gives Native American reservations as its own example. The reservation exercises real internal authority but not sovereignty, so it is neither a state nor merely a cultural group without territory."),
 dict(q="A geographer argues that a group is a nation but not a state. The evidence that would most directly support that argument is that the group", choices=[
   "shares a language and a homeland but has no government recognized as sovereign over it",
   "occupies a territory with clearly surveyed and demarcated boundaries",
   "is a member of several international trade organizations",
   "elects representatives to a national parliament",
   "has a larger population than several neighboring countries"], ans=0,
   why="The distinction turns on sovereignty, not on size, boundaries, or participation in institutions. Shared identity plus an absence of recognized sovereign authority is exactly the nation-without-a-state condition."),
 dict(q="Which pairing of a political entity with its defining feature is correct?", choices=[
   "Multinational state -- one sovereign government ruling several distinct peoples",
   "Nation-state -- several sovereign governments ruling one people",
   "Stateless nation -- a sovereign government with no permanent population",
   "Multistate nation -- one government administering several dependent colonies",
   "Autonomous region -- a fully sovereign entity conducting its own foreign policy"], ans=0,
   why="Only the first pairing keeps the plural on the right noun. The second describes a multistate nation, the third is not a coherent entity at all, the fourth describes an empire, and the fifth contradicts what autonomy means -- autonomy is internal authority granted by a sovereign, not sovereignty itself."),
 dict(q="Vatican City covers less than half a square kilometer, has a few hundred residents, its own government, and diplomatic recognition. Its size means that it is", choices=[
   "still an independent state, because sovereignty does not depend on area",
   "a semiautonomous region of Italy",
   "a stateless nation within Italy",
   "a multistate nation of Catholics",
   "a dependency administered by the United Nations"], ans=0,
   why="The criteria for statehood are territory, population, government, and recognition -- none of them specifies a minimum. Microstates are the case that shows the criteria are qualitative, which is why the CED calls independent states the building blocks without any size threshold."),
 dict(q="Antarctica has no permanent population and no single recognized government, and several states maintain overlapping claims there under a treaty that suspends them. On a world political map Antarctica is therefore", choices=[
   "not an independent state, because it lacks a permanent population and a sovereign government",
   "an independent state, because its boundaries are precisely known",
   "a multinational state, because researchers from many nations live there",
   "an autonomous region of the United Nations",
   "a stateless nation of Antarctic researchers"], ans=0,
   why="Two of the four statehood criteria are missing outright. Precisely known coastlines satisfy the territory criterion alone, and rotating research staff are neither a permanent population nor a nation with a shared homeland identity."),
 dict(table=dict(headers=["Group", "Population (millions)"],
   rows=[["Group W", "18.0"], ["Group X", "12.0"], ["Group Y", "6.0"], ["Group Z", "4.0"]]),
   q="A sovereign state's four largest cultural groups are listed in the accompanying table, and each has a distinct language and a historic home region inside the state. The largest group's share of the total listed population is", choices=[
   "45 percent",
   "18 percent",
   "40 percent",
   "50 percent",
   "60 percent"], ans=0,
   why="The four groups total 40.0 million, and 18.0 of 40.0 is 45 percent. The figure matters for the topic because no group holds a majority, so the state is multinational in fact and not only in name."),
 dict(q="A student says that because the population of a country speaks four different languages, the country cannot be a state. The best correction is that", choices=[
   "cultural diversity has no bearing on statehood, which is a matter of sovereignty over a defined territory",
   "a state must have a single official language to be recognized",
   "the country is a stateless nation until one language becomes dominant",
   "the country is a multistate nation because of its four languages",
   "statehood requires that all residents share a common ancestry"], ans=0,
   why="Statehood is a political condition -- territory, population, government, recognition -- and says nothing about cultural homogeneity. Cultural homogeneity is what distinguishes a nation-state from a multinational state, which is a different question from whether a state exists."),
 dict(q="Which of these would most strengthen a claim that a territory has achieved sovereignty in practice rather than only on paper?", choices=[
   "Its government collects taxes and enforces law throughout the territory without another state's permission",
   "It has declared independence in a written proclamation",
   "It has adopted a constitution modeled on a neighboring state's",
   "It has designed a national flag and currency",
   "Its people share a single language and religion"], ans=0,
   why="Effective control -- the ability to govern the territory without another state's leave -- is the test that separates a functioning state from a declaration. Documents, symbols, and cultural unity can all exist in a territory that some other government actually runs."),
 dict(q="Belgium's Flemish and Walloon communities each have their own language, their own region, and their own regional institutions inside one sovereign state. Belgium therefore illustrates", choices=[
   "a multinational state that has devolved power to its regions",
   "a nation-state with two official languages",
   "a multistate nation divided between two countries",
   "a stateless nation seeking recognition",
   "a supranational organization of two member states"], ans=0,
   why="Two nations inside one sovereign state is the multinational pattern, and the grant of regional institutions is the devolution PSO-4.A.2's autonomous-region category describes. Nothing here crosses an international boundary, which is what a multistate nation would require."),
 dict(q="Comparing Japan with Nigeria, the sharpest political-geographic contrast is that", choices=[
   "Japan approaches a nation-state while Nigeria is strongly multinational",
   "Japan is a multistate nation while Nigeria is a nation-state",
   "Japan is a stateless nation while Nigeria is an autonomous region",
   "neither is an independent state, since both were once occupied",
   "both are multistate nations because both have overseas populations"], ans=0,
   why="Japan's population is drawn overwhelmingly from one national group, so state and nation nearly coincide; Nigeria contains Hausa-Fulani, Yoruba, Igbo, and hundreds of smaller groups under one sovereign government. Emigrant communities abroad do not make a multistate nation, which requires the nation's homeland itself to straddle state borders."),
 dict(q="Which observation about a territory would be the weakest evidence that it is an independent state?", choices=[
   "Its residents strongly identify with a shared culture and history",
   "It maintains embassies in other countries",
   "It is a voting member of the United Nations General Assembly",
   "It signs treaties in its own name",
   "It controls entry across its own borders"], ans=0,
   why="Shared culture and history define a nation, not a state; every one of the other four observations is an exercise of sovereignty that only a state can perform. This is the recurring trap in the topic -- cultural evidence is offered where political evidence is required."),
 dict(q="Palestinians and Basques are often grouped together in this course because both", choices=[
   "constitute nations that lack a fully sovereign state of their own",
   "govern autonomous regions with their own foreign policies",
   "form multistate nations with two recognized sovereign governments",
   "are minorities within nation-states that have no internal divisions",
   "were created by the boundary decisions of the Berlin Conference"], ans=0,
   why="Both are groups with a shared identity and a claimed homeland that do not hold full sovereignty, which is what PSO-4.A.2 means by a stateless nation. Autonomy arrangements that either has grant internal authority only, and neither case originates in the Berlin Conference."),
 dict(q="A sovereign state grants one of its regions its own parliament, control of health and education, and the right to set some taxes, while retaining control of the currency, the armed forces, and treaty-making. This arrangement is best labeled", choices=[
   "regional autonomy within a single sovereign state",
   "the creation of a new independent state",
   "the formation of a multistate nation",
   "the dissolution of the state into a supranational union",
   "the recognition of a stateless nation as sovereign"], ans=0,
   why="The retained powers -- currency, defense, treaties -- are the external attributes of sovereignty, so no new state has come into being. What has been transferred is internal self-government, which is exactly the autonomous-region category."),
 dict(q="Which of the following best explains why the number of independent states on the world political map rose sharply after 1945?", choices=[
   "Colonies in Africa and Asia gained independence and were recognized as sovereign states",
   "Existing states merged into larger units to gain economic power",
   "Stateless nations were reclassified as autonomous regions",
   "International organizations replaced states as the primary units of the map",
   "Multistate nations consolidated into single nation-states"], ans=0,
   why="Decolonization converted dependent territories into recognized sovereign states, which is what adds building blocks to the political map under PSO-4.A.1. Mergers and consolidations would reduce the count, and reclassifying an entity that was never sovereign adds nothing to it."),
 dict(table=dict(headers=["State", "Largest cultural group as share of population"],
   rows=[["State J", "96%"], ["State K", "51%"], ["State L", "29%"], ["State M", "88%"]]),
   q="Using only the shares in the accompanying table, which state is the strongest candidate for classification as a multinational state?", choices=[
   "State L, because no group is close to a majority",
   "State J, because one group is nearly the whole population",
   "State M, because one group holds a large majority",
   "State K, because one group holds a bare majority",
   "None of them, because the table does not report the number of groups"], ans=0,
   why="A multinational state is one in which several nations live under one government, so the lower the largest group's share, the more of the population belongs to other groups. At 29 percent the remaining 71 percent must be divided among others, which is the strongest evidence in the table. The high-share states point the other way, toward a nation-state."),
 dict(q="A geographer studying political entities at the global scale would treat which unit as the basic building block of the analysis?", choices=[
   "The independent state",
   "The autonomous region",
   "The metropolitan area",
   "The cultural hearth",
   "The electoral district"], ans=0,
   why="PSO-4.A.1 says so directly: independent states are the primary building blocks of the world political map. The other units exist at subnational scales or are cultural rather than political, so a world political map is not assembled out of them."),
 dict(q="Hong Kong has its own legal system, currency, and immigration controls while China conducts its foreign relations and defense. Hong Kong is therefore best classified as", choices=[
   "a semiautonomous region of a sovereign state",
   "an independent state with limited recognition",
   "a stateless nation within China",
   "a multistate nation shared with China",
   "a supranational organization of Chinese cities"], ans=0,
   why="Extensive internal authority combined with no control over foreign policy or defense is the defining shape of semiautonomy. Immigration controls and a separate currency are internal powers a sovereign may delegate, so they do not by themselves establish statehood."),
 dict(q="Which statement about the relationship between nations and states is accurate?", choices=[
   "A nation is a cultural group, a state is a political unit, and the two need not have the same territory",
   "Every nation governs exactly one state",
   "Every state contains exactly one nation",
   "Nations and states are synonyms in political geography",
   "A state must be larger in area than the nation it contains"], ans=0,
   why="The whole point of the six-part list in PSO-4.A.2 is that the cultural map and the political map do not align: hence stateless nations, multinational states, and multistate nations, each of which is a different kind of mismatch. If the terms were synonyms none of those categories could exist."),
 dict(q="Territorial claims by several states over the same island group most directly complicate which criterion for statehood?", choices=[
   "Recognized sovereignty over a defined territory",
   "The presence of a permanent population",
   "The existence of an organized government",
   "Membership in a supranational organization",
   "The sharing of a common language"], ans=0,
   why="A contested claim means other governments do not accept one state's authority there, which strikes at recognition and at the definiteness of the territory. Population, government, language, and organizational membership are unaffected by who else claims the rocks."),
 dict(q="Greenland has its own parliament and controls most domestic policy, while Denmark retains responsibility for defense and foreign affairs. In this course Greenland is best used as an example of", choices=[
   "an autonomous region rather than an independent state",
   "an independent state that shares a monarch with Denmark",
   "a stateless nation with no territorial base",
   "a multinational state containing Danes and Inuit",
   "a multistate nation spread across the Arctic"], ans=0,
   why="Home rule over domestic policy with defense and foreign affairs reserved is autonomy, the same test applied to Hong Kong earlier in this module. Greenland does have a territorial base, which is what rules out the stateless-nation reading."),
 dict(q="Two neighboring states each contain a large population of the same ethnic group, whose historic homeland straddles the border between them. This situation is most likely to produce", choices=[
   "pressure for the group's territory on both sides of the border to be joined",
   "the automatic dissolution of both states",
   "the reclassification of both states as nation-states",
   "the disappearance of the group's shared identity",
   "the transfer of the border dispute to a supranational parliament"], ans=0,
   why="A nation divided by an international boundary is the multistate-nation case, and the characteristic political consequence is a demand to unite the divided homeland. Nothing about the situation dissolves states, erases identity, or makes either state culturally homogeneous."),
 dict(table=dict(headers=["Entity", "Own foreign policy", "Own internal laws", "UN membership"],
   rows=[["Entity P", "Yes", "Yes", "Yes"], ["Entity Q", "No", "Yes", "No"],
         ["Entity R", "No", "No", "No"], ["Entity S", "No", "Yes", "No"]]),
   q="Using the accompanying table of powers exercised by four entities, which one is an independent state?", choices=[
   "Entity P, because it conducts its own foreign policy and is recognized internationally",
   "Entity Q, because it makes its own internal laws",
   "Entity R, because it exercises no listed powers",
   "Entity S, because it makes its own internal laws",
   "All four, because each occupies a defined territory"], ans=0,
   why="Conducting foreign policy in one's own name and being seated at the United Nations are exercises of external sovereignty, which only a state has. Making internal law is a power an autonomous region also holds, so the two entities that have that alone are semiautonomous, not sovereign."),
 dict(q="Which change would convert a stateless nation into a nation-state?", choices=[
   "Achieving recognized sovereignty over a territory that is its homeland",
   "Gaining seats in the legislature of the state it currently lives in",
   "Being granted a reservation with its own tribal courts",
   "Having its language made co-official across several countries",
   "Migrating so that its members are spread across more states"], ans=0,
   why="A nation-state requires the nation's territory and a sovereign state's territory to coincide, so the missing ingredient for a stateless nation is sovereignty over its homeland. Legislative seats, reservations, and language status all leave the group short of sovereignty, and dispersal moves it toward the multistate-nation case instead."),
 dict(q="At which scale of analysis is the distinction between a unitary map of independent states and the underlying map of nations most visible?", choices=[
   "The global scale, where state borders can be compared with the distribution of cultural groups",
   "The neighborhood scale, where individual households are surveyed",
   "The scale of a single city block",
   "The scale of one household's ancestry records",
   "The scale of an individual voter's ballot"], ans=0,
   why="The mismatch between states and nations is a pattern that only appears when many borders and many cultural distributions are laid over one another, which is a global-scale comparison. At household or block scale there are not enough borders in view for the pattern to exist."),
]
