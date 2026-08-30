# AP U.S. GOVERNMENT AND POLITICS 1.7 Relationship Between the States and National Government -- 30 questions
# CED V.1 (c) 2026, Unit 1 Foundations of American Democracy.
# Learning objective 1.7.A: explain how the constitutional allocation of power
# between the national and state governments affects society.
#
# Essential knowledge relied on:
#   EK 1.7.A.1 -- federalism is "the system of government in the United States
#     in which power is shared between the national and state governments," and
#     "Federalist No. 39 explains that this division of authority combines
#     national and state features to limit the concentration of power in any one
#     part of the government while also allowing multiple access points for
#     political participation."
#   EK 1.7.A.2 -- EXCLUSIVE power "is held by only one level of government and
#     includes enumerated powers that are written in the Constitution, and
#     implied powers that are not specifically written in the Constitution but
#     are inferred from the Necessary and Proper Clause."
#   EK 1.7.A.3 -- RESERVED powers "are those not delegated or enumerated to the
#     national government but are reserved to the states, as stated in the Tenth
#     Amendment."
#   EK 1.7.A.4 -- CONCURRENT powers "are shared between both levels of
#     government such as the power to collect taxes, the power to make and
#     enforce laws and the power to build roads."
#   EK 1.7.A.5 -- the distribution is demonstrated by four fiscal instruments,
#     and the CED RANKS them, which is course content and not commentary:
#       i.   Revenue sharing -- "almost no restrictions... and is the LEAST USED
#            form of funding"
#       ii.  Block grants -- "minimal restrictions... and is PREFERRED BY THE
#            STATES"
#       iii. Categorical grants -- "restricted to specific categories of
#            expenditures, is PREFERRED BY THE NATIONAL GOVERNMENT, and is the
#            MOST COMMONLY USED form of funding"
#       iv.  Mandates -- "requirements by the national government of the states"
#
# THE THREE FACTS IN EK 1.7.A.5 THAT A STUDENT CANNOT GUESS, and the reason
# items 14 to 18 exist: which grant type each level prefers, and which is most
# and least used, are stated by the framework and are not deducible from the
# definitions. A bank that only defines the three types leaves those three
# claims untested, and they are the ones the exam can ask about.
#
# ONE ORDERING TRAP THIS MODULE AVOIDS: block grants carry MINIMAL restrictions
# and revenue sharing ALMOST NONE, so revenue sharing is the freer of the two.
# The intuitive ranking -- most used equals least restricted -- is backwards
# here: the most restricted instrument, the categorical grant, is the most
# commonly used one.
#
# Documents the CED attaches to 1.7.A (p. 26): the Articles of Confederation,
# Federalist No. 39.
# Required cases the CED attaches to 1.7.A (p. 31-32): McCulloch v. Maryland,
# Baker v. Carr, Shaw v. Reno, United States v. Lopez.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: the Tenth Amendment, the Necessary and
# Proper Clause and the Supremacy Clause are quoted verbatim from the
# constitutional text; Federalist No. 39 is quoted verbatim. The two tables are
# labelled hypothetical, because federal grant outlays by type could not be
# verified against a source here and SOCIAL_BRIEF.md forbids presenting an
# invented figure as fact.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("1.7", "Relationship Between the States and National Government", 1)

_POWERS = ("The table classifies six governmental powers under the constitutional allocation "
           "between the national and state governments.")
_POWERS_TABLE = dict(
    headers=["Power", "Held by the national government", "Held by the state governments"],
    rows=[["Coin money", "Yes", "No"],
          ["Regulate commerce among the states", "Yes", "No"],
          ["Collect taxes", "Yes", "Yes"],
          ["Make and enforce laws", "Yes", "Yes"],
          ["Build roads", "Yes", "Yes"],
          ["Establish public schools", "No", "Yes"]])

_GRANTS = ("In a hypothetical federal system, the table reports the share of all national "
           "funding to the states that flowed through each instrument in two years.")
_GRANTS_TABLE = dict(
    headers=["Instrument", "Share of funding, earlier year (%)", "Share of funding, later year (%)"],
    rows=[["Categorical grants", "68", "72"],
          ["Block grants", "24", "22"],
          ["Revenue sharing", "8", "6"]])

QUESTIONS = [
 dict(q="According to the course framework, federalism is best defined as",
   choices=[
     "the system of government in which power is shared between the national and state governments",
     "the assignment of distinct powers to the legislative, executive and judicial branches",
     "a system in which the national government may exercise only powers expressly written down",
     "a system in which the states may nullify national laws they judge unconstitutional",
     "the practice of electing officials at every level of government"], ans=0,
   why="EK 1.7.A.1 defines federalism in exactly these terms. The second option describes separation of powers, which divides authority among branches rather than between levels."),

 dict(q="Read the following excerpt.\n\n“The proposed Constitution, therefore, is, in strictness, neither a national nor a federal Constitution, but a composition of both.”\n—James Madison, Federalist No. 39, 1788\n\nAccording to the course framework, this division of authority is significant because it",
   choices=[
     "limits the concentration of power in any one part of the government while allowing multiple access points for political participation",
     "guarantees that the national government will prevail in every dispute with a state",
     "assigns every governmental power to one level or the other, with no overlap",
     "makes the state governments the sole judges of the extent of national power",
     "eliminates the need for checks and balances among the branches"], ans=0,
   why="EK 1.7.A.1 credits Federalist No. 39 with exactly this pair of effects. The third option contradicts EK 1.7.A.4, which names concurrent powers held at both levels."),

 dict(q="Which of the following is an EXCLUSIVE power of the national government as the course framework uses the term?",
   choices=[
     "The power to coin money",
     "The power to collect taxes",
     "The power to make and enforce laws",
     "The power to build roads",
     "The power to establish public schools"], ans=0,
   why="EK 1.7.A.2 defines an exclusive power as one held by only one level of government, and EK 1.7.A.4 names taxation, lawmaking and road building as concurrent. Coinage is denied to the states by Article I Section 10."),

 dict(q="According to the course framework, an implied power is one that",
   choices=[
     "is not specifically written in the Constitution but is inferred from the Necessary and Proper Clause",
     "is written into the Constitution in so many words",
     "is reserved to the states by the Tenth Amendment",
     "is exercised jointly by the national and state governments",
     "may be exercised only with the consent of a majority of the states"], ans=0,
   why="EK 1.7.A.2 states this definition verbatim, and it places implied powers inside the category of EXCLUSIVE powers rather than outside it. An enumerated power is the one written in the text."),

 dict(q="Read the following excerpt.\n\n“The Congress shall have Power... To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers, and all other Powers vested by this Constitution in the Government of the United States.”\n—U.S. Constitution, Article I, Section 8\n\nWhich statement about this clause is most accurate?",
   choices=[
     "It is the textual source of implied powers, since it authorizes means not themselves listed for carrying out powers that are",
     "It grants Congress a general power to legislate on any subject it chooses",
     "It reserves to the states all powers not written in the Constitution",
     "It gives the president authority to execute laws Congress has not passed",
     "It bars Congress from exercising any power not written in the text"], ans=0,
   why="The clause attaches to 'the foregoing Powers,' so it supplies means for enumerated ends rather than a freestanding grant, which is why EK 1.7.A.2 calls implied powers inferences from it. The last option states the Articles of Confederation's express-delegation rule."),

 dict(q="Read the following excerpt.\n\n“The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people.”\n—U.S. Constitution, Tenth Amendment\n\nThis provision is the textual source of which category of power?",
   choices=[
     "Reserved powers, which belong to the states because they were not delegated to the national government",
     "Implied powers, which are inferred from the Necessary and Proper Clause",
     "Concurrent powers, which both levels of government exercise",
     "Enumerated powers, which are written into Article I",
     "Exclusive powers of the national government"], ans=0,
   why="EK 1.7.A.3 defines reserved powers as those not delegated or enumerated to the national government but reserved to the states 'as stated in the Tenth Amendment,' which is this text."),

 dict(q="Which of the following is a CONCURRENT power as the course framework uses the term?",
   choices=[
     "The power to collect taxes",
     "The power to coin money",
     "The power to regulate commerce among the states",
     "The power to conduct foreign relations",
     "The power to declare war"], ans=0,
   why="EK 1.7.A.4 names the power to collect taxes, to make and enforce laws, and to build roads as its examples of powers shared between both levels. The other four options are exercised by the national government alone."),

 dict(q="A state establishes a police force, levies a sales tax, and maintains a highway system. Which of these activities rests on a power the state does NOT share with the national government?",
   choices=[
     "None of them, since law enforcement, taxation and road building are all concurrent powers",
     "The police force only, because criminal law is reserved to the states",
     "The sales tax only, because the national government may not tax consumption",
     "The highway system only, because roads are a purely local matter",
     "All three, because state powers and national powers never overlap"], ans=0,
   why="EK 1.7.A.4 names precisely these three -- collecting taxes, making and enforcing laws, and building roads -- as its examples of concurrent powers, so each is shared rather than exclusive."),

 dict(q="Which pairing of a power with its category is correct under the course framework?",
   choices=[
     "Establishing public schools, with the reserved powers of the states",
     "Coining money, with the concurrent powers of both levels",
     "Collecting taxes, with the exclusive powers of the national government",
     "Regulating commerce among the states, with the reserved powers of the states",
     "Building roads, with the exclusive powers of the state governments"], ans=0,
   why="Education is not delegated to the national government and is therefore reserved to the states under EK 1.7.A.3. Coinage is exclusive, taxation and road building are concurrent, and interstate commerce is a national power."),

 dict(q="In McCulloch v. Maryland (1819), the Supreme Court upheld Congress's power to charter a national bank and held that Maryland could not tax it, establishing the supremacy of the U.S. Constitution and federal laws over state laws. Which two categories from the course framework does the decision most directly involve?",
   choices=[
     "Implied powers, since chartering a bank is not enumerated, and the supremacy of national law over a conflicting state law",
     "Reserved powers and concurrent powers, since both levels may charter corporations",
     "Enumerated powers only, since the power to charter a bank appears in Article I Section 8",
     "Concurrent powers only, since both levels may levy taxes on the same institution",
     "Reserved powers only, since banking was not mentioned at the Convention"], ans=0,
   why="No clause enumerates a power to charter a bank, so the authority is implied under EK 1.7.A.2, and the CED states the holding as establishing supremacy of federal law over state law. The third option asserts an enumeration that does not exist."),

 dict(q="In United States v. Lopez (1995), the Supreme Court held that Congress exceeded its power under the Commerce Clause when it made possession of a gun in a school zone a federal crime. What does the decision establish about the allocation of power between the levels?",
   choices=[
     "That the national government's enumerated powers have judicially enforceable limits, beyond which a subject remains with the states",
     "That the Commerce Clause gives Congress no authority over economic activity",
     "That the states may regulate firearms only with the permission of Congress",
     "That the Tenth Amendment was repealed by the Commerce Clause",
     "That the Supreme Court may not review acts of Congress for constitutionality"], ans=0,
   why="The CED states the holding as Congress exceeding its Commerce Clause power in this instance, which marks a boundary rather than abolishing the power. Beyond that boundary the subject falls within the reserved powers of EK 1.7.A.3."),

 dict(q="A non-required case: Congress enacts a statute making it a federal offense to possess a certain item within a specified distance of a public library, citing the Commerce Clause but making no findings about any effect on commerce. A federal court strikes the statute down. Which required case is the closest precedent, and why?",
   choices=[
     "United States v. Lopez (1995), because the Court there held that Congress exceeded its Commerce Clause power in criminalizing gun possession in a school zone",
     "McCulloch v. Maryland (1819), because the Court there upheld an implied power of Congress",
     "Baker v. Carr (1962), because the Court there held that redistricting does not raise political questions",
     "Shaw v. Reno (1993), because the Court there allowed challenges to majority-minority districts drawn solely on race",
     "Marbury v. Madison (1803), because the Court there established judicial review"], ans=0,
   why="The fact patterns match almost exactly: a federal criminal statute about possession near a public institution, justified under the Commerce Clause. Marbury supplies the court's authority to decide the question but not the rule that decides it."),

 dict(q="In Shaw v. Reno (1993), the Supreme Court held that majority-minority districts created under the Voting Rights Act of 1965 may be constitutionally challenged by voters if race is the only factor used in creating the district. Which feature of the federal system does the case illustrate?",
   choices=[
     "The national government may enforce constitutional limits on how a state exercises a power the state otherwise controls",
     "The drawing of legislative districts is an exclusive power of the national government",
     "The states may disregard national statutes that affect elections",
     "Federal courts may not hear cases arising from state districting decisions",
     "The Voting Rights Act transferred districting from the states to Congress"], ans=0,
   why="Districting is a state function, and the holding subjects it to a national constitutional limit under the Fourteenth Amendment's Equal Protection Clause. The fourth option is refuted by Baker v. Carr, which made such cases justiciable."),

 dict(q="According to the course framework, which form of national funding to the states carries almost no restrictions on how the money is used and is the least used?",
   choices=[
     "Revenue sharing",
     "Categorical grants",
     "Block grants",
     "Mandates",
     "Concurrent appropriations"], ans=0,
   why="EK 1.7.A.5.i describes revenue sharing as national funding with almost no restrictions and as the least used form of funding. Both halves of that sentence are course content."),

 dict(q="According to the course framework, which form of national funding is restricted to specific categories of expenditure, is preferred by the national government, and is the most commonly used?",
   choices=[
     "Categorical grants",
     "Block grants",
     "Revenue sharing",
     "Mandates",
     "Reserved appropriations"], ans=0,
   why="EK 1.7.A.5.iii states all three of these facts about categorical grants. The most restricted instrument being the most used is the framework's own claim and is not deducible from the definitions."),

 dict(q="Which form of national funding does the course framework identify as preferred by the STATES?",
   choices=[
     "Block grants, which carry minimal restrictions on their use",
     "Categorical grants, which are restricted to specific categories of expenditure",
     "Mandates, which are requirements imposed by the national government",
     "Revenue sharing, which the framework identifies as the most commonly used",
     "Matching grants, which require the states to contribute their own funds"], ans=0,
   why="EK 1.7.A.5.ii names block grants as preferred by the states and describes them as carrying minimal restrictions. Revenue sharing is the LEAST used form, so the fourth option misstates the framework."),

 dict(q="A governor argues that her state should receive its national education funding as a lump sum with only broad conditions, rather than as separate awards each tied to a named program. Which instrument is she asking for, and which does she want to replace?",
   choices=[
     "She wants block grants in place of categorical grants",
     "She wants categorical grants in place of block grants",
     "She wants mandates in place of revenue sharing",
     "She wants revenue sharing in place of mandates",
     "She wants matching grants in place of block grants"], ans=0,
   why="Minimal restrictions and broad purposes describe the block grant of EK 1.7.A.5.ii, and funding tied to named programs is the categorical grant of EK 1.7.A.5.iii. Her preference is the one the framework says the states hold generally."),

 dict(q="Congress requires every state to adopt a uniform standard for driver licensing but appropriates no money to pay for the change. According to the course framework, this instrument is best described as",
   choices=[
     "a mandate, a requirement by the national government of the states",
     "a categorical grant, since it names a specific area of expenditure",
     "a block grant, since it leaves the states discretion in implementation",
     "revenue sharing, since no restrictions accompany the funds",
     "an exclusive power, since licensing drivers is enumerated in Article I"], ans=0,
   why="EK 1.7.A.5.iv defines a mandate as a requirement by the national government of the states, and the defining feature here is a requirement without accompanying funds, so none of the three grant types applies."),

 dict(q="Which observation would best support an argument that national grant conditions have shifted power toward the national government even in areas the Constitution reserves to the states?",
   choices=[
     "States adopt policies they would not otherwise have chosen in order to remain eligible for funds they have come to depend on",
     "States retain the legal authority to decline any grant offered to them",
     "The Tenth Amendment reserves to the states the powers not delegated to the national government",
     "Grants are appropriated by Congress rather than by the executive branch",
     "The number of separate grant programs has changed over time"], ans=0,
   why="The argument is about influence exercised through conditions rather than through legal compulsion, so the evidence has to be states changing behavior to keep funding. The formal right to decline is the fact the argument concedes rather than the fact that supports it."),

 dict(q="A state legalizes an activity that remains a federal crime, and federal officers continue to enforce the federal statute within that state. Which constitutional provision most directly explains why they may do so?",
   choices=[
     "The Supremacy Clause, which makes the Constitution and federal laws made in pursuance of it the supreme law of the land",
     "The Tenth Amendment, which reserves undelegated powers to the states",
     "The Necessary and Proper Clause, which lets Congress carry its enumerated powers into execution",
     "The Full Faith and Credit Clause, which requires each state to honor the acts of the others",
     "The Commerce Clause, which gives Congress power over commerce among the states"], ans=0,
   why="A conflict between a valid federal law and a contrary state policy is resolved by the Supremacy Clause, which is the rule McCulloch v. Maryland applied. The Commerce Clause may be the SOURCE of the federal statute but is not what settles the conflict."),

 dict(q=_POWERS + " Which conclusion is best supported by the table?",
   table=_POWERS_TABLE,
   choices=[
     "Three of the six powers are held by both levels, and the remaining three are held by one level only",
     "Every power in the table is held by both levels of government",
     "The national government holds every power in the table",
     "No power in the table is held by the states alone",
     "The state governments hold more of the listed powers than the national government does"], ans=0,
   why="Taxation, lawmaking and road building are marked yes in both columns; coinage and interstate commerce are national only, and public schools are state only. The national column carries five yes entries and the state column four, so the states do not hold more of the listed powers."),

 dict(q=_POWERS + " Which row of the table illustrates a RESERVED power as the course framework defines the term?",
   table=_POWERS_TABLE,
   choices=[
     "Establish public schools, which the states hold and the national government does not",
     "Coin money, which the national government holds and the states do not",
     "Collect taxes, which both levels hold",
     "Regulate commerce among the states, which the national government holds",
     "Build roads, which both levels hold"], ans=0,
   why="EK 1.7.A.3 defines a reserved power as one not delegated to the national government but reserved to the states, which is the pattern of a row marked no for the national column and yes for the state column."),

 dict(q=_POWERS + " A student concludes from the table that the two levels of government are equally powerful. Which limitation of the data most undercuts that conclusion?",
   table=_POWERS_TABLE,
   choices=[
     "The table counts powers without weighing them, and the powers it lists differ enormously in reach and consequence",
     "The table omits the state governments entirely, so no comparison is possible",
     "The table lists every power in the Constitution, so no further evidence exists",
     "The table reports survey responses rather than constitutional provisions",
     "The table contains no row in which the two levels differ"], ans=0,
   why="Counting rows treats the power to coin money and the power to build roads as equivalent, which is the flaw in any tally of unweighted categories. Three rows plainly differ between the columns, and the state column is present."),

 dict(q=_GRANTS + " Which conclusion is best supported by the data?",
   table=_GRANTS_TABLE,
   choices=[
     "The most restricted instrument grew as a share of funding while the two less restricted instruments shrank",
     "Every instrument's share of funding increased between the two years",
     "Block grants accounted for a majority of funding in both years",
     "Revenue sharing was the largest of the three instruments in the earlier year",
     "The three shares together account for less than half of national funding to the states"], ans=0,
   why="Categorical grants, the instrument EK 1.7.A.5.iii describes as restricted to specific categories, rise from 68 to 72 percent while block grants and revenue sharing both fall. The three shares sum to 100 in each year."),

 dict(q=_GRANTS + " Which statement in the course framework do the data most directly illustrate?",
   table=_GRANTS_TABLE,
   choices=[
     "That categorical grants are the most commonly used form of funding and revenue sharing the least used",
     "That block grants are preferred by the national government",
     "That mandates are the largest source of national funding to the states",
     "That revenue sharing carries the most restrictive conditions of the three",
     "That the states prefer categorical grants to block grants"], ans=0,
   why="EK 1.7.A.5 ranks the instruments, and the table shows categorical grants largest and revenue sharing smallest in both years, which is that ranking. The other four options each reverse one of the framework's own claims."),

 dict(q=_GRANTS + " A state official argues that the data show the states losing discretion over how national funds are spent. Which feature of the data most directly supports that argument?",
   table=_GRANTS_TABLE,
   choices=[
     "The share flowing through the instrument with the tightest conditions rose by four percentage points while the freest instrument fell to six percent",
     "All three instruments are represented in both years",
     "Revenue sharing changed by a smaller number of percentage points than categorical grants did",
     "The two years are reported side by side rather than as a longer series",
     "Block grants remain larger than revenue sharing in both years"], ans=0,
   why="The claim is about discretion, so the supporting evidence must pair the direction of change with how restrictive each instrument is: the most restricted rises and the least restricted falls to the smallest share in the table. The other options are true and say nothing about conditions on the money."),

 dict(q="Which argument would a critic of an expanding national role in areas traditionally left to the states most likely make, using the course framework's own categories?",
   choices=[
     "That funding conditions and mandates let the national government direct outcomes in fields the Tenth Amendment reserves to the states",
     "That the Necessary and Proper Clause has been read too narrowly by the courts",
     "That concurrent powers should be eliminated so that each level acts alone",
     "That the states should be permitted to coin their own money",
     "That the Supremacy Clause should apply only to treaties"], ans=0,
   why="The critic's complaint uses EK 1.7.A.5's instruments to reach EK 1.7.A.3's reserved powers, which is the framework's own vocabulary for that argument. The remaining options propose changes no participant in this debate advances."),

 dict(q="Federalist No. 39 argues that the proposed Constitution combines national and state features. Which pair of constitutional provisions best illustrates that combination?",
   choices=[
     "The House apportioned by population, alongside the Senate representing each state equally",
     "The presidential veto, alongside the congressional override",
     "The Necessary and Proper Clause, alongside the Supremacy Clause",
     "Judicial review, alongside life tenure for federal judges",
     "The Bill of Rights, alongside the amendment process of Article V"], ans=0,
   why="EK 1.7.A.1 credits Federalist No. 39 with explaining that the division of authority combines national and state features, and Congress's two chambers carry the two principles at once. The other four pairs illustrate checks and balances or judicial independence rather than the national/state combination."),

 dict(q="Which of the following is the best evidence for EK 1.7.A.1's claim that federalism allows multiple access points for political participation?",
   choices=[
     "A group defeated on an issue in its state legislature can pursue the same goal in Congress, in another state, or in federal court",
     "Every citizen may vote in national elections once every four years",
     "The national government may set uniform standards that apply in all states",
     "State constitutions may be amended more easily than the national Constitution",
     "The national government employs more officials than any single state government"], ans=0,
   why="An access point is a place where a claim can be pressed, and having two levels of government plus courts at each multiplies those places. Uniform national standards and relative employment figures speak to national capacity rather than to participation."),

 dict(q="A student writes that federalism means the national government and the states each have their own separate sphere and never overlap. Which correction does the course framework most directly support?",
   choices=[
     "Some powers are exercised by both levels at once, which the framework calls concurrent powers",
     "The national government exercises every power, and the states administer its decisions",
     "The states exercise every power not exercised by local governments",
     "The two levels overlap only in the area of foreign relations",
     "Overlap between the levels was eliminated by the Tenth Amendment"], ans=0,
   why="EK 1.7.A.4 defines concurrent powers as shared between both levels and names taxation, lawmaking and road building as examples, so overlap is part of the design rather than a defect in it."),
]
