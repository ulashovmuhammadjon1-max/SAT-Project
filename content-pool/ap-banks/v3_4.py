# AP U.S. GOVERNMENT AND POLITICS 3.4 First Amendment: Freedom of the Press -- 30 questions
# CED V.1 (c) 2026, Unit 3 Civil Liberties and Civil Rights.
# Learning objective 3.4.A: explain THE EXTENT TO WHICH the Supreme Court's
# interpretation of the First Amendment reflects a commitment to individual
# liberty.
# Suggested skill for this topic (CED p. 85): 4.D, explain how the VISUAL
# ELEMENTS of a source -- a cartoon, map, or infographic -- illustrate or relate
# to political principles, institutions, processes, policies and behaviors.
#
# Essential knowledge relied on. ONE sentence, and every word of it is load
# bearing:
#   EK 3.4.A.1 -- "The Supreme Court BOLSTERED the freedom of the press,
#     affirming support for a HEAVY PRESUMPTION AGAINST PRIOR RESTRAINT EVEN IN
#     CASES INVOLVING NATIONAL SECURITY."
#
# THREE THINGS IN THAT SENTENCE, AND THE MODULE IS BUILT ON ALL THREE:
#   1. PRIOR RESTRAINT is the specific thing presumed against -- government
#      stopping publication BEFORE it happens. It is not the same as punishing
#      what has been published, and the distinction is the whole doctrine.
#      Items 1 to 8 turn on it, because a student who thinks the case protects
#      the press from all consequences has learned something false.
#   2. A HEAVY PRESUMPTION is not a prohibition. The framework's word is
#      presumption, which means the government may still try and will usually
#      fail. Items 9 to 14 keep the claim at that strength; a bank that upgrades
#      it to an absolute bar makes the exam's own hedge unanswerable.
#   3. "EVEN IN CASES INVOLVING NATIONAL SECURITY" is the clause that gives the
#      holding its force, because national security is the strongest interest a
#      government can assert. Items 15 to 20 turn on it.
#
# WHY THIS TOPIC HAS A SEPARATE CODE FROM 3.3, which matters when deciding what
# belongs here: 3.3 is the SPEECH topic and owns symbolic speech, time place and
# manner, obscenity, defamation and the danger standard. 3.4 is the PRESS topic
# and owns exactly one holding. No item here re-tests a 3.3 category, and the
# defamation items that would fit both live in 3.3 where the framework puts them.
#
# ON SKILL 4.D: the CED's visual sources are cartoons, maps and infographics.
# This bank cannot ship a cartoon, so the two stimuli here are infographic-style
# tables whose items ask what the ARRANGEMENT shows -- which quantity is being
# compared with which, what the ordering implies, what a reader would wrongly
# infer from the layout. That is the part of 4.D a table can carry honestly.
#
# Documents the CED attaches to 3.4.A (p. 26-27): "Letter from a Birmingham
# Jail."
# Required cases the CED attaches to 3.4.A (p. 32-33): New York Times Co. v.
# United States.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the First Amendment and "Letter from a
# Birmingham Jail" are quoted verbatim. Non-required cases are described and
# never named. Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("3.4", "First Amendment: Freedom of the Press", 3)

_ATTEMPTS = ("The infographic below arranges, in a hypothetical study, every government "
             "attempt over one decade to stop a publication before it appeared, grouped by "
             "the interest the government asserted.")
_ATTEMPTS_TABLE = dict(
    headers=["Interest asserted by the government", "Attempts to block publication", "Attempts that succeeded"],
    rows=[["National security", "23", "2"],
          ["Protecting an ongoing trial", "31", "7"],
          ["Protecting a person's reputation", "44", "1"],
          ["Preventing embarrassment to an agency", "12", "0"]])

_TIMING = ("The infographic below arranges, in a hypothetical legal system, the actions "
           "available to a government that objects to a publication, by whether the action "
           "comes before or after the material appears.")
_TIMING_TABLE = dict(
    headers=["Action", "Before or after publication", "Presumption the government must overcome"],
    rows=[["Court order forbidding publication", "Before", "Heavy"],
          ["Seizing copies before distribution", "Before", "Heavy"],
          ["Prosecution for what was published", "After", "Ordinary"],
          ["Civil suit for reputational harm", "After", "Ordinary"]])

QUESTIONS = [
 dict(q="According to the course framework, what did the Supreme Court affirm support for?",
   choices=[
     "A heavy presumption against prior restraint, even in cases involving national security",
     "An absolute prohibition on any government action against a publication",
     "A rule permitting the government to stop publication whenever it claims a security interest",
     "A requirement that publications be approved by a court before release",
     "A rule that the press may be sued but never prosecuted"], ans=0,
   why="EK 3.4.A.1 states this in exactly these words. Note that the framework says PRESUMPTION rather than prohibition, which is why the second option overstates it."),

 dict(q="What is prior restraint?",
   choices=[
     "Government action stopping material from being published in the first place",
     "Government punishment imposed after material has been published",
     "A newspaper's decision not to run a story",
     "A court's award of damages for a false statement",
     "A statute limiting how many newspapers one owner may hold"], ans=0,
   why="The word PRIOR is the whole of it: the restraint operates before publication. EK 3.4.A.1's presumption runs against that specific move, not against every consequence a publisher may face."),

 dict(q="Why does the framework's doctrine single out restraint BEFORE publication rather than punishment after?",
   choices=[
     "Material never published cannot be evaluated by anyone, so a mistaken restraint is invisible while a mistaken punishment is at least visible",
     "Punishment after publication is unconstitutional in every case",
     "Restraint before publication is easier for a court to review",
     "Punishment after publication is imposed by the press rather than by the government",
     "The First Amendment mentions prior restraint by name"], ans=0,
   why="A suppressed publication leaves nothing for the public to weigh, which is why the presumption is heaviest at that stage. The First Amendment's text does not use the phrase; the doctrine is interpretive."),

 dict(q="A government agency sues a publisher after an article appears, seeking damages for what the article said. Does EK 3.4.A.1's heavy presumption apply?",
   choices=[
     "No, because the action comes after publication and is therefore not a prior restraint",
     "Yes, because any government action against a publisher is a prior restraint",
     "Yes, because the agency is part of the government",
     "No, because the First Amendment does not apply to publishers",
     "No, because damages actions are always unconstitutional"], ans=0,
   why="EK 3.4.A.1's presumption is against PRIOR restraint, and the timing is what places an action inside or outside it. A suit after publication is subject to ordinary rules, which does not mean it must succeed."),

 dict(q="A court orders a newspaper not to publish a story it has already written. Which doctrine does the order implicate?",
   choices=[
     "The heavy presumption against prior restraint, since the order stops publication before it occurs",
     "The clear and present danger standard, since the story may be dangerous",
     "Protections against defamation, since the story concerns a person",
     "Time, place, and manner regulation, since the order concerns when the story appears",
     "The Establishment Clause, since a court is involved"], ans=0,
   why="A judicial order forbidding publication is the paradigm prior restraint, which is what EK 3.4.A.1's presumption governs. The other options name EK 3.3's speech categories, which this topic does not own."),

 dict(q="What does calling the presumption HEAVY rather than absolute mean in practice?",
   choices=[
     "The government may still seek a prior restraint and will usually fail, rather than being barred from trying",
     "The government may obtain a prior restraint whenever it asks",
     "The government is prohibited from ever seeking a prior restraint",
     "The presumption applies only to newspapers and not to other publishers",
     "The presumption applies only when national security is not involved"], ans=0,
   why="EK 3.4.A.1's word is PRESUMPTION, which is a burden rather than a bar. Reading it as absolute makes LO 3.4.A's question about the EXTENT of the commitment unanswerable."),

 dict(q="Why does the framework's phrase 'even in cases involving national security' strengthen the holding rather than weaken it?",
   choices=[
     "National security is the strongest interest a government can assert, so a presumption that survives it is strong everywhere else too",
     "National security cases are rare, so the phrase has little effect",
     "It creates an exception for national security cases",
     "It limits the presumption to national security cases",
     "It transfers national security cases to military courts"], ans=0,
   why="The clause is an a fortiori argument: if the presumption holds against the government's best claim, it holds against weaker ones. Reading it as an exception inverts the sentence."),

 dict(q="In New York Times Co. v. United States (1971), the Supreme Court bolstered freedom of the press, establishing a heavy presumption against prior restraint even in cases involving national security. Which statement of the holding is accurate?",
   choices=[
     "The government bore a heavy burden to justify stopping publication and did not meet it",
     "The government may never take any action against a publisher",
     "The government may stop publication whenever national security is asserted",
     "The Court declined to decide the case",
     "The Court held that the material could be published only after a delay"], ans=0,
   why="The CED's own statement of the holding is a heavy presumption AGAINST prior restraint, which places the burden on the government. Neither an absolute bar nor a security exception is what the framework records."),

 dict(q="A non-required case: a government agency asks a court to stop a magazine from publishing documents the agency says would endanger an operation abroad. Which required case is the closest comparison, and why?",
   choices=[
     "New York Times Co. v. United States (1971), because it also involved a request to stop publication on national security grounds",
     "Schenck v. United States (1919), because it also involved speech during wartime",
     "Tinker v. Des Moines (1969), because it also involved symbolic expression",
     "Engel v. Vitale (1962), because it also involved a government policy",
     "Gideon v. Wainwright (1963), because it also involved a right of the accused"], ans=0,
   why="The facts match on both dimensions the doctrine cares about: the government seeks to stop publication BEFORE it occurs, and it asserts national security. Schenck concerns punishment for speech already uttered."),

 dict(q="How does the press freedom in EK 3.4.A.1 relate to the accountability of government?",
   choices=[
     "A press that can publish without prior approval can report what officials would prefer to conceal",
     "The press has a constitutional duty to support the government's position",
     "The press may publish only material the government has verified",
     "The press has no role in holding officials accountable",
     "The press may be compelled to publish government statements"], ans=0,
   why="LO 3.4.A ties the interpretation to a commitment to individual liberty, and the practical consequence of no prior approval is that officials cannot decide in advance what the public learns."),

 dict(q="Read the following excerpt.\n\n“Congress shall make no law... abridging the freedom of speech, or of the press.”\n—U.S. Constitution, First Amendment\n\nWhat does the framework's account add to this text?",
   choices=[
     "It identifies a specific form of abridgement, restraint before publication, against which the Court has set a heavy presumption",
     "It replaces the text with a rule that the press may never be regulated",
     "It limits the text to newspapers printed on paper",
     "It states that the clause applies only to Congress and not to other government actors",
     "It says the clause has no application when national security is asserted"], ans=0,
   why="The text forbids abridgement in general terms, and EK 3.4.A.1 records the Court identifying prior restraint as the form most strongly presumed against. The framework's clause about national security runs the opposite way from the fifth option."),

 dict(q="Which of the following is NOT a prior restraint?",
   choices=[
     "A criminal prosecution brought after an article appears",
     "A court order forbidding a broadcast scheduled for tomorrow",
     "A statute requiring government approval before a book may be sold",
     "An injunction stopping a newspaper from printing documents",
     "A licensing scheme under which publications must be cleared in advance"], ans=0,
   why="Four of the five operate before material reaches the public, which is what makes them prior restraints. A prosecution after publication is subsequent punishment, subject to ordinary rules rather than to EK 3.4.A.1's heavy presumption."),

 dict(q="Which observation would most strengthen a claim that the presumption against prior restraint is doing real work?",
   choices=[
     "Government requests to block publication are made and almost always denied, including when security is asserted",
     "Governments rarely object to what is published",
     "Publishers rarely print material governments dislike",
     "Courts hear few cases involving the press",
     "Publications are widely available in many formats"], ans=0,
   why="A presumption is doing work when the government tries and loses, which is why the evidence must include attempts as well as outcomes. Rarity of conflict is consistent with a strong presumption and with a timid press equally."),

 dict(q="Which observation would most WEAKEN a claim that press freedom in practice matches EK 3.4.A.1's protection?",
   choices=[
     "Publishers routinely withhold material because they anticipate litigation, so the restraint operates without any court order",
     "Some publications are more widely read than others",
     "Courts occasionally rule against publishers in defamation suits",
     "The government sometimes declines to seek a restraint",
     "Publishers employ lawyers to review material before publication"], ans=0,
   why="EK 3.4.A.1 constrains what the government may do, so the strongest rebuttal is a mechanism that suppresses publication without government action at all. Losing a defamation suit is a consequence the framework's presumption never covered."),

 dict(q="Read the following excerpt.\n\n“Injustice anywhere is a threat to justice everywhere.”\n—Martin Luther King, Jr., “Letter from a Birmingham Jail,” 1963\n\nHow does a free press bear on the claim in this sentence?",
   choices=[
     "If injustice in one place concerns everyone, then the ability to report it beyond that place is what makes the concern possible",
     "It shows that the press should report only local matters",
     "It shows that the press should be licensed to ensure accuracy",
     "It shows that injustice is a matter for courts rather than for publication",
     "It shows that the press has no role in matters of justice"], ans=0,
   why="The Letter's claim depends on people elsewhere learning what happened, and a press that publishes without prior approval is the mechanism. The CED attaches the Letter to 3.4.A."),

 dict(q="A government argues that a publication should be stopped because it would embarrass an agency. Under EK 3.4.A.1's standard, how should that argument fare?",
   choices=[
     "It should fail easily, since embarrassment is a far weaker interest than the national security claim the presumption already survives",
     "It should succeed, since agencies are entitled to protect their reputations",
     "It should succeed, since the government has asserted an interest",
     "The standard does not apply, since no security claim was made",
     "The standard does not apply, since the material has not yet been published"], ans=0,
   why="EK 3.4.A.1's clause about national security is an a fortiori: a presumption that holds against the strongest interest holds a fortiori against a weaker one. The fifth option describes the exact circumstance in which the standard DOES apply."),

 dict(q="LO 3.4.A asks about the extent to which the Court's interpretation reflects a commitment to INDIVIDUAL LIBERTY. How does a press protection serve individual liberty?",
   choices=[
     "It protects both the publisher's liberty to publish and the public's ability to learn what government does",
     "It protects only the financial interests of publishing companies",
     "It protects the government's ability to control information",
     "It protects individuals from ever being written about",
     "It protects only individuals who own a publication"], ans=0,
   why="LO 3.4.A frames the press interpretation as a commitment to individual liberty, and the liberty runs in two directions: the publisher's and the reader's. The fourth option describes the opposite of a press freedom."),

 dict(q="Which tension does a strong presumption against prior restraint create?",
   choices=[
     "Material that genuinely would cause harm may be published, since the harm cannot be prevented in advance",
     "Publishers may be sued for what they print, which the presumption forbids",
     "Governments may not respond to publications in any way",
     "Courts must approve every publication before it appears",
     "There is no tension, since publication never causes harm"], ans=0,
   why="The cost of a presumption against advance suppression is that some harmful material gets out, which is the balance EK 3.3.A.2 calls the effort to reconcile social order and individual freedom. Suits after publication are unaffected."),

 dict(q="Which of the following best distinguishes this topic's holding from the speech doctrines in topic 3.3?",
   choices=[
     "This topic concerns WHEN the government may act against expression; the speech categories concern WHAT KIND of expression may be limited",
     "This topic concerns speech and 3.3 concerns the press",
     "This topic concerns symbolic expression and 3.3 concerns written expression",
     "This topic concerns state governments and 3.3 concerns Congress",
     "There is no distinction; the two topics state the same rule"], ans=0,
   why="EK 3.4.A.1 is about restraint BEFORE publication -- a question of timing -- while EK 3.3.A.2's four categories sort expression by type. The two axes are independent, which is why the framework gives them separate codes."),

 dict(q="A publisher argues that a licensing scheme requiring advance approval is unconstitutional even though approval is almost always granted. Which reasoning best supports the argument?",
   choices=[
     "A scheme requiring approval is a prior restraint whatever its approval rate, because the government still decides in advance what may appear",
     "The scheme is unconstitutional only if approval is frequently denied",
     "The scheme is constitutional because approval is usually granted",
     "The scheme concerns speech rather than the press",
     "The scheme is a time, place and manner regulation"], ans=0,
   why="EK 3.4.A.1's presumption attaches to the STRUCTURE of advance approval rather than to how often it is exercised, because the power to decide in advance is itself the restraint."),

 dict(q=_ATTEMPTS + " Which conclusion is best supported by the infographic?",
   table=_ATTEMPTS_TABLE,
   choices=[
     "Attempts to block publication succeeded in a small minority of cases under every interest asserted",
     "Attempts succeeded in a majority of cases under every interest asserted",
     "National security was the interest most often asserted",
     "Attempts asserting embarrassment succeeded more often than those asserting national security",
     "Every attempt to block publication failed"], ans=0,
   why="The four success rates are 2 of 23, 7 of 31, 1 of 44 and 0 of 12, all well under half. Reputation is the most frequently asserted interest at 44, and embarrassment succeeded no times at all."),

 dict(q=_ATTEMPTS + " What does the ARRANGEMENT of this infographic invite a reader to compare, and what would that comparison miss?",
   table=_ATTEMPTS_TABLE,
   choices=[
     "It invites comparison of success rates across asserted interests, and it misses that every row concerns attempts made before publication, so none of it speaks to what happens afterward",
     "It invites comparison of publications by size, and it misses their subject matter",
     "It invites comparison across years, and it misses the interests asserted",
     "It invites comparison of publishers, and it misses the government's role",
     "It invites no comparison at all, since it reports a single figure"], ans=0,
   why="Skill 4.D asks what a visual's arrangement does. Grouping by asserted interest puts the interests side by side, and the whole table is confined to EK 3.4.A.1's prior restraints, so subsequent punishment is outside it entirely."),

 dict(q=_ATTEMPTS + " Which claim from the course framework do these data most directly illustrate?",
   table=_ATTEMPTS_TABLE,
   choices=[
     "That a heavy presumption operates against prior restraint even where national security is asserted",
     "That the press may never be sued for what it publishes",
     "That obscene communication may be limited",
     "That symbolic speech is protected by the First Amendment",
     "That time, place and manner regulations are permissible"], ans=0,
   why="Two successes in twenty-three national security attempts is EK 3.4.A.1's presumption surviving the government's strongest claim. The other options name EK 3.3 categories the table does not report."),

 dict(q=_TIMING + " Which conclusion is best supported by the infographic?",
   table=_TIMING_TABLE,
   choices=[
     "The two actions taken before publication face a heavy presumption, and the two taken afterward face an ordinary one",
     "All four actions face a heavy presumption",
     "All four actions face an ordinary presumption",
     "The actions taken after publication face the heavier burden",
     "The presumption does not depend on when the action is taken"], ans=0,
   why="The two Before rows read Heavy and the two After rows read Ordinary, which is EK 3.4.A.1's doctrine arranged as a table: the timing determines the burden."),

 dict(q=_TIMING + " How does the ARRANGEMENT of this infographic make the doctrine visible?",
   table=_TIMING_TABLE,
   choices=[
     "Sorting the actions by timing puts the two burdens in adjacent blocks, which shows that the burden follows the timing rather than the severity of the action",
     "Sorting by severity shows that harsher actions face heavier burdens",
     "Sorting alphabetically shows that the order has no meaning",
     "Sorting by publisher shows which outlets are most affected",
     "The arrangement conceals the relationship between timing and burden"], ans=0,
   why="Skill 4.D asks what the visual's organisation does. Grouping by Before and After makes the burden column constant within each group, which is the doctrinal point EK 3.4.A.1 states in prose."),

 dict(q=_TIMING + " A reader concludes from the infographic that the two actions taken after publication are constitutionally unproblematic. What is the most important correction?",
   table=_TIMING_TABLE,
   choices=[
     "An ordinary presumption is still a burden the government must carry, so those actions may fail on their own terms",
     "Those actions are in fact prior restraints",
     "Those actions face a heavier burden than the ones taken before publication",
     "The table shows that no action after publication is ever permitted",
     "The table shows that all four actions are identical"], ans=0,
   why="The column reads Ordinary rather than None, and a defamation suit or a prosecution can fail for many reasons. Reading a lighter burden as no burden is the misreading the arrangement invites."),

 dict(q="A student writes that New York Times Co. v. United States means the press can publish anything without consequence. What is the correction?",
   choices=[
     "The case concerns stopping publication in advance; a publisher may still face suits or prosecution for what it publishes",
     "The case concerns suits after publication rather than restraint before it",
     "The student is right, since the First Amendment is absolute",
     "The case applies only to newspapers and not to broadcasters",
     "The case was overruled by a later constitutional amendment"], ans=0,
   why="EK 3.4.A.1's presumption is specifically against PRIOR restraint. Collapsing it into immunity from all consequences is the most common error about this holding and is what makes item 12 necessary."),

 dict(q="LO 3.4.A asks about the extent of the Court's commitment to individual liberty in this area. Which answer is best supported by the framework?",
   choices=[
     "The commitment is strong on the specific question of advance suppression, and the framework says nothing about immunity from later consequences",
     "The commitment is absolute across every question involving the press",
     "There is no commitment, since the framework records only one holding",
     "The commitment applies only when national security is not asserted",
     "The extent cannot be assessed, since the framework takes no position"], ans=0,
   why="EK 3.4.A.1 is a single, narrow and strong statement: heavy presumption, prior restraint, even in security cases. Reading more into it or less both misstate a sentence that is precise about what it covers."),

 dict(q="Which question would best test whether the presumption described in EK 3.4.A.1 is being honored in a given period?",
   choices=[
     "When the government sought to stop a publication in advance, how often did it succeed, and on what interests did it rely?",
     "How many publications appeared during the period?",
     "How many people read the average publication?",
     "How many lawyers each publisher employed",
     "How many press conferences officials held"], ans=0,
   why="EK 3.4.A.1's claim is about the government's success rate when it seeks a prior restraint, so the test must count attempts and outcomes. Circulation and staffing measure the industry rather than the doctrine."),

 dict(q="Why does the framework treat this single holding as worth its own topic code?",
   choices=[
     "It settles a distinct question -- whether government may act before publication -- that the speech categories in 3.3 do not address",
     "It is the only First Amendment holding the Court has issued",
     "It applies to more people than the speech doctrines do",
     "It concerns state governments while 3.3 concerns Congress",
     "It replaced the speech doctrines in 3.3"], ans=0,
   why="EK 3.3.A.2 sorts expression by TYPE and EK 3.4.A.1 sorts government action by TIMING, so the two answer different questions and neither subsumes the other."),
]
