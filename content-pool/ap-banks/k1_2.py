# AP COMPARATIVE GOVERNMENT AND POLITICS 1.2 Defining Political Organizations
# CED effective Fall 2026, Unit 1 Political Systems, Regimes, and Governments.
# Enduring understanding PAU-1; learning objective PAU-1.A (describe differences
# between regimes, states, nations, and governments). Suggested skill 1.A.
#
# Essential knowledge relied on:
#   PAU-1.A.1  a POLITICAL SYSTEM comprises the laws, ideas and procedures that
#              address who should have authority to rule and what the
#              government's influence on its people and economy should be
#   PAU-1.A.2  a STATE is a political organization combining a permanent
#              population with governing institutions to exercise control over a
#              defined territory with international recognition; a REGIME is the
#              fundamental rules that control access to and the exercise of
#              political power, and regimes typically ENDURE FROM GOVERNMENT TO
#              GOVERNMENT
#   PAU-1.A.3  a regime can be characterized as democratic or authoritarian
#              based on how it sets rules or makes decisions about how to
#              exercise power
#   PAU-1.A.4  a GOVERNMENT is the set of institutions or individuals legally
#              empowered to make binding decisions for a state; its authority
#              derives from the state's legitimate right to use power to enforce
#              policies and decisions; the right and power to govern itself
#              without outside interference is a crucial aspect of SOVEREIGNTY;
#              a sovereign state has independent legal authority over a
#              population in a particular territory
#   PAU-1.A.5  a NATION is a group of people with commonalities including race,
#              language, religion, ethnicity, political identity and aspirations
#
# The four terms are near-synonyms in ordinary English and the whole point of
# the topic is that they are not synonyms here, so every scenario item below is
# built so that exactly one of the four has anything to act on. Country
# illustrations are limited to what the CED itself states: the United Kingdom's
# Scottish, English, Welsh and Irish nations and Nigeria's more than 250 ethnic
# groups are LEG-2.A.1f and LEG-2.A.1d; Russia's ethnic Russians at more than 80
# percent is LEG-2.A.1e.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("1.2", "Defining Political Organizations", 1)

_T_NATION = dict(
    headers=["Country", "Largest ethnic or national group as share of population (hypothetical)",
             "Number of recognized minority groups (hypothetical)"],
    rows=[["Country W", "82%", "20"],
          ["Country X", "56%", "8"],
          ["Country Y", "29%", "250"],
          ["Country Z", "91%", "55"]])

QUESTIONS = [
 dict(q="A political organization has a permanent population, governing institutions that exercise control over a defined territory, and recognition by other countries. The framework calls this organization a",
   choices=[
     "state",
     "nation",
     "regime",
     "government",
     "political culture"], ans=0,
   why="EK PAU-1.A.2 defines a state by exactly these three elements together. A nation is a people rather than a territorial organization, a regime is a set of rules, and a government is the officials and institutions currently in office."),
 dict(q="A country holds an election, the governing party loses, and a new prime minister and cabinet take office. The constitutional rules governing how power is won and used are unchanged. What has changed?",
   choices=[
     "the government, but not the regime",
     "the regime, but not the government",
     "both the regime and the state",
     "the state, but not the government",
     "the nation, but not the state"], ans=0,
   why="EK PAU-1.A.2 says regimes are the fundamental rules controlling access to and exercise of power and typically endure from government to government. An election replaces officeholders while leaving those rules intact, which is a change of government only."),
 dict(q="Which of the following would count as a change of regime rather than a change of government?",
   choices=[
     "A country replaces its constitution, abolishes competitive elections, and vests lawmaking in a single party",
     "A president completes a term and is succeeded by a rival from another party",
     "A prime minister reshuffles the cabinet after a poor by-election result",
     "A legislature passes a budget over the executive's objections",
     "A head of state makes a state visit to a neighbouring country"], ans=0,
   why="EK PAU-1.A.2 defines a regime as the fundamental rules controlling access to and exercise of political power. Replacing the constitution and abolishing competitive elections changes those rules themselves; the other four are events that occur inside unchanged rules."),
 dict(q="A group of people share a language, a religious tradition, a sense of common history and a desire for self-government, but they hold no territory of their own and are not recognized by other countries. In the framework's terms they are",
   choices=[
     "a nation but not a state",
     "a state but not a nation",
     "a regime but not a government",
     "a government but not a state",
     "a political system but not a regime"], ans=0,
   why="EK PAU-1.A.5 defines a nation by commonalities of race, language, religion, ethnicity, political identity and aspirations, none of which requires territory. EK PAU-1.A.2 makes territory and international recognition necessary to a state, and this group has neither."),
 dict(q="The set of institutions and individuals legally empowered to make binding decisions for a state is the",
   choices=[
     "government",
     "regime",
     "nation",
     "civil society",
     "political culture"], ans=0,
   why="EK PAU-1.A.4 gives this as the definition of a government. The regime is the rules under which those institutions operate, a nation is a people, and civil society is by definition autonomous from the state rather than empowered to bind it."),
 dict(q="The framework describes sovereignty as centrally involving",
   choices=[
     "the right and power of a state to govern itself without outside interference",
     "the right of a nation to preserve its language and religion",
     "the ability of a government to win a national election",
     "the ability of a legislature to override an executive veto",
     "recognition of a political party by other parties"], ans=0,
   why="EK PAU-1.A.4 states that the right and power to govern itself without outside interference is a crucial aspect of a state's sovereignty, and that a sovereign state has independent legal authority over a population in a particular territory."),
 dict(q="A regime is characterized as democratic or authoritarian on the basis of",
   choices=[
     "how it sets rules and makes decisions about the exercise of power",
     "the size of the territory it controls",
     "whether its population shares a single language",
     "the number of ministries in its cabinet",
     "whether its economy is growing"], ans=0,
   why="EK PAU-1.A.3 states this directly. The classification turns on the rules governing access to and exercise of power, not on territory, ethnic composition, administrative structure or economic performance."),
 dict(q="The laws, ideas and procedures that address who should have authority to rule and how far government should reach into people's lives and the economy are what the framework calls a",
   choices=[
     "political system",
     "nation",
     "state",
     "cabinet",
     "civil society"], ans=0,
   why="EK PAU-1.A.1 gives exactly this definition of a political system. It is broader than the state, which is a territorial organization, and broader than the government, which is the set of officeholders."),
 dict(q="A country's borders and international recognition are unchanged, its constitution is unchanged, but a new party has taken office after an election. Which of the following is the most accurate description?",
   choices=[
     "The state and regime persist; the government has changed",
     "The state persists; the regime and government have both changed",
     "The regime persists; the state has changed",
     "The nation has changed; the state persists",
     "All three have changed together"], ans=0,
   why="EK PAU-1.A.2 separates the three: unchanged borders and recognition mean the state persists, an unchanged constitution means the fundamental rules of access to power persist, and a new party in office is a change of officeholders alone."),
 dict(q="Which of the following pairs of course countries are both states in which more than one nation is commonly identified?",
   choices=[
     "The United Kingdom and Nigeria",
     "China and the United Kingdom only because both are unitary",
     "Mexico and Russia, because both are federal",
     "Iran and Mexico, because both hold presidential elections",
     "Russia and China, because both border many countries"], ans=0,
   why="EK LEG-2.A.1f identifies Scottish, English, Welsh and Irish national differences within the United Kingdom, and EK LEG-2.A.1d identifies more than 250 ethnic groups within Nigeria. The other pairings rest on unitary or federal structure, election type or geography, none of which bears on how many nations a state contains."),
 dict(q="A political scientist writes that a country's regime 'outlived four prime ministers.' The statement is best understood to mean that",
   choices=[
     "the fundamental rules for gaining and using power stayed in place while officeholders came and went",
     "the same person governed under four different constitutions",
     "the country ceased to be a state four times",
     "four different nations occupied the same territory",
     "the country's sovereignty was interrupted four times"], ans=0,
   why="EK PAU-1.A.2 says regimes typically endure from government to government. A succession of prime ministers is a succession of governments; the regime outliving them is the framework's expected relationship, not an unusual one."),
 dict(q="Which of the following most directly threatens a state's sovereignty as the framework defines it?",
   choices=[
     "A foreign power exercises legal authority over part of the state's territory",
     "The governing party loses seats at a general election",
     "A cabinet minister resigns over a policy disagreement",
     "A national legislature passes a law the executive opposes",
     "A supreme court strikes down an act of the legislature"], ans=0,
   why="EK PAU-1.A.4 makes independent legal authority over a population in a particular territory, free of outside interference, the core of sovereignty. Only foreign legal authority over the territory touches that; the rest are ordinary internal politics."),
 dict(q="An observer notes that a country has a permanent population and governing institutions, but that most other countries refuse to recognize it. Under the framework's definition, its status as a state is doubtful because it lacks",
   choices=[
     "international recognition",
     "a defined territory",
     "a shared language",
     "a written constitution",
     "a growing economy"], ans=0,
   why="EK PAU-1.A.2 lists a permanent population, governing institutions, control over a defined territory and international recognition. The first three are present in this case and the fourth is not, so recognition is what is missing."),
 dict(q="Which statement best captures the relationship between a regime and a government?",
   choices=[
     "A regime sets the rules within which governments are formed and replaced",
     "A government sets the rules within which regimes are formed and replaced",
     "A regime and a government are two words for the same institutions",
     "A government must be replaced whenever a regime endures",
     "A regime exists only in authoritarian systems"], ans=0,
   why="EK PAU-1.A.2 makes the regime the fundamental rules controlling access to and exercise of power, and says regimes endure from government to government. The rules therefore frame the succession of governments rather than the other way round, and both democratic and authoritarian systems have regimes."),
 dict(q="A country's constitution is suspended by the military, elections are cancelled, and a council of officers assumes lawmaking power. Which of the framework's categories has most clearly changed?",
   choices=[
     "the regime, because the rules of access to power have been replaced",
     "the state, because the territory is now differently defined",
     "the nation, because the population's commonalities have changed",
     "the political culture, because attitudes must have changed instantly",
     "nothing, because the same territory and population remain"], ans=0,
   why="EK PAU-1.A.2. Suspending the constitution and cancelling elections replaces the fundamental rules controlling access to and the exercise of political power, which is what distinguishes a change of regime from a change of government."),
 dict(q="The table gives hypothetical figures on the ethnic and national composition of four unnamed states. Which state's composition most resembles the framework's description of Nigeria?",
   table=_T_NATION,
   choices=[
     "Country Y, because no group approaches a majority and the number of recognized groups is by far the largest",
     "Country W, because a single group holds a large majority",
     "Country X, because the largest group is just above half",
     "Country Z, because it has the highest share for its largest group",
     "None, because the framework gives no figures for any country"], ans=0,
   why="EK LEG-2.A.1d describes Nigeria as containing more than 250 ethnic groups with no single group dominant, and the table's Country Y is the only row with both a sub-thirty-percent largest group and a group count in the hundreds. The rows with 82, 56 and 91 percent all have a leading group far larger than that."),
 dict(q="Using the same hypothetical figures, which state most resembles the framework's description of Russia, where the largest group is more than 80 percent of the population?",
   table=_T_NATION,
   choices=[
     "Country W, at 82 percent",
     "Country X, at 56 percent",
     "Country Y, at 29 percent",
     "Country Z, at 91 percent, because that is closest to the whole population",
     "Country Y, because Russia contains many minority groups"], ans=0,
   why="EK LEG-2.A.1e states that ethnic Russians are more than 80 percent of the population. Country W's 82 percent is the value just above that threshold; Country Z's 91 percent is more than 80 percent as well but is far from the framework's figure, and a match should be the closest value above the stated line, not merely any value above it."),
 dict(q="Two neighbouring states each contain a large community that speaks the same language and identifies with the same historical homeland. In the framework's terms, this community is best described as",
   choices=[
     "a nation divided across two states",
     "a state divided across two nations",
     "two regimes sharing one government",
     "a government without a state",
     "a political system without a regime"], ans=0,
   why="EK PAU-1.A.5 defines a nation by shared language, identity and aspirations rather than by borders, so nothing prevents a nation from lying across a state boundary. EK PAU-1.A.2's state, by contrast, is defined by a single defined territory."),
 dict(q="Which of the following best explains why the framework treats 'state' and 'government' as different concepts?",
   choices=[
     "The state persists as a legal and territorial entity while the individuals and institutions empowered to make binding decisions for it are replaced",
     "The state is always democratic while the government may be authoritarian",
     "The state is a group of people while the government is a territory",
     "The state exists only in federal systems while the government exists only in unitary systems",
     "The government is recognized internationally while the state is not"], ans=0,
   why="EK PAU-1.A.2 and EK PAU-1.A.4 taken together: the state is the territorial organization with a permanent population and international recognition, while the government is the current set of institutions and individuals legally empowered to bind it. One outlasts the other."),
 dict(q="A commentator argues that a country 'has a government but is not really a state.' The strongest evidence for that argument would be that the country",
   choices=[
     "does not exercise effective control over a defined territory recognized by other countries",
     "has recently changed its prime minister",
     "contains more than one ethnic group",
     "has a written constitution that has never been amended",
     "belongs to several international organizations"], ans=0,
   why="EK PAU-1.A.2's state requires control over a defined territory with international recognition, so the absence of that control is what would make the label doubtful. Leadership turnover, ethnic diversity, constitutional stability and treaty membership all coexist comfortably with statehood."),
 dict(q="Which of the following most clearly illustrates the exercise of a government's authority as the framework describes it?",
   choices=[
     "A legislature enacts a tax that residents are legally obliged to pay",
     "A newspaper publishes an editorial criticizing a tax",
     "A professional association issues guidance to its members",
     "A religious body advises worshippers on charitable giving",
     "A foreign firm decides where to invest"], ans=0,
   why="EK PAU-1.A.4 defines a government as the institutions and individuals legally empowered to make BINDING decisions for a state. Only the enacted tax binds; the other four are influential but leave residents legally free to disregard them."),
 dict(q="A country's regime type is disputed: it holds elections, but the same party wins every time and opposition candidates are removed from the ballot. Applying the framework's criterion, the dispute is best resolved by examining",
   choices=[
     "how the rules of access to power actually operate in practice, not merely that elections occur",
     "the size of the country's population",
     "whether the country is federal or unitary",
     "how many nations live within the country's borders",
     "whether the country's economy is growing"], ans=0,
   why="EK PAU-1.A.3 makes the classification depend on how a regime sets rules and makes decisions about exercising power. The holding of an election is one such rule; whether opponents may contest it is another, and both belong to the same assessment."),
 dict(q="Which of the following is the clearest example of a change in a country's political system as EK PAU-1.A.1 uses that term?",
   choices=[
     "A country adopts a new settlement of who may rule and how far the government may direct the economy",
     "A minister is replaced after a scandal",
     "A city council changes its refuse collection schedule",
     "A national football team changes its manager",
     "A political party changes its logo"], ans=0,
   why="EK PAU-1.A.1 defines a political system as the laws, ideas and procedures addressing who should have authority to rule and what government's influence on people and economy should be. Only the first option alters both of those, and the others do not touch either."),
 dict(q="'Sovereignty' and 'legitimacy' differ in that sovereignty concerns",
   choices=[
     "a state's independent legal authority over a population and territory",
     "whether citizens believe their government has the right to use power as it does",
     "the number of political parties allowed to compete",
     "the fairness of a country's electoral districts",
     "the size of a government's budget"], ans=0,
   why="EK PAU-1.A.4 locates sovereignty in independent legal authority free of outside interference, while EK LEG-1.A.1 locates legitimacy in whether a government's constituents believe it has the right to use power in the way it does. The first is a legal standing, the second a belief."),
 dict(q="A single state contains several nations, and one of them presses for its own independent state. Which framework distinction does this situation most directly illustrate?",
   choices=[
     "that a nation and a state need not coincide",
     "that a regime and a government need not coincide",
     "that sovereignty and territory need not coincide",
     "that a political system and a political culture need not coincide",
     "that a legislature and an executive need not coincide"], ans=0,
   why="EK PAU-1.A.5's nation is a people with shared commonalities and aspirations, while EK PAU-1.A.2's state is a territorial organization with recognition. A secession demand is precisely a demand that the two be made to coincide, which presupposes that they currently do not."),
 dict(q="Which of the following would a comparativist classify as an attribute of a regime rather than of a particular government?",
   choices=[
     "The constitutional rule fixing how a head of government is selected",
     "The current head of government's policy on public transport",
     "The name of the party currently holding a legislative majority",
     "The identity of the current finance minister",
     "The date of the most recent cabinet reshuffle"], ans=0,
   why="EK PAU-1.A.2 assigns to the regime the fundamental rules controlling access to power. A selection rule is such a rule and survives every change of officeholder; the other four describe who currently holds office and what they are doing."),
 dict(q="Which statement about states and nations is consistent with the framework?",
   choices=[
     "A state may contain many nations, and a nation may extend beyond one state",
     "Every state contains exactly one nation",
     "Every nation controls exactly one state",
     "A nation must possess international recognition to exist",
     "A state must share a single language to be sovereign"], ans=0,
   why="EK PAU-1.A.2 defines the state territorially and EK PAU-1.A.5 defines the nation by shared commonalities, so the two are independent. The CED's own cleavage statements describe several nations inside single states, including the Scottish, English, Welsh and Irish within the United Kingdom."),
 dict(q="A new country is admitted to international organizations, its borders are accepted by its neighbours, and it establishes a legislature, an executive and courts. Which of the following has it acquired?",
   choices=[
     "the attributes of a state, including the governing institutions and recognition the framework requires",
     "a nation, since its people now share a political identity",
     "a political culture, since its institutions now exist",
     "legitimacy, since other countries have recognized it",
     "sovereignty over its neighbours' territory as well as its own"], ans=0,
   why="EK PAU-1.A.2's list is satisfied: permanent population, governing institutions, defined and accepted territory, international recognition. Recognition by others is not the same as EK LEG-1.A.1's legitimacy, which concerns the beliefs of a government's own constituents."),
 dict(q="A researcher wants to compare the six course countries on the dimension EK PAU-1.A.3 uses to classify regimes. The most appropriate comparison would examine",
   choices=[
     "the rules by which each country's leaders gain office and the constraints on how they use power once there",
     "the total population of each country",
     "the number of provinces or states in each country",
     "each country's principal exports",
     "the age of each country's capital city"], ans=0,
   why="EK PAU-1.A.3 makes the democratic-authoritarian classification depend on how a regime sets rules and makes decisions about exercising power. Rules of access and constraints on exercise are exactly those two halves; the remaining options are descriptive facts with no bearing on the classification."),
 dict(q="Which of the following best explains why the framework says regimes 'typically endure from government to government'?",
   choices=[
     "The rules of access to power are ordinarily changed far less often than the officeholders those rules select",
     "Governments are constitutionally forbidden from lasting more than one term",
     "Regimes are protected from change by international organizations",
     "Officeholders are chosen by the regime rather than by any electorate",
     "A regime cannot be changed once a constitution has been written"], ans=0,
   why="EK PAU-1.A.2's phrase describes the ordinary rhythm of politics: elections, appointments and successions replace officeholders frequently, while the constitutional rules that structure those events are amended rarely. EK PAU-1.D.3 makes clear that regimes can nonetheless change, so the endurance is a tendency, not a bar."),
]
