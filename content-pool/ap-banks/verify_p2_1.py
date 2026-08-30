"""Key audit for AP PSYCHOLOGY 2.1 Perception.

One (anchor, claim) per item, in module order. The anchor must appear in the
keyed choice and in no distractor; the claim states the framework assertion the
key rests on. That written claim is the whole discipline here -- there is no
computation to fall back on, and an unstated assertion is how a wrong key ships.

Two structural facts about this topic drive the item design:

  * EK 2.1.A.4 names exactly FOUR Gestalt principles (closure, figure and
    ground, proximity, similarity) and EK 2.1.B.2 names exactly FIVE monocular
    cues (relative clarity, relative size, texture gradient, linear perspective,
    interposition), with an explicit exclusion statement closing that second
    list. Every scenario item below is keyed to a member of one of those lists,
    and items 11 and 23 test the boundaries of the lists themselves. Nothing
    outside them is ever a key, and no invented cue appears as a distractor.
  * The internal/external split in EK 2.1.A.2 and 2.1.A.3 is a real dividing
    line the framework draws and a student can get backwards: schemas and
    perceptual sets are INTERNAL; contexts, experiences, and cultural
    expectations are EXTERNAL. Items 4 and 5 are keyed to opposite sides of it
    and are adjacent on purpose.

The distinctions tested against each other because they are the ones that
collapse: bottom-up (external sensory information) vs top-down (internal prior
expectation); binocular cues (retinal disparity, convergence -- both eyes) vs
monocular cues (all five of EK 2.1.B.2 -- one eye, flat surfaces); perceptual
constancy (the object's appearance holds while the retinal image changes) vs
apparent movement (motion perceived where there is none); the cocktail party
effect (attention succeeding selectively) vs change blindness (attention
failing).

Item 1 sits on the unit boundary deliberately. Sensation is Topic 1.6 in Unit 1
and perception is here in Unit 2; the superseded nine-unit framework had a single
"Sensation and Perception" unit, so most material a student finds does not draw
the line the current course draws.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p2_1

CLAIMS = [
 ("sensation detects and transduces stimuli; perception organizes and interprets",
  "EK 1.6.A.1 assigns detection and transduction to sensation and identifies later processing in the brain as perception. The first distractor is that sentence reversed, which is the error the two-topic split in the current framework is designed to prevent."),
 ("bottom-up processing",
  "EK 2.1.A.1: bottom-up processing is primarily relying on external sensory information. Working from the color and edge of each puzzle piece, with no expectation of the finished picture, is that reliance with the top-down contribution removed."),
 ("top-down processing",
  "EK 2.1.A.1: top-down processing is relying on internal prior expectations. Reading the expected word instead of the printed letters is prior expectation overriding the sensory data, the mirror image of item 2."),
 ("internal factors that filter perception",
  "EK 2.1.A.2, near verbatim: schemas and perceptual sets are internal factors that filter perceptions of the world. Paired with item 5, which is keyed to the other side of the same distinction."),
 ("external factors that filter perception",
  "EK 2.1.A.3, near verbatim: contexts, experiences, and cultural experiences and expectations are external factors that filter perceptions of the world."),
 ("readiness to perceive something in a particular way because of prior expectation",
  "EK 2.1.A.2 groups perceptual sets with schemas as internal filters, and EK 2.1.A.1 makes prior expectation the top-down route. The distractors are a perceptual constancy (2.1.B.3), convergence (2.1.B.1), and change blindness (2.1.A.5.ii) -- all real terms from this topic."),
 ("closure",
  "EK 2.1.A.4 names closure among the four Gestalt principles. Completing a gapped outline into a whole form is what the principle denotes."),
 ("proximity",
  "EK 2.1.A.4 names proximity. Grouping by nearness in space is what it denotes, and the stem supplies clustering as the only available cue."),
 ("similarity",
  "EK 2.1.A.4 names similarity. The stem specifies that the dots are EVENLY spaced, which removes proximity as a possible explanation and leaves shared color -- without that clause the item would have two defensible answers."),
 ("figure and ground",
  "EK 2.1.A.4 names figure and ground. The reversible vase/faces image is the standard case: the same stimulus supports two assignments of object and background."),
 ("convergence",
  "EK 2.1.A.4's list is closure, figure and ground, proximity, similarity -- and convergence is not on it; EK 2.1.B.1 makes convergence a binocular DEPTH cue. This item tests the boundary of the Gestalt list rather than a single member of it."),
 ("interaction of sensation and perception",
  "EK 2.1.A.5, near verbatim: attention is an interaction of sensation and perception that is affected by internal and external processes. The 'purely internal' distractor contradicts the 'and external' half."),
 ("cocktail party effect",
  "EK 2.1.A.5.i gives the cocktail party effect as the example of selective attention: attending to mentions of one's name or specific topics in loud or distracting environments."),
 ("change blindness",
  "EK 2.1.A.5.ii: change blindness occurs when changes to the environment are not perceived due to inattention. It is the failure case paired against item 13's success case."),
 ("two eyes are set apart, so each receives a slightly different image",
  "EK 2.1.B.1 defines retinal disparity as the difference between the images projecting onto the retina. The three distractors are relative clarity, linear perspective, and interposition -- all monocular cues from EK 2.1.B.2, so the item tests the binocular/monocular line."),
 ("merging of the two eyes' retinal images by the brain",
  "EK 2.1.B.1 defines convergence as the merging of the retinal images by the brain, and groups it with retinal disparity as binocular."),
 ("retinal disparity and convergence",
  "EK 2.1.B.1 names exactly these two as binocular. Every other option pairs cues from EK 2.1.B.2's monocular list (or, in the last case, pairs a monocular cue with a Gestalt principle), so the item can only be answered by knowing which list each term is on."),
 ("linear perspective",
  "EK 2.1.B.2 lists linear perspective among the five monocular cues in scope; converging parallel lines are its defining case."),
 ("texture gradient",
  "EK 2.1.B.2 lists texture gradient; increasingly fine, less distinguishable detail with distance is what the term denotes."),
 ("interposition",
  "EK 2.1.B.2 lists interposition; a nearer object occluding part of a farther one is what it names. Convergence is offered as a distractor because it is a depth cue, but a binocular one from EK 2.1.B.1."),
 ("relative clarity",
  "EK 2.1.B.2 lists relative clarity; haziness with distance is what it denotes. Retinal disparity appears as a distractor to keep the binocular/monocular line in play."),
 ("relative size",
  "EK 2.1.B.2 lists relative size; judging distance from image size for objects assumed similar in actual size is what it names."),
 ("retinal disparity",
  "EK 2.1.B.2's exclusion statement closes the monocular list to relative clarity, relative size, texture gradient, linear perspective, and interposition. Retinal disparity is binocular (EK 2.1.B.1), so it is the one option that does not belong -- the boundary test for the second of this topic's two closed lists."),
 ("perceptual constancy",
  "EK 2.1.B.3: visual perceptual constancies maintain the perception of an object even when the images of the object in the visual field change. A door's trapezoidal retinal image and its perceived rectangular shape is exactly that case."),
 ("perceptual constancy operating on size",
  "EK 2.1.B.3 again, applied to size rather than shape. The shrinking retinal image is read as increasing distance rather than as a shrinking friend, which is what a constancy does."),
 ("apparent movement",
  "EK 2.1.B.4: apparent movement can be visually perceived even when objects are not actually moving. Sequentially flashing lights are the standard demonstration."),
 ("cultural expectations acting as an external filter",
  "EK 2.1.A.3 lists cultural experiences and expectations among the external filters on perception. The stem holds the stimulus identical for both viewers, which rules out every sensory explanation offered -- threshold, retinal disparity, transduction -- and leaves the perceptual one."),
 ("which expectation the participants were given beforehand",
  "Science practice 2.B: the independent variable is the manipulated, assigned condition -- here the expectation. What participants reported is the dependent variable; the figure's ambiguity was held constant for everyone; cultural background was neither manipulated nor assigned."),
 ("perceptual set created by the instructions",
  "EK 2.1.A.2 makes perceptual sets internal filters, and EK 2.1.A.1 places reliance on prior expectation on the top-down side. The instructions installed the expectation, so bottom-up processing -- driven by the figure alone -- is exactly what the result rules out."),
 ("monocular cues give an illusion of depth on flat surfaces, while binocular cues use images from both eyes",
  "EK 2.1.B.2 (monocular cues give the illusion of depth on flat or two-dimensional surfaces) and EK 2.1.B.1 (binocular cues utilize images from each eye), stated together. The first distractor is that sentence with the two halves swapped."),
]

psych_check.check(p2_1, CLAIMS, per_topic=30, n_choices=4)
