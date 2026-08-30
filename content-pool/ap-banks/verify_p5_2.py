"""Key verification for AP PSYCH 5.2 (Positive Psychology).

No computation is possible here, so for EVERY item the specific claim the key
rests on is written out: a CED definition, a named study's actual result, or
what a theory actually predicts. That statement is what replaces sympy.

Source: AP Psychology Course and Exam Description, (c) 2024 College Board,
Course Framework V.1, Topic 5.2, p. 116.

TWO THINGS CHECKED WITH CARE:
  * The classification of character strengths has SIX virtue categories and
    EK 5.2.B.2 names them: wisdom, courage, humanity, justice, temperance,
    transcendence. Humility, patience, prudence, kindness and the rest are
    strengths WITHIN categories, not categories -- so a distractor naming one
    of them at category level is wrong for a reason worth stating.
  * EK 5.2.B.3 says posttraumatic growth MAY result. One item keys that
    hedge directly, because reading it as a rule turns a finding about some
    people into a standard others get judged against.

Positive psychology is new in the redesigned framework; the pre-2024 course did
not contain it, so there is no older material to check this topic against.

Run: python3 verify_p5_2.py
"""
import p5_2
from psych_check import check

CLAIMS = [
 ("well-being, resilience, positive emotions, and psychological health",
  "EK 5.2.A.1, in substance verbatim: positive psychology seeks to identify "
  "factors that lead to well-being, resilience, positive emotions, and "
  "psychological health. The distractors describe Topics 5.3, 4.4, and 1.6."),

 ("what makes people function well, rather than only what goes wrong",
  "EK 5.2.A.1. The field is defined by what it SEEKS. The shift is in the question "
  "asked, not a denial that disorders exist -- which is why the "
  "'whether disorders exist at all' option misrepresents the field rather than "
  "merely understating it."),

 ("capacity to adapt and recover in the face of adversity",
  "EK 5.2.A.1 names resilience among the outcomes studied. Resilience concerns "
  "recovery and adaptation UNDER adversity; the distractors redefine it as never "
  "feeling distress or never encountering adversity, which would make it "
  "unmeasurable in exactly the populations it matters for."),

 ("person's own evaluation of their life satisfaction",
  "EK 5.2.B.1 and 5.2.B.2 both use subjective well-being as the outcome. The word "
  "SUBJECTIVE marks it as the person's own appraisal, which is what separates it "
  "from an observer's rating or an objective health measure."),

 ("increases subjective well-being",
  "EK 5.2.B.1 states it directly: expressing gratitude, a positive subjective "
  "experience, increases subjective well-being."),

 ("effect of expressing gratitude on subjective well-being",
  "EK 5.2.B.1 applied. The practice is deliberate expression of gratitude and the "
  "outcome is raised life satisfaction. No trauma appears, ruling out "
  "posttraumatic growth and resilience, and nothing concerns fairness."),

 ("character strengths most central to a particular person",
  "EK 5.2.B.2 speaks of people who exercise THEIR signature strengths or virtues, "
  "which marks the strengths as individual rather than a universal list. Trained "
  "skills and employer-valued traits are different things entirely."),

 ("higher levels of happiness and subjective well-being",
  "EK 5.2.B.2: people who exercise their signature strengths or virtues report "
  "higher levels of positive experiences such as happiness and subjective "
  "well-being."),

 ("six",
  "EK 5.2.B.2 states the classification of character strengths has been developed "
  "around SIX categories of virtues. The number is stated explicitly in the "
  "framework, so this is a fact rather than an inference."),

 ("wisdom, courage, humanity, justice, temperance, transcendence",
  "EK 5.2.B.2 names exactly these six. Humility, patience, prudence, ambition, "
  "creativity and loyalty are not CATEGORY names -- several are strengths that sit "
  "within a category, which is what makes those distractors effective."),

 ("wisdom",
  "EK 5.2.B.2 names wisdom among the six. Curiosity, love of learning, and "
  "judgment are the knowledge-related strengths grouped under it."),

 ("courage",
  "EK 5.2.B.2 names courage among the six. Perseverance through setbacks and "
  "honesty when it is costly are strengths of courage -- note the framework's "
  "courage category is not limited to physical bravery, which is the narrow "
  "reading that sends students to temperance instead."),

 ("humanity",
  "EK 5.2.B.2 names humanity among the six. Kindness and social intelligence are "
  "its characteristic strengths. Justice is the near-miss: it concerns fairness in "
  "one's conduct within groups, whereas humanity concerns one-to-one warmth."),

 ("justice",
  "EK 5.2.B.2 names justice among the six. Fairness, teamwork, and leadership are "
  "its strengths. The discriminator against humanity is the group focus, and the "
  "item supplies all three group-oriented cues so it is not ambiguous."),

 ("temperance",
  "EK 5.2.B.2 names temperance among the six. Forgiveness, humility, prudence, and "
  "self-regulation are the strengths that protect against excess."),

 ("transcendence",
  "EK 5.2.B.2 names transcendence among the six. Appreciation of beauty and "
  "excellence, hope, and connection to something larger are its strengths. "
  "Gratitude also falls in this category, but the item deliberately avoids using "
  "gratitude as the cue, since gratitude carries its own separate claim in "
  "EK 5.2.B.1 and would make the item ambiguous."),

 ("positive psychological change that may follow the experience of trauma",
  "EK 5.2.B.3: posttraumatic growth, a positive subjective experience, may result "
  "after the experience of trauma or stress. It is change BEYOND the prior "
  "baseline, which is why fading memory and simple return to baseline are wrong."),

 ("recovering to prior functioning, while posttraumatic growth involves positive change beyond",
  "EK 5.2.A.1 names resilience and EK 5.2.B.3 names posttraumatic growth as "
  "separate constructs. Bouncing back is not the same as being changed for the "
  "better, and the reversed statement is the trap."),

 ("posttraumatic growth",
  "EK 5.2.B.3 applied. Changed priorities and closer relationships after a serious "
  "illness are change beyond the prior baseline following a major stressor, which "
  "is what the construct names -- not a phase of the stress response and not a "
  "coping technique."),

 ("may follow trauma for some people, but trauma is not thereby beneficial",
  "EK 5.2.B.3 says growth MAY result. The hedge is the whole point: reading it as "
  "a rule converts a finding about some people into a standard others are judged "
  "against, and the 'coped incorrectly' and 'seek out trauma' options are the two "
  "harmful misreadings this item exists to rule out. The framework licenses "
  "neither."),

 ("complementary, since building well-being addresses a question distinct",
  "EK 5.2.A.1 makes well-being and psychological health the objects of study. "
  "Raising well-being and reducing symptoms are different targets, so the field "
  "adds to treatment rather than replacing it -- and, per the later item in this "
  "module, well-being is not merely the absence of disorder."),

 ("randomly assign participants to a gratitude-journaling condition",
  "Research-methods item (Science Practice 2.B). Random assignment to a "
  "manipulated condition with an active comparison group is what licenses the "
  "causal claim EK 5.2.B.1 makes. Every other option compares people who already "
  "differ in gratitude, confounding the disposition with the practice."),

 ("associated in this sample",
  "Research-methods item (Science Practice 2.C). Both variables were measured, so "
  "only an association is established. Note EK 5.2.B.2's own wording is that "
  "people REPORT higher levels, which is itself the language of an observed "
  "association rather than a demonstrated cause."),

 ("what participants think they should say",
  "Research-methods item. Self-report is subject to social desirability. The "
  "point worth holding: this is a limitation, not a fatal objection, because "
  "subjective well-being is BY DEFINITION the person's own appraisal (EK 5.2.B.1) "
  "and so cannot simply be replaced by an observer measure."),

 ("randomly assigned to write weekly gratitude letters",
  "Argumentation item (Science Practice 4.B). EK 5.2.B.1 makes a causal claim, so "
  "support requires a manipulation, random assignment, and a comparison condition. "
  "The other findings are correlational, attitudinal, or concern likeability, "
  "which is a different outcome from the writer's own well-being."),

 ("no more improvement in well-being than a comparison group",
  "Argumentation item (Science Practice 4.B). A well-controlled manipulation "
  "showing no advantage cuts directly against EK 5.2.B.2's causal reading. "
  "Retest consistency speaks only to reliability, and cultural variation in which "
  "strengths are emphasized does not bear on whether exercising one's OWN "
  "strengths helps."),

 ("resilience",
  "EK 5.2.A.1 versus EK 5.2.B.3. The stem specifies a return to the PREVIOUS level "
  "with an unchanged outlook, which is recovery, not change beyond baseline. The "
  "unchanged outlook is the detail that rules out posttraumatic growth."),

 ("well-being is more than the absence of disorder",
  "EK 5.2.A.1 makes well-being and psychological health objects of study in their "
  "own right, which presupposes they are not simply what is left when symptoms are "
  "subtracted. A person with no diagnosis and little engagement is the standard "
  "illustration of that gap."),

 ("increase the writer's own subjective well-being",
  "EK 5.2.B.1 attributes the rise in subjective well-being to EXPRESSING "
  "gratitude, so the benefit accrues to the person expressing it and is not "
  "contingent on the recipient's reply -- which is what makes the gratitude-letter "
  "exercise usable as an intervention at all."),

 ("well-being, positive emotions, and resilience",
  "Synthesis item. EK 5.2.A.1 names the outcomes, and each program component maps "
  "onto the framework: identifying characteristic strengths is EK 5.2.B.2, a "
  "gratitude practice is EK 5.2.B.1, and recovering from setbacks is resilience "
  "from EK 5.2.A.1."),
]

check(p5_2, CLAIMS)
