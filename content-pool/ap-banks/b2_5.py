# AP BIOLOGY 2.5 Membrane Transport
# CED effective Fall 2025, Unit 2 Cells. Big Idea 2 Energetics.
# Learning objectives 2.5.A, describe the mechanisms that organisms use to maintain
# solute and water balance, and 2.5.B, describe the mechanisms that organisms use to
# transport large molecules across the plasma membrane.
# Suggested skill 3.D, propose a new investigation based on an evaluation of the
# experimental design or evidence.
#
# Essential knowledge relied on, in the framework's own words:
#   2.5.A.1    The selective permeability of membranes allows for the formation of
#              concentration gradients of solutes across the membrane.
#   2.5.A.2    Passive transport is the net movement of molecules from regions of high
#              concentration to regions of low concentration without the direct input
#              of metabolic energy.
#   2.5.A.3    Active transport requires the direct input of energy to move molecules.
#              In some cases, active transport is utilized to move molecules from
#              regions of low concentration to regions of high concentration.
#   2.5.B.1    The processes of endocytosis and exocytosis require energy to move large
#              substances or large amounts of substances into and out of cells.
#     i.       In endocytosis, the cell takes in large molecules and particulate matter
#              by folding the plasma membrane in on itself and forming new (small)
#              vesicles that engulf material from the external environment.
#
# HONEST NOTE ON SUB-POINT ii. EK 2.5.B.1 has a second sub-point, on exocytosis, whose
# text is NOT recoverable from the pdftotext dump of the CED used for this bank -- the
# two-column layout drops it at a page break. So no item here keys a mechanism for
# exocytosis. What IS keyed about exocytosis is only what the readable lead sentence
# supports: that it requires energy, and that between them the two processes move large
# substances INTO AND OUT OF cells, with sub-point i naming endocytosis as the inward
# one. That is the full extent of the claim, and it is stated in every relevant claim
# in verify_b2_5.py.
#
# ON SCOPE. Facilitated diffusion is topic 2.6, tonicity and water potential are 2.7,
# and the pumps and electrochemical gradients are 2.8. This topic is the passive
# against active distinction and bulk transport, which is what EK 2.5.A.1 to EK 2.5.B.1
# state.
#
# ON THE DATA. Every table is labelled hypothetical, and every keyed conclusion is
# recoverable from the table alone and recomputed in verify_b2_5.py.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("2.5", "Membrane Transport", 2)

_T_ENERGY = dict(
    headers=["Transport process (hypothetical)",
             "Direction of net movement relative to the concentration gradient",
             "Rate when ATP production is blocked (percentage of the untreated rate)"],
    rows=[["Process 1", "from high concentration to low concentration", "97"],
          ["Process 2", "from low concentration to high concentration", "4"],
          ["Process 3", "from high concentration to low concentration", "95"],
          ["Process 4", "from low concentration to high concentration", "8"]])

_T_GRADIENT = dict(
    headers=["Solute (hypothetical)", "Concentration inside the cell (millimolar)",
             "Concentration outside the cell (millimolar)"],
    rows=[["Solute W", "12", "140"],
          ["Solute X", "150", "5"],
          ["Solute Y", "30", "30"]])

_T_VESICLE = dict(
    headers=["Treatment (hypothetical)",
             "Vesicles formed at the plasma membrane per cell in ten minutes",
             "Large particulate matter taken into the cell (arbitrary units)"],
    rows=[["Untreated cells", "46", "88"],
          ["Cells with ATP synthesis blocked", "3", "6"]])

QUESTIONS = [

 dict(q="What does the selective permeability of a membrane allow, according to the "
        "course framework?",
      choices=[
        "The formation of concentration gradients of solutes across the membrane",
        "The complete equalization of every solute on both sides of the membrane",
        "The synthesis of the proteins embedded in the membrane",
        "The digestion of material taken in from the environment",
        "The capture of light energy by the cell"],
      ans=0,
      why="EK 2.5.A.1 states that the selective permeability of membranes allows for the "
          "formation of concentration gradients of solutes across the membrane. A "
          "membrane that let everything through equally could not hold a gradient at all."),

 dict(q="How does the course framework define passive transport?",
      choices=[
        "The net movement of molecules from regions of high concentration to regions of "
        "low concentration without the direct input of metabolic energy",
        "The net movement of molecules from regions of low concentration to regions of "
        "high concentration without the direct input of metabolic energy",
        "The net movement of molecules in either direction using the direct input of "
        "metabolic energy",
        "The movement of large particles into the cell inside newly formed vesicles",
        "The movement of molecules only when embedded proteins are absent"],
      ans=0,
      why="EK 2.5.A.2 states that passive transport is the net movement of molecules from "
          "regions of high concentration to regions of low concentration without the "
          "direct input of metabolic energy. Both halves matter: the direction and the "
          "absence of an energy input."),

 dict(q="What does the course framework say active transport requires?",
      choices=[
        "The direct input of energy to move molecules",
        "The absence of any concentration gradient across the membrane",
        "The removal of the embedded proteins from the membrane",
        "A membrane that has lost its selective permeability",
        "The formation of new vesicles at the plasma membrane"],
      ans=0,
      why="EK 2.5.A.3 states that active transport requires the direct input of energy to "
          "move molecules. That energy requirement is precisely what EK 2.5.A.2 denies of "
          "passive transport, so the two definitions are complementary."),

 dict(q="What does the course framework say active transport is used for in some cases?",
      choices=[
        "Moving molecules from regions of low concentration to regions of high "
        "concentration",
        "Moving molecules from regions of high concentration to regions of low "
        "concentration",
        "Preventing all movement of molecules across the membrane",
        "Building the phospholipids of which the membrane is made",
        "Removing the cell wall from a walled cell"],
      ans=0,
      why="EK 2.5.A.3 states that in some cases active transport is utilized to move "
          "molecules from regions of low concentration to regions of high concentration. "
          "The opposite direction is what EK 2.5.A.2 assigns to passive transport."),

 dict(q="What do endocytosis and exocytosis have in common, according to the course "
        "framework?",
      choices=[
        "Both require energy to move large substances or large amounts of substances "
        "into and out of cells.",
        "Both move small nonpolar molecules across the membrane without energy.",
        "Both require the membrane to lose its selective permeability first.",
        "Both move molecules only from high concentration to low concentration.",
        "Both take place only in cells that have a cell wall."],
      ans=0,
      why="EK 2.5.B.1 states that the processes of endocytosis and exocytosis require "
          "energy to move large substances or large amounts of substances into and out of "
          "cells. Small nonpolar molecules cross without any such process under EK "
          "2.4.A.2."),

 dict(q="How does the course framework describe endocytosis?",
      choices=[
        "The cell folds the plasma membrane in on itself, forming new small vesicles that "
        "engulf material from the external environment.",
        "The cell dissolves a portion of its plasma membrane to let material pass through "
        "the gap.",
        "The cell pushes material out through channels embedded in the plasma membrane.",
        "The cell moves material across the membrane one molecule at a time using "
        "transport proteins.",
        "The cell allows material to diffuse in through the hydrophobic interior of the "
        "membrane."],
      ans=0,
      why="EK 2.5.B.1 i states that in endocytosis the cell takes in large molecules and "
          "particulate matter by folding the plasma membrane in on itself and forming new "
          "small vesicles that engulf material from the external environment. No gap, "
          "channel or diffusion step appears in that description."),

 dict(q="What kind of material does the course framework say endocytosis brings into the "
        "cell?",
      choices=[
        "Large molecules and particulate matter",
        "Small nonpolar molecules such as oxygen",
        "Individual ions moving down their concentration gradient",
        "Water molecules only",
        "The phospholipids of the membrane itself"],
      ans=0,
      why="EK 2.5.B.1 i states that in endocytosis the cell takes in large molecules and "
          "particulate matter. Small nonpolar molecules cross the membrane freely under "
          "EK 2.4.A.2 and need no vesicle."),

 dict(q="Taking the course framework's account of endocytosis together with its statement "
        "about the two bulk processes, what can be said about the direction each one "
        "moves material?",
      choices=[
        "Endocytosis brings material into the cell, and exocytosis is the process that "
        "moves large substances out.",
        "Endocytosis moves material out of the cell, and exocytosis brings it in.",
        "Both processes bring material into the cell.",
        "Both processes move material out of the cell.",
        "Neither process moves material across the plasma membrane."],
      ans=0,
      why="EK 2.5.B.1 states that the two processes together move large substances or "
          "large amounts of substances into and out of cells, and EK 2.5.B.1 i identifies "
          "endocytosis as the one that takes material in from the external environment. "
          "The outward half of the pair is therefore exocytosis."),

 dict(q="Which single feature distinguishes active transport from passive transport in "
        "the course framework's definitions?",
      choices=[
        "Whether the direct input of energy is required",
        "Whether the membrane is selectively permeable",
        "Whether the substance moved is a solute",
        "Whether the substance moved is large or small",
        "Whether a cell wall is present outside the membrane"],
      ans=0,
      why="EK 2.5.A.2 defines passive transport as occurring without the direct input of "
          "metabolic energy and EK 2.5.A.3 defines active transport as requiring the "
          "direct input of energy. Selective permeability is common ground under EK "
          "2.5.A.1, and size is what distinguishes the bulk processes of EK 2.5.B.1."),

 dict(q="A solute is observed moving across a membrane from where it is more concentrated "
        "to where it is less concentrated, with no energy supplied. Which process is "
        "this?",
      choices=["Passive transport", "Active transport", "Endocytosis", "Exocytosis",
               "No transport process, because movement always requires energy"],
      ans=0,
      why="EK 2.5.A.2 defines passive transport as the net movement of molecules from "
          "regions of high concentration to regions of low concentration without the "
          "direct input of metabolic energy, which is exactly what is described. EK "
          "2.5.A.3 and EK 2.5.B.1 all require an energy input."),

 dict(q="A cell accumulates a solute until its internal concentration is far above the "
        "external concentration, and the accumulation stops when the cell's energy supply "
        "is cut off. Which process is responsible?",
      choices=["Active transport", "Passive transport", "Free diffusion through the "
               "hydrophobic interior", "Endocytosis of the solute in vesicles",
               "No process, because a solute cannot be more concentrated inside than "
               "outside"],
      ans=0,
      why="EK 2.5.A.3 states that active transport requires the direct input of energy "
          "and that in some cases it moves molecules from regions of low concentration to "
          "regions of high concentration. Both features of the observation match, and "
          "neither matches the energy-free definition in EK 2.5.A.2."),

 dict(q="A drug stops a cell from producing usable energy. Which of the following would "
        "be expected to continue essentially unchanged?",
      choices=[
        "The net movement of a solute down its concentration gradient",
        "The accumulation of a solute against its concentration gradient",
        "The uptake of large particulate matter in newly formed vesicles",
        "The release of large substances out of the cell",
        "None of these, because every kind of membrane transport requires energy"],
      ans=0,
      why="EK 2.5.A.2 defines passive transport as occurring without the direct input of "
          "metabolic energy, so it is the one process on the list that does not depend on "
          "the drug's target. EK 2.5.A.3 and EK 2.5.B.1 make the other three "
          "energy-requiring."),

 dict(q="The table describes four transport processes by the direction of net movement "
        "and by what happens when ATP production is blocked. Which processes are examples "
        "of active transport?",
      table=_T_ENERGY,
      choices=[
        "Process 2 and Process 4",
        "Process 1 and Process 3",
        "Process 1 and Process 2",
        "Process 3 and Process 4",
        "All four processes"],
      ans=0,
      why="EK 2.5.A.3 makes active transport the kind that requires the direct input of "
          "energy, and in some cases moves molecules from low concentration to high. "
          "Exactly two rows of the table both run against the gradient and nearly stop "
          "when ATP production is blocked."),

 dict(q="Among the same four processes, which are examples of passive transport?",
      table=_T_ENERGY,
      choices=[
        "Process 1 and Process 3",
        "Process 2 and Process 4",
        "Process 1 and Process 2",
        "Process 3 and Process 4",
        "None of them"],
      ans=0,
      why="EK 2.5.A.2 defines passive transport as net movement from high concentration "
          "to low concentration without the direct input of metabolic energy. Exactly two "
          "rows run down the gradient and keep almost all of their rate when ATP "
          "production is blocked."),

 dict(q="What does the effect of blocking ATP production, shown in the same table, "
        "demonstrate about the four processes?",
      table=_T_ENERGY,
      choices=[
        "Two of them depend on a direct energy input and two do not.",
        "All four of them depend on a direct energy input.",
        "None of them depends on a direct energy input.",
        "The processes that run down the gradient are the ones that depend on energy.",
        "Blocking ATP production affected all four processes to the same degree."],
      ans=0,
      why="Two rows retain nearly all of their rate when ATP production is blocked and "
          "two fall to a small fraction of it, so the table separates the group EK 2.5.A.3 "
          "describes from the group EK 2.5.A.2 describes. The rows that keep their rate "
          "are the ones running down the gradient, not the reverse."),

 dict(q="The table gives the concentration of three solutes inside and outside a cell. "
        "Which solute would move into the cell by passive transport?",
      table=_T_GRADIENT,
      choices=["Solute W", "Solute X", "Solute Y",
               "All three would move in by passive transport.",
               "None of them, because passive transport moves solutes only outward."],
      ans=0,
      why="EK 2.5.A.2 gives passive transport the direction from high concentration to "
          "low concentration, so inward passive movement requires the outside "
          "concentration to exceed the inside. Exactly one row of the table satisfies "
          "that, and the framework attaches no fixed direction of its own to passive "
          "transport."),

 dict(q="Among the same three solutes, which one is already far more concentrated inside "
        "the cell than outside, so that further accumulation inside would require an "
        "energy input?",
      table=_T_GRADIENT,
      choices=["Solute X", "Solute W", "Solute Y",
               "All three are more concentrated inside.",
               "None of them is more concentrated inside."],
      ans=0,
      why="Exactly one row of the table records a higher inside concentration than "
          "outside. Adding more against that difference is movement from low to high, "
          "which EK 2.5.A.3 assigns to active transport and its direct input of energy."),

 dict(q="Which solute in the same table would show no net movement by passive transport?",
      table=_T_GRADIENT,
      choices=["Solute Y", "Solute W", "Solute X",
               "All three would show no net movement.",
               "The table does not allow this to be determined."],
      ans=0,
      why="EK 2.5.A.2 makes passive transport a NET movement from high concentration to "
          "low concentration, so equal concentrations on the two sides leave no net "
          "direction. Exactly one row of the table records equal values, so the table "
          "does settle the question."),

 dict(q="Cells were observed with and without ATP synthesis blocked, and both vesicle "
        "formation and the uptake of large particulate matter were measured, with the "
        "results in the table. Which conclusion is best supported?",
      table=_T_VESICLE,
      choices=[
        "Both vesicle formation and the uptake of large particles depend on an energy "
        "supply.",
        "Vesicle formation depends on an energy supply but the uptake of large particles "
        "does not.",
        "The uptake of large particles depends on an energy supply but vesicle formation "
        "does not.",
        "Neither vesicle formation nor the uptake of large particles depends on an energy "
        "supply.",
        "Blocking ATP synthesis increased both measurements."],
      ans=0,
      why="Both measured quantities fall to a small fraction of their untreated values "
          "when ATP synthesis is blocked. EK 2.5.B.1 states that endocytosis requires "
          "energy, and EK 2.5.B.1 i makes the forming of new vesicles the mechanism by "
          "which the cell takes in large molecules and particulate matter."),

 dict(q="A student proposes a follow-up to the vesicle experiment in the table. Which "
        "proposal would best strengthen the conclusion that the effect is due to the loss "
        "of usable energy rather than to some other action of the treatment?",
      table=_T_VESICLE,
      choices=[
        "Restore an energy supply to the treated cells and test whether vesicle formation "
        "and particle uptake recover.",
        "Repeat the experiment with the same treatment and the same measurements on the "
        "same cells.",
        "Measure the surface area of the plasma membrane in untreated cells only.",
        "Treat a second group of cells with a different drug and report only their "
        "particle uptake.",
        "Count the vesicles in untreated cells at several additional time points."],
      ans=0,
      why="A treatment can act through more than one route, so showing that restoring the "
          "proposed cause restores the effect is what separates it from the "
          "alternatives. Repeating the same measurement adds precision but no new "
          "comparison, and the other proposals drop the treated group or the second "
          "measurement. This is the CED's suggested skill 3.D for this topic."),

 dict(q="Why can a concentration gradient exist across a plasma membrane at all, "
        "according to the course framework?",
      choices=[
        "Because the membrane is selectively permeable, so solutes are not free to "
        "equalize across it",
        "Because the membrane is freely permeable, so solutes distribute themselves "
        "evenly",
        "Because the membrane contains no embedded proteins",
        "Because the cell wall holds the solutes in place",
        "Because solutes cannot move at all once inside a cell"],
      ans=0,
      why="EK 2.5.A.1 states that the selective permeability of membranes allows for the "
          "formation of concentration gradients of solutes across the membrane, and EK "
          "2.4.A.1 traces that permeability to the membrane's hydrophobic interior. Free "
          "permeability would abolish the gradient rather than allow it."),

 dict(q="A student states that passive transport happens because the membrane simply is "
        "not there for some molecules. What is the best correction?",
      choices=[
        "The membrane is present throughout; passive transport is net movement across it "
        "down a concentration gradient without a direct energy input.",
        "The membrane is indeed absent wherever passive transport occurs, which is why no "
        "energy is needed.",
        "Passive transport requires the direct input of metabolic energy, so the student "
        "has the definition backwards.",
        "Passive transport moves molecules from low concentration to high concentration "
        "across an intact membrane.",
        "Passive transport occurs only inside vesicles formed at the plasma membrane."],
      ans=0,
      why="EK 2.5.A.2 defines passive transport as net movement ACROSS the membrane from "
          "high to low concentration without the direct input of metabolic energy, so the "
          "membrane is a participant rather than an absence. Movement from low to high is "
          "EK 2.5.A.3's active case."),

 dict(q="The new vesicles formed during endocytosis are made from which structure?",
      choices=[
        "The plasma membrane, which folds in on itself",
        "The cell wall, which detaches in fragments",
        "The nuclear envelope, which buds outward",
        "Ribosomes, which assemble around the material",
        "The hydrophobic interior alone, with no membrane involved"],
      ans=0,
      why="EK 2.5.B.1 i states that the cell takes in large molecules and particulate "
          "matter by folding the plasma membrane in on itself and forming new small "
          "vesicles. The vesicle is therefore derived from the plasma membrane itself."),

 dict(q="Why does a cell need endocytosis for some materials when small nonpolar "
        "molecules cross the membrane without any such process?",
      choices=[
        "Endocytosis handles large molecules and particulate matter, which are too big to "
        "cross the membrane the way small nonpolar molecules do.",
        "Endocytosis handles small nonpolar molecules, which cannot cross the membrane on "
        "their own.",
        "Endocytosis is needed only when the concentration gradient runs the wrong way.",
        "Endocytosis is needed only in cells that lack a plasma membrane.",
        "Endocytosis replaces the membrane's selective permeability with free "
        "permeability."],
      ans=0,
      why="EK 2.5.B.1 assigns the bulk processes to large substances or large amounts of "
          "substances and EK 2.5.B.1 i names large molecules and particulate matter, "
          "while EK 2.4.A.2 lets small nonpolar molecules cross freely with no process at "
          "all. Size rather than gradient direction is what separates the two cases."),

 dict(q="Which observation would provide the strongest evidence that a particular "
        "transport process is active rather than passive?",
      choices=[
        "It moves the substance against its concentration gradient and stops when the "
        "cell's energy supply is cut off.",
        "It moves the substance down its concentration gradient and continues when the "
        "cell's energy supply is cut off.",
        "It moves the substance across an intact plasma membrane.",
        "It moves a substance that is a solute rather than a solvent.",
        "It occurs faster at a higher external concentration of the substance."],
      ans=0,
      why="EK 2.5.A.3 attaches both features to active transport: the direct input of "
          "energy, and in some cases movement from low concentration to high. The second "
          "option is the passive case defined in EK 2.5.A.2, and crossing an intact "
          "membrane is common to both."),

 dict(q="Which observation would be most consistent with a transport process being "
        "passive?",
      choices=[
        "Its rate is unchanged when the cell's supply of usable energy is removed.",
        "Its rate falls to almost nothing when the cell's supply of usable energy is "
        "removed.",
        "It builds a concentration of the substance inside the cell far above the "
        "concentration outside.",
        "It requires the formation of new vesicles at the plasma membrane.",
        "It occurs only in cells that possess a cell wall."],
      ans=0,
      why="EK 2.5.A.2 defines passive transport as occurring without the direct input of "
          "metabolic energy, so insensitivity to the loss of that energy is the "
          "diagnostic. Building a concentration against the gradient and forming vesicles "
          "are the EK 2.5.A.3 and EK 2.5.B.1 cases, both of which require energy."),

 dict(q="A membrane is modified so that it becomes freely permeable to every solute. What "
        "happens to the concentration gradients across it?",
      choices=[
        "They cannot be maintained, because it was the selective permeability that "
        "allowed them to form.",
        "They become steeper, because solutes can now move more easily.",
        "They are unaffected, because gradients depend only on the total amount of "
        "solute.",
        "They reverse direction, so each solute becomes more concentrated on the other "
        "side.",
        "They can still be maintained, because active transport does not depend on "
        "permeability."],
      ans=0,
      why="EK 2.5.A.1 states that the selective permeability of membranes is what allows "
          "for the formation of concentration gradients of solutes across the membrane, "
          "so removing the selectivity removes the condition the gradient rests on."),

 dict(q="Which pairing of process with energy requirement matches the course framework?",
      choices=[
        "Passive transport needs no direct energy input; active transport, endocytosis "
        "and exocytosis all do.",
        "Passive transport, active transport and endocytosis all need a direct energy "
        "input; only exocytosis does not.",
        "Only active transport needs a direct energy input; endocytosis and exocytosis "
        "do not.",
        "None of the four processes needs a direct energy input.",
        "All four processes need a direct energy input."],
      ans=0,
      why="EK 2.5.A.2 places passive transport outside the energy-requiring group, EK "
          "2.5.A.3 places active transport inside it, and EK 2.5.B.1 states that both "
          "endocytosis and exocytosis require energy. The four processes therefore split "
          "one against three."),

 dict(q="A researcher finds that a solute crosses a membrane at a rate proportional to "
        "the difference in its concentration on the two sides, and that the rate is "
        "unaffected by removing the cell's energy supply. Which classification is best "
        "supported?",
      choices=[
        "Passive transport, since movement follows the gradient and needs no direct "
        "energy input",
        "Active transport, since movement follows the gradient and needs no direct energy "
        "input",
        "Active transport, since the rate depends on the concentration difference",
        "Endocytosis, since the solute enters the cell",
        "Exocytosis, since the solute crosses the membrane"],
      ans=0,
      why="Both reported features are the two halves of EK 2.5.A.2's definition of "
          "passive transport: net movement set by the concentration difference, and no "
          "direct input of metabolic energy. EK 2.5.A.3 and EK 2.5.B.1 all require that "
          "input."),

 dict(q="Which summary correctly sorts the mechanisms the course framework describes in "
        "this topic?",
      choices=[
        "Passive transport moves molecules down a gradient without a direct energy input; "
        "active transport uses a direct energy input and can move them up a gradient; "
        "endocytosis and exocytosis use energy to move large substances.",
        "Passive transport uses a direct energy input to move molecules up a gradient; "
        "active transport moves them down a gradient without energy; endocytosis and "
        "exocytosis move small molecules.",
        "All three mechanisms move molecules down a concentration gradient without any "
        "energy input.",
        "All three mechanisms require a direct energy input and move molecules up a "
        "concentration gradient.",
        "Passive and active transport are two names for the same mechanism, and only the "
        "bulk processes differ from them."],
      ans=0,
      why="The three parts line up with three statements: EK 2.5.A.2 for passive "
          "transport, EK 2.5.A.3 for active transport including the low to high case, and "
          "EK 2.5.B.1 for the energy requirement of endocytosis and exocytosis with large "
          "substances or large amounts of substances."),
]
