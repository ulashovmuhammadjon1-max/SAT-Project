r"""AP CHEMISTRY 3.13 Beer-Lambert Law.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.13.A: explain the amount of light absorbed by a solution of
molecules or ions in relationship to the concentration, path length, and molar
absorptivity. Suggested skill 2.E, identify or describe potential sources of
experimental error.

Essential knowledge relied on, in the framework's own words:

  3.13.A.1  The Beer-Lambert law relates the absorption of light by a solution
            to three variables according to the equation:  EQN: A = epsilon b c.
            The molar absorptivity, epsilon, describes how intensely a chemical
            species absorbs light of a specific wavelength. The path length, b,
            and concentration, c, are proportional to the number of
            light-absorbing particles in the light path.
  3.13.A.2  In most experiments the path length and wavelength of light are held
            constant. In such cases, the absorbance is proportional only to the
            concentration of absorbing molecules or ions. The spectrophotometer
            is typically set to the wavelength of maximum absorbance (optimum
            wavelength) for the species being analyzed to ensure the maximum
            sensitivity of measurement.

THE CONDITION IS PART OF THE CLAIM. EK 3.13.A.2 does not say the absorbance is
proportional to the concentration; it says the path length and the wavelength are
usually held constant and that IN SUCH CASES the absorbance is proportional only
to the concentration. Every item below that asserts the proportionality states
the condition with it, and verify_h3_13.py checks that it does -- a key that
drops the condition is a claim the framework does not make, and it is the claim
that makes the two error items (29 and 30) come out wrong.

EVERY PRODUCT IS RECOMPUTED. The three variables multiply, so a wrong answer here
is almost always the right numbers combined the wrong way: the path length left
out, divided by instead of multiplied by, counted twice, or a power of ten
dropped from the concentration. Every distractor that carries a number is one of
those routes computed on purpose, and verify_h3_13.py recomputes each of them
from the stimulus and requires it to sit in exactly one distractor. Nothing here
is a filler number.

NO FIGURES. A calibration curve is the natural stimulus for this topic and the
bank cannot show one, so the standards are carried as a TABLE of concentration
against absorbance and the questions are asked of the table.

NOTATION. export_units.py does not typeset Chemistry, so every span below is
hand-written. The equation, scientific notation and the units of the molar
absorptivity sit inside spans; absorbance is a pure number and carries no unit.
"""
TOPIC = ("3.13", "Beer-Lambert Law", 3)

_EPS_UNIT = "\\( \\mathrm{M^{-1}\\,cm^{-1}} \\)"

# Three standards of one species, measured in one cuvette at one wavelength.
# The absorbance rises in step with the concentration, which is EK 3.13.A.2's
# proportionality; nothing here needs a curve to be drawn.
_T_CAL = dict(
    headers=["Standard", "Concentration (in units of \\( 10^{-4} \\) M)", "Absorbance"],
    rows=[["Standard 1", "1.0", "0.15"],
          ["Standard 2", "2.0", "0.30"],
          ["Standard 3", "4.0", "0.60"]])

_T_EPS = dict(
    headers=["Species", "Molar absorptivity (in " + _EPS_UNIT + " )"],
    rows=[["Species X", "800"],
          ["Species Y", "2500"],
          ["Species Z", "1200"]])

_T_WL = dict(
    headers=["Wavelength (nm)", "Absorbance of the sample"],
    rows=[["440", "0.12"],
          ["510", "0.62"],
          ["590", "0.28"]])

_T_SOLN = dict(
    headers=["Solution", "Molar absorptivity (in " + _EPS_UNIT + " )",
             "Path length (cm)", "Concentration (in units of \\( 10^{-4} \\) M)"],
    rows=[["Solution D", "2500", "0.50", "4.0"],
          ["Solution E", "1000", "2.00", "2.0"],
          ["Solution F", "2000", "1.00", "3.0"]])

QUESTIONS = [

 dict(q="The Beer-Lambert law relates the absorption of light by a solution to three "
        "variables. Which three does the framework name?",
      choices=[
        "The molar absorptivity, the path length, and the concentration",
        "The molar absorptivity, the temperature, and the concentration",
        "The path length, the concentration, and the volume of the solution",
        "The wavelength, the temperature, and the path length",
        "The molar mass, the path length, and the concentration"],
      ans=0,
      why="EK 3.13.A.1 states that the Beer-Lambert law relates the absorption of light by a "
          "solution to three variables, and its equation names them as the molar "
          "absorptivity, the path length and the concentration. Temperature and volume are "
          "not among them."),

 dict(q="Which equation does the framework give for the Beer-Lambert law?",
      choices=[
        "\\( A = \\varepsilon b c \\)",
        "\\( A = \\frac{\\varepsilon b}{c} \\)",
        "\\( A = \\frac{\\varepsilon c}{b} \\)",
        "\\( A = \\frac{b c}{\\varepsilon} \\)",
        "\\( \\varepsilon = A b c \\)"],
      ans=0,
      why="EK 3.13.A.1 gives that equation, with the absorbance equal to the product of the "
          "three variables. Because it is a product, raising any one of the three raises the "
          "absorbance in the same proportion."),

 dict(q="What does the framework say the molar absorptivity describes?",
      choices=[
        "How intensely a chemical species absorbs light of a specific wavelength",
        "How many particles of the species lie in the light path",
        "How far the light travels through the solution",
        "How concentrated the solution is",
        "How quickly the species reacts once it has absorbed light"],
      ans=0,
      why="EK 3.13.A.1 says the molar absorptivity describes how intensely a chemical species "
          "absorbs light of a specific wavelength. It is a property of the species at that "
          "wavelength, not a property of the sample being measured."),

 dict(q="According to the framework, the path length and the concentration are proportional "
        "to what?",
      choices=[
        "The number of light-absorbing particles in the light path",
        "The molar absorptivity of the species",
        "The wavelength at which the measurement is made",
        "The temperature of the solution being measured",
        "The volume of the cuvette that holds no solution"],
      ans=0,
      why="EK 3.13.A.1 states that the path length and concentration are proportional to the "
          "number of light-absorbing particles in the light path, which is why raising either "
          "one raises the absorbance."),

 dict(q="In most experiments, which two quantities does the framework say are held constant?",
      choices=[
        "The path length and the wavelength of light",
        "The concentration and the molar absorptivity",
        "The absorbance and the concentration",
        "The path length and the concentration",
        "The wavelength of light and the concentration"],
      ans=0,
      why="EK 3.13.A.2 opens by saying that in most experiments the path length and "
          "wavelength of light are held constant. The concentration is the quantity the "
          "experiment is usually there to find, so it is the one allowed to vary."),

 dict(q="When the path length and the wavelength are held constant, the absorbance is "
        "proportional only to which quantity?",
      choices=[
        "The concentration of the absorbing molecules or ions",
        "The path length of the cuvette",
        "The molar absorptivity of the species",
        "The wavelength at which the measurement is made",
        "The total volume of solution in the cuvette"],
      ans=0,
      why="EK 3.13.A.2 states that in such cases the absorbance is proportional only to the "
          "concentration of absorbing molecules or ions. The other two variables are still in "
          "the equation; they have simply been fixed."),

 dict(q="To which wavelength does the framework say a spectrophotometer is typically set?",
      choices=[
        "The wavelength of maximum absorbance for the species being analyzed",
        "The wavelength of minimum absorbance for the species being analyzed",
        "The wavelength at which the solvent absorbs most strongly",
        "The longest wavelength the instrument is able to produce",
        "A wavelength chosen at random from the visible range"],
      ans=0,
      why="EK 3.13.A.2 says the spectrophotometer is typically set to the wavelength of "
          "maximum absorbance for the species being analyzed. The setting is chosen for the "
          "species under study, not for the solvent or for the instrument."),

 dict(q="Why does the framework say the spectrophotometer is set to the wavelength of maximum "
        "absorbance?",
      choices=[
        "To ensure the maximum sensitivity of the measurement",
        "To ensure the path length stays constant during the measurement",
        "To make the absorbance independent of the concentration",
        "To make the molar absorptivity the same at every wavelength",
        "To remove the need to know the path length"],
      ans=0,
      why="EK 3.13.A.2 gives the reason in those words: to ensure the maximum sensitivity of "
          "measurement. A given change in concentration produces the largest change in "
          "absorbance where the species absorbs most strongly."),

 dict(q="What name does the framework give to the wavelength of maximum absorbance?",
      choices=[
        "The optimum wavelength",
        "The critical wavelength",
        "The reference wavelength",
        "The limiting wavelength",
        "The standard wavelength"],
      ans=0,
      why="EK 3.13.A.2 puts the term in parentheses immediately after the wavelength of "
          "maximum absorbance, so the two phrases name the same setting."),

 dict(q="In the framework's equation for the Beer-Lambert law, which quantity does the symbol "
        "b stand for?",
      choices=[
        "The path length",
        "The molar absorptivity",
        "The concentration",
        "The absorbance",
        "The number of absorbing particles"],
      ans=0,
      why="EK 3.13.A.1 names the three variables as it introduces them, calling b the path "
          "length. It is the distance the light travels through the solution, which is why a "
          "longer cuvette raises the absorbance."),

 dict(q="Written as the framework writes it, the Beer-Lambert law puts the symbol A alone on "
        "one side. Which quantity is that?",
      choices=[
        "The absorption of light by the solution",
        "The molar absorptivity of the species",
        "The path length through the solution",
        "The concentration of the solution",
        "The wavelength of the light used"],
      ans=0,
      why="EK 3.13.A.1 introduces the equation as relating the absorption of light by a "
          "solution to the three variables on the right, so the quantity standing alone on "
          "the left is that absorption."),

 dict(q="The concentration of an absorbing species is doubled while the path length and the "
        "wavelength are unchanged. What happens to the absorbance?",
      choices=[
        "It doubles",
        "It is halved",
        "It quadruples",
        "It is unchanged",
        "It falls to one quarter"],
      ans=0,
      why="EK 3.13.A.1 makes the absorbance the product of the three variables, and "
          "EK 3.13.A.2 makes it proportional to the concentration alone once the other two "
          "are held constant, so a factor applied to the concentration passes straight into "
          "the absorbance."),

 dict(q="A solution is moved from a 1.00 cm cuvette to a 3.00 cm cuvette, with the wavelength "
        "and the concentration unchanged. What happens to the absorbance?",
      choices=[
        "It triples",
        "It falls to one third",
        "It is unchanged",
        "It doubles",
        "It is nine times as large"],
      ans=0,
      why="EK 3.13.A.1's equation multiplies the path length into the absorbance, and "
          "EK 3.13.A.1 also says the path length is proportional to the number of "
          "light-absorbing particles in the light path, so tripling it triples the "
          "absorbance."),

 dict(q="A solution is diluted until its concentration is one fifth of its original value, "
        "then measured in the same cuvette at the same wavelength. What happens to the "
        "absorbance?",
      choices=[
        "It falls to one fifth of its original value",
        "It is five times its original value",
        "It is unchanged",
        "It falls to one tenth of its original value",
        "It is halved"],
      ans=0,
      why="EK 3.13.A.2 makes the absorbance proportional only to the concentration once the "
          "path length and wavelength are held constant, which is exactly the condition this "
          "dilution is measured under, so the two fall together."),

 dict(q="Two species are measured at the same concentration, in the same cuvette, each at the "
        "wavelength for which its own molar absorptivity is quoted. Species M has twice the "
        "molar absorptivity of species N. How do the absorbances compare?",
      choices=[
        "Species M shows twice the absorbance of species N",
        "Species N shows twice the absorbance of species M",
        "Species M shows half the absorbance of species N",
        "The two show the same absorbance",
        "No comparison is possible, since the molar absorptivity does not affect absorbance"],
      ans=0,
      why="EK 3.13.A.1 makes the molar absorptivity one of the three factors in the product, "
          "and it is the factor describing how intensely the species absorbs, so with the "
          "other two factors equal it sets the ratio of the absorbances."),

 dict(q="In an experiment in which the path length and the wavelength are held constant, how "
        "does the absorbance vary with the concentration?",
      choices=[
        "It is directly proportional to the concentration",
        "It is inversely proportional to the concentration",
        "It does not depend on the concentration",
        "It is proportional to the square of the concentration",
        "It is proportional to the square root of the concentration"],
      ans=0,
      why="EK 3.13.A.2 states that when the path length and wavelength are held constant the "
          "absorbance is proportional only to the concentration of absorbing molecules or "
          "ions, which is a direct proportionality and not a power of any other order."),

 dict(q="A measurement is repeated with a cuvette of half the path length, with everything "
        "else unchanged. What happens to the absorbance?",
      choices=[
        "It is halved",
        "It doubles",
        "It is unchanged",
        "It falls to one quarter",
        "It quadruples"],
      ans=0,
      why="EK 3.13.A.1's equation multiplies the path length into the absorbance, so halving "
          "the distance the light travels through the solution halves the absorbance the "
          "instrument reports."),

 dict(q="A species with a molar absorptivity of 1500 " + _EPS_UNIT + " is measured in a "
        "2.00 cm cuvette at a concentration of \\( 2.0 \\times 10^{-4} \\) M. What is the "
        "absorbance?",
      choices=[
        "0.60",
        "0.30",
        "0.15",
        "1.20",
        "6.0"],
      ans=0,
      why="EK 3.13.A.1's equation multiplies the three quantities together. Leaving the path "
          "length out, dividing by it instead of multiplying, counting it twice, or losing a "
          "power of ten from the concentration each give one of the other values offered."),

 dict(q="A solution of a species measured in a 2.00 cm cuvette at a concentration of "
        "\\( 8.0 \\times 10^{-5} \\) M gives an absorbance of 0.48. What is the molar "
        "absorptivity of the species at that wavelength?",
      choices=[
        "3000 " + _EPS_UNIT,
        "6000 " + _EPS_UNIT,
        "1500 " + _EPS_UNIT,
        "300 " + _EPS_UNIT,
        "30000 " + _EPS_UNIT],
      ans=0,
      why="EK 3.13.A.1's equation rearranged divides the absorbance by the product of the "
          "path length and the concentration. Leaving the path length out, counting it twice, "
          "or misplacing the power of ten in the concentration each give one of the other "
          "values offered."),

 dict(q="A species whose molar absorptivity is 1500 " + _EPS_UNIT + " gives an absorbance of "
        "0.90 in a 2.00 cm cuvette. What is its concentration?",
      choices=[
        "\\( 3.0 \\times 10^{-4} \\) M",
        "\\( 6.0 \\times 10^{-4} \\) M",
        "\\( 1.5 \\times 10^{-4} \\) M",
        "\\( 3.0 \\times 10^{-3} \\) M",
        "\\( 2.7 \\times 10^{3} \\) M"],
      ans=0,
      why="EK 3.13.A.1's equation rearranged divides the absorbance by the product of the "
          "molar absorptivity and the path length. Leaving the path length out, counting it "
          "twice, slipping a power of ten, or multiplying the three quantities instead of "
          "dividing each give one of the other values offered."),

 dict(q="A species whose molar absorptivity is 1000 " + _EPS_UNIT + " is measured at a "
        "concentration of \\( 4.0 \\times 10^{-4} \\) M and gives an absorbance of 0.80. What "
        "was the path length of the cuvette?",
      choices=[
        "2.00 cm",
        "0.50 cm",
        "0.32 cm",
        "20.0 cm",
        "0.20 cm"],
      ans=0,
      why="EK 3.13.A.1's equation rearranged divides the absorbance by the product of the "
          "molar absorptivity and the concentration. Inverting that quotient, multiplying all "
          "three quantities together, or misplacing the power of ten in the concentration "
          "each give one of the other values offered."),

 dict(q="A solution gives an absorbance of 0.24. A second solution of the same species, at "
        "three times the concentration, is measured in the same cuvette at the same "
        "wavelength. What is its absorbance?",
      choices=[
        "0.72",
        "0.08",
        "0.24",
        "2.16",
        "It cannot be found without the molar absorptivity of the species"],
      ans=0,
      why="EK 3.13.A.2 makes the absorbance proportional only to the concentration once the "
          "path length and wavelength are held constant, so the ratio of the two absorbances "
          "is the ratio of the concentrations and neither the molar absorptivity nor the path "
          "length needs to be known."),

 dict(q="Two solutions of one species are measured in the same cuvette at the same "
        "wavelength. Solution P has a concentration of \\( 2.0 \\times 10^{-4} \\) M and an "
        "absorbance of 0.36; solution Q has an absorbance of 0.90. What is the concentration "
        "of solution Q?",
      choices=[
        "\\( 5.0 \\times 10^{-4} \\) M",
        "\\( 8.0 \\times 10^{-5} \\) M",
        "\\( 2.5 \\times 10^{-4} \\) M",
        "\\( 1.8 \\times 10^{-4} \\) M",
        "\\( 5.0 \\times 10^{-5} \\) M"],
      ans=0,
      why="EK 3.13.A.2 makes the absorbance proportional only to the concentration under "
          "these conditions, so the concentrations stand in the same ratio as the "
          "absorbances. Inverting that ratio, or slipping a power of ten, gives two of the "
          "other values offered."),

 dict(q="The tabulated standards contain one species and were all measured in the same "
        "cuvette at the same wavelength. What absorbance would a solution of concentration "
        "\\( 3.0 \\times 10^{-4} \\) M give?",
      table=_T_CAL,
      choices=[
        "0.45",
        "0.30",
        "0.60",
        "0.90",
        "0.05"],
      ans=0,
      why="EK 3.13.A.2 makes the absorbance proportional only to the concentration when the "
          "path length and wavelength are held constant, which the tabulated standards were, "
          "so the ratio the table fixes carries over to the new concentration."),

 dict(q="A sample of the same species is measured under the conditions the tabulated "
        "standards were measured under and gives an absorbance of 0.75. What is its "
        "concentration?",
      table=_T_CAL,
      choices=[
        "\\( 5.0 \\times 10^{-4} \\) M",
        "\\( 2.5 \\times 10^{-4} \\) M",
        "\\( 1.0 \\times 10^{-3} \\) M",
        "\\( 5.0 \\times 10^{-3} \\) M",
        "\\( 5.0 \\times 10^{-5} \\) M"],
      ans=0,
      why="EK 3.13.A.2's proportionality runs both ways under the stated conditions, so the "
          "ratio the tabulated standards fix turns a measured absorbance back into a "
          "concentration. Halving, doubling or misplacing a power of ten gives the other "
          "values offered."),

 dict(q="Three solutions, each of concentration \\( 2.0 \\times 10^{-4} \\) M, are measured "
        "in the same 1.00 cm cuvette, each at the wavelength for which its tabulated molar "
        "absorptivity applies. Which shows the greatest absorbance?",
      table=_T_EPS,
      choices=[
        "Species Y",
        "Species X",
        "Species Z",
        "All three show the same absorbance",
        "It cannot be decided without the wavelengths themselves"],
      ans=0,
      why="EK 3.13.A.1 makes the absorbance the product of the three variables, and with the "
          "path length and concentration equal across the three the molar absorptivity alone "
          "decides which absorbs most intensely at its own wavelength."),

 dict(q="A student must choose one wavelength at which to measure a series of solutions of "
        "the species whose absorbances are tabulated. Which should be chosen?",
      table=_T_WL,
      choices=[
        "510 nm",
        "440 nm",
        "590 nm",
        "Any of the three, since the Beer-Lambert law holds at every wavelength",
        "The one furthest from the maximum, so that the absorbances stay small"],
      ans=0,
      why="EK 3.13.A.2 says the spectrophotometer is typically set to the wavelength of "
          "maximum absorbance for the species being analyzed to ensure the maximum "
          "sensitivity of measurement, and the table says which of the three that is."),

 dict(q="Each tabulated solution is measured at the wavelength for which its molar "
        "absorptivity applies. Which gives the greatest absorbance?",
      table=_T_SOLN,
      choices=[
        "Solution F",
        "Solution D",
        "Solution E",
        "All three give the same absorbance",
        "It cannot be decided without the wavelengths themselves"],
      ans=0,
      why="EK 3.13.A.1's equation multiplies all three tabulated quantities together, so no "
          "one column decides the answer on its own. The solution that wins holds neither "
          "the largest molar absorptivity, nor the longest path length, nor the highest "
          "concentration; only the product picks it out."),

 dict(q="A student measures a set of standards in a 1.00 cm cuvette, then measures the "
        "unknown in a 2.00 cm cuvette at the same wavelength and reads its concentration off "
        "the standards. What is the effect on the concentration reported?",
      choices=[
        "It comes out twice the true value, because the longer path length raises the "
        "absorbance while the concentration is unchanged",
        "It comes out half the true value, because the longer path length lowers the "
        "absorbance",
        "It is unaffected, because the path length does not appear in the Beer-Lambert law",
        "It is unaffected, because the absorbance depends only on the concentration under all "
        "conditions",
        "It comes out twice the true value, because the molar absorptivity doubles with the "
        "path length"],
      ans=0,
      why="EK 3.13.A.2 makes the absorbance proportional only to the concentration when the "
          "path length is held constant, and here it was not: doubling the path length "
          "doubles the absorbance under EK 3.13.A.1's equation, and the standards then "
          "translate that raised absorbance into a raised concentration."),

 dict(q="A student measures one solution at two different wavelengths, gets two different "
        "absorbances, and concludes that the concentration changed between the measurements. "
        "What is wrong with that conclusion?",
      choices=[
        "The molar absorptivity applies to light of a specific wavelength, so the two "
        "absorbances are expected to differ at one concentration",
        "The absorbance does not depend on the concentration at all",
        "The path length must have changed as well, which explains the difference",
        "An absorbance cannot be measured at more than one wavelength",
        "The two absorbances must in fact be equal, so one of them was misread"],
      ans=0,
      why="EK 3.13.A.1 says the molar absorptivity describes how intensely a species absorbs "
          "light of a specific wavelength, so changing the wavelength changes that factor in "
          "the product. EK 3.13.A.2's proportionality to concentration alone is stated for "
          "measurements at a constant wavelength, which these were not."),
]
