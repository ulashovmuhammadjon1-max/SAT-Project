# AP U.S. GOVERNMENT AND POLITICS 3.12 Balancing Minority and Majority Rights
# -- 30 questions
# CED V.1 (c) 2026, Unit 3 Civil Liberties and Civil Rights.
# Learning objective 3.12.A: explain how the government has AT TIMES ALLOWED THE
# RESTRICTION of the civil rights of minority groups and AT OTHER TIMES HAS
# PROTECTED those rights.
# Suggested skill for this topic (CED p. 94): 2.C, SCOTUS application -- explain
# how the FACTS, ISSUE, HOLDING, REASONING, DECISION and MAJORITY OPINION of a
# required Supreme Court case compare to a non-required Supreme Court case.
#
# Essential knowledge relied on:
#   EK 3.12.A.1 -- "Decisions demonstrating that minority rights have been
#     RESTRICTED AT TIMES and PROTECTED AT OTHER TIMES include:
#       i.   The Emancipation Proclamation freed enslaved people from the states
#            in rebellion against the United States, and the subsequent
#            ratification of the THIRTEENTH AMENDMENT permanently abolished
#            slavery and marked a shift toward the establishment of civil rights
#            for the formerly enslaved
#       ii.  State laws and Supreme Court holdings based on the 'SEPARATE BUT
#            EQUAL' doctrine restricting African American access to the same
#            restaurants, hotels, schools, etc., as the majority white population
#       iii. Court decisions declaring that race-based school segregation
#            violates the Fourteenth Amendment's Equal Protection Clause
#       iv.  The Supreme Court UPHOLDING THE RIGHTS OF THE MAJORITY in cases that
#            limit and prohibit MAJORITY-MINORITY DISTRICTING"
#
# THE LIST ALTERNATES DIRECTION, AND THAT IS THE TOPIC. Item i protects, item ii
# restricts, item iii protects, item iv limits a measure adopted for a minority.
# LO 3.12.A's own construction is AT TIMES... AT OTHER TIMES, which is a claim
# about oscillation rather than about progress. A module that presented these
# four as a staircase would be teaching the opposite of the objective, and the
# verifier's _oscillation gate exists to keep that from creeping in. Items 3, 4,
# 22 and 23 make the alternation itself the question.
#
# WHAT THIS MODULE DELIBERATELY DOES NOT NAME. EK 3.12.A.1.ii describes "state
# laws and Supreme Court holdings based on the 'separate but equal' doctrine"
# and names no case. Plessy v. Ferguson is not on the required list and the CED
# does not name it here, so this module describes the doctrine exactly as the
# framework does and never attributes it to a case by name. SOCIAL_BRIEF.md's
# rule is that a key must trace to a CED sentence; naming a case the framework
# withholds would put content the exam cannot ask about beside content it can,
# with no way for a student to tell them apart.
#
# THE CED'S OWN SCOTUS VOCABULARY (p. 29) is used exactly, because skill 2.C is
# defined in terms of it: FACTS are the relevant events before courts became
# involved; the ISSUE is the legal or constitutional question considered; the
# HOLDING is the court's response to the issue; the REASONING is the explanation
# of a holding; the DECISION is the outcome including facts, issue, holding and
# reasoning; the MAJORITY OPINION is the written analysis agreed to by more than
# half. Items 12 to 16 test those distinctions directly. Students are not
# expected to know dissenting or concurring opinions (CED p. 29), so none is
# asked about, and every non-required case in this module prints its own facts
# and holding in the stem, as the CED says the exam does.
#
# Documents the CED attaches to 3.12.A (pp. 26-27): the Emancipation
# Proclamation and "Letter from a Birmingham Jail."
# Required cases the CED attaches to 3.12.A (p. 31): Brown v. Board of Education.
# Shaw v. Reno is cross-listed to other topics rather than to 3.12.A, but its
# holding as the CED states it IS the framework's own description of EK
# 3.12.A.1.iv, so it appears here with that holding stated verbatim and cited to
# the required-case list.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the Thirteenth and Fourteenth
# Amendments, the Emancipation Proclamation and the Letter are quoted verbatim.
# Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("3.12", "Balancing Minority and Majority Rights", 3)

_ACCESS = ("In a hypothetical jurisdiction operating under a separate but equal rule, the table "
           "compares facilities provided for the two groups of residents in one year.")
_ACCESS_TABLE = dict(
    headers=["Facility", "Provided for the majority group", "Provided for the minority group"],
    rows=[["Public secondary schools", "24", "4"],
          ["Public libraries", "11", "1"],
          ["Public parks with playgrounds", "18", "2"],
          ["Public hospitals", "6", "1"]])

_RULINGS = ("The table classifies a hypothetical set of Supreme Court rulings on claims brought "
            "by members of minority groups, by decade and by outcome.")
_RULINGS_TABLE = dict(
    headers=["Period", "Rulings restricting the claimed right",
             "Rulings protecting the claimed right"],
    rows=[["First period", "14", "3"],
          ["Second period", "9", "8"],
          ["Third period", "4", "19"],
          ["Fourth period", "10", "12"]])

QUESTIONS = [
 dict(q="According to the course framework, what do the decisions listed in EK 3.12.A.1 demonstrate?",
   choices=[
     "That minority rights have been restricted at some times and protected at others",
     "That minority rights have been steadily expanded without interruption",
     "That minority rights have been steadily narrowed without interruption",
     "That minority rights have never been the subject of a Supreme Court decision",
     "That minority rights are determined entirely by state law"], ans=0,
   why="EK 3.12.A.1 introduces its list with exactly this pairing, and LO 3.12.A's construction is AT TIMES ALLOWED THE RESTRICTION and AT OTHER TIMES HAS PROTECTED. The claim is about a record that moves in both directions."),

 dict(q="LO 3.12.A pairs the phrases AT TIMES and AT OTHER TIMES. What does that construction commit the objective to?",
   choices=[
     "A record that moves in both directions rather than in one",
     "A record of continuous improvement",
     "A record of continuous decline",
     "A record in which the government never acted at all",
     "A record confined to a single decade"], ans=0,
   why="The objective could have been written as a claim about progress and was not; it names two directions and assigns each to some times. Reading the framework's list as a staircase contradicts the sentence that introduces it."),

 dict(q="Which of the four items in EK 3.12.A.1 describes a restriction of minority rights rather than a protection of them?",
   choices=[
     "State laws and Supreme Court holdings based on the separate but equal doctrine",
     "The Emancipation Proclamation and the subsequent ratification of the Thirteenth Amendment",
     "Court decisions declaring race-based school segregation unconstitutional",
     "The permanent abolition of slavery",
     "The extension of civil rights to the formerly enslaved"], ans=0,
   why="EK 3.12.A.1.ii describes the separate but equal doctrine as restricting access to the same restaurants, hotels and schools as the majority population, which is the restricting item in a list that otherwise protects."),

 dict(q="Why does EK 3.12.A.1 include an item about the Supreme Court upholding the rights of the majority?",
   choices=[
     "Because the framework's claim is about a record moving in both directions, and a decision limiting a measure adopted for a minority is part of that record",
     "Because the framework treats majority rights as the only rights that matter",
     "Because the framework holds that minority rights have never been protected",
     "Because the framework treats every Supreme Court decision as a restriction",
     "Because the item was included by mistake and has no bearing on the topic"], ans=0,
   why="EK 3.12.A.1.iv names the Court upholding the rights of the majority in cases limiting majority-minority districting, and it sits in a list introduced as showing restriction at some times and protection at others. The item is what keeps the list from reading as a one-way trend."),

 dict(q="Read the following excerpt.\n\n“Neither slavery nor involuntary servitude, except as a punishment for crime whereof the party shall have been duly convicted, shall exist within the United States, or any place subject to their jurisdiction.”\n—U.S. Constitution, Thirteenth Amendment, Section 1\n\nHow does this text differ in reach from the Emancipation Proclamation as EK 3.12.A.1 describes it?",
   choices=[
     "It reaches the whole United States and any place subject to its jurisdiction, rather than only states in rebellion",
     "It reaches only the states that had been in rebellion",
     "It reaches only persons convicted of a crime",
     "It applies only to future generations",
     "It applies only where a state legislature has adopted it"], ans=0,
   why="EK 3.12.A.1.i says the Proclamation freed enslaved people from the states in rebellion and that the subsequent Thirteenth Amendment permanently abolished slavery. The amendment's own text names the United States and any place subject to its jurisdiction, which is why the framework calls it permanent."),

 dict(q="According to EK 3.12.A.1, what did the ratification of the Thirteenth Amendment mark?",
   choices=[
     "A shift toward the establishment of civil rights for the formerly enslaved",
     "The end of all discrimination in the United States",
     "The beginning of the separate but equal doctrine",
     "The repeal of the Emancipation Proclamation",
     "The transfer of civil rights questions to the states"], ans=0,
   why="EK 3.12.A.1.i uses exactly the phrase 'marked a shift toward the establishment of civil rights for the formerly enslaved.' The framework's word SHIFT is a beginning rather than a completion, which is why items ii and iv follow it in the same list."),

 dict(q="Why is the framework's word SHIFT, rather than a word like completion, the accurate one for what the Thirteenth Amendment marked?",
   choices=[
     "Because the same list goes on to describe restrictions that came afterward",
     "Because the amendment was never ratified by enough states",
     "Because the amendment applied only to one state",
     "Because the amendment was repealed a decade later",
     "Because the amendment concerned voting rather than slavery"], ans=0,
   why="EK 3.12.A.1's second item describes the separate but equal doctrine restricting access to facilities, and its fourth describes decisions upholding the rights of the majority. A list whose later items restrict cannot have been completed by its first."),

 dict(q="According to EK 3.12.A.1, what did the separate but equal doctrine restrict?",
   choices=[
     "African American access to the same restaurants, hotels, schools, and similar facilities as the majority white population",
     "The right to vote in federal elections only",
     "The right to serve on juries only",
     "The right to own property in any state",
     "The right to travel between states"], ans=0,
   why="EK 3.12.A.1.ii names restaurants, hotels and schools among the facilities to which access was restricted, and says the restriction ran to the same facilities as those of the majority white population. The doctrine's subject is access to shared facilities."),

 dict(q="The framework attributes the separate but equal doctrine to two kinds of source. What are they?",
   choices=[
     "State laws and Supreme Court holdings",
     "Federal statutes and executive orders",
     "Local ordinances and private agreements",
     "Constitutional amendments and treaties",
     "Party platforms and campaign promises"], ans=0,
   why="EK 3.12.A.1.ii names 'state laws and Supreme Court holdings based on the separate but equal doctrine.' Naming both is what shows the restriction was carried by the courts as well as by legislatures."),

 dict(q="A student asks why the doctrine was called separate BUT EQUAL. Which answer best reflects how the framework describes what the doctrine actually produced?",
   choices=[
     "The name asserted equality while the framework describes the doctrine as restricting access to the same facilities as the majority population",
     "The name accurately described facilities that were identical in every respect",
     "The name referred to equality between states rather than between persons",
     "The name was chosen by Congress rather than by any court",
     "The name applied only to schools and to no other facility"], ans=0,
   why="EK 3.12.A.1.ii's verb is RESTRICTING and its object is access to the same restaurants, hotels and schools as the majority white population, which is a description of unequal access under a name that claimed equality."),

 dict(q="In Brown v. Board of Education (1954), the Supreme Court held that race-based school segregation violates the equal protection clause of the Fourteenth Amendment. Which item of EK 3.12.A.1 does the holding correspond to?",
   choices=[
     "The item on court decisions declaring that race-based school segregation violates the Fourteenth Amendment's equal protection clause",
     "The item on the separate but equal doctrine",
     "The item on the Emancipation Proclamation and the Thirteenth Amendment",
     "The item on the Court upholding the rights of the majority",
     "None of the items, since the case concerns education rather than civil rights"], ans=0,
   why="EK 3.12.A.1.iii describes exactly this class of decision, and the CED attaches Brown to 3.12.A. The holding is stated under the equal protection clause, which is the clause the framework's item names."),

 dict(q="Using the course framework's vocabulary for analyzing a Supreme Court case, what are the FACTS of a case?",
   choices=[
     "The relevant events that occurred before the courts became involved",
     "The legal or constitutional question the Court considered",
     "The Court's response to the question presented",
     "The explanation the Court gave for its answer",
     "The written analysis agreed to by more than half the justices"], ans=0,
   why="The CED defines facts as the relevant events before courts became involved, and defines issue, holding, reasoning and majority opinion separately. Skill 2.C is stated in terms of these six words, so the distinctions among them are course content."),

 dict(q="Using the course framework's vocabulary, what is the ISSUE in a Supreme Court case?",
   choices=[
     "The legal or constitutional question the Court considered",
     "The events that occurred before any lawsuit was filed",
     "The Court's answer to the question presented",
     "The remedy ordered for the winning party",
     "The number of justices who joined the majority"], ans=0,
   why="The CED defines the issue as the legal or constitutional question considered, which is distinct both from the events that produced the dispute and from the Court's answer to it."),

 dict(q="Using the course framework's vocabulary, what is the HOLDING of a case, as distinct from its reasoning?",
   choices=[
     "The Court's response to the issue, while the reasoning is the explanation of that response",
     "The explanation of the answer, while the reasoning is the answer itself",
     "The events preceding the litigation, while the reasoning is the question presented",
     "The number of votes cast, while the reasoning is the opinion's length",
     "The remedy ordered, while the reasoning is the identity of the parties"], ans=0,
   why="The CED defines the holding as the court's response to the issue and the reasoning as the explanation of a holding. Reversing the two is the standard confusion, and skill 2.C requires them to be kept apart."),

 dict(q="Using the course framework's vocabulary, what does the DECISION in a case include?",
   choices=[
     "The outcome including the facts, the issue, the holding, and the reasoning",
     "The holding alone",
     "The reasoning alone",
     "The name of the justice who wrote the opinion",
     "The vote count alone"], ans=0,
   why="The CED defines the decision as the outcome including facts, issue, holding, and reasoning, which makes it the broadest of the six terms rather than a synonym for the holding."),

 dict(q="Using the course framework's vocabulary, what makes an opinion the MAJORITY opinion?",
   choices=[
     "It is the written analysis agreed to by more than half the justices",
     "It is the longest opinion filed in the case",
     "It is the opinion written by the chief justice",
     "It is the first opinion released to the public",
     "It is the opinion that disagrees with the outcome"], ans=0,
   why="The CED defines the majority opinion as the justices' written analysis agreed to by more than half. The framework also states that students are not expected to know dissenting or concurring opinions of required cases."),

 dict(q="A non-required case is presented on the exam. What does the course framework say a student can rely on?",
   choices=[
     "That the case will be accompanied by a summary containing all the information necessary to compare it with a required case",
     "That the student is expected to have memorized the non-required case",
     "That only the vote count will be supplied",
     "That the required case will be summarized instead",
     "That no comparison will be asked for"], ans=0,
   why="The CED states that any non-required case on the exam will be accompanied by a summary containing all information necessary to compare it, which is why a comparison item supplies the unfamiliar case's facts and holding in the stem."),

 dict(q="In Shaw v. Reno (1993), the Supreme Court held that under the Fourteenth Amendment's equal protection clause, majority-minority districts created under the Voting Rights Act of 1965 may be constitutionally challenged by voters if race is the only factor used in creating the district. Which item of EK 3.12.A.1 does this holding illustrate?",
   choices=[
     "The item on the Court upholding the rights of the majority in cases that limit and prohibit majority-minority districting",
     "The item on the separate but equal doctrine",
     "The item on the Emancipation Proclamation",
     "The item on race-based school segregation",
     "None of them, since the case concerns districting rather than civil rights"], ans=0,
   why="EK 3.12.A.1.iv describes decisions limiting and prohibiting majority-minority districting, and the CED states the Shaw holding as allowing such districts to be challenged where race is the only factor used. The framework's item and the holding describe the same class of case."),

 dict(q="A non-required case: voters challenge a legislative map, and the record shows the mapmakers used several criteria, including keeping counties whole and preserving incumbents' districts, one of which was the racial composition of neighborhoods. Comparing the FACTS with those in Shaw v. Reno, what is the most significant difference?",
   choices=[
     "In the case described, race was one factor among several, while the holding in Shaw turns on race being the only factor used",
     "In the case described, no map was drawn at all",
     "In the case described, the challengers were the mapmakers themselves",
     "In the case described, the Fourteenth Amendment was not in force",
     "In the case described, the map was drawn by a federal agency"], ans=0,
   why="The CED states the Shaw holding as permitting a challenge where race is THE ONLY FACTOR used in creating the district, so a record showing several operative criteria differs on the fact the holding turns on. Skill 2.C asks precisely for comparisons of this kind."),

 dict(q="A non-required case: a state requires separate public waiting rooms for two groups of travelers and argues that the facilities are of equal quality. Comparing the ISSUE presented with the issue in Brown v. Board of Education, what do the two have in common?",
   choices=[
     "Both ask whether a government may separate people by race consistently with the Fourteenth Amendment's equal protection clause",
     "Both ask whether the federal government may regulate interstate travel",
     "Both ask whether a state may operate public facilities at all",
     "Both ask whether procedural due process was satisfied",
     "Both ask whether a statute was properly enacted"], ans=0,
   why="Skill 2.C compares the issue, which the CED defines as the legal or constitutional question considered. The equal protection question about racial separation by a government is the same question in both, whatever the facility."),

 dict(q="Read the following excerpt.\n\n“…all persons held as slaves within any State or designated part of a State, the people whereof shall then be in rebellion against the United States, shall be then, thenceforward, and forever free…”\n—Abraham Lincoln, Emancipation Proclamation, 1863\n\nWhy does EK 3.12.A.1 pair this document with the Thirteenth Amendment rather than presenting it alone?",
   choices=[
     "Because the Proclamation reached only the places named in its own text, and the amendment is what the framework calls the permanent abolition",
     "Because the Proclamation was never issued",
     "Because the amendment repealed the Proclamation",
     "Because the amendment was ratified before the Proclamation was issued",
     "Because the Proclamation applied to the entire country already"], ans=0,
   why="EK 3.12.A.1.i names the Proclamation's reach as the states in rebellion and calls the subsequent Thirteenth Amendment the permanent abolition of slavery. Pairing them is how the framework records a partial measure completed by a later one."),

 dict(q="Read the following excerpt.\n\n“An unjust law is a code that a numerical or power majority group compels a minority group to obey but does not make binding on itself.”\n—Martin Luther King, Jr., “Letter from a Birmingham Jail,” 1963\n\nHow does this test bear on the subject of this topic?",
   choices=[
     "It supplies a standard for identifying when a majority has restricted a minority's rights, which is one of the two directions LO 3.12.A names",
     "It argues that majorities never restrict minorities",
     "It argues that minority rights should be decided by referendum",
     "It concerns procedural due process rather than the treatment of groups",
     "It argues that no law creates any obligation"], ans=0,
   why="LO 3.12.A pairs restriction with protection, and the Letter's test asks whether a burden falls on a group that did not impose it. The CED attaches the Letter to 3.12.A, and read for implications the test names the pattern the objective's first half describes."),

 dict(q="A student writes that the history in EK 3.12.A.1 is a story of steady progress. What is the most important correction the framework itself supports?",
   choices=[
     "The list includes a restriction that came after an expansion and a limitation that came after a protection, so it is not a single direction",
     "The list includes no protections at all",
     "The list includes no restrictions at all",
     "The list covers only a single year",
     "The list concerns only voting rights"], ans=0,
   why="EK 3.12.A.1's items run from the Thirteenth Amendment's shift to the separate but equal doctrine to school desegregation decisions to decisions limiting majority-minority districting. LO 3.12.A's AT TIMES and AT OTHER TIMES is the framework's own summary of that shape."),

 dict(q="Which statement best describes the relationship EK 3.12.A.1 draws between majority rights and minority rights?",
   choices=[
     "Both appear in the same list, and a decision protecting one may limit a measure adopted for the other",
     "Only minority rights appear in the framework",
     "Only majority rights appear in the framework",
     "The two are always protected by the same decision",
     "The framework says the two never come into contact"], ans=0,
   why="EK 3.12.A.1's fourth item is about the Court upholding the rights of the majority in cases limiting majority-minority districting, placed in a list whose subject is the treatment of minority rights. The topic's own title is Balancing Minority and Majority Rights."),

 dict(q=_ACCESS + " Which conclusion is best supported by the data?",
   table=_ACCESS_TABLE,
   choices=[
     "For every facility listed, the number provided for the majority group is at least five times the number provided for the minority group",
     "The two groups were provided the same number of every facility",
     "The minority group was provided more facilities than the majority group in at least one category",
     "The table reports no facilities for the majority group",
     "Public hospitals were the only category with any difference between the groups"], ans=0,
   why="Comparing each row, the ratios are 24 to 4, 11 to 1, 18 to 2 and 6 to 1, and the smallest of these is six to one. Every category shows a difference, so no category is the only one."),

 dict(q=_ACCESS + " Which statement in the course framework does this table most directly illustrate?",
   table=_ACCESS_TABLE,
   choices=[
     "That the separate but equal doctrine restricted minority access to the same facilities as the majority population",
     "That the Thirteenth Amendment permanently abolished slavery",
     "That race-based school segregation violates the equal protection clause",
     "That the Court has upheld the rights of the majority in districting cases",
     "That procedural due process requires non-arbitrary methods"], ans=0,
   why="EK 3.12.A.1.ii names schools among the facilities to which access was restricted under the separate but equal doctrine, and every row of this table is such a facility. The other statements concern different items in the framework or a different topic entirely."),

 dict(q=_ACCESS + " A defender of the arrangement argues that the facilities were equal because both groups were provided with each type. What is the strongest objection the data supply?",
   table=_ACCESS_TABLE,
   choices=[
     "Providing 4 secondary schools against 24 is not equality, since the counts differ by a factor of six in the smallest gap in the table",
     "The table shows that one group was provided no facilities at all",
     "The table reports only a single category of facility",
     "The table shows the two groups provided identical counts",
     "The table gives no counts, so no comparison is possible"], ans=0,
   why="The argument turns equality into mere presence, and the counts answer it: the closest row is six to one and the widest is eleven to one. Every category is represented for both groups, which is why presence cannot be the test."),

 dict(q=_RULINGS + " Which conclusion is best supported by the data?",
   table=_RULINGS_TABLE,
   choices=[
     "Rulings protecting the claimed right outnumbered restricting rulings in the third period, but restricting rulings led in the first period",
     "Protecting rulings outnumbered restricting rulings in every period",
     "Restricting rulings outnumbered protecting rulings in every period",
     "The two columns were equal in every period",
     "No rulings of either kind were issued in any period"], ans=0,
   why="The first period reports 14 restricting against 3 protecting, and the third reports 4 against 19. Neither column leads throughout, which is what makes both of the sweeping alternatives false."),

 dict(q=_RULINGS + " Which statement in the course framework does the pattern across these four periods most directly illustrate?",
   table=_RULINGS_TABLE,
   choices=[
     "That minority rights have been restricted at some times and protected at other times",
     "That minority rights have never been restricted",
     "That minority rights have never been protected",
     "That the Supreme Court decides no cases about minority rights",
     "That every ruling on minority rights protects the claimed right"], ans=0,
   why="EK 3.12.A.1 introduces its list with exactly this pairing, and LO 3.12.A's AT TIMES and AT OTHER TIMES is the same claim. A table whose leading column changes across periods is that claim in observable form."),

 dict(q=_RULINGS + " A student projects from the third period that protecting rulings will continue to grow as a share of the total. What does the fourth period show about that projection?",
   table=_RULINGS_TABLE,
   choices=[
     "Protecting rulings still led, but their share of the period's rulings fell from about 83 percent to about 55 percent",
     "Protecting rulings disappeared entirely",
     "Protecting rulings grew as a share, confirming the projection",
     "The fourth period reports no rulings of either kind",
     "The fourth period is identical to the third"], ans=0,
   why="The third period is 19 protecting of 23 rulings and the fourth is 12 of 22, so the lead survives while the share falls by nearly thirty points. Extrapolating a direction from one period is the error, which is also why LO 3.12.A is written as an oscillation rather than a trend."),
]
