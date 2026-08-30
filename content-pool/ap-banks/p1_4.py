# AP PSYCHOLOGY 1.4 The Brain — 25 questions
# CED effective Fall 2024/2025, Unit 1 Biological Bases of Behavior.
# Learning objective 1.4.A. Essential knowledge: 1.4.A.1 brain stem and medulla
# (basic functioning such as breathing and heart rate); 1.4.A.2 reticular
# activating system and reward center (alertness, some voluntary and eye
# movement, some learning, cognition, emotion); 1.4.A.3 cerebellum
# (coordination, balance, some procedural learning); 1.4.A.4 the cerebral cortex,
# its two hemispheres, and the structures the framework groups with it -- the
# limbic system (thalamus, hypothalamus, pituitary gland, hippocampus,
# amygdala), the corpus callosum, and the four lobes; 1.4.A.4.i-iv occipital,
# temporal, parietal (association areas and somatosensory cortex) and frontal
# lobes (higher-order thinking, executive functioning, prefrontal cortex, and
# the motor cortex at the rear of the frontal lobes); 1.4.A.5 split-brain
# research and hemispheric specialization, Broca's area, Wernicke's area,
# aphasia, contralateral organization; 1.4.A.6 plasticity; 1.4.A.7 research
# methods -- EEG, fMRI, case studies, and lesioning.
#
# A quarter of the items ask what a LESION to a structure would cause, because
# that is where knowing a label stops being enough and the function has to be
# known.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p1_4.py.
TOPIC = ("1.4", "The Brain", 1)
QUESTIONS = [
 dict(q="The brain stem, including the medulla, is primarily responsible for", choices=[
   "basic functioning such as breathing and heart rate",
   "the planning and judgment involved in complex decisions",
   "the interpretation of visual information",
   "the coordination of balance during walking"], ans=0,
   why="EK 1.4.A.1 states that the brain stem, including the medulla, generally controls basic functioning such as breathing and heart rate."),
 dict(q="Damage to the medulla would most likely disrupt a person's", choices=[
   "breathing and heart rate",
   "ability to recall the names of familiar objects",
   "sense of touch on the left hand",
   "ability to plan a week in advance"], ans=0,
   why="Because EK 1.4.A.1 assigns basic life functions such as breathing and heart rate to the brain stem and medulla, a lesion there disrupts exactly those functions."),
 dict(q="The reticular activating system is most closely associated with", choices=[
   "alertness and arousal",
   "the storage of new long-term memories",
   "the production of fluent speech",
   "the processing of touch sensitivity"], ans=0,
   why="EK 1.4.A.2 groups the reticular activating system with control of alertness, along with some voluntary and eye movement and some learning, cognition, and emotion."),
 dict(q="The cerebellum is best described as the structure that generally controls", choices=[
   "coordination of muscle movement, balance, and some procedural learning",
   "breathing, heart rate, and other basic life functions",
   "the conscious interpretation of what a person sees",
   "the formation of new conscious memories of events"], ans=0,
   why="EK 1.4.A.3 assigns coordination of muscle movement, balance, and some forms of procedural learning to the cerebellum."),
 dict(q="A patient can move his limbs and feel them normally, but his movements have become clumsy and poorly coordinated and he stumbles when he walks. Damage is most likely to his", choices=[
   "cerebellum",
   "occipital lobes",
   "medulla",
   "hippocampus"], ans=0,
   why="Intact strength and sensation with impaired coordination and balance points to the cerebellum, the structure EK 1.4.A.3 assigns those functions to."),
 dict(q="The occipital lobes, located at the rear of the brain, generally control", choices=[
   "visual information processing",
   "auditory and linguistic processing",
   "touch sensitivity",
   "executive functioning"], ans=0,
   why="EK 1.4.A.4.i states that the occipital lobes generally control visual information processing and are located in the rear of the brain."),
 dict(q="A person who has sustained damage to the occipital lobes is most likely to have difficulty", choices=[
   "seeing and interpreting visual information, even though her eyes are undamaged",
   "hearing speech directed at her",
   "coordinating her balance while standing",
   "regulating her body temperature"], ans=0,
   why="EK 1.4.A.4.i assigns visual processing to the occipital lobes, so a lesion there impairs vision at the level of the brain rather than at the level of the eye."),
 dict(q="The temporal lobes, located on the sides of the brain, generally control", choices=[
   "auditory and linguistic processing",
   "visual information processing",
   "coordination and balance",
   "breathing and heart rate"], ans=0,
   why="EK 1.4.A.4.ii states that the temporal lobes generally control auditory and linguistic processing and are located on the sides of the brain."),
 dict(q="The somatosensory cortex, which processes touch sensitivity, is located in the", choices=[
   "parietal lobes",
   "occipital lobes",
   "temporal lobes",
   "cerebellum"], ans=0,
   why="EK 1.4.A.4.iii places the somatosensory cortex, which processes touch sensitivity, in the parietal lobes, near the back crown of the brain."),
 dict(q="Association areas, which process and organize information, are described in the AP Psychology framework as a function of the", choices=[
   "parietal lobes",
   "medulla",
   "corpus callosum",
   "reticular activating system"], ans=0,
   why="EK 1.4.A.4.iii states that the parietal lobes generally control association areas, which process and organize information."),
 dict(q="Higher-order thinking and executive functioning are controlled especially by the", choices=[
   "prefrontal cortex of the frontal lobes",
   "somatosensory cortex of the parietal lobes",
   "visual cortex of the occipital lobes",
   "cerebellum"], ans=0,
   why="EK 1.4.A.4.iv assigns linguistic processing, higher-order thinking, and executive functioning to the frontal lobes, especially the prefrontal cortex."),
 dict(q="The motor cortex, which controls most types of skeletal movement, is located", choices=[
   "at the rear of the frontal lobes",
   "at the front of the occipital lobes",
   "at the base of the brain stem",
   "along the underside of the temporal lobes"], ans=0,
   why="EK 1.4.A.4.iv places the motor cortex at the rear of the frontal lobes and assigns it most types of skeletal movement."),
 dict(q="After an injury, a man is described by his family as impulsive, poor at planning, and unable to hold a job he once did well, although his memory, vision, and movement are intact. The damage is most consistent with an injury to the", choices=[
   "frontal lobes",
   "occipital lobes",
   "cerebellum",
   "medulla"], ans=0,
   why="Loss of planning, judgment, and impulse control with other functions intact points to the executive functioning that EK 1.4.A.4.iv assigns to the frontal lobes and prefrontal cortex."),
 dict(q="Which limbic structure is most directly involved in the formation of new memories?", choices=[
   "the hippocampus",
   "the amygdala",
   "the thalamus",
   "the pituitary gland"], ans=0,
   why="Among the limbic structures listed in EK 1.4.A.4, the hippocampus is the one associated with forming new memories; the amygdala is associated with emotion, particularly fear."),
 dict(q="Which limbic structure is most directly involved in fear and other strong emotional responses?", choices=[
   "the amygdala",
   "the hippocampus",
   "the corpus callosum",
   "the medulla"], ans=0,
   why="Among the limbic structures listed in EK 1.4.A.4, the amygdala is the one associated with fear and emotional response, distinct from the hippocampus's role in memory formation."),
 dict(q="The thalamus is best described as the structure that", choices=[
   "relays incoming sensory information to the appropriate areas of the cortex",
   "regulates hunger, thirst, and body temperature",
   "connects the two hemispheres of the brain",
   "coordinates balance and fine motor movement"], ans=0,
   why="The thalamus, one of the limbic structures named in EK 1.4.A.4, is the sensory relay station; regulation of hunger, thirst, and temperature belongs to the hypothalamus and hemispheric connection to the corpus callosum."),
 dict(q="A researcher wants to name the structure that regulates hunger, thirst, and body temperature and that also directs the pituitary gland. She should name the", choices=[
   "hypothalamus",
   "hippocampus",
   "amygdala",
   "cerebellum"], ans=0,
   why="The hypothalamus is the limbic structure in EK 1.4.A.4 that governs these regulatory drives and directs the pituitary gland, the one gland the framework keeps in scope."),
 dict(q="The corpus callosum is best described as", choices=[
   "the band of fibers connecting the brain's two hemispheres",
   "the outer layer of the cerebral cortex",
   "the structure that relays sensory information",
   "the region responsible for speech production"], ans=0,
   why="EK 1.4.A.4 lists the corpus callosum among the structures of the cerebral cortex, and EK 1.4.A.5 identifies it as the structure severed in split-brain surgery, which is only meaningful because it joins the hemispheres."),
 dict(q="Split-brain surgery, which severs the corpus callosum, has most often been performed as a treatment for", choices=[
   "severe epilepsy",
   "chronic depression",
   "memory loss following a stroke",
   "loss of coordination"], ans=0,
   why="EK 1.4.A.5 states that severing the corpus callosum is often a treatment for severe epilepsy, and that the procedure is what made split-brain research possible."),
 dict(q="What has split-brain research most directly revealed?", choices=[
   "that the right and left hemispheres may specialize in different activities and functions",
   "that the two hemispheres perform identical functions in parallel",
   "that language is processed equally by both hemispheres",
   "that severing the corpus callosum has no measurable effect on behavior"], ans=0,
   why="EK 1.4.A.5 states that split-brain research reveals that the right and left hemispheres may specialize in different activities and functions."),
 dict(q="Researchers test split-brain patients by presenting information in one visual field at a time. This method works because", choices=[
   "the brain is organized contralaterally, so each visual field is processed by the opposite hemisphere",
   "each eye sends information to only one hemisphere",
   "the corpus callosum grows back after surgery",
   "visual information bypasses the cortex entirely"], ans=0,
   why="EK 1.4.A.5.ii states that researchers take advantage of the brain's contralateral hemispheric organization by showing information in each visual field."),
 dict(q="A patient can understand everything said to her but produces only slow, effortful, broken speech. This pattern points to damage in", choices=[
   "Broca's area",
   "Wernicke's area",
   "the occipital lobes",
   "the cerebellum"], ans=0,
   why="EK 1.4.A.5.i assigns speech production to Broca's area and speech comprehension to Wernicke's area; intact comprehension with impaired production isolates the former."),
 dict(q="A patient speaks fluently and with normal rhythm, but her sentences carry little meaning and she cannot understand what others say to her. This pattern points to damage in", choices=[
   "Wernicke's area",
   "Broca's area",
   "the motor cortex",
   "the medulla"], ans=0,
   why="EK 1.4.A.5.i assigns speech comprehension to Wernicke's area; fluent but meaningless speech with impaired understanding is the complement of the Broca's pattern in the previous item."),
 dict(q="After a childhood injury to one region of the brain, another region gradually takes over much of the lost function. This illustrates", choices=[
   "brain plasticity",
   "the all-or-none principle",
   "contralateral organization",
   "hemispheric specialization"], ans=0,
   why="EK 1.4.A.6 defines brain plasticity as the brain's ability to rewire itself and to allow the function of a damaged part to be assumed by a different part."),
 dict(q="A researcher wants to record the electrical activity of the whole cortex, moment by moment, while participants fall asleep. Which technique is best suited to that purpose?", choices=[
   "an EEG, which records electrical activity over time",
   "a lesion, which destroys tissue to observe the result",
   "a case study of a single patient with an unusual injury",
   "a survey of participants' self-reported alertness"], ans=0,
   why="EK 1.4.A.7 lists scans including EEG and fMRI, case studies, and surgical procedures such as lesioning as the methods of brain research; recording ongoing electrical activity over time is specifically what an EEG does, and it is the method Topic 1.5 relies on for sleep stages."),
]
