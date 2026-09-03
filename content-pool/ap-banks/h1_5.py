r"""AP CHEMISTRY 1.5 Atomic Structure and Electron Configuration.

CED effective Fall 2024, Unit 1 Atomic Structure and Properties.
Learning objective 1.5.A: represent the ground-state electron configuration of
an atom of an element or its ions using the Aufbau principle.
Suggested skill 1.A, describe the components of and quantitative information
from models and representations that illustrate particulate-level properties.

Essential knowledge relied on, in the framework's own words:

  1.5.A.1  The atom is composed of negatively charged electrons and a
           positively charged nucleus that is made of protons and neutrons.
  1.5.A.2  Coulomb's law is used to calculate the force between two charged
           particles.  EQN: F_coulombic is proportional to q1 q2 / r^2
  1.5.A.3  In atoms and ions, the electrons can be thought of as being in
           "shells (energy levels)" and "subshells (sublevels)," as described
           by the ground-state electron configuration. Inner electrons are
           called core electrons, and outer electrons are called valence
           electrons. The electron configuration is explained by quantum
           mechanics, as delineated in the Aufbau principle and exemplified in
           the periodic table of the elements.

           Exclusion Statement: The assignment of quantum numbers to electrons
           in subshells of an atom will not be assessed on the AP Exam.

  1.5.A.4  The relative energy required to remove an electron from different
           subshells of an atom or ion or from the same subshell in different
           atoms or ions (ionization energy) can be estimated through a
           qualitative application of Coulomb's law. This energy is related to
           the distance from the nucleus and the effective (shield) charge of
           the nucleus.

HOW UNIT 1 IS PARTITIONED, so that 1.5, 1.6 and 1.7 do not become three ways of
asking the same question. SOCIAL_DEDUPE.md's finding is that repeats come from
topics sharing statements, and these three share the shell model outright.

  * 1.5 (here): writing and reading a ground-state configuration; core against
    valence; Coulomb's law itself; and the relative ionization energy of
    DIFFERENT SUBSHELLS of one atom, or the same subshell in two atoms, which
    is what EK 1.5.A.4 literally says.
  * 1.6: photoelectron spectroscopy -- recovering a configuration from peak
    positions and heights.
  * 1.7: periodicity -- predicting the four listed atomic properties from an
    element's POSITION in the table.

So no item here is answered by knowing where an element sits in the periodic
table, and no item here reads a spectrum.

ON THE EXCLUSION. No item assigns quantum numbers to any electron. Subshells
are named (1s, 2p, 3s) and counted, which the framework does throughout, and
nothing more.

ON AUFBAU EXCEPTIONS. The CED excludes writing configurations for elements that
are exceptions to the Aufbau principle, so chromium and copper appear nowhere.
The one transition metal used, iron, is used as a neutral atom only.

NOTATION. Configurations are hand-written spans with SUPERSCRIPTS --
\(1s^2\,2s^2\,2p^6\,3s^1\) -- because that is precisely what the converter got
wrong when it was tried on Chemistry, setting them as subscripts.
"""
TOPIC = ("1.5", "Atomic Structure and Electron Configuration", 1)

_T_PAIRS = dict(
    headers=["Pair", "Charge on the first particle", "Charge on the second particle",
             "Separation (picometers)"],
    rows=[["Pair 1", "+1", "-1", "100"],
          ["Pair 2", "+2", "-1", "100"],
          ["Pair 3", "+1", "-1", "200"],
          ["Pair 4", "+1", "-2", "200"]])

_T_IE_SUBSHELLS = dict(
    headers=["Subshell the electron is removed from",
             "Energy required (megajoules per mole)"],
    rows=[["1s", "104"], ["2s", "6.84"], ["2p", "3.67"], ["3s", "0.50"]])

_T_IE_SAME_SUBSHELL = dict(
    headers=["Atom", "Protons in the nucleus",
             "Energy to remove one 3s electron (megajoules per mole)"],
    rows=[["Sodium", "11", "0.50"],
          ["Magnesium", "12", "0.74"],
          ["Aluminum", "13", "1.09"]])

_T_COUNTS = dict(
    headers=["Species", "Protons", "Neutrons", "Electrons"],
    rows=[["Species 1", "11", "12", "11"],
          ["Species 2", "11", "12", "10"],
          ["Species 3", "17", "18", "18"],
          ["Species 4", "12", "12", "10"]])

QUESTIONS = [

 dict(q="Which statement describes the composition of an atom?",
      choices=[
        "Negatively charged electrons surround a positively charged nucleus that is "
        "made of protons and neutrons.",
        "Positively charged electrons surround a negatively charged nucleus that is "
        "made of protons and neutrons.",
        "Electrons and protons are both found inside the nucleus, while neutrons "
        "surround it.",
        "The nucleus is made of electrons and neutrons, and protons surround it.",
        "Protons, neutrons and electrons are distributed evenly throughout the volume "
        "of the atom."],
      ans=0,
      why="EK 1.5.A.1, near verbatim: the atom is composed of negatively charged "
          "electrons and a positively charged nucleus that is made of protons and "
          "neutrons. Every rejected option moves a particle into or out of the nucleus "
          "or reverses a sign."),

 dict(q="A neutral sodium atom has eleven electrons. Which of the following is its "
        "ground-state electron configuration?",
      choices=[
        r"\(1s^2\,2s^2\,2p^6\,3s^1\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\)",
        r"\(1s^2\,2s^2\,2p^7\)",
        r"\(1s^2\,2s^2\,3s^1\,2p^6\)",
        r"\(1s^2\,2s^3\,2p^6\)"],
      ans=0,
      why="Filling the subshells in the order the Aufbau principle of EK 1.5.A.3 gives, "
          "and stopping when eleven electrons have been placed, leaves one electron in "
          "the third shell. A p subshell holds at most six electrons and an s subshell "
          "at most two, which rules out two of the rejected forms outright."),

 dict(q="What is the difference between a core electron and a valence electron?",
      choices=[
        "Core electrons are the inner electrons of an atom and valence electrons are "
        "the outer ones.",
        "Core electrons carry a positive charge and valence electrons carry a negative "
        "charge.",
        "Core electrons sit inside the nucleus and valence electrons sit outside it.",
        "Core electrons belong to the nucleus and valence electrons belong to the "
        "shells.",
        "Core electrons are found only in metals and valence electrons only in "
        "nonmetals."],
      ans=0,
      why="EK 1.5.A.3, near verbatim: inner electrons are called core electrons, and "
          "outer electrons are called valence electrons. Both are electrons and both "
          "sit outside the nucleus, since EK 1.5.A.1 puts only protons and neutrons "
          "inside it."),

 dict(q="An atom has the ground-state electron configuration "
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^4\) . How many valence electrons does it have?",
      choices=["Six valence electrons", "Four valence electrons",
               "Two valence electrons", "Ten valence electrons",
               "Sixteen valence electrons"],
      ans=0,
      why="EK 1.5.A.3 calls the outer electrons the valence electrons, and the outermost "
          "shell here is the third, which holds two electrons in its s subshell and four "
          "in its p subshell. Counting only the p subshell gives one rejected value and "
          "counting every electron gives another."),

 dict(q="Two charged particles attract each other with a certain force. If the charge "
        "on one particle is doubled while the separation is unchanged, what happens to "
        "the force?",
      choices=["It doubles.", "It is halved.", "It quadruples.",
               "It falls to one quarter of its original value.", "It is unchanged."],
      ans=0,
      why="EK 1.5.A.2 gives the Coulombic force as proportional to the product of the "
          "two charges divided by the square of the separation, so doubling one charge "
          "doubles the product and therefore the force. The squaring applies to the "
          "distance, not to the charge, which is what the quadrupling option assumes."),

 dict(q="Two charged particles attract each other with a certain force. If the distance "
        "between them is halved while both charges are unchanged, what happens to the "
        "force?",
      choices=["It becomes four times as large.", "It doubles.",
               "It is halved.", "It falls to one quarter of its original value.",
               "It is unchanged."],
      ans=0,
      why="EK 1.5.A.2 puts the separation in the denominator and squared, so halving it "
          "divides the denominator by four and multiplies the force by four. Treating "
          "the dependence as a simple inverse gives the doubling answer instead."),

 dict(q="An oxygen atom gains two electrons to become an oxide ion. What is the "
        "ground-state electron configuration of that ion?",
      choices=[
        r"\(1s^2\,2s^2\,2p^6\)",
        r"\(1s^2\,2s^2\,2p^4\)",
        r"\(1s^2\,2s^2\,2p^2\)",
        r"\(1s^2\,2s^4\,2p^6\)",
        r"\(1s^2\,2s^2\,2p^8\)"],
      ans=0,
      why="A neutral oxygen atom holds eight electrons, so the ion holds ten, and the "
          "Aufbau order of EK 1.5.A.3 places them as two, two and six. The "
          "configuration of the neutral atom is one rejected option, and an eight "
          "electron p subshell is impossible."),

 dict(q="Which of these electron configurations is NOT a ground-state configuration?",
      choices=[
        r"\(1s^2\,2s^2\,2p^5\,3s^1\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^1\)",
        r"\(1s^2\,2s^2\,2p^3\)",
        r"\(1s^2\,2s^1\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^3\)"],
      ans=0,
      why="The Aufbau principle named in EK 1.5.A.3 fills a lower subshell completely "
          "before any electron enters a higher one, and one configuration here starts "
          "the third shell while the 2p subshell still has a vacancy. Every other "
          "option fills in order without gaps."),

 dict(q="In a single atom, which requires more energy: removing an electron from the 1s "
        "subshell or removing one from the 3s subshell? Why?",
      choices=[
        "Removing the 1s electron, because it lies closer to the nucleus and is "
        "shielded by fewer other electrons.",
        "Removing the 3s electron, because it lies farther from the nucleus and so is "
        "held more tightly.",
        "Removing the 3s electron, because outer subshells always hold more electrons.",
        "The two require the same energy, because both electrons belong to the same "
        "atom and the same nucleus.",
        "Removing the 1s electron, because electrons closer to the nucleus carry a "
        "larger negative charge."],
      ans=0,
      why="EK 1.5.A.4 says the energy to remove an electron from different subshells of "
          "an atom is estimated by a qualitative application of Coulomb's law and is "
          "related to the distance from the nucleus and the effective charge. A smaller "
          "separation and less shielding both raise the attraction, and by EK 1.5.A.2 a "
          "smaller separation raises it steeply."),

 dict(q="Four pairs of oppositely charged particles are described in the table. In "
        "which pair is the force of attraction the largest?",
      table=_T_PAIRS,
      choices=["Pair 2", "Pair 1", "Pair 3", "Pair 4",
               "Pairs 2 and 4 are equal and both larger than the others"],
      ans=0,
      why="EK 1.5.A.2 makes the force proportional to the product of the charges over "
          "the square of the separation, so both the charge product and the separation "
          "have to be taken into account. Choosing on charge alone or on distance alone "
          "leads to a different and wrong row."),

 dict(q="A chlorine atom gains one electron to become a chloride ion. Which "
        "ground-state configuration belongs to that ion?",
      choices=[
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^6\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^5\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^4\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^1\,3p^6\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^7\)"],
      ans=0,
      why="A neutral chlorine atom holds seventeen electrons and the ion holds eighteen, "
          "which the Aufbau order of EK 1.5.A.3 places as a filled third shell s and p. "
          "The configuration of the neutral atom is one rejected option and a seven "
          "electron p subshell is impossible."),

 dict(q="An atom has the ground-state configuration "
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^1\) . How many core electrons does it have?",
      choices=["Ten core electrons", "Three core electrons", "Thirteen core electrons",
               "Two core electrons", "Eighteen core electrons"],
      ans=0,
      why="EK 1.5.A.3 calls the inner electrons core electrons, so the count is every "
          "electron outside the outermost shell: the whole first and second shells. The "
          "three electrons in the third shell are the valence electrons, which is the "
          "rejected value a student reaches by counting the wrong group."),

 dict(q="Which statement about shells and subshells is correct, according to the shell "
        "model?",
      choices=[
        "Electrons in an atom can be thought of as occupying shells, which are energy "
        "levels, and subshells within them, as described by the ground-state "
        "configuration.",
        "Each shell contains exactly one subshell, so the two words mean the same thing.",
        "Subshells contain shells, which are the smaller divisions of the two.",
        "Shells describe the arrangement of protons, while subshells describe the "
        "arrangement of electrons.",
        "The shell model applies to neutral atoms only and breaks down entirely for "
        "ions."],
      ans=0,
      why="EK 1.5.A.3, near verbatim: in atoms and ions the electrons can be thought of "
          "as being in shells (energy levels) and subshells (sublevels), as described "
          "by the ground-state electron configuration. The framework applies the same "
          "model to ions, which is what the last rejected option denies."),

 dict(q="Why does the fourth shell begin to fill before the 3d subshell in a "
        "ground-state configuration?",
      choices=[
        "Because the Aufbau principle fills subshells in order of increasing energy, "
        "and the 4s subshell lies lower in energy than the 3d subshell.",
        "Because the third shell can hold only eight electrons in total.",
        "Because d subshells are never occupied in a ground-state configuration.",
        "Because electrons always enter the shell with the largest number first.",
        "Because the 3d subshell holds only two electrons and fills instantly."],
      ans=0,
      why="EK 1.5.A.3 states that the electron configuration is explained by quantum "
          "mechanics as delineated in the Aufbau principle, which orders the subshells "
          "by energy rather than by shell number. A d subshell holds ten electrons and "
          "is occupied in many ground-state configurations."),

 dict(q="Two ions are separated by a fixed distance. One pair carries charges of plus "
        "one and minus one; the other carries plus two and minus one at the same "
        "separation. How do the forces of attraction compare?",
      choices=[
        "The second pair attracts twice as strongly, because the product of the charges "
        "is twice as large.",
        "The second pair attracts four times as strongly, because the charge is squared "
        "in Coulomb's law.",
        "The two pairs attract equally, because the separation is the same.",
        "The first pair attracts more strongly, because smaller charges are held closer "
        "together.",
        "The comparison cannot be made without knowing the masses of the ions."],
      ans=0,
      why="EK 1.5.A.2 makes the force proportional to the product of the two charges "
          "over the square of the separation, so doubling one charge at fixed distance "
          "doubles the product and the force. Only the distance is squared, and mass "
          "does not appear in the relationship at all."),

 dict(q="A magnesium atom loses two electrons to form a magnesium ion. Which "
        "ground-state configuration belongs to that ion?",
      choices=[
        r"\(1s^2\,2s^2\,2p^6\), a total of ten electrons",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\), a total of twelve electrons",
        r"\(1s^2\,2s^2\,2p^4\), a total of eight electrons",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^2\), a total of fourteen electrons",
        r"\(1s^2\,2s^2\,2p^2\), a total of six electrons"],
      ans=0,
      why="A neutral magnesium atom holds twelve electrons and the ion holds ten, and "
          "the two electrons lost are the outermost ones. Removing electrons from an "
          "inner subshell instead, which is what the rejected configurations with a "
          "depleted 2p subshell represent, would not be a ground state."),

 dict(q="The table lists the energy needed to remove one electron from each of four "
        "different subshells of the same atom. Which subshell holds the electron that "
        "lies closest to the nucleus?",
      table=_T_IE_SUBSHELLS,
      choices=["The 1s subshell", "The 3s subshell", "The 2p subshell",
               "The 2s subshell",
               "The distance cannot be inferred from removal energies"],
      ans=0,
      why="EK 1.5.A.4 relates the energy required to remove an electron to its distance "
          "from the nucleus and the effective nuclear charge, and EK 1.5.A.2 makes a "
          "smaller separation mean a stronger attraction. The largest tabulated energy "
          "therefore marks the electron held closest and most tightly."),

 dict(q="A species has eleven protons, twelve neutrons and ten electrons. What is it?",
      choices=[
        "A positively charged ion, because it has one more proton than it has electrons.",
        "A negatively charged ion, because it has more neutrons than protons.",
        "A neutral atom, because protons and neutrons nearly balance.",
        "A positively charged ion, because neutrons carry a positive charge.",
        "A neutral atom, because the neutrons cancel the extra proton."],
      ans=0,
      why="EK 1.5.A.1 gives the electron a negative charge, the proton a positive one "
          "and puts protons and neutrons in the nucleus, so the net charge is set by "
          "the difference between the proton and electron counts. Neutrons carry no "
          "charge and cannot balance anything."),

 dict(q="Two charged particles are moved from a separation of 100 picometers to a "
        "separation of 300 picometers, with both charges unchanged. The force between "
        "them becomes",
      choices=["one ninth of its original value.", "one third of its original value.",
               "three times its original value.", "nine times its original value.",
               "unchanged, since the charges did not change."],
      ans=0,
      why="EK 1.5.A.2 puts the separation in the denominator and squared, so tripling "
          "it divides the force by nine. Treating the dependence as a simple inverse "
          "gives the one third answer."),

 dict(q="Which species in the table carries a charge of minus one?",
      table=_T_COUNTS,
      choices=["Species 3", "Species 1", "Species 2", "Species 4",
               "None of them, because every species listed has more protons than "
               "electrons"],
      ans=0,
      why="EK 1.5.A.1 makes the electron negative and the proton positive, so a net "
          "charge of minus one means exactly one more electron than proton. Neutrons "
          "are uncharged and do not enter the comparison."),

 dict(q="The table gives the energy needed to remove one 3s electron from each of three "
        "different atoms. Which explanation best accounts for the pattern?",
      table=_T_IE_SAME_SUBSHELL,
      choices=[
        "The energy rises as the nuclear charge rises, because a larger positive charge "
        "attracts the 3s electron more strongly at a comparable distance.",
        "The energy rises as the nuclear charge rises, because a larger nucleus pushes "
        "the 3s electron farther away.",
        "The energy falls as the nuclear charge rises, because more protons means more "
        "shielding of the 3s electron.",
        "The energy depends only on which subshell the electron sits in, so the three "
        "values should have been identical.",
        "The pattern is coincidental, since ionization energy is unrelated to nuclear "
        "charge."],
      ans=0,
      why="EK 1.5.A.4 covers exactly this comparison, the same subshell in different "
          "atoms, and attributes it to a qualitative application of Coulomb's law "
          "through distance and effective nuclear charge. EK 1.5.A.2 then makes a "
          "larger positive charge a stronger attraction at fixed separation."),

 dict(q="An atom has the ground-state configuration "
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\) . In which shell are its valence "
        "electrons, and how many are there?",
      choices=["Two electrons in the fourth shell", "Eight electrons in the third shell",
               "Two electrons in the third shell", "Twenty electrons in all four shells",
               "Six electrons in the fourth shell"],
      ans=0,
      why="EK 1.5.A.3 calls the outer electrons the valence electrons, and the "
          "outermost shell occupied here is the fourth, which holds two electrons. "
          "Counting the filled third shell instead is the commonest way to reach a "
          "rejected option."),

 dict(q="Two particles carry charges of the same sign. What does Coulomb's law say "
        "about the force between them?",
      choices=[
        "They repel each other, and the repulsion weakens rapidly as their separation "
        "grows.",
        "They attract each other, and the attraction weakens rapidly as their "
        "separation grows.",
        "They repel each other with a force that does not depend on their separation.",
        "They neither attract nor repel, because like charges cancel.",
        "They attract each other with a force that grows as their separation grows."],
      ans=0,
      why="EK 1.5.A.2 makes the force proportional to the product of the charges over "
          "the square of the separation, so a product of two like signs gives a "
          "repulsion, and the inverse square dependence makes that repulsion fall "
          "steeply with distance."),

 dict(q="How many electrons are described by the ground-state configuration "
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\,3d^6\) ?",
      choices=["Twenty-six electrons", "Twenty electrons", "Eighteen electrons",
               "Thirty electrons", "Sixteen electrons"],
      ans=0,
      why="The superscripts count the electrons in each subshell, so the total is the "
          "sum of two, two, six, two, six, two and six. Stopping at the fourth shell s "
          "subshell and ignoring the d subshell gives one of the rejected values."),

 dict(q="Which of the following is the best statement of the Aufbau principle as the "
        "framework uses it?",
      choices=[
        "Electrons occupy the available subshells starting from the lowest in energy, "
        "which is what produces the ground-state configuration.",
        "Electrons occupy the available subshells starting from the highest in energy "
        "and work downward.",
        "Electrons are distributed equally among all the subshells of an atom.",
        "Electrons fill the outermost shell of an atom first and the innermost shell "
        "last.",
        "Electrons occupy only those subshells whose quantum numbers have been "
        "assigned in advance."],
      ans=0,
      why="EK 1.5.A.3 states that the electron configuration is explained by quantum "
          "mechanics as delineated in the Aufbau principle and exemplified in the "
          "periodic table. Filling from the lowest energy upward is what makes a "
          "configuration the GROUND state rather than an excited one."),

 dict(q="Using the same table of removal energies, which pair of subshells shows the "
        "largest jump in the energy required, and what does that jump indicate?",
      table=_T_IE_SUBSHELLS,
      choices=[
        "Between the 2s and 1s subshells, indicating that the 1s electrons are held far "
        "more tightly than any others in the atom.",
        "Between the 3s and 2p subshells, indicating that the 3s electrons are the most "
        "tightly held.",
        "Between the 2p and 2s subshells, indicating that the second shell is split "
        "into two widely separated shells.",
        "There is no jump, because the four energies fall in equal steps.",
        "Between the 1s and 2s subshells, indicating that the 1s electrons are the most "
        "loosely held."],
      ans=0,
      why="The tabulated energies are compared directly, and the largest gap separates "
          "the innermost subshell from all the rest. EK 1.5.A.4 attributes a large "
          "removal energy to a short distance from the nucleus and a large effective "
          "nuclear charge, which is what an innermost subshell has."),

 dict(q="A neutral calcium atom has twenty electrons. Which ground-state configuration "
        "belongs to it?",
      choices=[
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^2\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,3d^2\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^8\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4p^2\)",
        r"\(1s^2\,2s^2\,2p^6\,3s^2\,3p^6\,4s^1\,3d^1\)"],
      ans=0,
      why="Twenty electrons placed in the Aufbau order of EK 1.5.A.3 fill through the "
          "third shell p subshell and put the last two in the fourth shell s subshell, "
          "which lies lower in energy than the 3d subshell. A p subshell cannot hold "
          "eight electrons, and splitting the last two electrons across two subshells "
          "would not be a ground state."),

 dict(q="Which species in the table has the same number of electrons as a neutral neon "
        "atom, which has ten?",
      table=_T_COUNTS,
      choices=["Species 2 and Species 4", "Species 1 only", "Species 3 only",
               "Species 1 and Species 3", "No species listed has ten electrons"],
      ans=0,
      why="The electron column is read directly, and two of the four species carry ten "
          "electrons despite having different numbers of protons. EK 1.5.A.3 makes the "
          "configuration a description of the electrons, so those two share a "
          "configuration while remaining different elements."),

 dict(q="A student writes the configuration of a neutral boron atom, which has five "
        "electrons, as " r"\(1s^2\,2s^1\,2p^2\) and calls it the ground state. Which "
        "evaluation is correct?",
      choices=[
        "It is wrong, because the 2s subshell can hold two electrons and must be filled "
        "before any electron enters the 2p subshell.",
        "It is wrong, because boron has six electrons rather than five.",
        "It is wrong, because the 1s subshell must hold four electrons.",
        "It is correct, because the superscripts add to five.",
        "It is correct, because electrons may be placed in any subshell as long as the "
        "total is right."],
      ans=0,
      why="The Aufbau principle named in EK 1.5.A.3 fills each subshell in energy order "
          "before moving on, so a configuration that skips a vacancy in a lower "
          "subshell describes an excited state rather than a ground state. The "
          "superscripts do add correctly, which is exactly why the total alone cannot "
          "settle the question."),

 dict(q="Removing one electron from a neutral atom leaves a positive ion. Compared with "
        "removing the first electron, removing a second electron from that ion "
        "generally requires",
      choices=[
        "more energy, because the remaining electrons are held by the same nuclear "
        "charge with one fewer electron sharing the attraction.",
        "less energy, because the ion is already positively charged and wants to lose "
        "more electrons.",
        "the same energy, because the nuclear charge has not changed.",
        "less energy, because the second electron comes from a shell farther from the "
        "nucleus.",
        "no energy at all, because a positive ion releases electrons spontaneously."],
      ans=0,
      why="EK 1.5.A.4 has ionization energy estimated by a qualitative application of "
          "Coulomb's law through distance and effective nuclear charge, and EK 1.5.A.2 "
          "makes a fixed positive nuclear charge pull harder on each of a smaller "
          "number of electrons. The nuclear charge is indeed unchanged, which is why "
          "the reasoning has to turn on the electron count."),
]
