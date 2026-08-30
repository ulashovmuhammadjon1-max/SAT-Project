# AP PSYCH 4.4 Psychodynamic and Humanistic Theories of Personality — 30 questions
# Required content: CED (c) 2024 College Board, Course Framework V.1, p. 101.
# EK 4.4.A.1 psychodynamic theory (unconscious processes drive personality);
# EK 4.4.A.2 the eight named ego defense mechanisms -- denial, displacement,
# projection, rationalization, reaction formation, regression, repression,
# sublimation; EK 4.4.A.3 projective tests; EK 4.4.B.1 humanistic theory
# (unconditional regard and the self-actualizing tendency).
#
# TWO EXCLUSION STATEMENTS, both printed in the CED on this page, both routinely
# violated by older test-prep material:
#   * "The stage theory of psychosexual development is out of scope for the AP
#     Psychology Exam."  (EK 4.4.A.1)  -- no oral/anal/phallic/latency/genital
#     item appears in this module, and no item turns on fixation at a stage.
#   * "Maslow's hierarchy of needs is outside the scope of the AP Psychology
#     Exam."  (EK 4.4.B.1)  -- the humanistic items below are built on
#     unconditional regard and the self-actualizing tendency instead.
# The CED also names no researchers in required content, so no item requires a
# surname.
#
# No sympy: every key's claim is stated item by item in verify_p4_4.py.
TOPIC = ("4.4", "Psychodynamic and Humanistic Theories of Personality", 4)
QUESTIONS = [
 dict(q="The central claim of the psychodynamic theory of personality is that personality is driven by", choices=[
   "processes that operate outside of conscious awareness",
   "the pattern of rewards and punishments a person has received",
   "a set of enduring traits measurable by questionnaire",
   "the person's conscious evaluation of their own worth"], ans=0,
   why="EK 4.4.A.1: according to the psychodynamic theory of personality, unconscious processes drive personality. The distractors state the behavioral, trait, and humanistic positions."),

 dict(q="According to psychodynamic theory, ego defense mechanisms function to", choices=[
   "protect the ego from threat, and they operate unconsciously",
   "help a person consciously plan a response to a known danger",
   "strengthen a person's memory for distressing events",
   "increase the accuracy of a person's self-assessment"], ans=0,
   why="EK 4.4.A.2 states that ego defense mechanisms serve to protect the ego unconsciously from threats. Operating outside awareness is part of the definition, which is why a deliberate coping plan is not a defense mechanism."),

 dict(q="Told that a routine scan found a serious problem, a patient insists there has been a mix-up and does not schedule the follow-up. This response is best identified as", choices=[
   "denial",
   "displacement",
   "sublimation",
   "regression"], ans=0,
   why="EK 4.4.A.2. Denial is the refusal to acknowledge a threatening reality; nothing is redirected, channeled, or replaced by earlier behavior."),

 dict(q="After being criticized by a manager she cannot safely confront, an employee goes home and snaps angrily at her roommate over a trivial matter. This is an example of", choices=[
   "projection",
   "reaction formation",
   "rationalization",
   "displacement"
], ans=3,
   why="EK 4.4.A.2. Displacement redirects an impulse from a threatening target onto a safer substitute target; the anger itself is unchanged, only its object is."),

 dict(q="A person who frequently bends the rules becomes convinced that his colleagues are all looking for ways to cheat. This is best identified as", choices=[
   "denial",
   "repression",
   "projection",
   "displacement"
], ans=2,
   why="EK 4.4.A.2. Projection attributes one's own unacceptable impulse to other people. The impulse is not redirected onto a substitute target, which is what would make it displacement."),

 dict(q="A student who skipped studying and failed an exam explains at length that the course was badly taught and the exam was unrepresentative. This explanation is best identified as", choices=[
   "reaction formation",
   "sublimation",
   "regression",
   "rationalization"
], ans=3,
   why="EK 4.4.A.2. Rationalization supplies a plausible-sounding justification that conceals the real, less acceptable reason for a behavior."),

 dict(q="A man who feels a strong dislike for a new colleague becomes conspicuously and effusively friendly toward him. This pattern is best identified as", choices=[
   "denial",
   "displacement",
   "projection",
   "reaction formation"
], ans=3,
   why="EK 4.4.A.2. Reaction formation expresses the OPPOSITE of the unacceptable impulse, characteristically in exaggerated form; the exaggeration is the diagnostic detail."),

 dict(q="An adult who is overwhelmed during a family crisis begins sulking, refusing to speak, and expecting others to manage everything for him. This is best identified as", choices=[
   "sublimation",
   "regression",
   "repression",
   "rationalization"
], ans=1,
   why="EK 4.4.A.2. Regression is a retreat to behavior characteristic of an earlier and less demanding period of development."),

 dict(q="A person cannot recall any details of a frightening event from years earlier, although others present remember it clearly and the person has no injury or illness affecting memory. Psychodynamic theory would call this", choices=[
   "denial",
   "displacement",
   "reaction formation",
   "repression"
], ans=3,
   why="EK 4.4.A.2. Repression is the exclusion of anxiety-arousing material from consciousness. Denial concerns a present reality being refused rather than a past memory becoming inaccessible."),

 dict(q="A person with strong aggressive impulses becomes a highly successful competitive athlete and channels that energy into training. This is best identified as", choices=[
   "reaction formation",
   "denial",
   "sublimation",
   "displacement"
], ans=2,
   why="EK 4.4.A.2. Sublimation redirects an unacceptable impulse into a socially valued activity; the socially constructive outlet is what separates it from displacement."),

 dict(q="What distinguishes displacement from projection?", choices=[
   "Displacement attributes the impulse to another person, while projection redirects it onto a safer target",
   "Displacement operates consciously, while projection operates unconsciously",
   "Displacement applies only to anger, while projection applies only to fear",
   "Displacement redirects the impulse onto a safer target, while projection attributes the impulse to another person"
], ans=3,
   why="EK 4.4.A.2 lists both. In displacement the person still has the impulse and acts on it toward a substitute; in projection the person disowns the impulse and sees it in someone else."),

 dict(q="What distinguishes reaction formation from denial?", choices=[
   "Reaction formation is used only by children, while denial is used only by adults",
   "Reaction formation requires a substitute target, while denial requires a socially valued outlet",
   "Reaction formation actively expresses the opposite of the impulse, while denial simply refuses to acknowledge the threatening reality",
   "Reaction formation refuses to acknowledge the reality, while denial expresses the opposite impulse"
], ans=2,
   why="EK 4.4.A.2 lists both. Denial is a failure to register the threat at all; reaction formation registers the impulse and converts it into its visible opposite."),

 dict(q="What distinguishes sublimation from displacement?", choices=[
   "Sublimation is conscious, while displacement is unconscious",
   "Sublimation removes the impulse entirely, while displacement strengthens it",
   "Sublimation channels the impulse into a socially valued activity, while displacement merely shifts it to a safer target",
   "Sublimation shifts the impulse to a safer target, while displacement channels it into a socially valued activity"
], ans=2,
   why="EK 4.4.A.2 lists both as separate mechanisms. Both redirect, but only sublimation redirects toward something the culture values; that is the whole difference."),

 dict(q="A heavy smoker dismisses each new report on smoking and health as exaggerated and continues as before. Psychodynamic theory would describe this as", choices=[
   "denial",
   "projection",
   "regression",
   "sublimation"], ans=0,
   why="EK 4.4.A.2. The threatening reality is refused rather than redirected, attributed to someone else, or channeled elsewhere."),

 dict(q="A person who is quietly envious of a friend's success repeatedly accuses that friend of being jealous of her. This is best identified as", choices=[
   "rationalization",
   "regression",
   "displacement",
   "projection"
], ans=3,
   why="EK 4.4.A.2. The unacceptable feeling is disowned and relocated in the other person, which is projection; the feeling is not redirected onto a substitute target."),

 dict(q="A manager who passed over a well-qualified candidate for reasons she is uncomfortable with tells herself the candidate 'would not have fit the team culture.' This is best identified as", choices=[
   "denial",
   "reaction formation",
   "rationalization",
   "repression"
], ans=2,
   why="EK 4.4.A.2. A comfortable justification is substituted for the real motive, which is rationalization; the decision itself is fully remembered and acknowledged, so repression and denial do not apply."),

 dict(q="A child who has been managing well at school begins wetting the bed again after a new sibling arrives. Psychodynamic theory would describe this as", choices=[
   "regression",
   "displacement",
   "projection",
   "sublimation"], ans=0,
   why="EK 4.4.A.2. Under stress the child returns to behavior belonging to an earlier developmental period, which is the definition of regression."),

 dict(q="A person who finds their own grief unbearable to sit with becomes an energetic volunteer organizing support services for others in the same situation. Psychodynamic theory would most likely describe this as", choices=[
   "denial",
   "projection",
   "reaction formation",
   "sublimation"
], ans=3,
   why="EK 4.4.A.2. Distressing feeling is converted into a socially valued and productive activity, which is sublimation. Denial would require the loss itself to go unacknowledged, and the volunteering is not the opposite of grief."),

 dict(q="Projective personality tests are designed on the assumption that", choices=[
   "people can accurately report their own enduring traits when asked directly",
   "personality is best measured by observing behavior in a controlled setting",
   "a person's score should be compared against a large standardized norm group",
   "responses to an ambiguous stimulus will reveal preconscious and unconscious material"
], ans=3,
   why="EK 4.4.A.3: psychodynamic personality psychologists assess personality using projective tests designed to probe the preconscious and unconscious mind, which is why the stimulus must be ambiguous."),

 dict(q="A frequently raised methodological criticism of projective personality tests is that", choices=[
   "they require the respondent to read at a college level",
   "they measure conscious attitudes and therefore miss unconscious material",
   "scoring depends heavily on the individual interpreter, so different scorers often reach different conclusions",
   "they can only be administered to groups rather than to individuals"
], ans=2,
   why="Research-methods item. Open-ended responses to ambiguous stimuli must be interpreted, and interpreter-dependent scoring produces low interrater reliability. The last option inverts the tests' stated purpose (EK 4.4.A.3)."),

 dict(q="According to humanistic theory, the primary motivating force in personality is", choices=[
   "the accumulation of reinforcement across the lifespan",
   "the avoidance of situations that provoke anxiety",
   "an inherent tendency toward growth and the realization of one's potential",
   "the reduction of unconscious conflict"
], ans=2,
   why="EK 4.4.B.1 names the self-actualizing tendency as a primary motivating factor in humanistic psychology."),

 dict(q="Unconditional regard, in humanistic theory, means accepting a person", choices=[
   "on the basis of an objective assessment of their strengths",
   "as they are, without making that acceptance depend on their meeting standards",
   "only after they have demonstrated genuine effort to improve",
   "while withholding any evaluation of their behavior whatsoever"
], ans=1,
   why="EK 4.4.B.1 names unconditional regard as a primary motivating factor. It is acceptance of the person that is not made contingent on performance; it does not require abandoning all judgment about specific behavior."),

 dict(q="A humanistic psychologist would predict that a child raised with acceptance made strictly conditional on achievement is most likely to", choices=[
   "develop an unusually accurate view of their own abilities",
   "show markedly higher self-actualizing behavior than other children",
   "become incapable of forming any attachment to caregivers",
   "come to value themselves only insofar as they meet others' standards"
], ans=3,
   why="If regard is conditional, worth becomes contingent on performance, which is the predicted consequence humanistic theory contrasts with unconditional regard (EK 4.4.B.1). The remaining options overstate the claim well beyond what the theory predicts."),

 dict(q="A counselor who assumes clients possess an inner capacity to move toward growth if given the right conditions is working from which assumption?", choices=[
   "behavior as the product of reinforcement history",
   "the self-actualizing tendency",
   "unconscious conflict as the engine of personality",
   "personality as a fixed set of measurable traits"
], ans=1,
   why="EK 4.4.B.1. The self-actualizing tendency is the humanistic premise that people are inherently oriented toward growth, and that the counselor's task is to supply the conditions for it."),

 dict(q="Psychodynamic and humanistic theories disagree most sharply about", choices=[
   "whether personality is driven by hidden conflict or by an inherent tendency toward growth",
   "whether personality can change at all after early childhood",
   "whether personality should be measured with questionnaires or with interviews",
   "whether biological inheritance contributes anything to personality"], ans=0,
   why="EK 4.4.A.1 puts unconscious processes at the center of the psychodynamic account, while EK 4.4.B.1 puts an inherent growth tendency at the center of the humanistic one. That is the substantive disagreement, not a methodological one."),

 dict(q="Which pairing of theory and assessment method is correct?", choices=[
   "psychodynamic theory with structured behavioral observation",
   "humanistic theory with projective tests",
   "humanistic theory with tests of unconscious conflict",
   "psychodynamic theory with projective tests"
], ans=3,
   why="EK 4.4.A.3 explicitly pairs psychodynamic personality assessment with projective tests. Humanistic assessment centers on the person's own reported experience, not on probes of unconscious material."),

 dict(q="Much early psychodynamic theory was built from detailed accounts of individual patients in treatment. The principal limitation of that evidence base is that", choices=[
   "case studies require random assignment in order to be interpreted",
   "case studies always involve deceiving the participant",
   "conclusions drawn from a small number of unrepresentative individuals may not generalize",
   "case studies cannot produce any usable information about a person"
], ans=2,
   why="Research-methods item (Science Practice 2.C). A case study yields rich detail but no basis for generalization; it is a non-experimental design, so random assignment does not apply, and it is not inherently deceptive."),

 dict(q="A frequent scientific criticism of psychodynamic theory is that many of its central claims", choices=[
   "make numerical predictions that are too precise to evaluate",
   "can be made to fit any outcome, and so are difficult to test or disconfirm",
   "have been tested many times and confirmed in every study",
   "apply only to behavior that can be directly observed"
], ans=1,
   why="Research-methods item. A construct that explains an outcome and also its opposite yields no risky prediction, so no observation can count against it. The remaining options describe the opposite property or are simply false."),

 dict(q="A therapist says, 'My aim is to provide a relationship so accepting that you feel free to explore who you are, because I believe the capacity to grow is already in you.' This statement reflects", choices=[
   "the trait view of personality",
   "the behavioral view of personality",
   "the humanistic view of personality",
   "the psychodynamic view of personality"
], ans=2,
   why="Both humanistic elements named in EK 4.4.B.1 are present: acceptance that is not made conditional, and an inherent tendency toward growth the therapist need only make room for."),

 dict(q="An employee who is passed over for a promotion tells everyone she never wanted it and had been planning to turn it down. A psychodynamic account would most likely identify this as", choices=[
   "rationalization, because a face-saving justification replaces the real disappointment",
   "sublimation, because disappointment is channeled into valued work",
   "regression, because the employee returns to an earlier stage of development",
   "projection, because the employee attributes her own wish to her colleagues"], ans=0,
   why="EK 4.4.A.2. A comfortable reason is supplied after the fact to protect the ego from the real, unwelcome one -- the defining move of rationalization. No socially valued outlet, no developmental retreat, and no impulse relocated to another person appears here."),
]
