r"""AP CHEMISTRY 3.5 Kinetic Molecular Theory.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.5.A: explain the relationship between the motion of
particles and the macroscopic properties of gases with (i) the kinetic molecular
theory, (ii) a particulate model, (iii) a graphical representation.
Suggested skill 4.A, predict and/or explain chemical properties or phenomena
using given chemical theories, models, and representations.

Essential knowledge relied on, in the framework's own words:

  3.5.A.1  The kinetic molecular theory (KMT) relates the macroscopic properties
           of gases to motions of the particles in the gas. The Maxwell-Boltzmann
           distribution describes the distribution of the kinetic energies of
           particles at a given temperature.
  3.5.A.2  All the particles in a sample of matter are in continuous, random
           motion. The average kinetic energy of a particle is related to its
           average velocity by the equation:  EQN: KE = 1/2 mv^2.
  3.5.A.3  The Kelvin temperature of a sample of matter is proportional to the
           average kinetic energy of the particles in the sample.
  3.5.A.4  The Maxwell-Boltzmann distribution provides a graphical
           representation of the energies/velocities of particles at a given
           temperature.

THE ONE DERIVATION THIS TOPIC ALLOWS, and its warrant. EK 3.5.A.3 makes the
average kinetic energy of the particles a function of the Kelvin temperature
alone, and EK 3.5.A.2 gives that average kinetic energy as half the mass times
the square of the average velocity. Put together, two gases at the same Kelvin
temperature share an average kinetic energy, so the lighter one must have the
larger average speed. Every speed comparison below rests on exactly those two
sentences and on nothing else -- no effusion law is asserted, because the CED
does not state one here.

WHAT THIS TOPIC DOES NOT OWN. 3.4 owns the ideal gas law and partial pressures;
3.6 owns every departure from ideal behaviour. verify_h3_5.py asserts neither
appears.

TWO THINGS NO KEY MAY SAY, both of them things students are routinely taught
wrongly. First, that all the particles at a given temperature share one kinetic
energy or one speed -- EK 3.5.A.1 and 3.5.A.4 make it a DISTRIBUTION, and
several distractors here say the uniform thing so a student meets it and
rejects it. Second, that anything is proportional to a temperature without
saying it is the KELVIN temperature. verify_h3_5.py asserts both, and each
assertion carries a control proving it is not running over an empty set.

NO FIGURES. EK 3.5.A.4 is a graphical representation and this bank cannot show
one, so the distribution is carried as a table of the fraction of particles in
each speed range at two temperatures, and the questions are asked of the table.

ARITHMETIC. Every number a key asserts is recomputed in verify_h3_5.py from the
stimulus alone.

NOTATION. export_units.py does not typeset Chemistry, so the spans below are
hand-written.
"""
TOPIC = ("3.5", "Kinetic Molecular Theory", 3)

# EK 3.5.A.4's distribution, carried as a table because this bank has no images.
# Both columns sum to 1.00, which verify_h3_5.py recomputes.
_T_MB = dict(
    headers=["Speed range (meters per second)",
             "Fraction of particles at 300 K",
             "Fraction of particles at 900 K"],
    rows=[["0 to 200", "0.30", "0.10"],
          ["200 to 400", "0.45", "0.25"],
          ["400 to 600", "0.18", "0.30"],
          ["600 to 800", "0.05", "0.20"],
          ["800 to 1000", "0.02", "0.15"]])

# EK 3.5.A.3's proportionality, tabulated for three samples.
_T_KE = dict(
    headers=["Sample", "Kelvin temperature (K)", "Average kinetic energy (relative units)"],
    rows=[["Sample 1", "200", "2.0"],
          ["Sample 2", "400", "4.0"],
          ["Sample 3", "600", "6.0"]])

# Three gases held at ONE Kelvin temperature, given by molar mass.
_T_MASS = dict(
    headers=["Gas", "Molar mass (grams per mole)"],
    rows=[["Gas X", "4.0"],
          ["Gas Y", "16.0"],
          ["Gas Z", "64.0"]])

QUESTIONS = [

 dict(q="What does the kinetic molecular theory relate, according to the framework?",
      choices=[
        "The macroscopic properties of gases to the motions of the particles in the gas",
        "The mass of a gas sample to the number of moles it contains",
        "The identity of a gas to the strength of its intermolecular forces",
        "The volume of a container to the mass of the container",
        "The colour of a gas to the wavelengths its particles absorb"],
      ans=0,
      why="EK 3.5.A.1 opens by saying that the kinetic molecular theory relates the "
          "macroscopic properties of gases to motions of the particles in the gas. It is a "
          "bridge between the particulate scale and the measurable scale, not a statement "
          "about composition or colour."),

 dict(q="What does the framework say the Maxwell-Boltzmann distribution describes?",
      choices=[
        "The distribution of the kinetic energies of particles at a given temperature",
        "The single kinetic energy shared by every particle at a given temperature",
        "The distribution of molar masses in a mixture of gases",
        "The way pressure is divided among the components of a mixture",
        "The change in kinetic energy of one particle over time"],
      ans=0,
      why="EK 3.5.A.1's second sentence says the Maxwell-Boltzmann distribution describes "
          "the distribution of the kinetic energies of particles at a given temperature. A "
          "distribution is a spread of values, so a single shared value is the opposite of "
          "what is asserted."),

 dict(q="What does the framework say about the motion of the particles in a sample of "
        "matter?",
      choices=[
        "They are in continuous, random motion",
        "They move only when the sample is heated",
        "They move in a fixed repeating pattern",
        "They move only in the gas phase",
        "They are motionless below room temperature"],
      ans=0,
      why="EK 3.5.A.2 opens with the claim that all the particles in a sample of matter are "
          "in continuous, random motion. Both words matter: the motion never stops and it "
          "has no set pattern."),

 dict(q="Which equation does the framework give as relating the average kinetic energy of a "
        "particle to its average velocity?",
      choices=[
        "\\( KE = \\frac{1}{2}mv^{2} \\)",
        "\\( KE = \\frac{1}{2}m^{2}v \\)",
        "\\( KE = 2mv^{2} \\)",
        "\\( KE = \\frac{1}{2}\\frac{v^{2}}{m} \\)",
        "\\( KE = mv \\)"],
      ans=0,
      why="EK 3.5.A.2 gives that equation. The mass enters to the first power and the "
          "velocity is squared, which is why a difference in speed counts for more than the "
          "same relative difference in mass."),

 dict(q="According to the framework, the Kelvin temperature of a sample is proportional to "
        "what?",
      choices=[
        "The average kinetic energy of the particles in the sample",
        "The average velocity of the particles in the sample",
        "The total mass of the sample",
        "The number of particles in the sample",
        "The volume the sample occupies"],
      ans=0,
      why="EK 3.5.A.3 states that the Kelvin temperature of a sample of matter is "
          "proportional to the average kinetic energy of the particles in the sample. The "
          "average velocity is related to that energy through the squaring in EK 3.5.A.2, so "
          "it is not itself the proportional quantity."),

 dict(q="The Kelvin temperature of a gas sample is doubled. What happens to the average "
        "kinetic energy of its particles?",
      choices=[
        "It doubles",
        "It quadruples",
        "It is halved",
        "It is unchanged",
        "It rises by two units of energy"],
      ans=0,
      why="EK 3.5.A.3 makes the average kinetic energy proportional to the Kelvin "
          "temperature, and a proportional quantity changes by the same factor as the "
          "quantity it follows."),

 dict(q="A gas sample is warmed from 200 K to 800 K. By what factor does the average kinetic "
        "energy of its particles change?",
      choices=[
        "It becomes four times as large",
        "It becomes twice as large",
        "It becomes sixteen times as large",
        "It is unchanged",
        "It becomes half as large"],
      ans=0,
      why="EK 3.5.A.3's proportionality carries the ratio of the Kelvin temperatures "
          "straight through to the average kinetic energy, and 800 K is four times 200 K."),

 dict(q="Two different gases are held at the same Kelvin temperature. How do the average "
        "kinetic energies of their particles compare?",
      choices=[
        "They are equal, since the average kinetic energy follows the Kelvin temperature "
        "alone",
        "The gas of larger molar mass has the greater average kinetic energy",
        "The gas of smaller molar mass has the greater average kinetic energy",
        "The comparison cannot be made without the two pressures",
        "The comparison cannot be made without the two volumes"],
      ans=0,
      why="EK 3.5.A.3 makes the average kinetic energy of the particles proportional to the "
          "Kelvin temperature of the sample and names no other quantity, so two samples at "
          "one temperature must agree in it whatever they are made of."),

 dict(q="Two gases of different molar mass are held at the same Kelvin temperature. Which "
        "has the greater average speed, and why?",
      choices=[
        "The lighter gas, because equal average kinetic energies with a smaller mass require "
        "a larger speed",
        "The heavier gas, because equal average kinetic energies with a larger mass require "
        "a larger speed",
        "The lighter gas, because its particles have the greater average kinetic energy",
        "The heavier gas, because its particles have the greater average kinetic energy",
        "Neither, because average speed does not depend on mass"],
      ans=0,
      why="EK 3.5.A.3 equalises the average kinetic energies at one Kelvin temperature and "
          "EK 3.5.A.2 writes that energy as half the mass times the square of the velocity. "
          "Holding the product fixed while lowering the mass forces the squared speed up."),

 dict(q="At fixed mass, the average speed of a particle becomes three times as large. What "
        "happens to its average kinetic energy?",
      choices=[
        "It becomes nine times as large",
        "It becomes three times as large",
        "It becomes six times as large",
        "It is unchanged",
        "It becomes one third as large"],
      ans=0,
      why="EK 3.5.A.2 squares the velocity in the expression for kinetic energy, so a factor "
          "applied to the speed appears squared in the energy."),

 dict(q="Two particles have the same average kinetic energy, but the second has four times "
        "the mass of the first. How does the second particle's average speed compare?",
      choices=[
        "It is half as large",
        "It is one quarter as large",
        "It is twice as large",
        "It is four times as large",
        "It is the same"],
      ans=0,
      why="EK 3.5.A.2 makes the kinetic energy proportional to the mass times the square of "
          "the velocity. Holding the energy fixed while multiplying the mass by four "
          "requires the squared velocity to fall to a quarter, and so the velocity itself to "
          "half."),

 dict(q="The table reports the average kinetic energy of three samples at three Kelvin "
        "temperatures. What relationship do the tabulated data show?",
      table=_T_KE,
      choices=[
        "The average kinetic energy is directly proportional to the Kelvin temperature",
        "The average kinetic energy is inversely proportional to the Kelvin temperature",
        "The average kinetic energy is the same at every Kelvin temperature",
        "The average kinetic energy is proportional to the square of the Kelvin temperature",
        "The average kinetic energy and the Kelvin temperature vary independently"],
      ans=0,
      why="EK 3.5.A.3 asserts that proportionality, and the tabulated rows bear it out: each "
          "sample's average kinetic energy divided by its Kelvin temperature gives the same "
          "value, which is what a direct proportionality means."),

 dict(q="The table reports the fraction of particles in each speed range for one gas at two "
        "Kelvin temperatures. Which tabulated comparison shows that raising the temperature "
        "moves particles to higher speeds?",
      table=_T_MB,
      choices=[
        "The fraction faster than 600 meters per second rises from 0.07 to 0.35",
        "The fraction faster than 600 meters per second falls from 0.35 to 0.07",
        "The fraction slower than 200 meters per second rises from 0.10 to 0.30",
        "The fraction in every range is the same in the two samples",
        "The fractions in each column fail to add to one, so no comparison is possible"],
      ans=0,
      why="EK 3.5.A.4 makes the distribution a representation of the particle energies at a "
          "given temperature, and EK 3.5.A.3 raises the average kinetic energy with the "
          "Kelvin temperature. The tabulated fractions above 600 meters per second grow "
          "several-fold from the cooler column to the hotter one, while the slowest range "
          "shrinks."),

 dict(q="Which speed range holds the largest fraction of the particles in the 300 K sample?",
      table=_T_MB,
      choices=[
        "200 to 400",
        "0 to 200",
        "400 to 600",
        "600 to 800",
        "800 to 1000"],
      ans=0,
      why="EK 3.5.A.1 makes the distribution a spread with a most-populated region rather "
          "than a single shared value, and the tabulated fractions for the cooler sample "
          "reach their maximum in one range and fall away on both sides of it."),

 dict(q="A particle of mass 2.0 kilograms moves at an average speed of 3.0 meters per "
        "second. What is its average kinetic energy?",
      choices=[
        "9.0 J",
        "3.0 J",
        "18 J",
        "6.0 J",
        "4.5 J"],
      ans=0,
      why="EK 3.5.A.2's equation takes half the mass times the square of the velocity, so "
          "the speed is squared before the halving is applied. Leaving out the factor of one "
          "half, or leaving out the squaring, gives two of the other values offered."),

 dict(q="At one temperature, do all the particles in a gas sample have the same kinetic "
        "energy?",
      choices=[
        "No, their kinetic energies are spread over a range described by the "
        "Maxwell-Boltzmann distribution",
        "Yes, every particle has the same kinetic energy, fixed by the Kelvin temperature",
        "Yes, but only for a monatomic gas",
        "No, but only because some particles have stopped moving",
        "The framework does not say either way"],
      ans=0,
      why="EK 3.5.A.1 says the Maxwell-Boltzmann distribution describes the DISTRIBUTION of "
          "the kinetic energies of particles at a given temperature, which asserts a spread "
          "of values. EK 3.5.A.3 makes the temperature proportional to the AVERAGE, which "
          "presupposes that the individual values differ."),

 dict(q="Does the framework's claim of continuous, random motion apply only to gases?",
      choices=[
        "No, it is made of all the particles in a sample of matter",
        "Yes, it is made only of gases",
        "Yes, it is restricted to the two fluid phases",
        "No, but it is restricted to samples above room temperature",
        "No, but it is restricted to samples of a single pure substance"],
      ans=0,
      why="EK 3.5.A.2 words the claim as being about all the particles in a sample of "
          "matter, without restriction to a phase, a temperature or a composition. The "
          "topic is introduced through gases, but the sentence itself is broader."),

 dict(q="What is held fixed along a single Maxwell-Boltzmann distribution?",
      choices=[
        "The temperature",
        "The kinetic energy of every particle",
        "The speed of every particle",
        "The pressure of the sample",
        "The number of collisions each particle undergoes"],
      ans=0,
      why="EK 3.5.A.1 and EK 3.5.A.4 both describe the distribution as being of the energies "
          "or velocities of particles at a GIVEN temperature, so one curve belongs to one "
          "temperature while the energies and speeds along it vary."),

 dict(q="What does the framework say the Maxwell-Boltzmann distribution provides?",
      choices=[
        "A graphical representation of the energies and velocities of particles at a given "
        "temperature",
        "A method for computing the pressure a gas exerts on its container",
        "A list of the molar masses of the gases in a mixture",
        "A record of one particle's speed as time passes",
        "A rule for deciding when a gas will condense"],
      ans=0,
      why="EK 3.5.A.4 says the Maxwell-Boltzmann distribution provides a graphical "
          "representation of the energies and velocities of particles at a given "
          "temperature. It represents a population at one instant and one temperature, not "
          "a history of one particle."),

 dict(q="The three tabulated gases are held at one Kelvin temperature. Which has the "
        "greatest average speed?",
      table=_T_MASS,
      choices=[
        "Gas X",
        "Gas Y",
        "Gas Z",
        "All three have the same average speed",
        "It cannot be decided without the three pressures"],
      ans=0,
      why="EK 3.5.A.3 gives the three samples the same average kinetic energy at one Kelvin "
          "temperature, and EK 3.5.A.2 makes that energy half the mass times the squared "
          "velocity. The lightest tabulated gas therefore needs the largest speed to reach "
          "the shared energy."),

 dict(q="Of the three tabulated samples, which has the greatest average kinetic energy per "
        "particle?",
      table=_T_KE,
      choices=[
        "Sample 3",
        "Sample 1",
        "Sample 2",
        "All three are equal",
        "It cannot be decided without the molar masses"],
      ans=0,
      why="EK 3.5.A.3 makes the average kinetic energy proportional to the Kelvin "
          "temperature, so the hottest tabulated sample carries the largest value, and the "
          "table reports that value directly as well."),

 dict(q="A gas sample is warmed from 300 K to 900 K. What happens to the average kinetic "
        "energy of its particles?",
      choices=[
        "It becomes three times as large",
        "It becomes nine times as large",
        "It becomes 600 times as large",
        "It is unchanged",
        "It becomes one third as large"],
      ans=0,
      why="EK 3.5.A.3's proportionality passes the ratio of the Kelvin temperatures directly "
          "to the average kinetic energy. Squaring the ratio would be right for an energy "
          "that followed the square of the temperature, which the framework does not "
          "assert."),

 dict(q="Two samples of the same gas have average particle kinetic energies in the ratio two "
        "to one. What is the ratio of their Kelvin temperatures?",
      choices=[
        "2 to 1",
        "1 to 2",
        "4 to 1",
        "1 to 4",
        "1 to 1"],
      ans=0,
      why="EK 3.5.A.3 makes the Kelvin temperature proportional to the average kinetic "
          "energy, so the two quantities keep the same ratio and neither is squared nor "
          "inverted along the way."),

 dict(q="A gas sample is warmed from 300 K to 600 K. What happens to the average speed of "
        "its particles?",
      choices=[
        "It rises by a factor of about 1.4",
        "It doubles",
        "It quadruples",
        "It is unchanged",
        "It rises by a factor of about 2.8"],
      ans=0,
      why="EK 3.5.A.3 doubles the average kinetic energy when the Kelvin temperature "
          "doubles, and EK 3.5.A.2 makes that energy proportional to the square of the "
          "velocity. Doubling a squared quantity multiplies the quantity itself by the "
          "square root of two."),

 dict(q="Which change would leave the average kinetic energy of a gas sample's particles "
        "unchanged?",
      choices=[
        "Compressing the sample into half its volume while holding the temperature fixed",
        "Warming the sample from 300 K to 400 K",
        "Cooling the sample from 400 K to 300 K",
        "Doubling the Kelvin temperature of the sample",
        "Halving the Kelvin temperature of the sample"],
      ans=0,
      why="EK 3.5.A.3 makes the average kinetic energy proportional to the Kelvin "
          "temperature and to nothing else, so a change that leaves the temperature alone "
          "leaves the average kinetic energy alone whatever it does to the volume."),

 dict(q="The tabulated gases are at one Kelvin temperature. What is the ratio of the average "
        "speed of Gas X to that of Gas Z?",
      table=_T_MASS,
      choices=[
        "4.0",
        "2.0",
        "16",
        "0.25",
        "1.0"],
      ans=0,
      why="EK 3.5.A.3 gives the two gases the same average kinetic energy, so by EK 3.5.A.2 "
          "the product of mass and squared speed is the same for both. The ratio of speeds "
          "is therefore the square root of the inverse ratio of the tabulated molar masses."),

 dict(q="Is the Kelvin temperature of a sample proportional to the average kinetic energy of "
        "its particles or to their average speed?",
      choices=[
        "To the average kinetic energy",
        "To the average speed",
        "To the square of the average kinetic energy",
        "To neither, since temperature is an independent quantity",
        "To both equally, since the two are the same thing"],
      ans=0,
      why="EK 3.5.A.3 names the average kinetic energy specifically. Speed enters only "
          "through EK 3.5.A.2, where it is squared and multiplied by the mass, so speed and "
          "temperature do not stand in a simple proportion."),

 dict(q="In the hotter of the two tabulated samples, which speed range holds the largest "
        "fraction of the particles?",
      table=_T_MB,
      choices=[
        "400 to 600",
        "0 to 200",
        "200 to 400",
        "600 to 800",
        "800 to 1000"],
      ans=0,
      why="EK 3.5.A.3 raises the average kinetic energy with the Kelvin temperature, so the "
          "most populated range in the hotter column sits higher than the most populated "
          "range in the cooler one. The tabulated fractions locate it directly."),

 dict(q="Which rearrangement of the framework's kinetic energy equation gives the average "
        "velocity of a particle?",
      choices=[
        "\\( v = \\sqrt{\\frac{2KE}{m}} \\)",
        "\\( v = \\sqrt{\\frac{m}{2KE}} \\)",
        "\\( v = \\frac{2KE}{m} \\)",
        "\\( v = 2mKE \\)",
        "\\( v = \\sqrt{2mKE} \\)"],
      ans=0,
      why="EK 3.5.A.2's equation multiplied by two and divided by the mass isolates the "
          "square of the velocity, and taking the square root then isolates the velocity "
          "itself."),

 dict(q="A gas sample is warmed. Which description of what happens to its particles matches "
        "the framework?",
      choices=[
        "The whole distribution of speeds shifts to higher values while a range of speeds "
        "remains",
        "Every particle speeds up to the same new speed",
        "Only the fastest particles speed up while the rest are unaffected",
        "The particles keep their speeds but collide more gently",
        "The particles stop moving randomly and begin to move together"],
      ans=0,
      why="EK 3.5.A.4 makes the distribution a representation of a whole population of "
          "energies and velocities at a given temperature, and EK 3.5.A.3 raises the average "
          "with the Kelvin temperature. Both sentences describe a population that keeps its "
          "spread while its centre moves, and EK 3.5.A.2 keeps the motion random throughout."),
]
