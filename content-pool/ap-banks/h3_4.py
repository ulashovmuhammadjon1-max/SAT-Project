r"""AP CHEMISTRY 3.4 Ideal Gas Law.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.4.A: explain the relationship between the macroscopic
properties of a sample of gas or mixture of gases using the ideal gas law.
Suggested skill 5.C, explain the relationship between variables within an
equation when one variable changes.

Essential knowledge relied on, in the framework's own words:

  3.4.A.1  The macroscopic properties of ideal gases are related through the
           ideal gas law:  EQN: PV = nRT.
  3.4.A.2  In a sample containing a mixture of ideal gases, the pressure exerted
           by each component (the partial pressure) is independent of the other
           components. Therefore, the partial pressure of a gas within the
           mixture is proportional to its mole fraction (X), and the total
           pressure of the sample is the sum of the partial pressures.
           EQN: PA = Ptotal x XA, where XA = moles A/total moles;
           EQN: Ptotal = PA + PB + PC + ...
  3.4.A.3  Graphical representations of the relationships between P, V, T, and n
           are useful to describe gas behavior.

WHAT THIS TOPIC OWNS AND WHAT IT DOES NOT. 3.5 owns the kinetic molecular theory
and the Maxwell-Boltzmann distribution; 3.6 owns every deviation from ideal
behaviour. Nothing here explains WHY the law works or where it fails, and
verify_h3_4.py asserts that.

TEMPERATURE IS ALWAYS THE KELVIN TEMPERATURE. The single most common wrong key
a topic like this can ship is a ratio taken on Celsius readings, so item 6 is
built on exactly that trap: 27 degrees Celsius to 327 degrees Celsius doubles
the Kelvin temperature and multiplies it by roughly twelve on the Celsius
scale, and the verifier recomputes both numbers so the distractor is provably
the Celsius mistake. No key anywhere asserts a proportionality to a Celsius
temperature, and the verifier asserts that too.

TWO SWAPS THAT MUST NOT SHIP. Adding an inert gas leaves the original gas's
partial pressure UNCHANGED while raising the TOTAL pressure, and pressure at
fixed volume and amount is DIRECTLY proportional to the Kelvin temperature, so
the RATIO is what stays constant. Both items keep a distractor that is the
half-swap of the key, so verify_h3_4.py requires those anchors to carry both
clauses.

NO FIGURES. EK 3.4.A.3 is about graphical representations and this bank cannot
show one, so every relationship a graph would carry is tabulated and the
question is asked of the table.

ARITHMETIC. Every number asserted by a key is recomputed in verify_h3_4.py from
the stimulus alone, with R taken as 0.08206 L atm per mole per kelvin only where
a mole count is asked for; everything else is a ratio and needs no constant.

NOTATION. export_units.py does not typeset Chemistry, so every span below is
hand-written. Formulas and unit words stay plain text.
"""
TOPIC = ("3.4", "Ideal Gas Law", 3)

# A three-component mixture, given by amount. Items 13, 14 and 15 ask different
# questions of it; the stem of each supplies the total pressure where one is
# needed.
_T_MIX = dict(
    headers=["Gas", "Moles present"],
    rows=[["Gas A", "1.0"],
          ["Gas B", "3.0"],
          ["Gas C", "4.0"]])

# EK 3.4.A.3's graphical relationships, carried as tables because this bank has
# no images. Pressure against volume at fixed amount and Kelvin temperature.
_T_PV = dict(
    headers=["Volume (L)", "Pressure (atm)"],
    rows=[["1.0", "12.0"],
          ["2.0", "6.0"],
          ["3.0", "4.0"],
          ["4.0", "3.0"]])

# Volume against Kelvin temperature at fixed amount and pressure.
_T_TV = dict(
    headers=["Kelvin temperature (K)", "Volume (L)"],
    rows=[["100", "2.0"],
          ["200", "4.0"],
          ["300", "6.0"],
          ["400", "8.0"]])

# Pressure against amount at fixed volume and Kelvin temperature.
_T_NP = dict(
    headers=["Moles of gas", "Pressure (atm)"],
    rows=[["0.10", "0.50"],
          ["0.20", "1.00"],
          ["0.30", "1.50"],
          ["0.40", "2.00"]])

QUESTIONS = [

 dict(q="Which equation does the framework give as relating the macroscopic properties of "
        "ideal gases?",
      choices=[
        "\\( PV = nRT \\)",
        "\\( P = nRTV \\)",
        "\\( PT = nRV \\)",
        "\\( PV = \\frac{nT}{R} \\)",
        "\\( P + V = nRT \\)"],
      ans=0,
      why="EK 3.4.A.1 states that the macroscopic properties of ideal gases are related "
          "through the ideal gas law and gives that equation. Pressure and volume appear as "
          "a product on one side, with amount and Kelvin temperature multiplying the gas "
          "constant on the other."),

 dict(q="A fixed amount of an ideal gas at 2.0 atm occupies 6.0 L. The volume is reduced to "
        "2.0 L at constant temperature. What is the new pressure?",
      choices=[
        "6.0 atm",
        "0.67 atm",
        "1.5 atm",
        "12 atm",
        "3.0 atm"],
      ans=0,
      why="EK 3.4.A.1's equation holds the product of pressure and volume fixed when amount "
          "and Kelvin temperature do not change, so cutting the volume to a third of its "
          "value raises the pressure to three times its value."),

 dict(q="A fixed amount of an ideal gas occupies 4.0 L at 200 K. It is warmed to 400 K at "
        "constant pressure. What volume does it occupy?",
      choices=[
        "8.0 L",
        "2.0 L",
        "4.0 L",
        "16 L",
        "0.50 L"],
      ans=0,
      why="EK 3.4.A.1's equation makes volume directly proportional to the Kelvin "
          "temperature when amount and pressure are held constant, so doubling the Kelvin "
          "temperature doubles the volume."),

 dict(q="A fixed amount of an ideal gas is sealed in a rigid vessel at 1.5 atm and 300 K. "
        "The vessel is heated to 900 K. What is the pressure?",
      choices=[
        "4.5 atm",
        "0.50 atm",
        "1.5 atm",
        "13.5 atm",
        "3.0 atm"],
      ans=0,
      why="EK 3.4.A.1's equation makes pressure directly proportional to the Kelvin "
          "temperature at fixed volume and amount. The Kelvin temperature is tripled, so "
          "the pressure is tripled as well."),

 dict(q="An ideal gas sample of 0.50 mol occupies 3.0 L. More of the same gas is added until "
        "1.5 mol is present, at constant pressure and temperature. What volume results?",
      choices=[
        "9.0 L",
        "1.0 L",
        "3.0 L",
        "4.5 L",
        "6.0 L"],
      ans=0,
      why="EK 3.4.A.1's equation makes volume directly proportional to the number of moles "
          "when pressure and Kelvin temperature are held constant, so tripling the amount "
          "triples the volume."),

 dict(q="An ideal gas in a rigid container is at 1.00 atm and 27 degrees Celsius. It is "
        "heated to 327 degrees Celsius. What is the new pressure?",
      choices=[
        "2.00 atm",
        "12.1 atm",
        "1.00 atm",
        "0.50 atm",
        "3.00 atm"],
      ans=0,
      why="EK 3.4.A.1's equation is written in the Kelvin temperature, so the ratio is 600 "
          "to 300 rather than 327 to 27. The pressure therefore doubles; taking the ratio "
          "on the Celsius readings would suggest a factor of about twelve, which is the "
          "error the other value represents."),

 dict(q="The pressure on a fixed amount of an ideal gas is doubled while its Kelvin "
        "temperature is also doubled. What happens to the volume?",
      choices=[
        "It is unchanged",
        "It doubles",
        "It is halved",
        "It quadruples",
        "It falls to one quarter"],
      ans=0,
      why="EK 3.4.A.1's equation makes volume proportional to the Kelvin temperature and "
          "inversely proportional to the pressure, so doubling both leaves the two effects "
          "exactly cancelling and the volume where it began."),

 dict(q="A 6.0 L sample of an ideal gas is at 3.0 atm and 400 K. Its pressure is lowered to "
        "1.0 atm and its temperature to 200 K, with no gas added or removed. What volume "
        "results?",
      choices=[
        "9.0 L",
        "4.0 L",
        "6.0 L",
        "3.0 L",
        "36 L"],
      ans=0,
      why="EK 3.4.A.1's equation gives the volume as proportional to the Kelvin temperature "
          "and inversely proportional to the pressure. Cutting the pressure to a third "
          "triples the volume and halving the Kelvin temperature halves it, leaving one and "
          "a half times the original."),

 dict(q="How many moles of an ideal gas occupy 44.8 L at 1.00 atm and 273 K? The gas "
        "constant is 0.0821 L atm per mole per kelvin.",
      choices=[
        "2.00 mol",
        "1.00 mol",
        "0.500 mol",
        "4.00 mol",
        "22.4 mol"],
      ans=0,
      why="EK 3.4.A.1's equation rearranged for amount divides the product of pressure and "
          "volume by the product of the gas constant and the Kelvin temperature. That "
          "denominator is about 22.4 L atm per mole, and 44.8 L atm divided by it is two "
          "moles."),

 dict(q="Which rearrangement of the ideal gas law gives the volume of a sample?",
      choices=[
        "\\( V = \\frac{nRT}{P} \\)",
        "\\( V = \\frac{P}{nRT} \\)",
        "\\( V = nRTP \\)",
        "\\( V = \\frac{PR}{nT} \\)",
        "\\( V = \\frac{nP}{RT} \\)"],
      ans=0,
      why="EK 3.4.A.1's equation divided through by the pressure isolates the volume, "
          "leaving the amount, the gas constant and the Kelvin temperature above the line "
          "and the pressure below it."),

 dict(q="A sealed flask holds three ideal gases whose partial pressures are 0.25 atm, 0.45 "
        "atm and 0.30 atm. What is the total pressure in the flask?",
      choices=[
        "1.00 atm",
        "0.45 atm",
        "0.033 atm",
        "3.00 atm",
        "0.70 atm"],
      ans=0,
      why="EK 3.4.A.2 states that the total pressure of the sample is the sum of the partial "
          "pressures, so the three values are added rather than averaged or multiplied."),

 dict(q="A mixture contains 2.0 mol of helium and 6.0 mol of neon. What is the mole fraction "
        "of helium?",
      choices=[
        "0.25",
        "0.33",
        "0.75",
        "4.0",
        "0.50"],
      ans=0,
      why="EK 3.4.A.2 defines the mole fraction of a component as its moles divided by the "
          "TOTAL moles, so the denominator is eight moles rather than the six moles of the "
          "other component."),

 dict(q="The tabulated gases are mixed in one rigid vessel, and the total pressure is 4.0 "
        "atm. What is the partial pressure of Gas B?",
      table=_T_MIX,
      choices=[
        "1.5 atm",
        "0.50 atm",
        "2.0 atm",
        "3.0 atm",
        "4.0 atm"],
      ans=0,
      why="EK 3.4.A.2 makes the partial pressure of a component the total pressure times "
          "that component's mole fraction. Three moles out of eight is three eighths of the "
          "mixture, and three eighths of the total pressure is the partial pressure."),

 dict(q="For the tabulated mixture held in a single vessel, which component exerts the "
        "greatest partial pressure?",
      table=_T_MIX,
      choices=[
        "Gas C",
        "Gas A",
        "Gas B",
        "All three exert the same partial pressure",
        "It cannot be decided without the molar masses"],
      ans=0,
      why="EK 3.4.A.2 makes each partial pressure proportional to that component's mole "
          "fraction, and the mole fraction is largest for the component present in the "
          "largest amount. Molar mass does not enter the relationship at all."),

 dict(q="What is the mole fraction of Gas A in the tabulated mixture?",
      table=_T_MIX,
      choices=[
        "0.125",
        "0.25",
        "0.375",
        "0.500",
        "8.00"],
      ans=0,
      why="EK 3.4.A.2 defines the mole fraction as the moles of that component divided by "
          "the total moles. One mole out of a total of eight gives one eighth."),

 dict(q="An inert gas is added to a rigid vessel that already holds an ideal gas, at "
        "constant temperature. What happens to the pressures in the vessel?",
      choices=[
        "The partial pressure of the original gas is unchanged and the total pressure rises",
        "The partial pressure of the original gas falls and the total pressure is unchanged",
        "The partial pressure of the original gas rises and the total pressure is unchanged",
        "Both the partial pressure of the original gas and the total pressure are unchanged",
        "Both the partial pressure of the original gas and the total pressure fall"],
      ans=0,
      why="EK 3.4.A.2 says the pressure exerted by each component is independent of the "
          "other components, so the original gas's own amount, volume and Kelvin "
          "temperature are unchanged and so is its partial pressure. The same statement "
          "makes the total the sum of the partial pressures, and a new term has been added "
          "to that sum."),

 dict(q="Which expression does the framework give for the mole fraction of a component A in "
        "a mixture?",
      choices=[
        "\\( X_A = \\frac{n_A}{n_{\\mathrm{total}}} \\)",
        "\\( X_A = \\frac{n_{\\mathrm{total}}}{n_A} \\)",
        "\\( X_A = n_A \\times n_{\\mathrm{total}} \\)",
        "\\( X_A = \\frac{P_A}{V} \\)",
        "\\( X_A = n_A - n_{\\mathrm{total}} \\)"],
      ans=0,
      why="EK 3.4.A.2 defines the mole fraction of A as moles A divided by total moles, "
          "which is a pure ratio of amounts and carries no pressure, volume or temperature "
          "term."),

 dict(q="In a gaseous mixture the partial pressure of component A is 1.2 atm while the total "
        "pressure is 6.0 atm. What is the mole fraction of A?",
      choices=[
        "0.20",
        "5.0",
        "0.80",
        "1.2",
        "0.12"],
      ans=0,
      why="EK 3.4.A.2 makes the partial pressure the total pressure times the mole fraction, "
          "so dividing the partial pressure by the total pressure recovers the mole "
          "fraction. Dividing the other way round would give a number larger than one, which "
          "no mole fraction can be."),

 dict(q="The table reports the pressure of a fixed amount of an ideal gas at several volumes "
        "at one Kelvin temperature. What do the tabulated data show?",
      table=_T_PV,
      choices=[
        "The product of pressure and volume is constant",
        "The sum of pressure and volume is constant",
        "Pressure is directly proportional to volume",
        "Pressure is proportional to the square of the volume",
        "Pressure and volume vary independently of each other"],
      ans=0,
      why="EK 3.4.A.1's equation holds the product of pressure and volume equal to the "
          "amount times the gas constant times the Kelvin temperature, all three of which "
          "are fixed here, so that product is the same in every row. EK 3.4.A.3 is the "
          "statement that such a relationship is worth representing this way."),

 dict(q="The table reports the volume of a fixed amount of an ideal gas at several Kelvin "
        "temperatures at one pressure. Which quantity is the same for every tabulated pair?",
      table=_T_TV,
      choices=[
        "The ratio of volume to Kelvin temperature",
        "The product of volume and Kelvin temperature",
        "The difference between volume and Kelvin temperature",
        "The ratio of Kelvin temperature to the square of the volume",
        "The sum of volume and Kelvin temperature"],
      ans=0,
      why="EK 3.4.A.1's equation makes volume directly proportional to the Kelvin "
          "temperature when amount and pressure are fixed, and a directly proportional pair "
          "keeps a constant ratio rather than a constant product or sum."),

 dict(q="The table reports the pressure of an ideal gas held at one volume and one Kelvin "
        "temperature for several amounts of gas. What pressure would 0.50 mol produce under "
        "the same conditions?",
      table=_T_NP,
      choices=[
        "2.50 atm",
        "2.00 atm",
        "5.00 atm",
        "0.50 atm",
        "1.25 atm"],
      ans=0,
      why="EK 3.4.A.1's equation makes pressure directly proportional to the amount of gas "
          "at fixed volume and Kelvin temperature, and the tabulated rows share one constant "
          "ratio of pressure to moles. Applying that same ratio to the new amount gives the "
          "pressure."),

 dict(q="Two rigid vessels of equal volume are held at the same temperature. One contains "
        "0.50 mol of helium and the other 0.50 mol of nitrogen. How do the pressures "
        "compare?",
      choices=[
        "The pressures are equal, since the ideal gas law contains no term for the identity "
        "of the gas",
        "The helium exerts the greater pressure, since its particles are lighter",
        "The nitrogen exerts the greater pressure, since its molar mass is larger",
        "The helium exerts the greater pressure, since it is monatomic",
        "The pressures cannot be compared without knowing the two molar masses"],
      ans=0,
      why="EK 3.4.A.1 relates pressure, volume, amount and Kelvin temperature and nothing "
          "else, so two samples agreeing in volume, amount and Kelvin temperature must agree "
          "in pressure whatever the substances are."),

 dict(q="Two sealed flasks of equal volume hold different ideal gases at the same pressure "
        "and the same temperature. What follows?",
      choices=[
        "They contain the same number of moles",
        "They contain the same mass of gas",
        "The flask holding the denser gas contains more moles",
        "The flask holding the gas of larger molar mass contains fewer moles",
        "Nothing follows without knowing the two molar masses"],
      ans=0,
      why="EK 3.4.A.1's equation fixes the amount once pressure, volume and Kelvin "
          "temperature are fixed, so equal values of those three force equal amounts. Mass "
          "would additionally require the molar masses, which the equation does not "
          "contain."),

 dict(q="Which change by itself would double the pressure of a fixed sample of an ideal gas "
        "sealed in a rigid container?",
      choices=[
        "Doubling the Kelvin temperature",
        "Doubling the Celsius temperature",
        "Halving the number of moles present",
        "Doubling the volume of the container",
        "Halving the Kelvin temperature"],
      ans=0,
      why="EK 3.4.A.1's equation makes pressure directly proportional to the Kelvin "
          "temperature at fixed volume and amount. A doubled Celsius reading is not a "
          "doubled Kelvin temperature, and a rigid container cannot change its volume at "
          "all."),

 dict(q="In the ideal gas law, how are pressure and temperature related when volume and "
        "amount of gas are held constant?",
      choices=[
        "Directly proportional, so the ratio of pressure to Kelvin temperature is constant",
        "Inversely proportional, so the ratio of pressure to Kelvin temperature is constant",
        "Directly proportional, so the product of pressure and Kelvin temperature is "
        "constant",
        "Inversely proportional, so the product of pressure and Kelvin temperature is "
        "constant",
        "Unrelated, since the equation fixes only the product of pressure and volume"],
      ans=0,
      why="EK 3.4.A.1's equation with volume and amount fixed leaves pressure equal to a "
          "constant times the Kelvin temperature, which is direct proportionality. A "
          "directly proportional pair keeps its RATIO constant; it is an inversely "
          "proportional pair that keeps a constant product."),

 dict(q="A vessel holds exactly three ideal gases at a total pressure of 3.0 atm. Two of "
        "them exert partial pressures of 1.5 atm and 0.8 atm. What is the third partial "
        "pressure?",
      choices=[
        "0.70 atm",
        "2.30 atm",
        "1.50 atm",
        "3.00 atm",
        "5.30 atm"],
      ans=0,
      why="EK 3.4.A.2 makes the total pressure the sum of the partial pressures, so the "
          "unknown partial pressure is the total less the two that are given rather than the "
          "sum of them."),

 dict(q="A rigid vessel holds 1.0 mol of gas A together with 4.0 mol of gas B, and the total "
        "pressure is 10.0 atm. What is the partial pressure of gas A?",
      choices=[
        "2.0 atm",
        "8.0 atm",
        "2.5 atm",
        "10.0 atm",
        "0.20 atm"],
      ans=0,
      why="EK 3.4.A.2 makes each partial pressure the total pressure times that component's "
          "mole fraction. One mole out of five total moles is a fifth of the mixture, so a "
          "fifth of the total pressure belongs to that component."),

 dict(q="What does the framework say about graphical representations of the relationships "
        "among pressure, volume, temperature and amount of gas?",
      choices=[
        "They are useful to describe gas behavior",
        "They replace the ideal gas law once a gas departs from ideality",
        "They are required in order to compute a molar mass",
        "They apply only at standard temperature and pressure",
        "They are placed outside the exam by an exclusion statement"],
      ans=0,
      why="EK 3.4.A.3 says exactly that graphical representations of the relationships "
          "between those four quantities are useful to describe gas behavior. It is a "
          "statement of what the representations are good for, not a restriction on when "
          "they may be used."),

 dict(q="What does the framework say about the pressure exerted by each component of a "
        "mixture of ideal gases?",
      choices=[
        "It is independent of the other components",
        "It depends on the molar masses of the other components",
        "It is the same for every component whatever the amounts present",
        "It is the total pressure divided by the number of different gases present",
        "It is negligible unless that component is the most abundant one"],
      ans=0,
      why="EK 3.4.A.2 opens by saying that in a mixture of ideal gases the pressure exerted "
          "by each component, its partial pressure, is independent of the other components. "
          "Dividing the total evenly among the components would only be right if the amounts "
          "happened to be equal."),

 dict(q="According to the framework, what is the partial pressure of a gas within a mixture "
        "proportional to?",
      choices=[
        "The mole fraction of that gas",
        "The molar mass of that gas",
        "The reciprocal of that gas's mole fraction",
        "The number of different gases present in the mixture",
        "The volume occupied by the mixture"],
      ans=0,
      why="EK 3.4.A.2 states that the partial pressure of a gas within the mixture is "
          "proportional to its mole fraction, and gives the mole fraction as that gas's "
          "moles over the total moles. Nothing in the statement refers to molar mass."),
]
