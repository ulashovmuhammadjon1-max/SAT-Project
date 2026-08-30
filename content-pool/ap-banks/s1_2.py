# AP STATISTICS 1.2 Variables — 25 questions
# CED: Fall 2026, Unit 1. Learning objectives 1.2.A (identify observational units,
# variables, parameters and statistics), 1.2.B (types of variables) and 1.2.C
# (discrete vs continuous quantitative variables).
#
# The parameter-versus-statistic distinction is the most-missed idea in this topic
# and is tested here from several directions: by definition, by notation
# (mu, sigma, p against x-bar, s, p-hat), by which group the number describes, and
# by the numeric case where both numbers appear in one stem. The few numeric keys
# are recomputed in verify_s1_2.py; the rest are documented there as conceptual.
TOPIC = ("1.2", "Variables", 1)
QUESTIONS = [
 dict(q="An observational unit is",
   choices=[
     "a numerical summary of a population",
     "an item or individual from which a datum is collected",
     "the difference between the largest and smallest value in a data set",
     "the question a study sets out to answer",
     "the units of measure attached to a quantitative variable"],
   ans=1,
   why="An observational unit is the item or individual that a piece of data is collected from."),

 dict(q="A variable is best defined as",
   choices=[
     "a characteristic that may change from one observational unit to another",
     "any number that appears in a data set",
     "the size of the sample being studied",
     "a quantity that is fixed for the whole population",
     "the name given to a study's investigative question"],
   ans=0,
   why="A variable is a characteristic that can differ from one observational unit to the next."),

 dict(q="A numerical summary of a variable of interest for an entire population is called a",
   choices=["statistic", "sample", "parameter", "variable", "datum"],
   ans=2,
   why="A parameter summarizes a population; a statistic summarizes a sample."),

 dict(q="A numerical summary of a variable of interest computed from a sample is called a",
   choices=["parameter", "population", "statistic", "census", "observational unit"],
   ans=2,
   why="A statistic is a numerical attribute of a sample, and it is generally not equal to the population parameter it estimates."),

 dict(q="A categorical variable is one that",
   choices=[
     "takes on values that are category names or group labels",
     "always takes on whole-number values",
     "must be measured with an instrument",
     "can take on any value in an interval",
     "has units of measure such as meters or seconds"],
   ans=0,
   why="A categorical, or qualitative, variable records category names or group labels rather than measured amounts."),

 dict(q="A quantitative variable is one that",
   choices=[
     "records a group label for each individual",
     "takes on numerical values for a measured or counted quantity and generally has units of measure",
     "can only take on the values 0 and 1",
     "is always continuous",
     "cannot be summarized with a mean"],
   ans=1,
   why="A quantitative, or numerical, variable takes numerical values for something measured or counted and normally carries units."),

 dict(q="A discrete quantitative variable is one that",
   choices=[
     "can take on any value in an interval of the number line",
     "can take on a countable number of values, possibly finite and possibly countably infinite",
     "always takes on exactly five possible values",
     "is recorded as a category label",
     "must be measured rather than counted"],
   ans=1,
   why="A discrete quantitative variable takes a countable set of values; the whole numbers are a countably infinite example."),

 dict(q="A continuous quantitative variable is one that",
   choices=[
     "can take on an infinite number of possible values within a given interval, including every value between any two of them",
     "can take on only whole-number values",
     "takes on a countable number of values",
     "is the same as a categorical variable with many categories",
     "cannot be measured to more than one decimal place"],
   ans=0,
   why="A continuous variable can take every value in an interval, so between any two of its possible values there is another."),

 dict(q="A veterinarian records, for each dog brought into her clinic, the dog's breed, weight in kilograms, and number of vaccinations received. The observational units are",
   choices=[
     "the breeds",
     "the individual dogs",
     "the three variables recorded",
     "the kilograms",
     "the clinic"],
   ans=1,
   why="Data are collected from each dog, so the individual dogs are the observational units."),

 dict(q="In the veterinarian's records described above, breed, weight, and number of vaccinations are, respectively,",
   choices=[
     "categorical, categorical, quantitative",
     "categorical, quantitative continuous, quantitative discrete",
     "quantitative, quantitative, categorical",
     "categorical, quantitative discrete, quantitative continuous",
     "quantitative discrete, categorical, quantitative continuous"],
   ans=1,
   why="Breed is a group label, weight is measured and can take any value in an interval, and a count of vaccinations is a whole number."),

 dict(q="Each house on a street is labeled with a five-digit ZIP code. For a study of these houses, the ZIP code should be treated as",
   choices=[
     "a continuous quantitative variable, because it is written with digits",
     "a discrete quantitative variable, because it is a whole number",
     "a categorical variable, because the digits serve as a group label rather than a measured amount",
     "not a variable at all",
     "a parameter of the street"],
   ans=2,
   why="A ZIP code is written with digits but identifies an area rather than measuring an amount, so averaging it would be meaningless and it is categorical."),

 dict(q="Which of the following is a continuous quantitative variable?",
   choices=[
     "The number of text messages a person sent yesterday",
     "The brand of a person's phone",
     "The exact amount of time, in seconds, a person spent on a phone call",
     "The number of people in a household",
     "Whether a person owns a phone"],
   ans=2,
   why="Elapsed time can take any value in an interval, so it is continuous; the others are counts, labels, or yes-no answers."),

 dict(q="Which of the following is a discrete quantitative variable?",
   choices=[
     "The height of a sunflower plant in centimeters",
     "The number of seeds in a sunflower head",
     "The color of a sunflower's petals",
     "The mass of a sunflower seed in grams",
     "The soil type a sunflower is grown in"],
   ans=1,
   why="A count of seeds takes whole-number values and is therefore discrete; heights and masses are measured and continuous, and color and soil type are labels."),

 dict(q="A school district of 9,000 students reports, from its complete enrollment records, that exactly 46% of its students ride a bus to school. The number 46% is",
   choices=[
     "a statistic, because it is a percent",
     "a parameter, because it describes the entire population of district students",
     "a statistic, because 9,000 students is a large group",
     "a variable, because it can change",
     "an observational unit"],
   ans=1,
   why="The figure comes from every student in the population of interest, so it is a parameter rather than an estimate from a sample."),

 dict(q="In a town of 40,000 adults, a researcher surveys 500 adults and finds that 0.34 of those surveyed own a bicycle. Unknown to the researcher, 0.29 of all 40,000 adults own a bicycle. The parameter is",
   choices=["0.29", "0.34", "0.63", "500", "40,000"],
   ans=0,
   why="The parameter is the value for the whole population of 40,000 adults, which is 0.29; 0.34 came from the sample and is a statistic."),

 dict(q="In that same bicycle study, the value 0.34 is",
   choices=[
     "a parameter, because it was actually observed",
     "a statistic, because it was computed from the sample of 500 adults",
     "the population size",
     "an observational unit",
     "a categorical variable"],
   ans=1,
   why="A number computed from the sample is a statistic, whether or not it happens to be close to the parameter."),

 dict(q="Which of the following notations refers to a parameter rather than a statistic?",
   choices=["x-bar", "s", "p-hat", "mu", "the sample size n"],
   ans=3,
   why="Greek letters such as mu and sigma denote population parameters, while x-bar, s and p-hat are computed from samples."),

 dict(q="A researcher writes 'p-hat = 0.62'. This tells you that 0.62 is",
   choices=[
     "the proportion for the entire population",
     "a proportion computed from a sample",
     "a categorical variable",
     "the number of individuals sampled",
     "the standard deviation of the population"],
   ans=1,
   why="The 'hat' notation marks a sample proportion, which is a statistic estimating the population proportion p."),

 dict(q="A quality engineer measures the diameter, in millimeters, of each of 60 ball bearings drawn from a day's production of 20,000. The variable of interest in this study is",
   choices=[
     "the 60 bearings measured",
     "the 20,000 bearings produced",
     "the diameter of a bearing",
     "the mean diameter of the 60 bearings",
     "the day of production"],
   ans=2,
   why="The variable is the characteristic that changes from bearing to bearing, which is the diameter; the mean of the 60 is a statistic, not the variable."),

 dict(q="For the same ball-bearing study, the mean diameter of the 60 measured bearings is a",
   choices=[
     "parameter, because diameter is quantitative",
     "statistic, because it summarizes the sample of 60",
     "variable, because it changes from bearing to bearing",
     "observational unit",
     "population size"],
   ans=1,
   why="It is a numerical summary of the sample, so it is a statistic."),

 dict(q="A survey asks each respondent to rate a film as 'poor', 'fair', 'good', or 'excellent'. This variable is",
   choices=[
     "quantitative and discrete, because the four ratings can be numbered 1 through 4",
     "quantitative and continuous, because opinion varies smoothly",
     "categorical, because each value is a group label rather than a measured amount",
     "a parameter of the audience",
     "not a variable, because opinions cannot be recorded"],
   ans=2,
   why="Assigning numbers to ordered labels does not make them measured amounts; the recorded values are category names, so the variable is categorical."),

 dict(q="Which pair of variables is correctly classified?",
   choices=[
     "Jersey number worn by a player: quantitative; number of points scored: quantitative",
     "Jersey number worn by a player: categorical; number of points scored: quantitative",
     "Jersey number worn by a player: categorical; number of points scored: categorical",
     "Jersey number worn by a player: quantitative; number of points scored: categorical",
     "Both are continuous quantitative variables"],
   ans=1,
   why="A jersey number identifies a player rather than measuring anything, so it is categorical, while points scored is a genuine count."),

 dict(q="A botanist studies 1,200 oak trees in a forest and measures the trunk circumference of 80 of them. Which of the following correctly identifies a component of this study?",
   choices=[
     "The observational unit is the forest",
     "The observational unit is an individual oak tree",
     "The variable is the number 80",
     "The parameter is the mean circumference of the 80 trees measured",
     "The sample is the 1,200 trees"],
   ans=1,
   why="Data are collected from each tree, so an individual oak tree is the observational unit; the 80 measured trees are the sample and their mean is a statistic."),

 dict(q="Which of the following statements about parameters and statistics is correct?",
   choices=[
     "A parameter varies from sample to sample, while a statistic is a fixed number",
     "A statistic varies from sample to sample, while a parameter is a fixed number for a given population",
     "Both parameters and statistics vary from sample to sample",
     "Neither a parameter nor a statistic can be a proportion",
     "A statistic can only be computed if the population size is known"],
   ans=1,
   why="The population value is a single fixed number; the value computed from a sample changes depending on which sample is drawn."),

 dict(q="A researcher records each participant's blood type (A, B, AB, or O) and resting heart rate in beats per minute. The correct classification is",
   choices=[
     "both variables categorical",
     "both variables quantitative",
     "blood type categorical and heart rate quantitative",
     "blood type quantitative and heart rate categorical",
     "blood type categorical and heart rate a parameter"],
   ans=2,
   why="Blood type is a group label and heart rate is a counted quantity with units, so the first is categorical and the second quantitative."),
]
