"""Key verification for AP PSYCH 4.7 (Emotion).

No computation is possible here, so for EVERY item the specific claim the key
rests on is written out: a CED definition, a named study's actual result, or
what a theory actually predicts. That statement is what replaces sympy.

Source: AP Psychology Course and Exam Description, (c) 2024 College Board,
Course Framework V.1, Topic 4.7, pp. 105-106.

SCOPE CHECK -- the governing constraint on this topic, verified by eye against
the module and recorded here:
  EK 4.7.A.1 carries the exclusion statement "Specific names of theories of
  emotion are outside the scope of the AP Psychology Exam." No item in p4_7.py
  names or requires a theory surname. The three early positions are tested by
  what each CLAIMS about the ordering of physiological and cognitive events:
    succession   -- the bodily change comes first and the feeling follows
    simultaneity -- the two components arise together
    labelling    -- arousal is insufficient without a cognitive interpretation
  Broaden-and-build IS named in required content (EK 4.7.A.2), so it is keyed by
  name; the exclusion attaches to the 4.7.A.1 theories only.

TWO HEDGES THE FRAMEWORK MAKES AND MOST STUDY GUIDES DROP, both keyed below:
  * facial-feedback research "has produced mixed results" (EK 4.7.A.1)
  * universality research "shows mixed results" (EK 4.7.B.1)
An item asserting either as settled would be wrong against this framework.

Run: python3 verify_p4_7.py
"""
import p4_7
from psych_check import check

CLAIMS = [
 ("distinguished from reasoning or knowledge, and reflects both internal and external",
  "EK 4.7.A.1: emotion is a complex psychological process distinguished from "
  "reasoning or knowledge, and emotions reflect internal AND external factors "
  "affecting an individual. Both halves are needed, which is why the "
  "entirely-internal and entirely-external options are wrong."),

 ("physiological change precedes and gives rise to the cognitive experience",
  "EK 4.7.A.1 records that some theories proposed the physiological and cognitive "
  "experiences occurred in SUCCESSION -- the body leads and the feeling is read "
  "off it. Tested as a claim about ordering, since the theory's name is excluded "
  "from scope."),

 ("occur simultaneously",
  "EK 4.7.A.1: while some theories proposed succession, others proposed the two "
  "components occurred SIMULTANEOUSLY. Again the claim is in scope and the name "
  "is not, so the item turns on the ordering alone."),

 ("interpret the arousal and apply a cognitive label",
  "EK 4.7.A.1: other theories emphasize that the cognitive label is REQUIRED to "
  "experience an emotion. The stem supplies the motivating problem -- one arousal "
  "state could belong to several emotions -- which the labelling requirement is "
  "what resolves."),

 ("cognitive interpretation of the arousal is needed",
  "EK 4.7.A.1 applied. Similar arousal accompanying different felt emotions is "
  "precisely the observation the labelling position was built on; if arousal alone "
  "fixed the emotion, the two experiences would feel the same. The 'different "
  "patterns of arousal' option is the alternative explanation, but the stem "
  "stipulates the racing heart is common to both."),

 ("experience of an emotion is influenced by one's facial expression",
  "EK 4.7.A.1: the facial-feedback hypothesis suggests that the experience of "
  "emotion is influenced by facial expressions. The causal direction -- expression "
  "influencing experience, not merely reflecting it -- is what makes it a "
  "hypothesis rather than an observation."),

 ("physiological experience of emotion precedes the cognitive appraisal",
  "EK 4.7.A.1 states this connection explicitly: the facial-feedback hypothesis "
  "supports theories proposing the physiological experience of emotion PRECEDES "
  "the cognitive appraisal. If arranging the face alters the feeling, the bodily "
  "state is leading."),

 ("mixed results",
  "EK 4.7.A.1, verbatim in substance: research testing this hypothesis has "
  "produced MIXED results. This is a hedge the framework makes deliberately and "
  "that most study guides drop, so an item asserting facial feedback is confirmed "
  "would be wrong against the current framework."),

 ("broaden awareness and encourage new thoughts and actions",
  "EK 4.7.A.2, in substance verbatim: the broaden-and-build theory proposes "
  "positive emotional experiences tend to broaden awareness and encourage new "
  "actions and thoughts. Broaden-and-build is named in required content, so it is "
  "in scope by name unlike the 4.7.A.1 theories."),

 ("narrow thinking and the range of action",
  "EK 4.7.A.2: negative emotions tend to reduce awareness and narrow thinking and "
  "action. This is the complement of the theory's positive-emotion claim, and the "
  "option asserting negative emotions broaden equally is the direct reversal."),

 ("broaden-and-build theory of emotion",
  "EK 4.7.A.2 applied. If positive emotion broadens thought, an amused group "
  "should generate a WIDER range of uses than an anxious group, which is what the "
  "result shows. No facial posture is manipulated, no cross-cultural recognition "
  "is measured, and no rule about display is at issue."),

 ("anger, disgust, sadness, happiness, surprise, fear",
  "EK 4.7.B.1 lists exactly these six as emotions that may be commonly "
  "experienced across cultures. Pride, envy, gratitude, shame, and guilt are not "
  "on the framework's list, and each distractor substitutes at least one of them."),

 ("mixed results",
  "EK 4.7.B.1: research on the universality of emotions shows MIXED results. The "
  "second hedge the framework makes and study guides drop. Both absolutes -- "
  "universality established, or nothing shared -- misstate the framework's "
  "position, and the confirmed reading is the one students carry in."),

 ("norms governing when and how an emotion may be shown",
  "EK 4.7.B.2: display rules regulate how people can display and interpret "
  "emotions and differ among cultures. The 'events that reliably trigger' option "
  "defines ELICITORS, the other construct named in the same statement, which is "
  "the pairing this topic most often blurs."),

 ("situations or events that bring about a particular emotion",
  "EK 4.7.B.2 names display rules AND elicitors together. An elicitor CAUSES the "
  "emotion; a display rule governs whether and how it may be shown. Keeping the "
  "two apart is the point of this item."),

 ("differing display rules",
  "EK 4.7.B.2. The stem holds the FELT emotion constant -- both groups report "
  "equal frustration -- and varies only outward expression, which isolates display "
  "rules. Had the two groups been frustrated by different events, that would "
  "implicate elicitors instead."),

 ("differing elicitors",
  "EK 4.7.B.2. Here the same event produces DIFFERENT emotions, which is an "
  "elicitor difference. The deliberate mirror of the previous item: that one holds "
  "feeling constant and varies expression, this one holds the event constant and "
  "varies the feeling."),

 ("gender, age, or socioeconomic class",
  "EK 4.7.B.2 states that display rules and elicitors may regulate how people "
  "from different genders, ages, or socioeconomic classes WITHIN a culture display "
  "and interpret emotions -- so cultural variation is not only between cultures."),

 ("observes is expression, which is shaped by rules",
  "EK 4.7.B.1 and 4.7.B.2 taken together. The measured variable is outward "
  "expression, and display rules regulate it, so a cross-cultural difference in "
  "expression is ambiguous between a difference in FEELING and a difference in "
  "permitted DISPLAY. That confound is part of why EK 4.7.B.1 reports mixed "
  "results."),

 ("distinguished from reasoning or knowledge",
  "EK 4.7.A.1 explicitly distinguishes emotion from reasoning or knowledge. The "
  "precision that matters: the framework does NOT say emotion lacks a cognitive "
  "component -- one position it records makes a cognitive label essential -- so "
  "the strongest-sounding denial is the wrong answer."),

 ("interpretation of the situation shapes which emotion is experienced",
  "EK 4.7.A.1's cognitive-label position. The stimulus is held constant, only the "
  "supplied interpretation varies, and the reported emotion differs -- an outcome "
  "a purely physiological account cannot produce. Display rules are excluded "
  "because the item reports what the observers FELT, not what they showed."),

 ("elicitor -- the event that causes the emotion; display rule -- the norm",
  "EK 4.7.B.2 names both constructs. Cause versus permitted expression is the "
  "entire distinction, and the reversed pairing offered against it is the standard "
  "trap on this content."),

 ("randomly assign participants to hold either a smiling or a neutral facial posture",
  "Research-methods item (Science Practice 2.B). Facial posture is the variable of "
  "interest, so it must be manipulated and randomly assigned with the stimulus "
  "held identical. Recording how often participants smile AT cartoons measures the "
  "posture as an outcome rather than a cause, which reverses the hypothesis."),

 ("shaped by what participants believe they are supposed to feel or show",
  "Research-methods item. Because EK 4.7.B.2's display rules govern how emotions "
  "are displayed and interpreted, a self-report passes through the participant's "
  "sense of what is appropriate. The 'unaffected by cultural norms' option asserts "
  "the exact opposite of the framework's position."),

 ("single unrepresentative sample cannot support a claim about all cultures",
  "Research-methods item (Science Practice 2.C). A universality claim is a claim "
  "about populations everywhere; a sample from one country and one narrow "
  "demographic cannot license it. This sampling limitation is part of why EK "
  "4.7.B.1 reports the evidence as mixed."),

 ("no exposure to outside media reliably assign different emotions",
  "Argumentation item (Science Practice 4.B). Universality predicts convergent "
  "interpretation, so a culturally isolated group interpreting the same "
  "expressions differently is a direct counterexample. The other three findings -- "
  "cross-national startle expressions, pre-linguistic infants, and congenitally "
  "blind athletes -- all SUPPORT universality, which is exactly why they are wrong "
  "answers to a weakening question."),

 ("same arousal-inducing drug report different emotions depending on how the situation is described",
  "Argumentation item (Science Practice 4.B). Holding the physiological state "
  "constant while varying only the available interpretation, and finding the "
  "reported emotion changes, is the design that isolates EK 4.7.A.1's labelling "
  "claim. Intensity of arousal tracking intensity of emotion is consistent with a "
  "purely physiological account and so discriminates nothing."),

 ("regulated by display rules, so the same outward expression can accompany different internal states",
  "EK 4.7.B.2 makes expression a REGULATED output rather than a transparent window "
  "on feeling, which is enough to defeat the student's inference. The stronger "
  "denial that expression relates to feeling at all overshoots: EK 4.7.A.1's "
  "facial-feedback material presupposes a relationship exists."),

 ("broaden-and-build theory of emotion",
  "EK 4.7.A.2. Positive emotion broadening awareness and encouraging new actions "
  "and thoughts is exactly the widening of activity and contact described, and the "
  "accumulation of new hobbies and restored relationships over weeks is the "
  "theory's 'build' component."),

 ("both cross-cultural commonalities and culturally specific regulation, and the research is not settled",
  "Synthesis item. EK 4.7.B.1 names six emotions that may be commonly experienced "
  "across cultures while reporting the research as mixed; EK 4.7.B.2 adds display "
  "rules and elicitors that vary by culture and within it. The framework's "
  "position is deliberately the qualified one, and both absolute alternatives "
  "misrepresent it."),
]

check(p4_7, CLAIMS)
