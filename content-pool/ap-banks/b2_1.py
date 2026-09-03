# AP BIOLOGY 2.1 Cell Structure and Function
# CED effective Fall 2025, Unit 2 Cells. Big Idea 4 Systems Interactions.
# Learning objective 2.1.A: explain how the structure and function of subcellular
# components and organelles contribute to the function of cells.
# Suggested skills 1.A, describe biological concepts and processes, and 6.A, make a
# scientific claim.
#
# Essential knowledge relied on, in the framework's own words:
#   2.1.A.1    Ribosomes are comprised of ribosomal RNA and protein. These
#              non-membrane, subcellular structures are found in cells in all forms of
#              life and reflect the common ancestry in all known life. Ribosomes
#              synthesize proteins according to messenger RNA sequences.
#   2.1.A.2    The endomembrane system consists of a group of membrane-bound organelles
#              and subcellular components -- endoplasmic reticulum, Golgi complex,
#              lysosomes, vacuoles and transport vesicles, the nuclear envelope, and
#              the plasma membrane -- that work together to modify, package, and
#              transport polysaccharides, lipids, and proteins intercellularly.
#   2.1.A.3    Endoplasmic reticulum provides mechanical support by helping cells
#              maintain shape and plays a role in intracellular transport.
#     i.       Rough ER is associated with membrane-bound ribosomes, allows for the
#              compartmentalization of cells, and helps carry out protein synthesis.
#     ii.      Smooth ER functions include the detoxification of cells and lipid
#              synthesis.
#   2.1.A.4    The Golgi complex is a membrane-bound structure that consists of a
#              series of flattened membrane sacs. Functions of the Golgi include
#              correctly folding and chemically modifying newly synthesized cellular
#              products, and packaging proteins for trafficking.
#              Illustrative example: glycosylation and other chemical modifications of
#              proteins that take place within the Golgi and determine protein function
#              or targeting.
#   2.1.A.5    Mitochondria have a double membrane that provides compartments for
#              different metabolic reactions involved in aerobic cellular respiration.
#              The outer membrane is smooth, while the inner membrane is highly
#              convoluted, forming folds that enable ATP to be synthesized more
#              efficiently.
#   2.1.A.6    Lysosomes are membrane-enclosed sacs that contain hydrolytic enzymes
#              that digest material. Lysosomes also play a role in programmed cell death
#              (apoptosis).
#   2.1.A.7    Vacuoles are membrane-bound sacs that play many different roles.
#     i.       In plant cells, a specialized large vacuole maintains turgor pressure
#              through nutrient and water storage.
#     ii.      In animal cells, vacuoles are smaller in size, are more plentiful than in
#              plant cells, and store cellular materials.
#   2.1.A.8    Chloroplasts are specialized organelles that are found in plants and
#              photosynthetic algae. Chloroplasts contain a double membrane and serve as
#              the location for photosynthesis.
#
# ON SCOPE. Compartmentalization as a general principle is topic 2.9 and the
# endosymbiotic origin of organelles is topic 2.10; neither is asked here. This module
# keys only what EK 2.1.A.1 to EK 2.1.A.8 state about the components themselves.
#
# ON THE DATA. Every table is labelled hypothetical and every keyed conclusion is
# recoverable from the table alone and recomputed in verify_b2_1.py.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("2.1", "Cell Structure and Function", 2)

_T_MITO = dict(
    headers=["Cell type (hypothetical)", "Mean number of mitochondria per cell",
             "Rate of aerobic cellular respiration (arbitrary units)"],
    rows=[["Cell type 1", "3,200", "88"],
          ["Cell type 2", "1,100", "31"],
          ["Cell type 3", "400", "12"],
          ["Cell type 4", "90", "3"]])

_T_CRISTAE = dict(
    headers=["Mitochondrial preparation (hypothetical)",
             "Inner membrane surface area per mitochondrion (square micrometers)",
             "ATP synthesized per minute (arbitrary units)"],
    rows=[["Preparation 1", "4", "20"],
          ["Preparation 2", "8", "41"],
          ["Preparation 3", "16", "78"],
          ["Preparation 4", "24", "119"]])

_T_VACUOLE = dict(
    headers=["Cell type (hypothetical measurements)", "Mean number of vacuoles per cell",
             "Mean volume of the largest vacuole (cubic micrometers)"],
    rows=[["Plant cell", "1", "900"],
          ["Animal cell", "14", "3"]])

_T_LYSO = dict(
    headers=["Cell line (hypothetical)",
             "Hydrolytic enzyme activity inside lysosomes (units)",
             "Undigested material accumulated per cell (arbitrary units)"],
    rows=[["Line 1", "100", "3"],
          ["Line 2", "62", "11"],
          ["Line 3", "24", "38"],
          ["Line 4", "5", "91"]])

QUESTIONS = [

 dict(q="Of what are ribosomes composed, according to the course framework?",
      choices=[
        "Ribosomal RNA and protein",
        "Phospholipid and cholesterol",
        "Messenger RNA and a double membrane",
        "Deoxyribonucleic acid and hydrolytic enzymes",
        "Polysaccharide and protein"],
      ans=0,
      why="EK 2.1.A.1 states that ribosomes are comprised of ribosomal RNA and protein. "
          "Messenger RNA is what a ribosome reads rather than what it is made of, and "
          "hydrolytic enzymes belong to lysosomes under EK 2.1.A.6."),

 dict(q="Which statement about the distribution of ribosomes does the course framework "
        "make, and what does it infer from it?",
      choices=[
        "They are found in cells in all forms of life, which reflects the common ancestry "
        "of all known life.",
        "They are found only in eukaryotic cells, which reflects the recent origin of "
        "eukaryotes.",
        "They are found only in cells that carry out photosynthesis.",
        "They are found only in animal cells, which is why animals synthesize protein.",
        "They are found in all cells, which shows that all cells are the same size."],
      ans=0,
      why="EK 2.1.A.1 states that these non-membrane subcellular structures are found in "
          "cells in all forms of life and reflect the common ancestry in all known life. "
          "Restricting them to one group of organisms contradicts the first half of that "
          "sentence."),

 dict(q="What do ribosomes do, and according to what?",
      choices=[
        "They synthesize proteins according to messenger RNA sequences.",
        "They synthesize messenger RNA according to protein sequences.",
        "They digest material using hydrolytic enzymes.",
        "They package proteins into vesicles for trafficking.",
        "They synthesize lipids and detoxify the cell."],
      ans=0,
      why="EK 2.1.A.1 states that ribosomes synthesize proteins according to messenger "
          "RNA sequences. Digestion belongs to lysosomes under EK 2.1.A.6, packaging to "
          "the Golgi under EK 2.1.A.4, and lipid synthesis and detoxification to smooth "
          "endoplasmic reticulum under EK 2.1.A.3 ii."),

 dict(q="Which of the following is listed by the course framework as part of the "
        "endomembrane system?",
      choices=["The Golgi complex", "The ribosome", "The chloroplast",
               "The mitochondrion", "The cell wall"],
      ans=0,
      why="EK 2.1.A.2 lists endoplasmic reticulum, Golgi complex, lysosomes, vacuoles and "
          "transport vesicles, the nuclear envelope, and the plasma membrane as the "
          "endomembrane system. Ribosomes are described in EK 2.1.A.1 as non-membrane "
          "structures, and mitochondria and chloroplasts are treated separately in EK "
          "2.1.A.5 and EK 2.1.A.8."),

 dict(q="What does the course framework say the components of the endomembrane system do "
        "when they work together?",
      choices=[
        "They modify, package, and transport polysaccharides, lipids, and proteins.",
        "They generate all of the cell's ATP by aerobic cellular respiration.",
        "They capture light energy and use it to build sugars.",
        "They copy the cell's hereditary information before division.",
        "They provide the rigid outer boundary that resists osmotic lysis."],
      ans=0,
      why="EK 2.1.A.2 states that the group works together to modify, package, and "
          "transport polysaccharides, lipids, and proteins intercellularly. Aerobic "
          "respiration is assigned to mitochondria in EK 2.1.A.5 and photosynthesis to "
          "chloroplasts in EK 2.1.A.8."),

 dict(q="Which pair of roles does the course framework assign to endoplasmic reticulum in "
        "general?",
      choices=[
        "Mechanical support that helps the cell maintain shape, and a role in "
        "intracellular transport",
        "Digestion of engulfed material, and a role in programmed cell death",
        "Storage of water and nutrients, and maintenance of turgor pressure",
        "Capture of light energy, and synthesis of sugars",
        "Assembly of ribosomal RNA, and synthesis of messenger RNA"],
      ans=0,
      why="EK 2.1.A.3 states that endoplasmic reticulum provides mechanical support by "
          "helping cells maintain shape and plays a role in intracellular transport. The "
          "rejected options give the functions EK 2.1.A.6, EK 2.1.A.7 i and EK 2.1.A.8 "
          "assign to lysosomes, plant vacuoles and chloroplasts."),

 dict(q="Which description of rough endoplasmic reticulum matches the course framework?",
      choices=[
        "It is associated with membrane-bound ribosomes and helps carry out protein "
        "synthesis.",
        "It is associated with membrane-bound ribosomes and carries out the "
        "detoxification of cells.",
        "It has no ribosomes associated with it and carries out lipid synthesis.",
        "It is the site of aerobic cellular respiration in the cell.",
        "It is a series of flattened sacs that package proteins for trafficking."],
      ans=0,
      why="EK 2.1.A.3 i states that rough ER is associated with membrane-bound ribosomes, "
          "allows for the compartmentalization of cells, and helps carry out protein "
          "synthesis. Detoxification and lipid synthesis are assigned to smooth ER in EK "
          "2.1.A.3 ii, and flattened sacs to the Golgi in EK 2.1.A.4."),

 dict(q="Which functions does the course framework assign to smooth endoplasmic "
        "reticulum?",
      choices=[
        "Detoxification of cells and lipid synthesis",
        "Protein synthesis and association with membrane-bound ribosomes",
        "Digestion of material and programmed cell death",
        "Photosynthesis and storage of starch",
        "Packaging of proteins for trafficking to other organelles"],
      ans=0,
      why="EK 2.1.A.3 ii states that smooth ER functions include the detoxification of "
          "cells and lipid synthesis. Protein synthesis and membrane-bound ribosomes "
          "belong to rough ER in EK 2.1.A.3 i, which is the contrast the two sub-points "
          "draw."),

 dict(q="How does the course framework describe the physical structure of the Golgi "
        "complex?",
      choices=[
        "A membrane-bound structure consisting of a series of flattened membrane sacs",
        "A double-membrane organelle whose inner membrane is highly convoluted",
        "A non-membrane structure built from RNA and protein",
        "A single large sac filled with hydrolytic enzymes",
        "A network of tubes that has no membrane of its own"],
      ans=0,
      why="EK 2.1.A.4 states that the Golgi complex is a membrane-bound structure that "
          "consists of a series of flattened membrane sacs. The convoluted inner membrane "
          "belongs to mitochondria under EK 2.1.A.5 and the enzyme-filled sac to "
          "lysosomes under EK 2.1.A.6."),

 dict(q="Which functions does the course framework assign to the Golgi complex?",
      choices=[
        "Correctly folding and chemically modifying newly synthesized products, and "
        "packaging proteins for trafficking",
        "Synthesizing proteins from messenger RNA sequences",
        "Providing compartments for the reactions of aerobic cellular respiration",
        "Maintaining turgor pressure through water storage",
        "Detoxifying the cell and synthesizing lipids"],
      ans=0,
      why="EK 2.1.A.4 lists correctly folding and chemically modifying newly synthesized "
          "cellular products and packaging proteins for trafficking as Golgi functions. "
          "Protein synthesis from messenger RNA is the ribosome's job under EK 2.1.A.1."),

 dict(q="The course framework offers glycosylation as an illustrative example of what?",
      choices=[
        "A chemical modification of proteins that takes place within the Golgi and "
        "determines protein function or targeting",
        "A reaction of aerobic cellular respiration that takes place in the mitochondrion",
        "A way in which lysosomes bring about programmed cell death",
        "A method by which a plant vacuole stores nutrients",
        "A step in the synthesis of ribosomal RNA"],
      ans=0,
      why="The illustrative example printed with EK 2.1.A.4 is glycosylation and other "
          "chemical modifications of proteins that take place within the Golgi and "
          "determine protein function or targeting. It is attached to the Golgi statement "
          "and to no other."),

 dict(q="What does the double membrane of a mitochondrion provide, according to the "
        "course framework?",
      choices=[
        "Compartments for different metabolic reactions involved in aerobic cellular "
        "respiration",
        "A rigid boundary that protects the cell from osmotic lysis",
        "The site at which light energy is captured for photosynthesis",
        "A store of hydrolytic enzymes used to digest material",
        "Mechanical support that helps the whole cell maintain its shape"],
      ans=0,
      why="EK 2.1.A.5 states that mitochondria have a double membrane that provides "
          "compartments for different metabolic reactions involved in aerobic cellular "
          "respiration. Photosynthesis is the chloroplast's role in EK 2.1.A.8 and "
          "mechanical support the endoplasmic reticulum's in EK 2.1.A.3."),

 dict(q="How do the two mitochondrial membranes differ, and what does that difference "
        "enable?",
      choices=[
        "The outer membrane is smooth and the inner is highly convoluted, forming folds "
        "that enable ATP to be synthesized more efficiently.",
        "The outer membrane is highly convoluted and the inner is smooth, which slows the "
        "loss of ATP.",
        "Both membranes are smooth, and the difference between them is only in "
        "thickness.",
        "Both membranes are convoluted, which allows the organelle to change shape.",
        "The outer membrane is smooth and the inner is convoluted, which allows the "
        "mitochondrion to carry out photosynthesis."],
      ans=0,
      why="EK 2.1.A.5 states that the outer membrane is smooth while the inner membrane "
          "is highly convoluted, forming folds that enable ATP to be synthesized more "
          "efficiently. The rejected options reverse the two membranes or attach the "
          "wrong process to the folds."),

 dict(q="What does the course framework say lysosomes contain, and what do those contents "
        "do?",
      choices=[
        "Hydrolytic enzymes that digest material",
        "Ribosomal RNA that synthesizes protein",
        "Chlorophyll that captures light energy",
        "Stored water that maintains turgor pressure",
        "A double membrane that compartmentalizes respiration"],
      ans=0,
      why="EK 2.1.A.6 states that lysosomes are membrane-enclosed sacs that contain "
          "hydrolytic enzymes that digest material. Each rejected option names the "
          "contents or feature the framework assigns to a different organelle."),

 dict(q="Besides digestion, what other role does the course framework assign to "
        "lysosomes?",
      choices=[
        "A role in programmed cell death",
        "A role in the synthesis of lipids",
        "A role in the capture of light energy",
        "A role in maintaining the shape of the cell",
        "A role in the synthesis of ribosomal RNA"],
      ans=0,
      why="EK 2.1.A.6 states that lysosomes also play a role in programmed cell death, "
          "which it names as apoptosis. Lipid synthesis is smooth ER's under EK 2.1.A.3 "
          "ii and maintaining cell shape is endoplasmic reticulum's under EK 2.1.A.3."),

 dict(q="How does the course framework describe vacuoles in general?",
      choices=[
        "Membrane-bound sacs that play many different roles",
        "Non-membrane structures built from RNA and protein",
        "Double-membrane organelles dedicated to respiration",
        "Sacs whose only role is the digestion of engulfed material",
        "Flattened stacks of membrane that package proteins"],
      ans=0,
      why="EK 2.1.A.7 states that vacuoles are membrane-bound sacs that play many "
          "different roles. Confining them to one role contradicts the statement, and the "
          "non-membrane description belongs to ribosomes under EK 2.1.A.1."),

 dict(q="What does the course framework say about the specialized large vacuole of a "
        "plant cell?",
      choices=[
        "It maintains turgor pressure through nutrient and water storage.",
        "It contains hydrolytic enzymes that digest the cell's own material.",
        "It is the site at which the cell carries out photosynthesis.",
        "It provides compartments for aerobic cellular respiration.",
        "It packages proteins for trafficking out of the cell."],
      ans=0,
      why="EK 2.1.A.7 i states that in plant cells a specialized large vacuole maintains "
          "turgor pressure through nutrient and water storage. Photosynthesis is assigned "
          "to chloroplasts in EK 2.1.A.8 and digestion to lysosomes in EK 2.1.A.6."),

 dict(q="How does the course framework compare the vacuoles of animal cells with those of "
        "plant cells?",
      choices=[
        "Animal vacuoles are smaller in size and more plentiful, and they store cellular "
        "materials.",
        "Animal vacuoles are larger in size and less plentiful, and they maintain turgor "
        "pressure.",
        "Animal cells contain no vacuoles at all.",
        "Animal and plant vacuoles are identical in both size and number.",
        "Animal vacuoles are larger in size and more plentiful, and they carry out "
        "photosynthesis."],
      ans=0,
      why="EK 2.1.A.7 ii states that in animal cells vacuoles are smaller in size, are "
          "more plentiful than in plant cells, and store cellular materials. Turgor "
          "pressure is what EK 2.1.A.7 i assigns to the plant cell's large vacuole."),

 dict(q="Where are chloroplasts found, and what do they do?",
      choices=[
        "In plants and photosynthetic algae, where they serve as the location for "
        "photosynthesis",
        "In all cells in all forms of life, where they synthesize protein",
        "In animal cells only, where they store cellular materials",
        "In plants only, where they carry out aerobic cellular respiration",
        "In photosynthetic algae only, where they digest engulfed material"],
      ans=0,
      why="EK 2.1.A.8 states that chloroplasts are specialized organelles found in plants "
          "and photosynthetic algae and that they serve as the location for "
          "photosynthesis. Being found in all forms of life is what EK 2.1.A.1 says of "
          "ribosomes, not chloroplasts."),

 dict(q="Which two structures does the course framework describe as having a double "
        "membrane?",
      choices=[
        "Mitochondria and chloroplasts",
        "Ribosomes and lysosomes",
        "The Golgi complex and rough endoplasmic reticulum",
        "Vacuoles and transport vesicles",
        "The nuclear envelope and the ribosome"],
      ans=0,
      why="EK 2.1.A.5 gives mitochondria a double membrane and EK 2.1.A.8 gives "
          "chloroplasts a double membrane. Ribosomes are non-membrane structures under EK "
          "2.1.A.1, and the framework attributes no second membrane to the Golgi, "
          "vacuoles or vesicles."),

 dict(q="Which subcellular structure named in the course framework has no membrane of its "
        "own?",
      choices=["The ribosome", "The lysosome", "The Golgi complex", "The vacuole",
               "The chloroplast"],
      ans=0,
      why="EK 2.1.A.1 calls ribosomes non-membrane subcellular structures. Lysosomes are "
          "membrane-enclosed sacs under EK 2.1.A.6, vacuoles are membrane-bound sacs "
          "under EK 2.1.A.7, the Golgi is membrane-bound under EK 2.1.A.4, and "
          "chloroplasts carry a double membrane under EK 2.1.A.8."),

 dict(q="Four hypothetical cell types were counted for mitochondria and measured for "
        "their rate of aerobic cellular respiration, with the results in the table. Which "
        "conclusion is best supported?",
      table=_T_MITO,
      choices=[
        "Cell types with more mitochondria carried out aerobic cellular respiration at "
        "higher rates.",
        "Cell types with more mitochondria carried out aerobic cellular respiration at "
        "lower rates.",
        "Mitochondrial number had no measurable association with the rate of respiration.",
        "The cell type with the fewest mitochondria had the highest rate of respiration.",
        "Every cell type carried out respiration at the same rate."],
      ans=0,
      why="Ranking the four rows by mitochondrial number gives the same order as ranking "
          "them by respiration rate. EK 2.1.A.5 assigns the reactions of aerobic cellular "
          "respiration to the compartments of the mitochondrion, which is why the "
          "association is the expected one."),

 dict(q="Mitochondria from four hypothetical preparations were measured for inner "
        "membrane surface area and for ATP synthesis, with the results in the table. "
        "Which conclusion is best supported?",
      table=_T_CRISTAE,
      choices=[
        "Preparations with more inner membrane area synthesized more ATP per minute.",
        "Preparations with more inner membrane area synthesized less ATP per minute.",
        "Inner membrane area was unrelated to the rate of ATP synthesis.",
        "The preparation with the least inner membrane area synthesized the most ATP.",
        "ATP synthesis depended on the smoothness of the outer membrane rather than on "
        "the inner membrane."],
      ans=0,
      why="ATP synthesis rises at every step as inner membrane area rises across the four "
          "preparations. EK 2.1.A.5 states that the folds of the highly convoluted inner "
          "membrane enable ATP to be synthesized more efficiently, and the outer membrane "
          "is described as smooth rather than as the site of that synthesis."),

 dict(q="Using the same inner membrane measurements, what happens to the amount of ATP "
        "synthesized per square micrometer of inner membrane as the area increases?",
      table=_T_CRISTAE,
      choices=[
        "It stays roughly constant, at about five arbitrary units per square micrometer.",
        "It roughly doubles with each increase in area.",
        "It falls to roughly half with each increase in area.",
        "It rises from about one to about twenty across the four preparations.",
        "It cannot be calculated from the values given."],
      ans=0,
      why="Dividing the ATP column by the area column gives nearly the same value for "
          "every preparation, so the total rises in proportion to the area rather than "
          "faster or slower. That is what makes the added folds of EK 2.1.A.5 an "
          "efficiency gain rather than an arbitrary association."),

 dict(q="A plant cell and an animal cell were measured for the number and size of their "
        "vacuoles, with the results in the table. Which statement is supported by the "
        "data?",
      table=_T_VACUOLE,
      choices=[
        "The animal cell contained more vacuoles, and its largest vacuole was smaller.",
        "The animal cell contained fewer vacuoles, and its largest vacuole was larger.",
        "The two cells contained the same number of vacuoles.",
        "The plant cell contained more vacuoles, each of them smaller.",
        "Neither cell contained any vacuole large enough to measure."],
      ans=0,
      why="The table records more vacuoles in the animal cell and a far larger single "
          "vacuole in the plant cell, which is exactly the comparison EK 2.1.A.7 ii draws "
          "when it says animal vacuoles are smaller in size and more plentiful than in "
          "plant cells."),

 dict(q="Four hypothetical cell lines differing in the hydrolytic enzyme activity of "
        "their lysosomes were measured for accumulated undigested material, with the "
        "results in the table. Which conclusion is best supported?",
      table=_T_LYSO,
      choices=[
        "Lines with less hydrolytic enzyme activity accumulated more undigested material.",
        "Lines with less hydrolytic enzyme activity accumulated less undigested material.",
        "Enzyme activity was unrelated to the accumulation of undigested material.",
        "The line with the greatest enzyme activity accumulated the most undigested "
        "material.",
        "Every line accumulated the same amount of undigested material."],
      ans=0,
      why="Accumulation rises at every step as enzyme activity falls across the four "
          "lines. EK 2.1.A.6 states that lysosomes contain hydrolytic enzymes that digest "
          "material, so less of that activity leaves more material undigested."),

 dict(q="A drug prevents the hydrolytic enzymes of a cell's lysosomes from functioning. "
        "Which outcome is predicted most directly by the course framework?",
      choices=[
        "Material the cell would normally digest will accumulate inside it.",
        "The cell will lose the ability to synthesize protein from messenger RNA.",
        "The cell will be unable to carry out photosynthesis.",
        "The cell's mitochondria will lose their inner membrane folds.",
        "The cell will begin to build a large central vacuole."],
      ans=0,
      why="EK 2.1.A.6 states that lysosomes contain hydrolytic enzymes that digest "
          "material, so removing that activity removes the digestion. Protein synthesis "
          "belongs to ribosomes under EK 2.1.A.1 and photosynthesis to chloroplasts under "
          "EK 2.1.A.8, neither of which the drug touches."),

 dict(q="A liver cell is exposed to a compound the cell must detoxify. Which subcellular "
        "component would be expected to increase in abundance, and why?",
      choices=[
        "Smooth endoplasmic reticulum, because the framework assigns detoxification of "
        "cells to it",
        "Rough endoplasmic reticulum, because the framework assigns detoxification of "
        "cells to it",
        "Chloroplasts, because they are the site of photosynthesis",
        "Ribosomes, because they synthesize proteins from messenger RNA",
        "The plant cell's large central vacuole, because it stores nutrients and water"],
      ans=0,
      why="EK 2.1.A.3 ii names the detoxification of cells among the functions of smooth "
          "endoplasmic reticulum, while EK 2.1.A.3 i gives rough ER membrane-bound "
          "ribosomes and protein synthesis instead. The distinction between the two "
          "sub-points is what the question turns on."),

 dict(q="A cell secretes very large quantities of protein. Which subcellular component "
        "would be expected to be especially abundant in it, and on what grounds?",
      choices=[
        "Rough endoplasmic reticulum, because it is associated with membrane-bound "
        "ribosomes and helps carry out protein synthesis",
        "Smooth endoplasmic reticulum, because it carries out lipid synthesis",
        "Chloroplasts, because they are the location for photosynthesis",
        "The large central vacuole, because it maintains turgor pressure",
        "The outer mitochondrial membrane, because it is smooth"],
      ans=0,
      why="EK 2.1.A.3 i states that rough ER is associated with membrane-bound ribosomes "
          "and helps carry out protein synthesis, and EK 2.1.A.1 makes ribosomes the "
          "structures that synthesize proteins. Lipid synthesis is the smooth ER's role "
          "in EK 2.1.A.3 ii."),

 dict(q="A newly synthesized protein is found to be chemically modified and then enclosed "
        "for delivery elsewhere in the cell. Which component of the endomembrane system "
        "does the course framework credit with those two steps?",
      choices=[
        "The Golgi complex",
        "The lysosome",
        "The mitochondrion",
        "The ribosome",
        "The chloroplast"],
      ans=0,
      why="EK 2.1.A.4 gives the Golgi both functions: correctly folding and chemically "
          "modifying newly synthesized cellular products, and packaging proteins for "
          "trafficking. EK 2.1.A.2 places the Golgi inside the endomembrane system, which "
          "is what the stem specifies."),
]
