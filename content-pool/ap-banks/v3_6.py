# AP U.S. GOVERNMENT AND POLITICS 3.6 Amendments: Balancing Individual Freedom with Public Order and Safety -- 30 questions
# CED V.1 (c) 2026, Unit 3 Civil Liberties and Civil Rights.
# Learning objective 3.6.A: explain how the Supreme Court has attempted to
# BALANCE claims of individual freedom with laws and enforcement procedures that
# promote PUBLIC ORDER AND SAFETY.
# Suggested skill for this topic (CED p. 87): 5.B, SUPPORT AN ARGUMENT OR CLAIM
# USING RELEVANT EVIDENCE. So a large share of this module gives a claim and
# asks which evidence supports, weakens, or is irrelevant to it -- the shape 5.B
# tests, and the same shape v1_9 uses for its own 5.B topic.
#
# Essential knowledge relied on. Two statements covering THREE amendments:
#   EK 3.6.A.1 -- "Court decisions defining CRUEL AND UNUSUAL PUNISHMENT involve
#     interpretation of the EIGHTH AMENDMENT and its application to DEATH
#     PENALTY STATUTES."
#   EK 3.6.A.2 -- "The debate about the SECOND AND FOURTH AMENDMENTS involves
#     concerns about public safety and whether or not the government regulation
#     of FIREARMS or collection of DIGITAL METADATA promotes or interferes with
#     public safety AND individual rights."
#
# THE WORD THE WHOLE TOPIC TURNS ON IS "BALANCE", AND IT IS IN THE OBJECTIVE
# RATHER THAN IN EITHER STATEMENT. LO 3.6.A does not ask which side wins. It
# asks how the Court has ATTEMPTED TO BALANCE two things that both matter, which
# means an answer naming only one of them is incomplete even when the fact it
# names is true. Items 1 to 6 and 27 to 30 turn on that.
#
# EK 3.6.A.2's STRUCTURE IS EASY TO HALF-READ. Its question is whether a measure
# "promotes OR INTERFERES WITH public safety AND individual rights" -- four
# possibilities, not two. A regulation can advance safety and burden rights at
# once; it can also fail to advance safety while burdening rights, which is the
# possibility a student who has framed the debate as a trade-off never
# considers. Items 15 to 20 are built on the full grid.
#
# WHAT THIS MODULE DOES NOT DO: it takes no position on the death penalty, on
# firearms regulation, or on metadata collection. The framework identifies these
# as subjects of DEBATE and supplies no resolution, so every item here asks what
# the debate consists of, what would count as evidence in it, or what the Court
# has actually held -- never who is right. SOCIAL_BRIEF.md's rule against
# guessing applies with special force where the framework itself says the
# question is contested.
#
# Documents the CED attaches to 3.6.A (p. 26-27): "Letter from a Birmingham
# Jail."
# Required cases the CED attaches to 3.6.A (p. 32-33): Tinker v. Des Moines,
# United States v. Lopez, McDonald v. Chicago.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the Fourth and Eighth Amendments and
# "Letter from a Birmingham Jail" are quoted verbatim. Both tables are labelled
# hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("3.6", "Amendments: Balancing Individual Freedom with Public Order and Safety", 3)

_GRID = ("The table sets out the four possible combinations EK 3.6.A.2 allows for a proposed "
         "public safety measure, with a hypothetical count of how many of forty measures "
         "studied fell into each.")
_GRID_TABLE = dict(
    headers=["Effect on public safety", "Effect on individual rights", "Measures in this category"],
    rows=[["Promotes", "Burdens", "17"],
          ["Promotes", "Does not burden", "6"],
          ["Does not promote", "Burdens", "13"],
          ["Does not promote", "Does not burden", "4"]])

_METADATA = ("In a hypothetical study, the table reports what a collection program gathered "
             "and what a court held about each category.")
_METADATA_TABLE = dict(
    headers=["Category collected", "Contents of communications included?", "Held to require a warrant?"],
    rows=[["Numbers dialed and call durations", "No", "No"],
          ["Location of a device over several months", "No", "Yes"],
          ["Recordings of conversations", "Yes", "Yes"],
          ["Addresses on the outside of mailed envelopes", "No", "No"]])

QUESTIONS = [
 dict(q="According to the learning objective for this topic, what has the Supreme Court attempted to do?",
   choices=[
     "Balance claims of individual freedom with laws and enforcement procedures that promote public order and safety",
     "Give individual freedom priority over public safety in every case",
     "Give public safety priority over individual freedom in every case",
     "Avoid deciding cases in which the two conflict",
     "Refer such conflicts to Congress for resolution"], ans=0,
   why="LO 3.6.A's own words are 'attempted to balance,' which is a description of a task rather than of an outcome. An answer naming only one side of the balance is incomplete even when the fact it names is true."),

 dict(q="Why does the framework describe the Court as ATTEMPTING to balance rather than as having balanced?",
   choices=[
     "The balance is struck case by case and remains contested, so no single decision settles it",
     "The Court has consistently failed to reach any decision",
     "Congress forbids the Court from deciding such cases",
     "The Constitution assigns the balance to the states",
     "The balance was settled at the founding and requires no further work"], ans=0,
   why="LO 3.6.A's verb is 'attempted', and EK 3.6.A.2 describes an ongoing DEBATE rather than a resolution. Both point to a balance that is redrawn rather than fixed."),

 dict(q="A student argues that a case was decided wrongly because the Court gave too much weight to public safety. Which framing of the disagreement is most consistent with the course framework?",
   choices=[
     "Both individual freedom and public safety are legitimate considerations, so the disagreement is about how they were weighed rather than about whether one counts",
     "Public safety is not a legitimate consideration in constitutional cases",
     "Individual freedom is not a legitimate consideration in constitutional cases",
     "The Court is prohibited from weighing considerations against each other",
     "The disagreement cannot be assessed, since the framework takes no position on any case"], ans=0,
   why="LO 3.6.A puts both on the scale, so a criticism of the weighting is inside the framework's terms while a claim that one side does not count is outside them."),

 dict(q="According to the course framework, court decisions defining cruel and unusual punishment involve interpretation of",
   choices=[
     "the Eighth Amendment and its application to death penalty statutes",
     "the Fourth Amendment and its application to searches",
     "the Second Amendment and its application to firearms",
     "the Fourteenth Amendment and its application to equal protection",
     "the First Amendment and its application to symbolic speech"], ans=0,
   why="EK 3.6.A.1 names the Eighth Amendment and death penalty statutes specifically. The other amendments appear elsewhere in this unit and in EK 3.6.A.2, but not in this statement."),

 dict(q="Read the following excerpt.\n\n“Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted.”\n—U.S. Constitution, Eighth Amendment\n\nWhy does this text require interpretation, as EK 3.6.A.1 says?",
   choices=[
     "The words excessive, cruel and unusual are standards rather than rules, so their content must be determined before they can be applied",
     "The text specifies which punishments are forbidden by name",
     "The text applies only to fines and not to punishments",
     "The text has been repealed as to the states",
     "The text expressly permits the death penalty"], ans=0,
   why="A clause that forbids what is 'cruel and unusual' without saying what qualifies is a standard, and EK 3.6.A.1's word INTERPRETATION follows from that. The Amendment neither names nor authorizes any particular punishment."),

 dict(q="Which of the following does the Eighth Amendment's text address in addition to punishments?",
   choices=[
     "Bail and fines",
     "Searches and seizures",
     "Speech and assembly",
     "Trial by jury",
     "The right to counsel"], ans=0,
   why="The Amendment's three clauses concern excessive bail, excessive fines and cruel and unusual punishments. The other options belong to the Fourth, First and Sixth Amendments."),

 dict(q="According to EK 3.6.A.1, to what have these interpretations been applied?",
   choices=[
     "Death penalty statutes",
     "Firearms regulations",
     "Collection of digital metadata",
     "School speech policies",
     "Campaign finance rules"], ans=0,
   why="EK 3.6.A.1 names death penalty statutes as the application. Firearms and metadata belong to EK 3.6.A.2, which is a separate statement about different amendments."),

 dict(q="Which question would a court interpreting the cruel and unusual punishments clause have to answer?",
   choices=[
     "What makes a punishment cruel and unusual, given that the text supplies no list",
     "Whether the legislature that enacted the punishment was popularly elected",
     "Whether the punishment is cheaper than the alternatives",
     "Whether a majority of residents approve of the punishment",
     "Whether the defendant is a citizen"], ans=0,
   why="EK 3.6.A.1 makes the interpretation of the standard the work the Court is doing. The other four options are political, fiscal or status questions the clause does not pose."),

 dict(q="A state enacts a statute imposing a particular punishment, and it is challenged as cruel and unusual. Which claim from the course framework does the case most directly involve?",
   choices=[
     "That court decisions defining cruel and unusual punishment involve interpretation of the Eighth Amendment and its application to statutes",
     "That the debate about the Second and Fourth Amendments involves public safety",
     "That symbolic speech is protected by the First Amendment",
     "That the Second Amendment applies to the states",
     "That prior restraint faces a heavy presumption"], ans=0,
   why="EK 3.6.A.1 is the statement about the Eighth Amendment; the other four options name statements belonging to EK 3.6.A.2 and to topics 3.3, 3.4 and 3.5."),

 dict(q="How does the Eighth Amendment question illustrate LO 3.6.A's balance?",
   choices=[
     "A punishment serves public order, and the constraint on how far it may go is the individual freedom side of the same scale",
     "The Eighth Amendment concerns only public order and not individual freedom",
     "The Eighth Amendment concerns only individual freedom and not public order",
     "The Eighth Amendment resolves the balance by prohibiting all punishment",
     "The Eighth Amendment applies only when public safety is not at issue"], ans=0,
   why="LO 3.6.A's balance is between individual freedom and 'laws and enforcement procedures that promote public order and safety,' and a punishment is such a procedure with a constitutional ceiling on it."),

 dict(q="According to the course framework, the debate about the Second and Fourth Amendments involves concerns about",
   choices=[
     "public safety, and whether regulation of firearms or collection of digital metadata promotes or interferes with public safety and individual rights",
     "the interpretation of cruel and unusual punishment",
     "the freedom of the press and prior restraint",
     "the establishment and free exercise of religion",
     "the apportionment of legislative districts"], ans=0,
   why="EK 3.6.A.2 names the two amendments, the two subjects -- firearms and digital metadata -- and the two things at stake. The other options name statements from other topics."),

 dict(q="Which two subjects does EK 3.6.A.2 name as the objects of the debate?",
   choices=[
     "Government regulation of firearms and collection of digital metadata",
     "The death penalty and prior restraint",
     "School prayer and compulsory education",
     "Districting and campaign finance",
     "Search warrants and jury trials"], ans=0,
   why="EK 3.6.A.2 names exactly these two, one for each amendment: firearms regulation under the Second, metadata collection under the Fourth."),

 dict(q="Read the following excerpt.\n\n“The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause.”\n—U.S. Constitution, Fourth Amendment\n\nWhich word in this text creates the interpretive question EK 3.6.A.2's metadata debate turns on?",
   choices=[
     "Unreasonable, since whether a particular collection is unreasonable is not answered by the text",
     "Warrants, since the text defines the term completely",
     "Persons, since the text lists everyone it protects",
     "Houses, since the text names every place it covers",
     "Oath, since the text specifies who must swear it"], ans=0,
   why="The Amendment forbids UNREASONABLE searches without saying what is unreasonable, which is the standard a court must fill in when a new form of collection appears. The other words are more determinate."),

 dict(q="Why does the collection of digital metadata raise a Fourth Amendment question that older cases did not answer?",
   choices=[
     "The Amendment speaks of persons, houses, papers and effects, and information held by third parties about a person's activity fits none of those categories obviously",
     "The Amendment expressly excludes electronic information",
     "The Amendment applies only to searches conducted with force",
     "The Amendment was repealed as to electronic records",
     "The Amendment applies only to state governments"], ans=0,
   why="The text's four nouns describe tangible things a person holds, and EK 3.6.A.2's metadata debate exists because a category the framers did not have has to be fitted to them by interpretation."),

 dict(q="EK 3.6.A.2 asks whether a measure PROMOTES OR INTERFERES WITH public safety AND individual rights. How many distinct combinations does that phrasing allow?",
   choices=[
     "Four, since a measure may promote or fail to promote safety and may or may not burden rights",
     "Two, since a measure either promotes safety or protects rights",
     "One, since safety and rights always move together",
     "Three, since a measure cannot both promote safety and burden rights",
     "None, since the two cannot be assessed separately"], ans=0,
   why="EK 3.6.A.2 pairs two independent questions, which produces a grid rather than a spectrum. Treating it as a single trade-off is the half-reading item 16 corrects."),

 dict(q="Which combination allowed by EK 3.6.A.2 does a student who frames the debate as a simple trade-off tend to overlook?",
   choices=[
     "A measure that burdens rights and does NOT in fact promote safety",
     "A measure that promotes safety and burdens rights",
     "A measure that promotes safety and does not burden rights",
     "A measure that neither promotes safety nor burdens rights",
     "None; a trade-off framing covers every possibility"], ans=0,
   why="A trade-off framing assumes any burden on rights buys some safety, so it has no place for a measure that costs rights and delivers nothing. EK 3.6.A.2's wording leaves room for exactly that."),

 dict(q="A proposal would collect a new category of data. Under EK 3.6.A.2's framing, which pair of questions should an analyst ask?",
   choices=[
     "Does the collection actually improve safety, and does it burden individual rights?",
     "Is the collection popular, and is it inexpensive?",
     "Was the collection proposed by the executive branch, and does Congress support it?",
     "Has any other country adopted the collection, and when?",
     "Is the collection technically feasible, and who would administer it?"], ans=0,
   why="EK 3.6.A.2 names public safety and individual rights as the two things a measure may promote or interfere with, so those are the two questions. Popularity, cost and feasibility are real considerations the framework does not put on this scale."),

 dict(q="Which evidence would most directly support a claim that a particular collection program does NOT promote public safety?",
   choices=[
     "Investigations in which the collected data was available produced no better outcomes than comparable investigations without it",
     "A large share of the public opposes the program",
     "The program is expensive to operate",
     "The program collects a very large quantity of data",
     "Officials declined to describe the program publicly"], ans=0,
   why="Skill 5.B asks for evidence that bears on the claim, and a claim about whether a program improves outcomes needs a comparison of outcomes. Opposition, cost, volume and secrecy speak to other objections."),

 dict(q="Which evidence would most directly support a claim that a particular firearms regulation DOES promote public safety?",
   choices=[
     "Comparable jurisdictions that adopted the regulation experienced a measurable decline relative to those that did not",
     "A majority of residents support the regulation",
     "The regulation was upheld by a court",
     "The regulation is similar to one adopted elsewhere",
     "The regulation was enacted by a large legislative majority"], ans=0,
   why="EK 3.6.A.2's question is whether the measure PROMOTES public safety, which is an empirical claim requiring a comparison. Support, similarity and legislative margins bear on legitimacy rather than on effect."),

 dict(q="In McDonald v. Chicago (2010), the Supreme Court held that the Second Amendment right to keep and bear arms for self-defense is applicable to the states. How does the decision bear on EK 3.6.A.2's debate?",
   choices=[
     "It establishes that state firearms regulations are subject to a constitutional right, so the debate now takes place within a constitutional constraint rather than as pure policy",
     "It resolves the debate by holding all firearms regulation unconstitutional",
     "It resolves the debate by holding all firearms regulation constitutional",
     "It removes the states from the debate entirely",
     "It concerns the Fourth Amendment rather than the Second"], ans=0,
   why="The CED's statement of the holding is about APPLICABILITY to the states, which puts state regulation inside a constitutional frame without deciding which regulations survive -- exactly why EK 3.6.A.2 still calls it a debate."),

 dict(q="Read the following excerpt.\n\n“An unjust law is a code that a numerical or power majority group compels a minority group to obey but does not make binding on itself.”\n—Martin Luther King, Jr., “Letter from a Birmingham Jail,” 1963\n\nHow does this test bear on LO 3.6.A's balance?",
   choices=[
     "It offers a way to distinguish a genuine public order measure from one that imposes burdens the majority would not accept for itself",
     "It holds that all laws promoting public order are unjust",
     "It holds that individual freedom must always yield to public order",
     "It concerns criminal procedure rather than the justice of laws",
     "It states that only courts may determine whether a law is just"], ans=0,
   why="The Letter's test asks who bears the burden, which is a way of examining whether a measure genuinely serves the public order it claims to. The CED attaches the Letter to 3.6.A."),

 dict(q=_GRID + " Which conclusion is best supported by the table?",
   table=_GRID_TABLE,
   choices=[
     "Thirteen measures burdened rights without promoting safety, more than the six that promoted safety without burdening rights",
     "Every measure that burdened rights also promoted safety",
     "Most measures promoted safety",
     "No measure fell into the fourth category",
     "The four categories contained equal numbers of measures"], ans=0,
   why="The burden-without-benefit row is 13 against 6 for the benefit-without-burden row. Twenty-three of forty promoted safety, which is a majority, but seventeen of the thirty that burdened rights did so while promoting safety and thirteen did not."),

 dict(q=_GRID + " Which feature of the table most directly illustrates EK 3.6.A.2's phrasing?",
   table=_GRID_TABLE,
   choices=[
     "It has four rows rather than two, because a measure's effect on safety and its effect on rights are separate questions",
     "It has four rows because there are four amendments in the topic",
     "It reports counts rather than percentages",
     "It concerns only firearms regulations",
     "It shows that safety and rights always move in opposite directions"], ans=0,
   why="EK 3.6.A.2 asks whether a measure promotes or interferes with public safety AND individual rights, which is two independent questions and therefore four combinations. The last option is the trade-off assumption the grid disproves."),

 dict(q=_GRID + " A student uses this table to argue that most public safety measures are unjustified. What is the most important limitation of that argument?",
   table=_GRID_TABLE,
   choices=[
     "Whether a measure is justified depends on how heavily each effect weighs, which a count of categories does not report",
     "The table omits measures that burden rights, so no comparison is possible",
     "The table covers a single measure, so no pattern can be observed",
     "The table reports percentages that do not sum to one hundred",
     "The table gives no information about effects on public safety"], ans=0,
   why="LO 3.6.A's balance is about weight, and a category count treats a small burden and a large one as identical. All four categories, forty measures and both effect columns are plainly present."),

 dict(q=_METADATA + " Which conclusion is best supported by the table?",
   table=_METADATA_TABLE,
   choices=[
     "A warrant was required in one category that did not include the contents of communications, so contents are not the only thing that matters",
     "A warrant was required only where the contents of communications were included",
     "A warrant was required in every category",
     "A warrant was required in no category",
     "Every category included the contents of communications"], ans=0,
   why="The location row is marked No for contents and Yes for a warrant, which breaks the contents-only rule the second option states. Only one of four rows includes contents."),

 dict(q=_METADATA + " What does the location row suggest about how a court applies the Fourth Amendment's standard?",
   table=_METADATA_TABLE,
   choices=[
     "The quantity and duration of collection can matter as much as whether the contents were obtained",
     "The Fourth Amendment applies only to the contents of communications",
     "The Fourth Amendment applies only to physical searches",
     "The Fourth Amendment applies only when a person is arrested",
     "The Fourth Amendment does not apply to electronic information"], ans=0,
   why="A category with no contents that nevertheless required a warrant shows the standard turning on something other than contents, which is what makes EK 3.6.A.2's metadata question genuinely open."),

 dict(q=_METADATA + " A student concludes from the table that collecting addresses on envelopes and collecting months of location data are constitutionally equivalent because neither includes contents. What is the correction?",
   table=_METADATA_TABLE,
   choices=[
     "The table itself distinguishes them: one required a warrant and the other did not, so absence of contents is not sufficient to settle the question",
     "The table shows both required a warrant",
     "The table shows neither required a warrant",
     "The table shows both included contents",
     "The table does not report whether a warrant was required"], ans=0,
   why="The two rows agree in the contents column and differ in the warrant column, which is precisely what refutes the inference. Reading one column and stopping is the error the table is arranged to expose."),

 dict(q="LO 3.6.A asks how the Court has ATTEMPTED to balance individual freedom against public order and safety. Which answer is best supported by the framework as a whole?",
   choices=[
     "It has interpreted open-ended standards case by case in areas the framework identifies as still contested, without settling the balance in general",
     "It has established a fixed rule giving individual freedom priority",
     "It has established a fixed rule giving public safety priority",
     "It has declined to hear cases in which the two conflict",
     "It has referred the question to the states"], ans=0,
   why="EK 3.6.A.1's interpretation of an open standard and EK 3.6.A.2's continuing debate both describe work in progress, which is what LO 3.6.A's verb 'attempted' records."),

 dict(q="Why does the framework place three different amendments in a single topic?",
   choices=[
     "Each raises the same structural question -- how far a government may go in the name of order and safety before a guarantee stops it",
     "All three amendments were ratified on the same day",
     "All three amendments concern criminal procedure",
     "All three amendments have been repealed",
     "All three amendments protect the same right"], ans=0,
   why="LO 3.6.A names the balance rather than any amendment, and the Eighth, Second and Fourth appear together because each supplies a constitutional limit on a measure justified by public order or safety."),

 dict(q="A student writes an argument about one of this topic's debates. Which approach is most consistent with the course framework?",
   choices=[
     "State the claim, then supply evidence that bears on whether the measure promotes safety and whether it burdens rights",
     "State the claim and assert that the framework resolves it",
     "Describe the measure without taking a position on any question",
     "Report which party supports the measure",
     "Argue that constitutional questions cannot be answered"], ans=0,
   why="Skill 5.B for this topic is supporting a claim with relevant evidence, and EK 3.6.A.2 names the two questions evidence must bear on. The framework identifies these as debates and resolves none of them."),
]
