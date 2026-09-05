# AP WORLD HISTORY: MODERN 7.1 Shifting Power After 1900
# CED effective Fall 2026, Unit 7 Global Conflict, c. 1900 to the present.
# Thematic focus Governance (GOV). Unit 7 Learning Objective A: explain how
# internal and external factors contributed to change in various states after
# 1900. Suggested skill 4.B, explain how a specific historical development or
# process is situated within a broader historical context.
#
# HISTORICAL DEVELOPMENTS THIS TOPIC RESTS ON, in the framework's own words:
#   KC-6.2.I    The West dominated the global political order at the beginning
#               of the 20th century, but both land-based and maritime empires
#               gave way to new states by the century's end.
#   KC-6.2.I.A  The older, land-based Ottoman, Russian, and Qing empires
#               collapsed due to a combination of internal and external
#               factors. These changes in Russia eventually led to communist
#               revolution.
#   KC-6.2.II.D States around the world challenged the existing political and
#               social order, including the Mexican Revolution that arose as a
#               result of political crisis.
#
# WHAT IS DELIBERATELY NOT ASKED. The framework gives no date for any single
# collapse, and it says explicitly that events are not constrained by the given
# dates. No item here keys to a year, a decade or an ordering of the three
# collapses against one another. It names no cause of the Mexican Revolution
# beyond "political crisis", so no item supplies one. It links communist
# revolution to Russia alone, so no item extends that link to the Ottoman or
# Qing case.
#
# SOURCES. The bank cannot show images, and the framework prints no document
# text for this topic, so every stimulus here is either an explicitly
# unattributed illustrative source or a table of illustrative data whose keyed
# conclusion is recoverable from the table itself. Nothing is attributed to a
# real person or document.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md.
TOPIC = ("7.1", "Shifting Power After 1900", 7)

_T_PRESSURE = dict(
    headers=["Empire (illustrative)",
             "Share of state revenue owed to foreign creditors (percent)",
             "Provinces reporting failed tax collection"],
    rows=[["Empire X", "46", "3"],
          ["Empire Y", "12", "5"],
          ["Empire Z", "28", "11"]])

_T_CHALLENGE = dict(
    headers=["Region (illustrative)",
             "Recorded strikes and uprisings, first decade",
             "Recorded strikes and uprisings, third decade"],
    rows=[["Region I", "14", "31"],
          ["Region II", "6", "9"],
          ["Region III", "22", "19"]])

QUESTIONS = [
 dict(q="An unattributed political pamphlet circulated in a large land-based empire early in the twentieth century complains that provincial governors can no longer collect the taxes the treasury is owed, and that foreign banks now set the terms on which the empire may borrow. Taken together, the two complaints best illustrate",
   choices=[
     "a combination of internal and external factors of the kind the framework uses to explain the collapse of the older land-based empires",
     "external financial pressure operating on its own, with the empire's own administration still intact",
     "internal administrative weakness operating on its own, with no pressure from outside the empire",
     "the expansion of maritime empires into territory that land-based empires had never governed",
     "a communist revolution already under way in the empire's provinces"], ans=0,
   why="KC-6.2.I.A explains the collapse of the older land-based Ottoman, Russian and Qing empires by a combination of internal and external factors. Failed provincial tax collection is internal and foreign control of borrowing terms is external, so the pamphlet names one of each rather than either alone."),
 dict(q="A textbook chapter on the first half of the twentieth century is titled 'The Collapse of the Older Land-Based Empires.' Which grouping of states is the chapter most likely to treat?",
   choices=[
     "The Ottoman, Russian, and Qing empires",
     "The British, French, and Dutch empires",
     "The Ottoman, Russian, and Japanese empires",
     "The Qing, Portuguese, and Spanish empires",
     "The German, Belgian, and Italian empires"], ans=0,
   why="KC-6.2.I.A names the older, land-based empires as the Ottoman, Russian and Qing. The other groupings are maritime empires, or mix a land-based case with maritime ones, and the framework does not treat them under this heading."),
 dict(q="Which statement best captures the framework's account of how the global political order changed across the twentieth century?",
   choices=[
     "Western domination at the start of the century gave way by the century's end to new states formed out of both land-based and maritime empires",
     "New states formed at the start of the century gave way by the century's end to renewed Western domination of the political order",
     "Western domination was unbroken from the start of the century to its end, and no new states were formed",
     "Land-based empires expanded across the century while maritime empires disappeared at its beginning",
     "The political order was already made up of independent states at the beginning of the century"], ans=0,
   why="KC-6.2.I states that the West dominated the global political order at the beginning of the twentieth century but that both land-based and maritime empires gave way to new states by the century's end. The order of the two clauses is the substance of the claim, and reversing it inverts the framework's account."),
 dict(q="A state's ruling group has held office for decades, rival factions can find no lawful route to power, and an armed movement then demands both a new government and a redistribution of land. According to the framework, this pattern is best described as",
   choices=[
     "a political crisis inside the state producing a challenge to the existing political and social order",
     "an external invasion producing a change of government against the wishes of the population",
     "an imperial power transferring a colony to another imperial power by treaty",
     "a technological change producing an unintended shift in the balance of power",
     "a communist revolution following the collapse of a land-based empire"], ans=0,
   why="KC-6.2.II.D states that states around the world challenged the existing political and social order, including the Mexican Revolution that arose as a result of political crisis. A demand for a new government together with a demand about landholding is a challenge to both orders the statement names."),
 dict(q="How does the framework relate the collapse of the old imperial order in Russia to communist revolution there?",
   choices=[
     "The collapse came first, and the framework describes it as leading eventually to communist revolution",
     "The communist revolution came first, and it destroyed an empire that was otherwise stable",
     "The two are described as unrelated developments that happened to fall in the same period",
     "The framework describes the communist revolution as an external factor imposed by other states",
     "The framework describes both as consequences of the expansion of maritime empires"], ans=0,
   why="KC-6.2.I.A says the older land-based empires collapsed from internal and external factors and that these changes in Russia eventually led to communist revolution. The word 'eventually' fixes the direction: the changes precede the revolution and lead to it, rather than the reverse."),
 dict(q="A historian argues that an old land-based empire fell for one reason only, namely its defeat in a war with a foreign power. On the framework's account, the strongest qualification to that argument is that",
   choices=[
     "the framework pairs external factors with internal ones in explaining these collapses rather than resting on either kind alone",
     "the framework denies that warfare had any part in the collapse of these empires",
     "the framework treats defeat in war as an internal rather than an external factor",
     "the framework treats these empires as maritime rather than land-based",
     "the framework dates every one of these collapses to the same year"], ans=0,
   why="KC-6.2.I.A attributes the collapses to a combination of internal and external factors. Defeat by a foreign power is an external factor, so an account resting on it alone omits the internal half of the framework's explanation without contradicting the framework about warfare."),
 dict(q="The table below reports illustrative data for three land-based empires in the early twentieth century. Which conclusion is best supported by the data as given?",
   table=_T_PRESSURE,
   choices=[
     "Empire X is under the greatest external financial pressure and Empire Z shows the most widespread internal breakdown",
     "Empire Z is under the greatest external financial pressure and Empire X shows the most widespread internal breakdown",
     "Empire Y is under the greatest pressure of both kinds at once",
     "External financial pressure and failed tax collection rise together across the three cases",
     "None of the three empires shows any sign of internal administrative difficulty"], ans=0,
   why="Read from the table alone: the largest share of revenue owed to foreign creditors belongs to one empire and the largest number of provinces failing to collect taxes belongs to a different one, so the two kinds of pressure named in KC-6.2.I.A do not fall on the same case here."),
 dict(q="A student writes an essay about a revolution that broke out in a single country in the 1910s. Which addition would most effectively situate that revolution in a broader historical context?",
   choices=[
     "Evidence that states in several regions were challenging the existing political and social order in the same period",
     "A longer description of the personalities of the revolution's leaders",
     "A list of the weapons carried by each side in the fighting",
     "An account of the country's climate and physical geography",
     "A summary of what the country's constitution said before the revolution"], ans=0,
   why="Suggested skill 4.B asks students to explain how a specific development is situated within a broader historical context, and KC-6.2.II.D supplies that context by stating that states around the world challenged the existing political and social order. Showing the same process elsewhere is what makes the single case an instance of something larger."),
 dict(q="Which of the following describes a change, rather than a continuity, in the global political order over the course of the twentieth century?",
   choices=[
     "The replacement of both land-based and maritime empires by new states",
     "The existence of large empires governing territory in more than one region",
     "The presence of trade between distant parts of the world",
     "The use of taxation by governments to fund their armies",
     "The existence of religious differences within large states"], ans=0,
   why="KC-6.2.I identifies the century's change as empires of both kinds giving way to new states. The other four describe conditions the framework does not present as beginning or ending in this period, so they cannot be the change the statement names."),
 dict(q="An unattributed newspaper editorial published in an unnamed empire shortly after 1900 states: 'Our regiments carry rifles bought abroad on credit, and our ministries are filled by men chosen for loyalty rather than competence.' The editorial identifies",
   choices=[
     "an external dependence and an internal administrative weakness in the same sentence",
     "two external pressures, both of them financial in character",
     "two internal weaknesses, neither of them connected to other states",
     "a challenge to the social order rather than to the political order",
     "the arrival of a communist revolution in the empire"], ans=0,
   why="KC-6.2.I.A explains imperial collapse by a combination of internal and external factors. Buying weapons abroad on credit is a dependence on outside states and creditors; appointing ministers for loyalty rather than competence is a weakness of the empire's own administration."),
 dict(q="On the framework's account, what became of the territory once governed by the older land-based empires?",
   choices=[
     "New states were formed where the empires' territory had been",
     "It was left ungoverned for the remainder of the century",
     "It was absorbed in its entirety by the surviving maritime empires",
     "It returned to the same dynasties under new titles",
     "It was administered jointly by the Western powers until the present"], ans=0,
   why="KC-6.2.I states that both land-based and maritime empires gave way to new states by the century's end. The framework describes replacement by new states and does not describe any of the four alternative outcomes."),
 dict(q="A comparison of a land-based empire with a maritime empire across the twentieth century would be best supported by which statement from the framework?",
   choices=[
     "The framework treats both land-based and maritime empires as giving way to new states over the course of the century",
     "The framework treats land-based empires as surviving the century while maritime empires ended",
     "The framework treats maritime empires as surviving the century while land-based empires ended",
     "The framework treats both kinds of empire as intact at the century's end",
     "The framework treats the distinction between the two kinds of empire as one it does not draw"], ans=0,
   why="KC-6.2.I names both land-based and maritime empires as giving way to new states by the century's end, and KC-6.2.I.A separately identifies the older land-based cases. Both parts of the comparison are therefore available, and neither kind is described as surviving intact."),
 dict(q="A commentator claims that the Mexican Revolution was brought about by an invasion from outside the country. Using the framework, the best correction is that it is described as arising from",
   choices=[
     "a political crisis within the state",
     "a war between two other empires",
     "the collapse of a land-based empire in another region",
     "an economic depression that began in the 1930s",
     "the transfer of colonies under a treaty settlement"], ans=0,
   why="KC-6.2.II.D states that the Mexican Revolution arose as a result of political crisis. The framework locates the cause inside the state's own politics, so an account beginning with an invasion replaces the stated cause with one the framework does not give."),
 dict(q="The table below reports illustrative counts of recorded strikes and uprisings in three regions across two decades of the early twentieth century. Which conclusion is best supported?",
   table=_T_CHALLENGE,
   choices=[
     "Every region records challenges in both decades, and the largest number in the later decade is Region I",
     "Region II records the largest number in the later decade",
     "Only one of the three regions records any challenges at all",
     "Every region records fewer challenges in the later decade than in the earlier one",
     "No region records fewer challenges in the later decade than in the earlier one"], ans=0,
   why="Read from the table alone: no cell is zero, one region has the largest later total, and exactly one region's total falls between the two decades. This is the pattern KC-6.2.II.D describes, of states around the world challenging the existing order rather than a single region doing so."),
 dict(q="A hypothetical memoir written decades afterwards by a former minister of a collapsed empire blames foreign bankers alone for the collapse. Which limitation on the source's usefulness is most significant?",
   choices=[
     "The author's own position gives him a reason to leave the empire's internal administration out of the account",
     "The author was not alive during the period the memoir describes",
     "A memoir cannot report anything about finance",
     "The memoir was written in the author's own language rather than in translation",
     "The memoir describes an empire rather than a republic"], ans=0,
   why="A minister was part of the administration whose failures KC-6.2.I.A counts among the internal factors, so an account naming only external causes is exactly the account his position would favour. That is a limit on the source, not a reason to discard it."),
 dict(q="Which finding, if it were established, would most strengthen a claim that internal factors were decisive in an empire's collapse?",
   choices=[
     "Records showing that the empire's tax and army administration had broken down before foreign pressure increased",
     "Records showing that foreign creditors imposed new terms before any administrative difficulty appeared",
     "Records showing that the empire's population grew steadily throughout the period",
     "Records showing that neighbouring empires collapsed in the same decade",
     "Records showing that the empire's borders were unchanged for a century before the collapse"], ans=0,
   why="A cause cannot follow its effect. If the administrative breakdown that KC-6.2.I.A counts as an internal factor is already under way before external pressure rises, the internal side has the earlier claim on the outcome. The other findings leave the sequence untouched."),
 dict(q="Which finding, if it were established, would most weaken that same claim about internal factors?",
   choices=[
     "Records showing that the administration functioned normally until foreign creditors imposed new terms",
     "Records showing that provincial governors had failed to collect taxes for a generation",
     "Records showing that the empire's ministries were filled by patronage appointments",
     "Records showing that the empire had lost no territory to any other state",
     "Records showing that the empire's army had not been reorganised for decades"], ans=0,
   why="The same sequencing rule read the other way: if the internal machinery is working until the external pressure arrives, the internal factors of KC-6.2.I.A cannot be what started the collapse. Three of the alternatives are themselves evidence of internal weakness and would strengthen the claim instead."),
 dict(q="A unit of study titled 'Shifting Power After 1900' would most appropriately open with which statement of the situation at the start of the period?",
   choices=[
     "The West dominated the global political order at the beginning of the twentieth century",
     "New states formed from former empires already governed most of the world's population",
     "Land-based empires had already been replaced by maritime ones",
     "No state exercised power beyond its own borders",
     "Communist governments held power across much of Europe and Asia"], ans=0,
   why="KC-6.2.I opens with the West dominating the global political order at the beginning of the twentieth century, and the rest of the statement describes movement away from that starting point. The other four describe conditions the framework places later in the century or not at all."),
 dict(q="The framework links a communist revolution to changes in which of the following states?",
   choices=[
     "Russia",
     "The Ottoman Empire",
     "Qing China",
     "Mexico",
     "Great Britain"], ans=0,
   why="KC-6.2.I.A says that the changes in one of the three collapsed land-based empires eventually led to communist revolution, and names that case specifically. The framework does not extend the link to the other two collapses or to the Mexican case, which KC-6.2.II.D attributes to political crisis."),
 dict(q="An unattributed founding declaration issued by a congress meeting in the 1920s announces that the provinces it represents will no longer be governed from the imperial capital and will govern themselves as a state. The declaration is best used as evidence of",
   choices=[
     "the formation of new states out of territory that empires had governed",
     "the expansion of an existing empire into territory it had not held",
     "the survival of imperial rule under a different name",
     "a challenge to the social order that left the political order untouched",
     "the transfer of a colony from one imperial power to another"], ans=0,
   why="KC-6.2.I describes empires giving way to new states across the century. A congress declaring that former imperial provinces will govern themselves is precisely that process, and it is not an expansion, a continuation or a transfer between empires."),
 dict(q="Which of the following best states the relationship the framework asserts between internal and external factors in imperial collapse?",
   choices=[
     "Each collapse is explained by a combination of the two rather than by either kind alone",
     "External factors are stated to be decisive and internal ones incidental",
     "Internal factors are stated to be decisive and external ones incidental",
     "The two kinds of factor are said never to operate on the same empire",
     "The framework offers no explanation of these collapses"], ans=0,
   why="KC-6.2.I.A says the collapses were due to a combination of internal and external factors. The statement neither ranks the two kinds nor excludes either, so an account that promotes one to decisive goes beyond what the framework asserts."),
 dict(q="A student writes that the world's empires all ended at a single moment. Using the framework, the best correction is that the end of empire is described as",
   choices=[
     "a process spread across the century rather than a single event",
     "a single event that took place at the century's opening",
     "something that happened only to maritime empires",
     "something that had already been completed before 1900",
     "a development the framework does not discuss"], ans=0,
   why="KC-6.2.I says empires gave way to new states by the century's end, which marks a span rather than a date, and the framework states elsewhere that developments are not constrained by the dates given for a period. The end of empire is therefore extended in time."),
 dict(q="What similarity does the framework support between the Mexican Revolution and the collapse of an older land-based empire?",
   choices=[
     "Both are challenges to an existing order that begin with a crisis inside the state",
     "Both are described as caused entirely by pressure from foreign creditors",
     "Both are described as leading directly to communist revolution",
     "Both are described as the work of an invading maritime empire",
     "Both are described as leaving the existing social order in place"], ans=0,
   why="KC-6.2.II.D attributes the Mexican Revolution to political crisis and groups it with states around the world challenging the existing political and social order, while KC-6.2.I.A counts internal factors among the causes of the imperial collapses. The shared element is a crisis inside the state, not an external agent."),
 dict(q="An unattributed government decree issued after a revolution orders large estates to be broken up and distributed among the people who work them. The decree is best read as evidence that the revolution challenged",
   choices=[
     "the social order as well as the political order",
     "the political order only, leaving landholding untouched",
     "the social order only, leaving the government in place",
     "neither order, since it concerns agriculture alone",
     "an order imposed from outside the country by treaty"], ans=0,
   why="KC-6.2.II.D describes states around the world challenging the existing political and social order. A revolutionary government redistributing land is acting on the arrangement of society as well as on who governs, which is the pairing the statement names."),
 dict(q="A source dated 1900 reports that decisions affecting most of the world's population were taken in a handful of Western capitals. How does this source stand in relation to the framework's account?",
   choices=[
     "It is consistent with Western predominance at the beginning of the century, which the framework treats as the starting point for the changes that followed",
     "It contradicts the framework, which denies that any state dominated the political order at that date",
     "It is irrelevant to the framework, which discusses only the period after the Second World War",
     "It shows that new states had already replaced the empires by that date",
     "It shows that land-based empires had already collapsed by that date"], ans=0,
   why="KC-6.2.I begins from Western domination of the global political order at the beginning of the twentieth century. A source describing that domination reports the framework's starting condition rather than contradicting it."),
 dict(q="Which statement is inconsistent with the framework's account of the twentieth century?",
   choices=[
     "Maritime empires survived the century intact while only land-based empires gave way",
     "Older land-based empires collapsed from a combination of internal and external factors",
     "States in many parts of the world challenged the existing political and social order",
     "The West dominated the global political order at the century's opening",
     "New states had replaced empires in much of the world by the century's end"], ans=0,
   why="KC-6.2.I says that both land-based and maritime empires gave way to new states. A statement exempting maritime empires contradicts the word 'both', while the other four restate KC-6.2.I, KC-6.2.I.A and KC-6.2.II.D."),
 dict(q="A researcher wants evidence bearing specifically on the internal factors in an empire's collapse. Which body of material is most directly useful?",
   choices=[
     "Provincial administrative records of tax collection and appointments",
     "The lending agreements signed with banks in other countries",
     "Treaties concluded with neighbouring empires",
     "Reports filed by foreign ambassadors to their own governments",
     "The tariff schedules of the empire's trading partners"], ans=0,
   why="KC-6.2.I.A distinguishes internal from external factors. Records of how the empire taxed and staffed its own provinces report on the empire's own machinery, whereas loans, treaties, ambassadors and foreign tariffs all document the empire's relations with others."),
 dict(q="Two states each experienced an imperial collapse, and a communist revolution followed in one of them. On the framework's account, the best conclusion is that",
   choices=[
     "the framework links communist revolution to only one of the collapsed land-based empires",
     "the framework treats communist revolution as the normal outcome of any imperial collapse",
     "the framework treats communist revolution as a cause of imperial collapse",
     "the framework denies that any communist revolution followed an imperial collapse",
     "the framework treats communist revolution as an external factor acting on both states"], ans=0,
   why="KC-6.2.I.A attaches the eventual communist revolution to the changes in Russia specifically, after naming three collapsed land-based empires. Generalising the outcome to every collapse asserts more than the sentence does."),
 dict(q="Why does the framework describe the Ottoman, Russian, and Qing empires as a group distinct from the empires of Western Europe?",
   choices=[
     "They are described as older and land-based rather than maritime",
     "They are described as newer and maritime rather than land-based",
     "They are described as colonies rather than as empires",
     "They are described as having no administration of their own",
     "They are described as unaffected by pressure from other states"], ans=0,
   why="KC-6.2.I.A calls them the older, land-based Ottoman, Russian and Qing empires, and KC-6.2.I sets land-based empires beside maritime ones as the two kinds that gave way to new states. The grouping is by age and by the land-based character of the empire."),
 dict(q="Which research question fits the stated learning objective for this topic most closely?",
   choices=[
     "Which internal and which external factors contributed to change in a given state after 1900",
     "Which weapons were most widely used by armies after 1900",
     "Which artists were most admired in the capitals of Europe after 1900",
     "Which crops were most widely grown in each region after 1900",
     "Which languages were most widely spoken in the former empires after 1900"], ans=0,
   why="Unit 7 Learning Objective A asks students to explain how internal and external factors contributed to change in various states after 1900. A question framed in those two categories is the objective restated as an inquiry; the other four are about matters the objective does not name."),
]
