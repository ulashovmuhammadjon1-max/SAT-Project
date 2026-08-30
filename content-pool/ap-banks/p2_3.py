# AP PSYCHOLOGY 2.3 Introduction to Memory — 30 questions
# CED effective Fall 2024/2025, Unit 2 Cognition. Learning objective 2.3.A.
#
# Essential knowledge relied on: 2.3.A.1 memories differentiated by how they are
# processed, stored, and retrieved; 2.3.A.1.i explicit memory (more easily
# described to others), with episodic and semantic as its types; 2.3.A.1.ii
# implicit memory (harder to describe), with procedural memory as a type;
# 2.3.A.1.iii prospective memory, for future actions; 2.3.A.2 long-term
# potentiation, the strengthening of synaptic connections with frequent
# activation; 2.3.A.3 the working memory model -- central executive, phonological
# loop, visuospatial sketchpad; 2.3.A.4 the multi-store model -- sensory memory
# (iconic and echoic), short-term memory, long-term memory -- and automatic
# versus effortful processing; 2.3.A.5 the levels of processing model, whose
# three levels run structural, phonemic, semantic from shallowest to deepest.
#
# Topic boundary this module keeps: 2.3 is the map of memory -- its TYPES,
# STRUCTURES, and MODELS. The pipeline stages get their own topics (encoding
# 2.4, storage 2.5, retrieval 2.6) and the failures get 2.7, so specific
# encoding strategies, storage capacities, retrieval cues, and forgetting are
# deliberately NOT keyed here.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p2_3.py.
TOPIC = ("2.3", "Introduction to Memory", 2)
QUESTIONS = [
 dict(q="Explicit memory is best described as memory that is", choices=[
   "more easily described or explained to others",
   "expressed through skilled action but hard to put into words",
   "held for only a fraction of a second after the stimulus ends",
   "concerned with actions a person intends to perform later"], ans=0,
   why="EK 2.3.A.1.i states that explicit memory is a type of memory that is more easily described or explained to others."),
 dict(q="Implicit memory is best described as memory that is", choices=[
   "more challenging to describe or explain to others",
   "always about events from a person's own life",
   "limited to general knowledge such as facts and definitions",
   "stored only for as long as it is being rehearsed"], ans=0,
   why="EK 2.3.A.1.ii states that implicit memory is more challenging to describe or explain to others."),
 dict(q="The two types of explicit memory named in the AP Psychology framework are", choices=[
   "episodic and semantic",
   "procedural and prospective",
   "iconic and echoic",
   "structural and phonemic"], ans=0,
   why="EK 2.3.A.1.i names episodic and semantic as types of explicit memory; procedural is implicit, iconic and echoic are sensory stores, and structural and phonemic are levels of processing."),
 dict(q="Remembering your own tenth birthday party is an example of", choices=[
   "episodic memory",
   "semantic memory",
   "procedural memory",
   "prospective memory"], ans=0,
   why="EK 2.3.A.1.i lists episodic memory as a type of explicit memory; it is memory for events one has personally experienced, as opposed to general knowledge."),
 dict(q="Remembering that the capital of France is Paris is an example of", choices=[
   "semantic memory",
   "episodic memory",
   "procedural memory",
   "implicit memory"], ans=0,
   why="EK 2.3.A.1.i lists semantic memory as a type of explicit memory; it is memory for general knowledge rather than for a personally experienced event."),
 dict(q="Riding a bicycle without consciously thinking about how to balance draws on", choices=[
   "procedural memory",
   "semantic memory",
   "episodic memory",
   "prospective memory"], ans=0,
   why="EK 2.3.A.1.ii identifies procedural memory as a type of implicit memory for procedures and processes, which is what a practiced motor skill is."),
 dict(q="Remembering to take a medication after dinner tonight relies on", choices=[
   "prospective memory",
   "episodic memory",
   "semantic memory",
   "procedural memory"], ans=0,
   why="EK 2.3.A.1.iii defines prospective memory as memory related to future actions."),
 dict(q="Which pairing of a memory type with an example is correct?", choices=[
   "procedural memory — tying a shoelace without thinking about the steps",
   "semantic memory — recalling the argument you had last Tuesday",
   "episodic memory — knowing that water freezes at zero degrees Celsius",
   "prospective memory — recalling where you spent last summer"], ans=0,
   why="EK 2.3.A.1.ii makes procedural memory a memory for procedures and processes; the other three options each attach a memory type to another type's example."),
 dict(q="Long-term potentiation is best described as", choices=[
   "the strengthening of synaptic connections between neurons with frequent activation",
   "the gradual fading of a memory that is not rehearsed",
   "the process of retrieving a memory into conscious awareness",
   "the limit on how many items short-term memory can hold"], ans=0,
   why="EK 2.3.A.2 defines long-term potentiation as a process by which synaptic connections between neurons become stronger with frequent activation, and identifies it as a biological process for memory."),
 dict(q="Long-term potentiation matters to the study of memory because it", choices=[
   "gives memory a biological mechanism at the level of the connections between neurons",
   "shows that memories are stored in a single location in the brain",
   "proves that all memories last a lifetime",
   "explains why information at the end of a list is remembered best"], ans=0,
   why="EK 2.3.A.2 presents long-term potentiation as a BIOLOGICAL process for memory, which is what connects Unit 2's models to the neural transmission of Topic 1.3."),
 dict(q="In the working memory model, the component that directs attention and coordinates the other components is the", choices=[
   "central executive",
   "phonological loop",
   "visuospatial sketchpad",
   "sensory register"], ans=0,
   why="EK 2.3.A.3 names the central executive, phonological loop, and visuospatial sketchpad as the components of working memory; the central executive is the coordinating one."),
 dict(q="Silently repeating a phone number to yourself until you can dial it uses the working memory component called the", choices=[
   "phonological loop",
   "visuospatial sketchpad",
   "central executive",
   "iconic store"], ans=0,
   why="EK 2.3.A.3 names the phonological loop as a component of working memory; it is the one that handles verbal and sound-based material."),
 dict(q="Mentally picturing the layout of your kitchen to count how many drawers it has uses the working memory component called the", choices=[
   "visuospatial sketchpad",
   "phonological loop",
   "central executive",
   "echoic store"], ans=0,
   why="EK 2.3.A.3 names the visuospatial sketchpad as a component of working memory; it is the one that handles visual and spatial material."),
 dict(q="The working memory model is best described as a model of", choices=[
   "a dynamic system with several interacting components that processes information into long-term memory",
   "a single storage container that holds seven items at a time",
   "the biological strengthening of connections between neurons",
   "the order in which items in a list are recalled"], ans=0,
   why="EK 2.3.A.3 describes working memory as the primary memory system engaging in a dynamic interaction with several components to process information into long-term memory."),
 dict(q="The multi-store model proposes that information must pass through three interacting systems, which are", choices=[
   "sensory memory, short-term memory, and long-term memory",
   "the central executive, phonological loop, and visuospatial sketchpad",
   "structural, phonemic, and semantic processing",
   "episodic, semantic, and procedural memory"], ans=0,
   why="EK 2.3.A.4 names sensory memory, short-term memory, and long-term memory as the three interacting systems of the multi-store model; the other options list the working memory components, the levels of processing, and memory types."),
 dict(q="Iconic and echoic memory are named in the AP Psychology framework as forms of", choices=[
   "sensory memory",
   "long-term memory",
   "working memory",
   "implicit memory"], ans=0,
   why="EK 2.3.A.4 places iconic and echoic memory inside sensory memory, the first of the multi-store model's three systems."),
 dict(q="A brief visual impression that lingers for a fraction of a second after a light is switched off is an example of", choices=[
   "iconic memory",
   "echoic memory",
   "semantic memory",
   "procedural memory"], ans=0,
   why="EK 2.3.A.4 includes iconic memory within sensory memory; it is the visual sensory store, as distinct from echoic memory, which is the auditory one."),
 dict(q="Being able to repeat back the last few words of a question you were not really listening to illustrates", choices=[
   "echoic memory",
   "iconic memory",
   "prospective memory",
   "long-term potentiation"], ans=0,
   why="EK 2.3.A.4 includes echoic memory within sensory memory; it is the auditory sensory store, which briefly retains sound after it has ended."),
 dict(q="Which statement correctly distinguishes iconic from echoic memory?", choices=[
   "iconic memory is the brief visual store; echoic memory is the brief auditory store",
   "echoic memory is the brief visual store; iconic memory is the brief auditory store",
   "iconic memory lasts a lifetime; echoic memory lasts seconds",
   "both are types of long-term memory"], ans=0,
   why="EK 2.3.A.4 lists both within sensory memory, distinguished by modality; the first distractor is that distinction reversed and the others misplace them in the multi-store model."),
 dict(q="The multi-store model focuses attention on the impact of automatic and effortful processing on", choices=[
   "encoding, storage, and retrieval",
   "the four Gestalt principles",
   "divergent and convergent thinking",
   "the sympathetic and parasympathetic systems"], ans=0,
   why="EK 2.3.A.4 states that the multi-store model focuses on the impact of automatic and effortful processing on memory encoding, storage, and retrieval."),
 dict(q="Reading a sentence and taking in its meaning without deliberate effort, while deliberately memorizing a definition takes concentration, illustrates the difference between", choices=[
   "automatic and effortful processing",
   "iconic and echoic memory",
   "episodic and semantic memory",
   "primacy and recency"], ans=0,
   why="EK 2.3.A.4 pairs automatic and effortful processing as the two modes whose impact on memory the multi-store model examines."),
 dict(q="The levels of processing model proposes that information is encoded at three levels, which from shallowest to deepest are", choices=[
   "structural, phonemic, semantic",
   "semantic, phonemic, structural",
   "sensory, short-term, long-term",
   "episodic, semantic, procedural"], ans=0,
   why="EK 2.3.A.5 states that the levels of processing model proposes memory encoded on three levels from shallowest to deepest: structural, phonemic, and semantic."),
 dict(q="Noticing only whether a printed word appears in capital letters is processing at which level?", choices=[
   "structural",
   "phonemic",
   "semantic",
   "procedural"], ans=0,
   why="EK 2.3.A.5 makes structural the shallowest level; attending only to the physical form of a word is structural rather than sound-based or meaning-based processing."),
 dict(q="Judging whether a printed word rhymes with another word is processing at which level?", choices=[
   "phonemic",
   "structural",
   "semantic",
   "episodic"], ans=0,
   why="EK 2.3.A.5 places phonemic between structural and semantic; attending to how a word sounds is the sound-based middle level."),
 dict(q="Judging whether a word would make sense in a given sentence is processing at which level?", choices=[
   "semantic",
   "phonemic",
   "structural",
   "iconic"], ans=0,
   why="EK 2.3.A.5 makes semantic the deepest of the three levels; attending to meaning is what semantic processing is."),
 dict(q="According to the levels of processing model, which task should produce the best later recall of a word?", choices=[
   "deciding whether the word fits meaningfully into a sentence",
   "deciding whether the word rhymes with another word",
   "deciding whether the word is printed in capital letters",
   "counting the number of letters in the word"], ans=0,
   why="EK 2.3.A.5 orders the levels from shallowest to deepest as structural, phonemic, semantic, and the model's claim is that deeper processing produces better retention."),
 dict(q="Which statement correctly distinguishes the working memory model from the multi-store model?", choices=[
   "the working memory model divides the primary memory system into interacting components; the multi-store model describes three systems information passes through",
   "the multi-store model divides the primary memory system into interacting components; the working memory model describes three systems information passes through",
   "the working memory model concerns retrieval only, while the multi-store model concerns encoding only",
   "the two models make identical claims under different names"], ans=0,
   why="EK 2.3.A.3 describes working memory as a dynamic interaction of components within the primary memory system, while EK 2.3.A.4 describes the multi-store model as three systems information must pass through; the first distractor reverses the two."),
 dict(q="A researcher gives one randomly assigned group a list to study by thinking about each word's meaning, and another group the same list to study by noticing each word's typeface, then tests recall in both groups. This study is", choices=[
   "an experiment, because the study method was manipulated and randomly assigned",
   "a correlational study, because two variables are measured",
   "a naturalistic observation, because participants studied on their own",
   "a case study, because only one list was used"], ans=0,
   why="Science practice 2.A: a manipulated, randomly assigned independent variable is what makes a design an experiment; the number of lists and where studying occurred do not change that classification."),
 dict(q="In the study described above, the researcher's prediction that the meaning group will recall more words is derived most directly from", choices=[
   "the levels of processing model",
   "the working memory model",
   "long-term potentiation",
   "prospective memory"], ans=0,
   why="EK 2.3.A.5's levels of processing model ranks semantic processing as deepest and structural as shallowest, which is exactly the comparison the two study conditions set up."),
 dict(q="A patient with damage to the hippocampus can still learn new motor skills through practice but cannot describe having practiced them. This pattern most directly supports the distinction between", choices=[
   "implicit and explicit memory",
   "iconic and echoic memory",
   "massed and distributed practice",
   "automatic and effortful attention"], ans=0,
   why="EK 2.3.A.1.i and 2.3.A.1.ii separate memory that is easily described to others from memory that is not; a preserved skill that cannot be reported is that separation shown in one person."),
]
