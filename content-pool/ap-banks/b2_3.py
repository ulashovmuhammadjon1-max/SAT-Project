# AP BIOLOGY 2.3 Plasma Membrane
# CED effective Fall 2025, Unit 2 Cells. Big Idea 2 Energetics.
# Learning objectives 2.3.A, describe the roles of each of the components of the cell
# membrane in maintaining the internal environment of the cell, and 2.3.B, describe the
# fluid mosaic model of cell membranes. Suggested skill 2.A.
#
# Essential knowledge relied on, in the framework's own words:
#   2.3.A.1    Phospholipids have both hydrophilic and hydrophobic regions. The polar
#              hydrophilic phosphate regions of the phospholipids are oriented toward
#              the aqueous external or internal environment, while the nonpolar
#              hydrophobic fatty acid regions face each other within the interior of
#              the membrane.
#   2.3.A.2    Embedded proteins can be hydrophilic (with charged and polar side
#              groups), hydrophobic (with nonpolar side groups), or both.
#     i.       Hydrophilic regions of the proteins are either inside the interior of
#              the protein or exposed to the cytosol (cytoplasm).
#     ii.      Hydrophobic regions of proteins make up the protein surface that
#              interacts with the fatty acids in the interior membrane.
#   2.3.B.1    Plasma membranes consist of a structural framework of phospholipid
#              molecules embedded with proteins, steroids (such as cholesterol in
#              vertebrate animals), glycoproteins, and glycolipids. All of these can
#              move around the surface of the cell within the membrane, as illustrated
#              by the fluid mosaic model.
#
# ON SCOPE. Selective permeability is topic 2.4 and every form of transport is topics
# 2.5 to 2.8; none of that is asked here. This module keys the COMPOSITION and the
# ORIENTATION of the membrane's parts and the fluid mosaic model, which is what
# EK 2.3.A.1, EK 2.3.A.2 and EK 2.3.B.1 state.
#
# ON THE DATA. Every table is labelled in its stem and every keyed conclusion is
# recoverable from the table alone and recomputed in verify_b2_3.py.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("2.3", "Plasma Membrane", 2)

_T_SEGMENTS = dict(
    headers=["Segment of one embedded membrane protein",
             "Chemical character of the side groups in that segment"],
    rows=[["Segment 1", "polar and charged"],
          ["Segment 2", "nonpolar"],
          ["Segment 3", "polar and charged"],
          ["Segment 4", "nonpolar"]])

_T_FLUIDITY = dict(
    headers=["Time after the membrane protein was labelled (minutes)",
             "Mean distance the labelled protein had moved within the membrane (micrometers)"],
    rows=[["0", "0.0"],
          ["10", "2.1"],
          ["20", "4.3"],
          ["30", "6.2"]])

_T_COMPOSITION = dict(
    headers=["Membrane component (hypothetical measurement)",
             "Percentage of all molecules in the membrane"],
    rows=[["Phospholipid", "55"],
          ["Protein", "25"],
          ["Cholesterol", "12"],
          ["Glycoprotein", "5"],
          ["Glycolipid", "3"]])

QUESTIONS = [

 dict(q="What does the course framework say about the regions of a phospholipid?",
      choices=[
        "It has both a hydrophilic region and a hydrophobic region.",
        "It is hydrophilic throughout its whole length.",
        "It is hydrophobic throughout its whole length.",
        "It has a hydrophilic region only when it sits in a membrane.",
        "It has neither a hydrophilic nor a hydrophobic region."],
      ans=0,
      why="EK 2.3.A.1 opens by stating that phospholipids have both hydrophilic and "
          "hydrophobic regions. That dual character is what allows one end to face water "
          "and the other to face away from it in the same molecule."),

 dict(q="Which part of a phospholipid is oriented toward the aqueous environment inside "
        "or outside the cell?",
      choices=[
        "The polar hydrophilic phosphate region",
        "The nonpolar hydrophobic fatty acid region",
        "The embedded protein attached to it",
        "The cholesterol molecule beside it",
        "The carbohydrate chain of a glycolipid"],
      ans=0,
      why="EK 2.3.A.1 states that the polar hydrophilic phosphate regions of the "
          "phospholipids are oriented toward the aqueous external or internal "
          "environment. The fatty acid regions are placed on the opposite side of that "
          "same sentence."),

 dict(q="Where do the nonpolar hydrophobic fatty acid regions of the phospholipids sit in "
        "a membrane?",
      choices=[
        "They face each other within the interior of the membrane.",
        "They face outward into the aqueous environment on both sides.",
        "They face the cytosol on one side and the external environment on the other.",
        "They lie flat along the outer surface of the membrane.",
        "They are found only where an embedded protein is absent."],
      ans=0,
      why="EK 2.3.A.1 states that the nonpolar hydrophobic fatty acid regions face each "
          "other within the interior of the membrane, which is the arrangement that keeps "
          "them away from the aqueous environment on either side."),

 dict(q="Why is the phosphate region of a phospholipid the part that faces the watery "
        "surroundings?",
      choices=[
        "It is polar and hydrophilic, so it is compatible with an aqueous environment.",
        "It is nonpolar and hydrophobic, so it is compatible with an aqueous "
        "environment.",
        "It is the largest part of the molecule, so it is pushed to the outside.",
        "It carries the fatty acid tails, which must remain in contact with water.",
        "It is attached to a protein, which anchors it at the membrane surface."],
      ans=0,
      why="EK 2.3.A.1 calls the phosphate regions polar and hydrophilic and states that "
          "they are oriented toward the aqueous external or internal environment. The "
          "second option attaches the correct orientation to the wrong chemical "
          "character, which EK 2.3.A.1 assigns to the fatty acid regions instead."),

 dict(q="What does the course framework say about the chemical character of proteins "
        "embedded in a membrane?",
      choices=[
        "They can be hydrophilic, hydrophobic, or both.",
        "They are always hydrophilic throughout.",
        "They are always hydrophobic throughout.",
        "They have no chemical character of their own, since they follow the "
        "phospholipids.",
        "They are hydrophilic in plants and hydrophobic in animals."],
      ans=0,
      why="EK 2.3.A.2 states that embedded proteins can be hydrophilic, with charged and "
          "polar side groups, hydrophobic, with nonpolar side groups, or both. Allowing "
          "all three possibilities is what makes a single protein able to span a membrane."),

 dict(q="Where does the course framework place the hydrophilic regions of an embedded "
        "membrane protein?",
      choices=[
        "Either inside the interior of the protein or exposed to the cytosol",
        "On the protein surface that touches the fatty acids in the membrane interior",
        "Only in the middle of the lipid bilayer",
        "Only on the outside of the cell and never facing the cytosol",
        "Distributed evenly over the whole protein surface"],
      ans=0,
      why="EK 2.3.A.2 i states that hydrophilic regions of the proteins are either inside "
          "the interior of the protein or exposed to the cytosol. The rejected first "
          "option is the location EK 2.3.A.2 ii assigns to the hydrophobic regions."),

 dict(q="Where does the course framework place the hydrophobic regions of an embedded "
        "membrane protein?",
      choices=[
        "On the protein surface that interacts with the fatty acids in the interior of "
        "the membrane",
        "Exposed to the cytosol on the inner face of the membrane",
        "Buried inside the interior of the protein and nowhere else",
        "On the outer surface of the cell, in contact with the external environment",
        "Wherever a carbohydrate chain is attached to the protein"],
      ans=0,
      why="EK 2.3.A.2 ii states that hydrophobic regions of proteins make up the protein "
          "surface that interacts with the fatty acids in the interior membrane. Exposure "
          "to the cytosol and burial inside the protein are what EK 2.3.A.2 i assigns to "
          "the hydrophilic regions."),

 dict(q="Which pairing of protein character with side groups matches the course "
        "framework?",
      choices=[
        "Hydrophilic proteins have charged and polar side groups; hydrophobic proteins "
        "have nonpolar side groups.",
        "Hydrophilic proteins have nonpolar side groups; hydrophobic proteins have "
        "charged and polar side groups.",
        "Both kinds have nonpolar side groups, and they differ only in size.",
        "Both kinds have charged side groups, and they differ only in position.",
        "Neither kind has side groups, because side groups belong to phospholipids."],
      ans=0,
      why="EK 2.3.A.2 pairs hydrophilic with charged and polar side groups and "
          "hydrophobic with nonpolar side groups in a single parenthetical. The rejected "
          "options swap the pairing or deny that proteins carry side groups at all, which "
          "EK 1.7.A.2 assigns to every amino acid."),

 dict(q="Which list matches the components the course framework says a plasma membrane "
        "consists of?",
      choices=[
        "A framework of phospholipids embedded with proteins, steroids, glycoproteins "
        "and glycolipids",
        "A framework of proteins embedded with phospholipids, nucleic acids and "
        "polysaccharides",
        "A framework of cellulose embedded with proteins and steroids",
        "A framework of glycolipids embedded with nucleic acids and steroids",
        "A framework of phospholipids alone, with nothing embedded in it"],
      ans=0,
      why="EK 2.3.B.1 states that plasma membranes consist of a structural framework of "
          "phospholipid molecules embedded with proteins, steroids such as cholesterol in "
          "vertebrate animals, glycoproteins, and glycolipids. Nucleic acids and "
          "cellulose appear nowhere in that list."),

 dict(q="Which steroid does the course framework name as a component of plasma membranes, "
        "and in what group of organisms?",
      choices=[
        "Cholesterol, in vertebrate animals",
        "Cholesterol, in bacteria only",
        "A phospholipid, in vertebrate animals",
        "A glycolipid, in all organisms",
        "A glycoprotein, in vertebrate animals"],
      ans=0,
      why="EK 2.3.B.1 names steroids, such as cholesterol in vertebrate animals, among "
          "the components embedded in the phospholipid framework. Glycolipids and "
          "glycoproteins are listed separately in the same sentence and are not steroids."),

 dict(q="What does the fluid mosaic model illustrate, according to the course framework?",
      choices=[
        "That the membrane's components can move around the surface of the cell within "
        "the membrane",
        "That the membrane's components are fixed rigidly in position once assembled",
        "That the membrane consists of a single layer of phospholipids",
        "That only proteins can move within the membrane, while lipids cannot",
        "That the membrane dissolves and reforms continuously"],
      ans=0,
      why="EK 2.3.B.1 ends by stating that all of these can move around the surface of "
          "the cell within the membrane, as illustrated by the fluid mosaic model. The "
          "word all is what rules out the option confining movement to proteins."),

 dict(q="Which class of molecule does the course framework identify as the structural "
        "framework of the plasma membrane?",
      choices=["Phospholipids", "Glycoproteins", "Steroids", "Glycolipids",
               "Nucleic acids"],
      ans=0,
      why="EK 2.3.B.1 states that plasma membranes consist of a structural framework of "
          "phospholipid molecules, with the other components embedded in that framework. "
          "The rejected options are named in the same sentence as the embedded "
          "components, or not named at all."),

 dict(q="Which two components named in the course framework's membrane list carry a "
        "carbohydrate portion in their names?",
      choices=[
        "Glycoproteins and glycolipids",
        "Phospholipids and steroids",
        "Proteins and steroids",
        "Phospholipids and glycoproteins",
        "Steroids and glycolipids"],
      ans=0,
      why="EK 2.3.B.1 lists proteins, steroids, glycoproteins, and glycolipids as "
          "embedded in the phospholipid framework, and the last two are the pair whose "
          "names carry the carbohydrate prefix. Nothing further about them is claimed by "
          "the framework."),

 dict(q="The table describes four segments of a single embedded membrane protein. Which "
        "segments would be expected to make up the protein surface that interacts with "
        "the fatty acids in the interior of the membrane?",
      table=_T_SEGMENTS,
      choices=[
        "Segment 2 and Segment 4",
        "Segment 1 and Segment 3",
        "Segment 1 and Segment 2",
        "Segment 3 and Segment 4",
        "All four segments"],
      ans=0,
      why="EK 2.3.A.2 ii states that hydrophobic regions of proteins make up the protein "
          "surface that interacts with the fatty acids in the interior membrane, and EK "
          "2.3.A.2 identifies hydrophobic regions by their nonpolar side groups. Exactly "
          "two segments in the table are recorded as nonpolar."),

 dict(q="Using the same four protein segments, which would be expected to lie inside the "
        "interior of the protein or to be exposed to the cytosol?",
      table=_T_SEGMENTS,
      choices=[
        "Segment 1 and Segment 3",
        "Segment 2 and Segment 4",
        "Segment 1 and Segment 2",
        "Segment 3 and Segment 4",
        "None of the segments"],
      ans=0,
      why="EK 2.3.A.2 i states that hydrophilic regions of the proteins are either inside "
          "the interior of the protein or exposed to the cytosol, and EK 2.3.A.2 "
          "identifies hydrophilic regions by their charged and polar side groups. Exactly "
          "two segments in the table are recorded that way."),

 dict(q="A membrane protein was labelled and the distance it had travelled within the "
        "membrane was measured over half an hour, with the results in the table. Which "
        "conclusion is best supported?",
      table=_T_FLUIDITY,
      choices=[
        "The labelled protein moved within the membrane over the course of the "
        "measurement.",
        "The labelled protein stayed in a fixed position within the membrane.",
        "The labelled protein moved only during the first ten minutes and then stopped.",
        "The labelled protein left the membrane entirely during the measurement.",
        "The measurement shows movement of the whole cell rather than of the protein."],
      ans=0,
      why="The recorded distance increases at every measurement, so the protein was still "
          "moving at the end of the period. EK 2.3.B.1 states that the membrane's "
          "components can move around the surface of the cell within the membrane, as "
          "illustrated by the fluid mosaic model."),

 dict(q="Using the same measurements, what was the approximate mean rate at which the "
        "labelled protein moved?",
      table=_T_FLUIDITY,
      choices=[
        "About 0.2 micrometers per minute",
        "About 2 micrometers per minute",
        "About 0.02 micrometers per minute",
        "About 6 micrometers per minute",
        "About 30 micrometers per minute"],
      ans=0,
      why="Dividing the total distance moved by the total time elapsed gives the mean "
          "rate directly from the table. The rejected values are the same figure off by a "
          "factor of ten, or the total distance and the total time reported as though "
          "they were rates."),

 dict(q="The table gives the proportions of the different kinds of molecule in a "
        "hypothetical plasma membrane. Which component is present in the largest "
        "proportion, and what role does the course framework give it?",
      table=_T_COMPOSITION,
      choices=[
        "Phospholipid, which forms the structural framework of the membrane",
        "Protein, which forms the structural framework of the membrane",
        "Cholesterol, which forms the structural framework of the membrane",
        "Glycoprotein, which forms the structural framework of the membrane",
        "Glycolipid, which forms the structural framework of the membrane"],
      ans=0,
      why="The phospholipid row carries the largest percentage in the table, and EK "
          "2.3.B.1 states that plasma membranes consist of a structural framework of "
          "phospholipid molecules with the other listed components embedded in it. Data "
          "and framework agree on the same component."),

 dict(q="According to the same table, what percentage of the membrane's molecules are "
        "something other than phospholipid?",
      table=_T_COMPOSITION,
      choices=["45 percent", "55 percent", "25 percent", "12 percent", "75 percent"],
      ans=0,
      why="The listed percentages account for the whole membrane, so subtracting the "
          "phospholipid share from 100 gives the rest. The 55 percent distractor is the "
          "phospholipid share itself and the 25 percent distractor is the protein share "
          "alone."),

 dict(q="A segment of a membrane protein that normally spans the interior of the bilayer "
        "is altered so that its side groups become charged and polar. Which prediction "
        "follows most directly from the course framework?",
      choices=[
        "That segment will no longer be suited to the surface that interacts with the "
        "fatty acids in the membrane interior.",
        "That segment will be more strongly attracted to the fatty acids in the membrane "
        "interior.",
        "The phospholipids around it will turn their phosphate regions inward to match "
        "it.",
        "The protein will leave the membrane and become a phospholipid.",
        "Nothing will change, because side groups have no bearing on where a protein "
        "region sits."],
      ans=0,
      why="EK 2.3.A.2 ii reserves the surface that interacts with the interior fatty "
          "acids for hydrophobic regions, and EK 2.3.A.2 identifies hydrophilic regions "
          "by exactly the charged and polar side groups described. EK 2.3.A.1 fixes the "
          "orientation of the phospholipids independently of any one protein."),

 dict(q="Phospholipids placed in water arrange themselves into a bilayer. Which "
        "explanation is best supported by the course framework?",
      choices=[
        "Their polar hydrophilic regions face the water on both sides while their "
        "nonpolar hydrophobic regions face each other in the interior.",
        "Their nonpolar hydrophobic regions face the water on both sides while their "
        "polar regions face each other in the interior.",
        "All parts of every phospholipid are attracted to water equally, so they spread "
        "into a single layer.",
        "The phospholipids form covalent bonds with the surrounding water molecules.",
        "The arrangement is set by the embedded proteins rather than by the "
        "phospholipids."],
      ans=0,
      why="EK 2.3.A.1 states that the polar hydrophilic phosphate regions are oriented "
          "toward the aqueous external or internal environment while the nonpolar "
          "hydrophobic fatty acid regions face each other within the interior of the "
          "membrane, and EK 1.5.A.2 iv states that phospholipids group together to form "
          "lipid bilayers."),

 dict(q="An embedded protein is described as being both hydrophilic and hydrophobic. "
        "Where would its two kinds of region be expected to sit?",
      choices=[
        "Its hydrophobic regions face the fatty acids in the membrane interior and its "
        "hydrophilic regions are buried in the protein or exposed to the cytosol.",
        "Its hydrophilic regions face the fatty acids in the membrane interior and its "
        "hydrophobic regions are exposed to the cytosol.",
        "Both kinds of region face the fatty acids in the membrane interior.",
        "Both kinds of region are exposed to the cytosol.",
        "Neither kind of region has a fixed position, since proteins move within the "
        "membrane."],
      ans=0,
      why="EK 2.3.A.2 allows a protein to be both, and its two sub-points then fix each "
          "kind of region: ii puts the hydrophobic regions on the surface that interacts "
          "with the interior fatty acids and i puts the hydrophilic regions inside the "
          "protein or exposed to the cytosol. Movement within the membrane under EK "
          "2.3.B.1 is lateral and does not reverse those placements."),

 dict(q="A student states that once a plasma membrane has been assembled, its components "
        "are locked in place. What is the best correction?",
      choices=[
        "The components can move around the surface of the cell within the membrane, "
        "which is what the fluid mosaic model illustrates.",
        "Only the phospholipids can move, while the proteins and steroids are fixed.",
        "Only the proteins can move, while the phospholipids are fixed.",
        "The components move by leaving the membrane and rejoining it elsewhere.",
        "The student is correct, since a mosaic is by definition a fixed pattern."],
      ans=0,
      why="EK 2.3.B.1 states that all of the listed components can move around the "
          "surface of the cell within the membrane, as illustrated by the fluid mosaic "
          "model. The word all rules out both options that confine movement to one class "
          "of component."),

 dict(q="Which description of the arrangement of phospholipids in a plasma membrane is "
        "consistent with the course framework?",
      choices=[
        "Two layers whose fatty acid regions face each other and whose phosphate regions "
        "face outward on both sides",
        "Two layers whose phosphate regions face each other and whose fatty acid regions "
        "face outward on both sides",
        "A single layer with the phosphate regions facing the cytosol",
        "A single layer with the fatty acid regions facing the cytosol",
        "Two layers arranged with the fatty acid regions of both layers facing the "
        "external environment"],
      ans=0,
      why="EK 2.3.A.1 orients the polar hydrophilic phosphate regions toward the aqueous "
          "external or internal environment and has the nonpolar hydrophobic fatty acid "
          "regions face each other within the interior of the membrane, which is the "
          "two-layer arrangement described."),

 dict(q="Which experimental result would provide the strongest evidence for the fluid "
        "mosaic model as the course framework describes it?",
      choices=[
        "Labelled membrane proteins and lipids are seen to change position within the "
        "membrane over time.",
        "Labelled membrane proteins are found in the same position at every time point "
        "measured.",
        "The membrane is shown to contain both phospholipids and proteins.",
        "The membrane is shown to have a hydrophobic interior.",
        "The membrane is shown to be thicker in some places than in others."],
      ans=0,
      why="EK 2.3.B.1 attaches the fluid mosaic model to the claim that all of the "
          "membrane's components can move around the surface of the cell within the "
          "membrane, so movement is what the evidence must show. Merely listing the "
          "components or reporting a hydrophobic interior tests EK 2.3.B.1's composition "
          "clause or EK 2.3.A.1 instead."),

 dict(q="A newly discovered protein has nonpolar side groups over its entire surface. "
        "Based on the course framework, where in a cell membrane would that protein be "
        "expected to sit?",
      choices=[
        "Entirely within the interior of the membrane, in contact with the fatty acid "
        "regions",
        "Entirely in the cytosol, away from the membrane",
        "Spanning the membrane with both ends exposed to water",
        "Attached to the outside of the cell by a carbohydrate chain",
        "Nowhere, because a protein cannot associate with a membrane unless it is "
        "hydrophilic"],
      ans=0,
      why="EK 2.3.A.2 identifies hydrophobic protein regions by their nonpolar side "
          "groups and EK 2.3.A.2 ii places those regions on the surface that interacts "
          "with the fatty acids in the interior membrane. A surface that is nonpolar "
          "throughout therefore has no region suited to the aqueous cytosol under EK "
          "2.3.A.2 i."),

 dict(q="Which statement about the interior of a plasma membrane follows from the course "
        "framework's account of phospholipid orientation?",
      choices=[
        "It is occupied by the nonpolar hydrophobic fatty acid regions of the two layers.",
        "It is occupied by the polar hydrophilic phosphate regions of the two layers.",
        "It is occupied by water drawn in from the cytosol.",
        "It is occupied only by embedded proteins, with no lipid present.",
        "It is empty space between two layers that do not touch."],
      ans=0,
      why="EK 2.3.A.1 states that the nonpolar hydrophobic fatty acid regions face each "
          "other within the interior of the membrane, while the phosphate regions are "
          "oriented toward the aqueous environments on either side."),

 dict(q="Two membranes are compared. One contains cholesterol among its lipids and the "
        "other does not. Which statement about that difference is supported by the course "
        "framework?",
      choices=[
        "Steroids such as cholesterol are named as a component of plasma membranes in "
        "vertebrate animals.",
        "Steroids such as cholesterol are named as the structural framework of every "
        "plasma membrane.",
        "Cholesterol is named as a kind of glycoprotein embedded in the membrane.",
        "Cholesterol is named as the component that carries out membrane transport.",
        "Cholesterol is named as a phospholipid with an unusually long fatty acid tail."],
      ans=0,
      why="EK 2.3.B.1 names steroids, such as cholesterol in vertebrate animals, among "
          "the components embedded in the phospholipid framework, and EK 1.5.A.2 ii calls "
          "steroids a class of lipid. The framework is the phospholipid layer under EK "
          "2.3.B.1, not the steroid."),

 dict(q="Which feature of a phospholipid explains why it can sit at the boundary between "
        "the watery cytosol and the water-free interior of a membrane?",
      choices=[
        "One end of the molecule is polar and hydrophilic while the other is nonpolar and "
        "hydrophobic.",
        "Both ends of the molecule are polar and hydrophilic.",
        "Both ends of the molecule are nonpolar and hydrophobic.",
        "The molecule carries a carbohydrate chain at each end.",
        "The molecule is held in place by covalent bonds to the proteins beside it."],
      ans=0,
      why="EK 2.3.A.1 states that phospholipids have both hydrophilic and hydrophobic "
          "regions and that the two are oriented in opposite directions, the phosphate "
          "region toward the aqueous environment and the fatty acid region toward the "
          "membrane interior. A molecule alike at both ends could not straddle that "
          "boundary."),

 dict(q="Which statement best summarizes the fluid mosaic model as the course framework "
        "presents it?",
      choices=[
        "A phospholipid framework carrying proteins, steroids, glycoproteins and "
        "glycolipids, all of which can move within the membrane",
        "A rigid protein framework carrying phospholipids that cannot move",
        "A single sheet of glycolipids with proteins attached only at its edges",
        "A phospholipid framework in which the components are fixed in a permanent "
        "pattern",
        "A double layer of proteins with phospholipids embedded between them"],
      ans=0,
      why="EK 2.3.B.1 combines both halves: plasma membranes consist of a structural "
          "framework of phospholipid molecules embedded with proteins, steroids, "
          "glycoproteins and glycolipids, and all of these can move around the surface of "
          "the cell within the membrane, as illustrated by the fluid mosaic model."),
]
