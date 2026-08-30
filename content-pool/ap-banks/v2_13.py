# AP U.S. GOVERNMENT AND POLITICS 2.13 Discretionary and Rulemaking Authority -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# Learning objective 2.13.A: explain how the federal bureaucracy uses DELEGATED
# discretionary authority for rulemaking and implementation.
# Suggested skill for this topic (CED p. 73): 1.D, describe political
# principles, institutions, processes, policies and behaviors ILLUSTRATED IN
# DIFFERENT SCENARIOS IN CONTEXT.
#
# Essential knowledge relied on. ONE statement, and it ends in a list of seven
# named agencies that are REQUIRED COURSE CONTENT rather than illustrative
# examples -- which is unusual and is why items 15 to 21 name them:
#   EK 2.13.A.1 -- "The federal bureaucracy uses DISCRETIONARY POWER AS
#     DELEGATED BY CONGRESS to interpret and implement policies. Through their
#     RULEMAKING AUTHORITY, federal bureaucratic agencies utilize their
#     discretion to create and enforce regulations. Bureaucratic agencies
#     include:
#       i.   Department of Homeland Security
#       ii.  Department of Transportation
#       iii. Department of Veterans Affairs
#       iv.  Department of Education
#       v.   Environmental Protection Agency (EPA)
#       vi.  Federal Elections Commission (FEC)
#       vii. Securities and Exchange Commission (SEC)"
#
# THE WORD "DELEGATED" IS THE WHOLE TOPIC, and items 1 to 8 are built on it.
# Discretion here is not an inherent executive power and not something an agency
# claims for itself; it is authority Congress HANDED OVER, which means Congress
# can define it narrowly, define it broadly, or take it back. A student who
# thinks agencies simply have discretion cannot explain why the same agency has
# wide latitude in one field and none in another.
#
# THE SECOND SENTENCE ADDS THE MECHANISM: rulemaking. Discretion is exercised by
# CREATING AND ENFORCING REGULATIONS, which is how a statute in general terms
# becomes a rule a particular firm must follow. Items 9 to 14 turn on the gap
# between what a statute says and what an agency must decide to apply it.
#
# ON THE AGENCY NAMES: the CED writes "Federal Elections Commission (FEC)". The
# agency's own legal name is the Federal Election Commission, singular. This
# module uses the CED's wording where it names the framework's list, because
# that is the examinable text, and no item turns on the difference.
#
# Documents the CED attaches to 2.13.A (p. 26-27): Federalist No. 70.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: constitutional text is quoted verbatim.
# Statutory language in scenarios is invented and labelled as hypothetical, and
# no item attributes a quotation to a real statute. Both tables are labelled
# hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. The
# verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.13", "Discretionary and Rulemaking Authority", 2)

_LATITUDE = ("In a hypothetical study, the table reports how much discretion four statutes "
             "left to the agency charged with implementing them, and how many pages of "
             "regulations the agency issued under each.")
_LATITUDE_TABLE = dict(
    headers=["Statute", "Standard the statute set", "Pages of regulation issued"],
    rows=[["Statute A", "A specific numerical limit", "14"],
          ["Statute B", "A list of prohibited practices", "62"],
          ["Statute C", "Whatever is reasonably necessary", "410"],
          ["Statute D", "Whatever serves the public interest", "588"]])

_RULEMAKING = ("In a hypothetical study, the table reports what happened to proposed rules at "
               "each stage of one agency's rulemaking process over five years.")
_RULEMAKING_TABLE = dict(
    headers=["Stage", "Proposed rules remaining"],
    rows=[["Proposed and published for comment", "340"],
          ["Revised after public comment", "227"],
          ["Issued as a final rule", "198"],
          ["Still in force after judicial challenge", "181"]])

QUESTIONS = [
 dict(q="According to the course framework, the discretionary power the federal bureaucracy uses is",
   choices=[
     "delegated by Congress",
     "granted directly by Article II of the Constitution",
     "claimed by each agency for itself",
     "conferred by the federal courts",
     "reserved to the agencies by the Tenth Amendment"], ans=0,
   why="EK 2.13.A.1 says the bureaucracy uses discretionary power AS DELEGATED BY CONGRESS. That word is the topic: the authority is handed over rather than inherent."),

 dict(q="What follows from the fact that an agency's discretion is delegated rather than inherent?",
   choices=[
     "Congress can narrow it, broaden it, or withdraw it by changing the statute",
     "The agency may expand its own discretion by issuing a regulation",
     "Only a constitutional amendment can change the agency's authority",
     "The president may transfer the discretion to a different branch",
     "The courts may grant an agency additional discretion when they think it useful"], ans=0,
   why="If the source of the authority is a statute, then the body that wrote the statute controls its scope. EK 2.11.B.1.i records the same logic for decisions: what legislation created, legislation can modify."),

 dict(q="According to the course framework, agencies use discretionary power to",
   choices=[
     "interpret and implement policies",
     "enact statutes without congressional involvement",
     "declare statutes unconstitutional",
     "appropriate funds for their own operations",
     "confirm the president's nominees"], ans=0,
   why="EK 2.13.A.1's verbs are INTERPRET and IMPLEMENT, which are the two things an agency does with a statute it did not write. The other options name powers belonging to Congress or the courts."),

 dict(q="A statute directs an agency to set standards that are 'adequate to protect the public,' without saying what is adequate. What has Congress done?",
   choices=[
     "Delegated broad discretion, since the agency must decide what the standard means before it can be applied",
     "Delegated no discretion, since the statute states a standard",
     "Transferred its legislative power permanently to the agency",
     "Required the agency to obtain the president's approval for each decision",
     "Directed the courts to write the standard instead"], ans=0,
   why="A general standard is a decision Congress declined to make, so it is a decision the agency must make, which is EK 2.13.A.1's discretion. The statute remains Congress's and can be rewritten."),

 dict(q="A statute directs an agency to prohibit a specific substance in quantities above a stated numerical limit. How much discretion has Congress delegated?",
   choices=[
     "Very little, since the statute has already made the decision the agency would otherwise make",
     "A great deal, since any statute requires interpretation",
     "None at all, since agencies never exercise discretion",
     "All of it, since the agency enforces the statute",
     "The same amount as a statute using a general standard"], ans=0,
   why="Discretion is what a statute leaves open, so a statute that fixes the number leaves little. Contrast EK 2.13.A.1's general delegations, where the agency must supply the content."),

 dict(q="Why does the same agency sometimes have wide latitude and sometimes almost none?",
   choices=[
     "Because the amount of discretion depends on how specifically the particular statute is written",
     "Because agencies choose how much discretion to exercise in each field",
     "Because the president assigns each agency a level of discretion annually",
     "Because the courts assign discretion case by case",
     "Because discretion is fixed by the size of the agency's budget"], ans=0,
   why="EK 2.13.A.1 makes the source of discretion a delegation, so the scope varies with the delegating statute rather than with anything about the agency itself."),

 dict(q="Which of the following best explains why Congress delegates discretion to agencies at all?",
   choices=[
     "Legislators cannot anticipate every situation a statute must cover, and agencies have the specialized staff to work out the details",
     "The Constitution requires Congress to delegate all technical questions",
     "Delegation allows Congress to avoid responsibility for any outcome",
     "Agencies would otherwise have no work to do",
     "Delegation is the only way to make a statute constitutional"], ans=0,
   why="Specialization is the reason a general legislature hands technical implementation to a permanent staff, which connects EK 2.13.A.1 to EK 2.12.A.2's merit criteria. Nothing in the Constitution requires delegation."),

 dict(q="Which is the strongest objection to broad delegations of discretion?",
   choices=[
     "Decisions with major consequences are made by officials the voters did not choose and cannot remove",
     "Agencies are prohibited from employing specialists",
     "Broad delegations prevent Congress from legislating at all",
     "Broad delegations require a constitutional amendment",
     "Broad delegations transfer the discretion to the courts"], ans=0,
   why="The democratic objection is the serious one and it follows from the delegation itself: the more a statute leaves open, the more is settled by unelected officials. The other options assert falsehoods about the system."),

 dict(q="According to the course framework, how do agencies exercise their discretion in practice?",
   choices=[
     "Through their rulemaking authority, by creating and enforcing regulations",
     "By issuing advisory opinions that carry no legal effect",
     "By voting on statutes alongside members of Congress",
     "By deciding appeals from the federal courts",
     "By negotiating agreements with foreign governments"], ans=0,
   why="EK 2.13.A.1's second sentence says agencies use their discretion 'to create and enforce regulations' through their rulemaking authority. The other options name activities of other branches."),

 dict(q="What is the relationship between a statute and a regulation issued under it?",
   choices=[
     "The regulation supplies operative detail the statute left open, and it must stay within what the statute authorizes",
     "The regulation replaces the statute once it takes effect",
     "The regulation may authorize what the statute forbids",
     "The regulation and the statute are enacted by the same body",
     "The regulation binds only the agency that issued it"], ans=0,
   why="EK 2.13.A.1 makes rulemaking an exercise of DELEGATED discretion, which means the delegation bounds it. A regulation exceeding the statute is the fact pattern judicial review addresses."),

 dict(q="An agency issues a regulation requiring a form of reporting the statute does not mention but that is necessary to determine whether the statute's requirements are met. Is the regulation within the agency's authority?",
   choices=[
     "Probably yes, since implementing a statutory requirement includes the means of determining compliance",
     "No, since a regulation may address only what the statute mentions by name",
     "No, since agencies may not require anything of private parties",
     "Yes, since agencies may require anything they consider useful",
     "The question cannot be answered, since regulations are not reviewable"], ans=0,
   why="EK 2.13.A.1's discretion is to interpret and implement, and a reporting requirement serving the statute's own standard is implementation. The fourth option drops the boundary the delegation creates."),

 dict(q="Why does the framework treat rulemaking as a form of policymaking rather than as mere administration?",
   choices=[
     "The choices an agency makes in writing a rule determine what the statute actually requires of anyone",
     "Agencies are permitted to disregard statutes they consider unwise",
     "Regulations are enacted by a vote of both chambers of Congress",
     "Rulemaking is conducted by elected officials",
     "Regulations may be issued only when Congress is out of session"], ans=0,
   why="EK 2.13.A.1 says agencies 'utilize their discretion' in rulemaking, and a discretionary choice about what a general standard means is a policy choice. The remaining options assert things that are false of the process."),

 dict(q="An agency reverses a regulation issued by a previous administration under the same statute. What does that possibility show about delegated discretion?",
   choices=[
     "Where a statute leaves a question open, the answer can change with the officials exercising the discretion",
     "Regulations are permanent once issued",
     "The statute must have been amended for the regulation to change",
     "Agencies may not consider the administration's priorities at all",
     "Only Congress may withdraw a regulation"], ans=0,
   why="EK 2.14.B.1 says presidential ideology, authority and influence affect how agencies carry out the administration's goals, and EK 2.13.A.1's discretion is the room in which that happens."),

 dict(q="Which of the following is NOT among the agencies the course framework lists as bureaucratic agencies?",
   choices=[
     "The Federal Reserve Board",
     "The Environmental Protection Agency",
     "The Securities and Exchange Commission",
     "The Department of Homeland Security",
     "The Department of Veterans Affairs"], ans=0,
   why="EK 2.13.A.1's list names Homeland Security, Transportation, Veterans Affairs, Education, the EPA, the Federal Elections Commission and the SEC. The Federal Reserve is not on it."),

 dict(q="An agency on the framework's list writes rules governing how publicly traded companies must report their finances to investors. Which agency is it?",
   choices=[
     "The Securities and Exchange Commission",
     "The Environmental Protection Agency",
     "The Department of Transportation",
     "The Department of Education",
     "The Federal Elections Commission"], ans=0,
   why="EK 2.13.A.1.vii names the Securities and Exchange Commission, whose subject matter is securities and the disclosure obligations of companies that issue them."),

 dict(q="An agency on the framework's list writes rules setting limits on emissions from industrial facilities. Which agency is it?",
   choices=[
     "The Environmental Protection Agency",
     "The Department of Homeland Security",
     "The Securities and Exchange Commission",
     "The Department of Veterans Affairs",
     "The Federal Elections Commission"], ans=0,
   why="EK 2.13.A.1.v names the Environmental Protection Agency, and emissions limits are the paradigm case of the discretion an environmental statute delegates."),

 dict(q="An agency on the framework's list writes rules governing how candidates and committees must report the money they raise and spend. Which agency is it?",
   choices=[
     "The Federal Elections Commission",
     "The Department of Education",
     "The Department of Transportation",
     "The Environmental Protection Agency",
     "The Department of Homeland Security"], ans=0,
   why="EK 2.13.A.1.vi names the Federal Elections Commission, whose subject is campaign finance reporting and the rules built on it."),

 dict(q="Which pairing of an agency from the framework's list with a plausible subject of its regulations is correct?",
   choices=[
     "The Department of Transportation, with standards for commercial vehicle operation",
     "The Department of Education, with emissions from power plants",
     "The Environmental Protection Agency, with the disclosure obligations of stock issuers",
     "The Securities and Exchange Commission, with benefits for former service members",
     "The Department of Veterans Affairs, with campaign finance reporting"], ans=0,
   why="EK 2.13.A.1.ii names the Department of Transportation, and vehicle operating standards fall within its subject. Each other option attaches a subject to the wrong agency on the same list."),

 dict(q="Why does the framework list agencies of two different kinds, departments and independent commissions, in the same statement?",
   choices=[
     "Both exercise delegated discretion through rulemaking, which is the property the statement is about",
     "Departments make rules and commissions do not",
     "Commissions are part of the legislative branch",
     "Departments are created by the Constitution and commissions by statute",
     "Only commissions may enforce the rules they write"], ans=0,
   why="EK 2.13.A.1's subject is discretionary rulemaking, and the list is of bodies that do it; EK 2.12.A.1 separately notes that the bureaucracy contains departments, agencies, commissions and government corporations."),

 dict(q="Read the following excerpt.\n\n“He shall take Care that the Laws be faithfully executed.”\n—U.S. Constitution, Article II, Section 3\n\nHow does delegated rulemaking fit with this clause?",
   choices=[
     "Agencies exercising delegated discretion are executing the laws, and the president is responsible for how they do it",
     "The clause gives agencies authority independent of both Congress and the president",
     "The clause is the source of the discretion agencies exercise",
     "The clause forbids Congress from delegating any authority",
     "The clause requires that all regulations be approved by the courts"], ans=0,
   why="The Take Care Clause makes execution the president's responsibility, while EK 2.13.A.1 makes the discretion's SOURCE a congressional delegation. Both are true at once, which is why the bureaucracy answers to both branches."),

 dict(q=_LATITUDE + " Which conclusion is best supported by the data?",
   table=_LATITUDE_TABLE,
   choices=[
     "The two statutes setting general standards produced far more regulation than the two setting specific ones",
     "The statute setting a numerical limit produced the most regulation",
     "The four statutes produced similar amounts of regulation",
     "The statute using the phrase about the public interest produced the least regulation",
     "The amount of regulation fell as the standard became more general"], ans=0,
   why="The two specific statutes produced 14 and 62 pages against 410 and 588 for the two general ones. The public interest statute produced the most, and the numerical limit the least."),

 dict(q=_LATITUDE + " Which claim from the course framework do these data most directly illustrate?",
   table=_LATITUDE_TABLE,
   choices=[
     "That the discretion an agency exercises is delegated by the statute, so its extent varies with how the statute is written",
     "That agencies choose for themselves how much discretion to exercise",
     "That the civil service uses a merit system",
     "That iron triangles form in specific policy areas",
     "That Congress oversees agencies through committee hearings"], ans=0,
   why="EK 2.13.A.1 makes discretion a function of the delegation, and a table pairing the specificity of a standard with the volume of regulation is that relationship measured."),

 dict(q=_LATITUDE + " A student concludes that the agency was most powerful under the statute producing the most pages. Which limitation of the data most undercuts that conclusion?",
   table=_LATITUDE_TABLE,
   choices=[
     "Pages of regulation measure volume, not significance, and a short rule may impose a far heavier obligation than a long one",
     "The table omits the standard each statute set, so no comparison is possible",
     "The table covers a single statute, so no comparison is possible",
     "The table reports percentages that do not sum to one hundred",
     "The table gives no information about how many pages were issued"], ans=0,
   why="Counting pages is an unweighted measure of output, which is the standard limitation. The standard column, four statutes and the page counts are all plainly present."),

 dict(q=_RULEMAKING + " Which conclusion is best supported by the data?",
   table=_RULEMAKING_TABLE,
   choices=[
     "Most proposed rules survived to become final, and most final rules survived judicial challenge",
     "Most proposed rules were abandoned before becoming final",
     "Every proposed rule became a final rule",
     "Judicial challenge removed more rules than the comment stage did",
     "No proposed rule was revised after public comment"], ans=0,
   why="198 of 340 proposed rules became final, a majority, and 181 of those 198 survived challenge. The comment stage accounts for the largest loss, and 227 rules were revised."),

 dict(q=_RULEMAKING + " Which feature of the process do these data most directly illustrate?",
   table=_RULEMAKING_TABLE,
   choices=[
     "Rulemaking is a constrained exercise of discretion, since a proposed rule must survive comment and may be challenged in court",
     "Agencies may issue any regulation they choose without review",
     "Congress approves each regulation before it takes effect",
     "The president personally reviews each proposed rule",
     "Regulations take effect only after a vote of the affected industry"], ans=0,
   why="EK 2.13.A.1's discretion operates within a process, and a table showing attrition at a comment stage and at a judicial stage is that constraint. The other options describe procedures that do not exist."),

 dict(q=_RULEMAKING + " A student concludes that judicial review is a weak check on agency rulemaking because most rules survived it. Which limitation of the data most complicates that conclusion?",
   table=_RULEMAKING_TABLE,
   choices=[
     "An agency that expects a challenge may write a narrower rule in the first place, which the table cannot show",
     "The table omits the number of rules challenged, so no rate can be computed",
     "The table covers a single rule, so no pattern can be observed",
     "The table reports percentages that do not sum to one hundred",
     "The table gives no information about whether any rule was issued"], ans=0,
   why="A survival rate measures only the rules an agency chose to issue, and anticipation is invisible to it -- the same limitation as any count of enforcement outcomes. Four stages and the counts are plainly present."),

 dict(q="Which scenario best illustrates the difference between interpreting a statute and implementing it?",
   choices=[
     "An agency first decides what a statute's general term means, then writes rules telling regulated parties what to do about it",
     "An agency asks Congress to clarify a statute and waits for an answer",
     "An agency refers a statute to the courts before applying it",
     "An agency enforces a statute without issuing any regulation",
     "An agency drafts a bill for a member of Congress to introduce"], ans=0,
   why="EK 2.13.A.1 names both verbs, and they are sequential: deciding what a term means is interpretation, and turning that meaning into operative requirements is implementation."),

 dict(q="Congress becomes dissatisfied with how an agency has used its discretion. Which response addresses the source of the problem most directly?",
   choices=[
     "Amending the statute to specify what the agency must do, narrowing the delegation",
     "Asking the courts to issue an advisory opinion on the agency's rules",
     "Directing the president to remove the agency's career staff",
     "Passing a resolution expressing disapproval of the agency's rules",
     "Waiting for the next election to change the agency's leadership"], ans=0,
   why="EK 2.13.A.1 makes the discretion a creature of the statute, so rewriting the statute reaches its source. Federal courts issue no advisory opinions, and a resolution expressing disapproval changes no authority."),

 dict(q="Which question would best measure how much discretion a particular statute delegates?",
   choices=[
     "How many of the decisions needed to apply the statute does the statute itself make, and how many does it leave to the agency?",
     "How many pages does the statute run to?",
     "How many members of Congress voted for the statute?",
     "How many agencies are named in the statute?",
     "How long did the statute take to pass?"], ans=0,
   why="Discretion is what a statute leaves open, so the measure has to count the decisions the text does not make. Length, vote margin and passage time measure other things entirely."),

 dict(q="Which statement best summarizes EK 2.13.A.1?",
   choices=[
     "Congress delegates discretion to agencies, which exercise it by creating and enforcing regulations that interpret and implement the statute",
     "Agencies possess inherent authority to make binding rules on any subject",
     "Congress writes all regulations and agencies merely enforce them",
     "The courts delegate rulemaking authority to agencies",
     "Regulations are proposals that carry no legal effect until Congress approves them"], ans=0,
   why="This restates the statement's two sentences in order: delegation as the source, rulemaking as the mechanism, interpretation and implementation as the purpose."),
]
