# AP BIOLOGY 6.1 DNA and RNA Structure
# CED effective Fall 2025, Unit 6 Gene Expression and Regulation. Big idea 3
# (Information Storage and Transmission). Learning objectives 6.1.A, describe
# the structures involved in passing hereditary information from one generation
# to the next, and 6.1.B, describe the characteristics of DNA that allow it to
# be used as hereditary material. Suggested skill 1.C, explain biological
# concepts and processes in applied contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   6.1.A.1     Genetic information is stored in and passed to subsequent
#               generations through DNA molecules and, IN SOME CASES, RNA
#               molecules.
#   6.1.A.1.i   Prokaryotic organisms typically have circular chromosomes.
#   6.1.A.1.ii  Eukaryotic organisms typically have multiple linear chromosomes
#               that are comprised of DNA. These chromosomes are condensed using
#               histones and associated proteins.
#   6.1.A.2     Prokaryotes AND eukaryotes can contain plasmids, which are
#               extra-chromosomal circular molecules of DNA.
#   6.1.B.1     Nucleic acids exhibit specific nucleotide base pairing that is
#               CONSERVED THROUGH EVOLUTION.
#   6.1.B.1.i   Purines (guanine and adenine) have a double ring structure.
#   6.1.B.1.ii  Pyrimidines (cytosine, thymine, and uracil) have a single ring
#               structure.
#   6.1.B.1.iii Purines pair with pyrimidines: adenine with thymine (or uracil
#               in RNA) and guanine with cytosine.
#
# DIVISION OF LABOUR ACROSS 6.1 TO 6.4, planned together because they are one
# continuous story and would otherwise collide:
#   6.1  what the molecule IS -- where genetic information is stored, chromosome
#        shape and number, histones, plasmids, the two ring classes, which base
#        pairs with which, and the arithmetic that follows from that pairing.
#        Directionality, enzymes and any synthesis step are NOT asked here.
#   6.2  copying DNA -- semiconservative replication, the 5 prime to 3 prime
#        direction of synthesis, the five named enzymes, primers, leading and
#        lagging strands.
#   6.3  DNA to RNA -- the three RNA types and their functions, RNA polymerase
#        reading a single template strand, the direction it reads and writes,
#        and the three eukaryotic modifications.
#   6.4  RNA to protein -- ribosomes, coupled transcription in prokaryotes, the
#        start codon, triplet reading, the genetic code and its universality,
#        tRNA delivery, elongation, stop codons, and reverse transcriptase.
# Base pairing is stated in 6.1 and USED in 6.2, 6.3 and 6.4; no item in those
# topics asks which base pairs with which, and no item here asks what an enzyme
# does with the pairing.
#
# ON FIGURES. No stem refers to a picture. Sequences are written out as text and
# every data set is in a table=.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX.
TOPIC = ("6.1", "DNA and RNA Structure", 6)

# Base composition of four samples, all as percentages of the total bases.
_T_CHARGAFF = dict(
    headers=["Sample", "Adenine (percent)", "Thymine (percent)",
             "Guanine (percent)", "Cytosine (percent)"],
    rows=[["Sample 1", "30", "30", "20", "20"],
          ["Sample 2", "31", "19", "19", "31"],
          ["Sample 3", "24", "24", "26", "26"],
          ["Sample 4", "35", "15", "30", "20"]])

# One double-stranded sample with two of the four percentages measured.
_T_CHARG2 = dict(
    headers=["Base", "Percent of the bases in the sample"],
    rows=[["Adenine", "22"],
          ["Thymine", "22"],
          ["Guanine", "not measured"],
          ["Cytosine", "not measured"]])

# Ring counts determined for five nitrogenous bases.
_T_RING = dict(
    headers=["Nitrogenous base", "Number of rings in the base structure"],
    rows=[["Adenine", "2"],
          ["Guanine", "2"],
          ["Cytosine", "1"],
          ["Thymine", "1"],
          ["Uracil", "1"]])

# Genome descriptions for four organisms.
_T_GENOMES = dict(
    headers=["Organism", "Number of chromosomes", "Chromosome shape",
             "Extra-chromosomal circular DNA molecules present"],
    rows=[["Organism W", "1", "Circular", "Yes"],
          ["Organism X", "8", "Linear", "No"],
          ["Organism Y", "46", "Linear", "No"],
          ["Organism Z", "1", "Circular", "No"]])

# Base composition of three nucleic acid samples, uracil included.
_T_RNA = dict(
    headers=["Sample", "Adenine (percent)", "Uracil (percent)",
             "Thymine (percent)", "Guanine (percent)", "Cytosine (percent)"],
    rows=[["Sample P", "30", "0", "30", "20", "20"],
          ["Sample Q", "28", "22", "0", "26", "24"],
          ["Sample R", "25", "0", "25", "25", "25"]])

QUESTIONS = [
 dict(q="A newly described single-celled organism is found to carry its genetic information on one closed loop of DNA with no free ends. This chromosome shape is typical of which group of organisms?",
   choices=[
     "Prokaryotic organisms, which typically have circular chromosomes",
     "Eukaryotic organisms, which typically have circular chromosomes",
     "Eukaryotic organisms, which typically have a single linear chromosome",
     "Organisms that store their genetic information in RNA rather than DNA",
     "Organisms that have lost their chromosomes and carry only plasmids"], ans=0,
   why="EK 6.1.A.1.i states that prokaryotic organisms typically have circular chromosomes, while EK 6.1.A.1.ii gives eukaryotes multiple linear chromosomes. A closed loop with no free ends is a circular molecule, which places the organism with the prokaryotes."),
 dict(q="Which description matches the chromosomes of a typical eukaryotic cell?",
   choices=[
     "Multiple linear chromosomes made of DNA and condensed using histones and associated proteins",
     "A single circular chromosome made of DNA and condensed using histones",
     "Multiple circular chromosomes made of RNA and condensed using histones",
     "A single linear chromosome made of DNA with no associated proteins",
     "Multiple linear chromosomes made of DNA with no condensation of any kind"], ans=0,
   why="EK 6.1.A.1.ii states that eukaryotic organisms typically have multiple linear chromosomes comprised of DNA, and that these chromosomes are condensed using histones and associated proteins. Each of the other descriptions changes one of those three features."),
 dict(q="What role do histones play in a eukaryotic cell?",
   choices=[
     "They are proteins that, with associated proteins, condense the cell's linear chromosomes",
     "They are the circular DNA molecules that sit outside the chromosomes",
     "They are the nucleotides from which the linear chromosomes are built",
     "They are the enzymes that join nucleotides together into a chromosome",
     "They are RNA molecules that store genetic information alongside the chromosomes"], ans=0,
   why="EK 6.1.A.1.ii states that eukaryotic linear chromosomes are condensed using histones and associated proteins. Histones are therefore proteins with a packaging role; the extra-chromosomal circular DNA molecules of EK 6.1.A.2 are plasmids, which is a different structure."),
 dict(q="A bacterial cell is found to contain, in addition to its chromosome, several small closed loops of DNA that are not part of that chromosome. What are these loops?",
   choices=[
     "Plasmids, which are extra-chromosomal circular molecules of DNA",
     "Histones, which are circular molecules that condense the chromosome",
     "Additional copies of the chromosome, since a prokaryotic chromosome is also circular",
     "RNA molecules, since only RNA is found outside a chromosome",
     "Fragments of the chromosome that were broken during the preparation of the sample"], ans=0,
   why="EK 6.1.A.2 states that prokaryotes and eukaryotes can contain plasmids, which are extra-chromosomal circular molecules of DNA. The description in the stem matches that definition term by term: circular, made of DNA, and outside the chromosome."),
 dict(q="A prokaryotic chromosome and a plasmid are both circular molecules of DNA in the same cell. What distinguishes them?",
   choices=[
     "The plasmid lies outside the chromosome, which is what the term extra-chromosomal records",
     "The plasmid is made of RNA while the chromosome is made of DNA",
     "The plasmid is linear while the chromosome is circular",
     "The plasmid is condensed with histones while the chromosome is not",
     "The plasmid is found only in eukaryotes while the chromosome is found only in prokaryotes"], ans=0,
   why="EK 6.1.A.2 defines a plasmid as an extra-chromosomal circular molecule of DNA, so the two structures share both the circular shape and the DNA composition and differ in being inside or outside the chromosome. The same statement gives plasmids to prokaryotes and eukaryotes alike."),
 dict(q="Which pair of nitrogenous bases is classified as the purines, and what structural feature defines that class?",
   choices=[
     "Guanine and adenine, which have a double ring structure",
     "Cytosine and thymine, which have a double ring structure",
     "Guanine and cytosine, which have a single ring structure",
     "Adenine and thymine, which have a single ring structure",
     "Thymine and uracil, which have a double ring structure"], ans=0,
   why="EK 6.1.B.1.i states that purines, guanine and adenine, have a double ring structure. EK 6.1.B.1.ii assigns cytosine, thymine and uracil to the pyrimidines with a single ring, so every other listed pairing mixes the two classes or reverses the ring counts."),
 dict(q="Which set of nitrogenous bases is classified as the pyrimidines?",
   choices=[
     "Cytosine, thymine and uracil",
     "Cytosine, guanine and adenine",
     "Adenine, thymine and uracil",
     "Guanine, adenine and uracil",
     "Cytosine, thymine and guanine"], ans=0,
   why="EK 6.1.B.1.ii names cytosine, thymine and uracil as the pyrimidines and states that they have a single ring structure. EK 6.1.B.1.i assigns guanine and adenine to the purines instead, so every other listed set imports at least one purine."),
 dict(q="The strand adenine, guanine, adenine, cytosine, adenine is paired twice: once with a partner strand of DNA and once with a partner strand of RNA. At how many of the five positions do the two partner strands differ from each other, and why?",
   choices=[
     "Three, because only adenine takes a different partner in the two cases",
     "Five, because every base takes a different partner in the two cases",
     "Two, because only guanine and cytosine take different partners in the two cases",
     "One, because only the first position differs between the two cases",
     "None, because the same partner strand is produced in both cases"], ans=0,
   why="EK 6.1.B.1.iii gives guanine and cytosine one partner each in both nucleic acids, and gives adenine thymine or uracil in RNA. The three adenines in this strand therefore take thymine in the DNA partner and uracil in the RNA partner, while the guanine and the cytosine take the same partners in both, so the two partner strands differ at exactly three positions."),
 dict(q="A segment of one DNA strand reads, in order, guanine, guanine, cytosine, adenine, guanine. What is the corresponding sequence of the complementary DNA strand, read against those bases in the same order?",
   choices=[
     "Cytosine, cytosine, guanine, thymine, cytosine",
     "Cytosine, cytosine, guanine, uracil, cytosine",
     "Guanine, guanine, cytosine, adenine, guanine",
     "Thymine, thymine, adenine, cytosine, thymine",
     "Adenine, adenine, thymine, guanine, adenine"], ans=0,
   why="EK 6.1.B.1.iii pairs guanine with cytosine and adenine with thymine in DNA. Applying that base by base to guanine, guanine, cytosine, adenine, guanine gives cytosine, cytosine, guanine, thymine, cytosine. Uracil appears only in RNA, and copying the sequence unchanged would pair each base with itself, which the statement forbids."),
 dict(q="A segment of one DNA strand reads, in order, adenine, cytosine, adenine, thymine. An RNA strand base pairs with it. What is the corresponding RNA sequence, read against those bases in the same order?",
   choices=[
     "Uracil, guanine, uracil, adenine",
     "Thymine, guanine, thymine, adenine",
     "Adenine, cytosine, adenine, uracil",
     "Uracil, cytosine, uracil, adenine",
     "Adenine, guanine, adenine, thymine"], ans=0,
   why="EK 6.1.B.1.iii states that adenine pairs with thymine or with uracil in RNA, and that guanine pairs with cytosine. Adenine on the DNA strand therefore takes uracil in the RNA, cytosine takes guanine, and thymine takes adenine; a partner strand that is RNA carries uracil rather than thymine."),
 dict(q="Why can adenine not pair with guanine in a nucleic acid, according to the framework's own rule?",
   choices=[
     "Both are purines, and the rule pairs each purine with a pyrimidine",
     "Both are pyrimidines, and the rule pairs each pyrimidine with a purine",
     "Adenine is a purine and guanine a pyrimidine, and like classes cannot pair",
     "Adenine is found only in DNA and guanine only in RNA, so they never meet",
     "Guanine has a single ring and adenine a double ring, so they are the same size"], ans=0,
   why="EK 6.1.B.1.i places guanine and adenine together among the purines with a double ring structure, and EK 6.1.B.1.iii states that purines pair with pyrimidines. A pairing between two purines would join two double ring structures, which is not one of the pairs the framework allows."),
 dict(q="Base pairing rules are described in the framework as conserved through evolution. What does an investigator most reasonably expect as a result?",
   choices=[
     "The same base pairing rules apply in organisms as distantly related as a bacterium and a mammal",
     "The base pairing rules differ between prokaryotes and eukaryotes, since their chromosomes differ in shape",
     "The base pairing rules change gradually along a lineage, so distant relatives pair different bases",
     "The base pairing rules apply only to DNA, so RNA in any organism pairs bases at random",
     "The base pairing rules were fixed in eukaryotes and arose separately in each prokaryotic species"], ans=0,
   why="EK 6.1.B.1 states that nucleic acids exhibit specific nucleotide base pairing that is conserved through evolution. A conserved feature is one that has been retained across lineages, so the expectation is that distantly related organisms share it; EK 6.1.B.1.iii states the same rules for RNA as for DNA."),
 dict(q="The framework says that genetic information is stored in and passed to subsequent generations through DNA molecules and, in some cases, RNA molecules. Which observation is consistent with the second half of that statement?",
   choices=[
     "Some viruses carry their genome as RNA rather than as DNA",
     "Every organism uses RNA to carry information from the nucleus to the ribosome",
     "RNA contains uracil in place of the thymine found in DNA",
     "Ribosomes contain RNA as a functional building block",
     "RNA molecules are shorter than the chromosomes of most organisms"], ans=0,
   why="EK 6.1.A.1 says genetic information is stored in and passed to subsequent generations through DNA and, in some cases, RNA molecules. The clause concerns the molecule that holds an organism's heritable genome, which is what an RNA genome is; the other options describe roles RNA plays in a cell whose genome is DNA."),
 dict(q="The table reports the base composition of four nucleic acid samples as percentages of total bases. Which samples are consistent with being double-stranded DNA?",
   table=_T_CHARGAFF,
   choices=[
     "Samples 1 and 3, in which adenine equals thymine and guanine equals cytosine",
     "Samples 2 and 4, in which adenine equals thymine and guanine equals cytosine",
     "Samples 1 and 2, in which the four percentages sum to one hundred",
     "All four samples, since every sample contains all four bases",
     "None of the samples, since a double-stranded molecule must contain equal amounts of all four bases"], ans=0,
   why="EK 6.1.B.1.iii pairs adenine with thymine and guanine with cytosine, so in a double-stranded molecule every adenine has a thymine opposite it and every guanine a cytosine. Adenine equals thymine and guanine equals cytosine in the samples reading 30, 30, 20, 20 and 24, 24, 26, 26 and in neither of the others; all four samples sum to one hundred, which therefore separates nothing."),
 dict(q="Two of the four base percentages were measured in a sample of double-stranded DNA, as shown in the table. What percentage of the bases in this sample is cytosine?",
   table=_T_CHARG2,
   choices=[
     "28 percent",
     "22 percent",
     "56 percent",
     "50 percent",
     "It cannot be determined without measuring guanine as well"], ans=0,
   why="EK 6.1.B.1.iii pairs guanine with cytosine, so in a double-stranded molecule those two are present in equal amounts. Adenine and thymine together account for 44 percent of the bases, leaving 56 percent to be divided equally between guanine and cytosine, which gives 28 percent each; guanine need not be measured because the pairing rule fixes it."),
 dict(q="In any sample of double-stranded DNA, how does the total amount of purine compare with the total amount of pyrimidine?",
   choices=[
     "They are equal, because every base pair joins one purine to one pyrimidine",
     "Purine always exceeds pyrimidine, because purines have two rings",
     "Pyrimidine always exceeds purine, because three bases are pyrimidines and only two are purines",
     "The comparison varies from species to species with no general rule",
     "Purine is always exactly twice pyrimidine, matching the ratio of their ring counts"], ans=0,
   why="EK 6.1.B.1.iii states that purines pair with pyrimidines, so each base pair in a double-stranded molecule contributes exactly one of each class. Summing over every pair therefore gives equal totals whatever the species, and the number of ring structures or of named bases in each class does not enter the count."),
 dict(q="The table reports the number of rings determined for five nitrogenous bases. Which grouping of these bases do the data support?",
   table=_T_RING,
   choices=[
     "The two bases with a double ring are the purines and the three with a single ring are the pyrimidines",
     "The two bases with a double ring are the pyrimidines and the three with a single ring are the purines",
     "All five bases belong to one class, since all five are found in nucleic acids",
     "The bases found in DNA form one class and the base found only in RNA forms another",
     "The number of rings is unrelated to the classification of a base"], ans=0,
   why="EK 6.1.B.1.i states that the purines, guanine and adenine, have a double ring structure, and EK 6.1.B.1.ii states that the pyrimidines, cytosine, thymine and uracil, have a single ring structure. The two bases the table gives two rings are adenine and guanine, and the three it gives one ring are cytosine, thymine and uracil."),
 dict(q="The table describes the genomes of four organisms. Which organisms are most likely prokaryotic?",
   table=_T_GENOMES,
   choices=[
     "Organisms W and Z, each of which has a single circular chromosome",
     "Organisms X and Y, each of which has multiple linear chromosomes",
     "Organism W only, because it is the only organism carrying extra-chromosomal circular DNA",
     "All four organisms, since every organism stores genetic information in DNA",
     "None of the organisms, because chromosome shape is the same in prokaryotes and eukaryotes"], ans=0,
   why="EK 6.1.A.1.i states that prokaryotic organisms typically have circular chromosomes and EK 6.1.A.1.ii gives eukaryotes multiple linear chromosomes, so the two organisms recorded with one circular chromosome fit the prokaryotic description. Extra-chromosomal circular DNA cannot be the criterion, because EK 6.1.A.2 states that both prokaryotes and eukaryotes can contain plasmids."),
 dict(q="The table reports the base composition of three nucleic acid samples. Which sample is RNA?",
   table=_T_RNA,
   choices=[
     "Sample Q, the only sample containing uracil and no thymine",
     "Sample P, the only sample in which adenine equals thymine",
     "Sample R, the only sample in which all four of its bases are present in equal amounts",
     "Samples P and R together, since both contain thymine",
     "None of the samples, because base composition cannot distinguish RNA from DNA"], ans=0,
   why="EK 6.1.B.1.ii lists uracil among the pyrimidines and EK 6.1.B.1.iii identifies uracil as the base that stands in for thymine in RNA. Only one sample in the table contains uracil, and it contains no thymine; the other two contain thymine and no uracil, which is the DNA composition."),
 dict(q="An investigator reports that a nucleic acid sample contains 40 percent adenine and 15 percent thymine. What does this measurement indicate about the sample?",
   choices=[
     "It is not a double-stranded molecule, because pairing would require adenine and thymine to be present in equal amounts",
     "It is double-stranded, and adenine is pairing with guanine in this organism",
     "It is RNA, because a molecule containing thymine must be single-stranded RNA",
     "It is a plasmid, because the circular shape of a plasmid exempts it from the pairing rules",
     "It is double-stranded, and the excess adenine simply remains unpaired, which is the usual arrangement"], ans=0,
   why="EK 6.1.B.1.iii pairs adenine with thymine, so in a double-stranded molecule each adenine has a thymine opposite it and the two percentages must match. Forty against fifteen therefore rules out a double-stranded molecule. The pairing rules are conserved under EK 6.1.B.1 rather than varying by organism or by the shape of the molecule, and thymine is the DNA base, with uracil standing in it for RNA."),
 dict(q="A student claims that because plasmids are circular, an organism found to contain plasmids must be a prokaryote. How should the claim be corrected?",
   choices=[
     "Both prokaryotes and eukaryotes can contain plasmids, so their presence does not identify the group",
     "Only eukaryotes contain plasmids, so the student has the two groups reversed",
     "Plasmids are linear rather than circular, so the premise of the claim is wrong",
     "Plasmids are made of RNA rather than DNA, so they are not part of the genome at all",
     "The claim is correct, because a circular molecule of DNA can exist only in a prokaryotic cell"], ans=0,
   why="EK 6.1.A.2 states that prokaryotes AND eukaryotes can contain plasmids, which are extra-chromosomal circular molecules of DNA. The shape and the composition in the student's premise are right; what fails is the inference, because the feature is not restricted to one group."),
 dict(q="Which feature of DNA does the framework identify as the characteristic that allows it to serve as hereditary material?",
   choices=[
     "Specific nucleotide base pairing, which is conserved through evolution",
     "The condensation of DNA by histones, which is found in every organism",
     "The circular shape of the molecule, which prevents its ends from being lost",
     "The presence of uracil, which distinguishes DNA from other molecules",
     "The variability of its base pairing rules, which allows new information to arise"], ans=0,
   why="Learning objective 6.1.B asks students to describe the characteristics of DNA that allow it to be used as hereditary material, and the essential knowledge under it is EK 6.1.B.1, that nucleic acids exhibit specific nucleotide base pairing conserved through evolution. Histones are eukaryote-specific under EK 6.1.A.1.ii, the circular shape is prokaryote-typical, and uracil belongs to RNA."),
 dict(q="A cell biologist examines a eukaryotic cell during a stage when its chromosomes are tightly compacted. Which components account for that compaction?",
   choices=[
     "Histones and associated proteins, which condense the linear chromosomes",
     "Plasmids, which wind the chromosome into loops",
     "Uracil-containing nucleotides, which shorten the chromosome",
     "Additional circular chromosomes that wrap around the linear ones",
     "The base pairing between purines and pyrimidines, which pulls the chromosome into a compact form"], ans=0,
   why="EK 6.1.A.1.ii states that eukaryotic linear chromosomes are condensed using histones and associated proteins. Base pairing under EK 6.1.B.1.iii holds the two strands of the double helix together but is not what the framework credits with condensing a chromosome, and plasmids are separate molecules under EK 6.1.A.2."),
 dict(q="Which statement about where genetic information resides is consistent with the framework?",
   choices=[
     "It is stored in and passed to later generations through DNA, and through RNA in some cases",
     "It is stored in DNA in prokaryotes and in RNA in eukaryotes",
     "It is stored in the histone proteins that condense the chromosomes",
     "It is stored in RNA in every organism and copied into DNA for storage",
     "It is stored only in plasmids, since these are the molecules that move between cells"], ans=0,
   why="EK 6.1.A.1 states that genetic information is stored in and passed to subsequent generations through DNA molecules and, in some cases, RNA molecules. Histones are the packaging proteins of EK 6.1.A.1.ii, plasmids are extra-chromosomal molecules under EK 6.1.A.2, and the framework assigns no group its own separate storage molecule."),
 dict(q="A DNA sample from an organism is found to contain 33 percent guanine. If the sample is double-stranded, what percentage is adenine?",
   choices=[
     "17 percent",
     "33 percent",
     "34 percent",
     "67 percent",
     "It cannot be determined, because adenine is unrelated to guanine"], ans=0,
   why="EK 6.1.B.1.iii pairs guanine with cytosine, so cytosine is also 33 percent and the two together account for 66 percent. The remaining 34 percent is shared equally between adenine and thymine because the same statement pairs those two, giving 17 percent each."),
 dict(q="Two nucleic acid strands are placed together and found not to pair along their length. Inspection shows that every base on the first strand is a purine and every base on the second is also a purine. Which rule accounts for the failure to pair?",
   choices=[
     "Purines pair with pyrimidines, so two purine strands offer no permitted partners",
     "Purines pair only with purines of the same kind, and the two strands carry different purines",
     "Purines are found only in DNA, so an RNA strand cannot contain them",
     "Purines have a single ring, which is too small to bridge the gap between two strands",
     "Purines pair with pyrimidines only in eukaryotes, and these strands came from a prokaryote"], ans=0,
   why="EK 6.1.B.1.iii states that purines pair with pyrimidines, naming adenine with thymine or uracil and guanine with cytosine. Two purine strands present no pyrimidine for any base to pair with. EK 6.1.B.1.i gives purines a double ring, and EK 6.1.B.1 makes the pairing rules conserved rather than group-specific."),
 dict(q="An organism's genome is reported as a single molecule of DNA, closed into a circle, together with two smaller circles of DNA that lie outside it. How should the three molecules be named?",
   choices=[
     "One circular chromosome and two plasmids",
     "Three chromosomes, since each is a separate circular molecule of DNA",
     "One chromosome and two histones",
     "Three plasmids, since all three are circular",
     "One plasmid and two chromosomes, since the largest circle is always the plasmid"], ans=0,
   why="EK 6.1.A.1.i gives prokaryotes a circular chromosome and EK 6.1.A.2 defines a plasmid as an extra-chromosomal circular molecule of DNA. The molecule that carries the genome is the chromosome and the ones lying outside it are the plasmids; histones are proteins under EK 6.1.A.1.ii, not DNA."),
 dict(q="Why does the framework describe base pairing as specific rather than as arbitrary?",
   choices=[
     "Each base has one permitted partner: adenine with thymine or uracil, and guanine with cytosine",
     "Each base can pair with any of the other three bases, which gives the molecule flexibility",
     "Each base pairs only with another copy of itself, which makes the two strands identical",
     "Only the purines pair, and the pyrimidines are left unpaired along the molecule",
     "Pairing is decided by the enzyme present rather than by the identity of the base"], ans=0,
   why="EK 6.1.B.1 states that nucleic acids exhibit specific nucleotide base pairing, and EK 6.1.B.1.iii spells out what specific means: purines pair with pyrimidines, adenine with thymine or uracil in RNA, and guanine with cytosine. Each base therefore has a determined partner rather than a choice among the others."),
 dict(q="A biologist compares the base pairing found in a bacterium, a fungus and a mammal and reports that the same pairs occur in all three. Which framework statement does this observation illustrate?",
   choices=[
     "That specific nucleotide base pairing is conserved through evolution",
     "That prokaryotes typically have circular chromosomes and eukaryotes linear ones",
     "That prokaryotes and eukaryotes can both contain plasmids",
     "That eukaryotic chromosomes are condensed using histones and associated proteins",
     "That genetic information can in some cases be stored in RNA"], ans=0,
   why="EK 6.1.B.1 states that nucleic acids exhibit specific nucleotide base pairing that is conserved through evolution. Finding the same pairs in three distantly related organisms is what a conserved feature looks like in data; the other statements concern chromosome shape, plasmids, packaging and the storage molecule, none of which the observation reports."),
 dict(q="A researcher wants to compare the amount of DNA packaging machinery in a bacterium and in a plant cell. Which expectation follows from the framework?",
   choices=[
     "The plant cell's linear chromosomes are condensed using histones and associated proteins, which the framework does not attribute to the bacterium",
     "Both cells condense their chromosomes with histones, since packaging is required by any chromosome",
     "The bacterium condenses its chromosome with histones and the plant cell does not",
     "Neither cell requires packaging, because a chromosome is already a compact molecule",
     "The plant cell packages its chromosomes with plasmids rather than with proteins"], ans=0,
   why="EK 6.1.A.1.ii attributes condensation using histones and associated proteins to eukaryotic linear chromosomes, and EK 6.1.A.1.i describes the prokaryotic chromosome as circular without making that attribution. A plant cell is eukaryotic and a bacterium is prokaryotic, and EK 6.1.A.2 makes plasmids separate DNA molecules rather than packaging."),
]
