# AP BIOLOGY 1.1 Structure of Water and Hydrogen Bonding
# CED effective Fall 2025, Unit 1 Chemistry of Life. Big Idea 4 Systems Interactions.
# Learning objective 1.1.A: explain how the properties of water that result from its
# polarity and hydrogen bonding affect its biological function.
# Suggested skill 2.A, describe characteristics of visual representations.
#
# Essential knowledge relied on, in the framework's own words:
#   1.1.A.1    Living systems depend on the properties of water to sustain life.
#     i.       Water has polarity, because of the formation of polar covalent bonds
#              between hydrogen and oxygen within water molecules. This polarity
#              contributes to hydrogen bonding between and within biological molecules.
#     ii.      Water has a high specific heat capacity, which allows for the
#              maintenance of homeostatic body temperature within living organisms.
#     iii.     Water has a high heat of vaporization, which allows for the evaporative
#              cooling of the surrounding environment. In living organisms, this
#              property allows for body temperature to be maintained.
#   1.1.A.2    The hydrogen bonds between adjacent polar water molecules result in
#              cohesion, adhesion, and surface tension.
#
# ON THE THREE NAMED CONSEQUENCES. EK 1.1.A.2 names cohesion, adhesion and surface
# tension as three separate results of hydrogen bonding between adjacent water
# molecules and does not define them. Where an item turns on which of the three is at
# work, the verifier's claim says so explicitly; the definitional content presupposed
# is only that cohesion is water holding to water and adhesion is water holding to
# another surface, which is what naming them as distinct results requires.
#
# ON THE DATA. Every table is labelled in the stem and every keyed conclusion is
# recoverable from the table alone and is recomputed in verify_b1_1.py. Nothing here
# asks a student to remember a measured value.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. The CED's own sample questions print four.
# No LaTeX: export_units.py does not typeset Biology.
TOPIC = ("1.1", "Structure of Water and Hydrogen Bonding", 1)

_T_SPECIFIC_HEAT = dict(
    headers=["Substance", "Specific heat capacity (joules per gram per degree Celsius)"],
    rows=[["Water", "4.18"],
          ["Ethanol", "2.44"],
          ["Olive oil", "1.97"],
          ["Dry sand", "0.83"],
          ["Iron", "0.45"]])

_T_VAPORIZATION = dict(
    headers=["Liquid", "Heat of vaporization (joules per gram)"],
    rows=[["Water", "2,260"],
          ["Ethanol", "841"],
          ["Acetone", "518"],
          ["Diethyl ether", "351"],
          ["Chloroform", "247"]])

_T_SHORE = dict(
    headers=["Site", "Lowest air temperature recorded in one day (degrees Celsius)",
             "Highest air temperature recorded in the same day (degrees Celsius)"],
    rows=[["Lakeshore station", "14", "22"],
          ["Station 40 km inland", "6", "34"]])

_T_SWEAT = dict(
    headers=["Treatment", "Water lost from the skin in one hour (grams)",
             "Core body temperature after one hour (degrees Celsius)"],
    rows=[["Sweating allowed", "480", "37.2"],
          ["Sweating blocked", "35", "40.1"]])

_T_TUBES = dict(
    headers=["Tube", "Inside diameter (millimeters)",
             "Height water rose inside the tube (millimeters)"],
    rows=[["Tube 1", "0.5", "60"],
          ["Tube 2", "1.0", "30"],
          ["Tube 3", "2.0", "15"]])

_T_SURFACE = dict(
    headers=["Liquid at 20 degrees Celsius", "Surface tension (millinewtons per meter)"],
    rows=[["Water", "72.8"],
          ["Glycerol", "63.4"],
          ["Ethanol", "22.4"],
          ["Hexane", "18.4"]])

QUESTIONS = [

 dict(q="A water molecule carries a partial negative charge near its oxygen atom and "
        "partial positive charges near its hydrogen atoms. Which of the following best "
        "explains the origin of this arrangement of charge?",
      choices=[
        "Hydrogen and oxygen form polar covalent bonds within the molecule, and the "
        "shared electrons are held more tightly by oxygen than by hydrogen.",
        "Hydrogen and oxygen are joined by ionic bonds, so each atom in the molecule "
        "carries a whole unit of charge.",
        "A hydrogen bond forms between the oxygen atom and each hydrogen atom inside "
        "the same molecule, separating charge across the molecule.",
        "The molecule loses one electron to the surrounding solution whenever it "
        "dissolves a solute, leaving it charged overall.",
        "Electrons are shared exactly evenly, and the bent shape alone produces the "
        "separation of charge."],
      ans=0,
      why="EK 1.1.A.1 i states that water has polarity because of the formation of polar "
          "covalent bonds between hydrogen and oxygen within water molecules. The bonds "
          "are covalent, so the electrons are shared, and polar, so they are shared "
          "unequally. Ionic bonding and internal hydrogen bonding are both the wrong "
          "kind of bond, and even sharing would leave no partial charges to explain."),

 dict(q="The polarity of water contributes most directly to which of the following, "
        "according to the course framework?",
      choices=[
        "Hydrogen bonding between biological molecules and within them",
        "The formation of covalent bonds between carbon atoms in a hydrocarbon chain",
        "The transfer of electrons from one molecule to another during a redox reaction",
        "The removal of a hydroxyl group from a monomer during polymerization",
        "The sharing of electron pairs that holds a peptide chain together"],
      ans=0,
      why="EK 1.1.A.1 i ends by stating that the polarity of water contributes to "
          "hydrogen bonding between and within biological molecules. The other four "
          "options name covalent bonding events, which do not depend on water being "
          "polar."),

 dict(q="A student measures the specific heat capacity of several substances and "
        "records the values in the table. Equal masses of each substance absorb the "
        "same quantity of heat. Which substance will show the smallest rise in "
        "temperature?",
      table=_T_SPECIFIC_HEAT,
      choices=["Water", "Ethanol", "Olive oil", "Dry sand", "Iron"],
      ans=0,
      why="Specific heat capacity is the heat needed to raise one gram by one degree, so "
          "for a fixed mass and a fixed quantity of heat the temperature rise is smallest "
          "for the largest capacity. Water's 4.18 is the largest value in the table. EK "
          "1.1.A.1 ii is the reason the framework cares about this property."),

 dict(q="Human cells continue to function while the air temperature outside the body "
        "swings widely over a single day. Which property of water named in the course "
        "framework most directly accounts for the stability of the internal temperature?",
      choices=[
        "Its high specific heat capacity, which resists a large temperature change for a "
        "given input of heat",
        "Its high heat of vaporization, which carries heat away only when liquid becomes "
        "gas",
        "Its cohesion, which holds adjacent water molecules to one another in a column",
        "Its adhesion, which holds water molecules to the walls of narrow vessels",
        "Its surface tension, which resists the deformation of a water surface"],
      ans=0,
      why="EK 1.1.A.1 ii ties the high specific heat capacity of water to the maintenance "
          "of homeostatic body temperature within living organisms. Heat of vaporization "
          "acts through evaporation and so applies where water is leaving the body, and "
          "the three properties of EK 1.1.A.2 concern how water holds together, not how "
          "it stores heat."),

 dict(q="Water evaporating from the surface of a leaf lowers the temperature of the "
        "leaf. Which property of water is responsible, and why does it have that effect?",
      choices=[
        "Its high heat of vaporization: a large quantity of heat must be absorbed for "
        "each gram of liquid that becomes vapor, and that heat leaves with the vapor.",
        "Its high specific heat capacity: the liquid remaining on the leaf stores heat "
        "and therefore cannot warm up.",
        "Its polarity: charged regions of the molecule repel one another and push heat "
        "outward from the leaf.",
        "Its surface tension: a taut surface film insulates the leaf from the warm air "
        "above it.",
        "Its adhesion: water molecules stick to the leaf and block sunlight from "
        "reaching the tissue underneath."],
      ans=0,
      why="EK 1.1.A.1 iii states that water has a high heat of vaporization, which allows "
          "for the evaporative cooling of the surrounding environment and, in living "
          "organisms, for body temperature to be maintained. Cooling depends on the heat "
          "that departs with the escaping molecules, not on the heat retained by the "
          "liquid left behind."),

 dict(q="The table gives the heat of vaporization of four liquids. A researcher wants "
        "the greatest amount of heat removed from a surface for each gram of liquid that "
        "evaporates from it. Which liquid should be chosen?",
      table=_T_VAPORIZATION,
      choices=["Water", "Ethanol", "Acetone", "Diethyl ether", "Chloroform"],
      ans=0,
      why="Heat of vaporization is the heat absorbed per gram converted from liquid to "
          "vapor, so the largest value removes the most heat per gram. Water's 2,260 is "
          "the largest of the four, which is what EK 1.1.A.1 iii means by calling water's "
          "heat of vaporization high."),

 dict(q="Cohesion, adhesion and surface tension are all listed by the course framework "
        "as consequences of the same underlying feature of liquid water. What is that "
        "feature?",
      choices=[
        "Hydrogen bonds forming between adjacent polar water molecules",
        "Covalent bonds forming between one water molecule and the next",
        "The high specific heat capacity of the liquid",
        "The ionization of a small fraction of the molecules into ions",
        "The absence of any attraction between neighboring molecules"],
      ans=0,
      why="EK 1.1.A.2 states that the hydrogen bonds between adjacent polar water "
          "molecules result in cohesion, adhesion, and surface tension. Hydrogen bonds "
          "form between molecules; the covalent bonds in water are inside each molecule "
          "and hold hydrogen to oxygen, which is EK 1.1.A.1 i."),

 dict(q="A small insect rests on the surface of a pond without breaking through it, even "
        "though the insect is denser than water. Which explanation is best supported by "
        "the course framework?",
      choices=[
        "Hydrogen bonds among the water molecules at the surface resist being pulled "
        "apart, producing surface tension.",
        "The insect is buoyed up because water has an unusually high specific heat "
        "capacity.",
        "Adhesion between the water and the air above it forms a solid film across the "
        "pond.",
        "Covalent bonds link the surface molecules into a continuous sheet.",
        "Evaporation from the pond pushes upward on the insect with enough force to "
        "support it."],
      ans=0,
      why="EK 1.1.A.2 names surface tension as one of the three results of hydrogen "
          "bonding between adjacent polar water molecules. Specific heat capacity governs "
          "temperature change, not mechanical resistance at a surface, and covalent bonds "
          "do not form between separate water molecules."),

 dict(q="Water rises inside a very narrow glass tube dipped into a dish of water, and "
        "the column of water stays intact as it rises. Which pair of properties best "
        "accounts for this observation?",
      choices=[
        "Adhesion pulls water up along the glass, and cohesion drags the molecules "
        "beneath it along.",
        "Cohesion pulls water up along the glass, and surface tension pushes the column "
        "from below.",
        "Specific heat capacity holds the column together, and adhesion warms the glass.",
        "Heat of vaporization lifts the column, and cohesion prevents it from boiling.",
        "Polar covalent bonds within each molecule stretch, and the molecules lengthen "
        "up the tube."],
      ans=0,
      why="EK 1.1.A.2 names both cohesion and adhesion as results of hydrogen bonding. "
          "Adhesion is the attraction of water to another surface, so it is what acts "
          "between water and glass; cohesion is the attraction of water to water, so it "
          "is what keeps the rising column continuous. The other options assign the two "
          "the wrong roles or invoke thermal properties for a mechanical effect."),

 dict(q="The table records how far water rose inside three vertical glass tubes of "
        "different bore placed in the same dish. Which statement is supported by the "
        "data?",
      table=_T_TUBES,
      choices=[
        "The narrower the tube, the higher the water rose.",
        "The wider the tube, the higher the water rose.",
        "The height the water rose was the same in every tube.",
        "Water rose only in the tube with the largest inside diameter.",
        "The height the water rose was proportional to the inside diameter of the tube."],
      ans=0,
      why="Read straight off the table: as the inside diameter falls from 2.0 to 1.0 to "
          "0.5 millimeters, the height rises from 15 to 30 to 60 millimeters. The trend "
          "is the reverse of proportional, so the option naming proportionality with "
          "diameter is false on the same numbers."),

 dict(q="Suppose a molecule the same size as water were built so that its two bonds to "
        "hydrogen were nonpolar and it therefore had no partial charges. Which of the "
        "following would be the most direct consequence for a cell filled with that "
        "liquid instead of water?",
      choices=[
        "Hydrogen bonds would not form between the molecules, so cohesion, adhesion and "
        "surface tension would all be lost.",
        "The molecules would form covalent bonds with one another instead, and the liquid "
        "would solidify.",
        "The liquid would gain a much higher specific heat capacity than water has.",
        "The molecules would dissolve nonpolar substances less readily than water does.",
        "Evaporation would become impossible because no molecule could leave the "
        "surface."],
      ans=0,
      why="EK 1.1.A.1 i makes polarity the source of hydrogen bonding, and EK 1.1.A.2 "
          "makes hydrogen bonding between adjacent molecules the source of all three of "
          "cohesion, adhesion and surface tension. Removing the polarity removes the "
          "cause of all three at once."),

 dict(q="The table shows the coldest and warmest air temperatures recorded on the same "
        "day at a lakeshore station and at a station 40 kilometers inland. Which "
        "conclusion is best supported?",
      table=_T_SHORE,
      choices=[
        "The daily temperature range at the lakeshore was smaller than the range inland.",
        "The daily temperature range at the lakeshore was larger than the range inland.",
        "The two stations recorded the same daily temperature range.",
        "The inland station never grew warmer than the lakeshore station.",
        "The lakeshore station recorded the lower of the two daily minimum "
        "temperatures."],
      ans=0,
      why="The lakeshore range is 22 minus 14, which is 8 degrees; the inland range is 34 "
          "minus 6, which is 28 degrees. A large mass of water resists temperature change "
          "for a given input of heat, which is the property EK 1.1.A.1 ii names, and the "
          "remaining options are false against the same four numbers."),

 dict(q="In an experiment, the sweat glands on one group of animals were blocked while "
        "another group sweated normally; both groups were then held in a warm chamber for "
        "one hour. The results are in the table. Which statement is best supported?",
      table=_T_SWEAT,
      choices=[
        "Losing water from the skin was associated with a lower core body temperature at "
        "the end of the hour.",
        "Losing water from the skin was associated with a higher core body temperature at "
        "the end of the hour.",
        "Water loss from the skin had no measurable association with core body "
        "temperature.",
        "The animals that sweated normally lost less water than the animals whose "
        "sweating was blocked.",
        "Both groups ended the hour at the same core body temperature."],
      ans=0,
      why="The group that lost 480 grams of water ended at 37.2 degrees and the group "
          "that lost 35 grams ended at 40.1 degrees, so more water lost went with the "
          "cooler body. This is the effect EK 1.1.A.1 iii attributes to the high heat of "
          "vaporization of water, and the four other readings contradict the table."),

 dict(q="Water is drawn upward through the vessels of a tall tree in an unbroken column. "
        "Which explanation relies only on properties the course framework attributes to "
        "hydrogen bonding between water molecules?",
      choices=[
        "Water molecules hold to one another and to the vessel walls, so a column pulled "
        "from the top does not separate.",
        "Water molecules store heat as they rise, and the stored heat lifts them further.",
        "Water molecules repel one another and so spread upward into the empty vessel.",
        "Covalent bonds between neighboring water molecules form a rigid rod inside each "
        "vessel.",
        "Vapor pressure inside the vessel pushes a column of liquid water ahead of it."],
      ans=0,
      why="EK 1.1.A.2 attributes cohesion and adhesion to hydrogen bonds between adjacent "
          "polar water molecules, and those are the two attractions the keyed explanation "
          "uses. The others invoke heat storage, repulsion, or intermolecular covalent "
          "bonds, none of which the framework attributes to water."),

 dict(q="Using the specific heat capacities in the table, how much heat is required to "
        "raise the temperature of 100 grams of water by 10 degrees Celsius?",
      table=_T_SPECIFIC_HEAT,
      choices=[
        "About 4,180 joules",
        "About 418 joules",
        "About 41.8 joules",
        "About 830 joules",
        "About 450 joules"],
      ans=0,
      why="Specific heat capacity multiplied by mass and by the temperature change gives "
          "the heat required: 4.18 times 100 times 10. The distractors are the same "
          "product off by a factor of ten or a hundred, or the product formed with the "
          "wrong substance's capacity from the same table."),

 dict(q="Two students disagree about hydrogen bonding in liquid water. One says the "
        "hydrogen bonds hold each molecule's own atoms together; the other says they form "
        "between separate molecules. Which response is correct, and on what grounds?",
      choices=[
        "The second student is correct, because within a molecule hydrogen and oxygen are "
        "held by covalent bonds and hydrogen bonds form between one molecule and its "
        "neighbors.",
        "The first student is correct, because the covalent bonds in water hold "
        "neighboring molecules together in the liquid.",
        "Both are correct, because hydrogen bonds and covalent bonds are two names for "
        "the same attraction.",
        "Neither is correct, because liquid water contains no bonds of any kind between "
        "its molecules.",
        "The first student is correct, because a molecule cannot attract anything outside "
        "itself."],
      ans=0,
      why="EK 1.1.A.1 i places the polar covalent bonds between hydrogen and oxygen "
          "within water molecules, and EK 1.1.A.2 places the hydrogen bonds between "
          "adjacent water molecules. The two kinds of bond therefore act at different "
          "levels and are not interchangeable."),

 dict(q="The table lists the surface tension of four liquids at the same temperature. "
        "Which statement is supported by the values shown?",
      table=_T_SURFACE,
      choices=[
        "Water has a higher surface tension than any other liquid in the table.",
        "Ethanol has a higher surface tension than water.",
        "Hexane and water have nearly equal surface tensions.",
        "The surface tension of glycerol is more than twice that of water.",
        "Every liquid in the table has a surface tension above 50 millinewtons per "
        "meter."],
      ans=0,
      why="Water's 72.8 is the largest of the four values, so the keyed statement holds "
          "and the ethanol comparison fails. Hexane's 18.4 is roughly a quarter of "
          "water's, glycerol's 63.4 is less than water's rather than more than twice it, "
          "and two of the four values fall below 50."),

 dict(q="Which observation would provide the strongest evidence that a newly discovered "
        "liquid forms hydrogen bonds between its molecules in the way water does?",
      choices=[
        "It has an unusually high surface tension and an unusually high heat of "
        "vaporization for a molecule of its size.",
        "It is a clear, colorless liquid at room temperature.",
        "It conducts electricity when a salt is dissolved in it.",
        "Its molecules contain a hydrogen atom bonded to a carbon atom.",
        "It expands slightly when it is heated."],
      ans=0,
      why="Attraction between neighboring molecules is what must be pulled apart to "
          "stretch a surface or to send a molecule into the vapor, so unusually large "
          "values of both quantities point to strong intermolecular attraction. The other "
          "observations are shared by many liquids that form no hydrogen bonds at all."),

 dict(q="A cell's cytosol is largely water. Which of the following best states why the "
        "course framework treats the properties of water as foundational to living "
        "systems rather than as an incidental fact of chemistry?",
      choices=[
        "Living systems depend on those properties to sustain life, so processes such as "
        "temperature regulation and molecular interaction rest on them.",
        "Water is the only compound on Earth that exists as a liquid.",
        "Water supplies the carbon skeletons from which macromolecules are assembled.",
        "Water is chemically inert and therefore never participates in cellular "
        "reactions.",
        "Water is the only molecule capable of forming covalent bonds with hydrogen."],
      ans=0,
      why="EK 1.1.A.1 opens by stating that living systems depend on the properties of "
          "water to sustain life, and its three sub-points name the properties. Water is "
          "not the source of carbon skeletons, and EK 1.3.A.1 shows it is a reactant in "
          "hydrolysis rather than inert."),

 dict(q="Beads of water on a waxed surface pull themselves into rounded drops rather "
        "than spreading out into a film. Which combination of attractions best explains "
        "the shape of the drops?",
      choices=[
        "Attraction of water to water is strong, and attraction of water to the waxed "
        "surface is weak.",
        "Attraction of water to water is weak, and attraction of water to the waxed "
        "surface is strong.",
        "Both attractions are weak, so the water has no tendency to gather at all.",
        "Both attractions are strong, so the water spreads into a thin, even film.",
        "Neither attraction matters, because drop shape is set by the specific heat "
        "capacity of the liquid."],
      ans=0,
      why="EK 1.1.A.2 makes both cohesion, the attraction of water to water, and "
          "adhesion, the attraction of water to a surface, results of hydrogen bonding. "
          "Beading is what happens when the first outweighs the second; a strong "
          "attraction to the surface would spread the drop instead."),

 dict(q="Ocean water absorbs a large amount of solar energy during the day yet its "
        "temperature changes only slightly. Which quantity is directly responsible, and "
        "what does a large value of it mean?",
      choices=[
        "Specific heat capacity: a large value means a large amount of heat is needed to "
        "raise each gram by one degree.",
        "Heat of vaporization: a large value means a large amount of heat is needed to "
        "raise each gram by one degree.",
        "Surface tension: a large value means the surface resists being warmed by "
        "sunlight.",
        "Cohesion: a large value means each molecule shields its neighbors from "
        "radiation.",
        "Polarity: a large value means the molecule reflects most of the light that "
        "strikes it."],
      ans=0,
      why="EK 1.1.A.1 ii names the high specific heat capacity of water as the property "
          "behind resistance to temperature change. The second option attaches the "
          "correct definition to the wrong quantity, since heat of vaporization is heat "
          "per gram converted to vapor rather than heat per degree."),

 dict(q="Which experimental design would best test the claim that evaporation of water "
        "from a surface lowers the temperature of that surface?",
      choices=[
        "Record the temperature of two identical damp cloths over time, placing one in "
        "moving dry air and the other in still air saturated with water vapor.",
        "Record the temperature of a dry cloth and a damp cloth left in two rooms held at "
        "different air temperatures.",
        "Weigh a damp cloth every minute and report how much mass it loses.",
        "Compare the temperature of a damp cloth with the temperature of the water used "
        "to dampen it before the experiment begins.",
        "Measure the specific heat capacity of the water used to dampen the cloth."],
      ans=0,
      why="The claim is about the effect of evaporation, so the treatments must differ in "
          "how readily water can evaporate while everything else is held constant. "
          "Saturated still air suppresses net evaporation and dry moving air promotes it. "
          "The other designs vary the wrong factor or measure mass or capacity rather "
          "than temperature."),

 dict(q="Ice floats on liquid water because the molecules in ice are held in an open "
        "arrangement by bonds between neighboring molecules. Which type of bond holds "
        "that arrangement together?",
      choices=[
        "Hydrogen bonds between adjacent polar water molecules",
        "Polar covalent bonds between the oxygen of one molecule and the hydrogen of the "
        "next",
        "Ionic bonds between hydroxide ions and hydrogen ions",
        "Peptide bonds of the kind found in a polypeptide backbone",
        "Nonpolar interactions between the hydrocarbon regions of the molecules"],
      ans=0,
      why="EK 1.1.A.2 identifies the attraction between adjacent polar water molecules as "
          "hydrogen bonding. The polar covalent bonds of EK 1.1.A.1 i lie inside a single "
          "molecule, peptide bonds belong to proteins under EK 1.7.A.1, and water has no "
          "hydrocarbon region."),

 dict(q="A researcher reports that a protein folds so that its charged side groups face "
        "the surrounding cytosol. Which property of water makes that arrangement "
        "favorable?",
      choices=[
        "Water is polar, so it can form hydrogen bonds with charged and polar groups on "
        "the protein.",
        "Water has a high specific heat capacity, so it holds the protein at a constant "
        "temperature.",
        "Water has a high heat of vaporization, so it evaporates away from charged "
        "groups.",
        "Water has high surface tension, so it presses charged groups toward the "
        "outside.",
        "Water is nonpolar, so it mixes freely with the charged groups on the protein."],
      ans=0,
      why="EK 1.1.A.1 i states that the polarity of water contributes to hydrogen bonding "
          "between and within biological molecules, which is the interaction the exposed "
          "charged groups make with the surrounding water. The thermal properties are "
          "real but do not explain where a side group sits, and water is not nonpolar."),

 dict(q="Which pair of statements correctly separates the property of water responsible "
        "for buffering a change in temperature from the property responsible for cooling "
        "by evaporation?",
      choices=[
        "Specific heat capacity buffers a change in temperature; heat of vaporization "
        "cools by evaporation.",
        "Heat of vaporization buffers a change in temperature; specific heat capacity "
        "cools by evaporation.",
        "Cohesion buffers a change in temperature; adhesion cools by evaporation.",
        "Surface tension buffers a change in temperature; polarity cools by "
        "evaporation.",
        "Polarity buffers a change in temperature; cohesion cools by evaporation."],
      ans=0,
      why="EK 1.1.A.1 ii assigns the maintenance of homeostatic body temperature to the "
          "high specific heat capacity of water, and EK 1.1.A.1 iii assigns evaporative "
          "cooling to the high heat of vaporization. The remaining options either swap "
          "the two or substitute the mechanical properties of EK 1.1.A.2."),

 dict(q="Referring again to the specific heat capacities in the table, a 200 gram block "
        "of iron and 200 grams of water each absorb 8,360 joules of heat. Which statement "
        "about the resulting temperature changes is correct?",
      table=_T_SPECIFIC_HEAT,
      choices=[
        "The iron warms by about 93 degrees and the water by about 10 degrees.",
        "The iron warms by about 10 degrees and the water by about 93 degrees.",
        "Both warm by about 10 degrees, because the masses and heat inputs are equal.",
        "The iron warms by about 20 degrees and the water by about 5 degrees.",
        "Neither changes temperature, because the heat input is identical."],
      ans=0,
      why="Dividing the heat by the mass and by the specific heat capacity gives the "
          "temperature change. For water that is 8,360 over 200 times 4.18, which is 10 "
          "degrees; for iron it is 8,360 over 200 times 0.45, which is about 93 degrees. "
          "This is why EK 1.1.A.1 ii calls the capacity of water high."),

 dict(q="Which statement about hydrogen bonds in liquid water is most accurate?",
      choices=[
        "Each hydrogen bond is weaker than a covalent bond, but very many of them act "
        "together throughout the liquid.",
        "Each hydrogen bond is stronger than the covalent bond that holds a water "
        "molecule together.",
        "Hydrogen bonds form only when water freezes and are absent from the liquid.",
        "A hydrogen bond permanently joins two water molecules into a single larger "
        "molecule.",
        "Hydrogen bonds form between two oxygen atoms that have equal charges."],
      ans=0,
      why="EK 1.1.A.2 makes hydrogen bonds between adjacent water molecules the source of "
          "cohesion, adhesion and surface tension in the liquid, so they are present in "
          "the liquid and act collectively. If a hydrogen bond fused two molecules into "
          "one, the liquid would not be made of water molecules at all."),

 dict(q="Sulfur hexafluoride is a nonpolar molecule that forms no hydrogen bonds. Which "
        "prediction about a sample of it, compared with a sample of water of the same "
        "mass, is best supported by the course framework?",
      choices=[
        "It will show a lower surface tension than water does, because the attraction "
        "between its molecules is weaker.",
        "It will show a higher surface tension than water does, because nonpolar "
        "molecules pack more tightly.",
        "It will show the same surface tension as water, because surface tension depends "
        "only on mass.",
        "It will form hydrogen bonds with water but not with itself.",
        "It will have a higher specific heat capacity than water, because it lacks "
        "hydrogen bonds."],
      ans=0,
      why="EK 1.1.A.2 traces surface tension to hydrogen bonds between adjacent polar "
          "molecules, so a liquid whose molecules form no such bonds has less "
          "intermolecular attraction to overcome at its surface. Nothing in the framework "
          "makes surface tension a function of mass, and a molecule that is nonpolar "
          "throughout offers no partial charge for a hydrogen bond."),

 dict(q="A diagram of liquid water shows dashed lines drawn between the hydrogen atom of "
        "one molecule and the oxygen atom of a neighboring molecule, and solid lines "
        "drawn between the hydrogen and oxygen atoms inside each molecule. What do the "
        "two kinds of line most likely represent?",
      choices=[
        "Dashed lines are hydrogen bonds between molecules and solid lines are polar "
        "covalent bonds within a molecule.",
        "Dashed lines are polar covalent bonds within a molecule and solid lines are "
        "hydrogen bonds between molecules.",
        "Both kinds of line represent hydrogen bonds, drawn differently only for "
        "clarity.",
        "Dashed lines represent ionic bonds and solid lines represent hydrogen bonds.",
        "Dashed lines represent the path a molecule travels and solid lines represent "
        "bonds."],
      ans=0,
      why="EK 1.1.A.1 i places polar covalent bonds inside the molecule, between its own "
          "hydrogen and oxygen atoms, and EK 1.1.A.2 places hydrogen bonds between "
          "adjacent molecules. The lines described match that division, with the weaker "
          "intermolecular attraction conventionally drawn dashed."),

 dict(q="A student claims that because water has a high specific heat capacity, a lake "
        "can absorb heat without ever changing temperature at all. What is the best "
        "correction to this claim?",
      choices=[
        "A high capacity means a large input of heat is needed for each degree of change, "
        "not that no change occurs.",
        "A high capacity means the lake will change temperature faster than the "
        "surrounding land does.",
        "A high capacity applies only to water vapor, so it says nothing about a lake.",
        "A high capacity means heat cannot enter the lake in the first place.",
        "A high capacity means the temperature of the lake falls whenever heat is added "
        "to it."],
      ans=0,
      why="Specific heat capacity is heat per gram per degree of temperature change, so a "
          "large value slows the change rather than abolishing it. The framework claims "
          "in EK 1.1.A.1 ii only that the property allows homeostatic body temperature to "
          "be maintained, which is a matter of degree."),
]
