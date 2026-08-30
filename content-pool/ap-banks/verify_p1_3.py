"""Key audit for AP PSYCHOLOGY 1.3 The Neuron and Neural Firing.

One (anchor, claim) per item: the anchor is the substring that must appear in
the keyed choice and in no distractor, and the claim states what the key rests
on and where it comes from in the framework. That is the discipline replacing
computation here -- an assertion nobody wrote down is how a wrong key ships.

Two scope rules govern this topic and both are enforced by reading, not by a
regex, so they are recorded here:

  * The sodium-potassium pump is excluded by EK 1.3.B.1's exclusion statement.
    It appears in no stem, choice, or claim.
  * EK 1.3.B.2 and 1.3.B.3 are CLOSED lists. The only neurotransmitters used are
    dopamine, serotonin, norepinephrine, glutamate, GABA, endorphins, substance P
    and acetylcholine; the only hormones are adrenaline, leptin, ghrelin,
    melatonin and oxytocin. Nothing outside those lists is ever a key, and
    nothing outside them appears as a distractor either, so a student is never
    penalised for not knowing an excluded term.

The pairs this topic invites a writer to get wrong, and which are therefore
tested against each other on purpose: threshold (the level needed to fire) vs
resting potential (the state before firing) vs refractory period (the interval
after firing); substance P (transmits pain) vs endorphins (relieve pain);
ghrelin (hunger) vs leptin (fullness); agonist (encourages firing) vs antagonist
(discourages firing) vs reuptake inhibitor (blocks reabsorption -- a mechanism,
not a direction); tolerance (dose escalation while using) vs withdrawal
(symptoms after stopping).

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p1_3

CLAIMS = [
 ("Neurons transmit information, while glial cells provide structure",
  "EK 1.3.A.1: neurons are the neural cells that transmit information; glial cells provide structure, insulation, communication, and waste transport. The keyed choice states the pairing in that direction, and the first distractor is that same pairing reversed."),
 ("reflex arc carried out through the spinal cord",
  "EK 1.3.A.2: the reflex arc in the spinal cord lets the central and peripheral systems respond to a stimulus without the response being decided in the brain, which is why the withdrawal precedes awareness of pain."),
 ("sensory neurons, interneurons, and motor neurons",
  "EK 1.3.A.2 names exactly these three types as the neurons working together in the spinal cord to create a reflex arc. Glial cells (EK 1.3.A.1) are not one of them."),
 ("motor neuron",
  "In the reflex arc of EK 1.3.A.2 the motor neuron carries the outgoing command to the muscle; the sensory neuron carries the incoming signal and the interneuron links them inside the cord."),
 ("resting potential",
  "EK 1.3.B.1 lists resting potential as the neuron's state before a signal. It is distinct from threshold, the stimulation level required to fire, and from the refractory period, the recovery interval after firing."),
 ("threshold",
  "EK 1.3.B.1 lists threshold as the level of stimulation a neuron must reach to fire. Deliberately paired against resting potential and refractory period, the two states students substitute for it."),
 ("either fires at full strength or does not fire at all",
  "EK 1.3.B.1's all-or-none principle: the size of a neuron's response does not scale with stimulus intensity once threshold is reached."),
 ("does not increase the strength of any one neuron's firing",
  "The all-or-none principle fixes the magnitude of a single neuron's response, so stimulus intensity must be coded some other way -- by how many neurons fire and how often. This is the item that tests the principle as a correction rather than a definition."),
 ("refractory period",
  "EK 1.3.B.1 lists the refractory period as the interval following firing during which the neuron cannot fire again."),
 ("reabsorbed by the neuron that released it",
  "EK 1.3.B.1 lists reuptake among the steps of neural transmission; it is the reabsorption of released neurotransmitter back into the sending cell, not a return to resting potential."),
 ("more likely",
  "EK 1.3.B.2: excitatory neurotransmitters make an action potential more likely, inhibitory ones make it less likely. The first two choices are the two halves of that sentence, so only the direction distinguishes them."),
 ("inhibitory neurotransmitter",
  "GABA appears on EK 1.3.B.2's closed list, and within that list it is the principal inhibitory neurotransmitter -- it makes an action potential less likely. Glutamate is the excitatory counterpart on the same list."),
 ("acetylcholine",
  "Acetylcholine is on EK 1.3.B.2's closed list and is the neurotransmitter acting at the neuron-muscle junction, which is why myasthenia gravis -- named in EK 1.3.B.1 as a disruption of neural transmission -- impairs movement."),
 ("substance P",
  "Substance P is on EK 1.3.B.2's closed list and its function there is the transmission of pain signals. Endorphins, on the same list, are its counterpart in reducing pain, which is why the two are separated across items 14 and 15."),
 ("reduce the experience of pain",
  "Endorphins are on EK 1.3.B.2's closed list as the pain-reducing neurotransmitters. Hunger and sleep-wake timing belong to hormones under EK 1.3.B.3, so those distractors are category errors as well as content errors."),
 ("ghrelin",
  "EK 1.3.B.3's hormone list is adrenaline, leptin, ghrelin, melatonin, oxytocin. Glutamate, GABA, and acetylcholine are all on the separate neurotransmitter list in EK 1.3.B.2, so exactly one option crosses the category line."),
 ("timing of sleep and waking",
  "Melatonin is on EK 1.3.B.3's hormone list and its behavioral role in the course is the sleep-wake cycle, linking this topic to Topic 1.5 Sleep."),
 ("ghrelin signals hunger while leptin signals fullness",
  "Both hormones are on EK 1.3.B.3's list; ghrelin signals hunger and leptin signals satiety. The distractor is the same sentence reversed, which is the error students actually make."),
 ("act outside the nervous system",
  "EK 1.3.B.3: outside the nervous system, hormones perform actions similar to those of neurotransmitters. Excitatory versus inhibitory is a contrast within the neurotransmitter category, not the hormone/neurotransmitter contrast."),
 ("an agonist",
  "EK 1.3.C.1: agonists encourage neural firing, antagonists discourage it, and reuptake inhibitors block reabsorption. All three are distinct mechanisms and all three appear here as options."),
 ("reuptake inhibitor",
  "EK 1.3.C.1 defines a reuptake inhibitor as blocking the reabsorption of neurotransmitters back into the cell -- a different mechanism from an antagonist, which discourages firing rather than preventing reabsorption."),
 ("depressant",
  "EK 1.3.C.2.ii gives alcohol as the framework's own example of a depressant, the category defined by decreased neural activity."),
 ("increased neural activity",
  "EK 1.3.C.2.i names caffeine and cocaine as stimulants and defines the category by increased neural activity. The remaining options are the definitions of opioids, hallucinogens, and depressants respectively."),
 ("tolerance",
  "EK 1.3.C.3 identifies tolerance as the state in which more of a drug is needed for the effect it previously produced. Withdrawal, in the same EK, is what follows stopping."),
 ("withdrawal",
  "EK 1.3.C.3: addiction can create significant withdrawal symptoms if the psychoactive drug is no longer consumed. Item 24 and this item are keyed to the two halves of that sentence so the pair cannot be answered by recognising one word."),
]

psych_check.check(p1_3, CLAIMS, per_topic=25, n_choices=4)
