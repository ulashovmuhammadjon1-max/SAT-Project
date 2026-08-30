"""Key verification for AP PSYCH 4.1 (Attribution Theory and Person Perception).

There is no computation to run here, so the discipline that replaces sympy is
this: for EVERY item, the specific claim the key rests on is written out --
a CED definition, a named study's actual result, or what a theory actually
predicts. An assertion nobody checked is how a wrong key ships.

Source of every definition below: AP Psychology Course and Exam Description,
(c) 2024 College Board, Course Framework V.1, Topic 4.1, pp. 96-97.

Run: python3 verify_p4_1.py
"""
import p4_1
from psych_check import check

CLAIMS = [
 ("internal to the person",
  "EK 4.1.A.1: dispositional attributions relate to internal qualities of others "
  "such as intelligence or personality; situational attributions relate to external "
  "circumstances. The key restates the CED's own definition."),

 ("dispositional attribution",
  "Cutting someone off is explained by the other driver's character, an internal "
  "quality, not by traffic conditions. Per EK 4.1.A.1 that is dispositional. It is "
  "not the mere exposure effect (no repeated exposure) nor social comparison "
  "(no self-evaluation against another)."),

 ("situational attribution",
  "A delayed train is an external circumstance the employee experienced rather than "
  "caused, which EK 4.1.A.1 defines as situational. Self-serving bias is excluded "
  "because the manager is explaining someone else's outcome, not his own."),

 ("overweight dispositional causes and underweight situational",
  "EK 4.1.A.3 lists the fundamental attribution error as a bias in attributions "
  "about others: dispositional causes are overweighted and the situation "
  "underweighted. The credit-successes/blame-circumstance option states the "
  "self-serving bias instead, and the shared-opinions option states the false "
  "consensus effect."),

 ("fundamental attribution error",
  "This is the standard attitude-attribution demonstration: when a position is "
  "assigned by chance, the situational cause is fully known, yet observers still "
  "infer a matching disposition. The self-serving bias is excluded because the "
  "observers' own outcomes are not involved."),

 ("successes to internal causes and one's own failures to external",
  "EK 4.1.A.3: the self-serving bias is directed at the self and is "
  "valence-dependent -- credit internally for good outcomes, blame externally for "
  "bad ones. The other-people-versus-oneself option describes the actor/observer "
  "bias instead."),

 ("self-serving bias",
  "Both explanations are about the student's OWN results and reverse with the "
  "valence of the outcome. That valence reversal is what distinguishes the "
  "self-serving bias from the fundamental attribution error, which concerns "
  "explanations of other people and does not depend on outcome valence."),

 ("own behavior situationally but the same behavior in others dispositionally",
  "EK 4.1.A.3 lists actor/observer bias as its own bias. Its content is the "
  "asymmetry of perspective: as actor a person sees the situation acting on them, "
  "as observer a person sees the other's disposition. The good-outcomes-internally "
  "option is the self-serving bias, a valence effect rather than a perspective "
  "effect."),

 ("actor/observer bias",
  "The SAME behavior -- being short with a cashier -- is explained situationally "
  "for the self and dispositionally for another person. No outcome is good or bad "
  "here, so the self-serving bias does not apply; the defining contrast is the "
  "actor-versus-observer perspective."),

 ("own outcomes and shifts with whether the outcome was good or bad",
  "The precise discriminator, and the one students most often miss: the "
  "fundamental attribution error is about explaining ANOTHER person and is "
  "indifferent to outcome valence, while the self-serving bias is about the SELF "
  "and reverses direction with valence. The collectivist-cultures-only option is "
  "false -- the self-serving bias is documented across cultures, though its "
  "magnitude varies."),

 ("underestimating the power of the situation",
  "Only the subordinate's outcome is at issue, so the supervisor's self-esteem is "
  "not at stake and this cannot be a self-serving bias. Three competing "
  "assignments is a situational cause that was available and was discounted, which "
  "is the fundamental attribution error (EK 4.1.A.3)."),

 ("habitual pattern of explaining good and bad events",
  "EK 4.1.A.2: explanatory style is a predictable pattern of attributions -- how "
  "people explain good and bad events in their own lives and others' lives -- and "
  "can be optimistic or pessimistic."),

 ("pessimistic explanatory style",
  "EK 4.1.A.2. A pessimistic style explains a bad event with causes framed as "
  "broad ('not good at anything') and enduring ('will keep happening'). Locus of "
  "control is excluded: the item reports one explanation of one event, not a "
  "generalized belief about who controls outcomes."),

 ("optimistic explanatory style",
  "EK 4.1.A.2. The athlete frames the cause of the loss as specific to that "
  "opponent and temporary ('the next tournament will be different'), which is the "
  "optimistic pattern."),

 ("own effort and choices",
  "LO 4.1.B: locus of control is internal when a person believes outcomes follow "
  "from their own effort and choices, external when outcomes are believed to rest "
  "on luck, fate, or powerful others."),

 ("external locus of control",
  "LO 4.1.B. Attributing one's health outcomes generally to luck rather than to "
  "one's own action is the external orientation. This is a standing belief about "
  "control, not an emotion-focused coping strategy, which would be a technique "
  "for managing an emotional reaction."),

 ("generalized belief about control over one's outcomes",
  "The distinction students collapse: an attribution (EK 4.1.A.1) is an "
  "explanation offered for one particular event, while locus of control (LO 4.1.B) "
  "is the broader, more stable expectancy carried across situations. The "
  "symptom-versus-normal-process option is false -- locus of control is a normal "
  "individual difference, not a symptom."),

 ("increase liking",
  "EK 4.1.C.1 states it directly: the mere exposure effect occurs when people are "
  "exposed to a stimulus repeatedly over time, which causes them to like the "
  "stimulus MORE. The habituation-decrease option is the common reversal error."),

 ("mere exposure effect",
  "EK 4.1.C.1. Liking rose from repetition alone: no reward was paired with the "
  "song (so not classical conditioning), no attitude-behavior inconsistency needed "
  "resolving (so not cognitive dissonance), and no comparison with other people "
  "occurred."),

 ("expectation prompts behavior that draws out the very response expected",
  "EK 4.1.C.2: people behave in ways that elicit behaviors from others confirming "
  "their beliefs or perceptions. The mechanism is behavioral elicitation. The "
  "remembering-only-the-fitting-evidence option is confirmation bias, a memory and "
  "search effect with no elicited behavior, and is the distractor most often "
  "mistaken for this."),

 ("self-fulfilling prophecy",
  "EK 4.1.C.2, and the classic teacher-expectancy demonstration: the label was "
  "assigned at random, so it carried no real information, yet the teacher's changed "
  "behavior produced the predicted improvement. Regression toward the mean is "
  "excluded because the students were selected at random rather than for extreme "
  "prior scores."),

 ("measuring one's standing against other people",
  "EK 4.1.C.3: social comparison is a type of person perception that occurs when "
  "people evaluate themselves based on comparisons to other members of society or "
  "their social circles."),

 ("upward social comparison",
  "EK 4.1.C.3 states social comparison can be upward or downward. Comparing "
  "oneself with someone judged better is upward by definition. Relative deprivation "
  "is excluded: the violinist reports no sense of being unfairly worse off."),

 ("relative deprivation",
  "EK 4.1.C.3: people often judge their own sense of deprivation relative to "
  "others. The diagnostic detail is that the raise itself never changed -- only the "
  "comparison standard did -- so the dissatisfaction is relative, not absolute."),

 ("described as chosen or assigned",
  "Research-methods item (Science Practice 2). The independent variable is what "
  "the experimenters manipulated and randomly assigned. Participants' rated belief "
  "about the speaker is the dependent variable; random assignment is a design "
  "procedure, not a variable; and sample size is a design parameter."),
]

check(p4_1, CLAIMS)
