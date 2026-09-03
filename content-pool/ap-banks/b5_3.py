# AP BIOLOGY 5.3 Mendelian Genetics
# CED effective Fall 2025, Unit 5 Heredity. Big ideas 1 (Evolution) and 3
# (Information Storage and Transmission). Learning objective 5.3.A, explain the
# inheritance of genes and traits as described by Mendel's laws. Suggested
# skills 5.C (perform chi-square hypothesis testing) and 6.E (predict the causes
# or effects of a change in a biological system).
#
# Essential knowledge relied on, in the framework's own words:
#   5.3.A.1     Mendel's laws of segregation and independent assortment can be
#               applied to genes that are on DIFFERENT chromosomes.
#   5.3.A.2     In most cases, fertilization involves the fusion of two haploid
#               gametes, restoring the diploid number of chromosomes and
#               increasing genetic variation in populations by creating new
#               combinations of alleles in the zygote.
#   5.3.A.2.i   Rules of probability can be applied to analyze the passing of
#               single-gene traits from parent to offspring.
#   5.3.A.2.ii  Monohybrid, dihybrid, and test crosses can be used to determine
#               whether alleles are dominant or recessive.
#   5.3.A.2.iii An organism's genotype is the set of alleles inherited for one or
#               more genes. A genotype can be homozygous or heterozygous for
#               each gene.
#   5.3.A.2.iv  An organism's phenotype is the observable expression of the
#               inherited traits.
#   5.3.A.2.v   Patterns of inheritance (autosomal, genetically linked,
#               sex-linked) and whether an allele is dominant or recessive can
#               often be predicted from data, INCLUDING PEDIGREES. Punnett
#               squares can be used to predict the genotypes and phenotypes of
#               parents and offspring.
#   Relevant equations (CED appendix): if A and B are mutually exclusive,
#               P(A or B) = P(A) + P(B); if A and B are independent,
#               P(A and B) = P(A) x P(B). Chi-square is the sum of (o - e)
#               squared over e, with degrees of freedom equal to the number of
#               distinct possible outcomes minus one; the printed critical
#               values at p = 0.05 are 3.84 for one degree of freedom, 5.99 for
#               two and 7.81 for three.
#
# ON FIGURES. The CED names pedigrees and Punnett squares, and this bank cannot
# carry a picture. Every pedigree here is therefore delivered as a TABLE of
# individuals with their parents, sex and phenotype, and every question about it
# is answerable from that table alone. No stem refers to a diagram, a gel or a
# square that the student cannot see.
#
# DIVISION OF LABOUR WITH 5.4. Linked genes, sex-linked traits, codominance,
# incomplete dominance, pleiotropy and non-nuclear inheritance are 5.4's
# material and are not keyed here. This topic stays on segregation, independent
# assortment of genes on different chromosomes, the probability rules, the three
# named cross types, genotype against phenotype, and autosomal pedigrees.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX: ratios are
# written out as "3 tall to 1 short" and probabilities as "1 in 16".
TOPIC = ("5.3", "Mendelian Genetics", 5)

# Monohybrid F2 counts. 787 to 277 is 2.84 to 1.
_T_MONO = dict(
    headers=["F2 phenotype", "Number of plants"],
    rows=[["Tall", "787"],
          ["Short", "277"]])

# Dihybrid F2 counts, total 556. Expected under 9 to 3 to 3 to 1 is
# 312.75, 104.25, 104.25, 34.75.
_T_DIHYBRID = dict(
    headers=["F2 phenotype", "Number of seeds"],
    rows=[["Round and yellow", "315"],
          ["Round and green", "108"],
          ["Wrinkled and yellow", "101"],
          ["Wrinkled and green", "32"]])

# Pedigree 1, delivered as data. Individual 5 is an affected female whose
# father (1) is unaffected and whose mother (2) is unaffected.
_T_PED_REC = dict(
    headers=["Individual", "Sex", "Mother", "Father", "Phenotype"],
    rows=[["1", "Male", "not recorded", "not recorded", "Unaffected"],
          ["2", "Female", "not recorded", "not recorded", "Unaffected"],
          ["3", "Male", "2", "1", "Unaffected"],
          ["4", "Male", "2", "1", "Affected"],
          ["5", "Female", "2", "1", "Affected"],
          ["6", "Female", "not recorded", "not recorded", "Unaffected"],
          ["7", "Male", "6", "3", "Unaffected"]])

# Pedigree 2. Individuals 4 and 5 are both affected and their child 6 is not;
# individual 1 is an affected father with an unaffected daughter (3).
_T_PED_DOM = dict(
    headers=["Individual", "Sex", "Mother", "Father", "Phenotype"],
    rows=[["1", "Male", "not recorded", "not recorded", "Affected"],
          ["2", "Female", "not recorded", "not recorded", "Unaffected"],
          ["3", "Female", "2", "1", "Unaffected"],
          ["4", "Male", "2", "1", "Affected"],
          ["5", "Female", "not recorded", "not recorded", "Affected"],
          ["6", "Male", "5", "4", "Unaffected"],
          ["7", "Female", "5", "4", "Affected"]])

# A test cross of a purple-flowered plant of unknown genotype to a
# white-flowered plant. 98 to 102 is close to 1 to 1.
_T_TESTCROSS = dict(
    headers=["Offspring phenotype", "Number of plants"],
    rows=[["Purple flowers", "98"],
          ["White flowers", "102"]])

# Three separate crosses of the same trait, reported together.
_T_THREE = dict(
    headers=["Cross", "Parent phenotypes", "Tall offspring", "Short offspring"],
    rows=[["Cross 1", "Tall by short", "60", "0"],
          ["Cross 2", "Tall by short", "31", "29"],
          ["Cross 3", "Tall by tall", "45", "15"]])

# Observed counts for a chi-square exercise. 320 offspring, four classes.
_T_CHISQ = dict(
    headers=["Phenotype class", "Observed number"],
    rows=[["Green and smooth", "170"],
          ["Green and rough", "70"],
          ["Yellow and smooth", "58"],
          ["Yellow and rough", "22"]])

QUESTIONS = [
 dict(q="A pea plant is heterozygous for a single gene that controls stem length. According to Mendel's law of segregation, what is true of the gametes this plant produces?",
   choices=[
     "Each gamete carries exactly one of the two alleles, and half of the gametes carry each allele",
     "Each gamete carries both alleles, which separate from each other at fertilization",
     "Each gamete carries the dominant allele only, because the recessive allele is lost during gamete formation",
     "Each gamete carries two copies of whichever allele the plant expresses in its phenotype",
     "Gametes carry the two alleles in the same 3 to 1 proportion that appears among the offspring"], ans=0,
   why="EK 5.3.A.1 states the law of segregation, and EK 5.3.A.2 states that fertilization is the fusion of two HAPLOID gametes restoring the diploid number. A haploid gamete carries one allele of the gene, not two, and the two alleles of a heterozygote separate into equal numbers of gametes."),
 dict(q="Mendel's law of independent assortment predicts that a plant of genotype AaBb produces the four gamete types AB, Ab, aB and ab in equal numbers. The framework states that this prediction applies to which pair of genes?",
   choices=[
     "Two genes carried on different chromosomes",
     "Two genes carried close together on the same chromosome",
     "Two genes carried far apart on the same chromosome",
     "Any two genes, regardless of which chromosomes carry them",
     "Two genes carried on the chromosomes that determine sex"], ans=0,
   why="EK 5.3.A.1 is explicit that Mendel's laws of segregation and independent assortment can be applied to genes that are on different chromosomes. Genes sharing a chromosome are genetically linked, which EK 5.4.A.1.i treats as a deviation from the predicted ratios rather than a case of the law."),
 dict(q="Two haploid gametes from unrelated parents fuse. Which statement best describes what fertilization contributes to a population, according to the framework?",
   choices=[
     "It restores the diploid chromosome number and increases variation by creating new combinations of alleles in the zygote",
     "It restores the diploid chromosome number but leaves the population's variation unchanged, since no new alleles are made",
     "It doubles the number of alleles at every gene, so each zygote carries four alleles per gene",
     "It creates new alleles by rearranging the nucleotides of the alleles the parents carried",
     "It removes recessive alleles from the population, since only dominant alleles appear in the zygote"], ans=0,
   why="EK 5.3.A.2 says fertilization restores the diploid number of chromosomes AND increases genetic variation in populations by creating new combinations of alleles in the zygote. The second option gets the first half right and denies the second half, which is the half the framework emphasizes; new combinations, not new alleles, is exactly the point."),
 dict(q="Two plants of genotype AaBb are crossed, and the two genes are on different chromosomes. What is the probability that a given offspring has the genotype aabb?",
   choices=[
     "1 in 16, because the probability of aa and the probability of bb are multiplied",
     "1 in 8, because the probability of aa and the probability of bb are added",
     "1 in 4, because a quarter of the offspring are homozygous recessive at any one gene",
     "1 in 2, because half the gametes from each parent carry a recessive allele",
     "9 in 16, because that is the largest class in a dihybrid cross"], ans=0,
   why="The CED's law of probability for independent events gives P(A and B) = P(A) x P(B). The two genes are on different chromosomes, so by EK 5.3.A.1 they assort independently: one quarter of offspring are aa and one quarter are bb, and one quarter of one quarter is one sixteenth."),
 dict(q="Two heterozygous plants, Aa by Aa, are crossed. What is the probability that a given offspring inherits at least one A allele?",
   choices=[
     "3 in 4, because the probabilities of the two mutually exclusive genotypes AA and Aa are added",
     "1 in 4, because only the homozygous dominant genotype carries the A allele",
     "1 in 2, because each parent transmits the A allele half the time",
     "1 in 16, because the probability from each parent is multiplied",
     "It is certain, because a dominant allele is always transmitted when a parent carries one"], ans=0,
   why="The CED's law of probability for mutually exclusive outcomes gives P(A or B) = P(A) + P(B). A cross of two heterozygotes gives one quarter AA and one half Aa; these are mutually exclusive genotypes, and one quarter plus one half is three quarters."),
 dict(q="A biologist records that a rabbit has black fur and, by breeding it, determines that it carries one allele for black fur and one for brown fur. Which of these two records is the rabbit's phenotype, and which is its genotype?",
   choices=[
     "Black fur is the phenotype, the observable expression of the trait, and the pair of alleles is the genotype",
     "Black fur is the genotype, since fur color is the inherited character, and the pair of alleles is the phenotype",
     "Both records are the phenotype, since both were determined by observing the rabbit",
     "Both records are the genotype, since both describe alleles that the rabbit inherited",
     "Neither is a genotype, because a genotype can only be assigned to an organism that is homozygous"], ans=0,
   why="EK 5.3.A.2.iii defines the genotype as the set of alleles inherited for one or more genes, and EK 5.3.A.2.iv defines the phenotype as the observable expression of the inherited traits. The visible fur color is the observable expression; the allele pair is the set inherited."),
 dict(q="A plant carries two different alleles of the flower-color gene and two identical alleles of the seed-shape gene. How should this plant's genotype be described?",
   choices=[
     "Heterozygous for flower color and homozygous for seed shape",
     "Homozygous for flower color and heterozygous for seed shape",
     "Heterozygous for both genes, because the whole genotype contains two different alleles",
     "Homozygous for both genes, because the two genes belong to the same individual",
     "Neither homozygous nor heterozygous, because those terms describe phenotypes rather than genotypes"], ans=0,
   why="EK 5.3.A.2.iii states that an organism's genotype can be homozygous or heterozygous FOR EACH GENE. The terms are assigned gene by gene, so one individual can be heterozygous at one gene and homozygous at another; they are also genotype terms, not phenotype terms."),
 dict(q="A researcher has a tall pea plant and wants to determine whether it carries a hidden allele for short stems. Which cross should the researcher perform?",
   choices=[
     "Cross the tall plant with a short plant, which must be homozygous recessive",
     "Cross the tall plant with a known homozygous dominant tall plant",
     "Cross the tall plant with itself and count only the tall offspring",
     "Cross the tall plant with another tall plant of unknown genotype",
     "Cross two short plants and compare their offspring with the tall plant"], ans=0,
   why="EK 5.3.A.2.ii names the test cross as one of the crosses used to determine whether alleles are dominant or recessive. Because short is the recessive phenotype, a short plant must carry two recessive alleles and contributes only recessive alleles to the offspring, so every offspring's phenotype reports directly which allele the tall parent supplied."),
 dict(q="A test cross between a purple-flowered plant of unknown genotype and a white-flowered plant produces offspring that are about half purple and half white. What does this result show about the purple parent?",
   choices=[
     "It is heterozygous, because half of its gametes carried the recessive allele",
     "It is homozygous dominant, because purple offspring were produced at all",
     "It is homozygous recessive, because white offspring were produced at all",
     "Its genotype cannot be determined, because a test cross reveals only phenotypes",
     "It carries three alleles of the flower color gene, one of which is silent"], ans=0,
   why="EK 5.3.A.2.ii names the test cross as a way to determine whether alleles are dominant or recessive. The white parent contributes only recessive alleles, so an offspring is white exactly when the purple parent contributed a recessive allele; a result near one half means half of that parent's gametes carried it, which is what a heterozygote produces."),
 dict(q="The table reports the phenotypes of the F2 generation from a monohybrid cross between two heterozygous pea plants. Which ratio do these counts most closely approximate?",
   table=_T_MONO,
   choices=[
     "About 3 tall plants to 1 short plant",
     "About 1 tall plant to 1 short plant",
     "About 9 tall plants to 1 short plant",
     "About 2 tall plants to 1 short plant",
     "About 1 tall plant to 3 short plants"], ans=0,
   why="EK 5.3.A.2.ii names the monohybrid cross as a way to determine dominance, and EK 5.3.A.2.i licenses the probability analysis: a cross of two heterozygotes gives three quarters showing the dominant phenotype. The counts divide to about 2.8 to 1, which is far closer to 3 to 1 than to any other listed ratio."),
 dict(q="Seeds from an F2 generation were scored for two traits, seed shape and seed color, whose genes are on different chromosomes. Which ratio do the counts in the table most closely approximate?",
   table=_T_DIHYBRID,
   choices=[
     "About 9 round yellow to 3 round green to 3 wrinkled yellow to 1 wrinkled green",
     "About 1 round yellow to 1 round green to 1 wrinkled yellow to 1 wrinkled green",
     "About 3 round yellow to 3 round green to 1 wrinkled yellow to 1 wrinkled green",
     "About 9 round yellow to 7 seeds of all three remaining classes combined",
     "About 12 round yellow to 3 round green to 1 wrinkled yellow, with no wrinkled green class"], ans=0,
   why="EK 5.3.A.1 permits independent assortment for genes on different chromosomes, and the multiplication rule then predicts the four classes in the proportions nine, three, three and one. Scaling the total of 556 by those proportions predicts about 313, 104, 104 and 35, each within a few seeds of the count in the table."),
 dict(q="The table records seven members of a family and their phenotypes for a single-gene trait. Which pattern of inheritance is best supported by these data?",
   table=_T_PED_REC,
   choices=[
     "Autosomal recessive, because two unaffected parents have affected children of both sexes",
     "Autosomal dominant, because every affected individual has at least one affected parent",
     "X-linked recessive, because affected individuals appear only among the sons",
     "X-linked dominant, because an affected father passes the trait to all of his daughters",
     "The trait cannot be inherited, because unaffected parents cannot transmit it"], ans=0,
   why="EK 5.3.A.2.v states that patterns of inheritance and whether an allele is dominant or recessive can often be predicted from data including pedigrees. Individuals 1 and 2 are unaffected and have affected children, so the allele is recessive and both parents are carriers; one of those affected children is a daughter whose father is unaffected, which an X-linked recessive trait cannot produce because a daughter's only paternal X carries the father's allele."),
 dict(q="The table records a second family scored for a different single-gene trait. Which pattern of inheritance is best supported by these data?",
   table=_T_PED_DOM,
   choices=[
     "Autosomal dominant, because two affected parents have an unaffected child and an affected father has an unaffected daughter",
     "Autosomal recessive, because unaffected individuals appear in every generation of the family",
     "X-linked recessive, because the trait passes from an affected father to his son",
     "X-linked dominant, because affected individuals appear in every generation",
     "The trait is not heritable, because two affected parents produced a child who is unaffected"], ans=0,
   why="EK 5.3.A.2.v licenses reading the pattern from pedigree data. Individuals 4 and 5 are both affected and have an unaffected son, which is possible only if both are heterozygous for a dominant allele; and individual 1 is an affected father whose daughter is unaffected, which rules out an X-linked dominant allele because a father transmits his single X to every daughter."),
 dict(q="A plant with genotype Aa is crossed with a plant of genotype aa. A Punnett square predicts which phenotypic outcome among the offspring?",
   choices=[
     "Half show the dominant phenotype and half show the recessive phenotype",
     "Three quarters show the dominant phenotype and one quarter shows the recessive phenotype",
     "All show the dominant phenotype, because a dominant allele is present in the cross",
     "All show the recessive phenotype, because one parent is homozygous recessive",
     "One quarter show the dominant phenotype and three quarters show the recessive phenotype"], ans=0,
   why="EK 5.3.A.2.v names Punnett squares as the tool for predicting genotypes and phenotypes. The aa parent supplies a recessive allele to every offspring; the Aa parent supplies A to half of them and a to the other half, giving half Aa and half aa, and only the aa half shows the recessive phenotype."),
 dict(q="Two parents, each of genotype Aa, plan to have two children. What is the probability that both children have the genotype aa?",
   choices=[
     "1 in 16, because the probability for each child is one quarter and the two are multiplied",
     "1 in 8, because the probability for one child is one quarter and there are two children",
     "1 in 4, because the probability is the same for two children as for one",
     "1 in 2, because each parent transmits the recessive allele half the time",
     "0, because two children of the same parents cannot share the same genotype"], ans=0,
   why="EK 5.3.A.2.i licenses applying the rules of probability to single-gene traits, and the CED's equation for independent events gives P(A and B) = P(A) x P(B). Each fertilization is a separate event with probability one quarter, and one quarter times one quarter is one sixteenth."),
 dict(q="The table reports the observed counts of four phenotype classes among 320 offspring. If the null hypothesis predicts the four classes in the proportions 9 to 3 to 3 to 1, what are the expected numbers used in a chi-square test?",
   table=_T_CHISQ,
   choices=[
     "180, 60, 60 and 20",
     "170, 70, 58 and 22, since the expected values are the values that were counted",
     "80, 80, 80 and 80, since the four classes are equally likely under any null hypothesis",
     "160, 80, 40 and 40, since the proportions halve down the list",
     "240, 40, 30 and 10, since the largest class takes three quarters of the total"], ans=0,
   why="The CED's chi-square formula uses expected results computed from the null hypothesis, not from the data. The proportions nine, three, three and one sum to sixteen parts, so one part of 320 is 20, and the four classes are predicted at 180, 60, 60 and 20. Using the observed counts as the expected counts would force the statistic to zero for any data whatever."),
 dict(q="A student performs a chi-square test on the offspring of a monohybrid cross, scoring two phenotype classes. How many degrees of freedom should the student use, and what is the corresponding critical value at p = 0.05 in the CED's table?",
   choices=[
     "One degree of freedom and a critical value of 3.84",
     "Two degrees of freedom and a critical value of 5.99",
     "Three degrees of freedom and a critical value of 7.81",
     "One degree of freedom and a critical value of 6.63",
     "Four degrees of freedom and a critical value of 9.49"], ans=0,
   why="The CED's chi-square table states that degrees of freedom equal the number of distinct possible outcomes minus one. Two phenotype classes give one degree of freedom, and the printed value in the p = 0.05 row of that column is 3.84; 6.63 is the value in the p = 0.01 row and belongs to a stricter test."),
 dict(q="A chi-square test on a monohybrid cross with two phenotype classes returns a value of 5.10. Using the CED's chi-square table, what should the student conclude?",
   choices=[
     "The value exceeds the critical value at p = 0.05, so the deviation from the predicted ratio is larger than chance alone comfortably explains",
     "The value is below the critical value at p = 0.05, so the data match the prediction closely",
     "The value exceeds the critical value, which proves that the student counted the offspring incorrectly",
     "The value cannot be interpreted without knowing the total number of offspring, since the table depends on sample size",
     "The value shows that the two alleles are located on the same chromosome"], ans=0,
   why="With two classes there is one degree of freedom, and the CED's table gives 3.84 at p = 0.05 for that column. A statistic of 5.10 is larger, so the null hypothesis of no difference between observed and expected is rejected. The table is indexed by degrees of freedom and not by sample size, and rejecting a null hypothesis identifies a discrepancy rather than its cause."),
 dict(q="The table reports three separate crosses involving stem length in a plant species in which tall is dominant to short. Which cross shows that the tall parent was heterozygous?",
   table=_T_THREE,
   choices=[
     "Cross 2, because a tall parent crossed to a short parent produced short offspring",
     "Cross 1, because a tall parent crossed to a short parent produced no short offspring",
     "Cross 3, because two tall parents produced some short offspring",
     "Cross 1 and cross 3 together, because both involve at least one homozygous parent",
     "None of the crosses, because a heterozygote can only be identified by examining its gametes directly"], ans=0,
   why="EK 5.3.A.2.ii names the test cross as a route to determining dominance relationships. The short parent contributes only recessive alleles, so a short offspring proves the tall parent contributed a recessive allele as well; that happens in the cross reporting 31 tall and 29 short and not in the cross reporting 60 tall and none short. The tall by tall cross also reveals heterozygosity but does not involve a tall parent crossed to a short one."),
 dict(q="A purple-flowered plant of unknown genotype was crossed with a white-flowered plant, and the offspring are reported in the table. About how many of these 200 offspring received a dominant purple allele from the purple parent?",
   table=_T_TESTCROSS,
   choices=[
     "About 98, since exactly the purple offspring received it",
     "About 200, since the purple parent transmits its dominant allele to every offspring",
     "About 102, since the white offspring are the ones that received an allele from the purple parent",
     "About 50, since one quarter of the offspring receive a dominant allele in any cross",
     "About 150, since three quarters of offspring show the dominant phenotype"], ans=0,
   why="The white parent is homozygous recessive and can supply only a recessive allele, so an offspring is purple exactly when the purple parent supplied the dominant allele. The number of such offspring is therefore the number of purple offspring in the table, 98, and no inference beyond counting the table is needed."),
 dict(q="Two pea plants heterozygous at the same gene are crossed, and one offspring shows the dominant phenotype. What is the probability that this particular offspring is heterozygous?",
   choices=[
     "2 in 3, because the dominant phenotype covers one homozygous dominant class and two heterozygous classes",
     "1 in 2, because half of all the offspring of the cross are heterozygous",
     "1 in 4, because one quarter of the offspring of the cross are homozygous dominant",
     "3 in 4, because three quarters of the offspring show the dominant phenotype",
     "1 in 3, because one of the three genotypes produced is homozygous dominant"], ans=0,
   why="EK 5.3.A.2.i licenses the probability analysis. A cross of two heterozygotes gives genotypes in the proportions one homozygous dominant, two heterozygous and one homozygous recessive. Restricting attention to the offspring that shows the dominant phenotype removes the homozygous recessive class, leaving one part homozygous dominant against two parts heterozygous."),
 dict(q="A plant of genotype AaBb, with the two genes on different chromosomes, is crossed with a plant of genotype aabb. What phenotypic ratio does a Punnett square predict among the offspring?",
   choices=[
     "1 dominant for both traits to 1 dominant for the first only to 1 dominant for the second only to 1 recessive for both",
     "9 dominant for both traits to 3 dominant for the first only to 3 dominant for the second only to 1 recessive for both",
     "3 dominant for both traits to 1 recessive for both traits, with no other classes appearing",
     "All offspring dominant for both traits, because the first parent carries a dominant allele of each gene",
     "1 dominant for both traits to 3 recessive for both traits, since recessive alleles predominate in the cross"], ans=0,
   why="EK 5.3.A.2.v names the Punnett square as the predictive tool and EK 5.3.A.1 permits independent assortment here. The aabb parent supplies ab to every offspring, and the AaBb parent supplies AB, Ab, aB and ab in equal numbers, so the four phenotype classes appear in equal numbers. The nine to three to three to one pattern belongs to a cross of two dihybrids, not to this dihybrid test cross."),
 dict(q="In a family in which neither parent shows a particular trait, one child does show it. Which conclusion about the allele responsible is best supported?",
   choices=[
     "The allele is recessive, and each parent carries one copy without showing the trait",
     "The allele is dominant, and one parent must have shown the trait without it being recorded",
     "The allele arose by a new mutation in the child, because parents cannot transmit an allele they do not express",
     "The allele is dominant in the child and recessive in the parents, since dominance varies by individual",
     "No conclusion is possible, because inheritance patterns cannot be read from a single family"], ans=0,
   why="EK 5.3.A.2.iv defines the phenotype as the observable expression of the trait, and EK 5.3.A.2.iii allows a genotype to be heterozygous. A heterozygote for a recessive allele shows the dominant phenotype but transmits the recessive allele, so two such parents can have an affected child; that is the standard reading EK 5.3.A.2.v says data including pedigrees supports."),
 dict(q="A homozygous dominant plant is crossed with a homozygous recessive plant of the same species. What are the genotypes and phenotypes of the F1 offspring?",
   choices=[
     "All are heterozygous and all show the dominant phenotype",
     "All are heterozygous and half show each phenotype",
     "Half are homozygous dominant and half are homozygous recessive, and half show each phenotype",
     "All are homozygous dominant, because the dominant allele replaces the recessive allele in the zygote",
     "One quarter are homozygous dominant, one half heterozygous and one quarter homozygous recessive"], ans=0,
   why="EK 5.3.A.2 states that fertilization fuses two haploid gametes. One parent can supply only a dominant allele and the other only a recessive allele, so every zygote receives one of each and is heterozygous by EK 5.3.A.2.iii; the dominant allele determines the observable expression named in EK 5.3.A.2.iv, so every offspring looks alike."),
 dict(q="A cross of two heterozygotes at a single gene with complete dominance produces offspring in the genotypic proportions 1 to 2 to 1 but the phenotypic proportions 3 to 1. Why do the two ratios differ?",
   choices=[
     "The heterozygotes and the homozygous dominant individuals look alike, so two genotypic classes are counted as one phenotypic class",
     "Some heterozygous zygotes fail to develop, which removes them from the phenotypic count",
     "The phenotypic ratio is measured in a later generation than the genotypic ratio",
     "Dominant alleles are transmitted more often than recessive alleles, which inflates the dominant phenotype",
     "The genotypic ratio applies to the gametes and the phenotypic ratio applies to the zygotes"], ans=0,
   why="EK 5.3.A.2.iii makes the genotype the set of alleles inherited and EK 5.3.A.2.iv makes the phenotype the observable expression. Under complete dominance the homozygous dominant and heterozygous genotypes produce the same observable expression, so the one and the two of the genotypic ratio merge into the three of the phenotypic ratio; nothing about transmission or survival is required."),
 dict(q="Two genes on different chromosomes each have a dominant and a recessive allele. A cross of two individuals heterozygous at both genes is performed. How many different genotypes and how many different phenotypes are possible among the offspring?",
   choices=[
     "Nine genotypes and four phenotypes",
     "Four genotypes and four phenotypes",
     "Sixteen genotypes and four phenotypes",
     "Nine genotypes and nine phenotypes",
     "Three genotypes and two phenotypes"], ans=0,
   why="EK 5.3.A.1 permits treating the two genes independently. Each gene alone yields three genotypes and two phenotypes in this cross, so together the multiplication rule from the CED's probability equations gives three times three genotypes and two times two phenotypes. Sixteen is the number of boxes in the Punnett square, not the number of distinct genotypes, because many boxes repeat."),
 dict(q="A single gene in a diploid organism has one dominant and one recessive allele in the population. How many distinct genotypes are possible for this gene, and how are they described?",
   choices=[
     "Three, described as homozygous for the dominant allele, heterozygous, or homozygous for the recessive allele",
     "Two, described as dominant or recessive, since a genotype is named for the allele that is expressed",
     "Four, since each of the two alleles can come from either parent and the source of each allele is part of the genotype",
     "Two, described as homozygous or heterozygous, because the homozygous condition covers a single genotype",
     "One, because every member of a species carries the same genotype at a given gene"], ans=0,
   why="EK 5.3.A.2.iii states that an organism's genotype is the set of alleles inherited for a gene and that the genotype can be homozygous or heterozygous for each gene. A diploid with two available alleles can hold two dominant alleles, one of each, or two recessive alleles. Which parent supplied which allele is not part of the set, so it does not multiply the count."),
 dict(q="A gardener crosses two heterozygous plants and expects a 3 to 1 ratio of purple to white flowers among the offspring, but collects only four offspring and finds three purple and one white in one trial and four purple in the next. What does this best illustrate about applying probability to inheritance?",
   choices=[
     "A predicted ratio describes the probability for each offspring, so small samples deviate from it by chance while large samples approach it",
     "A predicted ratio is a rule that each set of four offspring must obey, so one of the two trials was miscounted",
     "The prediction fails because the probability of an outcome changes after each offspring is produced",
     "The prediction applies only to genes on sex chromosomes and cannot be used for flower color",
     "The prediction applies only when the parents are homozygous, which these parents are not"], ans=0,
   why="EK 5.3.A.2.i says the rules of probability are applied to analyze the passing of single-gene traits. A probability governs each independent fertilization; it does not allot outcomes within a batch, and successive fertilizations are independent so the probability does not change between offspring."),
 dict(q="A researcher predicts a 3 to 1 phenotypic ratio in the offspring of a cross between two heterozygotes but instead observes a ratio close to 1 to 1. Which change to one of the parents would explain the observed result?",
   choices=[
     "One parent is in fact homozygous recessive rather than heterozygous",
     "One parent is in fact homozygous dominant rather than heterozygous",
     "Both parents are in fact homozygous dominant rather than heterozygous",
     "Both parents are in fact homozygous recessive rather than heterozygous",
     "One parent produces gametes that carry two alleles of the gene rather than one"], ans=0,
   why="This is the prediction skill 6.E applied to EK 5.3.A.2.v. A homozygous recessive parent supplies only a recessive allele, so the cross becomes a test cross of the remaining heterozygote and yields half dominant and half recessive offspring. A homozygous dominant parent in the cross would give offspring that all show the dominant phenotype, and two homozygous parents of the same kind would give a uniform generation."),
 dict(q="In pea plants, seed color and stem length are controlled by genes on different chromosomes. A plant heterozygous for both is self-crossed. What is the probability that a given offspring shows the recessive phenotype for seed color and the dominant phenotype for stem length?",
   choices=[
     "3 in 16, because one quarter is multiplied by three quarters",
     "1 in 16, because one quarter is multiplied by one quarter",
     "9 in 16, because three quarters is multiplied by three quarters",
     "1 in 4, because the two traits are counted as a single outcome",
     "7 in 16, because the probabilities for the two traits are added"], ans=0,
   why="EK 5.3.A.1 allows the two genes on different chromosomes to be treated independently, and the CED's equation for independent events multiplies their probabilities. The recessive phenotype at one gene has probability one quarter and the dominant phenotype at the other has probability three quarters, and one quarter times three quarters is three sixteenths."),
]
