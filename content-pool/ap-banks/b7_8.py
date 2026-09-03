# AP BIOLOGY 7.8 Continuing Evolution
# CED effective Fall 2025, Unit 7 Natural Selection, Big Idea 1 Evolution.
# Learning objective 7.8.A, explain how evolution is an ongoing process in all
# living organisms.
# Suggested skill 3.D, PROPOSE A NEW INVESTIGATION based on an evaluation of
# the experimental design or evidence.
#
# Essential knowledge relied on, in the framework's own terms:
#   7.8.A.1  ALL species have evolved and CONTINUE TO EVOLVE. Examples include:
#              i. genomic changes over time
#             ii. continuous change in the fossil record
#            iii. evolution of resistance to antibiotics, pesticides,
#                 herbicides, or chemotherapy drugs
#             iv. pathogens evolving and causing emergent diseases
#
# THE SHAPE OF THIS TOPIC. One essential knowledge statement with four named
# examples, and a suggested skill that is about experimental design. So half
# this module is skill 3.D: a study is described, and the question asks what
# investigation should come next or what the present design cannot settle.
# That is the ask the CED attaches to this topic, and it is what keeps thirty
# items off one sentence -- the failure mode SOCIAL_DEDUPE.md records.
#
# DELIBERATE OMISSIONS, to keep off neighbouring topics.
#  * 7.2 Natural Selection is a sibling's module and carries the framework's
#    own illustrative examples of DDT resistance and sickle cell under
#    EK 7.2.A.3. Nothing here asks whether a phenotype raises fitness, which is
#    7.2's question; every item here turns on evolution being ONGOING and
#    OBSERVABLE, or on how to investigate it.
#  * EK 8.7.A.3, that mutations are not directed by specific environmental
#    pressures, is asked in b8_7. Exactly ONE item here touches it, q19, and it
#    is posed as a design question -- what investigation would distinguish
#    pre-existing variation from change induced by the treatment -- which is
#    skill 3.D and not the content claim.
#  * Dating fossils is EK 7.6.B.1 and is asked in b7_6. The fossil items here
#    concern continuous change through a series, not how the series was dated.
#
# ON THE DATA. Both tables are HYPOTHETICAL and say so in the stem, and every
# number a key states about one is recomputed in verify_b7_8.py from that table
# alone. Every calculation is one step and calculator-free.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset.
TOPIC = ("7.8", "Continuing Evolution", 7)

_T_RESIST = dict(
    headers=["Sampling round", "Number of bacterial colonies tested",
             "Number of colonies that grew on the antibiotic"],
    rows=[["Round 1", "200", "4"],
          ["Round 2", "200", "20"],
          ["Round 3", "200", "60"],
          ["Round 4", "200", "120"]])

_T_FIELDS = dict(
    headers=["Field", "Number of seasons the insecticide has been applied",
             "Percentage of the pest population surviving the standard dose"],
    rows=[["Field J", "0", "3"],
          ["Field K", "4", "12"],
          ["Field L", "8", "31"],
          ["Field M", "12", "64"]])

QUESTIONS = [
 dict(q="Which statement best expresses what the course framework claims about evolution as a process?",
   choices=[
     "All species have evolved and continue to evolve",
     "Evolution occurred in the distant past and has since stopped in most lineages",
     "Only species under human management continue to evolve",
     "Only species with short generation times have ever evolved",
     "Evolution occurs only when a species is threatened with extinction"], ans=0,
   why="EK 7.8.A.1 opens with exactly that sentence: all species have evolved and continue to evolve. The four examples the statement then gives are offered as illustrations of an ongoing process, not as the only circumstances in which it occurs."),

 dict(q="A laboratory sequences the same species at intervals over many generations and records that the sequences differ measurably from the earliest sample. Which of the framework's named examples of continuing evolution does this illustrate?",
   choices=["Genomic changes over time", "Continuous change in the fossil record",
            "The evolution of resistance to a chemical treatment",
            "Pathogens evolving and causing emergent diseases",
            "The extinction of a species under environmental change"], ans=0,
   why="EK 7.8.A.1 lists genomic changes over time as its first example of continuing evolution. The study reports change in the genome of a living lineage across generations, which is that example and not one of the other three."),

 dict(q="A museum series contains fossils of one lineage from many successive levels of rock, and the form of the fossils shifts gradually through the series. Which named example of continuing evolution does this illustrate?",
   choices=["Continuous change in the fossil record", "Genomic changes over time",
            "The evolution of resistance to a chemical treatment",
            "Pathogens evolving and causing emergent diseases",
            "The spread of a species into a new geographic range"], ans=0,
   why="EK 7.8.A.1 lists continuous change in the fossil record as its second example. A graded shift in form through successive levels is a record of change over time in a lineage, which is what that example names."),

 dict(q="A weed species that a herbicide once killed reliably is now largely unaffected by the same application rate. Which named example of continuing evolution does this illustrate?",
   choices=[
     "The evolution of resistance to a herbicide",
     "Continuous change in the fossil record",
     "Genomic changes measured by direct sequencing over time",
     "A pathogen evolving and causing an emergent disease",
     "A change in the weed's geographic range"], ans=0,
   why="EK 7.8.A.1's third example is the evolution of resistance to antibiotics, pesticides, herbicides or chemotherapy drugs, and a herbicide is named there explicitly. The observation is a loss of effect of a chemical treatment on a target population."),

 dict(q="A disease not previously reported in humans appears in a population after a virus circulating in another animal species changes. Which named example of continuing evolution does this illustrate?",
   choices=[
     "Pathogens evolving and causing emergent diseases",
     "The evolution of resistance to a chemotherapy drug",
     "Continuous change in the fossil record",
     "Genomic changes measured in a museum specimen",
     "A change in the geographic range of the animal reservoir"], ans=0,
   why="EK 7.8.A.1's fourth example is pathogens evolving and causing emergent diseases. The scenario reports a pathogen changing and a disease appearing where it had not been reported, which is that example."),

 dict(q="Which of the following is NOT among the examples of continuing evolution the framework lists?",
   choices=[
     "A change in the number of individuals in a population from one year to the next",
     "Genomic changes over time",
     "Continuous change in the fossil record",
     "The evolution of resistance to antibiotics",
     "Pathogens evolving and causing emergent diseases"], ans=0,
   why="EK 7.8.A.1 lists four examples and a change in population size is not one of them. A population can grow or shrink without any change in the heritable makeup of the species, which is what the four named examples all report."),

 dict(q="Why does the framework treat the evolution of resistance in a pest species as evidence bearing on all species rather than only on pests?",
   choices=[
     "The claim is that all species continue to evolve, and pests are simply the case in which the change is quickest to observe",
     "Only species treated with chemicals evolve at all",
     "Pests are the only organisms whose genomes change",
     "Resistance shows that evolution has stopped in untreated species",
     "The framework restricts the claim to species of economic importance"], ans=0,
   why="EK 7.8.A.1 states that ALL species have evolved and continue to evolve, and offers resistance as one example rather than as the boundary of the claim. Short generation times and intense treatment make the change fast enough to watch, which is a fact about observability."),

 dict(q="Which feature of a study population makes continuing evolution easiest to observe directly within the span of a research project?",
   choices=[
     "A short generation time, so that many generations pass during the study",
     "A large body size, so that individuals are easy to count",
     "A long generation time, so that each generation can be studied carefully",
     "A stable environment, so that nothing changes during the study",
     "A small geographic range, so that all individuals live in one place"], ans=0,
   why="EK 7.8.A.1's examples that are watched in real time -- resistance and emergent pathogens -- both involve organisms that turn over many generations quickly. Heritable change accumulates between generations, so the number of generations elapsed, not the calendar time, is what a study can observe."),

 dict(q="A researcher finds no detectable change in a species over ten years and concludes that this species is an exception to the claim that all species continue to evolve. The most serious problem with the conclusion is that",
   choices=[
     "ten years may span too few generations, and too few measured characters, for any change to be detectable",
     "the claim about all species is a definition and cannot be tested",
     "a single species can never be studied",
     "detecting no change proves that the species is evolving rapidly",
     "the fossil record is the only admissible evidence about any species"], ans=0,
   why="EK 7.8.A.1 makes a claim about ongoing change without specifying a rate, so failing to detect change is not the same as showing there is none. Skill 3.D asks for an evaluation of the evidence, and the evidence here has limited power rather than a negative result."),

 dict(q="The framework's examples include both continuous change in the fossil record and genomic changes over time. What do these two examples have in common as evidence?",
   choices=[
     "Each is a record of the same lineage sampled at more than one time",
     "Each requires that the organism be alive at the time of sampling",
     "Each measures the number of individuals rather than their characteristics",
     "Each can be gathered from a single individual at a single moment",
     "Each depends on the organism being a pathogen"], ans=0,
   why="EK 7.8.A.1 offers both as examples of continuing evolution, and continuity is a claim about a sequence. A comparison across time is what turns a description of a lineage into evidence that it has changed, whether the samples are fossils or sequences."),

 dict(q="A hypothetical laboratory culture was sampled four times while an antibiotic was present, and the table reports how many colonies grew on the antibiotic in each round. What percentage of the colonies tested in Round 3 grew on the antibiotic?",
   table=_T_RESIST,
   choices=["30 percent", "60 percent", "10 percent", "2 percent", "120 percent"], ans=0,
   why="Skill 5.A includes percentages. The named round supplies both a number tested and a number that grew, and the percentage is the second divided by the first. EK 7.8.A.1 names the evolution of antibiotic resistance as an example of continuing evolution."),

 dict(q="Using the same four rounds of sampling, by how many colonies did the number growing on the antibiotic rise between the first round and the last?",
   table=_T_RESIST,
   choices=["116 colonies", "120 colonies", "60 colonies", "58 colonies", "4 colonies"], ans=0,
   why="Skill 4.B, identifying specific data points, and skill 5.A, performing the calculation. The first and last rounds each report a number of colonies that grew, and the rise is the difference between them."),

 dict(q="Which description of the pattern across those four rounds of sampling is accurate?",
   table=_T_RESIST,
   choices=[
     "The number growing on the antibiotic rose at every round while the number tested stayed the same",
     "The number growing on the antibiotic rose because more colonies were tested each round",
     "The number growing on the antibiotic fell after the second round",
     "The number tested rose while the number growing stayed the same",
     "Neither column changed across the four rounds"], ans=0,
   why="Skill 4.B asks for the trend and for the relationship between the variables. Holding the number tested constant is what makes the rising second column a change in the population rather than a change in sampling effort."),

 dict(q="The table reports four hypothetical fields that have received an insecticide for different numbers of seasons. What relationship do the two measured variables show?",
   table=_T_FIELDS,
   choices=[
     "The more seasons the insecticide has been applied, the larger the percentage of the pest population surviving it",
     "The more seasons the insecticide has been applied, the smaller the percentage surviving it",
     "The two variables are unrelated across these fields",
     "Survival is the same in every field regardless of the number of seasons",
     "Survival rises only in the fields treated for the fewest seasons"], ans=0,
   why="Skill 4.B asks for the relationship between variables. Reading the rows in order of seasons applied, the survival percentage rises without exception, which is the pattern EK 7.8.A.1's resistance example describes."),

 dict(q="In that same set of four fields, how many percentage points higher is survival in the field treated for the most seasons than in the field never treated?",
   table=_T_FIELDS,
   choices=["61 percentage points", "64 percentage points", "31 percentage points",
            "12 percentage points", "3 percentage points"], ans=0,
   why="Skill 5.A includes percentages and percent changes. The two rows named by the stem are located by the number of seasons applied, and the answer is the difference between their survival percentages."),

 dict(q="The field study just described compares fields that differ in how long the insecticide has been applied. Which criticism of that design is strongest?",
   choices=[
     "Fields that differ in years of treatment may also differ in soil, climate and neighbouring crops, and none of those was controlled",
     "Percentages cannot be compared across fields of different sizes",
     "Survival should have been measured before the pest population existed",
     "Four fields is too many for a comparison to be meaningful",
     "The study should have used a different insecticide in each field"], ans=0,
   why="Skill 3.D asks for an evaluation of the design. Fields chosen because they differ in treatment history will differ in other ways too, so the comparison cannot separate the effect of treatment from the effects of everything else that varies with it."),

 dict(q="Following that criticism, which new investigation would best test whether repeated application of the insecticide is what raises survival in the pest population?",
   choices=[
     "Assign comparable fields at random to receive the insecticide or not, and measure survival in both over the same seasons",
     "Apply the insecticide to every field and measure survival at the end",
     "Measure survival once in a single field that has been treated for many seasons",
     "Ask the growers to recall how well the insecticide worked in past seasons",
     "Compare the treated fields with fields growing a different crop entirely"], ans=0,
   why="Skill 3.D asks for a new investigation that repairs the design. Random assignment of comparable fields to treatment and no treatment breaks the link between treatment history and every other difference among fields, which is exactly what the original comparison could not do."),

 dict(q="An investigator wishes to know whether the bacterial population in the culture study changed over the four rounds or whether the antibiotic simply became less effective in storage. Which investigation would settle that?",
   choices=[
     "Test colonies from the first and the last round side by side against a freshly prepared batch of the antibiotic",
     "Repeat the last round using the same stored antibiotic",
     "Count more colonies in the last round only",
     "Test the stored antibiotic against a different species of bacterium",
     "Report the percentages instead of the raw counts"], ans=0,
   why="Skill 3.D asks for an investigation that separates two explanations. Testing early and late colonies at the same time against the same fresh antibiotic holds the chemical constant, so any difference that remains must lie in the bacteria."),

 dict(q="A student claims that exposure to the antibiotic caused the bacteria to become resistant. Which investigation would best distinguish that claim from the alternative that resistant cells were already present before exposure?",
   choices=[
     "Screen samples of the population for resistant cells before any antibiotic is applied, using a portion of the culture that is never exposed",
     "Apply a higher dose of the antibiotic and see whether resistance appears sooner",
     "Apply the antibiotic to a second culture and count the resistant colonies",
     "Sequence the resistant colonies from the final round only",
     "Compare the growth rates of resistant and non-resistant colonies after exposure"], ans=0,
   why="Skill 3.D asks for a design that discriminates between two accounts of the same result. Only a sample that has never met the antibiotic can show whether resistant cells were present beforehand; every option that begins with exposure leaves both accounts standing."),

 dict(q="A clinic reports that a drug which once cleared an infection now fails in most patients, and proposes to conclude that the pathogen population has evolved. Which additional evidence would most directly support that conclusion?",
   choices=[
     "Pathogen samples taken from patients before and after the change in outcomes, tested against the drug under the same conditions",
     "The number of patients treated in each year",
     "A survey of how satisfied patients were with their treatment",
     "The cost of the drug in each year",
     "The number of clinics that stock the drug"], ans=0,
   why="EK 7.8.A.1 names the evolution of resistance as an example of continuing evolution, and a claim of change requires a comparison across time. Testing early and late pathogen samples under identical conditions is that comparison; the other options record facts about the clinic rather than about the pathogen."),

 dict(q="Which of the following would most weaken the claim that a pest population in one field has evolved resistance to an insecticide?",
   choices=[
     "Records showing the applied dose has fallen steadily over the same period",
     "Records showing the dose applied has been identical throughout",
     "A finding that the pest species has a short generation time",
     "A finding that the insecticide is still effective in neighbouring fields",
     "A finding that the pest population has grown larger over the period"], ans=0,
   why="Skill 3.D asks for an evaluation of evidence. If less insecticide is being applied, greater survival is explained without any heritable change in the pest, so the observation no longer requires the evolutionary account EK 7.8.A.1 describes."),

 dict(q="A team wants to test whether a lineage known only from fossils shows continuous change through a rock sequence. Which investigation is best suited to that question?",
   choices=[
     "Measure the same set of characters on specimens from every level of the sequence and compare the values level by level",
     "Measure many characters on the specimens from the topmost level only",
     "Count how many fossils were recovered from the sequence in total",
     "Compare the fossils with a living species that has never been dated",
     "Measure a different character at each level of the sequence"], ans=0,
   why="EK 7.8.A.1 names continuous change in the fossil record, and continuity is a statement about a sequence of comparable measurements. Measuring different characters at different levels, or one level only, produces nothing that can be compared across time."),

 dict(q="Why does measuring a different character at each level of a fossil sequence make the resulting data useless for detecting continuous change?",
   choices=[
     "A change over time can only be seen by comparing like with like across the levels",
     "Fossils cannot be measured accurately at any level",
     "Continuous change is a claim about living species only",
     "Characters that differ between levels prove that no change occurred",
     "The number of levels is what determines whether change occurred"], ans=0,
   why="Skill 3.D asks for evaluation of a design. EK 7.8.A.1's fossil example is a claim about change in a lineage, and a difference between two measurements of different things is not evidence of change in either."),

 dict(q="A public health laboratory sequences samples of one pathogen collected from patients over several years. Which finding would best support the framework's claim that the pathogen is continuing to evolve?",
   choices=[
     "The sequences from later years differ systematically from those of earlier years",
     "The pathogen was found in more patients in later years than in earlier years",
     "The pathogen was found in more countries in later years",
     "The sequencing method improved over the period of the study",
     "The number of samples collected rose in every year"], ans=0,
   why="EK 7.8.A.1 names genomic changes over time and pathogens evolving among its examples. A systematic difference between early and late sequences is a heritable change in the population, whereas spread and sampling effort describe where and how hard people looked."),

 dict(q="If the sequencing method used in that laboratory improved partway through the study, what problem does that create for the conclusion?",
   choices=[
     "Differences between early and late sequences might be produced by the change in method rather than by change in the pathogen",
     "The improved method makes the early samples impossible to store",
     "It shows that the pathogen has not evolved",
     "It means percentages cannot be calculated from the data",
     "It means the study must be repeated on a different pathogen"], ans=0,
   why="Skill 3.D asks for an evaluation of the design. A measurement change that coincides with the passage of time is confounded with the change being measured, so the observed difference no longer identifies its cause."),

 dict(q="Which new investigation would best remove that confounding of method with time?",
   choices=[
     "Re-sequence the stored early samples with the improved method and compare like with like",
     "Discard the early samples and use only the later ones",
     "Report the results of the two methods separately without comparing them",
     "Collect more samples using the improved method only",
     "Change the method again before the next collection"], ans=0,
   why="Skill 3.D asks for the investigation that repairs the design. Applying one method to samples from both periods holds the measurement constant, so any remaining difference is a difference between the samples themselves."),

 dict(q="Which statement about the four examples the framework gives of continuing evolution is accurate?",
   choices=[
     "They are examples of an ongoing process, not an exhaustive list of where it occurs",
     "They are the only four circumstances in which evolution occurs",
     "They apply only to organisms that humans manage",
     "They describe processes that occurred in the past and have since stopped",
     "They are alternative names for a single observation"], ans=0,
   why="EK 7.8.A.1 introduces the four with the words examples include, after asserting that all species have evolved and continue to evolve. A list of examples illustrates a general claim rather than bounding it."),

 dict(q="A cancer treatment that at first shrinks a tumour becomes ineffective after several months, and cells sampled late in treatment grow in concentrations of the drug that killed the early cells. Which framework example does this best illustrate?",
   choices=[
     "The evolution of resistance to a chemotherapy drug",
     "Continuous change in the fossil record",
     "Pathogens evolving and causing emergent diseases",
     "A change in the number of cells present in the body",
     "A change in the patient's environment rather than in the cells"], ans=0,
   why="EK 7.8.A.1's third example names chemotherapy drugs alongside antibiotics, pesticides and herbicides. The comparison of early and late cells under the same drug concentration is what makes this a change in the cell population."),

 dict(q="Which of the following best explains why a treatment that kills most but not all of a target population can be followed by a population that the same treatment no longer controls?",
   choices=[
     "The survivors are the source of the next generation, so heritable differences that allowed survival become more common in it",
     "The treatment teaches each individual how to survive the next application",
     "The treatment changes the environment so that the population no longer needs to reproduce",
     "The population becomes larger, which by itself makes the treatment weaker",
     "The treatment loses effectiveness because it has been stored too long"], ans=0,
   why="EK 7.8.A.1 names the evolution of resistance as continuing evolution, which is a heritable change in a population across generations. Only the survivors contribute to the next generation, so whatever heritable difference distinguished them is what that generation inherits."),

 dict(q="Taken together, the framework's four examples of continuing evolution support which general statement?",
   choices=[
     "Evolutionary change is happening now and can be observed and investigated in living populations and in the record",
     "Evolutionary change can be inferred only from fossils",
     "Evolutionary change can be observed only in the laboratory",
     "Evolutionary change stopped once modern species appeared",
     "Evolutionary change occurs only in species that cause disease"], ans=0,
   why="EK 7.8.A.1 asserts that all species have evolved and continue to evolve, and its four examples span living populations, the fossil record, managed systems and pathogens. That range is what makes the claim general rather than restricted to any one setting."),
]
