# AP PSYCHOLOGY 3.7 Classical Conditioning — 30 questions
# CED effective Fall 2024/2025, Unit 3 Development and Learning.
# Learning objective 3.7.A.
#
# Essential knowledge relied on: 3.7.A.1 the behavioral perspective and its
# traditional focus on observable behavior to the exclusion of mental processes;
# 3.7.A.2 classical conditioning as associating one STIMULUS with another
# STIMULUS to elicit a response, with acquisition as the learning of that
# association; 3.7.A.2.i the UCS elicits the UCR, and that response becomes the
# CR when performed in response to the CS; 3.7.A.2.ii the ORDER of presentation
# of CS with UCS matters for acquisition; 3.7.A.2.iii extinction when the CS is
# no longer paired with the UCS, and spontaneous recovery when the CS is
# presented again after extinction; 3.7.A.2.iv stimulus discrimination and
# generalization; 3.7.A.2.v a CS used as a UCS in higher-order conditioning;
# 3.7.A.3 emotional responses can be classically conditioned, which grounds
# therapeutic interventions such as counterconditioning; 3.7.A.4 taste aversions,
# one-trial conditioning, and biological preparedness; 3.7.A.5 habituation.
#
# TWO EXCLUSION STATEMENTS respected, both in this topic:
#   * EK 3.7.A.2.v excludes DELAYED, TRACE, SIMULTANEOUS, and BACKWARD
#     conditioning. None of those four terms appears in this module.
#   * EK 3.7.A.3 excludes EXPECTANCY THEORY. It appears only in item 30, where
#     naming the excluded theory is the correct response.
# The framework still says the ORDER of CS and UCS matters (3.7.A.2.ii), so item
# 9 tests that principle WITHOUT using any of the four excluded procedure names.
#
# The four-component vocabulary -- UCS, UCR, CS, CR -- is the single most
# error-prone thing in Unit 3, and the framework's own sample multiple-choice
# question in the CED is a UCS/CS identification item. Items 3-8 therefore work
# the same scenario from every side, and each stem states which stimulus was
# effective BEFORE any pairing, since that is the fact that fixes every label.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p3_7.py.
TOPIC = ("3.7", "Classical Conditioning", 3)
QUESTIONS = [
 dict(q="Behaviorists have traditionally focused on", choices=[
   "observable behavior, to the exclusion of mental processes",
   "unconscious conflicts formed in early childhood",
   "the biological structures of the nervous system",
   "the ways people organize and interpret sensory information"], ans=0,
   why="EK 3.7.A.1 states that the behavioral perspective evolved from theories about learning via conditioning and that behaviorists have traditionally focused on observable behavior to the exclusion of mental processes."),
 dict(q="Classical conditioning focuses on the association of", choices=[
   "one stimulus with another stimulus, so that a response is elicited",
   "a behavior with a consequence that follows it",
   "a person's beliefs with their emotions",
   "a memory with the setting in which it was formed"], ans=0,
   why="EK 3.7.A.2 states that classical conditioning focuses on the association of one stimulus with another stimulus to elicit a response; associating a behavior with a consequence is operant conditioning in EK 3.8.A.1."),
 dict(q="An unconditioned stimulus is best defined as a stimulus that", choices=[
   "elicits a response without any prior learning",
   "elicits a response only after being paired with another stimulus",
   "produces no response of any kind",
   "follows a behavior and makes it more likely"], ans=0,
   why="EK 3.7.A.2.i states that the unconditioned stimulus elicits an unconditioned response, which means the response is already in place before any conditioning occurs."),
 dict(q="A conditioned stimulus is best defined as a stimulus that", choices=[
   "comes to elicit a response only after being paired with an unconditioned stimulus",
   "elicits a response without any prior learning",
   "is delivered after a behavior to change its frequency",
   "always produces a stronger response than the unconditioned stimulus"], ans=0,
   why="EK 3.7.A.2.i states that the unconditioned response becomes the conditioned response when it is performed in response to the conditioned stimulus, which means the CS acquires its power through pairing."),
 dict(q="A dog salivates when it is given food. After a bell is repeatedly rung just before the food arrives, the dog salivates to the bell alone. In this example the FOOD is the", choices=[
   "unconditioned stimulus (UCS)",
   "conditioned stimulus (CS)",
   "unconditioned response (UCR)",
   "conditioned response (CR)"], ans=0,
   why="EK 3.7.A.2.i: the food produced salivation before any pairing occurred, which makes it the unconditioned stimulus."),
 dict(q="In that same example, the BELL is the", choices=[
   "conditioned stimulus (CS)",
   "unconditioned stimulus (UCS)",
   "conditioned response (CR)",
   "unconditioned response (UCR)"], ans=0,
   why="EK 3.7.A.2.i: the bell produced no salivation until it was paired with the food, so it is the conditioned stimulus."),
 dict(q="In that same example, salivation to the FOOD is the", choices=[
   "unconditioned response (UCR)",
   "conditioned response (CR)",
   "unconditioned stimulus (UCS)",
   "conditioned stimulus (CS)"], ans=0,
   why="EK 3.7.A.2.i states that the unconditioned stimulus elicits an unconditioned response; salivation to food required no learning."),
 dict(q="In that same example, salivation to the BELL alone is the", choices=[
   "conditioned response (CR)",
   "unconditioned response (UCR)",
   "conditioned stimulus (CS)",
   "unconditioned stimulus (UCS)"], ans=0,
   why="EK 3.7.A.2.i states that the unconditioned response becomes the conditioned response when it is performed in response to the conditioned stimulus, which is exactly salivation to the bell."),
 dict(q="According to the AP Psychology framework, what determines whether acquisition is successful?", choices=[
   "the order in which the conditioned stimulus and the unconditioned stimulus are presented",
   "the loudness of the conditioned stimulus",
   "whether the learner can describe the association in words",
   "how many other learners are present during training"], ans=0,
   why="EK 3.7.A.2.ii states that the order of presentation of the CS with the UCS is important to successful acquisition."),
 dict(q="Acquisition, in classical conditioning, refers to", choices=[
   "the learning of the association between the two stimuli",
   "the disappearance of a conditioned response",
   "the reappearance of a response after a rest period",
   "responding to stimuli similar to the conditioned stimulus"], ans=0,
   why="EK 3.7.A.2 identifies acquisition as learning the association; the distractors name extinction, spontaneous recovery, and generalization from the following EKs."),
 dict(q="Extinction of a conditioned response occurs when", choices=[
   "the conditioned stimulus is presented repeatedly without the unconditioned stimulus",
   "the unconditioned stimulus is presented repeatedly without the conditioned stimulus",
   "a new conditioned stimulus is introduced",
   "the learner is punished for responding"], ans=0,
   why="EK 3.7.A.2.iii states that a CR can become extinct when the CS is no longer paired with the UCS."),
 dict(q="Spontaneous recovery occurs when", choices=[
   "a previously extinguished conditioned response reappears after the conditioned stimulus is presented again following extinction",
   "a conditioned response is acquired in a single pairing",
   "a response spreads to stimuli that resemble the conditioned stimulus",
   "an organism stops responding to a repeated stimulus"], ans=0,
   why="EK 3.7.A.2.iii states that a formerly extinct CR can be spontaneously recovered when the CS is again presented after extinction."),
 dict(q="A dog conditioned to salivate to a bell stops salivating after the bell is rung many times with no food. Two days later the bell is rung and the dog salivates again. The reappearance is", choices=[
   "spontaneous recovery",
   "a second acquisition",
   "stimulus generalization",
   "habituation"], ans=0,
   why="EK 3.7.A.2.iii's spontaneous recovery is precisely the return of an extinguished CR when the CS is presented again after extinction, with no new pairings required."),
 dict(q="Stimulus generalization occurs when", choices=[
   "a response is elicited by stimuli similar to the conditioned stimulus",
   "a response occurs to the conditioned stimulus but not to similar stimuli",
   "a response weakens because the pairing has stopped",
   "an unrelated behavior is strengthened by chance"], ans=0,
   why="EK 3.7.A.2.iv states that stimulus discrimination and generalization have been demonstrated in studies of classical conditioning; generalization is the spread of the response to similar stimuli."),
 dict(q="Stimulus discrimination occurs when", choices=[
   "a response occurs to the conditioned stimulus but not to other similar stimuli",
   "a response spreads to stimuli that resemble the conditioned stimulus",
   "a response disappears after repeated unpaired presentations",
   "a response returns after a rest period"], ans=0,
   why="EK 3.7.A.2.iv names discrimination alongside generalization; discrimination is responding selectively to the trained stimulus and not to similar ones."),
 dict(q="A child conditioned to fear a white rat also becomes afraid of a white rabbit and a cotton ball. This best illustrates", choices=[
   "stimulus generalization",
   "stimulus discrimination",
   "extinction",
   "higher-order conditioning"], ans=0,
   why="EK 3.7.A.2.iv's generalization is the spread of a conditioned response to similar stimuli, which is what fear spreading across similar white furry objects demonstrates."),
 dict(q="A dog salivates to a bell of one particular pitch but not to bells of other pitches. This best illustrates", choices=[
   "stimulus discrimination",
   "stimulus generalization",
   "spontaneous recovery",
   "habituation"], ans=0,
   why="EK 3.7.A.2.iv's discrimination is responding to the conditioned stimulus and not to similar ones, which is what selective responding by pitch demonstrates."),
 dict(q="Higher-order conditioning occurs when", choices=[
   "an established conditioned stimulus is used as an unconditioned stimulus to condition a new stimulus",
   "two unconditioned stimuli are paired with each other",
   "a conditioned response grows stronger with each pairing",
   "an organism learns a behavior by watching another organism"], ans=0,
   why="EK 3.7.A.2.v states that a CS can be used as a UCS in higher-order conditioning."),
 dict(q="A dog is conditioned to salivate to a bell. A black square is then repeatedly presented just before the bell, until the square alone produces salivation. This procedure illustrates", choices=[
   "higher-order conditioning",
   "spontaneous recovery",
   "stimulus discrimination",
   "biological preparedness"], ans=0,
   why="EK 3.7.A.2.v's higher-order conditioning is exactly this: the bell, already an established CS, now serves as the UCS for conditioning the square."),
 dict(q="What does the AP Psychology framework say can be classically conditioned, forming the basis for several therapeutic interventions?", choices=[
   "emotional responses",
   "language rules",
   "measures of intelligence",
   "the stages of sleep"], ans=0,
   why="EK 3.7.A.3 states that research has demonstrated that emotional responses can be classically conditioned, and that these findings form the basis of therapeutic interventions for many mental disorders."),
 dict(q="Counterconditioning is cited in the AP Psychology framework as", choices=[
   "a therapeutic intervention grounded in the classical conditioning of emotional responses",
   "a schedule on which reinforcement is delivered",
   "a failure of a conditioned response to generalize",
   "a technique for measuring the strength of an attachment"], ans=0,
   why="EK 3.7.A.3 names counterconditioning as an example of the therapeutic interventions that the classical conditioning of emotional responses makes possible."),
 dict(q="One-trial learning, as demonstrated in research on taste aversions, occurs when", choices=[
   "the association is acquired through a single pairing and is not strengthened by further pairings",
   "a response is acquired only after many repeated pairings",
   "a learner acquires a behavior by watching one other person",
   "a conditioned response is extinguished in a single session"], ans=0,
   why="EK 3.7.A.4 states that one-trial learning occurs when the association is acquired through one pairing of the stimulus and response and is not strengthened by further pairings."),
 dict(q="Biological preparedness refers to the fact that", choices=[
   "animals are biologically predisposed to learn certain stimulus-response pairings more quickly than others",
   "all stimulus-response pairings are learned at equal rates",
   "conditioning requires a fully mature nervous system",
   "an organism must be physically rested before learning can occur"], ans=0,
   why="EK 3.7.A.4 states that biological preparedness refers to how animals are biologically predisposed to learning certain stimulus-response pairings more quickly than others."),
 dict(q="A person becomes violently ill hours after eating an unfamiliar dish and afterward cannot stand the smell of it, though she knows a virus caused the illness. This best illustrates", choices=[
   "a taste aversion acquired through one-trial conditioning",
   "stimulus discrimination",
   "habituation to a novel stimulus",
   "learned helplessness"], ans=0,
   why="EK 3.7.A.4 identifies taste aversions as acquired through classical conditioning and as the framework's demonstration of one-trial conditioning; the person's knowledge of the true cause does not undo the conditioned aversion."),
 dict(q="Why does the framework treat taste aversion as evidence for biological preparedness?", choices=[
   "an association between a taste and later illness is learned far more readily than most other pairings",
   "taste aversions are impossible to extinguish",
   "taste aversions require many pairings to form",
   "taste aversions occur only in laboratory animals"], ans=0,
   why="EK 3.7.A.4 links taste aversion research to both one-trial conditioning and biological preparedness, the latter being the predisposition to learn certain pairings more quickly than others."),
 dict(q="Habituation occurs when an organism", choices=[
   "grows accustomed to a repeated or enduring stimulus and shows a diminished response to it",
   "learns to associate two stimuli with each other",
   "responds to a stimulus that resembles a conditioned stimulus",
   "recovers a response that had previously been extinguished"], ans=0,
   why="EK 3.7.A.5 states that habituation occurs when organisms grow accustomed to and exhibit a diminished response to a repeated or enduring stimulus."),
 dict(q="Which statement correctly distinguishes habituation from extinction?", choices=[
   "habituation is a diminished response to a repeated stimulus; extinction is the loss of a conditioned response when the pairing stops",
   "extinction is a diminished response to a repeated stimulus; habituation is the loss of a conditioned response when the pairing stops",
   "both require a conditioned stimulus to have been established first",
   "both describe the recovery of a response after a rest period"], ans=0,
   why="EK 3.7.A.5's habituation needs no prior conditioning at all, while EK 3.7.A.2.iii's extinction presupposes an established CS-UCS pairing that has stopped; the first distractor reverses them."),
 dict(q="A researcher proposes conditioning a fear response in young children in order to study how quickly it generalizes. The decisive ethical objection is that", choices=[
   "deliberately inducing fear in children risks lasting harm that the study's value cannot justify",
   "fear responses cannot be measured in children",
   "classical conditioning does not work on humans",
   "the study would need more than one conditioned stimulus"], ans=0,
   why="Science practice 2.D, one of this topic's stated skills: protection from harm limits what may be done to participants, and deliberately inducing a fear that may generalize and persist is exactly such a harm."),
 dict(q="A therapist repeatedly pairs a feared object with deep relaxation until the object no longer produces anxiety. This intervention rests most directly on", choices=[
   "the classical conditioning of emotional responses",
   "the reinforcement schedules of operant conditioning",
   "the social clock",
   "latent learning"], ans=0,
   why="EK 3.7.A.3 states that emotional responses can be classically conditioned and that this grounds therapeutic interventions such as counterconditioning, which is what pairing a feared object with relaxation is."),
 dict(q="Topic 3.7 names one theory that the AP Psychology Exam will not address. Which is it?", choices=[
   "the expectancy theory",
   "spontaneous recovery",
   "higher-order conditioning",
   "biological preparedness"], ans=0,
   why="The exclusion statement under EK 3.7.A.3 places the expectancy theory outside the scope of the exam; spontaneous recovery, higher-order conditioning, and biological preparedness are all required content in EK 3.7.A.2.iii, 3.7.A.2.v, and 3.7.A.4."),
]
