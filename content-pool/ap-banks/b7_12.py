# AP BIOLOGY 7.12 Origins of Life on Earth
# CED effective Fall 2025, Unit 7 Natural Selection, BIG IDEA 4 Systems
# Interactions.
# Learning objective 7.12.A, describe the scientific evidence that supports
# models of the origin of life on Earth.
# Suggested skill 3.B, STATE THE NULL HYPOTHESIS OR PREDICT THE RESULTS OF AN
# EXPERIMENT.
#
# Essential knowledge relied on, in the framework's own terms:
#   7.12.A.1  the origin of life on Earth is supported by SCIENTIFIC EVIDENCE.
#               i. GEOLOGICAL evidence reinforces models of the origin of life
#                  on Earth.
#              ii. Earth formed approximately 4.6 BILLION YEARS AGO. The
#                  environment was TOO HOSTILE FOR LIFE UNTIL ABOUT 3.9 billion
#                  years ago, and the EARLIEST FOSSIL EVIDENCE for life dates to
#                  3.5 billion years ago. Taken together, this evidence provides
#                  A PLAUSIBLE RANGE OF DATES for the origin of life.
#   7.12.A.2  the RNA WORLD HYPOTHESIS PROPOSES that RNA could have been the
#             earliest genetic material. There are THREE ASSUMPTIONS:
#               i. at some point in time, GENETIC CONTINUITY WAS ASSURED BY THE
#                  REPLICATION OF RNA.
#              ii. BASE-PAIRING IS NECESSARY FOR REPLICATION.
#             iii. GENETICALLY ENCODED PROTEINS WERE NOT INVOLVED AS CATALYSTS.
#
# ON THE THREE DATES. They are the only numbers the framework prints for this
# topic and they are printed as approximations. Every arithmetic item here works
# from a table that carries those three dates, and verify_b7_12.py recomputes
# each interval from the table rather than from a remembered figure. No item
# asks a student to recall a date that the CED does not state.
#
# ON WHAT IS NOT CLAIMED. EK 7.12.A.2 says the hypothesis PROPOSES and lists
# ASSUMPTIONS. No key here treats the RNA world hypothesis as established, and
# no key adds a fourth assumption or a mechanism the framework does not print.
# Where an item asks WHY an assumption is made, the claim in the verifier says
# plainly that the reasoning follows from the three statements taken together
# rather than from a further CED sentence.
#
# DELIBERATE OMISSIONS. Dating fossils by rock age and isotope decay is
# EK 7.6.B.1 and is asked in b7_6; no item here asks how any of these dates was
# obtained. RNA structure, base pairing chemistry and the roles of the RNA
# molecules are EK 6.1 and EK 6.3 and belong to those topics; the items here
# use base-pairing only as EK 7.12.A.2's second assumption names it.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset.
TOPIC = ("7.12", "Origins of Life on Earth", 7)

_T_DATES = dict(
    headers=["Event", "Time before the present, in billions of years"],
    rows=[["Formation of Earth", "4.6"],
          ["End of the period too hostile for life", "3.9"],
          ["Earliest fossil evidence for life", "3.5"]])

_T_ASSUMPTIONS = dict(
    headers=["Statement", "Listed by the framework as an assumption of the RNA world hypothesis"],
    rows=[["Genetic continuity was assured by the replication of RNA", "Yes"],
          ["Base-pairing is necessary for replication", "Yes"],
          ["Genetically encoded proteins were not involved as catalysts", "Yes"],
          ["DNA was the earliest genetic material", "No"],
          ["Genetically encoded proteins carried out the earliest catalysis", "No"]])

QUESTIONS = [
 dict(q="According to the course framework, the origin of life on Earth is supported by",
   choices=["scientific evidence", "a single laboratory experiment",
            "the absence of any competing account", "the fossil record alone, with no other evidence",
            "reasoning that no observation could bear on"], ans=0,
   why="EK 7.12.A.1 states that the origin of life on Earth is supported by scientific evidence, and its two sub-statements name geological evidence and a set of dates. The topic is built on evidence of more than one kind, not on one experiment or on the fossil record by itself."),

 dict(q="What role does the framework assign to geological evidence in this topic?",
   choices=[
     "It reinforces models of the origin of life on Earth",
     "It replaces the need for any model of the origin of life",
     "It shows that life originated somewhere other than Earth",
     "It establishes the exact date on which life originated",
     "It bears only on events after the earliest fossils formed"], ans=0,
   why="EK 7.12.A.1 states that geological evidence reinforces models of the origin of life on Earth. Reinforcing a model is supporting it, which is different from replacing it or from fixing an exact date."),

 dict(q="According to the framework, Earth formed approximately how long before the present?",
   choices=["4.6 billion years", "3.9 billion years", "3.5 billion years",
            "1.1 billion years", "0.4 billion years"], ans=0,
   why="EK 7.12.A.1 states that Earth formed approximately 4.6 billion years ago. The other figures are the framework's other two dates and the intervals between them, none of which is the age of the planet."),

 dict(q="According to the framework, the environment of Earth was too hostile for life until about how long before the present?",
   choices=["3.9 billion years", "4.6 billion years", "3.5 billion years",
            "0.7 billion years", "0.4 billion years"], ans=0,
   why="EK 7.12.A.1 states that the environment was too hostile for life until about 3.9 billion years ago. That date is the earlier boundary of the interval within which the origin of life is placed."),

 dict(q="According to the framework, the earliest fossil evidence for life dates to about how long before the present?",
   choices=["3.5 billion years", "3.9 billion years", "4.6 billion years",
            "0.4 billion years", "0.7 billion years"], ans=0,
   why="EK 7.12.A.1 states that the earliest fossil evidence for life dates to 3.5 billion years ago. That date is the later boundary of the interval within which the origin of life is placed."),

 dict(q="What does the framework say the three dates provide when they are taken together?",
   choices=[
     "A plausible range of dates for the origin of life",
     "The exact date on which life originated",
     "Proof that life could not have originated on Earth",
     "A measure of how quickly life spread once it had appeared",
     "The date on which the first eukaryotic cell appeared"], ans=0,
   why="EK 7.12.A.1 states that, taken together, this evidence provides a plausible range of dates for the origin of life. A range of dates is not a single date, and nothing in the statement concerns the spread of life or the first eukaryote."),

 dict(q="Between which two of the framework's dates does the origin of life most plausibly fall?",
   choices=[
     "Between the end of the period too hostile for life and the earliest fossil evidence",
     "Between the formation of Earth and the end of the period too hostile for life",
     "Before the formation of Earth",
     "After the earliest fossil evidence for life",
     "The framework gives no basis for placing it between any two dates"], ans=0,
   why="EK 7.12.A.1 gives one date before which the environment was too hostile for life and one date by which life had left fossils. Life could not have originated before conditions allowed it, and it must already have existed to leave the earliest fossils, so the interval between the two is what the statement calls a plausible range."),

 dict(q="Why does the framework's account place a lower limit on how early life could have originated?",
   choices=[
     "The environment was too hostile for life until about 3.9 billion years ago",
     "No rocks older than that date have ever formed",
     "Fossils cannot be preserved in rocks of any age",
     "The Earth had not yet formed at that date",
     "Life is known to require exactly one billion years to arise"], ans=0,
   why="EK 7.12.A.1 states that the environment was too hostile for life until about 3.9 billion years ago, which is a statement about conditions rather than about the availability of rocks. Earth had already formed well before that date, at approximately 4.6 billion years ago."),

 dict(q="Why does the framework treat the date of the earliest fossil evidence as a limit on the origin of life rather than as the date of that origin?",
   choices=[
     "Life must already have existed in order to leave the fossils, so the origin was at or before that date",
     "Fossils always form at the moment a lineage originates",
     "The fossil record contains no evidence relevant to the origin of life",
     "The earliest fossils are older than the formation of Earth",
     "The framework treats the fossil date as the exact date of the origin"], ans=0,
   why="EK 7.12.A.1 uses the earliest fossil evidence as one bound of a plausible RANGE of dates rather than as the origin itself. A fossil records an organism that was already alive, so it establishes that life existed by that date and not that it began then."),

 dict(q="What does the RNA world hypothesis propose?",
   choices=[
     "That RNA could have been the earliest genetic material",
     "That DNA was the earliest genetic material",
     "That proteins were the earliest genetic material",
     "That the earliest organisms had no genetic material at all",
     "That RNA and DNA appeared at exactly the same time"], ans=0,
   why="EK 7.12.A.2 states that the RNA world hypothesis proposes that RNA could have been the earliest genetic material. The word proposes marks it as a hypothesis rather than an established finding."),

 dict(q="Which of the following is one of the three assumptions the framework lists for the RNA world hypothesis?",
   choices=[
     "At some point in time, genetic continuity was assured by the replication of RNA",
     "Genetic continuity was assured by the replication of DNA",
     "Genetic continuity required a cell membrane from the beginning",
     "Genetic continuity was unnecessary in the earliest organisms",
     "Genetic continuity was assured by protein catalysts"], ans=0,
   why="EK 7.12.A.2 lists three assumptions, of which the first is that at some point in time genetic continuity was assured by the replication of RNA. Substituting DNA or proteins reverses the hypothesis the assumption belongs to."),

 dict(q="Which of the following is the second assumption the framework lists for the RNA world hypothesis?",
   choices=[
     "Base-pairing is necessary for replication",
     "Replication can occur without any pairing of bases",
     "Replication requires an enzyme encoded by a gene",
     "Replication occurred only after cells had appeared",
     "Replication of RNA is faster than replication of DNA"], ans=0,
   why="EK 7.12.A.2's second assumption is that base-pairing is necessary for replication. The assumption states a requirement for copying a sequence and says nothing about rates or about the appearance of cells."),

 dict(q="Which of the following is the third assumption the framework lists for the RNA world hypothesis?",
   choices=[
     "Genetically encoded proteins were not involved as catalysts",
     "Genetically encoded proteins carried out all of the earliest catalysis",
     "No catalysis of any kind occurred in the earliest systems",
     "Proteins and RNA were encoded by the same gene",
     "Catalysis required a membrane-bound compartment"], ans=0,
   why="EK 7.12.A.2's third assumption is that genetically encoded proteins were not involved as catalysts. The assumption excludes one particular kind of catalyst rather than denying that any catalysis took place."),

 dict(q="How many assumptions does the framework list for the RNA world hypothesis?",
   choices=["Three", "One", "Two", "Four", "Five"], ans=0,
   why="EK 7.12.A.2 states that there are three assumptions and then lists them: genetic continuity assured by RNA replication, base-pairing as a requirement for replication, and the absence of genetically encoded proteins as catalysts."),

 dict(q="Which of the following is NOT among the assumptions the framework lists for the RNA world hypothesis?",
   choices=[
     "That the earliest genetic material was contained within a cell membrane",
     "That genetic continuity was assured by the replication of RNA",
     "That base-pairing is necessary for replication",
     "That genetically encoded proteins were not involved as catalysts",
     "That RNA could have been the earliest genetic material"], ans=0,
   why="EK 7.12.A.2 names the proposal and its three assumptions, and a membrane is not among them. Adding a condition the framework does not print would change the hypothesis being described."),

 dict(q="Why is the third assumption, that genetically encoded proteins were not involved as catalysts, a natural part of a hypothesis about the EARLIEST genetic material?",
   choices=[
     "A genetically encoded protein presupposes a genetic system already in place, which is the thing the hypothesis is trying to account for",
     "Proteins cannot act as catalysts under any conditions",
     "Proteins are not made of amino acids in early organisms",
     "The hypothesis denies that proteins exist",
     "Genetically encoded proteins are the same molecules as RNA"], ans=0,
   why="EK 7.12.A.2 proposes RNA as the EARLIEST genetic material and lists the exclusion of genetically encoded proteins among its assumptions. The reasoning connecting the two is that a genetically encoded catalyst would already require the genetic system whose origin is at issue; the framework prints the assumption and this claim states the connection rather than adding new content."),

 dict(q="The table gives the three times the framework states for this topic. How long after the formation of Earth did the period too hostile for life come to an end?",
   table=_T_DATES,
   choices=["0.7 billion years", "0.4 billion years", "1.1 billion years",
            "3.9 billion years", "4.6 billion years"], ans=0,
   why="Skill 5.A includes rates and differences. The two rows named by the stem each report a time before the present, and the interval between the events is the difference between those two values."),

 dict(q="Using the same three times, how long is the plausible range within which the origin of life falls?",
   table=_T_DATES,
   choices=["0.4 billion years", "0.7 billion years", "1.1 billion years",
            "3.5 billion years", "3.9 billion years"], ans=0,
   why="EK 7.12.A.1 bounds the origin of life below by the end of the hostile period and above by the earliest fossil evidence, and calls the result a plausible range of dates. The width of that range is the difference between those two times."),

 dict(q="Using the same three times, how long after the formation of Earth is the earliest fossil evidence for life dated?",
   table=_T_DATES,
   choices=["1.1 billion years", "0.4 billion years", "0.7 billion years",
            "3.5 billion years", "4.6 billion years"], ans=0,
   why="Skill 5.A includes differences. The interval between the formation of Earth and the earliest fossil evidence is the difference between the two times those rows report before the present."),

 dict(q="Which comparison of the intervals in that table of three times is accurate?",
   table=_T_DATES,
   choices=[
     "The plausible range for the origin of life is shorter than the interval between the formation of Earth and the end of the hostile period",
     "The plausible range for the origin of life is longer than the interval between the formation of Earth and the end of the hostile period",
     "The two intervals are of equal length",
     "The plausible range for the origin of life is longer than the whole interval since Earth formed",
     "The intervals cannot be compared, because the dates are approximate"], ans=0,
   why="Skill 4.B asks for relationships among data points and skill 5.A for the arithmetic. Both intervals are differences between times the table reports, so they can be compared directly even though each date is stated as an approximation."),

 dict(q="The table lists five statements and records which of them the framework gives as assumptions of the RNA world hypothesis. How many of the five are listed as assumptions?",
   table=_T_ASSUMPTIONS,
   choices=["Three", "Two", "Four", "Five", "One"], ans=0,
   why="EK 7.12.A.2 states that there are three assumptions and lists them. Counting the rows the table marks as assumptions gives the same number, which is the check a student can perform on the table itself."),

 dict(q="Which statement in that same table is marked as NOT an assumption of the RNA world hypothesis, and why is that marking correct?",
   table=_T_ASSUMPTIONS,
   choices=[
     "The claim that DNA was the earliest genetic material, because the hypothesis proposes RNA in that role",
     "The claim that base-pairing is necessary for replication, because replication needs no pairing",
     "The claim that RNA replication assured genetic continuity, because continuity was unnecessary",
     "The claim that genetically encoded proteins were not catalysts, because they were the first catalysts",
     "None of the statements is marked as an assumption"], ans=0,
   why="EK 7.12.A.2 proposes that RNA could have been the earliest genetic material, so a statement putting DNA in that role contradicts the proposal rather than assuming it. The other three explanations offered each contradict one of the framework's own three assumptions."),

 dict(q="Considering the statements in that table that are marked as assumptions, what do the three have in common?",
   table=_T_ASSUMPTIONS,
   choices=[
     "Each is a condition the hypothesis takes for granted rather than a result it has demonstrated",
     "Each has been demonstrated by experiment",
     "Each concerns the structure of DNA",
     "Each states a date at which an event occurred",
     "Each is a conclusion the fossil record establishes"], ans=0,
   why="EK 7.12.A.2 introduces the three as assumptions of a hypothesis that PROPOSES an account of the earliest genetic material. An assumption is what an account takes as given; none of the three is presented as a demonstrated result or as a date."),

 dict(q="A researcher sets up an experiment to test whether a sample of RNA can be copied in the absence of any protein catalyst, comparing tubes that contain a protein catalyst with tubes that do not. What is the null hypothesis for this comparison?",
   choices=[
     "The presence or absence of the protein catalyst makes no difference to the amount of RNA copied",
     "RNA will be copied only in the tubes containing the protein catalyst",
     "RNA will be copied only in the tubes lacking the protein catalyst",
     "The protein catalyst will be destroyed during the experiment",
     "RNA cannot be copied under any conditions"], ans=0,
   why="Skill 3.B asks for the null hypothesis, which states that the manipulated variable has no effect. The other options each predict a particular outcome, and a prediction of an effect is the alternative to a null hypothesis rather than the null itself."),

 dict(q="If the first assumption of the RNA world hypothesis holds, what result should an experiment on RNA replication produce?",
   choices=[
     "New RNA molecules whose sequences correspond to the sequence of the starting molecule",
     "New RNA molecules with sequences unrelated to the starting molecule",
     "No new molecules of any kind",
     "New protein molecules rather than new RNA",
     "A starting molecule that changes into DNA"], ans=0,
   why="EK 7.12.A.2's first assumption is that genetic continuity was assured by the replication of RNA. Continuity means the information is carried forward, so copies must correspond in sequence to the molecule they were copied from."),

 dict(q="A researcher supplies a replication system with modified nucleotides that cannot pair with the bases of the template. Under the second assumption of the RNA world hypothesis, what result is predicted?",
   choices=[
     "No faithful copy of the template will be produced",
     "Copies will be produced at the usual rate",
     "Copies will be produced faster than with ordinary nucleotides",
     "The template will be converted into a protein",
     "The template will pair with itself and be destroyed"], ans=0,
   why="EK 7.12.A.2's second assumption is that base-pairing is necessary for replication. Removing the ability to pair therefore removes the requirement the assumption names, and the predicted result is a failure to copy the sequence."),

 dict(q="Under the framework's account, what should the geological record from before the end of the hostile period show?",
   choices=[
     "No fossil evidence of life, because the environment could not support it",
     "Abundant fossil evidence of life",
     "Fossil evidence of eukaryotic cells only",
     "The same fossil evidence as rocks from after that date",
     "Nothing at all, because no rocks of that age exist"], ans=0,
   why="EK 7.12.A.1 states that the environment was too hostile for life until about 3.9 billion years ago and that geological evidence reinforces models of the origin of life. A prediction that follows from an account is what skill 3.B asks a student to state, and life absent means fossils absent."),

 dict(q="Suppose fossil evidence of life were found in rocks reliably dated to well before the end of the period the framework describes as too hostile. What would follow?",
   choices=[
     "The proposed range of dates for the origin of life would have to be revised",
     "The fossils would have to be discarded without examination",
     "Nothing would follow, because the range is a definition",
     "The Earth would have to be older than 4.6 billion years",
     "The RNA world hypothesis would be confirmed"], ans=0,
   why="EK 7.12.A.1 calls the interval a PLAUSIBLE RANGE supported by evidence, and a range supported by evidence is one further evidence can move. The hostile-period boundary is one of the two dates that set that range."),

 dict(q="What is the status of the RNA world hypothesis in the framework's presentation?",
   choices=[
     "A proposal resting on stated assumptions, which evidence can support or challenge",
     "An established fact about the earliest organisms",
     "A definition of what genetic material means",
     "A claim that no observation could bear on",
     "A description of how genetic material works in organisms today"], ans=0,
   why="EK 7.12.A.2 says the hypothesis PROPOSES that RNA could have been the earliest genetic material and sets out three ASSUMPTIONS. Both words mark it as a proposed account rather than as an established fact or a definition."),

 dict(q="Taken together, what do the framework's two statements about the origin of life assert?",
   choices=[
     "That geological and fossil evidence bound the origin of life within a plausible range of dates, and that one proposed account of the earliest genetic material is the RNA world hypothesis",
     "That the exact date and the exact mechanism of the origin of life are both established",
     "That no evidence bears on the origin of life",
     "That the origin of life is known to have occurred before Earth formed",
     "That the RNA world hypothesis has replaced the need for geological evidence"], ans=0,
   why="EK 7.12.A.1 supplies evidence and a plausible range of dates, and EK 7.12.A.2 supplies a proposed account of the earliest genetic material with three assumptions. Neither statement claims an exact date or a settled mechanism, and neither displaces the other."),
]
