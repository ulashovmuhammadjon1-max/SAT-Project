r"""AP CHEMISTRY 3.12 Properties of Photons.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.12.A: explain the properties of an absorbed or emitted
photon in relationship to an electronic transition in an atom or molecule.
Suggested skill 5.F, calculate, estimate, or predict an unknown quantity from
known quantities by selecting and following a logical computational pathway and
attending to precision.

Essential knowledge relied on, in the framework's own words:

  3.12.A.1  When a photon is absorbed (or emitted) by an atom or molecule, the
            energy of the species is increased (or decreased) by an amount equal
            to the energy of the photon.
  3.12.A.2  The wavelength of the electromagnetic wave is related to its
            frequency and the speed of light by the equation:  EQN: c = lambda
            nu. The energy of a photon is related to the frequency of the
            electromagnetic wave through Planck's equation:  EQN: E = h nu.

THE SWAP THAT MUST NOT SHIP. EK 3.12.A.1 puts ABSORPTION with an INCREASE and
EMISSION with a DECREASE, and it is one sentence with both cases folded into a
parenthesis, which is precisely how a bank ends up keying it backwards.
verify_h3_12.py reads the direction out of every key that states one -- falling
back to the stem where the key states only half -- and checks the pairing with
named booleans rather than by indexing into parallel lists.

THE CHANGE IS EQUAL, NOT MERELY RELATED. The same sentence says the energy of
the species changes BY AN AMOUNT EQUAL TO the energy of the photon. Nothing here
keys a partial transfer, and one item asks that directly.

WHAT THIS TOPIC DOES NOT OWN. 3.11 owns which spectral region goes with which
kind of transition, and 3.13 owns absorbance and the Beer-Lambert law. Neither
appears here, and verify_h3_12.py asserts it.

ARITHMETIC IS THE GATE. Every number a key asserts is recomputed in
verify_h3_12.py from the stimulus alone, using the constants the stems quote:
the speed of light as 3.00 times ten to the eighth metres per second and
Planck's constant as 6.626 times ten to the minus thirty-fourth joule seconds.
Every item is answerable in one or two steps.

NO FIGURES. The photon tables carry frequencies, wavelengths and energies as
numbers with the power of ten named in the column header.

NOTATION. export_units.py does not typeset Chemistry, so every span below is
hand-written. Scientific notation always sits inside a span; unit words stay
plain text.
"""
TOPIC = ("3.12", "Properties of Photons", 3)

_T_FREQ = dict(
    headers=["Photon", "Frequency (in units of \\( 10^{14} \\) per second)"],
    rows=[["Photon 1", "2.0"],
          ["Photon 2", "6.0"],
          ["Photon 3", "4.0"]])

_T_WAVE = dict(
    headers=["Photon", "Wavelength (in units of \\( 10^{-7} \\) metres)"],
    rows=[["Photon J", "2.0"],
          ["Photon K", "6.0"],
          ["Photon L", "3.0"]])

_T_ENERGY = dict(
    headers=["Photon", "Energy (in units of \\( 10^{-19} \\) joules)"],
    rows=[["Photon P", "2.0"],
          ["Photon Q", "5.0"],
          ["Photon R", "3.0"]])

QUESTIONS = [

 dict(q="An atom absorbs a photon. What does the framework say happens to the energy of the "
        "atom?",
      choices=[
        "It increases by an amount equal to the energy of the photon",
        "It decreases by an amount equal to the energy of the photon",
        "It increases by half the energy of the photon",
        "It increases by twice the energy of the photon",
        "It is unchanged, since the photon passes straight through"],
      ans=0,
      why="EK 3.12.A.1 says that when a photon is absorbed by an atom or molecule the energy "
          "of the species is increased by an amount equal to the energy of the photon. Both "
          "halves matter: the direction of the change and its size."),

 dict(q="An atom emits a photon. What does the framework say happens to the energy of the "
        "atom?",
      choices=[
        "It decreases by an amount equal to the energy of the photon",
        "It increases by an amount equal to the energy of the photon",
        "It decreases by half the energy of the photon",
        "It decreases by twice the energy of the photon",
        "It is unchanged, since the photon carries no energy away"],
      ans=0,
      why="EK 3.12.A.1 folds emission into the same sentence as absorption: the energy of the "
          "species is decreased by an amount equal to the energy of the photon. The size of "
          "the change is the same either way; only its sign differs."),

 dict(q="Which equation does the framework give as relating the wavelength of an "
        "electromagnetic wave to its frequency and the speed of light?",
      choices=[
        "\\( c = \\lambda \\nu \\)",
        "\\( c = \\frac{\\lambda}{\\nu} \\)",
        "\\( c = \\frac{\\nu}{\\lambda} \\)",
        "\\( \\lambda = c \\nu \\)",
        "\\( c = \\lambda + \\nu \\)"],
      ans=0,
      why="EK 3.12.A.2 gives that equation, with the speed of light equal to the product of "
          "wavelength and frequency. Because the product is fixed, a longer wavelength must "
          "come with a lower frequency."),

 dict(q="Which equation does the framework call Planck's equation?",
      choices=[
        "\\( E = h \\nu \\)",
        "\\( E = \\frac{h}{\\nu} \\)",
        "\\( E = \\frac{\\nu}{h} \\)",
        "\\( E = h \\lambda \\)",
        "\\( E = h + \\nu \\)"],
      ans=0,
      why="EK 3.12.A.2 says the energy of a photon is related to the frequency of the "
          "electromagnetic wave through Planck's equation and gives it in that form. Energy "
          "goes with frequency directly, not with wavelength."),

 dict(q="The frequency of a photon is doubled. What happens to its energy?",
      choices=[
        "It doubles",
        "It is halved",
        "It quadruples",
        "It is unchanged",
        "It falls to one quarter"],
      ans=0,
      why="EK 3.12.A.2's Planck equation makes the energy of a photon the product of a "
          "constant and the frequency, so any factor applied to the frequency appears "
          "unchanged in the energy."),

 dict(q="The wavelength of an electromagnetic wave is doubled. What happens to its frequency?",
      choices=[
        "It is halved",
        "It doubles",
        "It quadruples",
        "It is unchanged",
        "It falls to one quarter"],
      ans=0,
      why="EK 3.12.A.2 makes the product of wavelength and frequency equal to the speed of "
          "light, which does not change, so doubling one factor of a fixed product halves "
          "the other."),

 dict(q="The wavelength of a photon is halved. What happens to its energy?",
      choices=[
        "It doubles",
        "It is halved",
        "It is unchanged",
        "It quadruples",
        "It falls to one quarter"],
      ans=0,
      why="EK 3.12.A.2's two equations combine: halving the wavelength doubles the frequency "
          "because their product is the fixed speed of light, and doubling the frequency "
          "doubles the energy through Planck's equation."),

 dict(q="A photon has a wavelength of \\( 6.00 \\times 10^{-7} \\) metres. Taking the speed of "
        "light as \\( 3.00 \\times 10^{8} \\) metres per second, what is its frequency?",
      choices=[
        "\\( 5.00 \\times 10^{14} \\) per second",
        "\\( 2.00 \\times 10^{-15} \\) per second",
        "\\( 1.80 \\times 10^{2} \\) per second",
        "\\( 5.00 \\times 10^{15} \\) per second",
        "\\( 1.80 \\times 10^{-14} \\) per second"],
      ans=0,
      why="EK 3.12.A.2's equation rearranged divides the speed of light by the wavelength. "
          "Multiplying the two instead, or dividing the other way round, gives the other "
          "values offered; attending to the powers of ten is what suggested skill 5.F asks "
          "for."),

 dict(q="A photon has a frequency of \\( 5.00 \\times 10^{14} \\) per second. Taking Planck's "
        "constant as \\( 6.626 \\times 10^{-34} \\) joule seconds, what is its energy?",
      choices=[
        "\\( 3.31 \\times 10^{-19} \\) J",
        "\\( 3.31 \\times 10^{19} \\) J",
        "\\( 1.33 \\times 10^{-48} \\) J",
        "\\( 7.55 \\times 10^{47} \\) J",
        "\\( 3.31 \\times 10^{-49} \\) J"],
      ans=0,
      why="EK 3.12.A.2's Planck equation multiplies the constant by the frequency, so the "
          "powers of ten add. Dividing the constant by the frequency, or the frequency by "
          "the constant, gives two of the other values offered."),

 dict(q="A photon has a frequency of \\( 1.00 \\times 10^{15} \\) per second. Taking the speed "
        "of light as \\( 3.00 \\times 10^{8} \\) metres per second, what is its wavelength?",
      choices=[
        "\\( 3.00 \\times 10^{-7} \\) metres",
        "\\( 3.00 \\times 10^{7} \\) metres",
        "\\( 3.00 \\times 10^{23} \\) metres",
        "\\( 3.33 \\times 10^{6} \\) metres",
        "\\( 3.33 \\times 10^{-24} \\) metres"],
      ans=0,
      why="EK 3.12.A.2's equation rearranged divides the speed of light by the frequency. "
          "Multiplying the two instead gives a value larger by many powers of ten, which is "
          "one of the numbers offered."),

 dict(q="An atom absorbs a photon whose energy is \\( 4.0 \\times 10^{-19} \\) joules. By how "
        "much does the energy of the atom change, and in which direction?",
      choices=[
        "It increases by \\( 4.0 \\times 10^{-19} \\) joules",
        "It decreases by \\( 4.0 \\times 10^{-19} \\) joules",
        "It increases by \\( 2.0 \\times 10^{-19} \\) joules",
        "It increases by \\( 8.0 \\times 10^{-19} \\) joules",
        "It does not change"],
      ans=0,
      why="EK 3.12.A.1 makes the change equal in size to the energy of the photon and upward "
          "for an absorption, so the number is carried across unaltered and the direction "
          "follows from which of the two cases the sentence covers."),

 dict(q="An atom emits a photon whose energy is \\( 2.5 \\times 10^{-19} \\) joules. By how "
        "much does the energy of the atom change, and in which direction?",
      choices=[
        "It decreases by \\( 2.5 \\times 10^{-19} \\) joules",
        "It increases by \\( 2.5 \\times 10^{-19} \\) joules",
        "It decreases by \\( 1.25 \\times 10^{-19} \\) joules",
        "It decreases by \\( 5.0 \\times 10^{-19} \\) joules",
        "It does not change"],
      ans=0,
      why="EK 3.12.A.1's parenthesis covers emission with the same equality of size and the "
          "opposite direction, so the atom loses exactly what the photon carries away."),

 dict(q="Which of the tabulated photons carries the greatest energy?",
      table=_T_FREQ,
      choices=[
        "Photon 2",
        "Photon 1",
        "Photon 3",
        "All three carry the same energy",
        "It cannot be decided without the wavelengths"],
      ans=0,
      why="EK 3.12.A.2's Planck equation makes energy proportional to frequency, so the "
          "tabulated photon of highest frequency is the one of highest energy. The wavelength "
          "would give the same ordering, since the two are fixed by each other."),

 dict(q="Which of the tabulated photons has the greatest frequency?",
      table=_T_WAVE,
      choices=[
        "Photon J",
        "Photon K",
        "Photon L",
        "All three have the same frequency",
        "It cannot be decided without the speed of light"],
      ans=0,
      why="EK 3.12.A.2 makes the product of wavelength and frequency the fixed speed of "
          "light, so the shortest tabulated wavelength belongs to the highest frequency. The "
          "value of the constant is not needed to rank them, only to compute any one of "
          "them."),

 dict(q="Which of the tabulated photons carries the least energy?",
      table=_T_WAVE,
      choices=[
        "Photon K",
        "Photon J",
        "Photon L",
        "All three carry the same energy",
        "It cannot be decided from wavelength alone"],
      ans=0,
      why="EK 3.12.A.2's two equations combine to make energy fall as wavelength rises, so "
          "the longest tabulated wavelength carries the least energy. Wavelength alone is "
          "enough to rank them, since the two constants are the same for every photon."),

 dict(q="Taking the speed of light as \\( 3.00 \\times 10^{8} \\) metres per second, what is "
        "the frequency of the photon tabulated as Photon L?",
      table=_T_WAVE,
      choices=[
        "\\( 1.0 \\times 10^{15} \\) per second",
        "\\( 1.0 \\times 10^{14} \\) per second",
        "\\( 9.0 \\times 10^{1} \\) per second",
        "\\( 1.0 \\times 10^{-15} \\) per second",
        "\\( 3.0 \\times 10^{15} \\) per second"],
      ans=0,
      why="EK 3.12.A.2's equation rearranged divides the speed of light by that row's "
          "tabulated wavelength, with the power of ten taken from the column header."),

 dict(q="To which quantity does Planck's equation relate the energy of a photon?",
      choices=[
        "The frequency of the electromagnetic wave",
        "The wavelength of the electromagnetic wave",
        "The speed of light in a vacuum",
        "The number of photons present",
        "The mass of the atom that emitted it"],
      ans=0,
      why="EK 3.12.A.2 says the energy of a photon is related to the FREQUENCY of the "
          "electromagnetic wave through Planck's equation. Wavelength enters only through "
          "the other equation, which ties it to frequency."),

 dict(q="Which equation does the framework use to relate wavelength and frequency?",
      choices=[
        "\\( c = \\lambda \\nu \\)",
        "\\( E = h \\nu \\)",
        "\\( E = h \\lambda \\)",
        "\\( \\nu = h E \\)",
        "\\( \\lambda = h \\nu \\)"],
      ans=0,
      why="EK 3.12.A.2 gives one equation tying wavelength and frequency through the speed of "
          "light and a second tying energy to frequency through Planck's constant. Only the "
          "first contains a wavelength at all."),

 dict(q="An atom undergoes an electronic transition and emits a photon. How does the energy "
        "of the photon compare with the energy lost by the atom?",
      choices=[
        "The two are equal",
        "The photon carries half as much",
        "The photon carries twice as much",
        "The photon carries none of it",
        "The comparison depends on the frequency of the photon"],
      ans=0,
      why="EK 3.12.A.1 says the energy of the species is decreased by an amount EQUAL TO the "
          "energy of the photon, so the two quantities are the same number. The frequency "
          "fixes what that number is without changing the equality."),

 dict(q="Two photons are absorbed by identical atoms, one of higher frequency than the other. "
        "Which produces the larger change in the atom's energy?",
      choices=[
        "The photon of higher frequency, since Planck's equation gives it the larger energy",
        "The photon of lower frequency, since Planck's equation gives it the larger energy",
        "The photon of higher frequency, since a higher frequency means a longer wavelength",
        "Neither, since every photon changes an atom's energy by the same amount",
        "It cannot be decided without the mass of the atoms"],
      ans=0,
      why="EK 3.12.A.2's Planck equation makes energy proportional to frequency, and "
          "EK 3.12.A.1 makes the change in the atom's energy equal to the photon's energy, so "
          "the larger energy produces the larger change."),

 dict(q="A photon carries \\( 1.99 \\times 10^{-18} \\) joules. Taking Planck's constant as "
        "\\( 6.626 \\times 10^{-34} \\) joule seconds, what is its frequency?",
      choices=[
        "\\( 3.00 \\times 10^{15} \\) per second",
        "\\( 3.00 \\times 10^{-15} \\) per second",
        "\\( 1.32 \\times 10^{-51} \\) J",
        "\\( 3.33 \\times 10^{16} \\) per second",
        "\\( 1.32 \\times 10^{51} \\) per second"],
      ans=0,
      why="EK 3.12.A.2's Planck equation rearranged divides the energy by the constant, so "
          "the powers of ten subtract. Multiplying them instead gives a product with a "
          "wildly different exponent, which is one of the values offered."),

 dict(q="A photon has a wavelength of \\( 2.00 \\times 10^{-7} \\) metres. Taking the speed of "
        "light as \\( 3.00 \\times 10^{8} \\) metres per second and Planck's constant as "
        "\\( 6.626 \\times 10^{-34} \\) joule seconds, what is its energy?",
      choices=[
        "\\( 9.94 \\times 10^{-19} \\) J",
        "\\( 9.94 \\times 10^{-20} \\) J",
        "\\( 4.42 \\times 10^{-49} \\) J",
        "\\( 9.94 \\times 10^{19} \\) J",
        "\\( 1.01 \\times 10^{18} \\) J"],
      ans=0,
      why="Both of EK 3.12.A.2's equations are needed: the wavelength gives the frequency "
          "through the speed of light, and the frequency then gives the energy through "
          "Planck's constant. Following that pathway in order is what suggested skill 5.F "
          "asks for."),

 dict(q="EK 3.12.A.1 says the energy of the species changes by an amount EQUAL TO the energy "
        "of the photon. What does that rule out?",
      choices=[
        "That only part of the photon's energy is transferred to the species",
        "That the energy of the species changes at all",
        "That absorption and emission are both covered by the statement",
        "That the photon has an energy given by Planck's equation",
        "That the direction of the change depends on which process occurred"],
      ans=0,
      why="EK 3.12.A.1's word is equal, which makes the whole of the photon's energy the size "
          "of the change. The four rejected statements are each part of what the sentence "
          "does assert."),

 dict(q="The energy of an atom decreased. According to the framework, was a photon absorbed "
        "or emitted?",
      choices=[
        "Emitted",
        "Absorbed",
        "Either, since the framework does not distinguish them",
        "Neither, since a change in energy needs no photon",
        "It depends on the wavelength of the photon"],
      ans=0,
      why="EK 3.12.A.1 pairs emission with a decrease in the energy of the species and "
          "absorption with an increase, so the direction of the change identifies which "
          "process occurred."),

 dict(q="Two photons have wavelengths of 400 nm and 800 nm. How do their energies compare?",
      choices=[
        "The 400 nm photon carries twice the energy",
        "The 800 nm photon carries twice the energy",
        "The 400 nm photon carries half the energy",
        "The two carry the same energy",
        "The comparison needs Planck's constant to be given"],
      ans=0,
      why="EK 3.12.A.2's two equations make energy inversely proportional to wavelength, so "
          "halving the wavelength doubles the energy. The constants are the same for both "
          "photons, so they cancel out of the comparison."),

 dict(q="How are the energy of a photon and its wavelength related, according to the "
        "framework's two equations?",
      choices=[
        "Inversely, so a longer wavelength means a lower energy",
        "Directly, so a longer wavelength means a higher energy",
        "Inversely, so a longer wavelength means a higher energy",
        "Directly, so a longer wavelength means a lower energy",
        "They are unrelated, since the equations connect energy only to frequency"],
      ans=0,
      why="EK 3.12.A.2 makes frequency inversely proportional to wavelength through the fixed "
          "speed of light, and energy directly proportional to frequency through Planck's "
          "constant. Putting the two together leaves energy falling as wavelength rises."),

 dict(q="Absorbing which of the tabulated photons would increase an atom's energy by the "
        "most?",
      table=_T_ENERGY,
      choices=[
        "Photon Q",
        "Photon P",
        "Photon R",
        "All three would increase it equally",
        "It cannot be decided without the atom's identity"],
      ans=0,
      why="EK 3.12.A.1 makes the increase equal to the energy of the photon absorbed, so the "
          "largest tabulated photon energy produces the largest increase. Nothing about the "
          "absorbing species enters the size of the change."),

 dict(q="An atom absorbs the photon tabulated as Photon R. By how much does its energy "
        "increase?",
      table=_T_ENERGY,
      choices=[
        "By \\( 3.0 \\times 10^{-19} \\) joules",
        "By \\( 2.0 \\times 10^{-19} \\) joules",
        "By \\( 5.0 \\times 10^{-19} \\) joules",
        "By \\( 1.5 \\times 10^{-19} \\) joules",
        "By \\( 6.0 \\times 10^{-19} \\) joules"],
      ans=0,
      why="EK 3.12.A.1 makes the increase equal to that row's tabulated photon energy, with "
          "the power of ten taken from the column header. No halving or doubling enters."),

 dict(q="In the framework's equation relating wavelength and frequency, what does the symbol "
        "c stand for?",
      choices=[
        "The speed of light",
        "The concentration of the absorbing species",
        "Planck's constant",
        "The energy of the photon",
        "The number of photons emitted"],
      ans=0,
      why="EK 3.12.A.2 introduces the equation as relating the wavelength of the "
          "electromagnetic wave to its frequency and the speed of light. Planck's constant "
          "belongs to the other equation, and concentration belongs to topic 3.13's "
          "Beer-Lambert law."),

 dict(q="Which statement puts together what EK 3.12.A.1 and EK 3.12.A.2 assert?",
      choices=[
        "A photon's energy follows its frequency, its frequency and wavelength are fixed by "
        "the speed of light, and absorbing or emitting it changes the species' energy by that "
        "same amount",
        "A photon's energy follows its wavelength, and absorbing it lowers the species' "
        "energy",
        "A photon's energy is fixed by the species that absorbs it, not by its own frequency",
        "A photon's energy follows its frequency, but only part of it reaches the species",
        "A photon's energy is unrelated to its frequency and to its wavelength alike"],
      ans=0,
      why="EK 3.12.A.2 supplies both equations and EK 3.12.A.1 supplies the equality between "
          "the photon's energy and the change in the species' energy. Each rejected option "
          "breaks one of those three links."),
]
