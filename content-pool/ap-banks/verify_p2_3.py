"""Key audit for AP PSYCHOLOGY 2.3 Introduction to Memory.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on. There is no computation here, so the written claim IS the check.

The topic boundary is the thing to get right in this module, and it is enforced
by reading rather than by any mechanical test, so it is recorded here. Topic 2.3
is the MAP of memory -- its types, its structures, and the three models. The
pipeline stages have their own topics: encoding is 2.4, storage 2.5, retrieval
2.6, and the failures 2.7. So mnemonics, chunking, the spacing effect, the
serial position effect, storage capacities, retrieval cues and forgetting are
deliberately absent as keys here, even though several would fit comfortably in a
general memory bank. Items 21, 28 and 29 mention the neighbouring topics only as
distractors or as the source of a prediction, never as the answer.

The framework supplies four separate three-item lists in this one topic, and
they are exactly what a careless writer cross-contaminates. Item 3, 15, 22 and
27 test the lists against each other on purpose:

    memory types      episodic, semantic (explicit) / procedural (implicit)
                      / prospective
    working memory    central executive, phonological loop,
                      visuospatial sketchpad
    multi-store       sensory (iconic, echoic), short-term, long-term
    levels of proc.   structural, phonemic, semantic (shallowest to deepest)

Pairs tested in both directions because knowing one does not give the other:
episodic (an event you lived) vs semantic (general knowledge); iconic (visual)
vs echoic (auditory); phonological loop (verbal) vs visuospatial sketchpad
(visual/spatial); working memory model (components within one system) vs
multi-store model (systems passed through in sequence).

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p2_3

CLAIMS = [
 ("more easily described or explained to others",
  "EK 2.3.A.1.i, verbatim: explicit memory is a type of memory that is more easily described or explained to others. The framework defines it by reportability, not by content, which is why the key is worded that way."),
 ("more challenging to describe or explain to others",
  "EK 2.3.A.1.ii, verbatim. Paired with item 1 so the explicit/implicit contrast is defined from both sides."),
 ("episodic and semantic",
  "EK 2.3.A.1.i names episodic and semantic as the types of explicit memory. The distractors are drawn from the other three-item lists in this topic -- implicit/prospective types, the sensory stores, and the levels of processing -- so the item tests which list a term belongs to."),
 ("episodic memory",
  "EK 2.3.A.1.i lists episodic among the explicit types; it is memory for a personally experienced event. Paired against item 5, which supplies general knowledge instead."),
 ("semantic memory",
  "EK 2.3.A.1.i lists semantic among the explicit types; it is general knowledge with no personal event attached. A capital city is knowledge the person did not have to witness."),
 ("procedural memory",
  "EK 2.3.A.1.ii: procedural memory is a type of implicit memory for procedures and processes. A practised motor skill performed without conscious attention to its steps is that definition acted out."),
 ("prospective memory",
  "EK 2.3.A.1.iii: prospective memory is a type of memory related to future actions. It is the only one of the four types that points forward in time, which is what the stem supplies."),
 ("tying a shoelace without thinking about the steps",
  "EK 2.3.A.1.ii. This is the matching item: each of the three distractors attaches a memory type to ANOTHER type's example (semantic to an episode, episodic to a fact, prospective to a past experience), so it cannot be answered by recognising one label."),
 ("strengthening of synaptic connections between neurons",
  "EK 2.3.A.2, near verbatim: long-term potentiation is a process by which synaptic connections between neurons become stronger with frequent activation."),
 ("biological mechanism at the level of the connections between neurons",
  "EK 2.3.A.2 calls long-term potentiation a BIOLOGICAL process for memory, which is its significance -- it links Unit 2's models to the neural transmission of Topic 1.3. The 'single location' distractor is a claim the EK does not make, and the serial position distractor belongs to Topic 2.4."),
 ("central executive",
  "EK 2.3.A.3 names the central executive, phonological loop, and visuospatial sketchpad as working memory's components; the central executive is the coordinating one. 'Sensory register' is offered as a distractor because it belongs to the multi-store model instead."),
 ("phonological loop",
  "EK 2.3.A.3. The phonological loop is working memory's verbal and sound-based component, which silent rehearsal of digits uses. Paired against item 13, its visual counterpart."),
 ("visuospatial sketchpad",
  "EK 2.3.A.3. The visuospatial sketchpad is working memory's visual and spatial component; mentally inspecting a remembered layout uses it rather than the verbal loop."),
 ("dynamic system with several interacting components",
  "EK 2.3.A.3: working memory engages in a dynamic interaction with several components to process information into long-term memory. The 'single container holding seven items' distractor is the popular short-term-memory picture the working memory model was proposed to replace."),
 ("sensory memory, short-term memory, and long-term memory",
  "EK 2.3.A.4 names exactly these three interacting systems. Each distractor is one of this topic's OTHER three-item lists, which is the whole point of the item."),
 ("sensory memory",
  "EK 2.3.A.4 places iconic and echoic memory inside sensory memory, the first of the multi-store systems."),
 ("iconic memory",
  "EK 2.3.A.4 includes iconic memory within sensory memory; it is the visual store. A lingering visual impression after the light stops is the standard case."),
 ("echoic memory",
  "EK 2.3.A.4 includes echoic memory within sensory memory; it is the auditory store. Repeating back words you were not attending to is the standard demonstration."),
 ("iconic memory is the brief visual store",
  "EK 2.3.A.4 lists both within sensory memory, separated only by modality. The first distractor is that separation reversed; the remaining two misplace them in the model."),
 ("encoding, storage, and retrieval",
  "EK 2.3.A.4: the multi-store model focuses on the impact of automatic and effortful processing on memory encoding, storage, and retrieval. Those three words are also the names of Topics 2.4, 2.5 and 2.6, which is why the framework introduces them here."),
 ("automatic and effortful processing",
  "EK 2.3.A.4 pairs automatic and effortful processing as the two modes the multi-store model examines. The distractors are drawn from Topic 2.4 (primacy/recency) and elsewhere in this topic, so all four options are real course terms."),
 ("structural, phonemic, semantic",
  "EK 2.3.A.5, verbatim in order: three levels from shallowest to deepest, structural then phonemic then semantic. The first distractor is the same list reversed, so the item tests the ORDER and not just the membership."),
 ("structural",
  "EK 2.3.A.5 makes structural the shallowest level. Attending only to a word's physical form -- its case -- is structural processing by definition."),
 ("phonemic",
  "EK 2.3.A.5 places phonemic between structural and semantic. A rhyme judgment requires the word's sound but not its meaning, which is what puts it at the middle level."),
 ("semantic",
  "EK 2.3.A.5 makes semantic the deepest level. Judging whether a word fits a sentence requires its meaning."),
 ("fits meaningfully into a sentence",
  "EK 2.3.A.5 orders the levels shallowest to deepest and the model's claim is that deeper processing yields better retention, so the semantic task should win. Items 23-25 establish which task is which level, and this item is the one that requires the model's PREDICTION rather than just its taxonomy."),
 ("divides the primary memory system into interacting components; the multi-store model describes three systems information passes through",
  "EK 2.3.A.3 versus EK 2.3.A.4. The two models are not rivals in the framework's presentation but they answer different questions, and the first distractor is this contrast with the two halves swapped. The 'identical claims' distractor is false because the models decompose memory along different axes."),
 ("experiment, because the study method was manipulated and randomly assigned",
  "Science practice 2.A: a manipulated, randomly assigned independent variable is what defines an experiment. The distractors attach the label to features that are irrelevant to the classification -- how many variables are measured, where studying happened, how many lists were used."),
 ("levels of processing model",
  "EK 2.3.A.5 ranks semantic processing deepest and structural shallowest, and the two study conditions in item 28 are exactly a semantic task and a structural one. The working memory model and long-term potentiation make no prediction about which of two study instructions produces better recall."),
 ("implicit and explicit memory",
  "EK 2.3.A.1.i and 2.3.A.1.ii define the pair by whether the memory can be described to others. A retained skill that cannot be reported is that distinction demonstrated within a single patient, which is why the pattern is evidence for the distinction rather than merely consistent with it."),
]

psych_check.check(p2_3, CLAIMS, per_topic=30, n_choices=4)
