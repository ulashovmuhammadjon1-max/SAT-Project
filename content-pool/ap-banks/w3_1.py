# AP WORLD HISTORY: MODERN 3.1 Empires Expand
# CED effective Fall 2024/2026, Unit 3 Land-Based Empires, c. 1450 to c. 1750.
# Unit 3: Learning Objective A -- explain how and why various land-based empires
# developed and expanded from 1450 to 1750. Suggested skill 1.B, explain a
# historical concept, development, or process. Reasoning process: causation.
#
# Historical developments this module keys to, in the framework's own words:
#   KC-4.3.II     Imperial expansion relied on the increased use of gunpowder,
#                 cannons, and armed trade to establish large empires in both
#                 hemispheres.
#   KC-4.3.II.B   Land empires included the Manchu in Central and East Asia; the
#                 Mughal in South and Central Asia; the Ottoman in Southern
#                 Europe, the Middle East, and North Africa; and the Safavids in
#                 the Middle East.
#   KC-4.3.III.i  Political and religious disputes led to rivalries and conflict
#                 between states.
# Illustrative examples printed beside the topic (state rivalries): the
# Safavid-Mughal conflict, and the Songhai Empire's conflict with Morocco.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT. The framework names the four
# land empires and their regions and nothing else about them here: no dynastic
# dates, no battles, no rulers, no confessional identification of the Ottomans
# or the Safavids (topic 3.3's KC-4.1.VI.ii says their rivalry intensified the
# Sunni and Shi'a split without saying which empire stood on which side, so no
# item here or there keys that). Every stimulus is explicitly hypothetical or
# unattributed; no quotation is put in a real person's mouth.
#
# Dates are written "1450 to 1750". Five choices A-E per HISTORY_BRIEF.md.
TOPIC = ("3.1", "Empires Expand", 3)

_T_ARMS = dict(
    headers=["Force described", "Soldiers carrying gunpowder weapons",
             "Soldiers carrying other weapons"],
    rows=[["Force 1", "2,000", "18,000"],
          ["Force 2", "6,000", "14,000"],
          ["Force 3", "9,000", "11,000"],
          ["Force 4", "14,000", "6,000"]])

_T_FOUNDRY = dict(
    headers=["Decade", "Heavy cannon cast", "Light field guns cast"],
    rows=[["First decade", "40", "120"],
          ["Second decade", "75", "260"],
          ["Third decade", "160", "540"],
          ["Fourth decade", "310", "1,100"]])

_T_DISPUTES = dict(
    headers=["Dispute", "What the states quarrelled over"],
    rows=[["Dispute 1", "Which ruling house held the rightful claim to a contested throne"],
          ["Dispute 2", "Which reading of a shared religion the border provinces would follow"],
          ["Dispute 3", "The price a town council set for grain in its own market"]])

QUESTIONS = [
 dict(
  q=("A hypothetical chronicle of a campaign in the period 1450 to 1750 describes a "
     "besieging army that dragged heavy cannon to a fortified city, battered a breach "
     "in the wall over several days, and entered through it. The campaign added the "
     "surrounding province to a large land empire.\n\n"
     "The account best illustrates which development of the period?"),
  choices=[
   "Imperial expansion that relied on the increased use of gunpowder and cannons",
   "The construction of a global trading-post empire by a seaborne power",
   "The spread of scientific learning from the Classical, Islamic, and Asian worlds into Europe",
   "The adoption of restrictive trade policies by a state seeking to limit foreign contact",
   "The recruitment of bureaucratic elites to hold a large population under central control"],
  ans=0,
  why=("KC-4.3.II states that imperial expansion relied on the increased use of gunpowder, "
       "cannons, and armed trade to establish large empires in both hemispheres. A siege won "
       "by artillery and followed by annexation is that process. The rejected options belong "
       "to other statements of the framework: the trading-post empire is KC-4.1.III.A, the "
       "diffusion of learning is KC-4.1.II, restrictive policies are KC-4.3.II.A.i, and "
       "bureaucratic recruitment is KC-4.3.I.C.")),
 dict(
  q=("The framework names the land empires of the period 1450 to 1750 together with the "
     "regions in which each was situated. Which of the following pairings is consistent "
     "with that statement?"),
  choices=[
   "The Manchu in Central and East Asia, and the Mughal in South and Central Asia",
   "The Manchu in South and Central Asia, and the Mughal in Central and East Asia",
   "The Manchu in the Middle East, and the Mughal in North Africa",
   "The Manchu in Southern Europe, and the Mughal in the Middle East",
   "The Manchu in South and Central Asia, and the Mughal in Southern Europe"],
  ans=0,
  why=("KC-4.3.II.B lists the Manchu in Central and East Asia and the Mughal in South and "
       "Central Asia. The rejected pairings exchange the two empires' regions or move one of "
       "them into a region the framework assigns to the Ottomans or the Safavids, which is "
       "the kind of near-miss that reads well and is still wrong.")),
 dict(
  q=("According to the framework's list of the period's land empires, the Ottoman Empire "
     "was situated in which regions?"),
  choices=[
   "Southern Europe, the Middle East, and North Africa",
   "Central and East Asia only",
   "South and Central Asia only",
   "West Africa and the western Sahara",
   "Northern Europe and the Baltic coast"],
  ans=0,
  why=("KC-4.3.II.B places the Ottoman Empire in Southern Europe, the Middle East, and North "
       "Africa. The same statement assigns Central and East Asia to the Manchu and South and "
       "Central Asia to the Mughal, and it names no land empire of this period in West Africa "
       "or in Northern Europe.")),
 dict(
  q=("A student is listing the land empires the framework names for the period 1450 to 1750 "
     "and the region each occupied. Which entry is correct for the Safavids?"),
  choices=[
   "The Safavids were situated in the Middle East",
   "The Safavids were situated in Central and East Asia",
   "The Safavids were situated in North Africa and Southern Europe",
   "The Safavids were situated in South and Central Asia",
   "The Safavids were situated in the Andes and Mesoamerica"],
  ans=0,
  why=("KC-4.3.II.B names the Safavids in the Middle East. The other regions listed belong in "
       "the same statement to the Manchu, the Ottomans and the Mughal respectively, and the "
       "framework names no land empire of the Americas in this list at all.")),
 dict(
  q=("The framework's account of imperial expansion in the period names three things on which "
     "that expansion relied. Which of the following is one of them?"),
  choices=[
   "Armed trade",
   "Free trade agreements between neighbouring states",
   "The abolition of standing armies",
   "A shared currency across the land empires",
   "The renunciation of territorial claims by treaty"],
  ans=0,
  why=("KC-4.3.II names gunpowder, cannons, and armed trade as what imperial expansion relied "
       "on. Armed trade is the framework's own term for commerce backed by force; the other "
       "options describe arrangements the framework nowhere attributes to these empires.")),
 dict(
  q=("The framework states that imperial expansion relied on gunpowder, cannons, and armed "
     "trade to establish large empires. In how much of the world does it locate that process?"),
  choices=[
   "In both hemispheres",
   "In the Eastern Hemisphere only",
   "In the Western Hemisphere only",
   "In Europe alone",
   "In the Indian Ocean basin alone"],
  ans=0,
  why=("KC-4.3.II ends by saying that these means established large empires in both "
       "hemispheres, so the process is not confined to one side of the Atlantic. Restricting "
       "it to Europe, to one hemisphere, or to a single ocean basin narrows the claim the "
       "framework actually makes.")),
 dict(
  q=("Two neighbouring states in the period 1450 to 1750 fall into open war. Their quarrel "
     "began over a contested succession and hardened when each ruler backed a different "
     "reading of a shared faith in the border provinces.\n\n"
     "Which statement of the framework does this sequence illustrate?"),
  choices=[
   "Political and religious disputes led to rivalries and conflict between states",
   "Economic disputes alone accounted for warfare between the land empires",
   "Rulers used monumental architecture to legitimize their rule",
   "Colonial economies in the Americas introduced new labor systems",
   "American food crops improved nutrition across Afro-Eurasia"],
  ans=0,
  why=("KC-4.3.III.i states that political and religious disputes led to rivalries and "
       "conflict between states, and the scenario supplies one dispute of each kind. The "
       "framework does treat economic disputes as a cause of conflict as well, at KC-4.3.III.ii, "
       "so a claim that economics alone accounts for war misstates it.")),
 dict(
  q=("Among the state rivalries the framework offers as illustrative examples for this topic "
     "is a conflict between which pair?"),
  choices=[
   "The Safavid and Mughal empires",
   "The Manchu and Ottoman empires",
   "The Mughal and Ottoman empires",
   "The Safavid and Manchu empires",
   "The Ottoman and Songhai empires"],
  ans=0,
  why=("The illustrative examples printed beside Unit 3: Learning Objective A name the "
       "Safavid-Mughal conflict and the Songhai Empire's conflict with Morocco as state "
       "rivalries of the period, and KC-4.3.III.i is the statement they illustrate. The "
       "rejected pairs combine empires the framework names without pairing them, which is "
       "exactly the sort of plausible-looking claim the source does not support.")),
 dict(
  q=("The framework's second illustrative state rivalry for this topic sets an empire of West "
     "Africa against which power?"),
  choices=[
   "Morocco",
   "The Safavid Empire",
   "The Manchu Empire",
   "The Kingdom of the Kongo",
   "Tokugawa Japan"],
  ans=0,
  why=("The illustrative examples name the Songhai Empire's conflict with Morocco. The other "
       "states listed appear elsewhere in the framework, the Kongo at KC-4.3.II.A.ii and "
       "Tokugawa Japan among the restrictive-policy examples, but none is paired with Songhai "
       "there.")),
 dict(
  q=("A hypothetical merchant's letter from the period reports that a company's ships carried "
     "cannon and armed men alongside their cargo, and that the same ships enforced the "
     "company's terms of trade at ports on the route.\n\n"
     "Which term does the framework use for commerce conducted this way?"),
  choices=[
   "Armed trade",
   "Tax farming",
   "Tribute collection",
   "Indentured servitude",
   "Cultural syncretism"],
  ans=0,
  why=("KC-4.3.II names armed trade, alongside gunpowder and cannons, as a means on which "
       "imperial expansion relied. Tax farming and tribute collection are revenue methods at "
       "KC-4.3.I.D, indentured servitude is a labor system at KC-4.2.II.D, and syncretism is a "
       "religious development at KC-4.1.VI.")),
 dict(
  q=("A historian argues that in the period 1450 to 1750 the growth of large land empires "
     "cannot be explained without reference to military technology. Which piece of evidence "
     "would most directly support that argument as the framework frames it?"),
  choices=[
   "Records of expansion by armies equipped with cannon and gunpowder weapons",
   "Records of the number of manuscripts copied in an imperial library",
   "Records of the tonnage of grain stored in a provincial granary",
   "Records of pilgrims travelling to a shrine in a border province",
   "Records of the wages paid to stonemasons building a palace"],
  ans=0,
  why=("KC-4.3.II ties imperial expansion to the increased use of gunpowder, cannons, and "
       "armed trade, so evidence bearing on that claim has to connect territorial growth with "
       "those weapons. Library, granary, pilgrimage and wage records document other things "
       "about an empire and leave the stated causal claim untested.")),
 dict(
  q=("A hypothetical treasury account from a land empire in this period records rising sums "
     "spent on casting cannon and on powder, in the same years that the empire annexed two "
     "neighbouring provinces.\n\n"
     "Which conclusion does the account most directly support?"),
  choices=[
   "Spending on gunpowder weaponry accompanied the empire's territorial expansion",
   "The empire's expansion was accomplished without any use of force",
   "The empire abandoned land warfare in favour of seaborne trade",
   "The empire's revenue came entirely from overseas colonies",
   "The empire's population declined during the years of annexation"],
  ans=0,
  why=("KC-4.3.II makes gunpowder and cannon central to imperial expansion in this period, and "
       "the account pairs rising outlay on both with new territory. Nothing in a treasury "
       "record speaks to population, to the source of all revenue, or to a shift away from land "
       "warfare, so those readings go beyond the evidence.")),
 dict(
  q=("Which of the following best states why the framework treats the four land empires of "
     "1450 to 1750 together, despite the distance between their territories?"),
  choices=[
   "Each established a large empire by means that included gunpowder weaponry and armed trade",
   "Each was governed from a single capital city on the Mediterranean",
   "Each drew its revenue chiefly from silver mined in the Americas",
   "Each renounced expansion in favour of fixed borders",
   "Each was founded by merchants rather than by rulers"],
  ans=0,
  why=("KC-4.3.II makes the shared reliance on gunpowder, cannons, and armed trade the common "
       "thread, and KC-4.3.II.B lists the four empires and their widely separated regions. The "
       "rejected options assert a shared capital, a shared revenue source, a renunciation of "
       "expansion and a merchant founding, none of which the framework says.")),
 dict(
  q=("A student writes that in the period 1450 to 1750 land empires and maritime empires grew "
     "by entirely unrelated means, since the land empires used force and the maritime empires "
     "used trade. How should this claim be assessed against the framework?"),
  choices=[
   "It is inaccurate, because the framework names armed trade among the means of imperial expansion",
   "It is accurate, because the framework separates force from commerce",
   "It is accurate, because maritime empires are said to have avoided the use of cannon",
   "It is inaccurate, because the framework denies that land empires used gunpowder at all",
   "It is inaccurate, because the framework says trade played no part in expansion"],
  ans=0,
  why=("KC-4.3.II puts gunpowder, cannons, and armed trade in one sentence as the means of "
       "imperial expansion, so force and commerce are not separated there. The three rejected "
       "corrections misreport the same statement in the opposite direction, denying the "
       "gunpowder or denying the trade.")),
 dict(
  q=("The table below reports hypothetical figures for four forces described in a campaign "
     "account of the period 1450 to 1750.\n\n"
     "Which conclusion is best supported by the table alone?"),
  table=_T_ARMS,
  choices=[
   "The share of soldiers carrying gunpowder weapons rises steadily from the first force to the fourth",
   "Every force listed carried gunpowder weapons for a majority of its soldiers",
   "The largest force listed is the one with the fewest gunpowder weapons",
   "No force listed carried any gunpowder weapons at all",
   "The four forces are identical in composition"],
  ans=0,
  why=("KC-4.3.II makes the increased use of gunpowder weapons the process at issue, and the "
       "table's four forces are ordered by exactly that share. The recomputation in the "
       "verifier confirms that only one force reaches a majority, that the four totals are "
       "equal so none is largest, and that every force carries some gunpowder weapons.")),
 dict(
  q=("The table below gives hypothetical output figures for an imperial gun foundry over four "
     "successive decades in the period 1450 to 1750.\n\n"
     "Which statement about the table is accurate?"),
  table=_T_FOUNDRY,
  choices=[
   "Output of both kinds of gun rises in every decade shown",
   "Output of heavy cannon rises while output of light field guns falls",
   "Output of light field guns rises while output of heavy cannon falls",
   "Output of both kinds of gun falls after the second decade",
   "Output of the two kinds of gun is equal in every decade shown"],
  ans=0,
  why=("Recomputed from the table, both columns increase at every step, which is the pattern "
       "KC-4.3.II describes as the increased use of gunpowder and cannons. The two swapped "
       "options assert that one column falls, and the table shows no decrease anywhere.")),
 dict(
  q=("Three disputes between states in the period 1450 to 1750 are described in the table "
     "below.\n\n"
     "Which of them are of the kinds the framework identifies as leading to rivalries and "
     "conflict between states?"),
  table=_T_DISPUTES,
  choices=[
   "Dispute 1 and Dispute 2 only",
   "Dispute 1 and Dispute 3 only",
   "Dispute 2 and Dispute 3 only",
   "Dispute 3 alone",
   "None of the three"],
  ans=0,
  why=("KC-4.3.III.i names political and religious disputes as leading to rivalries and "
       "conflict between states. The contested throne is a political dispute and the quarrel "
       "over a reading of a shared faith is a religious one; a town council's grain price is "
       "neither, and it sets no two states against each other.")),
 dict(
  q=("Which of the following would be the strongest evidence that a rivalry between two states "
     "in this period had a religious dimension as well as a political one?"),
  choices=[
   "Each ruler claimed to defend a different understanding of a faith the two populations shared",
   "Each ruler minted coins of a different weight",
   "Each state used a different calendar for its harvest festivals",
   "Each state recruited its soldiers from a different province",
   "Each state built its fortifications from a different kind of stone"],
  ans=0,
  why=("KC-4.3.III.i pairs political with religious disputes as causes of rivalry and conflict "
       "between states, so the religious dimension has to be a disagreement about belief that "
       "the states themselves take up. Coinage, calendars, recruitment and building materials "
       "differ between neighbouring states without any dispute over faith.")),
 dict(
  q=("An examiner asks for the reason the framework gives for the growth of large land empires "
     "in both hemispheres during this period. Which answer is best supported?"),
  choices=[
   "The increased use of gunpowder, cannons, and armed trade",
   "The invention of the printing press in Europe",
   "The exhaustion of silver mines in the Americas",
   "A worldwide fall in agricultural output",
   "The abandonment of tribute collection by rulers"],
  ans=0,
  why=("KC-4.3.II gives exactly this reason and no other in this topic. The printing press is "
       "not named in the unit, silver appears at KC-4.1.IV as a stimulus to trade rather than "
       "as exhausted, and KC-4.3.I.D says rulers used tribute collection rather than "
       "abandoning it.")),
 dict(
  q=("A hypothetical account written by a captured officer describes an army whose foot "
     "soldiers advanced behind a line of wheeled guns, and whose commanders insisted the guns "
     "reach the field before the infantry did.\n\n"
     "What does the account most usefully show a student of this period?"),
  choices=[
   "That gunpowder weaponry had become central to the way expanding empires fought",
   "That the empire in question had renounced the use of cavalry entirely",
   "That the empire drew all of its soldiers from a single subject population",
   "That the empire had no fortifications of its own to defend",
   "That the empire funded its campaigns without any form of taxation"],
  ans=0,
  why=("KC-4.3.II ties imperial expansion to the increased use of gunpowder and cannons, and an "
       "order of march built around the guns shows that centrality. Nothing in the account "
       "bears on cavalry, recruitment, fortification or finance, and KC-4.3.I.D says rulers did "
       "raise revenue for state power and expansion.")),
 dict(
  q=("The framework locates four named land empires across Asia, the Middle East, Southern "
     "Europe, and North Africa. What does that geographic spread most directly support?"),
  choices=[
   "That the pattern of imperial expansion described was not confined to a single region",
   "That the four empires shared a single ruling dynasty",
   "That the four empires formed a defensive alliance against maritime powers",
   "That the four empires all lay within the Western Hemisphere",
   "That the four empires each governed the same amount of territory"],
  ans=0,
  why=("KC-4.3.II.B lists regions stretching from East Asia to North Africa, and KC-4.3.II says "
       "the same means built large empires in both hemispheres, so the spread shows a pattern "
       "wider than one region. A shared dynasty, an alliance and equal territory are claims the "
       "framework never makes.")),
 dict(
  q=("Which of the following best explains why a historian would call the conflicts among the "
     "land empires of this period rivalries rather than isolated wars?"),
  choices=[
   "The framework describes disputes that produced sustained rivalry and conflict between states",
   "The framework describes conflicts that each ended within a single campaign season",
   "The framework describes states that never fought one another more than once",
   "The framework describes conflicts fought entirely at sea",
   "The framework describes disputes settled by a single treaty binding all four empires"],
  ans=0,
  why=("KC-4.3.III.i says political and religious disputes led to rivalries and conflict "
       "between states, so rivalry is the framework's own word for the resulting relationship. "
       "Short campaigns, single encounters, naval theatres and a general treaty are all "
       "assertions the framework does not make.")),
 dict(
  q=("A textbook chapter is titled with a claim about how land empires grew between 1450 and "
     "1750. Which title would be most consistent with the framework's account?"),
  choices=[
   "Guns, Armed Commerce, and the Building of Large Land Empires",
   "Peaceful Federation: How Land Empires Grew Without Armies",
   "The Sea Alone: Why Land Empires Depended on Naval Power",
   "Isolation and Retreat: Land Empires Turn Inward",
   "One Faith, One Ruler: Religious Uniformity Across the Land Empires"],
  ans=0,
  why=("KC-4.3.II names gunpowder, cannons, and armed trade as what expansion relied on, which "
       "is what the keyed title states. Peaceful federation and retreat contradict that "
       "statement, naval power belongs to the maritime empires of unit 4, and KC-4.3.I.B "
       "records states accommodating religious diversity rather than enforcing uniformity "
       "everywhere.")),
 dict(
  q=("A student claims that because the framework names gunpowder as central to expansion, "
     "commerce played no role in the growth of the land empires. What is the best correction?"),
  choices=[
   "The same statement names armed trade alongside gunpowder and cannons",
   "The same statement denies that any weapons were used",
   "The same statement restricts expansion to the Western Hemisphere",
   "The same statement attributes expansion to religious conversion alone",
   "The same statement says the land empires did not expand at all"],
  ans=0,
  why=("KC-4.3.II lists three means in one sentence, gunpowder, cannons, and armed trade, so "
       "commerce backed by force is part of the framework's own explanation. Each rejected "
       "correction denies something the same sentence asserts.")),
 dict(
  q=("Which pairing of an empire with its region would a reader of the framework recognise as "
     "an error, even though both the empire and the region are named in the same statement?"),
  choices=[
   "The Safavids in Central and East Asia rather than in the Middle East",
   "The Ottomans in Southern Europe, the Middle East, and North Africa",
   "The Mughal in South and Central Asia",
   "The Manchu in Central and East Asia",
   "The Safavids in the Middle East"],
  ans=0,
  why=("KC-4.3.II.B assigns Central and East Asia to the Manchu and the Middle East to the "
       "Safavids, so moving the Safavids eastward is the error. The other four pairings are the "
       "framework's own, which is what makes the mistaken one hard to spot: every word in it "
       "appears in the source, only the combination does not.")),
 dict(
  q=("A hypothetical border official's report from the period notes that caravans entering the "
     "empire now pay duties at a post garrisoned by troops with firearms, and that the post was "
     "built the year the province was annexed.\n\n"
     "Which two developments does the report connect?"),
  choices=[
   "Territorial expansion and the use of armed force to control trade",
   "Maritime exploration and the founding of joint-stock companies",
   "The spread of a syncretic religion and the growth of pilgrimage",
   "The exchange of American and Afro-Eurasian crops",
   "The recruitment of enslaved labor for plantation agriculture"],
  ans=0,
  why=("KC-4.3.II joins expansion to gunpowder, cannons, and armed trade, and the report shows "
       "annexation followed by an armed post levying duties on commerce. The rejected pairs are "
       "developments of unit 4, at KC-4.1.IV.C, KC-4.1.VI, KC-4.1.V and KC-4.2.II.C "
       "respectively.")),
 dict(
  q=("Two empires the framework names for this period share a border and go to war repeatedly. "
     "Which further piece of information would best explain the persistence of the conflict in "
     "the framework's terms?"),
  choices=[
   "That the two states were divided by both a political claim and a religious disagreement",
   "That the two states used different weights and measures in their markets",
   "That the two states lay in different hemispheres",
   "That neither state possessed gunpowder weapons",
   "That both states had abandoned the collection of revenue"],
  ans=0,
  why=("KC-4.3.III.i names political and religious disputes as what led to rivalries and "
       "conflict between states, so a quarrel resting on both is the framework's explanation "
       "for a durable rivalry. Weights, hemispheres, an absence of guns and an absence of "
       "revenue are not offered there as causes of conflict.")),
 dict(
  q=("Why does the framework's statement about gunpowder and cannons matter for a comparison "
     "between empires in the Eastern and the Western Hemispheres?"),
  choices=[
   "Because it says these means established large empires in both hemispheres",
   "Because it says gunpowder was unknown outside Europe",
   "Because it says the Western Hemisphere had no empires in this period",
   "Because it says cannon were used only in siege warfare",
   "Because it says armed trade was practised only by land empires"],
  ans=0,
  why=("KC-4.3.II ends with the phrase about both hemispheres, which is precisely what makes a "
       "cross-hemispheric comparison available to a student. The rejected readings add "
       "restrictions, about who had gunpowder, where empires existed, how cannon were used and "
       "who traded under arms, that the sentence does not carry.")),
 dict(
  q=("An essay is to argue that the expansion of land empires in this period had both a "
     "military and a commercial character. Which pair of evidence types would support both "
     "halves of that argument?"),
  choices=[
   "Records of artillery in campaigns, together with records of duties levied on trade under guard",
   "Records of artillery in campaigns, together with records of monastic library holdings",
   "Records of harvest yields, together with records of court poetry",
   "Records of coin designs, together with records of festival calendars",
   "Records of palace floor plans, together with records of rainfall"],
  ans=0,
  why=("KC-4.3.II names gunpowder, cannons, and armed trade together, so an argument covering "
       "both halves needs evidence of the weaponry and evidence of commerce conducted under "
       "force. Each rejected pair leaves one half of the claim unevidenced or bears on neither "
       "half.")),
 dict(
  q=("A summary sentence about this topic is being drafted for students. Which version stays "
     "within what the framework actually asserts about the period 1450 to 1750?"),
  choices=[
   "Large land empires expanded using gunpowder weaponry and armed trade, and political and religious disputes set them against one another",
   "Large land empires expanded without warfare, and disputes among them were purely economic",
   "Large land empires expanded by sea, and their rivalries were settled by a general treaty",
   "Large land empires refused to trade with their neighbours, and none of them fought a war",
   "Large land empires were confined to the Eastern Hemisphere, and all shared one religion"],
  ans=0,
  why=("The keyed sentence joins KC-4.3.II on the means of expansion to KC-4.3.III.i on "
       "political and religious disputes leading to rivalries and conflict. Each rejected "
       "version contradicts one of those two statements, or contradicts KC-4.3.II's closing "
       "phrase about both hemispheres.")),
]
