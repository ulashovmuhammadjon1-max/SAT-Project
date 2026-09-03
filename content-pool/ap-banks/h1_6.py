r"""AP CHEMISTRY 1.6 Photoelectron Spectroscopy.

CED effective Fall 2024, Unit 1 Atomic Structure and Properties.
Learning objective 1.6.A: explain the relationship between the photoelectron
spectrum of an atom or ion and (i) the ground-state electron configuration of
the species, and (ii) the interactions between the electrons and the nucleus.
Suggested skill 4.B, explain whether a model is consistent with chemical
theories.

Essential knowledge relied on, in the framework's own words:

  1.6.A.1  The energies of the electrons in a given shell can be measured
           experimentally with photoelectron spectroscopy (PES). The position
           of each peak in the PES spectrum is related to the energy required
           to remove an electron from the corresponding subshell, and the
           relative height of each peak is (ideally) proportional to the number
           of electrons in that subshell.

ON THE TITLE. ``CHEMISTRY_topics.json`` records this topic as "Photoelectron
Spectroscopy Requir" -- the extractor swallowed the first word of the "Required
Course Content" heading that follows it on the CED page (the dump reads
"Requir ed Course Content" there, split by the two-column layout). The real
title is the two words used here. The JSON entry has been corrected to match;
see the note in the report.

ON FIGURES, WHICH IS THE WHOLE PROBLEM WITH THIS TOPIC. A PES spectrum is a
picture, and SCIENCE_BRIEF.md forbids writing a stem that refers to one the
bank cannot show. Every spectrum here is therefore printed as a TABLE of peak
binding energy against relative peak height -- exactly the two quantities EK
1.6.A.1 names -- and every item asks its question of that table. No stem says
"the spectrum shown".

ON THE DATA. Spectra are attributed to unnamed elements, and every key follows
from the ORDERING of the tabulated energies and the RATIOS of the tabulated
heights, never from recalling a measured value. The binding energies used are
of realistic magnitude, but no item turns on their exact size, and no item
attributes a specific measured number to a named element.

HOW THIS TOPIC IS KEPT DISTINCT FROM 1.5 AND 1.7. Topic 1.5 writes
configurations from electron counts and applies Coulomb's law directly; 1.7
predicts atomic properties from position in the periodic table. Everything here
starts from tabulated PES data and reasons back to a configuration or to the
electron-nucleus interaction, which is what LO 1.6.A asks and neither of the
others does.

NOTATION. Configurations are hand-written spans with superscripts.
"""
TOPIC = ("1.6", "Photoelectron Spectroscopy", 1)

_H = ["Peak", "Binding energy (megajoules per mole)", "Relative height"]

# Eleven electrons: 1s 2s 2p 3s at 2, 2, 6, 1.
_T_X = dict(headers=_H, rows=[["Peak 1", "104", "2"], ["Peak 2", "6.84", "2"],
                              ["Peak 3", "3.67", "6"], ["Peak 4", "0.50", "1"]])

# Eight electrons.
_T_Y = dict(headers=_H, rows=[["Peak 1", "52.6", "2"], ["Peak 2", "3.12", "2"],
                              ["Peak 3", "1.31", "4"]])

# Ten electrons, all in the first two shells.
_T_Z = dict(headers=_H, rows=[["Peak 1", "84.0", "2"], ["Peak 2", "4.68", "2"],
                              ["Peak 3", "2.08", "6"]])

# Twelve electrons.
_T_W = dict(headers=_H, rows=[["Peak 1", "126", "2"], ["Peak 2", "9.07", "2"],
                              ["Peak 3", "5.31", "6"], ["Peak 4", "0.74", "2"]])

# Six electrons.
_T_V = dict(headers=_H, rows=[["Peak 1", "28.6", "2"], ["Peak 2", "1.72", "2"],
                              ["Peak 3", "1.09", "2"]])

# Thirteen electrons.
_T_U = dict(headers=_H, rows=[["Peak 1", "151", "2"], ["Peak 2", "12.1", "2"],
                              ["Peak 3", "7.19", "6"], ["Peak 4", "1.09", "2"],
                              ["Peak 5", "0.58", "1"]])

# Ten electrons again, but every peak far higher in energy than in _T_Z.
_T_ION = dict(headers=_H, rows=[["Peak 1", "126", "2"], ["Peak 2", "9.07", "2"],
                                ["Peak 3", "5.31", "6"]])

_T_INNERMOST = dict(
    headers=["Element", "Binding energy of the highest-energy peak (megajoules per mole)",
             "Height of that peak"],
    rows=[["Element J", "28.6", "2"], ["Element K", "52.6", "2"],
          ["Element L", "84.0", "2"], ["Element M", "104", "2"]])

_T_CLAIMED = dict(headers=_H, rows=[["Peak 1", "39.6", "2"], ["Peak 2", "2.45", "2"],
                                    ["Peak 3", "1.45", "3"]])

QUESTIONS = [

 dict(q="In a photoelectron spectrum of a single element, what does the position of a "
        "peak along the binding energy axis correspond to?",
      choices=[
        "The energy required to remove an electron from the subshell that produced the "
        "peak.",
        "The number of electrons occupying the subshell that produced the peak.",
        "The number of protons in the nucleus of the atom.",
        "The mass of the electron that was removed from that subshell.",
        "The wavelength of the light used to carry out the measurement."],
      ans=0,
      why="EK 1.6.A.1 states that the position of each peak in the PES spectrum is "
          "related to the energy required to remove an electron from the corresponding "
          "subshell. Peak height, not peak position, is what the framework ties to the "
          "number of electrons."),

 dict(q="In the same spectrum, what does the relative height of a peak correspond to?",
      choices=[
        "The number of electrons in the subshell that produced the peak, at least "
        "ideally.",
        "The energy required to remove an electron from that subshell.",
        "The distance of that subshell from the nucleus, in picometers.",
        "The number of neutrons in the nucleus of the atom.",
        "The fraction of the sample that was ionized during the measurement."],
      ans=0,
      why="EK 1.6.A.1 states that the relative height of each peak is, ideally, "
          "proportional to the number of electrons in that subshell. The framework "
          "assigns the energy information to peak position instead."),

 dict(q="The table records the photoelectron spectrum of element X. What is the "
        "ground-state electron configuration of element X?",
      table=_T_X,
      choices=[
        r"\(1s^2\,2s^2\,2p^6\,3s^1\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\)",
        r"\(1s^2\,2s^2\,2p^7\)",
        r"\(1s^2\,2s^6\,2p^2\,3s^1\)",
        r"\(1s^1\,2s^2\,2p^6\,3s^2\)"],
      ans=0,
      why="EK 1.6.A.1 makes each peak a subshell, its height the electron count in that "
          "subshell and its position the removal energy, so reading the table from the "
          "highest binding energy downward gives the subshells in Aufbau order with "
          "heights two, two, six and one."),

 dict(q="How many electrons does an atom of element X contain, according to the "
        "tabulated spectrum?",
      table=_T_X,
      choices=["Eleven electrons", "Four electrons", "Ten electrons",
               "Twelve electrons", "One hundred and fifteen electrons"],
      ans=0,
      why="EK 1.6.A.1 makes each peak height proportional to the number of electrons in "
          "that subshell, so the total is the sum of the tabulated heights. Counting "
          "the peaks themselves rather than their heights gives one of the rejected "
          "values."),

 dict(q="Which peak in the tabulated spectrum of element X was produced by electrons in "
        "the subshell closest to the nucleus?",
      table=_T_X,
      choices=["Peak 1", "Peak 4", "Peak 3", "Peak 2",
               "The tallest peak, whichever one that is"],
      ans=0,
      why="EK 1.6.A.1 ties peak position to the energy needed to remove an electron "
          "from that subshell, and EK 1.5.A.4 relates that energy to distance from the "
          "nucleus and effective nuclear charge. The most tightly held electrons are "
          "therefore the ones at the largest binding energy, not the ones in the "
          "largest subshell."),

 dict(q="Element Y gives the spectrum recorded in the table. How many electrons occupy "
        "the outermost occupied subshell of element Y?",
      table=_T_Y,
      choices=["Four electrons", "Two electrons", "Six electrons",
               "Eight electrons", "Three electrons"],
      ans=0,
      why="The outermost subshell is the one whose electrons are held least tightly, so "
          "it produces the peak at the lowest binding energy, and EK 1.6.A.1 makes that "
          "peak's height its electron count. Reading the height of the highest-energy "
          "peak instead gives a rejected value."),

 dict(q="Why does the peak at the largest binding energy in any photoelectron spectrum "
        "have a height corresponding to exactly two electrons?",
      choices=[
        "Because it comes from the 1s subshell, which is the closest to the nucleus and "
        "holds at most two electrons.",
        "Because every subshell in every atom holds exactly two electrons.",
        "Because the instrument can detect only two electrons at the highest energy.",
        "Because the two electrons removed first are always valence electrons.",
        "Because a peak height of two is the smallest height a spectrum can record."],
      ans=0,
      why="EK 1.6.A.1 makes the highest binding energy the most tightly held electrons, "
          "which by EK 1.5.A.4 are the ones nearest the nucleus, and EK 1.5.A.3's shell "
          "model gives the 1s subshell a capacity of two. A p subshell holds six, so "
          "the claim about every subshell is false."),

 dict(q="The table gives the binding energy of the highest-energy peak in the spectrum "
        "of each of four elements. What does the trend across the four indicate about "
        "the interaction between those electrons and the nucleus?",
      table=_T_INNERMOST,
      choices=[
        "The innermost electrons are attracted more strongly as the nuclear charge "
        "increases, so more energy is needed to remove them.",
        "The innermost electrons are attracted less strongly as the nuclear charge "
        "increases, because the extra protons repel one another.",
        "The innermost electrons move farther from the nucleus as the nuclear charge "
        "increases, so the peak shifts higher.",
        "The number of innermost electrons increases across the four elements, which is "
        "why the energy increases.",
        "The trend reflects only the instrument settings and says nothing about the "
        "atoms."],
      ans=0,
      why="LO 1.6.A asks what a spectrum says about the interactions between the "
          "electrons and the nucleus, and EK 1.5.A.2 makes a larger nuclear charge a "
          "stronger attraction at a given distance. The tabulated heights are all the "
          "same, so a change in the number of innermost electrons cannot be the "
          "explanation."),

 dict(q="Element Z gives the spectrum in the table. What is the ratio of the number of "
        "electrons in its second-shell p subshell to the number in its second-shell s "
        "subshell?",
      table=_T_Z,
      choices=["Three to one", "One to three", "One to one", "Six to six",
               "The ratio cannot be found from peak heights"],
      ans=0,
      why="EK 1.6.A.1 makes relative peak height proportional to the number of "
          "electrons in the subshell, so the ratio of two heights is the ratio of two "
          "electron counts directly. The two second-shell peaks are the middle and "
          "lowest binding energies here."),

 dict(q="How many peaks should appear in the photoelectron spectrum of an atom whose "
        "ground-state configuration is " r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^4\) ?",
      choices=["Five peaks", "Three peaks", "Four peaks", "Sixteen peaks",
               "Two peaks"],
      ans=0,
      why="EK 1.6.A.1 assigns one peak to each subshell, so the count of peaks is the "
          "count of occupied subshells rather than the count of shells or of electrons. "
          "Counting the three occupied shells gives one rejected value and counting the "
          "electrons gives another."),

 dict(q="Element W gives the spectrum in the table. Which ground-state configuration is "
        "consistent with it?",
      table=_T_W,
      choices=[
        r"\(1s^2\,2s^2\,2p^6\,3s^2\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^1\)",
        r"\(1s^2\,2s^2\,2p^6\,3p^2\)",
        r"\(1s^2\,2s^2\,2p^8\)",
        r"\(1s^2\,2s^6\,2p^2\,3s^2\)"],
      ans=0,
      why="Reading the tabulated peaks from the highest binding energy downward gives "
          "the subshells in Aufbau order, and EK 1.6.A.1 makes the four heights their "
          "electron counts. Only one option matches all four heights in the right "
          "order."),

 dict(q="Two spectra are recorded. The first shows peaks at 84.0, 4.68 and 2.08 "
        "megajoules per mole with heights 2, 2 and 6. The second, tabulated below, "
        "shows the same three heights but every peak at a much larger binding energy. "
        "What is the most reasonable interpretation?",
      table=_T_ION,
      choices=[
        "The two species have the same number of electrons, but the second has more "
        "protons and so holds every electron more tightly.",
        "The two species are the same element measured twice, and the difference is "
        "instrument error.",
        "The second species has more electrons than the first, which is why its peaks "
        "lie higher.",
        "The second species has fewer protons than the first, so its electrons are "
        "harder to remove.",
        "The second species must have an additional subshell that the first lacks."],
      ans=0,
      why="EK 1.6.A.1 makes the heights the electron counts, and they are identical, so "
          "the electron count is unchanged. LO 1.6.A's second clause and EK 1.5.A.2 "
          "then attribute the uniformly larger removal energies to a stronger "
          "attraction, which a larger nuclear charge supplies."),

 dict(q="Within the second shell of an atom, the 2s and 2p electrons produce peaks at "
        "different binding energies. What does that difference show?",
      choices=[
        "That the two subshells are not equivalent, and 2s electrons are held more "
        "tightly than 2p electrons in the same atom.",
        "That the two subshells belong to different shells after all.",
        "That the 2p subshell contains more protons than the 2s subshell.",
        "That the spectrum was recorded at two different temperatures.",
        "That the 2s and 2p electrons carry different amounts of charge."],
      ans=0,
      why="EK 1.6.A.1 gives each subshell its own peak position, and EK 1.5.A.3 puts "
          "both subshells in the same shell, so a difference in position is a "
          "difference between sublevels rather than between shells. Protons are in the "
          "nucleus by EK 1.5.A.1 and all electrons carry the same charge."),

 dict(q="A student claims that the spectrum tabulated here belongs to an atom with the "
        "ground-state configuration " r"\(1s^2\,2s^2\,2p^6\) . Is the model consistent "
        "with the data?",
      table=_T_CLAIMED,
      choices=[
        "No, because the lowest-energy peak has a height of three rather than six, so "
        "that subshell holds three electrons.",
        "No, because the spectrum shows three peaks and the configuration names only "
        "two subshells.",
        "Yes, because the spectrum shows three peaks and the configuration names three "
        "subshells.",
        "Yes, because the two highest-energy peaks both have a height of two.",
        "The question cannot be answered, because a configuration cannot be tested "
        "against a spectrum."],
      ans=0,
      why="Suggested skill 4.B asks whether a model is consistent with the data, and EK "
          "1.6.A.1 makes each peak height the electron count of its subshell. Two of "
          "the three heights do match the proposed configuration, which is exactly why "
          "the mismatch in the third is decisive."),

 dict(q="Element V gives the spectrum in the table. How many electrons does an atom of "
        "element V contain, and what is the atomic number of the element?",
      table=_T_V,
      choices=[
        "Six electrons, so the atomic number is six.",
        "Three electrons, so the atomic number is three.",
        "Six electrons, so the atomic number is three.",
        "Twelve electrons, so the atomic number is twelve.",
        "The atomic number cannot be found from a spectrum of a neutral atom."],
      ans=0,
      why="EK 1.6.A.1 makes the sum of the peak heights the number of electrons, and a "
          "neutral atom has as many protons as electrons by EK 1.5.A.1, so the atomic "
          "number follows. Counting the peaks rather than their heights gives one "
          "rejected value."),

 dict(q="Element U gives the spectrum in the table. Which subshell holds the electron "
        "that would be removed most easily?",
      table=_T_U,
      choices=[
        "The subshell that produced the peak at the lowest binding energy, which holds "
        "one electron.",
        "The subshell that produced the peak at the highest binding energy, which holds "
        "two electrons.",
        "The subshell that produced the tallest peak, which holds six electrons.",
        "The subshell that produced the peak at the middle binding energy, which holds "
        "six electrons.",
        "Every subshell is equally easy to remove an electron from, since all belong to "
        "the same atom."],
      ans=0,
      why="EK 1.6.A.1 makes peak position the energy required to remove an electron "
          "from that subshell, so the smallest tabulated binding energy marks the "
          "electron that comes off most easily. Peak height carries the electron count "
          "and has no bearing on ease of removal."),

 dict(q="Using the same spectrum of element U, what is the ground-state electron "
        "configuration of the element?",
      table=_T_U,
      choices=[
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^1\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^3\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^1\,3p^2\)",
        r"\(1s^2\,2s^2\,2p^5\,3s^2\,3p^2\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3d^1\)"],
      ans=0,
      why="Ordering the tabulated peaks from the highest binding energy downward gives "
          "the subshells in Aufbau order and their heights give the electron counts two, "
          "two, six, two and one. Only one option reproduces all five."),

 dict(q="Why does a photoelectron spectrum contain no peak at all for a subshell that "
        "is unoccupied in the ground state?",
      choices=[
        "Because peak height is proportional to the number of electrons in a subshell, "
        "and an empty subshell has none to remove.",
        "Because an unoccupied subshell has no binding energy that could be measured.",
        "Because unoccupied subshells lie outside the atom entirely.",
        "Because the instrument records only the two innermost subshells.",
        "Because unoccupied subshells appear as peaks of negative height."],
      ans=0,
      why="EK 1.6.A.1 makes the relative height of a peak proportional to the number of "
          "electrons in that subshell, and a proportionality to zero is zero. The "
          "framework describes no negative heights and no restriction on which "
          "subshells the technique can reach."),

 dict(q="A spectrum shows exactly two peaks, at 6.26 and 0.52 megajoules per mole, with "
        "heights 2 and 1. What is the ground-state configuration of the species?",
      choices=[
        r"\(1s^2\,2s^1\)",
        r"\(1s^1\,2s^2\)",
        r"\(1s^2\,2s^2\)",
        r"\(1s^2\,2p^1\)",
        r"\(1s^3\)"],
      ans=0,
      why="EK 1.6.A.1 assigns one peak per occupied subshell, position giving removal "
          "energy and height giving electron count, so the higher-energy peak of height "
          "two is the innermost subshell and the lower-energy peak of height one is the "
          "next. The Aufbau order of EK 1.5.A.3 fills the second-shell s subshell before "
          "the p subshell."),

 dict(q="Comparing the spectra of two neighboring elements, one with eight electrons and "
        "one with nine, which peak is expected to shift the most in binding energy?",
      choices=[
        "The peak from the innermost subshell, because those electrons feel the full "
        "increase in nuclear charge with almost no additional shielding.",
        "The peak from the outermost subshell, because outer electrons are the ones "
        "that are added.",
        "Neither peak shifts, because both elements have the same number of shells.",
        "Both peaks shift by exactly the same amount, because the nuclear charge "
        "changes by one for every electron.",
        "The peak heights shift rather than the peak positions."],
      ans=0,
      why="LO 1.6.A's second clause concerns the interactions between the electrons and "
          "the nucleus, and EK 1.5.A.4 makes removal energy depend on distance and "
          "effective nuclear charge. An innermost electron sits inside almost all the "
          "other electrons, so an added proton reaches it nearly unshielded."),

 dict(q="An atom's spectrum shows peaks of heights 2, 2 and 6 at successively lower "
        "binding energies. Which statement about that atom is correct?",
      table=_T_Z,
      choices=[
        "Its outermost shell holds eight electrons, two in an s subshell and six in a p "
        "subshell.",
        "Its outermost shell holds six electrons, all in a p subshell.",
        "Its outermost shell holds two electrons, in the subshell of highest binding "
        "energy.",
        "Its outermost shell holds ten electrons, since that is the total.",
        "Its outermost shell cannot be identified without knowing the element."],
      ans=0,
      why="The two lowest binding energies belong to the outermost shell, and EK "
          "1.6.A.1 makes their heights the electron counts, so the outer shell holds "
          "two plus six. The highest-energy peak belongs to the innermost shell "
          "instead."),

 dict(q="What must be true of the sum of all the peak heights in the photoelectron "
        "spectrum of a neutral atom?",
      choices=[
        "It equals the number of electrons in the atom, which for a neutral atom equals "
        "the number of protons.",
        "It equals the number of shells occupied in the atom.",
        "It equals the binding energy of the innermost peak.",
        "It equals twice the number of peaks, since every subshell holds two electrons.",
        "It has no particular meaning, because heights are only relative."],
      ans=0,
      why="EK 1.6.A.1 makes each height proportional to the electrons in one subshell, "
          "so the heights add to the electron total, and EK 1.5.A.1 makes a neutral "
          "atom's electron count equal to its proton count. The heights being relative "
          "is what lets them be compared with one another."),

 dict(q="Two peaks in the spectrum of a single atom have heights of 6 and 2. What is "
        "the relationship between the numbers of electrons that produced them?",
      choices=[
        "The taller peak comes from three times as many electrons as the shorter one.",
        "The taller peak comes from twice as many electrons as the shorter one.",
        "The taller peak comes from four more electrons, but the ratio cannot be found.",
        "The taller peak comes from electrons that are three times harder to remove.",
        "The two peaks come from equal numbers of electrons at different energies."],
      ans=0,
      why="EK 1.6.A.1 makes relative height proportional to electron count, so a ratio "
          "of heights is a ratio of counts. The difficulty of removal is carried by the "
          "peak's position rather than by its height."),

 dict(q="An atom of an element in the third row of the periodic table gives a spectrum "
        "with four peaks. What does the number of peaks establish?",
      choices=[
        "That four subshells are occupied in the ground state of the atom.",
        "That the atom contains four electrons in total.",
        "That the atom occupies the fourth column of the periodic table.",
        "That the atom has four shells occupied in the ground state.",
        "That four different elements were present in the sample."],
      ans=0,
      why="EK 1.6.A.1 pairs one peak with each subshell, so a count of peaks is a count "
          "of occupied subshells. The electron total comes from the heights and the "
          "shell count from which subshells they are, neither of which is the number of "
          "peaks."),

 dict(q="A student says that the tallest peak in a photoelectron spectrum always comes "
        "from the subshell closest to the nucleus. Using the tabulated spectrum of "
        "element X, evaluate the claim.",
      table=_T_X,
      choices=[
        "The claim is wrong: the tallest peak here sits at the third-largest binding "
        "energy, while the innermost subshell produces a peak of height two.",
        "The claim is right: the tallest peak here is also the one at the largest "
        "binding energy.",
        "The claim is wrong, because peak height carries no information at all.",
        "The claim is right, because the innermost subshell always holds the most "
        "electrons.",
        "The claim cannot be tested against a spectrum of a single element."],
      ans=0,
      why="EK 1.6.A.1 assigns the electron count to height and the removal energy to "
          "position, so they are independent readings, and the tabulated spectrum "
          "separates them: its tallest peak and its highest-energy peak are different "
          "peaks."),

 dict(q="What does a photoelectron spectrum measure that a simple count of an element's "
        "electrons does not?",
      choices=[
        "How strongly the electrons in each subshell are held by the nucleus.",
        "How many protons and neutrons the nucleus contains.",
        "How the atom is bonded to its neighbors in a solid.",
        "How much the sample weighs in grams.",
        "How many isotopes of the element are present."],
      ans=0,
      why="EK 1.6.A.1 states that the energies of the electrons in a given shell can be "
          "measured experimentally with PES and that peak position is the removal "
          "energy, which is the part LO 1.6.A calls the interaction between the "
          "electrons and the nucleus. Isotopic composition is what a mass spectrum "
          "supplies under EK 1.2.A.1."),

 dict(q="Element Y's spectrum, tabulated below, is compared with element Z's, in which "
        "the same three subshells appear at 84.0, 4.68 and 2.08 megajoules per mole. "
        "Which conclusion follows?",
      table=_T_Y,
      choices=[
        "Element Z holds each of those subshells more tightly than element Y does, and "
        "element Z also has more electrons in its outermost subshell.",
        "Element Y holds each of those subshells more tightly than element Z does, "
        "because its binding energies are smaller.",
        "The two elements hold their electrons equally tightly, because both have three "
        "peaks.",
        "Element Y has more electrons in total, because it has the smaller binding "
        "energies.",
        "No comparison is possible, because the two spectra were recorded separately."],
      ans=0,
      why="Every corresponding binding energy is larger for the second element, which by "
          "EK 1.6.A.1 means every subshell takes more energy to ionize, and the "
          "outermost peak height rises from four to six, which by the same statement is "
          "an electron count. Both halves of the keyed statement are read from the two "
          "spectra."),

 dict(q="If the relative heights in a spectrum are recorded as 1.00, 1.00 and 3.00 "
        "rather than as 2, 2 and 6, does the interpretation change?",
      choices=[
        "No, because the heights are relative, so only their ratios carry information "
        "about the electron counts.",
        "Yes, because the atom now contains five electrons rather than ten.",
        "Yes, because a height below one cannot correspond to any electrons.",
        "No, because peak heights carry no information in either case.",
        "Yes, because the subshells must be reassigned to different shells."],
      ans=0,
      why="EK 1.6.A.1 makes the height proportional to the number of electrons in the "
          "subshell, and a proportionality fixes ratios rather than absolute values. "
          "Rescaling all three heights by the same factor therefore leaves every ratio, "
          "and so every electron count, unchanged."),

 dict(q="A proposed model states that all the electrons in a given shell of an atom are "
        "held with exactly the same energy. Which feature of real photoelectron spectra "
        "is inconsistent with that model?",
      choices=[
        "Atoms with a filled second shell give two separate peaks for that shell rather "
        "than one.",
        "Atoms with a filled second shell give a single peak of height eight for that "
        "shell.",
        "The innermost peak always has a height of two.",
        "Peak heights are only ever relative rather than absolute.",
        "The peaks of heavier elements lie at larger binding energies."],
      ans=0,
      why="Suggested skill 4.B asks whether a model is consistent with the evidence. EK "
          "1.6.A.1 gives one peak per SUBSHELL, and EK 1.5.A.3 puts the s and p "
          "subshells inside a single shell, so a shell with both occupied produces two "
          "peaks at different energies -- which is exactly what a single shared energy "
          "would forbid."),

 dict(q="A sample gives a spectrum whose peak heights are 2, 2 and 6 and whose lowest "
        "binding energy is much larger than that of a neutral atom with the same "
        "heights. What does the comparison suggest about the sample?",
      choices=[
        "It is a positively charged ion, whose remaining electrons are held more tightly "
        "than in the neutral atom.",
        "It is a negatively charged ion, whose extra electrons are held more tightly.",
        "It is a neutral atom of a lighter element.",
        "It is a mixture of two different elements.",
        "It is the same neutral atom measured with a more powerful instrument."],
      ans=0,
      why="EK 1.6.A.1 makes the equal heights an equal electron count and the larger "
          "positions larger removal energies, and EK 1.5.A.2 attributes a stronger hold "
          "on the same number of electrons to a larger net positive charge. Adding "
          "electrons would raise the total height instead."),
]
