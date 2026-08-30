"""Key audit for AP PSYCHOLOGY 2.5 Storing Memories.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on and, where the item could be read two ways, the clause in the stem
that closes the second reading.

Three things about this topic drove the item design and are recorded so they can
be audited rather than assumed:

1. EK 2.5.A.1 names exactly three dimensions on which the stores differ --
   DURATION, CAPACITY, CONTENT -- and does not assign numbers to any of them. So
   no item here keys a specific capacity or a specific number of seconds. Item 27
   makes that restraint the answer: a student who has absorbed "seven items" or
   "unlimited capacity" from outside material is asked to notice that the
   framework claims neither.

2. Rehearsal sits in 2.5.A.2 under STORAGE, not under encoding, even though many
   students meet it as an encoding strategy. Items 5-8 and 29 follow the
   framework's placement rather than the intuitive one. Similarly, the
   misinformation effect belongs to EK 2.7.A.4 (accuracy) and not here; item 18
   tests exactly that boundary.

3. The CED's suggested skill for this topic is 2.C, NON-experimental design, and
   the reason is substantive: amnesia and Alzheimer's disease cannot be assigned
   to anyone. Items 19-23 are therefore about case studies and group comparisons,
   and item 21 makes the impossibility of assignment the point rather than a
   throwaway limitation.

Pairs tested in both directions: retrograde (memories from BEFORE the event) vs
anterograde (forming memories AFTER it) -- items 11-15, where each scenario
states that the other direction is intact so exactly one answer fits;
maintenance rehearsal (repetition) vs elaborative rehearsal (meaning).

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p2_5

CLAIMS = [
 ("storage duration, capacity, and content",
  "EK 2.5.A.1, verbatim: sensory memory, short-term memory, working memory, and long-term memory are processes that differ in storage duration, capacity, and content. Those three dimensions are the whole of what the framework asserts about how the stores differ."),
 ("sensory memory",
  "EK 2.5.A.1 makes duration one of the distinguishing dimensions, and EK 2.3.A.4 places iconic and echoic memory inside sensory memory as the brief post-stimulus stores. Sensory memory is the shortest of the four."),
 ("long-term memory",
  "EK 2.5.A.1 distinguishes the stores by capacity and duration; long-term memory sits at the far end of both. The framework does not say 'unlimited', and the key does not either -- it says greatest, which is a comparison among the four."),
 ("sensory memory's duration",
  "EK 2.5.A.1. More is available momentarily than can be reported before it fades, which is a limit of how LONG the impression lasts rather than of how much it holds -- the item is keyed to duration specifically, and 'long-term memory's capacity' is offered as the wrong dimension."),
 ("repeating information over time in order to prolong its storage",
  "EK 2.5.A.2: storage may be prolonged by rehearsing information over time, which the framework calls maintenance rehearsal. Note that the framework files rehearsal under STORAGE, not encoding."),
 ("promote meaning",
  "EK 2.5.A.2: rehearsing information over time in ways that promote meaning is elaborative rehearsal, and it helps with memory retention. The distractors are maintenance rehearsal, the spacing effect (2.4.A.4), and method of loci (2.4.A.2)."),
 ("maintenance rehearsal repeats the material; elaborative rehearsal connects it to meaning",
  "EK 2.5.A.2 separates the two solely by whether the rehearsal promotes meaning. The first distractor is that separation reversed, which is the error a student who knows both labels but not which is which will make."),
 ("elaborative rehearsal, which helps with memory retention",
  "EK 2.5.A.2 says of elaborative rehearsal specifically that it helps with memory retention -- the framework's own comparison, not an inference. The second distractor attributes that advantage to maintenance rehearsal, which reverses the EK."),
 ("biological processes for superior memory storage",
  "EK 2.5.A.3, near verbatim: some people demonstrate highly superior autobiographical memory, which MAY indicate that there are biological processes for superior memory storage. The framework's hedge is preserved in the key; the distractors each overclaim."),
 ("connected to a person's own life or self are more memorable",
  "EK 2.5.A.3's second sentence: autobiographical memory may also explain why memories connected to our own lives or selves are more memorable. The distractors are the serial position effect (2.4.A.5) and retrieval phenomena from 2.6, so all are real course content placed in the wrong topic."),
 ("before the injury or onset",
  "EK 2.5.A.4 names retrograde and anterograde amnesia as storage impairments. Retrograde looks backward: what was already stored is lost."),
 ("after the injury or onset",
  "EK 2.5.A.4. Anterograde looks forward: new memories cannot be formed. Items 11 and 12 are adjacent so the pair must be known in both directions rather than by elimination."),
 ("retrograde amnesia",
  "EK 2.5.A.4. The stem states BOTH halves -- two years lost before the crash, and normal new memory formation after it -- so anterograde is positively excluded rather than merely less attractive."),
 ("anterograde amnesia",
  "EK 2.5.A.4. Again both halves are stated: childhood and career intact, no memory of anyone met since onset. The mirror image of item 13, and the pairing is deliberate."),
 ("retrograde affects memories from before the event; anterograde affects the formation of memories after it",
  "EK 2.5.A.4 distinguishes the two by direction in time relative to the injury. The first distractor reverses it; the third and fourth assert distinctions (permanence, skills versus facts) that the framework does not make."),
 ("adults to recall events from the earliest years of life",
  "EK 2.5.A.4 lists infantile amnesia among DEVELOPMENTAL LIMITATIONS on storage, alongside the physical impairments. It names an ordinary feature of development, not an injury -- which is what item 28 turns on."),
 ("physical impairment that negatively affects storage",
  "EK 2.5.A.4: storage processes may be negatively affected by physical impairment and developmental limitations, such as amnesia, Alzheimer's disease, and infantile amnesia."),
 ("misinformation effect",
  "EK 2.5.A.4's list is amnesia (retrograde and anterograde), Alzheimer's disease, and infantile amnesia. The misinformation effect belongs to EK 2.7.A.4, which concerns the ACCURACY of memories rather than the storage process -- this item tests the 2.5/2.7 boundary, and the three distractors are all genuinely on the 2.5.A.4 list."),
 ("a case study",
  "Science practice 2.C, non-experimental design: intensive study of a single individual over time is a case study. Nothing is manipulated, so it is not an experiment."),
 ("one unusual case may not generalize",
  "Generalizability is the standard limit of a single-case design. The remaining options misdescribe case studies -- they can be observed repeatedly, they produce detail rather than lacking it, and random assignment belongs to experiments."),
 ("cannot ethically or practically assign anyone to develop the disease",
  "An experiment requires a manipulated, randomly assigned independent variable. A disease cannot be assigned, which is precisely why the CED attaches non-experimental design (2.C) to this topic rather than experimental design."),
 ("two groups differ, though the illness has not been shown to be the sole cause",
  "Group membership was measured, not assigned, so the design is non-experimental. A difference between pre-existing groups establishes an association; other differences between the groups remain live explanations."),
 ("number of seconds after which fewer than half the letters are correctly reported",
  "An operational definition names the measurement procedure. A time criterion tied to a stated accuracy level is measurable; 'seems to be', 'general ability', and 'found it difficult' restate the construct or measure something else."),
 ("how the material has been organized into units",
  "EK 2.5.A.1 makes capacity one of the dimensions distinguishing the stores, and EK 2.4.A.3's chunking establishes that what counts as ONE unit is not fixed. So a capacity stated in items depends on the organisation of the material -- which is why the framework never fixes a number."),
 ("actively manipulates a small amount of information",
  "EK 2.3.A.3 describes working memory as a dynamic system of interacting components, while EK 2.3.A.4 places sensory memory as the brief first store; EK 2.5.A.1 says the stores differ in duration, capacity, and content. Active processing versus passive brief holding is that contrast. The 'shorter time than sensory memory' distractor is false in the other direction."),
 ("sensory memory \u2014 very brief duration",
  "EK 2.5.A.1's three dimensions applied to sensory memory. Each distractor attaches one store's properties to a different store, so the item requires the whole table rather than one row."),
 ("differing in capacity without claiming that any is literally unlimited",
  "EK 2.5.A.1 says only that the stores differ in duration, capacity, and content. It assigns no numbers and asserts no unlimited store, so both 'unlimited' and 'exactly seven' are claims the framework does not make -- this item is deliberately about what the CED does NOT say, since that is where outside material misleads students."),
 ("infantile amnesia makes the absence of such memories ordinary",
  "EK 2.5.A.4 lists infantile amnesia among developmental limitations, which makes the absence of very early memories normal rather than a sign of injury. The retrograde-amnesia distractor is attractive because it also concerns memories from before a time point, but it requires an injury the stem never mentions."),
 ("promotes meaning, which the framework identifies as what helps retention",
  "EK 2.5.A.2 attributes the advantage specifically to rehearsal that promotes MEANING. The 'takes more total time' distractor is the plausible but wrong mechanism -- the framework's account is about the kind of processing, not its duration."),
 ("implicit procedural memory being spared while explicit memory is impaired",
  "EK 2.5.A.4 places anterograde amnesia among storage impairments; EK 2.3.A.1.i and 2.3.A.1.ii distinguish explicit memory (reportable) from implicit procedural memory (not). Improving at a skill while denying ever having practised is that dissociation observed in one person, which is why the case is evidence for the distinction rather than merely consistent with it."),
]

psych_check.check(p2_5, CLAIMS, per_topic=30, n_choices=4)
