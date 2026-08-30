"""Key verification for AP PSYCH 4.5 (Social-Cognitive and Trait Theories).

No computation is possible here, so for EVERY item the specific claim the key
rests on is written out: a CED definition, a named study's actual result, or
what a theory actually predicts. That statement is what replaces sympy.

Source: AP Psychology Course and Exam Description, (c) 2024 College Board,
Course Framework V.1, Topic 4.5, p. 102.

The two claims most often misstated on this topic, both checked item by item:
  * The CED's Big Five list is agreeableness, openness to experience,
    extraversion, conscientiousness, and EMOTIONAL STABILITY -- not neuroticism.
    Every trait item keys on the CED's own naming, and one item addresses the
    two labels directly so a student is not ambushed by the other one.
  * Self-efficacy and self-esteem are separate contributors to self-concept.
    Self-efficacy is a capability belief tied to a DOMAIN; self-esteem is a
    GLOBAL worth judgment. Neither is locus of control, which is Topic 4.1.

Run: python3 verify_p4_5.py
"""
import p4_5
from psych_check import check

CLAIMS = [
 ("each influence the other two",
  "EK 4.5.A.1: reciprocal determinism shapes personality. The force of the word "
  "'reciprocal' is that influence runs in every direction; the one-way "
  "environment-to-behavior option is strict behaviorism, which is the position "
  "reciprocal determinism was formulated against."),

 ("reciprocal determinism",
  "EK 4.5.A.1 applied. Her disposition selects the environment, the environment "
  "changes her, and the change alters her behavior again -- influence circulating "
  "among person, behavior, and setting rather than running one way."),

 ("how a person views themselves, including in relation to others",
  "EK 4.5.A.1 defines self-concept as how one views themselves and in relation to "
  "others, and states that self-efficacy and self-esteem both contribute to it."),

 ("capability to carry out a particular task successfully",
  "EK 4.5.A.1. Self-efficacy is a capability judgment attached to a specific task "
  "or domain. The luck-versus-effort option is locus of control from Topic 4.1 -- "
  "a generalized expectancy about who controls outcomes, not a capability belief, "
  "and the distractor most often chosen here."),

 ("overall evaluation of their own worth",
  "EK 4.5.A.1 names self-esteem alongside self-efficacy as a contributor to "
  "self-concept. Self-esteem is the GLOBAL worth judgment; the specific-skill "
  "option is self-efficacy."),

 ("capability in a specific domain, while self-esteem is a global judgment",
  "Discriminator item. EK 4.5.A.1 lists both as separate contributors to "
  "self-concept, and specificity is what separates them: low self-efficacy for "
  "public speaking is entirely compatible with high overall self-esteem. The "
  "reversed statement is the trap; both constructs are conscious and both are "
  "routinely measured, so those options are simply false."),

 ("self-efficacy for that piece",
  "EK 4.5.A.1. Repeated successful performance raises the belief that one is "
  "capable of THAT task. Nothing here concerns a global worth judgment, a "
  "generalized expectancy about control, or a Big Five trait."),

 ("low self-efficacy in one domain alongside intact self-esteem",
  "EK 4.5.A.1. The student explicitly separates a specific capability judgment "
  "('not good at chemistry') from a global worth judgment ('a worthwhile "
  "person'), which is the practical form the distinction takes."),

 ("enduring characteristics that produce typical responses to stimuli",
  "EK 4.5.B.1, in substance verbatim: trait theories conclude personality "
  "involves a set of enduring characteristics that lead to typical responses to "
  "stimuli. The distractors state the psychodynamic, behavioral, and humanistic "
  "positions."),

 ("agreeableness, openness to experience, extraversion, conscientiousness, emotional stability",
  "EK 4.5.B.2 lists exactly these five. Optimism, achievement, empathy, and "
  "egocentrism are not Big Five factors, and each distractor substitutes one of "
  "them for a real factor."),

 ("opposite ends of one dimension",
  "EK 4.5.B.2 names emotional stability; the wider literature names the same "
  "dimension from the other pole as neuroticism. They are one factor with two "
  "labels, so scores run inversely. Treating them as two separate factors would "
  "make the Big Five six, which is the error this item exists to prevent."),

 ("openness to experience",
  "EK 4.5.B.2. Openness covers imagination, intellectual curiosity, and "
  "preference for variety and novelty -- the pattern described across music, "
  "ideas, and routines."),

 ("conscientiousness",
  "EK 4.5.B.2. Conscientiousness covers organization, discipline, and "
  "dependability; scheduling, early delivery, and reliable follow-through are its "
  "behavioral signature."),

 ("extraversion",
  "EK 4.5.B.2. Extraversion covers sociability and drawing energy from social "
  "contact. Note it says nothing about warmth, which is agreeableness."),

 ("agreeableness",
  "EK 4.5.B.2. Agreeableness covers warmth, cooperation, and trust in dealings "
  "with others -- as distinct from the sociability of extraversion."),

 ("emotional stability",
  "EK 4.5.B.2 names emotional stability as the fifth factor. Calmness under "
  "pressure and quick recovery from setbacks are its high pole; the low pole is "
  "what other sources call neuroticism."),

 ("high in conscientiousness and low in agreeableness",
  "EK 4.5.B.2 treats the five as independent dimensions, so any combination is "
  "possible. Organization and dependability load on conscientiousness, warmth and "
  "cooperation on agreeableness. Collapsing the two into a single 'good employee' "
  "factor is the error this item corners."),

 ("high in extraversion and low in agreeableness",
  "EK 4.5.B.2. Sociability is extraversion; cooperativeness is agreeableness. "
  "Being outgoing carries no implication of being pleasant, which is why these "
  "two factors are separate."),

 ("high in openness to experience and low in conscientiousness",
  "EK 4.5.B.2. Unconventional ideas load on openness; planning and follow-through "
  "load on conscientiousness. The independence of the dimensions is what allows "
  "the combination the item describes."),

 ("clusters of items that correlate with one another",
  "EK 4.5.B.2 states the Big Five traits are measured by specialized personality "
  "inventories that use factor analysis to organize item responses. Factor "
  "analysis reduces many correlated items to a few underlying dimensions; it is a "
  "data-reduction technique, not a causal test and not a typing procedure."),

 ("standardized items with fixed response options, while a projective test uses ambiguous",
  "EK 4.5.B.2 describes inventories as specialized and standardized; EK 4.4.A.3 "
  "describes projective tests as probing preconscious and unconscious material "
  "through ambiguous stimuli. The final option reverses both descriptions and is "
  "the trap."),

 ("present themselves favorably rather than accurately",
  "Research-methods item. Social desirability is the standard threat to "
  "self-report validity. The 'subjective interpretation' option is the criticism "
  "of PROJECTIVE tests (see Topic 4.4) and is the distractor most often chosen; "
  "standardized inventories are scored by key, not by interpretation."),

 ("average tendency across many situations rather than their behavior on any single occasion",
  "EK 4.5.B.1 defines traits as enduring characteristics producing TYPICAL "
  "responses. 'Typical' is an aggregate claim, so variation around an average is "
  "not a counterexample. The other options defend claims trait theory does not "
  "actually make, which is what makes them wrong rather than merely weak."),

 ("stable characteristics a person carries across settings, while social-cognitive theory emphasizes",
  "EK 4.5.B.1 defines traits as enduring characteristics; EK 4.5.A.1 puts "
  "reciprocal influence among person, behavior, and environment at the center of "
  "the social-cognitive account. Neither theory concerns unconscious material -- "
  "that is Topic 4.4 -- so that contrast is a category error."),

 ("associated with higher performance ratings",
  "Research-methods item (Science Practice 2.C). A correlation licenses an "
  "associational statement only. Neither causal direction is established, and the "
  "hiring recommendation is a policy conclusion the data cannot support."),

 ("randomly assign volunteers to the training or to a comparison activity",
  "Research-methods item (Science Practice 2.B). Manipulation plus random "
  "assignment plus a comparison group is what permits a causal claim. The "
  "self-selected and retrospective-interview options leave the groups differing "
  "before the training began, and the audience-size option manipulates the wrong "
  "variable entirely."),

 ("beliefs about her capability, and the opportunities her environment offers are shaping one another",
  "EK 4.5.A.1: reciprocal determinism with self-efficacy as the personal factor. "
  "Performance changes belief, belief changes behavior, and behavior changes what "
  "the environment offers next. The environment-alone option is precisely the "
  "one-way account reciprocal determinism rejects."),

 ("what each person expects will happen and how each has learned to act in that setting",
  "EK 4.5.A.1. Because the social-cognitive account gives personal cognition and "
  "the specific environment causal roles alongside disposition, equal trait scores "
  "need not produce equal behavior in a particular setting. The 'inventory must "
  "be in error' option assumes trait determinism, which is the position under "
  "dispute."),

 ("predicted far better by the specific situation than by their trait scores",
  "Argumentation item (Science Practice 4.B). EK 4.5.B.1 claims enduring "
  "characteristics produce typical responses, so evidence that situations predict "
  "behavior better than dispositions cuts directly against it. The other three "
  "findings -- longitudinal stability, cross-national factor recovery, and "
  "observer agreement -- all SUPPORT the trait account, which is what makes them "
  "the wrong answer to a weakening question."),

 ("both the personal and the environmental components",
  "EK 4.5.A.1 names person, behavior, and environment as mutually influencing. "
  "Building task-specific confidence targets the personal factor while redesigning "
  "tasks targets the environment, so the program acts on two components at once -- "
  "which is what reciprocal determinism implies an effective intervention should "
  "do."),
]

check(p4_5, CLAIMS)
