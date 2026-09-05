# AP WORLD HISTORY: MODERN 1.1  (title copied verbatim from WORLD_HISTORY_topics.json,
# which is why it reads as it does -- the CED topic page prints the title in a narrow
# column beside the skill statement and the extraction kept what that column held.)
# Unit 1 The Global Tapestry, c. 1200 to c. 1450. Suggested skill 4.A, identify and
# describe a historical context for a specific historical development or process.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   LO 1.A  Explain the systems of government employed by Chinese dynasties and how
#           they developed over time.
#   KC-3.2.I.A  Empires and states in Afro-Eurasia and the Americas demonstrated
#           continuity, innovation, and diversity in the 13th century. This included
#           the Song Dynasty of China, which utilized traditional methods of
#           Confucianism and an imperial bureaucracy to maintain and justify its rule.
#   LO 1.B  Explain the effects of Chinese cultural traditions on East Asia over time.
#   KC-3.1.III.D.i  Chinese cultural traditions continued, and they influenced
#           neighboring regions.
#   KC-3.1.III.D.ii  Buddhism and its core beliefs continued to shape societies in
#           Asia and included a variety of branches, schools, and practices.
#   LO 1.C  Explain the effects of innovation on the Chinese economy over time.
#   KC-3.3.III.A.i  The economy of Song China became increasingly commercialized
#           while continuing to depend on free peasant and artisanal labor.
#   KC-3.1.I.D  The economy of Song China flourished as a result of increased
#           productive capacity, expanding trade networks, and innovations in
#           agriculture and manufacturing.
#
#   Thematic focus GOV: a variety of internal and external factors contribute to state
#           formation, expansion, and decline; governments maintain order through a
#           variety of administrative institutions, policies, and procedures, and
#           governments obtain, retain, and exercise power in different ways and for
#           different purposes.
#   Thematic focus CDI: the development of ideas, beliefs, and religions illustrates
#           how groups in society view themselves, and the interactions of societies
#           and their beliefs often have political, social, and cultural implications.
#   Thematic focus ECN: as societies develop, they affect and are affected by the ways
#           that they produce, exchange, and consume goods and services.
#
#   Illustrative examples printed on this topic page (the CED calls them illustrative,
#   so they are used as instances of the key concepts above and never as the thing a
#   key turns on by itself): filial piety in East Asia; the influence of
#   Neo-Confucianism and Buddhism in East Asia; Confucian traditions of both respect
#   for and expected deference from women; Chinese literary and scholarly traditions
#   and their spread to Heian Japan and Korea; branches of Buddhism -- Theravada,
#   Mahayana, Tibetan; technological innovations -- Champa rice, transportation
#   innovations like the Grand Canal expansion, steel and iron production, textiles
#   and porcelains for export.
#
# ON THE SOURCES. Section I of this exam is stimulus based and this bank cannot show
# an image, so every stimulus here is either a table of HYPOTHETICAL figures whose
# keyed conclusion is recoverable from the table alone, or an explicitly unattributed
# illustrative source. No quotation is attributed to a real person or document:
# inventing one and signing a real name to it is fabrication, and a student would read
# it as fact.
#
# ON DATES. Spans are written "c. 1200 to c. 1450", never with a hyphen. The CED says
# its own dates are approximate -- events "are not constrained by the given dates and
# may begin before, or continue after, the period" -- so no key here turns on a
# boundary year.
TOPIC = ("1.1", "Developments in c. 1200 to c. 1450", 1)

_T_OUTPUT = dict(
    headers=["Period (hypothetical)", "Iron output (index)", "Registered urban households (thousands)"],
    rows=[["First", "100", "400"],
          ["Second", "160", "520"],
          ["Third", "240", "700"]])

_T_EXAM = dict(
    headers=["Prefecture (hypothetical)", "Candidates sitting the examination", "Official posts available"],
    rows=[["Prefecture A", "1,200", "30"],
          ["Prefecture B", "900", "30"],
          ["Prefecture C", "600", "30"]])

_T_HARVEST = dict(
    headers=["District (hypothetical)", "Rice harvests per year before the new variety",
             "Rice harvests per year after the new variety"],
    rows=[["District A", "1", "2"],
          ["District B", "1", "2"],
          ["District C", "1", "1"]])

QUESTIONS = [
 dict(q=("An unattributed administrative handbook from thirteenth-century China sets out a "
         "rule for staffing the provinces: candidates are examined on the classical texts, "
         "those who pass are appointed to provincial posts, and each appointee is rotated to "
         "a new post after a few years so that none becomes rooted in one place. Which of the "
         "following best explains how an arrangement of this kind helped a Chinese dynasty of "
         "the period both maintain and justify its rule?"),
      choices=[
        "It staffed an imperial bureaucracy with men trained in Confucian learning, so the same institution that carried out the dynasty's orders also supplied the standard by which its rule was defended.",
        "It replaced the imperial bureaucracy with a hereditary nobility whose rank came from birth rather than from examination.",
        "It transferred the appointment of provincial officials to Buddhist monasteries, which certified candidates on the dynasty's behalf.",
        "It abolished provincial posts in favor of direct rule by the emperor over every district in person.",
        "It made service in the army the only route into civil office, merging administration and military command into one career.",
      ], ans=0,
      why=("KC-3.2.I.A states that the Song Dynasty of China utilized traditional methods of "
           "Confucianism and an imperial bureaucracy to maintain and justify its rule. The "
           "examination and rotation described is that bureaucracy at work; the CED assigns no "
           "such role to monasteries, to a hereditary nobility or to the army.")),

 dict(q=("A historian writes that the states of the thirteenth century, taken across "
         "Afro-Eurasia and the Americas together, are better described as varied than as "
         "following one pattern. Which of the following observations would most directly "
         "support that judgment?"),
      choices=[
        "Governments in this period obtained, retained and exercised power in different ways and for different purposes, even where the problem of maintaining order was shared.",
        "Every state of the period recruited its officials by written examination on a common body of texts.",
        "No state of the period claimed any religious justification for the authority it exercised.",
        "All states of the period were governed by rulers who held office for a fixed and equal term.",
        "State systems in this period were confined to Afro-Eurasia and had no counterpart elsewhere.",
      ], ans=0,
      why=("The Governance thematic focus states that governments obtain, retain, and exercise "
           "power in different ways and for different purposes, and KC-3.2.I.A describes states "
           "in Afro-Eurasia and the Americas as demonstrating continuity, innovation, and "
           "diversity in the 13th century. Diversity is the claim; the four uniformity claims "
           "contradict it.")),

 dict(q=("A merchant's account from the period, its author unnamed, describes a Chinese city in "
         "which shops trade through the night, goods are bought with paper notes as well as "
         "coin, and craft workshops hire wage labor while the surrounding villages remain "
         "worked by peasant families holding their own land. Which of the following statements "
         "about the Song economy does the account best illustrate?"),
      choices=[
        "It was becoming more commercialized while still resting on the labor of free peasants and artisans.",
        "It had replaced peasant cultivation with large estates worked by enslaved field gangs.",
        "It had abandoned the use of money in favor of payment in grain alone.",
        "It was closed to exchange with regions beyond the dynasty's own borders.",
        "It concentrated all manufacturing in state workshops from which private craft was excluded.",
      ], ans=0,
      why=("KC-3.3.III.A.i states that the economy of Song China became increasingly "
           "commercialized while continuing to depend on free peasant and artisanal labor. The "
           "account shows both halves of that sentence at once, which is why the four "
           "alternatives, each of which denies one half, are unsupported.")),

 dict(q=("A fourteenth-century agricultural manual, author unknown, recommends a rice variety "
         "that ripens quickly and tolerates drier ground than the older sorts, so that fields "
         "which once yielded a single crop can be planted twice. Considered as a cause, an "
         "innovation of this kind contributed most directly to which development in China?"),
      choices=[
        "A rise in productive capacity that helped the economy flourish, since more food could be raised from the same land.",
        "A fall in the total population, since faster ripening shortened the growing season.",
        "The end of interregional trade, since regions could now feed themselves without exchange.",
        "The replacement of agriculture by manufacturing as the main employment of the population.",
        "The abolition of the imperial bureaucracy, which had existed only to allocate grain.",
      ], ans=0,
      why=("KC-3.1.I.D states that the economy of Song China flourished as a result of increased "
           "productive capacity, expanding trade networks, and innovations in agriculture and "
           "manufacturing. Champa rice is the CED's own illustrative example of such an "
           "agricultural innovation; none of the other four outcomes is asserted anywhere.")),

 dict(q=("Officials of a Chinese dynasty of this period undertook a large extension of an "
         "inland canal system linking the productive south to the political center in the "
         "north. Which of the following best states the historical significance of a project "
         "of that kind for the economy?"),
      choices=[
        "It was a transportation innovation that widened the trade networks on which the flourishing of the economy rested.",
        "It was a religious foundation whose purpose was to endow monasteries along its banks.",
        "It was a defensive work built to keep goods and people from moving between regions.",
        "It was a substitute for agriculture, since canal traffic replaced farming as the source of food.",
        "It was a purely local improvement with no consequence beyond the district in which it was dug.",
      ], ans=0,
      why=("KC-3.1.I.D names expanding trade networks and innovations in agriculture and "
           "manufacturing among the causes of Song China's flourishing economy, and the CED's "
           "illustrative list for this topic names transportation innovations like the Grand "
           "Canal expansion. A canal that carries goods widens a network rather than closing one.")),

 dict(q=("Buddhism in Asia during this period is described by historians as a single tradition "
         "carried in several distinct forms, among them Theravada, Mahayana and Tibetan. Which "
         "of the following claims about the religion in this period does that description best "
         "support?"),
      choices=[
        "Its core beliefs continued to shape societies across Asia even as it was practiced through a variety of branches and schools.",
        "It had ceased to influence society outside the monasteries by the thirteenth century.",
        "It existed in only one form, and regional differences in practice appeared only after 1450.",
        "It was confined to the region of its origin and did not reach societies beyond it.",
        "It replaced every other belief system in the societies where it was present.",
      ], ans=0,
      why=("KC-3.1.III.D.ii states that Buddhism and its core beliefs continued to shape "
           "societies in Asia and included a variety of branches, schools, and practices. "
           "Theravada, Mahayana and Tibetan are the CED's own illustrative branches, so "
           "variety within continuity is exactly the claim supported.")),

 dict(q=("A court diary kept in a neighboring East Asian society, whose author is not named, "
         "records that officials there composed poetry in Chinese characters, studied the same "
         "classical texts read by Chinese scholars, and modeled court ceremony on Chinese "
         "practice while retaining their own ruling house. Which of the following best explains "
         "the pattern the diary records?"),
      choices=[
        "Chinese cultural traditions continued in this period and influenced neighboring regions, which adopted them without ceasing to be governed separately.",
        "Chinese cultural traditions had lapsed by this period and were preserved only outside China.",
        "Neighboring societies could adopt Chinese literary practice only after being absorbed into a Chinese dynasty.",
        "Cultural influence in East Asia ran only outward from the smaller societies toward China.",
        "Classical Chinese learning was reserved to merchants and was unknown at any court.",
      ], ans=0,
      why=("KC-3.1.III.D.i states that Chinese cultural traditions continued and influenced "
           "neighboring regions; the CED's illustrative list names Chinese literary and "
           "scholarly traditions and their spread to Heian Japan and Korea. Influence without "
           "annexation is precisely what the statement describes.")),

 dict(q=("A household instruction text of the period, author unattributed, tells sons to "
         "support their parents in old age and to mourn them according to prescribed rites, and "
         "tells wives that they are owed respect within the household and are expected to defer "
         "to its senior men. A historian using this text to argue that belief systems had social "
         "consequences would be relying on which of the following?"),
      choices=[
        "The claim that ideas and beliefs shape how groups in a society view themselves, so that a tradition of filial obligation and of expected deference from women organizes ordinary household relations.",
        "The claim that household arrangements in this period were fixed by law and owed nothing to any belief system.",
        "The claim that Confucian teaching in this period applied only to the conduct of officials in office and not to families.",
        "The claim that texts of instruction describe what people already did and can never indicate what a tradition prescribed.",
        "The claim that respect within the household and deference within it are the same obligation under two names.",
      ], ans=0,
      why=("Learning Objective B of this unit asks for the effects of Chinese cultural "
           "traditions on East Asia, and the Cultural Developments thematic focus states that "
           "beliefs shape how groups view themselves and carry social implications; the topic's "
           "illustrative list names filial piety and Confucian traditions of both respect for "
           "and expected deference from women.")),

 dict(q=("Which of the following best describes what a historian means in calling Neo-Confucian "
         "thought and Buddhist practice in this period interacting rather than merely "
         "coexisting influences in East Asia?"),
      choices=[
        "Both were present in the same societies and each affected how people in them understood obligation and conduct, so their effects cannot be separated by region.",
        "One of them had displaced the other entirely by the thirteenth century, leaving a single tradition in place.",
        "Each was confined to a separate social class, so that no person encountered both.",
        "Both were state monopolies which private households were forbidden to observe.",
        "Neither had any bearing on how families or officials behaved, since both were purely speculative.",
      ], ans=0,
      why=("KC-3.1.III.D.i and KC-3.1.III.D.ii state that Chinese cultural traditions and "
           "Buddhism alike continued to shape societies in this period, and the topic's "
           "illustrative list pairs the influence of Neo-Confucianism and Buddhism in East "
           "Asia. Coexistence with mutual effect is what the two sentences together assert.")),

 dict(q=("Consider a claim that a dynasty's authority in this period rested on more than the "
         "force at its disposal. Which of the following pieces of evidence would most directly "
         "support that claim as the CED frames government in this period?"),
      choices=[
        "The dynasty appealed to an inherited body of teaching about right conduct and rule when it explained why obedience was owed to it.",
        "The dynasty maintained garrisons in every province and replaced their commanders often.",
        "The dynasty collected a land tax assessed on the area under cultivation.",
        "The dynasty fixed the weights and measures used in provincial markets.",
        "The dynasty repaired the roads by which its armies moved between the capital and the frontier.",
      ], ans=0,
      why=("KC-3.2.I.A says the Song used traditional methods of Confucianism and an imperial "
           "bureaucracy both to maintain and to JUSTIFY its rule, and the Governance thematic "
           "focus separates maintaining order from the purposes for which power is exercised. "
           "Only an appeal to a standard of right rule speaks to justification.")),

 dict(q=("The table below carries HYPOTHETICAL data supplied only to reason from. It records, "
         "for one region of China, an index of iron output and the number of registered urban "
         "households across three successive periods. Which conclusion does the data best "
         "support?"),
      table=_T_OUTPUT,
      choices=[
        "Iron output and registered urban households both rose in every period shown, a pattern consistent with increased productive capacity accompanying urban growth.",
        "Iron output fell across the three periods while urban households rose.",
        "Registered urban households more than tripled across the three periods shown.",
        "Iron output was unchanged between the second period and the third.",
        "Urban households rose while iron output stayed level throughout.",
      ], ans=0,
      why=("Recomputed from the table in the verifier: both columns rise at every step and no "
           "distractor survives the same numbers. KC-3.1.I.D attributes the flourishing of the "
           "Song economy to increased productive capacity and to innovations in manufacturing, "
           "which is the process such a pattern would illustrate.")),

 dict(q=("HYPOTHETICAL data for three prefectures in one examination year is set out in the "
         "table below, giving the number of candidates who sat the civil examination and the "
         "number of official posts to be filled. Which conclusion is best supported by that "
         "data alone?"),
      table=_T_EXAM,
      choices=[
        "In each prefecture shown, candidates outnumbered the available posts by more than ten to one.",
        "In at least one prefecture shown, posts outnumbered candidates.",
        "The prefecture with the fewest candidates had the highest number of candidates for each post.",
        "The three prefectures shown offered different numbers of posts from one another.",
        "Candidates and posts rose and fell together across the three prefectures.",
      ], ans=0,
      why=("Recomputed in the verifier from the table alone: the three ratios are forty, thirty "
           "and twenty candidates per post, so every alternative is false on the same numbers. "
           "The competition such figures describe is a feature of the imperial bureaucracy that "
           "KC-3.2.I.A names as a method of Song rule.")),

 dict(q=("For three districts, the table below records HYPOTHETICAL counts of the rice "
         "harvests gathered in a year before and after a fast-ripening variety was introduced. "
         "Which statement is best supported by that data?"),
      table=_T_HARVEST,
      choices=[
        "Two of the three districts shown doubled the number of harvests taken in a year, while the third was unchanged.",
        "Every district shown doubled the number of harvests taken in a year.",
        "No district shown gathered more harvests after the variety was introduced than before.",
        "The district that was unchanged had gathered the most harvests before the change.",
        "The introduction reduced the number of harvests in at least one district shown.",
      ], ans=0,
      why=("Recomputed in the verifier: two districts move from one harvest to two and the third "
           "does not move at all. KC-3.1.I.D names innovations in agriculture among the causes "
           "of the Song economy's flourishing, and an uneven effect across districts is what "
           "figures like these show.")),

 dict(q=("A student is asked to place the commercial growth of Song China in a historical "
         "context rather than simply to describe it. Which of the following statements does the "
         "work of contextualization best?"),
      choices=[
        "It occurred alongside rising productive capacity, widening trade networks and innovation in farming and manufacture, which together account for the economy's flourishing.",
        "It consisted of merchants buying goods in one place and selling them in another at a profit.",
        "It can be observed in the growth of particular cities whose names are recorded.",
        "It is described in written sources that survive from the period.",
        "It involved the use of coin and of paper notes side by side in the same markets.",
      ], ans=0,
      why=("Skill 4.A asks for the historical context of a development, not a restatement of it. "
           "KC-3.1.I.D supplies that context by naming productive capacity, trade networks and "
           "innovation as the conditions in which the economy flourished; the other four "
           "options describe or exemplify the development itself.")),

 dict(q=("Which of the following pairs a continuity with an innovation in Chinese government in "
         "the period from c. 1200 to c. 1450, as the CED characterizes that government?"),
      choices=[
        "A continuing reliance on Confucian methods of rule, together with administrative practice that changed as dynasties succeeded one another.",
        "A complete break with earlier methods of rule, together with an administration rebuilt on principles unknown before.",
        "A frozen administration in which nothing changed, together with a religion newly imposed from outside.",
        "The abandonment of bureaucracy, together with the rise of a purely military command over the provinces.",
        "The transfer of every governing function to merchant guilds, together with the end of imperial titles.",
      ], ans=0,
      why=("KC-3.2.I.A describes states of the 13th century as demonstrating continuity, "
           "innovation, and diversity at once, and names Confucianism and an imperial "
           "bureaucracy as the Song's traditional methods. LO 1.A asks how systems of government "
           "developed OVER TIME, which is change resting on continuity rather than replacing it.")),

 dict(q=("An unattributed traveler's notebook from the period describes workshops in a Chinese "
         "city turning out fine porcelain and woven silk in quantities far beyond what the city "
         "itself could use, packed for carriage to distant markets. This description is best "
         "used as evidence for which of the following?"),
      choices=[
        "That expanding production for export was one of the manufacturing innovations behind the flourishing of the Chinese economy.",
        "That Chinese cities of the period consumed everything they produced and traded nothing.",
        "That porcelain and silk were made only for the imperial household and never sold.",
        "That manufacturing in this period was carried on exclusively in the countryside.",
        "That production for distant markets began only after the middle of the fifteenth century.",
      ], ans=0,
      why=("KC-3.1.I.D names expanding trade networks and innovations in manufacturing among the "
           "causes of the Song economy's flourishing, and the topic's illustrative list names "
           "textiles and porcelains for export. The last option also fails because the CED's own "
           "dates are approximate and fix no such threshold.")),

 dict(q=("Two students disagree about the labor on which the Song economy rested. One says its "
         "growth must have required a change in who did the work; the other says the growth is "
         "compatible with the same kinds of workers as before. Which of the following resolves "
         "the disagreement as the CED states the matter?"),
      choices=[
        "The economy became more commercialized and yet continued to depend on free peasant and artisanal labor, so growth and continuity of the labor force are compatible.",
        "The economy became more commercialized only because free peasants were replaced by coerced field labor.",
        "The economy did not in fact become more commercialized, so the question of labor does not arise.",
        "The economy's growth was confined to state workshops, whose workers were not peasants or artisans.",
        "The economy depended on labor drawn entirely from neighboring regions rather than from China.",
      ], ans=0,
      why=("KC-3.3.III.A.i states in one sentence that the economy of Song China became "
           "increasingly commercialized WHILE CONTINUING to depend on free peasant and artisanal "
           "labor. The sentence itself settles the dispute, and each alternative denies one of "
           "its two halves.")),

 dict(q=("A description of a Chinese dynasty of this period notes that it recruited its "
         "officials by examination, promoted them by review of their record in post, and "
         "assigned them to districts far from their birthplaces. Taken together, these practices "
         "are best described as which of the following?"),
      choices=[
        "Administrative institutions and procedures through which a government maintained order across a large territory.",
        "Religious observances whose purpose was the instruction of the population in doctrine.",
        "Commercial regulations governing the conduct of merchants in the markets.",
        "Military arrangements for the defense of the frontier against outside attack.",
        "Kinship rules determining the inheritance of land within families.",
      ], ans=0,
      why=("The Governance thematic focus states that governments maintain order through a "
           "variety of administrative institutions, policies, and procedures, and KC-3.2.I.A "
           "names the imperial bureaucracy as a method the Song used to maintain and justify "
           "rule. Recruitment, promotion and posting are that machinery.")),

 dict(q=("Why is it inaccurate to say that Buddhism entered East Asian societies in this period "
         "for the first time?"),
      choices=[
        "Because the framework describes Buddhism and its core beliefs as continuing to shape societies in Asia during the period rather than arriving in them.",
        "Because Buddhism in this period was practiced only outside Asia.",
        "Because Buddhism had by this period been reduced to a single school with no regional variants.",
        "Because Buddhism in this period had no adherents outside monastic communities.",
        "Because Buddhism was in this period an official cult from which ordinary households were barred.",
      ], ans=0,
      why=("KC-3.1.III.D.ii states that Buddhism and its core beliefs CONTINUED to shape "
           "societies in Asia and included a variety of branches, schools, and practices. "
           "Continuation is the framework's word, and it is incompatible with a first arrival, "
           "with a single school, and with each of the other alternatives.")),

 dict(q=("A historian argues that the influence of Chinese traditions in East Asia in this "
         "period is best studied as a two-sided relationship rather than as a simple export. "
         "Which of the following observations would most weaken that argument?"),
      choices=[
        "Neighboring courts adopted Chinese literary and scholarly practice without any corresponding practice moving in the other direction.",
        "Neighboring courts adapted Chinese ceremonial to their own ruling houses rather than adopting it whole.",
        "Chinese scholarly writing circulated widely among officials in neighboring societies.",
        "Buddhism was practiced in several branches across the region during the same period.",
        "Chinese cultural traditions continued within China throughout the period.",
      ], ans=0,
      why=("KC-3.1.III.D.i asserts that Chinese cultural traditions influenced neighboring "
           "regions and asserts nothing about a return flow, so the observation that nothing "
           "moved the other way is the one that tells against a two-sided reading. The others "
           "are consistent with either account.")),

 dict(q=("Which of the following would be the strongest evidence that innovation in "
         "manufacturing, rather than in farming alone, contributed to the growth of the Chinese "
         "economy in this period?"),
      choices=[
        "A sustained rise in the output of iron and steel and in the quantity of woven and fired goods made for sale.",
        "A rise in the number of harvests taken from the same field in a single year.",
        "The extension of cultivation into land that had not been farmed before.",
        "An increase in the acreage sown with a drought-tolerant grain.",
        "A run of favorable seasons across several successive years.",
      ], ans=0,
      why=("KC-3.1.I.D distinguishes innovations in agriculture from innovations in "
           "manufacturing as separate causes of the Song economy's flourishing, and the topic's "
           "illustrative list names steel and iron production and textiles and porcelains. The "
           "other four options are all agricultural or climatic.")),

 dict(q=("A textbook states that Chinese dynasties of this period justified their rule as well "
         "as exercised it. Which of the following best explains why that distinction matters to "
         "a student of government?"),
      choices=[
        "Exercising power describes what a government does, while justifying it describes the grounds on which obedience is claimed, and a state can be strong in one and weak in the other.",
        "Exercising power and justifying it are two names for the same activity, so the distinction is a matter of wording.",
        "Justification is relevant only to religious institutions and never to governments.",
        "A government that exercises power effectively has no need of any justification for doing so.",
        "Justification precedes the exercise of power in every case and cannot follow it.",
      ], ans=0,
      why=("KC-3.2.I.A uses both verbs deliberately: the Song used Confucian methods and a "
           "bureaucracy to MAINTAIN AND JUSTIFY its rule. The Governance thematic focus "
           "likewise separates the ways power is obtained, retained and exercised from the "
           "purposes for which it is used.")),

 dict(q=("Suppose a source from this period records a Chinese dynasty appointing officials "
         "chosen for their learning in the classics and, in the same decade, adopting a new "
         "method of surveying land for taxation. A student who calls this an example of "
         "continuity and innovation together would be using which of the following correctly?"),
      choices=[
        "The framework's characterization of states in the 13th century as demonstrating continuity, innovation, and diversity at the same time.",
        "The framework's claim that states of the period changed completely from one dynasty to the next.",
        "The framework's claim that no state of the period altered any of its administrative methods.",
        "The framework's claim that innovation in government occurred only outside Afro-Eurasia.",
        "The framework's claim that learning and taxation were administered by separate states.",
      ], ans=0,
      why=("KC-3.2.I.A states that empires and states in Afro-Eurasia and the Americas "
           "demonstrated continuity, innovation, and diversity in the 13th century. The two "
           "measures described are an instance of exactly that combination; the other four "
           "options attribute to the framework claims it does not make.")),

 dict(q=("An unattributed account of a market town in this period notes that a farming family "
         "sold part of its harvest for coin and used the coin to buy cloth woven elsewhere, "
         "rather than weaving at home. This detail is most useful as evidence of which of the "
         "following?"),
      choices=[
        "Commercialization reaching into rural households, which bought and sold in markets while remaining free cultivators of their own land.",
        "The disappearance of agriculture as an occupation in the districts around market towns.",
        "The prohibition of household weaving by imperial decree.",
        "The replacement of coin by direct barter in rural exchange.",
        "The confinement of all buying and selling to the capital city.",
      ], ans=0,
      why=("KC-3.3.III.A.i pairs increasing commercialization with continued dependence on free "
           "peasant and artisanal labor, and the Economics thematic focus states that societies "
           "affect and are affected by the ways they produce, exchange, and consume goods. A "
           "peasant household buying in the market is both halves at once.")),

 dict(q=("Which of the following questions about East Asia in the period from c. 1200 to c. "
         "1450 could be settled by evidence, as distinct from being settled by a judgment about "
         "value?"),
      choices=[
        "Whether officials in a given dynasty were recruited by examination on classical texts.",
        "Whether a government that recruits officials by examination deserves the obedience of its subjects.",
        "Whether the deference expected of women in this period was just.",
        "Whether Buddhism or Confucian teaching offered the better guide to conduct.",
        "Whether a canal ought to have been built at public expense.",
      ], ans=0,
      why=("KC-3.2.I.A asserts a matter of fact about how the Song governed, and the CED's "
           "reasoning skills ask students to describe and explain historical developments rather "
           "than to rank them. Only the first question is answerable from evidence about what "
           "was done.")),

 dict(q=("A historian claims that the growth of Chinese cities in this period cannot be "
         "explained by any single cause. Which of the following would most strengthen that "
         "claim?"),
      choices=[
        "Evidence that rising farm output, wider trade networks and new manufacturing techniques each contributed and that removing any one of them leaves the growth unexplained.",
        "Evidence that the population of one particular city rose faster than that of its neighbors.",
        "Evidence that the growth began in a single decade and stopped in another.",
        "Evidence that officials in the cities were recruited by examination.",
        "Evidence that a traveler recorded the size of several cities.",
      ], ans=0,
      why=("KC-3.1.I.D lists three causes together for the flourishing of the Song economy: "
           "increased productive capacity, expanding trade networks, and innovations in "
           "agriculture and manufacturing. A multi-cause account is strengthened by evidence "
           "that each contributes, not by a fact about one city.")),

 dict(q=("Which of the following best describes the relationship between the imperial "
         "bureaucracy and Confucian learning in Song China as the framework presents it?"),
      choices=[
        "The learning supplied both the training of the officials and the language in which the dynasty defended its authority, so the two worked as one method of rule.",
        "The bureaucracy was staffed without reference to any body of learning and drew its personnel by lot.",
        "The learning was cultivated privately and was excluded by rule from the business of government.",
        "The bureaucracy and the learning were maintained by rival states rather than by one.",
        "The learning was adopted only after the bureaucracy had been dismantled.",
      ], ans=0,
      why=("KC-3.2.I.A names them together as the traditional methods the Song utilized to "
           "maintain and justify its rule, which is a single sentence linking the institution "
           "to the teaching. The four alternatives separate what the framework joins.")),

 dict(q=("A scholar wishes to argue that religious and philosophical traditions in East Asia in "
         "this period had political as well as private effects. Which of the following would be "
         "the most direct evidence for that argument?"),
      choices=[
        "That a dynasty drew on an inherited body of teaching to explain why its rule was legitimate, while the same teaching shaped conduct within ordinary households.",
        "That monasteries in the period maintained libraries of manuscripts.",
        "That travelers between regions carried religious texts with them.",
        "That several branches of one religion were practiced in the same region.",
        "That the population of the region grew across the period.",
      ], ans=0,
      why=("The Cultural Developments and Interactions thematic focus states that the "
           "interactions of societies and their beliefs often have political, social, and "
           "cultural implications, and KC-3.2.I.A shows the political side by having the Song "
           "justify rule through Confucian methods.")),

 dict(q=("Which of the following statements about the period from c. 1200 to c. 1450 is most "
         "consistent with the framework's own warning that its dates are approximate?"),
      choices=[
        "Processes such as commercialization and the spread of religious traditions may have begun before this period and continued after it.",
        "Every development studied in this period began in 1200 and ended in 1450.",
        "A development that can be traced before 1200 is by that fact outside the period's subject matter.",
        "The framework's dates mark legal boundaries that contemporaries themselves observed.",
        "No process may be described as continuing across the end of the period.",
      ], ans=0,
      why=("The CED states that events, processes, and developments are not constrained by the "
           "given dates and may begin before, or continue after, the period. KC-3.1.III.D.ii's "
           "word CONTINUED for Buddhism is an instance of a process that plainly predates the "
           "period's opening.")),

 dict(q=("A student writes that Song China shows how a government can be both conservative and "
         "innovative at once. Which of the following would be the best supporting evidence for "
         "that sentence?"),
      choices=[
        "That the dynasty governed through long-established Confucian methods and an imperial bureaucracy while its economy was transformed by new techniques in farming and manufacture.",
        "That the dynasty abandoned Confucian methods in order to make room for new techniques.",
        "That the dynasty rejected new techniques in order to preserve Confucian methods.",
        "That the dynasty neither used Confucian methods nor adopted new techniques.",
        "That the dynasty's methods and techniques were both imported unchanged from a neighboring state.",
      ], ans=0,
      why=("KC-3.2.I.A supplies the conservative half, the traditional methods of Confucianism "
           "and an imperial bureaucracy, and KC-3.1.I.D the innovative half, innovations in "
           "agriculture and manufacturing. Holding both at once is what the framework's phrase "
           "continuity, innovation, and diversity describes.")),
]
