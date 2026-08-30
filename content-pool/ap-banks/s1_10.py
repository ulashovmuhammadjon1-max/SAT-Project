# AP STATISTICS 1.10 The Investigative Question Revisited and Data Collection
# — 25 questions
# CED: Fall 2026, Unit 1. Learning objectives 1.10.A (the three components of an
# investigative question), 1.10.B (census), 1.10.C (experiment: experimental
# unit, explanatory variable/factor, levels, treatments, response variable),
# 1.10.D (observational study: prospective, retrospective, survey, confounding)
# and 1.10.E (when a generalization is justified).
#
# This is the topic where RANDOM SELECTION is established as the thing that
# licenses generalizing to a population (EK 1.10.E.2/1.10.E.4). Random
# ASSIGNMENT, which is what licenses a cause-and-effect conclusion, belongs to
# topic 1.13. Students conflate the two constantly, so here they are tested
# apart -- every generalization item in this module turns on selection alone --
# and 1.13 tests them together.
#
# Two items count treatments from a factorial design, which is the only
# arithmetic in the topic; both are recomputed in verify_s1_10.py.
TOPIC = ("1.10", "The Investigative Question Revisited and Data Collection", 1)

QUESTIONS = [
 dict(q="The first component of a well-posed investigative question should",
   choices=[
     "guide the data collection process and be phrased in terms of the variable or variables of interest",
     "state the researcher's expected answer",
     "name the statistical software that will be used",
     "report the size of the population",
     "specify the significance level"],
   ans=0,
   why="The opening component tells the researcher what to go and measure, so it has to name the variables of interest."),

 dict(q="The second component of a well-posed investigative question should",
   choices=[
     "guide the choice of data analysis",
     "list the individuals who will be sampled by name",
     "report the results already obtained",
     "describe the graph that will be drawn",
     "state the cost of the study"],
   ans=0,
   why="The second component points to the analysis: it makes clear whether a parameter is being estimated with an interval or tested against a stated alternative."),

 dict(q="The third component of a well-posed investigative question should indicate",
   choices=[
     "the type of conclusion the study supports, including the population the conclusion applies to",
     "the number of pages in the final report",
     "the mean of the data before it is collected",
     "which statistic will be largest",
     "the names of the researchers"],
   ans=0,
   why="The third component fixes the scope of the conclusion: which population it extends to, and whether a cause-and-effect claim is available."),

 dict(q="Recording information from all items or individuals in a population is called",
   choices=["a sample", "a census", "an experiment", "a survey of volunteers", "a retrospective study"],
   ans=1,
   why="A census measures the entire population rather than a subset of it."),

 dict(q="A study in which a researcher assigns conditions, or treatments, to units in order to explore an investigative question is",
   choices=[
     "an observational study",
     "a census",
     "an experiment",
     "a retrospective study",
     "a survey"],
   ans=2,
   why="Imposing treatments on the units is exactly what distinguishes an experiment from an observational study."),

 dict(q="In an experiment, the observational unit to which a treatment is assigned is called",
   choices=[
     "the response variable",
     "the experimental unit",
     "the factor",
     "the population",
     "the confounding variable"],
   ans=1,
   why="The unit receiving the treatment is the experimental unit, and when those units are people they are often called subjects or participants."),

 dict(q="In an experiment, a variable whose different categories are imposed on the experimental units is called",
   choices=[
     "the response variable",
     "a confounding variable",
     "an explanatory variable, or factor",
     "the sampling frame",
     "the parameter"],
   ans=2,
   why="The imposed variable is the explanatory variable, also called a factor, and its categories are its levels."),

 dict(q="In an experiment, the outcome measured on each experimental unit after the treatment has been administered is",
   choices=[
     "the explanatory variable",
     "the response variable",
     "the factor",
     "the treatment",
     "the experimental unit"],
   ans=1,
   why="What is measured afterward, to see what the treatment did, is the response variable."),

 dict(q="A researcher tests one factor at four levels. How many treatments does this experiment have?",
   choices=["1", "2", "4", "8", "16"],
   ans=2,
   why="With a single factor, each level is itself a treatment, so four levels give four treatments."),

 dict(q="An experiment uses two explanatory variables: fertilizer type at 3 levels and watering schedule at 2 levels, in every combination. How many treatments are there?",
   choices=["2", "3", "5", "6", "12"],
   ans=3,
   why="With more than one factor the treatments are the combinations of levels, so 3 x 2 = 6; the sum 3 + 2 = 5 is the common error."),

 dict(q="An experiment crosses three factors, at 2, 2, and 3 levels respectively, in every combination. How many treatments are there?",
   choices=["3", "7", "8", "12", "18"],
   ans=3,
   why="The treatments are all combinations of levels, so 2 x 2 x 3 = 12; the sum 2 + 2 + 3 = 7 is the common error."),

 dict(q="A study in which treatments are NOT imposed, and the researcher simply records the values of the variables of interest, is",
   choices=[
     "an experiment",
     "an observational study",
     "a census by definition",
     "always biased",
     "a randomized comparative design"],
   ans=1,
   why="An observational study records what is already there rather than assigning conditions."),

 dict(q="A study in which the units are selected at a point in time and data are then gathered at that time and into the future is called",
   choices=["retrospective", "prospective", "a census", "an experiment", "a cross-over design"],
   ans=1,
   why="A prospective study follows its units forward in time from the moment they are selected."),

 dict(q="A study in which the units are selected at a point in time and data from the PAST are gathered is called",
   choices=["prospective", "retrospective", "an experiment", "a census", "a randomized block design"],
   ans=1,
   why="A retrospective study looks backward, assembling data about the units from before they were selected."),

 dict(q="An observational study in which data are collected from people using a standard set of questions is called",
   choices=["a census", "an experiment", "a survey", "a retrospective study", "a treatment"],
   ans=2,
   why="A survey is the particular kind of observational study that gathers answers to a fixed set of questions."),

 dict(q="For a variable to be a confounding variable in an observational study, it must be",
   choices=[
     "associated with the explanatory variable only",
     "associated with the response variable only",
     "associated with both the explanatory variable and the response variable",
     "measured on a different set of individuals",
     "assigned at random by the researcher"],
   ans=2,
   why="A confounder offers an alternative explanation for the observed relationship, which requires it to be linked to both variables at once."),

 dict(q="A study finds that people who drink more coffee have higher rates of lung cancer. Smoking is more common among heavy coffee drinkers and is itself a cause of lung cancer. In this study, smoking is",
   choices=[
     "the response variable",
     "the explanatory variable",
     "a confounding variable, because it is associated with both coffee drinking and lung cancer",
     "an experimental unit",
     "irrelevant, because coffee and smoking are different substances"],
   ans=2,
   why="Smoking is associated with the explanatory variable and is a cause of the response, so it offers an alternative explanation for the coffee-cancer link."),

 dict(q="A researcher records how many hours each of 400 randomly selected employees slept last night and their score on an alertness test the next morning. No conditions were imposed. This study is",
   choices=[
     "an experiment, because two variables were measured",
     "an observational study, because the researcher did not assign how much anyone slept",
     "a census, because 400 is a large number",
     "an experiment, because the sample was random",
     "not a statistical study at all"],
   ans=1,
   why="Nothing was imposed on anyone; sleep hours were merely recorded, which makes this observational however the sample was chosen."),

 dict(q="A researcher randomly assigns each of 60 volunteers to sleep either 6 hours or 8 hours for one week and then measures their alertness. This study is",
   choices=[
     "an observational study, because sleep is a natural behaviour",
     "an experiment, because the researcher imposed the sleep conditions on the units",
     "a census of the 60 volunteers",
     "a survey",
     "a retrospective study"],
   ans=1,
   why="The researcher assigned the amount of sleep rather than recording it, and assigning conditions is what makes a study an experiment."),

 dict(q="In the sleep experiment above, the response variable is",
   choices=[
     "the amount of sleep assigned",
     "the alertness measured after the week",
     "the 60 volunteers",
     "the random assignment",
     "the researcher's hypothesis"],
   ans=1,
   why="Alertness is the outcome measured after the treatment was administered, which is the definition of the response variable."),

 dict(q="A sample is considered random when",
   choices=[
     "the researcher picks units without thinking carefully about them",
     "all observational units in the sample are selected from the population using some type of random mechanism",
     "the units volunteer themselves",
     "the sample size is at least 30",
     "every unit in the sample happens to be different"],
   ans=1,
   why="Randomness is a property of the selection mechanism, such as a random number generator, not of how haphazard the result looks."),

 dict(q="A university selects 500 of its 20,000 students using a random number generator and surveys them about campus dining. Generalizing the results to all 20,000 students is",
   choices=[
     "appropriate, because the units were randomly selected from that population",
     "inappropriate, because 500 is far fewer than 20,000",
     "appropriate only if every student responds",
     "inappropriate, because no treatment was assigned",
     "appropriate only if the students were also randomly assigned to groups"],
   ans=0,
   why="Random selection from the population of interest is exactly what licenses generalizing to that population; no treatment was assigned, so no causal claim follows, but the generalization does."),

 dict(q="A researcher posts a questionnaire online and analyzes the responses of the 800 people who chose to fill it in. The conclusions may appropriately be generalized to",
   choices=[
     "all internet users worldwide",
     "everyone in the researcher's country",
     "only a population of individuals similar to those who chose to respond",
     "all 800 respondents and no one else, including themselves",
     "any population the researcher names in advance"],
   ans=2,
   why="Volunteers are not a random sample, so generalization is limited to individuals similar to those actually studied."),

 dict(q="Which statement correctly describes what random selection does and does not permit?",
   choices=[
     "Random selection permits generalizing to the population sampled, but by itself does not permit a cause-and-effect conclusion",
     "Random selection permits a cause-and-effect conclusion, but not generalization",
     "Random selection permits both generalization and a cause-and-effect conclusion",
     "Random selection permits neither generalization nor a cause-and-effect conclusion",
     "Random selection is only relevant in experiments"],
   ans=0,
   why="How units are chosen fixes the population a conclusion reaches; establishing causation instead requires that treatments be randomly assigned."),

 dict(q="A biologist deliberately chooses the 40 trees nearest the road because they are easiest to reach, then measures each tree's height. The main limitation of this study is that",
   choices=[
     "the sample size is too small for any analysis",
     "heights cannot be measured accurately on trees",
     "the trees were deliberately chosen rather than randomly selected, so conclusions extend only to trees similar to those studied",
     "no response variable was measured",
     "the study is an experiment without a control group"],
   ans=2,
   why="Deliberate selection is not random selection, so the results describe roadside trees rather than the forest as a whole."),
]
