# AP BIOLOGY 6.6 Gene Expression and Cell Specialization
# CED effective Fall 2025, Unit 6 Gene Expression and Regulation. Big idea 3
# (Information Storage and Transmission). Learning objectives 6.6.A, explain how
# the binding of transcription factors to promoter regions affects gene
# expression and the phenotype of the organism, and 6.6.B, explain the
# connection between the regulation of gene expression and phenotypic
# differences in cells and organisms. Suggested skill 6.B, SUPPORT A CLAIM WITH
# EVIDENCE from biological principles, concepts, processes, and data.
#
# Essential knowledge relied on, in the framework's own words:
#   6.6.A.1  RNA polymerase and transcription factors bind to PROMOTER OR
#            ENHANCER DNA sequences to initiate transcription. These sequences
#            can be UPSTREAM OR DOWNSTREAM of the transcription start site.
#   6.6.A.2  NEGATIVE regulatory molecules inhibit gene expression by binding to
#            DNA and blocking transcription.
#   6.6.B.1  Gene regulation results in differential gene expression and
#            INFLUENCES CELL PRODUCTS AND FUNCTIONS.
#   6.6.B.2  Certain SMALL RNA molecules have roles in regulating gene
#            expression.
#
# DIVISION OF LABOUR WITH 6.5 is set out in full in the header of b6_5.py. In
# short: 6.5 asks what regulation is and what it produces -- regulatory
# sequences in general, constitutive against inducible, epigenetic modification,
# operons, coordinate regulation, differentiation, sequential induction. 6.6 asks
# WHERE the sequences sit and WHICH molecules act on them -- promoters and
# enhancers upstream or downstream of the start site, negative regulatory
# molecules, small RNAs, and the causal step from differential expression to cell
# products and functions. Both topics name transcription factors and neither asks
# the other's question about them.
#
# ON THE SUGGESTED SKILL. 6.B is support a claim with evidence, so the applied
# items here are built as claim-and-evidence pairs: the stem states a claim and
# the choices offer candidate evidence, or the table supplies data and the
# choices offer candidate claims. That is the shape the CED asks for and it is
# also what keeps thirty items off four statements from becoming thirty
# rewordings of those statements.
#
# ON FIGURES. No stem refers to a diagram of a gene, a gel or a blot. Every data
# set is a table=.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX. Positions
# are written "upstream" and "downstream", never with a hyphenated number.
TOPIC = ("6.6", "Gene Expression and Cell Specialization", 6)

# A reporter gene transcribed in two cell extracts.
_T_TF = dict(
    headers=["Cell extract", "Transcription factor 1 present",
             "Transcription of the reporter gene (arbitrary units)"],
    rows=[["Extract 1", "Yes", "165"],
          ["Extract 2", "No", "8"]])

# The same gene transcribed with and without one added molecule.
_T_NEG = dict(
    headers=["Reaction", "Molecule M added",
             "Transcription of the gene (arbitrary units)"],
    rows=[["Reaction 1", "No", "140"],
          ["Reaction 2", "Yes", "9"]])

# One regulatory sequence placed on either side of the start site, or removed.
_T_POS = dict(
    headers=["Construct",
             "Position of the regulatory sequence relative to the transcription start site",
             "Transcription of the gene (arbitrary units)"],
    rows=[["Construct 1", "Upstream", "150"],
          ["Construct 2", "Downstream", "144"],
          ["Construct 3", "The sequence was removed altogether", "11"]])

# Three genes measured in two kinds of cell from one organism.
_T_CELLS = dict(
    headers=["Gene", "Expression in liver cells (arbitrary units)",
             "Expression in muscle cells (arbitrary units)"],
    rows=[["Gene 1", "210", "6"],
          ["Gene 2", "5", "190"],
          ["Gene 3", "70", "74"]])

# One target gene followed after two small RNA molecules are supplied.
_T_SMALL = dict(
    headers=["Treatment of the cells",
             "Amount of the target gene's mRNA (arbitrary units)",
             "Amount of the target gene's protein (arbitrary units)"],
    rows=[["No small RNA supplied", "120", "95"],
          ["Small RNA 1 supplied", "118", "11"],
          ["Small RNA 2 supplied", "14", "10"]])

# One target gene surveyed across three kinds of cell.
_T_TFCELL = dict(
    headers=["Cell type", "Transcription factor 2 present", "Target gene expressed"],
    rows=[["Cell type 1", "Yes", "Yes"],
          ["Cell type 2", "No", "No"],
          ["Cell type 3", "Yes", "Yes"]])

QUESTIONS = [
 dict(q="Which molecules bind to promoter or enhancer DNA sequences in order to initiate transcription?",
   choices=[
     "RNA polymerase and transcription factors",
     "Ribosomal RNA and transfer RNA",
     "DNA polymerase and ligase",
     "Histones and the associated proteins that condense chromosomes",
     "The mature mRNA transcript and its poly-A tail"], ans=0,
   why="EK 6.6.A.1 states that RNA polymerase and transcription factors bind to promoter or enhancer DNA sequences to initiate transcription. DNA polymerase and ligase are replication participants under EK 6.2.A.1, and the two named RNA types belong to translation under EK 6.3.A.1."),
 dict(q="Where can the promoter and enhancer sequences that regulate a gene be located?",
   choices=[
     "Either upstream or downstream of the transcription start site",
     "Only upstream of the transcription start site",
     "Only downstream of the transcription start site",
     "Only on a different chromosome from the gene they regulate",
     "Only within the mRNA transcript, after it has been made"], ans=0,
   why="EK 6.6.A.1 states that these sequences can be upstream or downstream of the transcription start site. The framework therefore does not confine a regulatory sequence to one side, and the sequences are DNA rather than part of the transcript."),
 dict(q="A researcher finds a sequence that increases transcription of a gene and shows that it lies downstream of that gene's transcription start site. What should the researcher conclude?",
   choices=[
     "The finding is consistent with the framework, which allows these sequences on either side of the start site",
     "The finding must be an error, because a regulatory sequence can only lie upstream",
     "The sequence must be an intron, because only introns lie downstream of the start site",
     "The sequence must act on a different gene, because a sequence cannot regulate a gene it lies within",
     "The sequence must be a promoter rather than an enhancer, because promoters lie downstream"], ans=0,
   why="EK 6.6.A.1 states that promoter or enhancer sequences can be upstream or downstream of the transcription start site, so a downstream location is not a reason to doubt the result. The framework does not assign one side to promoters and the other to enhancers."),
 dict(q="How do negative regulatory molecules affect gene expression, according to the framework?",
   choices=[
     "They inhibit expression by binding to DNA and blocking transcription",
     "They inhibit expression by binding to the mRNA and blocking its export",
     "They increase expression by binding to DNA and recruiting RNA polymerase",
     "They inhibit expression by removing the gene from the chromosome",
     "They inhibit expression by breaking down the protein after it is made"], ans=0,
   why="EK 6.6.A.2 states that negative regulatory molecules inhibit gene expression by binding to DNA and blocking transcription. The framework names both the target, DNA, and the step blocked, transcription, so options that move the action to the transcript or to the finished protein change the statement."),
 dict(q="What distinguishes the action of a transcription factor at a promoter from the action of a negative regulatory molecule?",
   choices=[
     "The transcription factor binds a promoter or enhancer to initiate transcription, while the negative regulatory molecule binds DNA to block it",
     "The transcription factor binds DNA to block transcription, while the negative regulatory molecule binds a promoter to initiate it",
     "The transcription factor binds DNA while the negative regulatory molecule binds the mRNA",
     "The transcription factor acts in eukaryotes only while the negative regulatory molecule acts in prokaryotes only",
     "There is no difference, since both molecules increase the rate of transcription"], ans=0,
   why="EK 6.6.A.1 has RNA polymerase and transcription factors bind promoter or enhancer sequences to initiate transcription and EK 6.6.A.2 has negative regulatory molecules bind DNA and block it. Both act on DNA, so the difference is the direction of the effect rather than the kind of target."),
 dict(q="A reporter gene was transcribed in two cell extracts that differed only in one component, as reported in the table. Which claim do these data support?",
   table=_T_TF,
   choices=[
     "Transcription of this gene depends on the presence of transcription factor 1",
     "Transcription of this gene is blocked by the presence of transcription factor 1",
     "Transcription factor 1 has no measurable effect on transcription of this gene",
     "Transcription factor 1 is transcribed from the reporter gene",
     "Transcription of this gene depends on the absence of every transcription factor"], ans=0,
   why="EK 6.6.A.1 has transcription factors bind promoter or enhancer sequences to initiate transcription, and skill 6.B asks for a claim supported by the data. Transcription reads 165 units with the factor and 8 units without it, which is a large fall in its absence, so the factor is required rather than inhibitory or irrelevant."),
 dict(q="The same gene was transcribed with and without one added molecule, as reported in the table. Which claim do these data support?",
   table=_T_NEG,
   choices=[
     "Molecule M acts as a negative regulator of this gene",
     "Molecule M acts as a positive regulator of this gene",
     "Molecule M has no measurable effect on this gene",
     "Molecule M is the product of this gene's transcription",
     "Molecule M is required for transcription of this gene to occur at all"], ans=0,
   why="EK 6.6.A.2 states that negative regulatory molecules inhibit gene expression by binding to DNA and blocking transcription. Transcription reads 140 units without the molecule and 9 units with it, so adding the molecule reduces transcription, which is the negative direction and the opposite of what a requirement for transcription would show."),
 dict(q="One regulatory sequence was tested in three constructs, as reported in the table. Which claim do these data support?",
   table=_T_POS,
   choices=[
     "The sequence increases transcription from either side of the transcription start site",
     "The sequence increases transcription only when it lies upstream of the transcription start site",
     "The sequence increases transcription only when it lies downstream of the transcription start site",
     "The sequence has no effect on transcription, since transcription occurs in all three constructs",
     "The sequence decreases transcription, since removing it left transcription measurable"], ans=0,
   why="EK 6.6.A.1 states that promoter or enhancer sequences can be upstream or downstream of the transcription start site. Transcription reads 150 units with the sequence upstream and 144 with it downstream, which are close to each other, and 11 units when it is removed, so the sequence raises transcription and the side it sits on makes little difference."),
 dict(q="What does the framework say gene regulation results in, and what does that influence?",
   choices=[
     "Differential gene expression, which influences cell products and functions",
     "Differential DNA replication, which influences the number of genes a cell carries",
     "Differential base pairing, which influences the genetic code the cell uses",
     "Identical gene expression in every cell, which influences the organism's size",
     "The loss of unused genes, which influences which products a cell can make"], ans=0,
   why="EK 6.6.B.1 states that gene regulation results in differential gene expression and influences cell products and functions. Base pairing is conserved under EK 6.1.B.1 and the genetic code is shared under EK 6.4.A.3.iv, neither of which regulation alters."),
 dict(q="Three genes were measured in two kinds of cell from one organism, as reported in the table. Which claim do these data support?",
   table=_T_CELLS,
   choices=[
     "Two of the three genes are expressed very differently in the two cell types, which is differential gene expression",
     "All three genes are expressed very differently in the two cell types, which is differential gene expression",
     "None of the genes is expressed differently, so the two cell types must carry different genomes",
     "The two cell types carry different genes, which is why two of the measurements differ",
     "The gene expressed at similar levels in both cell types must be the one that specifies the cell type"], ans=0,
   why="EK 6.6.B.1 states that gene regulation results in differential gene expression and influences cell products and functions. Two genes differ by more than thirtyfold between the two cell types while the third reads 70 and 74 units, so the differential expression involves two of the three; cells of one organism share a genome, so a difference in genes is not available as an explanation."),
 dict(q="What does the framework say about small RNA molecules?",
   choices=[
     "Certain small RNA molecules have roles in regulating gene expression",
     "Small RNA molecules are the template strands from which genes are transcribed",
     "Small RNA molecules are the functional building blocks of ribosomes",
     "Small RNA molecules carry amino acids to the ribosome during translation",
     "Small RNA molecules replace the promoter sequences of the genes they act on"], ans=0,
   why="EK 6.6.B.2 states that certain small RNA molecules have roles in regulating gene expression. The rejected options assign them the roles the framework gives to the DNA template under EK 6.3.A.2, to rRNA under EK 6.3.A.1.iii and to tRNA under EK 6.3.A.1.ii."),
 dict(q="Cells were supplied with each of two small RNA molecules in turn, and the target gene's mRNA and protein were measured, as reported in the table. Which claim do these data support?",
   table=_T_SMALL,
   choices=[
     "Both small RNA molecules reduce the amount of the target gene's protein, so both have a role in regulating its expression",
     "Neither small RNA molecule affects the target gene, since some mRNA is present in every treatment",
     "Only the small RNA that reduces the amount of mRNA has a role in regulating the gene",
     "Both small RNA molecules increase the amount of the target gene's protein",
     "Both small RNA molecules act by removing the target gene from the chromosome"], ans=0,
   why="EK 6.6.B.2 states that certain small RNA molecules have roles in regulating gene expression. The protein falls from 95 units to 11 and to 10 under the two treatments, so both reduce the gene's product; one leaves the mRNA near its starting level while the other lowers it, which is a difference in how they act rather than in whether they regulate."),
 dict(q="A change makes the promoter of one gene unrecognizable to the molecules that normally bind it. What is the most direct expected consequence?",
   choices=[
     "Transcription of that gene is no longer initiated at its usual rate",
     "That gene is translated without being transcribed first",
     "The genetic code used to read that gene changes",
     "That gene is removed from the chromosome",
     "Every gene in the cell stops being transcribed"], ans=0,
   why="EK 6.6.A.1 has RNA polymerase and transcription factors bind promoter or enhancer sequences to initiate transcription, so a promoter that cannot be bound cannot serve that function for its own gene. Nothing in the framework allows translation without a transcript or changes the shared genetic code of EK 6.4.A.3.iv."),
 dict(q="A cell lacks one particular transcription factor. What is expected of the genes whose promoters that factor normally binds?",
   choices=[
     "They are transcribed at a much lower rate, because the molecule that helps initiate their transcription is absent",
     "They are transcribed at a much higher rate, because a factor blocking them is absent",
     "They are transcribed at their usual rate, because RNA polymerase acts alone",
     "They are removed from the genome, because a gene that is not transcribed is discarded",
     "They are transcribed into protein directly, bypassing the mRNA stage"], ans=0,
   why="EK 6.6.A.1 states that RNA polymerase and transcription factors bind promoter or enhancer sequences to initiate transcription, so both are named as participants in initiation. Blocking is what EK 6.6.A.2 assigns to negative regulatory molecules, which a transcription factor at a promoter is not."),
 dict(q="A researcher claims that a particular DNA segment is a regulatory sequence for a nearby gene. Which finding would best support that claim?",
   choices=[
     "Removing the segment sharply reduces transcription of that gene while leaving the gene's own sequence intact",
     "The segment is transcribed into an mRNA that is translated into a protein",
     "The segment has the same base composition as the rest of the chromosome",
     "The segment lies downstream of the gene's transcription start site",
     "The segment is present in every cell of the organism"], ans=0,
   why="EK 6.6.A.1 makes a regulatory sequence one that molecules bind in order to initiate transcription of a gene, so the supporting evidence is a change in that gene's transcription when the segment is altered. Position alone cannot support the claim because EK 6.6.A.1 allows either side, and every cell of an organism carries the whole genome."),
 dict(q="A researcher claims that a newly purified protein is a negative regulatory molecule. Which finding would best support that claim?",
   choices=[
     "Adding the protein to a transcription reaction reduces transcription, and the protein is found bound to the gene's DNA",
     "Adding the protein to a transcription reaction increases transcription, and the protein is found bound to the gene's DNA",
     "Adding the protein to a cell increases the amount of the gene's mRNA",
     "The protein is encoded by a gene that lies next to the gene it is said to regulate",
     "The protein is present in every cell type of the organism"], ans=0,
   why="EK 6.6.A.2 states that negative regulatory molecules inhibit gene expression by binding to DNA and blocking transcription, which names two things to demonstrate: the reduction in transcription and the binding to DNA. Evidence showing an increase supports the opposite claim, and neither the protein's own gene's position nor its distribution addresses either half."),
 dict(q="A liver cell and a muscle cell of one organism carry the same genome but make different sets of proteins and perform different functions. Which framework statement identifies the source of the difference?",
   choices=[
     "Gene regulation results in differential gene expression, which in turn influences cell products and functions",
     "Differences in cell products and functions cause the genes of each cell type to be regulated differently",
     "Each cell type is transcribed using a different genetic code, giving different products",
     "Each cell type retains only the genes whose products it needs",
     "Each cell type carries a different number of chromosomes, giving different products"], ans=0,
   why="EK 6.6.B.1 states that gene regulation results in differential gene expression and influences cell products and functions, which sets the direction of the account: regulation first, products and functions after. The reversed option makes the outcome the cause, and EK 6.4.A.3.iv makes the code shared across organisms."),
 dict(q="A target gene was surveyed across three kinds of cell, as reported in the table. Which claim do these data support?",
   table=_T_TFCELL,
   choices=[
     "The target gene is expressed in exactly the cell types in which transcription factor 2 is present",
     "The target gene is expressed in exactly the cell types in which transcription factor 2 is absent",
     "The target gene is expressed in every cell type surveyed",
     "The target gene is expressed in no cell type surveyed",
     "Transcription factor 2 is present in every cell type, so it cannot explain the pattern"], ans=0,
   why="EK 6.6.A.1 has transcription factors bind promoter or enhancer sequences to initiate transcription, and EK 6.6.B.1 makes differential expression the result of regulation. In the table the factor is present in two of the three cell types and the gene is expressed in exactly those two, so presence and expression coincide."),
 dict(q="What is the difference between a transcription factor and the sequence it binds?",
   choices=[
     "The transcription factor is a molecule that binds, and the sequence is the stretch of DNA it binds to",
     "The transcription factor is a stretch of DNA, and the sequence is the molecule that binds it",
     "The transcription factor is a stretch of RNA, and the sequence is the protein it binds",
     "They are the same thing described in two ways, since a factor is named for its sequence",
     "The transcription factor is the mRNA product, and the sequence is the promoter that made it"], ans=0,
   why="EK 6.6.A.1 states that RNA polymerase and transcription factors bind to promoter or enhancer DNA sequences, which places the factor on the binding side and the promoter or enhancer on the DNA side. EK 6.5.A.1 makes the same division for regulatory sequences and regulatory proteins."),
 dict(q="Why can one gene be transcribed in one kind of cell and not in another kind of cell of the same organism?",
   choices=[
     "The two cell types differ in which regulatory molecules are present to act on that gene",
     "The two cell types differ in which genes they carry in their genomes",
     "The two cell types differ in the genetic code they use to read the gene",
     "The two cell types differ in the direction in which they transcribe the gene",
     "The two cell types differ in whether their DNA obeys the base pairing rules"], ans=0,
   why="EK 6.6.A.1 makes transcription depend on molecules binding promoter or enhancer sequences and EK 6.6.A.2 adds molecules that block transcription, so which regulatory molecules a cell contains determines what it transcribes. EK 6.6.B.1 makes the resulting differential expression the source of the differences between cells."),
 dict(q="An experimental treatment supplies a cell with a small RNA molecule directed at one gene, and the amount of that gene's protein falls sharply while the gene itself is unchanged. What does this result illustrate?",
   choices=[
     "That certain small RNA molecules have roles in regulating gene expression",
     "That small RNA molecules alter the base sequence of the genes they act on",
     "That small RNA molecules are translated into the protein whose amount fell",
     "That small RNA molecules replace the transcription factors a gene requires",
     "That small RNA molecules bind amino acids and deliver them to the ribosome"], ans=0,
   why="EK 6.6.B.2 states that certain small RNA molecules have roles in regulating gene expression, which is a claim about the amount of a gene's product rather than about its sequence. The gene is stated to be unchanged, and delivering amino acids is tRNA's role under EK 6.3.A.1.ii."),
 dict(q="Adding a particular molecule to a cell causes the transcription of one gene to fall sharply, and the molecule is found bound to that gene's DNA. Which description fits the molecule?",
   choices=[
     "A negative regulatory molecule, which inhibits expression by binding DNA and blocking transcription",
     "A transcription factor at a promoter, which initiates transcription of the gene",
     "An enhancer sequence, which raises transcription from either side of the start site",
     "A small RNA molecule, which must be transcribed from the same gene",
     "An RNA polymerase, which synthesizes the transcript from a template strand"], ans=0,
   why="EK 6.6.A.2 states that negative regulatory molecules inhibit gene expression by binding to DNA and blocking transcription, and the observation supplies both halves. An enhancer is a DNA sequence rather than a molecule that binds DNA under EK 6.6.A.1, and RNA polymerase and transcription factors initiate transcription rather than reduce it."),
 dict(q="A construct is made in which the promoter of a gene is deleted while the rest of the gene is left intact. What is expected?",
   choices=[
     "Transcription of the gene falls sharply, because the sequence that molecules bind in order to initiate it is gone",
     "Transcription of the gene rises sharply, because a sequence that was blocking it is gone",
     "Transcription of the gene is unaffected, because the coding part of the gene is intact",
     "The gene is transcribed from a promoter on a different chromosome instead",
     "The gene is translated directly, since it no longer needs to be transcribed"], ans=0,
   why="EK 6.6.A.1 states that RNA polymerase and transcription factors bind promoter or enhancer DNA sequences to initiate transcription, so removing the promoter removes what initiation depends on. Blocking is the role EK 6.6.A.2 gives to negative regulatory molecules, not to a promoter."),
 dict(q="Which of the following pairs an event with the correct direction of its effect on transcription?",
   choices=[
     "A transcription factor binding an enhancer initiates transcription, while a negative regulatory molecule binding DNA blocks it",
     "A transcription factor binding an enhancer blocks transcription, while a negative regulatory molecule binding DNA initiates it",
     "Both a transcription factor and a negative regulatory molecule block transcription",
     "Both a transcription factor and a negative regulatory molecule initiate transcription",
     "Neither event affects transcription, since both molecules act after the transcript is made"], ans=0,
   why="EK 6.6.A.1 gives RNA polymerase and transcription factors the initiation of transcription at promoter or enhancer sequences, and EK 6.6.A.2 gives negative regulatory molecules the blocking of it. The two statements assign opposite directions, and both act at the DNA before a transcript exists."),
 dict(q="Which sequence of steps matches the framework's account of how regulation reaches the phenotype of a cell?",
   choices=[
     "Regulatory molecules act on a gene's DNA, transcription of that gene changes, the amount of its product changes, and the cell's function changes",
     "The cell's function changes, which changes the amount of a gene's product, which changes transcription of the gene",
     "The amount of a gene's product changes, which changes which genes the cell carries, which changes its function",
     "Transcription of every gene changes together, so no particular gene influences the cell's function",
     "The cell's function is set at fertilization, so regulation cannot change it"], ans=0,
   why="EK 6.6.A.1 and EK 6.6.A.2 put regulatory molecules on the gene's DNA affecting transcription, and EK 6.6.B.1 states that gene regulation results in differential gene expression and influences cell products and functions. The order runs from the DNA to the function, and EK 6.5.A.3.iii makes the amount of the product part of what sets the phenotype."),
 dict(q="Two constructs of one gene are compared: in the first, a regulatory sequence lies 300 nucleotides upstream of the transcription start site; in the second, the same sequence lies 300 nucleotides downstream. Transcription is high in both. What does this show?",
   choices=[
     "The sequence can act from either side of the transcription start site, which is what the framework allows",
     "The sequence must have been duplicated, since one sequence cannot act from two positions",
     "The sequence is not a regulatory sequence, since a regulatory sequence must lie upstream",
     "The two constructs must contain different genes, since one sequence cannot give the same result twice",
     "The sequence acts on the mRNA rather than on the DNA, which is why its position does not matter"], ans=0,
   why="EK 6.6.A.1 states that promoter or enhancer sequences can be upstream or downstream of the transcription start site, so a sequence working from both positions is exactly what the framework describes. The sequence is DNA rather than part of the transcript."),
 dict(q="An investigator wants to support the claim that differential gene expression accounts for the difference between two cell types. Which evidence would be most direct?",
   choices=[
     "Measurements showing that particular genes are expressed at very different levels in the two cell types that share a genome",
     "Measurements showing that the two cell types contain the same number of chromosomes",
     "Measurements showing that both cell types use the same genetic code",
     "Measurements showing that the two cell types are the same size",
     "Measurements showing that the two cell types both contain ribosomes"], ans=0,
   why="Skill 6.B asks for a claim supported by evidence, and EK 6.6.B.1 states that gene regulation results in differential gene expression and influences cell products and functions. The evidence therefore has to be a difference in expression between cells that share a genome; a shared chromosome number, code, size or organelle is common ground rather than a difference."),
 dict(q="A gene is found to be transcribed only in cells that contain a particular protein, and that protein is found bound to a DNA sequence next to the gene. Which claim is best supported, and by which framework statement?",
   choices=[
     "The protein is a transcription factor acting at a promoter or enhancer, since such molecules bind those sequences to initiate transcription",
     "The protein is a negative regulatory molecule, since such molecules bind DNA",
     "The protein is a small RNA molecule, since such molecules regulate gene expression",
     "The protein is the product of the gene, since the two are found together",
     "The protein is ribosomal RNA, since it is bound near the site where transcription begins"], ans=0,
   why="EK 6.6.A.1 states that RNA polymerase and transcription factors bind to promoter or enhancer DNA sequences to initiate transcription, and both observations fit: the protein binds a DNA sequence beside the gene and transcription occurs where the protein is present. A negative regulatory molecule under EK 6.6.A.2 would be associated with transcription being blocked, and a protein is not an RNA molecule."),
 dict(q="Why does the framework describe gene regulation as influencing cell products and functions rather than as changing which genes a cell has?",
   choices=[
     "Regulation determines which of the cell's genes are expressed, and the products of expression are what the cell uses",
     "Regulation removes the genes the cell does not need, which is why its products differ",
     "Regulation adds genes from neighboring cells, which is why its products differ",
     "Regulation changes the base sequence of the cell's genes, which is why its products differ",
     "Regulation has no effect on products, since every cell makes the same set of proteins"], ans=0,
   why="EK 6.6.B.1 states that gene regulation results in differential gene expression and influences cell products and functions, which places the effect on expression rather than on the genes themselves. A change in a base sequence is the mutation of EK 6.7.A.1, a different phenomenon."),
 dict(q="Which statement is consistent with everything the framework states in this topic?",
   choices=[
     "Molecules bind promoter or enhancer sequences on either side of the start site to initiate transcription, other molecules bind DNA to block it, certain small RNA molecules regulate expression, and the resulting differential expression influences cell products and functions",
     "Molecules bind promoter sequences upstream only to initiate transcription, no molecule can block transcription, and small RNA molecules have no regulatory role",
     "Molecules bind the mRNA rather than the DNA, and differential expression follows from differences in the genes each cell carries",
     "Regulation acts only after a protein has been made, so transcription is the same in every cell",
     "Regulation acts only in prokaryotes, since eukaryotic cells express every gene they carry"], ans=0,
   why="Each clause of the keyed option is one of the framework's own: EK 6.6.A.1 for the binding molecules and the two possible positions, EK 6.6.A.2 for negative regulatory molecules, EK 6.6.B.2 for small RNA molecules, and EK 6.6.B.1 for differential expression influencing cell products and functions. Every other option contradicts at least one of the four."),
]
