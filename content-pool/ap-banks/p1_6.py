# AP PSYCHOLOGY 1.6 Sensation — 30 questions
# CED effective Fall 2024/2025, Unit 1 Biological Bases of Behavior.
# Learning objectives 1.6.A through 1.6.G -- the widest topic in Unit 1, so the
# items are spread across all seven rather than concentrated on vision.
#
# Essential knowledge relied on: 1.6.A.1 sensation as detection above a threshold
# plus transduction into neurochemical messages, and the absolute threshold as
# detection at least 50% of the time; 1.6.A.2 just-noticeable difference, sensory
# adaptation, Weber's law; 1.6.A.3 sensory interaction and synesthesia; 1.6.B.1
# retina and blind spot with the brain filling gaps; 1.6.B.2 accommodation by the
# lens, nearsightedness and farsightedness; 1.6.B.3 rods -- periphery, shape and
# movement but not color, low light, light and dark adaptation; 1.6.B.4
# trichromatic and opponent-process theories; 1.6.B.4.i cones in the fovea, blue
# (short), green (medium), red (long) wavelengths; 1.6.B.4.ii afterimages and the
# red/green, blue/yellow, black/white ganglion pairs; 1.6.B.4.iii color vision
# deficiency, dichromatism and monochromatism; 1.6.B.5 prosopagnosia and
# blindsight from damage mainly to the occipital lobes; 1.6.C.1 pitch as
# wavelength and loudness as amplitude; 1.6.C.2 place, volley, and frequency
# theories; 1.6.C.3 sound localization; 1.6.C.4 conduction and sensorineural
# deafness; 1.6.D.1 olfaction, smell as the only sense not processed first in
# the thalamus, pheromones; 1.6.D.2 the six tastes including umami and
# oleogustus; 1.6.D.3 supertasters, medium tasters, nontasters; 1.6.D.4 taste
# muted or absent without smell; 1.6.E.1 "hot" from warm AND cold receptors
# together; 1.6.F.1 gate control theory and phantom limb sensation; 1.6.G.1
# vestibular sense and the semicircular canals; 1.6.G.2 kinesthesis.
#
# Coverage is deliberately spread one or two items per learning objective rather
# than concentrated on vision, which is where a sensation bank usually drifts:
# 1.6.A gets 7 items, 1.6.B 9, 1.6.C 5, 1.6.D 5, and 1.6.E, 1.6.F, 1.6.G one
# each. Research-design and data items for Unit 1 live in Topics 1.1, 1.2 and
# 1.5; this topic's 30 slots are spent on content because it carries seven
# learning objectives against those topics' one.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p1_6.py.
TOPIC = ("1.6", "Sensation", 1)
QUESTIONS = [
 dict(q="Sensation is best defined as the process of", choices=[
   "detecting information from the environment and transducing it into neurochemical messages",
   "organizing and interpreting information so that it becomes meaningful",
   "storing incoming information for later recall",
   "deciding which of several possible actions to take"], ans=0,
   why="EK 1.6.A.1 defines sensation as detecting information from the environment that meets a certain threshold and transducing stimuli into neurochemical messages for processing in the brain; interpretation is perception, which is Topic 2.1."),
 dict(q="Transduction refers specifically to", choices=[
   "the conversion of physical stimulus energy into neural signals the brain can use",
   "the movement of a signal from one neuron to the next across a gap",
   "the brain's interpretation of an ambiguous image",
   "the loss of sensitivity to an unchanging stimulus"], ans=0,
   why="EK 1.6.A.1 uses transduction for the conversion of stimuli into neurochemical messages; it is a conversion of form, not a transfer between neurons and not an act of interpretation."),
 dict(q="A stimulus is at a person's absolute threshold when it can be detected", choices=[
   "at least 50 percent of the time",
   "100 percent of the time",
   "only when the person is paying full attention",
   "only after repeated exposure over several days"], ans=0,
   why="EK 1.6.A.1 states that the absolute threshold occurs when a stimulus can be detected at least 50 percent of the time."),
 dict(q="The smallest change in a stimulus that a person can reliably notice is called the", choices=[
   "just-noticeable difference",
   "absolute threshold",
   "point of sensory adaptation",
   "amplitude of the stimulus"], ans=0,
   why="EK 1.6.A.2 pairs the just-noticeable difference with the detection of change in stimuli, as distinct from the absolute threshold, which concerns detecting a stimulus at all."),
 dict(q="Weber's law describes", choices=[
   "the degree to which two stimuli must differ before the difference can be detected",
   "the weakest stimulus a person can detect half the time",
   "the tendency of a constant stimulus to fade from awareness",
   "the way one sense can be experienced through another"], ans=0,
   why="EK 1.6.A.2 states that Weber's law describes the degree to which stimuli need to be different for the difference to be detected, which is a statement about proportional difference rather than about absolute detection."),
 dict(q="A person puts on a wristwatch in the morning and within minutes no longer feels it on her wrist. This illustrates", choices=[
   "sensory adaptation",
   "the absolute threshold",
   "sensory interaction",
   "accommodation"], ans=0,
   why="EK 1.6.A.2 names sensory adaptation as the diminished sensitivity to an unchanging stimulus, which is what an unnoticed watch demonstrates."),
 dict(q="Sensory interaction refers to the fact that", choices=[
   "the sensory systems constantly work together rather than independently",
   "one sensory system is always dominant over the others",
   "a stimulus must exceed a threshold before it is detected",
   "sensitivity declines when a stimulus does not change"], ans=0,
   why="EK 1.6.A.3 states that the sensory systems constantly work together in a process called sensory interaction."),
 dict(q="A person consistently experiences particular musical notes as having specific colors. This experience is called", choices=[
   "synesthesia",
   "sensory adaptation",
   "blindsight",
   "prosopagnosia"], ans=0,
   why="EK 1.6.A.3 defines synesthesia as an experience of sensation in which one system of sensation is experienced through another."),
 dict(q="The retina is best described as", choices=[
   "the photosensitive surface at the back of the eye",
   "the transparent structure that focuses light",
   "the region of the brain that interprets visual signals",
   "the nerve that carries visual information out of the eye"], ans=0,
   why="EK 1.6.B.1 defines the retina as the photosensitive surface at the back of the eye whose cells capture visual information for transduction to the brain."),
 dict(q="The blind spot in each eye exists because", choices=[
   "there are no receptor cells at the point where the visual nerve exits the eye",
   "the lens cannot focus light onto the center of the retina",
   "the two eyes send conflicting information to the brain",
   "rods are absent from the periphery of the retina"], ans=0,
   why="EK 1.6.B.1 identifies the blind spot as the location where the visual nerve exits the eye, evidence that the retinal image captured is incomplete."),
 dict(q="According to the AP Psychology framework, the sensation of \"hot\" is produced by", choices=[
   "the simultaneous activation of warm and cold receptors in the skin",
   "a single type of receptor dedicated to high temperatures",
   "pain receptors responding before temperature receptors do",
   "the thalamus interpreting an absence of cold signals"], ans=0,
   why="EK 1.6.E.1 states that the sensation of hot is produced by the activation of warm AND cold receptors in the skin, which is why a grid of alternating warm and cool bars feels hot to the touch."),
 dict(q="Accommodation, in the visual system, refers to", choices=[
   "the process by which the lens focuses visual stimuli onto the retina",
   "the gradual recovery of vision after entering a dark room",
   "the fading of a constant visual stimulus from awareness",
   "the brain's adjustment of perceived color under different lighting"], ans=0,
   why="EK 1.6.B.2 states that visual stimuli are focused onto the retina by the lens via a process called accommodation, and that alterations to that process can produce nearsightedness or farsightedness."),
 dict(q="Gustation is the sense of taste. Which list gives the basic tastes recognized in the AP Psychology course framework?", choices=[
   "sweet, sour, salty, bitter, umami, and oleogustus",
   "sweet, sour, salty, and bitter only",
   "sweet, salty, spicy, and cold",
   "sweet, sour, salty, bitter, and metallic"], ans=0,
   why="EK 1.6.D.2 defines gustation as the sense of taste and lists the types as sweet, sour, salty, bitter, umami, and oleogustus; the four-taste list is the older account the framework has moved past."),
 dict(q="Rods are the photoreceptor cells that", choices=[
   "lie in the periphery of the eye and detect shapes and movement in low light but not color",
   "cluster in the fovea and process color and fine detail",
   "carry visual information out of the eye toward the brain",
   "change shape to focus incoming light"], ans=0,
   why="EK 1.6.B.3 states that rods lie in the periphery, detect shapes and movement but not color, are mainly activated in low-light environments, and play a role in light and dark adaptation."),
 dict(q="Two people eat the same dish and one finds it overwhelmingly bitter while the other barely notices. According to the AP Psychology framework, the most likely explanation is a difference in", choices=[
   "the number of taste receptors on the tongue",
   "the number of rods in the retina",
   "the sensitivity of the semicircular canals",
   "how completely each has adapted to the smell of the room"], ans=0,
   why="EK 1.6.D.3 states that the number of taste receptors on the tongue is related to how sensitive people are to tastes, classifying them as supertasters, medium tasters, or nontasters."),
 dict(q="Cones, the photoreceptor cells located in the fovea, are responsible for", choices=[
   "processing color and fine detail",
   "detecting movement in the periphery of the visual field",
   "focusing light onto the retina",
   "producing the sensation of an afterimage"], ans=0,
   why="EK 1.6.B.4.i states that photoreceptor cells located in the fovea that process color and detail are called cones."),
 dict(q="According to the trichromatic theory of color vision, researchers have identified cones that detect", choices=[
   "short, medium, and long wavelengths, described as blue, green, and red",
   "red/green, blue/yellow, and black/white pairs",
   "only brightness rather than any wavelength",
   "movement rather than color"], ans=0,
   why="EK 1.6.B.4.i names blue (short wavelengths), green (medium), and red (long) cones in the retina; the paired opponents belong to the opponent-process account in EK 1.6.B.4.ii instead."),
 dict(q="After staring at a bright green shape and then looking at a white wall, a person sees a red shape. The AP Psychology framework explains this afterimage in terms of", choices=[
   "ganglion cells operating in opposing pairs",
   "cones in the fovea being permanently damaged",
   "the lens failing to accommodate",
   "rods taking over in low light"], ans=0,
   why="EK 1.6.B.4.ii states that afterimages result when certain ganglion cells in the retina are activated while others are not, in an opponent process."),
 dict(q="Gate control theory is offered in the AP Psychology framework as an attempt to describe", choices=[
   "the complexities of how pain is processed in the body and in the brain",
   "how the auditory system distinguishes one pitch from another",
   "how the retina converts light into neural signals",
   "why an unchanging stimulus fades from awareness"], ans=0,
   why="EK 1.6.F.1 states that pain is processed both in the body and in the brain and that gate control theory is one attempt to describe the complexities of pain."),
 dict(q="A person who can see only in shades of a single color has a color vision deficiency classified as", choices=[
   "monochromatism",
   "dichromatism",
   "prosopagnosia",
   "blindsight"], ans=0,
   why="EK 1.6.B.4.iii names dichromatism and monochromatism as the two forms of color vision deficiency; the mono- form leaves a single color dimension, the di- form leaves two."),
 dict(q="A man whose leg was amputated years ago reports aching in the foot that is no longer there. This experience is called", choices=[
   "phantom limb sensation",
   "sensory adaptation",
   "blindsight",
   "synesthesia"], ans=0,
   why="EK 1.6.F.1 states that phantom limb sensation occurs when people who have lost limbs report sensation or pain where the limb used to be, and it is offered there as evidence that pain is processed in the brain as well as in the body."),
 dict(q="One patient can describe objects placed in front of her but cannot recognize her own family members' faces. A second patient reports seeing nothing at all yet reliably points to lights she says she cannot see. These two patterns are, in order,", choices=[
   "prosopagnosia and blindsight",
   "blindsight and prosopagnosia",
   "monochromatism and dichromatism",
   "synesthesia and sensory adaptation"], ans=0,
   why="EK 1.6.B.5 names prosopagnosia as face blindness and blindsight as the other disorder following damage mainly to the occipital lobes; the stem describes each by its defining behavior rather than its label."),
 dict(q="In the auditory system, the pitch of a sound is determined by its wavelength, and its loudness is determined by its", choices=[
   "amplitude",
   "duration",
   "location in space",
   "distance from the ear"], ans=0,
   why="EK 1.6.C.1 states that sound occurs through the movement of air molecules at different wavelengths, called pitch, and amplitudes, called loudness."),
 dict(q="Place theory explains pitch perception by proposing that", choices=[
   "different pitches stimulate different locations along the auditory structures",
   "the rate at which neurons fire matches the frequency of the sound",
   "groups of neurons take turns firing to encode very high frequencies",
   "the brain compares the arrival time of a sound at each ear"], ans=0,
   why="EK 1.6.C.2 lists place, volley, and frequency theories as accounts of pitch perception. Place theory locates pitch in position along the auditory structures; the second option is frequency theory (firing rate matches the sound), the third is volley theory (neurons alternate to encode rates no single neuron could match), and the fourth is sound localization, which is a different question entirely."),
 dict(q="Which statement correctly distinguishes the vestibular sense from kinesthesis?", choices=[
   "the vestibular sense governs balance and is detected primarily by the semicircular canals, while kinesthesis is the sense of one's own body movement",
   "the vestibular sense is the sense of one's own body movement, while kinesthesis governs balance through the semicircular canals",
   "both refer to balance, but only one operates while a person is standing still",
   "both refer to body movement, but only one requires looking at the moving limb"], ans=0,
   why="EK 1.6.G.1 assigns balance to the vestibular sense and the semicircular canals; EK 1.6.G.2 defines kinesthesis as the sense of one's body movement, which allows coordinated movement without looking at the parts of the body."),
 dict(q="Sound localization refers to the process by which a person", choices=[
   "identifies where in the environment a sound is coming from",
   "distinguishes a high pitch from a low pitch",
   "judges whether a sound is loud enough to be heard",
   "recovers hearing sensitivity after a loud noise ends"], ans=0,
   why="EK 1.6.C.3 states that sound localization describes how we identify where sounds in our environment are coming from."),
 dict(q="Which statement correctly distinguishes conduction deafness from sensorineural deafness?", choices=[
   "conduction deafness involves the structures that carry sound waves inward, while sensorineural deafness involves the receptor and nerve pathway",
   "conduction deafness involves the receptor and nerve pathway, while sensorineural deafness involves the structures that carry sound waves inward",
   "conduction deafness affects only high pitches, while sensorineural deafness affects only low pitches",
   "conduction deafness results from aging, while sensorineural deafness never does"], ans=0,
   why="EK 1.6.C.4 names conduction and sensorineural deafness as the two types of hearing loss; the distinction is where the failure lies -- in the mechanical conduction of sound or in the receptors and neural pathway."),
 dict(q="Which sense is unusual in that it is not processed first in the thalamus?", choices=[
   "smell",
   "vision",
   "hearing",
   "touch"], ans=0,
   why="EK 1.6.D.1 states that smell is the only sense not processed first in the thalamus of the brain."),
 dict(q="Pheromones are best described as", choices=[
   "chemical messages detected by the olfactory system",
   "receptors on the tongue that respond to bitter tastes",
   "cells in the retina that respond to long wavelengths",
   "structures in the inner ear that detect head position"], ans=0,
   why="EK 1.6.D.1 states that pheromones produce chemical messages for the olfactory system."),
 dict(q="A person with a heavy head cold reports that her food has almost no flavor, although her tongue is unaffected. The best explanation is that", choices=[
   "taste sensations are muted or not experienced without the sense of smell",
   "the taste receptors on the tongue are temporarily destroyed by illness",
   "she has become a nontaster rather than a supertaster",
   "her thalamus is no longer processing gustatory information"], ans=0,
   why="EK 1.6.D.4 states that the chemical senses interact to create the sensation of taste and that without the sense of smell, taste sensations are either muted or not experienced."),
]
