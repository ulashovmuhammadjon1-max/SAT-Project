# AP U.S. GOVERNMENT AND POLITICS 3.7 Selective Incorporation -- 30 questions
# CED V.1 (c) 2026, Unit 3 Civil Liberties and Civil Rights.
# Learning objective 3.7.A: explain the IMPLICATIONS of the doctrine of
# selective incorporation.
#
# Essential knowledge relied on. ONE sentence, and it contains the whole
# mechanism -- what the doctrine does, to whom, by what route:
#   EK 3.7.A.1 -- "The doctrine of SELECTIVE INCORPORATION has imposed
#     LIMITATIONS ON STATE REGULATION of civil liberties by extending SELECT
#     protections of the Bill of Rights TO THE STATES through the DUE PROCESS
#     CLAUSE OF THE FOURTEENTH AMENDMENT."
#
# FOUR PARTS, AND A STUDENT MUST HAVE ALL FOUR:
#   WHAT     limitations on STATE regulation of civil liberties. The Bill of
#            Rights already restrained the national government; incorporation
#            adds the states and adds nothing else.
#   WHICH    SELECT protections. Not all of them. The framework's own adjective
#            is in the doctrine's name, and it is the difference between
#            selective incorporation and total incorporation -- a distinction
#            items 5 to 9 are built on, because a bank that says "the Bill of
#            Rights applies to the states" has dropped the word the topic is
#            named for.
#   TO WHOM  the states, and through them their local governments.
#   HOW      the DUE PROCESS CLAUSE of the Fourteenth Amendment. Not the
#            Supremacy Clause, not the Privileges or Immunities Clause as the
#            framework states it, not the Tenth Amendment. Items 10 to 14 turn
#            on the route.
#
# THE IMPLICATION LO 3.7.A ASKS ABOUT, and the reason this is a topic rather
# than a definition: before incorporation, a person whose state violated a Bill
# of Rights guarantee had no federal constitutional remedy, because the
# guarantee did not run against the state at all. Incorporation is what makes
# most of American civil liberties litigation possible, and every required case
# in this unit that involves a STATE or a SCHOOL DISTRICT depends on it. Items
# 15 to 22 use that: Engel, Gideon, Yoder and McDonald are all incorporation
# cases in the sense that none of them could have been brought without it.
#
# WHAT THIS MODULE DOES NOT DO: it does not list which guarantees have been
# incorporated and which have not. The framework says SELECT and names no roster,
# and a list assembled from outside the CED would be content the exam cannot
# ask about. Where a specific guarantee appears here it is one the CED itself
# supplies through a required case holding.
#
# Documents the CED attaches to 3.7.A (p. 26-27): the Articles of Confederation,
# "Letter from a Birmingham Jail."
# Required cases the CED attaches to 3.7.A (p. 31-33): Engel v. Vitale,
# Gideon v. Wainwright, Wisconsin v. Yoder, McDonald v. Chicago.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the Fourteenth Amendment, the First
# Amendment and the Articles of Confederation are quoted verbatim. Both tables
# are labelled hypothetical where they are not drawn from required holdings.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("3.7", "Selective Incorporation", 3)

_CASES = ("The table lists four required Supreme Court cases, the government whose action was "
          "challenged in each, and the guarantee the Court applied.")
_CASES_TABLE = dict(
    headers=["Case", "Whose action was challenged", "Guarantee applied"],
    rows=[["Engel v. Vitale (1962)", "A public school district", "Establishment Clause of the First Amendment"],
          ["Gideon v. Wainwright (1963)", "A state court", "Sixth Amendment right to an attorney"],
          ["Wisconsin v. Yoder (1972)", "A state", "Free Exercise Clause of the First Amendment"],
          ["McDonald v. Chicago (2010)", "A city", "Second Amendment right to keep and bear arms"]])

_TIMELINE = ("In a hypothetical account of one legal system, the table reports how many "
             "guarantees from a bill of rights had been made enforceable against subnational "
             "governments by the end of each period.")
_TIMELINE_TABLE = dict(
    headers=["Period", "Guarantees enforceable against the national government", "Guarantees enforceable against subnational governments"],
    rows=[["First", "24", "0"],
          ["Second", "24", "3"],
          ["Third", "24", "11"],
          ["Fourth", "24", "17"]])

QUESTIONS = [
 dict(q="According to the course framework, what has the doctrine of selective incorporation done?",
   choices=[
     "Imposed limitations on state regulation of civil liberties by extending select protections of the Bill of Rights to the states",
     "Extended every protection of the Bill of Rights to the states at once",
     "Removed limitations on state regulation of civil liberties",
     "Transferred civil liberties questions from the courts to Congress",
     "Applied the Bill of Rights to foreign governments"], ans=0,
   why="EK 3.7.A.1 states this in exactly these words, and the word SELECT is part of them. The second option describes total incorporation, which is the doctrine's alternative rather than the doctrine."),

 dict(q="Through which constitutional provision does selective incorporation operate?",
   choices=[
     "The due process clause of the Fourteenth Amendment",
     "The Supremacy Clause of Article VI",
     "The Necessary and Proper Clause of Article I",
     "The Tenth Amendment",
     "The Commerce Clause"], ans=0,
   why="EK 3.7.A.1 names the due process clause of the Fourteenth Amendment as the route. The other provisions do real work elsewhere in this course and none of them is the vehicle for incorporation."),

 dict(q="Read the following excerpt.\n\n“No State shall make or enforce any law which shall abridge the privileges or immunities of citizens of the United States; nor shall any State deprive any person of life, liberty, or property, without due process of law.”\n—U.S. Constitution, Fourteenth Amendment, Section 1\n\nWhy is this text the vehicle for incorporation rather than some other provision?",
   choices=[
     "It restrains the states by name and protects liberty, so a guarantee can be read into the liberty it protects",
     "It restrains Congress by name",
     "It grants the states power over civil liberties",
     "It repeals the Bill of Rights",
     "It applies only to citizens and not to other persons"], ans=0,
   why="The clause's subject is 'No State' and its object is life, liberty and property, which is why EK 3.7.A.1 routes incorporation through it. Note that the due process clause says 'any person' rather than citizens."),

 dict(q="Before incorporation, what was the position of a person whose STATE violated a Bill of Rights guarantee?",
   choices=[
     "The guarantee did not run against the state, so it supplied no federal constitutional remedy",
     "The guarantee applied to the state exactly as it applied to the national government",
     "The state was required to obtain congressional approval before acting",
     "The person could appeal directly to Congress",
     "The guarantee applied but could be enforced only by the state's own courts"], ans=0,
   why="EK 3.7.A.1's point is that incorporation EXTENDED protections to the states, which means they did not reach them before. That is the implication LO 3.7.A asks a student to explain."),

 dict(q="What does the word SELECTIVE in the doctrine's name signify?",
   choices=[
     "Some protections of the Bill of Rights have been extended to the states and others have not",
     "The states may select which protections to accept",
     "The Court selects which states are bound",
     "Congress selects which protections apply",
     "The doctrine applies only to selected years"], ans=0,
   why="EK 3.7.A.1's phrase is 'extending SELECT protections', so the selection is among GUARANTEES rather than among states, years or anyone's preferences."),

 dict(q="What is the difference between selective incorporation and total incorporation?",
   choices=[
     "Selective incorporation extends guarantees one at a time, so some remain unincorporated; total incorporation would extend all of them together",
     "Selective incorporation extends all guarantees at once and total incorporation extends them one at a time",
     "Selective incorporation applies to the national government and total incorporation to the states",
     "The two terms describe the same doctrine",
     "Selective incorporation operates through the Supremacy Clause and total incorporation through due process"], ans=0,
   why="The distinction is exactly the framework's word SELECT: guarantee-by-guarantee extension leaves some behind, which a total approach would not. EK 3.7.A.1 describes the selective version."),

 dict(q="A student writes that selective incorporation means the Bill of Rights applies to the states. What is the most important correction?",
   choices=[
     "SELECT protections have been extended, so the claim is true of many guarantees and not of all of them",
     "No protection has been extended to the states",
     "The Bill of Rights applies to the states but not to the national government",
     "The Bill of Rights applies only through the Supremacy Clause",
     "The student is right, since incorporation is complete"], ans=0,
   why="Dropping the adjective the doctrine is named for is the standard error, and EK 3.7.A.1 keeps it: SELECT protections, not all of them."),

 dict(q="Why does the framework's account make incorporation a matter of LIMITATIONS ON STATE REGULATION?",
   choices=[
     "A guarantee extended to the states is a restriction on what a state may do, which is what the Bill of Rights already was for the national government",
     "It transfers regulatory authority from the states to Congress",
     "It requires states to enact civil liberties statutes",
     "It gives states new powers over civil liberties",
     "It abolishes state regulation entirely"], ans=0,
   why="EK 3.7.A.1's phrase is 'imposed limitations on state regulation of civil liberties.' A guarantee is a limit on government, and incorporation adds a government it limits."),

 dict(q="Does incorporation reach city and county governments?",
   choices=[
     "Yes, because local governments are created by and exercise the authority of the states",
     "No, because EK 3.7.A.1 names only the states",
     "No, because local governments are part of the national government",
     "Only when Congress passes a statute saying so",
     "Only in states that have consented"], ans=0,
   why="McDonald v. Chicago, a required case, applied an incorporated guarantee to a CITY, which is how the framework's own required holdings answer this. A local government exercises state authority."),

 dict(q="In Gideon v. Wainwright (1963), the Supreme Court held that the Sixth Amendment's right to an attorney extends procedural due process protections to felony defendants in state courts. How does the holding illustrate EK 3.7.A.1?",
   choices=[
     "A guarantee that had bound the national government was extended to state proceedings through due process",
     "A guarantee was extended to the national government for the first time",
     "The Court held that the Sixth Amendment does not apply to state courts",
     "The Court transferred criminal trials to federal courts",
     "The Court held that states may define their own procedural rights"], ans=0,
   why="The CED's statement of the holding uses the phrase 'extends procedural due process protections... in state courts,' which is EK 3.7.A.1's mechanism named in the holding itself."),

 dict(q="In Engel v. Vitale (1962), the Supreme Court held that school sponsorship of religious activities violates the Establishment Clause of the First Amendment. Why is that case an incorporation case?",
   choices=[
     "A public school district is a state instrumentality, so applying a First Amendment guarantee to it requires that the guarantee reach the states",
     "The case concerned an act of Congress",
     "The case concerned a federal school",
     "The Establishment Clause applies to the states by its own terms",
     "The case was decided under the Tenth Amendment"], ans=0,
   why="The First Amendment's text restrains Congress, so reaching a school district requires the extension EK 3.7.A.1 describes. That is what makes an ordinary-looking school case an incorporation case."),

 dict(q="In Wisconsin v. Yoder (1972), the Supreme Court held that compelling Amish students to attend school past the eighth grade violates the Free Exercise Clause of the First Amendment. Whose law was limited?",
   choices=[
     "A state's, since compulsory attendance laws are state laws",
     "Congress's, since the requirement was a federal statute",
     "A school district's alone, leaving state law untouched",
     "A foreign government's",
     "The Court's own, by narrowing its jurisdiction"], ans=0,
   why="Compulsory attendance is state law, and a First Amendment guarantee limiting it is only possible because of incorporation. The CED attaches Yoder to 3.7.A for exactly that reason."),

 dict(q="In McDonald v. Chicago (2010), the Supreme Court held that the Second Amendment right to keep and bear arms for self-defense is applicable to the states. Which words in that holding name the incorporation question?",
   choices=[
     "Applicable to the states",
     "The Second Amendment",
     "To keep and bear arms",
     "For self-defense",
     "The Supreme Court held"], ans=0,
   why="EK 3.7.A.1's whole subject is which governments a guarantee binds, and 'applicable to the states' is the phrase that answers it. 'For self-defense' names the purpose rather than the reach."),

 dict(q="What do Engel, Gideon, Yoder and McDonald have in common that makes them all relevant to this topic?",
   choices=[
     "In each, a guarantee from the Bill of Rights was applied against a state or a government exercising state authority",
     "In each, the Court struck down an act of Congress",
     "In each, the Court applied the same amendment",
     "In each, the Court declined to reach the merits",
     "In each, the challenged action was taken by a federal agency"], ans=0,
   why="The four cases involve a school district, a state court, a state and a city, and four different guarantees. What unites them is the direction of the limit, which is EK 3.7.A.1's subject."),

 dict(q="Read the following excerpt.\n\n“Each state retains its sovereignty, freedom, and independence, and every power, jurisdiction, and right, which is not by this Confederation expressly delegated to the United States, in Congress assembled.”\n—Articles of Confederation, Article II\n\nWhat does this provision show about the situation incorporation later changed?",
   choices=[
     "Under the Articles the union had no authority over how a state treated its own residents, which is the condition the Fourteenth Amendment and incorporation reversed",
     "Under the Articles the Bill of Rights already bound the states",
     "Under the Articles Congress could review every state law",
     "Under the Articles the states had no authority of their own",
     "Under the Articles a national court enforced individual rights against the states"], ans=0,
   why="The CED attaches the Articles to 3.7.A, and the connection is the starting point: a union confined to expressly delegated powers reached nothing a state did internally. EK 1.4.A.1 records that the Confederation also had no national court system."),

 dict(q="Which statement best expresses the IMPLICATION of selective incorporation that LO 3.7.A asks about?",
   choices=[
     "Most civil liberties litigation in the United States is possible only because guarantees run against the states as well as the national government",
     "The Bill of Rights has been repealed as to the national government",
     "State constitutions no longer protect any rights",
     "Congress now enacts all civil liberties protections",
     "The Fourteenth Amendment applies only to criminal cases"], ans=0,
   why="LO 3.7.A asks for implications, and the practical implication is the volume: state and local governments make most of the decisions that touch daily life, so a guarantee reaching only Congress would reach very little."),

 dict(q="A state constitution protects a right more broadly than the incorporated federal guarantee does. What follows?",
   choices=[
     "The state may protect more than the federal floor requires; incorporation sets a minimum rather than a maximum",
     "The state protection is invalid, since the federal guarantee controls",
     "The federal guarantee no longer applies in that state",
     "Congress must approve the broader state protection",
     "The Supreme Court must reduce the state protection to the federal level"], ans=0,
   why="EK 3.7.A.1 describes LIMITATIONS ON STATE REGULATION, which is a floor beneath which a state may not go. Nothing in the doctrine stops a state from doing more."),

 dict(q="Which of the following is NOT an implication of selective incorporation?",
   choices=[
     "State governments lost the power to legislate on subjects the Bill of Rights mentions",
     "State laws may be challenged in federal court on Bill of Rights grounds",
     "Local government actions are subject to guarantees that once bound only Congress",
     "The Fourteenth Amendment's due process clause became a route for enforcing individual rights",
     "The reach of a guarantee can differ depending on whether it has been incorporated"], ans=0,
   why="A limit on how a state may regulate is not a removal of the power to regulate; a state may still legislate on speech, searches and religion within the constitutional bounds. The other four follow directly from EK 3.7.A.1."),

 dict(q="Why did incorporation proceed guarantee by guarantee rather than all at once?",
   choices=[
     "Each extension came in a case raising that particular guarantee, so the doctrine grew as cases arose",
     "Congress incorporated the guarantees one at a time by statute",
     "The states each accepted one guarantee per year",
     "The Constitution requires a separate amendment for each guarantee",
     "The Court is limited to one decision per amendment"], ans=0,
   why="Courts decide the cases before them, so a doctrine developed through litigation extends only what a case puts in issue. That is why the framework's adjective is SELECTIVE."),

 dict(q="A state argues that a Bill of Rights guarantee does not limit it because the guarantee's text names Congress. What is the strongest response?",
   choices=[
     "If that guarantee has been incorporated, it reaches the state through the Fourteenth Amendment's due process clause regardless of the original text's wording",
     "The guarantee's text has been amended to name the states",
     "The Supremacy Clause makes every federal provision binding on the states",
     "The state waived the argument by joining the union",
     "Congress has enacted a statute applying the guarantee to states"], ans=0,
   why="EK 3.7.A.1's mechanism is precisely this: the original text's audience does not settle the question once the guarantee has been extended through due process. The word IF matters, because incorporation is selective."),

 dict(q=_CASES + " Which conclusion is best supported by the table?",
   table=_CASES_TABLE,
   choices=[
     "All four cases challenged the action of a state or of a government exercising state authority, and each applied a different guarantee",
     "All four cases challenged an act of Congress",
     "All four cases applied the same guarantee",
     "Two of the four challenged the action of the national government",
     "None of the cases involved a state government"], ans=0,
   why="The second column reads school district, state court, state and city -- none of them the national government -- and the third column names four different guarantees."),

 dict(q=_CASES + " Which row shows most directly that incorporation reaches LOCAL government?",
   table=_CASES_TABLE,
   choices=[
     "McDonald v. Chicago, in which the action challenged was a city's",
     "Engel v. Vitale, in which the action challenged was a state court's",
     "Gideon v. Wainwright, in which the action challenged was a city's",
     "Wisconsin v. Yoder, in which the action challenged was Congress's",
     "None of them, since all four involved state governments"], ans=0,
   why="The McDonald row names a city. The distractors misstate the second column for the other three rows, which the table itself contradicts."),

 dict(q=_CASES + " What does the variety in the third column show about the doctrine?",
   table=_CASES_TABLE,
   choices=[
     "Guarantees from different amendments have been extended separately, which is what makes the incorporation selective",
     "Only First Amendment guarantees have been extended",
     "Only guarantees concerning criminal procedure have been extended",
     "All guarantees were extended in a single decision",
     "The amendment involved makes no difference to the analysis"], ans=0,
   why="Four cases, four guarantees, four decades: extension case by case is exactly what EK 3.7.A.1's word SELECT describes."),

 dict(q=_TIMELINE + " Which conclusion is best supported by the data?",
   table=_TIMELINE_TABLE,
   choices=[
     "The number binding subnational governments grew across the periods while the number binding the national government did not change",
     "Both columns grew across the periods",
     "The number binding subnational governments reached the number binding the national government",
     "The number binding the national government fell",
     "No guarantee bound subnational governments in any period"], ans=0,
   why="The national column is 24 in every period while the subnational column runs 0, 3, 11 and 17. Seventeen is short of twenty-four, which is the gap the doctrine's name predicts."),

 dict(q=_TIMELINE + " What does the gap between the two columns in the final period show?",
   table=_TIMELINE_TABLE,
   choices=[
     "Some guarantees still bind the national government without binding subnational ones, which is what selective incorporation means",
     "Every guarantee now binds both levels",
     "More guarantees bind subnational governments than the national government",
     "The two columns have always been equal",
     "The gap shows an error in the table"], ans=0,
   why="Seventeen against twenty-four leaves seven guarantees that reach one level and not the other, which is the selective half of EK 3.7.A.1 shown as a number."),

 dict(q=_TIMELINE + " A student concludes from the data that incorporation will eventually be complete. Which limitation of the data most undercuts that conclusion?",
   table=_TIMELINE_TABLE,
   choices=[
     "A trend of past extensions cannot show that the remaining guarantees will be extended, since each requires a case raising it",
     "The table omits the subnational column, so no trend can be observed",
     "The table covers a single period, so no trend can be observed",
     "The table reports percentages that do not sum to one hundred",
     "The table gives no information about the national government"], ans=0,
   why="Extrapolating a doctrinal series assumes the remaining items are like the ones already extended, which nothing in the table supports. Both columns and four periods are plainly present."),

 dict(q="Read the following excerpt.\n\n“Injustice anywhere is a threat to justice everywhere.”\n—Martin Luther King, Jr., “Letter from a Birmingham Jail,” 1963\n\nHow does this claim bear on the implications of selective incorporation?",
   choices=[
     "A national guarantee enforceable against every state is the institutional form of the idea that injustice in one place is a national concern",
     "It argues that each state should set its own standards for rights",
     "It argues that rights should be enforced only locally",
     "It argues that the Bill of Rights should apply only to Congress",
     "It has no bearing on the reach of constitutional guarantees"], ans=0,
   why="The CED attaches the Letter to 3.7.A, and the connection is structural: a guarantee that binds only the national government leaves the treatment of a person in a state a purely local matter."),

 dict(q="Which question would best test whether a particular guarantee has been incorporated?",
   choices=[
     "Has the Supreme Court held that this guarantee applies to state or local government action?",
     "Does the guarantee appear in the Bill of Rights?",
     "Has Congress passed a statute mentioning the guarantee?",
     "Do most states protect the guarantee in their own constitutions?",
     "Was the guarantee ratified before the Fourteenth Amendment?"], ans=0,
   why="EK 3.7.A.1 makes incorporation a matter of extension by the Court through due process, so the test is whether a holding has done it. Appearing in the Bill of Rights is what makes a guarantee a CANDIDATE, not what incorporates it."),

 dict(q="Which statement best summarizes what the course framework establishes about selective incorporation?",
   choices=[
     "Select Bill of Rights protections have been extended to the states through the Fourteenth Amendment's due process clause, limiting state regulation of civil liberties",
     "All Bill of Rights protections apply to the states through the Supremacy Clause",
     "The states are free to regulate civil liberties without federal constraint",
     "Congress determines which protections apply to the states",
     "The Fourteenth Amendment repealed the Bill of Rights"], ans=0,
   why="This restates EK 3.7.A.1's four parts in order: which protections (select), to whom (the states), by what route (due process), with what effect (limits on state regulation)."),

 dict(q="Why does the framework treat selective incorporation as a doctrine with IMPLICATIONS rather than as a definition to be memorized?",
   choices=[
     "Its consequences reach every civil liberties question involving a state or local government, which is most of them",
     "It has no practical consequences",
     "It applies only to cases decided before 1900",
     "It concerns the structure of Congress rather than individual rights",
     "It is a rule of statutory rather than constitutional interpretation"], ans=0,
   why="LO 3.7.A's word is IMPLICATIONS, and the reason is scope: state and local governments make most of the decisions that touch individuals, so which governments a guarantee binds determines how much it does."),
]
