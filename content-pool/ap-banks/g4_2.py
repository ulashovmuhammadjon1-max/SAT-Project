# AP HUMAN GEOGRAPHY 4.2 Political Processes -- 30 questions
# CED (2020 framework), Unit 4, enduring understanding PSO-4.
# Learning objective PSO-4.B: explain the processes that have shaped
# contemporary political geography.
#
# Essential knowledge:
#   PSO-4.B.1  The concepts of sovereignty, nation-states, and self-determination
#              shape the contemporary world.
#   PSO-4.B.2  Colonialism, imperialism, independence movements, and devolution
#              along national lines have influenced contemporary political
#              boundaries.
#
# The topic is a set of PROCESSES, so nearly every item hands over an outcome and
# asks which process produced it, or hands over a process and asks what map it
# leaves behind. The two that students routinely merge are colonialism (settling
# and administering a distant territory) and imperialism (extending control over
# another people by any means, including indirect economic control), so items 8,
# 9 and 10 separate them on that difference rather than on a definition.
#
# Suggested skill 3.E, explain what maps or data imply about geographic
# processes: items 6, 17 and 26 carry real data tables.
#
# The Berlin Conference is named in the CED at IMP-4.B.2 and its consequences are
# the standard worked example of superimposed boundaries; here it is used only as
# an illustration of colonial boundary-drawing, and the boundary TYPOLOGY is left
# to Topic 4.4, where the CED puts it.
#
# FIVE choices (A-E), matching the real AP Human Geography exam.
TOPIC = ("4.2", "Political Processes", 4)
QUESTIONS = [
 dict(q="A newly recognized government insists that no other state may set its tax rates, station troops on its soil, or overrule its courts. The principle it is asserting is", choices=[
   "sovereignty",
   "self-determination",
   "devolution",
   "irredentism",
   "supranationalism"], ans=0,
   why="Sovereignty is the claim to supreme authority within a territory and independence from outside authority, which is exactly what refusing external taxation, garrisoning, and judicial review amounts to. Self-determination concerns who gets to form a state in the first place, and the other three describe transfers of authority rather than the assertion of it."),
 dict(q="A people occupying a distinct region petitions for the right to decide its own political status, including whether to remain part of its current state. The principle invoked is", choices=[
   "self-determination",
   "sovereignty already held by the region",
   "neocolonialism",
   "gerrymandering",
   "the rank-size rule"], ans=0,
   why="Self-determination is the claim that a people may choose its own political arrangements; the region is asking for that right, which means it does not yet hold sovereignty. PSO-4.B.1 names self-determination alongside sovereignty precisely because they are different stages of the same argument."),
 dict(q="Which outcome would count as the clearest realization of the principle of self-determination?", choices=[
   "A referendum in which the residents of a region vote to become an independent state and are recognized as one",
   "A neighboring state annexing the region by force",
   "An international organization assigning the region to a new administrator",
   "A colonial power redrawing the region's internal boundaries",
   "A national government relocating settlers into the region"], ans=0,
   why="Self-determination locates the decision with the people of the territory, so a vote by those residents followed by recognition is the principle working as stated. Annexation, external assignment, boundary redrawing, and settlement all place the decision somewhere other than with the people concerned."),
 dict(q="Between 1945 and 1975 dozens of African and Asian territories became sovereign states. Taken together these events are best described as", choices=[
   "independence movements ending colonial rule",
   "devolution of powers within existing states",
   "the growth of supranational organizations",
   "the diffusion of the nation-state ideal from Asia to Europe",
   "the redrawing of maritime boundaries under a new convention"], ans=0,
   why="A colony becoming sovereign is a change in who holds sovereignty over the territory, which is what an independence movement seeks; devolution by contrast keeps the original state intact and moves powers downward. PSO-4.B.2 lists independence movements as one of the processes shaping today's boundaries."),
 dict(q="Czechoslovakia separated into the Czech Republic and Slovakia in 1993, with the new border following the line between two national communities. This is an example of", choices=[
   "devolution along national lines",
   "colonialism",
   "irredentism by a neighboring state",
   "the imposition of a superimposed boundary by an outside power",
   "the creation of a supranational organization"], ans=0,
   why="PSO-4.B.2 names devolution along national lines, and the separation followed the existing Czech-Slovak national division rather than an outside power's decision. No external state acquired territory, which is what rules out both the colonial and the irredentist readings."),
 dict(table=dict(headers=["Year", "Member states of the United Nations"],
   rows=[["1945", "51"], ["1960", "99"], ["1975", "144"], ["1990", "159"], ["2000", "189"]]),
   q="Using the accompanying membership counts, the increase in the number of United Nations member states from 1945 to 1975 was", choices=[
   "93 states, driven mainly by decolonization in Africa and Asia",
   "51 states, driven mainly by devolution in Europe",
   "144 states, driven mainly by the founding of the organization",
   "45 states, driven mainly by the breakup of the Soviet Union",
   "30 states, driven mainly by maritime boundary agreements"], ans=0,
   why="144 minus 51 is 93, and the period covered is exactly the decolonization era in which former African and Asian colonies became sovereign and joined. The Soviet breakup falls after 1990 and so cannot explain a change that ended in 1975."),
 dict(q="A state's constitution transfers control of health, education, and policing to elected regional assemblies while the central government keeps defense and the currency. The process is", choices=[
   "devolution",
   "the loss of sovereignty by the state",
   "imperialism practiced internally",
   "the creation of several independent states",
   "the imposition of a consequent boundary"], ans=0,
   why="Devolution is the transfer of powers from a central government to subnational units within the same state. Sovereignty is unaffected because the central government retains defense and currency and could in principle reclaim the transferred powers -- which is the difference between devolution and independence."),
 dict(q="Which situation best illustrates imperialism without settlement colonialism?", choices=[
   "A powerful state controls a weaker state's trade policy and military basing through treaties while leaving its government in place",
   "A state sends thousands of its own citizens to farm and permanently occupy a distant territory",
   "Two states of equal power sign a mutual defense pact",
   "A state grants one of its provinces an elected assembly",
   "A region votes to join a neighboring state"], ans=0,
   why="Imperialism is control over another people by any means; colonialism in the narrow sense involves settling and directly administering the territory. Treaty-based control that leaves the local government nominally in charge is the first without the second, which is why the CED lists both terms."),
 dict(q="European powers at the Berlin Conference of 1884-1885 divided African territory among themselves with little reference to African political and cultural divisions. The most lasting geographic consequence was that", choices=[
   "many later African states inherited borders that cut across ethnic homelands",
   "African states inherited borders that matched ethnic homelands closely",
   "African territory was left unclaimed until after 1945",
   "African states were formed as a single supranational union",
   "African borders were determined by referendums among local populations"], ans=0,
   why="Borders drawn to suit European claims rather than African settlement patterns divided some peoples between colonies and combined rivals within them, and independence transferred those lines intact to the new states. That inheritance is why so many African states are strongly multinational."),
 dict(q="A former colonial power no longer governs its ex-colony but continues to control its largest banks, its main export crop, and its currency arrangements. Geographers describe this as", choices=[
   "neocolonialism, because control persists through economic means after formal independence",
   "devolution, because powers have been transferred downward",
   "self-determination, because the colony now has its own flag",
   "supranationalism, because two states are cooperating",
   "irredentism, because territory is being reclaimed"], ans=0,
   why="Formal sovereignty has been granted while effective economic control has not, which is what makes the prefix 'neo' do work: the mechanism changed from administration to finance and trade. A flag and a seat at the UN are the appearance of independence that the term is designed to look past."),
 dict(q="Which of the following would most strongly suggest that a state's sovereignty exists on paper but not in practice?", choices=[
   "Large areas of its territory are governed by armed groups the central government cannot dislodge",
   "It belongs to several international trade organizations",
   "It has recently changed its official language policy",
   "Its capital city is not its largest city",
   "It has a written constitution modeled on another state's"], ans=0,
   why="Sovereignty requires effective authority throughout the territory; if a government cannot enforce its writ over much of its own land, the claim is nominal. Treaty membership, language policy, capital-city choice, and borrowed constitutional text are all consistent with fully effective control."),
 dict(q="The idea that every nation should have its own state, spreading from nineteenth-century Europe outward, most directly encouraged", choices=[
   "movements to redraw boundaries so that they matched national homelands",
   "the merging of nations into large multinational empires",
   "the abandonment of the sovereignty principle",
   "the growth of colonial administration in Africa",
   "the replacement of states by city-states"], ans=0,
   why="If the nation is the proper basis for a state, then any boundary that splits a nation or locks two nations together is illegitimate, and the political program that follows is boundary revision. This is the nation-state ideal named in PSO-4.B.1 and it is why the number of states rose as empires fell."),
 dict(q="A minority nation inside a state demands not independence but a regional parliament with taxation powers. The demand is best characterized as", choices=[
   "a devolutionary demand short of secession",
   "a demand for full sovereignty",
   "an act of imperialism",
   "an assertion of neocolonial control",
   "a request to join a supranational organization"], ans=0,
   why="Devolution moves powers downward while leaving the state intact, and a regional parliament with tax powers is a transfer of exactly that kind. Sovereignty would require control of foreign policy and defense, which the demand does not mention."),
 dict(q="Which comparison of colonialism and imperialism is accurate?", choices=[
   "Imperialism is the broader process of extending control over other peoples; colonialism is one form of it involving settlement and direct administration",
   "Colonialism is the broader process; imperialism is one form of it involving trade agreements",
   "The two terms describe the same process at different scales of analysis",
   "Imperialism applies only to maritime empires and colonialism only to land empires",
   "Colonialism ended in 1945 while imperialism began in 1945"], ans=0,
   why="The relationship is genus and species: control over another people can be exercised by settlement, by administration, or by economic and military leverage, and colonialism names the settlement-and-administration version. The distinction matters because neocolonialism is imperialism continuing after colonies are gone."),
 dict(q="After independence, a state whose borders were drawn by a colonial power keeps those borders rather than redrawing them along ethnic lines. The most common reason given is that", choices=[
   "redrawing them would invite competing claims and conflict across the whole region",
   "colonial borders always matched ethnic homelands",
   "international law forbids any change to a state's boundaries",
   "ethnic homelands are identical from one census to the next",
   "supranational organizations assign all boundaries"], ans=0,
   why="Once one boundary is opened for revision on ethnic grounds, every neighbouring boundary becomes contestable, so the inherited lines are kept as the less destabilizing option. The claim that colonial borders matched homelands is false, which is the whole difficulty."),
 dict(q="Scotland's parliament, restored in 1999 with powers over health, education, and justice while defense and foreign policy remained at Westminster, is used in this course as an example of", choices=[
   "devolution within a unitary state",
   "the creation of a new sovereign state",
   "colonial administration",
   "irredentism directed at a neighboring state",
   "the formation of a supranational body"], ans=0,
   why="Powers were transferred downward while the reserved matters -- defense and foreign affairs -- stayed central, so no new sovereign entity was created. That reserved list is the standard test for telling devolution from independence."),
 dict(table=dict(headers=["Territory", "Year sovereignty transferred", "Former administering power"],
   rows=[["Territory 1", "1947", "United Kingdom"], ["Territory 2", "1960", "France"],
         ["Territory 3", "1975", "Portugal"], ["Territory 4", "1990", "South Africa"]]),
   q="Using the accompanying record of four transfers of sovereignty, the process common to all four entries is", choices=[
   "an independence movement ending administration by an outside power",
   "devolution of powers within an existing state",
   "the voluntary merger of two sovereign states",
   "the annexation of territory by a neighboring state",
   "the creation of a supranational trade bloc"], ans=0,
   why="In every row sovereignty passes from an outside administering power to the territory itself, which is decolonization however the dates differ. Devolution would leave the administering state sovereign, and none of the rows shows a merger or an annexation."),
 dict(q="A supranational organization requires its members to accept common rules on trade and to submit disputes to a shared court. From the standpoint of a member state this most directly", choices=[
   "limits the state's exercise of sovereignty in exchange for expected benefits",
   "transfers the state's territory to the organization",
   "converts the state into a colony of the organization",
   "eliminates the state's borders entirely",
   "makes the state a stateless nation"], ans=0,
   why="Accepting binding external rules is a voluntary restriction on how sovereignty is exercised, not a loss of the territory or of the state's existence. States accept it because they expect the trade or security gains to exceed the cost of the constraint."),
 dict(q="Which pair of processes pushes in opposite directions on the number of independent states in the world?", choices=[
   "Devolution along national lines, which tends to increase it, and supranational integration, which tends to pool authority among existing states",
   "Colonialism and imperialism, which both reduce it",
   "Self-determination and independence movements, which both reduce it",
   "Irredentism and annexation, which both increase it",
   "Neocolonialism and decolonization, which both increase it"], ans=0,
   why="Devolution taken to its endpoint fragments states into more sovereign units, while supranational bodies bind existing states more tightly together without creating new ones. Self-determination and independence movements both work in the same direction, upward, which is why that pairing is not a contrast."),
 dict(q="Sudan's separation into Sudan and South Sudan in 2011 followed a referendum in the southern region. The combination of processes best illustrated is", choices=[
   "self-determination expressed through a vote, resulting in a new sovereign state",
   "devolution that stopped short of independence",
   "colonial partition imposed by an outside power",
   "supranational integration of two neighbors",
   "neocolonial economic control replacing formal rule"], ans=0,
   why="The decision was made by the residents of the territory and produced full sovereignty, which is self-determination carried through to statehood rather than devolution, which by definition stops short. No outside power imposed the line."),
 dict(q="Why does the nation-state ideal generate political tension in a state whose national groups are geographically intermixed rather than living in separate regions?", choices=[
   "No boundary can be drawn that gives each group a territory without also leaving minorities on the wrong side",
   "Intermixed populations always share a single language",
   "Sovereignty cannot be exercised over an intermixed population",
   "Intermixed populations are exempt from the principle of self-determination",
   "Supranational organizations automatically redraw such boundaries"], ans=0,
   why="The ideal assumes nations occupy distinct blocks of territory; where settlement is interleaved, any line creates new minorities, so partition reproduces the problem it was meant to solve. That is why intermixed cases produce prolonged conflict rather than clean separations."),
 dict(q="A state that gained independence in the 1960s still exports one mineral to its former colonial ruler and imports nearly all manufactured goods from it. This pattern is most useful as evidence of", choices=[
   "an economic relationship inherited from the colonial period that constrains the new state's choices",
   "a devolutionary process inside the former ruler",
   "the absence of any independence movement in the territory",
   "the state's failure to meet the criteria for sovereignty",
   "the operation of self-determination in the former ruler"], ans=0,
   why="Colonial economies were built to send raw materials one way and manufactures the other, and that structure survives the transfer of sovereignty; the state is sovereign but its economic options are narrowed. Nothing in the pattern bears on whether the state meets the statehood criteria, which it plainly does."),
 dict(q="Which of the following best explains why the concepts of sovereignty and self-determination can come into direct conflict?", choices=[
   "A state's sovereignty covers its whole territory, while self-determination lets a people within that territory claim part of it",
   "Sovereignty applies only to colonies and self-determination only to states",
   "Self-determination is a legal doctrine and sovereignty is a cultural one",
   "Sovereignty concerns maritime space and self-determination concerns land",
   "The two concepts are applied at the same scale and therefore never overlap"], ans=0,
   why="The existing state invokes its territorial integrity while the region invokes its people's right to choose, and both principles are recognized, so the conflict is between two valid claims over the same ground. That structural clash is why secession disputes are so difficult to settle."),
 dict(q="Which of these is the strongest evidence that a devolutionary movement has become a secessionist one?", choices=[
   "The movement demands control of foreign policy, defense, and international recognition",
   "The movement demands a regional broadcasting service in its own language",
   "The movement demands more seats in the national parliament",
   "The movement demands that road signs be bilingual",
   "The movement demands a larger share of national infrastructure spending"], ans=0,
   why="Foreign policy, defense, and recognition are the external attributes of sovereignty, and demanding them is demanding statehood. Language, representation, and spending are all things a devolved region can obtain without leaving the state."),
 dict(q="A geographer comparing 1914 and 2014 world political maps of the same region finds far more states in the later map. The most likely explanation is", choices=[
   "empires were dismantled and their territories became sovereign states",
   "supranational organizations divided the region among themselves",
   "the total land area of the region increased",
   "states merged to gain economic strength",
   "boundaries were converted from land to maritime boundaries"], ans=0,
   why="The century between those maps is the century of decolonization and imperial collapse, both of which convert one large administered territory into many sovereign ones. Mergers would move the count the other way, and land area does not change."),
 dict(table=dict(headers=["Region", "States in 1914", "States in 2014"],
   rows=[["Region A", "4", "48"], ["Region B", "22", "44"], ["Region C", "3", "3"]]),
   q="Using the accompanying counts, the region whose state total grew by the largest multiple between 1914 and 2014 is", choices=[
   "Region A, which grew twelvefold",
   "Region B, which grew twofold",
   "Region C, which did not grow",
   "Region A, which grew fourfold",
   "Region B, which grew twenty-twofold"], ans=0,
   why="48 divided by 4 is 12, against 44 divided by 22 which is 2 and 3 divided by 3 which is 1. A twelvefold increase over a century is the signature of a region that was almost entirely under colonial administration in 1914."),
 dict(q="Two neighboring states form a customs union, adopt a common external tariff, and create a joint tribunal. At which scale has authority moved?", choices=[
   "Upward, from the state scale to a supranational scale",
   "Downward, from the state scale to the regional scale",
   "Downward, from the state scale to the local scale",
   "It has not moved, since tariffs are not exercises of sovereignty",
   "Upward, from the local scale to the state scale"], ans=0,
   why="A common tariff and a joint tribunal place decisions that were made in each capital into a body above both states, which is a move up the scale ladder. Devolution is the mirror image and moves the same kinds of decision downward."),
 dict(q="Which statement about the contemporary map best reflects PSO-4.B.1's claim that sovereignty, nation-states, and self-determination shape the world?", choices=[
   "Most boundary disputes today involve a claim about who is sovereign, who counts as a nation, or who may choose",
   "Most boundaries today are drawn purely along physical features such as rivers",
   "Most states today contain exactly one nation",
   "Most territory today is administered by colonial powers",
   "Most boundaries today are set by supranational organizations"], ans=0,
   why="Those three ideas supply the vocabulary in which territorial arguments are actually made, which is what the framework means by saying they shape the contemporary world. The alternatives are empirically false: most states are multinational and almost no territory remains under colonial administration."),
 dict(q="A state facing a strong independence movement in one region responds by granting the region an assembly with wide powers. From the central government's point of view the likely purpose is to", choices=[
   "satisfy demands for self-rule while preserving the state's territorial integrity",
   "convert the region into a colony",
   "transfer sovereignty to the region immediately",
   "invite a neighboring state to annex the region",
   "dissolve the state into a supranational union"], ans=0,
   why="Devolution is the standard central-government answer to secessionist pressure because it concedes self-rule without conceding sovereignty. Whether it defuses the movement or feeds it is contested, but the intent is to keep the state whole."),
 dict(q="At the global scale, which process would a geographer expect to REDUCE the political importance of individual state boundaries without changing their location?", choices=[
   "The growth of supranational agreements that let goods and people cross freely",
   "The devolution of powers to regions within states",
   "The rise of independence movements in colonial territories",
   "The drawing of new boundaries after a partition",
   "The extension of one state's control over another's economy"], ans=0,
   why="Free movement across a line leaves the line exactly where it is while stripping it of the function that made it matter. The other options all either create new lines or change who exercises power inside existing ones."),
]
