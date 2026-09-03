# AP BIOLOGY 1.6 Nucleic Acids
# CED effective Fall 2025, Unit 1 Chemistry of Life. Big Idea 3 Information Storage
# and Transmission. Learning objective 1.6.A: describe the structure and function of
# DNA and RNA. Suggested skill 2.A.
#
# Essential knowledge relied on, in the framework's own words:
#   1.6.A.1    In nucleic acids (DNA and RNA), biological information is encoded in
#              sequences of nucleotide monomers. Each nucleotide has the following
#              structural components: a five-carbon sugar (deoxyribose or ribose), a
#              phosphate, and a nitrogenous base (adenine, thymine, guanine, cytosine,
#              or uracil).
#   1.6.A.2    Nucleic acids have a linear sequence of nucleotides that have ends,
#              defined by the 3 prime hydroxyl and 5 prime phosphates of the sugar in
#              the nucleotide. During nucleic acid synthesis, nucleotides are added to
#              the 3 prime end of the growing strand, resulting in the formation of
#              covalent bonds between nucleotides.
#              EXCLUSION STATEMENT -- The molecular structure of specific nucleotides
#              is beyond the scope of the AP Exam.
#   1.6.A.3    DNA is structured as an antiparallel double helix, with two strands of
#              nucleotides running in opposite 5 prime to 3 prime orientation. In DNA,
#              adenine nucleotides pair with thymine nucleotides via hydrogen bonds,
#              and cytosine nucleotides pair with guanine nucleotides via hydrogen
#              bonds. In RNA, adenine pairs with uracil.
#   1.6.A.4    Structural differences between DNA and RNA include:
#     i.       DNA contains the sugar deoxyribose, and RNA contains the sugar ribose.
#     ii.      DNA contains the nitrogenous base thymine, and RNA contains the
#              nitrogenous base uracil.
#     iii.     DNA is typically double stranded, while RNA is typically single
#              stranded.
#
# ON NOTATION. The CED prints 3' and 5' with a prime mark. Biology is exported as
# prose with no typesetting, so this bank writes "3 prime" and "5 prime" in words.
#
# ON THE DATA. The base composition tables are labelled in the stem and every keyed
# conclusion follows from EK 1.6.A.3's pairing rule applied to the numbers shown.
# Item 22's complementary strand is recomputed from the stem's own sequence in
# verify_b1_6.py, not taken on trust.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: Biology is exported as prose.
TOPIC = ("1.6", "Nucleic Acids", 1)

# The sequence used by item 22, and the reverse complement the verifier recomputes.
_SEQ_TOP = "A G G T C A"
_SEQ_COMPLEMENT = "T G A C C T"

_T_BASES = dict(
    headers=["Nucleic acid sample", "Adenine (percentage of all bases)",
             "Thymine (percentage of all bases)", "Guanine (percentage of all bases)",
             "Cytosine (percentage of all bases)", "Uracil (percentage of all bases)"],
    rows=[["Sample 1", "30", "30", "20", "20", "0"],
          ["Sample 2", "24", "0", "31", "20", "25"],
          ["Sample 3", "18", "18", "32", "32", "0"],
          ["Sample 4", "35", "20", "28", "17", "0"]])

_T_CHARGAFF = dict(
    headers=["Double-stranded DNA sample", "Adenine (percentage of all bases)"],
    rows=[["DNA W", "20"],
          ["DNA X", "32"],
          ["DNA Y", "15"],
          ["DNA Z", "25"]])

QUESTIONS = [

 dict(q="Which three structural components does the course framework list for every "
        "nucleotide?",
      choices=[
        "A five-carbon sugar, a phosphate, and a nitrogenous base",
        "A six-carbon sugar, a phosphate, and an amine group",
        "A five-carbon sugar, a fatty acid tail, and a nitrogenous base",
        "A phosphate, a carboxyl group, and an amine group",
        "A five-carbon sugar, a phosphate, and a variable R group"],
      ans=0,
      why="EK 1.6.A.1 lists exactly these three: a five-carbon sugar, deoxyribose or "
          "ribose, a phosphate, and a nitrogenous base. The carboxyl group, amine group "
          "and variable R group belong to an amino acid under EK 1.7.A.2, and a fatty "
          "acid tail belongs to a lipid under EK 1.5.A.1."),

 dict(q="Which set names all five nitrogenous bases the course framework lists for "
        "nucleic acids?",
      choices=[
        "Adenine, thymine, guanine, cytosine and uracil",
        "Adenine, thymine, guanine, cytosine and ribose",
        "Adenine, thymine, guanine, cytosine and deoxyribose",
        "Adenine, guanine, cytosine, uracil and phosphate",
        "Adenine, thymine, guanine, uracil and glycine"],
      ans=0,
      why="EK 1.6.A.1 names adenine, thymine, guanine, cytosine, or uracil as the "
          "nitrogenous base of a nucleotide. Ribose and deoxyribose are the sugars in the "
          "same sentence, phosphate is the third component, and glycine appears nowhere "
          "among the bases."),

 dict(q="Which two sugars does the course framework name as the five-carbon sugar of a "
        "nucleotide?",
      choices=["Deoxyribose and ribose", "Glucose and fructose",
               "Deoxyribose and glucose", "Ribose and cellulose",
               "Glycogen and starch"],
      ans=0,
      why="EK 1.6.A.1 gives the five-carbon sugar as deoxyribose or ribose. The rejected "
          "options substitute sugars and polysaccharides from the carbohydrate topic, "
          "which EK 1.4.A.1 treats and which are not nucleotide components."),

 dict(q="Where does the course framework say biological information is encoded in a "
        "nucleic acid?",
      choices=[
        "In the sequence of its nucleotide monomers",
        "In the total number of phosphate groups it contains",
        "In the ratio of its sugars to its bases",
        "In the number of hydrogen bonds holding its two strands together",
        "In the overall length of the molecule alone"],
      ans=0,
      why="EK 1.6.A.1 states that in nucleic acids biological information is encoded in "
          "sequences of nucleotide monomers. Counts, ratios and lengths are properties "
          "two different sequences can share, so none of them can be what carries the "
          "information."),

 dict(q="According to the course framework, what defines the two ends of a nucleic acid "
        "strand?",
      choices=[
        "The 3 prime hydroxyl and the 5 prime phosphate of the sugar in the nucleotide",
        "The nitrogenous base at each end of the strand",
        "The number of hydrogen bonds available at each end",
        "The 3 prime phosphate and the 5 prime hydroxyl of the nitrogenous base",
        "The point at which the double helix stops twisting"],
      ans=0,
      why="EK 1.6.A.2 states that nucleic acids have a linear sequence of nucleotides "
          "that have ends, defined by the 3 prime hydroxyl and 5 prime phosphates of the "
          "sugar in the nucleotide. The rejected option swaps which group sits at which "
          "end and moves both onto the base rather than the sugar."),

 dict(q="During nucleic acid synthesis, to which end of the growing strand are new "
        "nucleotides added?",
      choices=["The 3 prime end", "The 5 prime end", "Either end, at random",
               "Both ends at the same time", "The middle of the strand"],
      ans=0,
      why="EK 1.6.A.2 states that during nucleic acid synthesis nucleotides are added to "
          "the 3 prime end of the growing strand. The framework gives one direction, not "
          "a choice of ends and not a bidirectional or internal addition."),

 dict(q="What kind of bond forms between one nucleotide and the next as a strand is "
        "synthesized?",
      choices=["A covalent bond", "A hydrogen bond", "An ionic bond",
               "A hydrophobic interaction", "A peptide bond"],
      ans=0,
      why="EK 1.6.A.2 states that adding nucleotides to the 3 prime end results in the "
          "formation of covalent bonds between nucleotides. Hydrogen bonds are what EK "
          "1.6.A.3 uses for base pairing across the two strands, and a peptide bond joins "
          "amino acids under EK 1.7.A.1."),

 dict(q="How does the course framework describe the arrangement of the two strands in a "
        "DNA molecule?",
      choices=[
        "An antiparallel double helix, with the two strands running in opposite 5 prime "
        "to 3 prime orientation",
        "A parallel double helix, with both strands running in the same 5 prime to 3 "
        "prime orientation",
        "A single helix folded back on itself at one end",
        "Two straight strands lying side by side without twisting",
        "A branched network of strands joined at many points"],
      ans=0,
      why="EK 1.6.A.3 states that DNA is structured as an antiparallel double helix with "
          "two strands of nucleotides running in opposite 5 prime to 3 prime orientation. "
          "Antiparallel is precisely the denial of the parallel arrangement the second "
          "option describes."),

 dict(q="Which base pairs does the course framework give for DNA, and what holds each "
        "pair together?",
      choices=[
        "Adenine with thymine and cytosine with guanine, held by hydrogen bonds",
        "Adenine with guanine and cytosine with thymine, held by hydrogen bonds",
        "Adenine with thymine and cytosine with guanine, held by covalent bonds",
        "Adenine with uracil and cytosine with guanine, held by hydrogen bonds",
        "Adenine with cytosine and thymine with guanine, held by ionic bonds"],
      ans=0,
      why="EK 1.6.A.3 states that in DNA adenine nucleotides pair with thymine "
          "nucleotides via hydrogen bonds and cytosine nucleotides pair with guanine "
          "nucleotides via hydrogen bonds. Adenine with uracil is the RNA pairing in the "
          "same statement, and the covalent bonds of EK 1.6.A.2 run along a strand rather "
          "than across the pair."),

 dict(q="In RNA, adenine pairs with which base?",
      choices=["Uracil", "Thymine", "Guanine", "Cytosine", "Adenine"],
      ans=0,
      why="EK 1.6.A.3 ends by stating that in RNA adenine pairs with uracil. Thymine is "
          "adenine's partner in DNA under the same statement, and EK 1.6.A.4 ii places "
          "thymine in DNA and uracil in RNA."),

 dict(q="Which sugar difference does the course framework give between DNA and RNA?",
      choices=[
        "DNA contains deoxyribose and RNA contains ribose.",
        "DNA contains ribose and RNA contains deoxyribose.",
        "Both contain deoxyribose, and only the bases differ.",
        "Both contain ribose, and only the number of strands differs.",
        "DNA contains glucose and RNA contains ribose."],
      ans=0,
      why="EK 1.6.A.4 i states that DNA contains the sugar deoxyribose and RNA contains "
          "the sugar ribose. The second option reverses the assignment and the last "
          "substitutes a carbohydrate that EK 1.4.A.1 treats as a monosaccharide, not a "
          "nucleotide sugar."),

 dict(q="Which base is found in DNA but not in RNA, and which is found in RNA but not in "
        "DNA?",
      choices=[
        "Thymine is in DNA and uracil is in RNA.",
        "Uracil is in DNA and thymine is in RNA.",
        "Guanine is in DNA and cytosine is in RNA.",
        "Adenine is in DNA and thymine is in RNA.",
        "Cytosine is in DNA and adenine is in RNA."],
      ans=0,
      why="EK 1.6.A.4 ii states that DNA contains the nitrogenous base thymine and RNA "
          "contains the nitrogenous base uracil. Adenine, guanine and cytosine are common "
          "to both, so the rejected options name bases that do not distinguish them."),

 dict(q="How do DNA and RNA typically differ in the number of strands they contain?",
      choices=[
        "DNA is typically double stranded and RNA is typically single stranded.",
        "DNA is typically single stranded and RNA is typically double stranded.",
        "Both are always double stranded.",
        "Both are always single stranded.",
        "DNA is always triple stranded and RNA is always double stranded."],
      ans=0,
      why="EK 1.6.A.4 iii states that DNA is typically double stranded while RNA is "
          "typically single stranded. The framework says typically rather than always, "
          "which is why the two options asserting a universal rule overstate it."),

 dict(q="The course framework carries an exclusion statement for this topic. What does it "
        "place beyond the scope of the exam?",
      choices=[
        "The molecular structure of specific nucleotides",
        "The names of the nitrogenous bases",
        "The pairing of adenine with thymine in DNA",
        "The direction in which a growing strand is extended",
        "The difference in sugar between DNA and RNA"],
      ans=0,
      why="The exclusion statement printed under EK 1.6.A.2 says that the molecular "
          "structure of specific nucleotides is beyond the scope of the AP Exam. The four "
          "rejected options restate content EK 1.6.A.1, EK 1.6.A.2, EK 1.6.A.3 and EK "
          "1.6.A.4 do require."),

 dict(q="The table gives the base composition of four purified nucleic acid samples. "
        "Which nitrogenous base is present in exactly one of the four samples?",
      table=_T_BASES,
      choices=["Uracil", "Adenine", "Guanine", "Cytosine", "Thymine"],
      ans=0,
      why="Reading down the five base columns, four of them are nonzero in more than one "
          "sample and only one is nonzero in a single sample. EK 1.6.A.4 ii is why that "
          "base is the scarce one: it places thymine in DNA and uracil in RNA, and only "
          "one of the four samples is a nucleic acid of the second kind."),

 dict(q="Which samples in the table have base compositions consistent with a "
        "double-stranded DNA molecule?",
      table=_T_BASES,
      choices=[
        "Sample 1 and Sample 3",
        "Sample 1 and Sample 2",
        "Sample 2 and Sample 4",
        "Sample 3 and Sample 4",
        "All four samples"],
      ans=0,
      why="EK 1.6.A.3 pairs every adenine with a thymine and every cytosine with a "
          "guanine across the two strands, so in a double-stranded DNA the adenine and "
          "thymine percentages must match and so must the cytosine and guanine "
          "percentages. Exactly two rows satisfy both equalities and carry no uracil."),

 dict(q="One sample in the table contains no uracil yet cannot be a double-stranded DNA "
        "molecule. Which sample is it, and why?",
      table=_T_BASES,
      choices=[
        "Sample 4, because its adenine and thymine percentages are unequal",
        "Sample 1, because its adenine and thymine percentages are unequal",
        "Sample 3, because it contains more guanine than adenine",
        "Sample 2, because it contains no thymine",
        "Sample 4, because it contains more adenine than any other sample"],
      ans=0,
      why="Under EK 1.6.A.3 each adenine in a double helix is paired with a thymine and "
          "each cytosine with a guanine, so unequal adenine and thymine percentages rule "
          "the double-stranded arrangement out. Holding more guanine than adenine or the "
          "most adenine of any sample violates nothing in the framework."),

 dict(q="For the sample in the table whose adenine and thymine percentages are both 18, "
        "what percentage of the bases are guanine and cytosine taken together?",
      table=_T_BASES,
      choices=["64 percent", "32 percent", "36 percent", "50 percent", "82 percent"],
      ans=0,
      why="The four base percentages of that row must sum to 100, so subtracting the "
          "adenine and thymine shares leaves the guanine and cytosine share. The 32 "
          "percent distractor is the guanine share alone, which is half the correct "
          "total because EK 1.6.A.3 makes guanine and cytosine equal in a double helix."),

 dict(q="Each sample in the second table is a double-stranded DNA molecule, with its "
        "adenine content given as a percentage of all bases. What percentage of the bases "
        "in the sample containing 20 percent adenine are guanine?",
      table=_T_CHARGAFF,
      choices=["30 percent", "20 percent", "40 percent", "60 percent", "80 percent"],
      ans=0,
      why="EK 1.6.A.3 makes thymine equal to adenine and cytosine equal to guanine in a "
          "double helix. Adenine and thymine therefore take 40 percent between them, "
          "leaving 60 percent shared equally by guanine and cytosine. The 60 percent "
          "distractor is that shared total reported as one base's share."),

 dict(q="Among the double-stranded DNA samples in the second table, which one contains "
        "the greatest percentage of cytosine?",
      table=_T_CHARGAFF,
      choices=["DNA Y", "DNA W", "DNA X", "DNA Z",
               "All four contain the same percentage of cytosine."],
      ans=0,
      why="Under EK 1.6.A.3 adenine equals thymine and cytosine equals guanine, so the "
          "cytosine share is half of what is left after twice the adenine share is "
          "removed. That share is largest where adenine is smallest, and the table gives "
          "a unique smallest adenine value."),

 dict(q="One double-stranded DNA sample in the second table contains 25 percent adenine. "
        "What does that imply about its other three bases?",
      table=_T_CHARGAFF,
      choices=[
        "Each of the other three bases also makes up 25 percent of the total.",
        "Thymine makes up 25 percent and guanine and cytosine make up 12.5 percent each.",
        "Guanine makes up 50 percent and cytosine and thymine make up 12.5 percent each.",
        "Thymine makes up 75 percent and the remaining bases are absent.",
        "The other three bases cannot be determined from the adenine percentage alone."],
      ans=0,
      why="EK 1.6.A.3 forces thymine to equal adenine and cytosine to equal guanine in a "
          "double helix, so 25 percent adenine leaves 50 percent to be shared equally "
          "between guanine and cytosine. The pairing rule is exactly what makes the other "
          "three determinable, contrary to the final option."),

 dict(q="One strand of a DNA double helix reads, from its 5 prime end to its 3 prime end, "
        "A G G T C A. Written from its own 5 prime end to its own 3 prime end, what is "
        "the sequence of the complementary strand?",
      choices=["T G A C C T", "T C C A G T", "A G G T C A", "U G A C C U", "A C T G G A"],
      ans=0,
      why="EK 1.6.A.3 pairs adenine with thymine and cytosine with guanine, and makes the "
          "two strands antiparallel, so the partner of each base must be read back in the "
          "opposite direction. Pairing without reversing gives the second option, and "
          "substituting uracil would make the partner RNA rather than DNA."),

 dict(q="A strand of DNA is being extended by the addition of nucleotides. Which "
        "statement about that extension matches the course framework?",
      choices=[
        "New nucleotides join the 3 prime end and are attached by covalent bonds.",
        "New nucleotides join the 5 prime end and are attached by covalent bonds.",
        "New nucleotides join the 3 prime end and are attached by hydrogen bonds.",
        "New nucleotides join wherever a hydrogen bond happens to break.",
        "New nucleotides are inserted between existing nucleotides in the middle of the "
        "strand."],
      ans=0,
      why="EK 1.6.A.2 puts both halves in one sentence: nucleotides are added to the 3 "
          "prime end of the growing strand, resulting in the formation of covalent bonds "
          "between nucleotides. Hydrogen bonds belong to base pairing across strands "
          "under EK 1.6.A.3."),

 dict(q="If one strand of a DNA double helix is drawn running from left to right in the 5 "
        "prime to 3 prime direction, how does its partner strand run?",
      choices=[
        "From right to left in the 5 prime to 3 prime direction",
        "From left to right in the 5 prime to 3 prime direction",
        "From left to right, but with no defined orientation",
        "In the same direction, since both strands are identical in sequence",
        "Perpendicular to the first strand"],
      ans=0,
      why="EK 1.6.A.3 states that the two strands of the antiparallel double helix run in "
          "opposite 5 prime to 3 prime orientation, so if one reads left to right in that "
          "direction the other must read right to left. The strands are also "
          "complementary rather than identical under the same statement."),

 dict(q="Which comparison correctly separates the two kinds of bond the course framework "
        "assigns to a DNA molecule?",
      choices=[
        "Covalent bonds join neighbouring nucleotides along a strand; hydrogen bonds hold "
        "the paired bases across the two strands.",
        "Hydrogen bonds join neighbouring nucleotides along a strand; covalent bonds hold "
        "the paired bases across the two strands.",
        "Covalent bonds do both jobs, since every bond in DNA is covalent.",
        "Hydrogen bonds do both jobs, since every bond in DNA is a hydrogen bond.",
        "Ionic bonds join neighbouring nucleotides and covalent bonds hold the pairs."],
      ans=0,
      why="EK 1.6.A.2 gives covalent bonds between nucleotides as the result of adding to "
          "the 3 prime end, and EK 1.6.A.3 gives hydrogen bonds as what pairs adenine "
          "with thymine and cytosine with guanine. The two statements assign the two "
          "bond types to two different places in the molecule."),

 dict(q="A compound is found to block the addition of nucleotides to the 3 prime end of a "
        "growing nucleic acid strand. Which outcome is predicted most directly?",
      choices=[
        "Strands already present will not be extended.",
        "Existing double-stranded DNA will separate into single strands.",
        "Adenine will begin to pair with cytosine instead of thymine.",
        "The sugar in each nucleotide will change from deoxyribose to ribose.",
        "Strands will be extended from their 5 prime end instead."],
      ans=0,
      why="EK 1.6.A.2 makes addition at the 3 prime end the way a strand is extended, so "
          "blocking it blocks extension. The framework offers no alternative growing end, "
          "and neither the pairing rule of EK 1.6.A.3 nor the sugar of EK 1.6.A.4 i "
          "depends on that step."),

 dict(q="A student states that DNA and RNA differ only in the sugar each contains. Which "
        "correction is best supported by the course framework?",
      choices=[
        "They also differ in one nitrogenous base and in how many strands they typically "
        "have.",
        "They also differ in whether their nucleotides carry a phosphate group.",
        "They also differ in whether their monomers are joined by covalent bonds.",
        "They also differ in whether they encode biological information at all.",
        "The student is correct, because the sugar is the only difference the framework "
        "names."],
      ans=0,
      why="EK 1.6.A.4 lists three differences, not one: the sugar in i, thymine against "
          "uracil in ii, and typically double stranded against typically single stranded "
          "in iii. Both molecules carry a phosphate under EK 1.6.A.1, are joined "
          "covalently under EK 1.6.A.2, and encode information under EK 1.6.A.1."),

 dict(q="A nucleic acid is found to be single stranded, to contain ribose, and to contain "
        "uracil but no thymine. What is it?",
      choices=["RNA", "DNA", "A protein", "A polysaccharide", "A phospholipid"],
      ans=0,
      why="All three observations are the RNA side of EK 1.6.A.4: ribose in i, uracil in "
          "ii, and typically single stranded in iii. A protein, a polysaccharide and a "
          "phospholipid contain none of these components under EK 1.7.A.1, EK 1.4.A.1 and "
          "EK 1.5.A.2 iv."),

 dict(q="Which component of a nucleotide is the same whether the nucleotide belongs to "
        "DNA or to RNA?",
      choices=["The phosphate", "The five-carbon sugar",
               "The base that pairs with adenine", "The number of strands present",
               "The direction in which the strand is extended"],
      ans=0,
      why="EK 1.6.A.1 gives a phosphate as a component of every nucleotide and EK 1.6.A.4 "
          "lists what differs between DNA and RNA: the sugar, one base, and typical "
          "strandedness. The phosphate appears on neither side of that list of "
          "differences."),

 dict(q="Two DNA molecules of the same length contain exactly the same percentages of all "
        "four bases but carry different genetic information. How is that possible, "
        "according to the course framework?",
      choices=[
        "Biological information is encoded in the order of the nucleotides, which "
        "composition percentages do not fix.",
        "Biological information is encoded in the base percentages, so the two molecules "
        "must in fact carry the same information.",
        "Biological information is encoded in the number of hydrogen bonds, which can "
        "differ at equal composition.",
        "Biological information is encoded in the sugar, which can differ between two DNA "
        "molecules.",
        "Biological information is encoded in the length of the molecule, so equal "
        "lengths make this impossible."],
      ans=0,
      why="EK 1.6.A.1 states that biological information is encoded in sequences of "
          "nucleotide monomers, and a sequence is an order rather than a count. Two "
          "different orders of the same collection of nucleotides therefore encode "
          "different information while sharing every percentage."),
]
