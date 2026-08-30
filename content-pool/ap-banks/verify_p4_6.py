"""Key verification for AP PSYCH 4.6 (Motivation).

No computation is possible here, so for EVERY item the specific claim the key
rests on is written out: a CED definition, a named study's actual result, or
what a theory actually predicts. That statement is what replaces sympy.

Source: AP Psychology Course and Exam Description, (c) 2024 College Board,
Course Framework V.1, Topic 4.6, pp. 103-104.

Three claims checked with particular care, because each is easy to state
backwards and nothing in the item text would look wrong:
  * GHRELIN raises hunger; LEPTIN signals satiety. Reversing them is the most
    common error on this content, and the reversed statement reads perfectly
    plausibly.
  * The Yerkes-Dodson optimum is LOWER for difficult tasks and HIGHER for
    simple, well-practiced ones -- not the same for every task, and not higher
    when the task is harder.
  * EK 4.6.A.3 says humans do NOT seem to demonstrate instinctual behavior.
    Older material routinely explains human motivation by instinct.

SCOPE: Maslow's hierarchy is excluded by EK 4.4.B.1 and appears nowhere in this
module, despite being the traditional centrepiece of a motivation unit.

Run: python3 verify_p4_6.py
"""
import p4_6
from psych_check import check

CLAIMS = [
 ("drive that behavior acts to reduce, restoring homeostasis",
  "EK 4.6.A.1: drive-reduction theory addresses how certain behaviors help "
  "maintain homeostasis. Need creates drive; the behavior that reduces the drive "
  "is the motivated one. The remaining options state arousal theory, incentive "
  "theory, and instinct."),

 ("restoring the body's internal balance",
  "EK 4.6.A.1 applied. Dehydration is a departure from homeostasis, the drive "
  "energizes search behavior, and drinking reduces it -- the full drive-reduction "
  "sequence, with no reward pulling and no arousal being sought."),

 ("seek an optimal level of arousal, which can mean increasing stimulation",
  "EK 4.6.A.1: arousal theory addresses how people seek an OPTIMAL level of "
  "arousal. This is the whole contrast with drive reduction, which can only "
  "explain behavior that lowers a need -- and so cannot explain curiosity or "
  "thrill-seeking. The 'eliminate all arousal' option is drive-reduction pushed "
  "to a caricature and is the distractor to beat."),

 ("moderate level of arousal",
  "EK 4.6.A.1 cites the Yerkes-Dodson Law as the demonstration of optimal "
  "arousal. The function is an inverted U, so performance falls at both extremes; "
  "'as much arousal as possible' is the intuitive but wrong reading."),

 ("lower for difficult or unfamiliar tasks",
  "EK 4.6.A.1. The refinement most often missed, and the one an item can quietly "
  "reverse: the optimum SHIFTS with task difficulty. Arousal that would still aid "
  "a simple, well-learned task disrupts a complex or unfamiliar one, so the "
  "harder task peaks at a LOWER arousal level."),

 ("arousal theory, because the person is raising stimulation",
  "EK 4.6.A.1. Deliberately increasing arousal, with the fear itself named as the "
  "appeal, is exactly what drive-reduction theory cannot accommodate. No reward is "
  "offered, ruling out incentive theory, and EK 4.6.A.3 rules out an instinct "
  "account of human behavior."),

 ("satisfaction of the activity itself",
  "EK 4.6.A.2: self-determination theory proposes that people are motivated by "
  "intrinsic (internal) or extrinsic (external) motivations. Intrinsic motivation "
  "arises from the activity itself rather than from anything it secures."),

 ("outcome separate from the activity",
  "EK 4.6.A.2, which names incentive theory's rewards specifically as an extrinsic "
  "motivation. The defining feature is that the motivating outcome is separable "
  "from the activity."),

 ("first is intrinsically motivated and the second extrinsically",
  "EK 4.6.A.2. The discriminator is where the satisfaction lies -- in the reading "
  "itself, or in the grade the reading secures. The reversed pairing is the trap."),

 ("pull of external rewards",
  "EK 4.6.A.2: incentive theory explores the role of rewards, an extrinsic "
  "motivation, in motivating behavior. Incentives PULL from the environment, in "
  "contrast to a drive that PUSHES from an internal need -- which is the "
  "drive-reduction option offered against it."),

 ("external reward can weaken motivation that was previously intrinsic",
  "EK 4.6.A.2 sets intrinsic against extrinsic motivation and names rewards as "
  "extrinsic. Once an already-enjoyed activity is reframed as something done FOR "
  "the certificate, withdrawing the certificate withdraws the reason. Note this "
  "result runs OPPOSITE to what a simple reinforcement account predicts, which is "
  "why 'rewards always strengthen behavior' is the attractive wrong answer."),

 ("humans do not appear to demonstrate instinctual behavior",
  "EK 4.6.A.3, and this is a direct statement of the framework rather than an "
  "interpretation: instincts are innate, typically fixed patterns of behavior in "
  "ANIMALS in response to certain stimuli, and humans do not seem to demonstrate "
  "instinctual behavior or mental processes. The 'learned patterns' option also "
  "contradicts the definition, since an instinct is innate."),

 ("approach-approach conflict",
  "EK 4.6.A.4. Two desirable options, only one obtainable. It remains a conflict "
  "because choosing one forfeits the other, which is why the 'not a conflict' "
  "option is wrong even though it sounds reasonable."),

 ("avoidance-avoidance conflict",
  "EK 4.6.A.4. Two undesirable options with no attractive alternative. A social "
  "trap (EK 4.3.B.5) is excluded because that requires multiple actors whose "
  "self-interested choices harm the group; this is one person's choice."),

 ("approach-avoidance conflict",
  "EK 4.6.A.4. ONE goal carrying both positive and negative features -- higher "
  "pay against longer hours and relocation. Counting the options is what separates "
  "this from the other two conflicts."),

 ("single option with both positive and negative features",
  "EK 4.6.A.4 names all three conflicts. The structural test is the number of "
  "options: two attractive (approach-approach), two unattractive "
  "(avoidance-avoidance), or one mixed (approach-avoidance). The reversed "
  "statement is the trap."),

 ("level of need for varied or novel experiences",
  "EK 4.6.A.5, in substance verbatim: sensation-seeking theory proposes that one's "
  "level of need for varied or novel experiences is the basis of motivation."),

 ("thrill or adventure seeking",
  "EK 4.6.A.5 names four types. Thrill or adventure seeking is the pursuit of "
  "risky PHYSICAL activity; skydiving and whitewater rafting are both instances, "
  "and the stem names the risk itself as the draw."),

 ("experience seeking",
  "EK 4.6.A.5. Experience seeking pursues novelty through the mind and senses -- "
  "travel, unusual art, unconventional living -- rather than through physical "
  "risk, which is the discriminator against thrill seeking."),

 ("boredom susceptibility",
  "EK 4.6.A.5. Boredom susceptibility is a low tolerance for repetition and "
  "monotony. It is defined by the AVERSIVE reaction to sameness rather than by an "
  "appetite for any particular activity, which is what separates it from the "
  "other three types."),

 ("uninhibited social activity",
  "EK 4.6.A.5 lists disinhibition as the fourth type. It is the social-behavioral "
  "form of sensation seeking, marked by loosened restraint in social settings, "
  "and the three distractors are the other three named types."),

 ("increasing feelings of hunger",
  "EK 4.6.B.1.i names ghrelin and leptin as the hormones regulating hunger and "
  "satiety. Ghrelin is the HUNGER signal. Reversing ghrelin and leptin is the "
  "single most common error on this content, and the reversed claim reads just as "
  "plausibly, so the direction is worth stating explicitly here."),

 ("signaling satiety",
  "EK 4.6.B.1.i. Leptin is the SATIETY signal, the counterpart to ghrelin. Checked "
  "in the opposite direction from the previous item on purpose, so a reversal "
  "cannot pass both."),

 ("hypothalamus, acting via the pituitary gland",
  "EK 4.6.B.1.i states parenthetically that ghrelin and leptin are regulated by "
  "the hypothalamus via the pituitary gland. The distractor structures -- "
  "hippocampus, cerebellum, amygdala -- have no role in hunger regulation in the "
  "required content."),

 ("promotes eating while leptin suppresses it",
  "EK 4.6.B.1.i. The two hormones act in OPPOSITE directions on food intake. "
  "Stating the contrast as a pair is the reliable check against the reversal, "
  "since either hormone alone can be misremembered without the error showing."),

 ("influence of external factors on eating",
  "EK 4.6.B.1.ii: external factors like the presence of food, time of day, or "
  "social gatherings around meals also influence eating. The stem specifies the "
  "person has JUST FINISHED a large meal, which rules out a hunger signal as the "
  "cause and makes the external account the only one available."),

 ("number of minutes a participant spends exercising",
  "Research-methods item (Science Practice 2.B). An operational definition states "
  "the observable procedure by which a variable is measured. The other three "
  "restate the construct -- wants, drive, disposition -- in language that "
  "specifies no measurement at all."),

 ("free-choice period with no payment available",
  "Research-methods item (Science Practice 2.B). The research question is about "
  "behavior AFTER payment ends, so only a free-choice measure taken with no reward "
  "available can answer it; random assignment is what makes the comparison causal. "
  "Measuring during the paid period answers a different question, and the "
  "self-selected comparison confounds pre-existing interest with the treatment."),

 ("arousal theory",
  "Each clause of the stem maps to a different named theory and the question asks "
  "about one: performance peaking under MODERATE pressure is the inverted U of "
  "arousal theory and the Yerkes-Dodson Law (EK 4.6.A.1). Genuine interest is "
  "self-determination theory, good pay is incentive theory, and the choice between "
  "two appealing projects is Lewin's approach-approach conflict -- so each "
  "distractor is correct for a different clause, which is what makes the item "
  "test reading as well as recall."),

 ("explore a novel environment with no reward available",
  "Argumentation item (Science Practice 4.B). Drive-reduction theory explains "
  "behavior as the reduction of an EXISTING need, so behavior by a satiated animal "
  "with no reward on offer is what it cannot account for -- and it is exactly the "
  "observation arousal theory addresses (EK 4.6.A.1). The other three findings are "
  "all consistent with drive reduction and therefore cannot challenge it."),
]

check(p4_6, CLAIMS)
