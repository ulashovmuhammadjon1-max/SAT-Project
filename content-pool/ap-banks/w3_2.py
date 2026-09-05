# AP WORLD HISTORY: MODERN 3.2 Empires: Administration
# CED effective Fall 2024/2026, Unit 3 Land-Based Empires, c. 1450 to c. 1750.
# Unit 3: Learning Objective B -- explain how rulers used a variety of methods to
# legitimize and consolidate their power in land-based empires from 1450 to 1750.
# Suggested skill 4.A, identify and describe a historical context for a specific
# historical development or process. Reasoning process: comparison.
#
# Historical developments this module keys to, in the framework's own words:
#   KC-4.3.I.C  Recruitment and use of bureaucratic elites, as well as the
#               development of military professionals, became more common among
#               rulers who wanted to maintain centralized control over their
#               populations and resources.
#   KC-4.3.I.A  Rulers continued to use religious ideas, art, and monumental
#               architecture to legitimize their rule.
#   KC-4.3.I.D  Rulers used tribute collection, tax farming, and innovative
#               tax-collection systems to generate revenue in order to forward
#               state power and expansion.
#
# The illustrative examples are printed beside the topic under four headings,
# and the HEADING an example sits under is itself framework content, so several
# items turn on it:
#   Bureaucratic elites or military professionals: Ottoman devshirme; salaried
#     samurai.
#   Religious ideas: Mexica practice of human sacrifice; European notions of
#     divine right; Songhai promotion of Islam.
#   Art and monumental architecture: Qing imperial portraits; Incan sun temple
#     of Cuzco; Mughal mausolea and mosques; European palaces, such as Versailles.
#   Tax-collection systems: Mughal zamindar tax collection; Ottoman tax farming;
#     Mexica tribute lists; Ming practice of collecting taxes in hard currency.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT ASSERT. The framework names these
# practices and does not describe how any of them worked in detail -- it does
# not say how the devshirme recruited, what a zamindar's share was, or when
# Versailles was built -- so no item keys any of that. Every stimulus is
# explicitly hypothetical or unattributed; no quotation is attributed to a real
# person or document.
#
# Dates are written "1450 to 1750". Five choices A-E per HISTORY_BRIEF.md.
TOPIC = ("3.2", "Empires: Administration", 3)

_T_REVENUE = dict(
    headers=["Province", "Revenue raised by tax farmers", "Revenue raised by salaried officials"],
    rows=[["Province 1", "9,000", "1,000"],
          ["Province 2", "7,500", "2,500"],
          ["Province 3", "4,000", "6,000"],
          ["Province 4", "1,500", "8,500"]])

_T_METHODS = dict(
    headers=["Measure recorded in an imperial register", "What the register says was done"],
    rows=[["Measure 1", "A corps of salaried officials was recruited and posted to the provinces"],
          ["Measure 2", "A great mosque and a tomb for the dynasty were raised in the capital"],
          ["Measure 3", "The right to collect a district's taxes was sold to a contractor"]])

_T_HARDCASH = dict(
    headers=["Decade", "Share of taxes received in grain and cloth",
             "Share of taxes received in hard currency"],
    rows=[["First decade", "80", "20"],
          ["Second decade", "65", "35"],
          ["Third decade", "45", "55"],
          ["Fourth decade", "25", "75"]])

QUESTIONS = [
 dict(
  q=("A hypothetical imperial decree of the period 1450 to 1750 orders that district "
     "governorships be filled by men trained at the ruler's own school, paid from the "
     "treasury, and moved from post to post every few years.\n\n"
     "Which development of the period does the decree best illustrate?"),
  choices=[
   "The recruitment and use of bureaucratic elites to maintain centralized control",
   "The use of monumental architecture to legitimize a ruler's authority",
   "The sale of the right to collect taxes to private contractors",
   "The adoption of restrictive trade policies against foreign merchants",
   "The introduction of chattel slavery into a colonial plantation economy"],
  ans=0,
  why=("KC-4.3.I.C states that recruitment and use of bureaucratic elites, as well as the "
       "development of military professionals, became more common among rulers who wanted to "
       "maintain centralized control over their populations and resources. Salaried officials "
       "posted and rotated by the ruler are that practice. Architecture is KC-4.3.I.A, tax "
       "farming is KC-4.3.I.D, restrictive trade is KC-4.3.II.A.i, and chattel slavery is "
       "KC-4.2.II.D.")),
 dict(
  q=("According to the framework, what did rulers of land-based empires want to achieve by "
     "recruiting bureaucratic elites and developing military professionals?"),
  choices=[
   "To maintain centralized control over their populations and resources",
   "To transfer the administration of the empire to merchant companies",
   "To reduce the size of the state's revenue",
   "To replace religious justifications of rule with elected assemblies",
   "To end the collection of tribute from subject peoples"],
  ans=0,
  why=("KC-4.3.I.C gives the purpose in its own words: rulers who wanted to maintain "
       "centralized control over their populations and resources. Handing administration to "
       "companies, shrinking revenue, elected assemblies and abolishing tribute are all "
       "contrary to what the framework says these rulers did.")),
 dict(
  q=("Which three things does the framework say rulers continued to use in order to legitimize "
     "their rule in this period?"),
  choices=[
   "Religious ideas, art, and monumental architecture",
   "Standing navies, chartered companies, and overseas colonies",
   "Printed newspapers, public elections, and written constitutions",
   "Coin debasement, price controls, and grain rationing",
   "Foreign alliances, dynastic marriages, and border treaties"],
  ans=0,
  why=("KC-4.3.I.A states that rulers continued to use religious ideas, art, and monumental "
       "architecture to legitimize their rule. None of the rejected sets appears in that "
       "statement, and several of them describe developments the framework places in later "
       "units altogether.")),
 dict(
  q=("Which three revenue methods does the framework attribute to rulers of land-based empires "
     "in the period 1450 to 1750?"),
  choices=[
   "Tribute collection, tax farming, and innovative tax-collection systems",
   "Customs unions, income taxes, and public borrowing from banks",
   "Confiscation of church lands, lotteries, and forced loans from guilds",
   "Sale of colonial offices, tolls on canals, and monopolies on salt",
   "Poll taxes on merchants, tithes to monasteries, and export bounties"],
  ans=0,
  why=("KC-4.3.I.D names tribute collection, tax farming, and innovative tax-collection "
       "systems, and says rulers used them to generate revenue in order to forward state power "
       "and expansion. The rejected lists name fiscal devices the framework does not "
       "attribute to these rulers here.")),
 dict(
  q=("The framework says rulers used tribute collection, tax farming, and innovative "
     "tax-collection systems. For what stated purpose?"),
  choices=[
   "To generate revenue in order to forward state power and expansion",
   "To equalize wealth among the empire's subject populations",
   "To replace agriculture with manufacturing as the basis of the economy",
   "To fund religious institutions independent of the ruler",
   "To reduce the burden of taxation on the provinces"],
  ans=0,
  why=("KC-4.3.I.D states the purpose directly: to generate revenue in order to forward state "
       "power and expansion. Redistribution, industrial policy, independent religious funding "
       "and tax relief are not the ends the framework attaches to these methods.")),
 dict(
  q=("Among the illustrative examples the framework prints for this topic, the Ottoman "
     "devshirme and the salaried samurai appear together under which heading?"),
  choices=[
   "Bureaucratic elites or military professionals",
   "Religious ideas",
   "Art and monumental architecture",
   "Tax-collection systems",
   "Restrictive or isolationist trade policies"],
  ans=0,
  why=("The illustrative examples beside Unit 3: Learning Objective B group the devshirme and "
       "the salaried samurai as bureaucratic elites or military professionals, the category "
       "KC-4.3.I.C describes. Restrictive trade policies belong to a different topic entirely, "
       "at KC-4.3.II.A.i.")),
 dict(
  q=("The framework's illustrative examples list the Mexica practice of human sacrifice, "
     "European notions of divine right, and the Songhai promotion of Islam together. What do "
     "these three have in common in the framework's account?"),
  choices=[
   "Each is an example of a religious idea used to legitimize rule",
   "Each is an example of an innovative tax-collection system",
   "Each is an example of the recruitment of military professionals",
   "Each is an example of a restrictive trade policy",
   "Each is an example of resistance to state expansion"],
  ans=0,
  why=("Those three examples are printed under the heading of religious ideas, and KC-4.3.I.A "
       "says rulers continued to use religious ideas, art, and monumental architecture to "
       "legitimize their rule. Tax systems are KC-4.3.I.D, military professionals KC-4.3.I.C, "
       "and resistance is KC-4.3.III.iii in unit 4.")),
 dict(
  q=("Qing imperial portraits, the Incan sun temple of Cuzco, Mughal mausolea and mosques, and "
     "European palaces such as Versailles are printed together as illustrative examples. Which "
     "practice do they illustrate?"),
  choices=[
   "The use of art and monumental architecture to legitimize rule",
   "The use of tax farming to raise revenue quickly",
   "The recruitment of bureaucratic elites from subject populations",
   "The exchange of plants and animals between hemispheres",
   "The financing of exploration by joint-stock companies"],
  ans=0,
  why=("These four sit under the heading of art and monumental architecture, and KC-4.3.I.A "
       "names art and monumental architecture, alongside religious ideas, as means by which "
       "rulers legitimized their rule. The rejected options belong to KC-4.3.I.D, KC-4.3.I.C, "
       "KC-4.1.V and KC-4.1.IV.C.")),
 dict(
  q=("Mughal zamindar tax collection, Ottoman tax farming, Mexica tribute lists, and the Ming "
     "practice of collecting taxes in hard currency are grouped together in the framework's "
     "illustrative examples. What do they illustrate?"),
  choices=[
   "The methods rulers used to generate revenue for state power and expansion",
   "The methods rulers used to legitimize their rule through religion",
   "The ways subject populations organized resistance to the state",
   "The ways empires restricted the activity of foreign merchants",
   "The ways enslaved persons were incorporated into households"],
  ans=0,
  why=("Those four are printed under tax-collection systems, and KC-4.3.I.D says rulers used "
       "tribute collection, tax farming, and innovative tax-collection systems to generate "
       "revenue in order to forward state power and expansion. Legitimation is KC-4.3.I.A, "
       "resistance KC-4.3.III.iii, restriction KC-4.3.II.A.i, and household enslavement "
       "KC-4.2.II.B.")),
 dict(
  q=("A hypothetical court record from the period notes that a ruler's officials paid a fixed "
     "sum into the treasury in advance and then recovered what they could from a district's "
     "taxpayers, keeping the difference.\n\n"
     "Which of the framework's revenue methods does the record describe?"),
  choices=[
   "Tax farming",
   "Tribute collection from a defeated neighbour",
   "A monopoly company chartered for overseas trade",
   "The recruitment of a salaried bureaucratic elite",
   "The building of monumental architecture"],
  ans=0,
  why=("KC-4.3.I.D names tax farming among the revenue methods of these rulers, and the "
       "illustrative examples print Ottoman tax farming as an instance. A contractor advancing "
       "a sum and recovering it locally is that arrangement rather than tribute, a chartered "
       "company at KC-4.1.IV.C, a salaried service at KC-4.3.I.C, or a building programme.")),
 dict(
  q=("A ruler in the period 1450 to 1750 commissions a great mosque, a dynastic tomb, and a "
     "series of formal portraits, and has them displayed where subjects and visiting envoys "
     "will see them.\n\n"
     "What does the framework say such a programme was meant to do?"),
  choices=[
   "Legitimize the ruler's rule",
   "Raise revenue for the treasury",
   "Recruit officials from among the ruler's subjects",
   "Restrict the movement of foreign merchants",
   "Increase the yield of the empire's farmland"],
  ans=0,
  why=("KC-4.3.I.A states that rulers continued to use religious ideas, art, and monumental "
       "architecture to legitimize their rule, which is the purpose the framework attaches to "
       "exactly this kind of programme. Revenue is KC-4.3.I.D and recruitment is KC-4.3.I.C, "
       "and neither is what a tomb or a portrait accomplishes.")),
 dict(
  q=("Why does the framework describe the recruitment of bureaucratic elites as becoming more "
     "common among rulers in this period rather than as an entirely new invention?"),
  choices=[
   "Because it states that the practice became more common, not that it began",
   "Because it states that no ruler before 1450 had any officials",
   "Because it states that bureaucratic elites replaced rulers altogether",
   "Because it states that officials were recruited only from foreign states",
   "Because it states that the practice ended before 1750"],
  ans=0,
  why=("KC-4.3.I.C says recruitment and use of bureaucratic elites, as well as the development "
       "of military professionals, became more common, which is a claim about frequency rather "
       "than about origin. The rejected readings add beginnings, endings and restrictions the "
       "sentence does not contain.")),
 dict(
  q=("The framework says rulers continued to use religious ideas to legitimize their rule. What "
     "does the word continued indicate about the practice in the period 1450 to 1750?"),
  choices=[
   "That it carried on from earlier periods rather than beginning in this one",
   "That it was abandoned in favour of secular justifications",
   "That it was confined to one empire in the period",
   "That it was practised only by rulers without armies",
   "That it applied only to newly conquered provinces"],
  ans=0,
  why=("KC-4.3.I.A uses the word continued, which places the practice in continuity with what "
       "came before rather than treating it as an innovation of the period. Nothing in the "
       "sentence confines the practice to one empire, to unarmed rulers, or to new "
       "territory.")),
 dict(
  q=("The table below reports hypothetical revenue figures from four provinces of one land "
     "empire in the period 1450 to 1750.\n\n"
     "Which conclusion is best supported by the table alone?"),
  table=_T_REVENUE,
  choices=[
   "The share of revenue raised by tax farmers falls steadily from the first province to the fourth",
   "Tax farmers raised more revenue than salaried officials in every province listed",
   "Salaried officials raised more revenue than tax farmers in every province listed",
   "The four provinces raised identical amounts by each method",
   "No province listed used tax farmers at all"],
  ans=0,
  why=("KC-4.3.I.D names tax farming as one revenue method among others, so a mixed picture "
       "across provinces is what the framework leads a student to expect. The verifier "
       "recomputes that the tax-farming share falls at every step, that each method leads in "
       "two provinces, and that every province used both.")),
 dict(
  q=("Three measures recorded in a hypothetical imperial register are described in the table "
     "below.\n\n"
     "Which measure is an example of the revenue methods the framework describes?"),
  table=_T_METHODS,
  choices=[
   "Measure 3 only",
   "Measure 1 only",
   "Measure 2 only",
   "Measure 1 together with Measure 2, but not Measure 3",
   "All three measures"],
  ans=0,
  why=("KC-4.3.I.D names tax farming among the revenue methods, and selling the right to "
       "collect a district's taxes to a contractor is that practice. The recruitment of "
       "salaried officials belongs to KC-4.3.I.C and the mosque and tomb to KC-4.3.I.A, so "
       "neither is a revenue measure.")),
 dict(
  q=("Using the same register, which measure best illustrates the framework's statement about "
     "how rulers legitimized their rule?"),
  table=_T_METHODS,
  choices=[
   "Measure 2 only",
   "Measure 1 only",
   "Measure 3 only",
   "Measure 1 together with Measure 3, but not Measure 2",
   "None of the three"],
  ans=0,
  why=("KC-4.3.I.A names religious ideas, art, and monumental architecture as the means of "
       "legitimation, and a great mosque and a dynastic tomb are monumental architecture with a "
       "religious character. Recruiting officials is KC-4.3.I.C and selling a tax right is "
       "KC-4.3.I.D.")),
 dict(
  q=("The table below gives the hypothetical composition of one empire's tax receipts across "
     "four decades in the period 1450 to 1750.\n\n"
     "Which statement about the table is accurate?"),
  table=_T_HARDCASH,
  choices=[
   "The share received in hard currency rises in every decade shown",
   "The share received in hard currency falls in every decade shown",
   "The share received in grain and cloth rises in every decade shown",
   "The two shares are equal in every decade shown",
   "Neither share changes across the four decades"],
  ans=0,
  why=("Recomputed from the table, the hard-currency share rises at every step while the "
       "payment-in-kind share falls, and the two are never equal. KC-4.3.I.D names innovative "
       "tax-collection systems among the revenue methods, and the illustrative examples print "
       "the Ming practice of collecting taxes in hard currency as one.")),
 dict(
  q=("A ruler wishes to reduce his dependence on great landholding families for the government "
     "of his provinces. Which method described in the framework addresses that aim most "
     "directly?"),
  choices=[
   "Recruiting officials who owe their position to the ruler and are paid by the state",
   "Commissioning a series of imperial portraits for the palace",
   "Endowing a shrine in a distant province",
   "Requiring taxes to be paid in grain rather than in coin",
   "Granting the great families the right to farm the taxes of their own districts"],
  ans=0,
  why=("KC-4.3.I.C ties the recruitment of bureaucratic elites and the development of military "
       "professionals to rulers who wanted to maintain centralized control over their "
       "populations and resources, which is precisely the aim stated. The last option moves "
       "control toward the families rather than away from them, and the others concern "
       "legitimation and revenue form.")),
 dict(
  q=("A hypothetical provincial account from the period lists goods delivered each year by a "
     "conquered people to the imperial capital, itemized by district. Which of the framework's "
     "revenue methods does the account document?"),
  choices=[
   "Tribute collection",
   "The chartering of a monopoly company",
   "The recruitment of military professionals",
   "The commissioning of monumental architecture",
   "The imposition of an isolationist trade policy"],
  ans=0,
  why=("KC-4.3.I.D names tribute collection first among the revenue methods, and the "
       "illustrative examples print Mexica tribute lists as an instance of a tax-collection "
       "system. Chartered companies are KC-4.1.IV.C, and the other options are not revenue "
       "methods at all.")),
 dict(
  q=("A student argues that in this period rulers relied on force alone and never troubled to "
     "justify their authority. How should the argument be assessed against the framework?"),
  choices=[
   "It is inaccurate, because the framework has rulers using religious ideas, art, and architecture to legitimize rule",
   "It is accurate, because the framework mentions no means of legitimation",
   "It is accurate, because the framework says legitimation ceased after 1450",
   "It is inaccurate, because the framework says rulers used no force at all",
   "It is inaccurate, because the framework says rulers were elected by their subjects"],
  ans=0,
  why=("KC-4.3.I.A is an explicit statement that rulers continued to use religious ideas, art, "
       "and monumental architecture to legitimize their rule, so the argument fails. The two "
       "rejected corrections overstate in the other direction: KC-4.3.II makes force central to "
       "expansion, and no statement makes these rulers elected.")),
 dict(
  q=("Which pair of practices would a student cite to show that a ruler pursued both "
     "legitimation and revenue, as the framework describes them?"),
  choices=[
   "A dynastic mosque built in the capital, together with a new system for collecting taxes",
   "A dynastic mosque built in the capital, together with a new cathedral in the same city",
   "A tribute list from a conquered province, together with a tax farm in a neighbouring one",
   "A salaried corps of officials, together with a professional standing army",
   "A restrictive trade policy, together with a ban on foreign missionaries"],
  ans=0,
  why=("KC-4.3.I.A covers legitimation through religious ideas, art, and monumental "
       "architecture and KC-4.3.I.D covers revenue through tribute, tax farming, and innovative "
       "collection systems, so the pair must draw one from each. The rejected pairs draw both "
       "from a single statement, or from neither.")),
 dict(
  q=("Why would a historian describe the development of military professionals as part of the "
     "same process as the recruitment of bureaucratic elites?"),
  choices=[
   "Because the framework attributes both to rulers seeking centralized control over populations and resources",
   "Because the framework says soldiers and officials were the same people",
   "Because the framework says both groups were unpaid volunteers",
   "Because the framework says both groups were recruited from foreign empires",
   "Because the framework says both groups replaced the ruler in governing"],
  ans=0,
  why=("KC-4.3.I.C names the recruitment and use of bureaucratic elites and the development of "
       "military professionals in one sentence, with the same stated motive of maintaining "
       "centralized control over populations and resources. The rejected options add "
       "identities, pay arrangements and origins the sentence does not state.")),
 dict(
  q=("An empire's ruler orders that taxes formerly paid in grain be paid in coin instead. "
     "Within the framework's categories, this change is best described as which of the "
     "following?"),
  choices=[
   "An innovative tax-collection system used to generate revenue",
   "A religious idea used to legitimize rule",
   "A form of monumental architecture",
   "A restrictive trade policy aimed at foreign merchants",
   "A new labor system introduced in a colonial economy"],
  ans=0,
  why=("KC-4.3.I.D names innovative tax-collection systems among the revenue methods rulers "
       "used to forward state power and expansion, and the illustrative examples print the Ming "
       "practice of collecting taxes in hard currency under that heading. The rejected "
       "categories belong to KC-4.3.I.A, KC-4.3.II.A.i and KC-4.2.II.D.")),
 dict(
  q=("A hypothetical envoy's report describes a capital where the ruler's palace, the chief "
     "temple, and the treasury stand on one square, and where ceremonies performed at the "
     "temple are said by officials to confirm the ruler's right to govern.\n\n"
     "Which statement of the framework best contextualizes the report?"),
  choices=[
   "Rulers continued to use religious ideas and monumental architecture to legitimize their rule",
   "Rulers relied on gunpowder and cannon to expand their territory",
   "Rulers adopted restrictive policies to limit long-distance trade",
   "Colonial economies in the Americas depended largely on agriculture",
   "Existing trade networks in the Indian Ocean continued to flourish"],
  ans=0,
  why=("KC-4.3.I.A joins religious ideas to art and monumental architecture as the means of "
       "legitimation, and the report describes a ceremony in a monumental religious building "
       "doing exactly that work. The rejected statements are KC-4.3.II, KC-4.3.II.A.i, "
       "KC-4.2.II.D and KC-4.3.II.A.iii, none of which the report bears on.")),
 dict(
  q=("Two land empires of this period each face the problem of governing a large and distant "
     "province. Which comparison would be most useful for a student applying the framework's "
     "account of administration?"),
  choices=[
   "How each recruited and deployed officials to keep central control over the province",
   "How each named the months of its calendar",
   "How each decorated the walls of its provincial granaries",
   "Which crops each province exported to the capital in a single year",
   "How many rivers ran through each province"],
  ans=0,
  why=("KC-4.3.I.C makes the recruitment and use of bureaucratic elites, and the development of "
       "military professionals, the framework's account of how rulers maintained centralized "
       "control, so that is the axis on which a comparison bears. Calendars, decoration, a "
       "single year's exports and geography answer other questions.")),
 dict(
  q=("Which of the following would be the strongest evidence that a ruler was using art to "
     "legitimize rule in the sense the framework intends?"),
  choices=[
   "Portraits of the ruler commissioned by the court and displayed in official settings",
   "Sketches of local landscapes made privately by a travelling merchant",
   "Designs for farm implements circulated among village smiths",
   "Decorative tiles produced for sale in a provincial market",
   "Illustrations copied into a physician's private notebook"],
  ans=0,
  why=("KC-4.3.I.A names art alongside religious ideas and monumental architecture as a means "
       "by which rulers legitimized their rule, and the illustrative examples print Qing "
       "imperial portraits under art and monumental architecture. Art made privately or for "
       "sale is not commissioned by the ruler and does no legitimating work.")),
 dict(
  q=("A ruler grants a landholder the right to collect the revenue of a district and to retain "
     "a share of it. Which two of the framework's concerns does this arrangement bring into "
     "tension?"),
  choices=[
   "Raising revenue quickly, and keeping control of the provinces in the ruler's own hands",
   "Legitimizing rule through architecture, and legitimizing rule through religion",
   "Restricting foreign trade, and expanding overseas exploration",
   "Recruiting soldiers, and building a fleet",
   "Exchanging crops between hemispheres, and spreading disease"],
  ans=0,
  why=("KC-4.3.I.D presents revenue methods including tax farming, while KC-4.3.I.C makes "
       "centralized control over populations and resources the aim behind recruiting salaried "
       "elites; devolving collection to a landholder serves the first and complicates the "
       "second. The rejected pairs set two halves of a single statement against each other or "
       "belong to unit 4.")),
 dict(
  q=("A hypothetical chronicle states that a ruler's authority came directly from a divine "
     "grant and that to resist him was therefore to resist heaven. In the framework's "
     "categories, the chronicle records which kind of claim?"),
  choices=[
   "A religious idea used to legitimize rule",
   "An innovative tax-collection system",
   "A method of recruiting military professionals",
   "An example of resistance to state expansion",
   "A restrictive trade policy"],
  ans=0,
  why=("KC-4.3.I.A names religious ideas among the means by which rulers legitimized their "
       "rule, and the illustrative examples print European notions of divine right under "
       "religious ideas. The rejected categories are KC-4.3.I.D, KC-4.3.I.C, KC-4.3.III.iii "
       "and KC-4.3.II.A.i.")),
 dict(
  q=("Why does the framework's account of administration in this period sit under the theme of "
     "governance rather than under economics?"),
  choices=[
   "Because the methods described are the ways governments obtained, retained, and exercised power",
   "Because the methods described concern only the exchange of goods between societies",
   "Because the methods described are limited to the movement of enslaved labor",
   "Because the methods described are confined to religious belief",
   "Because the methods described belong entirely to the nineteenth century"],
  ans=0,
  why=("The thematic focus printed with this topic states that governments maintain order "
       "through administrative institutions, policies, and procedures and obtain, retain, and "
       "exercise power in different ways and for different purposes, which is what KC-4.3.I.A, "
       "KC-4.3.I.C and KC-4.3.I.D between them describe.")),
 dict(
  q=("A summary sentence about this topic is being drafted for students. Which version stays "
     "within what the framework asserts about the period 1450 to 1750?"),
  choices=[
   "Rulers legitimized their rule through religious ideas, art, and architecture, staffed the state with recruited elites and military professionals, and raised revenue by tribute and tax collection",
   "Rulers abandoned religious justifications, dismissed their officials, and gave up collecting revenue",
   "Rulers governed without officials, funded the state from foreign gifts, and built nothing",
   "Rulers relied only on tax farming and never recruited any officials of their own",
   "Rulers left the government of their empires to chartered trading companies"],
  ans=0,
  why=("The keyed sentence joins KC-4.3.I.A on legitimation, KC-4.3.I.C on recruited elites and "
       "military professionals, and KC-4.3.I.D on tribute collection, tax farming, and "
       "innovative tax-collection systems. Each rejected version contradicts at least one of "
       "those three statements.")),
]
