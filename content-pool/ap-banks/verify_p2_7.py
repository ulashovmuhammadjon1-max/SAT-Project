"""Key audit for AP PSYCHOLOGY 2.7 Forgetting and Other Memory Challenges.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on and, for each interference scenario, which material the stem says
was learned FIRST -- because that single fact decides the answer and nothing else
in the scenario does.

Three deliberate design decisions, recorded so they can be audited:

1. PROACTIVE vs RETROACTIVE is the most reversible pair in Unit 2, and a
   scenario that does not make the learning ORDER explicit has no determinate
   answer. Items 8, 9, 10 each state which came first, which came second, and
   which is now hard to retrieve:

        item 8   old password first, new password now hard    -> proactive
        item 9   old number first, new number learned, old
                 number now hard                              -> retroactive
        item 10  Spanish first, Italian now hard              -> proactive

   Item 11 then asks for the distinction with the reversed definition as its
   first distractor.

2. EK 2.7.A.2's three causes (encoding failure, interference, inadequate
   retrieval) are separated by WHERE the process broke down, and EK 2.7.A.4's
   three influences (misinformation effect, source amnesia, constructive memory)
   concern ACCURACY rather than loss. Item 23 tests that boundary directly, with
   all three of its distractors drawn from the other list.

3. REPRESSION is attributed, not asserted. EK 2.7.A.3 begins "Psychodynamic
   theorists believe", and the key in item 15 preserves that attribution rather
   than presenting repression as an established mechanism. Item 16 makes the
   difference in the framework's own wording the answer. This matters: a key
   that stated repression as fact would be teaching something the CED
   deliberately declines to state, and would also conflict with the exclusion of
   the psychoanalytic theory of dreams in EK 1.5.A.4.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p2_7

CLAIMS = [
 ("rapidly after initial learning and then levels off",
  "EK 2.7.A.1, near verbatim: the forgetting curve shows that time is a significant factor in forgetting; forgetting occurs rapidly after initial learning and levels off over time. The 'constant rate' distractor is the shape the curve specifically contradicts."),
 ("shortly after learning",
  "EK 2.7.A.1. If loss is rapid early and levels off later, the earliest interval carries the largest share of it -- this item asks for the consequence of the curve's shape rather than its description."),
 ("within the first hours and days after learning",
  "EK 2.7.A.1 applied to a week-long interval. 'A steady rate spread evenly across the week' is the intuitive but wrong answer, and it is the one the curve exists to correct."),
 ("never entered memory in a durable form",
  "EK 2.7.A.2 lists encoding failure among the reasons memories are difficult to retrieve. The break is at the point of getting information IN (Topic 2.4's process), which is what distinguishes it from the storage and retrieval failures in the other options."),
 ("encoding failure",
  "EK 2.7.A.2. Handling a coin thousands of times without ever attending to the head's orientation means that detail was never encoded; exposure is not encoding. Interference is excluded because no competing coin design was learned."),
 ("previously learned information makes it harder to retrieve newly learned",
  "EK 2.7.A.2 names proactive and retroactive interference. Proactive runs FORWARD in time from the older material onto the newer."),
 ("newly learned information makes it harder to retrieve previously learned",
  "EK 2.7.A.2. Retroactive runs BACKWARD from the newer material onto the older. Items 6 and 7 are adjacent so the pair must be known in both directions."),
 ("proactive interference",
  "EK 2.7.A.2. The stem establishes the order explicitly: the old password was learned first and is disrupting the NEW one, so the older material is interfering forward."),
 ("retroactive interference",
  "EK 2.7.A.2. The stem again fixes the order: the new number was learned second and the OLD one is now inaccessible, so the newer material is interfering backward. The mirror image of item 8."),
 ("proactive interference",
  "EK 2.7.A.2. Spanish was learned first, Italian second, and the Italian is what is hard -- the older material interfering forward. A third proactive case with different surface content, since one worked example is not enough for a pair students reliably reverse."),
 ("proactive interference is older material disrupting newer",
  "EK 2.7.A.2 names the two as directions of interference. The first distractor is that definition reversed; the last denies there is any directional difference, which is the whole content of the pair."),
 ("in memory but cannot be brought out",
  "EK 2.7.A.2 lists inadequate retrieval as a third cause, separate from encoding failure and interference, with tip-of-the-tongue as its example. The information exists -- which is what rules out both 'never encoded' and 'permanently erased'."),
 ("tip-of-the-tongue phenomenon",
  "EK 2.7.A.2 gives this as its own example of inadequate retrieval. Partial access -- knowing the first letter, feeling it is imminent -- is positive evidence that the memory was encoded and stored, so encoding failure is excluded by the stem rather than merely less attractive."),
 ("encoding failure",
  "EK 2.7.A.2 separates its three causes by where the process broke down. In tip-of-the-tongue the memory demonstrably exists; in encoding failure it never formed. This item asks for that comparison rather than for either term alone."),
 ("psychodynamic theorists believe",
  "EK 2.7.A.3, and the attribution is the point: the framework says psychodynamic theorists BELIEVE information can be forgotten to defend the ego from distress. The second option, which states repression as an established biological mechanism, is what a key must not assert -- the CED does not."),
 ("attributed to what psychodynamic theorists believe, while interference is presented as a documented cause",
  "The contrast is in the framework's own wording: EK 2.7.A.3 opens with 'Psychodynamic theorists believe', EK 2.7.A.2 states interference flatly. The item tests reading the CED's epistemic hedges, which is a real skill for this topic and connects to EK 1.5.A.4's exclusion of the psychoanalytic theory of dreams."),
 ("alteration of a memory by information encountered after the event",
  "EK 2.7.A.4 names the misinformation effect among the influences on the accuracy of memories. The distractors are change blindness (2.1.A.5.ii), the gambler's fallacy (2.2.A.6), and retrograde amnesia (2.5.A.4) -- all real course terms from other topics."),
 ("misinformation effect",
  "EK 2.7.A.4. The verb in the question is post-event information, and the reported memory shifts with it. Source amnesia is excluded because the witnesses do not misattribute where anything came from; the CONTENT of the memory changes."),
 ("remembering information while misremembering where it came from",
  "EK 2.7.A.4 names source amnesia among the accuracy influences. The content survives and the origin does not -- which is what separates it from the amnesias of EK 2.5.A.4, all three of which appear here as distractors."),
 ("source amnesia",
  "EK 2.7.A.4. The fact itself is retained accurately and only its origin is wrong, which is the defining feature; the misinformation effect would require the content to have been altered, and the stem says it was not."),
 ("assembled rather than replayed",
  "EK 2.7.A.4 lists constructive memory among the accuracy influences, operating via memory consolidation and imagination inflation. Both routes presuppose that a memory is built at retrieval rather than played back unchanged, which is what the second option denies."),
 ("vividly imagining an event can increase confidence that it actually happened",
  "EK 2.7.A.4 names imagination inflation as one route by which constructive memory affects accuracy. This is also the item that supplies the evidence used in item 28."),
 ("source amnesia",
  "EK 2.7.A.4 groups the misinformation effect, source amnesia, and constructive memory as influences on ACCURACY; EK 2.7.A.2 lists encoding failure, interference, and inadequate retrieval as causes of retrieval difficulty. All three distractors come from the 2.7.A.2 list, so the item tests which of the topic's two lists a term belongs to."),
 ("misinformation effect changes the content of a memory; source amnesia leaves the content but loses its origin",
  "EK 2.7.A.4 lists both, but one alters WHAT is remembered and the other WHERE it is believed to have come from. The first distractor reverses that; the third invents a restriction to eyewitnesses and students that the framework does not make."),
 ("whether the question contained the misleading detail",
  "Science practice 2.B: the independent variable is the manipulated condition. The memory measure is the dependent variable; the video and the delay are explicitly held constant, which is why they are neither."),
 ("difference in what was witnessed",
  "A confounding variable changes alongside the manipulation and offers a rival explanation. If the groups saw different videos, what they witnessed rather than what they were asked could produce the later difference."),
 ("number of details a participant reports that match the video",
  "An operational definition names the countable procedure. Matching reported details against a fixed question set is measurable; vividness and confidence are different constructs -- and EK 2.7.A.4's imagination inflation is the framework's own evidence that confidence can rise while accuracy does not."),
 ("confidence in an event can rise without the event having occurred",
  "Science practice 4.B. EK 2.7.A.4's imagination inflation directly severs confidence from accuracy, which is exactly the link the student's claim assumes. The other three options are true framework statements that bear on forgetting or retrieval rather than on the confidence-accuracy relationship."),
 ("misinformation effect, by which post-event information can alter a memory",
  "EK 2.7.A.4. Leading questions asked after the event ARE post-event information, so the misinformation effect is the mechanism the argument needs. Repression is offered as a distractor precisely because it is the framework's attributed-not-asserted item and would be a weak basis for an argument."),
 ("forgetting curve, which shows rapid loss soon after initial learning",
  "EK 2.7.A.1 makes time a significant factor in forgetting, with loss rapid after initial learning. The other three options concern memory ACCURACY or ENCODING; none of them speaks to what happens to successfully learned material as time passes, which is the teacher's actual claim."),
]

psych_check.check(p2_7, CLAIMS, per_topic=30, n_choices=4)
