# AP BIOLOGY 6.3 Transcription and RNA Processing
# CED effective Fall 2025, Unit 6 Gene Expression and Regulation. Big idea 3
# (Information Storage and Transmission). Learning objective 6.3.A, describe the
# mechanisms by which genetic information flows from DNA to RNA to protein.
# Suggested skill 2.B, explain relationships between characteristics of
# biological models in both theoretical and applied contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   6.3.A.1      The sequence of the RNA bases, TOGETHER WITH the structure of
#                the RNA molecule, determines RNA function.
#   6.3.A.1.i    Messenger RNA (mRNA) molecules carry information from DNA in
#                the nucleus to the ribosome in the cytoplasm.
#   6.3.A.1.ii   Distinct transfer RNA (tRNA) molecules bind specific amino
#                acids and have anticodon sequences that base pair with the
#                codons of mRNA. tRNA is recruited to the ribosome during
#                translation to generate the primary peptide sequence based on
#                the mRNA sequence.
#   6.3.A.1.iii  Ribosomal RNA (rRNA) molecules are functional building blocks
#                of ribosomes.
#   6.3.A.2      RNA polymerases use a SINGLE TEMPLATE STRAND of DNA to direct
#                the inclusion of bases in the newly formed RNA molecule. This
#                process is known as transcription.
#   6.3.A.3      The enzyme RNA polymerase synthesizes mRNA molecules in the
#                5 prime to 3 prime direction by READING the template DNA strand
#                in the 3 prime to 5 prime direction.
#   6.3.A.4      In EUKARYOTIC cells the mRNA transcript undergoes a series of
#                enzyme-mediated modifications.
#   6.3.A.4.i    The addition of a poly-A tail makes mRNA more STABLE.
#   6.3.A.4.ii   The addition of a GTP cap helps with RIBOSOMAL RECOGNITION.
#   6.3.A.4.iii  The excision of introns, along with the splicing and retention
#                of exons, generates different versions of the resulting mature
#                mRNA molecule. This process is known as alternative splicing.
#
# DIVISION OF LABOUR ACROSS 6.1 TO 6.4 is set out in the header of b6_1.py.
# 6.1 owns which base pairs with which, so no item here asks a student to write
# an RNA sequence from a DNA one. 6.2 owns the 5 prime to 3 prime direction as
# the direction DNA is SYNTHESIZED; here the direction appears in its other
# framework statement, EK 6.3.A.3, which is about the direction RNA polymerase
# READS ITS TEMPLATE while synthesizing. 6.4 owns every step of translation:
# tRNA appears in this topic as a MOLECULE -- what it binds and what its
# anticodon pairs with -- and in 6.4 as a PARTICIPANT in the elongation cycle.
#
# ON FIGURES. No stem refers to a gel, a diagram of a gene or a splicing map.
# The splicing data are delivered as a table of segment lengths.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX.
TOPIC = ("6.3", "Transcription and RNA Processing", 6)

# The segments of one primary transcript, in the order they occur.
_T_SPLICE = dict(
    headers=["Segment of the primary transcript", "Length in nucleotides"],
    rows=[["Exon 1", "120"],
          ["Intron 1", "350"],
          ["Exon 2", "240"],
          ["Intron 2", "500"],
          ["Exon 3", "180"]])

# Three mature mRNA molecules recovered from one gene with four exons.
_T_ALT = dict(
    headers=["Mature mRNA version recovered", "Exons retained in that version"],
    rows=[["Version 1", "Exons 1, 2, 3 and 4"],
          ["Version 2", "Exons 1, 2 and 4"],
          ["Version 3", "Exons 1, 3 and 4"]])

# Two otherwise identical mRNA preparations, one with a poly-A tail added.
_T_TAIL = dict(
    headers=["mRNA preparation", "Poly-A tail present",
             "Percent of the mRNA still intact after four hours"],
    rows=[["Preparation 1", "Yes", "78"],
          ["Preparation 2", "No", "9"]])

# Two otherwise identical mRNA preparations, one with a GTP cap added.
_T_CAP = dict(
    headers=["mRNA preparation", "GTP cap present",
             "Percent of transcripts bound by a ribosome within ten minutes"],
    rows=[["Preparation A", "Yes", "82"],
          ["Preparation B", "No", "11"]])

QUESTIONS = [
 dict(q="What is the function of a messenger RNA molecule in a eukaryotic cell?",
   choices=[
     "It carries information from DNA in the nucleus to the ribosome in the cytoplasm",
     "It binds a specific amino acid and delivers it according to an anticodon sequence",
     "It serves as a functional building block of the ribosome itself",
     "It unwinds the DNA so that the template strand can be read",
     "It joins the fragments of a newly made strand into one continuous molecule"], ans=0,
   why="EK 6.3.A.1.i states that messenger RNA molecules carry information from DNA in the nucleus to the ribosome in the cytoplasm. Binding an amino acid and carrying an anticodon is tRNA's role under EK 6.3.A.1.ii, and being a functional building block of the ribosome is rRNA's under EK 6.3.A.1.iii."),
 dict(q="What two things does a transfer RNA molecule do, according to the framework?",
   choices=[
     "It binds a specific amino acid and carries an anticodon sequence that base pairs with a codon of mRNA",
     "It binds a specific codon and carries an amino acid sequence that base pairs with an anticodon",
     "It binds a ribosome and carries the information copied from the DNA template strand",
     "It binds a specific amino acid and serves as a functional building block of the ribosome",
     "It binds the DNA template strand and directs the inclusion of bases in the new RNA molecule"], ans=0,
   why="EK 6.3.A.1.ii states that distinct tRNA molecules bind specific amino acids and have anticodon sequences that base pair with the codons of mRNA. The second option reverses the two, since a codon belongs to the mRNA and an amino acid is not a sequence that pairs with anything."),
 dict(q="What role do ribosomal RNA molecules play?",
   choices=[
     "They are functional building blocks of ribosomes",
     "They carry information from the nucleus to the ribosome",
     "They bind specific amino acids and deliver them to the ribosome",
     "They are the enzymes that add a poly-A tail to a transcript",
     "They serve as the template strand from which mRNA is copied"], ans=0,
   why="EK 6.3.A.1.iii states that ribosomal RNA molecules are functional building blocks of ribosomes. Carrying information belongs to mRNA under EK 6.3.A.1.i and binding amino acids to tRNA under EK 6.3.A.1.ii; the template is a strand of DNA under EK 6.3.A.2."),
 dict(q="The framework says that what an RNA molecule does is determined by more than its base sequence alone. What is the other determinant?",
   choices=[
     "The structure of the RNA molecule, which together with the sequence determines its function",
     "The number of bases in the molecule, which together with the sequence determines its function",
     "The cell in which the molecule is found, which determines its function regardless of sequence",
     "The DNA strand it was copied from, which continues to determine its function afterward",
     "The amino acid it is destined to encode, which determines its function in advance"], ans=0,
   why="EK 6.3.A.1 states that the sequence of the RNA bases, together with the structure of the RNA molecule, determines RNA function. Structure is the second term the framework names, which is why a tRNA and an mRNA of similar length can do entirely different jobs."),
 dict(q="During transcription, how much of the DNA does RNA polymerase use as a template?",
   choices=[
     "A single template strand, which directs the inclusion of bases in the new RNA molecule",
     "Both strands at once, so that two complementary RNA molecules are made",
     "Neither strand, since the new RNA is assembled from a pre-existing RNA copy",
     "A single template strand for the first half of the gene and the other strand for the second half",
     "Both strands in turn, first one and then the other, to check the sequence for errors"], ans=0,
   why="EK 6.3.A.2 states that RNA polymerases use a single template strand of DNA to direct the inclusion of bases in the newly formed RNA molecule, and names that process transcription. Using both strands would give two different RNA molecules from one gene, which is not what the framework describes."),
 dict(q="What is the name of the process in which RNA polymerase uses a strand of DNA to direct the inclusion of bases in a new RNA molecule?",
   choices=[
     "Transcription",
     "Translation",
     "Replication",
     "Splicing",
     "Recognition"], ans=0,
   why="EK 6.3.A.2 states that RNA polymerases use a single template strand of DNA to direct the inclusion of bases in the newly formed RNA molecule, and adds that this process is known as transcription. Splicing is the removal of introns under EK 6.3.A.4.iii, and translation is the making of a polypeptide under EK 6.4.A.3."),
 dict(q="In which direction does RNA polymerase synthesize an mRNA molecule, and in which direction does it read the template?",
   choices=[
     "It synthesizes in the 5 prime to 3 prime direction while reading the template in the 3 prime to 5 prime direction",
     "It synthesizes in the 3 prime to 5 prime direction while reading the template in the 5 prime to 3 prime direction",
     "It synthesizes and reads in the same direction, both 5 prime to 3 prime",
     "It synthesizes and reads in the same direction, both 3 prime to 5 prime",
     "It synthesizes in whichever direction the gene is oriented and reads in the other"], ans=0,
   why="EK 6.3.A.3 states that the enzyme RNA polymerase synthesizes mRNA molecules in the 5 prime to 3 prime direction by reading the template DNA strand in the 3 prime to 5 prime direction. The two directions are opposite, which is why neither of the same-direction options can be right."),
 dict(q="A researcher identifies the end of the template DNA strand at which RNA polymerase begins reading. Which end is it?",
   choices=[
     "The 3 prime end, because the template is read in the 3 prime to 5 prime direction",
     "The 5 prime end, because the template is read in the 5 prime to 3 prime direction",
     "The 3 prime end, because the new RNA is built in the 3 prime to 5 prime direction",
     "Either end, because the polymerase can read a template in either direction",
     "Neither end, because the polymerase begins in the middle of the template and works outward"], ans=0,
   why="EK 6.3.A.3 states that RNA polymerase reads the template DNA strand in the 3 prime to 5 prime direction, so reading begins at the end that direction starts from. The same statement gives the new RNA the opposite direction, 5 prime to 3 prime, so the direction of synthesis cannot be used to locate the starting end of the template."),
 dict(q="What does the addition of a poly-A tail do for an mRNA transcript in a eukaryotic cell?",
   choices=[
     "It makes the mRNA more stable",
     "It helps the ribosome recognize the mRNA",
     "It removes the introns from the mRNA",
     "It provides the start codon at which translation begins",
     "It attaches the amino acid that the transcript encodes"], ans=0,
   why="EK 6.3.A.4.i states that the addition of a poly-A tail makes mRNA more stable. Helping with ribosomal recognition is what EK 6.3.A.4.ii assigns to the GTP cap, and intron excision is the separate modification of EK 6.3.A.4.iii."),
 dict(q="What does the addition of a GTP cap do for an mRNA transcript in a eukaryotic cell?",
   choices=[
     "It helps with ribosomal recognition of the transcript",
     "It makes the transcript more stable against being broken down",
     "It marks the introns so that they can be excised",
     "It joins the retained exons to one another",
     "It carries the transcript out of the nucleus by binding a transport protein"], ans=0,
   why="EK 6.3.A.4.ii states that the addition of a GTP cap helps with ribosomal recognition. Increasing stability is what EK 6.3.A.4.i assigns to the poly-A tail, and excision and splicing are the separate modification of EK 6.3.A.4.iii."),
 dict(q="What happens to the introns and the exons of a eukaryotic primary transcript?",
   choices=[
     "The introns are excised and the exons are spliced together and retained",
     "The exons are excised and the introns are spliced together and retained",
     "Both the introns and the exons are retained, and the ribosome ignores the introns",
     "Both the introns and the exons are excised, and the remaining sequence is translated",
     "The introns are excised and the exons are excised in the alternate transcript"], ans=0,
   why="EK 6.3.A.4.iii states that the excision of introns, along with the splicing and retention of exons, generates different versions of the mature mRNA molecule. The framework therefore removes the introns and keeps the exons, which is the reverse of the second option."),
 dict(q="Why can one eukaryotic gene give rise to more than one version of a mature mRNA molecule?",
   choices=[
     "Different combinations of exons can be retained when the introns are excised, a process called alternative splicing",
     "Different template strands can be used for the same gene, one giving each version",
     "Different RNA polymerases read the gene in opposite directions, giving two versions",
     "Different poly-A tails of different lengths change which bases the transcript contains",
     "Different ribosomes recognize the transcript and edit its sequence after it arrives"], ans=0,
   why="EK 6.3.A.4.iii states that the excision of introns along with the splicing and retention of exons generates different versions of the resulting mature mRNA molecule, and names the process alternative splicing. EK 6.3.A.2 gives transcription a single template strand, so no second version can come from the other strand."),
 dict(q="The table lists the segments of one eukaryotic primary transcript in the order in which they occur. How long is the mature mRNA after the introns are excised and the exons are spliced together?",
   table=_T_SPLICE,
   choices=[
     "540 nucleotides",
     "850 nucleotides",
     "1390 nucleotides",
     "310 nucleotides",
     "1080 nucleotides"], ans=0,
   why="EK 6.3.A.4.iii excises the introns and retains the spliced exons, so the mature molecule is the sum of the exon lengths only. Adding 120, 240 and 180 gives 540; 850 is the total of the two introns and 1390 is the whole primary transcript."),
 dict(q="Using the same primary transcript, how many nucleotides are removed from it during processing of this kind?",
   table=_T_SPLICE,
   choices=[
     "850 nucleotides, the total length of the introns",
     "540 nucleotides, the total length of the exons",
     "1390 nucleotides, the total length of the transcript",
     "500 nucleotides, the length of the longer intron only",
     "None, because processing rearranges the transcript without removing any part of it"], ans=0,
   why="EK 6.3.A.4.iii states that the introns are excised while the exons are spliced and retained, so what is removed is the intron total. The two introns are 350 and 500 nucleotides, which sum to 850; the exon total is what remains rather than what is lost."),
 dict(q="Three different mature mRNA molecules were recovered from one gene, as reported in the table. Which process accounts for this result, and which exons appear in every version?",
   table=_T_ALT,
   choices=[
     "Alternative splicing, and the first and fourth exons appear in every version",
     "Alternative splicing, and the second and third exons appear in every version",
     "Transcription from two different template strands, and no exon appears in every version",
     "Replication of the gene into three copies, each of which is transcribed differently",
     "Addition of poly-A tails of three different lengths to a single mature transcript"], ans=0,
   why="EK 6.3.A.4.iii states that the excision of introns along with the splicing and retention of exons generates different versions of the resulting mature mRNA molecule, and names that alternative splicing. Reading the table, the exons numbered one and four are listed in all three versions while the second and third are each missing from one."),
 dict(q="Two otherwise identical mRNA preparations were compared, as reported in the table. What does the comparison show?",
   table=_T_TAIL,
   choices=[
     "The preparation carrying a poly-A tail survived far better, which is the stability the tail confers",
     "The preparation carrying a poly-A tail survived far worse, so the tail marks the transcript for breakdown",
     "The two preparations survived equally well, so the poly-A tail has no measurable effect",
     "The poly-A tail improved ribosome binding rather than survival, which is what the table measures",
     "The poly-A tail removed the introns, which is why more of that preparation remained intact"], ans=0,
   why="EK 6.3.A.4.i states that the addition of a poly-A tail makes mRNA more stable. The preparation with the tail retained 78 percent after four hours against 9 percent without it, which is a large difference in the direction the framework predicts; the table measures intact mRNA rather than ribosome binding."),
 dict(q="Two further mRNA preparations were compared, as reported in the table. What does the comparison show?",
   table=_T_CAP,
   choices=[
     "The preparation carrying a GTP cap was bound by ribosomes far more often, which is the recognition the cap assists",
     "The preparation carrying a GTP cap was bound by ribosomes far less often, so the cap blocks ribosomes",
     "The two preparations were bound equally often, so the GTP cap has no measurable effect",
     "The GTP cap made the transcripts more stable rather than easier to recognize, which is what the table measures",
     "The GTP cap spliced the exons together, which is why ribosomes could bind that preparation"], ans=0,
   why="EK 6.3.A.4.ii states that the addition of a GTP cap helps with ribosomal recognition. The capped preparation was bound by a ribosome in 82 percent of transcripts against 11 percent uncapped, which is the effect the framework predicts; the table measures binding rather than survival, which is the poly-A tail's contribution under EK 6.3.A.4.i."),
 dict(q="In which kind of cell does the framework place the series of enzyme-mediated modifications of the mRNA transcript?",
   choices=[
     "In eukaryotic cells",
     "In prokaryotic cells",
     "In both kinds of cell equally, since every transcript is modified",
     "In neither, since modification happens only in viruses",
     "In whichever kind of cell lacks a nucleus, so that the transcript is protected"], ans=0,
   why="EK 6.3.A.4 opens by stating that in eukaryotic cells the mRNA transcript undergoes a series of enzyme-mediated modifications, and the three modifications listed under it are given for that setting. EK 6.3.A.1.i also locates the eukaryotic transcript's journey from a nucleus, which prokaryotic cells do not have."),
 dict(q="A cell is treated so that it can no longer add poly-A tails to its transcripts, while every other step continues. What is the expected consequence?",
   choices=[
     "The transcripts are broken down sooner, because the modification that makes them more stable is missing",
     "The transcripts are never recognized by ribosomes, because the tail is what ribosomes bind",
     "The introns are retained in the transcripts, because the tail is what triggers their excision",
     "The transcripts are never exported, because transcription itself cannot be completed",
     "The transcripts become more stable, because a shorter molecule is harder to break down"], ans=0,
   why="EK 6.3.A.4.i states that the addition of a poly-A tail makes mRNA more stable, so removing that modification removes the stability it confers. Ribosomal recognition is the GTP cap's contribution under EK 6.3.A.4.ii and intron excision is a separate modification under EK 6.3.A.4.iii."),
 dict(q="A cell is treated so that it can no longer add a GTP cap to its transcripts, while every other step continues. What is the expected consequence?",
   choices=[
     "Ribosomes recognize the transcripts less readily, because the modification that assists recognition is missing",
     "The transcripts are broken down almost immediately, because the cap is what makes them stable",
     "The introns are retained, because the cap marks the boundaries between introns and exons",
     "RNA polymerase reads the template in the wrong direction, because the cap sets the direction",
     "The transcripts acquire two poly-A tails instead of one, compensating for the missing cap"], ans=0,
   why="EK 6.3.A.4.ii states that the addition of a GTP cap helps with ribosomal recognition, so its absence impairs recognition. Stability is what EK 6.3.A.4.i assigns to the poly-A tail, and the direction of reading is fixed by EK 6.3.A.3 and unrelated to processing."),
 dict(q="A defect in a cell leaves one intron in place in an otherwise mature mRNA. Which step of processing has failed?",
   choices=[
     "The excision of that intron, which the framework pairs with the splicing and retention of the exons",
     "The addition of the poly-A tail, which is what marks introns for removal",
     "The addition of the GTP cap, which is what holds the exons in register",
     "The reading of the template strand, which determines which segments are introns",
     "The recruitment of tRNA, which normally removes the intron before translation"], ans=0,
   why="EK 6.3.A.4.iii names the excision of introns, along with the splicing and retention of exons, as the modification that generates the mature mRNA. A retained intron is a failure of that excision. The tail and the cap have the separate roles given in EK 6.3.A.4.i and EK 6.3.A.4.ii, and tRNA's role under EK 6.3.A.1.ii is at the ribosome."),
 dict(q="A mutation changes the anticodon sequence of one kind of tRNA molecule while leaving the amino acid it binds unchanged. Which framework statement identifies what has been disrupted?",
   choices=[
     "That tRNA anticodon sequences base pair with the codons of mRNA, so the tRNA will now pair with a different codon",
     "That tRNA molecules are functional building blocks of ribosomes, so the ribosome will not assemble",
     "That mRNA carries information from the nucleus to the cytoplasm, so the message will not arrive",
     "That RNA polymerase reads a single template strand, so transcription of that tRNA will fail",
     "That a GTP cap assists ribosomal recognition, so the tRNA will not be recognized"], ans=0,
   why="EK 6.3.A.1.ii states that distinct tRNA molecules bind specific amino acids and have anticodon sequences that base pair with the codons of mRNA. Changing the anticodon changes which codon the molecule pairs with while leaving the attached amino acid as it was, so the pairing relationship is what has been broken."),
 dict(q="A cell can no longer make ribosomal RNA. Which structure is most directly affected?",
   choices=[
     "The ribosome, of which ribosomal RNA molecules are functional building blocks",
     "The nucleus, from which messenger RNA departs",
     "The template strand of DNA, which ribosomal RNA normally stabilizes",
     "The poly-A tail, which is assembled from ribosomal RNA",
     "The anticodon of each transfer RNA, which ribosomal RNA supplies"], ans=0,
   why="EK 6.3.A.1.iii states that ribosomal RNA molecules are functional building blocks of ribosomes, so losing them affects the structure they build. The anticodon belongs to tRNA under EK 6.3.A.1.ii, and neither the DNA template of EK 6.3.A.2 nor the poly-A tail of EK 6.3.A.4.i is made of rRNA."),
 dict(q="What distinguishes transcription from the copying of DNA described in the previous topic?",
   choices=[
     "Transcription copies one template strand into an RNA molecule, while copying DNA uses both original strands as templates",
     "Transcription copies both strands into RNA, while copying DNA uses only one of them",
     "Transcription proceeds in the 3 prime to 5 prime direction, while copying DNA proceeds in the 5 prime to 3 prime direction",
     "Transcription requires no template at all, while copying DNA requires one",
     "Transcription produces two molecules from one, while copying DNA produces one molecule from two"], ans=0,
   why="EK 6.3.A.2 states that RNA polymerases use a single template strand of DNA in transcription, whereas EK 6.2.A.1.ii makes replication semiconservative, with each of the two original strands templating a new complementary strand. Both processes build their new molecule in the 5 prime to 3 prime direction under EK 6.3.A.3 and EK 6.2.A.1.i."),
 dict(q="Which comparison of the three kinds of RNA is consistent with the framework?",
   choices=[
     "Messenger RNA carries the information, transfer RNA brings amino acids according to its anticodon, and ribosomal RNA builds the ribosome",
     "Messenger RNA builds the ribosome, transfer RNA carries the information, and ribosomal RNA brings amino acids",
     "Messenger RNA brings amino acids, transfer RNA builds the ribosome, and ribosomal RNA carries the information",
     "All three carry information from the nucleus, and they differ only in length",
     "All three build the ribosome, and they differ only in which part of it they form"], ans=0,
   why="The three roles are stated separately: EK 6.3.A.1.i gives mRNA the carrying of information from DNA in the nucleus to the ribosome, EK 6.3.A.1.ii gives tRNA the binding of specific amino acids and an anticodon that pairs with mRNA codons, and EK 6.3.A.1.iii makes rRNA a functional building block of ribosomes."),
 dict(q="A tRNA molecule and an mRNA molecule of similar length behave completely differently in a cell. Which framework statement best accounts for that?",
   choices=[
     "The sequence of the RNA bases, together with the structure of the molecule, determines RNA function",
     "The length of an RNA molecule determines its function, so molecules of the same length behave alike",
     "The cell decides each molecule's function after it has been made, independently of the molecule itself",
     "Function is determined by which template strand the molecule was copied from",
     "Function is determined by whether the molecule received a poly-A tail, which is the only difference between them"], ans=0,
   why="EK 6.3.A.1 states that the sequence of the RNA bases, together with the structure of the RNA molecule, determines RNA function. Length is not among the determinants the framework names, which is exactly why two molecules of similar length can behave differently."),
 dict(q="Where does a eukaryotic mRNA molecule begin its journey and where does it end it, according to the framework?",
   choices=[
     "It begins at the DNA in the nucleus and ends at the ribosome in the cytoplasm",
     "It begins at the ribosome in the cytoplasm and ends at the DNA in the nucleus",
     "It begins and ends within the nucleus, where the ribosome is located",
     "It begins and ends within the cytoplasm, where the DNA is located",
     "It begins at a transfer RNA molecule and ends at the DNA template strand"], ans=0,
   why="EK 6.3.A.1.i states that messenger RNA molecules carry information from DNA in the nucleus to the ribosome in the cytoplasm. The direction of that journey is part of the statement, and it places the DNA in the nucleus and the ribosome in the cytoplasm."),
 dict(q="Which sequence of events is consistent with the framework's account of a eukaryotic gene being expressed as far as the ribosome?",
   choices=[
     "RNA polymerase copies a template strand, the transcript is capped, tailed and spliced, and the mature mRNA reaches a ribosome",
     "The transcript is capped and spliced, RNA polymerase then copies it from a template strand, and the mature mRNA reaches a ribosome",
     "The mature mRNA reaches a ribosome, RNA polymerase then copies a template strand, and the transcript is spliced afterward",
     "RNA polymerase copies both DNA strands, the two transcripts are joined, and the joined molecule reaches a ribosome",
     "A ribosome copies the template strand directly, so no separate transcript is made"], ans=0,
   why="The order follows from the statements themselves: EK 6.3.A.2 makes transcription the copying of a single template strand into a new RNA molecule, EK 6.3.A.4 then applies the modifications to that transcript, and EK 6.3.A.1.i has the resulting mRNA carry the information to the ribosome. Nothing can be modified before it exists."),
 dict(q="A biologist finds that a particular protein is made in two slightly different forms in different tissues, and that both are encoded by the same gene. Which mechanism described in this topic accounts for that?",
   choices=[
     "Alternative splicing, which generates different versions of the mature mRNA from one transcript",
     "Transcription from the opposite template strand in one of the two tissues",
     "The addition of a longer poly-A tail in one of the two tissues",
     "The addition of a second GTP cap in one of the two tissues",
     "Duplication of the gene, so that each tissue carries its own copy"], ans=0,
   why="EK 6.3.A.4.iii states that the excision of introns along with the splicing and retention of exons generates different versions of the resulting mature mRNA molecule, and names it alternative splicing. EK 6.3.A.2 gives transcription one template strand, and neither the tail nor the cap changes which bases the mature transcript contains."),
 dict(q="An investigator wants to know which of the two strands of a gene RNA polymerase used in a particular round of transcription. What does the framework allow the investigator to assume?",
   choices=[
     "That a single strand served as the template and directed which bases were included in the RNA",
     "That both strands served as templates and the two products were later joined",
     "That the strand used was chosen at random and changes between rounds of transcription",
     "That no strand served as a template, since the polymerase carries the sequence itself",
     "That the template strand was read in the 5 prime to 3 prime direction, which identifies it"], ans=0,
   why="EK 6.3.A.2 states that RNA polymerases use a single template strand of DNA to direct the inclusion of bases in the newly formed RNA molecule. EK 6.3.A.3 adds that this template is read in the 3 prime to 5 prime direction, so the option naming the opposite reading direction misstates the framework."),
]
