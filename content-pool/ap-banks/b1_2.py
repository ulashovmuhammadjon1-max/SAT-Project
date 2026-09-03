# AP BIOLOGY 1.2 Elements of Life
# CED effective Fall 2025, Unit 1 Chemistry of Life. Big Idea 2 Energetics.
# Learning objective 1.2.A: describe the composition of macromolecules required by
# living organisms. Suggested skill 2.A, describe characteristics of visual
# representations of biological concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   1.2.A.1    Atoms and molecules from the environment are necessary to build new
#              molecules. Carbon, hydrogen, and oxygen are the most prevalent elements
#              used to build biological molecules such as carbohydrates, proteins,
#              lipids, and nucleic acids. Additionally:
#     i.       Sulfur is used in the building of proteins.
#     ii.      Phosphorus is used in the building of phospholipids (a type of lipid)
#              and nucleic acids.
#     iii.     Nitrogen is used in the building of nucleic acids.
#
# ON WHAT THIS TOPIC DOES AND DOES NOT SAY. EK 1.2.A.1 iii names nitrogen for nucleic
# acids and does not repeat it for proteins. Two items here (26, 28) reach nitrogen in
# proteins, and both do it by CHAINING to EK 1.7.A.1 and EK 1.7.A.2, which put an amine
# group in every amino acid; the chain is stated in the claim. No item asserts a
# composition the framework does not print somewhere.
#
# ON THE DATA. Every table is labelled in the stem, every keyed conclusion is
# recoverable from the table alone, and each is recomputed in verify_b1_2.py.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("1.2", "Elements of Life", 1)

_T_SAMPLES = dict(
    headers=["Sample", "Carbon (percent by mass)", "Hydrogen (percent by mass)",
             "Oxygen (percent by mass)", "Nitrogen (percent by mass)",
             "Phosphorus (percent by mass)", "Sulfur (percent by mass)"],
    rows=[["Sample W", "44", "6", "50", "0", "0", "0"],
          ["Sample X", "52", "7", "24", "16", "0", "1"],
          ["Sample Y", "37", "4", "32", "17", "10", "0"],
          ["Sample Z", "64", "11", "21", "0", "4", "0"]])

_T_MEDIA = dict(
    headers=["Culture", "Sulfur supplied (millimolar)", "Phosphorus supplied (millimolar)",
             "Nitrogen supplied (millimolar)",
             "Cell density after 24 hours (millions of cells per milliliter)"],
    rows=[["Culture 1", "1.0", "1.0", "1.0", "9.6"],
          ["Culture 2", "0.0", "1.0", "1.0", "1.2"],
          ["Culture 3", "1.0", "0.0", "1.0", "0.8"],
          ["Culture 4", "1.0", "1.0", "0.0", "1.6"]])

_T_DRYMASS = dict(
    headers=["Element", "Percentage of the dry mass of one bacterial species"],
    rows=[["Carbon", "50"],
          ["Oxygen", "20"],
          ["Nitrogen", "14"],
          ["Hydrogen", "8"],
          ["All other elements combined", "4"],
          ["Phosphorus", "3"],
          ["Sulfur", "1"]])

_T_TRACER = dict(
    headers=["Culture", "Radioactive element added to the medium",
             "Radioactivity recovered in the purified protein fraction (counts per minute)",
             "Radioactivity recovered in the purified nucleic acid fraction (counts per minute)"],
    rows=[["Culture A", "Sulfur", "18,400", "120"],
          ["Culture B", "Phosphorus", "310", "22,700"]])

QUESTIONS = [

 dict(q="Which three elements does the course framework identify as the most prevalent "
        "in the biological molecules that living organisms build?",
      choices=[
        "Carbon, hydrogen and oxygen",
        "Carbon, nitrogen and phosphorus",
        "Hydrogen, nitrogen and sulfur",
        "Oxygen, phosphorus and sulfur",
        "Carbon, oxygen and nitrogen"],
      ans=0,
      why="EK 1.2.A.1 states that carbon, hydrogen, and oxygen are the most prevalent "
          "elements used to build biological molecules. The remaining elements the "
          "statement names, sulfur, phosphorus and nitrogen, are each tied to particular "
          "classes of molecule rather than described as most prevalent."),

 dict(q="A textbook lists four classes of biological molecule that organisms build from "
        "elements taken up from their surroundings. Which list matches the one the course "
        "framework gives?",
      choices=[
        "Carbohydrates, proteins, lipids and nucleic acids",
        "Carbohydrates, proteins, minerals and vitamins",
        "Sugars, salts, lipids and nucleic acids",
        "Proteins, lipids, nucleic acids and enzymes",
        "Carbohydrates, lipids, nucleic acids and water"],
      ans=0,
      why="EK 1.2.A.1 names carbohydrates, proteins, lipids, and nucleic acids as the "
          "biological molecules built from the prevalent elements. Minerals, salts, "
          "vitamins and water are not among them, and enzymes are not a fifth class "
          "alongside proteins."),

 dict(q="Sulfur is described by the course framework as an element used in building "
        "which class of biological molecule?",
      choices=["Proteins", "Nucleic acids", "Carbohydrates", "Phospholipids",
               "Monosaccharides"],
      ans=0,
      why="EK 1.2.A.1 i states plainly that sulfur is used in the building of proteins. "
          "Phosphorus rather than sulfur is the element EK 1.2.A.1 ii assigns to "
          "phospholipids and nucleic acids, and carbohydrates are built from the three "
          "prevalent elements alone."),

 dict(q="Phosphorus is used in the building of which two of the following, according to "
        "the course framework?",
      choices=[
        "Phospholipids and nucleic acids",
        "Proteins and nucleic acids",
        "Carbohydrates and proteins",
        "Phospholipids and carbohydrates",
        "Proteins and carbohydrates"],
      ans=0,
      why="EK 1.2.A.1 ii states that phosphorus is used in the building of phospholipids, "
          "a type of lipid, and nucleic acids. Sulfur rather than phosphorus is the "
          "element assigned to proteins, and carbohydrates appear in none of the "
          "element-specific sub-points."),

 dict(q="A researcher wants to supply a growing culture with the one element the course "
        "framework specifically associates with the building of nucleic acids in addition "
        "to phosphorus. Which element should be added?",
      choices=["Nitrogen", "Sulfur", "Calcium", "Iron", "Sodium"],
      ans=0,
      why="EK 1.2.A.1 iii states that nitrogen is used in the building of nucleic acids, "
          "and EK 1.2.A.1 ii adds phosphorus to the same class. Sulfur belongs to "
          "proteins in EK 1.2.A.1 i, and calcium, iron and sodium are not named in this "
          "statement at all."),

 dict(q="The table gives the elemental composition of four purified samples. Which "
        "sample is composed only of the three elements the framework calls most "
        "prevalent, and so is consistent with a pure carbohydrate?",
      table=_T_SAMPLES,
      choices=["Sample W", "Sample X", "Sample Y", "Sample Z",
               "None of the samples is consistent with a pure carbohydrate."],
      ans=0,
      why="Reading the table, only one sample records zero for nitrogen, zero for "
          "phosphorus and zero for sulfur, leaving carbon, hydrogen and oxygen. EK "
          "1.2.A.1 makes those three the elements from which such a molecule is built, "
          "and none of the element-specific sub-points assigns any other element to "
          "carbohydrates."),

 dict(q="Using the same four purified samples, which one contains the element that the "
        "framework ties specifically to the building of proteins?",
      table=_T_SAMPLES,
      choices=["Sample X", "Sample W", "Sample Y", "Sample Z",
               "Every sample contains that element."],
      ans=0,
      why="EK 1.2.A.1 i names sulfur as the element used in building proteins, and the "
          "sulfur column of the table is nonzero for exactly one sample. The remaining "
          "three record zero sulfur, so the final option is false against the table."),

 dict(q="Among the four purified samples in the table, which one contains both of the "
        "elements the framework assigns to nucleic acids?",
      table=_T_SAMPLES,
      choices=["Sample Y", "Sample W", "Sample X", "Sample Z",
               "Two of the samples contain both."],
      ans=0,
      why="EK 1.2.A.1 ii and iii assign phosphorus and nitrogen to nucleic acids. Exactly "
          "one sample in the table is nonzero in both of those columns; one other sample "
          "has nitrogen without phosphorus and another has phosphorus without nitrogen, "
          "so the final option is false."),

 dict(q="One of the four samples in the table contains phosphorus but no nitrogen and no "
        "sulfur. Which class of molecule named in the course framework is that "
        "composition most consistent with?",
      table=_T_SAMPLES,
      choices=[
        "A phospholipid",
        "A nucleic acid",
        "A protein",
        "A complex carbohydrate",
        "A monosaccharide"],
      ans=0,
      why="EK 1.2.A.1 ii names phospholipids and nucleic acids as the two phosphorus "
          "users, and EK 1.2.A.1 iii adds nitrogen to nucleic acids, so a phosphorus "
          "sample with no nitrogen fits the phospholipid and not the nucleic acid. "
          "Proteins would carry sulfur under EK 1.2.A.1 i and a carbohydrate would carry "
          "no phosphorus at all."),

 dict(q="For the sample in the table that contains 37 percent carbon, what percentage of "
        "its mass is made up of carbon, hydrogen and oxygen together?",
      table=_T_SAMPLES,
      choices=["73 percent", "27 percent", "63 percent", "83 percent", "90 percent"],
      ans=0,
      why="Adding the three columns for that row gives 37 plus 4 plus 32. The remaining "
          "27 percent is the nitrogen and phosphorus that EK 1.2.A.1 ii and iii assign to "
          "nucleic acids, which is why the two figures are complements."),

 dict(q="Four cultures of the same bacterium were grown in media differing only in which "
        "element was withheld, with the results in the table. In which culture is the "
        "building of proteins most directly limited by the missing element?",
      table=_T_MEDIA,
      choices=["Culture 2", "Culture 1", "Culture 3", "Culture 4",
               "The design cannot distinguish among the cultures."],
      ans=0,
      why="EK 1.2.A.1 i ties sulfur to the building of proteins, and exactly one culture "
          "in the table was supplied no sulfur. Its growth fell to a small fraction of "
          "the fully supplied culture, so the design does distinguish among them."),

 dict(q="In the same experiment, withholding one element should limit both phospholipid "
        "synthesis and nucleic acid synthesis at once. Which culture had that element "
        "withheld?",
      table=_T_MEDIA,
      choices=["Culture 3", "Culture 1", "Culture 2", "Culture 4",
               "No single culture had such an element withheld."],
      ans=0,
      why="EK 1.2.A.1 ii assigns phosphorus to both phospholipids and nucleic acids, so "
          "the phosphorus-free culture is the one whose deficiency reaches both classes. "
          "Exactly one row of the table records zero phosphorus supplied."),

 dict(q="Comparing the fully supplied culture in the table with the culture that received "
        "no sulfur, the fully supplied culture reached a final density approximately how "
        "many times as great?",
      table=_T_MEDIA,
      choices=["Eight times", "Twice", "Twelve times", "Twenty times",
               "About the same density"],
      ans=0,
      why="The two densities in the table are 9.6 and 1.2 million cells per milliliter, "
          "and the first divided by the second is exactly 8. The comparison is what makes "
          "the withheld element a limiting one in the sense of EK 1.2.A.1, that atoms "
          "from the environment are necessary to build new molecules."),

 dict(q="The table reports the elemental make-up of the dry mass of one bacterial "
        "species. What percentage of that dry mass is accounted for by the three elements "
        "the framework calls most prevalent?",
      table=_T_DRYMASS,
      choices=["78 percent", "84 percent", "70 percent", "92 percent", "58 percent"],
      ans=0,
      why="EK 1.2.A.1 names carbon, hydrogen and oxygen, whose tabulated shares are 50, 8 "
          "and 20. The 84 percent distractor is what a student gets by taking the three "
          "largest entries instead, which substitutes nitrogen for hydrogen."),

 dict(q="Looking again at the dry mass table, which element present in the smallest "
        "percentage is nevertheless one the framework names as required for building a "
        "specific class of macromolecule?",
      table=_T_DRYMASS,
      choices=["Sulfur", "Phosphorus", "Nitrogen", "Hydrogen", "Carbon"],
      ans=0,
      why="Sulfur holds the smallest tabulated percentage of any single element listed, "
          "and EK 1.2.A.1 i names it as used in the building of proteins. Being scarce by "
          "mass therefore does not make an element dispensable."),

 dict(q="Cells were grown with a radioactive form of one element, and the radioactivity "
        "recovered in two purified fractions was measured, as shown in the table. Which "
        "conclusion is best supported?",
      table=_T_TRACER,
      choices=[
        "The element supplied to the first culture is incorporated mainly into protein, "
        "and the element supplied to the second mainly into nucleic acid.",
        "Both elements are incorporated mainly into protein.",
        "Both elements are incorporated mainly into nucleic acid.",
        "The element supplied to the first culture is incorporated mainly into nucleic "
        "acid, and the element supplied to the second mainly into protein.",
        "Neither element is incorporated into either fraction to a measurable extent."],
      ans=0,
      why="In the table the sulfur culture recovers far more radioactivity in the protein "
          "fraction than in the nucleic acid fraction, and the phosphorus culture the "
          "reverse. That is the pattern EK 1.2.A.1 i and ii predict, since sulfur is used "
          "in proteins and phosphorus in nucleic acids and phospholipids."),

 dict(q="Why does the course framework begin its treatment of macromolecules by stating "
        "that atoms and molecules come from the environment?",
      choices=[
        "Because an organism cannot create the elements it needs and must obtain them "
        "from its surroundings in order to build new molecules",
        "Because organisms convert one element into another as they grow, using energy "
        "from food",
        "Because the elements in a cell are produced by chemical reactions inside the "
        "cell itself",
        "Because only carbon has to be taken up, while the other elements are made "
        "internally",
        "Because the environment supplies the finished macromolecules that a cell needs"],
      ans=0,
      why="EK 1.2.A.1 opens by stating that atoms and molecules from the environment are "
          "necessary to build new molecules. Building means assembling supplied atoms "
          "into larger molecules, not creating elements and not absorbing the finished "
          "polymers whole."),

 dict(q="A plant is grown in a nutrient solution from which sulfur has been omitted. "
        "Which prediction follows most directly from the course framework?",
      choices=[
        "Protein synthesis will be impaired before carbohydrate synthesis is.",
        "Carbohydrate synthesis will be impaired before protein synthesis is.",
        "Nucleic acid synthesis will stop immediately while protein synthesis continues "
        "normally.",
        "All four classes of macromolecule will be impaired to exactly the same degree.",
        "No class of macromolecule will be affected, because sulfur is not used in "
        "building any of them."],
      ans=0,
      why="EK 1.2.A.1 i names sulfur only for proteins, and EK 1.2.A.1 makes carbon, "
          "hydrogen and oxygen the elements of carbohydrates, none of which is withheld. "
          "The prediction therefore separates the two classes rather than treating them "
          "alike."),

 dict(q="A lake receives run-off that is rich in nitrogen but contains almost no "
        "phosphorus. Which class of molecule would algae in that lake have the greatest "
        "difficulty building?",
      choices=[
        "Phospholipids",
        "Carbohydrates such as those built from monosaccharides",
        "Proteins built from amino acids",
        "Molecules built only from carbon, hydrogen and oxygen",
        "Every class would be equally impaired."],
      ans=0,
      why="EK 1.2.A.1 ii is the only sub-point that names phosphorus, and it assigns it "
          "to phospholipids and nucleic acids. Nitrogen is supplied in this scenario, so "
          "the shortage falls on the phosphorus user that nitrogen cannot substitute "
          "for; carbohydrates need none of the three special elements."),

 dict(q="A student states that every biological macromolecule contains nitrogen. What is "
        "the best correction?",
      choices=[
        "Carbohydrates are built from carbon, hydrogen and oxygen, so nitrogen is not a "
        "requirement of every class.",
        "Nitrogen is required by every class except nucleic acids, which use phosphorus "
        "instead.",
        "Nitrogen is required only by lipids, which is why phospholipids are named "
        "separately.",
        "Nitrogen is required by every class, so the student's statement needs no "
        "correction.",
        "Nitrogen is never used by living organisms, which build only from carbon, "
        "hydrogen and oxygen."],
      ans=0,
      why="EK 1.2.A.1 names carbon, hydrogen and oxygen as the elements used to build "
          "biological molecules generally, and adds nitrogen in EK 1.2.A.1 iii only for "
          "nucleic acids. A carbohydrate is therefore the counterexample the student's "
          "claim needs."),

 dict(q="Which experimental design would best test whether an organism requires an "
        "environmental supply of phosphorus to grow?",
      choices=[
        "Grow replicate cultures in identical media that differ only in whether "
        "phosphorus is present, then compare growth.",
        "Grow one culture in a complete medium and a second in a medium lacking both "
        "phosphorus and nitrogen, then compare growth.",
        "Grow a single culture in a phosphorus-free medium and report whether it grows at "
        "all.",
        "Grow replicate cultures at several temperatures in a complete medium and measure "
        "the phosphorus content of the cells.",
        "Measure the phosphorus content of cells taken from a natural population at "
        "several times of year."],
      ans=0,
      why="Only one design isolates phosphorus as the single difference between "
          "treatments while replicating, which is what an attribution to phosphorus "
          "requires. Withholding two elements at once confounds them, and a single "
          "culture with no comparison supplies no baseline."),

 dict(q="Two purified molecules are analyzed. One contains carbon, hydrogen, oxygen and "
        "sulfur; the other contains carbon, hydrogen, oxygen, nitrogen and phosphorus. "
        "What is the most reasonable identification of the pair?",
      choices=[
        "The first is a protein and the second is a nucleic acid.",
        "The first is a nucleic acid and the second is a protein.",
        "Both are carbohydrates, since both contain carbon, hydrogen and oxygen.",
        "The first is a phospholipid and the second is a protein.",
        "Neither can be identified, because all four classes contain the same elements."],
      ans=0,
      why="EK 1.2.A.1 i assigns sulfur to proteins, and EK 1.2.A.1 ii and iii assign "
          "phosphorus and nitrogen together to nucleic acids. A phospholipid would carry "
          "phosphorus rather than sulfur, and the presence of the three prevalent "
          "elements alone does not make a molecule a carbohydrate when other elements are "
          "also present."),

 dict(q="Two elements named in the course framework are each tied to more than one kind "
        "of molecule or to a molecule shared between classes. Which statement about "
        "phosphorus is accurate on the framework's own terms?",
      choices=[
        "It is used both in a type of lipid and in nucleic acids.",
        "It is used in proteins and in carbohydrates but not in lipids.",
        "It is used only in nucleic acids and in no other class.",
        "It is used in all four classes of biological molecule.",
        "It is used only in the lipid class and in no nucleic acid."],
      ans=0,
      why="EK 1.2.A.1 ii states that phosphorus is used in the building of phospholipids, "
          "which it identifies parenthetically as a type of lipid, and of nucleic acids. "
          "It therefore spans two classes, but not all four and not proteins."),

 dict(q="An organism takes up ammonium from the soil and uses the nitrogen in it. "
        "According to the course framework, the building of which class of molecule most "
        "directly depends on that uptake?",
      choices=["Nucleic acids", "Simple sugars", "Steroids", "Complex carbohydrates",
               "Saturated fatty acids"],
      ans=0,
      why="EK 1.2.A.1 iii names nitrogen for the building of nucleic acids. Carbohydrates "
          "in all the forms listed are built from the three prevalent elements, and "
          "nothing in EK 1.2.A.1 assigns nitrogen to them."),

 dict(q="Which observation about a purified biological sample would most strongly "
        "indicate that it is not a carbohydrate?",
      choices=[
        "It contains a measurable amount of nitrogen.",
        "It contains a measurable amount of oxygen.",
        "It contains more carbon than hydrogen by mass.",
        "It contains hydrogen and oxygen in unequal amounts.",
        "It dissolves readily in water."],
      ans=0,
      why="EK 1.2.A.1 assigns carbon, hydrogen and oxygen to the building of biological "
          "molecules generally and adds nitrogen only for nucleic acids in EK 1.2.A.1 "
          "iii, so nitrogen is the element whose presence rules the sample out. Oxygen "
          "and carbon are expected in a carbohydrate, and solubility is not an elemental "
          "claim."),

 dict(q="Nucleotides are described elsewhere in the course framework as containing a "
        "phosphate and a nitrogenous base. How does that description fit the elements "
        "assigned to nucleic acids in this topic?",
      choices=[
        "The phosphate supplies the phosphorus and the nitrogenous base supplies the "
        "nitrogen, matching both elements assigned to nucleic acids.",
        "The phosphate supplies the nitrogen and the nitrogenous base supplies the "
        "phosphorus.",
        "Both the phosphate and the nitrogenous base supply sulfur.",
        "Neither component supplies an element beyond carbon, hydrogen and oxygen.",
        "The five-carbon sugar rather than the phosphate is the source of the "
        "phosphorus."],
      ans=0,
      why="EK 1.6.A.1 lists a five-carbon sugar, a phosphate and a nitrogenous base as "
          "the components of a nucleotide, which places phosphorus in the phosphate and "
          "nitrogen in the base. That is exactly the pair EK 1.2.A.1 ii and iii assign to "
          "nucleic acids, so the two statements agree."),

 dict(q="A geologist samples an ancient sediment and finds organic residues containing "
        "carbon, hydrogen, oxygen and phosphorus, with no detectable nitrogen or sulfur. "
        "Which of the following is the most defensible inference?",
      choices=[
        "The residues are more consistent with phospholipid remains than with protein or "
        "nucleic acid remains.",
        "The residues must be the remains of nucleic acids, since these contain "
        "phosphorus.",
        "The residues must be the remains of proteins, since these contain phosphorus.",
        "The residues cannot have come from a living organism, because phosphorus is not "
        "used by living organisms.",
        "The residues must be pure carbohydrate, since carbon, hydrogen and oxygen are "
        "present."],
      ans=0,
      why="EK 1.2.A.1 ii gives phosphorus two users, phospholipids and nucleic acids, and "
          "EK 1.2.A.1 iii adds nitrogen to nucleic acids while EK 1.2.A.1 i adds sulfur "
          "to proteins. With phosphorus present but nitrogen and sulfur absent, only the "
          "phospholipid reading survives, and a carbohydrate would carry no phosphorus."),

 dict(q="Amino acids are described elsewhere in the course framework as carrying an amine "
        "group. What does that imply about the elements a cell must obtain in order to "
        "build proteins?",
      choices=[
        "It must obtain nitrogen as well as the sulfur that this topic assigns to "
        "proteins.",
        "It must obtain phosphorus as well as the sulfur that this topic assigns to "
        "proteins.",
        "It needs only carbon, hydrogen and oxygen, because an amine group contains no "
        "additional element.",
        "It needs sulfur alone, because the amine group is assembled from sulfur.",
        "It needs no element from the environment, because amine groups are synthesized "
        "from water."],
      ans=0,
      why="EK 1.7.A.1 and EK 1.7.A.2 place an amine group on every amino acid, and an "
          "amine group contains nitrogen, so protein synthesis requires a nitrogen supply "
          "in addition to the sulfur EK 1.2.A.1 i names. The chain runs through the "
          "protein statements because EK 1.2.A.1 iii itself names nitrogen only for "
          "nucleic acids."),

 dict(q="An animal eats plant material and uses the atoms in it to build its own tissues. "
        "Which statement best captures the relationship the course framework describes "
        "between the environment and macromolecule synthesis?",
      choices=[
        "The atoms are supplied from outside the organism and are reassembled into new "
        "molecules inside it.",
        "The atoms are created inside the organism and released into the environment as "
        "waste.",
        "The organism absorbs finished macromolecules and stores them without altering "
        "them.",
        "The organism converts nitrogen atoms into carbon atoms as it builds new "
        "tissues.",
        "The environment supplies energy only, while the atoms are already present in the "
        "newborn animal."],
      ans=0,
      why="EK 1.2.A.1 states that atoms and molecules from the environment are necessary "
          "to build new molecules. That is a claim about supply and reassembly, not about "
          "creating atoms, transmuting one element into another, or storing intact "
          "polymers."),

 dict(q="Which single element, if entirely absent from an organism's surroundings, would "
        "most directly prevent the building of both a class of lipid and the molecules "
        "that store hereditary information?",
      choices=["Phosphorus", "Sulfur", "Nitrogen", "Hydrogen", "Oxygen"],
      ans=0,
      why="EK 1.2.A.1 ii is the only sub-point that names two classes at once: phosphorus "
          "is used in the building of phospholipids, a type of lipid, and of nucleic "
          "acids. Sulfur reaches only proteins and nitrogen, in EK 1.2.A.1 iii, only "
          "nucleic acids."),
]
