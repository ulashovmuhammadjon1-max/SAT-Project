"""Key audit for AP PSYCHOLOGY 1.6 Sensation.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor -- the machine-checkable half. The claim states
the specific framework assertion the key rests on, which is the half a human
audits, and it is the only defence a psychology bank has against a wrong key.

Topic 1.6 carries seven learning objectives, more than any other topic in Unit 1,
and a sensation bank left to itself drifts onto vision. Coverage was therefore
allocated deliberately and is recorded here so it can be checked rather than
assumed:

    1.6.A thresholds and adaptation   items 1-8    (8)
    1.6.B vision                      9,10,12,14,16,17,18,20,22  (9)
    1.6.C hearing                     23,24,26,27  (4)
    1.6.D chemical senses             13,15,28,29,30  (5)
    1.6.E touch                       11   (1)
    1.6.F pain                        19,21  (2)
    1.6.G vestibular and kinesthetic  25   (1)

Items 3.B and 3.C (data and statistics) are suggested skills for this topic, but
Unit 1's research-design and data items are carried by Topics 1.1, 1.2 and 1.5,
each of which has one learning objective against this topic's seven. Spending
slots here on content is the deliberate trade.

The distinctions this topic invites a writer to blur, tested against each other
on purpose: sensation (detect and transduce) vs perception (organize and
interpret, which is Topic 2.1, not this one); absolute threshold (detect a
stimulus at all, 50% of the time) vs just-noticeable difference (detect a CHANGE)
vs Weber's law (how large that change must be, proportionally); rods (periphery,
low light, no color) vs cones (fovea, color and detail); trichromatic (three cone
types, by wavelength) vs opponent-process (paired ganglion cells, explaining
afterimages); prosopagnosia (sees but cannot recognise faces) vs blindsight
(reports no sight yet responds accurately); conduction deafness (the mechanical
path inward) vs sensorineural deafness (receptors and nerve); vestibular
(balance, semicircular canals) vs kinesthesis (own body movement).

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p1_6

CLAIMS = [
 ("detecting information from the environment and transducing",
  "EK 1.6.A.1: sensation is detecting information from the environment that meets a certain threshold and transducing stimuli into neurochemical messages for processing in the brain. The first distractor is perception -- organizing and interpreting -- which EK 1.6.A.1 explicitly parks in the brain as a separate process and which Topic 2.1 covers."),
 ("conversion of physical stimulus energy into neural signals",
  "EK 1.6.A.1 uses transduction for the conversion of stimuli into neurochemical messages. It is a change of FORM, which is why the distractor describing transfer between neurons -- the neural transmission of Topic 1.3 -- is wrong rather than merely imprecise."),
 ("at least 50 percent of the time",
  "EK 1.6.A.1, verbatim: the absolute threshold occurs when a stimulus can be detected at least 50% of the time. The '100 percent' distractor is the specific misreading the number exists to correct."),
 ("just-noticeable difference",
  "EK 1.6.A.2 pairs the just-noticeable difference with detection of CHANGE in stimuli, whereas the absolute threshold (EK 1.6.A.1) concerns detecting a stimulus at all. The two are adjacent in the framework and are the pair most often swapped."),
 ("degree to which two stimuli must differ",
  "EK 1.6.A.2: Weber's law describes the degree to which stimuli need to be different for the difference to be detected. The remaining options are the absolute threshold, sensory adaptation, and synesthesia -- every one of them a real term from this same topic, so the item discriminates within the topic."),
 ("sensory adaptation",
  "EK 1.6.A.2 names sensory adaptation as the account of diminished sensitivity to stimuli. An unchanging stimulus fading from awareness is the standard demonstration."),
 ("constantly work together",
  "EK 1.6.A.3, near verbatim: the sensory systems constantly work together in a process called sensory interaction. The keyed wording keeps 'work together', which is what separates interaction from dominance of one sense over another."),
 ("synesthesia",
  "EK 1.6.A.3: synesthesia is an experience of sensation in which one system of sensation is experienced through another. Hearing notes as colors is exactly one system experienced through another."),
 ("photosensitive surface at the back of the eye",
  "EK 1.6.B.1, verbatim. The distractors are the lens (EK 1.6.B.2), the visual cortex (EK 1.4.A.4.i), and the visual nerve (EK 1.6.B.1's own blind-spot sentence), so each is a real structure with a different assigned role."),
 ("no receptor cells at the point where the visual nerve exits",
  "EK 1.6.B.1 identifies the blind spot as the place where the visual nerve exits the eye, and offers it as evidence that the retinal image is incomplete -- which is why the framework immediately adds that the brain fills in the gaps."),
 ("warm and cold receptors in the skin",
  "EK 1.6.E.1: the sensation of 'hot' is produced by the activation of warm AND cold receptors in the skin. The single-receptor distractor is the intuitive answer and the one the EK exists to correct."),
 ("lens focuses visual stimuli onto the retina",
  "EK 1.6.B.2: visual stimuli are focused onto the retina by the lens via a process called accommodation. The same EK adds that altering this process produces nearsightedness or farsightedness, which is why accommodation is a focusing process and not an adaptation to darkness."),
 ("sweet, sour, salty, bitter, umami, and oleogustus",
  "EK 1.6.D.2 lists exactly these six as the types of taste. The four-item distractor is the older account that omits umami and oleogustus, and it is the one most reference material still gives -- which is the reason to test it."),
 ("periphery of the eye and detect shapes and movement in low light but not color",
  "EK 1.6.B.3: rods lie in the periphery, detect shapes and movement but not color, are mainly activated in low-light environments, and play a role in light and dark adaptation. The first distractor is the cone description from EK 1.6.B.4.i, so the item tests the rod/cone contrast directly."),
 ("number of taste receptors on the tongue",
  "EK 1.6.D.3: the number of taste receptors on the tongue is related to how sensitive people are to tastes, classifying them as supertasters, medium tasters, or nontasters. The key states the mechanism rather than the label, so recognising the word 'supertaster' is not enough."),
 ("processing color and fine detail",
  "EK 1.6.B.4.i: photoreceptor cells located in the fovea that process color and detail are called cones. Paired against the rod item so the fovea/periphery and color/no-color contrasts both have to be known."),
 ("short, medium, and long wavelengths",
  "EK 1.6.B.4.i names blue (short wavelengths), green (medium), and red (long) cones in the retina. The paired-opponent distractor is the opponent-process account from EK 1.6.B.4.ii -- the real competing theory, not a straw man, which is what makes the item worth asking."),
 ("ganglion cells operating in opposing pairs",
  "EK 1.6.B.4.ii: afterimages result when certain ganglion cells in the retina are activated while others are not, and the ganglion cells involved in this opponent process are red/green, blue/yellow, and black/white. Green-then-red is the standard demonstration of that pairing."),
 ("complexities of how pain is processed in the body and in the brain",
  "EK 1.6.F.1: pain is processed both in the body and in the brain, and gate control theory is one attempt to describe the complexities of pain. The framework's own hedge -- 'one attempt to describe' -- is preserved in the key rather than upgraded to a settled mechanism."),
 ("monochromatism",
  "EK 1.6.B.4.iii names dichromatism and monochromatism as the forms of color vision deficiency. Seeing in shades of a single color is the mono- case; dichromatism, the other option, leaves two color dimensions rather than one."),
 ("phantom limb sensation",
  "EK 1.6.F.1: phantom limb sensation occurs when people who have lost limbs report sensation or pain where the limb used to be. It sits in the pain EK because it is the framework's evidence that pain is processed in the brain and not only at the site."),
 ("prosopagnosia and blindsight",
  "EK 1.6.B.5 names prosopagnosia (face blindness) and blindsight as disorders following damage mainly to the occipital lobes. The stem describes each by its defining behaviour and asks for them IN ORDER, so the reversed pairing is a live wrong answer rather than a throwaway."),
 ("amplitude",
  "EK 1.6.C.1: sound occurs through the movement of air molecules at different wavelengths (called pitch) and amplitudes (called loudness). The stem supplies the pitch half so the item turns entirely on the loudness half."),
 ("different pitches stimulate different locations",
  "EK 1.6.C.2 lists place, volley, and frequency theories of pitch perception. Place theory is the positional account; the two rejected theory options are frequency theory and volley theory, and the fourth option is sound localization (EK 1.6.C.3), a different question altogether. All four options are real course content."),
 ("vestibular sense governs balance and is detected primarily by the semicircular canals",
  "EK 1.6.G.1 assigns balance to the vestibular sense and the semicircular canals; EK 1.6.G.2 defines kinesthesis as the sense of one's own body movement, which lets the body move in coordinated ways without looking at its parts. The first distractor is the same sentence with the two senses swapped."),
 ("identifies where in the environment a sound is coming from",
  "EK 1.6.C.3: sound localization describes how we identify where sounds in our environment are coming from. Distinguishing pitch (EK 1.6.C.1) and judging audibility (the absolute threshold, EK 1.6.A.1) are the two nearby questions it is not."),
 ("structures that carry sound waves inward, while sensorineural deafness involves the receptor and nerve pathway",
  "EK 1.6.C.4 names conduction deafness and sensorineural deafness as the two types of hearing loss. The distinction is WHERE the failure lies -- mechanical conduction versus receptors and neural pathway -- and the first distractor is that sentence reversed. The 'never from aging' option is false because EK 1.6.C.4 attributes hearing difficulty to aging as well as damage."),
 ("smell",
  "EK 1.6.D.1, verbatim in substance: smell is the only sense not processed first in the thalamus of the brain. Vision, hearing, and touch -- the three distractors -- all are, which is what makes smell the exception worth naming."),
 ("chemical messages detected by the olfactory system",
  "EK 1.6.D.1: pheromones produce chemical messages for the olfactory system. Each distractor relocates the term to a different sensory system covered in this topic, so the item tests placement as well as definition."),
 ("muted or not experienced without the sense of smell",
  "EK 1.6.D.4: the chemical senses interact to create the sensation of taste, and without the sense of smell, taste sensations are either muted or not experienced. The stem states that the tongue is unaffected, which rules out the receptor-damage and nontaster explanations and leaves the interaction account."),
]

psych_check.check(p1_6, CLAIMS, per_topic=30, n_choices=4)
