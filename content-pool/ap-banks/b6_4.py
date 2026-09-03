# AP BIOLOGY 6.4 Translation
# CED effective Fall 2025, Unit 6 Gene Expression and Regulation. Big idea 3
# (Information Storage and Transmission). Learning objective 6.4.A, explain how
# the phenotype of an organism is determined by its genotype. Suggested skills
# 2.D, represent relationships within biological models, and 6.E, predict the
# causes or effects of a change in, or disruption to, one or more components in
# a biological system.
#
# Essential knowledge relied on, in the framework's own words:
#   6.4.A.1       Translation of the mRNA to generate a polypeptide occurs on
#                 ribosomes that are present in the CYTOPLASM OF BOTH
#                 prokaryotic and eukaryotic cells, as well as the CYTOPLASMIC
#                 SURFACE of the rough ER of eukaryotic cells.
#   6.4.A.2       In prokaryotic organisms, translation of the mRNA molecule
#                 occurs WHILE IT IS BEING TRANSCRIBED.
#   6.4.A.3       Translation involves many sequential steps, including
#                 initiation, elongation, and termination.
#   6.4.A.3.i     Translation is initiated when the rRNA in the ribosome
#                 interacts with the mRNA at the start codon (AUG, coding for
#                 the amino acid methionine).
#   6.4.A.3.ii    The sequence of nucleotides on the mRNA is read in TRIPLETS,
#                 called codons.
#   6.4.A.3.iii   Each codon encodes a specific amino acid, which can be deduced
#                 by using a GENETIC CODE CHART. Many amino acids are encoded by
#                 more than one codon.
#   6.4.A.3.iv    Nearly all living organisms use the same genetic code, which
#                 is evidence for the COMMON ANCESTRY of all living organisms.
#   6.4.A.3.v     tRNA brings the correct amino acid to the place specified by
#                 the codon on the mRNA.
#   6.4.A.3.vi    The amino acid is transferred to the growing polypeptide chain.
#   6.4.A.3.vii   The process continues along the mRNA until a STOP CODON is
#                 reached.
#   6.4.A.3.viii  Translation terminates with the release of the newly
#                 synthesized protein.
#   6.4.A.4       Genetic information in retroviruses is a special case and has
#                 an alternate flow of information: FROM RNA TO DNA, made
#                 possible by reverse transcriptase, an enzyme that copies the
#                 viral RNA genome into DNA. This DNA integrates into the host
#                 genome and is transcribed and translated for the assembly of
#                 new viral progeny.
#
# ON THE GENETIC CODE CHART. EK 6.4.A.3.iii says explicitly that the amino acid
# a codon encodes "can be deduced by using a genetic code chart", so the chart
# is stimulus material the framework expects a student to be given rather than
# to have memorised. It is delivered here as a table=, which is exactly what
# SCIENCE_BRIEF.md asks for: the data are in the question. No item asks a
# student to recall a codon assignment from memory.
#
# DIVISION OF LABOUR ACROSS 6.1 TO 6.4 is set out in the header of b6_1.py.
# tRNA appears in 6.3 as a molecule -- what it binds, what its anticodon pairs
# with -- and here as a participant in the elongation cycle, which is EK
# 6.4.A.3.v and vi. Base pairing itself is 6.1's and is not re-asked.
# DIVISION WITH 6.7: a premature stop codon is asked here as what the RIBOSOME
# does on reaching one (EK 6.4.A.3.vii and viii) and in 6.7 as what KIND OF
# MUTATION produced it (EK 6.7.A.1.iii).
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX.
TOPIC = ("6.4", "Translation", 6)

# A partial genetic code chart, supplied as stimulus.
_T_CODE = dict(
    headers=["mRNA codon", "Amino acid encoded"],
    rows=[["AUG", "Methionine"],
          ["UUU", "Phenylalanine"],
          ["UUC", "Phenylalanine"],
          ["GGA", "Glycine"],
          ["GGU", "Glycine"],
          ["CAU", "Histidine"],
          ["AAG", "Lysine"],
          ["UCA", "Serine"],
          ["UAA", "Stop"],
          ["UGA", "Stop"]])

# Coding regions of three transcripts, measured in nucleotides.
_T_LEN = dict(
    headers=["Transcript", "Length of the coding region in nucleotides"],
    rows=[["Transcript 1", "30"],
          ["Transcript 2", "45"],
          ["Transcript 3", "72"]])

QUESTIONS = [
 dict(q="Where does translation of an mRNA molecule into a polypeptide take place?",
   choices=[
     "On ribosomes in the cytoplasm of both prokaryotic and eukaryotic cells, and on the cytoplasmic surface of the rough endoplasmic reticulum in eukaryotic cells",
     "On ribosomes inside the nucleus of eukaryotic cells and in the cytoplasm of prokaryotic cells",
     "On the inner surface of the rough endoplasmic reticulum, where the polypeptide is enclosed as it is made",
     "On the DNA template strand itself, which the ribosome reads directly",
     "In the cytoplasm of eukaryotic cells only, since prokaryotic cells have no ribosomes"], ans=0,
   why="EK 6.4.A.1 states that translation occurs on ribosomes present in the cytoplasm of both prokaryotic and eukaryotic cells, as well as the cytoplasmic surface of the rough endoplasmic reticulum of eukaryotic cells. The surface named is the cytoplasmic one, and ribosomes are common to both kinds of cell."),
 dict(q="Which structure is required for translation in a prokaryotic cell and in a eukaryotic cell alike?",
   choices=[
     "The ribosome, which is present in the cytoplasm of both kinds of cell",
     "The nucleus, in which the ribosome assembles the polypeptide",
     "The rough endoplasmic reticulum, on whose surface all translation occurs",
     "The plasmid, which carries the mRNA to the site of translation",
     "The template DNA strand, which is read directly during translation"], ans=0,
   why="EK 6.4.A.1 places translation on ribosomes present in the cytoplasm of both prokaryotic and eukaryotic cells. The rough endoplasmic reticulum is named only for eukaryotic cells and only as an additional site, and a prokaryotic cell has no nucleus."),
 dict(q="What is distinctive about translation in a prokaryotic organism?",
   choices=[
     "Translation of the mRNA occurs while that mRNA is still being transcribed",
     "Translation of the mRNA occurs only after the transcript has been given a poly-A tail",
     "Translation occurs before transcription, so the polypeptide sets the sequence of the mRNA",
     "Translation occurs inside the nucleus, so the transcript never leaves it",
     "Translation occurs without ribosomes, which prokaryotic cells lack"], ans=0,
   why="EK 6.4.A.2 states that in prokaryotic organisms translation of the mRNA molecule occurs while it is being transcribed. The processing modifications of EK 6.3.A.4 are given for eukaryotic cells, and EK 6.4.A.1 gives prokaryotic cells ribosomes in their cytoplasm."),
 dict(q="Why can translation of a eukaryotic transcript not begin while that transcript is still being made, as it does in a prokaryote?",
   choices=[
     "The eukaryotic transcript is made at the DNA in the nucleus while the ribosome that translates it lies in the cytoplasm",
     "The eukaryotic transcript is made in the cytoplasm while the ribosome that translates it lies in the nucleus",
     "Eukaryotic ribosomes read DNA rather than mRNA, so no transcript is involved",
     "Eukaryotic transcription is too fast for a ribosome to keep pace with it",
     "Eukaryotic cells translate only on the rough endoplasmic reticulum, which is not present during transcription"], ans=0,
   why="EK 6.4.A.2 confines simultaneous transcription and translation to prokaryotic organisms, and EK 6.3.A.1.i places the eukaryotic transcript's origin at the DNA in the nucleus and its destination at the ribosome in the cytoplasm. The two processes are therefore in different compartments, while EK 6.4.A.1 puts eukaryotic ribosomes in the cytoplasm and on the cytoplasmic surface of the rough endoplasmic reticulum."),
 dict(q="Translation is described in the framework as involving many sequential steps. Which three does it name?",
   choices=[
     "Initiation, elongation and termination",
     "Transcription, splicing and termination",
     "Initiation, replication and elongation",
     "Recognition, capping and release",
     "Unwinding, priming and joining"], ans=0,
   why="EK 6.4.A.3 states that translation involves many sequential steps, including initiation, elongation, and termination. Splicing and capping are modifications of the transcript under EK 6.3.A.4, and unwinding, priming and joining belong to replication under EK 6.2.A.1."),
 dict(q="What event initiates translation?",
   choices=[
     "The rRNA in the ribosome interacts with the mRNA at the start codon",
     "A tRNA molecule binds the DNA template strand at the start codon",
     "RNA polymerase binds the mRNA and begins reading it in triplets",
     "The poly-A tail of the mRNA is joined to the ribosome",
     "The first amino acid is released from the growing polypeptide chain"], ans=0,
   why="EK 6.4.A.3.i states that translation is initiated when the rRNA in the ribosome interacts with the mRNA at the start codon. RNA polymerase acts on a DNA template under EK 6.3.A.2 and has no role here, and release of the protein is the terminating event under EK 6.4.A.3.viii."),
 dict(q="Which codon is the start codon, and which amino acid does it code for?",
   choices=[
     "AUG, coding for methionine",
     "AUG, coding for lysine",
     "UAA, coding for methionine",
     "UGA, coding for serine",
     "AAG, coding for methionine"], ans=0,
   why="EK 6.4.A.3.i names the start codon as AUG, coding for the amino acid methionine. UAA and UGA are stop codons, and the framework attaches methionine specifically to AUG."),
 dict(q="How is the sequence of nucleotides on an mRNA molecule read during translation?",
   choices=[
     "In triplets, each of which is called a codon",
     "In pairs, each of which is called a codon",
     "One nucleotide at a time, each specifying one amino acid",
     "In groups of four, each of which is called an anticodon",
     "In whole exons, each of which specifies one amino acid"], ans=0,
   why="EK 6.4.A.3.ii states that the sequence of nucleotides on the mRNA is read in triplets, called codons. The anticodon belongs to tRNA under EK 6.3.A.1.ii, and an exon is a segment retained during processing under EK 6.3.A.4.iii rather than a unit of reading."),
 dict(q="A student is asked which amino acid a particular mRNA codon specifies. What does the framework say the student should use?",
   choices=[
     "A genetic code chart, from which the amino acid encoded by each codon can be deduced",
     "A pedigree, from which the pattern of inheritance can be deduced",
     "A Punnett square, from which the genotype of the offspring can be deduced",
     "A density gradient, from which the strands of the molecule can be separated",
     "The anticodon of the mRNA, which names the amino acid directly"], ans=0,
   why="EK 6.4.A.3.iii states that each codon encodes a specific amino acid, which can be deduced by using a genetic code chart. Punnett squares and pedigrees are the tools of EK 5.3.A.2.v, and an anticodon belongs to tRNA rather than to mRNA under EK 6.3.A.1.ii."),
 dict(q="The framework states that many amino acids are encoded by more than one codon. What follows from this?",
   choices=[
     "Two different codons can specify the same amino acid",
     "Two different amino acids can be specified by the same codon",
     "Each codon specifies more than one amino acid, and the ribosome chooses between them",
     "Every amino acid is specified by exactly three codons",
     "An amino acid can be added to the chain without any codon specifying it"], ans=0,
   why="EK 6.4.A.3.iii states that each codon encodes a specific amino acid and that many amino acids are encoded by more than one codon. The relationship therefore runs many codons to one amino acid, never one codon to many amino acids, and the framework gives no fixed number of codons per amino acid."),
 dict(q="Nearly all living organisms use the same genetic code. What does the framework say this is evidence for?",
   choices=[
     "The common ancestry of all living organisms",
     "The independent origin of each major group of organisms",
     "The tendency of the genetic code to change rapidly within a lineage",
     "The absence of any relationship between DNA sequence and protein sequence",
     "The presence of a nucleus in every kind of cell"], ans=0,
   why="EK 6.4.A.3.iv states that nearly all living organisms use the same genetic code, which is evidence for the common ancestry of all living organisms. A code shared across lineages is what a feature inherited from a shared ancestor looks like, and independent origins would not predict it."),
 dict(q="What does a tRNA molecule do during elongation?",
   choices=[
     "It brings the correct amino acid to the place specified by the codon on the mRNA",
     "It brings the correct codon to the place specified by the amino acid on the ribosome",
     "It brings the mRNA from the nucleus to the ribosome in the cytoplasm",
     "It joins the growing polypeptide chain to the ribosome",
     "It reads the DNA template strand and copies it into mRNA"], ans=0,
   why="EK 6.4.A.3.v states that tRNA brings the correct amino acid to the place specified by the codon on the mRNA. The reversed option makes the amino acid specify the codon, and carrying information from the nucleus is mRNA's role under EK 6.3.A.1.i."),
 dict(q="Once a tRNA has delivered its amino acid at the correct codon, what happens next?",
   choices=[
     "The amino acid is transferred to the growing polypeptide chain",
     "The amino acid is released from the ribosome unchanged",
     "The codon is transferred to the growing polypeptide chain",
     "The tRNA is incorporated into the growing polypeptide chain",
     "The mRNA is cut at that codon so that the next codon can be read"], ans=0,
   why="EK 6.4.A.3.vi states that the amino acid is transferred to the growing polypeptide chain. What is added to the chain is the amino acid rather than the codon or the tRNA, and EK 6.4.A.3.vii has the process continue along the intact mRNA."),
 dict(q="What determines where the ribosome stops moving along an mRNA molecule?",
   choices=[
     "The process continues along the mRNA until a stop codon is reached",
     "The process continues until the ribosome has added a fixed number of amino acids",
     "The process continues until the poly-A tail is reached, which marks the end",
     "The process continues until the supply of tRNA in the cell is used up",
     "The process continues until a second ribosome arrives at the same mRNA"], ans=0,
   why="EK 6.4.A.3.vii states that the process continues along the mRNA until a stop codon is reached. The stopping point is a sequence feature of the message itself rather than a count of amino acids or a shortage of any component."),
 dict(q="What is the final event of translation?",
   choices=[
     "The newly synthesized protein is released",
     "The newly synthesized protein is joined to the mRNA that encoded it",
     "The mRNA is broken down into individual codons",
     "The ribosome is broken down into its ribosomal RNA components",
     "A stop codon is added to the end of the polypeptide chain"], ans=0,
   why="EK 6.4.A.3.viii states that translation terminates with the release of the newly synthesized protein. A stop codon is a feature of the mRNA under EK 6.4.A.3.vii, not something added to a polypeptide, and nothing in the framework has the ribosome or the message destroyed at termination."),
 dict(q="Using the genetic code chart in the table, what polypeptide is encoded by the mRNA sequence AUGUUUGGACAUUAA?",
   table=_T_CODE,
   choices=[
     "Methionine, phenylalanine, glycine, histidine",
     "Methionine, phenylalanine, glycine, histidine, serine",
     "Methionine, phenylalanine, glycine, histidine, lysine",
     "Methionine, glycine, phenylalanine, histidine",
     "Phenylalanine, glycine, histidine, methionine"], ans=0,
   why="EK 6.4.A.3.ii reads the sequence in triplets and EK 6.4.A.3.iii deduces each amino acid from the chart. The triplets are AUG, UUU, GGA, CAU and UAA, which the chart assigns to methionine, phenylalanine, glycine, histidine and a stop; by EK 6.4.A.3.vii and viii the ribosome stops at the last of these and releases the four amino acids already joined."),
 dict(q="For that same mRNA sequence and chart, how many amino acids does the finished polypeptide contain, and why?",
   table=_T_CODE,
   choices=[
     "Four, because the fifth triplet is a stop codon and adds no amino acid",
     "Five, because the sequence contains five triplets and each specifies one amino acid",
     "Fifteen, because each nucleotide specifies one amino acid",
     "Three, because the start codon is a signal rather than an amino acid",
     "Five, because the stop codon specifies the last amino acid of the chain"], ans=0,
   why="EK 6.4.A.3.ii divides the fifteen nucleotides into five triplets, and the chart assigns four of them an amino acid and the fifth a stop. EK 6.4.A.3.i makes the start codon an amino acid as well as a signal, since it codes for methionine, so the chain contains four residues."),
 dict(q="Which feature of the chart in the table illustrates the framework's statement that many amino acids are encoded by more than one codon?",
   table=_T_CODE,
   choices=[
     "Phenylalanine is listed for two different codons, UUU and UUC",
     "Methionine is listed for the codon AUG and also serves as the start signal",
     "Two different codons in the chart are marked as stop rather than as an amino acid",
     "Each amino acid in the chart is listed for exactly one codon",
     "One codon in the chart is listed for two different amino acids"], ans=0,
   why="EK 6.4.A.3.iii states that each codon encodes a specific amino acid and that many amino acids are encoded by more than one codon. In the chart the same amino acid appears against two distinct codons, which is that relationship; a codon listed against two amino acids would contradict the first half of the statement."),
 dict(q="According to the chart, what happens when a ribosome moving along an mRNA reaches the codon UAA?",
   table=_T_CODE,
   choices=[
     "The process stops there and the newly synthesized protein is released",
     "The amino acid listed for that codon is added and the ribosome continues",
     "A tRNA delivers methionine, because every chain both begins and ends with it",
     "The ribosome skips that codon and reads the following triplet instead",
     "The mRNA is spliced at that codon and translation resumes on the far side"], ans=0,
   why="The chart lists that codon as a stop rather than as an amino acid, and EK 6.4.A.3.vii states that the process continues along the mRNA until a stop codon is reached, with EK 6.4.A.3.viii terminating translation by releasing the newly synthesized protein. Nothing in the framework has a ribosome skip a codon or splice a message."),
 dict(q="The table reports the length of the coding region of three transcripts. Which transcript is read as 15 codons?",
   table=_T_LEN,
   choices=[
     "Transcript 2, whose coding region is 45 nucleotides long",
     "Transcript 1, whose coding region is 30 nucleotides long",
     "Transcript 3, whose coding region is 72 nucleotides long",
     "Transcript 1 and transcript 2 together, since neither alone is long enough",
     "None of them, because the number of codons cannot be worked out from a length"], ans=0,
   why="EK 6.4.A.3.ii states that the sequence of nucleotides is read in triplets, so the number of codons is the length divided by three. Dividing the three lengths gives 10, 15 and 24 codons, and 15 belongs to the 45 nucleotide transcript."),
 dict(q="How does genetic information flow in a retrovirus, and what makes that flow possible?",
   choices=[
     "From RNA to DNA, made possible by reverse transcriptase copying the viral RNA genome into DNA",
     "From DNA to RNA, made possible by reverse transcriptase copying the viral DNA genome into RNA",
     "From protein to RNA, made possible by an enzyme that reads the amino acid sequence",
     "From RNA to RNA, made possible by an enzyme that copies the genome without any DNA stage",
     "From DNA to protein directly, without any RNA intermediate"], ans=0,
   why="EK 6.4.A.4 states that genetic information in retroviruses is a special case with an alternate flow of information from RNA to DNA, made possible by reverse transcriptase, an enzyme that copies the viral RNA genome into DNA. The usual direction, DNA to RNA, is transcription under EK 6.3.A.2 and is what makes the retroviral case an alternate one."),
 dict(q="After reverse transcriptase has copied a retroviral RNA genome into DNA, what does the framework say happens to that DNA?",
   choices=[
     "It integrates into the host genome and is transcribed and translated for the assembly of new viral progeny",
     "It remains separate from the host genome and is copied only by reverse transcriptase",
     "It is translated directly into viral proteins without being transcribed",
     "It is exported from the cell so that it can infect a neighboring cell",
     "It replaces the host's own genome entirely, so the host cell can no longer express its own genes"], ans=0,
   why="EK 6.4.A.4 states that this DNA integrates into the host genome and is transcribed and translated for the assembly of new viral progeny. The framework therefore has the viral DNA rejoin the ordinary flow of information rather than bypass it, and it says nothing about the host genome being replaced."),
 dict(q="A drug is developed that inhibits reverse transcriptase in cells infected by a retrovirus. Which step is blocked first?",
   choices=[
     "The copying of the viral RNA genome into DNA",
     "The integration of viral DNA into the host genome, which occurs before any copying",
     "The translation of viral mRNA into viral proteins on host ribosomes",
     "The transcription of the host's own genes, which the virus depends on",
     "The release of the newly synthesized viral proteins from the ribosome"], ans=0,
   why="EK 6.4.A.4 makes reverse transcriptase the enzyme that copies the viral RNA genome into DNA, and puts integration into the host genome after that copying. Inhibiting the enzyme therefore blocks the copying step, and everything the same statement places downstream, integration, transcription and translation, follows from it."),
 dict(q="A single tRNA in a cell is altered so that it delivers the wrong amino acid while its anticodon is unchanged. What effect is expected on the polypeptides made?",
   choices=[
     "The wrong amino acid is inserted wherever the codon that tRNA reads occurs",
     "No amino acid is inserted at all, so every polypeptide ends at that codon",
     "The ribosome reads the mRNA in a different set of triplets from that point on",
     "Translation cannot be initiated, because the start codon is no longer recognized",
     "The mRNA is degraded before translation can begin"], ans=0,
   why="EK 6.4.A.3.v has tRNA bring the correct amino acid to the place specified by the codon, and EK 6.4.A.3.vi transfers that amino acid to the growing chain. With the anticodon unchanged the tRNA still arrives at the same codon under EK 6.3.A.1.ii, so what changes is which residue is added there. Ending the chain would require a stop codon under EK 6.4.A.3.vii."),
 dict(q="A change to an mRNA introduces a stop codon in the middle of the coding region. What does the ribosome do on reaching it?",
   choices=[
     "It stops there and releases a polypeptide shorter than the one usually made",
     "It reads through the stop codon and adds the amino acid the previous codon specified",
     "It returns to the start codon and begins the polypeptide again",
     "It waits until a tRNA arrives that can pair with the stop codon",
     "It continues to the usual stop codon, so the polypeptide is unchanged in length"], ans=0,
   why="EK 6.4.A.3.vii states that the process continues along the mRNA until a stop codon is reached, and EK 6.4.A.3.viii terminates translation with the release of the newly synthesized protein. The ribosome responds to the first stop codon it meets, so a stop codon reached early releases a shorter product."),
 dict(q="Which sequence of events matches the framework's account of translation?",
   choices=[
     "The ribosome interacts with the mRNA at the start codon, tRNA delivers amino acids that are transferred to the chain, and a stop codon ends the process",
     "tRNA delivers amino acids to the chain, the ribosome then finds the start codon, and a stop codon ends the process",
     "A stop codon is reached first, the ribosome then interacts with the start codon, and tRNA delivers amino acids afterward",
     "The protein is released, the ribosome then interacts with the mRNA, and tRNA delivers amino acids last",
     "The mRNA is read backward from its far end until the start codon is reached"], ans=0,
   why="The order is the one EK 6.4.A.3 names, initiation then elongation then termination, filled in by its own substatements: initiation at the start codon in EK 6.4.A.3.i, delivery and transfer of amino acids in EK 6.4.A.3.v and vi, and a stop codon with release in EK 6.4.A.3.vii and viii."),
 dict(q="A eukaryotic cell makes a protein on ribosomes attached to the rough endoplasmic reticulum. Which surface of that organelle are those ribosomes on?",
   choices=[
     "The cytoplasmic surface",
     "The inner surface, facing the space enclosed by the organelle",
     "Both surfaces equally, since the organelle is symmetrical",
     "The surface facing the nucleus, so that mRNA does not have to travel",
     "Neither surface, since ribosomes are never attached to an organelle"], ans=0,
   why="EK 6.4.A.1 places translation on ribosomes in the cytoplasm of both kinds of cell, as well as the cytoplasmic surface of the rough endoplasmic reticulum of eukaryotic cells. The framework names that surface specifically rather than the enclosed side."),
 dict(q="A researcher transfers a human gene into a bacterium and the bacterium produces the human protein. Which framework statement accounts for this working at all?",
   choices=[
     "Nearly all living organisms use the same genetic code, so the bacterium reads the codons as the human cell would",
     "Bacteria carry the same alleles as humans, so the protein was already being made",
     "Bacterial ribosomes read DNA rather than mRNA, so no transcription is needed",
     "The genetic code of a bacterium changes to match whatever gene it receives",
     "Human genes contain no introns, so a bacterium can translate them directly"], ans=0,
   why="EK 6.4.A.3.iv states that nearly all living organisms use the same genetic code, which is why a codon means the same amino acid in both cells. EK 6.4.A.1 gives prokaryotes ribosomes that translate mRNA, and EK 6.3.A.4.iii puts introns in eukaryotic transcripts rather than removing them from human genes."),
 dict(q="Which statement correctly describes the relationship between a codon and an amino acid, as the framework states it?",
   choices=[
     "Each codon encodes a specific amino acid, and an amino acid may be encoded by several codons",
     "Each amino acid is encoded by a specific codon, and a codon may encode several amino acids",
     "Each codon encodes a specific amino acid, and each amino acid is encoded by exactly one codon",
     "Codons and amino acids are unrelated, since the amino acid is selected by the ribosome",
     "Each codon encodes three amino acids, one for each of its nucleotides"], ans=0,
   why="EK 6.4.A.3.iii states both halves: each codon encodes a specific amino acid, and many amino acids are encoded by more than one codon. The mapping is therefore unambiguous in the direction from codon to amino acid and not in the reverse direction, and EK 6.4.A.3.ii makes a codon three nucleotides specifying one residue."),
 dict(q="A prokaryotic cell and a eukaryotic cell each express a gene as a protein. Which difference between them does the framework state?",
   choices=[
     "In the prokaryote the mRNA is translated while it is still being transcribed, which the framework states for prokaryotic organisms only",
     "In the eukaryote the mRNA is translated while it is still being transcribed, which the framework states for eukaryotic cells only",
     "In the prokaryote translation occurs without ribosomes, while the eukaryote uses them",
     "In the eukaryote the ribosome reads the DNA directly, while the prokaryote uses an mRNA intermediate",
     "In the prokaryote the polypeptide is made before the mRNA, reversing the usual order"], ans=0,
   why="EK 6.4.A.2 states that in prokaryotic organisms translation of the mRNA occurs while it is being transcribed, and states it for those organisms. EK 6.4.A.1 gives both kinds of cell cytoplasmic ribosomes, so the difference is not the presence of the machinery but whether the two processes overlap in time."),
]
