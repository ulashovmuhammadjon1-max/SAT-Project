# AP BIOLOGY 7.6 Evidence of Evolution
# CED effective Fall 2025, Unit 7 Natural Selection, Big Idea 1 Evolution.
# Learning objectives 7.6.A (describe the types of data that provide evidence
# for evolution) and 7.6.B (explain how morphological, biochemical, and
# geological data provide evidence that organisms have changed over time).
# Suggested skill 4.B, describe data from a table or graph, including
# (i) identifying specific data points, (ii) describing trends and patterns in
# the data, (iii) describing relationships between variables.
#
# Essential knowledge relied on, in the framework's own terms:
#   7.6.A.1  evolution is supported by scientific evidence from many
#            disciplines: GEOGRAPHICAL, GEOLOGICAL, PHYSICAL, BIOCHEMICAL and
#            MATHEMATICAL data.
#   7.6.B.1  molecular, morphological and genetic evidence from EXTANT AND
#            EXTINCT organisms adds to our understanding of evolution.
#              i. fossils can be dated by a variety of methods, which include
#                 1) the age of the rocks where a fossil is found, 2) the rate
#                 of decay of isotopes including carbon-14, and 3) geographical
#                 data.
#             ii. morphological homologies, INCLUDING VESTIGIAL STRUCTURES,
#                 provide evidence of common ancestry.
#   7.6.B.2  a comparison of DNA nucleotide sequences and protein amino acid
#            sequences provides evidence for evolution and common ancestry.
#
# ON THE DATA. Skill 4.B is a table-reading skill, so eight items here carry a
# table and every number stated about one is recomputed from that table alone
# in verify_b7_6.py. The isotope in the dating table is labelled HYPOTHETICAL
# and its half-life is given in the stem, because the CED names carbon-14 as a
# method without printing its half-life, and a bank must not ask a student to
# recall a figure the framework does not supply.
#
# DELIBERATE OMISSIONS, to keep off neighbouring topics of this same unit.
# Building or reading a phylogenetic tree or cladogram, shared derived
# characters, out-groups and nodes are EK 7.9.A and EK 7.9.B and are asked in
# b7_9; the sequence table here is read for what EK 7.6.B.2 claims of it, that
# such a comparison is evidence for evolution and common ancestry, and only one
# item turns a difference count into a statement about ancestry. The cellular
# and molecular features shared by all eukaryotes -- membrane-bound organelles,
# linear chromosomes and genes containing introns -- are EK 7.7.A.1 and are
# asked in b7_7, so no item here uses them.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset.
TOPIC = ("7.6", "Evidence of Evolution", 7)

_T_LAYERS = dict(
    headers=["Rock layer", "Depth below the present surface in metres",
             "Estimated age of the layer in millions of years"],
    rows=[["Layer 1", "2", "5"],
          ["Layer 2", "8", "22"],
          ["Layer 3", "15", "48"],
          ["Layer 4", "23", "70"]])

_T_ISOTOPE = dict(
    headers=["Number of half-lives elapsed",
             "Fraction of the original isotope still present",
             "Age of the sample in years"],
    rows=[["One", "one half", "4000"],
          ["Two", "one quarter", "8000"],
          ["Three", "one eighth", "12000"],
          ["Four", "one sixteenth", "16000"]])

_T_AA = dict(
    headers=["Species compared with species Q",
             "Number of amino acid differences in a protein of 100 amino acids"],
    rows=[["Species R", "2"],
          ["Species S", "12"],
          ["Species T", "21"],
          ["Species U", "34"]])

QUESTIONS = [
 dict(q="Which of the following best describes the range of scientific evidence that supports evolution?",
   choices=[
     "Geographical, geological, physical, biochemical, and mathematical data",
     "Only data gathered from laboratory experiments on living organisms",
     "Only the fossil record and the rock layers that contain it",
     "Only comparisons of DNA and protein sequences among living species",
     "Only observations of how species are distributed across islands and continents"], ans=0,
   why="EK 7.6.A.1 names exactly those five kinds of data. Each distractor names one legitimate line of evidence and then excludes the others, which is the error the essential knowledge statement is written against."),

 dict(q="A biologist maps which related species occur on each of a chain of islands and on the nearest mainland. This work supplies which of the kinds of data named as evidence for evolution?",
   choices=["Geographical data", "Biochemical data", "Mathematical data",
            "Physical data", "Molecular data from extinct organisms"], ans=0,
   why="EK 7.6.A.1 lists geographical data among the disciplines that supply evidence for evolution. Where species live in relation to one another is geographical information, whatever the species themselves are made of."),

 dict(q="A researcher records the order in which different fossil forms appear in successive rock layers at a quarry. This work supplies which kind of data?",
   choices=["Geological data", "Biochemical data", "Mathematical data",
            "Geographical data", "Physical data"], ans=0,
   why="EK 7.6.A.1 lists geological data, and EK 7.6.B.1 makes the age of the rocks in which a fossil is found one of the ways a fossil is dated. The layers themselves, not the fossils' chemistry, are what is being read."),

 dict(q="A laboratory determines the amino acid sequence of the same enzyme in several species and counts the positions at which the sequences differ. This work supplies which kind of data?",
   choices=["Biochemical data", "Geological data", "Geographical data",
            "Physical data", "Mathematical data"], ans=0,
   why="EK 7.6.A.1 lists biochemical data, and EK 7.6.B.2 names the comparison of protein amino acid sequences specifically as evidence for evolution and common ancestry."),

 dict(q="A team builds a model that predicts how a measured difference between two populations should accumulate over many generations, then compares the prediction with the measurements. This work supplies which kind of data?",
   choices=["Mathematical data", "Geographical data", "Geological data",
            "Biochemical data", "Data from extinct organisms only"], ans=0,
   why="EK 7.6.A.1 lists mathematical data among the disciplines supplying evidence for evolution. Building a quantitative prediction and testing it against measurements is the mathematical contribution, whatever the measurements are of."),

 dict(q="Which of the following best explains why evidence for evolution drawn from several different disciplines is considered stronger than the same weight of evidence drawn from one discipline?",
   choices=[
     "Independent kinds of data are subject to different sources of error, so agreement among them is unlikely to be an artefact of any one method",
     "Evidence from several disciplines removes the need for a hypothesis",
     "Each discipline measures the same quantity, so the measurements can be averaged",
     "A claim supported by five disciplines becomes a certainty rather than a hypothesis",
     "Only mathematical data can be checked, so the other disciplines confirm it"], ans=0,
   why="EK 7.6.A.1 names five separate disciplines rather than one authoritative source. Rock dating, sequence comparison and species distribution can each go wrong in their own way, so their convergence is not explained by any single method's weakness."),

 dict(q="EK statements about the evidence for evolution refer to molecular, morphological, and genetic evidence drawn from which organisms?",
   choices=[
     "Both organisms alive today and organisms known only as fossils",
     "Only organisms alive today, since sequences cannot be read from fossils",
     "Only organisms known from the fossil record",
     "Only organisms that can be bred in a laboratory",
     "Only organisms that share a recent common ancestor with humans"], ans=0,
   why="EK 7.6.B.1 states that molecular, morphological and genetic evidence from extant and extinct organisms adds to our understanding of evolution. Extant means living now and extinct means known from the record, and the statement names both."),

 dict(q="Which of the following is one of the methods the course framework names for dating a fossil?",
   choices=[
     "The age of the rocks in which the fossil is found",
     "The number of species alive in the same habitat today",
     "The depth of soil that has formed above the site since the excavation",
     "The size of the fossil relative to its living relatives",
     "The number of amino acid differences between the fossil species and a living one"], ans=0,
   why="EK 7.6.B.1 lists three dating methods, of which the age of the rocks where the fossil is found is the first. Body size and modern species counts are not dating methods, and sequence differences are a separate line of evidence under EK 7.6.B.2."),

 dict(q="A fossil is dated by measuring how much of an unstable isotope remains in the sample and comparing that with how much would have been present originally. This method rests on",
   choices=[
     "the rate at which the isotope decays",
     "the depth of the layer in which the sample was found",
     "the number of fossils found in the same layer",
     "the geographical distance between the site and the nearest related living species",
     "the total mass of the fossil"], ans=0,
   why="EK 7.6.B.1 names the rate of decay of isotopes, including carbon-14, as a fossil dating method. A known decay rate converts a measured remaining fraction into an elapsed time, which is what makes the measurement a date."),

 dict(q="Besides the age of the surrounding rocks and the decay of isotopes, the course framework names which third source of information for dating fossils?",
   choices=["Geographical data", "The colour of the fossil", "The number of bones recovered",
            "The presence of vestigial structures", "The amino acid sequence of any surviving protein"], ans=0,
   why="EK 7.6.B.1 lists three dating methods and geographical data is the third. Vestigial structures and sequence comparisons appear elsewhere in this topic as evidence of common ancestry, not as dating methods."),

 dict(q="Two independent methods assign nearly the same age to one fossil. The best reason for a palaeontologist to report both rather than the more precise one alone is that",
   choices=[
     "agreement between methods that fail in different ways makes the date harder to explain as a mistake in either",
     "reporting two dates doubles the precision of the estimate",
     "a date is accepted only when at least two methods have been applied",
     "the less precise method corrects the more precise one",
     "the two methods measure two different fossils"], ans=0,
   why="EK 7.6.B.1 offers a variety of dating methods rather than one, which is what makes cross-checking possible. Two methods with unrelated failure modes agreeing is evidence about the date, whereas restating one measurement is not."),

 dict(q="The table gives the depth and estimated age of four rock layers at one site. A fossil recovered from which layer is the oldest?",
   table=_T_LAYERS,
   choices=["The fossil from layer 4", "The fossil from layer 1", "The fossil from layer 2",
            "The fossil from layer 3", "The layers cannot be placed in order from these data"], ans=0,
   why="EK 7.6.B.1 makes the age of the rock in which a fossil is found a dating method. The table states an age for each layer directly, and the largest of the four ages belongs to the deepest layer listed."),

 dict(q="Using the ages in that same table of rock layers, how much older is the layer at a depth of 23 metres than the layer at a depth of 8 metres?",
   table=_T_LAYERS,
   choices=["48 million years", "26 million years", "22 million years",
            "70 million years", "92 million years"], ans=0,
   why="Skill 4.B calls for identifying specific data points and describing the relationship between variables. The two depths pick out two rows, and the answer is the difference between the ages those rows report."),

 dict(q="In the same set of rock layers, what relationship do the two measured variables show?",
   table=_T_LAYERS,
   choices=[
     "The deeper a layer lies, the greater its estimated age",
     "The deeper a layer lies, the smaller its estimated age",
     "Depth and estimated age are unrelated in these data",
     "Every layer is the same age because all four lie at the same site",
     "Age increases with depth only for the two shallowest layers"], ans=0,
   why="Skill 4.B asks for the relationship between variables. Reading the table down its rows, depth and age rise together across all four layers without exception, which is why the age of surrounding rock can date a fossil at all."),

 dict(q="A fossil bed is dated using a hypothetical isotope whose half-life is 4000 years, and the table records what fraction of that isotope remains after each half-life. A sample retaining one eighth of its original isotope is about how old?",
   table=_T_ISOTOPE,
   choices=["12000 years", "4000 years", "8000 years", "16000 years", "32000 years"], ans=0,
   why="EK 7.6.B.1 names the rate of decay of isotopes as a dating method. The table's fraction column locates the sample in the row for the stated remaining fraction, and the age column of that row gives the answer."),

 dict(q="A second sample from the same hypothetical isotope study is about 16000 years old. How many half-lives have elapsed in that sample?",
   table=_T_ISOTOPE,
   choices=["Four", "Two", "Three", "Eight", "Sixteen"], ans=0,
   why="Skill 4.B, identifying a specific data point. Reading the table from the age column back to the half-life column gives the number of half-lives that corresponds to the stated age."),

 dict(q="Reading down the fraction column of that isotope table, what pattern do the successive entries follow?",
   table=_T_ISOTOPE,
   choices=[
     "Each entry is half of the entry above it, so the amount remaining never reaches zero",
     "Each entry is the entry above it reduced by a fixed amount, so the isotope is gone after four half-lives",
     "The entries increase, because the isotope accumulates over time",
     "The entries stay the same, because decay stops once half the isotope is gone",
     "The entries have no pattern, because decay is random for each atom"], ans=0,
   why="Skill 4.B asks for the trend in the data. One half, one quarter, one eighth and one sixteenth each halve the previous entry, which is what makes a half-life a fixed interval rather than a countdown to zero."),

 dict(q="Morphological homologies, including vestigial structures, are cited by the course framework as evidence of",
   choices=["common ancestry", "identical function in living species", "a constant rate of mutation",
            "the age of the rocks in which fossils are found", "reproductive isolation between populations"], ans=0,
   why="EK 7.6.B.1 states that morphological homologies, including vestigial structures, provide evidence of common ancestry. Homology is a claim about shared origin, not about the current use of a structure."),

 dict(q="The forelimbs of a whale, a bat and a horse each contain the same set of bones in the same relative positions, although the three limbs are used quite differently. This observation is best described as",
   choices=[
     "a morphological homology, and evidence of common ancestry",
     "evidence that the three species use their forelimbs for the same purpose",
     "evidence that the three species are the same species",
     "a similarity produced by the fossil record rather than by descent",
     "a difference in bone arrangement that argues against common ancestry"], ans=0,
   why="EK 7.6.B.1 makes morphological homologies evidence of common ancestry. The shared bone arrangement despite different uses is exactly the pattern descent from a common ancestor predicts and that shared function does not."),

 dict(q="A species retains a small, non-functional version of a structure that is fully developed and functional in related species. The best interpretation of this structure is that it is",
   choices=[
     "a vestigial structure, retained from an ancestor in which it functioned",
     "a newly evolved structure that has not yet reached full size",
     "evidence that the species is unrelated to the species in which the structure functions",
     "a structure whose function is identical in both species",
     "a structure produced by the rock layer in which the species is found"], ans=0,
   why="EK 7.6.B.1 names vestigial structures among the morphological homologies that provide evidence of common ancestry. A reduced version of a relative's working structure is what descent with modification from a shared ancestor predicts."),

 dict(q="Which comparison does the course framework name as providing evidence for evolution and common ancestry?",
   choices=[
     "A comparison of DNA nucleotide sequences and of protein amino acid sequences",
     "A comparison of the body sizes of adults of two species",
     "A comparison of the number of offspring two species produce",
     "A comparison of the depths at which two fossils were found",
     "A comparison of the habitats two species occupy today"], ans=0,
   why="EK 7.6.B.2 names exactly that comparison. The other options describe measurements that may be interesting for other reasons but that the statement does not identify as evidence of common ancestry."),

 dict(q="The table reports how many amino acid positions differ between species Q and each of four other species in the same protein. Which species differs from species Q at 21 of those positions?",
   table=_T_AA,
   choices=["Species T", "Species R", "Species S", "Species U", "Species Q"], ans=0,
   why="Skill 4.B, identifying a specific data point. The stated number of differences appears in exactly one row of the table, and that row's label is the answer."),

 dict(q="Reading down the difference column of that protein comparison table from the first row to the last, the number of amino acid differences",
   table=_T_AA,
   choices=[
     "increases at every step",
     "decreases at every step",
     "stays the same at every step",
     "increases and then decreases",
     "cannot be compared because the species are different"], ans=0,
   why="Skill 4.B asks for the trend in the data. Each row's count is larger than the one above it, and describing that pattern is a separate step from interpreting what it means."),

 dict(q="Each species in that protein comparison was compared with species Q over the same protein of one hundred amino acids. What percentage of positions is identical between species S and species Q?",
   table=_T_AA,
   choices=["88 percent", "12 percent", "98 percent", "79 percent", "66 percent"], ans=0,
   why="Skill 5.A includes percentages. The protein has one hundred positions and the table gives the number that differ, so the identical positions are the remainder of the hundred expressed as a percentage."),

 dict(q="Which conclusion about common ancestry does the protein comparison table most directly support?",
   table=_T_AA,
   choices=[
     "Species Q shares its most recent common ancestor with the species that differs from it at the fewest positions",
     "Species Q shares its most recent common ancestor with the species that differs from it at the most positions",
     "Species Q is descended from one of the four species listed",
     "The four species have no common ancestor with species Q, because none of the sequences is identical",
     "The table shows how many years ago each species last shared an ancestor with species Q"], ans=0,
   why="EK 7.6.B.2 makes sequence comparison evidence for common ancestry. Differences accumulate after two lineages separate, so the smallest count corresponds to the shortest separate history; the table carries no calibration and so cannot state a date."),

 dict(q="What does the fact that every species in a comparison of this kind possesses a recognisably similar version of the same protein indicate?",
   choices=[
     "The gene for that protein was present in an ancestor shared by all of them",
     "The species must all live in the same habitat",
     "The protein performs a different function in each species",
     "Each species evolved the protein independently after they separated",
     "The species have not changed since they separated"], ans=0,
   why="EK 7.6.B.2 makes such comparisons evidence for evolution and common ancestry. Presence of the same sequence in every descendant is explained by inheritance from one ancestor, which is the point of calling it evidence of ancestry rather than of similar habitat."),

 dict(q="Two species look almost nothing alike as adults, yet their DNA nucleotide sequences for one gene are highly similar. This pair of observations is best handled by",
   choices=[
     "treating the sequence comparison as an independent line of evidence about their shared ancestry",
     "discarding the sequence data, because appearance is the more direct evidence",
     "concluding that the two species are the same species",
     "concluding that sequences cannot be compared between species that look different",
     "concluding that the gene has no function in either species"], ans=0,
   why="EK 7.6.A.1 makes biochemical data one of several disciplines supplying evidence, and EK 7.6.B.2 names sequence comparison specifically. Independent lines of evidence are not discarded when they disagree with appearance; they are weighed alongside it."),

 dict(q="A student concludes from a table of sequence differences alone that two species separated exactly forty million years ago. The most serious problem with this conclusion is that",
   choices=[
     "a count of differences gives no time scale unless it is calibrated against dated evidence",
     "sequence differences cannot be counted accurately",
     "sequence comparison is evidence about function rather than about ancestry",
     "the two species must be compared with a third before any conclusion is possible",
     "differences accumulate at a rate that is known to be identical in every lineage"], ans=0,
   why="EK 7.6.B.2 licenses the inference to common ancestry, not to a date; EK 7.6.B.1 puts dating with rock ages and isotope decay. Converting a difference count into years requires the independent dating evidence the student did not use."),

 dict(q="A researcher has assembled morphological homologies among a group of living species and now wishes to add an independent line of evidence bearing on the same relationships. Which addition would do the most to serve that purpose?",
   choices=[
     "Comparing the nucleotide sequences of a gene shared by the same species",
     "Measuring the same morphological structures again in more individuals of the same species",
     "Photographing the same structures at higher magnification",
     "Recording the common names used for the species in different regions",
     "Repeating the same morphological comparison with a second observer"], ans=0,
   why="EK 7.6.A.1 treats the disciplines as separate sources, and EK 7.6.B.2 names sequence comparison as one of them. More or better measurements of the same morphological characters are not independent of those characters; a molecular comparison is."),

 dict(q="Taken together, dated fossils in ordered rock layers, homologous structures among living species, and sequence comparisons across those species best support which statement?",
   choices=[
     "Organisms have changed over time and present-day species descend from shared ancestors",
     "Each present-day species arose independently and has not changed since",
     "Fossil evidence and molecular evidence cannot both be correct",
     "Only species that leave fossils have changed over time",
     "The rate of change has been identical in every lineage"], ans=0,
   why="This is what learning objective 7.6.B asks students to explain and what EK 7.6.B.1 and EK 7.6.B.2 assert jointly: geological, morphological and molecular data are evidence that organisms have changed over time and share ancestry. No statement in the topic claims a uniform rate."),
]
