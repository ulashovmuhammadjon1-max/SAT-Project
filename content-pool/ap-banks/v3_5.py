# AP U.S. GOVERNMENT AND POLITICS 3.5 Second Amendment: Right to Bear Arms -- 30 questions
# CED V.1 (c) 2026, Unit 3 Civil Liberties and Civil Rights.
# Learning objective 3.5.A: explain THE EXTENT TO WHICH the Supreme Court's
# interpretation of the Second Amendment reflects a commitment to individual
# liberty.
# Suggested skill for this topic (CED p. 86): 4.A, describe the argument,
# perspective, evidence and reasoning presented in the source.
#
# Essential knowledge relied on. This is the THINNEST statement in the course --
# a single sentence that names no doctrine, no test and no outcome:
#   EK 3.5.A.1 -- "The Supreme Court's decisions on the Second Amendment rest
#     upon its CONSTITUTIONAL INTERPRETATION of the right to bear arms."
#
# HOW A THIN STATEMENT CONSTRAINS RATHER THAN LIBERATES. A sentence that says
# only "the decisions rest on interpretation" is an invitation to fill thirty
# questions with contemporary firearms policy, and that would be off-syllabus
# and undateable at once. What the framework actually supplies for this topic is
# three things, and this module uses only those three:
#   1. THE TEXT of the Second Amendment, which is a required document (the
#      Constitution) and which is the object of the interpretation EK 3.5.A.1
#      names. Its two clauses are the reason interpretation is required at all.
#   2. McDONALD v. CHICAGO, a required case, whose holding the CED states as:
#      "The Second Amendment right to keep and bear arms for self-defense is
#      applicable to the states."
#   3. UNITED STATES v. LOPEZ, also attached to 3.5.A -- and this is the trap
#      the module is built around. Lopez is a case ABOUT A GUN LAW that holds
#      NOTHING about the right to bear arms: the CED's own statement of it is
#      that Congress exceeded its power under the Commerce Clause. A student who
#      files it as a Second Amendment case has learned a false holding, and it
#      is exactly the kind of error that survives into an FRQ. Items 15 to 20
#      exist for it.
#
# WHAT THIS MODULE DOES NOT DO, and the reason is SOCIAL_BRIEF.md's rule that an
# uncertain key is cut rather than guessed: it states no test for evaluating a
# firearms regulation, names no case outside the CED's required list, and takes
# no position on any policy question. The framework supplies a holding about
# APPLICABILITY TO THE STATES and nothing about what regulations survive, so
# neither does this bank.
#
# Required cases the CED attaches to 3.5.A (p. 32-33): McDonald v. Chicago,
# United States v. Lopez.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the Second and Fourteenth Amendments
# are quoted verbatim. Non-required cases are described and never named. Both
# tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("3.5", "Second Amendment: Right to Bear Arms", 3)

_CLAUSES = ("The table sets out the two clauses of the Second Amendment and what a reader "
            "emphasizing each would take the Amendment to protect.")
_CLAUSES_TABLE = dict(
    headers=["Clause", "What a reader emphasizing it takes the Amendment to protect", "Is the clause in the text?"],
    rows=[["A well regulated Militia, being necessary to the security of a free State", "A right connected to service in an organized militia", "Yes"],
          ["the right of the people to keep and bear Arms, shall not be infringed", "A right held by individuals", "Yes"],
          ["A right to any particular weapon", "Nothing; the phrase does not appear", "No"],
          ["A prohibition on all firearms regulation", "Nothing; the phrase does not appear", "No"]])

_REACH = ("In a hypothetical study, the table reports which level of government a set of "
          "constitutional guarantees restrained before and after a series of decisions "
          "applying them to the states.")
_REACH_TABLE = dict(
    headers=["Guarantee", "Restrained the national government", "Restrained the states before the decision", "Restrains the states after the decision"],
    rows=[["Freedom of speech", "Yes", "No", "Yes"],
          ["Right to counsel in felony cases", "Yes", "No", "Yes"],
          ["Right to keep and bear arms for self-defense", "Yes", "No", "Yes"],
          ["Requirement of a grand jury indictment", "Yes", "No", "No"]])

QUESTIONS = [
 dict(q="According to the course framework, what do the Supreme Court's decisions on the Second Amendment rest upon?",
   choices=[
     "The Court's constitutional interpretation of the right to bear arms",
     "A statute Congress passed defining the right",
     "The policy preferences of the states",
     "An international agreement on firearms",
     "The Court's assessment of crime statistics"], ans=0,
   why="EK 3.5.A.1 states this in exactly these words. The framework locates the source of the decisions in constitutional interpretation rather than in legislation or in empirical judgment."),

 dict(q="Read the following excerpt.\n\n“A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed.”\n—U.S. Constitution, Second Amendment\n\nWhy does this text require interpretation before it can be applied?",
   choices=[
     "It opens with a clause about a militia and then states a right of the people, and the relationship between the two is not spelled out",
     "It contains no statement of any right",
     "It expressly lists the weapons it protects",
     "It expressly states which level of government it restrains",
     "It was written in a language other than English"], ans=0,
   why="The Amendment's structure -- a prefatory clause about a militia followed by an operative clause about the right of the people -- is what makes EK 3.5.A.1's constitutional interpretation necessary rather than optional."),

 dict(q="Which phrase does NOT appear in the text of the Second Amendment?",
   choices=[
     "Self-defense",
     "A well regulated Militia",
     "The security of a free State",
     "The right of the people",
     "Shall not be infringed"], ans=0,
   why="The other four are the Amendment's own words. Self-defense appears in the CED's statement of the McDonald holding, not in the constitutional text, which is precisely why interpretation was required to get there."),

 dict(q="A reader who emphasizes the Amendment's opening clause would most likely conclude that the right is",
   choices=[
     "connected to service in an organized militia",
     "held by individuals regardless of any militia connection",
     "limited to members of Congress",
     "a power of the state governments rather than a right of persons",
     "unenforceable in any court"], ans=0,
   why="The prefatory clause names a well regulated militia as the reason given, so a reading that gives it controlling weight ties the right to that purpose. The operative clause supports the second option, which is the competing reading."),

 dict(q="A reader who emphasizes the Amendment's second clause would most likely conclude that the right is",
   choices=[
     "held by individuals, since the text says the right of the people",
     "held only by those enrolled in a militia",
     "held by the states rather than by persons",
     "held only during a declared war",
     "held only by those who own property"], ans=0,
   why="The operative clause speaks of 'the right of the people,' the same phrase the First and Fourth Amendments use for individual rights. Which clause controls is the interpretive question EK 3.5.A.1 points at."),

 dict(q="Why does the framework describe the Court's Second Amendment decisions as resting on INTERPRETATION rather than on the text alone?",
   choices=[
     "The text does not resolve the relationship between its two clauses, so a court must decide what that relationship is before applying it",
     "The text has been amended several times",
     "The text is written in terms that no court has ever examined",
     "The text expressly delegates the question to Congress",
     "The text applies only to the federal government by its own terms"], ans=0,
   why="EK 3.5.A.1's word is interpretation, and what makes interpretation necessary is a text whose two clauses can each be read as controlling. Nothing in the Amendment assigns the question elsewhere."),

 dict(q="In McDonald v. Chicago (2010), the Supreme Court held that the Second Amendment right to keep and bear arms for self-defense is applicable to the states. What did the decision change?",
   choices=[
     "A guarantee that had restrained the national government was made enforceable against state and local governments as well",
     "It created the right to keep and bear arms, which had not existed before",
     "It held that states may regulate firearms without limit",
     "It transferred firearms regulation to Congress",
     "It repealed the Second Amendment"], ans=0,
   why="The CED states the holding as the right being APPLICABLE TO THE STATES, which is a question about which governments the guarantee restrains rather than about whether the right exists."),

 dict(q="Which phrase in the CED's statement of the McDonald holding identifies the PURPOSE the Court attached to the right?",
   choices=[
     "For self-defense",
     "Applicable to the states",
     "The Second Amendment",
     "To keep and bear arms",
     "The Supreme Court held"], ans=0,
   why="The CED's wording is 'the right to keep and bear arms FOR SELF-DEFENSE is applicable to the states,' and that phrase is the interpretive content EK 3.5.A.1 refers to, since the text itself does not name self-defense."),

 dict(q="Read the following excerpt.\n\n“No State shall... deprive any person of life, liberty, or property, without due process of law.”\n—U.S. Constitution, Fourteenth Amendment, Section 1\n\nWhy is this provision relevant to McDonald v. Chicago?",
   choices=[
     "It is the textual route by which a guarantee originally aimed at the national government is applied against the states",
     "It gives states the power to regulate firearms",
     "It repeals the Second Amendment as to the states",
     "It requires states to arm their residents",
     "It applies only to criminal procedure"], ans=0,
   why="The clause restrains STATES and protects liberty, which is what makes it the vehicle for applying a Bill of Rights guarantee against them. Topic 3.7's selective incorporation is the general form of this move."),

 dict(q="Which best describes the relationship between the McDonald holding and the topic of selective incorporation?",
   choices=[
     "McDonald is one instance of the general process by which Bill of Rights guarantees are applied to the states",
     "McDonald is unrelated to incorporation, since it concerns firearms",
     "McDonald incorporated the entire Bill of Rights at once",
     "McDonald reversed the incorporation of other guarantees",
     "Incorporation applies only to the First Amendment"], ans=0,
   why="The CED's statement of the holding -- applicable to the states -- is what incorporation means, so McDonald is an instance rather than an exception. Topic 3.7 covers the process itself."),

 dict(q="A state law is challenged on the ground that it violates the Second Amendment. Before McDonald, what would the state's strongest structural response have been?",
   choices=[
     "That the Second Amendment restrained the national government and not the states",
     "That the Second Amendment had been repealed",
     "That the Second Amendment protects only the federal militia",
     "That the state had not signed the Constitution",
     "That the Second Amendment applies only during wartime"], ans=0,
   why="The CED states McDonald's holding as making the right applicable to the states, which means the question was open before it. That structural defence is what the decision removed."),

 dict(q="What does McDonald v. Chicago show about EK 3.5.A.1's claim that the decisions rest on constitutional interpretation?",
   choices=[
     "Neither the phrase self-defense nor the words applicable to the states appears in the Second Amendment, so both came from interpretation",
     "The holding is quoted directly from the Second Amendment's text",
     "The holding was added to the Constitution by amendment",
     "The holding rests on a statute rather than on the Constitution",
     "The holding rests on the Court's reading of crime statistics"], ans=0,
   why="EK 3.5.A.1's point is exactly this: the operative content of the decision -- purpose and reach -- is interpretive, because the constitutional text supplies neither."),

 dict(q="Which question would a court applying EK 3.5.A.1's interpretive approach have to answer FIRST?",
   choices=[
     "What the Second Amendment's two clauses mean when read together",
     "Whether the challenged regulation is good policy",
     "How many firearms are owned in the jurisdiction",
     "Whether a majority of residents support the regulation",
     "Which political party enacted the regulation"], ans=0,
   why="EK 3.5.A.1 makes constitutional interpretation the foundation of the decisions, and the interpretive question is prior to any application. The other four are policy or political questions rather than legal ones."),

 dict(q="Why does the framework's phrasing -- decisions RESTING UPON interpretation -- matter for how a student should discuss this topic?",
   choices=[
     "It directs attention to the reasoning behind a holding rather than to whether the outcome is desirable",
     "It means the Court's decisions have no legal effect",
     "It means any interpretation is as good as any other",
     "It means the Second Amendment may be ignored",
     "It means the Court must follow public opinion"], ans=0,
   why="LO 3.5.A asks about the EXTENT to which the interpretation reflects a commitment to individual liberty, which is a question about reasoning. Whether a policy is wise is a different question the framework does not pose."),

 dict(q="In United States v. Lopez (1995), the Supreme Court held that Congress exceeded its power under the Commerce Clause when it made possession of a gun in a school zone a federal crime. What did the Court hold about the Second Amendment in that case?",
   choices=[
     "Nothing; the holding rests on the limits of the Commerce Clause, not on the right to bear arms",
     "That the statute violated the right to keep and bear arms",
     "That the Second Amendment applies to the states",
     "That the Second Amendment protects possession near schools",
     "That the Second Amendment protects only militia service"], ans=0,
   why="The CED's statement of the Lopez holding names the Commerce Clause and nothing else. It is a case about a gun law that decides a question of congressional power, and filing it as a Second Amendment holding is a false statement a student may repeat in an essay."),

 dict(q="Why does a case about a firearms statute end up being decided on the Commerce Clause rather than on the Second Amendment?",
   choices=[
     "The question in the case was whether Congress had power to enact the statute at all, which is answered before any question about individual rights",
     "The Second Amendment does not apply to statutes",
     "The Commerce Clause replaced the Second Amendment",
     "The Court may choose which amendment to apply at random",
     "Congress had not yet ratified the Second Amendment"], ans=0,
   why="A statute outside Congress's enumerated powers fails whatever rights it does or does not burden, so the power question comes first. That ordering is EK 1.8.A's subject and is why Lopez has a Commerce Clause holding."),

 dict(q="A student writes that United States v. Lopez established a Second Amendment right to possess firearms near schools. What is the correction?",
   choices=[
     "The case held only that Congress exceeded its Commerce Clause power, which leaves states free to regulate the same conduct",
     "The case held that the Second Amendment does not apply to schools",
     "The case held that the Second Amendment applies to the states",
     "The student is right, and the case is a Second Amendment holding",
     "The case was decided under the Fourteenth Amendment"], ans=0,
   why="The CED states the Lopez holding as a limit on federal power, and a limit on CONGRESS says nothing about what a state may do. Both halves of the correction matter, and the second is the one students miss."),

 dict(q="Which comparison between McDonald v. Chicago and United States v. Lopez is accurate?",
   choices=[
     "McDonald decides a question about individual rights and which governments they bind; Lopez decides a question about the scope of congressional power",
     "Both decide questions about the scope of the Second Amendment",
     "Both decide questions about the scope of the Commerce Clause",
     "McDonald decides a Commerce Clause question and Lopez a Second Amendment question",
     "Neither case concerns firearms in any way"], ans=0,
   why="The two required cases the CED attaches to this topic answer different constitutional questions and happen to share a subject matter. Confusing them is the error item 15 is built to catch."),

 dict(q="Why does the CED attach a Commerce Clause case to a Second Amendment topic at all?",
   choices=[
     "Because the two cases together show that a firearms regulation raises questions of both governmental power and individual rights",
     "Because the Court made an error in deciding Lopez",
     "Because Lopez was later reinterpreted as a Second Amendment case",
     "Because the Commerce Clause is part of the Second Amendment",
     "Because every case involving a firearm is a Second Amendment case"], ans=0,
   why="A regulation must be within some government's power AND consistent with individual rights, and the two cases illustrate the two inquiries. The last option states the error the pairing is meant to prevent."),

 dict(q="A state enacts a firearms regulation. Which of the two required cases attached to this topic bears on whether the regulation is constitutional?",
   choices=[
     "McDonald, since it makes the Second Amendment right applicable to the states",
     "Lopez, since it concerns a firearms statute",
     "Both equally, since both concern firearms",
     "Neither, since both concern federal law",
     "Lopez, since it limits state power"], ans=0,
   why="Lopez limits CONGRESS's Commerce Clause power and says nothing about state authority, while McDonald's holding is precisely that the right applies to the states. Subject matter is not the same as legal question."),

 dict(q=_CLAUSES + " Which conclusion is best supported by the table?",
   table=_CLAUSES_TABLE,
   choices=[
     "Two of the four rows quote language actually in the Amendment, and the other two describe readings the text does not state",
     "All four rows quote language in the Amendment",
     "None of the rows quotes language in the Amendment",
     "The Amendment expressly prohibits all firearms regulation",
     "The Amendment expressly protects a right to any particular weapon"], ans=0,
   why="The last column reads Yes twice and No twice. The two No rows are propositions the text does not contain, which is why the fourth and fifth options misdescribe the Amendment."),

 dict(q=_CLAUSES + " What does the arrangement of this table show about why interpretation is necessary?",
   table=_CLAUSES_TABLE,
   choices=[
     "The two clauses that ARE in the text support different readings of the same sentence, so the text alone does not settle the question",
     "The two clauses in the text say the same thing in different words",
     "The table shows that the Amendment has only one clause",
     "The table shows that the Amendment settles the question expressly",
     "The table shows that the Amendment has been amended"], ans=0,
   why="EK 3.5.A.1 makes interpretation the basis of the decisions, and the first two rows are why: one sentence, two clauses, two defensible emphases. The last two rows are there to show what the text does NOT say."),

 dict(q=_CLAUSES + " Why do the third and fourth rows of the table have 'No' in the last column?",
   table=_CLAUSES_TABLE,
   choices=[
     "Neither a right to a particular weapon nor a ban on all regulation appears in the Amendment's text, so neither can be read directly out of it",
     "Both appear in the text but were later removed",
     "Both appear in the Fourteenth Amendment instead",
     "Both were added by the Supreme Court in McDonald",
     "The table is in error, since both appear in the text"], ans=0,
   why="The Amendment's words are quoted in the first two rows and contain neither proposition. Including the two absent readings is what lets the table distinguish what the text says from what people claim it says."),

 dict(q=_REACH + " Which conclusion is best supported by the table?",
   table=_REACH_TABLE,
   choices=[
     "Three of the four guarantees came to restrain the states after a decision, and one did not",
     "All four guarantees came to restrain the states",
     "None of the guarantees restrained the national government",
     "All four guarantees restrained the states from the beginning",
     "The right to keep and bear arms is the only guarantee that restrains the states"], ans=0,
   why="The last column reads Yes three times and No once, the third column reads No four times, and the second reads Yes four times. The grand jury row is the one that did not change."),

 dict(q=_REACH + " Which row corresponds to the holding in McDonald v. Chicago?",
   table=_REACH_TABLE,
   choices=[
     "The right to keep and bear arms for self-defense, which restrained the national government and came to restrain the states",
     "Freedom of speech, which restrained the national government first",
     "The right to counsel in felony cases, which concerns criminal procedure",
     "The requirement of a grand jury indictment, which did not change",
     "None of the rows, since McDonald concerned the Commerce Clause"], ans=0,
   why="The CED's statement of the McDonald holding is that the right to keep and bear arms FOR SELF-DEFENSE is applicable to the states, which is exactly the third row's pattern. The fifth option confuses McDonald with Lopez."),

 dict(q=_REACH + " What does the grand jury row imply about the process the other three rows illustrate?",
   table=_REACH_TABLE,
   choices=[
     "Guarantees have been applied to the states one at a time rather than all together, so some have not been applied at all",
     "Every guarantee in the Bill of Rights has been applied to the states",
     "No guarantee has been applied to the states",
     "The states apply guarantees to the national government",
     "Guarantees apply to the states only when Congress says so"], ans=0,
   why="A table in which three rows changed and one did not is the definition of a SELECTIVE process, which is topic 3.7's subject and the reason McDonald had to be decided at all."),

 dict(q="LO 3.5.A asks about the extent to which the Court's Second Amendment interpretation reflects a commitment to individual liberty. Which answer is best supported by the framework?",
   choices=[
     "The framework records that the right was held applicable to the states for self-defense, and says nothing about which regulations survive, so the extent is established on reach and open on limits",
     "The framework establishes that no firearms regulation is permissible",
     "The framework establishes that all firearms regulation is permissible",
     "The framework takes no position on whether the right binds the states",
     "The framework says the Second Amendment protects only militia service"], ans=0,
   why="EK 3.5.A.1 and the CED's statement of McDonald together settle applicability and purpose and settle nothing about permissible regulation. Answering beyond what the framework states would be guessing, which SOCIAL_BRIEF.md forbids."),

 dict(q="Which piece of evidence would a student need in order to argue that a particular firearms regulation is unconstitutional?",
   choices=[
     "A standard for evaluating such regulations, which the course framework does not supply",
     "Nothing further, since McDonald settled the question for all regulations",
     "Evidence that the regulation is unpopular",
     "Evidence that another state has no such regulation",
     "Evidence that the regulation was enacted recently"], ans=0,
   why="The framework's content for this topic is a holding about applicability and purpose, not a test. Recognizing what the course does NOT establish is part of answering LO 3.5.A's question about extent."),

 dict(q="Which statement best summarizes what the course framework establishes about the Second Amendment?",
   choices=[
     "That the Court's decisions rest on interpretation of the text, and that the right to keep and bear arms for self-defense applies to the states",
     "That the Second Amendment prohibits all regulation of firearms",
     "That the Second Amendment protects only members of an organized militia",
     "That the Second Amendment restrains only the national government",
     "That the Second Amendment was interpreted for the first time in United States v. Lopez"], ans=0,
   why="EK 3.5.A.1 supplies the first clause and the CED's statement of the McDonald holding supplies the second. The remaining options each assert something the framework does not say, and the last misattributes a Commerce Clause holding."),

 dict(q="Why is it important that a student answering a question about this topic distinguish what the framework states from what is politically contested?",
   choices=[
     "An answer that asserts a holding the framework does not record is wrong even if it matches a common opinion",
     "Political contest determines what the Constitution means",
     "The framework changes whenever public opinion changes",
     "Questions about this topic have no correct answers",
     "The framework endorses one side of the policy debate"], ans=0,
   why="LO 3.5.A asks about the Court's interpretation, and the CED's statements of the required holdings are the record of it. EK 3.6.A.2 separately identifies firearms policy as a subject of debate, which is a different question from what has been decided."),
]
