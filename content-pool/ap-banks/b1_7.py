# AP BIOLOGY 1.7 Proteins
# CED effective Fall 2025, Unit 1 Chemistry of Life. Big Idea 3 Information Storage
# and Transmission. Learning objective 1.7.A: describe the structure and function of
# proteins. Suggested skill 6.E, predict the causes or effects of a change in, or
# disruption to, one or more components in a biological system.
#
# Essential knowledge relied on, in the framework's own words:
#   1.7.A.1    Proteins comprise linear chains of amino acids connected by the
#              formation of covalent (peptide) bonds that form between a carboxyl group
#              of one amino acid and an amine group of the next amino acid, resulting
#              in a growing peptide chain.
#   1.7.A.2    Amino acids are composed of a central carbon atom with a hydrogen atom,
#              a carboxyl group, an amine group, and a variable R group covalently
#              bound to it. The R group of an amino acid can be categorized by three
#              possible chemical properties: hydrophobic/nonpolar, hydrophilic/polar,
#              or ionic. The interactions of these R groups determine the structure and
#              function of that region of the protein.
#   1.7.A.3    The specific sequence of amino acids in proteins determines the primary
#              structure of a polypeptide as well as the overall shape of the protein.
#              EXCLUSION STATEMENT -- The molecular structure of amino acids is beyond
#              the scope of the AP Exam.
#   1.7.A.4    Secondary structures of proteins are made through the local folding that
#              forms from interactions between atoms of the polypeptide backbone of the
#              amino acid chain. Hydrogen bonding forms shapes such as alpha helices
#              and beta pleated sheets.
#   1.7.A.5    The three-dimensional shape of the tertiary structure of a protein
#              results from the formation of hydrogen bonds, hydrophobic interactions,
#              ionic interactions, or disulfide bridges.
#   1.7.A.6    The quaternary structure arises from interactions between multiple
#              polypeptides. All four levels of a protein structure determine the
#              function of a protein.
#
# ON NOTATION. The CED prints the two functional groups as chemical formulas. Biology
# is exported as prose with no typesetting, so this bank writes "carboxyl group" and
# "amine group" in words throughout.
#
# ON THE DATA. Every table is labelled in its stem and every keyed conclusion follows
# from the table alone; each is recomputed in verify_b1_7.py. The framework prints no
# amino acid names and none is asked for -- its exclusion statement puts the molecular
# structure of amino acids outside the exam.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("1.7", "Proteins", 1)

_T_RESIDUES = dict(
    headers=["Position in the polypeptide chain",
             "Chemical property of the R group at that position"],
    rows=[["Position 12", "hydrophobic, that is nonpolar"],
          ["Position 27", "ionic"],
          ["Position 41", "hydrophilic, that is polar"],
          ["Position 58", "hydrophobic, that is nonpolar"],
          ["Position 63", "ionic"]])

_T_COMPOSITION = dict(
    headers=["Protein", "Amino acids with hydrophobic R groups",
             "Amino acids with hydrophilic R groups", "Amino acids with ionic R groups",
             "Total amino acids in the chain"],
    rows=[["Protein A", "120", "60", "20", "200"],
          ["Protein B", "40", "110", "50", "200"],
          ["Protein C", "150", "30", "20", "200"]])

_T_VARIANTS = dict(
    headers=["Protein variant",
             "Chemical property of the R group at position 40",
             "Enzyme activity (percentage of the unaltered protein)"],
    rows=[["Unaltered protein", "ionic", "100"],
          ["Variant 1", "ionic", "96"],
          ["Variant 2", "hydrophobic, that is nonpolar", "14"],
          ["Variant 3", "hydrophobic, that is nonpolar", "9"]])

QUESTIONS = [

 dict(q="What kind of bond connects one amino acid to the next in a polypeptide, "
        "according to the course framework?",
      choices=[
        "A covalent bond, also called a peptide bond",
        "A hydrogen bond between the two amino acids",
        "An ionic bond between two R groups",
        "A hydrophobic interaction between two nonpolar regions",
        "A disulfide bridge between two central carbon atoms"],
      ans=0,
      why="EK 1.7.A.1 states that proteins comprise linear chains of amino acids "
          "connected by the formation of covalent, that is peptide, bonds. Hydrogen "
          "bonds, ionic interactions, hydrophobic interactions and disulfide bridges "
          "appear in EK 1.7.A.4 and EK 1.7.A.5 as forces that fold an already connected "
          "chain."),

 dict(q="Between which two groups does the bond joining two amino acids form?",
      choices=[
        "The carboxyl group of one amino acid and the amine group of the next",
        "The amine group of one amino acid and the amine group of the next",
        "The R group of one amino acid and the R group of the next",
        "The central carbon of one amino acid and the central carbon of the next",
        "The carboxyl group of one amino acid and the R group of the next"],
      ans=0,
      why="EK 1.7.A.1 states that the covalent, peptide bonds form between a carboxyl "
          "group of one amino acid and an amine group of the next amino acid. The R "
          "groups are what EK 1.7.A.2 assigns to folding interactions, not to the bond "
          "that builds the chain."),

 dict(q="Which list gives the components of an amino acid as the course framework "
        "describes them?",
      choices=[
        "A central carbon atom bound to a hydrogen atom, a carboxyl group, an amine "
        "group, and a variable R group",
        "A central carbon atom bound to two hydrogen atoms and two carboxyl groups",
        "A five-carbon sugar, a phosphate, and a nitrogenous base",
        "A glycerol backbone bound to three fatty acid tails",
        "A central carbon atom bound only to an amine group and a variable R group"],
      ans=0,
      why="EK 1.7.A.2 states that amino acids are composed of a central carbon atom with "
          "a hydrogen atom, a carboxyl group, an amine group, and a variable R group "
          "covalently bound to it. The third option is EK 1.6.A.1's nucleotide."),

 dict(q="The course framework sorts R groups into how many chemical categories, and "
        "which are they?",
      choices=[
        "Three: hydrophobic or nonpolar, hydrophilic or polar, and ionic",
        "Two: polar and nonpolar only",
        "Three: saturated, unsaturated, and ionic",
        "Four: hydrophobic, hydrophilic, ionic, and covalent",
        "Two: acidic and basic only"],
      ans=0,
      why="EK 1.7.A.2 states that the R group of an amino acid can be categorized by "
          "three possible chemical properties: hydrophobic or nonpolar, hydrophilic or "
          "polar, or ionic. Saturated and unsaturated are the fatty acid categories of EK "
          "1.5.A.1."),

 dict(q="What do the interactions of the R groups determine, according to the course "
        "framework?",
      choices=[
        "The structure and function of that region of the protein",
        "The order in which amino acids are joined into the chain",
        "The number of polypeptides the protein contains",
        "Whether the chain is built from a carboxyl group or an amine group",
        "The elements from which the amino acids were assembled"],
      ans=0,
      why="EK 1.7.A.2 ends by stating that the interactions of these R groups determine "
          "the structure and function of that region of the protein. The order of the "
          "amino acids is the primary structure of EK 1.7.A.3 and is what those R groups "
          "follow from, not the reverse."),

 dict(q="What does the specific sequence of amino acids in a protein determine?",
      choices=[
        "The primary structure of the polypeptide and the overall shape of the protein",
        "The primary structure only, with the overall shape set independently",
        "The overall shape only, with the primary structure set independently",
        "Neither the primary structure nor the overall shape",
        "Only the number of polypeptides in the finished protein"],
      ans=0,
      why="EK 1.7.A.3 states that the specific sequence of amino acids in proteins "
          "determines the primary structure of a polypeptide as well as the overall shape "
          "of the protein. Both halves are in the same sentence, so separating them "
          "misreads it."),

 dict(q="How does the course framework describe the origin of a protein's secondary "
        "structure?",
      choices=[
        "Local folding formed by interactions between atoms of the polypeptide backbone, "
        "with hydrogen bonding producing shapes such as alpha helices",
        "Folding formed by interactions between R groups, with disulfide bridges "
        "producing shapes such as alpha helices",
        "Interactions between two or more separate polypeptides",
        "The order in which the amino acids were joined into the chain",
        "Covalent peptide bonds forming between distant parts of the chain"],
      ans=0,
      why="EK 1.7.A.4 states that secondary structures are made through the local folding "
          "that forms from interactions between atoms of the polypeptide backbone, and "
          "that hydrogen bonding forms shapes such as alpha helices and beta pleated "
          "sheets. R group interactions belong to the tertiary level in EK 1.7.A.5 and "
          "multiple polypeptides to the quaternary level in EK 1.7.A.6."),

 dict(q="Which set of interactions does the course framework name as producing the "
        "three-dimensional shape of a protein's tertiary structure?",
      choices=[
        "Hydrogen bonds, hydrophobic interactions, ionic interactions, or disulfide "
        "bridges",
        "Peptide bonds alone",
        "Interactions between two or more separate polypeptides",
        "Hydrogen bonds between atoms of the backbone only",
        "Covalent bonds between the central carbon atoms of distant amino acids"],
      ans=0,
      why="EK 1.7.A.5 states that the three-dimensional shape of the tertiary structure "
          "results from the formation of hydrogen bonds, hydrophobic interactions, ionic "
          "interactions, or disulfide bridges. Backbone-only hydrogen bonding is the "
          "secondary level of EK 1.7.A.4 and multiple polypeptides the quaternary level "
          "of EK 1.7.A.6."),

 dict(q="What gives rise to the quaternary structure of a protein?",
      choices=[
        "Interactions between multiple polypeptides",
        "Local folding within a single stretch of one polypeptide",
        "The order of amino acids within one polypeptide",
        "Peptide bonds between neighbouring amino acids",
        "The presence of a variable R group on every amino acid"],
      ans=0,
      why="EK 1.7.A.6 states that the quaternary structure arises from interactions "
          "between multiple polypeptides. Local folding within one chain is the secondary "
          "level of EK 1.7.A.4 and the order of amino acids is the primary level of EK "
          "1.7.A.3."),

 dict(q="How many levels of protein structure does the course framework say determine a "
        "protein's function?",
      choices=["All four of them", "Only the primary level", "Only the tertiary level",
               "Only the tertiary and quaternary levels",
               "None of them, because function depends only on the elements present"],
      ans=0,
      why="EK 1.7.A.6 ends by stating that all four levels of a protein structure "
          "determine the function of a protein. Singling out one or two levels contradicts "
          "that sentence directly."),

 dict(q="The exclusion statement attached to this topic places which of the following "
        "beyond the scope of the exam?",
      choices=[
        "The molecular structure of amino acids",
        "The three chemical categories of R group",
        "The bond that joins one amino acid to the next",
        "The four levels of protein structure",
        "The claim that sequence determines overall shape"],
      ans=0,
      why="The exclusion statement printed under EK 1.7.A.3 says that the molecular "
          "structure of amino acids is beyond the scope of the AP Exam. The rejected "
          "options restate content EK 1.7.A.1, EK 1.7.A.2, EK 1.7.A.3 and EK 1.7.A.6 do "
          "require."),

 dict(q="A protein is found to consist of two separate polypeptide chains bound to each "
        "other. Which level of structure does that association represent?",
      choices=["Quaternary structure", "Tertiary structure", "Secondary structure",
               "Primary structure", "No level of structure, since the chains are "
               "separate molecules"],
      ans=0,
      why="EK 1.7.A.6 states that the quaternary structure arises from interactions "
          "between multiple polypeptides, which is exactly what two associated chains "
          "are. The other three levels are described in EK 1.7.A.3, EK 1.7.A.4 and EK "
          "1.7.A.5 as properties of a single chain."),

 dict(q="Which comparison of the secondary and tertiary levels matches the course "
        "framework?",
      choices=[
        "The secondary level forms from interactions between backbone atoms, while the "
        "tertiary level also draws on hydrophobic, ionic and disulfide interactions.",
        "The secondary level forms from disulfide bridges, while the tertiary level forms "
        "from backbone hydrogen bonding alone.",
        "Both levels form only from interactions between separate polypeptides.",
        "Both levels form only from covalent peptide bonds along the chain.",
        "The secondary level forms from the order of amino acids, while the tertiary "
        "level forms from the number of chains."],
      ans=0,
      why="EK 1.7.A.4 confines the secondary level to local folding from interactions "
          "between atoms of the polypeptide backbone, with hydrogen bonding, while EK "
          "1.7.A.5 gives the tertiary level hydrogen bonds, hydrophobic interactions, "
          "ionic interactions and disulfide bridges."),

 dict(q="The table lists five positions in one polypeptide chain and the chemical "
        "category of the R group at each. Which pair of positions could form an ionic "
        "interaction with each other as the chain folds?",
      table=_T_RESIDUES,
      choices=[
        "Position 27 and Position 63",
        "Position 12 and Position 58",
        "Position 12 and Position 41",
        "Position 41 and Position 63",
        "No pair in the table could form an ionic interaction."],
      ans=0,
      why="EK 1.7.A.5 names ionic interactions among the forces producing tertiary "
          "structure, and EK 1.7.A.2 makes ionic one of the three R group categories. "
          "Exactly two positions in the table carry R groups in that category, so they "
          "are the only pair that can form such an interaction with each other."),

 dict(q="Using the same five positions, how many carry R groups in the hydrophobic "
        "category?",
      table=_T_RESIDUES,
      choices=["Two", "One", "Three", "Four", "Zero"],
      ans=0,
      why="Counting the rows assigned to the hydrophobic, that is nonpolar, category "
          "under EK 1.7.A.2's three-way classification gives the answer directly from the "
          "table. The other two categories account for the remaining three positions."),

 dict(q="Two of the positions in the same table carry R groups that would be expected to "
        "associate with each other away from the surrounding water. Which interaction "
        "named in the course framework would that be?",
      table=_T_RESIDUES,
      choices=[
        "A hydrophobic interaction between the two nonpolar R groups",
        "An ionic interaction between the two nonpolar R groups",
        "A disulfide bridge between the two polar R groups",
        "A peptide bond between the two nonpolar R groups",
        "A hydrogen bond between the two nonpolar R groups and the surrounding water"],
      ans=0,
      why="EK 1.7.A.5 names hydrophobic interactions among the forces producing tertiary "
          "structure, and EK 1.7.A.2 makes hydrophobic the same thing as nonpolar. The "
          "table carries exactly two positions in that category, and a peptide bond is "
          "reserved by EK 1.7.A.1 for the link between neighbouring amino acids."),

 dict(q="Three proteins of equal length were analyzed for the chemical categories of "
        "their R groups, with the results in the table. Which protein has the largest "
        "proportion of hydrophobic R groups?",
      table=_T_COMPOSITION,
      choices=["Protein C", "Protein A", "Protein B",
               "All three have the same proportion.",
               "The table does not allow the proportions to be compared."],
      ans=0,
      why="All three chains hold the same total number of amino acids, so the largest "
          "count of hydrophobic R groups is also the largest proportion. EK 1.7.A.2's "
          "three categories are what the columns record, so the comparison is one the "
          "table supports."),

 dict(q="For the protein in the table with 110 hydrophilic amino acids, what percentage "
        "of its amino acids carry R groups that are not hydrophobic?",
      table=_T_COMPOSITION,
      choices=["80 percent", "55 percent", "20 percent", "25 percent", "45 percent"],
      ans=0,
      why="The three R group categories of EK 1.7.A.2 account for every amino acid in the "
          "chain, so the share that is not hydrophobic is the hydrophilic and ionic "
          "counts added and divided by the total. The 55 percent distractor is the "
          "hydrophilic share alone."),

 dict(q="Which of the three proteins in the composition table would be expected to rely "
        "most heavily on hydrophobic interactions in forming its tertiary structure?",
      table=_T_COMPOSITION,
      choices=["Protein C", "Protein B", "Protein A",
               "All three would rely on them equally.",
               "None of them, because hydrophobic interactions do not affect tertiary "
               "structure."],
      ans=0,
      why="EK 1.7.A.5 names hydrophobic interactions among the forces producing the "
          "three-dimensional tertiary shape, and EK 1.7.A.2 makes the hydrophobic "
          "category an R group property. The chain with the most hydrophobic R groups out "
          "of an equal total therefore has the most opportunities for that interaction."),

 dict(q="An enzyme was altered at a single position and the activity of each variant was "
        "measured, with the results in the table. Which conclusion is best supported?",
      table=_T_VARIANTS,
      choices=[
        "Activity fell sharply only when the chemical category of the R group at that "
        "position changed.",
        "Activity fell sharply whenever any substitution was made at that position.",
        "Activity was unaffected by every substitution made at that position.",
        "Activity rose whenever the R group category changed.",
        "Activity depended on the total number of amino acids rather than on the "
        "substitution."],
      ans=0,
      why="The variant that kept the ionic category retained almost all activity, while "
          "both variants that moved the position to the hydrophobic category lost most of "
          "it. EK 1.7.A.2 states that the interactions of the R groups determine the "
          "structure and function of that region, and the chain length was not varied."),

 dict(q="In the same set of variants, one retained nearly the activity of the unaltered "
        "protein. What best explains that result in the framework's own terms?",
      table=_T_VARIANTS,
      choices=[
        "The substituted R group falls in the same chemical category, so the "
        "interactions available at that region are unchanged.",
        "The substituted R group falls in a different chemical category, which restored "
        "the original interactions.",
        "The substitution removed the peptide bond at that position, which had been "
        "blocking activity.",
        "The substitution changed the protein from two polypeptides to one.",
        "The substitution changed the sequence, and sequence has no bearing on shape."],
      ans=0,
      why="EK 1.7.A.2 sorts R groups into three chemical categories and makes their "
          "interactions the determinant of the structure and function of that region, so "
          "a substitution within one category leaves those interactions in place. EK "
          "1.7.A.3 makes sequence determine overall shape, which is why the final option "
          "is false."),

 dict(q="A single amino acid in the middle of a polypeptide is replaced by one whose R "
        "group falls in a different chemical category. Which outcome does the course "
        "framework support as a prediction?",
      choices=[
        "The interactions available in that region change, which can alter the shape and "
        "the function of the protein.",
        "The primary structure is unchanged, since only one position differs.",
        "The overall shape is guaranteed to be unchanged, since sequence does not "
        "determine shape.",
        "The protein gains an additional polypeptide chain.",
        "The peptide bonds along the backbone are converted into hydrogen bonds."],
      ans=0,
      why="EK 1.7.A.2 makes the interactions of the R groups determine the structure and "
          "function of that region, and EK 1.7.A.3 makes the specific sequence determine "
          "the primary structure and the overall shape. A changed position therefore "
          "changes the sequence and can propagate to shape and function."),

 dict(q="A disulfide bridge holds two distant parts of a single folded polypeptide "
        "together. Which level of structure does the course framework associate with that "
        "bridge?",
      choices=["Tertiary structure", "Secondary structure", "Primary structure",
               "Quaternary structure", "No level, since a bridge is not an interaction"],
      ans=0,
      why="EK 1.7.A.5 names disulfide bridges among the forces from which the "
          "three-dimensional shape of the tertiary structure results. EK 1.7.A.4 confines "
          "the secondary level to backbone hydrogen bonding and EK 1.7.A.6 confines the "
          "quaternary level to interactions between multiple polypeptides."),

 dict(q="An alpha helix and a beta pleated sheet are examples of which level of protein "
        "structure?",
      choices=["Secondary structure", "Primary structure", "Tertiary structure",
               "Quaternary structure", "They belong to no level of protein structure."],
      ans=0,
      why="EK 1.7.A.4 states that hydrogen bonding forms shapes such as alpha helices and "
          "beta pleated sheets in the local folding that makes the secondary structure of "
          "a protein. The framework names those two shapes at no other level."),

 dict(q="A functional protein consists of exactly one polypeptide chain. Which level of "
        "structure does it therefore lack?",
      choices=["Quaternary structure", "Tertiary structure", "Secondary structure",
               "Primary structure", "It lacks none of the four levels."],
      ans=0,
      why="EK 1.7.A.6 states that the quaternary structure arises from interactions "
          "between multiple polypeptides, so a protein with a single chain has no such "
          "interaction to give rise to it. The other three levels are described in EK "
          "1.7.A.3, EK 1.7.A.4 and EK 1.7.A.5 as features of one chain."),

 dict(q="Disulfide bridges are named as one of the forces that fold a protein. Which "
        "element assignment in the course framework is consistent with a protein forming "
        "such a bridge?",
      choices=[
        "That sulfur is used in the building of proteins",
        "That phosphorus is used in the building of nucleic acids",
        "That nitrogen is used in the building of nucleic acids",
        "That carbon is the most prevalent element in biological molecules",
        "That oxygen is one of the three most prevalent elements"],
      ans=0,
      why="EK 1.7.A.5 names disulfide bridges among the tertiary forces, and EK 1.2.A.1 i "
          "assigns sulfur specifically to the building of proteins. The other options "
          "name element assignments the framework makes to other classes or to biological "
          "molecules generally, none of which supplies a sulfur bridge."),

 dict(q="Hydrogen bonding appears in the course framework's account of more than one "
        "level of protein structure. Which statement describes that accurately?",
      choices=[
        "Hydrogen bonding acts between backbone atoms at the secondary level and is also "
        "one of several forces at the tertiary level.",
        "Hydrogen bonding acts only at the secondary level and plays no part at the "
        "tertiary level.",
        "Hydrogen bonding acts only at the tertiary level and plays no part at the "
        "secondary level.",
        "Hydrogen bonding is what joins one amino acid to the next along the chain.",
        "Hydrogen bonding is what holds two separate polypeptides together and does "
        "nothing within a chain."],
      ans=0,
      why="EK 1.7.A.4 attributes the local folding of the secondary level to hydrogen "
          "bonding between atoms of the polypeptide backbone, and EK 1.7.A.5 lists "
          "hydrogen bonds first among the forces producing the tertiary shape. The bond "
          "joining neighbouring amino acids is covalent under EK 1.7.A.1."),

 dict(q="A student states that the variable R group is part of the polypeptide backbone. "
        "Which correction is best supported by the course framework?",
      choices=[
        "The R group is bound to the central carbon of an amino acid, and the secondary "
        "level is described in terms of the backbone rather than the R groups.",
        "The R group is bound to the amine group, and it forms the peptide bond to the "
        "next amino acid.",
        "The R group is part of the backbone, and it is what hydrogen bonds at the "
        "secondary level.",
        "The R group is a separate molecule that is not bound to the amino acid at all.",
        "The R group is identical in every amino acid, so it cannot be distinguished "
        "from the backbone."],
      ans=0,
      why="EK 1.7.A.2 places the variable R group on the central carbon alongside a "
          "hydrogen atom, a carboxyl group and an amine group, and EK 1.7.A.4 describes "
          "the secondary level as folding from interactions between atoms of the "
          "polypeptide backbone. Calling the R group variable is itself the denial of the "
          "final option."),

 dict(q="A hydrophilic R group that normally sits on the outside of a folded protein, "
        "facing the surrounding water, is replaced by a hydrophobic one. Which prediction "
        "follows from the course framework?",
      choices=[
        "The interactions of that region with the surrounding water change, which can "
        "alter the structure and function of that region.",
        "Nothing changes, because R groups on the outside of a protein take part in no "
        "interactions.",
        "The peptide bonds on either side of that position are broken.",
        "The protein's primary structure is unaffected, since the chain is the same "
        "length.",
        "The protein automatically acquires an additional level of structure."],
      ans=0,
      why="EK 1.7.A.2 sorts R groups into hydrophobic, hydrophilic and ionic categories "
          "and states that the interactions of these R groups determine the structure and "
          "function of that region of the protein. A change of category is therefore a "
          "change in the available interactions, and EK 1.7.A.3 makes any changed position "
          "a change of sequence."),

 dict(q="Which ordering correctly matches each level of protein structure to what the "
        "course framework says produces it?",
      choices=[
        "Primary from the amino acid sequence, secondary from backbone interactions, "
        "tertiary from R group interactions and disulfide bridges, quaternary from "
        "multiple polypeptides",
        "Primary from backbone interactions, secondary from the amino acid sequence, "
        "tertiary from multiple polypeptides, quaternary from R group interactions",
        "Primary from multiple polypeptides, secondary from R group interactions, "
        "tertiary from the amino acid sequence, quaternary from backbone interactions",
        "Primary from R group interactions, secondary from multiple polypeptides, "
        "tertiary from the amino acid sequence, quaternary from backbone interactions",
        "All four levels arise from the same interactions between multiple polypeptides"],
      ans=0,
      why="The four statements line up one to one: EK 1.7.A.3 gives primary structure to "
          "the specific sequence of amino acids, EK 1.7.A.4 gives secondary structure to "
          "interactions between atoms of the backbone, EK 1.7.A.5 gives tertiary shape to "
          "hydrogen bonds, hydrophobic and ionic interactions and disulfide bridges, and "
          "EK 1.7.A.6 gives quaternary structure to interactions between multiple "
          "polypeptides."),
]
