"""Key verification for AP PSYCH 5.1 (Introduction to Health Psychology).

No computation is possible here, so for EVERY item the specific claim the key
rests on is written out: a CED definition, a named study's actual result, or
what a theory actually predicts. That statement is what replaces sympy.

Source: AP Psychology Course and Exam Description, (c) 2024 College Board,
Course Framework V.1, Topic 5.1, pp. 114-115.

THE CLAIM MOST OFTEN GOT BACKWARDS, keyed explicitly below: EK 5.1.C.1 states
that the greatest susceptibility to illness occurs during the EXHAUSTION phase
of the general adaptation syndrome -- not the alarm phase, where arousal peaks
and where intuition sends most students.

Health psychology is NEW in the redesigned framework, so older test-prep
material has no coverage of this topic at all and cannot be used to check it.

Run: python3 verify_p5_1.py
"""
import p5_1
from psych_check import check

CLAIMS = [
 ("behavior and mental processes relate to physical health and wellness",
  "LO 5.1.A: health psychology addresses issues of physical health and wellness as "
  "they apply to behavior and mental processes. The distractors describe Topic 5.3 "
  "(classifying disorders), Topic 1.6 (sensation), and Topic 3.5 (language)."),

 ("heightened susceptibility to disorders and disease",
  "EK 5.1.B.1, verbatim in substance: stress is a factor in heightened "
  "susceptibility to disorders and disease. The improved-immune-function option is "
  "the direct reversal, since the same statement names immune suppression."),

 ("hypertension, headaches, and immune suppression",
  "EK 5.1.B.1 names exactly these three physiological issues as linked to stress. "
  "The distractor sets are sensory conditions, physical injuries, and dietary "
  "conditions, none of which the framework links to stress."),

 ("motivating",
  "EK 5.1.B.2: stressors can be viewed as motivating (eustress) or debilitating "
  "(distress). The precision worth holding: eustress is not the ABSENCE of stress "
  "or of arousal, it is stress experienced as energizing."),

 ("debilitating",
  "EK 5.1.B.2, the paired term. Distress is the debilitating form. Neither "
  "duration nor whether the cause is physical or psychological is what separates "
  "the two, which is what makes those distractors plausible and wrong."),

 ("eustress for the first and distress for the second",
  "EK 5.1.B.2 applied. The stressor is held identical across the two musicians, so "
  "the difference lies entirely in how it is experienced -- motivating versus "
  "debilitating. That is precisely why the framework needs two terms rather than a "
  "single measure of stressor severity."),

 ("individually minor but can build up over time",
  "EK 5.1.B.2: stressors can be experienced as traumatic or as daily hassles that "
  "can BUILD UP over time. Accumulation is the mechanism that makes individually "
  "small stressors consequential; the framework makes no claim that hassles "
  "outrank traumatic events in severity."),

 ("throughout the lifespan",
  "EK 5.1.B.2 names adverse childhood experiences as sources of stress that can "
  "affect a person THROUGHOUT THE LIFESPAN. The whole significance of the "
  "construct is that the effects are not confined to childhood, which is what the "
  "'only during childhood' distractor denies."),

 ("alarm reaction, resistance, exhaustion",
  "EK 5.1.C.1 gives the order: alarm reaction when the stress is encountered, then "
  "resistance as it is confronted, then exhaustion. The distractors are "
  "permutations, and the sequence is the whole content of the item."),

 ("first encountered, via a fight-flight-freeze response",
  "EK 5.1.C.1: initially, alarm reaction occurs when the stress is encountered, "
  "via a fight-flight-freeze response. Note the framework's term includes FREEZE, "
  "not only fight or flight."),

 ("sustained mobilization of resources while the stress is being confronted",
  "EK 5.1.C.1: a resistance phase occurs as the stress is confronted. The body "
  "stays mobilized rather than returning to baseline, which is what makes the "
  "phase costly and sets up exhaustion -- so 'complete return to baseline' is "
  "exactly wrong."),

 ("stress subsides or the body's resources are spent",
  "EK 5.1.C.1, in the framework's own terms: an exhaustion phase occurs when the "
  "stress subsides, or resources are spent. Note that the phase can arrive when "
  "the stressor ENDS, which is counterintuitive and is what the next item turns "
  "on."),

 ("exhaustion",
  "EK 5.1.C.1 states explicitly that the greatest susceptibility to illness occurs "
  "during the exhaustion phase. This is the single most reversed claim on the "
  "topic: intuition says the alarm phase, because that is when arousal peaks, and "
  "the framework says otherwise."),

 ("tending to their own or others' needs and seeking connection",
  "EK 5.1.C.2: the tend-and-befriend theory proposes that some people react to "
  "stress by tending to their own needs and/or the needs of others and seeking "
  "connection with others. Withdrawal from social contact is the opposite of the "
  "befriend component."),

 ("mostly in women",
  "EK 5.1.C.2 states that this phenomenon seems to occur mostly in women. The "
  "hedged wording -- 'seems to' -- is the framework's own and is preserved in the "
  "item rather than hardened into a stronger claim."),

 ("turns toward others and toward caregiving, while fight-flight-freeze prepares the body",
  "EK 5.1.C.1 attaches fight-flight-freeze to the alarm reaction; EK 5.1.C.2 "
  "describes tend-and-befriend as an alternative pattern oriented toward "
  "connection and care. The reversed pairing is the trap, and the claim that "
  "tend-and-befriend involves no physiological change is not one the framework "
  "makes."),

 ("problem to be solved and working at solutions until one is found",
  "EK 5.1.D.1, in substance verbatim: problem-focused coping involves seeing "
  "stress as a problem to be solved and working solutions until a solution is "
  "found. Avoidance and passivity are not coping strategies the framework names."),

 ("managing one's emotional reactions",
  "EK 5.1.D.2: emotion-focused coping involves managing emotional reactions to "
  "stress as a means of coping, with deep breathing, meditation, and medication "
  "named as examples. Removing the source directly is the problem-focused "
  "alternative."),

 ("problem-focused coping",
  "EK 5.1.D.1 applied. Listing assignments and building a schedule act on the "
  "STRESSOR -- the workload itself -- rather than on the feelings it produces, "
  "which is the defining direction of problem-focused coping."),

 ("emotion-focused coping",
  "EK 5.1.D.2 names deep breathing and meditation explicitly among emotion-focused "
  "strategies. The stem specifies a result the person cannot influence, so the "
  "stressor is unalterable and only the reaction can be managed."),

 ("stressor is something the person can actually change",
  "EK 5.1.D.1 defines problem-focused coping as working solutions UNTIL A SOLUTION "
  "IS FOUND, which presupposes a stressor that admits of one. Where nothing can be "
  "changed, solution-seeking effort has no target and EK 5.1.D.2's emotion-focused "
  "strategies fit better. This is the standard controllability finding and it "
  "follows directly from the framework's own definitions."),

 ("targets the stressor itself, while emotion-focused coping targets the person's reaction",
  "EK 5.1.D.1 and 5.1.D.2. The discriminator is the TARGET of the effort. Note the "
  "'always more effective' option is false: neither is universally superior, since "
  "fit depends on whether the stressor can be changed."),

 ("emotion-focused coping strategy",
  "EK 5.1.D.2 names taking medication aimed at reducing stressful emotional "
  "responses among emotion-focused strategies, alongside deep breathing and "
  "meditation. Medication is easy to misfile as problem-focused because it is an "
  "active step, but its target is the emotional response."),

 ("associated in this sample",
  "Research-methods item (Science Practice 2.C). Both variables were measured "
  "rather than manipulated, so only an associational claim is licensed. Both "
  "causal options are live possibilities the design cannot separate, and a third "
  "variable could produce both."),

 ("number of hassles a participant records in a standardized daily diary",
  "Research-methods item (Science Practice 2.B). An operational definition "
  "specifies the observable measurement procedure. The other three restate the "
  "construct -- feeling burdened, underlying tension, seeming stressed -- without "
  "specifying anything that could be counted."),

 ("depend on memory collected long after the events",
  "Research-methods item (Science Practice 2.C). This is a retrospective design "
  "and recall accuracy is its central weakness. Note random assignment is not "
  "merely impractical here but ethically impossible -- no one may assign a child "
  "to adversity -- which is exactly why the correlational design is used."),

 ("exposed to a virus under controlled conditions",
  "Argumentation item (Science Practice 4.B). EK 5.1.B.1's claim concerns "
  "susceptibility to DISEASE, so supporting evidence must link prior stress to an "
  "objective disease outcome under controlled exposure. The other three findings "
  "concern subjective experience and bear on the claim not at all."),

 ("exhaustion phase, when resources are spent",
  "EK 5.1.C.1. The diagnostic detail is the TIMING: illness appearing after the "
  "prolonged stress ends, once resources are spent, is the exhaustion phase, which "
  "the framework names as the point of greatest susceptibility. 'Illness appeared "
  "suddenly' is a tempting but irrelevant cue toward the alarm reaction."),

 ("risk of harm that cannot be justified by the knowledge gained",
  "Ethics item (Science Practice 2.D). Research must minimize harm, and "
  "deliberately driving participants to resource depletion imposes serious risk "
  "that a milder design avoids. This is why the stress-illness literature relies "
  "on correlational designs and naturally occurring stressors."),

 ("problem-focused and emotion-focused strategies together",
  "EK 5.1.D.1 and 5.1.D.2 describe two categories, not two mutually exclusive "
  "types of person. Applying for positions targets the stressor and running "
  "targets the emotional reaction, so both are in use at once -- and the framework "
  "nowhere requires a person to pick one."),
]

check(p5_1, CLAIMS)
