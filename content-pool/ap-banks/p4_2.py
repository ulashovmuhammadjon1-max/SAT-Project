# AP PSYCH 4.2 Attitude Formation and Attitude Change — 30 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, p. 98.
# EK 4.2.A.1 stereotypes, prejudice, discrimination; 4.2.A.2 implicit attitudes,
# just-world phenomenon, out-group homogeneity bias, in-group bias, ethnocentrism;
# EK 4.2.B.1 belief perseverance and confirmation bias; 4.2.B.2 cognitive dissonance.
# NOTE: persuasion (elaboration likelihood model, halo effect, foot-in-the-door,
# door-in-the-face) is EK 4.3.A.3 in the current CED, not 4.2 -- it is authored in
# p4_3.py. Many older sources place it here.
# No sympy: every key's claim is stated item by item in verify_p4_2.py.
TOPIC = ("4.2", "Attitude Formation and Attitude Change", 4)
QUESTIONS = [
 dict(q="A stereotype is best defined as", choices=[
   "a generalized concept about the members of a group",
   "a hostile feeling directed at the members of a group",
   "an action that treats the members of a group unequally",
   "an emotional reaction that a person cannot consciously report"
], ans=0,
   why="A stereotype is a cognition -- a generalized concept about a group -- as distinct from the attitude of prejudice and the behavior of discrimination."),

 dict(q="Which sequence correctly matches stereotype, prejudice, and discrimination to what each one is?", choices=[
   "stereotype is an attitude, prejudice is a behavior, discrimination is a belief",
   "all three are beliefs that differ only in how strongly they are held",
   "stereotype is a belief, prejudice is an attitude, discrimination is a behavior",
   "stereotype is a behavior, prejudice is a belief, discrimination is an attitude"
], ans=2,
   why="The three terms separate the cognitive, affective, and behavioral components; conflating them is the most common error on this topic."),

 dict(q="According to the CED, one reason stereotypes persist is that they", choices=[
   "are transmitted genetically rather than socially",
   "cannot be changed once formed in early childhood",
   "reduce cognitive load when a person makes judgments or decisions",
   "are almost always accurate descriptions of group averages"
], ans=2,
   why="EK 4.2.A.1 notes that stereotypes can help reduce cognitive load when making decisions or judgments, which is why they are cognitively efficient and therefore sticky."),

 dict(q="A hiring manager privately dislikes applicants from a particular region but interviews and scores them the same as everyone else. This situation involves", choices=[
   "an implicit attitude that has become explicit",
   "cognitive dissonance that has already been resolved",
   "prejudice without discrimination",
   "discrimination without prejudice"
], ans=2,
   why="Prejudice is the attitude and discrimination the behavior; a negative attitude that never changes how people are treated is prejudice unaccompanied by discrimination."),

 dict(q="A landlord refuses to rent to applicants of a particular nationality. This refusal is an example of", choices=[
   "prejudice",
   "a stereotype",
   "an implicit attitude",
   "discrimination"
], ans=3,
   why="The item describes an unequal ACTION taken toward group members, which is the behavioral term; the underlying attitude and belief are not what the question asks about."),

 dict(q="Implicit attitudes are attitudes that a person", choices=[
   "states publicly but does not privately endorse",
   "has deliberately chosen after weighing evidence",
   "shares with every member of their culture",
   "holds but may be unaware of or may not acknowledge"
], ans=3,
   why="EK 4.2.A.2 defines implicit attitudes as those individuals hold but may be unaware of or may not acknowledge."),

 dict(q="The just-world phenomenon is the tendency to believe that", choices=[
   "people generally get the outcomes they deserve",
   "most people would behave ethically if given the chance",
   "the world is becoming fairer over successive generations",
   "one's own group is more varied than other groups are"
], ans=0,
   why="EK 4.2.A.2 lists the just-world phenomenon among the ways implicit attitudes can reflect negative evaluations of others: if the world is just, misfortune implies the sufferer deserved it."),

 dict(q="Told that a stranger lost a home in a flood, an observer's first thought is that the stranger must have been careless about insurance. This reaction most directly reflects", choices=[
   "cognitive dissonance",
   "the just-world phenomenon",
   "in-group bias",
   "out-group homogeneity bias"
], ans=1,
   why="A misfortune is reinterpreted as deserved, which is the signature of the just-world belief; no group membership or attitude-behavior conflict is involved."),

 dict(q="Out-group homogeneity bias is the tendency to perceive members of a group one does not belong to as", choices=[
   "less numerous than they actually are",
   "more deserving of resources than one's own group",
   "more similar to one another than they actually are",
   "more hostile toward one's own group than they actually are"
], ans=2,
   why="EK 4.2.A.2. The bias is about perceived VARIABILITY: out-group members look interchangeable while one's own group looks richly differentiated."),

 dict(q="In-group bias is best illustrated by a person who", choices=[
   "judges their own culture to be the standard by which others should be measured",
   "consistently rates the work of their own team more favorably than identical work by another team",
   "believes that members of another team are all alike",
   "assumes that a stranger's misfortune must have been deserved"
], ans=1,
   why="In-group bias is favoritism toward one's own group; the other options name out-group homogeneity bias, the just-world phenomenon, and ethnocentrism respectively."),

 dict(q="Ethnocentrism is most precisely described as", choices=[
   "judging other cultures by the standards of one's own culture",
   "preferring to associate with people of similar economic background",
   "the belief that cultures cannot meaningfully be compared at all",
   "the tendency to adopt the customs of whatever culture one is visiting"
], ans=0,
   why="EK 4.2.A.2 lists ethnocentrism among the implicit-attitude phenomena; it is the use of one's own culture as the reference standard for evaluating others."),

 dict(q="Belief perseverance occurs when a person", choices=[
   "cannot remember where a particular belief originally came from",
   "adopts whichever belief was most recently encountered",
   "maintains a belief even after evidence against it has been presented",
   "changes a belief as soon as any counterevidence appears"
], ans=2,
   why="EK 4.2.B.1: belief perseverance occurs when a belief persists even if evidence suggests it is not accurate."),

 dict(q="A reader who is convinced a certain diet works reads only websites that endorse it and skips the studies that question it. This selective search is", choices=[
   "cognitive dissonance",
   "the mere exposure effect",
   "confirmation bias",
   "the just-world phenomenon"
], ans=2,
   why="EK 4.2.B.1 pairs belief perseverance with confirmation bias: the person seeks evidence favorable to the existing belief and avoids evidence against it."),

 dict(q="How do belief perseverance and confirmation bias differ?", choices=[
   "Belief perseverance applies only to beliefs about oneself, while confirmation bias applies only to beliefs about others",
   "Belief perseverance is unconscious, while confirmation bias is always deliberate and strategic",
   "Belief perseverance requires new evidence to occur, while confirmation bias requires no evidence at all",
   "Belief perseverance is the persistence of the belief itself, while confirmation bias is the biased seeking and weighing of evidence that helps sustain it"
], ans=3,
   why="EK 4.2.B.1 treats them as linked but distinct: one names the outcome (the belief survives), the other names the process that protects it."),

 dict(q="Cognitive dissonance is best defined as", choices=[
   "disagreement between two members of a group about a decision",
   "the gap between a person's actual self and their ideal self",
   "mental discomfort arising when a person's actions and attitudes are in conflict",
   "difficulty holding two unrelated ideas in working memory at once"
], ans=2,
   why="EK 4.2.B.2 defines cognitive dissonance as the mental discomfort occurring when actions or attitudes are in conflict."),

 dict(q="According to the theory of cognitive dissonance, a person experiencing that discomfort is motivated to", choices=[
   "delay any decision until additional evidence becomes available",
   "change either the action or the attitude so that the two align",
   "repress all memory of the inconsistent action",
   "seek out a group that shares the inconsistency"
], ans=1,
   why="EK 4.2.B.2: people are motivated to reduce the discomfort by changing either actions or attitudes to be more in line with each other."),

 dict(q="A person who believes strongly in conserving fuel takes a job requiring a long solo commute, and within months reports that the environmental impact of commuting is 'probably overstated.' This attitude change is best explained by", choices=[
   "belief perseverance about fuel use",
   "the mere exposure effect of the commute",
   "an external locus of control",
   "the reduction of cognitive dissonance"
], ans=3,
   why="The behavior could not easily change, so the attitude moved to align with it -- the standard route to dissonance reduction described in EK 4.2.B.2."),

 dict(q="Participants who are paid a very small amount to describe a dull task as enjoyable later rate the task as more enjoyable than participants paid a large amount. Dissonance theory explains this because the small payment", choices=[
   "increases the mere exposure participants have to the task",
   "operates as a punishment that suppresses honest reporting",
   "provides too little external justification, so the attitude shifts to match the statement",
   "makes participants resent the experimenter and comply less"
], ans=2,
   why="With a large payment the behavior is fully explained by the money and no inconsistency remains; with a small payment the only way to resolve the conflict is to revise the attitude."),

 dict(q="A student who cheated once and considers herself honest resolves the discomfort by deciding 'everyone in the class does it.' This resolution works by", choices=[
   "adding a belief that makes the action consistent with the self-image",
   "changing the behavior so it no longer conflicts with the attitude",
   "forgetting that the behavior occurred at all",
   "replacing the attitude with its exact opposite"
], ans=0,
   why="Dissonance can be reduced by revising the surrounding beliefs so the action no longer contradicts the attitude, without either the action or the core attitude changing."),

 dict(q="Which of the following is the clearest evidence that an attitude is implicit rather than explicit?", choices=[
   "The attitude was formed recently rather than in childhood",
   "The person's responses reveal a preference that the person sincerely denies holding",
   "The person states the attitude confidently when asked directly",
   "The attitude is shared by most members of the person's culture"
], ans=1,
   why="EK 4.2.A.2's defining feature of an implicit attitude is that the holder is unaware of it or does not acknowledge it, so a sincere denial alongside a measured preference is the diagnostic pattern."),

 dict(q="Researchers give participants a fabricated test result, later fully debrief them that the result was invented, and find that participants still rate themselves in line with the false result. This finding demonstrates", choices=[
   "the false consensus effect",
   "the actor/observer bias",
   "belief perseverance",
   "cognitive dissonance"
], ans=2,
   why="The evidence supporting the belief was explicitly withdrawn and the belief survived anyway, which is exactly EK 4.2.B.1's definition of belief perseverance."),

 dict(q="A campaign designed to reduce prejudice by having members of two groups work together toward a shared aim is targeting which component most directly?", choices=[
   "the display rules governing emotional expression",
   "the participants' locus of control",
   "the attitude held toward the other group",
   "the genetic basis of group preference"
], ans=2,
   why="Prejudice is the attitude toward a group, and cooperative contact toward a shared aim is an intervention on that attitude rather than on memory, biology, or display rules."),

 dict(q="Why does the CED describe stereotypes as both a cause and a result of biased experience?", choices=[
   "A stereotype is inherited and then reinforced by the environment in equal measure",
   "A stereotype begins as a behavior and later becomes a belief",
   "A stereotype is accurate at the group level but inaccurate at the individual level",
   "A stereotype shapes what a perceiver notices and remembers, and that filtered experience then appears to confirm the stereotype"
], ans=3,
   why="EK 4.2.A.1 states stereotypes can be the cause and/or result of biased perceptions and experiences; the loop runs through selective attention and memory, which is also why confirmation bias sustains them."),

 dict(q="A researcher measures attitudes with a self-report questionnaire and finds almost no reported prejudice in the sample. The most important methodological limitation of this finding is that", choices=[
   "self-report cannot capture attitudes participants are unaware of or unwilling to acknowledge",
   "self-report questionnaires cannot be scored numerically",
   "questionnaires require random assignment in order to be valid",
   "the sample must be at least half of the target population"
], ans=0,
   why="Research-methods item. EK 4.2.A.2's implicit attitudes are by definition not accessible to self-report, so a null result on a questionnaire cannot establish that prejudice is absent."),

 dict(q="Two study groups each read the same balanced report on a policy, and each group's members become MORE confident in the view they already held. The best explanation of this outcome is", choices=[
   "the report changed the readers' behavior before it changed their attitudes",
   "repeated exposure to the report increased liking for the policy in both directions",
   "the readers had no attitude toward the policy before reading",
   "each reader weighed the supportive portions of the report more heavily than the opposing portions"
], ans=3,
   why="Identical balanced evidence producing divergent strengthening is the classic outcome of confirmation bias operating on an existing belief (EK 4.2.B.1)."),

 dict(q="Students who complete a long and demanding application process for a club later rate that club more favorably than students admitted with no effort at all. Dissonance theory explains this because the effort", choices=[
   "would be inconsistent with holding a low opinion of the club, so the opinion rises",
   "makes the club objectively better organized than it would otherwise be",
   "increases the number of times students are exposed to the club's name",
   "creates a debt that the club is expected to repay"], ans=0,
   why="Effort justification: substantial effort spent on something judged worthless is the inconsistency, and since the effort cannot be undone, the attitude moves to match it (EK 4.2.B.2)."),

 dict(q="How does ethnocentrism differ from in-group bias?", choices=[
   "Ethnocentrism is always conscious, while in-group bias is always unconscious",
   "Ethnocentrism treats one's own culture as the standard for evaluating others, while in-group bias is favoritism toward one's own group without necessarily invoking a cultural standard",
   "Ethnocentrism applies only to nations, while in-group bias applies only to families",
   "Ethnocentrism is a behavior, while in-group bias is a belief"
], ans=1,
   why="EK 4.2.A.2 lists both. In-group bias is preference for one's own group; ethnocentrism adds the evaluative yardstick, judging other cultures by one's own culture's standards."),

 dict(q="Research on attitudes and behavior finds that an attitude predicts a person's behavior most strongly when the attitude is", choices=[
   "formed recently rather than held over a long period",
   "specific to the behavior in question and social pressures on that behavior are weak",
   "held very privately and never expressed to anyone",
   "general and abstract rather than tied to a particular action"
], ans=1,
   why="Attitude-behavior consistency rises when the attitude is measured at the same level of specificity as the behavior and when outside pressures do not override it -- which is also why a broad, abstract attitude is a poor predictor of any single act."),

 dict(q="A fan of one team insists that supporters of a rival team 'all behave the same way at matches,' while describing his own team's supporters as a varied mix of people. His perception illustrates", choices=[
   "out-group homogeneity bias",
   "the just-world phenomenon",
   "belief perseverance",
   "cognitive dissonance"], ans=0,
   why="EK 4.2.A.2. The diagnostic contrast is perceived VARIABILITY: the rival group looks uniform while his own looks differentiated."),

 dict(q="A researcher wants to test whether an applicant's group membership CAUSES lower hiring ratings. The strongest design would be to", choices=[
   "record how many members of each group were hired last year and compare the totals",
   "interview applicants who were not hired about why they believe they were rejected",
   "send identical application materials that differ only in a name signaling group membership, and compare the ratings each receives",
   "survey hiring managers about whether they hold any prejudiced attitudes"
], ans=2,
   why="Research-design item (Science Practice 2.B). Only the first option manipulates the variable of interest while holding the credentials identical, so a difference in ratings can be attributed to group membership. The others are self-report or archival, and cannot establish causation -- and the survey option also runs into EK 4.2.A.2's point that implicit attitudes are not reliably self-reported."),
]
