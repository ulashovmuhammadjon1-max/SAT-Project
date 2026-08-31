# AP U.S. GOVERNMENT AND POLITICS 3.10 Social Movements and Equal Protection
# -- 30 questions
# CED V.1 (c) 2026, Unit 3 Civil Liberties and Civil Rights.
# Learning objective 3.10.A: explain how CONSTITUTIONAL PROVISIONS have
# SUPPORTED AND MOTIVATED social movements.
# Suggested skill for this topic (CED p. 92): 4.C, source analysis -- explain how
# the implications of the argument or perspective in the source may affect
# political principles, institutions, processes, policies, and behaviors.
#
# Essential knowledge relied on:
#   EK 3.10.A.1 -- "Civil rights protect individuals from discrimination based on
#     characteristics such as RACE, NATIONAL ORIGIN, RELIGION, AND SEX; these
#     rights are guaranteed TO ALL PERSONS under the DUE PROCESS and EQUAL
#     PROTECTION clauses of the U.S. Constitution, AS WELL AS ACTS OF CONGRESS."
#     Three sources, not one, and the third is statutory.
#   EK 3.10.A.2 -- "The civil rights movement, the women's rights movement, and
#     advocacy for LGBTQ rights are evidence of how the EQUAL PROTECTION CLAUSE
#     CAN SUPPORT AND MOTIVATE social movements, as represented by:
#       i.   Dr. Martin Luther King's 'Letter from a Birmingham Jail' and the
#            civil rights movement of the 1960s
#       ii.  The National Organization for Women and the women's rights movement
#       iii. The pro-life and pro-choice movements"
#
# THE DIRECTION OF CAUSATION IS THE TOPIC, and it is the thing a definition-recall
# question would miss entirely. LO 3.10.A does not ask what the equal protection
# clause means; 3.12 does that. It asks how a constitutional provision SUPPORTED
# AND MOTIVATED people to organise -- a clause as a resource that a movement
# picks up and argues from, not a rule a court applies to it. Items 10 to 17 are
# built on that reading, which is also why the suggested skill is source
# analysis: the sources are what movements wrote, and the question is what
# follows from their arguments.
#
# EK 3.10.A.2.iii NAMES BOTH SIDES OF ONE QUESTION -- "the pro-life and
# pro-choice movements" -- and that is deliberate on the framework's part. A
# provision that motivates a movement motivates movements that disagree with each
# other, so the framework's claim is about MOBILISATION and not about which side
# the clause vindicates. Item 24 makes exactly that the question, and no item in
# this module takes a position on the merits of any movement it names.
#
# Documents the CED attaches to 3.10.A (pp. 26-27): the Emancipation
# Proclamation, the Gettysburg Address, and "Letter from a Birmingham Jail."
# Required cases the CED attaches to 3.10.A (p. 31): Brown v. Board of Education,
# Engel v. Vitale, Wisconsin v. Yoder. Engel and Yoder belong here because
# RELIGION is one of the characteristics EK 3.10.A.1 names.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the Fourteenth Amendment, the
# Emancipation Proclamation, the Gettysburg Address and the Letter are quoted
# verbatim. Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("3.10", "Social Movements and Equal Protection", 3)

_COMPLAINTS = ("In a hypothetical year, the table reports complaints filed with a state civil "
               "rights commission, classified by the characteristic the complainant alleged was "
               "the basis of the discrimination.")
_COMPLAINTS_TABLE = dict(
    headers=["Characteristic alleged", "Complaints filed", "Complaints found to have merit"],
    rows=[["Race", "1840", "412"],
          ["National origin", "610", "138"],
          ["Religion", "295", "71"],
          ["Sex", "1320", "349"]])

_PETITIONS = ("The table reports a hypothetical review of petitions filed by advocacy "
              "organizations, classified by the legal basis each petition principally invoked.")
_PETITIONS_TABLE = dict(
    headers=["Legal basis principally invoked", "Petitions", "Share of all petitions (%)"],
    rows=[["Equal protection clause of the Fourteenth Amendment", "246", "62"],
          ["Due process clause of the Fourteenth Amendment", "88", "22"],
          ["First Amendment", "44", "11"],
          ["An act of Congress only, with no constitutional provision", "20", "5"]])

QUESTIONS = [
 dict(q="According to the course framework, what do civil rights protect individuals from?",
   choices=[
     "Discrimination based on characteristics such as race, national origin, religion, and sex",
     "Prosecution for crimes they did not commit",
     "Searches conducted without a warrant",
     "Laws passed after the conduct they punish",
     "Taxation without representation in the legislature"], ans=0,
   why="EK 3.10.A.1 defines civil rights in exactly these terms and names exactly these four characteristics. The other four options describe protections the framework locates in the procedural guarantees of topic 3.8 or in provisions outside this topic."),

 dict(q="Which four characteristics does EK 3.10.A.1 name as bases of discrimination that civil rights protect against?",
   choices=[
     "Race, national origin, religion, and sex",
     "Race, wealth, party membership, and age",
     "Religion, occupation, residence, and education",
     "National origin, military service, marital status, and income",
     "Sex, political opinion, criminal record, and language"], ans=0,
   why="EK 3.10.A.1 lists race, national origin, religion, and sex, introduced by the words 'characteristics such as', which makes the list illustrative rather than closed but makes these four the framework's own examples."),

 dict(q="According to EK 3.10.A.1, from which sources are civil rights guaranteed?",
   choices=[
     "The due process and equal protection clauses of the Constitution, as well as acts of Congress",
     "The equal protection clause alone",
     "Acts of Congress alone",
     "State constitutions alone",
     "Executive orders issued by the president"], ans=0,
   why="EK 3.10.A.1 names three sources in one sentence: two constitutional clauses and legislation. A question that offers only the clause omits the statutory half of the framework's own answer."),

 dict(q="Why does it matter that EK 3.10.A.1 names acts of Congress alongside two constitutional clauses?",
   choices=[
     "It means a civil right may rest on a statute that a later Congress could amend, as well as on a constitutional provision that it could not",
     "It means constitutional clauses have no role in protecting civil rights",
     "It means Congress may amend the Constitution by ordinary legislation",
     "It means civil rights exist only where Congress has legislated",
     "It means the Supreme Court may not hear civil rights cases"], ans=0,
   why="EK 3.10.A.1's list mixes a constitutional source with a legislative one, and the two are not equally durable: a statute is repealable by the ordinary lawmaking process while a clause of the Constitution is not."),

 dict(q="EK 3.10.A.1 says civil rights are guaranteed to ALL PERSONS. What follows from that wording?",
   choices=[
     "The guarantee is not limited to citizens",
     "The guarantee applies only to citizens by birth",
     "The guarantee applies only to residents of a single state",
     "The guarantee applies only to persons who have registered to vote",
     "The guarantee applies only to adults"], ans=0,
   why="EK 3.10.A.1's phrase is 'guaranteed to all persons', and the Fourteenth Amendment's own equal protection language likewise runs to 'any person within its jurisdiction' rather than to citizens."),

 dict(q="Read the following excerpt.\n\n“…nor shall any State deprive any person of life, liberty, or property, without due process of law; nor deny to any person within its jurisdiction the equal protection of the laws.”\n—U.S. Constitution, Fourteenth Amendment, Section 1\n\nWhich pair of guarantees does this sentence contain?",
   choices=[
     "A due process guarantee and an equal protection guarantee, the two clauses EK 3.10.A.1 names",
     "A free exercise guarantee and an establishment guarantee",
     "A speech guarantee and a press guarantee",
     "A search guarantee and a seizure guarantee",
     "A counsel guarantee and a jury guarantee"], ans=0,
   why="The sentence contains the two clauses EK 3.10.A.1 identifies as constitutional sources of civil rights, and both run to ANY PERSON rather than to citizens. The other four pairs live in the First, Fourth and Sixth Amendments."),

 dict(q="Whose conduct does the sentence quoted from the Fourteenth Amendment restrain by its own terms?",
   choices=[
     "A State",
     "Congress",
     "The president",
     "A private employer",
     "A foreign government"], ans=0,
   why="The grammatical subject of both clauses is 'any State', which is why the Fourteenth Amendment is the provision that reaches state and local action. Reaching private conduct is what EK 3.10.A.1's third source, acts of Congress, is for."),

 dict(q="A private restaurant refuses service on the basis of a customer's race. Which source named in EK 3.10.A.1 most directly reaches that conduct?",
   choices=[
     "An act of Congress, since the equal protection clause by its terms restrains a State rather than a private business",
     "The equal protection clause, since it reaches all discrimination of any kind",
     "The due process clause, since a business decision is a procedure",
     "The Ninth Amendment, since dining is not mentioned in the Constitution",
     "No source, since the framework names only constitutional provisions"], ans=0,
   why="The Fourteenth Amendment's clauses are addressed to a State, so private conduct is reached by the third source EK 3.10.A.1 names. This is precisely why the framework's sentence has three items rather than two."),

 dict(q="According to EK 3.10.A.2, which constitutional provision can support and motivate social movements?",
   choices=[
     "The equal protection clause",
     "The Tenth Amendment",
     "The Commerce Clause",
     "The Supremacy Clause",
     "The Necessary and Proper Clause"], ans=0,
   why="EK 3.10.A.2 names the equal protection clause specifically as the provision the three movements it lists are evidence about. The other four clauses concern the distribution of power among governments rather than the treatment of persons."),

 dict(q="Which three movements does EK 3.10.A.2 name as evidence that the equal protection clause can support and motivate social movements?",
   choices=[
     "The civil rights movement, the women's rights movement, and advocacy for LGBTQ rights",
     "The abolitionist, temperance, and labor movements",
     "The progressive, populist, and environmental movements",
     "The suffrage, prohibition, and antiwar movements",
     "The consumer, veterans, and taxpayer movements"], ans=0,
   why="EK 3.10.A.2 names exactly these three. The other options list movements that are real but that the framework does not name in this statement, so they are not the course content this item tests."),

 dict(q="LO 3.10.A asks how constitutional provisions have SUPPORTED AND MOTIVATED social movements. What does that phrasing ask about, that a question on the meaning of the equal protection clause would not?",
   choices=[
     "How a clause functions as a resource that people organize around and argue from, rather than only as a rule a court applies",
     "How many cases the Supreme Court has decided under the clause",
     "Which state ratified the Fourteenth Amendment first",
     "How the clause is worded in each state constitution",
     "Whether the clause was originally intended to be enforceable"], ans=0,
   why="The objective's verbs are SUPPORTED and MOTIVATED, which describe an effect on people rather than on litigation, and the suggested skill for this topic is source analysis of what movements themselves argued."),

 dict(q="Read the following excerpt.\n\n“Injustice anywhere is a threat to justice everywhere. We are caught in an inescapable network of mutuality, tied in a single garment of destiny. Whatever affects one directly, affects all indirectly.”\n—Martin Luther King, Jr., “Letter from a Birmingham Jail,” 1963\n\nWhat implication does this argument have for how a local grievance should be treated?",
   choices=[
     "A wrong confined to one place is properly the concern of people everywhere, which supplies a reason for a national movement rather than a local complaint",
     "A wrong should be addressed only by the community in which it occurs",
     "A wrong may be ignored unless a majority is affected by it",
     "A wrong is a matter for courts alone and not for citizens",
     "A wrong should be addressed only after it has spread to other places"], ans=0,
   why="The passage's claim is that effects are not confined by locality, and the CED attaches the Letter to 3.10.A as a source about the civil rights movement of the 1960s. Read for its implications, as skill 4.C directs, it argues a local injustice into a national concern."),

 dict(q="Read the following excerpt.\n\n“One has not only a legal but a moral responsibility to obey just laws. Conversely, one has a moral responsibility to disobey unjust laws.”\n—Martin Luther King, Jr., “Letter from a Birmingham Jail,” 1963\n\nWhich claim does this passage rest on?",
   choices=[
     "That a law's justice can be assessed independently of the fact that it has been enacted",
     "That every enacted law is just because it was enacted",
     "That no law creates any obligation at all",
     "That obedience is owed only to laws a person voted for",
     "That courts rather than citizens decide which laws are just"], ans=0,
   why="The passage distinguishes a legal from a moral responsibility and makes the second turn on whether the law is just, which presupposes an assessment independent of enactment. That premise is what allows a movement to argue against a law that is validly on the books."),

 dict(q="A student is asked how “Letter from a Birmingham Jail” relates to the equal protection clause. Which answer best reflects EK 3.10.A.2?",
   choices=[
     "The framework lists the Letter and the civil rights movement of the 1960s as evidence of how the clause can support and motivate a movement",
     "The framework says the Letter was written by the Supreme Court to explain the clause",
     "The framework says the Letter repealed the clause",
     "The framework says the clause was adopted in response to the Letter",
     "The framework says the Letter concerns freedom of the press rather than equality"], ans=0,
   why="EK 3.10.A.2.i pairs the Letter with the civil rights movement of the 1960s as the framework's first illustration of the clause supporting and motivating a movement. The Letter was written in 1963 and the Fourteenth Amendment was ratified in 1868, so the clause could not be a response to it."),

 dict(q="Read the following excerpt.\n\n“Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.”\n—Abraham Lincoln, Gettysburg Address, 1863\n\nHow could a later social movement use this passage?",
   choices=[
     "As a statement of a national commitment to equality that existing practice had not yet met, and therefore as a standard to hold the country to",
     "As a statement that equality had already been achieved and required no further action",
     "As a legal holding binding on the Supreme Court",
     "As a repeal of the Constitution's provisions on representation",
     "As an argument that equality is a matter for the states alone"], ans=0,
   why="The CED attaches the Gettysburg Address to 3.10.A, and read for its implications the passage states a founding proposition rather than a description of conditions, which is what makes it usable as a measure of the distance still to travel."),

 dict(q="Read the following excerpt.\n\n“…all persons held as slaves within any State or designated part of a State, the people whereof shall then be in rebellion against the United States, shall be then, thenceforward, and forever free…”\n—Abraham Lincoln, Emancipation Proclamation, 1863\n\nWhich limitation is stated in the text itself?",
   choices=[
     "It reaches persons held in states or parts of states then in rebellion, rather than everywhere in the country",
     "It reaches only persons who had already escaped",
     "It takes effect only after a constitutional amendment is ratified",
     "It applies only to persons born after its issuance",
     "It applies to every state without exception"], ans=0,
   why="The text conditions its reach on the people of the place being 'in rebellion against the United States', which is a limitation on its own face. The CED attaches the Proclamation to 3.10.A, and EK 3.12.A.1.i records that the Thirteenth Amendment was the step that permanently abolished slavery."),

 dict(q="Why is the geographic limit written into the Emancipation Proclamation useful evidence for how constitutional provisions motivate social movements?",
   choices=[
     "A measure that falls short of a principle it invokes gives a movement a stated commitment to demand the completion of",
     "A measure that falls short of a principle proves the principle was abandoned",
     "A measure with a limit cannot be cited by anyone afterwards",
     "A limit in a document shows that no movement formed around it",
     "A limit shows that the document was never issued"], ans=0,
   why="LO 3.10.A asks how provisions have supported and motivated movements, and a document that states a principle while reaching only part of the country supplies both the standard and the visible gap. That gap is the material of a movement's argument."),

 dict(q="In Brown v. Board of Education (1954), the Supreme Court held that race-based school segregation violates the equal protection clause of the Fourteenth Amendment. Why is that decision relevant to LO 3.10.A?",
   choices=[
     "It shows the clause producing a concrete result that a movement could point to and build on",
     "It shows that the clause protects only school children",
     "It shows that movements have no effect on constitutional interpretation",
     "It shows that the clause was repealed and replaced",
     "It shows that segregation was a matter of due process rather than equal protection"], ans=0,
   why="The CED attaches Brown to 3.10.A and states its holding under the equal protection clause. LO 3.10.A is about how a provision supports and motivates a movement, and a decision applying the clause is the clearest form that support can take."),

 dict(q="In Engel v. Vitale (1962), the Supreme Court held that school sponsorship of religious activities violates the Establishment Clause of the First Amendment. Why does the course framework attach this case to a topic on social movements and equal protection?",
   choices=[
     "Religion is one of the characteristics EK 3.10.A.1 names, so a decision about religious practice bears on the protections this topic covers",
     "The case was decided on the equal protection clause",
     "The case concerned discrimination on the basis of sex",
     "The case held that acts of Congress cannot protect civil rights",
     "The case overruled Brown v. Board of Education"], ans=0,
   why="EK 3.10.A.1 lists religion among the characteristics civil rights protect against discrimination on, which is why the CED cross-lists a religion case here. The holding itself rests on the Establishment Clause, not on equal protection."),

 dict(q="In Wisconsin v. Yoder (1972), the Supreme Court held that compelling Amish students to attend school past the eighth grade violates the Free Exercise Clause of the First Amendment. What does the case add to this topic?",
   choices=[
     "An example of a small religious community's claim prevailing against a generally applicable state law",
     "An example of a claim brought under the equal protection clause",
     "An example of a claim that acts of Congress could not have reached",
     "An example of the Court declining to hear a religious claim",
     "An example of a decision that applied only to the national government"], ans=0,
   why="The CED states the Yoder holding under the Free Exercise Clause and attaches the case to 3.10.A, where religion is one of the named characteristics. Compulsory attendance is state law, so the case is about a state law giving way to a minority community's claim."),

 dict(q="Which organization does EK 3.10.A.2 name in connection with the women's rights movement?",
   choices=[
     "The National Organization for Women",
     "The League of Women Voters",
     "The American Civil Liberties Union",
     "The National Association of Manufacturers",
     "The National Education Association"], ans=0,
   why="EK 3.10.A.2.ii names the National Organization for Women specifically, which makes it course content for this topic rather than an example a teacher might substitute for."),

 dict(q="EK 3.10.A.2 names the pro-life and pro-choice movements together in a single item. What does naming both most directly show about the framework's claim?",
   choices=[
     "That a constitutional provision can motivate movements that disagree with one another, so the claim is about mobilization rather than about which side the provision vindicates",
     "That the framework endorses the position of one of the two movements",
     "That the two movements make identical arguments",
     "That neither movement invokes any constitutional provision",
     "That the framework treats only movements that agree with each other"], ans=0,
   why="EK 3.10.A.2 offers its three items as evidence that the equal protection clause CAN SUPPORT AND MOTIVATE social movements, and listing opposed movements under one heading shows the framework is describing an effect on organizing rather than settling the underlying dispute."),

 dict(q="A movement organizes around the claim that a state law treats a group unequally, cites the Fourteenth Amendment in its literature, and files suit. Which part of LO 3.10.A does the literature illustrate, as distinct from the lawsuit?",
   choices=[
     "The way a provision motivates people to organize, which operates before and apart from any court's ruling",
     "The way a court applies a provision to a set of facts",
     "The way Congress drafts a statute",
     "The way a governor enforces a judgment",
     "The way a provision is ratified"], ans=0,
   why="LO 3.10.A pairs two verbs, SUPPORTED and MOTIVATED, and the second describes the clause's effect on people rather than on litigation. The literature is evidence of motivation; the suit is where support becomes a legal result."),

 dict(q="A student argues that a social movement is unnecessary wherever a constitutional provision already guarantees a right. Which observation drawn from this topic best answers the argument?",
   choices=[
     "The provisions EK 3.10.A.1 names were in force long before the movements EK 3.10.A.2 describes formed, so a guarantee on paper did not by itself produce the treatment it promised",
     "The provisions EK 3.10.A.1 names were adopted after the movements formed",
     "The framework says movements have never affected policy",
     "The framework says courts enforce provisions automatically",
     "The framework says civil rights rest on statutes rather than on the Constitution"], ans=0,
   why="EK 3.10.A.2 offers movements from the 1960s onward as evidence about a clause ratified in 1868, and the gap between the two dates is the point. A written guarantee and its realization are different things, which is what makes the clause a motivator rather than a substitute for organizing."),

 dict(q=_COMPLAINTS + " Which conclusion is best supported by the data?",
   table=_COMPLAINTS_TABLE,
   choices=[
     "Complaints alleging race and complaints alleging sex together account for more than three-quarters of all complaints filed",
     "Complaints alleging religion were the most numerous category",
     "Each of the four categories drew a similar number of complaints",
     "No complaint in any category was found to have merit",
     "Complaints alleging national origin outnumbered complaints alleging sex"], ans=0,
   why="Race at 1840 and sex at 1320 total 3160 of the 4065 complaints filed, which is above three-quarters. Religion is the smallest category at 295, and national origin at 610 is well below sex."),

 dict(q=_COMPLAINTS + " The characteristics listed in the first column correspond most closely to which statement in the course framework?",
   table=_COMPLAINTS_TABLE,
   choices=[
     "EK 3.10.A.1's list of characteristics such as race, national origin, religion, and sex",
     "EK 3.10.A.2's list of three social movements",
     "EK 3.9.A.1's account of unenumerated rights",
     "EK 3.8.A.4's statement of the exclusionary rule",
     "EK 3.12.A.1's account of restrictions on minority rights"], ans=0,
   why="The four row labels are exactly the four characteristics EK 3.10.A.1 names as bases of discrimination that civil rights protect against. The other statements concern movements, unwritten rights, evidence, and the balance between minority and majority rights."),

 dict(q=_COMPLAINTS + " A student concludes from the table that complaints alleging religion are the least likely of the four to be found to have merit. What is the most important correction?",
   table=_COMPLAINTS_TABLE,
   choices=[
     "Religion complaints were found to have merit in 71 of 295 cases, a higher share than race complaints at 412 of 1840",
     "The table does not report how many complaints were found to have merit",
     "Religion complaints were the most numerous category",
     "No category had any complaint found to have merit",
     "The table covers a single complaint, so no share can be computed"], ans=0,
   why="Comparing merit rates rather than raw counts, religion stands at about 24 percent against race at about 22 percent, so religion is not the lowest. Reading the smallest count as the weakest record is a base-rate error, and the four rates in this table sit within a few points of one another."),

 dict(q=_PETITIONS + " Which conclusion is best supported by the data?",
   table=_PETITIONS_TABLE,
   choices=[
     "The equal protection clause was invoked as the principal basis more than twice as often as the due process clause",
     "The First Amendment was the most frequently invoked basis",
     "The four bases were invoked about equally often",
     "No petition rested on an act of Congress",
     "The due process clause was invoked more often than the equal protection clause"], ans=0,
   why="The table reports 246 petitions principally invoking the equal protection clause against 88 invoking the due process clause, a ratio well above two. Twenty petitions rested on an act of Congress alone, so that category is not empty."),

 dict(q=_PETITIONS + " Which statement in the course framework does the largest row of this table most directly illustrate?",
   table=_PETITIONS_TABLE,
   choices=[
     "That the equal protection clause can support and motivate social movements",
     "That procedural due process requires non-arbitrary methods",
     "That the exclusionary rule bars illegally seized evidence",
     "That the Fifth Amendment's due process clause binds the national government",
     "That unenumerated rights include the right to privacy"], ans=0,
   why="EK 3.10.A.2 makes exactly this claim about the equal protection clause, and organizations choosing it as their principal basis nearly two-thirds of the time is the claim in observable form. The four alternatives are statements from topics 3.8 and 3.9."),

 dict(q=_PETITIONS + " A student concludes from the table that acts of Congress play no part in protecting civil rights. What is the most important correction?",
   table=_PETITIONS_TABLE,
   choices=[
     "EK 3.10.A.1 names acts of Congress as a source of civil rights alongside the two clauses, and 20 petitions here rested on a statute alone",
     "The table shows that no petition invoked a constitutional provision",
     "The table shows that acts of Congress were the most common basis",
     "EK 3.10.A.1 names acts of Congress as the only source of civil rights",
     "The table reports shares but not counts, so no comparison is possible"], ans=0,
   why="The framework's own sentence lists three sources and the third is legislation, and the table's smallest row is not an empty one. A category that is small is not a category that is absent, and the statute's reach over private conduct is what the constitutional clauses cannot supply."),
]
