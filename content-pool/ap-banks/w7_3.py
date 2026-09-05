# AP WORLD HISTORY: MODERN 7.3 Conducting World War I
# CED effective Fall 2026, Unit 7 Global Conflict, c. 1900 to the present.
# Thematic focus Technology and Innovation (TEC). Unit 7 Learning Objective C:
# explain how governments used a variety of methods to conduct war. Suggested
# skill 3.B, identify the evidence used in a source to support an argument.
#
# THE HISTORICAL DEVELOPMENTS THIS TOPIC RESTS ON, in the framework's own words:
#   KC-6.2.IV.A.i   World War I was the first total war. Governments used a
#                   variety of strategies, including political propaganda, art,
#                   media, and intensified forms of nationalism, to mobilize
#                   populations (both in the home countries and the colonies)
#                   for the purpose of waging war.
#   KC-6.1.III.C.i  New military technology led to increased levels of wartime
#                   casualties.
#
# The parenthesis is not decoration: the framework says populations were
# mobilized in the home countries AND the colonies, and items 4, 8, 16, 18 and
# 27 turn on it. The purpose clause matters too -- the strategies are directed
# at waging war, which is what separates them from cultural policy in general.
#
# BOUNDARY WITH 7.7. The second war's conduct is KC-6.2.IV.A.ii and
# KC-6.1.III.C.ii: those add ideologies used to mobilize resources, the
# repression of basic freedoms in totalitarian states, and the atomic bomb and
# fire-bombing among the new technologies. Nothing from those sentences is keyed
# here, and item 11 is the item that holds the line between the two.
#
# WHAT IS DELIBERATELY NOT ASKED. No item keys to a battle, a date, a weapon's
# name, a casualty total, a poster, a painting or a newspaper: the framework
# names none of them. KC-6.1.III.C.i asserts a direction -- new technology led
# to increased casualties -- and no item asks a student to quantify it, because
# the framework prints no number.
#
# SOURCES. The bank cannot show images, and this is the topic where that
# constraint bites hardest, since the framework's own examples are posters, art
# and media. Every stimulus here is therefore an explicitly unattributed,
# illustrative source DESCRIBED or quoted in prose, or a table of illustrative
# data whose keyed conclusion is recoverable from the table alone. Nothing is
# attributed to a real person, poster or publication.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md.
TOPIC = ("7.3", "Conducting World War I", 7)

_T_FIRE = dict(
    headers=["Front sector (illustrative)",
             "Rounds of rapid-fire artillery per day",
             "Casualties per thousand troops per month"],
    rows=[["Sector 1", "400", "22"],
          ["Sector 2", "1,900", "61"],
          ["Sector 3", "1,100", "44"]])

_T_RECRUIT = dict(
    headers=["Power (illustrative)",
             "Troops raised in the home country (thousands)",
             "Troops raised in its colonies (thousands)"],
    rows=[["Power A", "4,200", "610"],
          ["Power B", "3,800", "1,150"],
          ["Power C", "2,500", "90"]])

QUESTIONS = [
 dict(q="An unattributed wartime recruiting notice, illustrative of the period, tells readers that a woman filling shells in a factory and a farmer raising grain for the army are 'as much in the fight as the soldier at the front.' The notice is best used as evidence of",
   choices=[
     "the mobilization of a whole population for the purpose of waging war",
     "the recruitment of professional soldiers from a small volunteer class",
     "a government withdrawing from the direction of economic life",
     "an alliance obligation binding one state to defend another",
     "the transfer of a colony to another power by treaty"], ans=0,
   why="KC-6.2.IV.A.i states that World War I was the first total war and that governments used a variety of strategies to mobilize populations for the purpose of waging war. A notice telling factory and farm workers that their work is part of the fighting is that mobilization addressed to civilians."),
 dict(q="What does the framework mean in describing the First World War as the first total war?",
   choices=[
     "Governments mobilized populations at home and in the colonies for the purpose of waging war",
     "Every state in the world declared war on every other state",
     "The fighting was carried on without any use of new military technology",
     "Governments left the conduct of the war entirely to their professional armies",
     "The war was fought only in the colonies and not in the home countries"], ans=0,
   why="KC-6.2.IV.A.i pairs the phrase 'the first total war' directly with governments mobilizing populations, both in the home countries and the colonies, for the purpose of waging war. The scale referred to is the scale of mobilization within belligerent states, not the number of states involved."),
 dict(q="Which list matches the strategies of mobilization that the framework names?",
   choices=[
     "Political propaganda, art, media, and intensified forms of nationalism",
     "Five-year plans, collective farms, and state ownership of industry",
     "Tariffs, currency devaluation, and public works programmes",
     "Alliance treaties, arms limitation agreements, and neutrality pacts",
     "Land redistribution, literacy campaigns, and religious instruction"], ans=0,
   why="KC-6.2.IV.A.i lists political propaganda, art, media, and intensified forms of nationalism as the strategies governments used to mobilize populations for war. The other lists belong to KC-6.3.I.A.i on Soviet economic control or describe policies the framework does not name here."),
 dict(q="Whose populations does the framework say governments mobilized for the war effort?",
   choices=[
     "Populations in the colonies were mobilized as well as those in the home countries",
     "Populations in the home countries were mobilized while the colonies were left untouched",
     "Populations in the colonies were mobilized while the home countries were left untouched",
     "Only the populations of states that had no colonies were mobilized",
     "Only professional soldiers already under arms were mobilized"], ans=0,
   why="KC-6.2.IV.A.i states that governments mobilized populations both in the home countries and the colonies. The parenthesis covers both at once, so an answer that exempts either side of it contradicts the sentence."),
 dict(q="What does the framework state about the relationship between new military technology and the human cost of the war?",
   choices=[
     "New military technology led to increased levels of wartime casualties",
     "Increased levels of wartime casualties led governments to develop new military technology",
     "New military technology reduced the level of wartime casualties",
     "Casualty levels were unaffected by changes in military technology",
     "New military technology was introduced only after the fighting had ended"], ans=0,
   why="KC-6.1.III.C.i states that new military technology led to increased levels of wartime casualties. The direction of that sentence is the substance of the claim, and reversing it makes the casualties the cause rather than the effect."),
 dict(q="An unattributed wartime pamphlet argues that victory depends on the entire nation rather than on the army alone. To support this, it states that most of the shells fired in the previous month were made by people who had never worked in a factory before the war. Within the pamphlet's argument, that statement functions as",
   choices=[
     "evidence for the claim that the whole population is engaged in waging the war",
     "the pamphlet's main claim, which the rest of the text then explains",
     "a concession that the army alone determines the outcome of the war",
     "a description of the enemy's industrial capacity rather than the writer's own",
     "an instruction to the reader about how to enlist in the armed forces"], ans=0,
   why="Suggested skill 3.B asks students to identify the evidence a source uses to support its argument. The claim is that victory depends on the whole nation; the statement about newly recruited factory workers is offered in support of it, which is the relation KC-6.2.IV.A.i describes as total war."),
 dict(q="The table below reports illustrative artillery use and casualty rates in three sectors of a front. Which conclusion is best supported by the data as given?",
   table=_T_FIRE,
   choices=[
     "The sectors with heavier use of rapid-fire artillery record the higher casualty rates",
     "The sectors with heavier use of rapid-fire artillery record the lower casualty rates",
     "Casualty rates are identical across the three sectors",
     "The sector firing the fewest rounds records the highest casualty rate",
     "No sector records any casualties at all"], ans=0,
   why="Read from the table alone: ranking the sectors by rounds fired and by casualty rate produces the same order. That is the pattern KC-6.1.III.C.i asserts, that new military technology led to increased levels of wartime casualties."),
 dict(q="The table below reports illustrative recruitment totals for three imperial powers. Which conclusion is best supported?",
   table=_T_RECRUIT,
   choices=[
     "Each power raised troops in its colonies as well as at home, and Power B raised the most colonial troops",
     "Each power raised troops in its colonies as well as at home, and Power A raised the most colonial troops",
     "Only one of the three powers raised any troops in its colonies",
     "Each power raised more troops in its colonies than in its home country",
     "The power with the largest home-country army also raised the most colonial troops"], ans=0,
   why="Read from the table alone: no colonial total is zero, one power's colonial total is the largest, and that power is not the one with the largest home-country total. This is the mobilization in both the home countries and the colonies that KC-6.2.IV.A.i describes."),
 dict(q="According to the framework, what was the purpose of the propaganda, art, and media that governments produced during the war?",
   choices=[
     "To mobilize populations for the purpose of waging war",
     "To record the war accurately for later historians",
     "To encourage private trade with neutral states",
     "To settle the territorial disputes that had caused the war",
     "To reduce the level of casualties at the front"], ans=0,
   why="KC-6.2.IV.A.i states that governments used these strategies to mobilize populations for the purpose of waging war. The purpose clause is part of the sentence, and none of the other four purposes appears in it."),
 dict(q="A government commissions paintings of soldiers at the front and pays for their display in every large town. Under the framework's account, this is best described as",
   choices=[
     "a use of art among the strategies of wartime mobilization",
     "a cultural policy unrelated to the conduct of the war",
     "a form of military technology that raised casualty levels",
     "an economic measure intended to relieve unemployment",
     "an alliance obligation undertaken towards another state"], ans=0,
   why="KC-6.2.IV.A.i names art explicitly among the strategies, alongside political propaganda, media, and intensified forms of nationalism, that governments used to mobilize populations for the purpose of waging war."),
 dict(q="Which statement about total war does the framework make specifically about the First World War rather than the Second?",
   choices=[
     "It was the first total war",
     "Governments used ideologies including fascism and communism to mobilize all of the state's resources",
     "Totalitarian states repressed basic freedoms and dominated many aspects of daily life",
     "New tactics including the atomic bomb and fire-bombing raised casualty levels",
     "Governments mobilized the populations of former colonies as well as colonies"], ans=0,
   why="KC-6.2.IV.A.i opens by calling World War I the first total war. The other four statements come from KC-6.2.IV.A.ii and KC-6.1.III.C.ii, which the framework attaches to the conduct of the Second World War in topic 7.7."),
 dict(q="Which of the following does the framework NOT name among the strategies used to mobilize populations for the First World War?",
   choices=[
     "State control of the national economy through five-year plans",
     "Political propaganda",
     "Art",
     "Media",
     "Intensified forms of nationalism"], ans=0,
   why="KC-6.2.IV.A.i names political propaganda, art, media, and intensified forms of nationalism. Control of the national economy through the Five Year Plans is KC-6.3.I.A.i, which the framework attaches to the Soviet Union in the interwar period rather than to wartime mobilization."),
 dict(q="A student writes that soldiers died in large numbers, and that this is why governments developed machine guns and heavy artillery. Using the framework, the best correction is that",
   choices=[
     "the framework has the new technology coming first and the higher casualties following from it",
     "the framework has the higher casualties coming first and the new technology following from them",
     "the framework describes the two as unconnected",
     "the framework denies that casualties rose during the war",
     "the framework attributes rising casualties to propaganda rather than to technology"], ans=0,
   why="KC-6.1.III.C.i states that new military technology led to increased levels of wartime casualties, so the technology is the cause and the casualties the effect. The student has reversed the order the sentence gives."),
 dict(q="Why does the mobilization the framework describes require action by governments rather than by armies alone?",
   choices=[
     "Because the populations to be mobilized were civilian and lay outside the army's own organisation",
     "Because armies had been abolished in the belligerent states",
     "Because the framework describes the war as fought without soldiers",
     "Because propaganda was illegal for any body other than an army to produce",
     "Because the colonies were governed directly by their own armies"], ans=0,
   why="KC-6.2.IV.A.i has governments using propaganda, art, media, and intensified nationalism to mobilize populations in the home countries and the colonies. Those populations are not under military command, which is why the framework assigns the work to governments."),
 dict(q="A wartime poster survives from a belligerent state. What can it most reliably be used as evidence for?",
   choices=[
     "What the government wanted the population to do, rather than whether the population complied",
     "The exact number of people who enlisted in response to it",
     "The private opinions of the artist who designed it",
     "The military situation at the front on the day it appeared",
     "The terms of the settlement that ended the war"], ans=0,
   why="KC-6.2.IV.A.i identifies propaganda and art as government strategies for mobilizing populations, so such a source documents the strategy directly. Whether the strategy worked is a separate question the source itself cannot settle, which is the limit a student should state."),
 dict(q="A historian claims that imperial powers fought the war using their home populations only. Which evidence would most directly refute that claim?",
   choices=[
     "Records of recruitment and requisitioning carried out in colonial territories",
     "Records of the tonnage of shipping built in the home countries",
     "Records of the paintings commissioned by the war ministry",
     "Records of the alliances signed before the fighting began",
     "Records of the casualty rate in a single front sector"], ans=0,
   why="KC-6.2.IV.A.i states that populations were mobilized both in the home countries and the colonies. Records of colonial recruitment and requisitioning bear on the colonial half of that statement, which is precisely what the claim denies."),
 dict(q="In this topic, intensified nationalism appears in what role?",
   choices=[
     "As a method governments used to mobilize populations for war",
     "As a cause that helped bring the war about in the first place",
     "As a consequence of the peace settlement that ended the war",
     "As a form of military technology that raised casualties",
     "As an economic policy adopted during the depression"], ans=0,
   why="KC-6.2.IV.A.i lists intensified forms of nationalism among the strategies governments used to mobilize populations for the purpose of waging war. KC-6.2.IV.B.i places intense nationalism among the war's causes, which is topic 7.2; the same phenomenon appears in the framework in two different roles."),
 dict(q="A colonial administration issues an order requiring villages to supply a fixed quota of labourers and grain to the war effort. This order is best used as evidence for which part of the framework's account?",
   choices=[
     "That mobilization extended to the colonies and not only to the home countries",
     "That mobilization was confined to the home countries",
     "That new military technology raised casualty levels",
     "That the war's causes included competition for resources",
     "That the peace settlement transferred colonies between powers"], ans=0,
   why="KC-6.2.IV.A.i says populations were mobilized both in the home countries and the colonies. An order compelling colonial villages to supply labour and food is that mobilization in a colonial setting."),
 dict(q="A government department buys space in every newspaper to publish accounts of the war written to its own instructions. Under the framework's list, this is an example of",
   choices=[
     "the use of media as a strategy of mobilization",
     "an economic policy of the kind adopted after the depression",
     "a military technology that increased casualties",
     "a diplomatic strategy for securing new allies",
     "the transfer of colonial territory by treaty"], ans=0,
   why="KC-6.2.IV.A.i names media among the strategies, together with political propaganda, art, and intensified forms of nationalism, that governments used to mobilize populations for the purpose of waging war."),
 dict(q="Which finding would most strengthen the framework's claim about technology and casualties?",
   choices=[
     "Casualty totals that rise sharply in the months after a new weapon is introduced along a front",
     "Casualty totals that are the same before and after a new weapon is introduced",
     "Records showing that the new weapon was never issued to any unit",
     "Records showing that both sides used the same weapons throughout the war",
     "Records showing that the war lasted longer than either side expected"], ans=0,
   why="KC-6.1.III.C.i asserts that new military technology led to increased levels of wartime casualties. A rise in casualties following the introduction of a weapon is evidence for that direction; totals that do not move, or a weapon never used, leave the claim unsupported."),
 dict(q="Which finding would most weaken that same claim?",
   choices=[
     "Casualty rates that fall on the sectors where the newest weapons are concentrated",
     "Casualty rates that rise on the sectors where the newest weapons are concentrated",
     "Evidence that governments produced propaganda encouraging enlistment",
     "Evidence that colonial troops served alongside home-country troops",
     "Evidence that the war was described at the time as a total war"], ans=0,
   why="KC-6.1.III.C.i ties higher casualties to new military technology, so casualties falling exactly where that technology is concentrated is the observation the claim cannot absorb. Propaganda, colonial service and the phrase total war bear on KC-6.2.IV.A.i instead and leave the technology claim untouched."),
 dict(q="A state directs its factories to war production, rations food to civilians, and conscripts labour for the transport of supplies. These measures together are best described as",
   choices=[
     "the conduct of a total war, in which the whole society is turned to the war effort",
     "a peacetime industrial policy unrelated to any war",
     "an alliance system linking several states in a common defence",
     "a settlement imposed on a defeated power after a war",
     "a programme of colonial expansion in search of resources"], ans=0,
   why="KC-6.2.IV.A.i calls World War I the first total war and describes governments mobilizing populations for the purpose of waging war. Direction of industry, rationing and conscripted labour are that mobilization reaching civilian life."),
 dict(q="An unattributed government instruction to newspaper editors, illustrative of the period, forbids the printing of casualty totals. The instruction is best understood as",
   choices=[
     "an attempt to manage what the population believed about the war while mobilization continued",
     "evidence that the government had no interest in what its population believed",
     "a military technology of the kind that raised casualty levels",
     "an economic measure intended to reduce the cost of newsprint",
     "a step towards ending the war by negotiation"], ans=0,
   why="KC-6.2.IV.A.i names media and political propaganda among the strategies governments used to mobilize populations for the purpose of waging war. Controlling what appears in the press is the management of that channel, which is why the framework treats media as a government strategy rather than as a neutral record."),
 dict(q="An unattributed wartime speech argues that the enemy must be defeated because the nation's very existence is at stake, and offers as support a list of towns damaged in enemy raids. Which part of the speech is the evidence?",
   choices=[
     "The list of damaged towns, offered in support of the claim about national survival",
     "The claim about national survival, offered in support of the list of damaged towns",
     "The speech contains a claim but no evidence of any kind",
     "The speech contains evidence but makes no claim",
     "Both the claim and the list are conclusions rather than support"], ans=0,
   why="Suggested skill 3.B asks students to identify the evidence a source uses to support its argument. The argument is that survival is at stake and the damaged towns are what is offered in its support, which is the direction the anchor fixes; the speech is also an instance of the intensified nationalism KC-6.2.IV.A.i names."),
 dict(q="A student writes that wars before 1900 had already been total wars in the framework's sense. What is the difficulty with that statement?",
   choices=[
     "The framework identifies the First World War as the first total war",
     "The framework identifies the Second World War as the first total war",
     "The framework says that no war has ever been a total war",
     "The framework applies the term only to wars fought in the colonies",
     "The framework uses the term only for wars fought after 1945"], ans=0,
   why="KC-6.2.IV.A.i states plainly that World War I was the first total war, and KC-6.2.IV.A.ii separately states that World War II was a total war. A claim that earlier wars already met the description contradicts the first of those sentences."),
 dict(q="Which of the following best distinguishes propaganda, as the framework uses the term here, from ordinary reporting of the war?",
   choices=[
     "It is produced by a government as a strategy for mobilizing its population",
     "It is produced only after a war has ended",
     "It is produced by soldiers rather than by civilians",
     "It concerns the economy rather than the fighting",
     "It is distributed only in the colonies and never at home"], ans=0,
   why="KC-6.2.IV.A.i attributes political propaganda to governments and gives its purpose as mobilizing populations for waging war. The government's authorship and that purpose are what the framework's own wording supplies."),
 dict(q="Why does the framework's parenthesis about the colonies matter for understanding the war's scale?",
   choices=[
     "Because it extends the war effort to populations far from where most of the fighting took place",
     "Because it shows that the colonies were left out of the war effort entirely",
     "Because it shows that the fighting took place only in colonial territory",
     "Because it shows that colonies were transferred between powers during the war",
     "Because it shows that colonial populations were exempt from taxation"], ans=0,
   why="KC-6.2.IV.A.i says populations were mobilized both in the home countries and the colonies. Including colonial populations places the demands of the war on societies distant from the fronts, which is part of what makes the mobilization total."),
 dict(q="A researcher wants to study how one belligerent government tried to sustain popular support for the war. Which body of material is most directly relevant?",
   choices=[
     "The output of the government's own propaganda and information offices",
     "The technical specifications of artillery produced during the war",
     "The alliance treaties signed before the war began",
     "The tonnage of grain harvested in neutral states",
     "The border changes recorded in the peace settlement"], ans=0,
   why="KC-6.2.IV.A.i names political propaganda, art, and media among the strategies governments used to mobilize populations for the purpose of waging war, so material produced by the offices responsible for them documents the effort directly."),
 dict(q="Which pairing correctly matches one of the framework's statements about this topic with what it asserts?",
   choices=[
     "New military technology, asserted to have raised the level of wartime casualties",
     "New military technology, asserted to have shortened the war and reduced casualties",
     "Political propaganda, asserted to have been produced by soldiers rather than governments",
     "Intensified nationalism, asserted to have been discouraged by governments during the war",
     "Colonial populations, asserted to have been excluded from the war effort"], ans=0,
   why="KC-6.1.III.C.i states that new military technology led to increased levels of wartime casualties, and KC-6.2.IV.A.i attributes propaganda and intensified nationalism to governments and includes colonial populations in the mobilization. Only the first pairing states what the framework states."),
 dict(q="Which research question follows most directly from this topic's learning objective?",
   choices=[
     "By what methods did governments conduct the war and mobilize their populations",
     "Which general made the best tactical decisions during the war",
     "How many paintings were produced in Europe during the war",
     "Which crops were most profitable for farmers during the war",
     "How did the climate of the front sectors change during the war"], ans=0,
   why="Unit 7 Learning Objective C asks students to explain how governments used a variety of methods to conduct war, and KC-6.2.IV.A.i supplies those methods. A question about governments' methods restates the objective; the others ask about matters it does not name."),
]
