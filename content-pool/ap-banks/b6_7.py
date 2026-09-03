# AP BIOLOGY 6.7 Mutations
# CED effective Fall 2025, Unit 6 Gene Expression and Regulation. Big idea 3
# (Information Storage and Transmission). Learning objectives 6.7.A, describe the
# various types of mutation; 6.7.B, explain how changes in genotype may result in
# changes in phenotype; 6.7.C, explain how alterations in DNA sequences
# contribute to variation that can be subject to natural selection. Suggested
# skill 2.C, explain how biological models relate to larger principles,
# concepts, processes, systems, or theories.
#
# Essential knowledge relied on, in the framework's own words:
#   6.7.A.1     Alterations in a DNA sequence are mutations that can cause
#               changes in the TYPE OR AMOUNT of the protein produced and the
#               consequent phenotype. DNA mutations can be beneficial,
#               detrimental, or neutral based on the effect or the lack of
#               effect they have on the resulting nucleic acid or protein and
#               the phenotypes that are conferred by the protein.
#   6.7.A.1.i   POINT mutations occur when one nucleotide has been substituted
#               for a different nucleotide.
#   6.7.A.1.ii  FRAMESHIFT mutations occur when one or more nucleotides are
#               inserted or deleted, causing the reading frame to be shifted.
#   6.7.A.1.iii NONSENSE mutations occur when there is a point mutation that
#               causes a PREMATURE STOP.
#   6.7.A.1.iv  SILENT mutations occur when the change in the nucleotide
#               sequence has no effect on the amino acid sequence.
#   6.7.B.1     Errors in DNA replication or DNA repair mechanisms as well as
#               external factors, including RADIATION and REACTIVE CHEMICALS,
#               can cause RANDOM mutations in the DNA.
#   6.7.B.1.i   Whether a mutation is beneficial, detrimental, or neutral
#               depends on the ENVIRONMENTAL CONTEXT.
#   6.7.B.1.ii  Mutations are a source of genetic variation.
#   6.7.B.2     Errors in mitosis or meiosis can result in changes in phenotype.
#   6.7.B.2.i   Changes in chromosome number resulting from NONDISJUNCTION often
#               result in new phenotypes.
#   6.7.B.2.ii  Changes in chromosome number often result in disorders with
#               developmental limitations.
#   6.7.B.2.iii Alterations in chromosome STRUCTURE lead to genetic disorders.
#   6.7.C.1     Changes in genotype may affect phenotypes that are subject to
#               natural selection. Genetic changes that enhance survival and
#               reproduction can be selected for by environmental conditions.
#   6.7.C.1.i   The horizontal acquisitions of genetic information in prokaryotes
#               via TRANSFORMATION (uptake of DNA), TRANSDUCTION (viral
#               transmission of genetic information), CONJUGATION (cell-to-cell
#               transfer of DNA), and TRANSPOSITION (movement of DNA segments
#               within and between DNA molecules) increase genetic variation.
#   6.7.C.1.ii  Related viruses can recombine genetic information if they infect
#               the same host cell.
#   6.7.C.1.iii Reproductive processes that increase genetic variation are
#               evolutionarily conserved and are shared by various organisms.
#
# TWO EXCLUSION STATEMENTS GOVERN THIS TOPIC and they are the reason several
# obvious questions are not here:
#   - printed with EK 6.7.A.1: "Knowledge of specific mutations and their effects
#     is beyond the scope of the AP Exam."
#   - printed with EK 6.7.B.2: "Knowledge of specific disorders related to
#     changes in chromosome number is beyond the scope of the AP Exam."
# The CED does print illustrative examples beside these statements -- the CFTR
# gene, the MC1R gene in pocket mice, sickle cell anemia -- but an illustrative
# example is a teaching suggestion and the exclusion statement is a limit on what
# may be examined. NO item here names a gene, a disease or a chromosome disorder,
# and verify_b6_7.py scans the whole module and fails if one appears.
#
# ON EK 6.7.B.2.i. The CED's printed text for this statement reads "new
# phenotypes caused by triploidy (aneuploidy)", which conflates two terms that
# are not synonyms. Nothing here is keyed to the difference between them; the
# items rest on the part of the statement that is unambiguous, that nondisjunction
# changes chromosome number and that this often results in new phenotypes.
#
# ON FIGURES. No stem refers to a karyotype, a gel or a chromosome diagram.
# Sequences are written out and every data set is a table=.
#
# DIVISION WITH 6.4: a premature stop is asked there as what the RIBOSOME does on
# reaching one, and here as what KIND of mutation produced it. DIVISION WITH 6.5:
# epigenetic modification is 6.5's and is reversible; a mutation is an alteration
# of the sequence and is not asked there.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX.
TOPIC = ("6.7", "Mutations", 6)

# A partial genetic code chart, supplied as stimulus for the mutation items.
_T_CODE = dict(
    headers=["mRNA codon", "Amino acid encoded"],
    rows=[["AUG", "Methionine"],
          ["CGU", "Arginine"],
          ["CGC", "Arginine"],
          ["UGU", "Cysteine"],
          ["AAA", "Lysine"],
          ["GAG", "Glutamate"],
          ["UAG", "Stop"],
          ["UAA", "Stop"]])

# The four products of one meiosis, counted.
_T_NONDIS = dict(
    headers=["Cell or gamete", "Number of chromosomes counted"],
    rows=[["The parent cell before meiosis", "46"],
          ["Gamete 1", "24"],
          ["Gamete 2", "22"],
          ["Gamete 3", "23"],
          ["Gamete 4", "23"]])

# Four mutations described by what changed and what followed.
_T_MUT = dict(
    headers=["Mutation", "Change to the DNA sequence",
             "Effect on the amino acid sequence of the protein"],
    rows=[["Mutation 1", "One nucleotide substituted for a different nucleotide",
           "One amino acid differs from the usual one"],
          ["Mutation 2", "One nucleotide substituted for a different nucleotide",
           "No amino acid differs from the usual sequence"],
          ["Mutation 3", "One nucleotide substituted for a different nucleotide",
           "A stop appears earlier than usual, where an amino acid had been"],
          ["Mutation 4", "One nucleotide deleted from the sequence",
           "Every amino acid after the site of the change differs"]])

QUESTIONS = [
 dict(q="What is a mutation, and what can it change?",
   choices=[
     "An alteration in a DNA sequence, which can change the type or amount of the protein produced and the phenotype that follows",
     "An alteration in an amino acid sequence, which can change the DNA sequence that produced it",
     "A reversible modification of DNA or histones, which can change how strongly a gene is expressed",
     "A change in the environment of a cell, which can change which of its genes are expressed",
     "A change in the genetic code, which can change which amino acid each codon specifies"], ans=0,
   why="EK 6.7.A.1 states that alterations in a DNA sequence are mutations that can cause changes in the type or amount of the protein produced and the consequent phenotype. A reversible modification of DNA or histones is the epigenetic change of EK 6.5.A.2, and the genetic code is shared across nearly all organisms under EK 6.4.A.3.iv."),
 dict(q="On what does the framework say the classification of a mutation as beneficial, detrimental or neutral rest?",
   choices=[
     "The effect, or the lack of effect, the mutation has on the resulting nucleic acid or protein and the phenotypes that protein confers",
     "The number of nucleotides that were changed, with larger changes always being detrimental",
     "Whether the mutation occurred during replication or was caused by an external factor",
     "Whether the mutation lies near the start or the end of the gene",
     "Whether the organism carrying it is a prokaryote or a eukaryote"], ans=0,
   why="EK 6.7.A.1 states that DNA mutations can be beneficial, detrimental, or neutral based on the effect or the lack of effect they have on the resulting nucleic acid or protein and the phenotypes that are conferred by the protein. The classification therefore turns on consequences rather than on the size, cause or position of the change."),
 dict(q="What is a point mutation?",
   choices=[
     "A mutation in which one nucleotide has been substituted for a different nucleotide",
     "A mutation in which one nucleotide has been inserted into the sequence",
     "A mutation in which one nucleotide has been deleted from the sequence",
     "A mutation in which an entire chromosome has been gained or lost",
     "A mutation in which the amino acid sequence changes without any change to the DNA"], ans=0,
   why="EK 6.7.A.1.i states that point mutations occur when one nucleotide has been substituted for a different nucleotide. Insertions and deletions are what EK 6.7.A.1.ii calls frameshift mutations, and a change in chromosome number belongs to EK 6.7.B.2.i."),
 dict(q="What is a frameshift mutation, and what causes the shift?",
   choices=[
     "A mutation in which one or more nucleotides are inserted or deleted, which shifts the reading frame",
     "A mutation in which one nucleotide is substituted for another, which shifts the reading frame",
     "A mutation in which the ribosome begins reading at the wrong codon without any change to the DNA",
     "A mutation in which a whole chromosome is duplicated, which shifts the reading frame",
     "A mutation in which the poly-A tail is removed, which shifts the reading frame"], ans=0,
   why="EK 6.7.A.1.ii states that frameshift mutations occur when one or more nucleotides are inserted or deleted, causing the reading frame to be shifted. A substitution leaves the number of nucleotides unchanged and so leaves the triplet boundaries of EK 6.4.A.3.ii where they were."),
 dict(q="What is a nonsense mutation?",
   choices=[
     "A point mutation that causes a premature stop",
     "A deletion that causes a premature stop",
     "A point mutation that has no effect on the amino acid sequence",
     "An insertion that adds an extra amino acid to the protein",
     "A mutation that changes the genetic code so that a codon means something new"], ans=0,
   why="EK 6.7.A.1.iii states that nonsense mutations occur when there is a point mutation that causes a premature stop, so the framework specifies both the kind of change and its consequence. A point mutation with no effect on the amino acid sequence is the silent mutation of EK 6.7.A.1.iv."),
 dict(q="What is a silent mutation?",
   choices=[
     "A change in the nucleotide sequence that has no effect on the amino acid sequence",
     "A change in the amino acid sequence that has no effect on the nucleotide sequence",
     "A change in the nucleotide sequence that causes a premature stop",
     "A change in the nucleotide sequence that shifts the reading frame",
     "A change that is never inherited by the next generation"], ans=0,
   why="EK 6.7.A.1.iv states that silent mutations occur when the change in the nucleotide sequence has no effect on the amino acid sequence. That such a change is possible follows from EK 6.4.A.3.iii, which states that many amino acids are encoded by more than one codon."),
 dict(q="Using the chart in the table, a coding sequence reads AUGCGUAAAUAG before a change and AUGUGUAAAUAG after it. How should this change be classified?",
   table=_T_CODE,
   choices=[
     "A point mutation, because one nucleotide has been substituted for a different nucleotide",
     "A frameshift mutation, because the reading frame after the change is shifted",
     "A silent mutation, because the amino acid sequence is unaffected",
     "A nonsense mutation, because a premature stop has been introduced",
     "Not a mutation, because the sequence is still the same length"], ans=0,
   why="EK 6.7.A.1.i defines a point mutation as one nucleotide substituted for a different nucleotide, which is what has happened here: the second triplet changes from CGU to UGU, one nucleotide of difference. The chart makes that a change from arginine to cysteine, so the amino acid sequence does change, which rules out the silent classification, and no stop appears early."),
 dict(q="Using the same chart, a coding sequence reads AUGCGUAAAUAG before a change and AUGCGCAAAUAG after it. How should this change be classified?",
   table=_T_CODE,
   choices=[
     "A silent mutation, because the change in the nucleotide sequence has no effect on the amino acid sequence",
     "A point mutation that changes one amino acid, because one nucleotide has been substituted",
     "A nonsense mutation, because a premature stop has been introduced",
     "A frameshift mutation, because the number of nucleotides has changed",
     "Not a mutation, because the amino acid sequence is unchanged"], ans=0,
   why="EK 6.7.A.1.iv defines a silent mutation as a change in the nucleotide sequence with no effect on the amino acid sequence. The chart assigns both the original and the altered second triplet to arginine, so the protein is unchanged. EK 6.7.A.1 makes any alteration in a DNA sequence a mutation, so a change without effect is still one."),
 dict(q="Using the same chart, a coding sequence reads AUGGAGAAAUAA before a change and AUGUAGAAAUAA after it. How should this change be classified?",
   table=_T_CODE,
   choices=[
     "A nonsense mutation, because a point mutation has introduced a premature stop",
     "A silent mutation, because the change occurs in only one nucleotide",
     "A frameshift mutation, because the codons after the change are read differently",
     "A point mutation with no effect on the protein, because the sequence is the same length",
     "Not a mutation, because the original sequence already ended in a stop codon"], ans=0,
   why="EK 6.7.A.1.iii defines a nonsense mutation as a point mutation causing a premature stop. One nucleotide of the second triplet has been substituted, and the chart assigns the new triplet a stop where it previously assigned glutamate, so translation would end there under EK 6.4.A.3.vii rather than at the original ending."),
 dict(q="A coding sequence reads AUGCGUAAAUGUUAA before a change and AUGGUAAAUGUUAA after it. How should this change be classified, and why does it usually affect more of the protein than a substitution would?",
   choices=[
     "A frameshift mutation, because a nucleotide has been deleted and every triplet after the site is read differently",
     "A point mutation, because only one nucleotide is involved in the change",
     "A silent mutation, because the first triplet is unchanged",
     "A nonsense mutation, because the sequence still ends in a stop codon",
     "A change in chromosome structure, because the length of the molecule has changed"], ans=0,
   why="EK 6.7.A.1.ii states that frameshift mutations occur when one or more nucleotides are inserted or deleted, causing the reading frame to be shifted. Removing one nucleotide moves every following triplet boundary, and EK 6.4.A.3.ii has the message read in triplets from that point on, so all the codons downstream of the site are different rather than just one."),
 dict(q="What does the framework name as causes of random mutations in DNA?",
   choices=[
     "Errors in DNA replication or DNA repair mechanisms, and external factors including radiation and reactive chemicals",
     "Only errors in DNA replication, since external factors cannot reach the DNA",
     "Only external factors such as radiation, since replication is always accurate",
     "The need of the organism for a new trait, which directs where mutations occur",
     "The presence of a transcription factor at the gene's promoter"], ans=0,
   why="EK 6.7.B.1 states that errors in DNA replication or DNA repair mechanisms as well as external factors, including radiation and reactive chemicals, can cause random mutations in the DNA. Both internal and external causes are named, and the word random rules out an account in which an organism's needs decide where mutations fall."),
 dict(q="A population of bacteria is exposed to an antibiotic and some cells survive because they already carried a mutation conferring resistance. Which statement about the mutation is consistent with the framework?",
   choices=[
     "The mutation arose at random, and the antibiotic then selected the cells that happened to carry it",
     "The antibiotic caused the mutation to arise in the cells that needed it",
     "The mutation arose because the cells detected the antibiotic and altered their DNA in response",
     "The mutation could not have existed before the antibiotic was applied, since it had no use",
     "The mutation was inherited from the antibiotic itself during exposure"], ans=0,
   why="EK 6.7.B.1 calls the mutations that arise from replication errors, repair errors and external factors random, and EK 6.7.C.1 states that genetic changes that enhance survival and reproduction can be selected for by environmental conditions. The randomness is in where the change occurs and the direction comes from the selecting condition afterward."),
 dict(q="On what does the framework say it depends whether a mutation is beneficial, detrimental or neutral?",
   choices=[
     "The environmental context in which the organism carrying it lives",
     "The chromosome on which the mutation is located",
     "Whether the mutation was inherited or arose during the organism's own lifetime",
     "The number of offspring the organism has already produced",
     "Whether the organism is a prokaryote or a eukaryote"], ans=0,
   why="EK 6.7.B.1.i states that whether a mutation is beneficial, detrimental, or neutral depends on the environmental context. A change that helps under one set of conditions can be useless or harmful under another, which is why the framework does not attach the label to the change itself."),
 dict(q="Why does the framework describe mutations as a source of genetic variation?",
   choices=[
     "A mutation introduces a version of a sequence that was not previously present in the population",
     "A mutation removes existing versions of a sequence from the population",
     "A mutation causes every individual in a population to acquire the same change",
     "A mutation rearranges the amino acids of a protein without changing its gene",
     "A mutation makes an organism's offspring identical to one another"], ans=0,
   why="EK 6.7.B.1.ii states that mutations are a source of genetic variation, and EK 6.7.A.1 makes a mutation an alteration in a DNA sequence. An alteration produces a sequence version that was not there before, which is what adding to the variation of a population means."),
 dict(q="What does the framework say can result from errors in mitosis or meiosis?",
   choices=[
     "Changes in phenotype",
     "Changes in the genetic code the cell uses",
     "Reversible modifications of the histones",
     "The addition of a poly-A tail to the chromosome",
     "The loss of the ability to transcribe any gene"], ans=0,
   why="EK 6.7.B.2 states that errors in mitosis or meiosis can result in changes in phenotype, and EK 6.7.B.2.i and iii identify changes in chromosome number and alterations in chromosome structure as the routes. Reversible histone modification is the epigenetic change of EK 6.5.A.2, a different phenomenon."),
 dict(q="What does nondisjunction produce, according to the framework?",
   choices=[
     "Changes in chromosome number, which often result in new phenotypes",
     "Changes in the nucleotide sequence of a single gene, which often result in new phenotypes",
     "Reversible modifications of DNA that switch genes off",
     "A shift in the reading frame of every gene on the affected chromosome",
     "The exchange of genetic information between two unrelated species"], ans=0,
   why="EK 6.7.B.2.i states that changes in chromosome number resulting from nondisjunction often result in new phenotypes. The change is at the level of whole chromosomes rather than of a nucleotide sequence, which is what EK 6.7.A.1 covers."),
 dict(q="The table reports chromosome counts for one parent cell and the four gametes produced from it. Which gametes carry a chromosome number that nondisjunction would explain?",
   table=_T_NONDIS,
   choices=[
     "The gametes counted at 24 and at 22, one having gained a chromosome and the other lost one",
     "The two gametes counted at 23, since that number differs from the parent cell's count",
     "All four gametes, since every gamete has fewer chromosomes than the parent cell",
     "None of them, since the four gamete counts add up to twice the parent cell's count",
     "The parent cell itself, since it has the largest count in the table"], ans=0,
   why="A meiosis of a cell with 46 chromosomes gives gametes of 23. EK 6.7.B.2.i attributes changes in chromosome number to nondisjunction, and two of the four gametes here depart from 23, one upward by one and one downward by one; the other two are the expected number. The four gamete counts do sum to 92, which is consistent with one chromosome having gone to the wrong cell rather than with anything being lost."),
 dict(q="If the gamete counted at 24 chromosomes in the table is fertilized by a gamete carrying the expected number, how many chromosomes will the zygote have?",
   table=_T_NONDIS,
   choices=[
     "47 chromosomes",
     "46 chromosomes",
     "48 chromosomes",
     "24 chromosomes",
     "23 chromosomes"], ans=0,
   why="EK 5.3.A.2 makes fertilization the fusion of two haploid gametes, so the zygote's count is the sum of the two gametes' counts. The expected gamete number for a parent cell of 46 is 23, and 24 added to 23 is 47, which is a change in chromosome number of the kind EK 6.7.B.2.i attributes to nondisjunction."),
 dict(q="What does the framework say about alterations in chromosome structure, as distinct from changes in chromosome number?",
   choices=[
     "They lead to genetic disorders",
     "They have no effect, since the same genes are still present",
     "They are reversible and so do not affect the phenotype",
     "They change the genetic code used to read the affected genes",
     "They occur only in prokaryotes, which have a single chromosome"], ans=0,
   why="EK 6.7.B.2.iii states that alterations in chromosome structure lead to genetic disorders, which the framework lists alongside the changes in chromosome number of EK 6.7.B.2.i and ii as a route from an error in cell division to a change in phenotype."),
 dict(q="What does the framework state about changes in chromosome number and development?",
   choices=[
     "Changes in chromosome number often result in disorders with developmental limitations",
     "Changes in chromosome number are always neutral, because no gene sequence is altered",
     "Changes in chromosome number affect only the cell in which they occur",
     "Changes in chromosome number can be reversed by DNA repair mechanisms",
     "Changes in chromosome number occur only during mitosis and never during meiosis"], ans=0,
   why="EK 6.7.B.2.ii states that changes in chromosome number often result in disorders with developmental limitations, and EK 6.7.B.2 attributes the errors to mitosis or meiosis rather than to one of them alone."),
 dict(q="The table describes four mutations by the change made and the effect that followed. Which is a silent mutation?",
   table=_T_MUT,
   choices=[
     "The mutation in which a substitution leaves the amino acid sequence unchanged",
     "The mutation in which a substitution changes one amino acid",
     "The mutation in which a substitution introduces an early stop",
     "The mutation in which a deletion changes every amino acid after the site",
     "None of them, because every change to DNA changes the protein"], ans=0,
   why="EK 6.7.A.1.iv defines a silent mutation as a change in the nucleotide sequence that has no effect on the amino acid sequence, and exactly one row of the table records a substitution with no change to the protein. That such a row is possible follows from EK 6.4.A.3.iii, which states that many amino acids are encoded by more than one codon."),
 dict(q="Using the same four mutations, which is a frameshift mutation?",
   table=_T_MUT,
   choices=[
     "The mutation in which a nucleotide is deleted and every amino acid after the site differs",
     "The mutation in which a substitution changes one amino acid",
     "The mutation in which a substitution introduces an early stop",
     "The mutation in which a substitution leaves the amino acid sequence unchanged",
     "All four of them, since each one changes the DNA sequence"], ans=0,
   why="EK 6.7.A.1.ii states that frameshift mutations occur when one or more nucleotides are inserted or deleted, causing the reading frame to be shifted. Only one row records a deletion, and the effect recorded beside it, every amino acid after the site differing, is what a shifted reading frame produces under EK 6.4.A.3.ii. The other three are substitutions, which are point mutations under EK 6.7.A.1.i."),
 dict(q="What connection does the framework draw between changes in genotype and natural selection?",
   choices=[
     "Changes in genotype may affect phenotypes that are subject to natural selection, and changes that enhance survival and reproduction can be selected for by environmental conditions",
     "Changes in genotype are produced by natural selection in the individuals that need them",
     "Changes in genotype are always neutral, so natural selection cannot act on them",
     "Natural selection acts on genotypes directly, without any phenotype being involved",
     "Natural selection removes every mutation from a population within one generation"], ans=0,
   why="EK 6.7.C.1 states that changes in genotype may affect phenotypes that are subject to natural selection and that genetic changes enhancing survival and reproduction can be selected for by environmental conditions. The mutations themselves are random under EK 6.7.B.1, so selection follows the change rather than producing it."),
 dict(q="A bacterial cell takes up a piece of DNA from its surroundings. Which of the horizontal acquisitions of genetic information named by the framework is this?",
   choices=[
     "Transformation, the uptake of DNA",
     "Transduction, the viral transmission of genetic information",
     "Conjugation, the transfer of DNA from one cell to another cell",
     "Transposition, the movement of DNA segments within and between DNA molecules",
     "Nondisjunction, the failure of chromosomes to separate"], ans=0,
   why="EK 6.7.C.1.i names four horizontal acquisitions and defines each: transformation is the uptake of DNA, transduction is viral transmission, conjugation is cell-to-cell transfer, and transposition is the movement of DNA segments within and between DNA molecules. Taking DNA up from the surroundings is the first of these."),
 dict(q="A virus carries genetic information from one bacterial cell into another. Which of the horizontal acquisitions named by the framework is this?",
   choices=[
     "Transduction, the viral transmission of genetic information",
     "Transformation, the uptake of DNA from the surroundings",
     "Conjugation, the transfer of DNA directly from one cell to another",
     "Transposition, the movement of DNA segments within and between DNA molecules",
     "Alternative splicing, the retention of different combinations of exons"], ans=0,
   why="EK 6.7.C.1.i defines transduction as the viral transmission of genetic information, which is what a virus carrying DNA between cells performs. Alternative splicing is a processing step under EK 6.3.A.4.iii and has nothing to do with the transfer of information between cells."),
 dict(q="Two bacterial cells come into contact and DNA passes directly from one to the other. Which of the horizontal acquisitions named by the framework is this?",
   choices=[
     "Conjugation, the transfer of DNA from one cell to another cell",
     "Transformation, the uptake of DNA from the surroundings",
     "Transduction, the transmission of genetic information by a virus",
     "Transposition, the movement of DNA segments within and between DNA molecules",
     "Fertilization, the fusion of two haploid gametes"], ans=0,
   why="EK 6.7.C.1.i defines conjugation as cell-to-cell transfer of DNA, which is the direct passage described. Fertilization is the fusion of two haploid gametes under EK 5.3.A.2 and is not one of the horizontal acquisitions in prokaryotes."),
 dict(q="A segment of DNA moves from one position to another within a bacterial genome. Which of the horizontal acquisitions named by the framework is this, and what does the framework say all four of them do?",
   choices=[
     "Transposition, and all four increase genetic variation",
     "Transformation, and all four decrease genetic variation",
     "Conjugation, and all four leave genetic variation unchanged",
     "Transduction, and all four increase the number of chromosomes",
     "Nondisjunction, and all four increase genetic variation"], ans=0,
   why="EK 6.7.C.1.i defines transposition as the movement of DNA segments within and between DNA molecules, and states that the four named acquisitions increase genetic variation. Nondisjunction belongs to EK 6.7.B.2.i and is a failure of chromosome separation rather than an acquisition of genetic information."),
 dict(q="What does the framework say can happen when two related viruses infect the same host cell?",
   choices=[
     "They can recombine genetic information",
     "They can exchange the proteins they have already made but not their genetic information",
     "They can convert the host cell's DNA into RNA",
     "They can each acquire a nucleus from the host cell",
     "They cannot interact, because a cell can be infected by only one virus"], ans=0,
   why="EK 6.7.C.1.ii states that related viruses can recombine genetic information if they infect the same host cell, which the framework lists among the processes that increase genetic variation."),
 dict(q="What does the framework say about reproductive processes that increase genetic variation?",
   choices=[
     "They are evolutionarily conserved and are shared by various organisms",
     "They arose independently in each lineage and are shared by no two groups",
     "They occur only in prokaryotes, which lack meiosis",
     "They occur only in eukaryotes, which alone reproduce sexually",
     "They reduce the variation available to natural selection"], ans=0,
   why="EK 6.7.C.1.iii states that reproductive processes that increase genetic variation are evolutionarily conserved and are shared by various organisms. Being shared across groups is what conserved means, and it is the opposite of arising separately in each lineage."),
 dict(q="A mutation appears in a population and has no effect on survival under the conditions the population currently experiences. Those conditions later change, and the mutation now improves survival and reproduction. Which two framework statements together account for this?",
   choices=[
     "That whether a mutation is beneficial, detrimental or neutral depends on the environmental context, and that genetic changes enhancing survival and reproduction can be selected for by environmental conditions",
     "That mutations are always detrimental, and that natural selection removes them",
     "That mutations are directed by the needs of the organism, and that the environment supplies those needs",
     "That mutations arise only from external factors, and that the environment therefore decides which arise",
     "That mutations are reversible modifications, and that the environment reverses them when they are not needed"], ans=0,
   why="EK 6.7.B.1.i states that whether a mutation is beneficial, detrimental, or neutral depends on the environmental context, and EK 6.7.C.1 states that genetic changes that enhance survival and reproduction can be selected for by environmental conditions. Together they allow one unchanged sequence to be neutral under one set of conditions and favoured under another; EK 6.7.B.1 also names internal errors among the causes and calls the mutations random."),
]
