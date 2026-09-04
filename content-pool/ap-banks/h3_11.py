r"""AP CHEMISTRY 3.11 Spectroscopy and the Electromagnetic Spectrum.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.11.A: explain the relationship between a region of the
electromagnetic spectrum and the types of molecular or electronic transitions
associated with that region.
Suggested skill 4.A, predict and/or explain chemical properties or phenomena
using given chemical theories, models, and representations.

Essential knowledge relied on, in the framework's own words:

  3.11.A.1  Differences in absorption or emission of photons in different
            spectral regions are related to the different types of molecular
            motion or electronic transition:
              i. Microwave radiation is associated with transitions in molecular
                 rotational levels.
             ii. Infrared radiation is associated with transitions in molecular
                 vibrational levels.
            iii. Ultraviolet/visible radiation is associated with transitions in
                 electronic energy levels.

THE WHOLE TOPIC IS THREE PAIRINGS, WHICH IS EXACTLY WHY THEY GET SWAPPED.
Microwave goes with ROTATION, infrared with VIBRATION, ultraviolet and visible
with ELECTRONIC energy levels. verify_h3_11.py transcribes those three
associations once and then reads every key that names a region together with a
transition, checking the pairing against the transcription. A key that pairs
infrared with an electronic transition cannot ship, except at the one item that
asks which claim contradicts the framework, where the stem disowns it and the
check requires that framing.

WHAT THIS TOPIC DOES NOT OWN. The photon equations belong to 3.12 and the
Beer-Lambert law to 3.13, so nothing here computes a photon energy, a frequency
or a wavelength, and verify_h3_11.py asserts that. Nor does anything here rank
the three regions by energy: EK 3.11.A.1 states the associations and does not
order the regions, and 3.12's equations are about one photon rather than about
the layout of the spectrum. An ordering claim would be true and unsourced,
which is the thing this project cuts rather than guesses.

BOTH DIRECTIONS ARE ASKED. The framework's sentence runs region to transition;
a spectroscopist reads it transition to region. Items go both ways, and the
verifier's transcription is consulted in both directions from the same
dictionary, so the two can never drift apart.

NO FIGURES. Every spectrum is a table naming the region in which absorption was
observed.

NOTATION. Plain prose; no math spans are needed in this module.
"""
TOPIC = ("3.11", "Spectroscopy and the Electromagnetic Spectrum", 3)

# Three claimed pairings, exactly one of which the framework does not make.
_T_CHECK = dict(
    headers=["Row", "Region of the spectrum", "Transition claimed for it"],
    rows=[["Row 1", "Microwave", "Molecular rotational levels"],
          ["Row 2", "Infrared", "Molecular vibrational levels"],
          ["Row 3", "Ultraviolet/visible", "Molecular rotational levels"]])

# Three samples, each with the region in which absorption was observed.
_T_SAMPLES = dict(
    headers=["Sample", "Region in which absorption was observed"],
    rows=[["Sample E", "Microwave"],
          ["Sample F", "Infrared"],
          ["Sample G", "Ultraviolet/visible"]])

QUESTIONS = [

 dict(q="According to the framework, differences in the absorption or emission of photons in "
        "different spectral regions are related to what?",
      choices=[
        "The different types of molecular motion or electronic transition",
        "The different masses of the molecules absorbing the photons",
        "The different concentrations of the substances in the sample",
        "The different volumes of the containers used",
        "The different temperatures at which the spectra were recorded"],
      ans=0,
      why="EK 3.11.A.1's lead sentence says exactly that: differences in absorption or "
          "emission of photons in different spectral regions are related to the different "
          "types of molecular motion or electronic transition. Concentration is what the "
          "Beer-Lambert law of topic 3.13 relates absorbance to, which is a separate claim."),

 dict(q="With which kind of transition does the framework associate microwave radiation?",
      choices=[
        "Transitions in molecular rotational levels",
        "Transitions in molecular vibrational levels",
        "Transitions in electronic energy levels",
        "Transitions between phases of matter",
        "Transitions between isotopes of an element"],
      ans=0,
      why="EK 3.11.A.1's first sub-point says microwave radiation is associated with "
          "transitions in molecular rotational levels. Vibrational levels are the second "
          "sub-point's association and electronic levels the third's."),

 dict(q="With which kind of transition does the framework associate infrared radiation?",
      choices=[
        "Transitions in molecular vibrational levels",
        "Transitions in molecular rotational levels",
        "Transitions in electronic energy levels",
        "Transitions between phases of matter",
        "Transitions between nuclear energy levels"],
      ans=0,
      why="EK 3.11.A.1's second sub-point says infrared radiation is associated with "
          "transitions in molecular vibrational levels. Rotational levels belong to the "
          "microwave region under the first sub-point."),

 dict(q="With which kind of transition does the framework associate ultraviolet and visible "
        "radiation?",
      choices=[
        "Transitions in electronic energy levels",
        "Transitions in molecular vibrational levels",
        "Transitions in molecular rotational levels",
        "Transitions between phases of matter",
        "Transitions between nuclear energy levels"],
      ans=0,
      why="EK 3.11.A.1's third sub-point says ultraviolet and visible radiation is associated "
          "with transitions in electronic energy levels, which is the only one of the three "
          "sub-points that concerns electrons rather than the motion of a whole molecule."),

 dict(q="Which region of the spectrum does the framework associate with transitions in "
        "molecular rotational levels?",
      choices=[
        "Microwave",
        "Infrared",
        "Ultraviolet and visible",
        "The framework associates no region with rotational levels",
        "Every region equally"],
      ans=0,
      why="EK 3.11.A.1's first sub-point makes that association, read from the transition "
          "back to the region. The framework's sentence runs the other way, but the pairing "
          "it states is the same in both directions."),

 dict(q="Transitions in molecular vibrational levels are associated by the framework with "
        "which region of the spectrum?",
      choices=[
        "Infrared",
        "Microwave",
        "Ultraviolet and visible",
        "The framework associates no region with vibrational levels",
        "Every region equally"],
      ans=0,
      why="EK 3.11.A.1's second sub-point makes that association. Microwave radiation is "
          "assigned to rotational levels by the sub-point before it, so the two cannot both "
          "belong to the same region."),

 dict(q="Transitions in electronic energy levels belong, in the framework's account, to "
        "which region of the spectrum?",
      choices=[
        "Ultraviolet and visible",
        "Microwave",
        "Infrared",
        "The framework associates no region with electronic levels",
        "Every region equally"],
      ans=0,
      why="EK 3.11.A.1's third sub-point makes that association. The other two sub-points "
          "assign their regions to motions of the molecule as a whole rather than to changes "
          "in the arrangement of its electrons."),

 dict(q="A molecule absorbs a photon of microwave radiation. What does the framework "
        "associate that absorption with?",
      choices=[
        "A transition in its molecular rotational levels",
        "A transition in its molecular vibrational levels",
        "A transition in its electronic energy levels",
        "The breaking of one of its covalent bonds",
        "A change in the number of molecules present"],
      ans=0,
      why="EK 3.11.A.1's lead sentence relates absorption in a spectral region to a type of "
          "transition, and its first sub-point assigns the microwave region to molecular "
          "rotational levels."),

 dict(q="A molecule absorbs a photon of infrared radiation. What does the framework associate "
        "that absorption with?",
      choices=[
        "A transition in its molecular vibrational levels",
        "A transition in its molecular rotational levels",
        "A transition in its electronic energy levels",
        "The breaking of one of its covalent bonds",
        "A change in the phase of the sample"],
      ans=0,
      why="EK 3.11.A.1's second sub-point assigns the infrared region to molecular "
          "vibrational levels, and the lead sentence is what licenses reading an absorption "
          "as a transition of the associated type."),

 dict(q="A molecule absorbs a photon of ultraviolet radiation. What does the framework "
        "associate that absorption with?",
      choices=[
        "A transition in its electronic energy levels",
        "A transition in its molecular vibrational levels",
        "A transition in its molecular rotational levels",
        "A change in the mass of the molecule",
        "A change in the concentration of the solution"],
      ans=0,
      why="EK 3.11.A.1's third sub-point assigns ultraviolet and visible radiation to "
          "transitions in electronic energy levels. Concentration is what topic 3.13's "
          "Beer-Lambert law relates absorbance to, which is a different claim entirely."),

 dict(q="Does the framework's statement cover emission of photons as well as absorption?",
      choices=[
        "Yes, its lead sentence names absorption or emission",
        "No, it names absorption only",
        "No, it names emission only",
        "Yes, but only in the ultraviolet and visible region",
        "The framework does not say"],
      ans=0,
      why="EK 3.11.A.1 opens with differences in absorption OR EMISSION of photons in "
          "different spectral regions, so both directions are covered by the same set of "
          "associations."),

 dict(q="Which kind of transition does the framework NOT associate with infrared radiation?",
      choices=[
        "Transitions in electronic energy levels",
        "Transitions in molecular vibrational levels",
        "Any transition at all, since infrared is not in the framework's list",
        "Transitions of molecules, as opposed to atoms",
        "Transitions that absorb rather than emit a photon"],
      ans=0,
      why="EK 3.11.A.1's third sub-point assigns electronic energy levels to the ultraviolet "
          "and visible region, and its second assigns the infrared region to molecular "
          "vibrational levels. Infrared is in the list, so the option denying that is wrong "
          "as well."),

 dict(q="One of the tabulated rows claims a pairing the framework does not make. Which row is "
        "it?",
      table=_T_CHECK,
      choices=[
        "Row 3",
        "Row 1",
        "Row 2",
        "All three rows are inconsistent with the framework",
        "None of the rows is inconsistent with the framework"],
      ans=0,
      why="EK 3.11.A.1 assigns molecular rotational levels to the microwave region and "
          "electronic energy levels to the ultraviolet and visible region, so a row giving "
          "rotational levels to the ultraviolet and visible region crosses two of the three "
          "sub-points at once."),

 dict(q="How many of the tabulated rows state a pairing the framework does make?",
      table=_T_CHECK,
      choices=[
        "Exactly two",
        "Exactly one",
        "All three",
        "None of them",
        "It cannot be decided without knowing the substances"],
      ans=0,
      why="Each tabulated row is checked against the association EK 3.11.A.1 states for the "
          "region it names, and the count is taken across the whole table. The identity of "
          "the substance does not enter, since the framework attaches the association to the "
          "spectral region."),

 dict(q="Absorption was observed for each tabulated sample in the region shown. Which sample "
        "underwent a transition in electronic energy levels?",
      table=_T_SAMPLES,
      choices=[
        "Sample G",
        "Sample E",
        "Sample F",
        "All three did",
        "None of them did"],
      ans=0,
      why="EK 3.11.A.1's third sub-point associates ultraviolet and visible radiation with "
          "transitions in electronic energy levels, and the table names the region for each "
          "sample."),

 dict(q="Which tabulated sample underwent a transition in molecular vibrational levels?",
      table=_T_SAMPLES,
      choices=[
        "Sample F",
        "Sample E",
        "Sample G",
        "All three did",
        "None of them did"],
      ans=0,
      why="EK 3.11.A.1's second sub-point associates infrared radiation with transitions in "
          "molecular vibrational levels, and the table names the region in which each "
          "sample's absorption was observed."),

 dict(q="Which tabulated sample underwent a transition in molecular rotational levels?",
      table=_T_SAMPLES,
      choices=[
        "Sample E",
        "Sample F",
        "Sample G",
        "All three did",
        "None of them did"],
      ans=0,
      why="EK 3.11.A.1's first sub-point associates microwave radiation with transitions in "
          "molecular rotational levels, and the table names the region for each sample."),

 dict(q="For how many of the tabulated samples does the framework associate the absorption "
        "with a motion of the molecule rather than with an electronic transition?",
      table=_T_SAMPLES,
      choices=[
        "Exactly two",
        "Exactly one",
        "All three",
        "None of them",
        "It cannot be decided from the region alone"],
      ans=0,
      why="EK 3.11.A.1's first two sub-points name molecular rotational and molecular "
          "vibrational levels, both of which are motions of the molecule, while only the "
          "third names electronic energy levels. The count follows from the regions the "
          "table gives."),

 dict(q="A spectroscopist wants to excite a molecular vibration. Which region of the spectrum "
        "does the framework point to?",
      choices=[
        "Infrared",
        "Microwave",
        "Ultraviolet and visible",
        "Any region, since all photons excite vibrations equally",
        "No region, since vibrations cannot be excited by light"],
      ans=0,
      why="EK 3.11.A.1's second sub-point associates infrared radiation with transitions in "
          "molecular vibrational levels, so that is the region to reach for. Predicting a "
          "phenomenon from a given model in this way is what suggested skill 4.A asks for."),

 dict(q="A spectroscopist wants to excite a molecular rotation. Which region of the spectrum "
        "does the framework point to?",
      choices=[
        "Microwave",
        "Infrared",
        "Ultraviolet and visible",
        "Any region, since all photons excite rotations equally",
        "No region, since rotations cannot be excited by light"],
      ans=0,
      why="EK 3.11.A.1's first sub-point associates microwave radiation with transitions in "
          "molecular rotational levels. The infrared region belongs to vibrational levels "
          "under the following sub-point."),

 dict(q="A spectroscopist wants to promote an electron between energy levels. Which region of "
        "the spectrum does the framework point to?",
      choices=[
        "Ultraviolet and visible",
        "Microwave",
        "Infrared",
        "Any region, since all photons move electrons equally",
        "No region, since electrons cannot be moved by light"],
      ans=0,
      why="EK 3.11.A.1's third sub-point associates ultraviolet and visible radiation with "
          "transitions in electronic energy levels, which is the only one of the three "
          "sub-points about electrons."),

 dict(q="What does EK 3.11.A.1 relate to what?",
      choices=[
        "A region of the spectrum to a type of molecular motion or electronic transition",
        "A region of the spectrum to the concentration of the absorbing species",
        "A type of transition to the mass of the molecule undergoing it",
        "A type of transition to the volume of the sample",
        "The temperature of a sample to its colour"],
      ans=0,
      why="EK 3.11.A.1's lead sentence, and learning objective 3.11.A in the same words, tie "
          "a spectral region to the types of molecular or electronic transitions associated "
          "with it. Concentration belongs to topic 3.13's Beer-Lambert law instead."),

 dict(q="Which of the framework's three associations concerns electrons rather than the "
        "motion of a whole molecule?",
      choices=[
        "The one for ultraviolet and visible radiation",
        "The one for microwave radiation",
        "The one for infrared radiation",
        "All three of them",
        "None of them"],
      ans=0,
      why="EK 3.11.A.1's first two sub-points name molecular rotational and molecular "
          "vibrational levels, which are ways a molecule moves, while the third names "
          "electronic energy levels, which concern the arrangement of its electrons."),

 dict(q="Which two of the framework's three associations concern a motion of the molecule?",
      choices=[
        "Those for microwave and infrared radiation",
        "Those for microwave and ultraviolet radiation",
        "Those for infrared and visible radiation",
        "All three of them concern a motion of the molecule",
        "None of them concerns a motion of the molecule"],
      ans=0,
      why="EK 3.11.A.1's first sub-point names molecular ROTATIONAL levels and its second "
          "names molecular VIBRATIONAL levels; both words describe the molecule moving. The "
          "third sub-point's electronic energy levels do not."),

 dict(q="A spectrum shows absorption in the infrared region. What does the framework allow a "
        "student to infer?",
      choices=[
        "That transitions in molecular vibrational levels are taking place",
        "That transitions in electronic energy levels are taking place",
        "That transitions in molecular rotational levels are taking place",
        "That the sample is more concentrated than a reference sample",
        "That the sample contains no molecules at all"],
      ans=0,
      why="EK 3.11.A.1's lead sentence relates absorption in a spectral region to a type of "
          "transition, and its second sub-point supplies the type for the infrared region. "
          "An inference about concentration would need topic 3.13's Beer-Lambert law."),

 dict(q="A spectrum shows absorption in the microwave region. What does the framework allow a "
        "student to infer?",
      choices=[
        "That transitions in molecular rotational levels are taking place",
        "That transitions in molecular vibrational levels are taking place",
        "That transitions in electronic energy levels are taking place",
        "That the sample has changed phase",
        "That a chemical reaction has occurred"],
      ans=0,
      why="EK 3.11.A.1's first sub-point supplies the type of transition for the microwave "
          "region, and its lead sentence is what licenses reading an observed absorption that "
          "way."),

 dict(q="Which region is NOT one of the three the framework names in this statement?",
      choices=[
        "The radio region",
        "The microwave region",
        "The infrared region",
        "The ultraviolet region",
        "The visible region"],
      ans=0,
      why="EK 3.11.A.1's three sub-points name microwave, infrared, and ultraviolet and "
          "visible radiation. Other regions of the spectrum exist, but the framework's "
          "statement here attaches an association to those three only."),

 dict(q="Which claim contradicts the framework?",
      choices=[
        "Infrared radiation is associated with transitions in electronic energy levels",
        "Infrared radiation is associated with transitions in molecular vibrational levels",
        "Microwave radiation is associated with transitions in molecular rotational levels",
        "Ultraviolet and visible radiation is associated with transitions in electronic "
        "energy levels",
        "Absorption and emission are both covered by the framework's statement"],
      ans=0,
      why="EK 3.11.A.1 assigns electronic energy levels to ultraviolet and visible radiation "
          "and molecular vibrational levels to infrared radiation, so attaching electronic "
          "transitions to the infrared region moves one sub-point's transition onto another "
          "sub-point's region. The four rejected statements each appear in the framework."),

 dict(q="A molecule emits a photon and returns to a lower electronic energy level. In which "
        "region does the framework place that photon?",
      choices=[
        "The ultraviolet and visible region",
        "The microwave region",
        "The infrared region",
        "The framework does not associate emission with any region",
        "It depends on the concentration of the sample"],
      ans=0,
      why="EK 3.11.A.1's lead sentence covers emission as well as absorption, and its third "
          "sub-point associates electronic energy levels with ultraviolet and visible "
          "radiation, so the association applies in either direction."),

 dict(q="Which statement lists all three of the framework's associations correctly?",
      choices=[
        "Microwave with rotational levels, infrared with vibrational levels, and ultraviolet "
        "and visible with electronic levels",
        "Microwave with vibrational levels, infrared with rotational levels, and ultraviolet "
        "and visible with electronic levels",
        "Microwave with electronic levels, infrared with rotational levels, and ultraviolet "
        "and visible with vibrational levels",
        "Microwave with rotational levels, infrared with electronic levels, and ultraviolet "
        "and visible with vibrational levels",
        "All three regions are associated with electronic levels"],
      ans=0,
      why="EK 3.11.A.1's three sub-points give exactly those pairings, in that order. Each "
          "rejected option keeps all three regions and all three kinds of transition while "
          "exchanging at least one pair, which is the error this topic is most likely to "
          "produce."),
]
