# AP BIOLOGY 5.4 Non-Mendelian Genetics
# CED effective Fall 2025, Unit 5 Heredity. Big idea 3 (Information Storage and
# Transmission). Learning objective 5.4.A, explain deviations from Mendel's
# model of the inheritance of traits. Suggested skills 5.A (perform mathematical
# calculations, including means, rates, ratios, percentages and percent changes)
# and 5.C (perform chi-square hypothesis testing).
#
# Essential knowledge relied on, in the framework's own words:
#   5.4.A.1     Patterns of inheritance of many traits do not follow the ratios
#               predicted by Mendel's laws and can be identified by quantitative
#               analysis, when the observed phenotypic ratios STATISTICALLY
#               DIFFER from the predicted ratios.
#   5.4.A.1.i   Genes located on the same chromosome are referred to as being
#               genetically linked. The probability that these linked genes
#               segregate together during meiosis can be used to calculate the
#               map distance (or map units) between them on a chromosome. This
#               calculation is called gene or genetic mapping.
#   5.4.A.1.ii  Codominance occurs when the phenotype from BOTH alleles is
#               expressed such that the heterozygote would have a different
#               phenotype than either homozygote.
#   5.4.A.1.iii Incomplete dominance occurs when neither allele of a gene can
#               mask the other, so the phenotype of the heterozygote is a
#               BLENDED version of the dominant and recessive phenotypes.
#   5.4.A.2     Some traits, known as sex-linked traits (X- or Y-linked), are
#               determined by genes on sex chromosomes. The pattern of
#               inheritance of sex-linked traits can often be predicted from
#               data, including pedigrees, indicating the genotypes and
#               phenotypes of both parents and offspring.
#     illustrative examples printed with 5.4.A.2: sex-linked traits reside on
#     sex chromosomes; sex-linked traits are inherited at HIGHER RATES in XY
#     individuals than in XX individuals; in certain species the chromosomal
#     basis of sex determination is not based on X and Y chromosomes (ZW in
#     birds, haplodiploidy in bees).
#   5.4.A.3     Pleiotropy is a phenomenon in which the expression of a SINGLE
#               gene results in multiple traits or effects; these traits
#               therefore do not segregate independently.
#   5.4.A.4     Some traits result from non-nuclear inheritance.
#   5.4.A.4.i   Chloroplasts and mitochondria are randomly assorted to gametes
#               and daughter cells; thus traits determined by chloroplast and
#               mitochondrial DNA do not follow simple Mendelian rules.
#   5.4.A.4.ii  In animals, mitochondria are usually transmitted by the egg and
#               not by sperm; those traits are typically maternally inherited.
#   5.4.A.4.iii In plants, mitochondria and chloroplasts are transmitted in the
#               OVULE and not in the pollen; those traits are typically
#               maternally inherited.
#
# ON FIGURES. No stem refers to a picture. The two pedigrees are delivered as
# tables of individuals with their parents, sex and phenotype, and every
# question about them is answerable from the table alone. Where a pedigree item
# would otherwise rest on a mode of inheritance that the data cannot exclude,
# the stem STATES the mode and asks for a consequence, which is exactly what
# EK 5.4.A.2 asks of pedigree data: the genotypes and phenotypes of parents and
# offspring.
#
# DIVISION OF LABOUR WITH 5.3. Segregation, independent assortment of genes on
# different chromosomes, monohybrid and dihybrid ratios under complete
# dominance, the probability rules and autosomal pedigrees belong to 5.3 and are
# not re-asked here. This topic is the deviations: linkage and mapping,
# codominance, incomplete dominance, sex linkage, pleiotropy and non-nuclear
# inheritance.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. Prose notation, no LaTeX.
TOPIC = ("5.4", "Non-Mendelian Genetics", 5)

# F2 of an incomplete-dominance cross. 480 plants, 1 to 2 to 1 predicts
# 120, 240, 120.
_T_PINK = dict(
    headers=["F2 flower color", "Number of plants"],
    rows=[["Red", "118"],
          ["Pink", "242"],
          ["White", "120"]])

# Test cross progeny for two genes on the SAME chromosome. 1000 offspring,
# 180 recombinant, so 18 map units.
_T_LINK = dict(
    headers=["Offspring class", "Number of offspring"],
    rows=[["Gray body and normal wing (both parental traits)", "415"],
          ["Black body and vestigial wing (both parental traits)", "405"],
          ["Gray body and vestigial wing (recombinant)", "88"],
          ["Black body and normal wing (recombinant)", "92"]])

# Pairwise recombination frequencies among three genes on one chromosome.
_T_MAP = dict(
    headers=["Pair of genes", "Recombination frequency (percent)"],
    rows=[["Genes P and Q", "7"],
          ["Genes Q and R", "12"],
          ["Genes P and R", "19"]])

# A second linkage test cross. 800 offspring, 120 recombinant, so 85 percent
# parental.
_T_LINK2 = dict(
    headers=["Offspring class", "Number of offspring"],
    rows=[["Both parental traits, combination 1", "336"],
          ["Both parental traits, combination 2", "344"],
          ["Recombinant, combination 1", "62"],
          ["Recombinant, combination 2", "58"]])

# A dihybrid test cross whose four classes are near equal. 240 offspring,
# 60 expected in each class.
_T_CHI4 = dict(
    headers=["Offspring class", "Number of offspring"],
    rows=[["Tall and purple", "62"],
          ["Tall and white", "58"],
          ["Short and purple", "61"],
          ["Short and white", "59"]])

# Pedigree A. Individual 1 is an affected mother; all three of her sons are
# affected and both of her daughters are not.
_T_XLINK = dict(
    headers=["Individual", "Sex", "Mother", "Father", "Phenotype"],
    rows=[["1", "Female", "not recorded", "not recorded", "Affected"],
          ["2", "Male", "not recorded", "not recorded", "Unaffected"],
          ["3", "Male", "1", "2", "Affected"],
          ["4", "Male", "1", "2", "Affected"],
          ["5", "Male", "1", "2", "Affected"],
          ["6", "Female", "1", "2", "Unaffected"],
          ["7", "Female", "1", "2", "Unaffected"]])

# Pedigree B, for a trait STATED in the stem to be X-linked recessive.
# Individual 1 is an affected father, so his daughter 3 must carry his allele.
_T_XCARRIER = dict(
    headers=["Individual", "Sex", "Mother", "Father", "Phenotype"],
    rows=[["1", "Male", "not recorded", "not recorded", "Affected"],
          ["2", "Female", "not recorded", "not recorded", "Unaffected"],
          ["3", "Female", "2", "1", "Unaffected"],
          ["4", "Male", "2", "1", "Unaffected"]])

# Reciprocal crosses in a plant with variegated and all-green leaves.
_T_RECIP = dict(
    headers=["Cross", "Plant supplying the ovule", "Plant supplying the pollen",
             "Offspring"],
    rows=[["Cross 1", "All green", "Variegated", "All green"],
          ["Cross 2", "Variegated", "All green", "Variegated"]])

QUESTIONS = [
 dict(q="A plant with red flowers is crossed with a plant with white flowers, and every offspring bears petals patterned with distinct red patches and white patches. Which inheritance pattern do these offspring illustrate?",
   choices=[
     "Codominance, because the phenotype from both alleles is expressed and the heterozygote differs from either homozygote",
     "Incomplete dominance, because the heterozygote's petals are intermediate between the two parental colors",
     "Complete dominance, because one of the two parental colors is fully visible in the offspring",
     "Pleiotropy, because a single gene is producing more than one petal color",
     "Non-nuclear inheritance, because the petal color did not follow Mendel's predicted ratio"], ans=0,
   why="EK 5.4.A.1.ii defines codominance as the case in which the phenotype from both alleles is expressed such that the heterozygote has a different phenotype than either homozygote. Both parental colors appear separately and unmixed, which is expression of both alleles rather than the blend that EK 5.4.A.1.iii describes."),
 dict(q="A snapdragon with red flowers is crossed with a snapdragon with white flowers, and every offspring bears pink flowers. Which inheritance pattern do these offspring illustrate?",
   choices=[
     "Incomplete dominance, because neither allele masks the other and the heterozygote is a blend of the two parental phenotypes",
     "Codominance, because both the red phenotype and the white phenotype are visible in the same flower",
     "Complete dominance, because the pink color is the dominant phenotype for this gene",
     "Sex linkage, because flower color is determined by a gene on a sex chromosome",
     "Genetic linkage, because the red allele and the white allele are on the same chromosome"], ans=0,
   why="EK 5.4.A.1.iii defines incomplete dominance as the case in which neither allele of a gene can mask the other, so the phenotype of the heterozygote is a blended version of the dominant and recessive phenotypes. A uniform intermediate color is a blend, not the separate expression of both phenotypes that EK 5.4.A.1.ii requires for codominance."),
 dict(q="Two heterozygous individuals are crossed at the same gene in two different species. In the first species the heterozygotes are an even intermediate shade; in the second, the heterozygotes show both parental colors in separate patches. Which statement correctly assigns the two patterns?",
   choices=[
     "The intermediate shade is incomplete dominance and the separate patches are codominance",
     "The intermediate shade is codominance and the separate patches are incomplete dominance",
     "Both are codominance, because in both cases the heterozygote differs from either homozygote",
     "Both are incomplete dominance, because in both cases neither allele is fully dominant",
     "Neither is a deviation from Mendel's model, because both crosses involve a single gene"], ans=0,
   why="The framework separates the two by the appearance of the heterozygote. EK 5.4.A.1.iii makes the incompletely dominant heterozygote a BLENDED version of the two phenotypes, while EK 5.4.A.1.ii makes the codominant heterozygote one in which the phenotype from both alleles is expressed. Both do satisfy the clause about differing from either homozygote, which is why that clause alone cannot sort them."),
 dict(q="Two pink-flowered plants, each heterozygous at a gene showing incomplete dominance, were crossed and the F2 generation was scored. Which ratio do the counts in the table most closely approximate?",
   table=_T_PINK,
   choices=[
     "About 1 red to 2 pink to 1 white",
     "About 3 red to 1 white, with the pink plants counted as red",
     "About 9 red to 3 pink to 1 white, as in a dihybrid cross",
     "About 1 red to 1 pink, with white plants appearing only rarely",
     "About 2 red to 1 pink to 2 white"], ans=0,
   why="Under incomplete dominance each genotype has its own visible phenotype, so the phenotypic ratio equals the genotypic ratio a cross of two heterozygotes produces, which is one to two to one. Scaling the 480 plants by those proportions predicts 120, 240 and 120, and the counted 118, 242 and 120 are within a few plants of each."),
 dict(q="In a cross of two heterozygotes at a gene showing incomplete dominance, the phenotypic ratio and the genotypic ratio are the same. Why?",
   choices=[
     "Each of the three genotypes produces its own distinguishable phenotype, so no two genotypic classes are counted together",
     "The heterozygotes fail to develop, so only the two homozygous classes are counted",
     "The gene is on a sex chromosome, so genotype and phenotype are recorded in the same way",
     "Incomplete dominance changes the proportions in which gametes are produced",
     "Incomplete dominance prevents segregation, so each offspring inherits both alleles from one parent"], ans=0,
   why="EK 5.4.A.1.iii makes the heterozygote a blend, which is a third visible phenotype. Under complete dominance the heterozygous and homozygous dominant classes look alike and merge into one phenotypic class; here they do not merge, so the two ratios coincide. Segregation and gamete production are unaffected, which is why the underlying genotypic ratio is the usual one."),
 dict(q="A pink-flowered snapdragon, heterozygous at a gene showing incomplete dominance, is crossed with a white-flowered snapdragon. What phenotypes are expected among the offspring?",
   choices=[
     "About half pink and about half white, with no red offspring",
     "All pink, because the pink phenotype is dominant to white",
     "About three quarters pink and one quarter white",
     "About one quarter red, one half pink and one quarter white",
     "All white, because white is the recessive phenotype and the other parent carries a white allele"], ans=0,
   why="The white parent carries two white alleles and can supply only one of them. The pink parent supplies a red allele to half its gametes and a white allele to the other half, so half of the offspring are heterozygous and, by EK 5.4.A.1.iii, blended pink, while the other half carry two white alleles. No offspring can receive two red alleles, so the red class cannot appear."),
 dict(q="Two genes are described as genetically linked. What does that mean in the framework's terms?",
   choices=[
     "The two genes are located on the same chromosome",
     "The two genes produce phenotypes that always appear together in an organism",
     "The two genes are both located on a sex chromosome",
     "One of the two genes controls the expression of the other",
     "The two genes are located on chromosomes that pair with each other during meiosis"], ans=0,
   why="EK 5.4.A.1.i states that genes located on the same chromosome are referred to as being genetically linked. Homologous chromosomes pair during meiosis, but genes on the two members of a pair are alleles of one gene rather than linked genes, and a gene controlling another gene's expression is regulation rather than linkage."),
 dict(q="The table reports the four classes of offspring from a test cross involving two genes carried on the same chromosome. What map distance between the two genes do these data give?",
   table=_T_LINK,
   choices=[
     "18 map units",
     "82 map units",
     "9 map units",
     "50 map units",
     "180 map units"], ans=0,
   why="EK 5.4.A.1.i states that the probability that linked genes segregate together during meiosis is used to calculate the map distance in map units, a calculation called gene mapping. The recombinant offspring number 88 plus 92, which is 180 of the 1000 scored, so the recombination frequency is 18 percent and the map distance is 18 map units. The 82 comes from the parental classes and the 9 from halving the recombinants."),
 dict(q="The table gives the recombination frequency measured for each pair among three genes carried on one chromosome. Which pair of genes lies farthest apart on that chromosome?",
   table=_T_MAP,
   choices=[
     "Genes P and R, whose recombination frequency is the largest of the three",
     "Genes P and Q, whose recombination frequency is the smallest of the three",
     "Genes Q and R, because its frequency lies between the other two",
     "Genes P and Q, because the two genes closest together recombine most often",
     "The distances cannot be ordered, because recombination frequency does not vary with distance"], ans=0,
   why="EK 5.4.A.1.i makes the probability that linked genes segregate together the basis for calculating map distance. Genes farther apart are separated by crossing over more often, so a larger recombination frequency means a larger distance; among 7, 12 and 19 percent the largest is the pair reported at 19, which is also close to the sum of the other two as a linear map requires."),
 dict(q="The table reports the offspring of a second test cross between two linked genes. What percentage of the offspring received a parental combination of the two traits?",
   table=_T_LINK2,
   choices=[
     "85 percent",
     "15 percent",
     "50 percent",
     "75 percent",
     "42 percent"], ans=0,
   why="Suggested skill 5.A asks for ratios and percentages. The two parental classes total 336 plus 344, which is 680 of the 800 offspring scored, and 680 divided by 800 is 85 percent. The remaining 15 percent are the recombinant classes, which is also the recombination frequency for this pair."),
 dict(q="A dihybrid individual is test crossed and the four classes of offspring are counted, as reported in the table. What do these counts indicate about the two genes?",
   table=_T_CHI4,
   choices=[
     "The four classes are near equal, so the two genes are not linked and assort independently",
     "The four classes are near equal, so the two genes must lie very close together on one chromosome",
     "Two classes greatly outnumber the other two, so the genes are linked",
     "The counts show codominance, because four phenotypes appeared instead of two",
     "The counts show pleiotropy, because a single gene produced four phenotypes"], ans=0,
   why="EK 5.4.A.1 makes the deviation detectable when observed phenotypic ratios statistically differ from the predicted ones. The predicted result for unlinked genes in a test cross is four equal classes, 60 each out of 240, and the counted 62, 58, 61 and 59 are all within two of that. Tightly linked genes would give the opposite pattern, two large parental classes and two small recombinant ones."),
 dict(q="Why do two genes carried close together on the same chromosome fail to give the ratio that Mendel's law of independent assortment predicts?",
   choices=[
     "They tend to segregate together during meiosis, so parental combinations of their alleles are overrepresented among the offspring",
     "They mutate more often than genes on separate chromosomes, which introduces new phenotypes",
     "They are expressed only in one sex, so half of the expected classes never appear",
     "One of the two genes is silenced by the other, so only three phenotype classes can be produced",
     "They are transmitted through the cytoplasm rather than through the nucleus"], ans=0,
   why="EK 5.4.A.1.i states that linked genes have a probability of segregating together during meiosis, and that probability is what gene mapping measures. Alleles that travel together into the same gamete produce more offspring of the parental combinations than independent assortment predicts, which is the statistical difference EK 5.4.A.1 describes."),
 dict(q="A recessive allele of a gene on the X chromosome causes a particular trait. In a population, this trait appears more often in XY individuals than in XX individuals. Which statement best accounts for that difference?",
   choices=[
     "An XY individual carries only one copy of the gene, so a single recessive allele is enough to produce the trait",
     "An XY individual carries three copies of the gene, so the recessive allele is present more often",
     "The recessive allele mutates more frequently in XY individuals than in XX individuals",
     "XX individuals inherit the allele less often, because mothers rarely transmit X chromosomes",
     "XY individuals express every allele they inherit, including alleles on their other chromosomes"], ans=0,
   why="EK 5.4.A.2 places sex-linked traits on the sex chromosomes, and the illustrative examples printed with it state that sex-linked traits are inherited at higher rates in XY individuals than in XX individuals. An XY individual has a single X chromosome and therefore a single allele of an X-linked gene, with no second allele that could mask it, whereas an XX individual needs two recessive alleles."),
 dict(q="The table records a family scored for a single-gene trait. Individual 1 is affected and her mate is not. Which pattern of inheritance is best supported by these data?",
   table=_T_XLINK,
   choices=[
     "X-linked recessive, because an affected mother transmits her only X chromosome to every son and all three sons are affected",
     "X-linked recessive, because an affected mother transmits the trait to all of her daughters and none of her sons",
     "Y-linked, because the trait appears in the sons and the mother is the affected parent",
     "Autosomal dominant, because the affected mother has affected children",
     "Non-nuclear, because the affected parent is the mother and all of her children are affected"], ans=0,
   why="EK 5.4.A.2 states that the inheritance of sex-linked traits can often be predicted from data including pedigrees indicating genotypes and phenotypes of parents and offspring. An affected mother of an X-linked recessive trait carries the allele on both X chromosomes, so every son receives it with no second X to mask it, while every daughter also receives the father's unaffected X and is a carrier. All three sons here are affected and both daughters are not, and a Y-linked allele could not be transmitted by a mother at all."),
 dict(q="The table records a second family. The trait scored is known to be caused by a recessive allele on the X chromosome. Which individual must carry that allele without showing the trait?",
   table=_T_XCARRIER,
   choices=[
     "Individual 3, because her father is affected and a father transmits his single X chromosome to every daughter",
     "Individual 4, because he received an X chromosome from his affected father",
     "Individual 2, because a mother must be a carrier for any child to be affected",
     "Individual 1, because an affected individual is also a carrier of the allele",
     "None of them, because a carrier cannot be identified without testing the offspring"], ans=0,
   why="EK 5.4.A.2 asks for the genotypes and phenotypes of parents and offspring to be read from pedigree data. An affected father carries the allele on his only X chromosome and transmits that X to every daughter and to no son, so the daughter must carry it; the son received his father's Y chromosome instead, and the mother's status cannot be settled because no child here is affected."),
 dict(q="A woman who carries one copy of an X-linked recessive allele but does not show the trait has children with a man who does not carry the allele. What proportion of their sons is expected to show the trait?",
   choices=[
     "About half, because half of the mother's X chromosomes carry the allele and a son has no second X",
     "None, because the father does not carry the allele and sons inherit the trait from their father",
     "All, because a son receives his only X chromosome from his mother",
     "About one quarter, because both parents must transmit an allele for the trait to appear",
     "About three quarters, because the allele is recessive only in the mother"], ans=0,
   why="EK 5.4.A.2 makes the pattern predictable from the parents' genotypes. A son receives his single X chromosome from his mother, and half of her X chromosomes carry the recessive allele; because the son's other sex chromosome is the Y he received from his father, there is no second allele of this gene to mask it, so half of the sons are expected to show the trait."),
 dict(q="A trait in a mammal is caused by a gene on the Y chromosome. What transmission pattern does this predict?",
   choices=[
     "It passes from an affected father to all of his sons and to none of his daughters",
     "It passes from an affected father to all of his daughters and to none of his sons",
     "It passes from an affected mother to all of her children of both sexes",
     "It passes to half of the children of an affected parent, regardless of their sex",
     "It cannot be transmitted, because the Y chromosome carries no genes"], ans=0,
   why="EK 5.4.A.2 names Y-linked as well as X-linked traits as sex-linked. In a species where the male is XY, every son receives the father's Y chromosome and every daughter receives his X chromosome instead, so a Y-linked allele travels down the male line only and a mother has no Y chromosome to transmit."),
 dict(q="In birds, the female carries two different sex chromosomes, designated Z and W, and the male carries two Z chromosomes. What does this system show about sex determination?",
   choices=[
     "In certain species the chromosomal basis of sex determination is not based on X and Y chromosomes",
     "Birds do not use chromosomes to determine sex, relying on environmental cues instead",
     "The Z and W chromosomes are simply other names for the X and Y chromosomes",
     "Sex-linked traits cannot occur in birds, because neither sex carries a single unpaired chromosome",
     "In birds every trait is sex-linked, because both sex chromosomes carry the same genes"], ans=0,
   why="The illustrative examples the CED prints with EK 5.4.A.2 state that in certain species the chromosomal basis of sex determination is not based on X and Y chromosomes, and name ZW in birds and haplodiploidy in bees. The system is chromosomal but differently arranged; in birds it is the female that carries the two unlike sex chromosomes, which reverses which sex is more often affected by a recessive sex-linked allele."),
 dict(q="In honeybees, fertilized eggs develop into diploid females and unfertilized eggs develop into haploid males. This arrangement is named in the framework as an example of which point?",
   choices=[
     "That in certain species sex determination rests on the number of chromosome sets rather than on X and Y chromosomes",
     "That sex is determined by the environment rather than by inheritance in insects",
     "That male bees inherit both a maternal and a paternal copy of every gene",
     "That haploid organisms cannot show any inherited trait, since they carry only one allele of each gene",
     "That non-nuclear inheritance determines sex in species without X and Y chromosomes"], ans=0,
   why="Haplodiploidy in bees is one of the illustrative examples the CED prints with EK 5.4.A.2 for the statement that in certain species the chromosomal basis of sex determination is not based on X and Y chromosomes. A male bee develops from an unfertilized egg and therefore has one set of chromosomes and one parent, and having only one allele of each gene is why every allele he carries is expressed."),
 dict(q="A single gene in a plant is found to affect flower color, seed coat thickness and root growth rate at the same time. Which phenomenon does this describe?",
   choices=[
     "Pleiotropy, in which the expression of a single gene results in multiple traits",
     "Genetic linkage, in which several genes on one chromosome are inherited together",
     "Codominance, in which more than one allele of a gene is expressed at once",
     "Incomplete dominance, in which the heterozygote shows a blend of several traits",
     "Non-nuclear inheritance, in which several traits are transmitted through the cytoplasm"], ans=0,
   why="EK 5.4.A.3 defines pleiotropy as a phenomenon in which the expression of a single gene results in multiple traits or effects. The framework adds that these traits therefore do not segregate independently, which is what separates it from a set of genes that happen to be inherited together."),
 dict(q="Both pleiotropy and genetic linkage can make several traits appear together in the offspring of a cross. What distinguishes them?",
   choices=[
     "Pleiotropy involves one gene with several effects, while linkage involves several genes carried on one chromosome",
     "Pleiotropy involves several genes on one chromosome, while linkage involves one gene with several effects",
     "Pleiotropy affects only sex-linked traits, while linkage affects only autosomal traits",
     "Pleiotropy can be broken up by crossing over, while linkage cannot be broken up at all",
     "Pleiotropy produces blended phenotypes, while linkage produces patched phenotypes"], ans=0,
   why="EK 5.4.A.3 makes pleiotropy a property of a single gene whose expression results in multiple traits, and EK 5.4.A.1.i makes linkage a relationship among genes located on the same chromosome. Crossing over can separate linked genes, which is exactly what map distance measures, but it cannot separate the several effects of one gene."),
 dict(q="A trait in a mammal is determined by a gene carried on mitochondrial DNA. What transmission pattern is expected?",
   choices=[
     "Offspring of both sexes inherit the trait from their mother, and an affected father transmits it to none of his offspring",
     "Offspring of both sexes inherit the trait from their father, because sperm supply the mitochondria of the zygote",
     "Only sons inherit the trait, because mitochondrial DNA follows the same rule as a Y-linked gene",
     "Half of the offspring of an affected parent of either sex inherit the trait",
     "The trait appears only when both parents carry the mitochondrial allele"], ans=0,
   why="EK 5.4.A.4.ii states that in animals mitochondria are usually transmitted by the egg and not by sperm, so traits determined by mitochondrial DNA are typically maternally inherited. Every offspring of an affected mother receives her mitochondria regardless of its sex, and a father contributes essentially none, which is why the pattern is not symmetrical between the parents."),
 dict(q="In a flowering plant, a leaf trait is determined by chloroplast DNA. Which parent determines the trait in the offspring?",
   choices=[
     "The parent that supplies the ovule, because chloroplasts are transmitted in the ovule and not in the pollen",
     "The parent that supplies the pollen, because pollen delivers the cytoplasm of the zygote",
     "Either parent equally, because chloroplasts are contributed in equal numbers by both gametes",
     "Whichever parent shows the trait, since a chloroplast trait is always dominant",
     "Neither parent, because chloroplast DNA is replaced by nuclear DNA in the zygote"], ans=0,
   why="EK 5.4.A.4.iii states that in plants mitochondria and chloroplasts are transmitted in the ovule and not in the pollen, so mitochondria-determined and chloroplast-determined traits are typically maternally inherited. The pollen parent contributes a nucleus but essentially no organelles, so its chloroplast alleles do not reach the offspring."),
 dict(q="Chloroplasts and mitochondria are distributed to gametes and daughter cells at random rather than by the mechanism that separates chromosomes in meiosis. What consequence does the framework draw from that?",
   choices=[
     "Traits determined by chloroplast and mitochondrial DNA do not follow simple Mendelian rules",
     "Traits determined by chloroplast and mitochondrial DNA follow Mendel's laws more exactly than nuclear traits",
     "Chloroplasts and mitochondria are lost from the cell within a few generations",
     "Each daughter cell receives exactly half of the organelles the parent cell contained",
     "Organelle DNA is copied only in gametes, so it cannot vary among body cells"], ans=0,
   why="EK 5.4.A.4.i states that chloroplasts and mitochondria are randomly assorted to gametes and daughter cells; thus traits determined by chloroplast and mitochondrial DNA do not follow simple Mendelian rules. Mendel's ratios depend on the orderly separation of paired chromosomes, and organelles are not paired or separated in that way, so no fixed ratio is predicted."),
 dict(q="The table reports two reciprocal crosses between an all-green plant and a variegated plant of the same species. What do the results indicate about the trait?",
   table=_T_RECIP,
   choices=[
     "It is inherited through the cytoplasm, because the offspring resemble the parent that supplied the ovule in both crosses",
     "It is inherited through the nucleus, because the offspring resemble one parent in each cross",
     "It is a codominant trait, because both parental phenotypes appear among the offspring of the two crosses",
     "It is sex-linked, because the outcome depends on which parent was used as the source of pollen",
     "It is an incompletely dominant trait, because the offspring of the two crosses differ from one another"], ans=0,
   why="EK 5.4.A.4.iii states that in plants mitochondria and chloroplasts are transmitted in the ovule and not in the pollen. A nuclear gene gives the same result whichever parent supplies the pollen, so the fact that the offspring match the ovule parent in both directions of the cross is what identifies the trait as cytoplasmic."),
 dict(q="EK 5.4.A.1 says that patterns of inheritance that do not follow Mendel's predicted ratios can be identified by quantitative analysis. What role does a chi-square test play in that identification?",
   choices=[
     "It measures whether the observed phenotypic counts differ from the predicted counts by more than chance alone would explain",
     "It calculates the predicted phenotypic ratio directly from the observed counts",
     "It determines which chromosome carries each of the genes under study",
     "It proves that the two genes under study are linked whenever the test statistic is small",
     "It converts a phenotypic ratio into a genotypic ratio without a cross being performed"], ans=0,
   why="EK 5.4.A.1 states that these patterns can be identified by quantitative analysis, when the observed phenotypic ratios statistically differ from the predicted ratios. The CED's chi-square formula compares observed with expected results and its table of critical values is what turns a difference into a judgement about chance; expected counts come from the hypothesis being tested, not from the data."),
 dict(q="A biologist wants to determine whether a gene with two alleles shows codominance or incomplete dominance in a species new to study. Which observation would settle the question?",
   choices=[
     "Whether a heterozygote shows both parental phenotypes side by side or a single intermediate phenotype",
     "Whether a cross of two heterozygotes yields three phenotype classes rather than two",
     "Whether the offspring of two homozygotes are uniform in phenotype",
     "Whether the gene is located on an autosome or on a sex chromosome",
     "Whether the phenotypic ratio of a test cross is one to one"], ans=0,
   why="Both patterns give three phenotype classes in a cross of two heterozygotes and both give a uniform generation from two homozygotes, so neither of those results discriminates. The framework's own difference is the heterozygote's appearance: EK 5.4.A.1.ii has both alleles expressed and EK 5.4.A.1.iii has a blend of the two phenotypes."),
 dict(q="A man who shows an X-linked recessive trait has children with a woman who carries no copy of the allele. What is expected of their children?",
   choices=[
     "No child shows the trait, but every daughter carries one copy of the allele",
     "Every child shows the trait, because the father carries the allele on his only X chromosome",
     "Every son shows the trait, because a son receives his X chromosome from his father",
     "Half of the children of each sex show the trait",
     "No child shows the trait and no child carries the allele, because the mother contributes both X chromosomes"], ans=0,
   why="EK 5.4.A.2 makes the pattern predictable from parental genotypes. A father transmits his single X chromosome to every daughter and his Y chromosome to every son, so each daughter receives his recessive allele together with an unaffected allele from her mother and is an unaffected carrier, while each son receives only the mother's unaffected X allele."),
 dict(q="A single mutation is found to shorten an animal's limbs, thicken its skull and reduce its litter size, and the three effects are never seen apart in the offspring of any cross. Which explanation does the framework offer, and what does it predict?",
   choices=[
     "Pleiotropy, and it predicts that the three effects do not segregate independently because one gene produces all of them",
     "Genetic linkage, and it predicts that the three effects will be separated in a small fraction of offspring by crossing over",
     "Codominance, and it predicts that heterozygotes will show all three effects at half intensity",
     "Non-nuclear inheritance, and it predicts that only the mother transmits the three effects",
     "Independent assortment, and it predicts that the three effects appear in a nine to three to three to one ratio"], ans=0,
   why="EK 5.4.A.3 defines pleiotropy as the expression of a single gene resulting in multiple traits or effects, and adds that these traits therefore do not segregate independently. That is why the effects are never seen apart; linked genes, by contrast, are separated at a rate set by their map distance under EK 5.4.A.1.i, so linkage predicts occasional recombinants."),
 dict(q="Which experimental result would be a deviation from Mendel's model of inheritance rather than an example of it?",
   choices=[
     "A dihybrid test cross yields the two parental classes far more often than the two recombinant classes",
     "A cross of two heterozygotes at one gene yields three quarters showing the dominant phenotype",
     "A cross of a homozygous dominant individual with a homozygous recessive one yields a uniform generation",
     "A test cross of a heterozygote at one gene yields half of the offspring with each phenotype",
     "A dihybrid test cross yields four classes of offspring in nearly equal numbers"], ans=0,
   why="EK 5.4.A.1 defines the deviation as an observed phenotypic ratio that statistically differs from the predicted one. Mendel's laws predict four equal classes from a dihybrid test cross; an excess of parental combinations is the signature of the linkage described in EK 5.4.A.1.i. The other listed results are the ratios his laws predict."),
]
