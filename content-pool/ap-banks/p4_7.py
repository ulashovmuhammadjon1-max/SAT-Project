# AP PSYCH 4.7 Emotion — 30 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, pp. 105-106.
# EK 4.7.A.1 emotion as a complex psychological process distinguished from
#   reasoning or knowledge; the early 20th-century dispute over whether the
#   physiological and cognitive experiences occur in SUCCESSION or
#   SIMULTANEOUSLY, and the position that a cognitive LABEL is required; the
#   facial-feedback hypothesis, whose research has produced MIXED results.
# EK 4.7.A.2 the broaden-and-build theory of emotion.
# EK 4.7.B.1 universality of emotional expression -- anger, disgust, sadness,
#   happiness, surprise, fear -- with research showing mixed results.
# EK 4.7.B.2 display rules and elicitors, which differ among cultures and may
#   regulate expression across genders, ages, and socioeconomic classes.
#
# THE EXCLUSION THAT GOVERNS THIS WHOLE MODULE, printed in the CED under
# EK 4.7.A.1: "Specific names of theories of emotion are outside the scope of the
# AP Psychology Exam." Nearly every study guide in circulation drills the surnames
# attached to the succession, simultaneity and cognitive-label positions. No item
# here names or requires one; the positions are tested by what each one actually
# CLAIMS about the ordering of physiological and cognitive events. Note that
# broaden-and-build IS named in required content (EK 4.7.A.2) and so may be keyed
# by name -- the exclusion attaches to the early 20th-century theories in 4.7.A.1.
#
# No sympy: every key's claim is stated item by item in verify_p4_7.py.
TOPIC = ("4.7", "Emotion", 4)
QUESTIONS = [
 dict(q="The AP Psychology framework describes emotion as a complex psychological process that is", choices=[
   "distinguished from reasoning or knowledge, and reflects both internal and external factors",
   "identical to a reasoned judgment about a situation",
   "produced entirely by factors internal to the body",
   "produced entirely by factors in the external environment"], ans=0,
   why="EK 4.7.A.1: emotion is a complex psychological process distinguished from reasoning or knowledge, and emotions reflect internal AND external factors affecting an individual."),

 dict(q="One early theoretical position held that the bodily response comes FIRST and the conscious feeling follows from noticing it. This position claims that", choices=[
   "physiological change precedes and gives rise to the cognitive experience of emotion",
   "the cognitive experience precedes and produces the physiological change",
   "the physiological and cognitive components occur at the same moment",
   "emotions occur without any physiological component at all"], ans=0,
   why="EK 4.7.A.1 records that some theories proposed the physiological and cognitive experiences occurred in SUCCESSION. This is the version in which the body leads and the feeling is read off it."),

 dict(q="A competing early position held that the bodily response and the conscious feeling are triggered together rather than one causing the other. This position claims that", choices=[
   "the physiological and cognitive components occur simultaneously",
   "the physiological component always occurs several seconds before the feeling",
   "the feeling always occurs before any bodily change",
   "the bodily response is irrelevant to emotion"], ans=0,
   why="EK 4.7.A.1: while some theories proposed succession, others proposed the physiological and cognitive experiences occurred SIMULTANEOUSLY. This item tests the claim, which is in scope, rather than the theory's name, which is not."),

 dict(q="A third position holds that physiological arousal alone is not enough for an emotion, because the same arousal could accompany several different emotions. This position adds the requirement that", choices=[
   "the arousal must reach a particular intensity threshold",
   "the arousal must be accompanied by a facial expression",
   "the arousal must last for a minimum period of time",
   "the person must interpret the arousal and apply a cognitive label to it"
], ans=3,
   why="EK 4.7.A.1: other theories emphasize that the cognitive label is required to experience an emotion. Ambiguous arousal is exactly the problem the labelling requirement solves."),

 dict(q="A person's heart races on a first date and again during a near-miss in traffic, and the two experiences feel like entirely different emotions. This observation gives most support to the view that", choices=[
   "the two situations must have produced different patterns of arousal",
   "a cognitive interpretation of the arousal is needed to determine which emotion is felt",
   "physiological arousal alone fully determines which emotion is felt",
   "emotions have no physiological component"
], ans=1,
   why="EK 4.7.A.1. Similar arousal accompanied by different emotions is the observation that motivates the cognitive-label requirement; if arousal alone fixed the emotion, the two experiences would feel alike."),

 dict(q="The facial-feedback hypothesis proposes that", choices=[
   "facial expressions are learned entirely from watching others",
   "facial expressions have no relationship to felt emotion",
   "the face is the only reliable channel for reading another person's emotion",
   "the experience of an emotion is influenced by one's facial expression"
], ans=3,
   why="EK 4.7.A.1: the facial-feedback hypothesis suggests that the experience of emotion is influenced by facial expressions. The causal arrow runs from expression to experience, which is what makes it a hypothesis worth testing."),

 dict(q="The facial-feedback hypothesis is described in the framework as supporting which broader view?", choices=[
   "that emotional expression is unrelated to emotional experience",
   "that the physiological experience of emotion precedes the cognitive appraisal",
   "that the cognitive appraisal precedes the physiological experience",
   "that emotions are entirely learned through culture"
], ans=1,
   why="EK 4.7.A.1 states that the facial-feedback hypothesis supports theories proposing the physiological experience of emotion PRECEDES the cognitive appraisal: if arranging the face changes the feeling, the bodily state is leading."),

 dict(q="What does the framework say about the research testing the facial-feedback hypothesis?", choices=[
   "It has produced mixed results",
   "It has confirmed the hypothesis in essentially every study",
   "It has disconfirmed the hypothesis in essentially every study",
   "It has never been attempted experimentally"], ans=0,
   why="EK 4.7.A.1 states that research testing this hypothesis has produced MIXED results. Study guides frequently present facial feedback as settled, and the framework deliberately does not."),

 dict(q="The broaden-and-build theory of emotion proposes that positive emotional experiences tend to", choices=[
   "reduce the range of behavior a person will consider",
   "broaden awareness and encourage new thoughts and actions",
   "narrow attention onto the source of the emotion",
   "have no measurable effect on thinking"
], ans=1,
   why="EK 4.7.A.2, in substance verbatim: the broaden-and-build theory proposes that positive emotional experiences tend to broaden awareness and encourage new actions and thoughts."),

 dict(q="According to the broaden-and-build theory, negative emotions tend to", choices=[
   "produce a permanent reduction in emotional capacity",
   "narrow thinking and the range of action a person considers",
   "broaden awareness in the same way positive emotions do",
   "leave attention and behavior unchanged"
], ans=1,
   why="EK 4.7.A.2: negative emotions tend to reduce awareness and narrow thinking and action -- the complement of the theory's claim about positive emotions."),

 dict(q="A researcher finds that participants induced to feel amused subsequently list more possible uses for an everyday object than participants induced to feel anxious. This result is most consistent with", choices=[
   "the facial-feedback hypothesis",
   "the claim that emotional expression is universal",
   "the operation of cultural display rules",
   "the broaden-and-build theory of emotion"
], ans=3,
   why="EK 4.7.A.2 applied: positive emotion broadening thought should yield a wider range of generated ideas, and negative emotion narrowing it should yield fewer. Nothing here concerns facial posture, cross-cultural recognition, or rules about display."),

 dict(q="Which set names the emotions the framework identifies as commonly experienced across cultures?", choices=[
   "guilt, disgust, sadness, happiness, surprise, fear",
   "anger, disgust, sadness, happiness, surprise, fear",
   "anger, pride, sadness, happiness, surprise, envy",
   "anger, disgust, sadness, gratitude, shame, fear"
], ans=1,
   why="EK 4.7.B.1 lists exactly these six. Pride, envy, gratitude, shame, and guilt are not on the framework's list, and each distractor substitutes one or more of them."),

 dict(q="What does the framework conclude about research on the universality of emotional expression?", choices=[
   "The research has established universality beyond dispute",
   "The research has shown that no expression is shared across cultures",
   "The question has not been investigated empirically",
   "The research shows mixed results"
], ans=3,
   why="EK 4.7.B.1 states that research on the universality of emotions shows MIXED results. Both absolute readings -- fully universal, or not shared at all -- overstate what the framework claims."),

 dict(q="Display rules are best defined as", choices=[
   "the facial muscles involved in producing an expression",
   "culturally learned norms governing when and how an emotion may be shown",
   "the physiological changes that accompany an emotion",
   "the events that reliably trigger a particular emotion"
], ans=1,
   why="EK 4.7.B.2: display rules regulate how people can display and interpret emotions, and they differ among cultures. Note the option about triggering events describes ELICITORS, the other construct named in the same statement."),

 dict(q="Elicitors, as distinguished from display rules, are", choices=[
   "the situations or events that bring about a particular emotion",
   "the norms governing whether an emotion may be shown",
   "the words a culture uses to name an emotion",
   "the physiological signature of a particular emotion"], ans=0,
   why="EK 4.7.B.2 names display rules AND elicitors as both differing among cultures. An elicitor causes the emotion; a display rule governs its expression -- the pair most often collapsed into one idea."),

 dict(q="A traveler notices that colleagues in one country routinely suppress visible frustration in meetings, while in another the same frustration is expressed openly, even though both groups report feeling equally frustrated. This difference is best explained by", choices=[
   "a difference in which emotions the two groups are capable of feeling",
   "the broaden-and-build theory of emotion",
   "differing display rules",
   "differing elicitors"
], ans=2,
   why="EK 4.7.B.2. The stem holds the FELT emotion constant and varies only its outward expression, which isolates display rules; if the two groups had been frustrated by different events, that would implicate elicitors instead."),

 dict(q="An event treated as a serious insult in one culture and as harmless teasing in another produces anger in the first and amusement in the second. This difference is best explained by", choices=[
   "differing display rules",
   "differing facial musculature",
   "differing levels of physiological arousal capacity",
   "differing elicitors"
], ans=3,
   why="EK 4.7.B.2. Here the same event causes DIFFERENT emotions, which is an elicitor difference; a display-rule difference would show the same emotion expressed differently."),

 dict(q="The framework notes that display rules and elicitors can also vary WITHIN a single culture according to", choices=[
   "the season of the year",
   "a person's dominant hand",
   "a person's gender, age, or socioeconomic class",
   "a person's blood type"
], ans=2,
   why="EK 4.7.B.2 states that display rules and elicitors may regulate how people from different genders, ages, or socioeconomic classes WITHIN a culture display and interpret emotions."),

 dict(q="Why does the existence of display rules complicate research on whether emotional expression is universal?", choices=[
   "Display rules make it impossible to photograph facial expressions",
   "Display rules mean that people in every culture feel entirely different emotions",
   "Display rules apply only to researchers, not to participants",
   "What a researcher observes is expression, which is shaped by rules, rather than the felt emotion itself"
], ans=3,
   why="EK 4.7.B.1 and 4.7.B.2 together: the measured variable is outward expression, which display rules regulate, so a cross-cultural difference in expression is ambiguous between a difference in feeling and a difference in permitted display. That ambiguity is part of why EK 4.7.B.1 reports mixed results."),

 dict(q="Someone argues that emotion is simply a form of reasoning about a situation. The framework's own description of emotion contradicts this because emotion is described as", choices=[
   "identical to reasoning but faster",
   "a process that occurs only in the absence of reasoning",
   "a process with no cognitive component whatsoever",
   "a process distinguished from reasoning or knowledge"
], ans=3,
   why="EK 4.7.A.1 explicitly distinguishes emotion from reasoning or knowledge. Note the framework does NOT say emotion lacks a cognitive component -- one position it records makes a cognitive label essential -- so the strongest-sounding denial is wrong."),

 dict(q="A person who is told a stranger's frown means disapproval reports feeling anxious, while another told the same frown reflects concentration reports feeling nothing. This best supports the position that", choices=[
   "display rules determine how the observers may show emotion",
   "interpretation of the situation shapes which emotion is experienced",
   "the physiological response alone determines the emotion",
   "emotional expression is universal across all contexts"
], ans=1,
   why="EK 4.7.A.1's cognitive-label position: the stimulus is held constant and only the interpretation varies, yet the emotion differs -- which is what a purely physiological account cannot deliver."),

 dict(q="Which pairing of emotional phenomenon and its level of description is correct?", choices=[
   "elicitor -- the event that causes the emotion; display rule -- the norm governing its expression",
   "elicitor -- the norm governing expression; display rule -- the event that causes the emotion",
   "elicitor -- a facial muscle movement; display rule -- a physiological change",
   "elicitor -- a cultural stereotype; display rule -- an unconscious defense"], ans=0,
   why="EK 4.7.B.2 names both. Cause versus permitted expression is the whole distinction, and the reversed pairing is the standard trap."),

 dict(q="An emotion researcher wants to know whether adopting a smiling facial posture changes reported amusement. The strongest design would be to", choices=[
   "ask participants to recall a time they smiled and report how amused they felt",
   "compare amusement ratings of people who smile often with those who smile rarely",
   "show cartoons to participants and record how often each one smiles",
   "randomly assign participants to hold either a smiling or a neutral facial posture while rating identical cartoons"
], ans=3,
   why="Research-methods item (Science Practice 2.B). Facial posture is the variable of interest, so it must be MANIPULATED and randomly assigned, with the stimulus held identical. The last option reverses cause and effect by measuring smiling as an outcome."),

 dict(q="A study measures emotion using only participants' self-reported ratings. The clearest limitation of this approach is that", choices=[
   "self-reports cannot be converted into numbers for analysis",
   "self-reports can only be collected from one participant at a time",
   "self-reports are unaffected by cultural norms",
   "reports may be shaped by what participants believe they are supposed to feel or show"
], ans=3,
   why="Research-methods item. Because EK 4.7.B.2's display rules govern how emotions are displayed and interpreted, a self-report is filtered through what a participant thinks is appropriate. The final option asserts the opposite of the framework's position."),

 dict(q="A researcher tests recognition of facial expressions using participants drawn only from university students in one country and concludes that recognition is universal. The central problem with this conclusion is that", choices=[
   "recognition accuracy cannot be measured numerically",
   "university students are incapable of recognizing emotions",
   "a single unrepresentative sample cannot support a claim about all cultures",
   "facial expressions cannot be photographed accurately"
], ans=2,
   why="Research-methods item (Science Practice 2.C). A universality claim is a claim about populations everywhere, and a sample from one country and one narrow demographic cannot license it -- a sampling limitation that is part of why EK 4.7.B.1 reports mixed results."),

 dict(q="Which finding, if obtained, would most directly WEAKEN the claim that emotional expression is universal?", choices=[
   "Members of a culture with no exposure to outside media reliably assign different emotions to the same expressions than other groups do",
   "People in several countries produce similar expressions when startled",
   "Infants across many cultures show similar expressions before learning language",
   "Blind and sighted athletes show similar expressions at the moment of winning"], ans=0,
   why="Argumentation item (Science Practice 4.B). Universality predicts convergent interpretation, so a culturally isolated group interpreting the same expressions differently is a direct counterexample. The other three findings all SUPPORT universality, which is what makes them wrong answers to a weakening question."),

 dict(q="Which finding would most directly SUPPORT the position that a cognitive label is required to experience a specific emotion?", choices=[
   "Participants can identify emotions in photographs at above-chance rates",
   "Participants given the same arousal-inducing drug report different emotions depending on how the situation is described to them",
   "Participants report stronger emotion when arousal is more intense",
   "Participants show the same facial expression whenever heart rate rises"
], ans=1,
   why="Argumentation item (Science Practice 4.B). Holding the physiological state constant while varying only the available interpretation, and finding the reported emotion changes, is the design that isolates the labelling claim in EK 4.7.A.1."),

 dict(q="A student claims that because two people show the same expression, they must be feeling the same emotion. The best objection is that", choices=[
   "only trained clinicians can experience emotions",
   "emotions have no external component at all",
   "expression is regulated by display rules, so the same outward expression can accompany different internal states",
   "expressions are never related to internal states in any way"
], ans=2,
   why="EK 4.7.B.2 makes expression a regulated output rather than a transparent window on feeling. The strong denial that expression relates to feeling at all overshoots -- EK 4.7.A.1's facial-feedback material assumes a relationship exists."),

 dict(q="A person receives unexpected good news, and over the following weeks notices herself taking up new hobbies and reaching out to people she had lost touch with. This pattern is best described by", choices=[
   "an elicitor unique to her culture",
   "the broaden-and-build theory of emotion",
   "the facial-feedback hypothesis",
   "a cultural display rule"
], ans=1,
   why="EK 4.7.A.2. Positive emotion broadening awareness and encouraging new actions and thoughts is precisely the widening of activity and contact described; the theory's 'build' component is this accumulation of new pursuits and relationships."),

 dict(q="Which statement about emotion is most consistent with the AP Psychology framework as a whole?", choices=[
   "Emotional expression shows both cross-cultural commonalities and culturally specific regulation, and the research is not settled",
   "Emotional expression is entirely universal and unaffected by culture",
   "Emotional expression is entirely cultural and shows no commonalities",
   "Emotional expression has been shown to be unrelated to internal states"], ans=0,
   why="EK 4.7.B.1 names six emotions commonly experienced across cultures while reporting mixed results, and EK 4.7.B.2 adds culturally varying display rules and elicitors. The framework's position is deliberately the qualified one, and both absolute alternatives misrepresent it."),
]
