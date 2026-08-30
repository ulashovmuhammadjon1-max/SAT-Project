# AP U.S. GOVERNMENT AND POLITICS 3.1 The Bill of Rights -- 30 questions
# CED V.1 (2026), Unit 3 Civil Liberties and Civil Rights, 13-18% of the exam.
#
# LO 3.1.A Explain how the U.S. Constitution protects individual liberties and
#   rights.
#   EK 3.1.A.1 The Constitution includes a Bill of Rights specifically designed
#     to protect individual liberties and rights.
#   EK 3.1.A.2 Civil liberties are constitutionally established guarantees and
#     freedoms that protect citizens, opinions, and property against ARBITRARY
#     GOVERNMENT INTERFERENCE.
#   EK 3.1.A.3 The application of the Bill of Rights is CONTINUOUSLY
#     INTERPRETED by the courts.
# LO 3.1.B Describe the rights protected in the Bill of Rights.
#   EK 3.1.B.1 The Bill of Rights consists of the first ten Amendments, which
#     enumerate the liberties and rights of individuals.
#
# Every quoted amendment below is the ratified constitutional text, quoted and
# not paraphrased, per the brief's rule that a quotation is never invented. The
# two data stimulus items use a clearly labelled hypothetical survey, because
# this bank cannot verify a real pollster's numbers and a fabricated attribution
# would be worse than an honest hypothetical; every figure in them is recomputed
# from the table in verify_v3_1.py.
#
# The civil liberties / civil rights line matters here and is drawn the way the
# CED draws it: a civil LIBERTY is protection against arbitrary government
# interference (EK 3.1.A.2), a civil RIGHT is protection against discrimination
# based on a characteristic such as race or sex (EK 3.10.A.1). Items 9 and 10
# turn on exactly that distinction.
TOPIC = ("3.1", "The Bill of Rights", 3)
QUESTIONS = [
 dict(q="\"Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances.\"\n\nThe passage above is best understood as",
   choices=[
     "a restriction placed on government action in order to protect individual liberty",
     "a grant of authority allowing Congress to regulate expression in the public interest",
     "a guarantee that every person will receive the equal protection of the laws",
     "a power reserved to the states rather than delegated to the national government",
     "a procedural rule governing how federal criminal trials must be conducted"],
   ans=0,
   why="The amendment opens with the words \"Congress shall make no law,\" which is a prohibition on the government rather than a power given to it. EK 3.1.A.2 defines civil liberties as constitutional guarantees protecting citizens, opinions, and property against arbitrary government interference."),

 dict(q="\"The enumeration in the Constitution, of certain rights, shall not be construed to deny or disparage others retained by the people.\"\n\nWhich of the following claims is most directly supported by this text?",
   choices=[
     "Individuals may hold rights that the Constitution never lists by name",
     "Only the rights written into the first eight amendments may be enforced in court",
     "The states may add to the list of federal rights by amending their own constitutions",
     "Congress decides which rights the people retain in any given era",
     "A right must be exercised regularly or it is forfeited"],
   ans=0,
   why="This is the Ninth Amendment, and its whole function is to deny that the written list is exhaustive. EK 3.9.A.1 relies on it directly, noting that some justices and scholars point to the Ninth Amendment as support for the existence of unenumerated rights."),

 dict(q="\"The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people.\"\n\nThis amendment differs from most of the rest of the Bill of Rights because it",
   choices=[
     "allocates authority between levels of government rather than naming an individual freedom",
     "applies only to criminal proceedings brought in state courts",
     "was added to the Constitution long after the other nine amendments were ratified",
     "creates a right that the Supreme Court has never been asked to interpret",
     "gives Congress an explicit power to regulate commerce among the states"],
   ans=0,
   why="The Tenth Amendment is a federalism provision: it speaks about which government holds a power, not about a freedom an individual may assert. EK 3.1.B.1 describes the Bill of Rights as enumerating liberties and rights, and this amendment is the clearest exception to that pattern."),

 dict(q="A city ordinance requires a permit for any march on public streets. The city grants permits to a veterans' association and a labor union but denies one to an environmental group because officials disagree with the group's message. Which provision of the Bill of Rights does the denial most directly implicate?",
   choices=[
     "The First Amendment protections for speech and peaceable assembly",
     "The Fourth Amendment protection against unreasonable searches and seizures",
     "The Fifth Amendment protection against compelled self-incrimination",
     "The Eighth Amendment prohibition on excessive fines",
     "The Tenth Amendment reservation of powers to the states"],
   ans=0,
   why="The First Amendment protects both freedom of speech and the right of the people peaceably to assemble, and a permit denied because of the applicant's viewpoint is government interference with expression rather than a neutral regulation of traffic or safety."),

 dict(q="Police enter an apartment without a warrant and without consent, search a locked desk, and seize a laptop. Which amendment supplies the standard a court would apply first?",
   choices=[
     "The Fourth Amendment, which bars unreasonable searches and seizures and requires warrants on probable cause",
     "The First Amendment, which protects the freedom to express unpopular opinions",
     "The Sixth Amendment, which guarantees a speedy and public trial by an impartial jury",
     "The Eighth Amendment, which forbids cruel and unusual punishments",
     "The Second Amendment, which protects a right to keep and bear arms"],
   ans=0,
   why="The Fourth Amendment's text secures \"persons, houses, papers, and effects, against unreasonable searches and seizures\" and provides that no warrants shall issue but upon probable cause, which is precisely the question a warrantless entry raises."),

 dict(q="\"In all criminal prosecutions, the accused shall enjoy the right to a speedy and public trial, by an impartial jury of the State and district wherein the crime shall have been committed . . . and to have the Assistance of Counsel for his defence.\"\n\nA defendant who claims that he was tried four years after his arrest, with no explanation for the delay, is invoking",
   choices=[
     "the guarantee of a speedy trial",
     "the guarantee of assistance of counsel",
     "the guarantee of an impartial jury",
     "the requirement that trial occur in the district where the crime happened",
     "the requirement that the proceeding be open to the public"],
   ans=0,
   why="The Sixth Amendment lists these guarantees separately, and an unexplained four-year gap between arrest and trial is a complaint about timing rather than about the lawyer, the jury, the venue, or public access."),

 dict(q="A state legislature passes a law providing that anyone arrested for arson may be held for six months before any hearing, with no opportunity to contest the detention. Which principle of the Bill of Rights does this most clearly violate?",
   choices=[
     "The requirement that government not deprive a person of liberty without due process of law",
     "The prohibition on establishing an official religion",
     "The protection of the right to keep and bear arms",
     "The reservation to the states of powers not delegated to the national government",
     "The guarantee that private property will not be taken without just compensation"],
   ans=0,
   why="Detention with no hearing at all is the textbook case of an arbitrary procedure. EK 3.8.A.2 states that procedural due process requires government officials to use methods that are not arbitrary when making decisions affecting constitutionally protected rights."),

 dict(q="Which of the following best describes what the Bill of Rights was designed to do when it was ratified in 1791?",
   choices=[
     "Limit the powers of the newly created national government over individuals",
     "Give the national government authority to override state bills of rights",
     "Set out the qualifications required for federal office",
     "Establish the structure and jurisdiction of the federal court system",
     "Guarantee that every adult citizen would be eligible to vote"],
   ans=0,
   why="EK 3.1.A.1 states that the Constitution includes a Bill of Rights specifically designed to protect individual liberties and rights, and the ratification debate that produced it turned on Anti-Federalist fears of an unchecked national government."),

 dict(q="A state statute bars any person who was born outside the United States from holding a license to practice architecture. The challenge to this statute is best described as a claim about",
   choices=[
     "civil rights, because it concerns discrimination based on a personal characteristic",
     "civil liberties, because it concerns government interference with private opinion",
     "federalism, because it concerns which level of government may license professions",
     "separation of powers, because it concerns the legislature acting instead of an agency",
     "judicial review, because it concerns the authority of courts to hear the case"],
   ans=0,
   why="EK 3.10.A.1 defines civil rights as protections against discrimination based on characteristics such as race, national origin, religion, and sex, guaranteed by the due process and equal protection clauses; a rule keyed to place of birth is a classification of persons, not an interference with expression."),

 dict(q="A city forbids all leafleting in a public park because officials find some of the leaflets distasteful. The challenge to this ordinance is best described as a claim about",
   choices=[
     "civil liberties, because it concerns arbitrary government interference with expression",
     "civil rights, because it concerns unequal treatment based on national origin",
     "federalism, because it concerns the balance of authority between a city and a state",
     "the Electoral College, because it concerns how political messages reach voters",
     "checks and balances, because it concerns the executive rather than the legislature"],
   ans=0,
   why="EK 3.1.A.2 defines a civil liberty as a constitutional guarantee protecting citizens and opinions against arbitrary government interference, which is exactly what a ban imposed because officials dislike the content is. Nothing in the ordinance sorts people by a personal characteristic."),

 dict(q="The Supreme Court has held that the Fourth Amendment requires a warrant before police may search the data on an arrested person's cell phone, a question the framers could not have anticipated. This development best illustrates which claim about the Bill of Rights?",
   choices=[
     "Its application is continuously interpreted by the courts as circumstances change",
     "Its provisions expire unless Congress renews them each session",
     "Its meaning is fixed by the text and has not been the subject of judicial disagreement",
     "It applies only to the national government and never to the states",
     "It may be amended by a majority vote of the Supreme Court"],
   ans=0,
   why="EK 3.1.A.3 states that the application of the Bill of Rights is continuously interpreted by the courts, and the CED lists Riley v. California (2014) as an illustrative example of exactly this at Topic 3.8."),

 dict(q="\"Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted.\"\n\nA defendant argues that a mandatory sentence for a minor offense is grossly disproportionate to the crime. This argument rests on which clause of the passage?",
   choices=[
     "The prohibition on cruel and unusual punishments",
     "The prohibition on excessive bail",
     "The prohibition on excessive fines",
     "The guarantee of an impartial jury",
     "The guarantee against double jeopardy"],
   ans=0,
   why="Bail is the money required to secure release before trial and a fine is a monetary penalty, so a claim about the severity of a term of imprisonment falls under the Eighth Amendment's cruel and unusual punishments clause, which EK 3.6.A.1 identifies as the site of proportionality debates."),

 dict(q="Which of the following statements about the Bill of Rights is accurate?",
   choices=[
     "It consists of the first ten amendments to the Constitution",
     "It was included in the original document signed in Philadelphia in 1787",
     "It may be suspended by executive order during an economic emergency",
     "It applies only to citizens and never to lawfully present noncitizens",
     "It contains a provision guaranteeing a right to public education"],
   ans=0,
   why="EK 3.1.B.1 states that the Bill of Rights consists of the first ten Amendments to the Constitution, which enumerate the liberties and rights of individuals; they were proposed by the First Congress and ratified in 1791, after the original document."),

 dict(q="A school district requires every student to recite a prayer written by the district's board at the start of each day. Students who object may remain silent. Which pair of First Amendment concerns does this policy raise most directly?",
   choices=[
     "Establishment of religion and free exercise of religion",
     "Freedom of the press and the right to petition",
     "Peaceable assembly and the right to bear arms",
     "Free exercise of religion and protection against self-incrimination",
     "Freedom of speech and protection against unreasonable searches"],
   ans=0,
   why="A prayer composed and prescribed by a government body is state sponsorship of religious activity, which is the establishment question decided in Engel v. Vitale (1962), and compelling students to participate presses on the free exercise of those who believe differently."),

 dict(q="Which of the following scenarios is NOT a civil liberties question under the Bill of Rights?",
   choices=[
     "A private employer fires a worker for criticizing the company on social media",
     "A state prohibits a newspaper from publishing an article about a pending trial",
     "A police officer searches a car trunk without a warrant or probable cause",
     "A county jail denies an inmate access to a lawyer before questioning",
     "A city bans door-to-door religious canvassing"],
   ans=0,
   why="Civil liberties under EK 3.1.A.2 protect against GOVERNMENT interference; the Bill of Rights restrains state action, so a purely private employer's discipline of an employee raises no constitutional claim, however unfair it may be."),

 dict(q="The Fifth Amendment provides that no person shall \"be compelled in any criminal case to be a witness against himself.\" A suspect who refuses to answer a detective's questions during a custodial interrogation is exercising",
   choices=[
     "the privilege against compelled self-incrimination",
     "the right to a speedy and public trial",
     "the protection against unreasonable seizure of property",
     "the guarantee of just compensation for a taking",
     "the prohibition on excessive bail"],
   ans=0,
   why="The clause quoted forbids compelling a person to testify against himself, and EK 3.8.A.2 notes that the Miranda rule exists to inform accused persons of exactly these Fifth and Sixth Amendment protections before interrogation."),

 dict(q="A state transportation agency takes a strip of privately owned farmland to widen a highway and pays the owner nothing. The owner's strongest constitutional claim arises from",
   choices=[
     "the requirement that private property not be taken for public use without just compensation",
     "the prohibition on establishing an official religion",
     "the guarantee of trial by an impartial jury in criminal prosecutions",
     "the protection of the right to keep and bear arms",
     "the prohibition on cruel and unusual punishments"],
   ans=0,
   why="The Fifth Amendment's takings clause states that private property shall not \"be taken for public use, without just compensation,\" which is the express constitutional protection of property named in EK 3.1.A.2."),

 dict(q="Consider the following two situations.\n\nI. A federal statute makes it a crime to burn a copy of the Constitution in protest.\nII. A private university expels a student for burning a copy of the Constitution on campus.\n\nWhich of the following correctly describes these situations?",
   choices=[
     "Only situation I raises a Bill of Rights claim, because only it involves government action",
     "Only situation II raises a Bill of Rights claim, because only it involves an educational institution",
     "Both raise Bill of Rights claims, because both punish symbolic expression",
     "Neither raises a Bill of Rights claim, because destroying a document is conduct rather than speech",
     "Both raise Bill of Rights claims, but only in states that have adopted their own bills of rights"],
   ans=0,
   why="The Bill of Rights limits government, so a federal criminal statute is squarely covered while a private institution's discipline is not state action. EK 3.3.A.1 separately establishes that symbolic speech is protected expression, which is why the first situation is a real claim rather than a frivolous one."),

 dict(q="An interest group publishes a report arguing that a proposed federal database of citizens' medical records would let officials monitor individuals without any showing of wrongdoing. The group's argument is best understood as an appeal to",
   choices=[
     "the protection of individuals against arbitrary government interference",
     "the reservation of undelegated powers to the states",
     "the guarantee of equal protection for groups facing discrimination",
     "the requirement that revenue bills originate in the House of Representatives",
     "the prohibition on religious tests for federal office"],
   ans=0,
   why="EK 3.1.A.2 defines civil liberties as guarantees protecting citizens, opinions, and property against arbitrary government interference, and surveillance with no individualized suspicion is the paradigm of an arbitrary intrusion. EK 3.6.A.2 raises the same concern about the collection of digital metadata."),

 dict(q="Which of the following best explains why the Bill of Rights has generated so much litigation over more than two centuries?",
   choices=[
     "Its guarantees are stated in broad terms whose application to new circumstances must be worked out by courts",
     "It contains a clause directing the Supreme Court to review each amendment every ten years",
     "Its provisions contradict one another so directly that no case can be decided consistently",
     "It was written to expire unless reauthorized, so its status is repeatedly relitigated",
     "It applies to private conduct as well as to government, which multiplies the possible disputes"],
   ans=0,
   why="EK 3.1.A.3 states that the application of the Bill of Rights is continuously interpreted by the courts; phrases such as \"unreasonable\" searches and \"cruel and unusual\" punishments do not decide their own cases, so their meaning is settled case by case."),

 dict(q="A national survey asked adults how essential each of the following rights is to their own sense of freedom. The percentage saying \"essential\" is shown by whether the respondent owns a firearm.\n\nAccording to the data, gun owners and non-owners differed most sharply on",
   table=dict(headers=["Right", "Gun owners saying essential", "Non-owners saying essential"],
     rows=[["Freedom of speech", "91", "89"],
           ["Freedom of religion", "84", "80"],
           ["The right to vote", "90", "92"],
           ["The right to own guns", "74", "35"],
           ["Freedom from unreasonable searches", "77", "74"]]),
   choices=[
     "the right to own guns",
     "freedom of speech",
     "the right to vote",
     "freedom of religion",
     "freedom from unreasonable searches"],
   ans=0,
   why="The gap between the two columns is 39 percentage points on gun ownership and no more than 4 percentage points on any other row, so the firearms item is the only one on which the two groups diverge substantially."),

 dict(q="A national survey asked adults how essential each of the following rights is to their own sense of freedom. The percentage saying \"essential\" is shown by whether the respondent owns a firearm.\n\nWhich of the following conclusions is best supported by the data?",
   table=dict(headers=["Right", "Gun owners saying essential", "Non-owners saying essential"],
     rows=[["Freedom of speech", "91", "89"],
           ["Freedom of religion", "84", "80"],
           ["The right to vote", "90", "92"],
           ["The right to own guns", "74", "35"],
           ["Freedom from unreasonable searches", "77", "74"]]),
   choices=[
     "Americans broadly agree that most Bill of Rights protections matter, while disagreeing sharply over the scope of one of them",
     "Americans are deeply divided over every liberty protected by the Bill of Rights",
     "Gun owners place a lower value on constitutional protections generally than non-owners do",
     "Non-owners regard the right to vote as unimportant compared with other freedoms",
     "A majority of both groups regards freedom of religion as inessential to personal freedom"],
   ans=0,
   why="Four of the five rows show both groups within a few points of each other and above 70 percent, while the firearms row shows a 39-point gap, so the pattern is broad consensus with a single sharp disagreement. EK 3.6.A.2 frames that firearms disagreement as an ongoing debate about public safety and individual rights."),

 dict(q="Two students are debating whether the Bill of Rights is best described as a list of things the government must do or a list of things it may not do. Which piece of textual evidence most strongly supports the second view?",
   choices=[
     "The First Amendment begins by saying that Congress \"shall make no law\" on certain subjects",
     "The Tenth Amendment refers to powers reserved to the states",
     "The Sixth Amendment requires that a jury be drawn from the district where the crime occurred",
     "The Ninth Amendment refers to rights retained by the people",
     "The Fifth Amendment refers to a grand jury indictment"],
   ans=0,
   why="An express prohibition on lawmaking is the clearest form of a negative restraint, which is what the second view asserts. The Sixth Amendment's venue requirement is in fact an affirmative obligation on government, so it cuts the other way."),

 dict(q="Congress passes a statute providing that no federal court may hear any claim that a federal agency violated the Fourth Amendment. A critic argues the statute is dangerous because it would leave a constitutional guarantee with no way to be enforced. This criticism rests most directly on the idea that",
   choices=[
     "the meaning and force of the Bill of Rights depend on judicial interpretation and enforcement",
     "the Bill of Rights was intended to apply only to the states",
     "Congress may not pass any statute affecting the jurisdiction of the federal courts",
     "the Fourth Amendment protects only property rather than persons",
     "constitutional amendments take effect only when Congress passes enabling legislation"],
   ans=0,
   why="EK 3.1.A.3 makes judicial interpretation the mechanism by which the Bill of Rights is applied; a guarantee that no court may consider becomes, in practical terms, unenforceable, which is exactly the critic's point."),

 dict(q="A city council responds to a series of burglaries by authorizing officers to enter and inspect any home in a designated neighborhood without a warrant. A resident who challenges the policy would rely on the Fourth Amendment's language that",
   choices=[
     "no warrants shall issue but upon probable cause, particularly describing the place to be searched",
     "the accused shall enjoy the right to a speedy and public trial",
     "excessive bail shall not be required",
     "private property shall not be taken for public use without just compensation",
     "Congress shall make no law abridging the freedom of speech"],
   ans=0,
   why="A blanket authorization to search every home in an area is the opposite of a warrant supported by probable cause and particularly describing the place to be searched, which is the standard the Fourth Amendment's warrant clause sets."),

 dict(q="Which of the following pairs correctly matches a right to the amendment that protects it?",
   choices=[
     "The right to counsel in a criminal prosecution and the Sixth Amendment",
     "The right to petition the government and the Fifth Amendment",
     "The protection against double jeopardy and the Fourth Amendment",
     "The prohibition on quartering soldiers in private homes and the Second Amendment",
     "The protection against unreasonable searches and the Eighth Amendment"],
   ans=0,
   why="The Sixth Amendment's text guarantees the accused \"the Assistance of Counsel for his defence,\" and Gideon v. Wainwright (1963) rests on that clause. Petition belongs to the First Amendment, double jeopardy to the Fifth, quartering to the Third, and searches to the Fourth."),

 dict(q="A political scientist writes that \"the Bill of Rights is not self-executing; it becomes real only when someone with standing brings a claim and a court agrees to hear it.\" This argument implies that",
   choices=[
     "the practical scope of constitutional liberties depends partly on access to the courts",
     "constitutional rights belong only to people who have already been convicted of a crime",
     "the Supreme Court may add new amendments when existing ones prove inadequate",
     "state courts have no authority to interpret provisions of the federal Constitution",
     "a right that has never been litigated has been formally repealed"],
   ans=0,
   why="If a guarantee operates through litigation, then whoever cannot reach a court cannot enforce it, which is a claim about access rather than about the text. This follows from EK 3.1.A.3's account of continuous judicial interpretation."),

 dict(q="A state passes a law requiring every household to display the state flag. A homeowner refuses on the ground that the government may not compel her to express a message she rejects. Her claim is best characterized as",
   choices=[
     "a First Amendment claim, because compelled expression is a form of interference with speech",
     "a Fourth Amendment claim, because the requirement concerns the home",
     "a Tenth Amendment claim, because the state has exceeded its reserved powers",
     "an Eighth Amendment claim, because the penalty for refusal is a fine",
     "a Fifth Amendment claim, because displaying a flag is a taking of property"],
   ans=0,
   why="EK 3.3.A.1 states that speech including symbolic speech, defined as nonverbal action that communicates an idea or belief, is protected by the First Amendment; forcing a person to display a symbol conscripts that protected channel rather than merely regulating conduct."),

 dict(q="Which of the following best explains why the Bill of Rights was proposed and ratified so soon after the Constitution itself?",
   choices=[
     "Several states ratified the Constitution only after being assured that a list of protected liberties would be added",
     "The Supreme Court ordered Congress to draft one in its first term",
     "The Articles of Confederation had required that any successor document include one",
     "President Washington refused to take office until the amendments were ratified",
     "The original Constitution had granted Congress an explicit power to abolish the state courts"],
   ans=0,
   why="Ratification in several states was secured on the understanding that amendments protecting individual liberties would follow, which is why EK 3.1.A.1 describes the Bill of Rights as specifically designed for that purpose. The Court did not exist until after ratification, and the Articles contained no such requirement."),

 dict(q="A federal law bars anyone convicted of a felony from ever publishing a book about the crime. Which of the following best states why this raises a Bill of Rights problem even though the people affected have been convicted of crimes?",
   choices=[
     "Constitutional liberties limit what government may do to any person, not only to the sympathetic",
     "Felons are the only group the Bill of Rights was written to protect",
     "The Bill of Rights applies only after a sentence has been fully served",
     "Publishing a book is conduct rather than expression, so a special rule applies",
     "Only Congress, and not the states, may regulate publishing"],
   ans=0,
   why="EK 3.1.A.2 frames civil liberties as guarantees against arbitrary government interference with citizens and their opinions, with no exception for unpopular claimants; a permanent ban on writing about a subject is a restriction on expression regardless of who is subject to it."),
]
