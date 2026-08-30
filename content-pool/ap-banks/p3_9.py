# AP PSYCHOLOGY 3.9 Social, Cognitive, and Neurological Factors in Learning
# — 30 questions
# CED effective Fall 2024/2025, Unit 3 Development and Learning.
# Learning objectives 3.9.A (social learning) and 3.9.B (cognitive factors).
#
# Essential knowledge relied on, quoted because the whole topic is three
# sentences:
#
#   3.9.A.1  "Social learning theory proposes that learning can occur by
#            observation and does not have to involve personal experience with a
#            consequence (vicarious conditioning). Learning can occur by copying
#            the behavior of models. The more similar a model is, the more likely
#            the behavior is to be learned."
#   3.9.B.1  "Insight learning occurs when the solution to a problem occurs
#            without any association, consequence, or model being present."
#   3.9.B.2  "Latent learning occurs when information is learned without
#            reinforcement but is not immediately evident. Latent learning is
#            often demonstrated by cognitive maps."
#
# THE TOPIC TITLE SAYS "NEUROLOGICAL" BUT THE CED PRINTS NO NEUROLOGICAL
# ESSENTIAL KNOWLEDGE. There is a 3.9.A and a 3.9.B and no 3.9.C; the word
# "mirror" does not appear anywhere in the CED. This was checked by extracting
# Course Framework page 88 on its own, since a dropped column in a longer
# extraction would look the same as an absent one. No item here keys mirror
# neurons or any other neural mechanism of imitation, because the framework
# supplies none.
#
# Because the required content is small, breadth comes from application and from
# the contrasts with Topics 3.7 and 3.8: insight learning is defined by the
# ABSENCE of association, consequence, and model, and latent learning by the
# absence of reinforcement, so both are stated in terms of what the two
# conditioning topics require.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p3_9.py.
TOPIC = ("3.9", "Social, Cognitive, and Neurological Factors in Learning", 3)
QUESTIONS = [
 dict(q="Social learning theory proposes that learning", choices=[
   "can occur by observation, without personal experience of a consequence",
   "requires the learner to experience a consequence personally",
   "occurs only when two stimuli are paired together",
   "cannot occur unless the learner is reinforced immediately"], ans=0,
   why="EK 3.9.A.1 states that social learning theory proposes that learning can occur by observation and does not have to involve personal experience with a consequence."),
 dict(q="Vicarious conditioning refers to learning that occurs", choices=[
   "through observing the consequences experienced by someone else",
   "through repeated pairing of two stimuli",
   "only after the learner is personally reinforced",
   "without any behavior being performed by anyone"], ans=0,
   why="EK 3.9.A.1 names vicarious conditioning as the case where learning does not involve personal experience with a consequence, which is what observing another's consequences supplies."),
 dict(q="According to EK 3.9.A.1, learning can occur by", choices=[
   "copying the behavior of models",
   "pairing a neutral stimulus with an unconditioned stimulus",
   "receiving reinforcement on a variable-ratio schedule",
   "habituating to a repeated stimulus"], ans=0,
   why="EK 3.9.A.1 states that learning can occur by copying the behavior of models; the distractors are classical conditioning, an operant schedule, and habituation from Topics 3.7 and 3.8."),
 dict(q="What does the AP Psychology framework say about how similar a model is to the observer?", choices=[
   "the more similar the model, the more likely the behavior is to be learned",
   "the less similar the model, the more likely the behavior is to be learned",
   "similarity has no effect on whether the behavior is learned",
   "similarity matters only for models who are adults"], ans=0,
   why="EK 3.9.A.1 states that the more similar a model is, the more likely the behavior is to be learned."),
 dict(q="A child watches an older sibling operate a tablet and then uses it correctly on her first attempt, having never been rewarded for doing so. This best illustrates", choices=[
   "observational learning",
   "classical conditioning",
   "shaping through successive approximations",
   "habituation"], ans=0,
   why="EK 3.9.A.1's social learning is learning by observation without personal experience of a consequence, which is exactly what the child's first successful attempt demonstrates."),
 dict(q="A student sees a classmate praised for volunteering an answer and afterward volunteers more often herself. This best illustrates", choices=[
   "vicarious reinforcement",
   "negative reinforcement",
   "a fixed-interval schedule",
   "insight learning"], ans=0,
   why="EK 3.9.A.1's vicarious conditioning covers learning from consequences experienced by another; the observer's behavior increased after seeing someone else reinforced."),
 dict(q="A driver sees another car pulled over for speeding and slows down for the rest of the trip. This best illustrates", choices=[
   "vicarious punishment",
   "positive reinforcement",
   "stimulus generalization",
   "latent learning"], ans=0,
   why="EK 3.9.A.1's vicarious conditioning applies to punishing as well as reinforcing consequences; the driver's behavior decreased after observing someone else's consequence rather than her own."),
 dict(q="Which statement best distinguishes social learning from operant conditioning?", choices=[
   "social learning does not require the learner to personally experience a consequence, while operant conditioning associates a learner's own behavior with its consequence",
   "operant conditioning does not require the learner to personally experience a consequence, while social learning does",
   "social learning applies only to children and operant conditioning only to adults",
   "the two describe the same process under different names"], ans=0,
   why="EK 3.9.A.1 makes the absence of personal experience with a consequence the defining feature of social learning, while EK 3.8.A.1 has operant conditioning associate consequences with the learner's own behaviors."),
 dict(q="Which statement best distinguishes social learning from classical conditioning?", choices=[
   "social learning involves copying an observed behavior, while classical conditioning associates one stimulus with another",
   "classical conditioning involves copying an observed behavior, while social learning associates one stimulus with another",
   "both require a model to be present",
   "both require the learner to be reinforced"], ans=0,
   why="EK 3.9.A.1 makes copying the behavior of models central to social learning, while EK 3.7.A.2 makes classical conditioning the association of one stimulus with another."),
 dict(q="Social learning theory poses a difficulty for the traditional behaviorist position described in EK 3.7.A.1 because it", choices=[
   "requires processes that occur in the observer and are not visible in the observer's behavior at the time",
   "denies that consequences influence behavior at all",
   "shows that stimuli cannot be associated with one another",
   "applies only to non-human animals"], ans=0,
   why="EK 3.7.A.1 says behaviorists traditionally focused on observable behavior to the exclusion of mental processes, and EK 3.9.A.1's learning by observation without any performance or consequence at the time is a change that is not visible in behavior when it occurs."),
 dict(q="A public health campaign wants adolescents to adopt a safety behavior. According to EK 3.9.A.1, the campaign should choose models who", choices=[
   "resemble the adolescents in the audience",
   "differ as much as possible from the audience",
   "have never performed the behavior before",
   "are anonymous and unidentifiable"], ans=0,
   why="EK 3.9.A.1 states that the more similar a model is, the more likely the behavior is to be learned, which is a direct implication for who should be shown performing the behavior."),
 dict(q="Insight learning occurs when the solution to a problem arrives", choices=[
   "without any association, consequence, or model being present",
   "only after many reinforced attempts",
   "through gradual reinforcement of successive approximations",
   "by copying another person's solution"], ans=0,
   why="EK 3.9.B.1 states that insight learning occurs when the solution to a problem occurs without any association, consequence, or model being present."),
 dict(q="A person has struggled with a puzzle for an hour, sets it aside, and suddenly sees the solution while doing something else. No one showed her and nothing rewarded her. This best illustrates", choices=[
   "insight learning",
   "shaping",
   "vicarious conditioning",
   "classical conditioning"], ans=0,
   why="EK 3.9.B.1's insight learning is defined by the absence of association, consequence, and model, and the stem states that all three were absent."),
 dict(q="Which feature separates insight learning from shaping?", choices=[
   "insight learning involves no reinforcement of intermediate steps, while shaping reinforces successive approximations",
   "shaping involves no reinforcement of intermediate steps, while insight learning reinforces them",
   "insight learning requires a model and shaping does not",
   "the two terms describe the same procedure"], ans=0,
   why="EK 3.9.B.1 defines insight learning by the absence of a consequence, while EK 3.8.A.3 defines shaping as rewarding successive approximations -- reinforcement of intermediate steps is precisely what shaping is."),
 dict(q="Latent learning occurs when information is learned", choices=[
   "without reinforcement, and is not immediately evident in behavior",
   "with reinforcement, and appears immediately in behavior",
   "only after a model demonstrates it",
   "only when two stimuli are repeatedly paired"], ans=0,
   why="EK 3.9.B.2 states that latent learning occurs when information is learned without reinforcement but is not immediately evident."),
 dict(q="Latent learning is often demonstrated by", choices=[
   "cognitive maps",
   "reinforcement schedules",
   "conditioned taste aversions",
   "the scalloped fixed-interval pattern"], ans=0,
   why="EK 3.9.B.2 states that latent learning is often demonstrated by cognitive maps."),
 dict(q="A cognitive map is best described as", choices=[
   "a mental representation of the layout of an environment",
   "a diagram a researcher draws of a participant's responses",
   "a record of every reinforcement a learner has received",
   "a physical chart posted in a laboratory"], ans=0,
   why="EK 3.9.B.2 names cognitive maps as the demonstration of latent learning; a mental representation formed without reinforcement is what makes the learning latent until it becomes useful."),
 dict(q="A commuter walks the same route daily without paying attention to side streets. When the main road closes, she immediately takes an efficient detour. This best illustrates", choices=[
   "latent learning revealed by a cognitive map",
   "vicarious conditioning",
   "insight learning with no prior exposure",
   "a variable-ratio schedule"], ans=0,
   why="EK 3.9.B.2's latent learning is information acquired without reinforcement and not evident until it is needed, and the framework names cognitive maps as its usual demonstration -- which is exactly the layout knowledge the detour reveals."),
 dict(q="Which statement correctly distinguishes latent learning from insight learning?", choices=[
   "latent learning is acquired earlier and shown later; insight learning is a solution that arrives without association, consequence, or model",
   "insight learning is acquired earlier and shown later; latent learning is a solution that arrives suddenly",
   "both require reinforcement to occur",
   "both require a model to be observed"], ans=0,
   why="EK 3.9.B.2 makes latent learning a delay between acquisition and demonstration, while EK 3.9.B.1 makes insight learning the arrival of a solution in the absence of association, consequence, and model; neither requires reinforcement or a model."),
 dict(q="Latent learning is significant because it shows that", choices=[
   "learning can occur without reinforcement, even though reinforcement may be needed for the learning to be shown",
   "reinforcement is necessary for any learning to occur",
   "learning always appears in behavior as soon as it happens",
   "cognitive processes play no role in learning"], ans=0,
   why="EK 3.9.B.2 separates the acquisition of information, which happens without reinforcement, from its appearance in behavior, which may not be immediate; that separation is what makes latent learning a cognitive rather than a purely behavioral finding."),
 dict(q="Which of the three learning processes in Topic 3.9 is defined by what is ABSENT when it occurs?", choices=[
   "insight learning, which occurs with no association, consequence, or model present",
   "vicarious conditioning, which occurs with no observation",
   "social learning, which occurs with no model",
   "latent learning, which occurs with no information acquired"], ans=0,
   why="EK 3.9.B.1 defines insight learning entirely by absences; the other options misstate their own definitions, since vicarious conditioning requires observation, social learning involves models, and latent learning does involve information being acquired."),
 dict(q="A rat explores a maze for several days with no food reward, then finds the goal box quickly on the first day food is placed there. The exploration phase best illustrates", choices=[
   "latent learning",
   "shaping",
   "insight learning",
   "vicarious conditioning"], ans=0,
   why="EK 3.9.B.2's latent learning is information acquired without reinforcement that is not immediately evident; the unrewarded exploration produced knowledge that only appeared once there was a reason to use it."),
 dict(q="An apprentice watches a skilled worker complete a task several times before attempting it, and performs it well on the first try. This best illustrates", choices=[
   "learning by copying the behavior of a model",
   "learning through insight with no model present",
   "learning through a continuous reinforcement schedule",
   "learning through stimulus discrimination"], ans=0,
   why="EK 3.9.A.1 states that learning can occur by copying the behavior of models, which is what watching a demonstration and then performing the task describes."),
 dict(q="A chimpanzee that has never seen the problem solved stacks two boxes to reach fruit after a period of inactivity. This best illustrates", choices=[
   "insight learning",
   "observational learning from a model",
   "latent learning revealed by reinforcement",
   "instinctive drift"], ans=0,
   why="EK 3.9.B.1's insight learning requires that no association, consequence, or model be present, and the stem states that the animal had never seen the problem solved."),
 dict(q="A researcher randomly assigns children to watch either a video of an adult playing gently with a toy or a video of an adult playing roughly with it, then records how each child plays with the same toy afterward. The independent variable is", choices=[
   "which video the child was assigned to watch",
   "how the child plays with the toy afterward",
   "the toy, which is the same for every child",
   "the children's ages"], ans=0,
   why="Science practice 2.B: the independent variable is the manipulated, randomly assigned condition, which is the video shown; how the child plays is the measured dependent variable and the toy is held constant."),
 dict(q="In that study, using the same toy for every child is important because", choices=[
   "otherwise a difference in the toy, rather than in the video, could explain how the children played",
   "otherwise the study would have no independent variable",
   "it makes the sample representative of all children",
   "it converts the experiment into a naturalistic observation"], ans=0,
   why="A variable that changes along with the manipulation and offers a rival explanation is a confounding variable; holding the toy constant leaves the video as the only difference between conditions."),
 dict(q="Which is the best operational definition of \"imitation\" for that study?", choices=[
   "the number of specific actions from the video that the child reproduces within five minutes",
   "how closely the child seems to copy the adult",
   "the child's general tendency to imitate others",
   "whether the child liked the video"], ans=0,
   why="An operational definition states a countable measurement procedure; a count of reproduced actions within a stated interval is measurable, while the alternatives restate the construct or measure preference."),
 dict(q="Researchers proposing a study in which children observe an adult behaving aggressively must, at a minimum,", choices=[
   "obtain informed consent from guardians, minimize distress, and be able to justify the risks against the study's value",
   "conceal the study from guardians so that behavior remains natural",
   "guarantee in advance that no child will imitate the behavior",
   "recruit only children who have already behaved aggressively"], ans=0,
   why="Science practice 2.D: children cannot consent for themselves, exposure to modeled aggression is a foreseeable risk given EK 3.9.A.1's own claim that observed behavior is copied, and a risk-benefit justification is what an ethical review requires."),
 dict(q="A school argues that showing students a video of a peer performing a study skill will be more effective than showing a video of a teacher performing it. The strongest framework-based support for that argument is", choices=[
   "EK 3.9.A.1's statement that the more similar a model is, the more likely the behavior is to be learned",
   "EK 3.9.B.1's account of insight learning",
   "EK 3.9.B.2's account of cognitive maps",
   "EK 3.8.A.5's account of reinforcement schedules"], ans=0,
   why="Science practice 4.B: only the model-similarity claim bears on which of two models should be shown; insight learning, cognitive maps, and reinforcement schedules are accurate framework content that says nothing about the choice."),
 dict(q="A teacher claims: \"If a student's behavior has not changed, no learning has taken place.\" Which framework content most directly refutes this?", choices=[
   "EK 3.9.B.2's latent learning, in which information is learned but is not immediately evident",
   "EK 3.9.A.1's claim that models influence what is learned",
   "EK 3.8.A.1's Law of Effect",
   "EK 3.7.A.5's account of habituation"], ans=0,
   why="Science practice 4.B: latent learning is precisely the case of learning that has occurred without yet appearing in behavior, which is what the teacher's claim denies is possible."),
]
