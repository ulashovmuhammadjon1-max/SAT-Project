# AP BIOLOGY 6.5 Regulation of Gene Expression
# CED effective Fall 2025, Unit 6 Gene Expression and Regulation. Big idea 3
# (Information Storage and Transmission). Learning objectives 6.5.A, describe
# the types of interactions that regulate gene expression, and 6.5.B, explain
# how the location of regulatory sequences relates to their function. Suggested
# skill 6.A, make a scientific claim.
#
# Essential knowledge relied on, in the framework's own words:
#   6.5.A.1     Regulatory sequences are stretches of DNA that interact with
#               regulatory proteins to control transcription. Some genes are
#               CONSTITUTIVELY EXPRESSED, and others are INDUCIBLE.
#   6.5.A.2     Epigenetic changes can affect gene expression through REVERSIBLE
#               modifications of DNA or histones.
#   6.5.A.3     The phenotype of a cell or an organism is determined by the
#               COMBINATION of genes that are expressed AND THE LEVELS at which
#               they are expressed.
#   6.5.A.3.i   Observable cell differentiation results from the expression of
#               genes for TISSUE-SPECIFIC proteins.
#   6.5.A.3.ii  Induction of transcription factors during development results in
#               SEQUENTIAL gene expression.
#   6.5.A.3.iii The function and amount of gene products determine the phenotype
#               of organisms.
#   6.5.B.1     Both prokaryotes and eukaryotes have groups of genes that are
#               COORDINATELY REGULATED.
#   6.5.B.1.i   Prokaryotes regulate operons in an inducible or repressible
#               system.
#   6.5.B.1.ii  In eukaryotes, groups of genes may be influenced by the same
#               transcription factors to coordinately regulate expression.
#
# DIVISION OF LABOUR WITH 6.6, planned before either was written because the two
# topics are one subject cut in half by the CED:
#   6.5  WHAT regulation is and WHAT it produces -- regulatory sequences and
#        regulatory proteins in general, constitutive against inducible,
#        epigenetic modification and its reversibility, phenotype as the
#        combination and the levels of expression, differentiation, sequential
#        induction during development, operons, and coordinate regulation.
#   6.6  WHERE the sequences sit and WHICH molecules act on them -- promoter and
#        enhancer sequences upstream or downstream of the transcription start
#        site, negative regulatory molecules that block transcription by binding
#        DNA, differential expression as the source of differences in cell
#        products and functions, and small regulatory RNA molecules.
# Transcription factors are named in both, and deliberately: here they appear as
# the inducing agents of EK 6.5.A.3.ii and the shared agents of EK 6.5.B.1.ii,
# and in 6.6 as molecules binding a promoter or enhancer under EK 6.6.A.1. No
# item in either topic asks the other's question.
#
# 5.5 owns the environment's effect on expression; no item here is about
# environmental conditions producing different phenotypes from one genotype.
#
# ON FIGURES. No stem refers to a diagram of an operon or a gel. Every data set
# is a table=.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX.
TOPIC = ("6.5", "Regulation of Gene Expression", 6)

# Three genes of one bacterium, measured with and without a particular sugar.
_T_EXPR = dict(
    headers=["Gene", "Expression with the sugar absent (arbitrary units)",
             "Expression with the sugar present (arbitrary units)"],
    rows=[["Gene 1", "100", "98"],
          ["Gene 2", "3", "240"],
          ["Gene 3", "4", "5"]])

# One gene followed through a chemical treatment and its withdrawal.
_T_EPI = dict(
    headers=["Condition of the cell sample", "Level of the histone modification",
             "Expression of the gene (arbitrary units)"],
    rows=[["Before treatment", "Low", "180"],
          ["During treatment", "High", "12"],
          ["After the treatment is withdrawn", "Low", "175"]])

# Three proteins sought in three kinds of cell from one organism.
_T_TISSUE = dict(
    headers=["Protein", "Detected in liver cells", "Detected in muscle cells",
             "Detected in nerve cells"],
    rows=[["Protein Q", "Yes", "No", "No"],
          ["Protein R", "No", "Yes", "No"],
          ["Protein S", "Yes", "Yes", "Yes"]])

# One embryo followed through three developmental stages.
_T_DEV = dict(
    headers=["Developmental stage", "Transcription factor 1 present",
             "Gene A expressed", "Gene B expressed"],
    rows=[["Stage 1", "No", "No", "No"],
          ["Stage 2", "Yes", "Yes", "No"],
          ["Stage 3", "Yes", "Yes", "Yes"]])

# Three individuals carrying the same gene but making different amounts of it.
_T_AMOUNT = dict(
    headers=["Individual", "Amount of the enzyme produced (percent of the typical amount)",
             "Observed phenotype"],
    rows=[["Individual 1", "100", "Typical pigment"],
          ["Individual 2", "45", "Reduced pigment"],
          ["Individual 3", "5", "Almost no pigment"]])

# A group of bacterial genes measured with and without a nutrient they process.
_T_OPERON_I = dict(
    headers=["Condition of the culture",
             "Transcription of the group of genes (arbitrary units)"],
    rows=[["The nutrient the genes process is absent", "2"],
          ["The nutrient the genes process is present", "190"]])

# A second group of bacterial genes measured against the abundance of what they make.
_T_OPERON_R = dict(
    headers=["Condition of the culture",
             "Transcription of the group of genes (arbitrary units)"],
    rows=[["The product the genes make is scarce", "210"],
          ["The product the genes make is abundant", "6"]])

# Four eukaryotic genes measured before and after one signal.
_T_COORD = dict(
    headers=["Gene", "Expression before the signal (arbitrary units)",
             "Expression two hours after the signal (arbitrary units)"],
    rows=[["Gene W", "10", "95"],
          ["Gene X", "12", "102"],
          ["Gene Y", "9", "88"],
          ["Gene Z", "40", "41"]])

QUESTIONS = [
 dict(q="What is a regulatory sequence, and what does it do?",
   choices=[
     "A stretch of DNA that interacts with regulatory proteins to control transcription",
     "A stretch of RNA that interacts with regulatory proteins to control transcription",
     "A protein that binds a stretch of DNA and is itself transcribed into RNA",
     "A stretch of DNA that is translated into a regulatory protein",
     "A stretch of DNA that replaces a gene when that gene is not needed"], ans=0,
   why="EK 6.5.A.1 states that regulatory sequences are stretches of DNA that interact with regulatory proteins to control transcription. The sequence is the DNA and the regulatory protein is what interacts with it, so the options that make the sequence RNA, a protein, or something translated all reverse part of that definition."),
 dict(q="What is the difference between a gene that is constitutively expressed and one that is inducible?",
   choices=[
     "A constitutively expressed gene is expressed continually, while an inducible gene is expressed when it is turned on",
     "A constitutively expressed gene is expressed when it is turned on, while an inducible gene is expressed continually",
     "A constitutively expressed gene is present in every cell, while an inducible gene is present in only some cells",
     "A constitutively expressed gene has a regulatory sequence, while an inducible gene has none",
     "A constitutively expressed gene is found in prokaryotes and an inducible gene in eukaryotes"], ans=0,
   why="EK 6.5.A.1 states that some genes are constitutively expressed and others are inducible, which is a distinction between being expressed all the time and being switched on. Every cell of an organism carries the same genes, so presence is not what separates them, and EK 6.5.B.1 gives regulated groups of genes to prokaryotes and eukaryotes alike."),
 dict(q="A bacterium makes an enzyme for breaking down a particular sugar only when that sugar is available in its surroundings. How is the gene for that enzyme best described?",
   choices=[
     "Inducible, because its expression is switched on under a particular condition",
     "Constitutively expressed, because the bacterium retains the gene at all times",
     "A regulatory sequence, because its expression depends on a signal",
     "Epigenetically modified, because its expression changes during the bacterium's life",
     "Absent from the genome until the sugar appears, at which point it is acquired"], ans=0,
   why="EK 6.5.A.1 distinguishes genes that are constitutively expressed from those that are inducible, and a gene expressed only under a particular condition is the second kind. Retaining a gene is not the same as expressing it, and a regulatory sequence under the same statement is a stretch of DNA rather than a gene's expression pattern."),
 dict(q="A gene encoding a protein that every cell needs at all times is transcribed at a steady rate under every condition tested. How is this gene best described?",
   choices=[
     "Constitutively expressed, because its transcription does not depend on a particular condition",
     "Inducible, because its steady transcription must be switched on by a signal",
     "Repressible, because nothing has yet switched it off",
     "Coordinately regulated, because it is transcribed in every cell of the organism",
     "Epigenetic, because its expression level is a property of the cell rather than of the sequence"], ans=0,
   why="EK 6.5.A.1 states that some genes are constitutively expressed and others are inducible; a gene transcribed at a steady rate whatever the conditions is the constitutive case. Coordinate regulation under EK 6.5.B.1 concerns groups of genes regulated together rather than a gene expressed in every cell."),
 dict(q="The table reports the expression of three bacterial genes measured with and without a particular sugar. Which gene is constitutively expressed?",
   table=_T_EXPR,
   choices=[
     "Gene 1, which is expressed at a high level whether or not the sugar is present",
     "Gene 2, which is expressed at a high level only when the sugar is present",
     "Gene 3, which is expressed at a low level whether or not the sugar is present",
     "Gene 2 and gene 3 together, since both respond to the sugar",
     "None of them, because expression cannot be constitutive in a bacterium"], ans=0,
   why="EK 6.5.A.1 makes a constitutively expressed gene one whose expression does not depend on the condition. Only the gene reading 100 and 98 units is both substantially expressed and unchanged by the sugar; the gene reading 3 and 240 units is switched on by it and the gene reading 4 and 5 units is barely expressed at all."),
 dict(q="Using the same measurements, which gene is inducible with respect to this sugar?",
   table=_T_EXPR,
   choices=[
     "Gene 2, whose expression rises many times over when the sugar is present",
     "Gene 1, whose expression stays near 100 units under both conditions",
     "Gene 3, whose expression stays near 5 units under both conditions",
     "Gene 1 and gene 3 together, since neither changes with the sugar",
     "All three genes, since all three are transcribed under both conditions"], ans=0,
   why="EK 6.5.A.1 makes an inducible gene one whose expression is switched on. The gene reading 3 units without the sugar and 240 with it changes by a factor of about eighty, while the other two change by a few units at most, which is the pattern of a gene whose expression does not depend on this condition."),
 dict(q="What are epigenetic changes, according to the framework?",
   choices=[
     "Reversible modifications of DNA or histones that can affect gene expression",
     "Permanent alterations to the sequence of bases in DNA that change gene expression",
     "Modifications of the mRNA transcript that occur after transcription",
     "Changes in the number of chromosomes a cell carries",
     "Changes in which alleles a gene has, brought about by the environment"], ans=0,
   why="EK 6.5.A.2 states that epigenetic changes can affect gene expression through reversible modifications of DNA or histones. Reversibility is the framework's own word, and it is what distinguishes such a change from the alteration of a DNA sequence that EK 6.7.A.1 calls a mutation."),
 dict(q="The table follows one gene through a chemical treatment and its withdrawal. Which claim do these data best support?",
   table=_T_EPI,
   choices=[
     "The histone modification reduces expression of the gene, and its effect is reversible",
     "The histone modification raises expression of the gene, and its effect is reversible",
     "The histone modification reduces expression of the gene, and its effect is permanent",
     "The histone modification has no effect on expression, since the gene is expressed in every sample",
     "The treatment deleted the gene, which is why expression fell during it"], ans=0,
   why="EK 6.5.A.2 states that epigenetic changes affect gene expression through reversible modifications of DNA or histones. Expression falls from 180 to 12 units as the modification goes from low to high, which is a reduction, and returns to 175 units when the modification returns to low, which is what reversible means; a deleted gene could not be expressed again."),
 dict(q="What determines the phenotype of a cell or an organism, according to the framework?",
   choices=[
     "The combination of genes that are expressed and the levels at which they are expressed",
     "The combination of genes that are present in the genome, whether or not they are expressed",
     "The number of chromosomes the cell carries, regardless of which genes they hold",
     "The levels at which genes are expressed, with the particular genes involved making no difference",
     "The order in which the genes appear along the chromosome"], ans=0,
   why="EK 6.5.A.3 states that the phenotype of a cell or an organism is determined by the combination of genes that are expressed and the levels at which they are expressed. Both halves are stated, so an account resting on presence alone, or on levels alone, drops one of them."),
 dict(q="Two cells in one multicellular organism carry the same genome but have very different structures and functions. What accounts for the difference?",
   choices=[
     "The two cells express different combinations of their genes and at different levels",
     "The two cells carry different alleles, which arose after the organism was formed",
     "The two cells carry different numbers of chromosomes",
     "One cell has lost the genes it does not use, which is why it cannot make those products",
     "The two cells use different genetic codes to read the same genes"], ans=0,
   why="EK 6.5.A.3 makes the phenotype of a cell the product of the combination of genes expressed and the levels of expression, so cells sharing a genome can differ in exactly that way. EK 6.4.A.3.iv makes the genetic code shared across nearly all organisms, and nothing in the framework has a differentiated cell discard genes."),
 dict(q="What does the framework say produces observable cell differentiation?",
   choices=[
     "The expression of genes for tissue-specific proteins",
     "The loss of the genes that a differentiated cell does not need",
     "The addition of new genes acquired from neighboring cells",
     "A change in the genetic code used by each tissue",
     "The permanent alteration of the DNA sequence in each tissue"], ans=0,
   why="EK 6.5.A.3.i states that observable cell differentiation results from the expression of genes for tissue-specific proteins. The framework locates differentiation in what is expressed, not in genes being lost, added or rewritten."),
 dict(q="Three proteins were sought in three kinds of cell from one organism, as reported in the table. Which proteins are tissue-specific?",
   table=_T_TISSUE,
   choices=[
     "Protein Q and protein R, each detected in only one kind of cell",
     "Protein S alone, because it is detected in every kind of cell",
     "All three proteins, because each is detected in at least one kind of cell",
     "Protein Q alone, because it is the first protein listed in the table",
     "None of them, because a protein detected in any cell must be present in all of them"], ans=0,
   why="EK 6.5.A.3.i attributes observable cell differentiation to the expression of genes for tissue-specific proteins, so a tissue-specific protein is one confined to a particular kind of cell. Two of the three proteins are detected in exactly one cell type apiece and the third is detected in all three, which is what a protein common to every cell looks like."),
 dict(q="What does the framework say results from the induction of transcription factors during development?",
   choices=[
     "Sequential gene expression, in which genes come to be expressed one after another",
     "Simultaneous gene expression, in which every gene of the embryo is expressed at once",
     "The permanent silencing of every gene that a transcription factor does not bind",
     "The replication of the genome once for each transcription factor induced",
     "The removal of the introns from every transcript made in the embryo"], ans=0,
   why="EK 6.5.A.3.ii states that induction of transcription factors during development results in sequential gene expression. Intron removal is a processing step under EK 6.3.A.4.iii and replication is EK 6.2.A.1's subject, neither of which the induction of a transcription factor brings about."),
 dict(q="The table follows one embryo through three developmental stages. Which claim do these data best support?",
   table=_T_DEV,
   choices=[
     "The transcription factor appears first, and the two genes then come to be expressed one after the other",
     "The two genes are expressed first, and the transcription factor appears afterward",
     "The transcription factor and both genes appear together at a single stage",
     "The transcription factor prevents both genes from being expressed at any stage",
     "Neither gene is ever expressed, so no conclusion about sequence can be drawn"], ans=0,
   why="EK 6.5.A.3.ii states that induction of transcription factors during development results in sequential gene expression. In the table the factor is absent at the first stage, present with the first gene at the second, and present with both genes at the third, so the factor precedes the genes and the genes appear in order rather than together."),
 dict(q="Two individuals both carry a working copy of the same gene, but one makes far less of its product than the other and shows a milder version of the associated trait. Which framework statement accounts for this?",
   choices=[
     "The function and amount of gene products determine the phenotype of organisms",
     "The presence of a gene alone determines the phenotype of organisms",
     "The order of the genes along the chromosome determines the phenotype of organisms",
     "The number of copies of a chromosome determines the phenotype of organisms",
     "The genetic code used by the organism determines the phenotype of organisms"], ans=0,
   why="EK 6.5.A.3.iii states that the function and amount of gene products determine the phenotype of organisms, and EK 6.5.A.3 names the levels of expression alongside the combination of genes expressed. The amount is therefore part of what the framework says sets the phenotype, which presence alone cannot capture."),
 dict(q="The table reports the amount of one enzyme made by three individuals and the phenotype each shows. Which claim do these data best support?",
   table=_T_AMOUNT,
   choices=[
     "The amount of the gene product, and not merely whether it is made at all, corresponds to the phenotype",
     "Only whether the gene product is made at all corresponds to the phenotype, since all three individuals make some",
     "The amount of the gene product is unrelated to the phenotype in these individuals",
     "The individuals differ in the genetic code they use to make the enzyme",
     "The individual making the least enzyme shows the most pigment"], ans=0,
   why="EK 6.5.A.3.iii states that the function and amount of gene products determine the phenotype of organisms. All three individuals make some enzyme, so presence alone cannot separate them, while the recorded amounts of 100, 45 and 5 percent fall alongside pigment described as typical, reduced and almost absent."),
 dict(q="Which statement about groups of genes regulated together is consistent with the framework?",
   choices=[
     "Both prokaryotes and eukaryotes have groups of genes that are coordinately regulated",
     "Only prokaryotes have groups of genes that are coordinately regulated",
     "Only eukaryotes have groups of genes that are coordinately regulated",
     "Neither group regulates genes together, since each gene is controlled separately",
     "Coordinate regulation occurs only in genes that are constitutively expressed"], ans=0,
   why="EK 6.5.B.1 states that both prokaryotes and eukaryotes have groups of genes that are coordinately regulated, and its two substatements give each group its own mechanism: operons in prokaryotes under EK 6.5.B.1.i and shared transcription factors in eukaryotes under EK 6.5.B.1.ii."),
 dict(q="How does the framework describe the way prokaryotes regulate groups of genes?",
   choices=[
     "They regulate operons in an inducible or a repressible system",
     "They regulate operons by removing the genes they do not need",
     "They regulate each gene separately using its own transcription factor",
     "They regulate groups of genes by alternative splicing of a shared transcript",
     "They regulate operons only by epigenetic modification of histones"], ans=0,
   why="EK 6.5.B.1.i states that prokaryotes regulate operons in an inducible or repressible system. Alternative splicing is a processing step under EK 6.3.A.4.iii, and EK 6.5.B.1 makes coordinate regulation a matter of groups of genes rather than of separately controlled ones."),
 dict(q="A group of bacterial genes is transcribed only when the substance those genes break down is present in the medium. Which kind of system is this?",
   choices=[
     "An inducible system, because the presence of the substance switches transcription on",
     "A repressible system, because the presence of the substance switches transcription on",
     "An inducible system, because the absence of the substance switches transcription on",
     "A constitutive system, because the genes are transcribed under a defined condition",
     "An epigenetic system, because transcription changes without a change to the DNA sequence"], ans=0,
   why="EK 6.5.B.1.i states that prokaryotes regulate operons in an inducible or repressible system, and EK 6.5.A.1 defines an inducible gene as one whose expression is switched on. Transcription that appears when the substance appears is switched on by it; a repressible system is the opposite arrangement, in which a substance switches transcription off."),
 dict(q="A group of bacterial genes encoding the steps of a synthetic pathway is transcribed at a high rate when the pathway's end product is scarce and at a very low rate when it is abundant. Which kind of system is this?",
   choices=[
     "A repressible system, because abundance of the end product switches transcription off",
     "An inducible system, because abundance of the end product switches transcription off",
     "A repressible system, because abundance of the end product switches transcription on",
     "A constitutive system, because the genes are transcribed under both conditions",
     "A coordinately regulated system in a eukaryote, since only eukaryotes control pathways this way"], ans=0,
   why="EK 6.5.B.1.i names inducible and repressible systems as the two ways prokaryotes regulate operons. A system switched off by the abundance of a substance is the repressible one, and EK 6.5.B.1 gives operons to prokaryotes while assigning eukaryotes shared transcription factors under EK 6.5.B.1.ii."),
 dict(q="The table reports transcription of one group of bacterial genes under two conditions. Which kind of system do these data indicate?",
   table=_T_OPERON_I,
   choices=[
     "An inducible system, because transcription is far higher when the nutrient is present",
     "A repressible system, because transcription is far higher when the nutrient is present",
     "An inducible system, because transcription is far higher when the nutrient is absent",
     "A constitutive system, because transcription occurs under both conditions",
     "No regulation at all, because a difference of this size can arise by chance"], ans=0,
   why="EK 6.5.B.1.i names inducible and repressible systems for prokaryotic operons and EK 6.5.A.1 makes an inducible gene one that is switched on. Transcription of 2 units without the nutrient and 190 with it is a rise of about ninety times in the presence of the substance, which is induction rather than repression."),
 dict(q="The table reports transcription of a second group of bacterial genes under two conditions. Which kind of system do these data indicate?",
   table=_T_OPERON_R,
   choices=[
     "A repressible system, because transcription is far lower when the product is abundant",
     "An inducible system, because transcription is far lower when the product is abundant",
     "A repressible system, because transcription is far higher when the product is abundant",
     "A constitutive system, because transcription is measurable under both conditions",
     "An epigenetic system, because the change involves a modification of histones"], ans=0,
   why="EK 6.5.B.1.i names inducible and repressible systems for prokaryotic operons. Transcription of 210 units when the product is scarce and 6 when it is abundant is transcription switched off by the substance, which is the repressible arrangement. Epigenetic modification of histones under EK 6.5.A.2 is a different mechanism and is not what these data report."),
 dict(q="How does the framework describe coordinate regulation in eukaryotes?",
   choices=[
     "Groups of genes may be influenced by the same transcription factors, so their expression is regulated together",
     "Groups of genes are joined into a single operon, which is transcribed as one unit",
     "Groups of genes share one regulatory protein that removes them from the genome together",
     "Groups of genes are regulated by the order in which they lie along the chromosome",
     "Groups of genes are regulated only by reversible modification of the mRNA transcript"], ans=0,
   why="EK 6.5.B.1.ii states that in eukaryotes groups of genes may be influenced by the same transcription factors to coordinately regulate expression. Operons are the prokaryotic arrangement under EK 6.5.B.1.i, and EK 6.5.A.2 puts reversible modification on DNA or histones rather than on the transcript."),
 dict(q="The table reports the expression of four eukaryotic genes before and two hours after a single signal reaches the cell. Which claim do these data best support?",
   table=_T_COORD,
   choices=[
     "Three of the four genes rose together after the signal, which is the pattern of coordinate regulation",
     "All four genes rose together after the signal, which is the pattern of coordinate regulation",
     "Three of the four genes fell together after the signal, which is the pattern of coordinate regulation",
     "The four genes changed independently of one another, so none is coordinately regulated",
     "The gene whose expression did not change must be the one regulating the other three"], ans=0,
   why="EK 6.5.B.1 states that both prokaryotes and eukaryotes have groups of genes that are coordinately regulated, and EK 6.5.B.1.ii attributes the eukaryotic case to shared transcription factors. Three genes rise from about ten units to about ninety while the fourth moves from 40 to 41, so the group that moves together is three of the four rather than all of them."),
 dict(q="What distinguishes a regulatory sequence from the gene whose transcription it controls?",
   choices=[
     "The regulatory sequence is a stretch of DNA that regulatory proteins interact with, rather than the stretch that is transcribed into the product",
     "The regulatory sequence is a protein, while the gene is a stretch of DNA",
     "The regulatory sequence is transcribed into the same product as the gene it controls",
     "The regulatory sequence is made of RNA, while the gene is made of DNA",
     "There is no difference, since every stretch of DNA both regulates and is transcribed"], ans=0,
   why="EK 6.5.A.1 defines regulatory sequences as stretches of DNA that interact with regulatory proteins to control transcription, which makes them a target for proteins rather than the source of the transcribed product. Both are DNA, which is why the composition options are wrong."),
 dict(q="A change makes it impossible for a regulatory protein to interact with the regulatory sequence of a particular gene. What is the most direct expected consequence?",
   choices=[
     "The transcription of that gene is no longer controlled in the way the interaction provided",
     "The gene is removed from the chromosome, since it can no longer be regulated",
     "The gene is transcribed into a protein directly, without an RNA intermediate",
     "The genetic code used to read that gene changes",
     "Every gene in the genome stops being transcribed"], ans=0,
   why="EK 6.5.A.1 states that regulatory sequences are stretches of DNA that interact with regulatory proteins to control transcription, so the interaction is what supplies the control. Losing it removes that control over the gene concerned; nothing in the framework makes an unregulated gene leave the chromosome or changes the code of EK 6.4.A.3.iv."),
 dict(q="An investigator claims that a newly discovered chemical acts epigenetically on a gene. Which finding would best support that claim?",
   choices=[
     "Expression of the gene falls while the chemical is applied and returns when it is withdrawn, with the modification of histones tracking the change",
     "Expression of the gene falls while the chemical is applied and never returns after it is withdrawn",
     "The base sequence of the gene is different in every treated cell",
     "The chemical increases the number of chromosomes in the treated cells",
     "The chemical prevents the cell from dividing while it is applied"], ans=0,
   why="Suggested skill 6.A asks for a scientific claim, and EK 6.5.A.2 states that epigenetic changes affect gene expression through reversible modifications of DNA or histones. The supporting evidence therefore has to show both parts, an effect on expression and a modification that can be undone; a change in the base sequence would be the mutation of EK 6.7.A.1 instead."),
 dict(q="During development, one transcription factor is induced and a set of genes begins to be expressed in a fixed order over the following hours. Which two framework statements together account for this?",
   choices=[
     "That induction of transcription factors during development results in sequential gene expression, and that groups of genes may be influenced by the same transcription factors",
     "That epigenetic changes are reversible, and that some genes are constitutively expressed",
     "That prokaryotes regulate operons, and that the same genetic code is used by nearly all organisms",
     "That mRNA carries information out of the nucleus, and that ribosomes read it in triplets",
     "That replication is semiconservative, and that each original strand templates a new one"], ans=0,
   why="EK 6.5.A.3.ii states that induction of transcription factors during development results in sequential gene expression, and EK 6.5.B.1.ii states that groups of genes may be influenced by the same transcription factors to coordinately regulate expression. Together they give both the order in time and the grouping of the genes that respond."),
 dict(q="A student claims that because two cells of one organism look different, they must carry different genes. How should the claim be corrected using this topic's statements?",
   choices=[
     "They carry the same genes but express a different combination of them, and at different levels",
     "They carry different genes because differentiation removes the genes a cell does not use",
     "They carry the same genes and express all of them equally, so the difference must be an artifact",
     "They carry different genes because each tissue acquires new genes as it develops",
     "They carry the same genes but read them with different genetic codes"], ans=0,
   why="EK 6.5.A.3 states that the phenotype of a cell is determined by the combination of genes expressed and the levels of expression, and EK 6.5.A.3.i attributes observable differentiation to the expression of genes for tissue-specific proteins. Nothing in the framework has a differentiating cell gain or lose genes, and EK 6.4.A.3.iv makes the code shared."),
 dict(q="Which statement about the regulation of gene expression is consistent with everything the framework states in this topic?",
   choices=[
     "Regulatory sequences and regulatory proteins control transcription, epigenetic modifications are reversible, and groups of genes can be regulated together in both kinds of cell",
     "Regulatory sequences are proteins, epigenetic modifications are permanent, and only prokaryotes regulate groups of genes together",
     "Regulatory sequences control translation rather than transcription, and epigenetic modifications act on the ribosome",
     "Every gene is either constitutively expressed or absent, and no gene is inducible",
     "The phenotype of a cell depends on which genes it carries rather than on which it expresses"], ans=0,
   why="Each clause of the keyed option is one of the framework's own: EK 6.5.A.1 for regulatory sequences and proteins controlling transcription, EK 6.5.A.2 for the reversibility of epigenetic modifications, and EK 6.5.B.1 for coordinate regulation in both prokaryotes and eukaryotes. Every other option contradicts at least one of those three."),
]
