# AP STATISTICS 1.13 Experimental Design — 25 questions
# CED: Fall 2026, Unit 1. Learning objectives 1.13.A (elements of a well-designed
# experiment), 1.13.B (completely randomized, randomized block and matched pairs
# designs) and 1.13.C (justifying the choice of design).
#
# This is where RANDOM ASSIGNMENT is established as the thing that licenses a
# cause-and-effect conclusion (EK 1.13.A.7). Topic 1.11 established that random
# SELECTION licenses generalizing to a population. Students merge the two, so
# this module tests them apart and then, in the last four items, together across
# all four combinations:
#     random selection + random assignment -> generalize AND conclude causation
#     random assignment only              -> causation, but only for these units
#     random selection only               -> generalize, but no causation
#     neither                             -> neither
#
# Design vocabulary that is routinely swapped, and is tested against its
# neighbour here:
#   blocking (experiments, groups units by an extraneous variable BEFORE random
#     assignment) against stratifying (sampling, groups the population before
#     random selection);
#   matched pairs, which is a randomized block design with exactly two
#     treatments and blocks of size two;
#   single-blind against double-blind;
#   replication (more than one unit per treatment) against repeating a study.
TOPIC = ("1.13", "Experimental Design", 1)

QUESTIONS = [
 dict(q="Which of the following is NOT one of the elements of a well-designed experiment?",
   choices=[
     "Comparison of at least two treatment groups",
     "Random assignment of treatments to experimental units",
     "Replication",
     "Random selection of the experimental units from a larger population",
     "Direct control of potential extraneous sources of variation"],
   ans=3,
   why="Comparison, random assignment, replication and direct control are the four elements; random selection is a sampling matter that determines generalizability, not a requirement of good experimental design."),

 dict(q="In an experiment, a control group is",
   choices=[
     "a collection of experimental units created for comparison, which may receive a placebo or a different treatment",
     "the group that receives the largest dose",
     "the group of units excluded from the study",
     "the researchers who run the experiment",
     "the population from which units were drawn"],
   ans=0,
   why="A control group exists to give the treatment of interest something to be compared against."),

 dict(q="The placebo effect is",
   choices=[
     "the difference between the average response to a placebo and the average response to no treatment",
     "the tendency of a real drug to work better than expected",
     "the failure of an experiment to include a control group",
     "the difference between two active treatments",
     "an error made in recording responses"],
   ans=0,
   why="It is the response produced by the act of receiving something inert, measured against receiving nothing at all."),

 dict(q="In a single-blind experiment,",
   choices=[
     "neither the participants nor the researchers interacting with them know which treatment each participant receives",
     "participants do not know which treatment they receive, but the researchers interacting with them do",
     "the researchers do not know the purpose of the study",
     "no one is assigned a treatment",
     "the response variable is not measured"],
   ans=1,
   why="One party is masked in a single-blind study, and it is the participants."),

 dict(q="In a double-blind experiment,",
   choices=[
     "participants know their treatment but researchers do not",
     "neither the participants nor the members of the research team who interact with them know which treatment each participant is receiving",
     "the study is run twice",
     "two control groups are used",
     "the data are analyzed twice by different people"],
   ans=1,
   why="Both the participants and the staff interacting with them are masked, which protects against expectations influencing either the response or its measurement."),

 dict(q="An extraneous source of variation in an experiment is",
   choices=[
     "a variable known or believed to affect the response but which is not an explanatory variable being studied",
     "the response variable itself",
     "any variable measured with error",
     "the treatment with the largest effect",
     "a variable that has no effect on anything"],
   ans=0,
   why="Extraneous variables affect the response without being what the experiment is about, which is why they are controlled, blocked on, or randomized away."),

 dict(q="The purpose of random assignment in an experiment is to",
   choices=[
     "create treatment groups that are as similar as possible with respect to extraneous sources of variation",
     "make the sample representative of a larger population",
     "guarantee that each treatment group has exactly the same number of units",
     "eliminate the need for a control group",
     "remove the need to measure the response variable"],
   ans=0,
   why="Randomly assigning units balances the extraneous variables across groups on average, so a difference in response can be attributed to the treatment."),

 dict(q="Replication within an experiment means that",
   choices=[
     "the entire experiment is repeated by a different research team",
     "more than one experimental unit is assigned to each treatment",
     "each unit receives the treatment more than once",
     "the results are published twice",
     "two response variables are measured"],
   ans=1,
   why="Replication in the design sense is having several units per treatment, so that the variation among units can be seen and the treatment effect distinguished from it."),

 dict(q="Direct control in an experiment means",
   choices=[
     "keeping the settings of certain potential extraneous variables the same from unit to unit",
     "assigning treatments at random",
     "using a control group",
     "controlling who is selected into the sample",
     "deciding the results in advance"],
   ans=0,
   why="Direct control holds an extraneous variable fixed for everyone, so it cannot vary and therefore cannot explain any difference in the response."),

 dict(q="A confounding variable in an experiment is one that",
   choices=[
     "is related to the explanatory variable in such a way that it becomes impossible to tell which of the two is producing the change in the response",
     "has no relationship with any other variable",
     "is the same as the response variable",
     "is randomly assigned by the researcher",
     "is measured after the treatment only"],
   ans=0,
   why="Confounding means the treatment effect and the other variable's effect cannot be separated, which is precisely what random assignment is designed to prevent."),

 dict(q="In a completely randomized design, treatments are",
   choices=[
     "assigned to experimental units completely at random",
     "assigned according to which units the researcher expects to respond best",
     "assigned only after the units are grouped by an extraneous variable",
     "given to every unit in turn",
     "never compared with a control"],
   ans=0,
   why="A completely randomized design imposes no prior grouping; every unit is assigned by chance alone, and the group sizes need not be equal."),

 dict(q="In a randomized block design, the experimental units are",
   choices=[
     "first grouped by similar values of an extraneous variable, and then treatments are randomly assigned within each group",
     "randomly assigned to treatments with no prior grouping",
     "grouped after the treatments have been given",
     "chosen by the participants themselves",
     "assigned the same treatment within each group"],
   ans=0,
   why="Blocks are formed first from an extraneous source of variation, and the randomization then happens separately inside each block."),

 dict(q="The purpose of blocking in an experiment is to",
   choices=[
     "separate the variation in the response caused by the blocking variable from the rest of the extraneous variation, allowing more precise comparisons among treatments",
     "increase the number of experimental units",
     "make a cause-and-effect conclusion possible where random assignment alone would not",
     "guarantee the sample represents the population",
     "remove the need for randomization"],
   ans=0,
   why="Blocking pulls a known source of variation out of the comparison, which sharpens the estimate of the treatment effect; randomization still happens within blocks."),

 dict(q="A matched pairs design is best described as",
   choices=[
     "a completely randomized design with exactly two treatments",
     "a randomized block design with exactly two treatments, in which units are matched in pairs and each pair receives both treatments in random order, or each unit serves as its own pair",
     "an observational study of two groups",
     "a design in which two researchers each run half the experiment",
     "a design with two response variables"],
   ans=1,
   why="Matched pairs is the special case of blocking where each block is a pair and there are two treatments, with the assignment randomized inside each pair."),

 dict(q="Twenty pairs of identical twins take part in a study of two teaching methods. Within each pair, a coin flip decides which twin gets Method A and which gets Method B. This is",
   choices=[
     "a completely randomized design",
     "an observational study",
     "a matched pairs design",
     "a design with no randomization",
     "a stratified random sample"],
   ans=2,
   why="The twins form natural pairs matched on many extraneous variables, and the two treatments are randomly assigned within each pair."),

 dict(q="A researcher has 60 plants of two clearly different varieties and wants to compare three fertilizers. Because variety strongly affects growth, the best design is to",
   choices=[
     "assign all 60 plants to the three fertilizers completely at random, ignoring variety",
     "block by variety, then randomly assign the three fertilizers within each variety",
     "give one variety one fertilizer and the other variety another",
     "use only one variety and discard the rest",
     "let each plant's grower choose its fertilizer"],
   ans=1,
   why="Variety is a known extraneous source of variation, so blocking on it removes that variation from the fertilizer comparison; assigning by variety would confound the two."),

 dict(q="Blocking in an experiment and stratifying in a sample are analogous in that both",
   choices=[
     "group units by a variable before randomization, in order to reduce variability",
     "allow a cause-and-effect conclusion",
     "eliminate the need for randomization",
     "require exactly two groups",
     "are used only when the population is small"],
   ans=0,
   why="Both form groups first and randomize within them to reduce variability, but blocking sits inside an experiment while stratifying sits inside a sampling plan."),

 dict(q="An experiment compares a new painkiller with a placebo. Neither the patients nor the nurses handing out the pills know which is which. The main reason for this arrangement is to",
   choices=[
     "prevent expectations of either the patients or the staff from systematically influencing the reported responses",
     "make the study cheaper to run",
     "allow the sample to be generalized to the population",
     "increase the number of treatments",
     "avoid the need for random assignment"],
   ans=0,
   why="Double-blinding removes the systematic effect of belief about which treatment was given, from the participants and from the people who interact with them."),

 dict(q="A well-designed experiment finds that units receiving Treatment A had a significantly better mean response than those receiving Treatment B. The experimental units were 200 volunteers, randomly assigned to the two treatments. The appropriate conclusion is that",
   choices=[
     "Treatment A causes a better response, and this conclusion extends to the whole population",
     "Treatment A causes a better response among volunteers like those studied, but the result cannot be generalized to a wider population",
     "Treatment A is associated with a better response, but no causal claim is possible",
     "no conclusion of any kind is possible",
     "the volunteers must have been randomly selected for the assignment to work"],
   ans=1,
   why="Random assignment supports the causal claim, but because the units were volunteers rather than a random sample, the conclusion does not extend beyond individuals like them."),

 dict(q="A study randomly selects 500 adults from a national register and records how much each exercises and their blood pressure. Those who exercise more tend to have lower blood pressure. The appropriate conclusion is that",
   choices=[
     "exercising more causes lower blood pressure in the national population",
     "more exercise is associated with lower blood pressure in the national population, but no causal conclusion is justified because exercise was not assigned",
     "no conclusion may be drawn, because the sample is only 500 of many millions",
     "exercising more causes lower blood pressure, but only for these 500 adults",
     "blood pressure causes people to exercise"],
   ans=1,
   why="Random selection licenses generalizing the association to the national population, but nothing was assigned, so a confounding variable such as overall health could explain the pattern."),

 dict(q="Researchers randomly select 300 patients from all patients at a large hospital network and then randomly assign each to one of two therapies. A significant difference in outcome is found. This design supports",
   choices=[
     "a causal conclusion that generalizes to the hospital network's patient population",
     "a causal conclusion that applies only to the 300 patients studied",
     "generalization to the network, but no causal conclusion",
     "neither generalization nor a causal conclusion",
     "a causal conclusion about all patients everywhere"],
   ans=0,
   why="Random selection from the network's patients supports generalizing to that population, and random assignment of the therapies supports the causal claim; both are present, so both conclusions are available."),

 dict(q="A teacher lets students choose whether to attend an optional review session, then compares exam scores of attendees and non-attendees. Attendees score higher. The most important limitation is that",
   choices=[
     "students were not randomly assigned to attend, so more motivated students may have self-selected into the session and motivation, not the session, may explain the difference",
     "the sample size is too small",
     "exam scores are a categorical variable",
     "the teacher should have used a matched pairs design with three treatments",
     "there is no response variable"],
   ans=0,
   why="Without random assignment the groups differ in ways beyond the treatment, so motivation is confounded with attendance and no causal claim about the session is available."),

 dict(q="Which change to a study would newly make a cause-and-effect conclusion available?",
   choices=[
     "Increasing the sample size from 200 to 2,000",
     "Selecting the units by simple random sampling instead of by convenience",
     "Randomly assigning the treatments instead of letting units choose their own",
     "Measuring the response variable more precisely",
     "Reporting a confidence interval instead of a single estimate"],
   ans=2,
   why="Only random assignment balances extraneous variables across the treatment groups; the other changes improve precision or generalizability but leave confounding untouched."),

 dict(q="An experiment assigns 5 experimental units to each of 4 treatments. Compared with an otherwise identical experiment assigning 25 units to each treatment, the smaller experiment",
   choices=[
     "has more replication and so gives a more precise comparison",
     "has less replication, so ordinary unit-to-unit variation is harder to distinguish from a real treatment effect",
     "is biased, while the larger one is not",
     "cannot use random assignment",
     "has more treatments"],
   ans=1,
   why="Both designs have replication, but with only five units per treatment the natural variation among units makes a genuine treatment difference much harder to detect."),

 dict(q="A researcher runs an experiment on 40 volunteers with no control group, giving every volunteer the new treatment and observing improvement in most of them. The most serious flaw is that",
   choices=[
     "there is nothing to compare the treated group against, so the improvement cannot be attributed to the treatment rather than to a placebo effect or natural recovery",
     "40 is an even number of units",
     "volunteers cannot be used in experiments",
     "the response variable was measured after the treatment",
     "the treatment should have been assigned at random to the single group"],
   ans=0,
   why="A well-designed experiment compares at least two treatment groups; with only one group there is no way to know what would have happened without the treatment."),
]
