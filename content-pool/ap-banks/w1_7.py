# AP WORLD HISTORY: MODERN 1.7 Comparison in the Period from c. 1200 to c. 1450
# (title copied verbatim from WORLD_HISTORY_topics.json). Unit 1 The Global Tapestry.
# Suggested skill 6.A, make a historically defensible claim.
#
# THIS IS THE UNIT'S REASONING TOPIC, so it is written as a reasoning set and not as
# fact recall. The CED says of every unit's final topic that it "focuses on the skill
# of argumentation and so provides an opportunity for your students to draw upon the
# key concepts and historical developments they have studied in this unit", and that
# the final topic page "includes key concepts, which summarize the historical
# developments in the unit". So the content here is unit 1's own key concepts and the
# question is nearly always which CLAIM about them a student may defend.
#
# THE REVIEW KEY CONCEPTS PRINTED ON THIS TOPIC PAGE, in the framework's own words:
#
#   LO 1.N  Explain the similarities and differences in the processes of state
#           formation from c. 1200 to c. 1450.
#   KC-3.2  State formation and development demonstrated continuity, innovation, and
#           diversity in various regions.
#   KC-3.2.I  As the Abbasid Caliphate fragmented, new Islamic political entities
#           emerged, most of which were dominated by Turkic peoples. These states
#           demonstrated continuity, innovation, and diversity.
#   KC-3.2.I.A  Empires and states in Afro-Eurasia and the Americas demonstrated
#           continuity, innovation, and diversity in the 13th century. This included
#           the Song Dynasty of China, which utilized traditional methods of
#           Confucianism and an imperial bureaucracy to maintain and justify its rule.
#   KC-3.2.I.B.i  State formation and development demonstrated continuity, innovation,
#           and diversity, including the new Hindu and Buddhist states that emerged in
#           South and Southeast Asia.
#   KC-3.2.I.D.i  In the Americas, as in Afro-Eurasia, state systems demonstrated
#           continuity, innovation, and diversity, and expanded in scope and reach.
#   KC-3.2.I.D.ii  In Africa, as in Eurasia and the Americas, state systems
#           demonstrated continuity, innovation, and diversity, and expanded in scope
#           and reach.
#
# ONE CITATION COMES FROM ELSEWHERE IN THE UNIT AND IS FLAGGED AS SUCH. KC-3.2.I.B.ii
# -- "Europe was politically fragmented and characterized by decentralized monarchies,
# feudalism, and the manorial system" -- is printed on topic 1.6 and is NOT in the
# list of review concepts this page reprints. It is cited in the few items that
# compare Europe with another region, and it is a unit 1 key concept, but the reader
# should know it was taken from the neighbouring topic page rather than from this one.
#
# THE SKILL SHAPES THE BANK. Skill 6.A is to MAKE A HISTORICALLY DEFENSIBLE CLAIM, so
# these items ask which of several drafts a student could defend, what a draft would
# need in order to become defensible, and which drafts overreach the framework --
# deliberately a different shape from 3.4 and 2.7, whose skill is 6.B and whose items
# ask which EVIDENCE supports a claim already made.
#
# ON THE SOURCES. This bank cannot show an image, so the stimuli are HYPOTHETICAL
# tables whose keyed conclusion is recoverable from the table alone, drafts of a
# student's own claims, or explicitly unattributed illustrative sources. Nothing is
# put into a real person's mouth.
#
# ON DATES. Spans are written "c. 1200 to c. 1450". The CED states that events,
# processes, and developments are not constrained by the given dates and may begin
# before, or continue after, the period, so no key turns on a boundary year -- and
# one item below is about exactly that trap.
TOPIC = ("1.7", "Comparison in the Period from c. 1200 to c. 1450", 1)

_T_POLITIES = dict(
    headers=["Region (hypothetical)", "Separate polities recorded at an earlier date",
             "Separate polities recorded at a later date"],
    rows=[["Region One", "12", "4"],
          ["Region Two", "3", "3"],
          ["Region Three", "6", "11"]])

_T_RECRUIT = dict(
    headers=["State (hypothetical)", "Officials recorded as recruited by examination",
             "Officials recorded as inheriting their posts"],
    rows=[["State One", "180", "20"],
          ["State Two", "40", "160"],
          ["State Three", "100", "100"]])

_T_INSTITUTIONS = dict(
    headers=["Region (hypothetical)", "Institutions carried forward from an earlier state",
             "Institutions first recorded in this period"],
    rows=[["Region One", "14", "6"],
          ["Region Two", "9", "9"],
          ["Region Three", "5", "15"]])

QUESTIONS = [
 dict(q=("A student is asked for a historically defensible claim about the processes of state "
         "formation between c. 1200 and c. 1450. Which of the following drafts best meets that "
         "description?"),
      choices=[
        "States in this period built authority on inherited methods and on new ones at the same time, and the balance between the two differed from region to region.",
        "States in this period were all built in the same way, since every region faced the same problem of maintaining order.",
        "States in this period were interesting, and studying them repays the effort a student puts into it.",
        "States in this period existed, as the surviving records show beyond dispute.",
        "States in this period should have governed their subjects more justly than they did.",
      ], ans=0,
      why=("KC-3.2 states that state formation and development demonstrated continuity, "
           "innovation, and diversity in various regions, and Learning Objective N asks for the "
           "similarities AND differences in those processes. A defensible claim must be arguable "
           "and supportable: the second contradicts diversity, the third and fourth are not "
           "arguable, and the fifth is a judgment of value rather than a historical claim.")),

 dict(q=("Which of the following identifies what is wrong with the draft claim: states in this "
         "period had governments?"),
      choices=[
        "It is not arguable, since nothing in the evidence could count against it, so there is nothing for an argument to establish.",
        "It is not true, since the framework denies that states in this period had governments.",
        "It is too specific, since it names a single region and a single century.",
        "It relies on a value judgment about what governments ought to have done.",
        "It compares two regions without saying which is being compared with which.",
      ], ans=0,
      why=("Suggested skill 6.A asks for a historically DEFENSIBLE claim, which is a claim an "
           "argument could defend against a rival reading. KC-3.2 asserts continuity, innovation "
           "and diversity in state formation, all of which are contestable claims; that states "
           "had governments is not one.")),

 dict(q=("Two drafts read as follows. The first: state formation in East Asia and state formation "
         "in the Americas both showed continuity and innovation. The second: state formation in "
         "East Asia rested on an inherited body of teaching in a way state formation in the "
         "Americas is not described as doing. Which of the following identifies the difference "
         "between them?"),
      choices=[
        "The first asserts a similarity and the second a difference, and Learning Objective N asks a student to be able to make claims of both kinds.",
        "The first asserts a difference and the second a similarity, so the two have been drafted the wrong way round.",
        "Both assert similarities, so neither meets the objective's requirement.",
        "Both assert differences, so neither meets the objective's requirement.",
        "Neither is a claim at all, since both name more than one region.",
      ], ans=0,
      why=("Learning Objective N asks students to explain the similarities AND differences in the "
           "processes of state formation from c. 1200 to c. 1450. KC-3.2.I.A and KC-3.2.I.D.i "
           "apply the same three terms to Afro-Eurasia and the Americas, which is the similarity, "
           "while only KC-3.2.I.A names Confucian methods, which is the difference. The anchor "
           "carries both halves because the strongest distractor exchanges them.")),

 dict(q=("A draft claim reads: every state of this period recruited its officials by written "
         "examination. Which of the following identifies the strongest objection?"),
      choices=[
        "The framework names an imperial bureaucracy as a method of one dynasty in particular, and asserts diversity among the state systems of every region, so a claim that all states did one thing runs against it.",
        "The framework denies that any state of this period recruited officials by examination.",
        "The claim is unobjectionable, since diversity in the framework's sense concerns religion rather than government.",
        "The claim is unobjectionable, since a claim about every state is easier to defend than a claim about one.",
        "The framework asserts nothing at all about how officials were recruited anywhere.",
      ], ans=0,
      why=("KC-3.2.I.A names the Song Dynasty of China as utilizing traditional methods of "
           "Confucianism and an imperial bureaucracy to maintain and justify its rule, and KC-3.2 "
           "asserts diversity in state formation across various regions. A universal claim is "
           "defeated by the diversity the framework repeatedly asserts.")),

 dict(q=("The table below carries HYPOTHETICAL counts of the separate polities recorded in three "
         "regions at an earlier and at a later date. Which claim does this data best support?"),
      table=_T_POLITIES,
      choices=[
        "The region holding the most polities at the earlier date is not the region holding the most at the later date, and the three regions together hold fewer at the later date than at the earlier one.",
        "The region holding the most polities at the earlier date also holds the most at the later date, and the three together hold more at the later date.",
        "Every region listed holds fewer polities at the later date than at the earlier one.",
        "No region listed holds more polities at the later date than at the earlier one.",
        "The three regions together hold the same number of polities at both dates.",
      ], ans=0,
      why=("Recomputed in the verifier from the table alone, distractors included. KC-3.2 states "
           "that state formation and development demonstrated continuity, innovation, and "
           "diversity in various regions, and a total falling while the region that leads the "
           "count changes hands is what a defensible claim of diversity rests on: the regions do "
           "not move together. The anchor carries both clauses because the strongest distractor "
           "inverts each of them.")),

 dict(q=("A student's thesis reads: state formation between c. 1200 and c. 1450 was everywhere a "
         "process of building something entirely new. Which of the following revisions would make "
         "it defensible on the framework's terms?"),
      choices=[
        "State formation in this period drew on arrangements inherited from earlier states as well as on arrangements that had no precedent anywhere before.",
        "State formation in this period preserved earlier arrangements without alteration everywhere.",
        "State formation in this period cannot be described, since the regions concerned are too unlike one another.",
        "State formation in this period was a process confined to Afro-Eurasia.",
        "State formation in this period produced states that were alike in every respect.",
      ], ans=0,
      why=("KC-3.2 and KC-3.2.I both name continuity, innovation, and diversity together, and "
           "KC-3.2.I.D.i and KC-3.2.I.D.ii repeat the same three terms of the Americas and of "
           "Africa. A claim of pure novelty drops continuity, and a claim of pure preservation "
           "drops innovation; the framework asserts both at once.")),

 dict(q=("HYPOTHETICAL counts of how officials came to hold their posts in three states are given "
         "in the table below. Which claim is best supported by that data alone?"),
      table=_T_RECRUIT,
      choices=[
        "The states listed differ sharply in how their officials came to hold office, so a claim that they obtained their officials in similar ways is not supportable from this data.",
        "In every state listed, officials recruited by examination outnumber those inheriting their posts.",
        "In every state listed, officials inheriting their posts outnumber those recruited by examination.",
        "The three states listed show the same balance between the two routes into office.",
        "Only one of the states listed records officials recruited by examination at all.",
      ], ans=0,
      why=("Recomputed in the verifier from the two columns. KC-3.2 asserts diversity in state "
           "formation across various regions and KC-3.2.I.A names an imperial bureaucracy as a "
           "method of one dynasty in particular, so figures pointing in opposite directions "
           "support a claim of difference rather than of similarity.")),

 dict(q=("An unattributed digest of four chronicles reports, of four different states, that one "
         "kept the titles of the state it displaced, that one created an office no predecessor "
         "had, that one did both, and that one did neither. Which claim about state formation "
         "does this material best support?"),
      choices=[
        "Continuity and innovation were both available to state builders in this period, and states combined them in different measures rather than choosing one or the other.",
        "State builders in this period had to choose between continuity and innovation and could not combine them.",
        "State builders in this period all made the same choice, so the four cases must be misreported.",
        "Continuity and innovation are the same thing described in two ways, so the four cases do not differ.",
        "The four cases show that state formation in this period cannot be described at all.",
      ], ans=0,
      why=("KC-3.2 states that state formation and development demonstrated continuity, "
           "innovation, and diversity in various regions, and KC-3.2.I says the same of the new "
           "Islamic political entities. The framework lists the three properties together, which "
           "is why a state may show any combination of them.")),

 dict(q=("Which of the following claims about the states that emerged as the Abbasid Caliphate "
         "fragmented is supported by the framework as it stands?"),
      choices=[
        "New Islamic political entities emerged, most of them dominated by Turkic peoples, and they showed continuity, innovation and diversity.",
        "A single new Islamic political entity emerged and absorbed the whole of the Caliphate's former territory.",
        "The entities that emerged were dominated by peoples drawn from outside Afro-Eurasia.",
        "No new political entity emerged, and the territory remained without government.",
        "The entities that emerged were uniform in their institutions and unchanging in extent.",
      ], ans=0,
      why=("KC-3.2.I states that as the Abbasid Caliphate fragmented, new Islamic political "
           "entities emerged, most of which were dominated by Turkic peoples, and that these "
           "states demonstrated continuity, innovation, and diversity. The key restates that "
           "sentence; each rejected option contradicts a part of it.")),

 dict(q=("Which of the following claims about South and Southeast Asia in this period does the "
         "framework support?"),
      choices=[
        "New Hindu and Buddhist states emerged there, and their formation showed the same continuity, innovation and diversity the framework finds elsewhere.",
        "No new state emerged there during this period.",
        "The states that emerged there were formed by a process the framework describes as unlike any other region's.",
        "The states that emerged there were Islamic entities dominated by Turkic peoples.",
        "The states that emerged there were the only states of the period to show innovation.",
      ], ans=0,
      why=("KC-3.2.I.B.i states that state formation and development demonstrated continuity, "
           "innovation, and diversity, including the new Hindu and Buddhist states that emerged "
           "in South and Southeast Asia. KC-3.2.I attaches Turkic domination to the entities "
           "that emerged from the Abbasid fragmentation, which is a different case.")),

 dict(q=("For three regions, the table below gives HYPOTHETICAL counts of institutions carried "
         "forward from an earlier state and institutions first recorded in this period. Which "
         "claim does the data best support?"),
      table=_T_INSTITUTIONS,
      choices=[
        "Every region listed records institutions of both kinds, and the balance between them differs from region to region.",
        "One of the regions listed records institutions carried forward and none first recorded.",
        "The balance between the two kinds is the same in all three regions listed.",
        "No region listed records an institution first recorded in this period.",
        "The region recording the most institutions carried forward also records the most first recorded in this period.",
      ], ans=0,
      why=("Recomputed in the verifier from the table alone. KC-3.2 names continuity, innovation, "
           "and diversity together as properties of state formation in various regions, and both "
           "kinds present everywhere in differing proportions is exactly that combination in "
           "figures.")),

 dict(q=("A student claims that state formation in this period followed different paths in "
         "different regions. Which of the following additions would most strengthen the claim by "
         "meeting the strongest objection to it?"),
      choices=[
        "An acknowledgment that the regions nonetheless shared the combination of inherited and new arrangements, together with an account of why that shared feature does not collapse the differences.",
        "A restatement of the claim in stronger words, so that an objection has less room in which to operate.",
        "A list of further regions the claim is said to cover, without any treatment of the objection.",
        "A statement that the objection cannot be assessed because the surviving evidence is incomplete.",
        "A concession that the claim is a matter of opinion on which reasonable people simply differ.",
      ], ans=0,
      why=("KC-3.2 asserts continuity, innovation, AND diversity together, so the strongest "
           "objection to a claim of difference is the framework's own claim of a shared pattern, "
           "and Learning Objective N asks for similarities and differences together. Meeting that "
           "objection is what strengthens the claim; restating it more loudly is not.")),

 dict(q=("A draft claim reads: state systems in the Americas and in Africa both grew in scope and "
         "reach. Which of the following identifies what a student would still need in order to "
         "turn this into an argument rather than a statement?"),
      choices=[
        "A reason why the two should be expected to resemble each other, and evidence from each region bearing on what growing in scope and in reach consisted of there.",
        "A larger number of regions, since a claim about two regions cannot be argued.",
        "A judgment about which of the two regions grew more admirably.",
        "A date on which the growth began in both regions simultaneously.",
        "A source written by a participant in each region rather than by a historian.",
      ], ans=0,
      why=("KC-3.2.I.D.i and KC-3.2.I.D.ii say of the Americas and of Africa that state systems "
           "demonstrated continuity, innovation, and diversity, and expanded in scope and reach. "
           "Skill 6.A asks for a defensible claim, which needs a ground and evidence rather than "
           "more cases, an evaluation or a shared date.")),

 dict(q=("Which of the following drafts is a comparison rather than two descriptions set side by "
         "side?"),
      choices=[
        "Both the Song Dynasty and the state systems of Africa are described as showing continuity, innovation and diversity, but only the former is described as justifying its rule through an inherited body of teaching.",
        "The Song Dynasty used an imperial bureaucracy. The state systems of Africa expanded in scope and reach.",
        "The Song Dynasty is described in one key concept, and African state systems are described in another key concept.",
        "The Song Dynasty and the state systems of Africa both belong to the period from c. 1200 to c. 1450.",
        "The Song Dynasty existed in Asia, and state systems in Africa existed in Africa.",
      ], ans=0,
      why=("Learning Objective N asks for the similarities and differences in the processes of "
           "state formation, which requires a relation between the cases and not two statements "
           "in sequence. KC-3.2.I.A supplies the Confucian justification and KC-3.2.I.D.ii the "
           "expansion in scope and reach, so the relation the key asserts is one the framework "
           "supports.")),

 dict(q=("A draft claim reads: state formation in this period was driven by trade. Which of the "
         "following identifies why a student should hesitate before defending it in this unit?"),
      choices=[
        "The unit's key concepts on state formation name continuity, innovation and diversity and a variety of internal and external factors, without singling out any one driver.",
        "The framework denies that trade existed in this period.",
        "A claim naming a cause can never be defended in history.",
        "The framework states that state formation had no causes at all.",
        "Trade belongs to a later period than the one this unit covers.",
      ], ans=0,
      why=("KC-3.2 names continuity, innovation, and diversity in state formation, and the "
           "Governance thematic focus states that a variety of internal and external factors "
           "contribute to state formation, expansion, and decline. A single-driver claim is not "
           "forbidden but is answerable to that variety, which is what a student must be ready "
           "for.")),

 dict(q=("An unattributed summary of a region's history says that a ruling house was replaced but "
         "that the offices, the titles and the manner of collecting dues went on as before. Which "
         "claim does this best support?"),
      choices=[
        "A change of ruler and a change of the arrangements through which a state governs are separate things, so continuity in state formation can survive a break in the ruling line.",
        "A change of ruler necessarily means a change in the arrangements through which a state governs.",
        "A state that keeps its offices after a change of ruler has not really changed its ruler.",
        "Continuity in the framework's sense refers only to an unbroken line of rulers.",
        "The summary describes an impossible situation, since offices cannot outlast the house that created them.",
      ], ans=0,
      why=("KC-3.2 states that state formation and development demonstrated continuity, "
           "innovation, and diversity, and the Governance thematic focus names administrative "
           "institutions, policies, and procedures as how governments maintain order. The "
           "framework attaches continuity to those arrangements, not to a line of descent.")),

 dict(q=("Which of the following claims about this period would be indefensible because it "
         "depends on a boundary the framework explicitly loosens?"),
      choices=[
        "That a process observable in 1210 must have begun after 1200, since the period opens there.",
        "That processes studied in this period may be traced in evidence from before it.",
        "That a state formed in this period may have preserved arrangements older than the period.",
        "That a development studied in this period may have continued after it ended.",
        "That the framework's dates are approximate rather than exact.",
      ], ans=0,
      why=("The CED states that events, processes, and developments are not constrained by the "
           "given dates and may begin before, or continue after, the period. KC-3.2's word "
           "continuity presupposes arrangements older than the period's opening, so a claim "
           "resting on the opening year as a barrier is the one the framework rules out.")),

 dict(q=("A student writes: because the framework uses the same three words of every region, all "
         "the regions were the same. Which of the following identifies the mistake?"),
      choices=[
        "One of the three words is diversity, so the shared description asserts variation rather than sameness.",
        "The three words are used of only one region, so the student has misread which region is meant.",
        "The three words describe institutions, so using them of two regions does assert that their institutions matched.",
        "The three words are used only of Afro-Eurasia and never of the Americas or Africa.",
        "The student is correct, since a shared description always implies a shared character.",
      ], ans=0,
      why=("KC-3.2, KC-3.2.I, KC-3.2.I.A, KC-3.2.I.B.i, KC-3.2.I.D.i and KC-3.2.I.D.ii all name "
           "continuity, innovation, AND DIVERSITY together. A vocabulary whose third term is "
           "diversity cannot be evidence of uniformity.")),

 dict(q=("Which of the following pairs a claim with the kind of evidence that would bear on it "
         "most directly?"),
      choices=[
        "The claim that a state expanded in reach, paired with a record of dues rendered from a district that had rendered none before.",
        "The claim that a state expanded in reach, paired with a record of a new office created at the existing capital.",
        "The claim that a state expanded in scope, paired with a record of its frontier moved outward.",
        "The claim that a state showed continuity, paired with a record of an office no predecessor of that state had held.",
        "The claim that state formation was diverse, paired with a record of one office in one state in one year.",
      ], ans=0,
      why=("KC-3.2.I.D.i and KC-3.2.I.D.ii name expansion in scope and expansion in reach as two "
           "different things, and KC-3.2 joins continuity to innovation. Dues arriving from a "
           "district that owed none before is authority reaching further; each rejected pairing "
           "attaches its evidence to the wrong half of one of those distinctions.")),

 dict(q=("Two drafts differ by one word. The first says that the new political entities that "
         "emerged as the Abbasid Caliphate fragmented were dominated by Turkic peoples. The "
         "second says that most of them were. Which of the following identifies why the second is "
         "the defensible draft?"),
      choices=[
        "Because the framework says most of them were so dominated, and a draft covering all of them asserts more than the sentence it rests on.",
        "Because a draft using the word most is always safer than one using the word all, whatever its source says.",
        "Because the framework says none of them were so dominated, so both drafts overstate the case.",
        "Because the framework does not mention Turkic peoples anywhere, so neither draft can be defended.",
        "Because the two drafts assert the same thing, so the choice between them makes no difference.",
      ], ans=0,
      why=("KC-3.2.I states that as the Abbasid Caliphate fragmented, new Islamic political "
           "entities emerged, MOST OF WHICH were dominated by Turkic peoples. A defensible claim "
           "matches the quantifier of the sentence it rests on; the second rejected option "
           "reaches the right draft for the wrong reason, which is not a defence at all.")),

 dict(q=("Which of the following is the strongest reason for a student to write about processes "
         "of state formation rather than about a list of states?"),
      choices=[
        "Learning Objective N asks about the processes of state formation, so a claim about how states came to be governed can be compared across regions in a way a list of names cannot.",
        "The framework does not permit any state to be named in an argument.",
        "A list of names is easier to defend and therefore a weaker exercise.",
        "Processes are the same everywhere, so comparing them removes the need for evidence.",
        "The framework treats every state of the period as an example of one process.",
      ], ans=0,
      why=("Learning Objective N asks students to explain the similarities and differences in the "
           "PROCESSES of state formation from c. 1200 to c. 1450, and KC-3.2 describes those "
           "processes as showing continuity, innovation, and diversity. A process is the thing "
           "the objective makes comparable.")),

 dict(q=("A draft claim reads: African and American state systems both expanded, but for opposite "
         "reasons. Which of the following identifies the problem with defending the second half "
         "of that claim from this unit?"),
      choices=[
        "The framework asserts the expansion of both in the same words and assigns no reasons at all, so the reasons would have to come from outside the unit's key concepts.",
        "The framework assigns reasons to the American case only, so the African half is the unsupported one.",
        "The framework denies that either expanded, so the first half is the unsupported one.",
        "The framework assigns the same reason to both, so the word opposite is the only error.",
        "The framework forbids any claim that names two regions at once.",
      ], ans=0,
      why=("KC-3.2.I.D.i and KC-3.2.I.D.ii state in parallel words that state systems in the "
           "Americas and in Africa demonstrated continuity, innovation, and diversity, and "
           "expanded in scope and reach. Neither sentence supplies a cause, so a claim about "
           "opposite reasons has nothing in this unit's concepts to rest on.")),

 dict(q=("An unattributed traveller's notebook describes two neighbouring states, one governed "
         "through officers appointed and paid by its ruler and one through lords who held land "
         "and brought their own followers. Which claim does this best support?"),
      choices=[
        "That a claim asserting diversity in how states maintained order is defensible here, since two arrangements answering the same need is what the framework's third term names.",
        "One of the two described cannot have been a state, since only one arrangement counts as government.",
        "The two arrangements are the same, since both end in the ruler's authority being felt.",
        "The difference between the two shows that one of them lay outside the period.",
        "Neighbouring states must always govern in the same way, so the notebook is unreliable.",
      ], ans=0,
      why=("KC-3.2 names diversity as the third of the three terms it applies to state formation "
           "across various regions, and the Governance thematic focus states that governments "
           "maintain order through a variety of administrative institutions, policies, and "
           "procedures and exercise power in different ways and for different purposes.")),

 dict(q=("A student notices that the framework uses the language of fragmentation both of Europe "
         "and of the territory of the Abbasid Caliphate. Which of the following claims about that "
         "shared language can be defended from the unit's key concepts?"),
      choices=[
        "That fragmentation is said of both, but the framework attaches to the Abbasid case the emergence of new political entities mostly dominated by Turkic peoples and to the European case decentralized monarchies, feudalism and the manorial system, so the shared word covers different outcomes.",
        "That fragmentation is said of both, so the outcomes the framework attaches to the two cases must have been the same.",
        "That fragmentation is said only of Europe, so the student has misread the Abbasid case.",
        "That fragmentation is said only of the Abbasid case, so the student has misread the European one.",
        "That the framework attaches no outcome to either case, so nothing whatever can be claimed about the difference.",
      ], ans=0,
      why=("KC-3.2.I states that as the Abbasid Caliphate fragmented, new Islamic political "
           "entities emerged, most of which were dominated by Turkic peoples, while KC-3.2.I.B.ii "
           "-- printed on topic 1.6 rather than on this page -- states that Europe was politically "
           "fragmented and characterized by decentralized monarchies, feudalism, and the manorial "
           "system. One word, two different consequences in the framework's own text.")),

 dict(q=("Which of the following would make a claim about state formation in this period LESS "
         "defensible rather than more?"),
      choices=[
        "Widening it from the regions the evidence covers to every region of the world.",
        "Naming the regions it applies to and the period it covers.",
        "Stating what would count as evidence against it.",
        "Distinguishing the similarity it asserts from the differences it concedes.",
        "Citing the framework sentence the claim is drawn from.",
      ], ans=0,
      why=("Skill 6.A asks for a historically DEFENSIBLE claim, and KC-3.2 confines its own "
           "assertion to various regions rather than to all of them. A claim stretched past its "
           "evidence becomes harder to defend, while specification, falsifiability and citation "
           "all make defence easier.")),

 dict(q=("A student's draft asserts that the states of this period were more alike than "
         "different. Which of the following identifies what would most directly count against it?"),
      choices=[
        "The framework's repeated assertion of diversity alongside continuity and innovation, in every region it applies the three terms to.",
        "The framework's assertion that states in this period existed in more than one region.",
        "The framework's use of the same three terms of several regions.",
        "The framework's statement that its own dates are approximate.",
        "The framework's silence about the size of any state's population.",
      ], ans=0,
      why=("KC-3.2, KC-3.2.I, KC-3.2.I.A, KC-3.2.I.B.i, KC-3.2.I.D.i and KC-3.2.I.D.ii each name "
           "DIVERSITY beside continuity and innovation. That repeated word is what a claim of "
           "predominant likeness must answer; the mere use of a shared vocabulary is not, since "
           "one of the shared terms is diversity itself.")),

 dict(q=("Which of the following claims goes beyond what the unit's key concepts assert?"),
      choices=[
        "That the state systems of Africa expanded further in scope and reach than those of the Americas did.",
        "That the state systems of Africa expanded in scope and reach.",
        "That the state systems of the Americas expanded in scope and reach.",
        "That state systems in both regions showed continuity, innovation and diversity.",
        "That the framework describes both regions in parallel terms.",
      ], ans=0,
      why=("KC-3.2.I.D.i and KC-3.2.I.D.ii assert the same expansion of the Americas and of "
           "Africa in the same words and never compare their extents. A claim that one expanded "
           "FURTHER than the other adds a comparison of magnitude the framework does not make.")),

 dict(q=("An unattributed account states that a state's founder took the regalia of the dynasty "
         "he displaced and also created a new council that had no counterpart before. A student "
         "wishes to use this in an argument about the period as a whole. Which of the following "
         "identifies the soundest use?"),
      choices=[
        "As one illustration of a pattern the framework asserts generally, with the general claim carrying the argument and the case supporting it.",
        "As proof that every state of the period behaved in the same way as this one.",
        "As evidence that the framework's account of the period is mistaken.",
        "As a substitute for any general claim, since a vivid case argues for itself.",
        "As evidence about the period only if the state concerned can be shown to be typical in every respect.",
      ], ans=0,
      why=("KC-3.2 states that state formation and development demonstrated continuity, "
           "innovation, and diversity in various regions, which is the general claim, and skill "
           "6.A asks for a defensible claim rather than for a narrative. One case can illustrate "
           "a general assertion without establishing it and without needing to be typical in "
           "every respect.")),

 dict(q=("Which of the following identifies a similarity the framework does assert across the "
         "regions of this unit?"),
      choices=[
        "That state formation and development in each of them showed continuity, innovation and diversity.",
        "That each of them recruited officials by examination on a common body of texts.",
        "That each of them was governed by a single ruler for the whole period.",
        "That each of them was in regular contact with all the others.",
        "That each of them adopted the same religious tradition.",
      ], ans=0,
      why=("KC-3.2 asserts that state formation and development demonstrated continuity, "
           "innovation, and diversity in various regions, and KC-3.2.I.A, KC-3.2.I.B.i, "
           "KC-3.2.I.D.i and KC-3.2.I.D.ii repeat the three terms of Afro-Eurasia, South and "
           "Southeast Asia, the Americas and Africa in turn. None of the other four uniformities "
           "is asserted anywhere.")),

 dict(q=("Taken together, which of the following is the most defensible summary claim a student "
         "could make about the processes of state formation from c. 1200 to c. 1450?"),
      choices=[
        "Across the regions the unit covers, the process was alike in showing continuity, innovation and diversity everywhere, and unlike in the particular arrangements each region produced.",
        "Across the regions the unit covers, states were built on one common model that varied only in detail.",
        "Across the regions the unit covers, states abandoned every inherited arrangement and began afresh.",
        "Across the regions the unit covers, state formation cannot be compared, since each region is a separate case.",
        "Across the regions the unit covers, states are best ranked by how far each had advanced toward a single form of government.",
      ], ans=0,
      why=("KC-3.2 states that state formation and development demonstrated continuity, "
           "innovation, and diversity in various regions, and Learning Objective N asks for the "
           "similarities AND the differences in those processes. The key names one of each, which "
           "is what the objective requires; each rejected option drops a term or replaces the "
           "comparison with a ranking the framework never makes.")),
]
