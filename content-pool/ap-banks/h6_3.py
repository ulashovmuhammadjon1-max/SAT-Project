# AP CHEMISTRY 6.3 Heat Transfer and Thermal Equilibrium
# CED effective Fall 2024, Unit 6 Thermochemistry.
# Learning objective 6.3.A: explain the relationship between the transfer of thermal
# energy and molecular collisions. Suggested skill 6.E, provide reasoning to justify a
# claim using connections between particulate and macroscopic scales or levels.
#
# Essential knowledge relied on, in the framework's own words:
#   6.3.A.1  The particles in a warmer body have a greater average kinetic energy than
#            those in a cooler body.
#   6.3.A.2  Collisions between particles in thermal contact can result in the transfer of
#            energy. This process is called "heat transfer," "heat exchange," or "transfer
#            of energy as heat."
#   6.3.A.3  Eventually, thermal equilibrium is reached as the particles continue to
#            collide. At thermal equilibrium, the average kinetic energy of both bodies is
#            the same, and hence, their temperatures are the same.
#
# THE SKILL IS THE PARTICULATE-TO-MACROSCOPIC LINK, which is what suggested skill 6.E asks
# for and what the three statements are built to support: a thermometer reading is a
# macroscopic fact, an average kinetic energy is a particulate one, and EK 6.3.A.1 and
# 6.3.A.3 are the bridge. So the items keep both ends in view rather than settling for one.
#
# THE WORD "AVERAGE" IS LOAD-BEARING AND IS THE TRAP IN THIS TOPIC. EK 6.3.A.3 equates the
# AVERAGE KINETIC ENERGY of the two bodies at thermal equilibrium, and hence their
# temperatures. It does NOT equate their total energies, and a large cool body can hold far
# more energy in total than a small warm one. No key here says otherwise, and
# verify_h6_3.py asserts it: any keyed choice on an equilibrium item that claims an
# equality must be claiming it of the average kinetic energy or of the temperature, never
# of a total.
#
# THE OTHER THING EK 6.3.A.3 SAYS AND IS EASILY DROPPED: the particles CONTINUE TO COLLIDE
# at equilibrium. Equilibrium is the absence of a net transfer, not the absence of
# collisions, and item 7 and item 21 are there because that is worth a question of its own.
#
# THE DIRECTION. The framework does not state in one sentence which way energy goes, so no
# key here asserts it as a bare fact. It is derived where it is used: EK 6.3.A.1 gives the
# warmer body the greater average kinetic energy and EK 6.3.A.3 requires the two to finish
# equal, so the warmer must fall and the cooler must rise. Every key that names a direction
# names that reason with it, and verify_h6_3.py checks both clauses are present.
#
# SCOPE. 6.1 owns the words endothermic and exothermic and NOT ONE appears here, in a stem,
# a key or a why -- the two topics would otherwise write the same question. 6.2 owns the
# energy diagram. 6.4 owns q = mc(delta T), the specific heat capacity and the calorimeter,
# so no item here computes a final temperature or a quantity of energy; where a final
# temperature appears it is a MEASURED value in a table, and the questions asked of it are
# about direction and about what equilibrium means. verify_h6_3.py asserts all of that.
#
# NOTATION. export_units.py does not typeset Chemistry. Temperatures are plain numbers with
# "degrees Celsius" written out, because a raw degree glyph reaches a student raw.
TOPIC = ("6.3", "Heat Transfer and Thermal Equilibrium", 6)

_T_CONTACT = dict(
    headers=["Pair", "Temperature of body 1 (degrees Celsius)",
             "Temperature of body 2 (degrees Celsius)"],
    rows=[["Pair 1", "85", "20"],
          ["Pair 2", "15", "40"],
          ["Pair 3", "30", "30"],
          ["Pair 4", "5", "-10"],
          ["Pair 5", "60", "62"]])

_T_KE = dict(
    headers=["Sample", "Temperature (degrees Celsius)"],
    rows=[["Sample K", "120"],
          ["Sample L", "25"],
          ["Sample M", "-40"],
          ["Sample N", "78"],
          ["Sample P", "25"]])

_T_EQUIL = dict(
    headers=["Trial", "Initial temperature of the metal block (degrees Celsius)",
             "Initial temperature of the water (degrees Celsius)",
             "Final temperature of both (degrees Celsius)"],
    rows=[["Trial 1", "95", "20", "28"],
          ["Trial 2", "80", "20", "24"],
          ["Trial 3", "20", "20", "20"],
          ["Trial 4", "60", "55", "56"],
          ["Trial 5", "10", "45", "41"]])

QUESTIONS = [

 dict(q="How do the particles in a warmer body compare with those in a cooler body, "
        "according to the framework?",
      choices=[
        "They have a greater average kinetic energy",
        "They have a smaller average kinetic energy",
        "They are greater in number",
        "They are larger in size",
        "They are closer together"],
      ans=0,
      why="EK 6.3.A.1 states that the particles in a warmer body have a greater average "
          "kinetic energy than those in a cooler body. Nothing in the statement concerns "
          "how many particles there are or how large they are."),

 dict(q="What does the framework say can result from collisions between particles in "
        "thermal contact?",
      choices=[
        "The transfer of energy",
        "The transfer of particles from one body to the other",
        "A change in the number of particles present",
        "A chemical reaction between the two bodies",
        "A permanent increase in the energy of both bodies"],
      ans=0,
      why="EK 6.3.A.2 states that collisions between particles in thermal contact can "
          "result in the transfer of energy. It is energy that moves between the bodies, "
          "not matter."),

 dict(q="Which three names does the framework give to the process by which colliding "
        "particles in thermal contact transfer energy?",
      choices=[
        "Heat transfer, heat exchange, and transfer of energy as heat",
        "Heat transfer, thermal expansion, and transfer of energy as work",
        "Heat exchange, thermal conduction, and radiation",
        "Transfer of energy as heat, transfer of energy as work, and convection",
        "Thermal equilibrium, heat capacity, and heat exchange"],
      ans=0,
      why="EK 6.3.A.2 gives exactly these three names to the process: heat transfer, heat "
          "exchange, or transfer of energy as heat. The other terms are not names the "
          "framework gives it here."),

 dict(q="Two bodies at different temperatures are left in thermal contact. What does the "
        "framework say is eventually reached?",
      choices=[
        "Thermal equilibrium",
        "A state in which one body has lost all of its energy",
        "A state in which the particles have stopped moving",
        "A chemical equilibrium between the two bodies",
        "A state in which the two bodies have equal masses"],
      ans=0,
      why="EK 6.3.A.3 states that eventually thermal equilibrium is reached as the "
          "particles continue to collide. Neither body is emptied of energy and no "
          "chemical change is involved."),

 dict(q="At thermal equilibrium, what does the framework say is the same for both bodies?",
      choices=[
        "The average kinetic energy of their particles, and hence their temperatures",
        "The total energy each body holds, and hence their temperatures",
        "The number of particles each body contains",
        "The rate at which their particles collide with one another",
        "The mass of each body"],
      ans=0,
      why="EK 6.3.A.3 states that at thermal equilibrium the average kinetic energy of "
          "both bodies is the same, and hence their temperatures are the same. The "
          "statement equates an average, not a total."),

 dict(q="A small warm block reaches thermal equilibrium with a large tank of cooler "
        "water. Do the two now hold the same total amount of energy?",
      choices=[
        "Not necessarily; what the framework equates is the average kinetic energy of the "
        "particles, and hence the temperatures",
        "Yes; thermal equilibrium means the two bodies hold equal total energy",
        "Yes, provided neither body changes state during the process",
        "No; the smaller body must always hold the greater total energy",
        "It cannot be decided, since energy in a body cannot be compared at all"],
      ans=0,
      why="EK 6.3.A.3 equates the average kinetic energy of both bodies and hence their "
          "temperatures. A body made of far more particles can hold far more energy in "
          "total at the same average, so nothing in the statement makes the totals equal."),

 dict(q="Once two bodies have reached thermal equilibrium, have the collisions between "
        "their particles stopped?",
      choices=[
        "No, the particles continue to collide",
        "Yes, which is what makes the temperatures stop changing",
        "Yes, but only at the surface where the two bodies touch",
        "Only if the two bodies are separated again",
        "Only if both bodies are solids"],
      ans=0,
      why="EK 6.3.A.3 says thermal equilibrium is reached AS THE PARTICLES CONTINUE TO "
          "COLLIDE, so the collisions are what carries the system to equilibrium and they "
          "do not cease when it arrives."),

 dict(q="At the level of particles, how does energy get from one body to another that it "
        "is touching?",
      choices=[
        "Through collisions between the particles of the two bodies",
        "Through particles moving bodily from one to the other",
        "Through the two bodies exchanging equal masses",
        "Through a change in the size of the particles",
        "Through the particles of the cooler body ceasing to move"],
      ans=0,
      why="EK 6.3.A.2 states that collisions between particles in thermal contact can "
          "result in the transfer of energy, which is the particulate account suggested "
          "skill 6.E asks a student to connect to the macroscopic observation."),

 dict(q="A warmer body and a cooler body are placed in thermal contact. Which way does "
        "energy pass between them, and why?",
      choices=[
        "From the warmer to the cooler, because the warmer body's particles have the "
        "greater average kinetic energy and the two must finish equal",
        "From the cooler to the warmer, because the warmer body's particles have the "
        "greater average kinetic energy and the two must finish equal",
        "From the warmer to the cooler, because the cooler body's particles have the "
        "greater average kinetic energy",
        "In neither direction, because collisions transfer energy equally both ways",
        "In whichever direction the larger body determines"],
      ans=0,
      why="EK 6.3.A.1 gives the warmer body's particles the greater average kinetic "
          "energy and EK 6.3.A.3 requires the two averages to end the same, so the warmer "
          "body's average must fall and the cooler body's must rise."),

 dict(q="Five pairs of bodies were each placed in thermal contact. In which pair is the "
        "difference between the two average kinetic energies the greatest at the start?",
      table=_T_CONTACT,
      choices=[
        "Pair 1",
        "Pair 2",
        "Pair 4",
        "Pair 5",
        "Pair 3"],
      ans=0,
      why="EK 6.3.A.1 ties a body being warmer to its particles having the greater "
          "average kinetic energy, so the pair whose two measured temperatures are "
          "furthest apart is the pair whose averages differ by the most."),

 dict(q="Among those same five pairs, in which will there be no net transfer of energy "
        "between the two bodies?",
      table=_T_CONTACT,
      choices=[
        "Pair 3",
        "Pair 1",
        "Pair 2",
        "Pair 4",
        "Pair 5"],
      ans=0,
      why="EK 6.3.A.3 makes equal temperatures the mark of equal average kinetic "
          "energies, which is the condition of thermal equilibrium, so the pair that "
          "starts at one temperature has nothing left to transfer on balance."),

 dict(q="Among those same five pairs, in which will body 1 become warmer, starting from "
        "the largest difference in temperature?",
      table=_T_CONTACT,
      choices=[
        "Pair 2",
        "Pair 5",
        "Pair 1",
        "Pair 4",
        "Pair 3"],
      ans=0,
      why="EK 6.3.A.1 and EK 6.3.A.3 together send the transfer from the body with the "
          "greater average kinetic energy to the other, so body 1 rises where it is the "
          "cooler of the two, and the largest such gap is the answer."),

 dict(q="Among the pairs whose two bodies start at different temperatures, in which will "
        "thermal equilibrium be reached after the smallest change in either temperature?",
      table=_T_CONTACT,
      choices=[
        "Pair 5",
        "Pair 4",
        "Pair 2",
        "Pair 1",
        "Pair 3"],
      ans=0,
      why="EK 6.3.A.3 has the two temperatures finish the same, so the distance each must "
          "travel is set by how far apart they began; the smallest gap between two "
          "unequal measured temperatures needs the smallest change."),

 dict(q="Five samples of the same substance were held at the temperatures recorded. In "
        "which sample do the particles have the greatest average kinetic energy?",
      table=_T_KE,
      choices=[
        "Sample K",
        "Sample N",
        "Sample L",
        "Sample P",
        "Sample M"],
      ans=0,
      why="EK 6.3.A.1 states that the particles in a warmer body have a greater average "
          "kinetic energy than those in a cooler body, so the highest measured "
          "temperature marks the greatest average."),

 dict(q="Among those same five samples, in which do the particles have the smallest "
        "average kinetic energy?",
      table=_T_KE,
      choices=[
        "Sample M",
        "Sample L",
        "Sample P",
        "Sample N",
        "Sample K"],
      ans=0,
      why="EK 6.3.A.1 read the other way: the cooler body's particles have the smaller "
          "average kinetic energy, so the lowest measured temperature marks the smallest "
          "average."),

 dict(q="Which two of those samples have particles of equal average kinetic energy?",
      table=_T_KE,
      choices=[
        "Sample L and Sample P",
        "Sample K and Sample N",
        "Sample L and Sample M",
        "Sample M and Sample P",
        "Sample K and Sample L"],
      ans=0,
      why="EK 6.3.A.3 ties equal average kinetic energies to equal temperatures, so the "
          "two samples recorded at the same temperature are the pair whose averages "
          "agree."),

 dict(q="A metal block was dropped into water in five trials and the temperatures "
        "recorded. In which trial did energy pass from the water into the block?",
      table=_T_EQUIL,
      choices=[
        "Trial 5",
        "Trial 1",
        "Trial 2",
        "Trial 3",
        "Trial 4"],
      ans=0,
      why="EK 6.3.A.1 gives the warmer body's particles the greater average kinetic "
          "energy and EK 6.3.A.3 requires the two to finish equal, so the transfer runs "
          "into whichever body started colder, which in one trial is the block."),

 dict(q="Among those same five trials, in which was there no net transfer of energy "
        "between the block and the water?",
      table=_T_EQUIL,
      choices=[
        "Trial 3",
        "Trial 4",
        "Trial 5",
        "Trial 1",
        "Trial 2"],
      ans=0,
      why="EK 6.3.A.3 makes equal temperatures the mark of equal average kinetic "
          "energies, so the trial in which the block and the water were already at one "
          "temperature is the trial with nothing to transfer on balance."),

 dict(q="Among those same five trials, in which did the metal block cool by the most?",
      table=_T_EQUIL,
      choices=[
        "Trial 1",
        "Trial 2",
        "Trial 4",
        "Trial 3",
        "Trial 5"],
      ans=0,
      why="EK 6.3.A.3 has both bodies finish at one temperature, so the fall in the "
          "block's temperature is its measured starting value less the measured final "
          "value, and the largest such fall is the answer."),

 dict(q="In every one of the five trials the final temperature lies between the two "
        "starting temperatures. Which statement explains why it must?",
      table=_T_EQUIL,
      choices=[
        "Energy passes from the body with the greater average kinetic energy to the "
        "other, so the warmer falls and the cooler rises until the two meet",
        "The two bodies always finish at the ordinary average of their starting "
        "temperatures",
        "The water always fixes the final temperature, whatever the block began at",
        "Some energy is destroyed in the transfer, which limits how far either can move",
        "The block and the water exchange equal temperatures rather than energy"],
      ans=0,
      why="EK 6.3.A.1 gives the warmer body the greater average kinetic energy and EK "
          "6.3.A.3 has the two averages, and hence the two temperatures, finish the same, "
          "so each moves toward the other and the meeting point lies between them."),

 dict(q="Two bodies already at the same temperature are placed in thermal contact. What "
        "happens?",
      choices=[
        "Their particles go on colliding, but there is no net transfer, because their "
        "average kinetic energies are already equal",
        "Their particles stop colliding, because there is nothing left to transfer",
        "Energy passes from the larger body to the smaller until the larger cools",
        "Energy passes in both directions until one of them becomes warmer",
        "Nothing at all happens, because particles in contact only collide when the "
        "temperatures differ"],
      ans=0,
      why="EK 6.3.A.3 describes thermal equilibrium as the state in which the average "
          "kinetic energies are the same and says the particles continue to collide, so "
          "the collisions persist while the net transfer does not."),

 dict(q="A student writes that a body at 100 degrees Celsius contains more heat than the "
        "same body at 20 degrees Celsius. What is wrong with the wording?",
      choices=[
        "The framework uses heat for the transfer of energy between bodies, not for "
        "something a body contains",
        "Nothing, since heat is the ordinary name for the energy inside a body",
        "The two temperatures should have been given on a different scale",
        "A body at the higher temperature in fact contains less energy",
        "Heat may only be spoken of when a chemical change occurs"],
      ans=0,
      why="EK 6.3.A.2 attaches the names heat transfer, heat exchange and transfer of "
          "energy as heat to the PROCESS by which colliding particles pass energy between "
          "bodies, so heat in the framework names a transfer rather than a store."),

 dict(q="One body is found to be warmer than another. What follows about its particles?",
      choices=[
        "Their average kinetic energy is the greater of the two",
        "Their average kinetic energy is the smaller of the two",
        "There are more of them than in the cooler body",
        "They are travelling in more nearly the same direction",
        "They collide with one another less often"],
      ans=0,
      why="EK 6.3.A.1 states exactly this: the particles in a warmer body have a greater "
          "average kinetic energy than those in a cooler body. The comparison the "
          "framework licenses is of the average, not of the number."),

 dict(q="A small sample and a very large sample of the same substance are both at 25 "
        "degrees Celsius. How do the average kinetic energies of their particles compare?",
      choices=[
        "They are the same, because equal temperatures go with equal average kinetic "
        "energies",
        "The larger sample's is greater, because it contains more particles",
        "The smaller sample's is greater, because its particles are less crowded",
        "The larger sample's is greater, because it holds more energy in total",
        "They cannot be compared unless the two samples are in thermal contact"],
      ans=0,
      why="EK 6.3.A.3 pairs the same average kinetic energy with the same temperature, "
          "and EK 6.3.A.1 makes a difference in average kinetic energy show up as a "
          "difference in temperature, so equal temperatures leave the averages equal "
          "however much substance is present."),

 dict(q="Two bodies at different temperatures are put in thermal contact and separated "
        "again before thermal equilibrium is reached. What can be said about them?",
      choices=[
        "Their temperatures are closer together than they were, but not yet the same",
        "Their temperatures are unchanged, since equilibrium was not reached",
        "Their temperatures have crossed over, the cooler becoming the warmer",
        "Their average kinetic energies are now equal even though the temperatures are not",
        "Nothing can be said, since a transfer that is interrupted leaves no effect"],
      ans=0,
      why="EK 6.3.A.2 has the collisions transfer energy while the bodies are in contact, "
          "and EK 6.3.A.3 has that transfer carry the two averages toward one another, so "
          "an interrupted contact leaves them partway rather than untouched."),

 dict(q="A hot metal block is dropped into cooler water and both are found afterwards at "
        "28 degrees Celsius. What has happened at the level of particles?",
      choices=[
        "Collisions where the two meet passed energy from the block's particles to the "
        "water's until the two average kinetic energies matched",
        "Collisions where the two meet passed energy from the water's particles to the "
        "block's until the two average kinetic energies matched",
        "Particles of the block moved into the water, carrying their energy with them",
        "The block's particles stopped moving and the water's took up the motion",
        "The two sets of particles exchanged temperatures directly, without colliding"],
      ans=0,
      why="EK 6.3.A.2 makes collisions between particles in thermal contact the mechanism "
          "of the transfer, and EK 6.3.A.1 with EK 6.3.A.3 send it from the body with the "
          "greater average kinetic energy, the hotter block, to the cooler water."),

 dict(q="Why does the framework say thermal equilibrium is reached eventually rather than "
        "at once?",
      choices=[
        "Because the transfer happens through repeated collisions, which take time to "
        "bring the two averages together",
        "Because the two bodies must first be brought to the same mass",
        "Because energy travels only while the temperatures are far apart",
        "Because the particles must stop colliding before equilibrium can be reached",
        "Because the framework is describing a chemical change, which is always slow"],
      ans=0,
      why="EK 6.3.A.3 says thermal equilibrium is reached EVENTUALLY, AS THE PARTICLES "
          "CONTINUE TO COLLIDE, so the collisions of EK 6.3.A.2 are what carries the "
          "system there and it arrives over the course of many of them."),

 dict(q="The particles of body 1 are found to have a greater average kinetic energy than "
        "those of body 2. Which body is warmer, and which way will energy pass when the "
        "two are brought into contact?",
      choices=[
        "Body 1 is warmer, and energy will pass from body 1 to body 2",
        "Body 2 is warmer, and energy will pass from body 2 to body 1",
        "Body 1 is warmer, and energy will pass from body 2 to body 1",
        "Body 2 is warmer, and energy will pass from body 1 to body 2",
        "Neither is warmer, since average kinetic energy and temperature are unrelated"],
      ans=0,
      why="EK 6.3.A.1 makes the greater average kinetic energy the mark of the warmer "
          "body, and EK 6.3.A.3 requires the two averages to finish equal, so the greater "
          "one must fall, which means the transfer runs away from body 1."),

 dict(q="Suggested skill 6.E asks for a claim justified across the particulate and "
        "macroscopic levels. Which pairing does the framework supply for this topic?",
      choices=[
        "A thermometer reading is macroscopic, the average kinetic energy of the "
        "particles is particulate, and the framework ties one to the other",
        "A thermometer reading is particulate and the average kinetic energy is "
        "macroscopic",
        "Both a thermometer reading and an average kinetic energy are macroscopic "
        "quantities",
        "Both a thermometer reading and an average kinetic energy are particulate "
        "quantities",
        "The framework treats the two levels as unconnected in this topic"],
      ans=0,
      why="EK 6.3.A.1 and EK 6.3.A.3 both state the link directly: a warmer body is one "
          "whose particles have the greater average kinetic energy, and equal averages "
          "mean equal temperatures, which is the particulate-to-macroscopic connection "
          "the skill names."),

 dict(q="How does the framework account for the transfer of thermal energy between two "
        "bodies in contact?",
      choices=[
        "Through collisions between their particles, continuing until the two average "
        "kinetic energies are the same",
        "Through collisions between their particles, continuing until the two totals of "
        "energy are the same",
        "Through the warmer body giving up all of its particle motion to the cooler",
        "Through a direct exchange of temperature that requires no collisions",
        "Through the movement of particles from the warmer body into the cooler one"],
      ans=0,
      why="EK 6.3.A.2 supplies the collisions and EK 6.3.A.3 the endpoint, which is the "
          "same AVERAGE kinetic energy in both bodies and hence the same temperature; the "
          "framework equates averages rather than totals."),
]
