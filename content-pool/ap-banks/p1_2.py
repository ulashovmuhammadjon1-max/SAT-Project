# AP PSYCHOLOGY 1.2 Overview of the Nervous System — 25 questions
# CED effective Fall 2024/2025, Unit 1 Biological Bases of Behavior.
# Learning objective 1.2.A (differentiate among the subsystems of the human
# nervous system and their functions); essential knowledge 1.2.A.1 (central
# nervous system = brain + spinal cord), 1.2.A.2 (peripheral nervous system
# relays messages from the CNS to the rest of the body and contains the
# autonomic and somatic divisions), 1.2.A.2.i (autonomic = involuntary,
# containing the sympathetic and parasympathetic divisions), 1.2.A.2.ii
# (somatic = voluntary).
#
# FOUR choices (A-D) -- the current exam's format; see AP_PSYCH_CED.md.
#
# The whole topic is a hierarchy, and the errors students make are hierarchy
# errors: placing the spinal cord in the peripheral system, treating sympathetic
# and somatic as the same thing because both begin with "s", or thinking the
# parasympathetic system opposes the somatic system rather than the sympathetic.
# Items are written to corner each of those directly.
#
# Every key's grounding claim is stated item by item in verify_p1_2.py.
TOPIC = ("1.2", "Overview of the Nervous System", 1)
QUESTIONS = [
 dict(q="The central nervous system consists of", choices=[
   "the brain and the spinal cord",
   "the brain and the sensory organs",
   "the spinal cord and the nerves that reach the limbs",
   "the sympathetic and parasympathetic divisions"], ans=0,
   why="EK 1.2.A.1 defines the central nervous system as the brain and the spinal cord."),
 dict(q="The primary function of the peripheral nervous system is to", choices=[
   "relay messages between the central nervous system and the rest of the body",
   "generate all conscious thought and decision making",
   "store long-term memories for later retrieval",
   "produce the hormones that regulate hunger and sleep"], ans=0,
   why="EK 1.2.A.2 states that the peripheral nervous system relays messages from the central nervous system to the rest of the body."),
 dict(q="The two divisions of the peripheral nervous system are the", choices=[
   "autonomic and somatic nervous systems",
   "sympathetic and parasympathetic nervous systems",
   "brain and spinal cord",
   "sensory and central nervous systems"], ans=0,
   why="EK 1.2.A.2 states that the peripheral nervous system includes the autonomic and somatic nervous systems; sympathetic and parasympathetic are the two divisions one level further down, inside the autonomic system."),
 dict(q="The autonomic nervous system governs processes that are", choices=[
   "involuntary, such as heartbeat and digestion",
   "voluntary, such as raising a hand",
   "carried out entirely within the brain",
   "limited to the transmission of pain signals"], ans=0,
   why="EK 1.2.A.2.i states that the autonomic nervous system governs processes that are involuntary."),
 dict(q="The somatic nervous system governs processes that are", choices=[
   "voluntary, such as deliberately turning one's head",
   "involuntary, such as the constriction of blood vessels",
   "confined to the spinal cord",
   "chemical rather than electrical"], ans=0,
   why="EK 1.2.A.2.ii states that the somatic nervous system governs processes that are voluntary."),
 dict(q="The sympathetic and parasympathetic nervous systems are both divisions of the", choices=[
   "autonomic nervous system",
   "somatic nervous system",
   "central nervous system",
   "spinal cord"], ans=0,
   why="EK 1.2.A.2.i states that the autonomic nervous system includes the parasympathetic and sympathetic nervous systems."),
 dict(q="A hiker suddenly sees a bear. Her heart rate climbs, her pupils widen, and digestion slows. Which division of her nervous system produced these changes?", choices=[
   "The sympathetic nervous system",
   "The parasympathetic nervous system",
   "The somatic nervous system",
   "The central nervous system acting alone"], ans=0,
   why="Arousing the body for vigorous action is the function of the sympathetic division of the autonomic nervous system."),
 dict(q="Twenty minutes after a frightening event has passed, a person's heart rate slows and digestion resumes. This return toward a calm state is produced by the", choices=[
   "parasympathetic nervous system",
   "sympathetic nervous system",
   "somatic nervous system",
   "peripheral nervous system's voluntary division"], ans=0,
   why="Calming the body and conserving energy after arousal is the function of the parasympathetic division of the autonomic nervous system."),
 dict(q="A pianist deliberately moves her fingers across the keys. The nervous system division most directly carrying those commands to her muscles is the", choices=[
   "somatic nervous system",
   "autonomic nervous system",
   "sympathetic nervous system",
   "parasympathetic nervous system"], ans=0,
   why="Deliberate skeletal muscle movement is voluntary, and EK 1.2.A.2.ii assigns voluntary processes to the somatic nervous system."),
 dict(q="Which of the following correctly orders the nervous system from the largest category to the smallest?", choices=[
   "peripheral nervous system, autonomic nervous system, sympathetic nervous system",
   "autonomic nervous system, peripheral nervous system, somatic nervous system",
   "sympathetic nervous system, autonomic nervous system, peripheral nervous system",
   "central nervous system, peripheral nervous system, autonomic nervous system"], ans=0,
   why="The peripheral system contains the autonomic system, which in turn contains the sympathetic division; the central and peripheral systems are parallel branches, so neither contains the other."),
 dict(q="A common error is to describe the spinal cord as part of the peripheral nervous system. The correct classification is that the spinal cord", choices=[
   "belongs to the central nervous system along with the brain",
   "belongs to the somatic nervous system because it carries voluntary commands",
   "belongs to the autonomic nervous system because it controls reflexes",
   "belongs to neither system, forming a third division of its own"], ans=0,
   why="EK 1.2.A.1 places both the brain and the spinal cord in the central nervous system."),
 dict(q="Which pair of nervous system divisions works in opposition to each other?", choices=[
   "sympathetic and parasympathetic",
   "sympathetic and somatic",
   "autonomic and peripheral",
   "central and spinal"], ans=0,
   why="The two divisions of the autonomic system are the opposing pair, one arousing the body and the other calming it; a system and the system that contains it cannot be opposites."),
 dict(q="A person's mouth goes dry, palms sweat, and breathing quickens immediately before a public speech. Which statement best describes what has happened?", choices=[
   "The sympathetic division of the autonomic nervous system has been activated",
   "The somatic nervous system has issued voluntary commands to the sweat glands",
   "The parasympathetic division has increased its activity",
   "The central nervous system has been temporarily disconnected from the body"], ans=0,
   why="Dry mouth, sweating, and rapid breathing are involuntary arousal responses, which places them in the autonomic system's sympathetic division rather than the voluntary somatic system."),
 dict(q="Which of the following is NOT under the direct control of the somatic nervous system?", choices=[
   "the rate at which the stomach digests a meal",
   "lifting a cup to one's mouth",
   "walking across a room",
   "typing a sentence on a keyboard"], ans=0,
   why="Digestion is involuntary and therefore autonomic; the other three are deliberate skeletal movements and therefore somatic."),
 dict(q="A researcher describes the nervous system as having a communication problem in a patient: messages leave the brain normally but never reach the muscles of the legs. The disruption is most likely located in the", choices=[
   "peripheral nervous system",
   "brain's decision-making regions",
   "parasympathetic nervous system",
   "hormone-producing structures outside the nervous system"], ans=0,
   why="Carrying messages from the central nervous system to the rest of the body is exactly the function EK 1.2.A.2 assigns to the peripheral nervous system, so a failure of delivery points there."),
 dict(q="Both the sympathetic and the parasympathetic nervous systems", choices=[
   "act on processes the person does not consciously control",
   "increase heart rate and respiration",
   "operate only during sleep",
   "carry voluntary commands to skeletal muscles"], ans=0,
   why="Both are divisions of the autonomic nervous system, which EK 1.2.A.2.i defines as governing involuntary processes; they differ in direction of effect, not in whether they are voluntary."),
 dict(q="Which everyday description best captures the difference between the autonomic and somatic nervous systems?", choices=[
   "the autonomic system runs the body without being asked; the somatic system does what a person decides to do",
   "the autonomic system handles thinking; the somatic system handles feeling",
   "the autonomic system is in the brain; the somatic system is in the spinal cord",
   "the autonomic system is faster; the somatic system is slower"], ans=0,
   why="EK 1.2.A.2.i and 1.2.A.2.ii distinguish the two divisions by involuntary versus voluntary control, not by location, speed, or the kind of mental content involved."),
 dict(q="A student writes that \"the peripheral nervous system makes decisions and sends them to the brain.\" The best correction is that the peripheral nervous system", choices=[
   "carries messages to and from the central nervous system rather than originating decisions",
   "is located entirely inside the skull",
   "consists of the sympathetic and central divisions",
   "operates only when a person is awake"], ans=0,
   why="EK 1.2.A.2 assigns the peripheral system a relay role between the central nervous system and the body; the central nervous system is where processing occurs."),
 dict(q="During a startling noise, a person's heart pounds and she also deliberately turns her head toward the sound. Which combination of divisions is involved?", choices=[
   "the sympathetic division for the pounding heart and the somatic division for turning the head",
   "the somatic division for the pounding heart and the sympathetic division for turning the head",
   "the parasympathetic division for both responses",
   "the central nervous system for the pounding heart and the autonomic system for turning the head"], ans=0,
   why="The involuntary cardiac response is sympathetic; deliberate movement of the neck muscles is somatic. The scenario is written so that one involuntary and one voluntary response occur together."),
 dict(q="Which statement about the central and peripheral nervous systems is accurate?", choices=[
   "The central nervous system interacts with all processes in the body",
   "The peripheral nervous system contains the brain",
   "The central nervous system contains the somatic nervous system",
   "The two systems never exchange signals with each other"], ans=0,
   why="EK 1.2.A.1 states that the central nervous system includes the brain and spinal cord and interacts with all processes in the body; the other options invert or sever the relationship between the two systems."),
 dict(q="A physician wants to describe which part of a patient's nervous system controls the muscles the patient can move on command. The physician should refer to the", choices=[
   "somatic nervous system",
   "autonomic nervous system",
   "parasympathetic nervous system",
   "central nervous system"], ans=0,
   why="Muscles moved on command are under voluntary control, and EK 1.2.A.2.ii assigns voluntary processes to the somatic nervous system."),
 dict(q="Which of the following best explains why the sympathetic and parasympathetic systems are described as complementary rather than redundant?", choices=[
   "one prepares the body to expend energy and the other restores and conserves it",
   "one operates in the brain and the other in the spinal cord",
   "one is voluntary and the other is involuntary",
   "one carries sensory signals and the other carries only hormones"], ans=0,
   why="Both are involuntary and both act on the same organs, but in opposite directions, so together they regulate arousal rather than duplicating a single function."),
 dict(q="An experiment measures whether a relaxation exercise reduces physiological arousal. The dependent variable is best operationally defined as", choices=[
   "the participant's heart rate in beats per minute measured after the exercise",
   "how relaxed the participant reports feeling in general",
   "whether the participant's parasympathetic nervous system is working",
   "the overall calmness of the laboratory setting"], ans=0,
   why="The dependent variable is the measured outcome, and an operational definition must state a specific measurable procedure; beats per minute is measurable, whereas the other options are vague or describe something other than the outcome."),
 dict(q="A study reports that people who meditate daily have lower resting heart rates than people who do not. Participants chose for themselves whether to meditate. The strongest limitation of this study is that", choices=[
   "without random assignment, a pre-existing difference between the groups could explain the result",
   "heart rate cannot be measured reliably in a laboratory",
   "the study has no dependent variable",
   "resting heart rate is unrelated to the autonomic nervous system"], ans=0,
   why="Self-selection into groups means the study is correlational; a third variable such as baseline fitness could produce the difference, so causation cannot be claimed."),
 dict(q="Which classification is correct?", choices=[
   "the spinal cord is central, the nerves in the arm are peripheral",
   "the spinal cord is peripheral, the brain is central",
   "the nerves in the arm are central, the spinal cord is peripheral",
   "the brain and the nerves in the arm are both central"], ans=0,
   why="EK 1.2.A.1 places the spinal cord with the brain in the central nervous system, leaving the nerves that reach the limbs in the peripheral nervous system."),
 dict(q="Sympathetic arousal is accompanied by the release of a hormone that prepares the body for vigorous action. Among the hormones covered in AP Psychology, that hormone is", choices=[
   "adrenaline",
   "melatonin",
   "leptin",
   "ghrelin"], ans=0,
   why="Of the five hormones EK 1.3.B.3 keeps in scope, adrenaline is the one released during arousal; melatonin governs sleep timing, and leptin and ghrelin signal fullness and hunger."),
 dict(q="In an experiment, half the participants are randomly assigned to practice a slow-breathing exercise for five minutes and the other half sit quietly; heart rate is then measured in both groups. The independent variable is", choices=[
   "whether the participant practiced the breathing exercise",
   "the participant's heart rate after the five minutes",
   "the five-minute duration of the session",
   "the participant's level of autonomic arousal before the study"], ans=0,
   why="The independent variable is what the researcher manipulates and assigns, which here is the presence or absence of the breathing exercise; heart rate is the measured outcome and the duration is held constant for everyone."),
 dict(q="Following an injury, a patient cannot voluntarily move her right leg, yet her heart rate, digestion, and breathing continue normally. The damage is most consistent with an injury affecting the", choices=[
   "somatic nervous system",
   "autonomic nervous system",
   "sympathetic nervous system",
   "parasympathetic nervous system"], ans=0,
   why="Voluntary movement is somatic (EK 1.2.A.2.ii) while heartbeat, digestion, and breathing are involuntary and therefore autonomic (EK 1.2.A.2.i); losing one while the other is intact isolates the somatic system."),
 dict(q="A researcher testing whether a new relaxation recording lowers arousal has every participant listen to the recording and finds that heart rates drop over the session. The most important flaw is that", choices=[
   "there is no comparison group, so the drop could reflect simply sitting still for the same length of time",
   "heart rate is not a valid measure of arousal",
   "the sample was randomly assigned to conditions",
   "the recording should have been played twice"], ans=0,
   why="Without a control group there is nothing to compare the change against, so an effect of the recording cannot be separated from an effect of resting quietly, which the parasympathetic system produces on its own."),
 dict(q="A person can deliberately hold her breath for a time, but breathing resumes on its own once she stops trying. This observation best illustrates that", choices=[
   "breathing is normally governed involuntarily but can be temporarily overridden by voluntary control",
   "breathing is governed entirely by the somatic nervous system",
   "the autonomic nervous system stops functioning during voluntary effort",
   "the sympathetic and parasympathetic systems alternate control of every organ on a fixed schedule"], ans=0,
   why="Breathing is one of the basic functions the autonomic system maintains without conscious direction, yet the somatic system can intervene briefly, which is why a single organ can be reached by both divisions."),
]
