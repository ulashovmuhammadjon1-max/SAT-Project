# AP PSYCHOLOGY 3.8 Operant Conditioning — 30 questions
# CED effective Fall 2024/2025, Unit 3 Development and Learning.
# Learning objective 3.8.A.
#
# Essential knowledge relied on: 3.8.A.1 operant conditioning associates
# CONSEQUENCES (reinforcement and punishment) with BEHAVIORS, and the Law of
# Effect -- behaviors with reinforcing consequences are more likely to be
# repeated while behaviors with punishing consequences are not as likely to be;
# 3.8.A.2 reinforcement and punishment can each be positive or negative,
# reinforcers can be primary or secondary, and reinforcement discrimination and
# generalization have been demonstrated; 3.8.A.3 shaping through rewarding
# successive approximations, and instinctive drift -- only certain behaviors can
# be shaped through reinforcement; 3.8.A.4 superstitious behavior and learned
# helplessness; 3.8.A.5 the schedule of reinforcement determining the strength of
# the association, the two main types being continuous and partial, and each
# schedule producing a distinctive graphed pattern (fixed-interval produces a
# scalloped graph); 3.8.A.5.i continuous schedules reinforcing every correct
# behavior; 3.8.A.5.ii partial schedules being either TIME-based (fixed- or
# variable-interval) or based on the NUMBER OF BEHAVIORS performed (fixed- or
# variable-ratio).
#
# NEGATIVE REINFORCEMENT IS NOT PUNISHMENT. It is the error this topic exists to
# produce, and ten items here bear on it directly (5, 6, 7, 8, 9, 10, 11, 12, 14,
# 15). Every scenario states what happened to the FREQUENCY of the behavior,
# because that -- not whether something was pleasant -- is what separates
# reinforcement from punishment, and every "negative" item states that something
# was REMOVED, because that is what separates negative from positive.
#
# NO FIGURES. EK 3.8.A.5 mentions graphs, so item 30 describes the scalloped
# fixed-interval pattern in words rather than showing it. The CED names the
# fixed-interval scallop specifically; no other schedule's characteristic rate is
# keyed here, because the framework does not print one.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p3_8.py.
TOPIC = ("3.8", "Operant Conditioning", 3)
QUESTIONS = [
 dict(q="Operant conditioning focuses on associating", choices=[
   "consequences with behaviors",
   "one stimulus with another stimulus",
   "a memory with the place it was formed",
   "a word with the object it names"], ans=0,
   why="EK 3.8.A.1 states that operant conditioning focuses on associating consequences (reinforcement and punishment) with behaviors; associating one stimulus with another is classical conditioning in EK 3.7.A.2."),
 dict(q="The Law of Effect states that", choices=[
   "behaviors with reinforcing consequences are more likely to be repeated, and behaviors with punishing consequences are less likely",
   "every behavior is repeated equally often regardless of its consequence",
   "a stimulus paired with another stimulus comes to elicit a response",
   "organisms grow accustomed to a repeated stimulus"], ans=0,
   why="EK 3.8.A.1 states the Law of Effect in exactly these terms; the third and fourth options are classical conditioning and habituation from Topic 3.7."),
 dict(q="Reinforcement is defined by its effect on behavior, which is that reinforcement", choices=[
   "makes the behavior more likely to occur again",
   "makes the behavior less likely to occur again",
   "leaves the behavior's frequency unchanged",
   "causes the behavior to occur only once"], ans=0,
   why="EK 3.8.A.1's Law of Effect defines reinforcement by outcome: behaviors with reinforcing consequences are more likely to be repeated. The definition is about frequency, not about whether the consequence feels good."),
 dict(q="Punishment is defined by its effect on behavior, which is that punishment", choices=[
   "makes the behavior less likely to occur again",
   "makes the behavior more likely to occur again",
   "removes the behavior from memory",
   "converts the behavior into a reflex"], ans=0,
   why="EK 3.8.A.1's Law of Effect defines punishment by outcome: behaviors with punishing consequences are not as likely to be repeated."),
 dict(q="Positive reinforcement occurs when", choices=[
   "something is added after a behavior and the behavior becomes more frequent",
   "something is removed after a behavior and the behavior becomes more frequent",
   "something is added after a behavior and the behavior becomes less frequent",
   "something is removed after a behavior and the behavior becomes less frequent"], ans=0,
   why="EK 3.8.A.2 states that reinforcement and punishment can be positive or negative; 'positive' names the addition of a stimulus and 'reinforcement' names the increase in the behavior."),
 dict(q="Negative reinforcement occurs when", choices=[
   "something is removed after a behavior and the behavior becomes more frequent",
   "something is added after a behavior and the behavior becomes less frequent",
   "something is removed after a behavior and the behavior becomes less frequent",
   "something unpleasant is added after a behavior to stop it"], ans=0,
   why="EK 3.8.A.2's positive/negative distinction is about adding versus removing, while reinforcement versus punishment is about increasing versus decreasing; negative reinforcement removes something AND increases the behavior."),
 dict(q="A driver buckles her seat belt, which stops an irritating beeping sound. She now buckles it immediately every time. This is an example of", choices=[
   "negative reinforcement",
   "positive reinforcement",
   "negative punishment",
   "positive punishment"], ans=0,
   why="Something aversive was REMOVED (the beeping stopped) and the behavior became MORE frequent, which is negative reinforcement under EK 3.8.A.2."),
 dict(q="Which statement about negative reinforcement is accurate?", choices=[
   "it increases the behavior it follows, so it is not a form of punishment",
   "it decreases the behavior it follows, so it is a form of punishment",
   "it is the same as positive punishment described in different words",
   "it has no measurable effect on the frequency of a behavior"], ans=0,
   why="EK 3.8.A.1 defines reinforcement by an increase in the behavior and punishment by a decrease, so a procedure that increases behavior cannot be punishment regardless of the word 'negative'."),
 dict(q="Positive punishment occurs when", choices=[
   "something is added after a behavior and the behavior becomes less frequent",
   "something is added after a behavior and the behavior becomes more frequent",
   "something is removed after a behavior and the behavior becomes less frequent",
   "something is removed after a behavior and the behavior becomes more frequent"], ans=0,
   why="EK 3.8.A.2's terms combine independently: 'positive' means a stimulus was added, and 'punishment' means the behavior decreased."),
 dict(q="Negative punishment occurs when", choices=[
   "something is removed after a behavior and the behavior becomes less frequent",
   "something is removed after a behavior and the behavior becomes more frequent",
   "something is added after a behavior and the behavior becomes less frequent",
   "something is added after a behavior and the behavior becomes more frequent"], ans=0,
   why="EK 3.8.A.2: 'negative' means a stimulus was removed, and 'punishment' means the behavior decreased; the second option is negative reinforcement instead."),
 dict(q="A teenager loses phone privileges after breaking curfew, and afterward breaks curfew less often. This is an example of", choices=[
   "negative punishment",
   "negative reinforcement",
   "positive punishment",
   "positive reinforcement"], ans=0,
   why="Something desirable was REMOVED and the behavior became LESS frequent, which is negative punishment; the removal makes it 'negative' and the decrease makes it punishment rather than reinforcement."),
 dict(q="A student takes an aspirin, her headache goes away, and she now reaches for aspirin sooner whenever a headache begins. The aspirin-taking has been", choices=[
   "negatively reinforced",
   "positively reinforced",
   "negatively punished",
   "positively punished"], ans=0,
   why="An aversive state was REMOVED and the behavior became MORE frequent, which is negative reinforcement under EK 3.8.A.2 -- the same structure as the seat-belt case, with an internal rather than external aversive stimulus."),
 dict(q="Reinforcement generalization, demonstrated in studies of operant conditioning, occurs when a behavior reinforced in one situation", choices=[
   "also occurs in situations that resemble the original one",
   "occurs only in the exact situation in which it was reinforced",
   "stops occurring once reinforcement is withdrawn",
   "is replaced by a species-typical behavior"], ans=0,
   why="EK 3.8.A.2 states that reinforcement discrimination and generalization have been demonstrated in studies of operant conditioning; generalization is the spread of the reinforced behavior to similar situations, as the parallel term does for stimuli in EK 3.7.A.2.iv."),
 dict(q="A child is scolded for interrupting and interrupts less often afterward. Which label is correct?", choices=[
   "positive punishment, because something was added and the behavior decreased",
   "negative reinforcement, because something unpleasant occurred",
   "negative punishment, because something was taken away",
   "positive reinforcement, because attention was given"], ans=0,
   why="Scolding was ADDED and the behavior DECREASED, so it is positive punishment; the unpleasantness of the consequence does not make it negative, since 'negative' refers to removal."),
 dict(q="What single fact must be known before any consequence can be labeled reinforcement or punishment?", choices=[
   "whether the behavior became more or less frequent afterward",
   "whether the consequence was pleasant or unpleasant",
   "whether the consequence was delivered by a person or a machine",
   "whether the learner could describe the consequence in words"], ans=0,
   why="EK 3.8.A.1 defines both by the Law of Effect's outcome -- more likely or less likely to be repeated -- so the direction of the change in frequency is what fixes the label."),
 dict(q="A primary reinforcer is best described as one that", choices=[
   "satisfies a biological need without any learning being required",
   "acquires its value by being paired with another reinforcer",
   "is delivered on a fixed schedule",
   "removes an unpleasant stimulus"], ans=0,
   why="EK 3.8.A.2 states that reinforcers can be primary or secondary; a primary reinforcer is effective without prior learning because it meets a biological need."),
 dict(q="A secondary reinforcer is best described as one that", choices=[
   "acquires its reinforcing value through association with other reinforcers",
   "satisfies a biological need directly",
   "is always delivered after every correct response",
   "decreases the behavior it follows"], ans=0,
   why="EK 3.8.A.2 pairs secondary with primary reinforcers; a secondary reinforcer works because of a learned association rather than because it meets a need directly."),
 dict(q="An employee's work is checked by a supervisor who arrives at unpredictable times, and praise is given if the work is up to date at that moment. This is a", choices=[
   "variable-interval schedule",
   "variable-ratio schedule",
   "fixed-interval schedule",
   "fixed-ratio schedule"], ans=0,
   why="EK 3.8.A.5.ii makes interval schedules time-based and variable schedules unpredictable; reinforcement available at unpredictable moments in time, regardless of how many times the work was updated, is both."),
 dict(q="Shaping is best described as", choices=[
   "reinforcing successive approximations of a desired behavior until the behavior itself occurs",
   "reinforcing only the completed behavior and ignoring everything before it",
   "punishing every behavior except the desired one",
   "pairing a neutral stimulus with an unconditioned stimulus"], ans=0,
   why="EK 3.8.A.3 states that reinforcement can be used to shape behavior gradually through rewarding successive approximations of the desired behavior."),
 dict(q="A trainer first rewards a dog for facing a hoop, then only for stepping toward it, then only for passing through it. This procedure is", choices=[
   "shaping",
   "extinction",
   "instinctive drift",
   "learned helplessness"], ans=0,
   why="EK 3.8.A.3's shaping is exactly this: reinforcement of progressively closer approximations until the target behavior appears."),
 dict(q="Instinctive drift refers to the finding that", choices=[
   "only certain behaviors can be shaped through reinforcement, because species-typical behaviors intrude",
   "any behavior can be shaped if the reinforcer is strong enough",
   "a learned behavior returns after a rest period",
   "an organism stops responding to a repeated stimulus"], ans=0,
   why="EK 3.8.A.3 states that research with animals shows that only certain behaviors can be shaped through reinforcement, which it names instinctive drift."),
 dict(q="Superstitious behavior, in operant conditioning, occurs when", choices=[
   "consequences reinforce behaviors that are unrelated to those consequences",
   "an organism learns that it cannot control an aversive outcome",
   "a behavior is reinforced only after a fixed number of responses",
   "a conditioned response reappears after extinction"], ans=0,
   why="EK 3.8.A.4 states that superstitious behavior occurs when consequences reinforce unrelated behaviors."),
 dict(q="Learned helplessness occurs when organisms", choices=[
   "learn that they have no control over their experience of aversive consequences in a situation",
   "learn a behavior by watching another organism perform it",
   "acquire an association in a single pairing",
   "respond only to the exact stimulus that was trained"], ans=0,
   why="EK 3.8.A.4 states that learned helplessness occurs when organisms learn that they have no control over their experience of aversive consequences in a given situation."),
 dict(q="A student who has failed repeatedly despite studying stops attempting new assignments, saying nothing she does will make a difference. This best illustrates", choices=[
   "learned helplessness",
   "superstitious behavior",
   "instinctive drift",
   "shaping"], ans=0,
   why="EK 3.8.A.4's learned helplessness is the learned expectation that one's actions do not control the aversive outcome, which is what the student's account states."),
 dict(q="According to EK 3.8.A.5, the two main types of reinforcement schedule are", choices=[
   "continuous and partial",
   "positive and negative",
   "primary and secondary",
   "fixed and variable"], ans=0,
   why="EK 3.8.A.5 states that the two main types of reinforcement schedules are continuous and partial; fixed and variable are subdivisions within the partial schedules of EK 3.8.A.5.ii."),
 dict(q="A continuous reinforcement schedule delivers reinforcement", choices=[
   "for each and every correct behavior",
   "after a set number of correct behaviors",
   "after an unpredictable amount of time",
   "only for the first correct behavior of each day"], ans=0,
   why="EK 3.8.A.5.i states that continuous reinforcement schedules deliver reinforcement for each and every correct behavior."),
 dict(q="Partial reinforcement schedules are divided according to whether reinforcement depends on", choices=[
   "elapsed time or the number of behaviors performed",
   "whether the reinforcer is primary or secondary",
   "whether something is added or removed",
   "whether the learner is a human or an animal"], ans=0,
   why="EK 3.8.A.5.ii states that the partial schedules focus on whether reinforcement is delivered on a time-based schedule (fixed- or variable-interval) or for the number of behaviors performed (fixed- or variable-ratio)."),
 dict(q="A factory worker is paid for every twenty units assembled. This is a", choices=[
   "fixed-ratio schedule",
   "fixed-interval schedule",
   "variable-ratio schedule",
   "variable-interval schedule"], ans=0,
   why="EK 3.8.A.5.ii makes ratio schedules depend on the number of behaviors performed and fixed schedules predictable; a set count of twenty units is both."),
 dict(q="A slot machine pays out after an unpredictable number of pulls. This is a", choices=[
   "variable-ratio schedule",
   "fixed-ratio schedule",
   "variable-interval schedule",
   "fixed-interval schedule"], ans=0,
   why="EK 3.8.A.5.ii makes ratio schedules depend on the number of behaviors and variable schedules unpredictable; an unpredictable number of pulls is both."),
 dict(q="EK 3.8.A.5 notes that each reinforcement schedule produces a distinctive graphed pattern, and gives as its example that a scalloped pattern -- responding that slows just after reinforcement and accelerates as the next opportunity approaches -- is produced by a", choices=[
   "fixed-interval schedule",
   "variable-ratio schedule",
   "continuous schedule",
   "fixed-ratio schedule"], ans=0,
   why="EK 3.8.A.5 names the fixed-interval schedule as producing a scalloped graph, which is the one schedule-to-pattern pairing the framework prints."),
]
