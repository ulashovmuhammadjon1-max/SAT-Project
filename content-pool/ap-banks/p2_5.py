# AP PSYCHOLOGY 2.5 Storing Memories — 30 questions
# CED effective Fall 2024/2025, Unit 2 Cognition. Learning objective 2.5.A.
#
# Essential knowledge relied on: 2.5.A.1 sensory, short-term, working, and
# long-term memory as processes that differ in storage DURATION, CAPACITY, and
# CONTENT; 2.5.A.2 maintenance rehearsal (repeating over time) versus elaborative
# rehearsal (rehearsing in ways that promote meaning, which helps retention);
# 2.5.A.3 highly superior autobiographical memory, and autobiographical memory as
# an account of why self-connected material is more memorable; 2.5.A.4 storage
# impaired by retrograde and anterograde amnesia, Alzheimer's disease, and
# infantile amnesia.
#
# Topic boundary: 2.5 is STORAGE -- what is held, for how long, how much, and what
# damages the holding. Getting information in is Topic 2.4 and getting it out is
# Topic 2.6, so encoding strategies and retrieval cues appear here only as
# distractors. The one place the line is genuinely thin is rehearsal, which the
# framework places in 2.5.A.2 under storage even though a student may think of it
# as encoding; items 8-12 follow the framework's placement.
#
# The CED's suggested skill 2.C for this topic is non-experimental design, so the
# research items concern case studies and correlational work rather than
# experiments -- amnesia and Alzheimer's cannot be assigned to anyone.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p2_5.py.
TOPIC = ("2.5", "Storing Memories", 2)
QUESTIONS = [
 dict(q="According to the AP Psychology framework, sensory memory, short-term memory, working memory, and long-term memory differ from one another in", choices=[
   "storage duration, capacity, and content",
   "which hemisphere of the brain holds them",
   "whether they involve neurons at all",
   "how many people can access them"], ans=0,
   why="EK 2.5.A.1 states that sensory memory, short-term memory, working memory, and long-term memory are processes that differ in storage duration, capacity, and content."),
 dict(q="Which memory store holds information for the SHORTEST time?", choices=[
   "sensory memory",
   "short-term memory",
   "working memory",
   "long-term memory"], ans=0,
   why="EK 2.5.A.1 distinguishes the stores by duration, and sensory memory -- which EK 2.3.A.4 subdivides into iconic and echoic -- holds information only briefly after the stimulus ends."),
 dict(q="Which memory store is described as having the greatest capacity and the longest duration?", choices=[
   "long-term memory",
   "sensory memory",
   "short-term memory",
   "working memory"], ans=0,
   why="EK 2.5.A.1 distinguishes the stores by capacity and duration; long-term memory is the store at the far end of both dimensions."),
 dict(q="A student glances at a page of text and, for a moment afterward, can still \"see\" more of it than she can report before the impression fades. This illustrates the limits of", choices=[
   "sensory memory's duration",
   "long-term memory's capacity",
   "elaborative rehearsal",
   "anterograde amnesia"], ans=0,
   why="EK 2.5.A.1 makes duration one of the dimensions that distinguish the stores, and a visual impression that fades before it can be reported is the duration limit of sensory memory."),
 dict(q="Maintenance rehearsal is best described as", choices=[
   "repeating information over time in order to prolong its storage",
   "connecting information to its meaning and to what is already known",
   "grouping information into meaningful units",
   "retrieving information without any cues"], ans=0,
   why="EK 2.5.A.2 states that storage may be prolonged by rehearsing information over time, which it calls maintenance rehearsal."),
 dict(q="Elaborative rehearsal is best described as", choices=[
   "rehearsing information in ways that promote meaning",
   "repeating information verbatim until it is needed",
   "spreading study sessions across several days",
   "attaching each item to a location along a familiar route"], ans=0,
   why="EK 2.5.A.2 states that rehearsing information over time in ways that promote meaning is elaborative rehearsal, and that it helps with memory retention."),
 dict(q="Which statement correctly distinguishes maintenance rehearsal from elaborative rehearsal?", choices=[
   "maintenance rehearsal repeats the material; elaborative rehearsal connects it to meaning",
   "elaborative rehearsal repeats the material; maintenance rehearsal connects it to meaning",
   "maintenance rehearsal is used for images and elaborative rehearsal for words",
   "the two terms describe the same process at different speeds"], ans=0,
   why="EK 2.5.A.2 separates the two by whether the rehearsal promotes meaning; the first distractor is that separation reversed."),
 dict(q="A student repeats a definition word for word twenty times. A second student explains the same definition in her own words and links it to an example from her own life. According to the framework, the second student's approach", choices=[
   "is elaborative rehearsal, which helps with memory retention",
   "is maintenance rehearsal, which is more effective for retention",
   "will produce worse retention because it takes longer",
   "makes no difference, since both students spent the same time"], ans=0,
   why="EK 2.5.A.2 identifies rehearsal that promotes meaning as elaborative rehearsal and states that it helps with memory retention, which is the framework's own comparison between the two forms."),
 dict(q="Highly superior autobiographical memory is significant to the study of memory because it", choices=[
   "may indicate that there are biological processes for superior memory storage",
   "shows that everyone can be trained to remember every day of their life",
   "demonstrates that long-term memory has no capacity limit",
   "proves that autobiographical memories are always accurate"], ans=0,
   why="EK 2.5.A.3 states that some people demonstrate highly superior autobiographical memory, which may indicate that there are biological processes for superior memory storage."),
 dict(q="According to the AP Psychology framework, autobiographical memory may also explain why", choices=[
   "memories connected to a person's own life or self are more memorable",
   "the first items on a list are recalled better than the middle items",
   "a familiar smell can trigger a memory",
   "information rehearsed aloud is remembered longer"], ans=0,
   why="EK 2.5.A.3 states that autobiographical memory may explain why memories connected to our own lives or selves are more memorable; the distractors are the serial position effect and retrieval phenomena from other topics."),
 dict(q="Retrograde amnesia is best described as the loss of", choices=[
   "memories formed before the injury or onset",
   "the ability to form new memories after the injury or onset",
   "the ability to speak fluently",
   "the ability to recognize familiar faces"], ans=0,
   why="EK 2.5.A.4 names retrograde and anterograde amnesia as impairments of storage; retrograde is the backward-looking one, affecting what was already stored."),
 dict(q="Anterograde amnesia is best described as the loss of", choices=[
   "the ability to form new memories after the injury or onset",
   "memories formed before the injury or onset",
   "the ability to perform previously learned skills",
   "the ability to perceive depth"], ans=0,
   why="EK 2.5.A.4 names retrograde and anterograde amnesia; anterograde is the forward-looking one, affecting the formation of memories after the event."),
 dict(q="A man in a car accident can recall nothing from the two years before the crash but forms new memories normally afterward. This pattern is", choices=[
   "retrograde amnesia",
   "anterograde amnesia",
   "infantile amnesia",
   "source amnesia"], ans=0,
   why="EK 2.5.A.4's retrograde amnesia affects material stored before the event, which is exactly what the two lost years describe, while new memory formation is stated to be intact."),
 dict(q="A woman recalls her childhood and career clearly but cannot remember anyone she has met since her illness began. This pattern is", choices=[
   "anterograde amnesia",
   "retrograde amnesia",
   "infantile amnesia",
   "the misinformation effect"], ans=0,
   why="EK 2.5.A.4's anterograde amnesia affects the formation of memories after onset, which is what failing to remember post-illness acquaintances describes, while pre-illness memory is stated to be intact."),
 dict(q="Which statement correctly distinguishes retrograde from anterograde amnesia?", choices=[
   "retrograde affects memories from before the event; anterograde affects the formation of memories after it",
   "anterograde affects memories from before the event; retrograde affects the formation of memories after it",
   "retrograde is temporary and anterograde is always permanent",
   "retrograde affects skills and anterograde affects facts"], ans=0,
   why="EK 2.5.A.4 names both as storage impairments distinguished by their direction in time relative to the injury; the first distractor is that distinction reversed."),
 dict(q="Infantile amnesia refers to", choices=[
   "the general inability of adults to recall events from the earliest years of life",
   "an injury in infancy that erases memories formed in adulthood",
   "the loss of language ability in early childhood",
   "a child's failure to recognize a parent"], ans=0,
   why="EK 2.5.A.4 lists infantile amnesia among the developmental limitations that negatively affect storage; it names the ordinary absence of memories from the earliest years rather than a pathology."),
 dict(q="Alzheimer's disease is included in the AP Psychology framework's account of memory because it", choices=[
   "is a physical impairment that negatively affects storage processes",
   "is an example of a mnemonic device that fails",
   "shows that retrieval cues are unnecessary",
   "demonstrates the accuracy of constructive memory"], ans=0,
   why="EK 2.5.A.4 states that storage processes may be negatively affected by physical impairment and developmental limitations, and lists Alzheimer's disease among them."),
 dict(q="Which of the following is NOT named in the AP Psychology framework as a condition that negatively affects memory STORAGE?", choices=[
   "the misinformation effect",
   "retrograde amnesia",
   "Alzheimer's disease",
   "infantile amnesia"], ans=0,
   why="EK 2.5.A.4 lists amnesia (retrograde and anterograde), Alzheimer's disease, and infantile amnesia; the misinformation effect belongs to EK 2.7.A.4, which concerns the ACCURACY of memories rather than the storage process."),
 dict(q="A researcher studies a single patient with a rare pattern of memory loss in great depth over many years. This design is", choices=[
   "a case study",
   "an experiment",
   "a correlational survey",
   "a naturalistic observation of a group"], ans=0,
   why="Science practice 2.C concerns non-experimental designs; intensive study of one individual is a case study, and no variable is manipulated."),
 dict(q="The main limitation of using a single amnesia patient to draw conclusions about memory in general is that", choices=[
   "one unusual case may not generalize to other people",
   "a single patient cannot be observed more than once",
   "case studies cannot produce any detailed information",
   "case studies require random assignment to be interpretable"], ans=0,
   why="Generalizability is the standard limit of a single-case design; depth of description is its strength, and random assignment belongs to experiments rather than to case studies."),
 dict(q="Why can the effect of Alzheimer's disease on memory not be studied with a true experiment?", choices=[
   "researchers cannot ethically or practically assign anyone to develop the disease",
   "memory cannot be measured in people who have the disease",
   "the disease has no measurable effect on behavior",
   "experiments cannot include a comparison group"], ans=0,
   why="An experiment requires a manipulated, randomly assigned independent variable; a disease cannot be assigned, so this question is necessarily addressed with non-experimental designs, which is science practice 2.C's subject."),
 dict(q="A study compares the memory test scores of adults who have a particular illness with those of adults who do not, and finds a large difference. The strongest conclusion available is that", choices=[
   "the two groups differ, though the illness has not been shown to be the sole cause",
   "the illness causes the difference in scores",
   "memory tests are invalid for people with the illness",
   "no relationship exists between the illness and memory"], ans=0,
   why="Group membership was measured rather than assigned, so the design is non-experimental; a difference between pre-existing groups establishes an association and leaves other differences between the groups as live explanations."),
 dict(q="A researcher wants to describe how long participants can hold a string of letters without rehearsing. The best operational definition of the outcome is", choices=[
   "the number of seconds after which fewer than half the letters are correctly reported",
   "how good the participant's short-term memory seems to be",
   "the participant's general memory ability",
   "whether the participant found the task difficult"], ans=0,
   why="An operational definition names the specific measurement procedure; a stated time criterion tied to a stated accuracy level is measurable, while the alternatives restate the construct."),
 dict(q="A person can hold about seven unrelated digits in mind at once but can hold far more digits when they form familiar dates. This shows that capacity limits depend partly on", choices=[
   "how the material has been organized into units",
   "the duration of sensory memory",
   "whether the person has anterograde amnesia",
   "whether retrieval is by recall or recognition"], ans=0,
   why="EK 2.5.A.1 makes capacity one of the dimensions on which the stores differ, and EK 2.4.A.3's chunking shows that what counts as one unit is not fixed, so capacity in items depends on how the material is grouped."),
 dict(q="Working memory differs from sensory memory principally in that working memory", choices=[
   "actively manipulates a small amount of information rather than briefly holding a sensory impression",
   "holds information for a shorter time than sensory memory does",
   "has unlimited capacity",
   "operates only during sleep"], ans=0,
   why="EK 2.5.A.1 distinguishes the stores by duration, capacity, and content, and EK 2.3.A.3 describes working memory as a dynamic system of interacting components -- active processing rather than passive brief holding."),
 dict(q="Which pairing of a memory store with a characteristic is correct?", choices=[
   "sensory memory — very brief duration, holds a raw sensory impression",
   "long-term memory — very brief duration, holds a raw sensory impression",
   "short-term memory — unlimited capacity, holds everything a person knows",
   "working memory — no capacity limit, requires no attention"], ans=0,
   why="EK 2.5.A.1 distinguishes the stores by duration, capacity, and content; only the first option pairs a store with characteristics the framework attributes to it, and the others attach one store's properties to another."),
 dict(q="A student argues that because she can recognize hundreds of song melodies, long-term memory must have no capacity limit. The most accurate response is that", choices=[
   "the framework describes the stores as differing in capacity without claiming that any is literally unlimited",
   "long-term memory holds exactly seven items",
   "recognition is not a form of memory",
   "melodies are stored in sensory memory rather than long-term memory"], ans=0,
   why="EK 2.5.A.1 says only that the stores differ in duration, capacity, and content; it makes no claim of unlimited capacity, and a large number of recognized melodies does not establish one."),
 dict(q="A memory researcher claims that a person's inability to recall a childhood third birthday is evidence of brain damage. The best objection is that", choices=[
   "infantile amnesia makes the absence of such memories ordinary rather than pathological",
   "third birthdays are never memorable to anyone",
   "retrograde amnesia would explain the pattern instead",
   "the memory must simply be inaccessible rather than absent"], ans=0,
   why="EK 2.5.A.4 lists infantile amnesia among developmental limitations on storage, which makes the absence of very early memories a normal developmental feature rather than a sign of injury."),
 dict(q="Which of the following best explains why elaborative rehearsal tends to outperform maintenance rehearsal?", choices=[
   "it promotes meaning, which the framework identifies as what helps retention",
   "it always takes more total time than maintenance rehearsal",
   "it stores information in sensory memory instead of long-term memory",
   "it removes the need for any retrieval cue"], ans=0,
   why="EK 2.5.A.2 attributes the advantage specifically to rehearsing in ways that promote MEANING; total time is not the framework's explanation, and the remaining options misplace where the information ends up."),
 dict(q="A person with anterograde amnesia improves at a mirror-tracing task over several days but insists each day that she has never tried it before. This pattern is best explained by", choices=[
   "storage of implicit procedural memory being spared while explicit memory is impaired",
   "the task being too easy to require memory of any kind",
   "retrograde amnesia affecting only her childhood",
   "the misinformation effect altering her account"], ans=0,
   why="EK 2.5.A.4 places anterograde amnesia among storage impairments, and EK 2.3.A.1.i-ii distinguish explicit memory, which is reportable, from implicit procedural memory, which is not; a skill that improves without a reportable memory of practising is that dissociation."),
]
