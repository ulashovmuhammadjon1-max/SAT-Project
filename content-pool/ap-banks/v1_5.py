# AP U.S. GOVERNMENT AND POLITICS 1.5 Ratification of the U.S. Constitution -- 30 questions
# CED V.1 (c) 2026, Unit 1 Foundations of American Democracy.
# Learning objective 1.5.A: explain the impact of political negotiation and
# compromise at the Constitutional Convention on the development of the
# constitutional system.
#
# Essential knowledge relied on:
#   EK 1.5.A.1 -- a CLOSED list of five compromises "deemed necessary for
#     ratification," each with the CED's own gloss:
#       i.   Great (Connecticut) Compromise -- "created a dual (bicameral)
#            system of congressional representation with the House of
#            Representatives based on each state's population and the Senate
#            representing each state equally"
#       ii.  Electoral College -- "created a system for electing the president
#            by electors from each state rather than by popular vote or by
#            congressional vote"
#       iii. Three-Fifths Compromise -- "provided a formula for calculating a
#            state's enslaved population for purposes of representation in the
#            House and for taxation"
#       iv.  "Postponing until 1808 a decision whether to ban the importation
#            of enslaved persons"
#       v.   "Agreement to add a Bill of Rights to address concerns of the
#            Anti-Federalists"
#   EK 1.5.A.2 -- Article V: proposal by "either a two-thirds vote in both
#     houses or a proposal from two-thirds of the state legislatures, with final
#     ratification determined by three-fourths of the states."
#   EK 1.5.A.3 -- the compromises "left some matters unresolved that continue to
#     generate discussion and debate today."
#   EK 1.5.A.4 -- that debate over national power, state power and individual
#     rights is "at the heart of present-day constitutional issues," represented
#     by (i) debates about government surveillance after the September 2001
#     attacks and (ii) debates about the role of government in public school
#     education.
#
# TWO THINGS THIS MODULE IS DELIBERATELY CAREFUL ABOUT
#
# 1. The Three-Fifths Compromise is a formula for REPRESENTATION AND TAXATION,
#    which is the CED's own wording, and it is not a statement about anyone's
#    humanity. Items 8 and 9 ask what the formula did and whom it advantaged;
#    none of them asks a student to evaluate it as arithmetic in the abstract.
# 2. EK 1.5.A.4's first illustration is written here as "the September 2001
#    attacks," never as the numeric shorthand. export_units.py runs every string
#    through mathfmt.convert, which reads a slash between digits as a fraction,
#    so the usual abbreviation would ship to students as typeset arithmetic.
#    The same reason the Units 3 to 5 checker bans a hyphen between two digits.
#
# Documents the CED attaches to 1.5.A (p. 26): the Articles of Confederation,
# the Emancipation Proclamation, Federalist No. 39, Federalist No. 51.
# Required cases the CED attaches to 1.5.A (p. 31-32): McCulloch v. Maryland,
# Schenck v. United States, Tinker v. Des Moines, United States v. Lopez.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: Federalist No. 39, Federalist No. 51,
# the Emancipation Proclamation and the Constitution's own text are quoted
# verbatim. The apportionment figures in items 21 to 23 are not estimates -- they
# are the numbers written into Article I Section 2 (House) and Article I Section 3
# (Senate) of the Constitution itself.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("1.5", "Ratification of the U.S. Constitution", 1)

_SEATS = ("Article I Section 2 of the Constitution fixed each state's representation in the "
          "first House of Representatives, and Article I Section 3 gave every state two "
          "senators. The table reports those figures for five states.")
_SEATS_TABLE = dict(
    headers=["State", "Seats in the first House", "Seats in the Senate"],
    rows=[["Virginia", "10", "2"],
          ["Pennsylvania", "8", "2"],
          ["New York", "6", "2"],
          ["Delaware", "1", "2"],
          ["Rhode Island", "1", "2"]])

_AMEND = ("The table reports the recorded support for a hypothetical proposed constitutional "
          "amendment at each stage of the Article V process.")
_AMEND_TABLE = dict(
    headers=["Stage", "In favor", "Total possible"],
    rows=[["House of Representatives", "290", "435"],
          ["Senate", "68", "100"],
          ["State legislatures ratifying", "34", "50"]])

QUESTIONS = [
 dict(q="Which compromise at the Constitutional Convention created a legislature in which one chamber represents states by population and the other represents them equally?",
   choices=[
     "The Great Compromise, also called the Connecticut Compromise",
     "The Three-Fifths Compromise",
     "The agreement postponing a decision on the importation of enslaved persons",
     "The agreement to add a Bill of Rights",
     "The creation of the Electoral College"], ans=0,
   why="EK 1.5.A.1.i describes the Great (Connecticut) Compromise as creating a dual bicameral system with the House based on each state's population and the Senate representing each state equally."),

 dict(q="A delegate from a small state refuses to accept a legislature apportioned entirely by population, and a delegate from a large state refuses one in which every state has an equal vote. The settlement they reach illustrates which general point about the Convention?",
   choices=[
     "The constitutional system took the shape it did because neither side could impose its preference, so both were built into the same institution",
     "The Convention resolved disputes by majority vote of the delegates without negotiation",
     "The large states prevailed on every contested question of representation",
     "The small states prevailed on every contested question of representation",
     "The dispute was left entirely to the state ratifying conventions to settle"], ans=0,
   why="EK 1.5.A.1 frames the compromises as deemed necessary for ratification, which means the design followed from what each side could refuse. A bicameral legislature carrying both principles at once is that logic made into an institution."),

 dict(q="According to the course framework, the Electoral College was created as a compromise because it established a system for electing the president",
   choices=[
     "by electors from each state, rather than by popular vote or by congressional vote",
     "by the House of Representatives voting as states",
     "by direct popular vote in every state simultaneously",
     "by the Senate with the advice of state governors",
     "by the state legislatures voting in a single national session"], ans=0,
   why="EK 1.5.A.1.ii names the two alternatives the Electoral College was chosen over: election by popular vote and election by Congress. Selection by electors from each state is the middle course the delegates settled on."),

 dict(q="Which argument would a delegate at the Convention most plausibly have made in favor of the Electoral College and against direct popular election of the president?",
   choices=[
     "That a body of electors chosen state by state would keep the choice from turning on the popularity of one candidate in the largest states alone",
     "That a president chosen by electors could be removed by them at any time",
     "That electors would be appointed by the Supreme Court and therefore be impartial",
     "That direct election would give the small states more influence than the large ones",
     "That the Constitution forbids the states from participating in the selection of the president"], ans=0,
   why="The compromise's logic is the same as the Great Compromise's: distribute the decision across states so that no bloc of large states decides alone. The fourth option reverses the effect, since direct election favors population."),

 dict(q="The Three-Fifths Compromise provided a formula that affected which two things?",
   choices=[
     "Representation in the House of Representatives and taxation",
     "Representation in the Senate and the selection of judges",
     "The admission of new states and the regulation of commerce",
     "The election of the president and the ratification of treaties",
     "The amendment process and the militia"], ans=0,
   why="EK 1.5.A.1.iii states the formula's two purposes as representation in the House and taxation. It had no bearing on the Senate, where representation is equal regardless of population."),

 dict(q="Which states gained the most from counting part of the enslaved population toward apportionment in the House of Representatives?",
   choices=[
     "States with large enslaved populations, whose representation exceeded what their free population alone would have supported",
     "States with small populations of any kind, since apportionment gave every state at least one seat",
     "States that had already abolished slavery, since the formula applied only to free residents",
     "Every state equally, since the formula applied uniformly across the union",
     "No state, since the formula affected taxation but not representation"], ans=0,
   why="A formula that adds part of a population to the apportionment base raises the seat count of the states holding that population. The last option contradicts EK 1.5.A.1.iii, which names representation in the House as one of the formula's two purposes."),

 dict(q="The Convention agreed to postpone until 1808 any decision about banning the importation of enslaved persons. What does this agreement best illustrate about the Convention?",
   choices=[
     "Some disputes were not resolved at all but deferred, so that ratification could proceed",
     "The delegates had reached agreement on the question and merely delayed announcing it",
     "The delegates had no authority to legislate about commerce of any kind",
     "The question was referred to the Supreme Court for decision at a later date",
     "The Articles of Confederation had already settled the question"], ans=0,
   why="EK 1.5.A.1.iv describes the item as postponing a decision, not making one, which is the clearest case of EK 1.5.A.3's point that the compromises left matters unresolved. No court existed to refer it to when the Convention met."),

 dict(q="Which compromise responded directly to Anti-Federalist objections raised during the ratification debate rather than to a dispute among the delegates at Philadelphia?",
   choices=[
     "The agreement to add a Bill of Rights",
     "The Great Compromise on congressional representation",
     "The Three-Fifths Compromise",
     "The Electoral College",
     "The postponement of a decision on the importation of enslaved persons"], ans=0,
   why="EK 1.5.A.1.v names the agreement to add a Bill of Rights as addressing concerns of the Anti-Federalists, who were the opponents of ratification rather than parties to the Convention's internal bargains."),

 dict(q="According to Article V of the Constitution, an amendment may be proposed by",
   choices=[
     "a two-thirds vote in both houses of Congress or a proposal from two-thirds of the state legislatures",
     "a majority vote in both houses of Congress alone",
     "the president with the concurrence of the Supreme Court",
     "three-fourths of the state legislatures acting without Congress",
     "a unanimous vote of the state legislatures"], ans=0,
   why="EK 1.5.A.2 states the two proposal routes in exactly these terms. Three-fourths is the RATIFICATION threshold, not the proposal threshold, which is the confusion the fourth option is built on."),

 dict(q="Final ratification of a proposed constitutional amendment requires the approval of",
   choices=[
     "three-fourths of the states",
     "two-thirds of the states",
     "a majority of the states",
     "every state",
     "three-fourths of the members of Congress"], ans=0,
   why="EK 1.5.A.2 sets final ratification at three-fourths of the states. Unanimity was the Articles of Confederation's rule under Article XIII and is precisely what Article V was written to replace."),

 dict(q="Compared with the amendment provision of the Articles of Confederation, Article V of the Constitution",
   choices=[
     "lowered the bar from unanimity to three-fourths, making change difficult but possible",
     "raised the bar from a simple majority to three-fourths",
     "left the requirement unchanged at unanimity",
     "removed the states from the amendment process entirely",
     "gave Congress the power to amend the document by itself"], ans=0,
   why="Article XIII of the Articles required confirmation by the legislatures of every state; EK 1.5.A.2 sets the Constitution's threshold at three-fourths. That change is the difference between a document one state can freeze and one a broad supermajority can revise."),

 dict(q="Read the following excerpt.\n\n“We may define a republic to be, or at least may bestow that name on, a government which derives all its powers directly or indirectly from the great body of the people, and is administered by persons holding their offices during pleasure, for a limited period, or during good behavior.”\n—James Madison, Federalist No. 39, 1788\n\nMadison offers this definition in order to",
   choices=[
     "show that the proposed government meets the standard of a republic even though its officers are chosen in different ways",
     "argue that only officials elected directly by the people may hold power",
     "establish that judges must be elected to fixed terms like legislators",
     "demonstrate that the proposed government is a pure democracy",
     "show that the Articles of Confederation already satisfied republican principles"], ans=0,
   why="The definition is written broadly enough to cover direct election, indirect election and tenure during good behavior, which is what the proposed Constitution actually contains. Reading it as a demand for direct election of everyone inverts its purpose."),

 dict(q="Read the following excerpt.\n\n“The proposed Constitution, therefore, is, in strictness, neither a national nor a federal Constitution, but a composition of both.”\n—James Madison, Federalist No. 39, 1788\n\nWhich feature of the ratified Constitution best illustrates the claim in this sentence?",
   choices=[
     "The House is apportioned by population while the Senate represents states equally",
     "The president is chosen by the House of Representatives",
     "Federal judges are appointed by the state legislatures",
     "Amendments may be adopted by Congress without the states",
     "The states may nullify acts of Congress within their own borders"], ans=0,
   why="EK 1.7.A.1 credits Federalist No. 39 with explaining that the division of authority combines national and state features, and the two chambers of Congress are that combination inside one institution. The other four options describe arrangements the Constitution does not contain."),

 dict(q="Read the following excerpt.\n\n“Ambition must be made to counteract ambition. The interest of the man must be connected with the constitutional rights of the place.”\n—James Madison, Federalist No. 51, 1788\n\nThis passage explains why the framers",
   choices=[
     "gave each branch the means and the motive to resist encroachment by the others, rather than relying on the virtue of officeholders",
     "assumed that officeholders would set aside their own interests once in office",
     "concentrated authority in a single branch to avoid conflict between them",
     "made the branches dependent on one another for their salaries and terms",
     "left the boundaries between the branches undefined so that they could negotiate"], ans=0,
   why="The sentence pairs a personal motive with an institutional power on purpose: a design that works because officeholders defend their own turf does not depend on their being good. Assuming virtue is the alternative Madison is rejecting."),

 dict(q="Read the following excerpt.\n\n“All persons held as slaves within any State or designated part of a State, the people whereof shall then be in rebellion against the United States, shall be then, thenceforward, and forever free.”\n—Abraham Lincoln, Emancipation Proclamation, 1863\n\nWhich statement about the relationship between this document and the constitutional compromises of 1787 is most accurate?",
   choices=[
     "It marks the point at which a matter the Convention had deferred was settled by war rather than by negotiation",
     "It amended the Constitution to abolish the Three-Fifths Compromise",
     "It applied to every state in the union without exception",
     "It was adopted by three-fourths of the state legislatures under Article V",
     "It restored the compromise postponing a decision on the importation of enslaved persons"], ans=0,
   why="EK 1.5.A.3 records that the compromises left matters unresolved, and the Proclamation's own words limit it to areas then in rebellion, so it was an executive war measure rather than an amendment. Abolition of the Three-Fifths clause came by amendment afterward, not by proclamation."),

 dict(q="A student writes that the compromises of 1787 settled the question of how power would be divided between the national government and the states. Which correction does the course framework most directly support?",
   choices=[
     "The compromises left that balance unresolved, and it remains at the heart of present-day constitutional debate",
     "The compromises settled the question, and no serious dispute has arisen since",
     "The question was settled by the Bill of Rights in 1791",
     "The question was never discussed at the Convention",
     "The question was settled by the Articles of Confederation before the Convention met"], ans=0,
   why="EK 1.5.A.3 states that the compromises left some matters unresolved that continue to generate discussion, and EK 1.5.A.4 places the national/state/individual balance at the heart of present-day constitutional issues."),

 dict(q="The course framework names debates about government surveillance following the September 2001 attacks as an illustration of an unresolved constitutional question. Which tension does that example most directly illustrate?",
   choices=[
     "Between the national government's responsibility for security and the individual's claim to be free from government intrusion",
     "Between the House and the Senate over the apportionment of representation",
     "Between the states over the regulation of interstate commerce",
     "Between the president and the Supreme Court over the appointment of judges",
     "Between two political parties over the outcome of a presidential election"], ans=0,
   why="EK 1.5.A.4 names this debate as an illustration of the unresolved balance among national power, state power and individual rights, and a surveillance program sets the first of those directly against the third."),

 dict(q="The framework also names debates about the role of government in public school education. Which question in such a debate belongs most clearly to the unresolved constitutional issues the framework describes?",
   choices=[
     "Whether decisions about school curriculum belong to national authorities, to state authorities, or to individual families",
     "Whether school buildings should be renovated before or after the school year begins",
     "Whether teachers should be paid monthly or twice each month",
     "Whether a school district should purchase textbooks from one publisher or several",
     "Whether the school year should begin in August or in September"], ans=0,
   why="EK 1.5.A.4 frames the illustration as a case of the national/state/individual balance, so the constitutional question is who decides rather than what is decided. The other four are administrative choices no constitutional principle governs."),

 dict(q="In United States v. Lopez (1995), the Supreme Court held that Congress exceeded its power under the Commerce Clause when it made possession of a gun in a school zone a federal crime. A student cites the case as evidence about the compromises of 1787. Which use is accurate?",
   choices=[
     "As evidence that the boundary between national and state authority was left for later argument rather than fixed in 1787",
     "As evidence that the Commerce Clause was added to the Constitution by amendment in 1995",
     "As evidence that Congress has no power to regulate commerce among the states",
     "As evidence that the Three-Fifths Compromise remained in force until 1995",
     "As evidence that the states may not regulate firearms within their own borders"], ans=0,
   why="The CED states the Lopez holding as Congress exceeding its Commerce Clause power, which is a boundary dispute two centuries after ratification -- exactly EK 1.5.A.3's unresolved matters. The holding limits a particular exercise of the power, not the power itself."),

 dict(q="In Schenck v. United States (1919), the Supreme Court held that speech creating a clear and present danger was not protected by the First Amendment and could be limited. How does the case bear on the compromise that produced the Bill of Rights?",
   choices=[
     "It shows that adding written guarantees did not by itself settle how far those guarantees reach",
     "It shows that the Bill of Rights was never actually ratified",
     "It shows that the First Amendment protects all speech without exception",
     "It shows that the Bill of Rights applies only to the states and not to Congress",
     "It shows that the Anti-Federalists opposed the addition of a Bill of Rights"], ans=0,
   why="EK 1.5.A.1.v records the agreement to add a Bill of Rights, and Schenck is the Court deciding what one of its clauses means in a hard case. The fifth option reverses the historical record, since the Anti-Federalists demanded the Bill of Rights."),

 dict(q=_SEATS + " Which conclusion is best supported by the data?",
   table=_SEATS_TABLE,
   choices=[
     "Virginia held ten times as many House seats as Delaware but exactly the same number of Senate seats",
     "Virginia held more Senate seats than Delaware because its population was larger",
     "Every state in the table held the same number of House seats",
     "The number of Senate seats varies with the number of House seats",
     "Delaware and Rhode Island together held more House seats than New York"], ans=0,
   why="The House column runs from 10 down to 1 while the Senate column is 2 in every row, which is the Great Compromise visible in a single table. Delaware and Rhode Island together hold 2 House seats against New York's 6."),

 dict(q=_SEATS + " Which of the five compromises named in the course framework does this table most directly illustrate, and how?",
   table=_SEATS_TABLE,
   choices=[
     "The Great Compromise, because one chamber varies with population and the other does not vary at all",
     "The Three-Fifths Compromise, because it explains why the Senate column is constant",
     "The Electoral College, because the table reports the method of choosing the president",
     "The agreement to add a Bill of Rights, because it guaranteed representation to small states",
     "The postponement of a decision on the importation of enslaved persons, because it fixed the House at these numbers until 1808"], ans=0,
   why="EK 1.5.A.1.i describes exactly this pattern: the House based on each state's population and the Senate representing each state equally. The Three-Fifths formula affected the House column rather than the constant Senate column."),

 dict(q=_SEATS + " A student concludes from the table that small states were the clear winners at the Constitutional Convention. Which limitation of the data most undercuts that conclusion?",
   table=_SEATS_TABLE,
   choices=[
     "The table shows seats but not what a chamber can do, and the two chambers hold different powers over legislation, treaties and appointments",
     "The table omits the Senate entirely, so no comparison between chambers is possible",
     "The table reports estimates rather than the figures written into the constitutional text",
     "The table covers all thirteen original states, so no state can be compared with any other",
     "The table gives population figures that contradict the seat counts"], ans=0,
   why="Counting seats measures presence, not leverage; a chamber's influence depends on its powers, and the Senate's advice and consent role has no House counterpart. The second and third options are false of this table, whose figures come from the constitutional text itself."),

 dict(q=_AMEND + " Which conclusion is best supported by the data?",
   table=_AMEND_TABLE,
   choices=[
     "The amendment cleared both congressional thresholds but fell short of the number of states required for ratification",
     "The amendment failed in the Senate and therefore never reached the states",
     "The amendment was ratified, since a majority of states approved it",
     "The amendment failed in the House, where support fell below two-thirds",
     "The amendment met every requirement of Article V"], ans=0,
   why="Two-thirds of 435 is 290 and two-thirds of 100 is 67, so both chambers cleared their thresholds; three-fourths of 50 is 38, and 34 states is four short. A simple majority of states is not the Article V standard."),

 dict(q=_AMEND + " How many additional states would have had to ratify for the amendment to be adopted?",
   table=_AMEND_TABLE,
   choices=[
     "Four",
     "One",
     "Two",
     "Eight",
     "Sixteen"], ans=0,
   why="Three-fourths of 50 is 37.5, so 38 states are required and 34 ratified, a shortfall of exactly four. EK 1.5.A.2 sets final ratification at three-fourths of the states."),

 dict(q=_AMEND + " A commentator argues that the data show the amendment process working as the framers intended rather than failing. Which reasoning best supports that argument?",
   table=_AMEND_TABLE,
   choices=[
     "Article V was designed so that a proposal with broad but not overwhelming support does not alter the Constitution",
     "Article V was designed so that any proposal reaching a majority in Congress becomes part of the Constitution",
     "Article V was designed to let a single state block any change, as the Articles of Confederation had",
     "Article V was designed to keep the states out of the amendment process",
     "Article V was designed so that ratification requires no action by state legislatures"], ans=0,
   why="A three-fourths ratification threshold exists precisely to stop changes that command a majority but not a broad consensus, so a proposal at 68 percent of the states failing is the rule operating rather than misfiring. Unanimity was the Articles' rule, which Article V replaced."),

 dict(q="Which statement best explains why the Constitution has been amended relatively few times since 1791?",
   choices=[
     "Article V requires supermajorities at two separate stages, so a proposal must survive both a national and a state-level consensus test",
     "Article V permits amendments only during the first decade after ratification",
     "The Supreme Court must approve any amendment before it takes effect",
     "The Constitution forbids amending any provision adopted at the Convention",
     "Amendments require unanimous consent of the state legislatures"], ans=0,
   why="EK 1.5.A.2 names two thresholds, two-thirds to propose and three-fourths to ratify, and a proposal must clear both. Nothing in Article V gives the Court a role or closes the process after a period of years."),

 dict(q="A group of states dissatisfied with a national policy wants to amend the Constitution without waiting for Congress to act. Which route does Article V make available to them?",
   choices=[
     "Two-thirds of the state legislatures may call for a convention to propose amendments",
     "Three-fourths of the state legislatures may adopt an amendment directly",
     "A majority of the states may petition the Supreme Court to order an amendment",
     "Any single state may propose an amendment for ratification by the others",
     "The states have no role in proposing amendments, only in ratifying them"], ans=0,
   why="EK 1.5.A.2 names a proposal from two-thirds of the state legislatures as the second of the two routes, which exists precisely so that Congress is not the only gateway. Ratification by three-fourths still follows, so the second option collapses the two stages into one."),

 dict(q="Which generalization about the Constitutional Convention is best supported by the five compromises the course framework lists?",
   choices=[
     "The document that emerged was shaped as much by what delegates would refuse to accept as by what any of them preferred",
     "The delegates agreed on fundamentals and differed only over wording",
     "Each compromise was adopted unanimously and without objection",
     "The compromises were imposed on the Convention by the Confederation Congress",
     "Every compromise on the list concerned the powers of the presidency"], ans=0,
   why="Four of the five items are bargains between positions neither of which could prevail, and the fifth was a concession extracted by the document's opponents, so the list is a record of constraints rather than of shared preferences."),

 dict(q="An essay claims that studying the ratification compromises is of purely historical interest. Which response is best supported by the course framework?",
   choices=[
     "The unresolved matters those compromises left behind are the subject of present-day constitutional argument, from surveillance policy to the governance of schools",
     "The compromises were repealed by the Bill of Rights and have no continuing effect",
     "The compromises are studied only because the Convention's records are unusually complete",
     "The compromises determined the outcome of every subsequent Supreme Court case",
     "The compromises are relevant only to the interpretation of the Articles of Confederation"], ans=0,
   why="EK 1.5.A.3 and EK 1.5.A.4 make exactly this claim and name the two illustrations, so the framework itself treats the compromises as live rather than historical."),
]
