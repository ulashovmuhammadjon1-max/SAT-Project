"""Key audit for AP PSYCHOLOGY 3.9 Social, Cognitive, and Neurological Factors
in Learning.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on.

THE TOPIC TITLE SAYS "NEUROLOGICAL" AND THE CED PRINTS NO NEUROLOGICAL CONTENT.
This is the first thing to check in any review of this module, because it is
exactly the kind of gap a writer fills from memory. The topic has a 3.9.A
(social learning) and a 3.9.B (cognitive factors) and there is no 3.9.C. The
word "mirror" does not occur anywhere in the CED. Verified by extracting Course
Framework page 88 from the PDF on its own, since a dropped column in a longer
extraction would be indistinguishable from an absent one.

So NO ITEM HERE KEYS MIRROR NEURONS or any other neural mechanism of imitation.
Test-prep material attaches them to this topic; the framework does not, and a key
resting on them would test content the course does not contain. If a later editor
notices the title promising neurology and no item delivering it, that is the
reason.

The required content is three sentences, so breadth comes from application and
from contrast with the two conditioning topics. That is not padding -- it is how
the framework itself defines two of the three processes, BY WHAT IS ABSENT:

  * insight learning (3.9.B.1): no association, no consequence, no model
  * latent learning (3.9.B.2): no reinforcement, and not immediately evident
  * social learning (3.9.A.1): no personal experience of a consequence needed

Each of those absences is a denial of something Topic 3.7 or 3.8 requires, which
is why items 8, 9, 14, 19 and 21 are contrast items rather than definitions.

The three scenario families are kept separable by stating the diagnostic fact in
every stem: whether a MODEL was present (social vs the other two), whether a
CONSEQUENCE was involved (insight excludes it), and whether the learning was
SHOWN LATER than it was acquired (latent). Items 13, 18, 22, 23 and 24 each state
the relevant absence explicitly, because a scenario missing it would have more
than one defensible answer.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p3_9

CLAIMS = [
 ("by observation, without personal experience of a consequence",
  "EK 3.9.A.1: social learning theory proposes that learning can occur by observation and does not have to involve personal experience with a consequence. Both halves are in the key, since 'by observation' alone would not distinguish it from the requirement the second half denies."),
 ("observing the consequences experienced by someone else",
  "EK 3.9.A.1 names vicarious conditioning as the case in which learning does not involve personal experience with a consequence -- which means the consequence observed is someone else's."),
 ("copying the behavior of models",
  "EK 3.9.A.1, verbatim: learning can occur by copying the behavior of models. The distractors are classical conditioning (3.7.A.2), an operant schedule (3.8.A.5.ii), and habituation (3.7.A.5)."),
 ("the more similar the model, the more likely",
  "EK 3.9.A.1, verbatim in substance: the more similar a model is, the more likely the behavior is to be learned. The direction matters, which is why the reversed version is the first distractor; item 11 then applies it and item 29 uses it as evidence."),
 ("observational learning",
  "EK 3.9.A.1. The stem states that the child was never rewarded, which rules out operant explanations, and that she succeeded on the FIRST attempt, which rules out shaping's successive approximations (3.8.A.3)."),
 ("vicarious reinforcement",
  "EK 3.9.A.1's vicarious conditioning. The consequence was experienced by the classmate, not the observer, and the observer's behavior INCREASED -- so it is the reinforcing case. Negative reinforcement is offered as a distractor because it also increases behavior, but it requires the learner's own experience of removal."),
 ("vicarious punishment",
  "EK 3.9.A.1's vicarious conditioning again, on the punishing side: the consequence belonged to the other driver and the observer's behavior DECREASED. Items 6 and 7 are the two directions of the same mechanism, so neither can be answered by recognising 'vicarious' alone."),
 ("does not require the learner to personally experience a consequence, while operant conditioning associates a learner's own behavior",
  "EK 3.9.A.1 against EK 3.8.A.1. The absence of personal experience is the defining feature of social learning; operant conditioning associates consequences with the learner's OWN behaviors. The first distractor is that contrast reversed."),
 ("copying an observed behavior, while classical conditioning associates one stimulus with another",
  "EK 3.9.A.1 against EK 3.7.A.2. The third and fourth distractors assert requirements neither process has -- classical conditioning needs no model, and neither process requires the learner to be reinforced."),
 ("occur in the observer and are not visible in the observer's behavior at the time",
  "EK 3.7.A.1 says behaviorists traditionally focused on observable behavior to the exclusion of mental processes; EK 3.9.A.1 has learning occur through observation with no performance and no consequence at that moment. A change that leaves no behavioral trace when it happens is what the traditional position had no room for. The second distractor overstates: social learning theory does not deny that consequences matter."),
 ("resemble the adolescents in the audience",
  "EK 3.9.A.1's model-similarity claim applied to a design decision. This is the practical implication of the same sentence tested definitionally in item 4."),
 ("without any association, consequence, or model being present",
  "EK 3.9.B.1, verbatim. All three absences are in the key because the definition is exactly the conjunction of them -- dropping any one would make the definition fit shaping or observational learning as well."),
 ("insight learning",
  "EK 3.9.B.1 applied. The stem supplies all three absences: no one showed her (no model), nothing rewarded her (no consequence), and the solution arrived without pairing (no association)."),
 ("no reinforcement of intermediate steps, while shaping reinforces successive approximations",
  "EK 3.9.B.1's insight excludes a consequence; EK 3.8.A.3's shaping IS the reinforcement of successive approximations. Reinforcement of intermediate steps is therefore the exact feature that separates them, and the first distractor reverses it."),
 ("without reinforcement, and is not immediately evident",
  "EK 3.9.B.2, verbatim in substance: latent learning occurs when information is learned without reinforcement but is not immediately evident. Both clauses are load-bearing and both are in the key."),
 ("cognitive maps",
  "EK 3.9.B.2, verbatim: latent learning is often demonstrated by cognitive maps. The distractors are drawn from EK 3.8.A.5, EK 3.7.A.4, and EK 3.8.A.5's scalloped pattern -- all real content from the two conditioning topics."),
 ("mental representation of the layout of an environment",
  "EK 3.9.B.2 names cognitive maps as latent learning's usual demonstration. The map is a representation held by the learner, which is what makes it available before it is used and what makes the learning latent -- the second and fourth distractors relocate it to something a researcher or a laboratory produces."),
 ("latent learning revealed by a cognitive map",
  "EK 3.9.B.2. The stem supplies both defining features: the route knowledge was acquired without reward and without attention, and it was not evident until the closure made it useful. The insight distractor is excluded by the stem's statement that she had walked the route daily -- there WAS prior exposure, which insight learning (3.9.B.1) excludes."),
 ("acquired earlier and shown later; insight learning is a solution that arrives without association, consequence, or model",
  "EK 3.9.B.2 versus EK 3.9.B.1. Latent learning is a gap between acquisition and demonstration; insight is a solution arriving in the absence of the three supports. The third and fourth distractors are false of both -- neither requires reinforcement and neither requires a model."),
 ("learning can occur without reinforcement, even though reinforcement may be needed for the learning to be shown",
  "EK 3.9.B.2 separates acquisition (no reinforcement required) from demonstration (not immediately evident). That separation is why latent learning counts as a COGNITIVE factor in learning under objective 3.9.B rather than as another conditioning phenomenon, and it is what the second distractor denies."),
 ("insight learning, which occurs with no association, consequence, or model",
  "EK 3.9.B.1 is the only one of the three processes defined purely by absences. Each distractor misstates its own term: vicarious conditioning requires observation (3.9.A.1), social learning involves models (3.9.A.1), and latent learning does involve information being acquired (3.9.B.2) -- so all three are wrong on the framework's own wording rather than merely unattractive."),
 ("latent learning",
  "EK 3.9.B.2. Unrewarded exploration produced knowledge that appeared only once there was a reason to use it, which is 'learned without reinforcement but not immediately evident' acted out. This is the framework's canonical demonstration and it pairs with the cognitive map of item 17."),
 ("copying the behavior of a model",
  "EK 3.9.A.1. The stem states that a demonstration was watched, which supplies the model, and that performance was successful on the first try, which rules out reinforcement-based accounts."),
 ("insight learning",
  "EK 3.9.B.1. The stem states that the animal had NEVER SEEN the problem solved, which removes the model, and describes no reward and no pairing -- so all three of the framework's absences hold. Without that clause the scenario would fit observational learning equally well, which is why it is stated."),
 ("which video the child was assigned to watch",
  "Science practice 2.B: the independent variable is the manipulated, randomly assigned condition. How the child plays is the dependent variable; the toy is held constant and age is neither manipulated nor assigned."),
 ("difference in the toy, rather than in the video",
  "A confounding variable changes alongside the manipulation and offers a rival explanation. Holding the toy constant leaves the video as the only difference between the two conditions."),
 ("number of specific actions from the video that the child reproduces",
  "An operational definition states the countable procedure with a stated interval. 'Seems to copy', 'general tendency to imitate', and liking the video restate the construct or measure preference."),
 ("informed consent from guardians, minimize distress, and be able to justify the risks",
  "Science practice 2.D. Children cannot consent for themselves; exposure to modeled aggression is a FORESEEABLE risk given EK 3.9.A.1's own claim that observed behavior is copied by observers, especially similar ones; and an ethical review weighs risk against value. The third distractor is impossible to promise for that same reason, which is what makes it wrong rather than merely insufficient."),
 ("more similar a model is, the more likely the behavior is to be learned",
  "Science practice 4.B. The school's argument is about WHICH of two models to show, and only EK 3.9.A.1's similarity claim bears on that. Insight learning, cognitive maps, and reinforcement schedules are accurate framework content with nothing to say about the choice of model."),
 ("information is learned but is not immediately evident",
  "Science practice 4.B. The teacher's claim -- no behavior change means no learning -- is precisely what EK 3.9.B.2's latent learning denies, since the information is acquired before it appears. The Law of Effect and habituation are true framework content that does not contradict the claim."),
]

psych_check.check(p3_9, CLAIMS, per_topic=30, n_choices=4)
