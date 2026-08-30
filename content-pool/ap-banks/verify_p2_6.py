"""Key audit for AP PSYCHOLOGY 2.6 Retrieving Memories.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on and, for every scenario item, the clause in the stem that rules out
the neighbouring effect.

EK 2.6.A.2 names THREE matching conditions in one sentence -- environmental space
(context-dependent), mood (mood-congruent), and physical state (state-dependent).
They are the three most confusable terms in Unit 2 because they share a form
("retrieval improves when X matches"), and a scenario that fails to specify which
X is varied has more than one defensible answer. Every scenario item here
therefore varies exactly one of the three and leaves the other two unmentioned,
and the claim below says which:

    item 10  room changes; mood and physical state not mentioned  -> context
    item 11  emotional state changes; room and body not mentioned -> mood
    item 12  fatigue changes; room and mood not mentioned         -> state

Items 13 and 14 then test the pairs head-on, each with the correct contrast
reversed as its first distractor, so a student who knows the three labels but not
which is which cannot pass by elimination.

Two smaller traps worth recording. Item 19's last distractor asserts that
recognition is not a kind of retrieval, which is false by EK 2.6.A.1 -- recall and
recognition are the two forms retrieval takes. And item 23 turns on the fact that
an EXPERIMENT with random assignment licenses a causal conclusion: the
"association only" answer is right for item 24's correlational study and wrong
here, so the two are placed adjacently on purpose. Being cautious is not
automatically correct.

The CED's suggested skills for this topic are 3.A and 3.C, data identification
and interpretation. Items 22 and 23 state small results in prose. There are no
figures in this bank, so nothing refers to a graph.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p2_6

CLAIMS = [
 ("getting information out of memory",
  "Learning objective 2.6.A is worded as explaining how memory retrieval processes get information OUT of memory. The distractors are encoding (2.4), storage (2.5), and forgetting (2.7), so the item fixes this topic's place in the four-topic memory sequence."),
 ("remembering without cues",
  "EK 2.6.A.1, verbatim: retrieval occurs through recall (remembering without cues) or recognition (which relies on retrieval cues)."),
 ("relies on retrieval cues",
  "EK 2.6.A.1, verbatim for recognition. Paired with item 2 so the definition is available from both sides."),
 ("recall proceeds without cues, while recognition relies on cues",
  "EK 2.6.A.1 separates the two solely by the presence of retrieval cues. The first distractor is that separation reversed; the third invents a modality restriction the framework does not make."),
 ("recall",
  "EK 2.6.A.1: recall is remembering without cues. A blank page supplies no options, so nothing is available to recognise."),
 ("recognition",
  "EK 2.6.A.1: recognition relies on retrieval cues, and four printed options ARE those cues. Items 5 and 6 are the same exam described two ways so the pair cannot be answered from one remembered word."),
 ("environmental space",
  "EK 2.6.A.2 attaches context-dependent memory to being in the same environmental space at retrieval as at encoding. The other two distractors are the OTHER two conditions named in the same sentence of the same EK, which is what makes the item a real discrimination."),
 ("mood as when the information was encoded",
  "EK 2.6.A.2 attaches mood-congruent memory to being in the same mood. Again the distractors are the sibling conditions from the same sentence."),
 ("physical state",
  "EK 2.6.A.2 attaches state-dependent memory to being in the same physical state. Items 7-9 cover the three conditions of one EK sentence, one item each."),
 ("context-dependent memory",
  "EK 2.6.A.2. The stem varies the ROOM only; the student's mood and physical condition are deliberately not mentioned, so mood-congruent and state-dependent memory are excluded by the absence of any variation in what they concern."),
 ("mood-congruent memory",
  "EK 2.6.A.2. The stem varies EMOTIONAL state only -- no change of room and no physical condition -- so the other two conditions have nothing to act on."),
 ("state-dependent memory",
  "EK 2.6.A.2. Fatigue is a physical condition, not a location and not an emotion, so the stem varies only the state-dependent condition. The serial position distractor comes from Topic 2.4 and concerns list position, which the stem never varies."),
 ("external surroundings; state-dependent memory concerns the person's physical condition",
  "EK 2.6.A.2 lists environmental space and physical state as two distinct matching conditions. The first distractor reverses them; the last collapses both into mood, which is the third condition in the same sentence."),
 ("emotional state at encoding and retrieval; context-dependent memory concerns the physical surroundings",
  "EK 2.6.A.2 lists mood and environmental space as distinct. The first distractor reverses them; the remaining two add restrictions -- 'only in people who are sad', 'only during recognition tasks' -- that the framework nowhere states."),
 ("retrieving material in a practice test improves later retention",
  "EK 2.6.A.3 names the testing effect among the retrieval practice processes that make successful retrieval more likely. The mechanism the framework points to is the act of retrieval during practice, not the length or format of the test."),
 ("close the book and try to retrieve the material without looking",
  "EK 2.6.A.3: successful retrieval is more likely when using retrieval practice processes. Rereading, highlighting, and recopying all leave the material in front of the student, so none of them requires a retrieval attempt -- the item turns on that shared property of the three distractors."),
 ("thinking about one's own thinking",
  "EK 2.6.A.3 names metacognition alongside the testing effect as a retrieval practice process. It is the monitoring of one's own knowledge, which is what lets a learner decide what still needs study."),
 ("metacognition",
  "EK 2.6.A.3. Judging which sections she could and could not explain is monitoring her own knowledge, not rehearsing (2.5.A.2), regrouping (2.4.A.3), or choosing among options (2.6.A.1)."),
 ("no retrieval attempt, and retrieval practice is what improves later retrieval",
  "EK 2.6.A.3 attributes the benefit to retrieval practice specifically, so a strategy that never requires retrieval does not engage the mechanism. The final distractor is substantively FALSE -- EK 2.6.A.1 makes recognition one of the two forms of retrieval -- and is included because it is the kind of half-remembered claim that sounds technical."),
 ("recognition of the material is better than her recall",
  "EK 2.6.A.1. Succeeding with options present and failing without them is precisely the cued/uncued difference. It also shows the material WAS encoded, which is what rules out the third option."),
 ("context-dependent memory",
  "EK 2.6.A.2. The only stated difference between the two testing conditions is the environmental space, and the direction of the result -- better in the matching room -- is what the effect predicts. The misinformation effect (2.7.A.4) and maintenance rehearsal (2.5.A.2) are real terms from other topics."),
 ("difference in mean recall between the two testing conditions",
  "Science practice 3.A/3.C. The stem states both figures as AVERAGES, so their difference is a difference in means. Standard deviation, percentile rank, and range are different statistics that cannot be computed from two means -- the item is about naming what a reported number is, which is what 3.A asks."),
 ("practice testing caused better performance",
  "Random assignment to a manipulated condition is what licenses a causal conclusion, so the cautious 'association only' answer is WRONG here. This item is placed immediately before item 24, which is correlational and where that same cautious answer is right; a student who applies caution reflexively rather than to the design will get exactly one of the pair wrong."),
 ("not assigned their study habits, so a third variable",
  "Study habits were self-reported, not assigned, so the design is correlational and motivation or conscientiousness could produce both. EK 2.6.A.3 does support retrieval practice, which is what makes the causal reading tempting -- the flaw is in this study's design, not in the claim."),
 ("tested in the same room in which they studied",
  "Science practice 2.B: the independent variable is the manipulated condition, the match or mismatch of environments. The recall count is the dependent variable, and list length and age are held constant or unmanipulated."),
 ("difficulty of the lists, rather than the environment, could explain",
  "A confounding variable changes alongside the manipulation and offers a rival explanation. Equating the list across groups removes list difficulty as an account of any difference in recall."),
 ("number of studied words a participant writes down correctly within three minutes",
  "An operational definition names the countable procedure. 'Seems to remember', 'overall memory ability', and 'felt the test went well' are unmeasurable as stated or measure confidence rather than performance."),
 ("may not represent the wider population",
  "Generalizability depends on the sample resembling the population the claim is about. The last distractor is included because it is a common confusion: where participants are recruited affects generalizability, not whether the design is experimental or correlational."),
 ("environmental space matches the one in which encoding occurred",
  "Science practices 4.A and 4.B: a defensible claim needs reasoning grounded in psychology-derived evidence. Only EK 2.6.A.2's context-dependent memory bears on whether matching the study and exam rooms should help; the other three options are accurate statements of framework content that are simply irrelevant to this claim."),
 ("advantage when the retrieval environment matches the encoding environment",
  "EK 2.6.A.2 predicts a benefit from matching environments, so deliberately varying the study room removes a cue that could support retrieval in the exam room. The other three options are true framework statements about retrieval that say nothing about WHERE studying happens, which is what the advice concerns."),
]

psych_check.check(p2_6, CLAIMS, per_topic=30, n_choices=4)
