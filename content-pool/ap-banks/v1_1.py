# AP U.S. GOVERNMENT AND POLITICS 1.1 Ideals of Democracy -- 30 questions
# CED V.1 (c) 2026, Unit 1 Foundations of American Democracy.
# Learning objective 1.1.A: explain how democratic ideals are reflected in the
# Declaration of Independence, the U.S. Constitution, AND THE GETTYSBURG
# ADDRESS. The Gettysburg Address is part of this objective in the current CED;
# it was not in the older framework, and EK 1.1.A.3 gives it a specific job --
# it "reaffirmed equality and popular sovereignty as defining foundations of
# democracy." Items 15-17 rest on that sentence, not on general knowledge.
#
# Essential knowledge relied on:
#   EK 1.1.A.1 -- the four democratic ideals, a CLOSED list: natural rights,
#     social contract, popular sovereignty, limited government, each with the
#     framework's own gloss.
#   EK 1.1.A.2 -- limited government is ensured by the interaction of four
#     principles: separation of powers, checks and balances, federalism,
#     republicanism. Note the framework's structure here: the four principles
#     are the MEANS and limited government is the END. Items 8-11 turn on that
#     relationship, because a student who lists all eight terms flat cannot
#     answer them.
#   EK 1.1.A.3 -- authorship and role of the three documents.
#
# Required cases the CED attaches to 1.1.A (p. 31-33): Marbury v. Madison,
# McCulloch v. Maryland, Schenck v. United States, Engel v. Vitale, Gideon v.
# Wainwright, Tinker v. Des Moines, New York Times Co. v. United States. The
# SCOTUS-comparison items below use only those, and each prints the
# non-required case's facts in the stem, as the real exam does.
#
# Quotations are verbatim from the Declaration of Independence and the
# Gettysburg Address (Bliss copy). Where a document's exact wording could not
# be verified it is described instead of quoted -- see SOCIAL_BRIEF.md.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md. The CED's own sample multiple-choice
# questions carry four; see AP_US_GOV_CED.md note 10. Key written first
# throughout; export_units.py redistributes it across A-E.
TOPIC = ("1.1", "Ideals of Democracy", 1)

_SURVEY = "In a hypothetical national survey, adults were asked how well each statement describes the United States today. Percentages of respondents answering “describes it well” are shown."

QUESTIONS = [
 dict(q="A state supreme court rules that a person may not be forced to testify against himself even though the legislature has passed a statute requiring it. The ruling rests most directly on which democratic ideal?",
   choices=[
     "Natural rights, because certain rights belong to people and cannot be taken away by government action",
     "Popular sovereignty, because the legislature was elected by the voters of the state",
     "Federalism, because a state court rather than a federal court issued the ruling",
     "Republicanism, because the people act through elected representatives",
     "The social contract, because people agree to surrender some freedoms for order"], ans=0,
   why="EK 1.1.A.1 defines natural rights as rights that cannot be taken away. A statute is exactly the government action the ideal limits, so the fact that the legislature was elected does not save it."),

 dict(q="Residents of a town accept speed limits, building codes, and a local tax in exchange for paved roads, a fire department, and policing. This arrangement most directly illustrates",
   choices=[
     "a social contract, an implicit agreement to give up some freedoms to maintain social order",
     "natural rights, which no government may take away",
     "popular sovereignty, in which all governmental power flows from the consent of the people",
     "limited government, in which governmental power cannot be absolute",
     "checks and balances among separate institutions of government"], ans=0,
   why="EK 1.1.A.1 defines the social contract as an implicit agreement among people in a society to give up some freedoms in order to maintain social order, which is precisely the trade the residents accept."),

 dict(q="A state constitution opens by declaring that all political power is inherent in the people and that government is founded on their authority. This language expresses which ideal?",
   choices=[
     "Popular sovereignty",
     "Natural rights",
     "Limited government",
     "Separation of powers",
     "Federalism"], ans=0,
   why="EK 1.1.A.1 defines popular sovereignty as the principle that all government power comes from the consent of its people, which is what the clause asserts."),

 dict(q="A city charter forbids the mayor from searching a home without a warrant issued by a judge. The restriction is the clearest example of",
   choices=[
     "limited government, because a government's power cannot be absolute",
     "popular sovereignty, because the charter was approved by the city's voters",
     "the social contract, because residents accept some restrictions to obtain order",
     "natural rights, because privacy is a right that predates government",
     "republicanism, because the charter was drafted by elected representatives"], ans=0,
   why="EK 1.1.A.1 defines limited government as the ideal that a government's power cannot be absolute; a rule that bars an official from acting without a warrant is a restriction on the government itself, not a statement about where its authority originates."),

 dict(q="Which statement best captures how the ideals of natural rights and the social contract fit together in the Declaration of Independence?",
   choices=[
     "People possess rights before government exists, and they form a government by consent in order to secure those rights",
     "Government creates rights and may withdraw them when the public interest requires it",
     "Rights belong only to citizens who participate in elections and pay taxes",
     "The social contract replaces natural rights with legal rights granted by a legislature",
     "Natural rights and the social contract are competing ideals that cannot both be honored"], ans=0,
   why="The Declaration states that people are endowed with unalienable rights and that “to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed” -- rights first, government second, and government's purpose is to secure them."),

 dict(q="Read the following excerpt.\n\n“We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.—That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed.”\n—Declaration of Independence, 1776\n\nWhich pair of ideals is expressed in the excerpt?",
   choices=[
     "Natural rights and popular sovereignty",
     "Federalism and separation of powers",
     "Checks and balances and judicial review",
     "Republicanism and bicameralism",
     "Judicial restraint and stare decisis"], ans=0,
   why="“Unalienable Rights” states natural rights; “deriving their just powers from the consent of the governed” states popular sovereignty. The other options name structures found in the Constitution, not ideals asserted in this passage."),

 dict(q="Read the following excerpt.\n\n“That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness.”\n—Declaration of Independence, 1776\n\nThe passage most directly supports which conclusion about the relationship between a government and the people it governs?",
   choices=[
     "A government's authority is conditional on its serving the purposes for which the people established it",
     "A government once established holds permanent authority that the people may not withdraw",
     "Only a legislature, and not the people at large, may change a form of government",
     "The people may alter a government only when a court has first declared it unlawful",
     "Governments derive their authority from tradition rather than from consent"], ans=0,
   why="The passage conditions the people's obligation on the government's serving “these ends” -- the securing of rights named in the preceding sentence -- and reserves to the people the right to alter or abolish it, which makes the authority conditional rather than permanent."),

 dict(q="EK 1.1.A.2 identifies four constitutional principles whose interaction ensures limited government. Which choice names all four?",
   choices=[
     "Separation of powers, checks and balances, federalism, republicanism",
     "Natural rights, social contract, popular sovereignty, limited government",
     "Judicial review, stare decisis, selective incorporation, due process",
     "Bicameralism, the filibuster, the veto, the amendment process",
     "Enumerated powers, implied powers, reserved powers, concurrent powers"], ans=0,
   why="EK 1.1.A.2 names exactly these four as the principles whose interaction ensures limited government. The second option lists the four democratic IDEALS of EK 1.1.A.1, which the principles serve rather than duplicate."),

 dict(q="Which statement best describes how separation of powers and checks and balances relate to the ideal of limited government?",
   choices=[
     "They are structural means by which limited government is achieved, not the ideal itself",
     "They are alternative names for the ideal of limited government",
     "They are ideals that the Constitution's structure was designed to overcome",
     "They limit the states while leaving the national government unlimited",
     "They apply to the legislative branch alone, since it is the most powerful"], ans=0,
   why="EK 1.1.A.2 states that the ideal of limited government is ENSURED BY the interaction of separation of powers, checks and balances, federalism, and republicanism -- so the four are the mechanism and limited government is the result."),

 dict(q="A national legislature may pass a law, but the chief executive may refuse to sign it, and the legislature may then pass it again by a supermajority. This arrangement is the clearest illustration of",
   choices=[
     "checks and balances, because each branch can restrain the actions of another",
     "separation of powers alone, because each branch has its own distinct function",
     "federalism, because power is divided between levels of government",
     "republicanism, because officials are chosen by the people",
     "popular sovereignty, because the legislature represents the voters"], ans=0,
   why="Separation of powers assigns distinct functions; checks and balances is the further step in which one branch can act on another's decision. A veto that a supermajority can override is one branch restraining another, which is the check."),

 dict(q="Under EK 1.1.A.2, republicanism contributes to limited government primarily because",
   choices=[
     "government decisions are made by representatives who answer to the people rather than by rulers who answer to no one",
     "the national government is forbidden to regulate commerce among the states",
     "courts may strike down any law a majority of citizens dislikes",
     "each state retains complete sovereignty over its own affairs",
     "officials are chosen by lottery rather than by election"], ans=0,
   why="Republicanism means the people govern through elected representatives; accountability to an electorate is what keeps officeholders' power from becoming absolute, which is how the principle serves the ideal of limited government."),

 dict(q="A national government may regulate the currency, while a state government may set the rules for its own public schools, and neither may abolish the other. This division most directly illustrates",
   choices=[
     "federalism",
     "checks and balances",
     "separation of powers",
     "the social contract",
     "judicial review"], ans=0,
   why="Federalism is the division of authority between national and state levels of government, each with powers the other cannot simply take away; checks and balances and separation of powers operate among branches at one level, not between levels."),

 dict(q="According to EK 1.1.A.3, the U.S. Constitution is best understood as an example of",
   choices=[
     "a social contract that establishes a system of limited government",
     "a declaration of natural rights that predates any government",
     "a statement of grievances against a distant executive",
     "a treaty among sovereign nations that may be dissolved at will",
     "an ordinary statute subject to repeal by a simple legislative majority"], ans=0,
   why="EK 1.1.A.3 states that the Constitution “is an example of a social contract and establishes a system of limited government.” The second and third options describe the Declaration of Independence instead."),

 dict(q="EK 1.1.A.3 credits the drafting of the Constitution at the Philadelphia convention chiefly to",
   choices=[
     "James Madison, at a convention led by George Washington and with contributions from Hamilton and the “Grand Committee”",
     "Thomas Jefferson, with help from John Adams and Benjamin Franklin",
     "Alexander Hamilton acting alone as the convention's presiding officer",
     "Abraham Lincoln, whose wartime address reaffirmed its principles",
     "John Locke, whose writings the delegates adopted without alteration"], ans=0,
   why="EK 1.1.A.3 names Madison as the drafter at the convention led by Washington, with important contributions from Hamilton and members of the “Grand Committee.” The second option is the framework's description of the Declaration's authorship, not the Constitution's."),

 dict(q="Read the following excerpt.\n\n“Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.”\n—Abraham Lincoln, Gettysburg Address, 1863\n\nThe passage most directly reaffirms which democratic ideal named in the course framework?",
   choices=[
     "Equality, by restating the Declaration of Independence's central proposition",
     "Federalism, by describing the relationship between the states and the Union",
     "Separation of powers, by distinguishing the wartime roles of the branches",
     "Judicial review, by asserting the courts' authority over legislation",
     "Limited government, by enumerating powers denied to the national government"], ans=0,
   why="EK 1.1.A.3 says the Gettysburg Address “reaffirmed equality and popular sovereignty as defining foundations of democracy,” and this sentence does the equality half by quoting the Declaration's proposition that all men are created equal."),

 dict(q="Read the following excerpt.\n\n“…that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth.”\n—Abraham Lincoln, Gettysburg Address, 1863\n\nThe closing phrase most directly reaffirms",
   choices=[
     "popular sovereignty, the principle that governmental power comes from the people",
     "the separation of powers among three branches of the national government",
     "the supremacy of federal law over conflicting state law",
     "the necessity of a written bill of rights",
     "the president's authority as commander in chief during wartime"], ans=0,
   why="“Of the people, by the people, for the people” locates the source, the operation, and the purpose of government in the people, which is the definition of popular sovereignty in EK 1.1.A.1; EK 1.1.A.3 names popular sovereignty as one of the two ideals the Address reaffirms."),

 dict(q="Which statement best explains why the course framework treats the Declaration of Independence and the Gettysburg Address as connected documents?",
   choices=[
     "The Address restates the Declaration's claims about equality and about government resting on the people",
     "The Address amended the Declaration to remove its list of grievances",
     "Both documents have the legal force of constitutional amendments",
     "Both documents establish the structure of the national government",
     "The Declaration was written to justify the policies announced in the Address"], ans=0,
   why="EK 1.1.A.3 pairs them by content: the Declaration “restates the philosophy of natural rights, and provides a foundation for popular sovereignty,” and the Address “reaffirmed equality and popular sovereignty.” Neither has the legal force of the Constitution, and the Address came 87 years later."),

 dict(q="A political scientist argues that the ideal of limited government is stated nowhere in a single clause of the Constitution but is instead produced by the document's structure. Which piece of evidence best supports that argument?",
   choices=[
     "Congress may pass a law, the president may veto it, and the courts may hold it unconstitutional",
     "The Constitution's preamble lists the purposes for which the government was established",
     "The Constitution was ratified by conventions in the states rather than by legislatures",
     "The Constitution may be amended by a two-thirds vote of both houses and ratification by three-fourths of the states",
     "The Constitution assigns the power to coin money to the national government"], ans=0,
   why="EK 1.1.A.2 says limited government is ensured by the INTERACTION of the four principles. A sequence in which three separate institutions can each stop the same policy is that interaction; a list of purposes or a single grant of power is not."),

 dict(q="In Marbury v. Madison (1803) the Supreme Court held that it could declare an act of Congress unconstitutional. Which democratic ideal does that holding most directly serve?",
   choices=[
     "Limited government, because it establishes that even the legislature's power is not absolute",
     "Popular sovereignty, because judges are elected by the people",
     "The social contract, because litigants agree in advance to accept a court's judgment",
     "Federalism, because the case arose from a dispute between two states",
     "Natural rights, because the decision recognized a right not listed in the Constitution"], ans=0,
   why="The CED states the holding as establishing judicial review, “empowering the Supreme Court to declare an act of the legislative or executive branch unconstitutional.” A power to void the acts of another branch is a limit on that branch, which is the ideal of limited government."),

 dict(q="A non-required case: a state court holds that a state agency may not close a newspaper for publishing an article criticizing the governor, even though a state statute authorizes the closure. Which required Supreme Court case rests on the most similar reasoning?",
   choices=[
     "New York Times Co. v. United States (1971), which established a heavy presumption against prior restraint on publication",
     "Marbury v. Madison (1803), which established the principle of judicial review",
     "McCulloch v. Maryland (1819), which established the supremacy of federal law over conflicting state law",
     "Gideon v. Wainwright (1963), which extended the right to an attorney to felony defendants in state courts",
     "Engel v. Vitale (1962), which held that school sponsorship of religious activities violates the Establishment Clause"], ans=0,
   why="Both cases stop a government from blocking publication in advance. The CED states the New York Times holding as bolstering freedom of the press and establishing “a heavy presumption against prior restraint” even where national security is claimed."),

 dict(q="A non-required case: a state law requires every public school day to begin with a prayer written by the state board of education, and a court strikes it down. Which required case supplies the closest precedent, and on what ground?",
   choices=[
     "Engel v. Vitale (1962), because school sponsorship of religious activities violates the Establishment Clause of the First Amendment",
     "Wisconsin v. Yoder (1972), because compelling school attendance past the eighth grade violated the Free Exercise Clause",
     "Tinker v. Des Moines (1969), because a ban on students' silent political expression violated freedom of speech",
     "Schenck v. United States (1919), because speech creating a clear and present danger may be limited",
     "Gideon v. Wainwright (1963), because procedural due process extends to state felony prosecutions"], ans=0,
   why="The CED states the Engel holding as school sponsorship of religious activities violating the Establishment Clause; a state-written prayer required in every school is that fact pattern. Yoder is a free-exercise case about compelled attendance, which is a different clause and a different injury."),

 dict(q="Which statement most accurately describes the relationship between the ideal of natural rights and the required case Gideon v. Wainwright (1963)?",
   choices=[
     "The decision made a protection meaningful in practice by requiring states to supply counsel to felony defendants who cannot afford it",
     "The decision established that the Supreme Court may declare acts of Congress unconstitutional",
     "The decision held that federal law is supreme over conflicting state law",
     "The decision limited speech that creates a clear and present danger",
     "The decision struck down race-based segregation in public schools"], ans=0,
   why="The CED states the Gideon holding as extending the Sixth Amendment right to an attorney, and so procedural due process protections, to felony defendants in state courts -- a right that exists on paper becomes usable in practice. The other options state the holdings of Marbury, McCulloch, Schenck, and Brown."),

 dict(q="Schenck v. United States (1919) held that speech creating a “clear and present danger” is not protected by the First Amendment. A student cites the case as evidence that",
   choices=[
     "even a right treated as fundamental can be limited when the government shows a sufficient justification",
     "natural rights are granted by government and may be revoked at will",
     "the First Amendment applies only to the national government and never to the states",
     "the Supreme Court may not review acts of Congress passed during wartime",
     "freedom of speech has no constitutional protection in the United States"], ans=0,
   why="The holding as the CED states it limits protection for a defined category of speech; it does not deny that the right exists. That is the difference between a limited right and a revocable one, and it is the distinction the second and fifth options miss."),

 dict(q=_SURVEY + " Which conclusion is best supported by the data?",
   table=dict(headers=["Statement", "Ages 18-29", "Ages 30-49", "Ages 50-64", "Ages 65 and older"],
              rows=[["Rights of citizens are protected", "48", "54", "58", "63"],
                    ["Elected officials answer to voters", "31", "35", "38", "42"],
                    ["Government power is effectively limited", "40", "44", "45", "49"]]),
   choices=[
     "For every statement, the share answering “describes it well” rises with each older age group",
     "A majority of every age group says elected officials answer to voters",
     "The youngest group is the most positive on every statement",
     "The three statements draw nearly identical responses within each age group",
     "Respondents aged 65 and older are less positive than those aged 50 to 64 on every statement"], ans=0,
   why="Reading across each row, the values increase from left to right in all three rows. The claim about a majority fails because the second row never reaches 50, and the claim about the youngest group being most positive reverses the pattern the table shows."),

 dict(q=_SURVEY + " A political scientist argues that Americans are more confident that their rights are protected than that officials are accountable to them. Which comparison in the data best supports that argument?",
   table=dict(headers=["Statement", "Ages 18-29", "Ages 30-49", "Ages 50-64", "Ages 65 and older"],
              rows=[["Rights of citizens are protected", "48", "54", "58", "63"],
                    ["Elected officials answer to voters", "31", "35", "38", "42"],
                    ["Government power is effectively limited", "40", "44", "45", "49"]]),
   choices=[
     "In every age group, the figure for protected rights exceeds the figure for officials answering to voters by at least 17 percentage points",
     "The figure for protected rights exceeds the figure for limited government by at least 20 percentage points in every age group",
     "Only among respondents aged 65 and older does the figure for protected rights exceed the figure for accountability",
     "The gap between the two statements narrows steadily as age increases and closes among the oldest group",
     "Every age group rates accountability higher than it rates the protection of rights"], ans=0,
   why="The row differences are 17, 19, 20 and 21 percentage points, so the smallest is 17 and the claim holds for every group. The gap widens rather than narrows with age, which is what rules out the fourth option."),

 dict(q="The table reports how a hypothetical national sample answered the question “Where does the authority of government ultimately come from?” Which statement about the data is accurate?",
   table=dict(headers=["Response", "2004 (%)", "2014 (%)", "2024 (%)"],
              rows=[["The consent of the people", "62", "58", "55"],
                    ["The Constitution as a written document", "24", "27", "29"],
                    ["Elected officials once in office", "9", "10", "11"],
                    ["Not sure", "5", "5", "5"]]),
   choices=[
     "The share naming the consent of the people fell by 7 percentage points over the period while the share naming the written Constitution rose by 5",
     "The share naming the consent of the people fell below half by 2024",
     "The share naming elected officials more than doubled over the period",
     "Every response category changed by at least 3 percentage points",
     "The three substantive responses were within 10 percentage points of one another in 2024"], ans=0,
   why="62 minus 55 is 7 and 29 minus 24 is 5. The consent figure remains above 50 in 2024, the elected-officials figure rises from 9 to 11 rather than doubling, and “not sure” does not change at all."),

 dict(q="The table reports the share of a hypothetical national sample agreeing that each institution's power is adequately limited. A student concludes that the public sees the courts as the least constrained institution. Which feature of the data most directly supports that conclusion?",
   table=dict(headers=["Institution", "Agree power is adequately limited (%)", "Disagree (%)"],
              rows=[["Congress", "46", "54"],
                    ["The presidency", "38", "62"],
                    ["The federal courts", "35", "65"],
                    ["State governments", "57", "43"]]),
   choices=[
     "The federal courts draw the lowest agreement figure and the highest disagreement figure of the four institutions",
     "The federal courts are the only institution for which disagreement exceeds agreement",
     "Agreement and disagreement for the federal courts differ by fewer than 10 percentage points",
     "State governments and the federal courts draw nearly identical figures",
     "Agreement rises steadily as one reads down the table"], ans=0,
   why="35 is the smallest agreement value and 65 the largest disagreement value in the table. Disagreement also exceeds agreement for Congress and the presidency, so the second option is false; the courts' own two figures differ by 30 points, not fewer than 10."),

 dict(q="A citizen writes that a government which cannot be voted out, cannot be sued, and cannot be overruled by any other institution has stopped being a democracy no matter how wisely it governs. The argument rests most directly on the claim that",
   choices=[
     "limited government requires enforceable external constraints, not merely good intentions",
     "natural rights are created by the government that recognizes them",
     "a social contract is void unless it is written down and ratified",
     "federalism requires that states retain more power than the national government",
     "popular sovereignty means the majority may do whatever it chooses"], ans=0,
   why="The three things the citizen names -- elections, courts, and other institutions -- are all external constraints. The argument is that limited government is a property of the constraints, which is EK 1.1.A.2's claim that the ideal is ensured by the interaction of structural principles."),

 dict(q="Which pairing of a democratic ideal with a constitutional feature is most accurate?",
   choices=[
     "Popular sovereignty and the requirement that the House of Representatives be elected directly by the people",
     "Natural rights and the requirement that revenue bills originate in the House of Representatives",
     "Limited government and the assignment of the power to coin money to Congress",
     "The social contract and the two-year term of a member of the House",
     "Federalism and the requirement that the president be at least thirty-five years old"], ans=0,
   why="Direct popular election of a chamber locates governmental authority in the consent of the people, which is EK 1.1.A.1's definition of popular sovereignty. The other pairings attach an ideal to a provision that does nothing to advance it -- an origination rule and an age qualification are procedural, and a grant of power is not a limit on one."),

 dict(q="A student claims that the four democratic ideals of EK 1.1.A.1 are simply four names for the same thing. Which observation is the strongest objection to that claim?",
   choices=[
     "A government could rest entirely on the consent of the people and still exercise unlimited power over them, so popular sovereignty and limited government are separable",
     "All four ideals appear in the Declaration of Independence, so they must be distinct",
     "The framework lists them in a fixed order, which shows that they differ in importance",
     "Only two of the four are mentioned in the Gettysburg Address",
     "The Constitution uses each of the four terms explicitly at least once"], ans=0,
   why="The objection has to show that two of the ideals can come apart, and majority rule without restraint is exactly that case: authority sourced in the people yet unlimited in scope. Counting mentions in a document shows nothing about whether the concepts are the same."),
]
