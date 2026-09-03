# AP BIOLOGY 1.4 Carbohydrates
# CED effective Fall 2025, Unit 1 Chemistry of Life. Big Idea 4 Systems Interactions.
# Learning objective 1.4.A: describe the structure and function of carbohydrates.
# Suggested skill 1.A, describe biological concepts and processes.
#
# Essential knowledge relied on -- the topic has exactly one statement:
#   1.4.A.1    Monosaccharides (simple sugars) are the monomers for polysaccharides
#              (complex carbohydrates). These monomers are connected by covalent bonds
#              to form polymers such as complex carbohydrates, which may be linear or
#              branched.
#              EXCLUSION STATEMENT -- The molecular structure of specific carbohydrate
#              polymers is beyond the scope of the AP Exam.
#              Illustrative examples: cellulose, starch, glycogen.
#
# WHAT THIS BANK DELIBERATELY DOES NOT ASK. The CED lists cellulose, starch and
# glycogen as illustrative examples and states NO function and NO structure for any of
# them, and the exclusion statement puts the molecular structure of specific
# carbohydrate polymers outside the exam. So no item here keys "starch is the storage
# form in plants" or "glycogen is branched" -- those are textbook facts the framework
# does not print. The three names are used only as instances of the one thing EK
# 1.4.A.1 does say about them: they are polymers built from monosaccharide monomers.
#
# WHERE ITEMS REACH OUTSIDE THE TOPIC they chain explicitly and the claim says so:
# EK 1.3.A.1 and EK 1.3.A.2 for the reactions that build and break the bonds, EK
# 1.2.A.1 for the elements, EK 1.7.A.1 for the parallel with polypeptides.
#
# ON OVERLAP WITH 1.3. That topic carries the water accounting; this one uses the bond
# count only twice, and one of those two turns on branching, which 1.3 does not treat.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("1.4", "Carbohydrates", 1)

_T_CARBS = dict(
    headers=["Carbohydrate sample", "Number of monosaccharide units in one molecule",
             "Shape of the connected chain"],
    rows=[["Sample J", "1", "not applicable"],
          ["Sample K", "300", "unbranched"],
          ["Sample L", "12,000", "branched"],
          ["Sample M", "2,000", "unbranched"]])

_T_HYDROLYSIS = dict(
    headers=["Sample", "Kinds of simple sugar recovered after complete hydrolysis",
             "Total number of simple sugar molecules recovered"],
    rows=[["Sample P", "1", "1"],
          ["Sample Q", "1", "740"],
          ["Sample R", "3", "520"],
          ["Sample S", "2", "2"]])

_T_ENDS = dict(
    headers=["Polysaccharide", "Number of monosaccharide units",
             "Number of chain ends counted on one molecule"],
    rows=[["Polymer T", "1,000", "2"],
          ["Polymer U", "1,000", "64"],
          ["Polymer V", "1,000", "2"],
          ["Polymer W", "1,000", "310"]])

QUESTIONS = [

 dict(q="According to the course framework, what is the monomer from which a "
        "polysaccharide is built?",
      choices=["A monosaccharide", "An amino acid", "A nucleotide", "A fatty acid",
               "A phospholipid"],
      ans=0,
      why="EK 1.4.A.1 states that monosaccharides, also called simple sugars, are the "
          "monomers for polysaccharides. The other four are the building units the "
          "framework assigns to other classes of molecule in EK 1.5.A.1, EK 1.6.A.1 and "
          "EK 1.7.A.1."),

 dict(q="The course framework gives a second name for each of two terms in this topic. "
        "Which pairing is the one it uses?",
      choices=[
        "Monosaccharides are simple sugars, and polysaccharides are complex "
        "carbohydrates.",
        "Monosaccharides are complex carbohydrates, and polysaccharides are simple "
        "sugars.",
        "Monosaccharides are simple sugars, and polysaccharides are amino acid chains.",
        "Monosaccharides are nucleotides, and polysaccharides are complex carbohydrates.",
        "Monosaccharides are polymers, and polysaccharides are monomers."],
      ans=0,
      why="EK 1.4.A.1 gives both parenthetical names in one sentence: monosaccharides "
          "(simple sugars) are the monomers for polysaccharides (complex carbohydrates). "
          "The remaining options invert the pair or borrow a name from another class."),

 dict(q="What kind of bond connects one monosaccharide to the next within a "
        "polysaccharide?",
      choices=["A covalent bond", "A hydrogen bond", "An ionic bond",
               "A hydrophobic interaction", "A disulfide bridge"],
      ans=0,
      why="EK 1.4.A.1 states that these monomers are connected by covalent bonds to form "
          "polymers. Hydrogen bonds and hydrophobic and ionic interactions appear in EK "
          "1.7.A.4 and EK 1.7.A.5 as forces that shape a folded protein, not as the link "
          "between sugar monomers."),

 dict(q="Which statement about the shape of complex carbohydrates matches the course "
        "framework?",
      choices=[
        "They may be linear or branched.",
        "They are always linear.",
        "They are always branched.",
        "They are always coiled into a helix.",
        "They have no consistent shape because they contain no bonds between monomers."],
      ans=0,
      why="EK 1.4.A.1 ends by saying that the polymers formed may be linear or branched, "
          "which allows both and requires neither. A helix is what EK 1.6.A.3 and EK "
          "1.7.A.4 describe for nucleic acids and for protein secondary structure."),

 dict(q="Cellulose, starch and glycogen are listed in the course framework as examples of "
        "which of the following?",
      choices=[
        "Polymers built from monosaccharide monomers",
        "Monomers from which polysaccharides are built",
        "Proteins built from amino acid monomers",
        "Lipids that group together to form bilayers",
        "Nucleic acids that encode biological information"],
      ans=0,
      why="The three names appear as illustrative examples for EK 1.4.A.1, whose subject "
          "is polymers such as complex carbohydrates formed by connecting monosaccharide "
          "monomers. Nothing in the framework assigns them to another class."),

 dict(q="The course framework carries an exclusion statement for this topic. Which "
        "expectation does it rule out?",
      choices=[
        "Knowing the molecular structure of specific carbohydrate polymers",
        "Knowing that monosaccharides are the monomers for polysaccharides",
        "Knowing that the monomers are joined by covalent bonds",
        "Knowing that a complex carbohydrate may be branched",
        "Knowing that carbohydrates are one of the classes organisms build"],
      ans=0,
      why="The exclusion statement attached to EK 1.4.A.1 says that the molecular "
          "structure of specific carbohydrate polymers is beyond the scope of the AP "
          "Exam. The other four options restate parts of EK 1.4.A.1 or EK 1.2.A.1 that "
          "the framework does require."),

 dict(q="The table describes four carbohydrate samples. Which sample is a monosaccharide "
        "rather than a polysaccharide?",
      table=_T_CARBS,
      choices=["Sample J", "Sample K", "Sample L", "Sample M",
               "None of the four is a monosaccharide."],
      ans=0,
      why="EK 1.4.A.1 makes a monosaccharide the monomer and a polysaccharide a polymer "
          "of many such monomers connected by covalent bonds. Exactly one row of the "
          "table records a single unit in the molecule, so it is the one with no bonds "
          "between monomers at all."),

 dict(q="Using the same four samples, which one is a branched complex carbohydrate?",
      table=_T_CARBS,
      choices=["Sample L", "Sample J", "Sample K", "Sample M",
               "Two of the samples are branched."],
      ans=0,
      why="EK 1.4.A.1 allows a complex carbohydrate to be linear or branched, and exactly "
          "one row of the table is recorded as branched while carrying many monomer "
          "units. The single-unit sample is not a polymer at all, so it cannot be the "
          "branched one."),

 dict(q="Two of the samples in the table are unbranched polymers of monosaccharides. "
        "Which two are they?",
      table=_T_CARBS,
      choices=["Sample K and Sample M", "Sample J and Sample K", "Sample J and Sample L",
               "Sample L and Sample M", "Sample J and Sample M"],
      ans=0,
      why="A row must record more than one monomer unit to be a polymer at all under EK "
          "1.4.A.1, and must be recorded as unbranched to be linear. Exactly two rows "
          "satisfy both, and the single-unit sample fails the first test."),

 dict(q="One sample in the table contains 300 monosaccharide units joined into a single "
        "unbranched chain. How many covalent bonds between monomers hold that molecule "
        "together?",
      table=_T_CARBS,
      choices=["299", "300", "301", "150", "598"],
      ans=0,
      why="A single unbranched chain of n units is held by n minus 1 bonds between "
          "monomers, since every unit but the first is added by forming one bond. EK "
          "1.4.A.1 states that those links are covalent, and EK 1.3.A.2 is the reaction "
          "that makes each of them."),

 dict(q="Four samples were hydrolyzed until no bonds between monomers remained, with the "
        "results in the table. Which sample was already a single monosaccharide before "
        "hydrolysis?",
      table=_T_HYDROLYSIS,
      choices=["Sample P", "Sample Q", "Sample R", "Sample S",
               "The results cannot distinguish a monosaccharide from a polysaccharide."],
      ans=0,
      why="Complete hydrolysis breaks every bond between monomers under EK 1.3.A.1, so "
          "the number of simple sugar molecules recovered equals the number of monomers "
          "the sample contained. Exactly one row recovers a single molecule, which is a "
          "sample that had no such bond to break."),

 dict(q="Among the hydrolyzed samples in the table, which one is a polysaccharide built "
        "from a single kind of monosaccharide?",
      table=_T_HYDROLYSIS,
      choices=["Sample Q", "Sample P", "Sample R", "Sample S",
               "No sample in the table fits that description."],
      ans=0,
      why="Being a polysaccharide requires many monomers, which shows up as many "
          "molecules recovered, and being built from one kind of monomer shows up as one "
          "kind of simple sugar recovered. Exactly one row satisfies both conditions."),

 dict(q="For the sample in the table from which 740 simple sugar molecules were "
        "recovered, how many covalent bonds between monomers were cleaved?",
      table=_T_HYDROLYSIS,
      choices=["739", "740", "741", "370", "1,479"],
      ans=0,
      why="Every molecule recovered was a monomer in one chain, and a chain of n monomers "
          "holds n minus 1 bonds between monomers. EK 1.3.A.1 makes hydrolysis the "
          "cleaving of exactly those covalent bonds, so the count follows from the "
          "recovery figure alone."),

 dict(q="Four polysaccharides, each a single connected molecule containing no rings, were "
        "examined and the number of chain ends on each was counted, as shown in the "
        "table. Which polymers must be branched?",
      table=_T_ENDS,
      choices=["Polymer U and Polymer W", "Polymer T and Polymer V",
               "Polymer T and Polymer U", "Polymer V and Polymer W",
               "All four polymers must be branched."],
      ans=0,
      why="A single unbranched chain has exactly two ends, so any molecule with more than "
          "two ends must divide somewhere along its length. EK 1.4.A.1 states that a "
          "complex carbohydrate may be linear or branched, and the end count is what "
          "distinguishes the two here."),

 dict(q="Each of the four polysaccharides in the same table contains 1,000 monosaccharide "
        "units in one connected molecule with no rings. What does that imply about the "
        "number of covalent bonds between monomers in each?",
      table=_T_ENDS,
      choices=[
        "Every one of them contains 999 such bonds, whether it is branched or not.",
        "The branched polymers contain more such bonds than the unbranched ones.",
        "The branched polymers contain fewer such bonds than the unbranched ones.",
        "The number of such bonds cannot be determined from the number of units.",
        "Every one of them contains 1,000 such bonds."],
      ans=0,
      why="Each added unit joins the growing molecule by one covalent bond, so a "
          "connected, ring-free molecule of n units holds n minus 1 bonds no matter how "
          "the bonds are arranged. Branching changes where the bonds go, not how many "
          "there are, which is why EK 1.4.A.1 can allow either shape for the same class "
          "of polymer."),

 dict(q="A researcher wishes to convert a complex carbohydrate into its simple sugars. "
        "Which reaction should be used?",
      choices=[
        "Hydrolysis, which adds water across the bonds between monomers and cleaves them",
        "Dehydration synthesis, which removes the equivalent of a water molecule and "
        "forms a bond",
        "Polymerization, which connects many monomers into a longer chain",
        "A reaction that breaks the hydrogen bonds holding the monomers together",
        "No reaction is needed, because complex carbohydrates separate into simple sugars "
        "on their own"],
      ans=0,
      why="EK 1.3.A.1 defines hydrolysis as the cleaving of covalent bonds by adding "
          "water across the bond between monomers, and EK 1.4.A.1 states that the links "
          "in a polysaccharide are covalent. Dehydration synthesis and polymerization run "
          "in the opposite direction."),

 dict(q="Which reaction joins monosaccharides into a complex carbohydrate, and what is "
        "released as it does so?",
      choices=[
        "Dehydration synthesis, releasing the equivalent of one water molecule for each "
        "bond formed",
        "Dehydration synthesis, releasing one simple sugar for each bond formed",
        "Hydrolysis, releasing the equivalent of one water molecule for each bond formed",
        "Hydrolysis, consuming one water molecule for each bond formed",
        "Neither reaction, because the monomers associate without forming any bond"],
      ans=0,
      why="EK 1.3.A.2 describes dehydration synthesis as joining two smaller molecules "
          "through covalent bonding with the loss of the equivalent of a water molecule "
          "from the reactants, and EK 1.4.A.1 makes the polysaccharide link covalent. "
          "Hydrolysis is the reverse reaction of EK 1.3.A.1."),

 dict(q="A purified carbohydrate is analyzed and found to contain carbon, hydrogen and "
        "oxygen and nothing else. How does that finding relate to the course framework's "
        "account of the elements of life?",
      choices=[
        "It is consistent, because carbon, hydrogen and oxygen are the elements named as "
        "most prevalent and no additional element is assigned to carbohydrates.",
        "It is inconsistent, because the framework assigns nitrogen to carbohydrates.",
        "It is inconsistent, because the framework assigns phosphorus to carbohydrates.",
        "It is inconsistent, because the framework assigns sulfur to carbohydrates.",
        "It is unrelated, because the framework makes no claim about which elements build "
        "carbohydrates."],
      ans=0,
      why="EK 1.2.A.1 names carbon, hydrogen and oxygen as the most prevalent elements "
          "used to build biological molecules including carbohydrates, and its three "
          "sub-points add sulfur to proteins and phosphorus and nitrogen to "
          "phospholipids and nucleic acids, never to carbohydrates."),

 dict(q="A student states that every carbohydrate polymer is a straight, unbranched "
        "chain. What is the best correction?",
      choices=[
        "A complex carbohydrate may be linear or branched, so an unbranched chain is one "
        "possibility rather than the rule.",
        "A complex carbohydrate is always branched, so the student has it exactly "
        "backwards.",
        "A complex carbohydrate has no defined shape, because its monomers are not "
        "bonded to one another.",
        "The student is right, because covalent bonds can only form in a straight line.",
        "The student is right for plants but wrong for animals, which build no "
        "carbohydrate polymers."],
      ans=0,
      why="EK 1.4.A.1 states that the polymers formed may be linear or branched. That "
          "permits both without requiring either, so the correction is to the "
          "universality of the student's claim rather than to its direction."),

 dict(q="Which experimental result would provide the strongest evidence that an unknown "
        "substance is a polysaccharide?",
      choices=[
        "Complete hydrolysis of the substance releases a large number of simple sugar "
        "molecules.",
        "The substance dissolves slowly in cold water.",
        "The substance contains carbon, hydrogen and oxygen.",
        "Complete hydrolysis of the substance releases a large number of amino acids.",
        "The substance forms a viscous solution when it is stirred."],
      ans=0,
      why="EK 1.4.A.1 defines a polysaccharide as a polymer of monosaccharide monomers, "
          "and EK 1.3.A.1 makes hydrolysis the reaction that releases those monomers. "
          "Amino acids would indicate a polypeptide under EK 1.7.A.1, and elemental "
          "composition alone does not distinguish a monomer from a polymer."),

 dict(q="How does the relationship between monosaccharides and polysaccharides compare "
        "with the relationship between amino acids and a polypeptide?",
      choices=[
        "In both cases many monomers are connected by covalent bonds into a polymer.",
        "In the first case the monomers are covalently bonded and in the second they are "
        "held by hydrogen bonds.",
        "In the first case a polymer is broken into monomers and in the second monomers "
        "are joined into a polymer.",
        "There is no comparison, because a polypeptide contains no repeating units.",
        "In both cases the monomers remain separate molecules held near one another."],
      ans=0,
      why="EK 1.4.A.1 connects monosaccharide monomers by covalent bonds into "
          "polysaccharides, and EK 1.7.A.1 connects amino acids by covalent peptide bonds "
          "into a growing peptide chain. The parallel is the covalent monomer-to-polymer "
          "relation that both statements assert."),

 dict(q="An organism cannot make the enzyme that catalyzes the formation of covalent "
        "bonds between monosaccharides. Which outcome is predicted most directly?",
      choices=[
        "It will be unable to assemble monosaccharides into complex carbohydrates.",
        "It will be unable to break complex carbohydrates down into monosaccharides.",
        "It will assemble complex carbohydrates from amino acids instead.",
        "Its monosaccharides will spontaneously join without any enzyme.",
        "It will accumulate complex carbohydrates faster than an unaffected organism."],
      ans=0,
      why="EK 1.4.A.1 makes the covalent bond between monomers the thing that turns "
          "monosaccharides into a polysaccharide, so losing the ability to form that bond "
          "blocks assembly rather than breakdown, which EK 1.3.A.1 assigns to hydrolysis "
          "instead."),

 dict(q="Which of the following is the least accurate statement about a complex "
        "carbohydrate, judged against the course framework?",
      choices=[
        "Its monomers are held to one another by hydrogen bonds.",
        "It is a polymer of monosaccharide units.",
        "It may be linear or it may be branched.",
        "Its monomers are held to one another by covalent bonds.",
        "It can be broken down into simple sugars by the addition of water across those "
        "bonds."],
      ans=0,
      why="EK 1.4.A.1 states that the monomers are connected by covalent bonds, so "
          "attributing the connection to hydrogen bonds contradicts it. The other four "
          "options restate EK 1.4.A.1 or the hydrolysis reaction of EK 1.3.A.1."),

 dict(q="Two carbohydrate molecules contain the same number of monosaccharide units, but "
        "one is linear and the other is branched. What does the course framework allow "
        "you to say about them?",
      choices=[
        "Both are complex carbohydrates, since the framework permits either shape.",
        "Only the linear one is a complex carbohydrate, since branching disqualifies a "
        "polymer.",
        "Only the branched one is a complex carbohydrate, since a linear chain is a "
        "single monomer.",
        "Neither is a complex carbohydrate unless it also contains nitrogen.",
        "The framework requires the two to contain different numbers of covalent bonds "
        "between monomers."],
      ans=0,
      why="EK 1.4.A.1 says the polymers formed may be linear or branched, so shape is not "
          "what decides membership in the class. Nitrogen belongs to nucleic acids under "
          "EK 1.2.A.1 iii, and a connected ring-free molecule of n units holds n minus 1 "
          "bonds whichever shape it takes."),

 dict(q="Why does describing a monosaccharide as a monomer rather than a polymer matter "
        "for how it can react?",
      choices=[
        "A monomer has no bond to another monomer to cleave, so hydrolysis cannot break "
        "it into smaller sugars.",
        "A monomer cannot take part in dehydration synthesis, because it has no covalent "
        "bonds of any kind.",
        "A monomer is broken down by hydrolysis into many smaller sugars.",
        "A monomer can only be joined to another monomer by a hydrogen bond.",
        "A monomer contains more covalent bonds between monomers than a polymer does."],
      ans=0,
      why="EK 1.4.A.1 makes the monosaccharide the unit and the polysaccharide the "
          "assembly of units, and EK 1.3.A.1 confines hydrolysis to the bond between "
          "monomers in a polymer. A single unit has no such bond, though it can still be "
          "joined to another under EK 1.3.A.2."),

 dict(q="A polysaccharide is completely hydrolyzed and yields simple sugars of three "
        "different kinds. What does that result show about the polymer?",
      choices=[
        "Its chain was assembled from more than one kind of monosaccharide monomer.",
        "Its chain was assembled from exactly one kind of monosaccharide monomer.",
        "Its chain contained no covalent bonds between monomers.",
        "It was not a carbohydrate at all, since carbohydrate polymers cannot be mixed.",
        "It must have been branched rather than linear."],
      ans=0,
      why="EK 1.3.A.1 releases the monomers of a polymer when its bonds are cleaved, so "
          "the identities of the products report the identities of the monomers. EK "
          "1.4.A.1 places no restriction on the shape or the number of kinds of monomer, "
          "so branching cannot be inferred from this result."),

 dict(q="Which sequence correctly describes the fate of a dietary complex carbohydrate "
        "inside an organism, in the terms the course framework uses?",
      choices=[
        "Covalent bonds between its monomers are cleaved by hydrolysis, releasing "
        "monosaccharides.",
        "Hydrogen bonds between its monomers are cleaved by hydrolysis, releasing "
        "monosaccharides.",
        "Its monomers are joined by dehydration synthesis, releasing water.",
        "It is converted directly into amino acids by the addition of water.",
        "It passes through unchanged, because covalent bonds cannot be cleaved in a "
        "living organism."],
      ans=0,
      why="EK 1.4.A.1 makes the links covalent, and EK 1.3.A.1 makes hydrolysis the "
          "reaction that cleaves covalent bonds and breaks molecules down into smaller "
          "molecules. Dehydration synthesis runs the other way, and hydrolysis of a "
          "carbohydrate yields sugars rather than amino acids."),

 dict(q="An investigator reports that a newly isolated molecule is made of many identical "
        "units joined end to end, and that adding water across each junction releases "
        "those units as simple sugars. Which classification is best supported?",
      choices=[
        "It is a polysaccharide, since it is a polymer of monosaccharide monomers.",
        "It is a monosaccharide, since the released units are simple sugars.",
        "It is a nucleic acid, since its units are joined end to end.",
        "It is a protein, since it is built from many identical units.",
        "It cannot be classified without knowing the molecular structure of the specific "
        "polymer."],
      ans=0,
      why="EK 1.4.A.1 defines a polysaccharide as a polymer whose monomers are "
          "monosaccharides connected by covalent bonds, which is exactly what the "
          "reported behaviour shows. The exclusion statement removes the need for "
          "structural detail rather than making classification impossible."),

 dict(q="Which pair of terms in this topic stand in the same relation to each other as "
        "'unit' and 'assembly of units'?",
      choices=[
        "Monosaccharide and polysaccharide",
        "Polysaccharide and complex carbohydrate",
        "Monosaccharide and simple sugar",
        "Covalent bond and hydrogen bond",
        "Linear chain and branched chain"],
      ans=0,
      why="EK 1.4.A.1 states that monosaccharides are the monomers for polysaccharides, "
          "which is the unit to assembly relation. Two of the rejected pairs are pairs of "
          "synonyms the same sentence supplies, and the other two are alternatives rather "
          "than a unit and its assembly."),

 dict(q="A sample of a complex carbohydrate is heated in acid until every bond between "
        "its monomers has been cleaved, and the products are collected. What has "
        "necessarily happened to the number of separate molecules in the sample?",
      choices=[
        "It has increased, because each released monomer is now a molecule of its own.",
        "It has decreased, because the released monomers combine into fewer, larger "
        "molecules.",
        "It has stayed the same, because cleaving a bond does not change how many "
        "molecules there are.",
        "It has decreased, because water molecules are lost as each bond is cleaved.",
        "It cannot be determined without knowing whether the polymer was branched."],
      ans=0,
      why="EK 1.3.A.1 states that hydrolysis breaks molecules down into smaller molecules, "
          "and EK 1.4.A.1 makes the monomers of a complex carbohydrate its "
          "monosaccharides. Water is consumed rather than lost in this direction, and the "
          "result holds for either shape EK 1.4.A.1 permits."),
]
