# AP U.S. GOVERNMENT AND POLITICS 3.11 Government Responses to Social Movements
# -- 30 questions
# CED V.1 (c) 2026, Unit 3 Civil Liberties and Civil Rights.
# Learning objective 3.11.A: explain how the government HAS RESPONDED to social
# movements.
# Suggested skill for this topic (CED p. 93): 2.B, SCOTUS application -- explain
# how a required Supreme Court case relates to a foundational document or to
# other primary or secondary sources.
#
# Essential knowledge relied on. One statement with four items, and the shape of
# the statement is the content:
#   EK 3.11.A.1 -- "The government can respond to social movements through COURT
#     RULINGS AND/OR POLICIES," including:
#       i.   "Supreme Court decisions which declared that race-based school
#            segregation violates the Fourteenth Amendment's equal protection
#            clause."
#       ii.  "The CIVIL RIGHTS ACT OF 1964 prohibits discrimination in public
#            places, provides for the integration of schools and other public
#            facilities, and makes employment discrimination illegal."
#       iii. "TITLE IX of the Education Amendments Act of 1972 prohibits SEX
#            discrimination in any education program or activity RECEIVING
#            FEDERAL FINANCIAL ASSISTANCE."
#       iv.  "The VOTING RIGHTS ACT OF 1965 prohibits RACIAL discrimination in
#            VOTING."
#
# TWO CHANNELS, AND THE CONJUNCTION IS "AND/OR". A response can be judicial, or
# legislative, or both, and the framework declines to rank them. Item 1 asks for
# the pair; items 15 to 17 work the judicial channel and items 5 to 14 the
# legislative one. Reading the topic as being about courts alone is the standard
# compression, and it is wrong three times over: three of the framework's four
# items are statutes.
#
# EACH STATUTE HAS A SCOPE, AND THE SCOPE IS WHAT A PARAPHRASE LOSES.
#   * Title IX's condition is RECEIVING FEDERAL FINANCIAL ASSISTANCE. Drop it
#     and the statute appears to reach every school in the country, which is a
#     different law. Items 10 and 11 turn on it.
#   * The Voting Rights Act's subject is RACIAL discrimination in VOTING --
#     one characteristic, one activity. Item 13 turns on it.
#   * The Civil Rights Act of 1964 carries THREE subjects in the framework's own
#     sentence: public places, integration of schools and other public
#     facilities, and employment. Item 6 asks for all three.
# Swapping any one statute's subject for another's is the error the verifier's
# _scopes gate exists to catch, because it is a clean falsehood that reads as a
# reasonable summary.
#
# Documents the CED attaches to 3.11.A (pp. 26-27): the Gettysburg Address and
# "Letter from a Birmingham Jail."
# Required cases the CED attaches to 3.11.A (p. 31): Brown v. Board of Education.
# Skill 2.B is why items 18 to 21 relate Brown to those two documents rather than
# to another case.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the Gettysburg Address and the Letter
# are quoted verbatim. Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("3.11", "Government Responses to Social Movements", 3)

_ACTIONS = ("The table reports a hypothetical year of federal enforcement activity, classified "
            "by the statute under which each action was opened.")
_ACTIONS_TABLE = dict(
    headers=["Statute invoked", "Enforcement actions opened",
             "Actions resolved with a finding of violation"],
    rows=[["Civil Rights Act of 1964, employment provisions", "1450", "402"],
          ["Title IX of the Education Amendments Act of 1972", "530", "173"],
          ["Voting Rights Act of 1965", "240", "96"]])

_DISTRICTS = ("The table follows a hypothetical set of 160 school districts in the years after a "
              "court ruling requiring desegregation.")
_DISTRICTS_TABLE = dict(
    headers=["Year after the ruling", "Districts operating under a desegregation plan",
             "Districts with no plan in place"],
    rows=[["First", "18", "142"],
          ["Fifth", "76", "84"],
          ["Tenth", "121", "39"],
          ["Fifteenth", "148", "12"]])

QUESTIONS = [
 dict(q="According to the course framework, through what does the government respond to social movements?",
   choices=[
     "Court rulings and policies, either separately or together",
     "Court rulings only",
     "Policies only",
     "Constitutional amendments only",
     "Executive orders only"], ans=0,
   why="EK 3.11.A.1 says the government can respond 'through court rulings and/or policies', and the conjunction is what makes both channels available. Three of the four items the statement then lists are statutes, so reading the topic as being about courts alone misses most of it."),

 dict(q="Of the four responses EK 3.11.A.1 lists, how many are acts of Congress rather than court decisions?",
   choices=[
     "Three",
     "One",
     "Two",
     "Four",
     "None"], ans=0,
   why="EK 3.11.A.1 lists the Civil Rights Act of 1964, Title IX of the Education Amendments Act of 1972, and the Voting Rights Act of 1965 as statutes, alongside a single item about Supreme Court decisions on school segregation."),

 dict(q="Why does it matter that the framework describes government responses as coming through court rulings AND policies rather than through court rulings alone?",
   choices=[
     "A ruling settles the case before the court while a statute can set a rule for conduct the court was never asked about",
     "A ruling and a statute always produce identical results",
     "A statute may be issued only after a court has ruled",
     "A court may not rule on a subject Congress has legislated about",
     "A statute has no effect until a court enforces it against a private party"], ans=0,
   why="EK 3.11.A.1 pairs the two channels without ranking them, and their reach differs: the Civil Rights Act of 1964 makes employment discrimination illegal generally, which no single judgment between two parties could do."),

 dict(q="A movement wins a Supreme Court decision, and Congress later passes a statute covering the same subject more broadly. In the framework's terms, this sequence shows",
   choices=[
     "both channels of government response being used on one subject",
     "that the statute overruled the decision",
     "that the decision was invalid until the statute passed",
     "that only one channel of response actually exists",
     "that Congress may not legislate on a subject the Court has decided"], ans=0,
   why="EK 3.11.A.1's phrase 'court rulings and/or policies' contemplates exactly this combination, and the framework's own list pairs decisions on school segregation with the Civil Rights Act of 1964 in a single statement."),

 dict(q="According to the course framework, what does the Civil Rights Act of 1964 do?",
   choices=[
     "Prohibits discrimination in public places, provides for the integration of schools and other public facilities, and makes employment discrimination illegal",
     "Prohibits racial discrimination in voting",
     "Prohibits sex discrimination in education programs receiving federal funds",
     "Requires that every school district adopt a desegregation plan approved by a federal court",
     "Guarantees the right to counsel in state criminal proceedings"], ans=0,
   why="EK 3.11.A.1.ii states these three subjects in one sentence. The second and third options are the Voting Rights Act of 1965 and Title IX, which the framework lists as separate items with different subjects."),

 dict(q="Which three subjects does the framework's own sentence about the Civil Rights Act of 1964 cover?",
   choices=[
     "Public places, the integration of schools and other public facilities, and employment",
     "Voting, jury service, and housing",
     "Education, health care, and transportation",
     "Wages, working hours, and union membership",
     "Immigration, naturalization, and citizenship"], ans=0,
   why="EK 3.11.A.1.ii names public places, integration of schools and other public facilities, and employment discrimination. A summary that reduces the statute to one of the three understates what the framework says it does."),

 dict(q="A restaurant open to the public refuses to serve customers because of their race. Which response named in EK 3.11.A.1 most directly reaches that conduct?",
   choices=[
     "The Civil Rights Act of 1964, which prohibits discrimination in public places",
     "Title IX, which concerns education programs",
     "The Voting Rights Act of 1965, which concerns voting",
     "A Supreme Court decision on school segregation",
     "None of them, since the conduct is private"], ans=0,
   why="EK 3.11.A.1.ii names discrimination in public places as one of the Civil Rights Act's three subjects, and a restaurant open to the public is such a place. The Fourteenth Amendment's clauses are addressed to a State, which is why a statute is the instrument that reaches a private business."),

 dict(q="An employer refuses to hire qualified applicants because of their national origin. Which response named in EK 3.11.A.1 most directly reaches that conduct?",
   choices=[
     "The Civil Rights Act of 1964, which makes employment discrimination illegal",
     "Title IX, which prohibits sex discrimination in education programs",
     "The Voting Rights Act of 1965, which prohibits racial discrimination in voting",
     "A Supreme Court decision declaring race-based school segregation unconstitutional",
     "The Fourteenth Amendment's equal protection clause, acting on its own"], ans=0,
   why="EK 3.11.A.1.ii names employment discrimination as one of the three subjects of the Civil Rights Act of 1964. The equal protection clause by its terms restrains a State, so it does not on its own reach a private employer's hiring."),

 dict(q="According to the course framework, what does Title IX of the Education Amendments Act of 1972 prohibit?",
   choices=[
     "Sex discrimination in any education program or activity receiving federal financial assistance",
     "Racial discrimination in voting",
     "Discrimination in public places of every kind",
     "Employment discrimination by any private business",
     "Segregation in housing sold or rented to the public"], ans=0,
   why="EK 3.11.A.1.iii states this in exactly these words, and both halves matter: the characteristic is sex and the reach is conditioned on federal financial assistance."),

 dict(q="Which condition does the framework's statement of Title IX place on the programs it reaches?",
   choices=[
     "That the education program or activity receives federal financial assistance",
     "That the education program is operated by a state government",
     "That the education program enrolls more than a set number of students",
     "That the education program has been sued previously",
     "That the education program operates in more than one state"], ans=0,
   why="EK 3.11.A.1.iii conditions the statute's reach on receiving federal financial assistance. Dropping that condition turns the framework's sentence into a claim about every school in the country, which is a different statute."),

 dict(q="Why does the federal funding condition in Title IX matter to how the statute works?",
   choices=[
     "It ties the obligation to the acceptance of federal money, which is how Congress reaches programs it does not otherwise administer",
     "It means Title IX applies only to federal employees",
     "It means Title IX may be enforced only by the Supreme Court",
     "It means Title IX expires when funding ends for the year",
     "It means Title IX applies only to programs Congress created"], ans=0,
   why="EK 3.11.A.1.iii's condition is receipt of federal financial assistance, and attaching a requirement to funds is the mechanism by which the statute reaches schools that Congress neither created nor runs."),

 dict(q="According to the course framework, what does the Voting Rights Act of 1965 prohibit?",
   choices=[
     "Racial discrimination in voting",
     "Sex discrimination in education programs",
     "Discrimination in public accommodations",
     "Employment discrimination on the basis of national origin",
     "Discrimination in the sale of housing"], ans=0,
   why="EK 3.11.A.1.iv states this in exactly these words. The statute the framework describes has one characteristic and one activity, and each of the other four options belongs to a different item in the same list."),

 dict(q="A state adopts a rule that in practice keeps voters of one race from registering. Which response named in EK 3.11.A.1 addresses this most directly?",
   choices=[
     "The Voting Rights Act of 1965",
     "Title IX of the Education Amendments Act of 1972",
     "The Civil Rights Act of 1964's employment provisions",
     "A Supreme Court decision on school segregation",
     "The Civil Rights Act of 1964's public accommodations provisions"], ans=0,
   why="EK 3.11.A.1.iv assigns racial discrimination in voting to the Voting Rights Act of 1965, and the scenario is exactly that combination of characteristic and activity. Each alternative names a statute or decision whose subject is something else."),

 dict(q="A university that accepts federal research funding is alleged to provide fewer athletic opportunities to women than to men. Which response named in EK 3.11.A.1 applies most directly?",
   choices=[
     "Title IX, since the allegation concerns sex discrimination in an education program receiving federal financial assistance",
     "The Voting Rights Act of 1965, since a public institution is involved",
     "The Civil Rights Act of 1964's public accommodations provisions, since a campus is open to visitors",
     "A Supreme Court decision on school segregation, since a school is involved",
     "No federal response, since athletics is not an academic program"], ans=0,
   why="Every element of EK 3.11.A.1.iii is present: the characteristic is sex, the setting is an education program or activity, and the institution receives federal financial assistance. The framework's word ACTIVITY is what brings athletics inside the statute."),

 dict(q="Which of the four responses in EK 3.11.A.1 is a court ruling rather than a statute?",
   choices=[
     "Supreme Court decisions declaring that race-based school segregation violates the equal protection clause",
     "The Civil Rights Act of 1964",
     "Title IX of the Education Amendments Act of 1972",
     "The Voting Rights Act of 1965",
     "None of them; all four are statutes"], ans=0,
   why="EK 3.11.A.1.i is the judicial item in the list and the other three are acts of Congress. It is the item the CED's own attachment of Brown v. Board of Education to this topic points at."),

 dict(q="In Brown v. Board of Education (1954), the Supreme Court held that race-based school segregation violates the equal protection clause of the Fourteenth Amendment. In the framework's terms, that decision is an example of",
   choices=[
     "a government response to a social movement arriving through the judicial channel",
     "a government response arriving through legislation",
     "a social movement responding to the government",
     "a constitutional amendment",
     "an executive order"], ans=0,
   why="EK 3.11.A.1 names court rulings as one of the two channels and its first item describes exactly this class of decision. The CED attaches Brown to 3.11.A, which is why it is the framework's own instance."),

 dict(q="What is one limitation of a court ruling as a government response, compared with a statute?",
   choices=[
     "A ruling decides the dispute presented to the court, so extending it to other institutions may require further litigation",
     "A ruling has no legal force until Congress approves it",
     "A ruling applies only to the party that lost the case and to no one else ever",
     "A ruling may be ignored by any government official who disagrees with it",
     "A ruling may be issued only when a statute already covers the subject"], ans=0,
   why="EK 3.11.A.1 lists both channels because they work differently: a court decides the case before it, while a statute states a general rule at once. The desegregation table in this topic shows the gap between a ruling and its general realization."),

 dict(q="Read the following excerpt.\n\n“Injustice anywhere is a threat to justice everywhere.”\n—Martin Luther King, Jr., “Letter from a Birmingham Jail,” 1963\n\nHow does the holding in Brown v. Board of Education relate to this claim?",
   choices=[
     "The holding treats segregation in particular school districts as a violation of a national constitutional guarantee rather than as a local arrangement",
     "The holding leaves each district free to decide the question for itself",
     "The holding concerns freedom of speech rather than equality",
     "The holding applies only to the parties who brought the case and creates no national standard",
     "The holding rests on the Establishment Clause"], ans=0,
   why="Skill 2.B asks how a required case relates to a foundational document. The Letter argues that a local injustice is everyone's concern, and Brown's holding under the Fourteenth Amendment's equal protection clause makes a local practice a national constitutional question."),

 dict(q="Read the following excerpt.\n\n“…a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.”\n—Abraham Lincoln, Gettysburg Address, 1863\n\nWhich statement best describes the relationship between this passage and the holding in Brown v. Board of Education?",
   choices=[
     "The passage states a national commitment to equality as a proposition, and the holding gives that commitment a specific legal consequence in public schooling",
     "The passage is the legal authority the Court cited as binding in the case",
     "The passage and the holding concern unrelated subjects",
     "The passage repeals the equal protection clause the holding applies",
     "The holding was issued before the passage was written"], ans=0,
   why="Skill 2.B asks how a case relates to a foundational document. The Address states a proposition; the holding applies the equal protection clause of the Fourteenth Amendment to a concrete practice. A speech is not a source of legal authority, which is why the second option fails."),

 dict(q="Read the following excerpt.\n\n“We know through painful experience that freedom is never voluntarily given by the oppressor; it must be demanded by the oppressed.”\n—Martin Luther King, Jr., “Letter from a Birmingham Jail,” 1963\n\nWhat does this claim imply about the government responses EK 3.11.A.1 describes?",
   choices=[
     "That such responses tend to follow sustained demands rather than to arise on their own",
     "That such responses arise without any pressure from outside government",
     "That such responses are always immediate and complete",
     "That court rulings are the only response that can ever be obtained",
     "That the government responds only to majorities"], ans=0,
   why="Read for its implications, the passage asserts that change follows demand rather than preceding it, and the topic's own title places the government's action in the position of a RESPONSE. The framework attaches the Letter to 3.11.A for exactly this connection."),

 dict(q="A student uses the Gettysburg Address as legal authority for a constitutional argument. What is the most important correction?",
   choices=[
     "The Address is a foundational document that states a principle, but the legal authority for an equal protection claim is the Fourteenth Amendment",
     "The Address has no relevance to any constitutional question",
     "The Address was superseded by the Emancipation Proclamation",
     "The Address is binding on the Supreme Court but not on Congress",
     "The Address may be cited only in cases about military policy"], ans=0,
   why="Skill 2.B asks how a case relates to a document, not that the document supplies the rule of decision. The Address is required course content and states a national proposition; the enforceable text is the amendment ratified in 1868."),

 dict(q="Which pairing of a response with the conduct it addresses is correct as the course framework states it?",
   choices=[
     "The Voting Rights Act of 1965 with racial discrimination in voting",
     "Title IX with racial discrimination in voting",
     "The Civil Rights Act of 1964 with sex discrimination in federally funded education programs",
     "The Voting Rights Act of 1965 with employment discrimination",
     "Title IX with discrimination in public accommodations"], ans=0,
   why="EK 3.11.A.1.iv assigns racial discrimination in voting to the Voting Rights Act of 1965. Each of the other four pairings gives one named statute the subject the framework assigns to a different one."),

 dict(q="A commentator says that after the Civil Rights Act of 1964 there was no further need for the Voting Rights Act of 1965. Which observation from the course framework best answers this?",
   choices=[
     "The framework assigns voting to a separate statute, so the subjects the 1964 act covers do not include it",
     "The framework says the 1964 act was repealed",
     "The framework says the 1965 act covers employment as well",
     "The framework says the two statutes have identical subjects",
     "The framework says the 1965 act was passed before the 1964 act"], ans=0,
   why="EK 3.11.A.1.ii names public places, integration of schools and other public facilities, and employment; EK 3.11.A.1.iv names voting and assigns it to the 1965 act. The framework lists them as separate items precisely because their subjects differ."),

 dict(q="Taken together, what do the four items in EK 3.11.A.1 suggest about how government responses to a movement accumulate?",
   choices=[
     "They arrive in more than one form and over a period of years rather than in a single act",
     "They arrive in a single act that settles every question at once",
     "They arrive only from the judiciary",
     "They arrive only from Congress",
     "They arrive before any movement has formed"], ans=0,
   why="The framework's own list spans a decision and three statutes enacted in 1964, 1965 and 1972, and it uses two channels. That spread across forms and years is what the list itself shows."),

 dict(q=_ACTIONS + " Which conclusion is best supported by the data?",
   table=_ACTIONS_TABLE,
   choices=[
     "The statute with the fewest actions opened had the largest share of actions resolved with a finding of violation",
     "The statute with the most actions opened had the largest share resolved with a finding of violation",
     "Each statute produced the same number of actions",
     "No action under any statute was resolved with a finding of violation",
     "Title IX produced fewer actions than the Voting Rights Act of 1965"], ans=0,
   why="The Voting Rights Act row is the smallest at 240 actions and its 96 findings are 40 percent of them, above Title IX at about 33 percent and the employment provisions at about 28 percent. Title IX at 530 is above the Voting Rights Act, not below it."),

 dict(q=_ACTIONS + " The three rows of this table correspond to which channel of government response in EK 3.11.A.1?",
   table=_ACTIONS_TABLE,
   choices=[
     "Policies, since each row names an act of Congress rather than a court decision",
     "Court rulings, since enforcement actions are filed in court",
     "Constitutional amendments, since civil rights are constitutional",
     "Executive orders, since federal agencies bring the actions",
     "Neither channel, since the framework names only court rulings"], ans=0,
   why="EK 3.11.A.1 names court rulings and policies as the two channels, and every row here is a statute the framework lists among its policy responses. That enforcement may end up in court does not change which instrument created the obligation."),

 dict(q=_ACTIONS + " A student concludes from the table that Title IX is the least used of the three statutes. What is the most important correction?",
   table=_ACTIONS_TABLE,
   choices=[
     "Title IX produced 530 actions against 240 under the Voting Rights Act of 1965, so it is not the least used",
     "The table does not report how many actions were opened",
     "Title IX produced more actions than any other statute in the table",
     "The three statutes produced identical numbers of actions",
     "The table covers a single action, so no comparison is possible"], ans=0,
   why="Ranking the three rows by actions opened gives 1450, then 530, then 240, so Title IX sits in the middle. A statute that is not the largest is not thereby the smallest."),

 dict(q=_DISTRICTS + " Which conclusion is best supported by the data?",
   table=_DISTRICTS_TABLE,
   choices=[
     "The number of districts operating under a plan rose in every period, and it passed the number without a plan between the fifth and tenth years",
     "The number of districts operating under a plan fell over the period",
     "A majority of districts were operating under a plan in the first year",
     "The two columns never cross during the period shown",
     "Every district was operating under a plan by the fifth year"], ans=0,
   why="The plan column runs 18, then 76, then 121, then 148, and the no-plan column falls from 142 to 12. At the fifth year 76 is still below 84, and by the tenth year 121 is above 39, so the crossing falls between those two observations."),

 dict(q=_DISTRICTS + " Which claim about government responses does this pattern best illustrate?",
   table=_DISTRICTS_TABLE,
   choices=[
     "A court ruling can set a requirement whose general realization takes years of further action",
     "A court ruling takes effect everywhere the moment it is issued",
     "A court ruling has no effect on the institutions it addresses",
     "A statute is the only instrument that can change institutional practice",
     "Institutional practice changes only when a majority of the public demands it"], ans=0,
   why="EK 3.11.A.1 lists court rulings as one channel of response, and the table shows the requirement spreading across fifteen years rather than arriving at once. Both extremes are contradicted by the data: the column moves, and it does not move immediately."),

 dict(q=_DISTRICTS + " A student concludes that the ruling produced immediate compliance across these districts. What is the most important correction?",
   table=_DISTRICTS_TABLE,
   choices=[
     "In the first year only 18 of the 160 districts were operating under a plan, well under a fifth of them",
     "The table shows every district under a plan in the first year",
     "The table does not report the first year",
     "The number of districts under a plan never rose above 100",
     "The table covers one district, so no share can be computed"], ans=0,
   why="The first row reports 18 districts under a plan against 142 without one, which is about 11 percent, and the plan column does not pass half until after the fifth year. Immediate compliance would require the first row to look like the last."),
]
