# AP BIOLOGY 6.8 Biotechnology
# CED effective Fall 2025, Unit 6 Gene Expression and Regulation. Big idea 3
# (Information Storage and Transmission). Learning objective 6.8.A, explain the
# use of genetic engineering techniques in analyzing or manipulating DNA.
# Suggested skill 6.D, explain the relationship between EXPERIMENTAL RESULTS and
# larger biological concepts, processes, or theories.
#
# Essential knowledge relied on, in the framework's own words:
#   6.8.A.1     Genetic engineering techniques can be used to analyze and
#               manipulate DNA and RNA.
#   6.8.A.1.i   GEL ELECTROPHORESIS is a process that separates DNA fragments by
#               SIZE AND CHARGE.
#   6.8.A.1.ii  During POLYMERASE CHAIN REACTION (PCR), DNA fragments are
#               AMPLIFIED by denaturing DNA, annealing primers to the original
#               strand, and extending the new DNA molecule.
#   6.8.A.1.iii BACTERIAL TRANSFORMATION introduces foreign DNA into bacterial
#               cells.
#   6.8.A.1.iv  DNA SEQUENCING technology determines the ORDER OF NUCLEOTIDES in
#               a DNA molecule. Typically, these techniques result in a DNA
#               FINGERPRINT that allows for the comparison of DNA sequences from
#               various samples.
#
#   EXCLUSION STATEMENT printed with EK 6.8.A.1: "Knowledge of the DETAILS of
#   each of these genetic engineering techniques is beyond the scope of the AP
#   Exam." Nothing here asks about a buffer, a gel concentration, a named
#   enzyme, a temperature or a cycle time. Every item stays at the level the
#   framework itself states: what each technique does and what its results mean.
#
#   Illustrative examples printed with EK 6.8.A.1: amplified DNA fragments can
#   be used to identify organisms and perform phylogenetic analysis; analysis of
#   DNA can be used for forensic identification; genetically modified organisms
#   include transgenic animals; gene cloning allows propagation of DNA fragments.
#
# ON FIGURES -- THE HAZARD SCIENCE_BRIEF.md NAMES FOR THIS TOPIC. A gel is a
# picture and this bank cannot show one, so NO stem here says "the gel shown" or
# "the bands in the diagram". Where a gel result is needed it is delivered as a
# TABLE of fragment lengths against migration distances, and the item is asked
# of the table. That has a second benefit worth stating: because the
# relationship between length and distance is IN the data, no key depends on a
# student remembering which way round a gel runs -- which would be one of the
# technique details the exclusion statement bars.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX. Lengths are
# written "500 base pairs" and ranges as "between 1000 and 2000", never hyphenated.
TOPIC = ("6.8", "Biotechnology", 6)

# Four fragments of known length run together, with how far each moved.
_T_GEL = dict(
    headers=["DNA fragment", "Length in base pairs",
             "Distance moved through the gel (millimeters)"],
    rows=[["Fragment 1", "500", "62"],
          ["Fragment 2", "1000", "48"],
          ["Fragment 3", "2000", "33"],
          ["Fragment 4", "4000", "19"]])

# The same four fragments of known length, run alongside one unknown.
_T_GEL2 = dict(
    headers=["DNA fragment", "Length in base pairs",
             "Distance moved through the gel (millimeters)"],
    rows=[["Reference fragment 1", "500", "62"],
          ["Reference fragment 2", "1000", "48"],
          ["Unknown fragment", "not measured", "40"],
          ["Reference fragment 3", "2000", "33"],
          ["Reference fragment 4", "4000", "19"]])

# The fragment lengths detected in four samples.
_T_FINGER = dict(
    headers=["Sample", "Lengths of the fragments detected, in base pairs"],
    rows=[["Evidence sample", "400, 900, 1500"],
          ["Person 1", "400, 900, 1500"],
          ["Person 2", "400, 1200, 1500"],
          ["Person 3", "700, 900, 1800"]])

# Copies of one fragment counted after each cycle of amplification.
_T_PCR = dict(
    headers=["Number of cycles completed", "Number of copies of the fragment"],
    rows=[["0", "1"],
          ["1", "2"],
          ["2", "4"],
          ["3", "8"],
          ["4", "16"]])

# Bacteria plated after treatment, on a medium only transformed cells grow on.
_T_TRANSFORM = dict(
    headers=["Plate", "Bacteria treated with the foreign DNA",
             "Number of colonies growing on the selective medium"],
    rows=[["Plate 1", "Yes", "243"],
          ["Plate 2", "No", "0"]])

# The same gene sequenced in three species and compared pair by pair.
_T_SEQCOMP = dict(
    headers=["Pair of species compared",
             "Number of nucleotide differences found in the same gene"],
    rows=[["Species A and species B", "12"],
          ["Species A and species C", "58"],
          ["Species B and species C", "61"]])

# One scarce sample, measured before and after amplification.
_T_AMOUNT = dict(
    headers=["Sample", "Amplified before measurement",
             "Amount of the DNA fragment detected (arbitrary units)"],
    rows=[["Sample 1", "No", "3"],
          ["Sample 2", "Yes", "480"]])

QUESTIONS = [
 dict(q="What does gel electrophoresis do to a mixture of DNA fragments?",
   choices=[
     "It separates the fragments by size and charge",
     "It makes many copies of each fragment in the mixture",
     "It determines the order of the nucleotides in each fragment",
     "It introduces the fragments into bacterial cells",
     "It joins the fragments together into one continuous molecule"], ans=0,
   why="EK 6.8.A.1.i states that gel electrophoresis is a process that separates DNA fragments by size and charge. Making copies is what EK 6.8.A.1.ii assigns to the polymerase chain reaction, reading the order of nucleotides is EK 6.8.A.1.iv's sequencing, and introducing DNA into bacteria is EK 6.8.A.1.iii's transformation."),
 dict(q="Four DNA fragments of known length were separated together, with the results in the table. What relationship between length and movement do these data show?",
   table=_T_GEL,
   choices=[
     "The longer a fragment is, the shorter the distance it moved through the gel",
     "The longer a fragment is, the greater the distance it moved through the gel",
     "Length and distance moved are unrelated in these data",
     "Every fragment moved the same distance, whatever its length",
     "Only fragments longer than 2000 base pairs moved through the gel at all"], ans=0,
   why="EK 6.8.A.1.i states that gel electrophoresis separates DNA fragments by size and charge, and the table shows how the separation ran here: as length rises from 500 to 4000 base pairs the distance moved falls from 62 to 19 millimeters. The relationship is read off the data rather than recalled."),
 dict(q="An unknown fragment was separated alongside four reference fragments of known length, with the results in the table. What is the best estimate of the unknown fragment's length?",
   table=_T_GEL2,
   choices=[
     "Between 1000 and 2000 base pairs",
     "Between 500 and 1000 base pairs",
     "Between 2000 and 4000 base pairs",
     "Less than 500 base pairs",
     "More than 4000 base pairs"], ans=0,
   why="EK 6.8.A.1.i makes gel electrophoresis a separation by size, so a set of reference fragments calibrates the separation. The unknown moved 40 millimeters, which lies between the 48 millimeters of the 1000 base pair reference and the 33 millimeters of the 2000 base pair reference, so its length lies between those two lengths."),
 dict(q="The table reports the fragment lengths detected in an evidence sample and in samples from three people. Which person's sample matches the evidence sample?",
   table=_T_FINGER,
   choices=[
     "Person 1, whose three fragment lengths are the same as the evidence sample's",
     "Person 2, who shares two of the three fragment lengths with the evidence sample",
     "Person 3, who shares one of the three fragment lengths with the evidence sample",
     "All three people, since each shares at least one fragment length with the evidence sample",
     "None of them, since a fragment length cannot be compared between samples"], ans=0,
   why="EK 6.8.A.1.iv states that these techniques typically result in a DNA fingerprint that allows for the comparison of DNA sequences from various samples, and forensic identification is one of the illustrative examples the CED prints with EK 6.8.A.1. Comparing the three sets against the evidence set, exactly one person matches at every fragment length and the other two differ at one or two."),
 dict(q="What does the polymerase chain reaction do?",
   choices=[
     "It amplifies DNA fragments, producing many copies of them",
     "It separates DNA fragments by size and charge",
     "It determines the order of the nucleotides in a DNA molecule",
     "It introduces foreign DNA into bacterial cells",
     "It removes the introns from a primary transcript"], ans=0,
   why="EK 6.8.A.1.ii states that during the polymerase chain reaction DNA fragments are amplified. Separation belongs to EK 6.8.A.1.i, determining the order of nucleotides to EK 6.8.A.1.iv, and introducing DNA into bacteria to EK 6.8.A.1.iii; intron removal is a cellular processing step under EK 6.3.A.4.iii, not a laboratory technique."),
 dict(q="Which three steps does the framework name as the way DNA fragments are amplified in the polymerase chain reaction?",
   choices=[
     "Denaturing the DNA, annealing primers to the original strand, and extending the new DNA molecule",
     "Denaturing the DNA, separating the fragments by size, and reading their sequence",
     "Annealing primers, removing the introns, and joining the exons together",
     "Transcribing the DNA, translating the transcript, and folding the protein",
     "Introducing the DNA into bacteria, growing the bacteria, and counting the colonies"], ans=0,
   why="EK 6.8.A.1.ii states that during the polymerase chain reaction DNA fragments are amplified by denaturing DNA, annealing primers to the original strand, and extending the new DNA molecule. The other options mix in steps belonging to other techniques or to processes inside a cell."),
 dict(q="In what order does the framework list the steps of the polymerase chain reaction, and why must that order hold?",
   choices=[
     "Denaturing, then annealing primers, then extending, because a primer can only anneal to a strand that has been separated and only an annealed primer can be extended",
     "Extending, then annealing primers, then denaturing, because the new molecule must exist before a primer can bind it",
     "Annealing primers, then denaturing, then extending, because the primer holds the two strands apart",
     "Denaturing, then extending, then annealing primers, because extension does not require a primer",
     "The three steps occur simultaneously, so no order can be given"], ans=0,
   why="EK 6.8.A.1.ii lists denaturing DNA, annealing primers to the original strand, and extending the new DNA molecule in that order, and each step supplies what the next requires: EK 6.2.A.1.ii makes a single strand the thing a new strand is built on, and extension is by definition the lengthening of something already annealed."),
 dict(q="The table reports the number of copies of one fragment present after each of the first four cycles of amplification. About how many copies will be present after ten cycles?",
   table=_T_PCR,
   choices=[
     "About 1000 copies",
     "About 20 copies",
     "About 100 copies",
     "About 10000 copies",
     "About 40 copies"], ans=0,
   why="EK 6.8.A.1.ii states that DNA fragments are amplified in the polymerase chain reaction, and the table shows the amplification doubling the count at each cycle, from 1 to 2 to 4 to 8 to 16. Doubling ten times from one copy gives 1024, which of the listed values is about a thousand."),
 dict(q="What does bacterial transformation do?",
   choices=[
     "It introduces foreign DNA into bacterial cells",
     "It removes foreign DNA from bacterial cells",
     "It separates the DNA of a bacterial cell by size and charge",
     "It determines the order of the nucleotides in a bacterial chromosome",
     "It converts a bacterial cell into a eukaryotic cell"], ans=0,
   why="EK 6.8.A.1.iii states that bacterial transformation introduces foreign DNA into bacterial cells. The remaining options describe the reverse of that, or the roles the framework gives to gel electrophoresis in EK 6.8.A.1.i and to sequencing in EK 6.8.A.1.iv."),
 dict(q="Bacteria were plated on a medium that only cells carrying the foreign DNA can grow on, with the results in the table. What do these results show?",
   table=_T_TRANSFORM,
   choices=[
     "The treatment introduced the foreign DNA into some of the bacterial cells",
     "The treatment removed the foreign DNA from the bacterial cells",
     "The foreign DNA was present in the untreated cells as well",
     "The treatment killed all of the bacteria it was applied to",
     "The medium supported growth of every cell placed on it"], ans=0,
   why="EK 6.8.A.1.iii states that bacterial transformation introduces foreign DNA into bacterial cells, and skill 6.D asks what an experimental result shows. Colonies appeared on the treated plate and none on the untreated plate, so growth on this medium followed the treatment and the untreated cells did not already carry the DNA."),
 dict(q="What does DNA sequencing technology determine?",
   choices=[
     "The order of the nucleotides in a DNA molecule",
     "The number of copies of a DNA molecule in a sample",
     "The size and charge of a DNA molecule",
     "The species of bacterium a DNA molecule was introduced into",
     "The amino acid sequence of a protein, read directly without an intermediate"], ans=0,
   why="EK 6.8.A.1.iv states that DNA sequencing technology determines the order of nucleotides in a DNA molecule. Counting copies is what amplification under EK 6.8.A.1.ii is for, and separating by size and charge is what EK 6.8.A.1.i assigns to gel electrophoresis."),
 dict(q="What does the framework say a DNA fingerprint allows?",
   choices=[
     "The comparison of DNA sequences from various samples",
     "The amplification of a DNA fragment without primers",
     "The introduction of foreign DNA into a bacterial cell",
     "The removal of introns from a DNA molecule",
     "The determination of an organism's phenotype without any observation of it"], ans=0,
   why="EK 6.8.A.1.iv states that these techniques typically result in a DNA fingerprint that allows for the comparison of DNA sequences from various samples. The other options belong to EK 6.8.A.1.ii and EK 6.8.A.1.iii or to processes the framework locates inside a cell."),
 dict(q="A researcher needs to know the order of the nucleotides in a purified DNA fragment. Which of the techniques named by the framework is appropriate?",
   choices=[
     "DNA sequencing, which determines the order of nucleotides in a DNA molecule",
     "Gel electrophoresis, which separates DNA fragments by size and charge",
     "The polymerase chain reaction, which amplifies DNA fragments",
     "Bacterial transformation, which introduces foreign DNA into bacterial cells",
     "None of them, since the order of nucleotides cannot be determined experimentally"], ans=0,
   why="EK 6.8.A.1.iv assigns the determination of the order of nucleotides to DNA sequencing technology. Each of the other three techniques is defined by the framework as doing something else: separating, amplifying and introducing DNA respectively."),
 dict(q="A researcher has only a very small quantity of a DNA fragment and needs much more of it before any analysis can be done. Which technique is appropriate?",
   choices=[
     "The polymerase chain reaction, in which DNA fragments are amplified",
     "Gel electrophoresis, in which DNA fragments are separated by size and charge",
     "DNA sequencing, in which the order of nucleotides is determined",
     "Bacterial transformation, in which foreign DNA is introduced into bacterial cells",
     "None of them, since the quantity of a DNA sample cannot be increased"], ans=0,
   why="EK 6.8.A.1.ii states that during the polymerase chain reaction DNA fragments are amplified, which is exactly the need described. Gene cloning, one of the illustrative examples the CED prints with EK 6.8.A.1, likewise allows propagation of DNA fragments, but of the listed techniques only amplification is defined as increasing the number of copies."),
 dict(q="A researcher has a mixture of DNA fragments of several different lengths and needs to separate them from one another. Which technique is appropriate?",
   choices=[
     "Gel electrophoresis, which separates DNA fragments by size and charge",
     "The polymerase chain reaction, which amplifies DNA fragments",
     "Bacterial transformation, which introduces foreign DNA into bacterial cells",
     "DNA sequencing, which determines the order of nucleotides",
     "None of them, since fragments of different lengths cannot be separated"], ans=0,
   why="EK 6.8.A.1.i states that gel electrophoresis is a process that separates DNA fragments by size and charge, which is the operation the researcher needs. The other three techniques are defined by the framework as amplifying, introducing and reading DNA rather than separating it."),
 dict(q="A researcher wants a bacterial culture to carry and propagate a particular DNA fragment. Which technique introduces the fragment into the cells?",
   choices=[
     "Bacterial transformation, which introduces foreign DNA into bacterial cells",
     "Gel electrophoresis, which separates DNA fragments by size and charge",
     "DNA sequencing, which determines the order of nucleotides",
     "The polymerase chain reaction, which amplifies DNA fragments in a tube",
     "None of them, since a bacterial cell cannot take up DNA from outside"], ans=0,
   why="EK 6.8.A.1.iii states that bacterial transformation introduces foreign DNA into bacterial cells, which is the step described. Gene cloning allowing propagation of DNA fragments is one of the illustrative examples the CED prints with EK 6.8.A.1, and it depends on the DNA first being introduced."),
 dict(q="The same gene was sequenced in three species and the pairs compared, with the results in the table. Which two species are most similar in this gene?",
   table=_T_SEQCOMP,
   choices=[
     "Species A and species B, which differ at the fewest nucleotides",
     "Species A and species C, which differ at the fewest nucleotides",
     "Species B and species C, which differ at the fewest nucleotides",
     "All three pairs are equally similar, since all three were compared",
     "The comparison cannot be made, because sequences from different species cannot be aligned"], ans=0,
   why="EK 6.8.A.1.iv states that these techniques result in a DNA fingerprint that allows for the comparison of DNA sequences from various samples, and using amplified DNA fragments to identify organisms and perform phylogenetic analysis is one of the illustrative examples the CED prints with EK 6.8.A.1. Fewer differences means greater similarity, and one pair differs at 12 nucleotides against 58 and 61 for the others."),
 dict(q="An investigator compares DNA from a crime scene with DNA from several people and reports a match. Which framework statement licenses that comparison?",
   choices=[
     "That DNA sequencing typically results in a fingerprint allowing comparison of DNA sequences from various samples",
     "That gel electrophoresis separates DNA fragments by size and charge",
     "That bacterial transformation introduces foreign DNA into bacterial cells",
     "That the polymerase chain reaction amplifies DNA fragments",
     "That genetic information in retroviruses flows from RNA to DNA"], ans=0,
   why="EK 6.8.A.1.iv states that these techniques typically result in a DNA fingerprint that allows for the comparison of DNA sequences from various samples, and forensic identification is one of the illustrative examples the CED prints with EK 6.8.A.1. Separation and amplification may be used along the way, but neither is what licenses a comparison between samples."),
 dict(q="Which of the following is an example of a genetically modified organism, as the CED illustrates the term?",
   choices=[
     "A transgenic animal, which carries DNA introduced from another source",
     "An animal whose coat color changed in response to a change in day length",
     "An animal that inherited two recessive alleles from its parents",
     "An animal in which a mutation arose spontaneously during replication",
     "An animal whose genes are expressed differently in different tissues"], ans=0,
   why="The CED prints among its illustrative examples for EK 6.8.A.1 that genetically modified organisms include transgenic animals, which follows from EK 6.8.A.1's statement that genetic engineering techniques can be used to manipulate DNA. A seasonal coat change is EK 5.5.A.1's phenotypic plasticity, a spontaneous mutation is EK 6.7.B.1's, and differential expression across tissues is EK 6.6.B.1's."),
 dict(q="The CED notes that gene cloning allows the propagation of DNA fragments. What does that mean for a researcher with a single fragment of interest?",
   choices=[
     "The fragment can be reproduced in quantity rather than being used up by a single analysis",
     "The fragment's nucleotide order can be read without any further technique",
     "The fragment can be separated from other fragments by its charge alone",
     "The fragment will be translated directly into the protein it encodes",
     "The fragment can be introduced into any organism without further manipulation"], ans=0,
   why="Gene cloning allowing propagation of DNA fragments is one of the illustrative examples the CED prints with EK 6.8.A.1, and to propagate a fragment is to produce more of it. Reading the order of nucleotides is EK 6.8.A.1.iv's separate technique and separation by size and charge is EK 6.8.A.1.i's."),
 dict(q="One scarce sample was measured before and after treatment, with the results in the table. Which technique best accounts for the difference between the two measurements?",
   table=_T_AMOUNT,
   choices=[
     "The polymerase chain reaction, which amplifies DNA fragments",
     "Gel electrophoresis, which separates DNA fragments by size and charge",
     "DNA sequencing, which determines the order of nucleotides",
     "Bacterial transformation, which introduces foreign DNA into bacterial cells",
     "Nothing, because the amount of DNA in a sample cannot change"], ans=0,
   why="EK 6.8.A.1.ii states that DNA fragments are amplified in the polymerase chain reaction, and skill 6.D asks what an experimental result shows. The amount detected rises from 3 units to 480 after the treatment, which is an increase of more than a hundredfold in the quantity of DNA; separating, reading or introducing DNA would not raise the amount present."),
 dict(q="What does annealing a primer to the original strand accomplish in the polymerase chain reaction?",
   choices=[
     "It provides the starting point from which the new DNA molecule is extended",
     "It separates the two strands of the original DNA molecule from each other",
     "It reads the order of the nucleotides in the original strand",
     "It separates the amplified fragments by size and charge",
     "It introduces the amplified fragment into a bacterial cell"], ans=0,
   why="EK 6.8.A.1.ii lists annealing primers to the original strand between denaturing the DNA and extending the new DNA molecule, so the annealed primer is what the extension step extends. Separating the strands is the denaturing step of the same statement, and the remaining options belong to EK 6.8.A.1.i, iii and iv."),
 dict(q="Why must the DNA be denatured before primers can anneal to it in the polymerase chain reaction?",
   choices=[
     "A primer anneals to a single strand, and denaturing separates the two strands of the molecule",
     "A primer anneals to a double-stranded molecule, and denaturing makes the molecule double-stranded",
     "Denaturing removes the primers left from the previous cycle so that new ones can bind",
     "Denaturing determines the order of the nucleotides so that a matching primer can be chosen",
     "Denaturing is not required, since the framework lists the three steps in no particular order"], ans=0,
   why="EK 6.8.A.1.ii names annealing primers TO THE ORIGINAL STRAND, and EK 6.2.A.1.ii makes a single strand the thing a complementary strand is built on. Denaturing is listed first for that reason, and the framework does give the three steps in an order."),
 dict(q="A polymerase chain reaction is set up with the DNA sample and everything else it needs except the primers. What is the expected result?",
   choices=[
     "No new DNA molecule is extended, because there is nothing annealed to the original strand to extend",
     "The DNA is amplified as usual, because the primers are only needed for the first cycle",
     "The DNA is separated by size and charge instead of being amplified",
     "The order of the nucleotides in the sample is determined instead",
     "The sample is introduced into bacterial cells instead of being amplified"], ans=0,
   why="EK 6.8.A.1.ii makes annealing primers to the original strand one of the three steps by which fragments are amplified, and the third step extends the new DNA molecule from what was annealed. With nothing annealed there is nothing to extend, so the amplification the statement describes cannot occur."),
 dict(q="Which pairing of a technique with what it produces is consistent with the framework?",
   choices=[
     "Gel electrophoresis produces fragments separated by size and charge, while sequencing produces the order of the nucleotides",
     "Gel electrophoresis produces the order of the nucleotides, while sequencing produces fragments separated by size and charge",
     "The polymerase chain reaction produces fragments separated by size and charge, while transformation produces many copies of a fragment",
     "Transformation produces the order of the nucleotides, while sequencing produces bacterial cells carrying foreign DNA",
     "All four techniques produce the same result by different means"], ans=0,
   why="EK 6.8.A.1.i assigns separation by size and charge to gel electrophoresis and EK 6.8.A.1.iv assigns the determination of the order of nucleotides to sequencing technology. Each of the rejected options exchanges the outputs the framework assigns to two of the four techniques."),
 dict(q="A researcher recovers a very small amount of DNA from an old specimen and wants to compare its sequence with sequences from living species. Which order of techniques matches what the framework says each one does?",
   choices=[
     "Amplify the fragment by the polymerase chain reaction, then determine the order of its nucleotides by sequencing, then compare the sequences",
     "Determine the order of its nucleotides by sequencing, then amplify the fragment, then compare the sequences",
     "Introduce the fragment into bacterial cells, then separate it by size and charge, then amplify it",
     "Compare the sequences, then amplify the fragment, then determine the order of its nucleotides",
     "Separate the fragment by size and charge, which by itself gives the order of its nucleotides"], ans=0,
   why="EK 6.8.A.1.ii makes amplification the way a scarce fragment is increased in quantity, EK 6.8.A.1.iv makes sequencing the technique that determines the order of nucleotides, and the same statement makes comparison across samples what the resulting fingerprint allows. Comparing sequences requires the sequences to exist, so the order is fixed by what each step supplies to the next."),
 dict(q="Using amplified DNA fragments to identify an unknown organism and place it among its relatives is which of the following?",
   choices=[
     "One of the illustrative uses the CED prints for genetic engineering techniques, resting on the comparison of DNA sequences from various samples",
     "An application of gel electrophoresis alone, since separation by size identifies a species",
     "An application of bacterial transformation, since the organism's DNA is introduced into bacteria",
     "Impossible under the framework, since DNA sequences cannot be compared between species",
     "An application of epigenetic modification, since expression differs between species"], ans=0,
   why="The CED prints among its illustrative examples for EK 6.8.A.1 that amplified DNA fragments can be used to identify organisms and perform phylogenetic analysis, and EK 6.8.A.1.iv supplies the comparison of DNA sequences from various samples that such an analysis rests on. Separation by size under EK 6.8.A.1.i does not by itself identify a species."),
 dict(q="What does the framework say genetic engineering techniques can be used to do, in general terms?",
   choices=[
     "Analyze and manipulate DNA and RNA",
     "Analyze DNA only, since RNA cannot be worked with in the laboratory",
     "Manipulate DNA only, since analysis requires no technique",
     "Analyze and manipulate proteins rather than nucleic acids",
     "Determine an organism's phenotype without examining any molecule"], ans=0,
   why="EK 6.8.A.1 states that genetic engineering techniques can be used to analyze and manipulate DNA and RNA, which names both kinds of activity and both kinds of nucleic acid. The four techniques listed beneath it are the framework's examples of that general statement."),
 dict(q="A student says that because a gel separates DNA by size and charge, running a gel will reveal the sequence of a fragment. How should this be corrected?",
   choices=[
     "Separation by size and charge places a fragment among others of known length; determining the order of its nucleotides is what sequencing does",
     "Separation by size and charge does reveal the sequence, so the student is correct",
     "Separation by size and charge reveals the sequence only for fragments shorter than 500 base pairs",
     "Separation by size and charge is a step of the polymerase chain reaction, so the student has named the wrong technique",
     "Separation by size and charge introduces the fragment into a bacterial cell, where its sequence can be read"], ans=0,
   why="EK 6.8.A.1.i confines gel electrophoresis to separating DNA fragments by size and charge, and EK 6.8.A.1.iv assigns the determination of the order of nucleotides to sequencing technology. The framework keeps the two techniques and the two results separate."),
 dict(q="Which statement about the four techniques named in this topic is consistent with the framework?",
   choices=[
     "One separates fragments by size and charge, one amplifies fragments, one introduces foreign DNA into bacterial cells, and one determines the order of nucleotides",
     "All four determine the order of nucleotides, differing only in how quickly they do so",
     "All four introduce foreign DNA into cells, differing only in the kind of cell",
     "Three of them amplify DNA and the fourth destroys it",
     "None of them can be applied to RNA, since the framework names DNA only"], ans=0,
   why="The four roles are stated separately in EK 6.8.A.1.i to iv, and this option assigns each technique the role the framework assigns it. EK 6.8.A.1 also states that genetic engineering techniques can be used to analyze and manipulate DNA AND RNA, so the last option misreports the framework's scope."),
]
