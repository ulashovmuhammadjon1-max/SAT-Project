# AP U.S. GOVERNMENT AND POLITICS 2.8 The Judicial Branch -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# Learning objective 2.8.A: explain the principle of judicial review and how it
# checks the power of other branches.
# Suggested skill for this topic (CED p. 68): 2.B, explain how a REQUIRED
# Supreme Court case relates to a FOUNDATIONAL DOCUMENT or to other primary or
# secondary sources. So the characteristic item here prints a document and asks
# how a required case connects to it, and roughly a third of this module has
# that shape.
#
# Essential knowledge relied on. ONE statement, and it is a pointer to two
# documents rather than a substantive claim, which is unusual:
#   EK 2.8.A.1 -- "The foundation for powers of the judicial branch and the
#     argument for how its independence checks the power of other branches is
#     set forth in the following documents, RESPECTIVELY:
#       i.  Article III of the Constitution
#       ii. Federalist No. 78"
#
# THE WORD "RESPECTIVELY" IS THE WHOLE STATEMENT, and item 3 is built on it.
# Article III supplies the FOUNDATION FOR THE POWERS; Federalist No. 78 supplies
# the ARGUMENT FOR INDEPENDENCE AS A CHECK. They are not two sources for the
# same claim, and a student who has learned "Article III and Federalist 78 are
# about the courts" cannot answer a question that asks which does which.
#
# WHERE JUDICIAL REVIEW ACTUALLY COMES FROM, stated carefully because this is
# where banks go wrong: the phrase "judicial review" appears nowhere in Article
# III. The CED credits the PRINCIPLE to Marbury v. Madison (1803), whose holding
# it states as establishing judicial review and empowering the Court to declare
# an act of the legislative or executive branch unconstitutional. Federalist
# No. 78 ARGUES for it before the fact; Article III VESTS the judicial power and
# supplies tenure during good behavior. Three sources, three different jobs, and
# items 4 to 12 keep them apart.
#
# Documents the CED attaches to 2.8.A (p. 26-27): Federalist No. 51,
# Federalist No. 70, Federalist No. 78.
# Required cases the CED attaches to 2.8.A (p. 31-33): Marbury v. Madison,
# New York Times Co. v. United States.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: Article III and Federalist No. 78 are
# quoted verbatim. Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere; vote splits
# are written in words. The verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.8", "The Judicial Branch", 2)

_STRUCK = ("In a hypothetical study, the table reports how many federal statutes and how many "
           "state statutes a nation's highest court held unconstitutional in each of four "
           "twenty year periods.")
_STRUCK_TABLE = dict(
    headers=["Period", "Federal statutes struck down", "State statutes struck down"],
    rows=[["First period", "2", "18"],
          ["Second period", "9", "64"],
          ["Third period", "21", "129"],
          ["Fourth period", "14", "97"]])

_SOURCES = ("The table identifies what each of three sources contributes to the principle of "
            "judicial review.")
_SOURCES_TABLE = dict(
    headers=["Source", "What it supplies", "Does the text use the phrase judicial review?"],
    rows=[["Article III of the Constitution", "The vesting of the judicial power and tenure during good behavior", "No"],
          ["Federalist No. 78", "The argument that an independent judiciary checks the other branches", "No"],
          ["Marbury v. Madison (1803)", "The establishment of the principle itself", "No"]])

QUESTIONS = [
 dict(q="According to the course framework, the foundation for the powers of the judicial branch is set forth in",
   choices=[
     "Article III of the Constitution",
     "Federalist No. 78",
     "Federalist No. 51",
     "the Tenth Amendment",
     "the Judiciary Act passed by the first Congress"], ans=0,
   why="EK 2.8.A.1 pairs the two documents RESPECTIVELY: Article III supplies the foundation for the powers, and Federalist No. 78 supplies the argument about independence as a check."),

 dict(q="According to the course framework, the argument for how the judiciary's independence checks the power of the other branches is set forth in",
   choices=[
     "Federalist No. 78",
     "Article III of the Constitution",
     "Federalist No. 10",
     "the Bill of Rights",
     "Marbury v. Madison"], ans=0,
   why="EK 2.8.A.1's second item is Federalist No. 78, and the word 'respectively' assigns it the independence argument rather than the foundation for the powers, which is Article III's job."),

 dict(q="EK 2.8.A.1 pairs two documents with two contributions using the word 'respectively.' What does that pairing establish?",
   choices=[
     "Article III supplies the foundation for the powers and Federalist No. 78 supplies the argument for independence as a check",
     "Federalist No. 78 supplies the foundation for the powers and Article III supplies the argument for independence",
     "Both documents supply the same argument in different words",
     "Neither document concerns the judiciary's relationship to the other branches",
     "Both documents establish the principle of judicial review by name"], ans=0,
   why="The order in the framework's sentence is foundation first and independence argument second, matched to Article III and Federalist No. 78 in that order. Reversing the pairing is the error the word 'respectively' exists to prevent."),

 dict(q="In which source does the phrase 'judicial review' actually appear?",
   choices=[
     "In none of them, since neither Article III nor Federalist No. 78 nor the Marbury opinion introduces the principle by that name",
     "In Article III, which grants the power in those words",
     "In Federalist No. 78, which names it explicitly",
     "In the Tenth Amendment",
     "In the Judiciary Act, which defines the term"], ans=0,
   why="The CED credits the PRINCIPLE to Marbury v. Madison and points to Article III and Federalist No. 78 for the foundation and the argument, but the constitutional text does not use the phrase. A student who expects to find it in Article III is looking for something that is not there."),

 dict(q="In Marbury v. Madison (1803), the Supreme Court established the principle of judicial review, empowering the Court to declare an act of the legislative or executive branch unconstitutional. Which statement about the case is accurate?",
   choices=[
     "It established a principle that the constitutional text does not state in those terms",
     "It applied a power expressly granted to the Court by Article III",
     "It was overruled by a later constitutional amendment",
     "It concerned only the powers of state courts",
     "It held that Congress may declare its own acts constitutional"], ans=0,
   why="The CED states the holding as ESTABLISHING the principle, which is a different act from applying a granted power. Article III vests the judicial power without naming this consequence of it."),

 dict(q="Read the following excerpt.\n\n“The judicial Power of the United States, shall be vested in one supreme Court, and in such inferior Courts as the Congress may from time to time ordain and establish. The Judges, both of the supreme and inferior Courts, shall hold their Offices during good Behaviour.”\n—U.S. Constitution, Article III, Section 1\n\nWhich two things does this passage establish?",
   choices=[
     "Where the judicial power is vested, and the tenure on which judges hold office",
     "The power of judicial review, and the size of the Supreme Court",
     "The jurisdiction of the federal courts, and the process for removing judges",
     "The number of federal judges, and the salary they are paid",
     "The right to a jury trial, and the right to counsel"], ans=0,
   why="The first sentence vests the judicial power and provides for inferior courts Congress may create; the second sets tenure during good behavior. The passage names neither judicial review nor the Court's size."),

 dict(q="What does the phrase 'during good Behaviour' in Article III establish, and why does it matter for the judiciary's relationship with the other branches?",
   choices=[
     "It gives federal judges tenure that does not expire, so a judge need not fear removal for an unpopular decision",
     "It gives federal judges fixed terms renewable by the president",
     "It allows the president to remove a judge whose decisions he opposes",
     "It requires judges to stand for retention election every ten years",
     "It permits Congress to reduce a judge's salary as a disciplinary measure"], ans=0,
   why="Tenure that does not expire is the structural source of judicial independence, which is why EK 2.8.A.1 places the FOUNDATION in Article III and EK 2.10.A.1 builds on life tenure. Article III also protects judicial salaries from reduction."),

 dict(q="Read the following excerpt.\n\n“The judiciary, on the contrary, has no influence over either the sword or the purse; no direction either of the strength or of the wealth of the society; and can take no active resolution whatever. It may truly be said to have neither FORCE nor WILL, but merely judgment.”\n—Alexander Hamilton, Federalist No. 78, 1788\n\nWhat is Hamilton's purpose in describing the judiciary this way?",
   choices=[
     "To argue that a branch with neither force nor will is the least dangerous, so its independence may safely be secured",
     "To argue that the judiciary should be given control over appropriations",
     "To argue that the judiciary should be abolished as unnecessary",
     "To argue that the judiciary should be subordinate to the legislature in all things",
     "To argue that judges should be elected so that they possess will as well as judgment"], ans=0,
   why="The passage is the premise of Hamilton's argument that the judiciary is the least dangerous branch, which is what makes independence safe rather than threatening. Reading it as an argument against the courts inverts it."),

 dict(q="Read the following excerpt.\n\n“No legislative act, therefore, contrary to the Constitution, can be valid. To deny this, would be to affirm, that the deputy is greater than his principal; that the servant is above his master.”\n—Alexander Hamilton, Federalist No. 78, 1788\n\nWhich later development does this passage most directly anticipate?",
   choices=[
     "The principle of judicial review established in Marbury v. Madison",
     "The creation of the Cabinet",
     "The adoption of the Twenty-Second Amendment",
     "The expansion of the Commerce Clause",
     "The requirement that revenue bills originate in the House"], ans=0,
   why="Hamilton's syllogism -- the Constitution is superior to the legislature, so a contrary statute is void -- is the reasoning the CED credits Marbury with establishing as a principle fifteen years later."),

 dict(q="Read the following excerpt.\n\n“The complete independence of the courts of justice is peculiarly essential in a limited Constitution. By a limited Constitution, I understand one which contains certain specified exceptions to the legislative authority.”\n—Alexander Hamilton, Federalist No. 78, 1788\n\nWhat connection does Hamilton draw between limits on government and judicial independence?",
   choices=[
     "Limits written into a constitution mean nothing unless a body independent of the legislature can enforce them",
     "Limits on government make an independent judiciary unnecessary",
     "Independence is needed only when a constitution places no limits on the legislature",
     "The legislature should determine for itself whether it has exceeded its limits",
     "Judicial independence is required by the separation of powers but not by limited government"], ans=0,
   why="The sentence makes independence 'peculiarly essential' precisely because the Constitution contains exceptions to legislative authority, so someone outside the legislature must enforce them. The fourth option is the alternative Hamilton is arguing against."),

 dict(q="A student writes that Federalist No. 78 created the power of judicial review. What is the correction?",
   choices=[
     "Federalist No. 78 is an argument for the practice, not a source of law; the CED credits Marbury v. Madison with establishing the principle",
     "Federalist No. 78 is part of the Constitution and did create the power",
     "Federalist No. 78 argued against judicial review, which the Court adopted anyway",
     "Federalist No. 78 concerns the executive branch rather than the judiciary",
     "Federalist No. 78 was written after Marbury v. Madison and describes it"], ans=0,
   why="The Federalist papers are essays urging ratification and have no legal force, which is why EK 2.8.A.1 calls Federalist No. 78 an ARGUMENT while the CED's required-case table credits Marbury with establishing the principle."),

 dict(q="Which sequence correctly orders the three sources by what each contributes to judicial review?",
   choices=[
     "Article III vests the judicial power, Federalist No. 78 argues that independence is essential, and Marbury establishes the principle",
     "Marbury vests the judicial power, Article III argues for independence, and Federalist No. 78 establishes the principle",
     "Federalist No. 78 vests the judicial power, Marbury argues for independence, and Article III establishes the principle",
     "All three establish the principle in the same terms",
     "None of the three concerns judicial review"], ans=0,
   why="EK 2.8.A.1 assigns the foundation to Article III and the independence argument to Federalist No. 78, and the CED's required-case table assigns the establishment of the principle to Marbury."),

 dict(q="How does judicial review check the LEGISLATIVE branch specifically?",
   choices=[
     "A court may hold that a statute Congress has enacted exceeds constitutional limits and refuse to give it effect",
     "A court may repeal a statute by a vote of its members",
     "A court may prevent Congress from considering a bill",
     "A court may require Congress to enact legislation on a subject",
     "A court may remove a member of Congress from office"], ans=0,
   why="The CED states the Marbury holding as empowering the Court to declare an act of the legislative or executive branch unconstitutional, which operates on a statute already enacted. Courts do not repeal statutes or direct Congress's agenda."),

 dict(q="How does judicial review check the EXECUTIVE branch specifically?",
   choices=[
     "A court may hold that an executive action exceeds the authority the Constitution or a statute confers",
     "A court may remove the president from office",
     "A court may issue an executive order of its own",
     "A court may refuse to allow the president to nominate officials",
     "A court may veto a bill the president has signed"], ans=0,
   why="The CED's statement of the Marbury holding names acts of the legislative OR EXECUTIVE branch, and the check operates by measuring an action against the authority for it. Removal is impeachment, under EK 1.6.B.2."),

 dict(q="In New York Times Co. v. United States (1971), the Supreme Court bolstered freedom of the press, establishing a heavy presumption against prior restraint even in cases involving national security. How does the case illustrate EK 2.8.A.1's claim about judicial independence?",
   choices=[
     "A court whose members need not fear removal ruled against the executive on a claim of national security, which is what independence makes possible",
     "The Court deferred to the executive's judgment about national security",
     "The Court held that the press may be restrained whenever secrecy is claimed",
     "The Court declined to decide the case because it raised a political question",
     "The Court's decision was later reversed by Congress"], ans=0,
   why="EK 2.8.A.1 credits Federalist No. 78 with the argument that judicial independence checks the other branches, and a ruling against the executive on its strongest asserted interest is that argument borne out."),

 dict(q="A non-required case: a federal appeals court holds that an agency rule adopted without the procedure a statute requires is invalid. Which required case supplies the underlying principle, and what is it?",
   choices=[
     "Marbury v. Madison (1803), which established that courts may declare an act of the legislative or executive branch unconstitutional",
     "New York Times Co. v. United States (1971), which established a heavy presumption against prior restraint",
     "Baker v. Carr (1962), which held that redistricting does not raise political questions",
     "McCulloch v. Maryland (1819), which established the supremacy of federal law over state law",
     "Shaw v. Reno (1993), which allowed challenges to districts drawn solely on race"], ans=0,
   why="A court measuring an executive action against the law and refusing it effect is exercising judicial review, which the CED credits to Marbury. The other four holdings concern the press, districting and federal supremacy."),

 dict(q="Which of the following is the strongest argument AGAINST judicial review as a feature of the constitutional design?",
   choices=[
     "Unelected judges with tenure that does not expire can set aside the work of officials the voters chose",
     "Judges lack the training needed to read statutes",
     "The Constitution forbids courts to hear cases involving the other branches",
     "Judicial review was abolished by the Eleventh Amendment",
     "Courts have no means of enforcing any decision, so review has no effect"], ans=0,
   why="The serious objection is democratic: the independence Article III secures is exactly what removes judges from electoral accountability. The fifth option overstates Federalist No. 78's point about force into a claim that decisions are never obeyed."),

 dict(q="Which of the following is the strongest argument FOR judicial review, drawing on Federalist No. 78?",
   choices=[
     "Written limits on legislative authority require an enforcer outside the legislature, or the legislature judges its own case",
     "Judges are better informed about policy than legislators are",
     "The judiciary controls the purse and can compel compliance",
     "Judicial decisions are always more popular than legislative acts",
     "Courts can act faster than Congress when a problem arises"], ans=0,
   why="This is Hamilton's own argument in the 'limited Constitution' passage: exceptions to legislative authority are meaningless if the legislature decides whether it has exceeded them. Federalist No. 78 explicitly denies the judiciary any control of the purse."),

 dict(q="Why does the course framework treat judicial independence as a matter of INSTITUTIONAL DESIGN rather than of judicial character?",
   choices=[
     "Tenure during good behavior removes the incentive to please whoever holds power, whatever an individual judge's disposition",
     "Judges are selected for their impartiality, which makes design unnecessary",
     "The Constitution requires judges to swear an oath of neutrality",
     "Judges are prohibited from having political opinions",
     "Independence follows from the requirement that decisions be unanimous"], ans=0,
   why="EK 2.8.A.1 locates the foundation in Article III, a structural provision, and Federalist No. 78's argument is about what the arrangement makes possible rather than about who is appointed. This is the same logic as Federalist No. 51's ambition counteracting ambition."),

 dict(q="A legislature enacts a statute that a court later holds unconstitutional. Which description of what has happened is most accurate?",
   choices=[
     "The court has declined to give the statute effect in cases before it, which is how judicial review operates",
     "The court has repealed the statute, removing it from the code",
     "The court has amended the Constitution to forbid the statute",
     "The court has ordered the legislature to enact a replacement",
     "The court has referred the statute to the executive for reconsideration"], ans=0,
   why="Judicial review operates through decisions in cases, so a court refuses to apply a statute rather than repealing it. Repeal and amendment belong to the legislature and to the Article V process respectively."),

 dict(q=_STRUCK + " Which conclusion is best supported by the data?",
   table=_STRUCK_TABLE,
   choices=[
     "The court struck down far more state statutes than federal statutes in every period",
     "The court struck down more federal statutes than state statutes in every period",
     "Both counts rose in every period",
     "The court struck down no federal statutes in any period",
     "The number of state statutes struck down was highest in the fourth period"], ans=0,
   why="The state figures are 18, 64, 129 and 97 against federal figures of 2, 9, 21 and 14, so states exceed federal by a wide margin throughout. Both counts fall in the fourth period, and the state peak is the third."),

 dict(q=_STRUCK + " Which claim about judicial review do these data most directly support?",
   table=_STRUCK_TABLE,
   choices=[
     "Judicial review operates against both levels of government, and in this court's practice against the states far more often",
     "Judicial review operates only against acts of the national legislature",
     "Judicial review operates only against acts of state legislatures",
     "Judicial review has never been used against a state statute",
     "Judicial review is exercised equally against the two levels"], ans=0,
   why="Both columns are non-zero in every period, so review reaches both levels, and the state column is several times larger throughout. The CED's statement of the Marbury holding names acts of the legislative or executive branch without limiting the level."),

 dict(q=_STRUCK + " A student concludes from these data that the court became more aggressive over time. Which limitation of the data most undercuts that conclusion?",
   table=_STRUCK_TABLE,
   choices=[
     "The table reports no denominator, so a rising count may reflect more statutes enacted rather than a more assertive court",
     "The table omits state statutes, so no comparison is possible",
     "The table covers a single period, so no trend can be observed",
     "The table reports percentages that do not sum to one hundred",
     "The table gives no information about how many statutes were struck down"], ans=0,
   why="A count with no base rate cannot distinguish a more assertive court from a more active legislature, which is the standard limitation of an unnormalized series. Both columns and four periods are plainly present."),

 dict(q=_SOURCES + " Which conclusion is best supported by the table?",
   table=_SOURCES_TABLE,
   choices=[
     "Each source contributes something different, and none of the three uses the phrase judicial review",
     "All three sources contribute the same thing in different words",
     "Two of the three sources use the phrase judicial review",
     "Article III establishes the principle and the other two describe it",
     "Federalist No. 78 vests the judicial power"], ans=0,
   why="The middle column gives three different contributions and the last column reads No in all three rows. Article III vests the power without establishing the principle, which the third row assigns to Marbury."),

 dict(q=_SOURCES + " Which row of the table corresponds to the first item of EK 2.8.A.1?",
   table=_SOURCES_TABLE,
   choices=[
     "The Article III row, which supplies the vesting of the judicial power and tenure during good behavior",
     "The Federalist No. 78 row, which supplies the independence argument",
     "The Marbury row, which supplies the principle itself",
     "None of the rows, since EK 2.8.A.1 names no documents",
     "All three rows equally, since the framework does not distinguish among them"], ans=0,
   why="EK 2.8.A.1 lists Article III first and Federalist No. 78 second, matched respectively to the foundation for the powers and the argument for independence."),

 dict(q=_SOURCES + " A student says the table shows that judicial review has no constitutional basis. What is the most important correction?",
   table=_SOURCES_TABLE,
   choices=[
     "A principle may rest on the structure and logic of a text without appearing in it as a phrase, which is what the first two rows describe",
     "The table shows that Article III uses the phrase, so the student has misread it",
     "The table shows that judicial review was created by statute rather than by the Constitution",
     "The table shows that Federalist No. 78 is part of the Constitution",
     "The table shows that the principle was established by constitutional amendment"], ans=0,
   why="Article III vests the judicial power and Federalist No. 78 supplies the argument from a limited constitution, so absence of the phrase is not absence of a basis. The Federalist papers are not law, and no amendment established the principle."),

 dict(q="Which pairing of a branch with the way judicial review reaches it is correct?",
   choices=[
     "Congress, through review of an enacted statute; the president, through review of an executive action",
     "Congress, through review of an executive action; the president, through review of a statute",
     "Congress, through removal of its members; the president, through impeachment",
     "Congress, through the veto; the president, through the override",
     "Neither branch, since judicial review reaches only the states"], ans=0,
   why="The CED's statement of the Marbury holding names acts of the legislative or executive branch, and the instrument each branch produces is a statute and an executive action respectively."),

 dict(q="Which scenario best illustrates the judiciary's dependence on the other branches, despite the independence Article III secures?",
   choices=[
     "A court's decision requires funds or enforcement action that only Congress or the executive can supply",
     "A court is unable to hear a case because no litigant has filed one",
     "A court's decision is reported in the press",
     "A court's opinion is written by a single justice",
     "A court's decision is appealed to a higher court"], ans=0,
   why="Federalist No. 78's own premise is that the judiciary commands neither the sword nor the purse, so a decision requiring either depends on another branch. That dependence coexists with the independence tenure secures."),

 dict(q="A president says he disagrees with a Supreme Court decision but will comply with it. What does that statement illustrate about the constitutional system?",
   choices=[
     "Judicial review functions because the other branches accept the Court's judgments even when they oppose them",
     "The president has the power to nullify a decision he disagrees with",
     "The Court's decisions are advisory and need not be followed",
     "The president's compliance converts the decision into a statute",
     "Disagreement by the president automatically sends the case back for rehearing"], ans=0,
   why="Federalist No. 78 grants the judiciary neither force nor will, so a decision's effect rests on acceptance by the branches that command both. The other options describe powers no president holds."),

 dict(q="Which question would best test whether judicial review is functioning as a check on the other branches in a given period?",
   choices=[
     "How often did courts rule against the government's position in cases where a constitutional limit was asserted?",
     "How many cases did the courts decide in total?",
     "How many judges were appointed during the period?",
     "How long did the average case take to decide?",
     "How many opinions were unanimous?"], ans=0,
   why="EK 2.8.A.1's claim is about independence CHECKING other branches, so the test has to be how often the check actually operates against the government. Case volume, appointments and timing measure activity rather than restraint."),
]
