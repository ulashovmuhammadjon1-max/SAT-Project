# AP U.S. GOVERNMENT AND POLITICS 3.13 Affirmative Action -- 30 questions
# CED V.1 (c) 2026, Unit 3 Civil Liberties and Civil Rights.
# Learning objective 3.13.A: DESCRIBE Supreme Court DEBATES about affirmative
# action policies.
# Suggested skill for this topic (CED p. 95): 1.E, concept application -- explain
# how political principles, institutions, processes, policies, and behaviors
# apply to different scenarios in context.
#
# Essential knowledge relied on. This is the SHORTEST essential knowledge
# statement in the unit, two sentences, and both are quoted here in full because
# everything in this module has to trace to one of them:
#   EK 3.13.A.1 -- "AFFIRMATIVE ACTION refers to policies intended to address
#     WORKPLACE AND EDUCATIONAL DISPARITIES related to RACE, ETHNIC ORIGIN,
#     GENDER, DISABILITY, AND AGE. Supreme Court debate has focused on WHETHER
#     affirmative action IS PROTECTED BY the EQUAL PROTECTION CLAUSE of the
#     Fourteenth Amendment to the Constitution."
#
# THREE THINGS THE FRAMEWORK'S WORDING DOES THAT A PARAPHRASE UNDOES:
#
#   1. FIVE characteristics, not one. Race, ethnic origin, gender, DISABILITY
#      and AGE. The last two are the ones a summary drops, and dropping them
#      makes affirmative action look like a policy about race alone, which is
#      not what the framework defines. Items 2 to 5 turn on the full list.
#
#   2. TWO domains: workplace AND educational. Not education alone.
#
#   3. The debate is over whether affirmative action is PROTECTED BY the equal
#      protection clause -- not whether it VIOLATES the clause. Those are
#      different questions with different burdens, and "protected by" is the
#      framework's own phrase. A student who has absorbed the other framing will
#      reach for it, so items 7 and 8 make the distinction the question.
#
# WHAT THIS MODULE REFUSES TO DO, AND WHY IT IS THE WHOLE DESIGN OF THE TOPIC.
# LO 3.13.A's verb is DESCRIBE and its object is DEBATES. The framework says the
# Court's debate HAS FOCUSED ON a question; it does not say how the question was
# answered. So no key anywhere in this module states an outcome. Where a student
# would naturally expect a resolution -- items 10, 11, 23, 27 and 30 -- the item
# asks instead what the framework does and does not settle, which is the honest
# examinable content and also the answer an FRQ reader would be looking for.
#
# NO CASE IS NAMED. The CED lists four illustrative examples for this topic and
# marks all of them NOT REQUIRED. Naming one would put content the exam cannot
# ask about beside content it can, exactly as in 3.12 with the separate but equal
# doctrine. The verifier enforces it: only the CED's fourteen required cases may
# appear, and none of the four illustrative ones is on that list.
#
# The equal protection clause background this topic assumes comes from EK
# 3.10.A.1 (civil rights guaranteed to all persons under the due process and
# equal protection clauses) and EK 3.12.A.1 (rights restricted at times and
# protected at others), both of which are cited where relied on.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the Fourteenth Amendment is quoted
# verbatim. Both tables are labelled hypothetical, and both are deliberately
# built so that the data CANNOT answer the constitutional question -- which is
# itself what items 27 and 30 test.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("3.13", "Affirmative Action", 3)

_HIRING = ("At a hypothetical firm, the table compares the composition of one year's applicant "
           "pool with the composition of those the firm hired.")
_HIRING_TABLE = dict(
    headers=["Applicant group", "Share of applicants (%)", "Share of those hired (%)"],
    rows=[["Group W", "44", "58"],
          ["Group X", "26", "19"],
          ["Group Y", "18", "14"],
          ["Group Z", "12", "9"]])

_ADMISSIONS = ("A hypothetical university reports, for four separate years, the share of its "
               "applicants and the share of its admitted students drawn from groups it "
               "identifies as underrepresented.")
_ADMISSIONS_TABLE = dict(
    headers=["Year", "Share of applicants (%)", "Share of admitted students (%)"],
    rows=[["Year one", "22", "9"],
          ["Year three", "24", "14"],
          ["Year five", "27", "21"],
          ["Year seven", "29", "26"]])

QUESTIONS = [
 dict(q="According to the course framework, what does affirmative action refer to?",
   choices=[
     "Policies intended to address workplace and educational disparities",
     "Court orders requiring a state to redraw its legislative districts",
     "Rules governing how evidence may be gathered by police",
     "Statutes setting the minimum wage in federally funded work",
     "Procedures a legislature must follow before enacting a law"], ans=0,
   why="EK 3.13.A.1 opens with exactly this definition. The framework defines affirmative action by the disparities the policies are intended to address, not by any particular method of addressing them."),

 dict(q="Which characteristics does EK 3.13.A.1 name in its definition of affirmative action?",
   choices=[
     "Race, ethnic origin, gender, disability, and age",
     "Race and gender only",
     "Race, religion, and national security status",
     "Income, education, and place of residence",
     "Citizenship, military service, and criminal record"], ans=0,
   why="EK 3.13.A.1 lists five characteristics, and disability and age are the two a summary usually drops. Reducing the list to race and gender describes a narrower policy than the one the framework defines."),

 dict(q="Which two characteristics in EK 3.13.A.1's list are most often left out of a summary of affirmative action?",
   choices=[
     "Disability and age",
     "Race and gender",
     "Ethnic origin and race",
     "Gender and ethnic origin",
     "Race and disability"], ans=0,
   why="EK 3.13.A.1 names race, ethnic origin, gender, disability, and age, and the last two extend the concept well beyond the categories it is usually discussed in. A definition that omits them is not the framework's definition."),

 dict(q="A workplace program is designed to address disparities in the hiring of older applicants. Under EK 3.13.A.1's definition, is this within the scope of affirmative action?",
   choices=[
     "Yes, because age is one of the five characteristics the framework's definition names",
     "No, because the framework's definition covers only race and gender",
     "No, because the framework's definition covers only educational settings",
     "Yes, but only if the program also addresses race",
     "No, because age is addressed by a separate constitutional amendment"], ans=0,
   why="EK 3.13.A.1's list of characteristics includes age, and its list of domains includes the workplace, so both elements of the scenario are inside the framework's definition."),

 dict(q="A university program is designed to address disparities in the enrollment of students with disabilities. Under EK 3.13.A.1's definition, is this within the scope of affirmative action?",
   choices=[
     "Yes, because disability is among the named characteristics and education is among the named domains",
     "No, because the framework's definition covers only workplace disparities",
     "No, because disability is not named in the framework's definition",
     "Yes, but only if the program is required by a court order",
     "No, because universities are not government institutions"], ans=0,
   why="EK 3.13.A.1 names disability among the five characteristics and education among the two domains, so the scenario satisfies both halves of the definition. Whether a university is public is a separate question the definition does not turn on."),

 dict(q="Which two domains does EK 3.13.A.1's definition of affirmative action cover?",
   choices=[
     "The workplace and education",
     "Education and voting",
     "The workplace and housing",
     "Voting and jury service",
     "Housing and public accommodations"], ans=0,
   why="EK 3.13.A.1 says the policies are intended to address 'workplace and educational disparities.' Voting, housing and public accommodations belong to statutes described in EK 3.11.A.1 rather than to this definition."),

 dict(q="According to EK 3.13.A.1, what has Supreme Court debate about affirmative action focused on?",
   choices=[
     "Whether affirmative action is protected by the equal protection clause of the Fourteenth Amendment",
     "Whether Congress may regulate interstate commerce",
     "Whether the states may tax federal institutions",
     "Whether procedural due process requires a hearing before a benefit is withdrawn",
     "Whether the Ninth Amendment supports unenumerated rights"], ans=0,
   why="EK 3.13.A.1's second sentence states the question in exactly these words, and the clause it names is the equal protection clause of the Fourteenth Amendment."),

 dict(q="The framework says the Court's debate has focused on whether affirmative action is PROTECTED BY the equal protection clause. How does that differ from asking whether it violates the clause?",
   choices=[
     "The two questions ask what the clause does for the policy and what the policy does to the clause, and they place the burden of argument on different sides",
     "The two questions are identical in every respect",
     "Only the second question involves the Fourteenth Amendment",
     "Only the first question can be decided by a court",
     "The first question concerns statutes and the second concerns the Constitution"], ans=0,
   why="EK 3.13.A.1's phrase is 'protected by', which asks whether the clause shelters the policy, while a violation question asks whether the policy offends the clause. Both concern the same clause, and the framework's own wording is the first."),

 dict(q="Which clause of the Constitution does EK 3.13.A.1 identify as the focus of the Supreme Court's debate about affirmative action?",
   choices=[
     "The equal protection clause of the Fourteenth Amendment",
     "The due process clause of the Fifth Amendment",
     "The privileges or immunities clause of the Fourteenth Amendment",
     "The Commerce Clause of Article I",
     "The Supremacy Clause of Article VI"], ans=0,
   why="EK 3.13.A.1 names the equal protection clause of the Fourteenth Amendment specifically. EK 3.10.A.1 names the same clause, along with the due process clause and acts of Congress, as a source of civil rights generally."),

 dict(q="LO 3.13.A asks students to DESCRIBE Supreme Court DEBATES about affirmative action. What does the choice of that verb and that object indicate about what the framework settles?",
   choices=[
     "That the framework records what the argument is about rather than how it came out",
     "That the framework states a single settled holding students must memorize",
     "That the framework treats the question as never having reached the Court",
     "That the framework requires students to take a position on the policy",
     "That the framework treats the question as one for Congress alone"], ans=0,
   why="EK 3.13.A.1 says the debate HAS FOCUSED ON a question and stops there, and a debate is described rather than resolved. Every other topic in this unit states a holding where there is one to state."),

 dict(q="A student asks what answer the course framework gives to the question the Supreme Court's debate has focused on. What is the accurate response?",
   choices=[
     "The framework states what the debate is about and does not state an answer",
     "The framework states that affirmative action is protected by the equal protection clause",
     "The framework states that affirmative action violates the equal protection clause",
     "The framework states that the question has been withdrawn from the courts",
     "The framework states that the question is governed by the Tenth Amendment"], ans=0,
   why="EK 3.13.A.1's second sentence identifies the focus of the debate and ends. An answer supplied from anywhere else would be presented to a student with the same authority as the framework's own sentence, which is what makes stating one a real risk."),

 dict(q="Read the following excerpt.\n\n“…nor deny to any person within its jurisdiction the equal protection of the laws.”\n—U.S. Constitution, Fourteenth Amendment, Section 1\n\nWhy does this text make affirmative action a constitutional question rather than only a policy question?",
   choices=[
     "Because the clause constrains how a government may treat persons, so a government policy that distinguishes among them must be measured against it",
     "Because the clause forbids all government policies of any kind",
     "Because the clause applies only to private employers",
     "Because the clause requires every government to adopt affirmative action",
     "Because the clause concerns criminal procedure"], ans=0,
   why="The clause runs to any person within a state's jurisdiction and constrains state action, which is why EK 3.13.A.1 locates the Court's debate there. A policy that sorts people by a characteristic raises the question the clause is about."),

 dict(q="Whose conduct does the equal protection clause restrain by its own terms?",
   choices=[
     "A State",
     "Congress",
     "A private university",
     "A private employer",
     "A foreign government"], ans=0,
   why="The clause sits in a sentence whose subject is 'any State', which is the same point EK 3.10.A.1 relies on when it names acts of Congress as a separate source of civil rights that can reach private conduct."),

 dict(q="A public agency adopts a hiring program intended to reduce a disparity in the employment of a group defined by ethnic origin. Applying EK 3.13.A.1, which question does the program raise?",
   choices=[
     "Whether the equal protection clause protects a policy of this kind, which is the question the framework says the Court's debate has focused on",
     "Whether the agency followed the correct procedures in adopting the program",
     "Whether the exclusionary rule applies to the agency's records",
     "Whether Congress has power to create the agency",
     "Whether the program restricts freedom of speech"], ans=0,
   why="Ethnic origin is among EK 3.13.A.1's five characteristics and the workplace is among its two domains, so the program is affirmative action as the framework defines it, and the constitutional question is the one EK 3.13.A.1 names."),

 dict(q="A private company with no government contracts adopts a program of the same kind. Which observation is most important in applying the framework to it?",
   choices=[
     "The equal protection clause by its terms restrains a State, so the constitutional question the framework describes does not arise in the same way",
     "The program is not affirmative action, since the framework covers only public employers",
     "The program raises no legal questions of any kind",
     "The program is governed by the due process clause of the Fifth Amendment",
     "The program must be approved by a federal court before it takes effect"], ans=0,
   why="EK 3.13.A.1's definition turns on the disparities addressed rather than on who addresses them, so the program is affirmative action; but the clause EK 3.13.A.1 names is addressed to a State, which is the distinction EK 3.10.A.1 also draws when it names acts of Congress separately."),

 dict(q="A school district adopts a policy addressing disparities in access to advanced coursework among students of different ethnic origins. Which element of EK 3.13.A.1's definition does the setting satisfy?",
   choices=[
     "The educational domain, one of the two the framework names",
     "The workplace domain, since teachers are employed there",
     "Neither domain, since the framework covers only universities",
     "Neither domain, since the framework covers only private institutions",
     "Both domains equally, since the framework does not distinguish them"], ans=0,
   why="EK 3.13.A.1 names workplace and educational disparities, and a policy about student access to coursework sits in the educational one. The framework's word is EDUCATIONAL rather than higher education, so a school district is inside it."),

 dict(q="A commentator says affirmative action is a policy about race. Which correction does EK 3.13.A.1 support?",
   choices=[
     "The framework's definition names five characteristics, of which race is one",
     "The framework's definition names race alone",
     "The framework's definition names no characteristics at all",
     "The framework's definition covers only gender",
     "The framework's definition applies only where a court has ordered a remedy"], ans=0,
   why="EK 3.13.A.1 lists race, ethnic origin, gender, disability, and age. A description that keeps only the first understates the framework's own scope by four characteristics."),

 dict(q="Two public agencies adopt programs addressing the same disparity, one in hiring and one in a training school it operates. Under EK 3.13.A.1, how do the two compare?",
   choices=[
     "Both are affirmative action as the framework defines it, since the framework names workplace and educational disparities together",
     "Only the hiring program is, since the framework covers workplaces alone",
     "Only the training school program is, since the framework covers education alone",
     "Neither is, since the framework covers only private institutions",
     "Neither is, since the framework requires a court order"], ans=0,
   why="EK 3.13.A.1 names both domains in one sentence and does not rank them, so a policy addressing a covered disparity is within the definition in either setting."),

 dict(q="How does this topic relate to EK 3.12.A.1's account of minority and majority rights?",
   choices=[
     "Both concern circumstances in which a government measure addressed to one group is measured against the equal protection clause",
     "Both concern the procedures officials must follow before acting",
     "Both concern the rights of persons accused of crimes",
     "Both concern the powers of Congress over interstate commerce",
     "Neither concerns the Fourteenth Amendment"], ans=0,
   why="EK 3.12.A.1's fourth item describes the Court upholding the rights of the majority in cases limiting majority-minority districting, and EK 3.13.A.1 locates its debate in the same clause. Both topics are about a measure adopted for one group being tested against a guarantee running to all persons."),

 dict(q="How does the equal protection clause function differently in topic 3.10 and in this topic?",
   choices=[
     "In 3.10 it is described as supporting and motivating movements, while here it is the standard against which a policy adopted for a group is measured",
     "In 3.10 it applies to private conduct and here it applies to state conduct",
     "In 3.10 it concerns criminal procedure and here it concerns education",
     "In 3.10 it is a statute and here it is a constitutional clause",
     "The clause has no role in either topic"], ans=0,
   why="EK 3.10.A.2 says the clause can support and motivate social movements, while EK 3.13.A.1 makes it the provision the Court's debate about affirmative action is conducted under. The same clause plays a mobilizing role in one topic and a testing role in the other."),

 dict(q="Why does the framework place this topic at the end of a unit that also covers social movements and government responses to them?",
   choices=[
     "Because a policy adopted to address a disparity raises a further question under the same clause that movements invoked, which is where the unit's argument arrives",
     "Because affirmative action is unrelated to the rest of the unit",
     "Because the topic concerns criminal procedure",
     "Because the topic is the only one in the unit about Congress",
     "Because the topic replaces the equal protection clause with a different provision"], ans=0,
   why="EK 3.10.A.2 has movements invoking the equal protection clause, EK 3.11.A.1 has the government responding, EK 3.12.A.1 records restriction and protection, and EK 3.13.A.1 asks what the same clause does about a remedy. The clause is the thread."),

 dict(q="A student writes that the Supreme Court has settled the question EK 3.13.A.1 describes. What is the most defensible response, given only the course framework?",
   choices=[
     "The framework describes a debate and identifies its focus, so a claim that it is settled goes beyond what the framework states",
     "The framework states that the question was settled in favor of affirmative action",
     "The framework states that the question was settled against affirmative action",
     "The framework states that no court has considered the question",
     "The framework states that the question belongs to state legislatures"], ans=0,
   why="LO 3.13.A's verb is DESCRIBE and its object is DEBATES, and EK 3.13.A.1 says the debate HAS FOCUSED ON a question without recording an answer. Reporting the framework accurately means reporting that."),

 dict(q="Which of the following is the best summary of what a student can be expected to know about this topic from the course framework alone?",
   choices=[
     "The definition of affirmative action, the five characteristics and two domains it covers, and the constitutional question the Court's debate has focused on",
     "The names and holdings of every Supreme Court case on the subject",
     "The vote in the most recent decision on the subject",
     "The text of the statutes that authorize affirmative action programs",
     "The position each political party takes on the subject"], ans=0,
   why="EK 3.13.A.1 supplies a definition, a list of characteristics, a pair of domains and the focus of a debate, and nothing else. The four cases the CED lists for this topic are marked as illustrative examples that are not required."),

 dict(q="The CED lists several Supreme Court cases alongside this topic and marks them as illustrative examples that are not required. What does that designation mean for a student preparing for the exam?",
   choices=[
     "The cases may help illustrate the debate, but the exam will not require knowledge of them the way it requires the holdings of the required cases",
     "The cases are required and must be memorized with their holdings",
     "The cases have been overruled and may be disregarded entirely",
     "The cases replace the required case list for this unit",
     "The cases are the only content the exam may test for this topic"], ans=0,
   why="The CED distinguishes required cases, whose holdings are course content, from illustrative examples marked NOT REQUIRED. Treating an illustrative example as required content misallocates study and misrepresents what the exam can ask."),

 dict(q=_HIRING + " Which conclusion is best supported by the data?",
   table=_HIRING_TABLE,
   choices=[
     "One group's share of those hired exceeds its share of applicants, and every other group's share of hires falls below its share of applicants",
     "Every group's share of hires matches its share of applicants",
     "Every group's share of hires exceeds its share of applicants",
     "The table reports shares of applicants but not of hires",
     "Two groups' shares of hires exceed their shares of applicants"], ans=0,
   why="Group W rises from 44 percent of applicants to 58 percent of hires, while Groups X, Y and Z each fall, by 7, 4 and 3 points. Both columns are reported and both total 100."),

 dict(q=_HIRING + " Under EK 3.13.A.1's definition, what does this table display?",
   table=_HIRING_TABLE,
   choices=[
     "A workplace disparity of the kind affirmative action policies are intended to address",
     "An educational disparity",
     "A violation of procedural due process",
     "A restriction on freedom of association",
     "A limitation on the bulk collection of metadata"], ans=0,
   why="EK 3.13.A.1 defines affirmative action as policies intended to address workplace and educational disparities, and a gap between a group's share of applicants and its share of hires is a workplace disparity. The table shows the condition a policy would address, not a policy."),

 dict(q=_HIRING + " A student concludes from this table that a policy adopted to close the gap would be unconstitutional. What is the most important correction?",
   table=_HIRING_TABLE,
   choices=[
     "The table measures a disparity, and whether such a policy is protected by the equal protection clause is the question the framework says the Court's debate has focused on",
     "The table shows no disparity at all",
     "The table settles the constitutional question in favor of such a policy",
     "The table shows that the firm is a government employer",
     "The table reports a single applicant, so no share can be computed"], ans=0,
   why="EK 3.13.A.1 identifies the constitutional question and does not answer it, and nothing in a table of hiring shares could. The data establish the condition; the framework leaves the legal consequence of addressing it as a described debate."),

 dict(q=_ADMISSIONS + " Which conclusion is best supported by the data?",
   table=_ADMISSIONS_TABLE,
   choices=[
     "The gap between the share of applicants and the share of admitted students narrowed in each successive year shown",
     "The gap widened in each successive year shown",
     "The gap was unchanged across the four years",
     "The share of admitted students fell across the four years",
     "The share of admitted students exceeded the share of applicants in the final year"], ans=0,
   why="The gaps run 13, then 10, then 6, then 3 percentage points, so each is smaller than the one before. The admitted share rises from 9 to 26 and remains below the applicant share of 29 in the final year."),

 dict(q=_ADMISSIONS + " Under EK 3.13.A.1's definition, which domain does this table concern?",
   table=_ADMISSIONS_TABLE,
   choices=[
     "The educational domain, one of the two the framework's definition names",
     "The workplace domain",
     "The voting domain",
     "The housing domain",
     "Neither domain named in the framework's definition"], ans=0,
   why="EK 3.13.A.1 names workplace and educational disparities, and university admissions sit in the second. Voting and housing are addressed by the statutes described in EK 3.11.A.1 rather than by this definition."),

 dict(q=_ADMISSIONS + " A student concludes from this table that the university's admissions policy is protected by the equal protection clause. What is the most important correction?",
   table=_ADMISSIONS_TABLE,
   choices=[
     "The table reports what a policy achieved, which is a different question from the constitutional one the framework says the Court's debate has focused on",
     "The table shows the policy achieved nothing",
     "The table settles the constitutional question against the policy",
     "The table reports the university's legal reasoning",
     "The table covers a single year, so no trend can be described"], ans=0,
   why="EK 3.13.A.1 states the focus of the debate and records no answer, and effectiveness and constitutionality are different questions in any event. Four years are reported, and the narrowing gap shows an effect rather than a legal conclusion."),
]
