# AP U.S. GOVERNMENT AND POLITICS 1.8 Constitutional Interpretations of Federalism -- 30 questions
# CED V.1 (c) 2026, Unit 1 Foundations of American Democracy.
# Learning objective 1.8.A: explain how the balance of power between national
# and state governments has changed over time based on interpretations of the
# Supreme Court of the United States.
# Suggested skill for this topic (CED p. 50): 2.A, describe the facts, issue,
# holding, reasoning, decision and majority opinion of REQUIRED cases. This
# module is weighted to SCOTUS items accordingly, and it uses only the fourteen
# required cases.
#
# Essential knowledge relied on. All four statements have the SAME shape, and
# that shape is the topic:
#   EK 1.8.A.1 -- the Due Process and Equal Protection Clauses of the Fourteenth
#     Amendment "give the national government the power to enforce protections
#     for any person against the states, BUT Supreme Court interpretations can
#     influence the extent of those protections."
#   EK 1.8.A.2 -- the Commerce Clause "gives the national government the power
#     to regulate interstate commerce, BUT Supreme Court interpretations can
#     influence the extent of this power."
#   EK 1.8.A.3 -- the Necessary and Proper Clause "gives Congress the power to
#     make laws related to carrying out its enumerated powers, BUT Supreme Court
#     interpretations can influence the extent of these powers."
#   EK 1.8.A.4 -- the Supremacy Clause "gives the national government and its
#     laws general precedence over states' laws, BUT Supreme Court
#     interpretations may affect when specific actions exceed this
#     constitutional power."
#
# The word doing the work in all four is the one the CED repeats: the clause
# grants a power, and the COURT'S READING sets how far the power reaches. So the
# examinable claim is never "the Commerce Clause allows X" but "the Court's
# interpretation of the Commerce Clause has allowed or refused X." Items in this
# module are written so that a student who has learned the clauses without the
# interpretive point cannot answer them, which is what LO 1.8.A asks for.
#
# THE TRAP THIS MODULE IS BUILT TO CATCH: McCulloch and Lopez are both Commerce
# and Necessary-and-Proper-adjacent federalism cases decided in OPPOSITE
# directions, 176 years apart, and a student who has memorised "the Court
# expands national power" gets Lopez wrong. Items 12 to 16 set them against each
# other on purpose.
#
# Required cases the CED attaches to 1.8.A (p. 31-32): McCulloch v. Maryland,
# Engel v. Vitale, Gideon v. Wainwright, Wisconsin v. Yoder,
# United States v. Lopez. (The CED's cross-reference table prints the Gideon
# entry as the typo "1..8.A"; see AP_US_GOV_CED.md note 9.)
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: constitutional text is quoted verbatim.
# No case is quoted; every holding is stated in the CED's own words, which
# AP_US_GOV_CED.md reproduces. The tables are labelled where hypothetical.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("1.8", "Constitutional Interpretations of Federalism", 1)

_CLAUSES = ("The table pairs five required Supreme Court cases with the constitutional "
            "provision each turned on and the direction of its result for national power.")
_CLAUSES_TABLE = dict(
    headers=["Case", "Provision at issue", "Effect on national power"],
    rows=[["McCulloch v. Maryland (1819)", "Necessary and Proper Clause and Supremacy Clause", "Expanded"],
          ["Engel v. Vitale (1962)", "First Amendment, applied to a state", "Expanded"],
          ["Gideon v. Wainwright (1963)", "Sixth Amendment, applied to a state", "Expanded"],
          ["Wisconsin v. Yoder (1972)", "First Amendment, applied to a state", "Expanded"],
          ["United States v. Lopez (1995)", "Commerce Clause", "Limited"]])

_SPEND = ("In a hypothetical federal system, the table reports the share of total government "
          "spending accounted for by each level of government in three periods.")
_SPEND_TABLE = dict(
    headers=["Level of government", "Period 1 (%)", "Period 2 (%)", "Period 3 (%)"],
    rows=[["National", "30", "52", "58"],
          ["State", "26", "24", "22"],
          ["Local", "44", "24", "20"]])

QUESTIONS = [
 dict(q="According to the course framework, the Due Process and Equal Protection Clauses of the Fourteenth Amendment give the national government the power to enforce protections for any person against the states, but",
   choices=[
     "Supreme Court interpretations can influence the extent of those protections",
     "the states may decline to be bound by them if they object",
     "Congress may not legislate to enforce them",
     "they apply only to citizens and not to other persons",
     "they were repealed by the Tenth Amendment"], ans=0,
   why="EK 1.8.A.1 states the grant and the qualification together, and the qualification is the point of the whole topic: the clause supplies the power and the Court's reading supplies its reach."),

 dict(q="Which statement best captures what LO 1.8.A asks a student to explain?",
   choices=[
     "How the balance of power between the national and state governments has changed over time as a result of Supreme Court interpretations",
     "How the framers allocated power between the levels in 1787 and why they chose that allocation",
     "How the states may amend the Constitution without the participation of Congress",
     "How Congress divides its own powers between the two chambers",
     "How political parties have changed their positions on federalism"], ans=0,
   why="The objective is about CHANGE OVER TIME driven by judicial interpretation, not about the original allocation. That distinction is why every item in this topic turns on a decision rather than on a clause alone."),

 dict(q="Read the following excerpt.\n\n“No State shall make or enforce any law which shall abridge the privileges or immunities of citizens of the United States; nor shall any State deprive any person of life, liberty, or property, without due process of law; nor deny to any person within its jurisdiction the equal protection of the laws.”\n—U.S. Constitution, Fourteenth Amendment, Section 1\n\nWhich feature of this text made it a turning point for the federal balance?",
   choices=[
     "It imposes obligations directly on the states and extends its protection to any person, not only to citizens",
     "It transfers all legislative power from the states to Congress",
     "It abolishes the reserved powers of the Tenth Amendment",
     "It applies only to the national government and not to the states",
     "It requires the states to obtain federal approval before enacting any law"], ans=0,
   why="The text names the states as the actors restrained and shifts from 'citizens' in the first clause to 'any person' in the due process and equal protection clauses. That is a national limit on state action, which is what EK 1.8.A.1 describes."),

 dict(q="In Gideon v. Wainwright (1963), the Supreme Court held that the Sixth Amendment's right to an attorney extends procedural due process protections to felony defendants in state courts. Which effect on the federal balance does the decision illustrate?",
   choices=[
     "A national constitutional guarantee was made binding on state criminal proceedings that the states had previously conducted on their own terms",
     "The states were given authority to define the rights of defendants in federal court",
     "Criminal law was transferred from the states to Congress",
     "The Sixth Amendment was held to apply only to federal prosecutions",
     "The Supreme Court declined to review the state court's decision"], ans=0,
   why="The CED states the holding as extending procedural due process protections to felony defendants in state courts, which is a national rule reaching a traditionally state function. The fourth option states the position the case rejected."),

 dict(q="In Engel v. Vitale (1962), the Supreme Court held that school sponsorship of religious activities violates the Establishment Clause of the First Amendment. What does the case demonstrate about the balance between national and state power?",
   choices=[
     "A First Amendment limit applies to a state institution, so state and local officials may not adopt a policy the national Constitution forbids",
     "The states may set their own rules about religion in public schools without national restriction",
     "Congress gained the power to write curricula for public schools",
     "The Establishment Clause restrains only Congress and not state governments",
     "Public education became an exclusive power of the national government"], ans=0,
   why="Public schools are a state and local institution, and the holding subjects one of their policies to a national constitutional limit. The fourth option describes the pre-incorporation reading, which is precisely what the decision does not follow."),

 dict(q="In Wisconsin v. Yoder (1972), the Supreme Court held that compelling Amish students to attend school past the eighth grade violates the Free Exercise Clause of the First Amendment. The decision limited which government's authority?",
   choices=[
     "The state's, since compulsory school attendance laws are state laws",
     "Congress's, since the compulsory attendance requirement was a federal statute",
     "The school district's alone, leaving the state law untouched",
     "The Supreme Court's own, by narrowing the cases it may hear",
     "The national government's authority over religious institutions"], ans=0,
   why="Compulsory attendance is a state requirement, and the holding is that applying it to these students violates a national guarantee. That is EK 1.8.A.1's pattern of national enforcement of protections against the states."),

 dict(q="Engel, Gideon and Yoder differ in subject matter but share a structural feature. What is it?",
   choices=[
     "In each, a provision of the Bill of Rights was enforced against a state or its instrumentalities",
     "In each, the Court upheld the state law under review",
     "In each, the Court expanded the powers of Congress under the Commerce Clause",
     "In each, the Court refused to decide the case on the merits",
     "In each, the Court struck down an act of Congress"], ans=0,
   why="All three apply a national guarantee -- the Establishment Clause, the right to counsel and the Free Exercise Clause -- to state action, which is the mechanism EK 1.8.A.1 describes. In all three the challenger prevailed against the state."),

 dict(q="Read the following excerpt.\n\n“The Congress shall have Power... To regulate Commerce with foreign Nations, and among the several States, and with the Indian Tribes.”\n—U.S. Constitution, Article I, Section 8\n\nAccording to the course framework, what determines how far this power actually reaches?",
   choices=[
     "Supreme Court interpretations, which can influence the extent of the power",
     "The text alone, which fixes the boundary without need for interpretation",
     "A vote of three-fourths of the state legislatures in each disputed case",
     "The president's judgment about what commerce requires",
     "The Tenth Amendment, which withdraws the power whenever a state objects"], ans=0,
   why="EK 1.8.A.2 says the clause grants the power BUT Supreme Court interpretations can influence its extent, which is why a case like Lopez is the answer to a question about how far it goes."),

 dict(q="In United States v. Lopez (1995), the Supreme Court held that Congress exceeded its power under the Commerce Clause when it made possession of a gun in a school zone a federal crime. Which conclusion about the federal balance does the case support?",
   choices=[
     "The Commerce Clause has a judicially enforced outer limit, so the Court's interpretations can contract national power as well as expand it",
     "The Commerce Clause gives Congress no authority to regulate any activity",
     "The states lost the power to regulate firearms near schools",
     "The Court held that Congress may regulate any subject with any connection to a school",
     "The Court declined to decide whether the statute was constitutional"], ans=0,
   why="A holding that Congress exceeded a power establishes that the power has a boundary a court will enforce. That is the direction of change EK 1.8.A.2 contemplates, and it runs opposite to the usual assumption that judicial interpretation only expands."),

 dict(q="A student writes that Supreme Court interpretation has moved steadily and only in the direction of greater national power. Which required case is the strongest counterexample?",
   choices=[
     "United States v. Lopez (1995), in which the Court held that Congress exceeded its Commerce Clause power",
     "McCulloch v. Maryland (1819), in which the Court upheld an implied power of Congress",
     "Gideon v. Wainwright (1963), in which the Court applied the right to counsel to state courts",
     "Engel v. Vitale (1962), in which the Court applied the Establishment Clause to public schools",
     "Wisconsin v. Yoder (1972), in which the Court applied the Free Exercise Clause to a state law"], ans=0,
   why="Lopez is the only one of the five in which the Court limited rather than extended national authority; the other four each enforce a national rule against a state or uphold a national power."),

 dict(q="Read the following excerpt.\n\n“This Constitution, and the Laws of the United States which shall be made in Pursuance thereof... shall be the supreme Law of the Land; and the Judges in every State shall be bound thereby, any Thing in the Constitution or Laws of any State to the Contrary notwithstanding.”\n—U.S. Constitution, Article VI\n\nAccording to the course framework, what qualification applies to this clause?",
   choices=[
     "Supreme Court interpretations may affect when specific actions exceed this constitutional power",
     "The clause applies only when a state has consented to be bound",
     "The clause applies only to treaties and not to statutes",
     "The clause gives state judges authority to disregard federal law they consider unwise",
     "The clause was superseded by the Fourteenth Amendment"], ans=0,
   why="EK 1.8.A.4 states the grant of general precedence and then this qualification, and the words 'in Pursuance thereof' are why the qualification matters: a federal action outside the Constitution is not supreme."),

 dict(q="McCulloch v. Maryland (1819) and United States v. Lopez (1995) are both federalism cases in which the Court read a source of congressional power. What is the most accurate comparison?",
   choices=[
     "McCulloch read national power broadly and upheld it; Lopez found a limit and struck the statute down",
     "Both read national power broadly and upheld the statute at issue",
     "Both found limits on national power and struck the statutes down",
     "McCulloch found a limit on national power; Lopez read it broadly",
     "Neither case concerned the allocation of power between the levels"], ans=0,
   why="The CED states McCulloch as establishing supremacy of federal law over state law after upholding an implied power, and Lopez as Congress exceeding its Commerce Clause power. The two run in opposite directions, which is the comparison the topic is built on."),

 dict(q="A non-required case: Congress enacts a statute regulating an activity that occurs entirely within one state and has no demonstrated connection to any commercial transaction. Which required case would a court most likely rely on in evaluating the statute, and what would it look for?",
   choices=[
     "United States v. Lopez (1995), asking whether the regulated activity substantially affects interstate commerce",
     "McCulloch v. Maryland (1819), asking whether a state has attempted to tax a federal institution",
     "Engel v. Vitale (1962), asking whether a public school sponsored a religious activity",
     "Gideon v. Wainwright (1963), asking whether a felony defendant was denied counsel",
     "Wisconsin v. Yoder (1972), asking whether a religious practice was burdened by a state law"], ans=0,
   why="The stem's facts are a Commerce Clause question about a wholly intrastate, noncommercial activity, which is the Lopez inquiry. Each other option names a case whose facts are absent from the stem."),

 dict(q="A non-required case: a state enacts a law that conflicts directly with a valid federal statute regulating the same subject, and a state court holds that the state law controls within the state. On appeal, which required case most directly resolves the conflict?",
   choices=[
     "McCulloch v. Maryland (1819), which established the supremacy of the U.S. Constitution and federal laws over state laws",
     "United States v. Lopez (1995), which held that Congress exceeded its Commerce Clause power",
     "Wisconsin v. Yoder (1972), which held that compelling Amish students to attend school past the eighth grade violates the Free Exercise Clause",
     "Engel v. Vitale (1962), which held that school sponsorship of religious activities violates the Establishment Clause",
     "Gideon v. Wainwright (1963), which extended the right to an attorney to felony defendants in state courts"], ans=0,
   why="A direct conflict between a valid federal statute and a state law is the Supremacy Clause question McCulloch settled, and the CED states that holding in those terms. Lopez asks whether the federal statute was valid in the first place, which the stem stipulates."),

 dict(q="Which pairing of a required case with the essential-knowledge statement it best illustrates is correct?",
   choices=[
     "United States v. Lopez with the Commerce Clause statement, since the Court set a limit on that power",
     "Gideon v. Wainwright with the Commerce Clause statement, since counsel is an economic service",
     "McCulloch v. Maryland with the Equal Protection statement, since Maryland treated the bank differently",
     "Engel v. Vitale with the Necessary and Proper statement, since Congress passed no statute",
     "Wisconsin v. Yoder with the Supremacy Clause statement, since no federal law was involved"], ans=0,
   why="Lopez is a Commerce Clause holding, which is EK 1.8.A.2. Each of the other four pairings attaches a case to a clause its holding did not turn on, and the last two say so in their own reasons."),

 dict(q="According to the course framework, the Necessary and Proper Clause gives Congress the power to make laws related to carrying out its enumerated powers. Which required case is the classic illustration of that reading?",
   choices=[
     "McCulloch v. Maryland (1819), in which the Court upheld a national bank that no clause enumerates",
     "United States v. Lopez (1995), in which the Court struck down a federal criminal statute",
     "Gideon v. Wainwright (1963), in which the Court applied the Sixth Amendment to state courts",
     "Engel v. Vitale (1962), in which the Court applied the Establishment Clause to public schools",
     "Wisconsin v. Yoder (1972), in which the Court applied the Free Exercise Clause to a state law"], ans=0,
   why="No clause enumerates a power to charter a bank, so upholding it rests on the Necessary and Proper Clause, which is EK 1.8.A.3. The other four cases turn on individual rights or on the Commerce Clause."),

 dict(q="Which of the following would be the strongest evidence that the balance of power described in EK 1.8.A has shifted toward the states in a given period?",
   choices=[
     "Courts in that period invalidated several federal statutes as exceeding Congress's enumerated powers",
     "Congress enacted more statutes in that period than in the preceding one",
     "The national government's budget grew faster than state budgets",
     "More cases were filed in federal court than in state courts",
     "The Supreme Court heard fewer cases than in the preceding period"], ans=0,
   why="EK 1.8.A ties the balance to judicial interpretation, so the evidence has to be decisions setting limits on national authority. Budget totals and case volumes measure activity rather than the allocation of constitutional power."),

 dict(q="A commentator argues that the Fourteenth Amendment did more to change the federal balance than any other provision. Which reasoning best supports the argument?",
   choices=[
     "It made the national government the enforcer of individual protections against state action, which the original Constitution largely did not",
     "It transferred the states' reserved powers to Congress in a single sentence",
     "It gave the states a veto over federal legislation affecting them",
     "It required that all state constitutions be approved by Congress",
     "It abolished the distinction between enumerated and implied powers"], ans=0,
   why="Before the amendment the Bill of Rights was read as restraining the national government, and after it the national government could enforce protections against the states, which is EK 1.8.A.1. The other options describe changes the amendment did not make."),

 dict(q="A state argues that a federal regulation is invalid because the subject is one the Tenth Amendment reserves to the states. Which question must a court answer first?",
   choices=[
     "Whether the regulation falls within one of the powers the Constitution grants the national government",
     "Whether a majority of states object to the regulation",
     "Whether the state adopted its own regulation on the subject first",
     "Whether Congress consulted the states before enacting the statute",
     "Whether the regulation is a wise policy"], ans=0,
   why="The Tenth Amendment reserves powers NOT delegated, so the reserved-powers question cannot be answered until the delegated-powers question is. That sequence is why Lopez turns on the scope of the Commerce Clause rather than on the Tenth Amendment directly."),

 dict(q="Which statement best explains why the same constitutional text can produce different allocations of power in different periods?",
   choices=[
     "The clauses grant powers in general terms, and the Court's interpretation of those terms determines how far each reaches at a given time",
     "The text of the Constitution is amended whenever the balance of power changes",
     "Congress may rewrite the meaning of a clause by statute",
     "Each state adopts its own interpretation of the federal Constitution",
     "The Supreme Court is required to follow the interpretation given by the previous Court in every case"], ans=0,
   why="All four essential-knowledge statements in EK 1.8.A have the same form: the clause grants a power, and interpretation sets its extent. If interpretation could not change, the topic's learning objective about change over time would have nothing to explain."),

 dict(q=_CLAUSES + " Which conclusion is best supported by the table?",
   table=_CLAUSES_TABLE,
   choices=[
     "Four of the five cases expanded national power and one limited it",
     "Every case in the table expanded national power",
     "Every case in the table turned on the Commerce Clause",
     "The only case that limited national power is the oldest one in the table",
     "No case in the table involved a provision of the Bill of Rights"], ans=0,
   why="The effect column reads Expanded four times and Limited once, and the one limiting case, Lopez in 1995, is the most recent rather than the oldest. Three rows name First or Sixth Amendment provisions."),

 dict(q=_CLAUSES + " Which case in the table is the best evidence that judicial interpretation can move the balance toward the states?",
   table=_CLAUSES_TABLE,
   choices=[
     "United States v. Lopez, the only case listed whose effect on national power was to limit it",
     "McCulloch v. Maryland, because it is the oldest case listed",
     "Engel v. Vitale, because it concerned a policy adopted by a local school board",
     "Gideon v. Wainwright, because it concerned proceedings in a state court",
     "Wisconsin v. Yoder, because it involved a state compulsory attendance law"], ans=0,
   why="Three of the distractors are true statements about state involvement, but in each of those cases the national rule prevailed over the state, which moves the balance the other way. Only the Lopez row is marked Limited."),

 dict(q=_CLAUSES + " A student concludes from the table that the Supreme Court expands national power about eighty percent of the time. Which limitation of the data most undercuts that conclusion?",
   table=_CLAUSES_TABLE,
   choices=[
     "Five required cases selected for a course are not a sample of the Court's decisions, so no rate can be estimated from them",
     "The table omits the effect of each case on national power",
     "The table covers only cases decided in the twentieth century",
     "The table reports the votes of individual justices rather than holdings",
     "The table does not identify the constitutional provision at issue in any case"], ans=0,
   why="A curated list chosen to illustrate a course objective carries no information about base rates, which is the limitation CED skill 3.E asks students to recognize. The table plainly contains provision and effect columns and spans from 1819 to 1995."),

 dict(q=_SPEND + " Which conclusion is best supported by the data?",
   table=_SPEND_TABLE,
   choices=[
     "The national share nearly doubled across the three periods while both other levels declined",
     "All three levels increased their share across the three periods",
     "Local government accounted for the largest share in every period",
     "The state share fell more sharply than the local share",
     "The national share exceeded half of all spending in every period"], ans=0,
   why="The national row runs 30, 52, 58 while the state row falls 26 to 22 and the local row falls 44 to 20. Local led only in Period 1, the local share fell by 24 points against the state's 4, and the national share was below half in Period 1."),

 dict(q=_SPEND + " A student argues that these data show a change in the federal balance of the kind EK 1.8.A describes. What is the most important limitation of that argument?",
   table=_SPEND_TABLE,
   choices=[
     "Spending shares measure fiscal activity, not constitutional authority, and the topic concerns how courts have read the allocation of power",
     "The table omits the national government, so no comparison is possible",
     "The table covers only one period, so no change can be observed",
     "The table reports dollar amounts that cannot be compared across periods",
     "The table shows no change in any row"], ans=0,
   why="A government may spend more without gaining any new constitutional power, and EK 1.8.A locates the change in Supreme Court interpretation rather than in budgets. The table plainly has three periods, a national row and shares rather than dollars."),

 dict(q=_SPEND + " Which additional piece of evidence would most strengthen an argument that the shift in these data reflects a genuine change in the federal balance?",
   table=_SPEND_TABLE,
   choices=[
     "Evidence that during the same periods courts upheld national statutes regulating subjects previously left to the states",
     "Evidence that the national population grew during the same periods",
     "Evidence that state governments employed more people at the end than at the beginning",
     "Evidence that local governments continued to operate schools throughout",
     "Evidence that total government spending rose in every period"], ans=0,
   why="The argument needs to connect the fiscal pattern to constitutional authority, and judicial approval of national regulation in previously state fields is exactly that link. Population, employment and total spending are all consistent with no change in the allocation of power."),

 dict(q="Which of the following best describes the relationship between the Necessary and Proper Clause and the Supremacy Clause as the course framework presents them?",
   choices=[
     "The first is a source of national power and the second settles what happens when a valid national law conflicts with a state law",
     "Both are sources of national power, and neither concerns conflicts with state law",
     "Both concern conflicts with state law, and neither is a source of national power",
     "The first settles conflicts with state law and the second is a source of national power",
     "Neither clause has any bearing on the balance between the national and state governments"], ans=0,
   why="EK 1.8.A.3 casts the Necessary and Proper Clause as a grant of power to carry out enumerated powers, and EK 1.8.A.4 casts the Supremacy Clause as giving national law general precedence. McCulloch applies both, in that order."),

 dict(q="A federal statute is challenged on the ground that Congress had no power to enact it. A state law covering the same subject is also challenged, on the ground that it conflicts with the federal statute. Which order of analysis follows from the course framework?",
   choices=[
     "First decide whether the federal statute is within a granted power; only if it is does the Supremacy Clause resolve the conflict",
     "First apply the Supremacy Clause, since federal law always prevails regardless of its source",
     "Decide the two questions independently, since they have no bearing on each other",
     "First decide whether the state law is wise policy, then consider the federal statute",
     "Refer both questions to Congress, which determines the scope of its own powers"], ans=0,
   why="Article VI makes supreme only those federal laws 'made in Pursuance' of the Constitution, so a statute outside Congress's powers has no precedence to assert. That is the qualification EK 1.8.A.4 describes."),

 dict(q="Which question would best guide research into how Supreme Court interpretation has changed the federal balance over a given century?",
   choices=[
     "In cases raising the scope of national power, how often and in which direction did the Court's holdings move the boundary?",
     "How many opinions did the Court issue in total during the century?",
     "How many justices served on the Court during the century?",
     "In how many cases did the Court reach a unanimous decision?",
     "How many cases originated in state rather than federal courts?"], ans=0,
   why="LO 1.8.A is about the direction and extent of change produced by holdings, so the research question has to sort cases by outcome and direction. Counts of opinions, justices and unanimity measure the institution rather than the boundary."),

 dict(q="A student claims that because the Constitution's text has not changed, the balance between national and state power cannot have changed either. Which response is best supported by the course framework?",
   choices=[
     "All four of this topic's essential-knowledge statements say that Supreme Court interpretations influence how far a granted power extends, so the same text can support different boundaries at different times",
     "The Constitution's text has in fact been rewritten several times since 1789",
     "The states have formally surrendered their reserved powers by treaty",
     "Congress has amended the Commerce Clause by statute",
     "The balance is fixed by the Tenth Amendment and has never been in dispute"], ans=0,
   why="EK 1.8.A.1 through EK 1.8.A.4 all contain the same qualification about the extent of a power turning on interpretation, which is a direct answer to the claim. The remaining options assert changes to the text that have not occurred."),
]
