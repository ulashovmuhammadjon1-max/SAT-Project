# AP PSYCH 4.1 Attribution Theory and Person Perception — 30 questions
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
   "an unconscious conflict formed in early childhood",
   "the reinforcement schedule that maintained the behavior"
], ans=0,
   why="Dispositional attributions locate the cause in internal qualities of the person; situational attributions locate it in external circumstances."),

 dict(q="A driver is cut off in traffic and immediately concludes that the other driver is a selfish person. This explanation is best classified as", choices=[
   "an upward social comparison",
   "a dispositional attribution",
   "a situational attribution",
   "an example of the mere exposure effect"
], ans=1,
   why="Attributing the behavior to the other driver's character rather than to traffic conditions is an appeal to an internal quality."),

 dict(q="A manager notices that an employee arrived late and thinks, 'The commuter train was delayed again this morning.' The manager has made", choices=[
   "a situational attribution",
   "a dispositional attribution",
   "a self-serving bias",
   "a downward social comparison"
], ans=0,
   why="The cause named is an external circumstance the employee did not control, which is what makes an attribution situational."),

 dict(q="The fundamental attribution error is the tendency to", choices=[
   "credit one's own successes to ability and one's own failures to circumstance",
   "assume that other people share one's own opinions more than they actually do",
   "overweight dispositional causes and underweight situational causes when explaining another person's behavior",
   "overweight situational causes when explaining another person's behavior"
], ans=2,
   why="The error is specifically about explaining OTHERS: dispositional causes are overestimated and the power of the situation is underestimated."),

 dict(q="Observers watch a volunteer read aloud an essay defending a position that the volunteer was ASSIGNED to defend by a coin flip. Observers still rate the volunteer as personally holding that position. This result illustrates", choices=[
   "the fundamental attribution error",
   "the self-serving bias",
   "belief perseverance about the coin flip",
   "the false consensus effect"
], ans=0,
   why="Observers discount an obvious situational cause -- the assignment -- and infer a matching disposition, which is the classic demonstration of the error."),

 dict(q="The self-serving bias is the tendency to attribute", choices=[
   "other people's behavior to their dispositions and one's own to the situation",
   "all outcomes, good and bad, to stable personal traits",
   "one's own successes to internal causes and one's own failures to external causes",
   "one's own successes to external causes and one's own failures to internal causes"
], ans=2,
   why="The self-serving bias is valence-dependent and self-directed: credit for good outcomes, deflection of blame for bad ones."),

 dict(q="After earning a high score, a student says, 'I have always been strong at this subject.' After a low score on the next exam the same student says, 'That test was written unfairly.' This pair of explanations demonstrates", choices=[
   "the self-serving bias",
   "the fundamental attribution error",
   "an external locus of control",
   "a pessimistic explanatory style"
], ans=0,
   why="Both explanations concern the student's OWN outcomes and flip with the valence of the outcome, which is the defining signature of the self-serving bias."),

 dict(q="The actor/observer bias refers to the asymmetry in which people explain", choices=[
   "the behavior of in-group members more harshly than that of out-group members",
   "their own behavior situationally but the same behavior in others dispositionally",
   "their own behavior dispositionally but the same behavior in others situationally",
   "good outcomes internally and bad outcomes externally, regardless of who acted"
], ans=1,
   why="The actor/observer bias is a contrast between perspectives: as actor one sees the situation, as observer one sees the person."),

 dict(q="A commuter who is short with a cashier thinks, 'I have had an exhausting day,' but when the next customer is short with the same cashier the commuter thinks, 'Some people are just rude.' This is best described as", choices=[
   "a self-fulfilling prophecy",
   "an optimistic explanatory style",
   "the actor/observer bias",
   "the self-serving bias"
], ans=2,
   why="The same behavior is explained situationally for the self and dispositionally for another person, which is the actor/observer asymmetry rather than a bias about success and failure."),

 dict(q="Which feature most clearly separates the self-serving bias from the fundamental attribution error?", choices=[
   "The self-serving bias occurs only in collectivist cultures",
   "The self-serving bias concerns explanations of one's own outcomes and shifts with whether the outcome was good or bad",
   "The self-serving bias applies only to strangers, whereas the other applies only to friends",
   "The self-serving bias always produces situational explanations and the other always produces dispositional ones"
], ans=1,
   why="The fundamental attribution error is about explaining ANOTHER person and does not depend on outcome valence; the self-serving bias is about the self and reverses direction with valence."),

 dict(q="A supervisor explains a subordinate's missed deadline by saying the subordinate is disorganized, without considering that the subordinate was given three competing assignments that week. The supervisor's reasoning most directly reflects", choices=[
   "an expectation that causes the subordinate to become disorganized",
   "underestimating the power of the situation when judging another person",
   "protecting the supervisor's own self-esteem after a poor outcome",
   "assuming most other supervisors would agree with this judgment"
], ans=1,
   why="Nothing about the supervisor's own outcome is at stake, so this is the dispositional overweighting of the fundamental attribution error rather than a self-serving bias."),

 dict(q="Explanatory style, as used in attribution research, refers to", choices=[
   "the cultural display rules governing how emotions are shown",
   "a person's habitual pattern of explaining good and bad events",
   "the vocabulary a therapist uses when delivering a diagnosis",
   "the degree to which a person's speech is organized and coherent"
], ans=1,
   why="Explanatory style is defined as the predictable pattern of attributions a person makes for events in their own life and others' lives; it can be optimistic or pessimistic."),

 dict(q="Following one rejected job application, an applicant concludes, 'I am not good at anything, and this will keep happening everywhere I apply.' This explanation is characteristic of", choices=[
   "an internal locus of control",
   "downward social comparison",
   "a pessimistic explanatory style",
   "an optimistic explanatory style"
], ans=2,
   why="A pessimistic explanatory style explains a bad event with causes treated as broad and enduring rather than specific and temporary."),

 dict(q="An athlete who loses one match says, 'That opponent's style was a bad matchup for me today, and the next tournament will be different.' The athlete is showing", choices=[
   "the fundamental attribution error",
   "an external locus of control",
   "an optimistic explanatory style",
   "a pessimistic explanatory style"
], ans=2,
   why="An optimistic explanatory style treats the cause of a bad event as specific to the occasion and temporary rather than global and permanent."),

 dict(q="A person with an internal locus of control most strongly believes that", choices=[
   "outcomes in life are largely determined by one's own effort and choices",
   "outcomes in life are largely determined by luck, fate, or powerful others",
   "one's personality is fixed at birth and cannot be changed",
   "other people are generally more competent than oneself"
], ans=0,
   why="Locus of control is a generalized belief about the source of control over one's outcomes; an internal locus places that source in the self."),

 dict(q="A patient who says, 'There is no point following the exercise plan, because whether I stay healthy is mostly a matter of luck,' is expressing", choices=[
   "the actor/observer bias",
   "an external locus of control",
   "an internal locus of control",
   "an emotion-focused coping strategy"
], ans=1,
   why="Attributing one's outcomes generally to luck rather than to one's own action is the defining belief of an external locus of control."),

 dict(q="How does locus of control differ from an attribution?", choices=[
   "Locus of control changes moment to moment, while attributions are stable across the lifespan",
   "Locus of control is a symptom of a disorder, while an attribution is a normal process",
   "Locus of control is a generalized belief about control over one's outcomes, while an attribution is an explanation offered for a particular event",
   "Locus of control applies only to other people, while an attribution applies only to the self"
], ans=2,
   why="An attribution is event-specific; locus of control is the broader, more stable expectancy a person carries across situations."),

 dict(q="The mere exposure effect predicts that repeated encounters with a stimulus will", choices=[
   "increase liking for that stimulus",
   "decrease liking for that stimulus through habituation",
   "improve recall of the stimulus without changing liking",
   "have no reliable effect once the stimulus is recognized"
], ans=0,
   why="The mere exposure effect is defined as increased liking produced by repeated exposure to a stimulus over time."),

 dict(q="A song a listener disliked on first hearing becomes a favorite after it plays repeatedly on the radio for several weeks. This change is best explained by", choices=[
   "the mere exposure effect",
   "classical conditioning of the song to a reward",
   "cognitive dissonance reduction",
   "a self-fulfilling prophecy about the song"
], ans=0,
   why="Liking rose with repetition alone, with no pairing, no inconsistency to resolve and no comparison to others."),

 dict(q="A self-fulfilling prophecy occurs when", choices=[
   "a person's expectation prompts behavior that draws out the very response expected",
   "a person remembers only the evidence that fits an existing belief",
   "a person's mood matches the emotional tone of the surrounding group",
   "a prediction turns out to be accurate purely by coincidence"
], ans=0,
   why="The mechanism is behavioral: the perceiver acts on the expectation, and that action elicits the confirming behavior from the target."),

 dict(q="A teacher told that certain randomly chosen students are 'late bloomers' gives those students more encouragement and challenging work, and by year's end their performance has risen. This outcome best illustrates", choices=[
   "an internal locus of control in the students",
   "a self-fulfilling prophecy",
   "the mere exposure effect",
   "regression toward the mean in test scores"
], ans=1,
   why="The expectation was groundless, but the teacher's changed behavior produced the very improvement expected, which is the defining sequence of a self-fulfilling prophecy."),

 dict(q="Social comparison, as a form of person perception, is the process of", choices=[
   "recalling one's own past performance more favorably than it was",
   "evaluating oneself by measuring one's standing against other people",
   "adjusting one's public behavior to match a group's norms",
   "predicting how another person will behave in an unfamiliar setting"
], ans=1,
   why="Social comparison is defined as self-evaluation carried out relative to other members of one's society or social circle."),

 dict(q="A new violinist who deliberately sits beside the section's strongest player in order to learn from her is engaging in", choices=[
   "downward social comparison",
   "relative deprivation",
   "the self-serving bias",
   "upward social comparison"
], ans=3,
   why="Comparison with someone judged better than oneself is upward; comparison with someone judged worse is downward."),

 dict(q="An employee is satisfied with a raise until learning that colleagues doing similar work received larger raises, after which the same raise feels inadequate. This shift illustrates", choices=[
   "an internal locus of control",
   "relative deprivation",
   "the mere exposure effect",
   "the fundamental attribution error"
], ans=1,
   why="Relative deprivation is a judgment of one's own deprivation made by reference to others rather than by an absolute standard; the raise itself never changed."),

 dict(q="Researchers randomly assign participants either to read that a speaker freely chose a position or to read that the speaker was assigned it, then measure how strongly participants believe the speaker holds that position. In this experiment, the independent variable is", choices=[
   "the random assignment of participants to conditions",
   "the number of participants in each condition",
   "whether the speaker's position was described as chosen or assigned",
   "how strongly participants believe the speaker holds the position"
], ans=2,
   why="The independent variable is the condition the experimenters manipulated; participants' rated belief about the speaker is the dependent variable, and random assignment is a design procedure rather than a variable."),

 dict(q="A patient recovering from surgery deliberately reads about others whose recovery has been slower than her own, and afterward feels more optimistic. This strategy is", choices=[
   "relative deprivation",
   "a pessimistic explanatory style",
   "downward social comparison",
   "upward social comparison"
], ans=2,
   why="EK 4.1.C.3 states social comparison can be upward or downward; comparing oneself with someone judged worse off is downward, and it tends to raise rather than lower subjective standing."),

 dict(q="Cross-cultural research finds that people raised in cultures emphasizing group obligation more often explain a stranger's behavior by pointing to the situation than do people raised in cultures emphasizing individual achievement. This finding suggests that the fundamental attribution error is", choices=[
   "shaped by cultural norms rather than fixed in every population",
   "entirely absent outside individualist cultures",
   "a purely biological reflex unaffected by upbringing",
   "the same thing as an external locus of control"], ans=0,
   why="Science Practice 1.B asks how cultural norms apply to behavior and mental processes. A difference in degree across cultures shows cultural shaping; it does not show total absence, and a group tendency in attribution is not the same construct as an individual's generalized locus of control."),

 dict(q="A coach and a player watch the same missed shot. Which pair of explanations best matches what the actor/observer bias predicts each will give?", choices=[
   "both cite the wet court, because the cause is obvious to everyone present",
   "both cite the player's concentration, because the player performed the action",
   "the player cites the wet court; the coach cites the player's concentration",
   "the player cites his own concentration; the coach cites the wet court"
], ans=2,
   why="EK 4.1.A.3. The actor sees the situation acting on him and the observer sees the actor, so the prediction is situational from the player and dispositional from the coach; the reversed pairing is the standard trap."),

 dict(q="In a survey of 400 employees, those scoring higher on a measure of internal locus of control also reported higher job satisfaction. A researcher concludes that an internal locus of control causes job satisfaction. This conclusion is unjustified because", choices=[
   "locus of control cannot be measured with a questionnaire",
   "job satisfaction is not a psychological variable",
   "no variable was manipulated, so the direction of the relationship cannot be established",
   "the sample of 400 employees is too small for any conclusion"
], ans=2,
   why="Research-methods item (Science Practice 2.C). Both variables were measured rather than manipulated, so satisfaction could just as well foster an internal orientation, or a third variable could produce both."),

 dict(q="Asked to explain a coworker's promotion, an employee first says the coworker 'just knows the right people.' Asked to explain her own promotion the following year, she says it reflected her sustained effort. Which two biases together best account for this pair of explanations?", choices=[
   "the self-serving bias for her own promotion and a dispositional discounting of the coworker's",
   "the mere exposure effect and relative deprivation",
   "belief perseverance and an external locus of control",
   "a self-fulfilling prophecy and social comparison"], ans=0,
   why="Her own good outcome is credited internally, which is the self-serving bias, while the coworker's good outcome is credited to circumstance -- the mirror image of the fundamental attribution error, which appears when the other person's outcome is favorable and the perceiver's standing is at stake."),
]
