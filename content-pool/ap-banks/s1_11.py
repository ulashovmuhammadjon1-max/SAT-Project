# AP STATISTICS 1.11 Random Sampling — 25 questions
# CED: Fall 2026, Unit 1. Learning objectives 1.11.A (identify a sampling method
# from a description of a study) and 1.11.B (justify why a method suits a
# particular population).
#
# The five ideas in EK 1.11.A.1 through 1.11.A.6:
#   sampling without replacement / with replacement;
#   simple random sample -- every sample of size n equally likely;
#   stratified random sample -- population split into non-overlapping strata,
#     then a random sample drawn WITHIN each stratum;
#   cluster random sample -- population split into clusters, then whole clusters
#     chosen at random, ideally each cluster mirroring the population;
#   systematic random sample -- a random start, then every kth unit.
#
# The stratified/cluster pair is the one students reverse, so several items here
# hinge on the operative difference: stratified samples *within every group*,
# cluster takes *entire groups*. Strata are built to be internally similar and
# different from one another; clusters are meant to each resemble the whole.
#
# A few items count how many units a systematic or stratified plan produces;
# those are recomputed in verify_s1_11.py.
TOPIC = ("1.11", "Random Sampling", 1)

QUESTIONS = [
 dict(q="Sampling without replacement is a strategy in which",
   choices=[
     "an observational unit can be selected only once",
     "an observational unit can be selected more than once",
     "no random mechanism is used",
     "the entire population is measured",
     "units are chosen because they are convenient"],
   ans=0,
   why="Without replacement, once a unit has been drawn it is set aside and cannot be drawn again."),

 dict(q="Sampling with replacement is a strategy in which",
   choices=[
     "each unit may be selected at most once",
     "an observational unit can be selected more than once",
     "the sample must equal the population",
     "only volunteers are used",
     "the sample is chosen without any randomization"],
   ans=1,
   why="With replacement, a selected unit is returned to the population and remains eligible to be drawn again."),

 dict(q="In a simple random sample of size n,",
   choices=[
     "every sample of size n has the same chance of being selected",
     "every individual has a different chance of being selected",
     "the population must first be divided into groups",
     "only the first n individuals on a list are used",
     "every kth individual is chosen after a random start"],
   ans=0,
   why="The defining property of an SRS is that all samples of the given size are equally likely, which is stronger than merely giving each individual an equal chance."),

 dict(q="A sampling method in which the population is divided into non-overlapping groups and then a random sample is taken from within EVERY group is called",
   choices=[
     "a cluster random sample",
     "a stratified random sample",
     "a systematic random sample",
     "a convenience sample",
     "a census"],
   ans=1,
   why="Stratified sampling samples inside each stratum, so every group is represented in the final sample."),

 dict(q="A sampling method in which the population is divided into groups and then a number of ENTIRE groups are selected at random is called",
   choices=[
     "a stratified random sample",
     "a cluster random sample",
     "a systematic random sample",
     "a simple random sample",
     "a voluntary response sample"],
   ans=1,
   why="Cluster sampling selects whole clusters and measures everyone in the chosen clusters, rather than sampling within every group."),

 dict(q="A sampling method in which members are selected from an ordered list according to a random starting point and then a fixed interval is called",
   choices=[
     "a stratified random sample",
     "a cluster random sample",
     "a systematic random sample",
     "a simple random sample",
     "a convenience sample"],
   ans=2,
   why="A systematic random sample picks a random start and then takes every kth unit from that point on."),

 dict(q="In a stratified random sample, the strata are ideally formed so that individuals within a stratum are",
   choices=[
     "similar to one another with respect to the variable of interest, while the strata differ from one another",
     "as different from one another as possible within each stratum",
     "chosen by the individuals themselves",
     "all measured without any randomization",
     "identical in number to the clusters"],
   ans=0,
   why="Strata that are internally homogeneous and mutually different are what make stratification reduce the variability of the estimate."),

 dict(q="In a cluster random sample, each cluster is ideally formed so that it",
   choices=[
     "contains only individuals who are alike",
     "mirrors the population as a whole",
     "contains exactly one individual",
     "is chosen by the researcher for convenience",
     "excludes part of the population"],
   ans=1,
   why="A cluster is meant to be a miniature of the population, so that a few whole clusters together represent it well."),

 dict(q="A school has 1,200 students listed alphabetically. A researcher generates a random number between 1 and 20, gets 7, and then surveys the 7th student, the 27th, the 47th, and so on. This is",
   choices=[
     "a simple random sample",
     "a stratified random sample",
     "a cluster random sample",
     "a systematic random sample",
     "a convenience sample"],
   ans=3,
   why="A random start followed by every 20th student on the list is the definition of a systematic random sample."),

 dict(q="In that systematic sample of the 1,200 alphabetically listed students, taking every 20th student starting at number 7, how many students are selected?",
   choices=["7", "20", "60", "120", "240"],
   ans=2,
   why="Starting at 7 and stepping by 20 through 1,200 selects 1,200/20 = 60 students."),

 dict(q="A university has 8,000 undergraduates and 2,000 graduate students. A researcher randomly selects 80 undergraduates and 20 graduate students. This is",
   choices=[
     "a simple random sample of 100 students",
     "a stratified random sample, with the two student types as strata",
     "a cluster random sample, with the two student types as clusters",
     "a systematic random sample",
     "a voluntary response sample"],
   ans=1,
   why="The population was split into two non-overlapping groups and a random sample was drawn within each, which is stratification."),

 dict(q="In that university sample, the fraction of undergraduates selected and the fraction of graduate students selected are",
   choices=[
     "both 0.01, so the strata are sampled proportionally",
     "0.01 and 0.10 respectively",
     "0.10 and 0.01 respectively",
     "both 0.10",
     "impossible to determine"],
   ans=0,
   why="80 of 8,000 is 0.01 and 20 of 2,000 is 0.01, so each stratum was sampled at the same rate and the sample mirrors the population's composition."),

 dict(q="A city has 300 apartment buildings. A researcher randomly selects 12 of the buildings and surveys every household in each of those 12 buildings. This is",
   choices=[
     "a stratified random sample",
     "a cluster random sample",
     "a systematic random sample",
     "a simple random sample of households",
     "a census"],
   ans=1,
   why="Whole buildings were chosen at random and everyone inside the chosen ones was surveyed, which is cluster sampling."),

 dict(q="A teacher writes each of 30 students' names on identical slips, mixes them thoroughly, and draws 6 slips without looking. This is",
   choices=[
     "a systematic random sample",
     "a simple random sample",
     "a stratified random sample",
     "a cluster random sample",
     "a convenience sample"],
   ans=1,
   why="Every group of 6 students is equally likely to be the one drawn, which is what makes it a simple random sample."),

 dict(q="A researcher stands outside a shopping centre and interviews the first 50 people who walk past and agree to talk. This is",
   choices=[
     "a simple random sample",
     "a systematic random sample",
     "a stratified random sample",
     "a convenience sample, which is not a random sampling method",
     "a cluster random sample"],
   ans=3,
   why="Nothing random governs who is approached or who agrees, so this is a convenience sample and gives no basis for generalizing to a wider population."),

 dict(q="Which statement correctly distinguishes stratified sampling from cluster sampling?",
   choices=[
     "Stratified sampling takes some units from every group; cluster sampling takes every unit from some groups",
     "Stratified sampling takes every unit from some groups; cluster sampling takes some units from every group",
     "The two methods are different names for the same procedure",
     "Stratified sampling uses no randomization; cluster sampling does",
     "Cluster sampling can only be used when the population is small"],
   ans=0,
   why="The operative difference is which direction the sampling runs: stratified samples within all groups, cluster selects entire groups."),

 dict(q="A researcher wants to be certain that all four grade levels of a high school appear in the sample in proportion to their sizes. The most appropriate method is",
   choices=[
     "a simple random sample of the whole school",
     "a stratified random sample using grade level as the strata",
     "a cluster random sample of homerooms",
     "a systematic sample from an alphabetical list",
     "a convenience sample from the cafeteria"],
   ans=1,
   why="Stratifying by grade guarantees each grade is represented, and sampling each stratum at the same rate makes the representation proportional; a simple random sample would probably but not certainly achieve it."),

 dict(q="A researcher must survey households spread across a very large rural region and cannot afford to travel to scattered individual addresses. The most practical random method is",
   choices=[
     "a simple random sample of all households in the region",
     "a cluster random sample of villages, surveying every household in the selected villages",
     "a convenience sample of households near the researcher's home",
     "a census of the region",
     "a voluntary response survey"],
   ans=1,
   why="Cluster sampling concentrates the fieldwork in a few randomly chosen locations, which is the situation the method exists for."),

 dict(q="A population contains 500 individuals. Which of the following is true of a simple random sample of size 50 drawn without replacement?",
   choices=[
     "Some individual could appear in the sample twice",
     "Every individual has a 50 in 500 chance of being in the sample, and no individual appears more than once",
     "Only the first 50 individuals on the list can be selected",
     "The sample must contain exactly 10 individuals from each of five groups",
     "The sample is not random unless it is repeated many times"],
   ans=1,
   why="Without replacement each individual appears at most once, and in an SRS of 50 from 500 each individual's chance of inclusion is 50/500."),

 dict(q="For a simple random sample of size 50 drawn from a population of 500, what is the probability that any one particular individual is included?",
   choices=["0.02", "0.05", "0.10", "0.50", "0.90"],
   ans=2,
   why="Each individual's chance of being in the sample is 50/500 = 0.10."),

 dict(q="A factory produces 4,800 items in a shift. An inspector selects a random starting point among the first 40 items and then inspects every 40th item after it. How many items are inspected?",
   choices=["40", "48", "80", "120", "160"],
   ans=3,
   why="Stepping by 40 through 4,800 items inspects 4,800/40 = 120 items."),

 dict(q="A population of 900 residents is divided into three strata of 300 each, and 15 residents are randomly chosen from each stratum. The total sample size is",
   choices=["15", "30", "45", "300", "900"],
   ans=2,
   why="Three strata contributing 15 residents each give 3 x 15 = 45 residents in total."),

 dict(q="Which of the following is a reason to prefer a stratified random sample over a simple random sample of the same size?",
   choices=[
     "It guarantees that every subgroup of interest is represented, and it can produce estimates that vary less from sample to sample",
     "It removes the need for any randomization",
     "It allows the researcher to choose which individuals are most interesting",
     "It always produces a larger sample",
     "It makes a cause-and-effect conclusion possible"],
   ans=0,
   why="Guaranteed representation of every stratum, and lower variability when the strata really do differ, are the reasons to stratify; no sampling method by itself supports a causal claim."),

 dict(q="A systematic random sample can give a misleading picture of a population when",
   choices=[
     "the population list has a repeating pattern whose period matches the sampling interval",
     "the population is very large",
     "the starting point is chosen at random",
     "the sampling interval is an odd number",
     "the sample is taken without replacement"],
   ans=0,
   why="If the list cycles with the same period as the interval, every selected unit can land in the same position of the cycle, so the sample systematically misses the rest."),

 dict(q="All four of the random sampling methods in this topic share the property that",
   choices=[
     "they divide the population into groups first",
     "they use a random mechanism to decide which units are measured, which is what supports generalizing to the population",
     "they measure the entire population",
     "they permit a cause-and-effect conclusion",
     "they require the sample size to be at least 30"],
   ans=1,
   why="Simple, stratified, cluster and systematic sampling all rely on chance rather than on the researcher's judgement, and that is what licenses generalization; causation still requires random assignment."),
]
