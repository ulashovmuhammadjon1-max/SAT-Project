# AP WORLD HISTORY: MODERN 7.5 Unresolved Tensions After World War I
# CED effective Fall 2026, Unit 7 Global Conflict, c. 1900 to the present.
# Thematic focus Governance (GOV). Unit 7 Learning Objective E: explain the
# continuities and changes in territorial holdings from 1900 to the present.
# Reasoning process: continuity and change. Suggested skill 2.C, explain the
# significance of a source's point of view, purpose, historical situation,
# and/or audience, including how these might limit the use(s) of a source.
#
# THE HISTORICAL DEVELOPMENT THIS TOPIC RESTS ON, in the framework's own words:
#   KC-6.2.I.B  Between the two world wars, Western and Japanese imperial states
#               predominantly maintained control over colonial holdings; in some
#               cases, they gained additional territories through conquest or
#               treaty settlement and in other cases faced anti-imperial
#               resistance.
#
# The sentence has three parts and every key here is one of them: continuity
# (control predominantly maintained), change by gain (through conquest OR treaty
# settlement -- two routes, not one), and resistance encountered. The word
# "predominantly" is a qualifier the framework chose, and items 8 and 20 turn on
# it: the sentence does not say that every holding was kept everywhere.
#
# ILLUSTRATIVE EXAMPLES the CED prints for this topic:
#   Territorial gains -- transfer of former German colonies to Great Britain and
#     France under the system of League of Nations mandates; Manchukuo and the
#     Greater East Asia Co-Prosperity Sphere.
#   Anti-imperial resistance -- the Indian National Congress; West African
#     resistance (strikes and congresses) to French rule.
# Those phrases are the framework's own, and nothing is asserted about what any
# of them contained beyond the heading it is printed under.
#
# WHAT IS DELIBERATELY NOT ASKED. No item keys to a date, a treaty article, a
# territory's area, a leader's name or the outcome of any resistance movement.
# The framework records that resistance was faced; it does not say here that it
# succeeded, and decolonisation belongs to unit 8, which a sibling holds.
#
# SOURCES. Every stimulus is an explicitly unattributed illustrative source or a
# table of illustrative data whose keyed conclusion is recoverable from the table
# alone. Nothing is attributed to a real person or document.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md.
TOPIC = ("7.5", "Unresolved Tensions After World War I", 7)

_T_HOLDINGS = dict(
    headers=["Imperial state (illustrative)",
             "Colonial territories administered at the start of the interwar period",
             "Colonial territories administered at the end of the interwar period"],
    rows=[["State 1", "12", "12"],
          ["State 2", "8", "10"],
          ["State 3", "5", "5"]])

_T_RESISTANCE = dict(
    headers=["Colonial territory (illustrative)",
             "Recorded strikes and congresses against colonial rule, first decade",
             "Recorded strikes and congresses against colonial rule, second decade"],
    rows=[["Territory J", "4", "17"],
          ["Territory K", "9", "28"],
          ["Territory L", "2", "3"]])

QUESTIONS = [
 dict(q="What does the framework say Western and Japanese imperial states did with their colonial holdings between the two world wars?",
   choices=[
     "They predominantly maintained control over them",
     "They predominantly surrendered control over them",
     "They exchanged them with one another under a general agreement",
     "They placed them all under the direct government of the League of Nations",
     "They abandoned them and withdrew to their home territories"], ans=0,
   why="KC-6.2.I.B states that between the two world wars, Western and Japanese imperial states predominantly maintained control over colonial holdings. Maintenance of control is the continuity the sentence opens with."),
 dict(q="By what two routes does the framework say imperial states gained additional territories in this period?",
   choices=[
     "Through conquest or through treaty settlement",
     "Through purchase or through inheritance",
     "Through referendum or through arbitration",
     "Through conquest only, with no other route recorded",
     "Through treaty settlement only, with no other route recorded"], ans=0,
   why="KC-6.2.I.B states that in some cases imperial states gained additional territories through conquest or treaty settlement. Both routes are named in the sentence, so an answer offering only one of them is incomplete."),
 dict(q="The CED gives the transfer of former German colonies to Great Britain and France under the system of League of Nations mandates as an example of what?",
   choices=[
     "A territorial gain made through a treaty settlement",
     "A territorial gain made through conquest in war",
     "An instance of anti-imperial resistance",
     "A government intervention in the economy",
     "A strategy for mobilizing a population for war"], ans=0,
   why="The CED prints the mandate transfers under the heading territorial gains for this topic, and KC-6.2.I.B names conquest and treaty settlement as the two routes to such gains. A transfer made under a system established by the postwar settlement is the second of those."),
 dict(q="Manchukuo and the Greater East Asia Co-Prosperity Sphere are printed in the CED under which heading for this topic?",
   choices=[
     "Territorial gains",
     "Anti-imperial resistance",
     "Government intervention in the economy",
     "Mobilization for total war",
     "Mass atrocities after 1900"], ans=0,
   why="The illustrative examples the CED prints beside KC-6.2.I.B are divided into territorial gains and anti-imperial resistance, and these two appear under the first heading. The other headings belong to topics 7.4, 7.3 and 7.8."),
 dict(q="Which pair does the CED print as illustrative examples of anti-imperial resistance in this period?",
   choices=[
     "The Indian National Congress, and West African strikes and congresses against French rule",
     "The League of Nations mandates, and the Greater East Asia Co-Prosperity Sphere",
     "The New Deal, and the fascist corporatist economy",
     "Political propaganda, and intensified forms of nationalism",
     "The Five Year Plans, and collective agriculture"], ans=0,
   why="The CED prints the Indian National Congress and West African resistance, in the form of strikes and congresses, to French rule as its examples of anti-imperial resistance beside KC-6.2.I.B. The other pairs are illustrative examples for topics 7.5's territorial gains, 7.4 and 7.3."),
 dict(q="Which states does the framework name as the imperial powers holding colonies between the wars?",
   choices=[
     "Western and Japanese imperial states",
     "Western imperial states only",
     "Japanese imperial states only",
     "The states newly formed out of the collapsed land-based empires",
     "The states that had remained neutral in the First World War"], ans=0,
   why="KC-6.2.I.B names Western and Japanese imperial states together as the holders of colonial holdings between the two world wars. Restricting the sentence to either one alone drops half of what it says."),
 dict(q="The table below reports illustrative counts of colonial territories administered by three imperial states at the start and the end of the interwar period. Which conclusion is best supported?",
   table=_T_HOLDINGS,
   choices=[
     "No state administered fewer territories at the end, two ended with the same number, and one gained",
     "No state administered fewer territories at the end, two gained, and one ended with the same number",
     "Every state administered fewer territories at the end than at the start",
     "Every state administered more territories at the end than at the start",
     "The three states administered the same number of territories as one another at the end"], ans=0,
   why="Read from the table alone: no state's later count is below its earlier one, most counts are unchanged, and one state's count rises. That is the pattern KC-6.2.I.B describes, control predominantly maintained with additional territories gained in some cases."),
 dict(q="The table below reports illustrative counts of strikes and congresses directed against colonial rule in three territories across two decades. Which conclusion is best supported?",
   table=_T_RESISTANCE,
   choices=[
     "Recorded activity rises in every territory, and the largest increase is in Territory K",
     "Recorded activity rises in every territory, and the largest increase is in Territory J",
     "Recorded activity falls in every territory between the two decades",
     "Only one of the three territories records any activity at all",
     "The territory with the highest count in the first decade shows the smallest increase"], ans=0,
   why="Read from the table alone: every territory's second-decade count exceeds its first, no count is zero, and subtracting gives one territory the largest increase. This is the anti-imperial resistance KC-6.2.I.B says imperial states faced in some cases."),
 dict(q="An unattributed annual report by a colonial administration states that the territory was governed throughout the year without interruption and that revenue was collected as usual. Which limitation on its use is most significant?",
   choices=[
     "It is written by the administration whose performance is in question, so it has reason to present the year as untroubled",
     "It was written during the period it describes, which makes it unusable as evidence",
     "It concerns revenue, so it can say nothing about colonial rule",
     "It names a territory, and no source naming a territory can be used",
     "It was written in an official language rather than a local one, so its author cannot be identified"], ans=0,
   why="Suggested skill 2.C asks how a source's point of view and purpose limit its uses. KC-6.2.I.B records that imperial states faced anti-imperial resistance in some cases, and an administration reporting on its own year is the party least likely to record it."),
 dict(q="A student writes that the interwar years saw imperial powers lose their colonies. Using the framework, the best correction is that between the wars those states",
   choices=[
     "predominantly kept their colonial holdings, and in some cases added to them",
     "predominantly lost their colonial holdings, and in some cases added to them",
     "kept every holding without exception and faced no resistance anywhere",
     "transferred every holding to the League of Nations for administration",
     "exchanged their holdings with one another by general agreement"], ans=0,
   why="KC-6.2.I.B states that Western and Japanese imperial states predominantly maintained control over colonial holdings and in some cases gained additional territories. The anchor carries both halves because the reversed reading is the plausible error."),
 dict(q="An unattributed resolution passed by a colonial political congress calls on its members to refuse cooperation with the colonial administration until the territory governs itself. The resolution is best used as evidence of",
   choices=[
     "the anti-imperial resistance that imperial states faced in some of their holdings",
     "the transfer of a colony from one imperial power to another",
     "a government taking a more active role in economic life",
     "the mobilization of a colonial population for the purpose of waging war",
     "the collapse of an older land-based empire"], ans=0,
   why="KC-6.2.I.B states that imperial states in some cases faced anti-imperial resistance, and the CED prints the Indian National Congress among its examples of that resistance. An organised refusal of cooperation aimed at self-government is resistance of that kind."),
 dict(q="Why does this topic's reasoning process, continuity and change, fit the framework's statement about territorial holdings?",
   choices=[
     "Because the statement records holdings kept and, alongside that, territories gained and resistance encountered",
     "Because the statement records only what stayed the same and nothing that changed",
     "Because the statement records only what changed and nothing that stayed the same",
     "Because the statement concerns a single year rather than a period",
     "Because the statement concerns economic policy rather than territory"], ans=0,
   why="KC-6.2.I.B pairs a continuity, control predominantly maintained between the two world wars, with two changes: additional territories gained through conquest or treaty settlement, and anti-imperial resistance faced. Both sides of the reasoning process are present in one sentence."),
 dict(q="An unattributed leaflet distributed at a dockworkers' strike in a colonial port demands equal wages and an end to rule from abroad. Under the framework's headings, this is best classified as",
   choices=[
     "anti-imperial resistance of the kind the CED illustrates with West African strikes and congresses",
     "a territorial gain achieved through treaty settlement",
     "a territorial gain achieved through conquest",
     "an instance of government intervention in the economy after the depression",
     "a strategy of wartime mobilization directed at a colonial population"], ans=0,
   why="The CED prints West African resistance in the form of strikes and congresses to French rule among its examples of anti-imperial resistance beside KC-6.2.I.B. A strike joining a wage demand to a demand about who governs is that kind of resistance."),
 dict(q="A historian claims that every addition to an empire in this period was made by force. What does the framework's wording show?",
   choices=[
     "That the framework records treaty settlement alongside conquest as a route to additional territory",
     "That the framework records conquest as the only route to additional territory",
     "That the framework records no additions to any empire in this period",
     "That the framework records additions only outside Asia",
     "That the framework records additions only by states that had lost the war"], ans=0,
   why="KC-6.2.I.B says imperial states in some cases gained additional territories through conquest or treaty settlement. The conjunction is the framework's own, and the CED's mandate example is a gain of the second kind."),
 dict(q="Which of the following best explains why the League of Nations mandate transfers count as a change in territorial holdings rather than a continuity?",
   choices=[
     "Because territory passed from one imperial power to others, altering who administered it",
     "Because the territory ceased to be administered by any state at all",
     "Because the population of the territory was removed from it",
     "Because the transfer reversed the outcome of the war that preceded it",
     "Because the territory was returned to the state that had held it before the war"], ans=0,
   why="KC-6.2.I.B counts additional territories gained through treaty settlement among the changes of the period, and the CED prints the transfer of former German colonies to Great Britain and France under the mandate system as its example. What changes is which power administers the territory."),
 dict(q="An unattributed speech by a colonial official tells an audience at home that the colonies are contented and well governed. What does the audience tell a historian about the source's use?",
   choices=[
     "It is addressed to people who fund and vote on colonial policy, which shapes what it reports",
     "It is addressed to the colonised population, which makes it a record of their views",
     "It is addressed to no one in particular, so its content cannot be interpreted",
     "It is addressed to a later generation of historians, which makes it reliable",
     "It is addressed to a foreign government, which makes it a treaty document"], ans=0,
   why="Suggested skill 2.C names audience among the things that shape a source's significance and limit its uses. KC-6.2.I.B records that imperial states faced anti-imperial resistance in some cases, which an address to metropolitan supporters has reason to leave out."),
 dict(q="Which statement about Japan's position in the framework's account of this period is accurate?",
   choices=[
     "Japan is named alongside Western states as an imperial power maintaining colonial holdings",
     "Japan is named as a colony held by a Western imperial power",
     "Japan is named only among the states that faced anti-imperial resistance and held no colonies",
     "Japan is not mentioned in the framework's account of this period",
     "Japan is named only in connection with the peace settlement that ended the war"], ans=0,
   why="KC-6.2.I.B names Western and Japanese imperial states together as the states that predominantly maintained control over colonial holdings between the two world wars, and the CED prints Manchukuo and the Greater East Asia Co-Prosperity Sphere among its examples of territorial gains."),
 dict(q="A researcher wants evidence about whether an imperial power's control of a territory was being contested in the interwar years. Which material is most directly useful?",
   choices=[
     "Records of strikes, congresses and other organised protest in that territory",
     "The imperial power's own budget for naval construction",
     "The tonnage of goods shipped between two other empires",
     "The text of an alliance treaty signed before the First World War",
     "Production totals from factories in the imperial power's home country"], ans=0,
   why="KC-6.2.I.B states that imperial states in some cases faced anti-imperial resistance, and the CED illustrates that with congresses and strikes. Records of organised protest in the territory bear on the contested-control question directly."),
 dict(q="How does the framework's account of this period relate to its account of the twentieth century as a whole?",
   choices=[
     "Imperial control is described as predominantly maintained between the wars, while over the century empires gave way to new states",
     "Imperial control is described as already ended between the wars, and as restored later in the century",
     "Imperial control is described as unchanged from 1900 to the present",
     "Imperial control is described as having begun only after the Second World War",
     "Imperial control is described as a matter the framework does not address"], ans=0,
   why="KC-6.2.I.B places the interwar years under maintained control, while KC-6.2.I states that both land-based and maritime empires gave way to new states by the century's end. The two statements describe different stretches of the same century and the anchor carries both."),
 dict(q="What does the word 'predominantly' add to the framework's statement about colonial control between the wars?",
   choices=[
     "It allows for exceptions rather than asserting that control was maintained everywhere",
     "It asserts that control was maintained everywhere without exception",
     "It asserts that control was lost in most places",
     "It restricts the statement to a single imperial power",
     "It restricts the statement to a single year of the period"], ans=0,
   why="KC-6.2.I.B says imperial states predominantly maintained control over colonial holdings, and the same sentence goes on to record cases of gain and cases of resistance. A qualifier of that kind states the general pattern while leaving room for the exceptions the sentence itself names."),
 dict(q="An unattributed newspaper article published in an imperial capital describes a distant strike as the work of a small minority. Which reading is best supported by the framework?",
   choices=[
     "The description may understate resistance that the framework records imperial states as facing",
     "The description settles the question of how widely the strike was supported",
     "The description shows that no strike took place",
     "The description shows that the territory had already become independent",
     "The description shows that the strike concerned wages alone and not colonial rule"], ans=0,
   why="KC-6.2.I.B states that imperial states in some cases faced anti-imperial resistance. Suggested skill 2.C asks what a source's point of view does to its report, and a paper published where colonial policy is made is positioned to minimise the scale of protest rather than to measure it."),
 dict(q="A territory changes hands under an agreement drawn up by the victorious powers after a war. In the framework's terms this is",
   choices=[
     "an additional territory gained through treaty settlement",
     "an additional territory gained through conquest",
     "an instance of anti-imperial resistance",
     "a case of colonial control being maintained unchanged",
     "a case of an empire giving way to a new state"], ans=0,
   why="KC-6.2.I.B names conquest or treaty settlement as the two routes by which imperial states gained additional territories, and a transfer arranged by the victors in a postwar agreement is the treaty route rather than the military one."),
 dict(q="Which research question follows most directly from this topic's learning objective?",
   choices=[
     "What stayed the same and what changed in territorial holdings from 1900 to the present",
     "Which imperial officials were the most competent administrators",
     "How many ships each empire built in each year of the period",
     "Which languages were taught in colonial schools",
     "How the climate of each colonial territory changed over the period"], ans=0,
   why="Unit 7 Learning Objective E asks students to explain the continuities and changes in territorial holdings from 1900 to the present, so a question framed as what stayed the same and what changed restates the objective."),
 dict(q="Two colonial territories in the same period show very different levels of organised protest. What does the framework allow a student to conclude?",
   choices=[
     "That resistance was faced in some cases rather than in every case",
     "That resistance was faced in every colonial territory equally",
     "That no colonial territory experienced resistance in this period",
     "That the territory with less protest had already become independent",
     "That the territory with more protest had been gained by conquest"], ans=0,
   why="KC-6.2.I.B says imperial states in other cases faced anti-imperial resistance, which places resistance in some holdings and not as a uniform condition of all of them. The framework supplies no rule linking the level of protest to how a territory was acquired."),
 dict(q="Why is the phrase 'unresolved tensions' an apt title for what the framework describes in this period?",
   choices=[
     "Because imperial control continued while resistance to it was being organised",
     "Because every dispute of the period had been settled by treaty",
     "Because no state held territory outside its own borders after the war",
     "Because the imperial powers had agreed to give up their holdings",
     "Because the framework describes the period as free of conflict"], ans=0,
   why="KC-6.2.I.B has imperial states predominantly maintaining control while in some cases facing anti-imperial resistance. Control continuing and resistance mounting at the same time is a tension the period leaves standing."),
 dict(q="An unattributed petition from a colonial territory asks the imperial government for a share in the making of its own laws. This document is most useful as evidence of",
   choices=[
     "the political demands of an organised anti-imperial movement",
     "the imperial government's own intentions for the territory",
     "the number of people living in the territory",
     "the outcome of a treaty settlement between two empires",
     "the level of industrial production in the imperial home country"], ans=0,
   why="KC-6.2.I.B records anti-imperial resistance among what imperial states faced, and the CED illustrates it with congresses as well as strikes. A petition states the movement's demands; it does not report the government's intentions or any figure about the territory."),
 dict(q="Which pairing correctly matches one of the framework's three elements with an example the CED prints for it?",
   choices=[
     "Territorial gain, illustrated by the transfer of former German colonies under the mandate system",
     "Anti-imperial resistance, illustrated by the transfer of former German colonies under the mandate system",
     "Territorial gain, illustrated by the Indian National Congress",
     "Maintained control, illustrated by West African strikes against French rule",
     "Anti-imperial resistance, illustrated by the Greater East Asia Co-Prosperity Sphere"], ans=0,
   why="The CED prints the mandate transfers and the Manchukuo case under territorial gains, and the Indian National Congress and West African strikes and congresses under anti-imperial resistance. Only the keyed pairing puts an example under the heading KC-6.2.I.B gives it."),
 dict(q="A source produced by an anti-imperial organisation reports mass support for its programme. How should it be weighed?",
   choices=[
     "As evidence of the movement's claims and activity, with its purpose of persuasion taken into account",
     "As a neutral measurement of how many people supported the movement",
     "As proof that the imperial administration had already withdrawn",
     "As a document of the imperial government's policy",
     "As useless, because a movement's own source can never be evidence"], ans=0,
   why="Suggested skill 2.C asks students to weigh point of view and purpose rather than accept or discard a source. KC-6.2.I.B records that imperial states faced anti-imperial resistance, which such a document evidences; how far its support claims went is a separate question."),
 dict(q="Which statement is inconsistent with the framework's account of territorial holdings between the wars?",
   choices=[
     "Imperial states gave up control of their colonial holdings during these years",
     "Imperial states predominantly maintained control of their colonial holdings",
     "Some imperial states gained additional territories through conquest",
     "Some imperial states gained additional territories through treaty settlement",
     "Some imperial states faced organised anti-imperial resistance"], ans=0,
   why="KC-6.2.I.B states that Western and Japanese imperial states predominantly maintained control over colonial holdings between the two world wars, so a general surrender of control contradicts the sentence while the other four restate its three parts."),
 dict(q="What is the most accurate summary of KC-6.2.I.B for a student revising this topic?",
   choices=[
     "Control mostly held, some territories added by conquest or treaty, and resistance faced in some places",
     "Control mostly lost, no territories added, and no resistance faced anywhere",
     "Control mostly held, no territories added, and resistance faced everywhere",
     "Control mostly lost, many territories added by conquest, and no resistance faced",
     "Control transferred in full to an international body, with no resistance recorded"], ans=0,
   why="KC-6.2.I.B combines a continuity with two changes: predominantly maintained control, additional territories gained in some cases through conquest or treaty settlement, and anti-imperial resistance faced in others. A summary has to carry all three, which is what the anchor does."),
]
