"""Key audit for AP PSYCHOLOGY 1.2 Overview of the Nervous System.

One (anchor, claim) per item. The anchor is the substring that must appear in
the keyed choice and in no distractor -- that is the mechanically checkable
part, and it is what catches an off-by-one key or a reordered choice list. The
claim states what the key rests on, in the framework's own terms, so a human can
audit it without re-deriving the whole item.

Topic 1.2 is a strict containment hierarchy, and almost every wrong answer a
student gives is a containment error. The claims below therefore name the level
of the hierarchy at issue, not just the correct label:

    central (brain, spinal cord)
    peripheral
        autonomic (involuntary)
            sympathetic (arousing)
            parasympathetic (calming)
        somatic (voluntary)

Two traps are tested on purpose. Items 3 and 10 separate "the two divisions of
the peripheral system" (autonomic and somatic) from "the two divisions of the
autonomic system" (sympathetic and parasympathetic), which are one level apart
and are the pair students swap. Item 12 tests that the opposing pair is
sympathetic/parasympathetic and not sympathetic/somatic -- the two words start
alike and name unrelated levels.

FOUR choices per item (A-D); see AP_PSYCH_CED.md.
"""
import psych_check
import p1_2

CLAIMS = [
 ("brain and the spinal cord",
  "EK 1.2.A.1: the central nervous system includes the brain and the spinal cord."),
 ("relay messages between the central nervous system and the rest of the body",
  "EK 1.2.A.2: the peripheral nervous system relays messages from the central nervous system to the rest of the body. Its role is transmission, not processing."),
 ("autonomic and somatic",
  "EK 1.2.A.2: the peripheral nervous system includes the autonomic and somatic nervous systems. Sympathetic and parasympathetic sit one level lower, inside the autonomic system, which is why that distractor is the tempting one."),
 ("involuntary, such as heartbeat",
  "EK 1.2.A.2.i: the autonomic nervous system governs processes that are involuntary."),
 ("voluntary, such as deliberately turning",
  "EK 1.2.A.2.ii: the somatic nervous system governs processes that are voluntary."),
 ("autonomic nervous system",
  "EK 1.2.A.2.i: the autonomic nervous system includes the parasympathetic and sympathetic nervous systems."),
 ("the sympathetic nervous system",
  "Raised heart rate, dilated pupils, and suppressed digestion are the arousal pattern produced by the sympathetic division of the autonomic system."),
 ("parasympathetic nervous system",
  "Slowed heart rate and resumed digestion after arousal are the calming, energy-conserving pattern of the parasympathetic division."),
 ("somatic nervous system",
  "Deliberate movement of skeletal muscle is voluntary, which EK 1.2.A.2.ii assigns to the somatic nervous system."),
 ("peripheral nervous system, autonomic nervous system, sympathetic",
  "Containment order: peripheral contains autonomic, which contains sympathetic. The central and peripheral systems are parallel branches, so the option that nests peripheral inside central is wrong for a structural reason, not a labeling one."),
 ("belongs to the central nervous system along with the brain",
  "EK 1.2.A.1 places the spinal cord in the central nervous system. Reflex arcs run through the spinal cord (EK 1.3.A.2) but that does not move it into the autonomic or somatic systems."),
 ("sympathetic and parasympathetic",
  "The opposing pair are the two divisions of the autonomic system, one arousing and one calming. Sympathetic and somatic are not opposites; they belong to different levels of the hierarchy. A system and its own parent cannot oppose each other either."),
 ("sympathetic division of the autonomic nervous system has been activated",
  "Dry mouth, sweating, and quickened breathing are involuntary, so they are autonomic, and they are arousing, so they are sympathetic. Sweat glands are not under somatic control."),
 ("rate at which the stomach digests",
  "Digestion is involuntary and therefore autonomic; lifting, walking, and typing are deliberate skeletal movements and therefore somatic. This is the only item keyed to a NOT stem."),
 ("peripheral nervous system",
  "Messages generated normally in the brain that fail to reach the muscles implicate the relay pathway, which EK 1.2.A.2 identifies as the peripheral nervous system."),
 ("processes the person does not consciously control",
  "Both divisions belong to the autonomic system, which EK 1.2.A.2.i defines as governing involuntary processes. They differ in direction of effect, so the option saying both increase arousal is false of the parasympathetic division."),
 ("runs the body without being asked",
  "The autonomic/somatic distinction in EK 1.2.A.2.i-ii is involuntary versus voluntary. It is not a distinction of location, speed, or thinking versus feeling."),
 ("carries messages to and from the central nervous system rather than originating decisions",
  "EK 1.2.A.2 gives the peripheral system a relay function; EK 1.2.A.1 gives the central nervous system the interaction with all body processes. The student's sentence reverses which system originates."),
 ("sympathetic division for the pounding heart and the somatic division for turning the head",
  "The scenario deliberately pairs one involuntary response (cardiac, sympathetic) with one voluntary response (neck muscles, somatic), so the correct answer requires assigning each to a different division rather than one division to both."),
 ("interacts with all processes in the body",
  "EK 1.2.A.1 states this in those terms. The distractors invert the hierarchy (peripheral containing the brain, central containing the somatic system) or deny that the two systems communicate at all."),
 ("somatic nervous system",
  "Muscles a patient can move on command are under voluntary control, assigned to the somatic nervous system by EK 1.2.A.2.ii."),
 ("prepares the body to expend energy and the other restores and conserves",
  "The two autonomic divisions act on the same organs in opposite directions, which is what makes them complementary. Both are involuntary, so the voluntary/involuntary option is false of the pair."),
 ("heart rate in beats per minute",
  "Science practice 2.B: the dependent variable is the measured outcome, and an operational definition must state the specific measurable procedure. Beats per minute is countable; 'how relaxed the participant feels in general' is not operationalized."),
 ("without random assignment, a pre-existing difference",
  "Science practice 2: participants selected their own group, so this is correlational. A third variable such as baseline fitness is a live rival explanation and causation cannot be claimed."),
 ("spinal cord is central, the nerves in the arm are peripheral",
  "EK 1.2.A.1 and 1.2.A.2 together: brain and spinal cord are central; everything relaying between the central system and the body, including the nerves of the limbs, is peripheral."),
]

psych_check.check(p1_2, CLAIMS, per_topic=25, n_choices=4)
