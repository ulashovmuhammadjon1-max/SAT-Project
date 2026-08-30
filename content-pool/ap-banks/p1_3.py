# AP PSYCHOLOGY 1.3 The Neuron and Neural Firing — 25 questions
# CED effective Fall 2024/2025, Unit 1 Biological Bases of Behavior.
# Learning objectives 1.3.A (neural cells and the reflex arc), 1.3.B (the
# process of neural transmission, neurotransmitters, hormones), 1.3.C
# (psychoactive drugs).
#
# Essential knowledge relied on: 1.3.A.1 neurons transmit information and glial
# cells provide structure, insulation, communication, and waste transport;
# 1.3.A.2 the spinal reflex arc built from sensory neurons, motor neurons, and
# interneurons; 1.3.B.1 the all-or-none principle, depolarization, refractory
# period, resting potential, reuptake, and threshold, with multiple sclerosis
# and myasthenia gravis as disruptions; 1.3.B.2 excitatory versus inhibitory
# messages and the eight neurotransmitters the exam covers (dopamine,
# serotonin, norepinephrine, glutamate, GABA, endorphins, substance P,
# acetylcholine); 1.3.B.3 the five hormones the exam covers (adrenaline, leptin,
# ghrelin, melatonin, oxytocin); 1.3.C.1 agonists, antagonists, and reuptake
# inhibitors; 1.3.C.2 stimulants, depressants, hallucinogens, opioids; 1.3.C.3
# tolerance, addiction, withdrawal.
#
# Exclusion statements respected: the sodium-potassium pump is out of scope and
# appears nowhere; no neurotransmitter or hormone outside the CED's two closed
# lists is ever a key; the glands of the endocrine system are out of scope apart
# from the pituitary, which belongs to Topic 1.4 rather than here.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p1_3.py.
TOPIC = ("1.3", "The Neuron and Neural Firing", 1)
QUESTIONS = [
 dict(q="Which of the following best distinguishes neurons from glial cells?", choices=[
   "Neurons transmit information, while glial cells provide structure, insulation, and waste transport",
   "Neurons provide structural support, while glial cells carry all the messages",
   "Neurons are found only in the brain, while glial cells are found only in the spinal cord",
   "Neurons are chemical, while glial cells are electrical"], ans=0,
   why="EK 1.3.A.1 defines neurons as the cells that transmit information and glial cells as the cells providing structure, insulation, communication, and waste transport."),
 dict(q="A person touches a hot surface and jerks her hand away before she is consciously aware of the pain. This response is best explained by", choices=[
   "a reflex arc carried out through the spinal cord",
   "a decision made in the brain and relayed downward",
   "the release of a hormone into the bloodstream",
   "the action of glial cells on the muscles of the arm"], ans=0,
   why="EK 1.3.A.2 describes the reflex arc in the spinal cord as the mechanism by which neurons respond to a stimulus without waiting on the brain."),
 dict(q="Which three types of neurons work together in the spinal cord to produce a reflex arc?", choices=[
   "sensory neurons, interneurons, and motor neurons",
   "sensory neurons, glial cells, and motor neurons",
   "excitatory neurons, inhibitory neurons, and interneurons",
   "afferent neurons, hormones, and reuptake receptors"], ans=0,
   why="EK 1.3.A.2 names sensory neurons, motor neurons, and interneurons as the three types working together in the spinal cord to create a reflex arc."),
 dict(q="In the reflex arc, the neuron that carries the signal from the spinal cord out to the muscle is the", choices=[
   "motor neuron",
   "sensory neuron",
   "interneuron",
   "glial cell"], ans=0,
   why="Motor neurons carry the outgoing command to muscle; sensory neurons carry the incoming signal and interneurons connect the two inside the cord, per EK 1.3.A.2."),
 dict(q="A neuron that is at rest and not currently sending a signal is described as being at its", choices=[
   "resting potential",
   "threshold",
   "refractory period",
   "point of depolarization"], ans=0,
   why="EK 1.3.B.1 lists resting potential as the state of the neuron before a signal, distinct from threshold (the level of stimulation needed to fire) and the refractory period (the recovery interval after firing)."),
 dict(q="The level of stimulation a neuron must reach before it will fire is called the", choices=[
   "threshold",
   "resting potential",
   "reuptake point",
   "refractory period"], ans=0,
   why="EK 1.3.B.1 lists threshold as the level of stimulation required to trigger firing."),
 dict(q="The all-or-none principle states that a neuron", choices=[
   "either fires at full strength or does not fire at all",
   "fires more strongly when the stimulus is more intense",
   "fires only when every neighboring neuron also fires",
   "cannot fire twice in the same second"], ans=0,
   why="EK 1.3.B.1's all-or-none principle means the strength of a neuron's response does not vary with the strength of the stimulus once threshold is reached."),
 dict(q="A student argues that a very painful pinch must make each individual pain neuron fire more strongly than a mild pinch does. The best correction is that", choices=[
   "a stronger stimulus does not increase the strength of any one neuron's firing, because firing is all or none",
   "a stronger stimulus lowers the resting potential of each neuron permanently",
   "pain neurons do not obey the all-or-none principle",
   "a stronger stimulus makes the refractory period longer than the resting potential"], ans=0,
   why="The all-or-none principle in EK 1.3.B.1 fixes the size of a single neuron's response; intensity is signaled by how many neurons fire and how often, not by a bigger individual response."),
 dict(q="Immediately after firing, a neuron cannot fire again until it has recovered. This brief interval is the", choices=[
   "refractory period",
   "resting potential",
   "threshold",
   "reuptake interval"], ans=0,
   why="EK 1.3.B.1 lists the refractory period as the recovery interval following firing, during which another action potential cannot be generated."),
 dict(q="Reuptake refers to the process in which", choices=[
   "a neurotransmitter is reabsorbed by the neuron that released it",
   "a neuron returns to its resting potential after firing",
   "a hormone is released into the bloodstream",
   "a glial cell removes waste from around a neuron"], ans=0,
   why="EK 1.3.B.1 lists reuptake, the reabsorption of released neurotransmitter back into the sending cell, as one step of neural transmission."),
 dict(q="An excitatory neurotransmitter is one that", choices=[
   "makes an action potential in the receiving neuron more likely",
   "makes an action potential in the receiving neuron less likely",
   "prevents the neuron from ever returning to its resting potential",
   "is released only outside the nervous system"], ans=0,
   why="EK 1.3.B.2 defines excitatory messages as making an action potential more likely and inhibitory messages as making one less likely."),
 dict(q="GABA is best described as the nervous system's principal", choices=[
   "inhibitory neurotransmitter",
   "excitatory neurotransmitter",
   "hormone involved in hunger",
   "reuptake inhibitor"], ans=0,
   why="Within EK 1.3.B.2's closed list, GABA is the major inhibitory neurotransmitter, reducing the likelihood of an action potential; glutamate is the major excitatory one."),
 dict(q="Which neurotransmitter from the AP Psychology list is most directly involved in muscle movement?", choices=[
   "acetylcholine",
   "serotonin",
   "dopamine",
   "substance P"], ans=0,
   why="Among the eight neurotransmitters in EK 1.3.B.2, acetylcholine is the one that acts at the junction between neuron and muscle, which is why myasthenia gravis disrupts movement."),
 dict(q="In the AP Psychology framework, which neurotransmitter carries pain signals toward the brain?", choices=[
   "substance P",
   "glutamate",
   "acetylcholine",
   "norepinephrine"], ans=0,
   why="EK 1.3.B.2 includes substance P, whose function in the list is pain transmission; endorphins are the body's counterpart that reduces the experience of pain."),
 dict(q="Endorphins are best described as neurotransmitters that", choices=[
   "reduce the experience of pain and can produce feelings of well-being",
   "transmit pain signals from the site of an injury",
   "regulate hunger from outside the nervous system",
   "control the timing of sleep and waking"], ans=0,
   why="Within EK 1.3.B.2's list, endorphins are the pain-relieving neurotransmitters, the opposite role from substance P; hunger and sleep are handled by hormones in EK 1.3.B.3, not by endorphins."),
 dict(q="Which of the following is a hormone rather than a neurotransmitter, according to the AP Psychology course framework?", choices=[
   "ghrelin",
   "glutamate",
   "GABA",
   "acetylcholine"], ans=0,
   why="EK 1.3.B.3 lists adrenaline, leptin, ghrelin, melatonin, and oxytocin as the hormones covered; glutamate, GABA, and acetylcholine appear on the neurotransmitter list in EK 1.3.B.2."),
 dict(q="Melatonin's role in behavior is most closely tied to", choices=[
   "the timing of sleep and waking",
   "the sensation of hunger before a meal",
   "the transmission of pain from an injury",
   "voluntary movement of skeletal muscle"], ans=0,
   why="Melatonin is one of the five hormones in EK 1.3.B.3, and its function in the course is the regulation of the sleep-wake cycle, which connects Topic 1.3 to Topic 1.5."),
 dict(q="Leptin and ghrelin are both hormones in the AP Psychology framework, but they differ in that", choices=[
   "ghrelin signals hunger while leptin signals fullness",
   "ghrelin signals fullness while leptin signals hunger",
   "ghrelin acts inside the nervous system while leptin acts outside it",
   "ghrelin is released during sleep while leptin is released during exercise"], ans=0,
   why="EK 1.3.B.3 includes both hormones; ghrelin is the hunger-signaling hormone and leptin the satiety-signaling one, so reversing them is the error the second option represents."),
 dict(q="Hormones differ from neurotransmitters primarily in that hormones", choices=[
   "act outside the nervous system, performing actions similar to those of neurotransmitters",
   "make an action potential more likely rather than less likely",
   "are reabsorbed by the neuron that released them",
   "are produced only by glial cells"], ans=0,
   why="EK 1.3.B.3 states that outside the nervous system, hormones perform actions similar to neurotransmitters; excitatory versus inhibitory is a distinction among neurotransmitters, not between the two categories."),
 dict(q="A drug that mimics a neurotransmitter and increases neural firing is functioning as", choices=[
   "an agonist",
   "an antagonist",
   "a reuptake inhibitor",
   "a depressant"], ans=0,
   why="EK 1.3.C.1 defines agonists as drugs that encourage neural firing and antagonists as drugs that discourage it; a reuptake inhibitor is a separate mechanism defined by blocking reabsorption."),
 dict(q="A drug that blocks the reabsorption of a neurotransmitter back into the sending neuron is", choices=[
   "a reuptake inhibitor, which leaves more of the neurotransmitter available in the synapse",
   "an antagonist, which prevents the neurotransmitter from being released at all",
   "a hormone, because it acts outside the nervous system",
   "a hallucinogen, because it distorts perception"], ans=0,
   why="EK 1.3.C.1 names reuptake inhibitors as drugs that block the reabsorption of neurotransmitters back into the cell, which is a distinct mechanism from blocking receptors."),
 dict(q="Alcohol is classified in the AP Psychology framework as a", choices=[
   "depressant, because it typically decreases neural activity",
   "stimulant, because it typically increases neural activity",
   "hallucinogen, because it distorts perception",
   "opioid, because it relieves pain"], ans=0,
   why="EK 1.3.C.2.ii gives alcohol as the framework's example of a depressant, defined by decreased neural activity."),
 dict(q="Caffeine and cocaine are grouped in the same drug category because both", choices=[
   "typically cause increased neural activity",
   "typically relieve physical pain",
   "typically distort perception and cognition",
   "typically slow breathing and heart rate"], ans=0,
   why="EK 1.3.C.2.i names caffeine and cocaine as stimulants, the category defined by increased neural activity."),
 dict(q="A person who has used a drug regularly finds that the usual dose no longer produces the effect it once did, so she takes more. This change is called", choices=[
   "tolerance",
   "withdrawal",
   "reuptake",
   "the refractory period"], ans=0,
   why="EK 1.3.C.3 identifies tolerance as the need for more of a drug to achieve the previous effect; withdrawal names the symptoms that follow stopping, not the escalation of dose."),
 dict(q="A person who has become addicted to a drug stops taking it and experiences tremors, nausea, and intense discomfort. These symptoms are best described as", choices=[
   "withdrawal",
   "tolerance",
   "an antagonist effect",
   "a refractory period"], ans=0,
   why="EK 1.3.C.3 states that addiction can create significant withdrawal symptoms if the drug is no longer consumed."),
]
