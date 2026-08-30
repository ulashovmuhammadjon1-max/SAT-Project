"""Key audit for AP PSYCHOLOGY 3.8 Operant Conditioning.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on.

THE ONE THING THIS TOPIC MUST GET RIGHT: NEGATIVE REINFORCEMENT IS NOT
PUNISHMENT. It is the most common error in the whole course, and it is a
grammatical trap rather than a conceptual one -- "negative" sounds like "bad" and
"bad" sounds like punishment. The framework's two terms vary independently, and
this module treats them as a two-by-two:

                    behavior INCREASES        behavior DECREASES
    something ADDED   positive reinforcement    positive punishment
    something REMOVED negative reinforcement    negative punishment

  * POSITIVE / NEGATIVE says whether a stimulus was ADDED or REMOVED. It says
    nothing about whether the stimulus is pleasant.
  * REINFORCEMENT / PUNISHMENT says whether the behavior became MORE or LESS
    frequent. That is the Law of Effect in EK 3.8.A.1, and it is the whole
    definition -- nothing about how the consequence feels enters it.

Ten items bear on this directly (5, 6, 7, 8, 9, 10, 11, 12, 14, 15). Items 5, 6,
9 and 10 define all four cells with the other three cells as distractors, so no
cell can be reached by elimination. Items 7, 11, 12 and 14 are scenarios, and
every one of them states BOTH facts the labels depend on -- what was added or
removed, and which way the behavior's frequency moved. A scenario missing either
fact would have no determinate answer, which is exactly how a bad operant item
ships. Item 8 states the misconception and refutes it outright; item 15 makes the
frequency change the answer.

Item 14 deserves its own note. Scolding is unpleasant, and a student reasoning
from feeling rather than from the framework will call it "negative". It is
POSITIVE punishment: the scolding was ADDED. That single item is the sharpest
test in the module of whether the positive/negative axis has been understood as
add/remove.

TWO PLACES THE FRAMEWORK IS QUIETER THAN TEST-PREP MATERIAL, and where this
module therefore stops short:

  * EK 3.8.A.5 says each schedule produces a distinctive graphed pattern and
    gives EXACTLY ONE example: fixed-interval produces a scalloped graph. Item 30
    keys that pairing. No other schedule's characteristic response RATE is keyed
    anywhere here, because the CED prints none -- the schedule items (18, 26, 27,
    28, 29) turn on the DEFINITIONS in EK 3.8.A.5.i and 3.8.A.5.ii instead.
  * NO FIGURES. Item 30 describes the scalloped pattern in words.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p3_8

CLAIMS = [
 ("consequences with behaviors",
  "EK 3.8.A.1: operant conditioning focuses on associating consequences (reinforcement and punishment) with behaviors. The first distractor is CLASSICAL conditioning as EK 3.7.A.2 defines it -- stimulus with stimulus -- which is the contrast the two topics exist to draw."),
 ("more likely to be repeated, and behaviors with punishing consequences are less likely",
  "EK 3.8.A.1 states the Law of Effect in these terms. Both halves are keyed because the reinforcement half alone would not distinguish it from a bare definition of reinforcement."),
 ("more likely to occur again",
  "EK 3.8.A.1's Law of Effect defines reinforcement by OUTCOME -- more likely to be repeated. Nothing in the definition concerns whether the consequence is pleasant, which is the point items 8, 14 and 15 build on."),
 ("less likely to occur again",
  "EK 3.8.A.1: behaviors with punishing consequences are not as likely to be repeated. Paired with item 3 so the two directions are each stated before the four-cell items begin."),
 ("added after a behavior and the behavior becomes more frequent",
  "EK 3.8.A.2's two axes combined: 'positive' = a stimulus was ADDED, 'reinforcement' = the behavior INCREASED. The three distractors are the other three cells of the two-by-two, so the cell cannot be reached by elimination."),
 ("removed after a behavior and the behavior becomes more frequent",
  "EK 3.8.A.2: 'negative' = REMOVED, 'reinforcement' = INCREASED. The fourth distractor -- something unpleasant added to stop a behavior -- is positive punishment stated in the everyday language that produces the misconception, and it is included for exactly that reason."),
 ("negative reinforcement",
  "EK 3.8.A.2. The stem supplies both determining facts: the beeping (aversive) was REMOVED, and the buckling became MORE frequent. Removal plus increase is negative reinforcement, and no other cell fits."),
 ("increases the behavior it follows, so it is not a form of punishment",
  "EK 3.8.A.1 defines reinforcement by an increase and punishment by a decrease. A procedure that increases behavior therefore cannot be punishment, whatever the word 'negative' suggests. This is the item that states the misconception and refutes it head-on."),
 ("added after a behavior and the behavior becomes less frequent",
  "EK 3.8.A.2: 'positive' = ADDED, 'punishment' = DECREASED. Third cell of the two-by-two."),
 ("removed after a behavior and the behavior becomes less frequent",
  "EK 3.8.A.2: 'negative' = REMOVED, 'punishment' = DECREASED. Fourth cell. The second distractor is negative REINFORCEMENT, one axis away, which is the nearest miss."),
 ("negative punishment",
  "EK 3.8.A.2. Phone privileges (desirable) were REMOVED and curfew-breaking became LESS frequent: removal plus decrease. Contrast with item 7, where removal plus INCREASE gave negative reinforcement -- the two scenarios share the removal and differ only in the direction of the frequency change."),
 ("negatively reinforced",
  "EK 3.8.A.2. An aversive state (headache) was REMOVED and the aspirin-taking became MORE frequent. Structurally identical to item 7 but with an internal rather than external aversive stimulus, which is where students stop recognising the pattern."),
 ("also occurs in situations that resemble the original one",
  "EK 3.8.A.2 states that reinforcement discrimination and generalization have been demonstrated in studies of operant conditioning. Generalization is the spread to similar situations, the operant parallel of the stimulus generalization in EK 3.7.A.2.iv; the first distractor is discrimination, its sibling in the same sentence."),
 ("positive punishment, because something was added",
  "EK 3.8.A.2. THE SHARPEST ITEM IN THE MODULE: scolding is unpleasant, so a student reasoning from feeling calls it negative. It was ADDED, which makes it positive; the behavior DECREASED, which makes it punishment. The second distractor states the misconception's reasoning out loud -- 'because something unpleasant occurred' -- so choosing it is a diagnosable error rather than a guess."),
 ("whether the behavior became more or less frequent afterward",
  "EK 3.8.A.1's Law of Effect defines both reinforcement and punishment by the direction of the change in frequency. Pleasantness, the source of the consequence, and the learner's ability to describe it are all irrelevant to the label, and all three appear as distractors."),
 ("satisfies a biological need without any learning",
  "EK 3.8.A.2 states that reinforcers can be primary or secondary. A primary reinforcer works without prior learning because it meets a biological need."),
 ("acquires its reinforcing value through association",
  "EK 3.8.A.2's other category: a secondary reinforcer is effective because of a learned association rather than a direct biological need. Paired with item 16."),
 ("variable-interval schedule",
  "EK 3.8.A.5.ii: interval schedules are TIME-based and variable schedules are unpredictable. Reinforcement available at unpredictable moments regardless of how many times the work was updated is both. The stem specifies that the count of behaviors does not matter, which is what rules out the ratio schedules."),
 ("reinforcing successive approximations",
  "EK 3.8.A.3: reinforcement can be used to shape behavior gradually through rewarding successive approximations of the desired behavior. The second distractor -- reinforcing only the completed behavior -- is what shaping exists because you cannot do."),
 ("shaping",
  "EK 3.8.A.3 applied. Reinforcing facing, then stepping toward, then passing through is a sequence of progressively closer approximations, which is the definition acted out."),
 ("only certain behaviors can be shaped",
  "EK 3.8.A.3: research with animals shows that only certain behaviors can be shaped through reinforcement, known as instinctive drift. The first distractor -- any behavior can be shaped with a strong enough reinforcer -- is the claim instinctive drift refutes."),
 ("reinforce behaviors that are unrelated to those consequences",
  "EK 3.8.A.4: superstitious behavior occurs when consequences reinforce unrelated behaviors. The 'unrelated' is the whole content -- the reinforcement is real, the causal connection is not."),
 ("no control over their experience of aversive consequences",
  "EK 3.8.A.4, near verbatim: learned helplessness occurs when organisms learn that they have no control over their experience of aversive consequences in a given situation. Note that it is something LEARNED, not a personality trait."),
 ("learned helplessness",
  "EK 3.8.A.4 applied. The student's own account -- nothing she does will make a difference -- is the learned expectation of no control, and the stem supplies the history of repeated failure despite effort that produced it."),
 ("continuous and partial",
  "EK 3.8.A.5 states that the two MAIN types of reinforcement schedules are continuous and partial. 'Fixed and variable' is the tempting distractor because those words appear in the schedule names, but EK 3.8.A.5.ii places them one level down, inside the partial schedules."),
 ("each and every correct behavior",
  "EK 3.8.A.5.i, verbatim: continuous reinforcement schedules deliver reinforcement for each and every correct behavior."),
 ("elapsed time or the number of behaviors performed",
  "EK 3.8.A.5.ii: the partial schedules focus on whether reinforcement is delivered on a time-based schedule (fixed- or variable-interval) or for the number of behaviors performed (fixed- or variable-ratio). Interval = time, ratio = count. That is the axis; fixed versus variable is the second axis."),
 ("fixed-ratio schedule",
  "EK 3.8.A.5.ii: ratio schedules depend on the NUMBER of behaviors, and fixed schedules are predictable. Payment for every twenty units is a set count, so it is both."),
 ("variable-ratio schedule",
  "EK 3.8.A.5.ii: ratio because payout depends on the number of pulls, variable because the number is unpredictable. Note that the key rests on the SCHEDULE'S DEFINITION, not on a claimed response rate -- the CED prints no characteristic rate for variable-ratio schedules, so none is asserted here."),
 ("fixed-interval schedule",
  "EK 3.8.A.5 gives exactly one schedule-to-pattern pairing: a fixed-interval schedule produces a scalloped graph. The stem describes the scallop in words -- slowing just after reinforcement, accelerating as the next opportunity nears -- because there are no figures in this bank. This is the only item in the module keyed to a response PATTERN rather than to a schedule definition, because it is the only one the framework supports."),
]

psych_check.check(p3_8, CLAIMS, per_topic=30, n_choices=4)
