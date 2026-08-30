"""Key audit for AP PSYCHOLOGY 1.4 The Brain.

One (anchor, claim) per item. The anchor must appear in the keyed choice and in
no distractor -- that is the machine-checkable half, and it is what catches an
off-by-one key. The claim states the specific framework assertion the key rests
on, so the reasoning is on the record instead of in someone's head.

Structure-function assignments used here come from EK 1.4.A.1 through 1.4.A.4.iv
verbatim. Four limbic structures (thalamus, hypothalamus, hippocampus, amygdala)
are named in EK 1.4.A.4 as a list without individual functions attached; their
functions are the standard course content those names denote, and each claim
below says which function is being asserted and which neighbouring structure it
is being distinguished from, because "named in a list" is not by itself a
justification for a key.

The lesion items (2, 5, 7, 13, 22, 23) are deliberate: a student can memorise a
label without knowing a function, and only a "what would damage cause" question
separates the two. Each is keyed by inverting the framework's own function
statement, and each claim below names that statement.

Pairs tested against each other on purpose, because they are the ones a question
writer confuses: hippocampus (forming memories) vs amygdala (fear and emotion);
thalamus (sensory relay) vs hypothalamus (hunger, thirst, temperature); Broca's
area (speech PRODUCTION -- effortful speech, intact comprehension) vs Wernicke's
area (speech COMPREHENSION -- fluent but empty speech, impaired understanding);
cerebellum (coordination) vs medulla (breathing and heart rate).

Scope: the pituitary is the only endocrine gland the CED keeps in scope (the
exclusion statement under EK 1.3.B.3 says so explicitly), and it appears here
only as the gland the hypothalamus directs.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p1_4

CLAIMS = [
 ("basic functioning such as breathing and heart rate",
  "EK 1.4.A.1: the brain stem, including the medulla, generally controls basic functioning such as breathing and heart rate."),
 ("breathing and heart rate",
  "Inverting EK 1.4.A.1: if the medulla controls breathing and heart rate, a lesion there disrupts breathing and heart rate. The distractors are the functions of the temporal/frontal lobes and the parietal somatosensory cortex, none of which the medulla carries."),
 ("alertness and arousal",
  "EK 1.4.A.2 groups the reticular activating system with control of alertness (along with some voluntary and eye movement and some learning, cognition, and emotion). Memory storage, speech production, and touch are assigned elsewhere in 1.4.A.4."),
 ("coordination of muscle movement, balance, and some procedural learning",
  "EK 1.4.A.3, near verbatim: the cerebellum generally controls coordination of muscle movement, balance, and some forms of procedural learning."),
 ("cerebellum",
  "Inverting EK 1.4.A.3. The stem specifies intact strength and intact sensation, which rules out the motor cortex and the somatosensory cortex, leaving coordination and balance -- the cerebellum's assignment."),
 ("visual information processing",
  "EK 1.4.A.4.i: the occipital lobes generally control visual information processing and are located in the rear of the brain."),
 ("seeing and interpreting visual information, even though her eyes are undamaged",
  "Inverting EK 1.4.A.4.i. The clause about undamaged eyes is load-bearing: it locates the deficit in cortical processing rather than in sensation, which is the distinction Topic 1.6 and Topic 2.1 turn on."),
 ("auditory and linguistic processing",
  "EK 1.4.A.4.ii: the temporal lobes generally control auditory and linguistic processing and are located on the sides of the brain."),
 ("parietal lobes",
  "EK 1.4.A.4.iii places the somatosensory cortex, which processes touch sensitivity, in the parietal lobes near the back crown of the brain."),
 ("parietal lobes",
  "EK 1.4.A.4.iii: the parietal lobes generally control association areas, which process and organize information. The corpus callosum and reticular activating system are given other functions in 1.4.A.4 and 1.4.A.2."),
 ("prefrontal cortex of the frontal lobes",
  "EK 1.4.A.4.iv: the frontal lobes generally control linguistic processing, higher-order thinking, and executive functioning, especially in the prefrontal cortex."),
 ("rear of the frontal lobes",
  "EK 1.4.A.4.iv places the motor cortex at the rear of the frontal lobes and assigns it most types of skeletal movement. The location is stated in the framework, so it is fair to test."),
 ("frontal lobes",
  "Inverting EK 1.4.A.4.iv. The stem holds memory, vision, and movement intact so that only executive functioning is impaired; that isolation is what makes the frontal lobes the answer rather than a general statement about personality change."),
 ("the hippocampus",
  "The hippocampus is named among the limbic structures in EK 1.4.A.4, and the function it denotes in the course is the formation of new memories -- the function lost in the amnesia case studies Unit 2 revisits. It is distinguished here from the amygdala, whose role is emotional rather than mnemonic."),
 ("the amygdala",
  "The amygdala is named among the limbic structures in EK 1.4.A.4 and denotes fear and strong emotional response. Item 14 and this item are deliberately adjacent so that the hippocampus/amygdala pair cannot be answered by recognising one word."),
 ("relays incoming sensory information",
  "The thalamus, listed in EK 1.4.A.4, is the sensory relay to the cortex. The distractors are the hypothalamus's regulatory role and the corpus callosum's connecting role, both drawn from the same EK's list, so the item tests within-list discrimination."),
 ("hypothalamus",
  "The hypothalamus, listed in EK 1.4.A.4, governs hunger, thirst, and temperature regulation and directs the pituitary gland -- the one gland the CED keeps in scope, per the exclusion statement under EK 1.3.B.3."),
 ("connecting the brain's two hemispheres",
  "EK 1.4.A.4 lists the corpus callosum among the cortex's structures, and EK 1.4.A.5 has it severed in split-brain surgery. Severing it disconnects the hemispheres, which is only coherent if it joins them."),
 ("severe epilepsy",
  "EK 1.4.A.5 states that severing the corpus callosum is often a treatment for severe epilepsy."),
 ("may specialize in different activities and functions",
  "EK 1.4.A.5, near verbatim: split brain research reveals that the right and left hemispheres may specialize in different activities and functions. Note the framework's hedge -- 'may specialize' -- so the key does not overclaim a strict division of labour."),
 ("contralaterally",
  "EK 1.4.A.5.ii: researchers test for cortex specialization by showing information in each visual field, taking advantage of the brain's contralateral hemispheric organization. The rejected option -- each EYE feeding one hemisphere -- is the specific misconception; it is each visual FIELD, not each eye."),
 ("Broca's area",
  "EK 1.4.A.5.i assigns speech production to Broca's area, in the left hemisphere, with damage leading to aphasia. Intact comprehension plus effortful, broken production is the production-side deficit."),
 ("Wernicke's area",
  "EK 1.4.A.5.i assigns speech comprehension to Wernicke's area. Fluent but meaningless speech with impaired understanding is the comprehension-side deficit, the mirror image of item 22, and the two are placed adjacently on purpose."),
 ("brain plasticity",
  "EK 1.4.A.6: plasticity is the brain's ability to rewire itself or create new connections, generally allowing a damaged part's function to be assumed by a different part."),
 ("EEG, which records electrical activity over time",
  "EK 1.4.A.7 lists EEG and fMRI scans, case studies, and surgical procedures such as lesioning as brain research methods. The stem asks for continuous electrical recording during a change of state, which is the EEG's specific capability and the basis for the sleep-stage evidence in Topic 1.5."),
 ("fMRI, which shows where activity is occurring",
  "EK 1.4.A.7 lists EEG and fMRI scans together, so the item has to separate them on what each actually delivers: an EEG gives electrical activity over TIME (item 25), an fMRI gives activity by LOCATION. Asking participants which part of the brain they used is included as a distractor because introspection cannot report on neural localization at all."),
 ("may not generalize to people in general",
  "EK 1.4.A.7 lists case studies among brain research methods. The limit on a single-case design is generalizability; the distractors misattribute to case studies the requirement of random assignment (which belongs to experiments) and the power to establish a cause (which a single case cannot)."),
 ("alertness, some voluntary movement",
  "EK 1.4.A.2, near verbatim: the reticular activating system and the brain's reward center generally control alertness, some voluntary movement, eye movement, and some types of learning, cognition, and emotion. The distractors are the assignments EK 1.4.A.1 and 1.4.A.3 give to the brain stem and cerebellum, plus the parietal somatosensory cortex from 1.4.A.4.iii."),
 ("impairment of language",
  "EK 1.4.A.5.i states that damage to Broca's area or Wernicke's area can lead to aphasia. The term therefore denotes a language deficit specifically; each distractor names a real deficit from a different structure in this topic, so the item tests what aphasia IS rather than whether the student recognises the word."),
 ("typically located in the left hemisphere",
  "EK 1.4.A.5.i: areas of the brain that affect language are typically located in the left hemisphere and include Broca's and Wernicke's areas. The framework says 'typically', which is why the option asserting an even distribution in EVERY person is wrong -- the key does not claim a universal, only a typical, location."),
]

psych_check.check(p1_4, CLAIMS, per_topic=30, n_choices=4)
