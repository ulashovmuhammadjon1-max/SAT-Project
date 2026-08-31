# AP U.S. GOVERNMENT AND POLITICS 3.9 Amendments: Due Process and the Right to
# Privacy -- 30 questions
# CED V.1 (c) 2026, Unit 3 Civil Liberties and Civil Rights.
# Learning objective 3.9.A: explain THE EXTENT TO WHICH the government is
# limited by SUBSTANTIVE due process from infringing upon individual rights.
# Suggested skill for this topic (CED p. 91): 1.A, describe political
# principles, institutions, processes, policies, and behaviors.
#
# Essential knowledge relied on:
#   EK 3.9.A.1 -- "Over time, the Supreme Court has recognized constitutionally
#     protected rights that are not explicitly listed in the Bill of Rights.
#     These UNENUMERATED rights include the RIGHT TO PRIVACY." Two arguments are
#     given for their existence, and the framework attributes them to "justices
#     and scholars" rather than settling between them:
#       * that an unenumerated right is IMPLIED BY CERTAIN AMENDMENTS that
#         assume the existence of such rights;
#       * that the NINTH AMENDMENT, "which states that individuals have
#         protected rights beyond those listed in the first eight amendments,"
#         supports them.
#     Then the operative sentence: "In a range of cases, the Supreme Court has
#     used SUBSTANTIVE DUE PROCESS to examine whether government laws and
#     actions are ARBITRARY INFRINGEMENTS of individual rights."
#   EK 3.9.A.2 -- three decisions, in sequence, each stated by the framework:
#       * Griswold v. Connecticut (1965): "while a right to privacy is not
#         explicitly named in the Constitution," the Court "interpreted the due
#         process clause to protect the right of privacy from government
#         infringement";
#       * Roe v. Wade (1973): "the application of substantive due process
#         further extended the privacy right to abortion";
#       * Dobbs v. Jackson Women's Health Organization (2022): "overturned Roe
#         v. Wade, holding that the Constitution does not confer a right to
#         abortion, leaving decisions about the regulation of abortion to
#         legislatures."
#     And the sentence that closes the topic: "The actions that are protected by
#     the right to privacy and substantive due process CONTINUE TO BE DEBATED."
#
# THE DISTINCTION THIS TOPIC EXISTS TO DRAW, and the reason 3.8 and 3.9 are
# separate topics with nearly identical titles: PROCEDURAL due process asks
# whether the METHODS officials used were arbitrary (EK 3.8.A.2); SUBSTANTIVE
# due process asks whether the LAW ITSELF is an arbitrary infringement (EK
# 3.9.A.1). A perfect hearing can produce a substantive violation and a correct
# rule can be applied through an arbitrary procedure, which is why neither
# swallows the other. Items 8 to 12 turn on it, and so does the first table.
#
# WHAT THIS MODULE REFUSES TO ASSERT. The framework states what Dobbs held and
# stops. It does not say what Dobbs did to Griswold, does not name a test for
# which unenumerated rights survive, and does not settle between the two
# arguments for unenumerated rights -- its own verbs are "some argue" and
# "others argue." No key here fills any of those three gaps. Where the debate is
# the content, the debate is what the item asks about; item 30 and the survey
# table carry EK 3.9.A.2's closing clause rather than a resolution of it.
#
# Required cases the CED attaches to 3.9.A (p. 31): Brown v. Board of Education.
# The CED attaches no foundational document to 3.9.A. Griswold, Roe and Dobbs
# are not on the required-case list, but EK 3.9.A.2 names all three and states
# each holding, so they are course content for this topic and are stated here in
# the framework's own words.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the Ninth and Fourteenth Amendments are
# quoted verbatim. Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("3.9", "Amendments: Due Process and the Right to Privacy", 3)

_CHALLENGES = ("In a hypothetical study, the table classifies constitutional challenges brought "
               "against one state's laws by the ground on which each was argued, and reports how "
               "often the government's action was struck down.")
_CHALLENGES_TABLE = dict(
    headers=["Ground of the challenge", "Challenges brought", "Government action struck down"],
    rows=[["Substantive: the law itself is an arbitrary infringement", "120", "34"],
          ["Procedural: the methods officials used were arbitrary", "260", "96"],
          ["Both grounds argued together", "45", "18"]])

_SURVEY = ("The table reports the share of respondents in a hypothetical survey who say each "
           "decision should be protected from government regulation as a matter of personal "
           "privacy.")
_SURVEY_TABLE = dict(
    headers=["Decision at issue", "All adults (%)", "Under 40 (%)", "40 and older (%)"],
    rows=[["Whether to use contraception", "88", "91", "86"],
          ["Which school a parent chooses for a child", "74", "72", "75"],
          ["Whether to refuse a recommended medical treatment", "81", "83", "80"],
          ["Whether to obtain an abortion", "52", "60", "47"]])

QUESTIONS = [
 dict(q="Read the following excerpt.\n\n“The enumeration in the Constitution, of certain rights, shall not be construed to deny or disparage others retained by the people.”\n—U.S. Constitution, Ninth Amendment\n\nWhich argument about constitutional rights does this text most directly support?",
   choices=[
     "That individuals hold protected rights beyond those listed in the first eight amendments",
     "That only the rights written into the Constitution may be enforced by a court",
     "That the states rather than the people retain any rights not listed",
     "That Congress may add rights to the Constitution by ordinary legislation",
     "That the rights listed in the Constitution may be denied when a majority wishes"], ans=0,
   why="EK 3.9.A.1 describes the Ninth Amendment as stating that individuals have protected rights beyond those listed in the first eight amendments, and names it as one of the two arguments offered for unenumerated rights."),

 dict(q="According to the course framework, what is an unenumerated right?",
   choices=[
     "A constitutionally protected right that is not explicitly listed in the Bill of Rights",
     "A right that a state constitution grants but the federal Constitution denies",
     "A right that Congress has created by statute",
     "A right that the Supreme Court has declined to protect",
     "A privilege that a government may withdraw at any time"], ans=0,
   why="EK 3.9.A.1 says the Supreme Court has recognized constitutionally protected rights that are not explicitly listed in the Bill of Rights and calls these unenumerated rights. The definition turns on absence from the text, not on the source of the protection."),

 dict(q="Which unenumerated right does EK 3.9.A.1 name?",
   choices=[
     "The right to privacy",
     "The right to bear arms",
     "The right to a speedy trial",
     "The right to petition the government",
     "The right to be free from unreasonable searches"], ans=0,
   why="EK 3.9.A.1 says 'these unenumerated rights include the right to privacy.' Each of the other four is written into the text of an amendment, which is what makes it enumerated rather than unenumerated."),

 dict(q="The course framework records two arguments that justices and scholars have made in defense of unenumerated rights. What are they?",
   choices=[
     "That such a right is implied by certain amendments which assume it exists, and that the Ninth Amendment supports rights beyond the first eight amendments",
     "That the Tenth Amendment reserves them to the states, and that the Supremacy Clause makes them binding",
     "That Congress has enacted them, and that the president has enforced them",
     "That international agreements guarantee them, and that state constitutions repeat them",
     "That the Preamble lists them, and that the Necessary and Proper Clause implies them"], ans=0,
   why="EK 3.9.A.1 gives exactly these two: implication from amendments that assume such rights exist, and the Ninth Amendment's statement about rights beyond the first eight. The framework's verbs are 'some argue' and 'others argue', so it records the debate rather than settling it."),

 dict(q="What is the reasoning behind the argument that an unenumerated right is IMPLIED by certain amendments?",
   choices=[
     "Those amendments are written as though the right already exists, so protecting them requires protecting it",
     "Those amendments were ratified after the Bill of Rights and therefore supersede it",
     "Those amendments explicitly name the right in a later section",
     "Those amendments were intended to apply only to the states",
     "Those amendments authorize Congress to create new rights by statute"], ans=0,
   why="EK 3.9.A.1's phrase is that the right is 'implied by certain amendments that assume the existence of such rights.' The argument is about what the text presupposes, which is why it does not require the right to appear anywhere in the text."),

 dict(q="A student claims that because a right is not written in the Constitution, no court may protect it. Which sentence of the course framework most directly answers the claim?",
   choices=[
     "That over time the Supreme Court has recognized constitutionally protected rights that are not explicitly listed in the Bill of Rights",
     "That the Fifth Amendment's due process clause applies to the national government",
     "That the exclusionary rule bars illegally seized evidence",
     "That the Miranda rule requires warnings before interrogation",
     "That procedural due process requires officials to use methods that are not arbitrary"], ans=0,
   why="EK 3.9.A.1 opens with exactly this recognition, which is the whole premise of the topic. The other four sentences all belong to topic 3.8 and concern procedure rather than the existence of an unwritten right."),

 dict(q="According to the course framework, what does the Supreme Court use substantive due process to examine?",
   choices=[
     "Whether government laws and actions are arbitrary infringements of individual rights",
     "Whether officials followed the procedures a statute prescribes",
     "Whether a defendant received notice of the charges against him",
     "Whether evidence was gathered under a valid warrant",
     "Whether a jury was drawn from a fair cross section of the community"], ans=0,
   why="EK 3.9.A.1 states this in exactly these words. The examination runs to the law or action itself, which is what makes the doctrine SUBSTANTIVE rather than procedural."),

 dict(q="What distinguishes substantive due process from procedural due process as the course framework defines the two?",
   choices=[
     "Substantive due process asks whether the law itself arbitrarily infringes a right, while procedural due process asks whether the methods officials used were arbitrary",
     "Substantive due process applies to states and procedural due process applies to the national government",
     "Substantive due process applies in criminal cases and procedural due process in civil ones",
     "Substantive due process was created by Congress and procedural due process by the Constitution",
     "The two are the same doctrine under different names"], ans=0,
   why="EK 3.9.A.1 aims substantive due process at whether laws and actions are arbitrary infringements; EK 3.8.A.2 aims procedural due process at whether officials' methods are arbitrary. Both clauses bind both governments, so the distinction is not about which government is acting."),

 dict(q="A state bans a private activity outright. Those challenging the ban do not dispute that the legislature followed every required step in enacting it; they argue instead that the ban itself invades a protected private choice. This challenge rests on",
   choices=[
     "substantive due process, because the objection is to what the law does rather than to how it was made",
     "procedural due process, because a legislature is a government body",
     "the exclusionary rule, because evidence would be needed to enforce the ban",
     "the Miranda rule, because enforcement would involve questioning",
     "the Establishment Clause, because a private activity is at issue"], ans=0,
   why="The challengers concede the procedure and attack the content, which is exactly the examination EK 3.9.A.1 assigns to substantive due process: whether the law is an arbitrary infringement of an individual right."),

 dict(q="An agency revokes a person's professional license without telling her what she is accused of and without letting her respond. She does not dispute the agency's authority to revoke licenses. Her claim rests on",
   choices=[
     "procedural due process, because the objection is to the methods used rather than to the agency's power",
     "substantive due process, because a license is valuable property",
     "substantive due process, because the agency acted rather than a legislature",
     "the Ninth Amendment, because licensing is not mentioned in the Constitution",
     "the equal protection clause, because other licensees were treated differently"], ans=0,
   why="EK 3.8.A.2's requirement is methods that are not arbitrary, and conceding the power while attacking the absence of notice and a hearing is a complaint about method. Nothing in the stem says another licensee was treated differently."),

 dict(q="Why can a government action satisfy procedural due process and still violate substantive due process?",
   choices=[
     "The two doctrines test different things, so a rule that is itself an arbitrary infringement is not rescued by being applied through fair procedures",
     "Procedural due process applies only in federal court",
     "Substantive due process applies only to laws passed before 1965",
     "A court may review only one due process claim in a case",
     "Procedural due process was superseded by substantive due process"], ans=0,
   why="EK 3.9.A.1 examines whether the law or action is an arbitrary infringement while EK 3.8.A.2 examines the methods, so passing one test says nothing about the other. This independence is why the framework treats them as separate topics with nearly identical titles."),

 dict(q="LO 3.9.A asks students to explain the EXTENT to which government is limited by substantive due process. Which feature of the framework's own treatment best explains why 'extent' rather than 'whether' is the right word?",
   choices=[
     "The framework says the actions protected by the right to privacy and substantive due process continue to be debated",
     "The framework says substantive due process applies only to criminal cases",
     "The framework says no government action has ever been struck down on this ground",
     "The framework says the doctrine binds only the national government",
     "The framework says the Ninth Amendment settles which rights are protected"], ans=0,
   why="EK 3.9.A.2 ends by saying the protected actions continue to be debated, so the boundary of the limitation is unsettled rather than absent. A doctrine whose scope is contested is measured by extent."),

 dict(q="According to the course framework, what did the Supreme Court do in Griswold v. Connecticut (1965)?",
   choices=[
     "Interpreted the due process clause to protect the right of privacy from government infringement",
     "Held that the Constitution does not confer a right to privacy",
     "Held that race-based school segregation violates the equal protection clause",
     "Established the principle of judicial review",
     "Held that political spending by organizations is protected speech"], ans=0,
   why="EK 3.9.A.2 states the Griswold holding in exactly these words, and it is the framework's own bridge from the abstract idea of an unenumerated right to a named constitutional protection."),

 dict(q="EK 3.9.A.2 introduces Griswold v. Connecticut with the observation that a right to privacy is not explicitly named in the Constitution. Why does that observation matter to the holding?",
   choices=[
     "It makes the privacy right an unenumerated one, so the Court had to locate it by interpretation rather than by reading a clause aloud",
     "It means the holding applied only to the state of Connecticut",
     "It means the holding rested on the Tenth Amendment",
     "It means Congress rather than the Court created the right",
     "It means the right was later added to the Constitution by amendment"], ans=0,
   why="EK 3.9.A.1 defines unenumerated rights as constitutionally protected rights not explicitly listed, and EK 3.9.A.2 places privacy in that category by saying it is not explicitly named. Interpretation of the due process clause is the route the framework records."),

 dict(q="According to the course framework, what did the Supreme Court hold in Roe v. Wade (1973)?",
   choices=[
     "That the application of substantive due process further extended the privacy right to abortion",
     "That the privacy right had no application beyond contraception",
     "That abortion regulation was committed to Congress rather than to the states",
     "That the Ninth Amendment alone supplied the right",
     "That the equal protection clause required states to permit abortion"], ans=0,
   why="EK 3.9.A.2 states the Roe holding in exactly these words. The framework's verb is EXTENDED, which places Roe as a continuation of the doctrine Griswold began rather than as a fresh start."),

 dict(q="According to the course framework, what did the Supreme Court hold in Dobbs v. Jackson Women's Health Organization (2022)?",
   choices=[
     "That the Constitution does not confer a right to abortion, leaving decisions about the regulation of abortion to legislatures",
     "That the Constitution requires states to permit abortion",
     "That the Constitution requires states to prohibit abortion",
     "That abortion regulation is committed exclusively to the federal courts",
     "That the right to privacy no longer exists in any form"], ans=0,
   why="EK 3.9.A.2 states the Dobbs holding in exactly these words, including where the decisions go afterwards. A holding that the Constitution does not confer a right is not a holding that the Constitution forbids or requires the practice."),

 dict(q="Under the course framework's statement of Dobbs, which institution decides how abortion is regulated?",
   choices=[
     "Legislatures",
     "The federal courts",
     "State governors acting alone",
     "The Department of Justice",
     "No institution, since the question is now beyond regulation"], ans=0,
   why="EK 3.9.A.2 says Dobbs left decisions about the regulation of abortion to legislatures. Where a constitutional right is held not to exist, the question returns to the ordinary lawmaking process."),

 dict(q="A student writes that Dobbs v. Jackson Women's Health Organization abolished the right to privacy. Which correction does the course framework support?",
   choices=[
     "The framework states only that Dobbs held the Constitution does not confer a right to abortion, and it separately says the protected actions continue to be debated",
     "The framework states that Dobbs expanded the right to privacy",
     "The framework states that Dobbs overturned Griswold v. Connecticut",
     "The framework states that Dobbs was decided on equal protection grounds",
     "The framework states that Dobbs returned the question to the federal courts"], ans=0,
   why="EK 3.9.A.2's sentence about Dobbs names Roe and the abortion right and goes no further, and its closing sentence keeps the scope of privacy open. Reading a holding for more than it says is the error the correction addresses."),

 dict(q="The sequence Griswold, then Roe, then Dobbs is best used as evidence for which claim in the course framework?",
   choices=[
     "That the actions protected by the right to privacy and substantive due process continue to be debated",
     "That the Supreme Court never revisits its own precedents",
     "That unenumerated rights are enforced only by statute",
     "That substantive due process has been abandoned by the Court",
     "That the Ninth Amendment has been repealed"], ans=0,
   why="EK 3.9.A.2 places the three decisions in order and then closes with exactly that sentence. A doctrine extended in one case and narrowed in another is the framework's own illustration of an unsettled boundary."),

 dict(q="In Brown v. Board of Education (1954), the Supreme Court held that race-based school segregation violates the equal protection clause of the Fourteenth Amendment. How does the constitutional basis of that holding differ from the basis of Griswold v. Connecticut?",
   choices=[
     "Brown rests on the equal protection clause and asks whether a group is treated unequally, while Griswold rests on the due process clause and asks whether a protected private choice is invaded",
     "Brown rests on the due process clause and Griswold on the equal protection clause",
     "Both rest on the Ninth Amendment",
     "Brown rests on the Establishment Clause and Griswold on the Free Exercise Clause",
     "Neither rests on the Fourteenth Amendment"], ans=0,
   why="The CED states the Brown holding under the equal protection clause and the Griswold holding under the due process clause. Both clauses sit in the Fourteenth Amendment's first section, which is why naming the amendment alone does not distinguish them."),

 dict(q="A non-required case: a state law forbids parents from sending their children to any school other than a public one, and parents challenge it as an arbitrary invasion of their authority over their children's upbringing rather than as unequal treatment. Which required or framework-named case does this challenge most closely resemble in its constitutional theory?",
   choices=[
     "Griswold v. Connecticut, because both argue that a law itself arbitrarily invades a protected private sphere under the due process clause",
     "Brown v. Board of Education, because both concern schools",
     "Gideon v. Wainwright, because both concern a state law",
     "Baker v. Carr, because both were heard in federal court",
     "McDonald v. Chicago, because both involve an unenumerated right"], ans=0,
   why="The theory rather than the subject matter is what makes cases comparable, and the stem's challengers attack the law's substance under due process, which is EK 3.9.A.1's substantive due process examination and the theory the framework attributes to Griswold. McDonald involves the Second Amendment, which is enumerated."),

 dict(q="A commentator argues that after Dobbs the Supreme Court can no longer strike down any state law as an arbitrary infringement of an individual right. Which observation about the course framework most directly weakens the argument?",
   choices=[
     "EK 3.9.A.1 states the substantive due process examination in the present tense and attaches it to a range of cases rather than to abortion alone",
     "EK 3.9.A.1 states that the Ninth Amendment was repealed",
     "EK 3.9.A.2 states that Dobbs applied only to federal law",
     "EK 3.8.A.4 states that the exclusionary rule was abolished",
     "EK 3.9.A.2 states that Griswold was decided after Dobbs"], ans=0,
   why="The framework describes substantive due process as a doctrine the Court has used in a range of cases to test whether laws are arbitrary infringements, which is broader than the single subject Dobbs addressed. A holding about one right does not retire the test."),

 dict(q="Which of the following is the best statement of what the course framework leaves unsettled about substantive due process?",
   choices=[
     "Which actions the right to privacy and substantive due process protect",
     "Whether the due process clauses exist",
     "Whether the Ninth Amendment is part of the Constitution",
     "Whether the Supreme Court may interpret the Constitution",
     "Whether procedural due process requires non-arbitrary methods"], ans=0,
   why="EK 3.9.A.2's final sentence is that the actions protected by the right to privacy and substantive due process continue to be debated. Each of the other four is stated flatly somewhere in the framework and is not in question."),

 dict(q=_CHALLENGES + " Which conclusion is best supported by the data?",
   table=_CHALLENGES_TABLE,
   choices=[
     "Challenges argued on procedural grounds alone were brought more than twice as often as challenges argued on substantive grounds alone",
     "Challenges argued on substantive grounds alone were the most numerous category",
     "Every category succeeded at the same rate",
     "No challenge in any category succeeded",
     "Challenges arguing both grounds together were the most numerous category"], ans=0,
   why="The table reports 260 procedural challenges against 120 substantive ones, which is more than double. Challenges arguing both grounds are the smallest category at 45."),

 dict(q=_CHALLENGES + " The substantive row of this table reports challenges of what kind, in the course framework's terms?",
   table=_CHALLENGES_TABLE,
   choices=[
     "Challenges asking whether a government law or action is an arbitrary infringement of an individual right",
     "Challenges asking whether officials gave notice and a hearing before acting",
     "Challenges asking whether evidence was lawfully seized",
     "Challenges asking whether a jury was impartial",
     "Challenges asking whether a statute was properly published"], ans=0,
   why="EK 3.9.A.1 defines the substantive examination in exactly these words. The four alternatives all describe complaints about method, which EK 3.8.A.2 assigns to procedural due process."),

 dict(q=_CHALLENGES + " A student concludes from the table that substantive due process is the route by which most constitutional challenges to this state's laws were argued. What is the most important correction?",
   table=_CHALLENGES_TABLE,
   choices=[
     "Substantive grounds alone account for 120 of the 425 challenges brought, so they are a minority of the total",
     "The table does not report how many challenges were brought",
     "The table reports only challenges that succeeded",
     "Substantive challenges succeeded more often than any other category",
     "The table covers a single challenge, so no comparison is possible"], ans=0,
   why="Adding the three rows gives 425 challenges, of which 120 were argued on substantive grounds alone, which is well under half. The success columns are a separate question from how often a ground was raised."),

 dict(q=_SURVEY + " Which conclusion is best supported by the data?",
   table=_SURVEY_TABLE,
   choices=[
     "The decision on which the two age groups differ most is also the decision with the least support among all adults",
     "The two age groups differ most on whether to use contraception",
     "Every decision draws more support from respondents under 40 than from older respondents",
     "A majority of all adults would deny protection to every decision listed",
     "The four decisions draw support within a few percentage points of one another"], ans=0,
   why="The age gap on abortion is 13 percentage points, the largest in the table, and its 52 percent among all adults is the lowest figure in that column. Support for a parent's choice of school is slightly higher among older respondents, and every figure in the all-adults column is above half."),

 dict(q=_SURVEY + " Which feature of the data is the best evidence for the framework's statement that the actions protected by the right to privacy continue to be debated?",
   table=_SURVEY_TABLE,
   choices=[
     "One decision draws support close to an even split and divides the two age groups more sharply than any other",
     "Every decision draws support from at least half of all adults",
     "The survey asked about four decisions rather than one",
     "Older respondents were more supportive than younger respondents on one item",
     "The survey reports whole percentages rather than fractions"], ans=0,
   why="EK 3.9.A.2 says the protected actions continue to be debated, and a debate shows up in data as a divided public rather than as a consensus. Abortion at 52 percent overall with a 13 point age gap is the divided item; near-universal support for contraception is the opposite pattern."),

 dict(q=_SURVEY + " A student concludes that the public treats all four decisions as equally private. What is the most important correction?",
   table=_SURVEY_TABLE,
   choices=[
     "Support among all adults ranges from 88 percent down to 52 percent, a spread of 36 percentage points",
     "The table reports figures for only one age group",
     "Support among all adults is identical for every decision",
     "The table reports no figure above half for any decision",
     "The survey covers a single respondent, so no share can be computed"], ans=0,
   why="The all-adults column runs from 88 percent for contraception to 52 percent for abortion, so the four items are not treated alike. A conclusion of equal treatment would require the column to be flat, and it is not."),

 dict(q="Which statement best captures how the course framework leaves the subject of this topic?",
   choices=[
     "A doctrine the Court has used in a range of cases, protecting at least one right the Constitution does not name, with the list of protected actions still contested",
     "A settled doctrine with a fixed list of protected actions",
     "A doctrine the Court has never applied",
     "A doctrine that protects only rights explicitly listed in the Bill of Rights",
     "A doctrine created by Congress and enforceable only by statute"], ans=0,
   why="EK 3.9.A.1 records the recognition of unenumerated rights and the substantive due process examination across a range of cases, and EK 3.9.A.2 closes by saying the protected actions continue to be debated. Reading the topic as settled in either direction contradicts that closing sentence."),
]
