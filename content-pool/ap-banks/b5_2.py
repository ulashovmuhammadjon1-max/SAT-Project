# AP BIOLOGY 5.2 Meiosis and Genetic Diversity
# CED effective Fall 2025, Unit 5 Heredity.
# Big Idea 3 Information Storage and Transmission.
# Learning objective 5.2.A, explain how the process of meiosis generates genetic
# diversity. Suggested skill 3.A, identify or pose a testable question based on
# an observation, data, or a model.
#
# Essential knowledge, in the framework's own terms:
#   5.2.A.1  CORRECT SEPARATION of the homologous chromosomes in MEIOSIS I and
#            sister chromatids in MEIOSIS II ensures that each gamete receives a
#            HAPLOID (1n) set of chromosomes comprising an ASSORTMENT OF BOTH
#            MATERNAL AND PATERNAL chromosomes. When INCORRECT SEPARATION occurs
#            (NONDISJUNCTION), gametes are NO LONGER HAPLOID.
#   5.2.A.2  During PROPHASE I, NON-SISTER CHROMATIDS EXCHANGE GENETIC MATERIAL
#            via CROSSING OVER (RECOMBINATION), which INCREASES GENETIC
#            DIVERSITY among the resultant gametes.
#   5.2.A.3  SEXUAL REPRODUCTION in eukaryotes INCREASES GENETIC VARIATION,
#            including CROSSING OVER, RANDOM ASSORTMENT of chromosomes during
#            meiosis, and subsequent FERTILIZATION of gametes.
#
# EXCLUSION STATEMENT OBSERVED. The CED puts knowledge of the details of sexual
# reproduction cycles in various plants and animals beyond the scope of the AP
# Exam, so no item here asks about any particular organism's life cycle.
#
# BOUNDARY WITH 5.1, HELD DELIBERATELY. The PHASES of meiosis and what happens
# in each are topic 5.1 and carry no key here. This module takes only what
# separation and exchange PRODUCE: a haploid assortment, or a gamete that is not
# haploid, and the three sources of variation EK 5.2.A.3 names. Items 3, 9 and
# 21 cite EK 5.1.A.2.i or EK 5.1.A.2.iii for the phase they name, and say so.
#
# BOUNDARY WITH 5.3, WHICH IS NOT THIS AGENT'S TOPIC. No item asks for a
# Punnett square, a genotype ratio, a map distance or any Mendelian
# calculation. The recombination table below asks only whether recombinant
# gametes appeared, which is what EK 5.2.A.2 asserts crossing over produces.
#
# NO FIGURES ANYWHERE. Crossing over and assortment invite a diagram and the
# bank cannot carry one, so every data item is a table of counts and the
# question is asked of the table.
#
# FIVE choices (A-E). Plain prose, no LaTeX.
TOPIC = ("5.2", "Meiosis and Genetic Diversity", 5)

_T_GAMETES = dict(
    headers=["Meiosis observed (hypothetical, 400 gametes scored each time)",
             "Gametes with the haploid number of chromosomes",
             "Gametes with more or fewer chromosomes than the haploid number"],
    rows=[["Separation correct at both divisions", "400", "0"],
          ["Separation incorrect at one division", "200", "200"]])

_T_RECOMBINANT = dict(
    headers=["Chromosome pair examined (hypothetical, 1,000 gametes scored each time)",
             "Gametes carrying a parental combination of the two markers",
             "Gametes carrying a combination found in neither parental chromosome"],
    rows=[["Pair 1", "820", "180"],
          ["Pair 2", "940", "60"]])

_T_ASSORTMENT = dict(
    headers=["Homologous pairs in the organism (hypothetical model)",
             "Different chromosome combinations a gamete could receive from assortment alone"],
    rows=[["1", "2"],
          ["2", "4"],
          ["3", "8"],
          ["4", "16"]])

_T_SOURCES = dict(
    headers=["Feature switched off in the model (hypothetical)",
             "Genetically different offspring types the model produces"],
    rows=[["Nothing switched off", "10,000"],
          ["Crossing over switched off", "1,200"],
          ["Random assortment switched off", "900"],
          ["Fusion of two different gametes switched off", "100"]])

QUESTIONS = [
 dict(q="What does the framework say correct separation during the two meiotic divisions ensures?",
   choices=[
     "That each gamete receives a haploid set comprising an assortment of maternal and paternal chromosomes",
     "That each gamete receives a diploid set identical to the parent cell's",
     "That each gamete receives only maternal chromosomes",
     "That each gamete receives only paternal chromosomes",
     "That every gamete produced is genetically identical to every other"],
   ans=0,
   why="EK 5.2.A.1 states that correct separation of homologous chromosomes in meiosis I and sister chromatids in meiosis II ensures that each gamete receives a haploid set of chromosomes that comprises an assortment of both maternal and paternal chromosomes."),

 dict(q="What does the framework call incorrect separation during meiosis, and what does it produce?",
   choices=[
     "Nondisjunction, which produces gametes that are no longer haploid",
     "Nondisjunction, which produces gametes that are more strictly haploid than usual",
     "Crossing over, which produces gametes that are no longer haploid",
     "Recombination, which produces gametes with no chromosomes at all",
     "Fertilization, which produces gametes that are no longer haploid"],
   ans=0,
   why="EK 5.2.A.1 states that when incorrect separation occurs, nondisjunction, gametes are no longer haploid. Crossing over and fertilization are named elsewhere for entirely different processes."),

 dict(q="Where in meiosis does the framework place crossing over, and between which structures?",
   choices=[
     "During prophase I, between non-sister chromatids",
     "During prophase I, between sister chromatids",
     "During anaphase II, between non-sister chromatids",
     "During telophase II, between sister chromatids",
     "After fertilization, between the two gamete nuclei"],
   ans=0,
   why="EK 5.2.A.2 states that during prophase I of meiosis, non-sister chromatids exchange genetic material via a process called crossing over. EK 5.1.A.2.i places synapsis and the possible formation of chiasmata in the same phase."),

 dict(q="What does the framework say crossing over accomplishes?",
   choices=[
     "It increases genetic diversity among the resultant gametes",
     "It decreases genetic diversity among the resultant gametes",
     "It restores the diploid chromosome number in each gamete",
     "It prevents the separation of homologous chromosomes",
     "It converts the gametes into body cells"],
   ans=0,
   why="EK 5.2.A.2 states that crossing over, also called recombination, increases genetic diversity among the resultant gametes."),

 dict(q="Which three contributors to genetic variation does the framework name under sexual reproduction in eukaryotes?",
   choices=[
     "Crossing over, random assortment of chromosomes during meiosis, and fertilization of gametes",
     "Crossing over, nondisjunction, and mitosis of body cells",
     "Random assortment, asexual reproduction, and cytokinesis",
     "Fertilization, denaturation of enzymes, and apoptosis",
     "Nondisjunction, fertilization, and the folding of the inner mitochondrial membrane"],
   ans=0,
   why="EK 5.2.A.3 states that sexual reproduction in eukaryotes increases genetic variation, including crossing over, random assortment of chromosomes during meiosis, and subsequent fertilization of gametes."),

 dict(q="What does the framework mean by random assortment of chromosomes during meiosis?",
   choices=[
     "Which member of each homologous pair goes to a given gamete is independent of the others, so many combinations are possible",
     "The chromosomes of a gamete are chosen from a single parent's set only",
     "The chromosomes are assorted after fertilization rather than during meiosis",
     "The chromosomes are duplicated at random until the diploid number is restored",
     "The chromosomes exchange material at random between sister chromatids"],
   ans=0,
   why="EK 5.2.A.3 names random assortment of chromosomes during meiosis as a contributor to genetic variation, and EK 5.2.A.1 describes the resulting haploid set as an assortment of both maternal and paternal chromosomes."),

 dict(q="Why does the framework count fertilization among the contributors to genetic variation?",
   choices=[
     "Because it combines two separately produced gametes into one new genetic combination",
     "Because it doubles the amount of crossing over that has already occurred",
     "Because it separates homologous chromosomes into different cells",
     "Because it converts a diploid cell into a haploid one",
     "Because it prevents nondisjunction from occurring in the parents"],
   ans=0,
   why="EK 5.2.A.3 names subsequent fertilization of gametes among the ways sexual reproduction in eukaryotes increases genetic variation, alongside crossing over and random assortment."),

 dict(q="What other name does the framework give to crossing over?",
   choices=[
     "Recombination",
     "Nondisjunction",
     "Synapsis",
     "Assortment",
     "Fertilization"],
   ans=0,
   why="EK 5.2.A.2 states that non-sister chromatids exchange genetic material via a process called crossing over, giving recombination in parentheses as the alternative name."),

 dict(q="Which separation does the framework assign to each of the two meiotic divisions when separation is correct?",
   choices=[
     "Homologous chromosomes at the first division and sister chromatids at the second",
     "Sister chromatids at the first division and homologous chromosomes at the second",
     "Homologous chromosomes at both divisions",
     "Sister chromatids at both divisions",
     "Neither, because separation occurs only after fertilization"],
   ans=0,
   why="EK 5.2.A.1 refers to correct separation of the homologous chromosomes in meiosis I and sister chromatids in meiosis II, which EK 5.1.A.2.iii and EK 5.1.A.3.iii state as the events of the two anaphases."),

 dict(q="What does the framework say a correctly produced haploid set of chromosomes comprises?",
   choices=[
     "An assortment of both maternal and paternal chromosomes",
     "Maternal chromosomes only",
     "Paternal chromosomes only",
     "One complete copy of each parent's full diploid set",
     "Chromosomes drawn at random from unrelated organisms"],
   ans=0,
   why="EK 5.2.A.1 states that each gamete receives a haploid set of chromosomes that comprises an assortment of both maternal and paternal chromosomes."),

 dict(q="Gametes from two meioses were scored for chromosome number, with the results shown. Which conclusion do the data support?",
   table=_T_GAMETES,
   choices=[
     "Incorrect separation produced gametes that are no longer haploid",
     "Incorrect separation produced only gametes with the haploid number",
     "Correct separation produced gametes with more chromosomes than the haploid number",
     "Both meioses produced the same proportion of haploid gametes",
     "Neither meiosis produced any gamete with the haploid number"],
   ans=0,
   why="EK 5.2.A.1 states that when incorrect separation occurs, nondisjunction, gametes are no longer haploid. The two rows differ exactly in that respect."),

 dict(q="Gametes were scored for two markers carried on one chromosome pair, with the results shown. What do the gametes carrying a combination found in neither parental chromosome indicate?",
   table=_T_RECOMBINANT,
   choices=[
     "That genetic material was exchanged between non-sister chromatids during meiosis",
     "That the two markers were carried on different chromosome pairs",
     "That nondisjunction occurred during one of the two divisions",
     "That fertilization combined two gametes before the markers were scored",
     "That the gametes were produced by mitosis rather than by meiosis"],
   ans=0,
   why="EK 5.2.A.2 states that non-sister chromatids exchange genetic material via crossing over, which increases genetic diversity among the resultant gametes. A combination present in neither parental chromosome is what such an exchange produces."),

 dict(q="A model was run for organisms with different numbers of homologous pairs, with the results shown. What pattern do the data show?",
   table=_T_ASSORTMENT,
   choices=[
     "The number of possible combinations doubles with each additional homologous pair",
     "The number of possible combinations increases by one with each additional pair",
     "The number of possible combinations halves with each additional pair",
     "The number of possible combinations is the same for every organism modeled",
     "The number of possible combinations falls to zero once there is more than one pair"],
   ans=0,
   why="EK 5.2.A.3 names random assortment of chromosomes during meiosis among the contributors to genetic variation, and skill 4.B asks students to describe the relationship between the two columns, which here is a doubling at each step."),

 dict(q="A model of offspring variation was run with each contributor switched off in turn, with the results shown. What do the data indicate?",
   table=_T_SOURCES,
   choices=[
     "Each of the three features contributes to the variety of offspring the model produces",
     "Only one of the three features contributes to the variety of offspring",
     "None of the three features affects the variety of offspring",
     "Switching a feature off increases the variety of offspring produced",
     "The three features contribute equally, since each removal gives the same result"],
   ans=0,
   why="EK 5.2.A.3 names crossing over, random assortment and fertilization together as ways sexual reproduction increases genetic variation, and every removal in the table lowers the number of offspring types."),

 dict(q="Using the same model results, which single feature accounts for the largest share of the variety when it is removed?",
   table=_T_SOURCES,
   choices=[
     "The one whose removal leaves the fewest genetically different offspring types",
     "The one whose removal leaves the most genetically different offspring types",
     "The one whose removal leaves the number of offspring types unchanged",
     "The condition in which nothing is switched off",
     "None of them, because the model's removals cannot be compared"],
   ans=0,
   why="Skill 4.B asks students to identify specific data points and compare them. The lowest remaining count marks the removal that cost the model the most variety, and EK 5.2.A.3 names all three removed features as contributors."),

 dict(q="Homologous chromosomes fail to separate during meiosis I in one cell. What does the framework's account predict about the resulting gametes?",
   choices=[
     "They are no longer haploid, because separation was incorrect",
     "They are haploid but carry only maternal chromosomes",
     "They are haploid but carry only paternal chromosomes",
     "They are unaffected, because only meiosis II determines chromosome number",
     "They contain no chromosomes at all"],
   ans=0,
   why="EK 5.2.A.1 states that correct separation of homologous chromosomes in meiosis I is part of what ensures a haploid set, and that when incorrect separation occurs, nondisjunction, gametes are no longer haploid."),

 dict(q="A treatment prevents any exchange of material between non-sister chromatids while meiosis otherwise proceeds normally. What is the most reasonable prediction?",
   choices=[
     "Genetic diversity among the resulting gametes is lower than it would otherwise be",
     "Genetic diversity among the resulting gametes is higher than it would otherwise be",
     "The gametes are no longer haploid",
     "The gametes are produced by mitosis instead",
     "Fertilization can no longer occur"],
   ans=0,
   why="EK 5.2.A.2 states that crossing over increases genetic diversity among the resultant gametes, so preventing it removes one of the contributions to that diversity while leaving separation, and therefore ploidy, intact."),

 dict(q="Which of the framework's named contributors to genetic variation is unavailable to an organism whose gametes never fuse with another gamete?",
   choices=[
     "Fertilization of gametes",
     "Crossing over during prophase I",
     "Random assortment of chromosomes during meiosis",
     "Correct separation of homologous chromosomes",
     "Nondisjunction during meiosis II"],
   ans=0,
   why="EK 5.2.A.3 names crossing over, random assortment and subsequent fertilization of gametes as the contributors. Only the last requires two gametes to come together."),

 dict(q="Which of these is a testable question about the framework's account of meiosis and diversity?",
   choices=[
     "Do gametes from a treated organism carry fewer new marker combinations than gametes from an untreated one?",
     "Is genetic diversity a good thing for an organism to have?",
     "Should crossing over be regarded as more important than fertilization?",
     "Which of the three contributors is the most elegant?",
     "Would organisms be happier if meiosis did not occur?"],
   ans=0,
   why="Skill 3.A asks students to identify or pose a testable question. Only the keyed question can be settled by counting gametes, and it tests the claim in EK 5.2.A.2 that crossing over increases diversity among the resultant gametes."),

 dict(q="An investigator wants to test whether random assortment contributes to the variety of gametes an organism makes. Which question is best posed for that purpose?",
   choices=[
     "How many different combinations of whole chromosomes appear among a large sample of this organism's gametes?",
     "How many chromosomes does a body cell of this organism contain?",
     "How long does one round of meiosis take in this organism?",
     "How many gametes does this organism produce in a lifetime?",
     "Is this organism more valuable than a related species?"],
   ans=0,
   why="Skill 3.A asks for a testable question aligned to the claim. EK 5.2.A.3 makes random assortment a source of variation in the combinations of chromosomes a gamete receives, so the question has to be about how many combinations appear."),

 dict(q="Why does the framework specify NON-SISTER chromatids as the ones that exchange material during crossing over?",
   choices=[
     "Because those chromatids belong to different members of a homologous pair, so the exchange combines material from two sources",
     "Because sister chromatids are located in different cells at that stage",
     "Because sister chromatids have already separated by prophase I",
     "Because only non-sister chromatids are attached to the meiotic spindle",
     "Because non-sister chromatids are the only chromatids present before meiosis II"],
   ans=0,
   why="EK 5.2.A.2 names non-sister chromatids specifically, and EK 5.1.A.2.i has homologous chromosomes pair up in prophase I, which is what puts chromatids from two different chromosomes alongside one another. EK 5.1.A.2.iii keeps sister chromatids attached until the second division."),

 dict(q="A gamete is found to carry a combination of markers on one chromosome that appears in neither of the chromosomes its parent cell started with. Which process does the framework's account point to?",
   choices=[
     "Crossing over between non-sister chromatids during prophase I",
     "Nondisjunction during meiosis I",
     "Random assortment of whole chromosomes during meiosis",
     "Fertilization of that gamete by another gamete",
     "Correct separation of sister chromatids during meiosis II"],
   ans=0,
   why="EK 5.2.A.2 states that non-sister chromatids exchange genetic material via crossing over, which increases genetic diversity among the resultant gametes. Assortment moves whole chromosomes and would not create a new combination within one chromosome."),

 dict(q="Two species differ in the number of homologous chromosome pairs their cells contain. What does the framework's account of random assortment imply about the gametes they produce?",
   choices=[
     "The species with more pairs can produce more different combinations of whole chromosomes",
     "The species with fewer pairs can produce more different combinations of whole chromosomes",
     "Both species can produce the same number of combinations",
     "Neither species produces more than one kind of gamete",
     "The number of pairs has no bearing on the combinations available"],
   ans=0,
   why="EK 5.2.A.3 names random assortment of chromosomes during meiosis as a source of genetic variation, and EK 5.2.A.1 makes each haploid set an assortment of maternal and paternal chromosomes, so more independently assorting pairs allow more distinct assortments."),

 dict(q="A gamete is found to contain one more chromosome than the haploid number for its species. Which process does the framework's account point to?",
   choices=[
     "Incorrect separation during meiosis, which the framework calls nondisjunction",
     "Crossing over between non-sister chromatids during prophase I",
     "Random assortment of chromosomes during meiosis",
     "Fertilization of the gamete by another gamete",
     "Correct separation of homologous chromosomes during meiosis I"],
   ans=0,
   why="EK 5.2.A.1 states that when incorrect separation occurs, nondisjunction, gametes are no longer haploid. Crossing over and assortment change combinations without changing the number of chromosomes a gamete receives."),

 dict(q="Which observation would best justify the claim that crossing over has occurred in an organism's meiosis?",
   choices=[
     "Gametes appear carrying marker combinations on one chromosome that neither parental chromosome carried",
     "Gametes appear carrying the normal haploid number of chromosomes",
     "Gametes appear in equal numbers from each meiosis observed",
     "Gametes are produced in a shorter time than in a related species",
     "Gametes are larger than the body cells that produced them"],
   ans=0,
   why="EK 5.2.A.2 states that non-sister chromatids exchange genetic material via crossing over, which increases genetic diversity among the resultant gametes. A new combination within a single chromosome is the observable signature of that exchange."),

 dict(q="Why does the framework describe the haploid set a gamete receives as an ASSORTMENT of maternal and paternal chromosomes rather than as one parent's set?",
   choices=[
     "Because which member of each homologous pair a gamete receives is settled independently for each pair",
     "Because each gamete receives a complete copy of both parents' chromosomes",
     "Because the maternal and paternal chromosomes fuse into single chromosomes before separation",
     "Because gametes are produced only from maternal cells",
     "Because the parental chromosomes are destroyed and replaced during meiosis"],
   ans=0,
   why="EK 5.2.A.1 says each gamete receives a haploid set that comprises an assortment of both maternal and paternal chromosomes, and EK 5.2.A.3 names random assortment of chromosomes during meiosis as one of the contributors to variation."),

 dict(q="Which of these is NOT one of the contributors to genetic variation the framework names for sexual reproduction in eukaryotes?",
   choices=[
     "Mitosis of body cells during growth and tissue repair",
     "Crossing over during prophase I",
     "Random assortment of chromosomes during meiosis",
     "Fertilization of gametes",
     "The exchange of genetic material between non-sister chromatids"],
   ans=0,
   why="EK 5.2.A.3 names crossing over, random assortment and fertilization. EK 4.5.B.1 makes mitosis a process producing two genetically IDENTICAL daughter cells, which is the opposite of a source of variation."),

 dict(q="Two processes both increase the variety of gametes an organism can produce, but only one of them creates new combinations WITHIN a single chromosome. Which pairing is correct?",
   choices=[
     "Crossing over creates new combinations within a chromosome; random assortment rearranges whole chromosomes",
     "Random assortment creates new combinations within a chromosome; crossing over rearranges whole chromosomes",
     "Both create new combinations within a chromosome",
     "Both rearrange whole chromosomes only",
     "Neither affects the combinations a gamete receives"],
   ans=0,
   why="EK 5.2.A.2 has non-sister chromatids EXCHANGE GENETIC MATERIAL, which alters what a single chromosome carries, while EK 5.2.A.3's random assortment concerns which whole chromosomes a gamete receives."),

 dict(q="Which statement about meiosis and genetic diversity is NOT supported by the framework?",
   choices=[
     "Nondisjunction produces gametes that are more reliably haploid than normal separation does",
     "Crossing over increases genetic diversity among the resultant gametes",
     "Correct separation gives each gamete an assortment of maternal and paternal chromosomes",
     "Fertilization of gametes contributes to genetic variation",
     "Crossing over occurs during prophase I between non-sister chromatids"],
   ans=0,
   why="EK 5.2.A.1 states that when incorrect separation occurs, nondisjunction, gametes are NO LONGER HAPLOID. The other four options restate EK 5.2.A.2, EK 5.2.A.1 and EK 5.2.A.3 directly."),

 dict(q="Taken together, how does the framework account for the genetic diversity of the offspring of sexual reproduction?",
   choices=[
     "Exchange between non-sister chromatids, independent assortment of chromosomes, and the fusion of two separately produced gametes",
     "Identical copying of the parental genome followed by division into four cells",
     "Repeated nondisjunction, which is the only source of new combinations",
     "The action of a spindle apparatus, which is the only difference between meiosis and mitosis",
     "The exchange of material between sister chromatids during the second division"],
   ans=0,
   why="EK 5.2.A.3 names crossing over, random assortment of chromosomes during meiosis and subsequent fertilization of gametes, and EK 5.2.A.2 supplies the mechanism of the first of those."),
]
