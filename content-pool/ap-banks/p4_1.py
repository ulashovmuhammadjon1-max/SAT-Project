# AP PSYCH 4.1 Attribution Theory and Person Perception — 25 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, pp. 96-97.
# EK 4.1.A.1 dispositional/situational attribution; 4.1.A.2 explanatory style;
# 4.1.A.3 actor/observer bias, fundamental attribution error, self-serving bias;
# LO 4.1.B locus of control; 4.1.C.1 mere exposure effect;
# 4.1.C.2 self-fulfilling prophecy; 4.1.C.3 social comparison, relative deprivation.
# No sympy: every key's claim is stated item by item in verify_p4_1.py.
TOPIC = ("4.1", "Attribution Theory and Person Perception", 4)
QUESTIONS = [
 dict(q="In attribution theory, a dispositional attribution explains a behavior by pointing to", choices=[
   "a quality internal to the person, such as personality or ability",
   "the circumstances surrounding the person at the time",
   "the statistical base rate of the behavior in the population",
   "an unconscious conflict formed in early childhood",
   "the reinforcement schedule that maintained the behavior"], ans=0,
   why="Dispositional attributions locate the cause in internal qualities of the person; situational attributions locate it in external circumstances."),

 dict(q="A driver is cut off in traffic and immediately concludes that the other driver is a selfish person. This explanation is best classified as", choices=[
   "a dispositional attribution",
   "a situational attribution",
   "an example of the mere exposure effect",
   "an upward social comparison",
   "an instance of relative deprivation"], ans=0,
   why="Attributing the behavior to the other driver's character rather than to traffic conditions is an appeal to an internal quality."),

 dict(q="A manager notices that an employee arrived late and thinks, 'The commuter train was delayed again this morning.' The manager has made", choices=[
   "a situational attribution",
   "a dispositional attribution",
   "a self-serving bias",
   "a downward social comparison",
   "an implicit personality judgment about competence"], ans=0,
   why="The cause named is an external circumstance the employee did not control, which is what makes an attribution situational."),

 dict(q="The fundamental attribution error is the tendency to", choices=[
   "overweight dispositional causes and underweight situational causes when explaining another person's behavior",
   "overweight situational causes when explaining another person's behavior",
   "credit one's own successes to ability and one's own failures to circumstance",
   "assume that other people share one's own opinions more than they actually do",
   "judge a group as more uniform than it really is"], ans=0,
   why="The error is specifically about explaining OTHERS: dispositional causes are overestimated and the power of the situation is underestimated."),

 dict(q="Observers watch a volunteer read aloud an essay defending a position that the volunteer was ASSIGNED to defend by a coin flip. Observers still rate the volunteer as personally holding that position. This result illustrates", choices=[
   "the fundamental attribution error",
   "the self-serving bias",
   "belief perseverance about the coin flip",
   "the false consensus effect",
   "downward social comparison"], ans=0,
   why="Observers discount an obvious situational cause -- the assignment -- and infer a matching disposition, which is the classic demonstration of the error."),

 dict(q="The self-serving bias is the tendency to attribute", choices=[
   "one's own successes to internal causes and one's own failures to external causes",
   "one's own successes to external causes and one's own failures to internal causes",
   "other people's behavior to their dispositions and one's own to the situation",
   "all outcomes, good and bad, to stable personal traits",
   "group outcomes to the group's least competent member"], ans=0,
   why="The self-serving bias is valence-dependent and self-directed: credit for good outcomes, deflection of blame for bad ones."),

 dict(q="After earning a high score, a student says, 'I have always been strong at this subject.' After a low score on the next exam the same student says, 'That test was written unfairly.' This pair of explanations demonstrates", choices=[
   "the self-serving bias",
   "the fundamental attribution error",
   "an external locus of control",
   "a pessimistic explanatory style",
   "the just-world phenomenon"], ans=0,
   why="Both explanations concern the student's OWN outcomes and flip with the valence of the outcome, which is the defining signature of the self-serving bias."),

 dict(q="The actor/observer bias refers to the asymmetry in which people explain", choices=[
   "their own behavior situationally but the same behavior in others dispositionally",
   "their own behavior dispositionally but the same behavior in others situationally",
   "good outcomes internally and bad outcomes externally, regardless of who acted",
   "the behavior of in-group members more harshly than that of out-group members",
   "unfamiliar behavior as more common than it actually is"], ans=0,
   why="The actor/observer bias is a contrast between perspectives: as actor one sees the situation, as observer one sees the person."),

 dict(q="A commuter who is short with a cashier thinks, 'I have had an exhausting day,' but when the next customer is short with the same cashier the commuter thinks, 'Some people are just rude.' This is best described as", choices=[
   "the actor/observer bias",
   "the self-serving bias",
   "the mere exposure effect",
   "a self-fulfilling prophecy",
   "an optimistic explanatory style"], ans=0,
   why="The same behavior is explained situationally for the self and dispositionally for another person, which is the actor/observer asymmetry rather than a bias about success and failure."),

 dict(q="Which feature most clearly separates the self-serving bias from the fundamental attribution error?", choices=[
   "The self-serving bias concerns explanations of one's own outcomes and shifts with whether the outcome was good or bad",
   "The self-serving bias applies only to strangers, whereas the other applies only to friends",
   "The self-serving bias always produces situational explanations and the other always produces dispositional ones",
   "The self-serving bias is a perceptual effect, whereas the other is a memory effect",
   "The self-serving bias occurs only in collectivist cultures"], ans=0,
   why="The fundamental attribution error is about explaining ANOTHER person and does not depend on outcome valence; the self-serving bias is about the self and reverses direction with valence."),

 dict(q="A supervisor explains a subordinate's missed deadline by saying the subordinate is disorganized, without considering that the subordinate was given three competing assignments that week. The supervisor's reasoning most directly reflects", choices=[
   "underestimating the power of the situation when judging another person",
   "protecting the supervisor's own self-esteem after a poor outcome",
   "assuming most other supervisors would agree with this judgment",
   "a repeated-exposure increase in liking for the subordinate",
   "an expectation that causes the subordinate to become disorganized"], ans=0,
   why="Nothing about the supervisor's own outcome is at stake, so this is the dispositional overweighting of the fundamental attribution error rather than a self-serving bias."),

 dict(q="Explanatory style, as used in attribution research, refers to", choices=[
   "a person's habitual pattern of explaining good and bad events",
   "the vocabulary a therapist uses when delivering a diagnosis",
   "the order in which a person reports the causes of an event",
   "the degree to which a person's speech is organized and coherent",
   "the cultural display rules governing how emotions are shown"], ans=0,
   why="Explanatory style is defined as the predictable pattern of attributions a person makes for events in their own life and others' lives; it can be optimistic or pessimistic."),

 dict(q="Following one rejected job application, an applicant concludes, 'I am not good at anything, and this will keep happening everywhere I apply.' This explanation is characteristic of", choices=[
   "a pessimistic explanatory style",
   "an optimistic explanatory style",
   "an internal locus of control",
   "the false consensus effect",
   "downward social comparison"], ans=0,
   why="A pessimistic explanatory style explains a bad event with causes treated as broad and enduring rather than specific and temporary."),

 dict(q="An athlete who loses one match says, 'That opponent's style was a bad matchup for me today, and the next tournament will be different.' The athlete is showing", choices=[
   "an optimistic explanatory style",
   "a pessimistic explanatory style",
   "the fundamental attribution error",
   "an external locus of control",
   "reaction formation against the loss"], ans=0,
   why="An optimistic explanatory style treats the cause of a bad event as specific to the occasion and temporary rather than global and permanent."),

 dict(q="A person with an internal locus of control most strongly believes that", choices=[
   "outcomes in life are largely determined by one's own effort and choices",
   "outcomes in life are largely determined by luck, fate, or powerful others",
   "one's personality is fixed at birth and cannot be changed",
   "other people are generally more competent than oneself",
   "emotions must be concealed in public settings"], ans=0,
   why="Locus of control is a generalized belief about the source of control over one's outcomes; an internal locus places that source in the self."),

 dict(q="A patient who says, 'There is no point following the exercise plan, because whether I stay healthy is mostly a matter of luck,' is expressing", choices=[
   "an external locus of control",
   "an internal locus of control",
   "an emotion-focused coping strategy",
   "the actor/observer bias",
   "a downward social comparison"], ans=0,
   why="Attributing one's outcomes generally to luck rather than to one's own action is the defining belief of an external locus of control."),

 dict(q="How does locus of control differ from an attribution?", choices=[
   "Locus of control is a generalized belief about control over one's outcomes, while an attribution is an explanation offered for a particular event",
   "Locus of control applies only to other people, while an attribution applies only to the self",
   "Locus of control is measured physiologically, while attributions are measured only by interview",
   "Locus of control changes moment to moment, while attributions are stable across the lifespan",
   "Locus of control is a symptom of a disorder, while an attribution is a normal process"], ans=0,
   why="An attribution is event-specific; locus of control is the broader, more stable expectancy a person carries across situations."),

 dict(q="The mere exposure effect predicts that repeated encounters with a stimulus will", choices=[
   "increase liking for that stimulus",
   "decrease liking for that stimulus through habituation",
   "improve recall of the stimulus without changing liking",
   "make the stimulus seem more threatening over time",
   "have no reliable effect once the stimulus is recognized"], ans=0,
   why="The mere exposure effect is defined as increased liking produced by repeated exposure to a stimulus over time."),

 dict(q="A song a listener disliked on first hearing becomes a favorite after it plays repeatedly on the radio for several weeks. This change is best explained by", choices=[
   "the mere exposure effect",
   "classical conditioning of the song to a reward",
   "cognitive dissonance reduction",
   "an upward social comparison with other listeners",
   "a self-fulfilling prophecy about the song"], ans=0,
   why="Liking rose with repetition alone, with no pairing, no inconsistency to resolve and no comparison to others."),

 dict(q="A self-fulfilling prophecy occurs when", choices=[
   "a person's expectation prompts behavior that draws out the very response expected",
   "a person remembers only the evidence that fits an existing belief",
   "a person's mood matches the emotional tone of the surrounding group",
   "a prediction turns out to be accurate purely by coincidence",
   "a person publicly states an intention and is then held to it"], ans=0,
   why="The mechanism is behavioral: the perceiver acts on the expectation, and that action elicits the confirming behavior from the target."),

 dict(q="A teacher told that certain randomly chosen students are 'late bloomers' gives those students more encouragement and challenging work, and by year's end their performance has risen. This outcome best illustrates", choices=[
   "a self-fulfilling prophecy",
   "the mere exposure effect",
   "regression toward the mean in test scores",
   "the false consensus effect",
   "an internal locus of control in the students"], ans=0,
   why="The expectation was groundless, but the teacher's changed behavior produced the very improvement expected, which is the defining sequence of a self-fulfilling prophecy."),

 dict(q="Social comparison, as a form of person perception, is the process of", choices=[
   "evaluating oneself by measuring one's standing against other people",
   "adjusting one's public behavior to match a group's norms",
   "predicting how another person will behave in an unfamiliar setting",
   "attributing a group's success to its individual members' traits",
   "recalling one's own past performance more favorably than it was"], ans=0,
   why="Social comparison is defined as self-evaluation carried out relative to other members of one's society or social circle."),

 dict(q="A new violinist who deliberately sits beside the section's strongest player in order to learn from her is engaging in", choices=[
   "upward social comparison",
   "downward social comparison",
   "relative deprivation",
   "the self-serving bias",
   "deindividuation within the section"], ans=0,
   why="Comparison with someone judged better than oneself is upward; comparison with someone judged worse is downward."),

 dict(q="An employee is satisfied with a raise until learning that colleagues doing similar work received larger raises, after which the same raise feels inadequate. This shift illustrates", choices=[
   "relative deprivation",
   "the mere exposure effect",
   "an optimistic explanatory style",
   "the fundamental attribution error",
   "an internal locus of control"], ans=0,
   why="Relative deprivation is a judgment of one's own deprivation made by reference to others rather than by an absolute standard; the raise itself never changed."),

 dict(q="Researchers randomly assign participants either to read that a speaker freely chose a position or to read that the speaker was assigned it, then measure how strongly participants believe the speaker holds that position. In this experiment, the independent variable is", choices=[
   "whether the speaker's position was described as chosen or assigned",
   "how strongly participants believe the speaker holds the position",
   "the content of the position the speaker defended",
   "the random assignment of participants to conditions",
   "the number of participants in each condition"], ans=0,
   why="The independent variable is the condition the experimenters manipulated; participants' rated belief about the speaker is the dependent variable, and random assignment is a design procedure rather than a variable."),
]
