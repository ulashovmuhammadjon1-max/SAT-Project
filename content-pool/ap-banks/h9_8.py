# AP CHEMISTRY 9.8 Galvanic (Voltaic) and Electrolytic Cells
# CED effective Fall 2024, Unit 9 Thermodynamics and Electrochemistry.
# Learning objective 9.8.A: explain the relationship between the physical components of
# an electrochemical cell and the overall operational principles of the cell.
# Suggested skill 2.F, explain how modifications to an experimental procedure will alter
# results.
#
# Essential knowledge relied on, in the framework's own words:
#   9.8.A.1  Each component of an electrochemical cell (electrodes, solutions in the
#            half-cells, salt bridge, voltage/current measuring device) plays a specific
#            role in the overall functioning of the cell. The operational characteristics
#            of the cell (galvanic vs. electrolytic, direction of electron flow, reactions
#            occurring in each half-cell, change in electrode mass, evolution of a gas at
#            an electrode, ion flow through the salt bridge) can be described at both the
#            macroscopic and particulate levels.
#   9.8.A.2  Galvanic, sometimes called voltaic, cells involve a thermodynamically favored
#            reaction, whereas electrolytic cells involve a thermodynamically unfavored
#            reaction. Visual representations of galvanic and electrolytic cells are tools
#            of analysis to identify where half-reactions occur and in what direction
#            current flows.
#   9.8.A.3  For all electrochemical cells, oxidation occurs at the anode and reduction
#            occurs at the cathode.
#            Exclusion Statement: Labeling an electrode as positive or negative will not
#            be assessed on the AP Exam.
#
# Supporting statements used where the framework's own reasoning needs them:
#   EK 4.7.A.3  In a redox reaction, electrons are transferred from the species that is
#               oxidized to the species that is reduced -- which is what fixes the
#               direction of electron flow once EK 9.8.A.3 says where each half-reaction
#               happens.
#               (Its own exclusion statement bars "reducing agent" and "oxidizing agent",
#               so neither phrase appears below.)
#
# THE FIGURE PROBLEM, and how it is solved. EK 9.8.A.2 makes a VISUAL REPRESENTATION the
# characteristic tool of this topic and this bank cannot show one. Every cell below is
# therefore described in words -- the electrodes, the solutions, the salt bridge, the
# external wire, and what is observed at each electrode -- or carried as a table of those
# observations. No stem says "shown", "the diagram" or "the cell above", and
# verify_h9_8.py asserts that. A question that genuinely needed a picture is not written.
#
# THE SWAP GUARD. EK 9.8.A.3 is the easiest sentence in the unit to ship backwards, so
# every key is checked to contain no reversed pairing, and every anchor belonging to a
# pairing item must name BOTH the electrode and the process -- an anchor naming only one
# would match a key that had them the wrong way round.
#
# SCOPE. 9.9 owns the cell potential and 9.11 owns Faraday's law, so no item states a
# potential in volts or a quantity of charge. The exclusion statement attached to EK
# 9.8.A.3 is respected: nothing here labels an electrode positive or negative.
TOPIC = ("9.8", "Galvanic (Voltaic) and Electrolytic Cells", 9)

_T_ZNCU = dict(
    headers=["Half-cell", "Electrode", "Solution", "Observation after one hour"],
    rows=[["Half-cell 1", "zinc", "1.0 M zinc nitrate", "the electrode loses mass"],
          ["Half-cell 2", "copper", "1.0 M copper(II) nitrate",
           "the electrode gains mass"]])

_T_TYPES = dict(
    headers=["Cell", "How it operates"],
    rows=[["Cell 1", "it delivers energy to a small lamp with nothing else connected"],
          ["Cell 2", "it requires an external power supply before any change occurs"],
          ["Cell 3", "it uses an external power supply to reverse a battery reaction"],
          ["Cell 4", "it turns a small motor with nothing else connected"]])

QUESTIONS = [

 dict(q="Which components of an electrochemical cell does the framework say each play a "
        "specific role?",
      choices=[
        "The electrodes, the solutions in the half-cells, the salt bridge, and the voltage "
        "or current measuring device",
        "The electrodes and the wire connecting them, and nothing else",
        "The solutions in the half-cells and the temperature of the room",
        "The salt bridge and the mass of each electrode",
        "The electrodes, the solvent, and the pressure above the solutions"],
      ans=0,
      why="EK 9.8.A.1 lists exactly these components as each playing a specific role in the "
          "overall functioning of the cell: electrodes, solutions in the half-cells, salt "
          "bridge, and voltage or current measuring device."),

 dict(q="In an electrochemical cell, which process occurs at which electrode?",
      choices=[
        "Oxidation occurs at the anode and reduction occurs at the cathode",
        "Reduction occurs at the anode and oxidation occurs at the cathode",
        "Oxidation occurs at both electrodes at once",
        "Reduction occurs at both electrodes at once",
        "Which process occurs at which electrode depends on the type of cell"],
      ans=0,
      why="EK 9.8.A.3 states that for ALL electrochemical cells, oxidation occurs at the "
          "anode and reduction occurs at the cathode, so the pairing does not depend on "
          "whether the cell is galvanic or electrolytic."),

 dict(q="A student is told that reduction is taking place at one electrode of a cell. What "
        "is that electrode called, and what is happening at the other one?",
      choices=[
        "The cathode, where reduction occurs, while oxidation occurs at the anode",
        "The anode, where reduction occurs, while oxidation occurs at the cathode",
        "The cathode, where reduction occurs, while reduction also occurs at the anode",
        "The anode, where oxidation occurs, while reduction occurs at the cathode",
        "It cannot be named without knowing whether the cell is galvanic"],
      ans=0,
      why="EK 9.8.A.3 assigns reduction to the cathode and oxidation to the anode in all "
          "electrochemical cells, so naming one electrode by the process occurring there "
          "fixes the other. The option that names the anode correctly does not answer the "
          "question asked, which is about the reduction electrode."),

 dict(q="What kind of reaction does a galvanic cell involve?",
      choices=[
        "A thermodynamically favored reaction",
        "A thermodynamically unfavored reaction",
        "A reaction whose free energy change is exactly zero",
        "A reaction that occurs only when an external supply drives it",
        "A reaction in which no electrons are transferred"],
      ans=0,
      why="EK 9.8.A.2 states that galvanic, sometimes called voltaic, cells involve a "
          "thermodynamically favored reaction, whereas electrolytic cells involve a "
          "thermodynamically unfavored one."),

 dict(q="What kind of reaction does an electrolytic cell involve?",
      choices=[
        "A thermodynamically unfavored reaction",
        "A thermodynamically favored reaction",
        "A reaction whose free energy change is exactly zero",
        "A reaction that requires no transfer of electrons",
        "A reaction that is favored only above room temperature"],
      ans=0,
      why="EK 9.8.A.2 states that electrolytic cells involve a thermodynamically unfavored "
          "reaction, which is why EK 9.7.A.1 lists electrical energy driving an "
          "electrolytic cell among its examples of an external source of energy."),

 dict(q="By what other name does the framework say a galvanic cell is sometimes known?",
      choices=["A voltaic cell", "An electrolytic cell", "A concentration cell",
               "A half-cell", "A salt-bridge cell"],
      ans=0,
      why="EK 9.8.A.2 opens with the phrase galvanic, sometimes called voltaic, cells, and "
          "distinguishes them from electrolytic cells by the favorability of the reaction "
          "involved."),

 dict(q="Which of these does the exclusion statement attached to the framework's rule about "
        "electrodes place outside the scope of the exam?",
      choices=[
        "Labelling an electrode as positive or as negative",
        "Identifying which electrode is the anode",
        "Describing the direction of electron flow",
        "Describing the change in mass of an electrode",
        "Naming the process occurring in each half-cell"],
      ans=0,
      why="The exclusion statement attached to EK 9.8.A.3 says that labelling an electrode "
          "as positive or negative will not be assessed, while EK 9.8.A.1 explicitly keeps "
          "electron flow, electrode mass and the half-cell reactions within scope."),

 dict(q="In which direction do electrons travel through the external wire of a cell?",
      choices=[
        "From the anode, where oxidation occurs, to the cathode, where reduction occurs",
        "From the cathode, where reduction occurs, to the anode, where oxidation occurs",
        "In whichever direction the salt bridge allows them to travel",
        "In both directions at once, so that the charge stays balanced",
        "Electrons do not travel through the wire at all"],
      ans=0,
      why="EK 4.7.A.3 says electrons are transferred from the species that is oxidized to "
          "the species that is reduced, and EK 9.8.A.3 puts the oxidation at the anode and "
          "the reduction at the cathode, so the wire carries them from the first to the "
          "second. Electrons do not travel through the salt bridge."),

 dict(q="What role does the salt bridge play in the functioning of a cell?",
      choices=[
        "It allows ions to move between the half-cells so charge does not build up in "
        "either solution",
        "It carries the electrons from one electrode to the other",
        "It supplies the energy that drives the reaction",
        "It keeps the two solutions at the same temperature",
        "It prevents any movement of matter between the half-cells"],
      ans=0,
      why="EK 9.8.A.1 lists the salt bridge as a component with a specific role and names "
          "ion flow through the salt bridge among the operational characteristics of a "
          "cell. Electrons travel through the external wire, not through the bridge."),

 dict(q="What role does the voltage or current measuring device play?",
      choices=[
        "It reports the electrical behaviour of the cell while it operates",
        "It drives the reaction in an electrolytic cell",
        "It carries ions between the two half-cells",
        "It determines which electrode is the anode",
        "It supplies the electrons that flow through the circuit"],
      ans=0,
      why="EK 9.8.A.1 lists the voltage or current measuring device among the components "
          "each playing a specific role, and its role is measurement rather than driving "
          "the cell, which in an electrolytic cell is the external supply's job under EK "
          "9.7.A.1."),

 dict(q="What role do the electrodes play in the functioning of a cell?",
      choices=[
        "They are the surfaces at which the two half-reactions take place",
        "They store the ions that move between the half-cells",
        "They keep the two solutions from mixing with one another",
        "They measure the current passing through the circuit",
        "They supply the energy that makes an unfavored reaction occur"],
      ans=0,
      why="EK 9.8.A.1 lists the electrodes among the components with a specific role, and "
          "EK 9.8.A.3 places one half-reaction at each of them, oxidation at the anode and "
          "reduction at the cathode."),

 dict(q="What role do the solutions in the half-cells play?",
      choices=[
        "They supply the species that are oxidized or reduced, and carry the ions involved",
        "They complete the external circuit through which electrons travel",
        "They hold the two electrodes apart so they cannot touch",
        "They measure the potential difference between the electrodes",
        "They prevent any ion from moving between the two half-cells"],
      ans=0,
      why="EK 9.8.A.1 lists the solutions in the half-cells among the components with a "
          "specific role and names the reactions occurring in each half-cell among the "
          "operational characteristics that can be described. The external circuit is the "
          "wire, not the solution."),

 dict(q="A galvanic cell is built from the two half-cells in the table, joined by a salt "
        "bridge and an external wire. Which half-cell contains the anode?",
      table=_T_ZNCU,
      choices=[
        "Half-cell 1, where oxidation occurs and the electrode loses mass",
        "Half-cell 2, where oxidation occurs and the electrode loses mass",
        "Half-cell 1, where reduction occurs and the electrode loses mass",
        "Half-cell 2, where reduction occurs and the electrode gains mass",
        "Neither, because a galvanic cell has no anode"],
      ans=0,
      why="EK 9.8.A.3 puts oxidation at the anode, and EK 4.7.A.3 makes oxidation the loss "
          "of electrons by the species oxidized, so a metal electrode that is oxidized to "
          "ions passes into solution and the electrode loses mass. EK 9.8.A.1 names change "
          "in electrode mass among the observable characteristics."),

 dict(q="Using the same two half-cells, which one contains the cathode?",
      table=_T_ZNCU,
      choices=[
        "Half-cell 2, where reduction occurs and the electrode gains mass",
        "Half-cell 1, where reduction occurs and the electrode gains mass",
        "Half-cell 2, where oxidation occurs and the electrode gains mass",
        "Half-cell 1, where oxidation occurs and the electrode loses mass",
        "Neither, because both electrodes are metals"],
      ans=0,
      why="EK 9.8.A.3 puts reduction at the cathode, and metal ions from the solution "
          "reduced onto the electrode add to its mass, which is the tabulated observation. "
          "EK 9.8.A.1 names change in electrode mass among the observable characteristics."),

 dict(q="For the same cell, in which direction do electrons travel through the external "
        "wire?",
      table=_T_ZNCU,
      choices=[
        "From the electrode in half-cell 1 to the electrode in half-cell 2",
        "From the electrode in half-cell 2 to the electrode in half-cell 1",
        "Through the salt bridge rather than through the wire",
        "In both directions equally, so that no net charge builds up",
        "The direction cannot be decided from the tabulated observations"],
      ans=0,
      why="EK 4.7.A.3 sends electrons from the species oxidized to the species reduced, and "
          "the tabulated mass changes identify which half-cell each process occurs in: the "
          "electrode losing mass is being oxidized. EK 9.8.A.3 then names the electrodes."),

 dict(q="For the same cell, why does one electrode gain mass while the other loses it?",
      table=_T_ZNCU,
      choices=[
        "Metal atoms leave the electrode being oxidized and metal ions are deposited on the "
        "other",
        "The solutions exchange metal through the salt bridge",
        "The heavier metal always gains mass from the lighter one",
        "The electrode connected to the measuring device always gains mass",
        "Both electrodes gain mass, and the tabulated loss must be an error"],
      ans=0,
      why="EK 9.8.A.3 puts oxidation at one electrode and reduction at the other, and EK "
          "4.7.A.3 makes those the loss and gain of electrons, so atoms leave one electrode "
          "as ions and ions arrive at the other as atoms. Metal does not travel through the "
          "salt bridge."),

 dict(q="An electrode made of the metal being oxidized is left in a working cell for "
        "several hours. What happens to its mass?",
      choices=[
        "It falls, because atoms leave the electrode as ions when they are oxidized",
        "It rises, because atoms leave the electrode as ions when they are oxidized",
        "It rises, because ions from the solution are deposited on it",
        "It stays the same, because the electrode is not part of the reaction",
        "It stays the same, because the ions formed remain attached to the surface"],
      ans=0,
      why="EK 4.7.A.3 makes oxidation the transfer of electrons away from the species "
          "oxidized, so metal atoms become ions and enter the solution. EK 9.8.A.1 names "
          "change in electrode mass among the characteristics that can be described at "
          "both the macroscopic and particulate levels."),

 dict(q="An electrode on which metal ions from the solution are being reduced is left in a "
        "working cell for several hours. What happens to its mass?",
      choices=[
        "It rises, because reduced ions are deposited on the electrode as metal atoms",
        "It falls, because reduced ions are deposited on the electrode as metal atoms",
        "It falls, because atoms leave the electrode as ions",
        "It stays the same, because reduction does not involve the electrode itself",
        "It stays the same, because the deposited metal dissolves again immediately"],
      ans=0,
      why="EK 9.8.A.3 puts reduction at the cathode, and metal ions gaining electrons "
          "become metal atoms that build up on the electrode surface. EK 9.8.A.1 names "
          "change in electrode mass among the observable characteristics of a cell."),

 dict(q="Hydrogen gas bubbles are seen forming at one electrode of a cell. Which process is "
        "occurring there, and what is that electrode called?",
      choices=[
        "Reduction, so that electrode is the cathode",
        "Oxidation, so that electrode is the anode",
        "Reduction, so that electrode is the anode",
        "Oxidation, so that electrode is the cathode",
        "Neither process, since a gas is not oxidized or reduced"],
      ans=0,
      why="Hydrogen ions gaining electrons to form hydrogen gas is a gain of electrons, "
          "which EK 4.7.A.3 identifies as reduction, and EK 9.8.A.3 places reduction at the "
          "cathode. EK 9.8.A.1 names evolution of a gas at an electrode among the "
          "observable characteristics."),

 dict(q="A cell does nothing until it is connected to an external power supply, after which "
        "a reaction proceeds. What kind of cell is it?",
      choices=[
        "An electrolytic cell, involving a thermodynamically unfavored reaction",
        "A galvanic cell, involving a thermodynamically favored reaction",
        "An electrolytic cell, involving a thermodynamically favored reaction",
        "A galvanic cell, involving a thermodynamically unfavored reaction",
        "Neither, since a cell that needs a supply is not an electrochemical cell"],
      ans=0,
      why="EK 9.8.A.2 pairs the electrolytic cell with a thermodynamically unfavored "
          "reaction, and EK 9.7.A.1 names electrical energy driving an electrolytic cell as "
          "an external source of energy used to make such a process occur."),

 dict(q="A cell lights a lamp with nothing else connected to it. What kind of cell is it?",
      choices=[
        "A galvanic cell, involving a thermodynamically favored reaction",
        "An electrolytic cell, involving a thermodynamically unfavored reaction",
        "A galvanic cell, involving a thermodynamically unfavored reaction",
        "An electrolytic cell, involving a thermodynamically favored reaction",
        "Neither, since lighting a lamp is not a chemical process"],
      ans=0,
      why="EK 9.8.A.2 pairs the galvanic cell with a thermodynamically favored reaction, "
          "and a reaction that delivers energy to an external circuit without being driven "
          "is one that proceeds of itself."),

 dict(q="The table describes how four cells operate. Which of them are galvanic cells?",
      table=_T_TYPES,
      choices=["Cells 1 and 4", "Cells 2 and 3", "Cell 1 alone", "Cell 2 alone",
               "All four cells"],
      ans=0,
      why="EK 9.8.A.2 makes a galvanic cell one involving a thermodynamically favored "
          "reaction, which proceeds without being driven, while an electrolytic cell "
          "requires the external supply EK 9.7.A.1 describes. Two of the tabulated cells "
          "operate with nothing else connected."),

 dict(q="Using the same table, which of the cells are electrolytic cells?",
      table=_T_TYPES,
      choices=["Cells 2 and 3", "Cells 1 and 4", "Cell 3 alone", "Cell 2 alone",
               "None of the four cells"],
      ans=0,
      why="EK 9.8.A.2 makes an electrolytic cell one involving a thermodynamically "
          "unfavored reaction, and EK 9.7.A.1 says such a process needs an external source "
          "of energy. Two of the tabulated cells describe exactly that."),

 dict(q="Which tabulated cells involve a thermodynamically unfavored reaction?",
      table=_T_TYPES,
      choices=[
        "Cells 2 and 3, which are the electrolytic cells",
        "Cells 1 and 4, which are the electrolytic cells",
        "Cells 1 and 4, which are the galvanic cells",
        "All four, since every cell needs energy to work",
        "None, since a cell cannot run an unfavored reaction"],
      ans=0,
      why="EK 9.8.A.2 ties the electrolytic cell to a thermodynamically unfavored reaction, "
          "and the tabulated cells needing an external supply are the electrolytic ones. A "
          "cell CAN run an unfavored reaction, which is the whole point of EK 9.7.A.1."),

 dict(q="In an electrolytic cell, where does oxidation occur?",
      choices=[
        "At the anode, as in every electrochemical cell",
        "At the cathode, because the cell is driven from outside",
        "At the anode in a galvanic cell but at the cathode in an electrolytic one",
        "At whichever electrode the external supply is connected to first",
        "At neither electrode, because the reaction is unfavored"],
      ans=0,
      why="EK 9.8.A.3 says that for ALL electrochemical cells, oxidation occurs at the "
          "anode and reduction occurs at the cathode. Being driven from outside changes the "
          "favorability of the reaction under EK 9.8.A.2, not the naming of the electrodes."),

 dict(q="In a galvanic cell, where does reduction occur?",
      choices=[
        "At the cathode, as in every electrochemical cell",
        "At the anode, because a galvanic cell runs of its own accord",
        "At the cathode in an electrolytic cell but at the anode in a galvanic one",
        "At both electrodes, since the reaction is favored",
        "At neither electrode, because no external supply is connected"],
      ans=0,
      why="EK 9.8.A.3 covers all electrochemical cells without exception, putting reduction "
          "at the cathode and oxidation at the anode whether the reaction is favored or "
          "unfavored."),

 dict(q="A student states that the anode is where reduction takes place. What is wrong with "
        "the statement?",
      choices=[
        "Oxidation occurs at the anode, and reduction occurs at the cathode",
        "Nothing is wrong, provided the cell is an electrolytic one",
        "Nothing is wrong, provided the cell is a galvanic one",
        "The anode is not one of the components of an electrochemical cell",
        "Neither process occurs at an electrode, since both occur in the solution"],
      ans=0,
      why="EK 9.8.A.3 assigns oxidation to the anode and reduction to the cathode for all "
          "electrochemical cells, so the statement reverses the framework's rule and does "
          "so for both types of cell alike."),

 dict(q="As a cell operates, ions move through the salt bridge. Why is that movement "
        "necessary?",
      choices=[
        "Without it, charge would build up in each solution and the reaction would stop",
        "Without it, the electrons would have no path between the electrodes",
        "Without it, the two solutions could not reach the same temperature",
        "Without it, the electrodes could not be weighed accurately",
        "Without it, the measuring device would read a current that is too large"],
      ans=0,
      why="EK 9.8.A.1 lists the salt bridge as a component with a specific role and names "
          "ion flow through it among the operational characteristics. Oxidation in one "
          "solution and reduction in the other would otherwise leave each with a net "
          "charge; the electrons themselves travel through the wire."),

 dict(q="At which levels does the framework say the operational characteristics of a cell "
        "can be described?",
      choices=[
        "At both the macroscopic and the particulate levels",
        "At the macroscopic level only",
        "At the particulate level only",
        "At neither level, since they must be measured rather than described",
        "At the macroscopic level for galvanic cells and the particulate level for "
        "electrolytic ones"],
      ans=0,
      why="EK 9.8.A.1 says the operational characteristics of the cell can be described at "
          "both the macroscopic and particulate levels, which is why the same observation "
          "has an account in terms of what is seen and an account in terms of particles."),

 dict(q="What does the framework say visual representations of galvanic and electrolytic "
        "cells are for?",
      choices=[
        "They are tools of analysis for identifying where the half-reactions occur and in "
        "which direction current flows",
        "They are required in order to calculate the mass of each electrode",
        "They replace the need to describe the cell at the particulate level",
        "They show which electrode carries the greater charge",
        "They are used only for galvanic cells, since electrolytic cells need no analysis"],
      ans=0,
      why="EK 9.8.A.2 says visual representations of galvanic and electrolytic cells are "
          "tools of analysis to identify where half-reactions occur and in what direction "
          "current flows, which is a claim about their use rather than about any single "
          "picture."),

]
