# AP PSYCHOLOGY 2.1 Perception — 30 questions
# CED effective Fall 2024/2025, Unit 2 Cognition.
# Learning objectives 2.1.A (how internal and external factors influence
# perception) and 2.1.B (how visual perceptual processes produce correct or
# incorrect interpretations of stimuli).
#
# Essential knowledge relied on: 2.1.A.1 bottom-up (external sensory
# information) versus top-down (internal prior expectations) processing;
# 2.1.A.2 schemas and perceptual sets as INTERNAL filters; 2.1.A.3 contexts,
# experiences, and cultural expectations as EXTERNAL filters; 2.1.A.4 the four
# Gestalt principles the framework names -- closure, figure and ground,
# proximity, similarity; 2.1.A.5 attention as an interaction of sensation and
# perception; 2.1.A.5.i selective attention and the cocktail party effect;
# 2.1.A.5.ii inattention and change blindness; 2.1.B.1 binocular cues, retinal
# disparity and convergence; 2.1.B.2 the five monocular cues -- relative clarity,
# relative size, texture gradient, linear perspective, interposition; 2.1.B.3
# perceptual constancies; 2.1.B.4 apparent movement.
#
# Exclusion statement respected: EK 2.1.B.2's monocular cue list is CLOSED. No
# cue outside those five is ever a key, and none appears as a distractor either.
#
# Note the unit boundary this topic sits on: SENSATION is Topic 1.6, in Unit 1;
# perception is here. Items 1 and 2 test that line directly because it is the
# one the old nine-unit framework, which had a single "Sensation and
# Perception" unit, taught people to ignore.
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
# Every key's grounding claim is stated item by item in verify_p2_1.py.
TOPIC = ("2.1", "Perception", 2)
QUESTIONS = [
 dict(q="Which of the following best distinguishes sensation from perception?", choices=[
   "sensation detects and transduces stimuli; perception organizes and interprets them",
   "sensation organizes and interprets stimuli; perception detects and transduces them",
   "sensation occurs in the brain; perception occurs in the sense organs",
   "sensation applies to vision only; perception applies to all the other senses"], ans=0,
   why="EK 1.6.A.1 assigns detection and transduction to sensation and identifies the later processing in the brain as perception, which is the subject of Topic 2.1."),
 dict(q="A person assembling a jigsaw puzzle examines the exact color and edge shape of each individual piece with no expectation of what the picture will be. This approach relies mainly on", choices=[
   "bottom-up processing",
   "top-down processing",
   "a perceptual set",
   "change blindness"], ans=0,
   why="EK 2.1.A.1 defines bottom-up processing as primarily relying on external sensory information, which is what building from the features of each piece describes."),
 dict(q="A proofreader misses a typo because she reads the word she expects rather than the letters actually printed. This illustrates", choices=[
   "top-down processing",
   "bottom-up processing",
   "retinal disparity",
   "perceptual constancy"], ans=0,
   why="EK 2.1.A.1 defines top-down processing as relying on internal prior expectations, which is what substituting an expected word for the printed one demonstrates."),
 dict(q="According to the AP Psychology framework, schemas and perceptual sets are", choices=[
   "internal factors that filter perception",
   "external factors that filter perception",
   "binocular depth cues",
   "types of apparent movement"], ans=0,
   why="EK 2.1.A.2 names schemas and perceptual sets as internal factors that filter perceptions of the world, in contrast to the external factors of EK 2.1.A.3."),
 dict(q="Contexts, personal experiences, and cultural expectations are described in the AP Psychology framework as", choices=[
   "external factors that filter perception",
   "internal factors that filter perception",
   "monocular depth cues",
   "forms of selective attention"], ans=0,
   why="EK 2.1.A.3 lists contexts, experiences, and cultural experiences and expectations as external factors that filter perceptions of the world."),
 dict(q="A perceptual set is best described as", choices=[
   "a readiness to perceive something in a particular way because of prior expectation",
   "the tendency for an object to appear the same size despite a changing retinal image",
   "the merging of the two eyes' images by the brain",
   "the inability to notice a change in a scene"], ans=0,
   why="EK 2.1.A.2 groups perceptual sets with schemas as internal filters on perception, which operate through prior expectation rather than through a depth cue or a constancy."),
 dict(q="A person sees a circle drawn with several small gaps in its outline and still perceives a complete circle. This illustrates the Gestalt principle of", choices=[
   "closure",
   "proximity",
   "similarity",
   "figure and ground"], ans=0,
   why="EK 2.1.A.4 names closure among the Gestalt principles; it is the tendency to complete an incomplete form into a whole."),
 dict(q="Dots printed in tight clusters are perceived as several groups rather than as many separate dots. This illustrates the Gestalt principle of", choices=[
   "proximity",
   "closure",
   "similarity",
   "figure and ground"], ans=0,
   why="EK 2.1.A.4 names proximity among the Gestalt principles; it is grouping by nearness in space."),
 dict(q="Red and blue dots scattered evenly across a page are perceived as a red group and a blue group. This illustrates the Gestalt principle of", choices=[
   "similarity",
   "proximity",
   "closure",
   "linear perspective"], ans=0,
   why="EK 2.1.A.4 names similarity among the Gestalt principles; here the dots are equally spaced, so nearness cannot be doing the grouping and only shared color can."),
 dict(q="Seeing a black vase against a white background, and then the same image as two white faces against black, illustrates the Gestalt principle of", choices=[
   "figure and ground",
   "closure",
   "proximity",
   "similarity"], ans=0,
   why="EK 2.1.A.4 names figure and ground among the Gestalt principles; the reversible vase-faces image is the standard demonstration of which region is taken as the object and which as the background."),
 dict(q="Which of the following is NOT one of the Gestalt perceptual principles named in the AP Psychology framework?", choices=[
   "convergence",
   "closure",
   "proximity",
   "similarity"], ans=0,
   why="EK 2.1.A.4 lists closure, figure and ground, proximity, and similarity; convergence is a binocular depth cue from EK 2.1.B.1, not a Gestalt grouping principle."),
 dict(q="Attention is described in the AP Psychology framework as", choices=[
   "an interaction of sensation and perception affected by internal and external processes",
   "a purely internal process unaffected by the environment",
   "a stage of memory that follows retrieval",
   "a binocular depth cue"], ans=0,
   why="EK 2.1.A.5 states that attention is an interaction of sensation and perception that is affected by internal and external processes."),
 dict(q="At a crowded party a person is following one conversation and suddenly notices her own name spoken across the room. This is called", choices=[
   "the cocktail party effect",
   "change blindness",
   "perceptual constancy",
   "apparent movement"], ans=0,
   why="EK 2.1.A.5.i gives the cocktail party effect as the example of selective attention, in which people attend to mentions of their names or specific topics in loud or distracting environments."),
 dict(q="A person watching a video fails to notice that the actor's shirt changed color between two shots. This is an example of", choices=[
   "change blindness",
   "the cocktail party effect",
   "retinal disparity",
   "functional fixedness"], ans=0,
   why="EK 2.1.A.5.ii states that change blindness occurs when changes to the environment are not perceived due to inattention."),
 dict(q="Retinal disparity provides depth information because", choices=[
   "the two eyes are set apart, so each receives a slightly different image",
   "objects farther away appear hazier than nearby objects",
   "parallel lines appear to meet in the distance",
   "a nearer object blocks part of a farther one"], ans=0,
   why="EK 2.1.B.1 defines retinal disparity as the difference between the images projecting onto the retina, a binocular cue; the other three options are monocular cues from EK 2.1.B.2."),
 dict(q="Convergence, as a depth cue, refers to", choices=[
   "the merging of the two eyes' retinal images by the brain",
   "the tendency of textures to appear finer with distance",
   "the persistence of an object's apparent size as it moves away",
   "the perception of motion in a series of still images"], ans=0,
   why="EK 2.1.B.1 defines convergence as the merging of the retinal images by the brain and groups it with retinal disparity as a binocular cue."),
 dict(q="Which pair of depth cues requires the use of both eyes?", choices=[
   "retinal disparity and convergence",
   "relative size and interposition",
   "linear perspective and texture gradient",
   "relative clarity and closure"], ans=0,
   why="EK 2.1.B.1 names retinal disparity and convergence as the binocular cues; every cue in EK 2.1.B.2 is monocular and works with one eye alone."),
 dict(q="A photograph shows a road whose edges appear to draw together in the distance, creating an impression of depth. This monocular cue is", choices=[
   "linear perspective",
   "texture gradient",
   "interposition",
   "relative clarity"], ans=0,
   why="EK 2.1.B.2 lists linear perspective among the five monocular cues in scope; converging parallel lines are its defining case."),
 dict(q="In a photograph a pebbled beach shows individual stones clearly in the foreground and an increasingly fine, smooth surface toward the horizon. This monocular cue is", choices=[
   "texture gradient",
   "linear perspective",
   "relative size",
   "interposition"], ans=0,
   why="EK 2.1.B.2 lists texture gradient among the five monocular cues; increasingly fine detail with distance is what the term denotes."),
 dict(q="One building partly blocks the view of another, so the blocked building is perceived as farther away. This monocular cue is", choices=[
   "interposition",
   "relative clarity",
   "texture gradient",
   "convergence"], ans=0,
   why="EK 2.1.B.2 lists interposition among the five monocular cues; a nearer object occluding a farther one is what it names."),
 dict(q="Distant mountains look hazier than nearby hills, and so are perceived as farther away. This monocular cue is", choices=[
   "relative clarity",
   "relative size",
   "linear perspective",
   "retinal disparity"], ans=0,
   why="EK 2.1.B.2 lists relative clarity among the five monocular cues; haziness with distance is what it denotes, and retinal disparity is binocular rather than monocular."),
 dict(q="Two cars are known to be about the same size, and the one that casts a smaller image is judged to be farther off. This monocular cue is", choices=[
   "relative size",
   "relative clarity",
   "interposition",
   "convergence"], ans=0,
   why="EK 2.1.B.2 lists relative size among the five monocular cues; judging distance from the size of the image cast by objects assumed to be similar is what it names."),
 dict(q="Which of the following is NOT one of the monocular depth cues the AP Psychology Exam will address?", choices=[
   "retinal disparity",
   "texture gradient",
   "interposition",
   "relative size"], ans=0,
   why="EK 2.1.B.2's exclusion statement limits the exam to relative clarity, relative size, texture gradient, linear perspective, and interposition; retinal disparity is a binocular cue from EK 2.1.B.1."),
 dict(q="A door swinging open casts a changing trapezoidal image on the retina, yet it continues to be perceived as a rectangular door. This illustrates", choices=[
   "perceptual constancy",
   "apparent movement",
   "change blindness",
   "a perceptual set"], ans=0,
   why="EK 2.1.B.3 states that visual perceptual constancies maintain the perception of an object even when the images of the object in the visual field change."),
 dict(q="A friend walking away casts a progressively smaller image on the retina, but she is not perceived as shrinking. This is best explained by", choices=[
   "a perceptual constancy operating on size",
   "convergence of the two retinal images",
   "the availability of a texture gradient",
   "the cocktail party effect"], ans=0,
   why="EK 2.1.B.3's perceptual constancies maintain the perception of the object as the retinal image changes; the changing image is the cue for distance rather than for a change in the object."),
 dict(q="A row of light bulbs flashing in sequence is perceived as a single light moving along the row. This illustrates", choices=[
   "apparent movement",
   "retinal disparity",
   "closure",
   "selective attention"], ans=0,
   why="EK 2.1.B.4 states that apparent movement can be visually perceived even when objects are not actually moving."),
 dict(q="Two people from different cultures view the same ambiguous drawing and describe it differently. According to the AP Psychology framework, this difference is best attributed to", choices=[
   "cultural expectations acting as an external filter on perception",
   "a difference in the absolute threshold of the two viewers",
   "one viewer having greater retinal disparity than the other",
   "a failure of transduction in one viewer's visual system"], ans=0,
   why="EK 2.1.A.3 identifies cultural experiences and expectations as external factors that filter perception; the sensory input is identical, so no sensory explanation applies."),
 dict(q="A researcher shows participants an ambiguous figure after telling half of them they will see an animal and the other half that they will see a musical instrument. Participants report seeing what they were told to expect. The independent variable is", choices=[
   "which expectation the participants were given beforehand",
   "what the participants reported seeing",
   "the ambiguity of the figure, which was the same for everyone",
   "the participants' cultural background"], ans=0,
   why="Science practice 2.B: the independent variable is what the researcher manipulates and assigns, which is the expectation given; what participants reported is the dependent variable, and the figure was held constant."),
 dict(q="In the study described above, the finding that expectation shapes what participants report seeing is best explained by", choices=[
   "a perceptual set created by the instructions",
   "bottom-up processing driven entirely by the figure",
   "change blindness caused by inattention",
   "the operation of a binocular depth cue"], ans=0,
   why="EK 2.1.A.2 makes perceptual sets internal filters on perception, and EK 2.1.A.1 makes reliance on prior expectation top-down rather than bottom-up processing."),
 dict(q="Which statement about depth perception is accurate?", choices=[
   "monocular cues give an illusion of depth on flat surfaces, while binocular cues use images from both eyes",
   "binocular cues give an illusion of depth on flat surfaces, while monocular cues use images from both eyes",
   "monocular cues operate only in complete darkness",
   "binocular cues are unnecessary because monocular cues are always more accurate"], ans=0,
   why="EK 2.1.B.2 states that monocular cues give the illusion of depth on flat or two-dimensional surfaces, and EK 2.1.B.1 states that binocular cues use images from each eye; the first distractor is that pairing reversed."),
]
