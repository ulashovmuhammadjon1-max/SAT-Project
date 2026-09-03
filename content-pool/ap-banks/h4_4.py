# AP CHEMISTRY 4.4 Physical and Chemical Changes
# CED effective Fall 2024, Unit 4 Chemical Reactions.
# Learning objective 4.4.A: explain the relationship between macroscopic
# characteristics and bond interactions for (i) chemical processes and
# (ii) physical processes. Suggested skill 6.B, support a claim with evidence
# from experimental data.
#
# Essential knowledge relied on, in the framework's own words:
#   4.4.A.1  Processes that involve the breaking and/or formation of chemical
#            bonds are typically classified as chemical processes. Processes
#            that involve only changes in intermolecular interactions, such as
#            phase changes, are typically classified as physical processes.
#   4.4.A.2  Sometimes physical processes involve the breaking of chemical
#            bonds. For example, plausible arguments could be made for the
#            dissolution of a salt in water, as either a physical or chemical
#            process, involves breaking of ionic bonds, and the formation of
#            ion-dipole interactions between ions and solvent.
#
# ON THE WORD "TYPICALLY". 4.4.A.1 hedges twice and 4.4.A.2 exists to say why.
# No item here keys on "a phase change is ALWAYS physical" or on "dissolving is
# ALWAYS physical" -- the salt items key on the framework's own answer, that a
# plausible argument runs either way because ionic bonds break and ion-dipole
# interactions form. Where a dissolution item does key cleanly on "physical",
# the solute is molecular and the only interactions broken are intermolecular,
# which is the condition 4.4.A.1 states.
#
# NOTATION. Chemistry is not typeset by export_units.py. Formulas in prose stay
# plain text (H2O, CO2, NaCl); only quantities that need it carry a hand-written
# \( ... \) span. See SCIENCE_BRIEF.md and h_chem_notation.py.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md.
TOPIC = ("4.4", "Physical and Chemical Changes", 4)

_T_WATER_ENERGY = dict(
    headers=["Process for H2O", "Energy required (kilojoules per mole)"],
    rows=[["Melting the solid", "6.0"],
          ["Vaporizing the liquid", "41"],
          ["Breaking one mole of O-H bonds within the molecules", "464"]])

_T_HALIDES = dict(
    headers=["Substance", "Enthalpy of vaporization (kilojoules per mole)",
             "Average enthalpy of the bond inside the molecule "
             "(kilojoules per mole)",
             "Normal boiling point (degrees Celsius)"],
    rows=[["HCl", "16.2", "431", "-85"],
          ["HBr", "17.6", "366", "-67"],
          ["HI", "19.8", "298", "-35"]])

_T_THREE_PROCESSES = dict(
    headers=["Process", "Substances present before", "Substances present afterward",
             "Energy change (kilojoules per mole)"],
    rows=[["Sublimation of dry ice", "CO2", "CO2", "+25"],
          ["Synthesis of ammonia", "N2 and H2", "NH3", "-92"],
          ["Boiling of ethanol", "Ethanol", "Ethanol", "+38"]])

_T_RECOVERY = dict(
    headers=["Trial", "Solid added to 100. grams of water", "Mass added (grams)",
             "Mass of solid recovered after all the water was evaporated (grams)"],
    rows=[["1", "Sucrose", "10.0", "10.0"],
          ["2", "Sodium chloride", "10.0", "10.0"],
          ["3", "Calcium carbonate, heated to 900 degrees Celsius", "10.0", "5.6"]])

_T_SEALED = dict(
    headers=["Flask", "Contents at the start", "Mass at the start (grams)",
             "Mass after 30 minutes (grams)"],
    rows=[["Sealed flask 1", "Liquid ethanol, warmed to boiling", "128.40", "128.40"],
          ["Sealed flask 2", "Magnesium ribbon and hydrochloric acid", "128.40", "128.40"]])

_T_LATTICE = dict(
    headers=["Quantity for NaCl", "Value (kilojoules per mole)"],
    rows=[["Energy to separate the ions from the crystal", "787"],
          ["Energy released when the separated ions are hydrated", "-784"],
          ["Net energy change on dissolving the crystal in water", "+3"]])

_T_ALKANES = dict(
    headers=["Alkane", "Enthalpy of vaporization (kilojoules per mole)",
             "Enthalpy of complete combustion (kilojoules per mole)"],
    rows=[["Pentane", "27", "-3510"],
          ["Hexane", "32", "-4160"],
          ["Heptane", "36", "-4810"]])

QUESTIONS = [

 dict(q="A sealed flask holds liquid bromine, Br2. The flask is warmed until the "
        "last of the liquid has become a reddish-brown gas. The mass of the flask "
        "and its contents is unchanged and the gas is still Br2. Which of the "
        "following best classifies this process and gives the reason?",
      choices=[
        "Physical, because only the attractions between whole Br2 molecules were "
        "overcome and no Br-Br bond was broken",
        "Chemical, because the Br-Br bonds had to be broken before the sample "
        "could enter the gas phase",
        "Chemical, because the color of the sample became more intense as it "
        "filled the larger volume",
        "Physical, because bromine atoms were rearranged into a different "
        "molecule with the same total mass",
        "Neither, because a process that conserves mass is not classified as "
        "either physical or chemical"],
      ans=0,
      why="EK 4.4.A.1 classifies a process that involves only changes in "
          "intermolecular interactions, such as a phase change, as physical. "
          "The sample is Br2 before and after, so the Br-Br bond is intact and "
          "only the attractions between molecules were overcome."),

 dict(q="Methane burns in oxygen according to CH4 + 2 O2 gives CO2 + 2 H2O. Which "
        "of the following identifies the bond interactions that make this a "
        "chemical process?",
      choices=[
        "C-H and O=O bonds within the reactant molecules are broken and new C=O "
        "and O-H bonds are formed",
        "Only the attractions between separate CH4 molecules are overcome, and "
        "the atoms are then free to move apart",
        "The hydrogen bonds holding CH4 molecules to O2 molecules are replaced "
        "by weaker London dispersion forces",
        "The molecules gain kinetic energy until they move fast enough to escape "
        "the container, leaving new substances behind",
        "Ion-dipole interactions form between the carbon atoms and the oxygen "
        "molecules, releasing energy as heat"],
      ans=0,
      why="EK 4.4.A.1 classifies processes that involve the breaking and/or "
          "formation of chemical bonds as chemical. Combustion breaks bonds "
          "inside CH4 and O2 and forms bonds inside CO2 and H2O, so the "
          "substances present afterward are not the substances present before."),

 dict(q="The table gives three energy values measured for water. A student wants "
        "to identify the value associated with breaking bonds inside the water "
        "molecules rather than with separating whole molecules from one another. "
        "Which value should the student choose, and why?",
      table=_T_WATER_ENERGY,
      choices=[
        "464 kilojoules per mole, because it is far larger than either value "
        "associated with a phase change of the same substance",
        "41 kilojoules per mole, because vaporization is the process that "
        "produces individual molecules in the gas phase",
        "6.0 kilojoules per mole, because melting is the first step in taking "
        "the sample apart and must break the strongest attractions",
        "The sum of 6.0 and 41 kilojoules per mole, because melting and boiling "
        "together convert the solid entirely into separate particles",
        "None of the values, because breaking a bond inside a molecule always "
        "releases energy rather than requiring it"],
      ans=0,
      why="EK 4.4.A.1 separates changes in intermolecular interactions from the "
          "breaking of chemical bonds. Melting and vaporizing only overcome "
          "attractions between whole H2O molecules; the tabulated 464 belongs "
          "to the O-H bond inside a molecule and is an order of magnitude larger."),

 dict(q="Solid sodium chloride is stirred into water until it has completely "
        "dissolved. Two students disagree about whether this is a physical or a "
        "chemical process. Which response is best supported by the course "
        "framework?",
      choices=[
        "A plausible argument can be made either way, because ionic bonds are "
        "broken and ion-dipole interactions between the ions and the solvent "
        "are formed",
        "It is strictly physical, because no bonds of any kind are broken when "
        "an ionic solid dissolves in water",
        "It is strictly chemical, because the sodium ions and chloride ions did "
        "not exist before the solid was placed in the water",
        "It is strictly physical, because the solution can be evaporated and the "
        "same mass of solid recovered, and reversibility settles the question",
        "It is strictly chemical, because water molecules are consumed as the "
        "solid dissolves and cannot be recovered"],
      ans=0,
      why="EK 4.4.A.2 states that plausible arguments could be made for the "
          "dissolution of a salt in water as either a physical or a chemical "
          "process, because it involves breaking of ionic bonds and the "
          "formation of ion-dipole interactions between ions and solvent."),

 dict(q="Solid iodine, I2, dissolves readily in liquid hexane to give a violet "
        "solution containing intact I2 molecules. Which classification of the "
        "dissolving is best justified?",
      choices=[
        "Physical, because only the London dispersion forces holding the I2 "
        "molecules in the crystal are replaced by forces between I2 and hexane",
        "Chemical, because the violet color of the solution differs from the "
        "gray-black color of the crystal",
        "Chemical, because the I-I bond must break in order for iodine to "
        "spread evenly through the solvent",
        "Physical, because iodine and hexane are both nonpolar and nonpolar "
        "substances cannot undergo any process at all",
        "Chemical, because hexane molecules bond covalently to the iodine and "
        "hold it in solution"],
      ans=0,
      why="EK 4.4.A.1 makes a process that involves only changes in "
          "intermolecular interactions a physical process. Intact I2 molecules "
          "are present afterward, so the I-I bond was never broken and only the "
          "attractions between molecules changed."),

 dict(q="A block of solid carbon dioxide is left in an open room and gradually "
        "disappears without ever becoming a liquid. Analysis of the surrounding "
        "air shows an increased amount of CO2. Which statement about bond "
        "interactions in this process is correct?",
      choices=[
        "The C=O bonds inside the molecules remain intact while the attractions "
        "between whole CO2 molecules are overcome",
        "Each C=O bond is broken and then re-formed as the molecules enter the "
        "gas phase, so the overall process is chemical",
        "The carbon atoms are transferred to oxygen molecules already present in "
        "the air, forming new CO2 molecules",
        "London dispersion forces are converted into covalent bonds as the solid "
        "becomes a gas, which is why no liquid appears",
        "No interactions of any kind are broken, because a solid becoming a gas "
        "requires no input of energy"],
      ans=0,
      why="EK 4.4.A.1 names phase changes as processes that involve only changes "
          "in intermolecular interactions. The substance is CO2 before and "
          "after, so the molecules survive and only the attractions holding them "
          "in the solid are overcome."),

 dict(q="An electric current is passed through water containing a small amount of "
        "dissolved electrolyte, and two gases collect at the electrodes in a two "
        "to one volume ratio. Testing shows one gas is H2 and the other is O2. "
        "Which classification and reason are correct?",
      choices=[
        "Chemical, because O-H bonds inside the water molecules were broken and "
        "H-H and O=O bonds were formed",
        "Physical, because the water was separated into its components without "
        "any new substance being made",
        "Physical, because passing a current through a sample can change only "
        "the arrangement of the molecules, not their identity",
        "Chemical, because the electrolyte dissolved in the water and produced "
        "ions where none had existed",
        "Physical, because the total mass of the two gases equals the mass of "
        "water that disappeared"],
      ans=0,
      why="EK 4.4.A.1 classifies as chemical a process involving the breaking "
          "and/or formation of chemical bonds. Water molecules do not survive "
          "the process; the O-H bonds within them are broken and the atoms are "
          "assembled into H2 and O2 molecules."),

 dict(q="A large crystal of table salt is ground with a mortar and pestle into a "
        "fine powder. Which statement best describes what happened at the "
        "particle level?",
      choices=[
        "The crystal was divided into smaller crystals, so the ions remain held "
        "to one another in the same lattice arrangement",
        "The ionic bonds between every sodium ion and chloride ion were broken, "
        "producing free ions in the powder",
        "The chloride ions were oxidized to chlorine atoms by the friction of "
        "the pestle",
        "The sodium chloride was converted into a different compound with the "
        "same empirical formula but smaller particles",
        "New ion-dipole interactions were formed between the ions and the "
        "surrounding air"],
      ans=0,
      why="Grinding produces smaller pieces of the same substance. EK 4.4.A.1 "
          "reserves the chemical classification for processes that break or form "
          "chemical bonds, and the ionic lattice within each fragment is "
          "unchanged, so no chemical bond has been broken."),

 dict(q="Hydrogen chloride gas is bubbled into water. The resulting solution "
        "conducts electricity well, and analysis finds H3O+ and Cl- ions and "
        "essentially no intact HCl molecules. Which reasoning supports "
        "classifying this as a chemical process?",
      choices=[
        "The covalent H-Cl bond is broken and a new O-H bond is formed on a "
        "water molecule, so the species present afterward are different",
        "The HCl molecules are simply surrounded by water molecules, and "
        "surrounding a molecule is what makes a process chemical",
        "The gas becomes a solution, and any change of physical state counts as "
        "a chemical process",
        "The solution conducts electricity, and conductivity by itself is proof "
        "that covalent bonds have been formed",
        "Water molecules are pulled apart into hydrogen and oxygen atoms, which "
        "then attach to the chloride ions"],
      ans=0,
      why="EK 4.4.A.1 makes bond breaking and bond formation the criterion. The "
          "H-Cl bond does not survive: the proton is transferred to water, "
          "forming a new O-H bond in H3O+, so different species are present "
          "after the process than before."),

 dict(q="The table lists, for three hydrogen halides, the enthalpy of "
        "vaporization, the average enthalpy of the bond inside the molecule, and "
        "the normal boiling point. Which conclusion is supported by these data?",
      table=_T_HALIDES,
      choices=[
        "Vaporizing each substance costs less than a tenth of what breaking its "
        "internal bond costs, consistent with boiling changing only "
        "intermolecular interactions",
        "The substance with the strongest bond inside the molecule also has the "
        "highest boiling point, so the two quantities measure the same "
        "attraction",
        "Boiling HI must break its H-I bond, because vaporizing HI costs more "
        "than vaporizing either of the other two",
        "The bond enthalpies increase from HCl to HI, so the heavier molecules "
        "are held together more tightly inside the molecule",
        "Because all three boiling points are below zero degrees Celsius, none "
        "of these substances has any attractions between its molecules"],
      ans=0,
      why="EK 4.4.A.1 distinguishes intermolecular interactions from chemical "
          "bonds. The tabulated vaporization enthalpies are under twenty "
          "kilojoules per mole against internal bonds of several hundred, and "
          "the bond column falls while the boiling point column rises."),

 dict(q="Steam at 100 degrees Celsius is passed over a cold surface and collects "
        "as liquid water. Energy is released to the surface. Which statement "
        "correctly relates the macroscopic observation to bond interactions?",
      choices=[
        "Attractions between H2O molecules are formed, releasing energy, while "
        "every O-H bond inside the molecules stays intact",
        "O-H bonds are formed as the gas condenses, which is the source of the "
        "energy released to the surface",
        "The hydrogen and oxygen atoms recombine into water molecules, which is "
        "why liquid appears on the cold surface",
        "Energy is released because the covalent bonds inside water are weaker "
        "in the liquid than in the gas",
        "Condensation forms ion-dipole interactions between hydrogen ions and "
        "oxide ions in the liquid"],
      ans=0,
      why="EK 4.4.A.1 names phase changes as processes that involve only changes "
          "in intermolecular interactions. Condensation is the reverse of "
          "vaporization: attractions between whole molecules re-form and release "
          "energy, and the molecules themselves are unaltered."),

 dict(q="For each of three processes the table gives the substances present "
        "before, the substances present afterward, and the energy change. Which "
        "process is best classified as chemical, and on what evidence in the "
        "table?",
      table=_T_THREE_PROCESSES,
      choices=[
        "The synthesis of ammonia, because it is the only row whose substances "
        "afterward differ from its substances before",
        "The sublimation of dry ice, because it is the only row with a positive "
        "energy change smaller than thirty",
        "The boiling of ethanol, because it has the largest positive energy "
        "change in the table",
        "All three, because every row in the table reports a nonzero energy "
        "change",
        "None of the three, because the sign of an energy change cannot indicate "
        "whether bonds were broken"],
      ans=0,
      why="EK 4.4.A.1 makes the breaking and forming of chemical bonds the test. "
          "Two rows list the same substance before and after, so only "
          "attractions between molecules changed; the ammonia row lists N2 and "
          "H2 before and a different substance afterward."),

 dict(q="Which of the following processes involves ONLY changes in intermolecular "
        "interactions?",
      choices=[
        "Liquid mercury freezing to a solid at negative 39 degrees Celsius",
        "Zinc metal reacting with hydrochloric acid to release hydrogen gas",
        "Silver nitrate solution mixing with sodium chloride solution to form a "
        "white solid",
        "Ammonia gas reacting with hydrogen chloride gas to form a white smoke "
        "of ammonium chloride",
        "Solid potassium chlorate decomposing on heating to give potassium "
        "chloride and oxygen"],
      ans=0,
      why="EK 4.4.A.1 offers phase changes as its example of processes involving "
          "only changes in intermolecular interactions. Freezing mercury is a "
          "phase change of one substance, while each of the other four produces "
          "a substance that was not present at the start."),

 dict(q="A student mixes two colorless solutions and observes that the mixture "
        "turns bright yellow. The student concludes that a chemical process must "
        "have occurred. Which evaluation of that reasoning is best?",
      choices=[
        "The color change alone is not sufficient, because the classification "
        "depends on whether chemical bonds were broken or formed",
        "The reasoning is sound, because a change of color is by definition the "
        "breaking of a chemical bond",
        "The reasoning is sound, because two solutions cannot be mixed without a "
        "reaction occurring between them",
        "The color change proves a physical process, because color is a physical "
        "property of a substance",
        "The reasoning fails only because the student did not measure the mass of "
        "the mixture before and after"],
      ans=0,
      why="EK 4.4.A.1 defines the two categories by bond interactions, not by "
          "any single observation. A colored species can appear because bonds "
          "were formed, but it can also appear because a colored solute was "
          "diluted or dissolved, so the observation alone does not decide."),

 dict(q="A student added a solid to water, treated it as described, and then "
        "evaporated all of the water away. The table shows how much solid was "
        "added and how much was recovered. Which trial gives the strongest "
        "evidence that the substance underwent a chemical process?",
      table=_T_RECOVERY,
      choices=[
        "The trial with calcium carbonate, because the recovered mass is smaller "
        "than the mass added and the missing mass cannot be the water",
        "The trial with sucrose, because sucrose is a molecular compound and "
        "molecular compounds are the ones that react",
        "The trial with sodium chloride, because dissolving an ionic solid "
        "always breaks ionic bonds",
        "Both the sucrose trial and the sodium chloride trial, because in each "
        "of them the solid disappeared from view",
        "None of the trials, because evaporating water is a physical process and "
        "cannot reveal anything about the solid"],
      ans=0,
      why="EK 4.4.A.1 makes the survival of the original substance the test. The "
          "first two trials return every gram that was added, so the solute was "
          "unchanged; the heated carbonate returns less than it started with, "
          "meaning part of it became something else and left the container."),

 dict(q="Two identical sealed flasks are prepared as described in the table. "
        "Neither flask changes mass over the half hour. What can be concluded "
        "about whether a chemical process occurred in each?",
      table=_T_SEALED,
      choices=[
        "Nothing can be concluded from mass alone, because mass is conserved "
        "whether or not chemical bonds are broken",
        "Neither flask underwent a chemical process, because a chemical process "
        "always changes the mass of the contents",
        "Both flasks underwent a chemical process, because sealing a container "
        "forces the contents to react",
        "Only the flask holding ethanol underwent a chemical process, because "
        "boiling requires the largest input of energy",
        "Only the flask holding ethanol underwent a physical process, and mass "
        "data are what establish that"],
      ans=0,
      why="EK 4.4.A.1 classifies by bond interactions. Atoms are conserved in "
          "both flasks, so both masses stay the same; boiling ethanol changes "
          "only intermolecular interactions while magnesium and acid form new "
          "substances, and the identical mass readings distinguish neither."),

 dict(q="Sucrose dissolves in water to give a solution containing intact sucrose "
        "molecules surrounded by water molecules. Which pair of statements "
        "correctly contrasts this with the dissolving of sodium chloride?",
      choices=[
        "Dissolving sucrose changes only intermolecular interactions, while "
        "dissolving sodium chloride also breaks the ionic bonds of the lattice",
        "Dissolving sucrose breaks covalent bonds within the molecules, while "
        "dissolving sodium chloride leaves the lattice intact in solution",
        "Both processes break covalent bonds, so both are unambiguously "
        "chemical processes",
        "Both processes leave every particle exactly as it was in the solid, so "
        "the two cases raise no different questions",
        "Dissolving sucrose forms ion-dipole interactions, while dissolving "
        "sodium chloride forms hydrogen bonds between the ions"],
      ans=0,
      why="EK 4.4.A.1 makes a process physical when only intermolecular "
          "interactions change, which is the sucrose case. EK 4.4.A.2 makes the "
          "salt case arguable precisely because ionic bonds are broken and "
          "ion-dipole interactions between ions and solvent are formed."),

 dict(q="Which interaction forms between a dissolved sodium ion and the water "
        "molecules that surround it?",
      choices=[
        "An ion-dipole interaction, because the partial negative end of a polar "
        "water molecule is attracted to the positive ion",
        "A covalent bond, because the sodium ion shares one of its electrons "
        "with an oxygen atom",
        "A hydrogen bond, because the sodium ion carries a partial positive "
        "charge on a hydrogen atom",
        "An ionic bond, because the sodium ion and the water molecule carry "
        "opposite whole charges",
        "A London dispersion force only, because sodium ions have no permanent "
        "charge in solution"],
      ans=0,
      why="EK 4.4.A.2 names the interaction formed between ions and solvent on "
          "dissolution as an ion-dipole interaction. The ion carries a whole "
          "charge and the water molecule is a dipole, which is exactly the pair "
          "of properties that interaction requires."),

 dict(q="A sample of liquid ethanol is heated in an open dish until none is left. "
        "A second sample of ethanol is burned completely in air. Which comparison "
        "of the two processes is correct?",
      choices=[
        "Only the burning breaks bonds within the ethanol molecules, so only the "
        "burning is a chemical process",
        "Both processes break bonds within the ethanol molecules, so both are "
        "chemical processes",
        "Neither process breaks bonds within the ethanol molecules, so both are "
        "physical processes",
        "Only the heating breaks bonds within the ethanol molecules, because "
        "heat is what supplies the energy to break a bond",
        "The two processes cannot be compared, because one occurred in an open "
        "dish and the other in air"],
      ans=0,
      why="EK 4.4.A.1 makes bond breaking the criterion. Evaporation leaves "
          "ethanol molecules intact in the vapor and changes only intermolecular "
          "interactions; combustion converts them into carbon dioxide and water, "
          "which requires bonds within the molecules to be broken."),

 dict(q="Copper wire is heated strongly in air and the shiny surface turns black. "
        "The black material has a greater mass than the copper taken and does not "
        "conduct electricity as copper does. Which claim is best supported?",
      choices=[
        "A chemical process occurred, because the added mass and the different "
        "properties show a new substance containing oxygen was formed",
        "A physical process occurred, because heating a metal changes only how "
        "tightly its atoms are packed",
        "A physical process occurred, because the black material can be scraped "
        "off and the copper underneath is unchanged",
        "A chemical process occurred, because heating any sample above room "
        "temperature breaks its bonds",
        "No conclusion is possible, because mass measurements taken in open air "
        "carry no information"],
      ans=0,
      why="EK 4.4.A.1 classifies a process as chemical when chemical bonds are "
          "broken or formed. Mass gained from the surrounding air together with "
          "properties unlike copper's identifies a new compound, so bonds "
          "between copper and oxygen were formed."),

 dict(q="A student is asked to design an observation that would distinguish a "
        "chemical process from a physical one for a white solid that disappears "
        "when stirred into water. Which observation would be most useful?",
      choices=[
        "Evaporate the water afterward and check whether the recovered solid has "
        "the same mass and melting point as the solid added",
        "Measure how long the solid takes to disappear, since chemical processes "
        "are always faster than physical ones",
        "Measure the volume of the solution, since a chemical process always "
        "increases the volume of a liquid",
        "Note whether the solid disappears completely, since only a chemical "
        "process can consume all of a solid",
        "Check whether the mixture is warm to the touch, since only a chemical "
        "process can release energy"],
      ans=0,
      why="EK 4.4.A.1 turns on whether the original substance survives. "
          "Recovering the same mass with the same characteristic properties "
          "shows the solute was unchanged, while a different mass or melting "
          "point points to bonds having been broken or formed."),

 dict(q="Molten sodium chloride at 850 degrees Celsius conducts electricity, while "
        "the solid at room temperature does not. Which statement about the "
        "melting is best supported?",
      choices=[
        "Melting separates the ions from their fixed positions so they can move, "
        "and no new substance is produced",
        "Melting converts the sodium ions and chloride ions into sodium atoms "
        "and chlorine atoms, which carry the current",
        "Melting forms covalent bonds between sodium and chlorine, and those "
        "bonds conduct the current",
        "Melting is a chemical process, because only a chemical process can "
        "change whether a sample conducts electricity",
        "Melting produces a solution of sodium chloride in water, which is why "
        "the liquid conducts"],
      ans=0,
      why="The same substance, sodium chloride, is present before and after; "
          "what changes is that the ions are no longer locked in fixed "
          "positions. EK 4.4.A.1 classifies a phase change as physical, and no "
          "new substance appears here."),

 dict(q="A solution of lead nitrate is added to a solution of potassium iodide, "
        "and a bright yellow solid settles out. Which statement identifies the "
        "bond interactions and the correct classification?",
      choices=[
        "Bonds between lead ions and iodide ions are formed in a new insoluble "
        "solid, so the process is chemical",
        "The two solutions are simply mixed and the yellow color is the sum of "
        "the two original colors, so the process is physical",
        "Water molecules are removed from around the ions and nothing else "
        "changes, so the process is physical",
        "Covalent bonds within the nitrate ions are broken, so the process is "
        "chemical",
        "The potassium ions and nitrate ions are destroyed, so the process is "
        "chemical"],
      ans=0,
      why="EK 4.4.A.1 makes the formation of chemical bonds a chemical process. "
          "Ions that were free in solution become held together in an insoluble "
          "ionic solid, which is bond formation; the potassium and nitrate ions "
          "remain in solution unchanged."),

 dict(q="Ammonium nitrate dissolves in water and the resulting solution becomes "
        "noticeably colder. Which statement about this observation is correct?",
      choices=[
        "Energy absorbed in separating the ions exceeded the energy released in "
        "forming ion-dipole interactions with water",
        "The cooling proves that no bonds of any kind were broken, since bond "
        "breaking always warms a sample",
        "The cooling proves that the process is chemical, since only chemical "
        "processes can lower a temperature",
        "The cooling shows that the water froze around the ions and released "
        "energy to the surroundings",
        "The cooling shows that ammonium nitrate molecules remained intact and "
        "simply spread through the water"],
      ans=0,
      why="EK 4.4.A.2 identifies the two interactions at work in dissolving a "
          "salt: ionic bonds are broken, which costs energy, and ion-dipole "
          "interactions with the solvent are formed, which releases it. A net "
          "cooling means the first outweighed the second."),

 dict(q="The table reports the energy needed to pull the ions of sodium chloride "
        "apart, the energy released when those separated ions are hydrated, and "
        "the net energy change on dissolving. Which conclusion follows from these "
        "three values?",
      table=_T_LATTICE,
      choices=[
        "The energy released on forming ion-dipole interactions nearly cancels "
        "the energy needed to break the ionic bonds, leaving a small net change",
        "Dissolving sodium chloride releases far more energy than it absorbs, "
        "which is why the net value is positive",
        "No ionic bonds are broken when sodium chloride dissolves, because the "
        "net energy change is close to zero",
        "The hydration step must occur before the separation step, because its "
        "value is negative",
        "The net value shows that dissolving sodium chloride breaks covalent "
        "bonds within the water molecules"],
      ans=0,
      why="EK 4.4.A.2 names both steps in the dissolution of a salt. The "
          "tabulated values are 787 to break the lattice and 784 released on "
          "hydration, so they nearly cancel and the small positive remainder is "
          "the net; a near-zero net does not mean nothing was broken."),

 dict(q="Which of the following statements about phase changes is consistent with "
        "the course framework?",
      choices=[
        "A phase change is typically classified as physical because it involves "
        "only changes in intermolecular interactions",
        "A phase change is always classified as chemical, because energy must be "
        "supplied for a substance to melt or boil",
        "A phase change is classified as physical only when the substance is "
        "molecular, and as chemical whenever it is ionic",
        "A phase change is classified as physical only if the mass of the sample "
        "increases during the change",
        "A phase change cannot be classified at all, because both bond breaking "
        "and intermolecular changes occur in equal measure"],
      ans=0,
      why="EK 4.4.A.1 states that processes involving only changes in "
          "intermolecular interactions, such as phase changes, are typically "
          "classified as physical processes. The hedge is in the framework's own "
          "wording and does not depend on the substance being molecular."),

 dict(q="Hexane and pentane are mixed and the mixture is then distilled, "
        "collecting the pentane first. The two collected liquids have the same "
        "properties they had before mixing. Which classification is correct for "
        "the mixing and for the distillation?",
      choices=[
        "Both are physical, because only attractions between whole molecules "
        "were changed and both substances survive unaltered",
        "The mixing is physical and the distillation is chemical, because "
        "heating a mixture always breaks bonds",
        "The mixing is chemical and the distillation is physical, because "
        "combining two liquids produces a new substance",
        "Both are chemical, because energy had to be supplied to separate the "
        "two liquids again",
        "Neither can be classified, because a mixture is not a substance and "
        "only substances undergo processes"],
      ans=0,
      why="EK 4.4.A.1 makes a process physical when only intermolecular "
          "interactions change. Both liquids are recovered with their original "
          "properties, so no bond within a pentane or hexane molecule was broken "
          "in either step."),

 dict(q="The table lists, for three alkanes, the enthalpy of vaporization and the "
        "enthalpy of complete combustion. Which comparison is supported and what "
        "does it indicate about bond interactions?",
      table=_T_ALKANES,
      choices=[
        "Combustion of each alkane involves an energy change more than a hundred "
        "times its vaporization, consistent with combustion breaking bonds "
        "within the molecules",
        "Vaporization and combustion release energy changes of similar size, so "
        "both processes must break the same bonds",
        "Vaporization of heptane releases more energy than its combustion, so "
        "vaporization is the more chemical of the two processes",
        "Combustion values are negative, so combustion breaks no bonds at all "
        "and only forms them",
        "The two columns trend in opposite directions, which shows that a larger "
        "molecule is easier to vaporize"],
      ans=0,
      why="EK 4.4.A.1 separates changes in intermolecular interactions from bond "
          "breaking and forming. Vaporization costs tens of kilojoules per mole "
          "here while combustion changes thousands, and only combustion converts "
          "the alkane into different substances."),

 dict(q="A chemist writes that a certain process is physical even though bonds "
        "were broken during it. Which example from the course framework supports "
        "the possibility of such a case?",
      choices=[
        "The dissolution of a salt in water, which breaks ionic bonds while "
        "still being commonly treated as a physical process",
        "The combustion of a hydrocarbon, which is treated as physical because "
        "the products are gases",
        "The evaporation of water, which is treated as physical because O-H "
        "bonds break as the molecules leave the liquid",
        "The rusting of iron, which is treated as physical because the iron can "
        "be recovered by scraping",
        "The electrolysis of water, which is treated as physical because the "
        "total mass does not change"],
      ans=0,
      why="EK 4.4.A.2 states that sometimes physical processes involve the "
          "breaking of chemical bonds and offers exactly this example: "
          "dissolving a salt breaks ionic bonds while forming ion-dipole "
          "interactions between the ions and the solvent."),

 dict(q="Solid ammonium chloride is heated and a white deposit forms on a cool "
        "surface higher in the tube. Testing shows the deposit is ammonium "
        "chloride, but a nearby probe detects both NH3 and HCl in the hot region. "
        "How is this best described?",
      choices=[
        "Bonds are broken to give NH3 and HCl on heating and re-formed when the "
        "gases cool, so a chemical process occurs even though the starting solid "
        "reappears",
        "Only intermolecular interactions change, because the same solid appears "
        "at the end as at the start",
        "The solid melts and then freezes on the cool surface, so nothing but a "
        "phase change has taken place",
        "The ammonium chloride is oxidized in the hot region and reduced again "
        "on the cool surface, gaining mass overall",
        "Nothing can be concluded, because a substance that reappears unchanged "
        "cannot have undergone any process"],
      ans=0,
      why="EK 4.4.A.1 classifies by whether chemical bonds are broken or formed, "
          "not by whether the starting material reappears. Detecting NH3 and HCl "
          "shows the bond holding the proton to the chloride was broken, and "
          "re-forming it on cooling is a second bond-forming step."),
]
