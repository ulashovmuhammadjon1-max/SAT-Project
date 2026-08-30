"""Key audit for AP PSYCHOLOGY 2.2 Thinking, Problem-Solving, Judgments, and
Decision-Making.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on AND, for this topic specifically, which neighbouring term the item
is separating the key from and what in the stem rules that neighbour out.

That second half matters more here than anywhere else in Units 1-3. Every term
in EK 2.2.A has a near neighbour, and the standard way a bad heuristics item
ships is that the scenario genuinely fits two of them. Where a scenario could
plausibly be read two ways, the stem carries a clause that closes the second
reading, and the claim below names that clause:

    representativeness (judged by resemblance to a stereotype)
        vs availability (judged by how easily an example is recalled)
    gambler's fallacy (a future probability misjudged)
        vs sunk cost (an unrecoverable past investment driving a present choice)
    mental set (fixation on a strategy that worked before)
        vs functional fixedness (fixation on an object's customary use)
    assimilation (schema unchanged) vs accommodation (schema revised)
    algorithm (exhaustive, guaranteed) vs heuristic (shortcut, fallible)
    priming (earlier exposure shapes a later response)
        vs framing (the same facts presented differently)
    divergent (generate many) vs convergent (narrow to one)

Six items (6, 12, 15, 18, 21, and the pairs they close) are explicit
"distinguish X from Y" questions whose first distractor is the correct
definition with the two halves swapped. That is deliberate: a student who has
memorised both labels but not which is which cannot pass those by elimination.

One cross-topic caution enforced by reading: "perceptual set" belongs to Topic
2.1 (EK 2.1.A.2) and "mental set" to Topic 2.2 (EK 2.2.A.5). They are different
constructs with similar names. Item 16 uses the perceptual set as a distractor
on purpose; neither is ever offered as a synonym for the other.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p2_2

CLAIMS = [
 ("mental categories that form the basis of thought",
  "EK 2.2.A.1: concepts form the basis of thought. The three distractors are algorithms (EK 2.2.A.3), heuristics (EK 2.2.A.4), and memories -- each a real construct with its own EK, so the item discriminates within the course."),
 ("ideal example of a given concept",
  "EK 2.2.A.1, verbatim: prototypes are the ideal example for any given concept."),
 ("closer to most people's prototype",
  "EK 2.2.A.1's prototype is the ideal example of a concept. The stem is built so that both animals really are birds -- the second distractor, which denies the penguin is a bird, is therefore false rather than merely unattractive, and prototypicality is the only thing separating the two."),
 ("assimilation",
  "EK 2.2.A.2 defines assimilation as taking in new information but NOT changing the schema in light of it. The stem states explicitly that she does not alter her idea of a dog, which is the clause that rules out accommodation."),
 ("accommodation",
  "EK 2.2.A.2 defines accommodation as taking in new information AND changing the schema to incorporate it. The stem states that she revises the category, which is the clause that rules out assimilation. Items 4 and 5 are the same child in sequence so the pair cannot be answered from one remembered word."),
 ("assimilation leaves the existing schema unchanged",
  "EK 2.2.A.2 defines the two solely by whether the schema itself changes. The first distractor is that definition with the halves swapped; the age-based and memory/perception distractors are inventions the framework does not make."),
 ("tries all possible solutions until the correct one is found",
  "EK 2.2.A.3, near verbatim. The distractors are the heuristic (2.2.A.4), the availability heuristic specifically, and mental set (2.2.A.5)."),
 ("mental shortcuts and so can produce errors",
  "EK 2.2.A.4: heuristics address problems by using mental shortcuts to make judgments, and using them can lead to errors in judgment. The 'guaranteed to reach the correct answer' distractor is the algorithm's property from EK 2.2.A.3, and 'require more time and effort' inverts the trade-off entirely."),
 ("an algorithm",
  "EK 2.2.A.3's algorithm is defined by attempting ALL possible solutions. The stem says 'systematically works through every possible ordering', which is the definition acted out and is what excludes a heuristic."),
 ("representativeness heuristic",
  "EK 2.2.A.4 describes the representativeness heuristic as deciding according to prior expectations or stereotypes. The stem supplies the base rate -- far more salespeople -- so the judgment is demonstrably driven by stereotype fit rather than by frequency, which is also what rules out availability."),
 ("availability heuristic",
  "EK 2.2.A.4 describes the availability heuristic as recalling the first or most vivid example that comes to mind. The stem supplies vivid news coverage as the source of the example, not a stereotype about who gets attacked, which is what rules out representativeness."),
 ("representativeness judges by resemblance to a stereotype",
  "EK 2.2.A.4 defines the pair by their different bases. The first distractor is the correct definition reversed. This is the item that catches a student who knows both names but not which is which."),
 ("gambler's fallacy",
  "EK 2.2.A.6 names the gambler's fallacy among the cognitive processes that hinder good decisions. The error is treating independent events as though past outcomes change future probability; nothing has been invested and nothing is unrecoverable, which is what rules out sunk cost."),
 ("sunk-cost fallacy",
  "EK 2.2.A.6 names the sunk-cost fallacy. The ticket price and the two hours are unrecoverable and are the stated reason for continuing; no probability is being misjudged, which is what rules out the gambler's fallacy."),
 ("misjudges the probability of a future event; the sunk-cost fallacy lets unrecoverable past investment",
  "EK 2.2.A.6 lists the two together, but one is an error about probability and the other about which costs bear on a decision. The first distractor is that contrast reversed; the remaining two assert a shared subject matter the framework does not."),
 ("approach a new problem the way a previous problem was successfully solved",
  "EK 2.2.A.5: decision making can be influenced by prior experiences that were successful -- mental set. The distractors are functional fixedness (2.2.A.8), the PERCEPTUAL set from Topic 2.1 (a different construct with a similar name), and the availability heuristic."),
 ("functional fixedness",
  "EK 2.2.A.8 names functional fixedness as what hinders creative thinking: the object is seen only in its customary function. The stem is about an object's use, not about a strategy carried over from an earlier problem, which is what rules out mental set."),
 ("mental set is fixation on a familiar strategy; functional fixedness is fixation on an object's usual function",
  "EK 2.2.A.5 and 2.2.A.8 attach the two fixations to different things -- a strategy and an object. The first distractor swaps them. The third distractor is also substantively false: EK 2.2.A.5 presents mental set as arising from experiences that WERE successful, so it is not simply an impediment."),
 ("priming",
  "EK 2.2.A.5 lists priming among the circumstances surrounding a decision that influence it: an earlier exposure shapes a later response without intention. Nothing here is worded two ways, which is what rules out framing."),
 ("framing",
  "EK 2.2.A.5 lists framing among those circumstances: the identical information is evaluated differently according to how it is presented. The stem states that it is the same product, which is the clause that makes this framing rather than a real difference in the option."),
 ("priming is the influence of a prior exposure on a later response; framing is the influence of how the same information is worded",
  "EK 2.2.A.5 names both, and they operate by different routes -- earlier exposure versus presentation of identical facts. The first distractor reverses them."),
 ("generate, organize, plan, and carry out goal-directed behavior",
  "EK 2.2.A.7, near verbatim: executive functions are cognitive processes that allow individuals to generate, organize, plan, and carry out goal-directed behaviors and experience critical thinking."),
 ("generating many different possible ideas",
  "EK 2.2.A.8 contrasts divergent with convergent thinking within its account of creativity. The second option is the definition of convergent thinking, so the item turns on the direction of the contrast."),
 ("divergent thinking",
  "EK 2.2.A.8. An open-ended 'list every possible use' task calls for many outputs, which is the divergent side; a single-best-answer task would call for the convergent side, which item 25 supplies as its complement."),
 ("convergent thinking",
  "EK 2.2.A.8. Narrowing to the single defensible answer is the convergent side, and items 24 and 25 are adjacent so that the pair has to be known in both directions."),
 ("generating novel ideas and engaging in divergent thinking",
  "EK 2.2.A.8, near verbatim: creativity is a way of thinking that includes generating novel ideas and engaging in divergent versus convergent thinking."),
 ("mental set carried over from prior successes",
  "EK 2.2.A.5. The stem specifies MANY previous WINS with the opening, which is 'prior experiences that were successful' stated in the scenario. No object's function is at issue, ruling out functional fixedness, and the player is not continuing because of time already spent, ruling out sunk cost."),
 ("number of participants in each group who choose the option",
  "Science practice 2.B: the dependent variable is the measured outcome. The wording -- 90 percent survival versus 10 percent mortality, which are the same fact framed two ways per EK 2.2.A.5 -- is the manipulated independent variable."),
 ("makes the two groups comparable so a difference can be attributed to the wording",
  "Random assignment equalizes the groups on everything but the manipulation, which is what licenses a causal conclusion. Representing the general population is what random SAMPLING does; the two are routinely confused and the distractor is there for that reason."),
 ("people who already plan well may be the ones who choose to use the app",
  "Users selected themselves into the group, so the design is correlational and the influence may run the other way. EK 2.2.A.7 does place planning and organization inside executive functions, which is exactly why the causal reading is tempting rather than obviously wrong -- the flaw is in the design, not in the construct."),
]

psych_check.check(p2_2, CLAIMS, per_topic=30, n_choices=4)
