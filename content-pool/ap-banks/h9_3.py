# AP CHEMISTRY 9.3 Gibbs Free Energy and Thermodynamic Favorability
# CED effective Fall 2024, Unit 9 Thermodynamics and Electrochemistry.
# Learning objective 9.3.A: explain whether a physical or chemical process is
# thermodynamically favored based on an evaluation of the standard Gibbs free energy
# change.
# Suggested skill 6.E, provide reasoning to justify a claim using connections between
# particulate and macroscopic scales or levels.
#
# Essential knowledge relied on, in the framework's own words:
#   9.3.A.1  The Gibbs free energy change for a chemical process in which all the
#            reactants and products are present in a standard state (as pure substances,
#            as solutions of 1.0 M concentration, or as gases at a pressure of 1.0 atm
#            (or 1.0 bar)) is given the symbol of the STANDARD free energy change.
#   9.3.A.2  The standard Gibbs free energy change for a chemical or physical process is
#            a measure of thermodynamic favorability. Historically, the term
#            "spontaneous" has been used to describe processes for which the standard
#            free energy change is less than zero. The phrase "thermodynamically
#            favored" is preferred instead so that common misunderstandings (equating
#            "spontaneous" with "suddenly" or "without cause") can be avoided. When the
#            standard free energy change is less than zero for the process, it is said
#            to be thermodynamically favored.
#   9.3.A.3  The standard Gibbs free energy change for a physical or chemical process
#            may also be determined from the standard Gibbs free energy of formation of
#            the reactants and products.
#            EQN: (free energy change of reaction) = (sum over products of the standard
#            free energy of formation) - (the same sum over the reactants)
#   9.3.A.4  In some cases, it is necessary to consider both enthalpy and entropy to
#            determine if a process will be thermodynamically favored. The freezing of
#            water and the dissolution of sodium nitrate are examples of such phenomena.
#   9.3.A.5  Knowing the values of the standard enthalpy and entropy changes for a
#            process at a given temperature allows the standard free energy change to be
#            calculated directly.
#            EQN: (free energy change) = (enthalpy change) - T (entropy change)
#   9.3.A.6  In general, the temperature conditions for a process to be thermodynamically
#            favored (free energy change below zero) can be predicted from the signs of
#            the enthalpy and entropy changes as shown in the framework's table:
#                enthalpy < 0, entropy > 0   favored at ALL temperatures
#                enthalpy > 0, entropy < 0   favored at NO temperature
#                enthalpy > 0, entropy > 0   favored at HIGH temperature
#                enthalpy < 0, entropy < 0   favored at LOW temperature
#            In cases where the enthalpy change is below zero and the entropy change
#            above it, NO calculation of the free energy change is necessary to
#            determine that the process is thermodynamically favored; in the mirrored
#            case no calculation is necessary to determine that it is unfavored.
#
# THE SIGN CONVENTION IS THE WHOLE TOPIC. A thermodynamically favored process has a
# NEGATIVE standard free energy change, and writing that backwards is the defect this
# module is most likely to ship. So every numeric choice states its sign explicitly AND
# says whether the process is favored, and verify_h9_3.py carries a swap guard that
# asserts the two agree on every such key -- a key that named the right number with the
# wrong verdict would otherwise pass every structural check there is.
#
# SCOPE. 9.4 owns kinetic control, 9.5 owns the equilibrium constant, and 9.8 to 9.11
# own the electrochemistry. verify_h9_3.py asserts that none of them appears here.
#
# ARITHMETIC. Every value is recomputed in verify_h9_3.py from the numbers in the stem
# or the table alone, including the J-to-kJ conversion that one item is built around.
#
# NO FIGURES. Every stimulus is a table or is stated in the stem.
TOPIC = ("9.3", "Gibbs Free Energy and Thermodynamic Favorability", 9)

_GFCOL = "Standard free energy of formation, kJ/mol"

_T_GF = dict(
    headers=["Species", _GFCOL],
    rows=[["N2(g)", "0"],
          ["H2(g)", "0"],
          ["O2(g)", "0"],
          ["NH3(g)", "-16.4"],
          ["CH4(g)", "-50.5"],
          ["CO(g)", "-137.2"],
          ["CO2(g)", "-394.4"],
          ["H2O(l)", "-237.1"],
          ["H2O(g)", "-228.6"],
          ["NO(g)", "86.6"],
          ["NO2(g)", "51.3"],
          ["CaCO3(s)", "-1128.8"],
          ["CaO(s)", "-604.0"]])

_T_QUAD = dict(
    headers=["Process", "Sign of the enthalpy change", "Sign of the entropy change"],
    rows=[["P", "negative", "positive"],
          ["Q", "positive", "negative"],
          ["R", "positive", "positive"],
          ["S", "negative", "negative"]])

QUESTIONS = [

 dict(q="Why does the course framework prefer the phrase thermodynamically favored to the "
        "older word spontaneous?",
      choices=[
        "Because spontaneous invites the misunderstandings that a process happens "
        "suddenly or without cause",
        "Because spontaneous applies only to physical processes and not to chemical ones",
        "Because spontaneous cannot be used of a process carried out under standard "
        "conditions",
        "Because the two phrases describe opposite conditions on the free energy change",
        "Because spontaneous was reserved for processes with a positive free energy "
        "change"],
      ans=0,
      why="EK 9.3.A.2 says the phrase thermodynamically favored is preferred so that "
          "common misunderstandings, equating spontaneous with suddenly or without "
          "cause, can be avoided. The two phrases pick out the same condition, a "
          "standard free energy change below zero, so they are not opposites."),

 dict(q="What conditions does the framework specify for the standard state used in "
        "defining the standard Gibbs free energy change?",
      choices=[
        "Pure substances, solutions at 1.0 M, and gases at a pressure of 1.0 atm or 1.0 "
        "bar",
        "Pure substances only, at any convenient temperature and pressure",
        "Solutions at 0.1 M and gases at a pressure of 1.0 atm",
        "Any mixture of reactants and products at 298 K",
        "Gases at 1.0 atm, with solids and liquids excluded from consideration"],
      ans=0,
      why="EK 9.3.A.1 defines the standard free energy change as the one for a process "
          "in which all the reactants and products are present in a standard state, "
          "named there as pure substances, as solutions of 1.0 M concentration, or as "
          "gases at a pressure of 1.0 atm or 1.0 bar."),

 dict(q="A process has \\( \\Delta H^\\circ = -100.0 \\) kJ/mol and \\( \\Delta S^\\circ "
        "= -200.0 \\) J/(mol K). What is its standard free energy change at 300 K?",
      choices=[
        "\\( -40.0 \\) kJ/mol, thermodynamically favored",
        "\\( +40.0 \\) kJ/mol, thermodynamically unfavored",
        "\\( -160.0 \\) kJ/mol, thermodynamically favored",
        "\\( -100.0 \\) kJ/mol, thermodynamically favored",
        "\\( +60.0 \\) kJ/mol, thermodynamically unfavored"],
      ans=0,
      why="EK 9.3.A.5's equation subtracts the temperature times the entropy change from "
          "the enthalpy change, and the entropy change must first be converted from "
          "joules to kilojoules. Subtracting a negative quantity raises the result, so "
          "adding instead of subtracting gives the value that is more negative. EK "
          "9.3.A.2 makes a result below zero thermodynamically favored."),

 dict(q="A process has \\( \\Delta H^\\circ = +50.0 \\) kJ/mol and \\( \\Delta S^\\circ = "
        "+100.0 \\) J/(mol K). What is its standard free energy change at 300 K?",
      choices=[
        "\\( +20.0 \\) kJ/mol, thermodynamically unfavored",
        "\\( -20.0 \\) kJ/mol, thermodynamically favored",
        "\\( +80.0 \\) kJ/mol, thermodynamically unfavored",
        "\\( -30.0 \\) kJ/mol, thermodynamically favored",
        "\\( +50.0 \\) kJ/mol, thermodynamically unfavored"],
      ans=0,
      why="EK 9.3.A.5's equation gives a positive result here because the temperature is "
          "too low for the entropy term to overcome the enthalpy term, and EK 9.3.A.2 "
          "makes a result above zero thermodynamically unfavored. This is the pair of "
          "signs EK 9.3.A.6 places in the favored-at-high-temperature case."),

 dict(q="The same process is now carried out at 600 K instead. Given \\( \\Delta H^\\circ "
        "= +50.0 \\) kJ/mol and \\( \\Delta S^\\circ = +100.0 \\) J/(mol K), what is its "
        "standard free energy change?",
      choices=[
        "\\( -10.0 \\) kJ/mol, thermodynamically favored",
        "\\( +10.0 \\) kJ/mol, thermodynamically unfavored",
        "\\( +20.0 \\) kJ/mol, thermodynamically unfavored",
        "\\( -60.0 \\) kJ/mol, thermodynamically favored",
        "\\( +110.0 \\) kJ/mol, thermodynamically unfavored"],
      ans=0,
      why="EK 9.3.A.5's equation multiplies the entropy change by the temperature, so "
          "doubling the temperature doubles the size of that term and turns the result "
          "negative. This is what EK 9.3.A.6 means by a process with both changes "
          "positive being favored at high temperature."),

 dict(q="Above what temperature does a process with \\( \\Delta H^\\circ = +50.0 \\) "
        "kJ/mol and \\( \\Delta S^\\circ = +100.0 \\) J/(mol K) become thermodynamically "
        "favored?",
      choices=["Above 500 K", "Above 50 K", "Above 5000 K", "Above 200 K",
               "It is favored at every temperature"],
      ans=0,
      why="EK 9.3.A.5's expression changes sign where the enthalpy change equals the "
          "temperature times the entropy change, so the crossover temperature is the "
          "enthalpy change divided by the entropy change once the units agree. Dividing "
          "without converting joules to kilojoules moves the answer by a factor of a "
          "thousand."),

 dict(q="A process has a negative enthalpy change and a positive entropy change. At which "
        "temperatures is it thermodynamically favored?",
      choices=["At all temperatures", "At no temperature", "Only at high temperatures",
               "Only at low temperatures", "Only at 298 K"],
      ans=0,
      why="EK 9.3.A.6's table places this pair of signs in the row favored at all "
          "temperatures, because both terms of EK 9.3.A.5's expression then push the "
          "free energy change below zero whatever the temperature is."),

 dict(q="A process has a positive enthalpy change and a negative entropy change. At which "
        "temperatures is it thermodynamically favored?",
      choices=["At no temperature", "At all temperatures", "Only at high temperatures",
               "Only at low temperatures", "Only above 298 K"],
      ans=0,
      why="EK 9.3.A.6's table places this pair of signs in the row favored at no "
          "temperature, because both terms of EK 9.3.A.5's expression then hold the free "
          "energy change above zero however the temperature is chosen."),

 dict(q="A process has a positive enthalpy change and a positive entropy change. At which "
        "temperatures is it thermodynamically favored?",
      choices=["Only at high temperatures", "Only at low temperatures",
               "At all temperatures", "At no temperature", "Only at exactly 298 K"],
      ans=0,
      why="EK 9.3.A.6's table places this pair of signs in the high-temperature row, "
          "because the entropy term of EK 9.3.A.5's expression grows with temperature "
          "and only then outweighs the positive enthalpy change."),

 dict(q="A process has a negative enthalpy change and a negative entropy change. At which "
        "temperatures is it thermodynamically favored?",
      choices=["Only at low temperatures", "Only at high temperatures",
               "At all temperatures", "At no temperature", "Only below 0 K"],
      ans=0,
      why="EK 9.3.A.6's table places this pair of signs in the low-temperature row, "
          "because the entropy term of EK 9.3.A.5's expression works against "
          "favorability here and grows with temperature, so only a small temperature "
          "leaves the negative enthalpy change in charge."),

 dict(q="The table gives the signs of the enthalpy and entropy changes for four "
        "processes. Which one is thermodynamically favored at all temperatures?",
      table=_T_QUAD,
      choices=["Process P", "Process Q", "Process R", "Process S",
               "None of the four processes"],
      ans=0,
      why="EK 9.3.A.6's table assigns the favored-at-all-temperatures row to a negative "
          "enthalpy change with a positive entropy change, and exactly one tabulated "
          "process has that pair of signs."),

 dict(q="Using the same table of signs, which process is thermodynamically favored at no "
        "temperature at all?",
      table=_T_QUAD,
      choices=["Process Q", "Process P", "Process R", "Process S",
               "All four are favored at some temperature"],
      ans=0,
      why="EK 9.3.A.6's table assigns the favored-at-no-temperature row to a positive "
          "enthalpy change with a negative entropy change, and exactly one tabulated "
          "process has that pair of signs."),

 dict(q="Using the tabulated signs once more, which process becomes thermodynamically "
        "favored only when the temperature is raised?",
      table=_T_QUAD,
      choices=["Process R", "Process S", "Process P", "Process Q",
               "None, because temperature does not affect favorability"],
      ans=0,
      why="EK 9.3.A.6's table assigns the high-temperature row to two positive changes, "
          "because the entropy term of EK 9.3.A.5's expression grows with temperature "
          "and must outgrow a positive enthalpy change before the process is favored."),

 dict(q="Using the tabulated signs again, which process is thermodynamically favored only "
        "while the temperature is kept low?",
      table=_T_QUAD,
      choices=["Process S", "Process R", "Process P", "Process Q",
               "None, because a low temperature always prevents a process"],
      ans=0,
      why="EK 9.3.A.6's table assigns the low-temperature row to two negative changes, "
          "because raising the temperature enlarges an entropy term that here works "
          "against favorability."),

 dict(q="In which cases does the framework say that no calculation of the standard free "
        "energy change is necessary?",
      choices=[
        "When the enthalpy change is negative with a positive entropy change, and when "
        "it is positive with a negative entropy change",
        "When the enthalpy change and the entropy change are both positive, and when "
        "both are negative",
        "Whenever the temperature is known to be 298 K",
        "Whenever the entropy change is exactly zero",
        "Only when the process is a phase change rather than a reaction"],
      ans=0,
      why="EK 9.3.A.6 says that where the enthalpy change is below zero and the entropy "
          "change above it, no calculation is necessary to determine that the process is "
          "favored, and that in the mirrored case no calculation is necessary to "
          "determine that it is unfavored. Those are exactly the two rows the "
          "temperature cannot move."),

 dict(q="For the reaction N2(g) + 3 H2(g) gives 2 NH3(g), what is the standard free "
        "energy change from the tabulated free energies of formation?",
      table=_T_GF,
      choices=[
        "\\( -32.8 \\) kJ/mol, thermodynamically favored",
        "\\( +32.8 \\) kJ/mol, thermodynamically unfavored",
        "\\( -16.4 \\) kJ/mol, thermodynamically favored",
        "\\( +16.4 \\) kJ/mol, thermodynamically unfavored",
        "\\( -65.6 \\) kJ/mol, thermodynamically favored"],
      ans=0,
      why="EK 9.3.A.3 subtracts the sum of the tabulated formation free energies of the "
          "reactants from that of the products, with every coefficient applied, and the "
          "two elements contribute nothing to the reactant sum. EK 9.3.A.2 then makes a "
          "result below zero thermodynamically favored."),

 dict(q="For the reaction CH4(g) + 2 O2(g) gives CO2(g) + 2 H2O(l), what is the standard "
        "free energy change from the same table?",
      table=_T_GF,
      choices=[
        "\\( -818.1 \\) kJ/mol, thermodynamically favored",
        "\\( +818.1 \\) kJ/mol, thermodynamically unfavored",
        "\\( -868.6 \\) kJ/mol, thermodynamically favored",
        "\\( -581.0 \\) kJ/mol, thermodynamically favored",
        "\\( -919.1 \\) kJ/mol, thermodynamically favored"],
      ans=0,
      why="EK 9.3.A.3's sums are coefficient-weighted, so the water entry is doubled, and "
          "the methane entry must be subtracted rather than left out. Failing to "
          "subtract the reactant gives the product sum by itself."),

 dict(q="For the reaction CaCO3(s) gives CaO(s) + CO2(g), what is the standard free "
        "energy change from the tabulated free energies of formation?",
      table=_T_GF,
      choices=[
        "\\( +130.4 \\) kJ/mol, thermodynamically unfavored",
        "\\( -130.4 \\) kJ/mol, thermodynamically favored",
        "\\( +734.4 \\) kJ/mol, thermodynamically unfavored",
        "\\( +524.8 \\) kJ/mol, thermodynamically unfavored",
        "\\( -2127.2 \\) kJ/mol, thermodynamically favored"],
      ans=0,
      why="EK 9.3.A.3 sums both products before subtracting the single reactant, and "
          "leaving either product out of the sum changes the answer by hundreds of "
          "kilojoules. EK 9.3.A.2 makes a result above zero thermodynamically unfavored "
          "under standard conditions."),

 dict(q="For the reaction N2(g) + O2(g) gives 2 NO(g), what is the standard free energy "
        "change from the same tabulated values?",
      table=_T_GF,
      choices=[
        "\\( +173.2 \\) kJ/mol, thermodynamically unfavored",
        "\\( -173.2 \\) kJ/mol, thermodynamically favored",
        "\\( +86.6 \\) kJ/mol, thermodynamically unfavored",
        "\\( -86.6 \\) kJ/mol, thermodynamically favored",
        "\\( +346.4 \\) kJ/mol, thermodynamically unfavored"],
      ans=0,
      why="EK 9.3.A.3 doubles the tabulated value for nitrogen monoxide, and both "
          "reactants are elements contributing nothing to the reactant sum. A positive "
          "result means the reaction is not favored under the standard conditions EK "
          "9.3.A.1 defines."),

 dict(q="For the reaction 2 NO(g) + O2(g) gives 2 NO2(g), what is the standard free "
        "energy change from the tabulated values?",
      table=_T_GF,
      choices=[
        "\\( -70.6 \\) kJ/mol, thermodynamically favored",
        "\\( +70.6 \\) kJ/mol, thermodynamically unfavored",
        "\\( -121.9 \\) kJ/mol, thermodynamically favored",
        "\\( +16.0 \\) kJ/mol, thermodynamically unfavored",
        "\\( +275.8 \\) kJ/mol, thermodynamically unfavored"],
      ans=0,
      why="EK 9.3.A.3 doubles both the nitrogen monoxide and the nitrogen dioxide "
          "entries, and dropping either coefficient changes both the size and, in one "
          "case, the sign of the answer."),

 dict(q="For the reaction H2O(l) gives H2O(g), what is the standard free energy change "
        "from the tabulated free energies of formation?",
      table=_T_GF,
      choices=[
        "\\( +8.5 \\) kJ/mol, thermodynamically unfavored",
        "\\( -8.5 \\) kJ/mol, thermodynamically favored",
        "\\( -465.7 \\) kJ/mol, thermodynamically favored",
        "\\( -228.6 \\) kJ/mol, thermodynamically favored",
        "\\( -237.1 \\) kJ/mol, thermodynamically favored"],
      ans=0,
      why="EK 9.3.A.3 applies to a physical process as it does to a chemical one, and "
          "the two tabulated water entries differ by only a few kilojoules. The result "
          "is above zero, so under the standard conditions of EK 9.3.A.1, which fix the "
          "vapour at 1.0 atm, the vaporization is not favored."),

 dict(q="For the reaction 2 NH3(g) gives N2(g) + 3 H2(g), what is the standard free "
        "energy change from the tabulated values?",
      table=_T_GF,
      choices=[
        "\\( +32.8 \\) kJ/mol, thermodynamically unfavored",
        "\\( -32.8 \\) kJ/mol, thermodynamically favored",
        "\\( +16.4 \\) kJ/mol, thermodynamically unfavored",
        "\\( -16.4 \\) kJ/mol, thermodynamically favored",
        "\\( +65.6 \\) kJ/mol, thermodynamically unfavored"],
      ans=0,
      why="EK 9.3.A.3's subtraction runs products less reactants, so writing the "
          "synthesis backwards reverses the sign and leaves the magnitude alone. A "
          "reaction and its reverse cannot both be favored under the same standard "
          "conditions."),

 dict(q="Which examples does the framework give of processes for which both enthalpy and "
        "entropy must be considered before favorability can be decided?",
      choices=[
        "The freezing of water and the dissolution of sodium nitrate",
        "The combustion of methane and the rusting of iron",
        "The synthesis of ammonia and the decomposition of limestone",
        "The vaporization of water and the melting of ice",
        "The formation of nitrogen monoxide and the formation of nitrogen dioxide"],
      ans=0,
      why="EK 9.3.A.4 states that in some cases it is necessary to consider both "
          "enthalpy and entropy to determine whether a process will be thermodynamically "
          "favored, and names the freezing of water and the dissolution of sodium "
          "nitrate as examples of such phenomena."),

 dict(q="The freezing of water has a negative enthalpy change and a negative entropy "
        "change. At which temperatures is it thermodynamically favored?",
      choices=["Only at low temperatures", "Only at high temperatures",
               "At all temperatures", "At no temperature",
               "At every temperature above the melting point"],
      ans=0,
      why="EK 9.3.A.4 names freezing as a case where both quantities must be weighed, and "
          "EK 9.3.A.6's table places two negative changes in the low-temperature row, "
          "because the entropy term of EK 9.3.A.5's expression grows with temperature "
          "and here opposes favorability."),

 dict(q="The dissolution of sodium nitrate has a positive enthalpy change and a positive "
        "entropy change. At which temperatures is it thermodynamically favored?",
      choices=["Only at high temperatures", "Only at low temperatures",
               "At all temperatures", "At no temperature",
               "Only where the solution is saturated"],
      ans=0,
      why="EK 9.3.A.4 names this dissolution as a case where both quantities must be "
          "weighed, and EK 9.3.A.6's table places two positive changes in the "
          "high-temperature row, because only a large enough temperature lets the "
          "entropy term outweigh the positive enthalpy change."),

 dict(q="A process has \\( \\Delta H^\\circ = -80.0 \\) kJ/mol and \\( \\Delta S^\\circ = "
        "-200.0 \\) J/(mol K). What is its standard free energy change at 500 K?",
      choices=[
        "\\( +20.0 \\) kJ/mol, thermodynamically unfavored",
        "\\( -20.0 \\) kJ/mol, thermodynamically favored",
        "\\( -180.0 \\) kJ/mol, thermodynamically favored",
        "\\( +100.0 \\) kJ/mol, thermodynamically unfavored",
        "\\( -80.0 \\) kJ/mol, thermodynamically favored"],
      ans=0,
      why="EK 9.3.A.5's equation subtracts a negative entropy term, which adds to the "
          "enthalpy change, and at this temperature that addition is larger than the "
          "enthalpy change itself. Two negative changes put the process in EK 9.3.A.6's "
          "low-temperature row, and 500 K is past the crossover."),

 dict(q="Below what temperature is a process with \\( \\Delta H^\\circ = -80.0 \\) kJ/mol "
        "and \\( \\Delta S^\\circ = -200.0 \\) J/(mol K) thermodynamically favored?",
      choices=["Below 400 K", "Below 40 K", "Below 4000 K", "Below 160 K",
               "It is favored at every temperature"],
      ans=0,
      why="EK 9.3.A.5's expression changes sign where the enthalpy change equals the "
          "temperature times the entropy change, so the crossover is their quotient once "
          "the entropy change is converted from joules to kilojoules. EK 9.3.A.6 makes "
          "the favored side of that crossover the low-temperature side for two negative "
          "changes."),

 dict(q="A process has \\( \\Delta H^\\circ = +20.0 \\) kJ/mol and \\( \\Delta S^\\circ = "
        "+50.0 \\) J/(mol K). What is its standard free energy change at 400 K?",
      choices=[
        "\\( 0.0 \\) kJ/mol, which is the temperature at which the sign changes over",
        "\\( +40.0 \\) kJ/mol, thermodynamically unfavored",
        "\\( -40.0 \\) kJ/mol, thermodynamically favored",
        "\\( +20.0 \\) kJ/mol, thermodynamically unfavored",
        "\\( -20.0 \\) kJ/mol, thermodynamically favored"],
      ans=0,
      why="EK 9.3.A.5's two terms are equal in size at this temperature, so the "
          "difference is zero and the process sits exactly on the boundary EK 9.3.A.2 "
          "draws. The enthalpy change alone and the entropy term alone are the two "
          "halves of the calculation and neither is the answer."),

 dict(q="A student computes the standard free energy change of a process with \\( \\Delta "
        "H^\\circ = -100.0 \\) kJ/mol and \\( \\Delta S^\\circ = -200.0 \\) J/(mol K) at "
        "300 K, and obtains \\( +59900.0 \\) kJ/mol. What went wrong?",
      choices=[
        "The entropy change was left in joules instead of being converted to kilojoules",
        "The temperature was left in degrees Celsius instead of kelvin",
        "The entropy term was added to the enthalpy change instead of being subtracted",
        "The enthalpy change was left in joules instead of being converted to kilojoules",
        "The signs of the two changes were exchanged before the calculation"],
      ans=0,
      why="EK 9.3.A.5's equation multiplies the entropy change by a temperature of a few "
          "hundred kelvin, so an entropy change left in joules makes that term about a "
          "thousand times too large, which is exactly the size of the error reported. "
          "Each other mistake named would give a value of ordinary size."),

 dict(q="What are the two routes the framework gives for obtaining the standard free "
        "energy change of a process?",
      choices=[
        "From the standard free energies of formation, or from the enthalpy and entropy "
        "changes at the temperature of interest",
        "From the absolute entropies alone, or from the temperature alone",
        "From the standard free energies of formation alone, since there is no other way",
        "From the enthalpy change alone, or from the entropy change alone",
        "From the temperature and the pressure of the system"],
      ans=0,
      why="EK 9.3.A.3 gives the route through the standard free energies of formation of "
          "the reactants and products, and EK 9.3.A.5 gives the route through the "
          "enthalpy and entropy changes at a given temperature. Neither the enthalpy nor "
          "the entropy change decides the matter on its own, which is the point of EK "
          "9.3.A.4."),

]
