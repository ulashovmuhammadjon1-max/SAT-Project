# AP BIOLOGY 1.3 Introduction to Macromolecules
# CED effective Fall 2025, Unit 1 Chemistry of Life. Big Idea 4 Systems Interactions.
# Learning objective 1.3.A: describe the chemical reactions that build and break
# biological macromolecules. Suggested skill 2.A.
#
# Essential knowledge relied on, in the framework's own words:
#   1.3.A.1    Hydrolysis is a chemical reaction involving the cleaving of covalent
#              bonds. This type of reaction breaks down molecules into smaller
#              molecules. When water is added to the bond between monomers in a
#              polymer, the bond is broken. The hydrogen ion from a water molecule is
#              added to one monomer and the hydroxyl group of the water molecule is
#              added to the other monomer, completing the reaction.
#   1.3.A.2    Dehydration synthesis occurs when two smaller molecules are joined
#              together through covalent bonding. A hydrogen ion is removed from one
#              monomer and a hydroxyl group is removed from the other. This causes the
#              loss of the equivalent of a water molecule from the reactants and the
#              connection of the two remaining monomers. The connection of many
#              monomers is known as polymerization.
#
# ON THE ARITHMETIC. Joining n monomers into one chain requires n minus 1 bonds, and
# EK 1.3.A.2 makes each bond cost the equivalent of one water molecule; EK 1.3.A.1
# makes the reverse consume one water per bond broken. Every quantitative item here is
# that single relation applied to numbers supplied in the stem or the table, and every
# one is recomputed in verify_b1_3.py. Nothing asks a student to recall a measured
# value; where a mass is needed the stem supplies it.
#
# ON SCOPE. This topic is the REACTIONS. Class-specific structure belongs to 1.4 to
# 1.7 and is not asked here; where a class is named it is only as an instance of the
# same two reactions.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("1.3", "Introduction to Macromolecules", 1)

_T_POLY = dict(
    headers=["Polymer", "Number of monomers joined into one unbranched chain"],
    rows=[["Polymer P", "4"],
          ["Polymer Q", "9"],
          ["Polymer R", "15"],
          ["Polymer S", "25"]])

_T_DIGEST = dict(
    headers=["Sample", "Number of monomers in the starting polymer",
             "Number of separate molecules present after hydrolysis is complete"],
    rows=[["Sample 1", "6", "6"],
          ["Sample 2", "11", "11"],
          ["Sample 3", "20", "20"]])

_T_MASS = dict(
    headers=["Reaction", "Total mass of the monomers before the reaction (daltons)",
             "Mass of the single polymer formed (daltons)"],
    rows=[["Reaction 1", "900", "864"],
          ["Reaction 2", "1,500", "1,446"],
          ["Reaction 3", "1,250", "1,178"],
          ["Reaction 4", "400", "382"]])

_T_TIMECOURSE = dict(
    headers=["Time (minutes)", "Number of intact polymer chains in the tube",
             "Number of free monomers in the tube"],
    rows=[["0", "100", "0"],
          ["15", "62", "190"],
          ["30", "24", "380"],
          ["45", "0", "500"]])

QUESTIONS = [

 dict(q="Hydrolysis is described by the course framework as a chemical reaction of which "
        "kind?",
      choices=[
        "One that cleaves covalent bonds and so breaks molecules down into smaller "
        "molecules",
        "One that forms covalent bonds and so builds molecules up into larger molecules",
        "One that cleaves hydrogen bonds between neighboring water molecules",
        "One that moves electrons from one molecule to another without breaking any bond",
        "One that changes a molecule's shape without altering any of its bonds"],
      ans=0,
      why="EK 1.3.A.1 opens by stating that hydrolysis is a chemical reaction involving "
          "the cleaving of covalent bonds and that this type of reaction breaks down "
          "molecules into smaller molecules. Building up is what EK 1.3.A.2 assigns to "
          "dehydration synthesis instead."),

 dict(q="In dehydration synthesis, what happens to the two monomers that become joined?",
      choices=[
        "A hydrogen ion is removed from one and a hydroxyl group from the other, and the "
        "two remaining monomers become connected.",
        "A hydrogen ion is added to one and a hydroxyl group to the other, and the two "
        "monomers separate.",
        "A whole water molecule is added between them and holds them together.",
        "Each monomer gains a hydrogen ion, and the two are then held together by "
        "hydrogen bonds.",
        "One monomer transfers an electron to the other, forming an ionic bond between "
        "them."],
      ans=0,
      why="EK 1.3.A.2 states that a hydrogen ion is removed from one monomer and a "
          "hydroxyl group is removed from the other, which causes the loss of the "
          "equivalent of a water molecule and the connection of the two remaining "
          "monomers. Adding rather than removing those groups is hydrolysis, EK 1.3.A.1."),

 dict(q="A cell is joining monomers into a long chain. Which statement about water "
        "during this process is correct?",
      choices=[
        "The equivalent of one water molecule is lost from the reactants for each bond "
        "formed.",
        "One water molecule is consumed from the surroundings for each bond formed.",
        "Water is neither lost nor consumed, because the bond forms between carbon atoms "
        "only.",
        "Two water molecules are lost for each bond formed, one from each monomer.",
        "Water is lost only when the very last monomer is added to the chain."],
      ans=0,
      why="EK 1.3.A.2 states that removing a hydrogen ion from one monomer and a hydroxyl "
          "group from the other causes the loss of the equivalent of a water molecule "
          "from the reactants. That accounting is per bond formed, and the hydrogen and "
          "the hydroxyl together make one water, not two."),

 dict(q="When a polymer is hydrolyzed, what becomes of the two parts of the water "
        "molecule that is added?",
      choices=[
        "The hydrogen ion joins one monomer and the hydroxyl group joins the other.",
        "The hydrogen ion and the hydroxyl group both join the same monomer.",
        "Both parts are released as gases and neither joins a monomer.",
        "The hydroxyl group joins one monomer and the remaining oxygen atom joins the "
        "other.",
        "The whole water molecule stays intact between the two separated monomers."],
      ans=0,
      why="EK 1.3.A.1 states that the hydrogen ion from a water molecule is added to one "
          "monomer and the hydroxyl group of the water molecule is added to the other "
          "monomer, completing the reaction. The water is therefore split between the two "
          "products rather than kept whole."),

 dict(q="The course framework gives a specific name to the connection of many monomers. "
        "What is that name?",
      choices=["Polymerization", "Hydrolysis", "Denaturation", "Condensation of water",
               "Diffusion"],
      ans=0,
      why="EK 1.3.A.2 ends by stating that the connection of many monomers is known as "
          "polymerization. Hydrolysis is the reverse reaction of EK 1.3.A.1, and the "
          "remaining terms name processes the framework treats elsewhere and not as the "
          "joining of monomers."),

 dict(q="Nine identical monomers are joined end to end into a single unbranched chain. "
        "How many water molecules are lost from the reactants in total?",
      choices=["Eight", "Nine", "Ten", "Seventeen", "One"],
      ans=0,
      why="Joining nine units into one chain takes eight bonds, and EK 1.3.A.2 makes each "
          "bond cost the equivalent of one water molecule from the reactants. Nine would "
          "be the count of monomers rather than bonds, and one would treat the whole "
          "chain as a single joining event."),

 dict(q="The table lists four unbranched polymers by the number of monomers joined to "
        "make each. Which polymer required the loss of exactly fourteen water molecules "
        "as it was assembled?",
      table=_T_POLY,
      choices=["Polymer R", "Polymer P", "Polymer Q", "Polymer S",
               "None of the four required exactly that number."],
      ans=0,
      why="A chain of n monomers holds n minus 1 bonds, and EK 1.3.A.2 costs one water "
          "equivalent per bond, so the polymer built from fifteen monomers accounts for "
          "fourteen. The other three rows give three, eight and twenty four, none of "
          "which is fourteen."),

 dict(q="Considering all four polymers in the table together, how many water molecules "
        "were lost in total during their assembly?",
      table=_T_POLY,
      choices=["49", "53", "45", "26", "63"],
      ans=0,
      why="Each chain costs one water equivalent per bond and holds one fewer bond than "
          "it has monomers, so the total is 3 plus 8 plus 14 plus 24. The 53 distractor "
          "is the raw sum of the monomer counts, which forgets that four separate chains "
          "each end one bond short."),

 dict(q="Which polymer in the table was assembled with the loss of exactly eight water "
        "molecules?",
      table=_T_POLY,
      choices=["Polymer Q", "Polymer P", "Polymer R", "Polymer S",
               "Two of the polymers match that number."],
      ans=0,
      why="Eight bonds join nine monomers, and EK 1.3.A.2 costs one water equivalent per "
          "bond. Only one row of the table records nine monomers, so no second polymer "
          "matches."),

 dict(q="Three samples were hydrolyzed until no bonds between monomers remained, with "
        "the results in the table. In which sample were the most water molecules "
        "consumed?",
      table=_T_DIGEST,
      choices=["Sample 3", "Sample 1", "Sample 2",
               "All three consumed the same number of water molecules.",
               "The table gives no way to compare them."],
      ans=0,
      why="EK 1.3.A.1 makes each bond broken consume one water molecule, and a chain of n "
          "monomers holds n minus 1 bonds, so water consumed rises with chain length. The "
          "largest starting chain in the table is therefore the answer, and the table "
          "does supply what the comparison needs."),

 dict(q="For the sample in the table whose starting polymer contained eleven monomers, "
        "how many water molecules were consumed in reaching complete hydrolysis?",
      table=_T_DIGEST,
      choices=["Ten", "Eleven", "Twelve", "Twenty two", "One"],
      ans=0,
      why="An eleven-unit chain holds ten bonds between monomers, and EK 1.3.A.1 adds one "
          "water molecule per bond broken. The eleven distractor counts monomers instead "
          "of bonds, which is the standard slip on this relation."),

 dict(q="In the same three samples, the number of separate molecules present after "
        "hydrolysis equals the number of monomers in the starting polymer. Why is that "
        "expected?",
      table=_T_DIGEST,
      choices=[
        "Complete hydrolysis breaks every bond between monomers, so each monomer ends up "
        "as its own molecule.",
        "Hydrolysis destroys some monomers, so the count after the reaction is always "
        "lower than the starting count.",
        "Each water molecule added becomes a separate product, so the count doubles.",
        "Hydrolysis joins monomers in pairs, so the count is halved.",
        "The number is a coincidence and would differ in any other sample."],
      ans=0,
      why="EK 1.3.A.1 states that hydrolysis cleaves the covalent bonds between monomers "
          "and breaks molecules down into smaller molecules. Once every such bond is "
          "cleaved, nothing joins one monomer to the next, and the framework describes no "
          "step that destroys or pairs monomers."),

 dict(q="Monomers were joined into single polymers in four separate reactions. The table "
        "gives the total mass of the monomers before each reaction and the mass of the "
        "polymer formed. Taking the mass of a water molecule as 18 daltons, in which "
        "reaction was the equivalent of exactly three water molecules lost?",
      table=_T_MASS,
      choices=["Reaction 2", "Reaction 1", "Reaction 3", "Reaction 4",
               "No reaction in the table lost exactly that amount."],
      ans=0,
      why="The mass lost is the difference between the two tabulated masses, and dividing "
          "by 18 daltons gives the number of water equivalents that EK 1.3.A.2 says are "
          "lost. Only one row gives a difference of 54, which is three water molecules."),

 dict(q="Using the same mass data and the same value of 18 daltons for a water molecule, "
        "how many monomers were joined in the reaction whose product has a mass of 1,178 "
        "daltons?",
      table=_T_MASS,
      choices=["Five", "Four", "Six", "Three", "Seven"],
      ans=0,
      why="That row loses 72 daltons, which is four water equivalents and therefore four "
          "bonds under EK 1.3.A.2. A chain holding four bonds between monomers contains "
          "five monomers, so the four distractor is the bond count reported as a monomer "
          "count."),

 dict(q="Among the four reactions in the mass table, which one joined the fewest monomers "
        "into its product?",
      table=_T_MASS,
      choices=["Reaction 4", "Reaction 1", "Reaction 2", "Reaction 3",
               "Two of the reactions joined equally few."],
      ans=0,
      why="Fewest monomers means fewest bonds, and the number of bonds is the mass lost "
          "divided by 18 daltons under EK 1.3.A.2. One row loses only 18 daltons, which "
          "is a single bond and therefore two monomers, and no other row matches it."),

 dict(q="A tube containing many identical polymer chains was held with an enzyme that "
        "hydrolyzes the bonds between monomers, and counts were taken over time as shown "
        "in the table. Which statement is best supported?",
      table=_T_TIMECOURSE,
      choices=[
        "As intact chains disappeared, free monomers accumulated.",
        "As intact chains disappeared, free monomers also disappeared.",
        "Both intact chains and free monomers increased throughout.",
        "Neither count changed measurably over the course of the experiment.",
        "Free monomers appeared only after every chain had already been destroyed."],
      ans=0,
      why="The table shows intact chains falling from 100 to zero while free monomers rise "
          "from zero to 500, and monomers are already present at the intermediate times. "
          "This is the pattern EK 1.3.A.1 predicts, since breaking the bonds within a "
          "chain releases its monomers."),

 dict(q="From the same time course, how many monomers did each original chain contain, on "
        "average?",
      table=_T_TIMECOURSE,
      choices=["Five", "Four", "Ten", "Two", "Fifty"],
      ans=0,
      why="Every chain has been hydrolyzed by the final row, so all monomers are free: 500 "
          "monomers came from 100 chains. Dividing gives the average length, and the "
          "distractors are the same two numbers combined by the wrong operation or read "
          "off the wrong row."),

 dict(q="A student claims that dehydration synthesis and hydrolysis both break covalent "
        "bonds. What is the best correction?",
      choices=[
        "Dehydration synthesis forms a covalent bond between monomers, while hydrolysis "
        "cleaves one.",
        "Dehydration synthesis cleaves a covalent bond, while hydrolysis forms one.",
        "Both reactions form covalent bonds, so no bond is ever broken in a cell.",
        "Neither reaction involves covalent bonds; both act on hydrogen bonds.",
        "The student is correct, because both reactions involve a water molecule."],
      ans=0,
      why="EK 1.3.A.2 describes dehydration synthesis as joining two smaller molecules "
          "through covalent bonding, and EK 1.3.A.1 describes hydrolysis as the cleaving "
          "of covalent bonds. Both involve water, but that shared feature is not what "
          "determines whether a bond is made or broken."),

 dict(q="An investigator supplies a cell with water in which the oxygen atoms are "
        "labelled, then isolates newly hydrolyzed monomers. Where would the label be "
        "expected to appear?",
      choices=[
        "In the hydroxyl group that has been added to one of the two monomers",
        "In the hydrogen ion that has been added to one of the two monomers",
        "Distributed evenly between both monomers, since water splits evenly",
        "Only in polymers that have not yet been hydrolyzed",
        "Nowhere, because the water molecule is released unchanged at the end"],
      ans=0,
      why="EK 1.3.A.1 splits the added water into a hydrogen ion, which goes to one "
          "monomer, and a hydroxyl group, which goes to the other. The oxygen atom is in "
          "the hydroxyl group, so a label on oxygen follows that half of the molecule."),

 dict(q="Which observation about a reaction mixture would most strongly indicate that "
        "polymerization rather than hydrolysis is taking place?",
      choices=[
        "The number of separate molecules in the mixture is falling while the average "
        "molecule is getting larger.",
        "The number of separate molecules in the mixture is rising while the average "
        "molecule is getting smaller.",
        "The total mass of the mixture is rising steadily.",
        "The temperature of the mixture is rising steadily.",
        "The number of separate molecules and their average size are both unchanged."],
      ans=0,
      why="EK 1.3.A.2 describes the connection of many monomers, which merges separate "
          "molecules into fewer and larger ones, while EK 1.3.A.1 describes breaking "
          "molecules down into smaller molecules, which does the reverse. Temperature and "
          "total mass do not distinguish the two directions."),

 dict(q="Why can a bond between two monomers in a polymer not be broken in a completely "
        "dry environment, according to the course framework?",
      choices=[
        "The reaction that cleaves that bond works by adding water across it.",
        "The bond between monomers is a hydrogen bond, and hydrogen bonds require liquid "
        "water to exist.",
        "Dry conditions cause monomers to fuse permanently into a single molecule.",
        "The bond can only be broken by removing a hydrogen ion and a hydroxyl group from "
        "the polymer.",
        "Water raises the temperature of the mixture, and heat alone breaks the bond."],
      ans=0,
      why="EK 1.3.A.1 defines the reaction by the addition of water to the bond between "
          "monomers, with the hydrogen ion going to one monomer and the hydroxyl group to "
          "the other. Removing those groups instead is dehydration synthesis, EK 1.3.A.2, "
          "which is the reaction that builds the bond."),

 dict(q="Two monomers react to form a single larger molecule. Which set of products is "
        "consistent with the course framework's description?",
      choices=[
        "One molecule containing both monomers, plus one water molecule",
        "One molecule containing both monomers, plus two water molecules",
        "Two separate monomers, plus one water molecule",
        "One molecule containing both monomers, with no other product",
        "Two separate monomers, with no other product"],
      ans=0,
      why="EK 1.3.A.2 states that joining two smaller molecules removes a hydrogen ion "
          "from one and a hydroxyl group from the other, causing the loss of the "
          "equivalent of one water molecule. One bond therefore accounts for exactly one "
          "water, and the monomers end connected rather than separate."),

 dict(q="A researcher builds a polymer from monomers and then hydrolyzes it completely "
        "back to the same monomers. Which statement about the water involved is correct?",
      choices=[
        "The number of water equivalents lost during assembly equals the number consumed "
        "during hydrolysis.",
        "Twice as much water is consumed during hydrolysis as was lost during assembly.",
        "Water is lost in both directions, so the mixture becomes progressively drier.",
        "Water is consumed in both directions, so the mixture becomes progressively "
        "wetter.",
        "No water is involved in either direction once the monomers are identical."],
      ans=0,
      why="Both statements are per bond: EK 1.3.A.2 loses the equivalent of one water for "
          "each bond formed and EK 1.3.A.1 adds one water for each bond cleaved. The same "
          "number of bonds is formed and cleaved, so the two counts match, and the two "
          "reactions run in opposite directions rather than the same one."),

 dict(q="A branched polymer contains twenty monomers held together by nineteen bonds "
        "between monomers. How many water equivalents were lost as it was assembled?",
      choices=["Nineteen", "Twenty", "Thirty eight", "Ten", "One"],
      ans=0,
      why="EK 1.3.A.2 costs the equivalent of one water molecule per bond formed between "
          "monomers, and the stem supplies the bond count directly. Branching changes how "
          "the bonds are arranged, not the one-water-per-bond accounting, so the answer "
          "follows from the nineteen bonds and not from the twenty monomers."),

 dict(q="What is the relationship between a monomer and a polymer as the course framework "
        "uses the two terms?",
      choices=[
        "A polymer is many monomers connected together, and connecting them is called "
        "polymerization.",
        "A monomer is many polymers connected together, and connecting them is called "
        "hydrolysis.",
        "A polymer and a monomer are two names for the same molecule at different "
        "temperatures.",
        "A polymer is a monomer that has absorbed a water molecule.",
        "A monomer is a fragment of a polymer that has lost all of its covalent bonds."],
      ans=0,
      why="EK 1.3.A.2 states that the connection of many monomers is known as "
          "polymerization, and EK 1.3.A.1 speaks of the bond between monomers in a "
          "polymer. The terms therefore name the unit and the assembly, not two states of "
          "one molecule."),

 dict(q="An enzyme in the digestive tract is blocked so that it can no longer catalyze "
        "the addition of water across the bonds between monomers in food polymers. Which "
        "outcome is predicted most directly?",
      choices=[
        "Fewer free monomers will be released from the food polymers.",
        "More free monomers will be released, because the polymers become unstable.",
        "The polymers will be converted directly into water and carbon dioxide.",
        "The polymers will lengthen, because dehydration synthesis will take over.",
        "The food polymers will pass through unchanged in mass but fully separated into "
        "monomers."],
      ans=0,
      why="Adding water across the bond between monomers is precisely the reaction EK "
          "1.3.A.1 describes, and it is what liberates the monomers. Blocking it removes "
          "the route to free monomers; nothing in the framework makes an unhydrolyzed "
          "polymer lengthen or decompose by another path."),

 dict(q="A chemist reports that in one reaction a hydrogen ion and a hydroxyl group were "
        "removed from two different starting molecules. Which reaction is being "
        "described, and what is the immediate consequence?",
      choices=[
        "Dehydration synthesis, and the two remaining molecules become covalently "
        "connected",
        "Hydrolysis, and the two remaining molecules become covalently connected",
        "Dehydration synthesis, and the two remaining molecules move apart from each "
        "other",
        "Hydrolysis, and the starting molecule is split into two",
        "Neither reaction, because removing those groups does not change any bond"],
      ans=0,
      why="EK 1.3.A.2 states that a hydrogen ion is removed from one monomer and a "
          "hydroxyl group from the other, causing the loss of the equivalent of a water "
          "molecule and the connection of the two remaining monomers. Removal is the "
          "signature of the synthesis direction; addition is the signature of hydrolysis "
          "in EK 1.3.A.1."),

 dict(q="Which pair of changes would both be expected in a sealed tube in which "
        "polymerization is proceeding and no other reaction is occurring?",
      choices=[
        "The count of separate molecules falls and the amount of free water rises.",
        "The count of separate molecules rises and the amount of free water falls.",
        "The count of separate molecules falls and the amount of free water also falls.",
        "The count of separate molecules rises and the amount of free water also rises.",
        "Neither the count of separate molecules nor the amount of free water changes."],
      ans=0,
      why="EK 1.3.A.2 merges monomers into fewer, larger molecules and releases the "
          "equivalent of a water molecule for each bond formed, so the two changes run in "
          "opposite directions. The reverse pattern belongs to hydrolysis under EK "
          "1.3.A.1, which splits molecules and takes water up."),

 dict(q="Two of the four classes of biological molecule are assembled from repeating "
        "monomers. What does the course framework's account of these reactions imply "
        "about how those different classes are built?",
      choices=[
        "The same pair of reactions builds and breaks the bonds between monomers "
        "regardless of which class the monomers belong to.",
        "Each class is built by a different chemical reaction unique to that class.",
        "Only one class is built by dehydration synthesis, and the others form without "
        "any reaction.",
        "The bonds between monomers are covalent in one class and hydrogen bonds in the "
        "others.",
        "Polymers of different classes cannot be broken down once they have formed."],
      ans=0,
      why="EK 1.3.A.1 and EK 1.3.A.2 are written about monomers and polymers in general "
          "rather than about any one class, and the topic sits ahead of the "
          "class-specific topics that follow. The framework states no class-specific "
          "alternative reaction and no class exempt from hydrolysis."),

 dict(q="A student writes that hydrolysis 'adds a whole water molecule to the polymer, "
        "which then falls apart on its own'. Which part of that description conflicts "
        "with the course framework?",
      choices=[
        "The water does not stay whole: it is split, with the hydrogen ion going to one "
        "monomer and the hydroxyl group to the other.",
        "Water is not involved in hydrolysis at all, so the whole description is "
        "irrelevant.",
        "The polymer does not fall apart into smaller molecules, it becomes larger.",
        "Hydrolysis removes rather than adds a hydrogen ion and a hydroxyl group.",
        "Hydrolysis acts on hydrogen bonds, so no covalent bond is cleaved."],
      ans=0,
      why="EK 1.3.A.1 states that the hydrogen ion from a water molecule is added to one "
          "monomer and the hydroxyl group of the water molecule to the other, which is "
          "the step the student's description leaves out. The rest of the description, "
          "that water is added and the polymer breaks into smaller molecules, matches the "
          "statement."),
]
