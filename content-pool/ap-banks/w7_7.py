# AP WORLD HISTORY: MODERN 7.7 Conducting World War II
# CED effective Fall 2026, Unit 7 Global Conflict, c. 1900 to the present.
# Thematic focus Governance (GOV). Unit 7 Learning Objective G: explain
# similarities and differences in how governments used a variety of methods to
# conduct war. Reasoning process: comparison. Suggested skill 3.D, explain how
# claims or evidence support, modify, or refute a source's argument.
#
# THE HISTORICAL DEVELOPMENTS THIS TOPIC RESTS ON, in the framework's own words:
#   KC-6.2.IV.A.ii   World War II was a total war. Governments used a variety of
#                    strategies, including political propaganda, art, media, and
#                    intensified forms of nationalism, to mobilize populations
#                    (both in the home countries and the colonies or former
#                    colonies) for the purpose of waging war. Governments used
#                    ideologies, including fascism and communism to mobilize all
#                    of their state's resources for war and, in the case of
#                    totalitarian states, to repress basic freedoms and dominate
#                    many aspects of daily life during the course of the
#                    conflicts and beyond.
#   KC-6.1.III.C.ii  New military technology and new tactics, including the
#                    atomic bomb, fire-bombing, and the waging of "total war",
#                    led to increased levels of wartime casualties.
#
# THE COMPARISON THIS TOPIC IS BUILT ON. The framework says governments used
# strategies to mobilize populations without restricting that to any one kind of
# state, and the CED prints its examples under two headings that BOTH read
# "mobilizing for war" -- Western democracies (Great Britain under Winston
# Churchill, United States under Franklin Roosevelt) and totalitarian states
# (Germany under Adolf Hitler, USSR under Joseph Stalin). The difference sits in
# one clause: repressing basic freedoms and dominating many aspects of daily life
# is stated "in the case of totalitarian states". Similarity in mobilization,
# difference in repression, is the axis of items 8, 14, 15, 16 and 18.
#
# BOUNDARY WITH 7.3. The first war's conduct is KC-6.2.IV.A.i and KC-6.1.III.C.i.
# What the SECOND war's sentences add, and what is therefore keyed here: the
# words "or former colonies"; ideologies including fascism and communism used to
# mobilize all of the state's resources; the repression clause and its "and
# beyond"; and, in the casualty sentence, new TACTICS alongside new technology,
# with the atomic bomb, fire-bombing and the waging of total war named. Item 1
# holds the other line: the framework calls the FIRST war the first total war and
# says of the second only that it WAS a total war.
#
# WHAT IS DELIBERATELY NOT ASKED. No item keys to a date, a battle, a campaign,
# a production total, a weapon's performance, a casualty figure or anything a
# named leader is supposed to have said. The four leaders the CED names are named
# only as the CED names them, under its own two headings, and no quotation is
# attributed to any of them. KC-6.1.III.C.ii asserts a direction, that new
# technology and tactics led to increased casualties, and no item asks a student
# to quantify it, because the framework prints no number.
#
# SOURCES. The bank cannot show images, so every stimulus is an explicitly
# unattributed illustrative source described or quoted in prose, or a table of
# illustrative data whose keyed conclusion is recoverable from the table alone.
# Nothing is attributed to a real person, broadcast or publication.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md.
TOPIC = ("7.7", "Conducting World War II", 7)

_T_MOBILIZE = dict(
    headers=["State (illustrative)",
             "Share of the adult population in the armed forces or war production, first year (percent)",
             "Share of the adult population in the armed forces or war production, fourth year (percent)"],
    rows=[["State G", "14", "52"],
          ["State H", "21", "58"],
          ["State J", "9", "36"]])

_T_CASUALTY = dict(
    headers=["Combatant state (illustrative)",
             "Recorded wartime casualties in the earlier global conflict (thousands)",
             "Recorded wartime casualties in the later global conflict (thousands)",
             "Combined casualties across the two conflicts (thousands)"],
    rows=[["State S", "1,200", "3,400", "4,600"],
          ["State T", "700", "2,900", "3,600"],
          ["State U", "2,100", "5,600", "7,700"]])

QUESTIONS = [
 dict(q="The framework opens its account of how the Second World War was fought with a single characterisation of that war. What is it?",
   choices=[
     "That it was a total war",
     "That it was the first total war",
     "That it was a war fought only by professional armies",
     "That it was a war in which governments left civilian life untouched",
     "That it was a war the framework declines to characterise"], ans=0,
   why="KC-6.2.IV.A.ii opens by stating that World War II was a total war. The framework reserves the phrase 'the first total war' for the earlier conflict in KC-6.2.IV.A.i, so applying it here moves a claim from one sentence to the other."),
 dict(q="Which set of strategies does the framework name as the means by which governments mobilized populations for the Second World War?",
   choices=[
     "Political propaganda, art, media, and intensified forms of nationalism",
     "Tariffs, currency controls, rationing, and public borrowing",
     "Conscription, blockade, alliance treaties, and naval construction",
     "Public education, religious instruction, sport, and civic architecture",
     "Land redistribution, price controls, and the collectivisation of farms"], ans=0,
   why="KC-6.2.IV.A.ii names political propaganda, art, media, and intensified forms of nationalism among the strategies governments used to mobilize populations for the purpose of waging war. The other four lists are made of measures the framework does not name in that sentence."),
 dict(q="Whose populations does the framework say governments mobilized for the Second World War?",
   choices=[
     "Populations in the home countries and in the colonies or former colonies alike",
     "Populations in the home countries only",
     "Populations in the colonies only",
     "Populations in states that had remained neutral in the previous war",
     "Populations in the territories occupied during the fighting only"], ans=0,
   why="KC-6.2.IV.A.ii places in parentheses that populations were mobilized both in the home countries and the colonies or former colonies. The parenthesis names two places at once, so an answer keeping only one of them drops half of what the sentence says."),
 dict(q="Which phrase does the framework use of the second war's mobilization that it does not use of the first war's?",
   choices=[
     "The colonies or former colonies",
     "Political propaganda",
     "Intensified forms of nationalism",
     "For the purpose of waging war",
     "A variety of strategies"], ans=0,
   why="KC-6.2.IV.A.i speaks of mobilizing populations in the home countries and the colonies, while KC-6.2.IV.A.ii writes the colonies or former colonies. The other four phrases appear in both sentences, so only the extension to former colonies distinguishes the later account."),
 dict(q="For what end does the framework say these mobilizing strategies were used?",
   choices=[
     "For the purpose of waging war",
     "For the purpose of raising the general level of education",
     "For the purpose of settling a disputed border by arbitration",
     "For the purpose of relieving unemployment left by the depression",
     "For the purpose of administering colonies more cheaply"], ans=0,
   why="KC-6.2.IV.A.ii states that the strategies were used to mobilize populations for the purpose of waging war. The purpose clause is what separates these measures from cultural or economic policy in general, and the framework supplies no other end for them."),
 dict(q="Which ideologies does the framework name as ones governments used to mobilize their states for the Second World War?",
   choices=[
     "Fascism and communism",
     "Liberalism and conservatism",
     "Mercantilism and free trade",
     "Nationalism and internationalism",
     "The framework names no ideology in this connection"], ans=0,
   why="KC-6.2.IV.A.ii says governments used ideologies, including fascism and communism, to mobilize all of their state's resources for war. Those two are the framework's own examples, and intensified nationalism appears in the sentence as a mobilizing strategy rather than as one of the named ideologies."),
 dict(q="What does the framework say governments used ideologies to mobilize?",
   choices=[
     "All of their state's resources for war",
     "Only the armed forces of their state",
     "Only the industrial workforce of their state",
     "Only the populations of their colonies",
     "Only the finances of neighbouring states"], ans=0,
   why="KC-6.2.IV.A.ii states that governments used ideologies, including fascism and communism, to mobilize all of their state's resources for war. The word 'all' is the framework's, and it is what makes the claim one about total war rather than about an army or an industry."),
 dict(q="To which governments does the framework attach the repression of basic freedoms and the domination of many aspects of daily life?",
   choices=[
     "To totalitarian states in particular, rather than to every government that fought",
     "To every government that fought, without distinction between them",
     "To the Western democracies in particular, rather than to totalitarian states",
     "To colonial administrations only, and not to any home government",
     "To no government, since the framework does not raise the matter"], ans=0,
   why="KC-6.2.IV.A.ii says governments used ideologies to mobilize all of their state's resources for war and, in the case of totalitarian states, to repress basic freedoms and dominate many aspects of daily life. The qualifying clause narrows the second half of the sentence to one kind of state while the mobilization claim stays general."),
 dict(q="Over what stretch of time does the framework say totalitarian states dominated many aspects of daily life?",
   choices=[
     "During the course of the conflicts and beyond them",
     "During the course of the conflicts only, ending with the fighting",
     "Only in the years before the fighting began",
     "Only in the colonies, and only while they were being administered",
     "The framework gives no indication of how long it lasted"], ans=0,
   why="KC-6.2.IV.A.ii ends with the words 'during the course of the conflicts and beyond', which extends the repression of basic freedoms and the domination of daily life past the end of the fighting. Dropping the last two words confines a claim the framework deliberately does not confine."),
 dict(q="According to the framework, what raised levels of wartime casualties in the Second World War?",
   choices=[
     "New military technology together with new tactics",
     "New military technology alone, with no change of tactics",
     "New tactics alone, with no change of technology",
     "A larger number of states declaring war than in the previous conflict",
     "The framework does not connect casualties to how the war was fought"], ans=0,
   why="KC-6.1.III.C.ii names new military technology and new tactics together as what led to increased levels of wartime casualties, whereas KC-6.1.III.C.i names only new military technology for the first war. The anchor for this item carries both terms because dropping either one turns the second war's sentence into the first war's."),
 dict(q="Which three things does the framework name among the new technology and tactics that raised casualty levels?",
   choices=[
     "The atomic bomb, fire-bombing, and the waging of total war",
     "The machine gun, the trench, and the naval blockade",
     "The tank, the submarine, and the field telegraph",
     "Conscription, rationing, and the censorship of newspapers",
     "Political propaganda, art, and media"], ans=0,
   why="KC-6.1.III.C.ii names the atomic bomb, fire-bombing, and the waging of total war among the new military technology and new tactics that led to increased levels of wartime casualties. The remaining lists mix items the framework does not name here with mobilizing strategies from KC-6.2.IV.A.ii."),
 dict(q="Which pair does the CED print as its illustrative examples of Western democracies mobilizing for war?",
   choices=[
     "Great Britain under Winston Churchill and the United States under Franklin Roosevelt",
     "Germany under Adolf Hitler and the USSR under Joseph Stalin",
     "Great Britain under Winston Churchill and the USSR under Joseph Stalin",
     "Germany under Adolf Hitler and the United States under Franklin Roosevelt",
     "The CED prints no examples of Western democracies for this topic"], ans=0,
   why="The illustrative examples the CED prints beside KC-6.2.IV.A.ii are divided into Western democracies mobilizing for war and totalitarian states mobilizing for war, and this pair appears under the first heading. Nothing is asserted about either government beyond the heading it is printed under."),
 dict(q="Which pair does the CED print as its illustrative examples of totalitarian states mobilizing for war?",
   choices=[
     "Germany under Adolf Hitler and the USSR under Joseph Stalin",
     "Great Britain under Winston Churchill and the United States under Franklin Roosevelt",
     "Germany under Adolf Hitler and Great Britain under Winston Churchill",
     "The USSR under Joseph Stalin and the United States under Franklin Roosevelt",
     "The CED prints no examples of totalitarian states for this topic"], ans=0,
   why="The illustrative examples the CED prints beside KC-6.2.IV.A.ii are divided into two headings, and this pair appears under totalitarian states mobilizing for war. KC-6.2.IV.A.ii is also the sentence that attaches the repression of basic freedoms to totalitarian states in particular."),
 dict(q="What do the CED's two headings of illustrative examples for this topic have in common?",
   choices=[
     "Both name states mobilizing for war, so mobilization is presented as something both kinds of state did",
     "Both name states that repressed basic freedoms and dominated daily life",
     "Both name states that stayed out of the fighting until it was nearly over",
     "Both name states that had lost the previous global conflict",
     "Both name states that held no colonies at any point in the period"], ans=0,
   why="The CED prints Western democracies mobilizing for war and totalitarian states mobilizing for war as its two headings, and KC-6.2.IV.A.ii states the mobilization claim of governments generally. The repression clause in the same sentence is attached to totalitarian states alone, so it is not what the two headings share."),
 dict(q="A student concludes that only single-party states were capable of mobilizing their populations for the Second World War. What is the best correction?",
   choices=[
     "The framework's mobilization claim is made of governments generally, and the CED illustrates it with Western democracies as well",
     "The framework's mobilization claim is made of single-party states only, so the student is right",
     "The framework denies that any government mobilized its population for the second war",
     "The framework restricts mobilization to colonial administrations",
     "The framework treats mobilization as a feature of the first war and not the second"], ans=0,
   why="KC-6.2.IV.A.ii says governments used a variety of strategies to mobilize populations for the purpose of waging war, without restricting the claim to one kind of state, and the CED prints Great Britain and the United States under a heading about mobilizing for war. The distinguishing clause in that sentence concerns repression, not mobilization."),
 dict(q="An unattributed wartime pamphlet argues that only a state with a single ruling party could direct its whole population towards the war effort. Which evidence would most directly refute that argument?",
   choices=[
     "Records showing that governments in Western democracies also mobilized their populations for war",
     "Records showing that a single-party state closed its independent newspapers during the war",
     "Records showing that new tactics raised casualty levels in the fighting",
     "Records showing that a colony supplied troops to a single-party state",
     "Records showing that one single-party state produced more munitions than another"], ans=0,
   why="Suggested skill 3.D asks how evidence supports, modifies or refutes an argument. KC-6.2.IV.A.ii makes its mobilization claim of governments generally and the CED prints Western democracies mobilizing for war among its examples, so evidence of that mobilization contradicts the pamphlet's exclusive claim rather than qualifying it."),
 dict(q="An unattributed account written after the war argues that the fighting reached further into civilian life than any earlier conflict had. Which evidence would most directly support that argument?",
   choices=[
     "Records showing that governments assigned civilians to war production and directed media towards the war effort",
     "Records showing that the armies were commanded by professional officers",
     "Records showing that war was declared by governments rather than by assemblies",
     "Records of the tonnage of merchant shipping built in the years before the war",
     "Records showing that colonies were administered by appointed governors"], ans=0,
   why="Suggested skill 3.D asks how evidence supports an argument. KC-6.2.IV.A.ii calls World War II a total war and names media among the strategies used to mobilize populations, while stating that governments mobilized all of their state's resources for war, so evidence of civilians directed into war work is evidence for the claim."),
 dict(q="An unattributed account argues that every wartime government dominated its people's daily lives to the same degree. Which evidence would most directly modify that argument while leaving the claim that governments mobilized their populations standing?",
   choices=[
     "Evidence that some governments mobilized their populations without repressing basic freedoms",
     "Evidence that no government mobilized its population at all",
     "Evidence that all the combatant governments used the same weapons",
     "Evidence that casualty levels rose in the later of the two wars",
     "Evidence that colonies supplied no troops to any combatant"], ans=0,
   why="Suggested skill 3.D distinguishes modifying an argument from refuting it. KC-6.2.IV.A.ii attaches the repression of basic freedoms and the domination of daily life to totalitarian states in particular while stating the mobilization claim generally, so such evidence narrows the account's scope without overturning its mobilization claim."),
 dict(q="The table below reports illustrative figures for the share of the adult population engaged in the armed forces or in war production in three states, in the first and fourth years of the war. Which conclusion is best supported?",
   table=_T_MOBILIZE,
   choices=[
     "The share rises in every state, and the largest increase in percentage points is in State G",
     "The share rises in every state, and the largest increase in percentage points is in State H",
     "The share falls in every state between the two years shown",
     "Only one of the three states engages any of its adult population in this way",
     "The three states reach the same share by the fourth year"], ans=0,
   why="Read from the table alone: every fourth-year share exceeds its first-year share, none is zero, and subtracting gives one state the largest increase, which is not the state that began highest. KC-6.2.IV.A.ii states that governments mobilized all of their state's resources for war, and a rising share of the adult population in war work is the kind of evidence that bears on it."),
 dict(q="The table below reports illustrative casualty figures for three combatant states across the two global conflicts of the period. Which conclusion is best supported?",
   table=_T_CASUALTY,
   choices=[
     "Recorded casualties are higher in the later conflict for every state, and the largest increase is in State U",
     "Recorded casualties are higher in the later conflict for every state, and the largest increase is in State T",
     "Recorded casualties are lower in the later conflict for every state",
     "Only one of the three states records any casualties in the later conflict",
     "The state with the most casualties in the earlier conflict records the smallest increase"], ans=0,
   why="Read from the table alone: every later figure exceeds its earlier one, the combined column agrees with the two it sums, and subtracting gives one state the largest increase, which is the state that recorded the most casualties in the earlier conflict as well. KC-6.1.III.C.ii states that new military technology and new tactics led to increased levels of wartime casualties."),
 dict(q="An unattributed poster text from the period, reproduced in prose, tells readers at home that the shell they finish today is fired tomorrow and that no worker stands outside the fight. The text is best used as evidence of",
   choices=[
     "political propaganda used to mobilize a home population for the purpose of waging war",
     "an ideology used to repress basic freedoms in a totalitarian state",
     "a new tactic that raised the level of wartime casualties",
     "the mobilization of a colonial population by an imperial government",
     "a government withdrawing from an active role in economic life"], ans=0,
   why="KC-6.2.IV.A.ii names political propaganda among the strategies governments used to mobilize populations, in the home countries and the colonies or former colonies, for the purpose of waging war. A text addressed to workers at home about their part in the fighting is that strategy directed at the home population."),
 dict(q="An unattributed recruiting appeal circulated in a territory that had until recently been governed as a colony calls on its inhabitants to enlist in the armed forces of the state that had governed it. Under the framework, this appeal illustrates",
   choices=[
     "mobilization reaching the colonies or former colonies as well as the home countries",
     "mobilization confined to the home countries of the combatant states",
     "the repression of basic freedoms in a totalitarian state",
     "a new military tactic that raised the level of wartime casualties",
     "the transfer of a colony from one imperial power to another by treaty"], ans=0,
   why="KC-6.2.IV.A.ii states that governments mobilized populations both in the home countries and the colonies or former colonies for the purpose of waging war. An appeal addressed to a recently governed territory falls inside the second half of that parenthesis, which is the phrase the framework adds for the second war."),
 dict(q="An unattributed wartime decree issued by a one-party state closes every independent newspaper, requires official permission for travel between towns and assigns each worker to a designated place of employment. The decree is best used as evidence of",
   choices=[
     "the repression of basic freedoms and domination of daily life the framework attributes to totalitarian states",
     "a strategy of political propaganda directed at a colonial population",
     "a new military technology that raised the level of wartime casualties",
     "an imperial state gaining additional territory through treaty settlement",
     "a government leaving economic life to private decision"], ans=0,
   why="KC-6.2.IV.A.ii states that governments used ideologies to mobilize all of their state's resources for war and, in the case of totalitarian states, to repress basic freedoms and dominate many aspects of daily life. Closing the press, controlling movement and directing labour reaches all three of the things that clause names."),
 dict(q="An unattributed wartime regulation controlling what may be printed is found still in force several years after the fighting has ended. How does this bear on the framework's account?",
   choices=[
     "It matches the framework's statement that such domination of daily life extended beyond the conflicts themselves",
     "It contradicts the framework, which confines such measures to the years of fighting",
     "It is irrelevant to the framework, which discusses only the years before the war",
     "It shows that the regulation had never been enforced during the war",
     "It shows that the state issuing it had ceased to be a combatant"], ans=0,
   why="KC-6.2.IV.A.ii says totalitarian states repressed basic freedoms and dominated many aspects of daily life during the course of the conflicts and beyond. A wartime control still operating after the fighting is the framework's own 'and beyond' rather than an exception to it."),
 dict(q="Which of the following does the framework NOT name among the strategies used to mobilize populations for the Second World War?",
   choices=[
     "State control of the national economy through five year plans",
     "Political propaganda",
     "Art",
     "Media",
     "Intensified forms of nationalism"], ans=0,
   why="KC-6.2.IV.A.ii names political propaganda, art, media, and intensified forms of nationalism as the mobilizing strategies. Control of a national economy through five year plans belongs to KC-6.3.I.A.i, which the framework attaches to the Soviet economy in topic 7.4 rather than to wartime mobilization."),
 dict(q="Which statement belongs to the framework's account of the second war's conduct rather than to its account of the first war's?",
   choices=[
     "Governments used ideologies, including fascism and communism, to mobilize all of the state's resources",
     "Governments used political propaganda to mobilize populations",
     "Governments used art and media to mobilize populations",
     "Governments used intensified forms of nationalism to mobilize populations",
     "New military technology led to increased levels of wartime casualties"], ans=0,
   why="KC-6.2.IV.A.i and KC-6.2.IV.A.ii both name propaganda, art, media and intensified nationalism, and both wars' casualty sentences name new military technology. The ideologies clause appears only in KC-6.2.IV.A.ii, which is the framework's statement about the second war."),
 dict(q="Which research question restates this topic's stated learning objective as an inquiry?",
   choices=[
     "In what ways were the methods governments used to conduct the war alike, and in what ways did they differ",
     "Which commander won the greatest number of engagements during the war",
     "Which state's factories produced the largest number of aircraft each year",
     "Which cities were the largest in each combatant state before the war",
     "Which crops were grown in each combatant state during the war"], ans=0,
   why="Unit 7 Learning Objective G asks students to explain similarities and differences in how governments used a variety of methods to conduct war, so a question asking in what ways the methods were alike and in what ways they differed restates the objective."),
 dict(q="Why is comparison the reasoning process the framework attaches to this topic?",
   choices=[
     "Because the framework states a mobilization claim about governments generally and then marks off one clause for totalitarian states",
     "Because the framework traces a single state's policy across a century",
     "Because the framework ranks the causes of the war against one another",
     "Because the framework describes a single campaign in detail",
     "Because the framework confines its account to one region of the world"], ans=0,
   why="KC-6.2.IV.A.ii says governments used strategies and ideologies to mobilize populations and resources, and then adds that in the case of totalitarian states they also repressed basic freedoms and dominated daily life. A general claim with an exception marked inside it is what a comparison is built from, and the CED's two headings of examples set the two kinds of state side by side."),
 dict(q="Which statement is inconsistent with the framework's account of how the Second World War was conducted?",
   choices=[
     "Governments left the populations of their colonies and former colonies out of the war effort",
     "Governments used political propaganda, art, media and intensified nationalism to mobilize populations",
     "Governments used ideologies, including fascism and communism, to mobilize their states' resources",
     "Totalitarian states repressed basic freedoms and dominated many aspects of daily life",
     "New military technology and new tactics led to increased levels of wartime casualties"], ans=0,
   why="KC-6.2.IV.A.ii states in its own parenthesis that populations were mobilized both in the home countries and the colonies or former colonies, so leaving those populations out contradicts the sentence, while the other four options restate KC-6.2.IV.A.ii and KC-6.1.III.C.ii."),
 dict(q="What is the most accurate summary of the framework's account of the Second World War's conduct for a student revising this topic?",
   choices=[
     "A total war in which governments mobilized populations at home and in the colonies and all of the state's resources, with totalitarian states also repressing freedoms, and with casualties raised by new technology and tactics",
     "A total war in which only totalitarian states mobilized anyone, and in which casualty levels were unchanged from the previous conflict",
     "A limited war in which governments left civilian populations and civilian resources alone",
     "A total war in which mobilization stopped at the borders of each combatant's home country",
     "A war whose conduct the framework declines to describe in any respect"], ans=0,
   why="KC-6.2.IV.A.ii supplies the total war characterisation, the mobilization of populations in the home countries and the colonies or former colonies, the mobilization of all the state's resources through ideologies, and the repression clause attached to totalitarian states, while KC-6.1.III.C.ii supplies the rise in casualties from new technology and new tactics. A summary has to carry all of them."),
]
