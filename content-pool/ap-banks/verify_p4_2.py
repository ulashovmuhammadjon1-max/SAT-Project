"""Key verification for AP PSYCH 4.2 (Attitude Formation and Attitude Change).

No computation is possible here, so for EVERY item the specific claim the key
rests on is written out: a CED definition, a named study's actual result, or
what a theory actually predicts. That statement is what replaces sympy.

Source: AP Psychology Course and Exam Description, (c) 2024 College Board,
Course Framework V.1, Topic 4.2, p. 98.

Run: python3 verify_p4_2.py
"""
import p4_2
from psych_check import check

CLAIMS = [
 ("generalized concept about the members of a group",
  "EK 4.2.A.1 states it verbatim: a stereotype is a generalized concept about a "
  "group. It is a cognition. The distractors are prejudice (attitude), "
  "discrimination (behavior), an implicit attitude, and a display rule."),

 ("stereotype is a belief, prejudice is an attitude, discrimination is a behavior",
  "EK 4.2.A.1 treats stereotypes as the cognitive basis of prejudiced ATTITUDES "
  "and discriminatory BEHAVIORS. The three-way cognition/affect/behavior split is "
  "the standard mapping and the single most common confusion on this topic."),

 ("reduce cognitive load",
  "EK 4.2.A.1 says explicitly that stereotypes can help reduce cognitive load when "
  "making decisions or judgments. Choice B is false as written -- the CED makes no "
  "accuracy claim, and stereotypes are described as frequently the basis of biased "
  "perception."),

 ("prejudice without discrimination",
  "Prejudice is the attitude, discrimination the behavior (EK 4.2.A.1). The "
  "manager holds the negative attitude but treatment is equal, so the behavioral "
  "term does not apply. This is the standard dissociation case."),

 ("discrimination",
  "Refusing to rent is unequal TREATMENT, the behavioral term. A stereotype or "
  "prejudice may well underlie it, but the item asks what the refusal itself is, "
  "and behavior is what is described."),

 ("holds but may be unaware of or may not acknowledge",
  "EK 4.2.A.2, verbatim. Choice B (states publicly but does not privately endorse) "
  "is the reverse case and is the distractor most often chosen."),

 ("get the outcomes they deserve",
  "EK 4.2.A.2 lists the just-world phenomenon as a way implicit attitudes reflect "
  "negative evaluations of others. Its content is that outcomes are deserved, "
  "which licenses blaming victims of misfortune."),

 ("just-world phenomenon",
  "The observer converts a misfortune into something the sufferer brought on "
  "themselves, which is the just-world inference (EK 4.2.A.2). No group membership "
  "is mentioned, ruling out in-group bias and out-group homogeneity, and no "
  "action-attitude conflict exists, ruling out dissonance."),

 ("more similar to one another than they actually are",
  "EK 4.2.A.2. The construct concerns perceived VARIABILITY within the out-group, "
  "not hostility, size, or entitlement. 'They are all alike; we are all "
  "individuals' is the pattern."),

 ("own team more favorably than identical work by another team",
  "In-group bias (EK 4.2.A.2) is favoritism toward one's own group, isolated here "
  "by holding the work identical. Each distractor names a different listed "
  "phenomenon: out-group homogeneity, the just-world phenomenon, ethnocentrism, "
  "and implicitness."),

 ("judging other cultures by the standards of one's own",
  "EK 4.2.A.2 lists ethnocentrism. It is specifically the use of one's own culture "
  "as the evaluative yardstick, which is what separates it from mere in-group "
  "preference."),

 ("maintains a belief even after evidence against it",
  "EK 4.2.B.1, verbatim: belief perseverance occurs when a belief persists even if "
  "evidence suggests it is not accurate."),

 ("confirmation bias",
  "EK 4.2.B.1 names confirmation bias as the process by which people cling to a "
  "belief regardless of evidence for or against it: evidence favorable to the "
  "belief is sought, unfavorable evidence avoided."),

 ("persistence of the belief itself",
  "The discriminator. EK 4.2.B.1 links the two but they are not the same: belief "
  "perseverance names the OUTCOME (the belief survives disconfirmation), "
  "confirmation bias names the PROCESS (selective search and weighting) that "
  "protects it. Choice C is false -- confirmation bias is typically not deliberate."),

 ("discomfort arising when a person's actions and attitudes are in conflict",
  "EK 4.2.B.2, verbatim: cognitive dissonance is the mental discomfort that occurs "
  "when actions or attitudes are in conflict. Choice E describes the humanistic "
  "self/ideal-self gap, a different construct entirely."),

 ("change either the action or the attitude",
  "EK 4.2.B.2: people are motivated to reduce the discomfort by changing either "
  "actions or attitudes to be more in line with each other. Note the theory "
  "predicts realignment, not repression -- choice B is the psychodynamic answer "
  "and is wrong here."),

 ("reduction of cognitive dissonance",
  "The commute is fixed, so the cheaper route to consistency is revising the "
  "attitude, which is what the person did. Belief perseverance is excluded because "
  "the belief did NOT persist -- it changed, which is the whole point."),

 ("too little external justification",
  "The insufficient-justification result. A large payment supplies an external "
  "reason for the statement, so no inconsistency needs resolving and the attitude "
  "does not move; a small payment supplies too little, leaving attitude change as "
  "the only route. Predicting the OPPOSITE (more money, more change) is the "
  "classic student error, and it is what a reinforcement account would wrongly "
  "predict."),

 ("adding a belief that makes the action consistent",
  "EK 4.2.B.2 allows dissonance reduction by bringing actions and attitudes into "
  "line; adding a consonant belief ('everyone does it') achieves that alignment "
  "without altering the past behavior or abandoning the self-image. Choice B is "
  "wrong because the behavior has already occurred and cannot be changed."),

 ("preference that the person sincerely denies holding",
  "EK 4.2.A.2's defining property is unawareness or non-acknowledgment, so the "
  "diagnostic pattern is a measured preference paired with a sincere denial. "
  "Choice B is the definition of an EXPLICIT attitude."),

 ("belief perseverance",
  "The debriefing removed the entire evidential basis for the belief and the "
  "belief survived, which is precisely EK 4.2.B.1. Dissonance is excluded because "
  "no action of the participant's conflicts with an attitude."),

 ("attitude held toward the other group",
  "Prejudice is defined as an attitude (EK 4.2.A.1), so an intervention aimed at "
  "reducing prejudice targets the attitude. Cooperative pursuit of a shared aim is "
  "the superordinate-goal approach noted in EK 4.3.B.5, and its target is the "
  "intergroup attitude."),

 ("shapes what a perceiver notices and remembers",
  "EK 4.2.A.1 states stereotypes can be the cause and/or result of biased "
  "perceptions and experiences. The mechanism closing that loop is selective "
  "attention and recall, the same process EK 4.2.B.1 calls confirmation bias. "
  "Choice D is a claim the CED does not make."),

 ("self-report cannot capture attitudes participants are unaware of",
  "Research-methods item (Science Practice 2). Because EK 4.2.A.2 defines implicit "
  "attitudes as ones the holder may not be aware of or may not acknowledge, a null "
  "self-report result cannot establish the absence of prejudice. The other options "
  "are false statements about methodology."),

 ("weighed the supportive portions of the report more heavily",
  "Identical balanced evidence strengthening opposite prior views is the standard "
  "signature of confirmation bias acting on an existing belief (EK 4.2.B.1). "
  "Choice C misstates the mere exposure effect, which concerns liking for a "
  "repeated stimulus, not divergent belief strengthening."),
]

check(p4_2, CLAIMS)
