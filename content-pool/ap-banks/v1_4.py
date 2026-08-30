# AP U.S. GOVERNMENT AND POLITICS 1.4 Challenges of the Articles of Confederation -- 30 questions
# CED V.1 (c) 2026, Unit 1 Foundations of American Democracy.
# Learning objective 1.4.A: explain the relationship between key provisions of
# the Articles of Confederation, and the debate over granting the federal
# government greater power formerly reserved to the states.
#
# Essential knowledge relied on. There is exactly ONE statement for this topic,
# and it is a CLOSED list of five items, quoted here from the CED because the
# whole module is built on it:
#
#   EK 1.4.A.1 -- "Specific incidents and legal challenges that highlighted key
#     weaknesses of the Articles of Confederation are represented by the:
#       i.   Lack of centralized military power to address Shays' Rebellion
#       ii.  Lack of an executive branch to enforce laws, including taxation
#       iii. Lack of a national court system
#       iv.  Lack of power to regulate interstate commerce
#       v.   Lack of the exclusive power to coin money"
#
# Because the list is closed and short, a bank on this topic fails in a
# predictable way: it becomes five recall questions repeated six times. The
# design here avoids that by asking, in most items, WHICH of the five a given
# incident illustrates -- the incidents differ, the discrimination is real, and
# a student who has memorised the list still has to reason. Items are written so
# that exactly one of the five fits; where two plausibly fit, the stem names the
# feature that decides between them.
#
# One point of care, and it is the reason item 5 is worded as it is: the
# Articles did not deny Congress a coinage power outright. Congress could coin
# money; so could the states. The CED's phrasing is the "lack of the EXCLUSIVE
# power to coin money," and every item in this module that touches currency uses
# that word, because "the Articles gave Congress no power to coin money" is
# false and would teach a student an error.
#
# Documents the CED attaches to 1.4.A (p. 26): the Articles of Confederation,
# Federalist No. 10, Federalist No. 51.
# Required cases the CED attaches to 1.4.A (p. 31-32): McCulloch v. Maryland,
# McDonald v. Chicago.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md. The Articles of Confederation are
# quoted verbatim from Article II and Article XIII only; Articles VIII and IX
# are DESCRIBED, because their wording could not be verified. Federalist No. 10
# and No. 51 are quoted verbatim.
#
# The two data items' tables are of two different kinds and are both honest
# about it: the powers comparison in items 21 to 23 is a categorical summary of
# the two documents' text, and the requisition table in items 24 and 26 is
# explicitly a HYPOTHETICAL confederation, because per-state Confederation
# revenue figures could not be verified and an invented number presented as
# history is exactly what SOCIAL_BRIEF.md forbids.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("1.4", "Challenges of the Articles of Confederation", 1)

_POWERS = ("The table summarizes whether the national legislature held each power under the "
           "Articles of Confederation and under the U.S. Constitution as ratified.")
_POWERS_TABLE = dict(
    headers=["Power of the national legislature", "Articles of Confederation", "U.S. Constitution"],
    rows=[["Levy taxes directly on individuals", "No", "Yes"],
          ["Raise and maintain an army of its own", "No", "Yes"],
          ["Regulate commerce among the states", "No", "Yes"],
          ["Establish a national court system", "No", "Yes"],
          ["Coin money to the exclusion of the states", "No", "Yes"],
          ["Amend the founding document without unanimous state consent", "No", "Yes"]])

_REQ = ("In a hypothetical confederation whose central congress may request but not compel "
        "revenue, the table reports the percentage of each member state's assigned share "
        "that the state actually paid in three consecutive years.")
_REQ_TABLE = dict(
    headers=["State", "Year 1 paid (%)", "Year 2 paid (%)", "Year 3 paid (%)"],
    rows=[["Alden", "62", "48", "35"],
          ["Brixton", "40", "33", "20"],
          ["Corwin", "78", "70", "66"],
          ["Dellwood", "25", "18", "10"],
          ["Eastmark", "55", "44", "39"]])

QUESTIONS = [
 dict(q="In 1786 and 1787, indebted farmers in western Massachusetts closed courts by force, and the Confederation Congress was unable to field troops to restore order. Which weakness of the Articles of Confederation does the episode most directly illustrate?",
   choices=[
     "The lack of centralized military power",
     "The lack of the exclusive power to coin money",
     "The lack of power to regulate commerce among the states",
     "The lack of a written guarantee of individual rights",
     "The lack of a formal amendment process of any kind"], ans=0,
   why="EK 1.4.A.1.i names the lack of centralized military power to address Shays' Rebellion as the first of the five weaknesses. The Articles did contain an amendment process in Article XIII; the defect was that it required unanimity, not that it was absent."),

 dict(q="Under the Articles of Confederation, Congress could set the sums each state owed to the common treasury but had to rely on the state legislatures to collect and forward them. Which listed weakness does that arrangement represent?",
   choices=[
     "The lack of an executive branch to enforce laws, including taxation",
     "The lack of a national court system",
     "The lack of centralized military power",
     "The lack of power to regulate commerce among the states",
     "The lack of any body authorized to assess what each state owed"], ans=0,
   why="EK 1.4.A.1.ii names the lack of an executive branch to enforce laws, including taxation. The fifth option misstates the facts: Congress could set the assessments, and the failure was that nothing existed to enforce them."),

 dict(q="Two states dispute the boundary of a river that divides them, and each state's own courts rule for its own side. Under the Articles of Confederation, which weakness made this dispute especially difficult to settle?",
   choices=[
     "The lack of a national court system able to give a binding judgment",
     "The lack of centralized military power to occupy the disputed territory",
     "The lack of an executive branch to negotiate a treaty between the states",
     "The lack of the exclusive power to coin money",
     "The lack of a national legislature of any kind"], ans=0,
   why="EK 1.4.A.1.iii names the lack of a national court system. With no forum standing above both states, each side's judgment binds only within its own borders, which is why the Constitution extends the judicial power to controversies between two or more states."),

 dict(q="A state places a tariff on goods brought in from a neighboring state, which then retaliates with a tariff of its own. Under the Articles of Confederation, which weakness allowed this to continue?",
   choices=[
     "The lack of power to regulate commerce among the states",
     "The lack of a national court system",
     "The lack of centralized military power",
     "The lack of the exclusive power to coin money",
     "The lack of an amendment process"], ans=0,
   why="EK 1.4.A.1.iv names the lack of power to regulate interstate commerce. Retaliatory state tariffs are the paradigm case, and the Constitution answers it with the Commerce Clause, which gives Congress the power to regulate commerce among the several states."),

 dict(q="Which statement about currency under the Articles of Confederation is accurate?",
   choices=[
     "Congress could coin money, but so could the states, so Congress lacked the exclusive power",
     "Congress was forbidden to coin money, and only the states could do so",
     "Congress held the exclusive power to coin money but chose not to exercise it",
     "Neither Congress nor the states could issue currency of any kind",
     "The Articles required all debts to be paid in a single national currency"], ans=0,
   why="EK 1.4.A.1.v names the lack of the EXCLUSIVE power to coin money, which is a statement about exclusivity rather than about the power itself. Saying Congress had no coinage power at all misdescribes the document."),

 dict(q="Read the following excerpt.\n\n“Each state retains its sovereignty, freedom, and independence, and every power, jurisdiction, and right, which is not by this Confederation expressly delegated to the United States, in Congress assembled.”\n—Articles of Confederation, Article II\n\nThe practical effect of the word “expressly” in this provision was to",
   choices=[
     "bar Congress from claiming any power that could not be pointed to in the text itself",
     "give Congress authority over every subject the states had not already legislated on",
     "make the states subordinate to Congress in all matters of national concern",
     "require the states to obtain congressional approval before amending their own constitutions",
     "establish a national judiciary to police the boundary between the two levels"], ans=0,
   why="An express-delegation rule leaves no room for implied powers, so a power not written down does not exist. That is the contrast the Constitution draws by omitting the word and adding the Necessary and Proper Clause."),

 dict(q="Read the following excerpt.\n\n“Nor shall any alteration at any time hereafter be made in any of them; unless such alteration be agreed to in a congress of the united states, and be afterwards confirmed by the legislatures of every state.”\n—Articles of Confederation, Article XIII\n\nWhich conclusion about the Articles follows most directly from this provision?",
   choices=[
     "A single state could block any change, so the document was nearly impossible to reform from within",
     "Amendments could be adopted by a simple majority of the states",
     "The Articles contained no procedure for amendment at all",
     "Congress could amend the Articles without consulting the states",
     "Amendment required the approval of three-fourths of the state legislatures"], ans=0,
   why="Confirmation by the legislatures of EVERY state is a unanimity rule, and unanimity means one holdout is a veto. The fifth option states the U.S. Constitution's Article V threshold, which is precisely the change the framers made."),

 dict(q="The delegates who met at Philadelphia in 1787 had been authorized to propose revisions to the Articles of Confederation and instead proposed an entirely new frame of government, to take effect on ratification by nine states. Which feature of the Articles best explains why they did not simply propose amendments?",
   choices=[
     "Amendment required the unanimous consent of the state legislatures, which no proposal of that magnitude was likely to obtain",
     "The Articles forbade any gathering of delegates from more than three states",
     "The Confederation Congress had already dissolved itself before the convention met",
     "The Articles required that all amendments originate with the Supreme Court",
     "The Articles set a fixed expiration date after which they ceased to have effect"], ans=0,
   why="Article XIII's unanimity requirement made piecemeal reform hopeless, which is why the convention set a ratification threshold of nine states in the new document instead. The other four options describe provisions the Articles do not contain."),

 dict(q="Read the following excerpt.\n\n“Complaints are everywhere heard from our most considerate and virtuous citizens, equally the friends of public and private faith, and of public and personal liberty, that our governments are too unstable, that the public good is disregarded in the conflicts of rival parties, and that measures are too often decided, not according to the rules of justice and the rights of the minor party, but by the superior force of an interested and overbearing majority.”\n—James Madison, Federalist No. 10, 1787\n\nMadison opens with this catalogue of complaints in order to",
   choices=[
     "establish that the existing arrangements had already failed, which is what makes a new constitution necessary rather than merely desirable",
     "argue that the state governments had performed well and needed no reform",
     "propose that the national government be given the power to appoint state legislators",
     "show that faction had been eliminated in the years since independence",
     "praise the stability of government under the Articles of Confederation"], ans=0,
   why="The passage is a diagnosis offered as a premise: the governments in existence are unstable and unjust, therefore something must change. Reading it as praise inverts the argument, and Madison never proposes national appointment of state officials."),

 dict(q="Read the following excerpt.\n\n“In framing a government which is to be administered by men over men, the great difficulty lies in this: you must first enable the government to control the governed; and in the next place oblige it to control itself.”\n—James Madison, Federalist No. 51, 1788\n\nA student uses this passage to explain the failure of the Articles of Confederation. Which explanation is most accurate?",
   choices=[
     "The Articles attended to the second requirement and neglected the first, leaving a government that could not act on the governed at all",
     "The Articles attended to the first requirement and neglected the second, leaving a government that could not be checked",
     "The Articles satisfied both requirements, which is why the Constitution changed so little",
     "The passage concerns the separation of powers within a state government and has no bearing on the Articles",
     "The Articles failed because they enabled the government to control the governed too effectively"], ans=0,
   why="Under the Articles the national government reached the states rather than individuals and could not enforce its own measures, so it failed the first requirement. Its weakness was the reason it needed no elaborate internal checks, which is the second requirement Madison names."),

 dict(q="Read the following excerpt.\n\n“If men were angels, no government would be necessary. If angels were to govern men, neither external nor internal controls on government would be necessary.”\n—James Madison, Federalist No. 51, 1788\n\nWhich claim does this passage most directly support in the debate over replacing the Articles?",
   choices=[
     "That a government must be given real power because people cannot be relied on to govern themselves without one",
     "That government should be abolished in favor of voluntary cooperation among the states",
     "That officeholders selected for their virtue require no institutional checks",
     "That the national government should be given unlimited authority",
     "That the states, being closer to the people, are naturally free of the problems Madison describes"], ans=0,
   why="The sentence is a two-sided argument for both the necessity of government and the necessity of controls on it, and the first half is the answer to those who thought the Confederation's weakness a virtue. It draws no distinction between state and national officeholders."),

 dict(q="In McCulloch v. Maryland (1819), the Supreme Court upheld Congress's authority to charter a national bank even though no such power appears in the constitutional text, and held that state law could not obstruct it. Which contrast with the Articles of Confederation does the decision most directly illustrate?",
   choices=[
     "The Constitution permits powers implied from those enumerated, whereas the Articles confined Congress to powers expressly delegated",
     "The Constitution restricts Congress to powers expressly delegated, whereas the Articles allowed implied powers",
     "Both documents allowed implied powers, and the decision turned on banking rather than on structure",
     "The Constitution left commercial regulation entirely to the states, as the Articles had done",
     "Both documents made state law supreme over national law in cases of conflict"], ans=0,
   why="The CED states the McCulloch holding as establishing supremacy of the U.S. Constitution and federal laws over state laws, and the reasoning rests on the Necessary and Proper Clause. Article II of the Articles contains the opposite rule, confining Congress to powers expressly delegated."),

 dict(q="In McDonald v. Chicago (2010), the Supreme Court held that the Second Amendment right to keep and bear arms for self-defense is applicable to the states. A student cites the case as evidence of how far the constitutional order has moved from the Articles of Confederation. Which reasoning best supports that use?",
   choices=[
     "The national government now enforces individual rights against state governments, an authority the Confederation possessed in no form",
     "The national government now regulates the sale of firearms in every state, which the Confederation Congress also did",
     "The case shows that the states retain every power not expressly delegated, exactly as Article II provided",
     "The case shows that the Second Amendment restrains only Congress and not the states",
     "The case shows that state courts are the final interpreters of the national constitution"], ans=0,
   why="Under the Articles the national government acted on states as members of a league and had no authority over what a state did to its own residents. A holding that a national guarantee binds a city is the clearest possible measure of that change, and the fourth option contradicts the holding."),

 dict(q="Which of the following best explains why the Confederation Congress could not respond effectively when several states issued their own paper currency and creditors refused to accept it across state lines?",
   choices=[
     "Congress lacked both the exclusive power over coinage and any means of enforcing a uniform standard",
     "Congress had the exclusive power over coinage but had delegated it to the states",
     "Congress was prohibited by the Articles from discussing economic matters",
     "Congress lacked a legislature capable of passing any measure at all",
     "Congress had already been replaced by a national executive with sole authority over currency"], ans=0,
   why="Two of the five listed weaknesses combine here: EK 1.4.A.1.v's lack of the exclusive coinage power and EK 1.4.A.1.ii's lack of an executive to enforce anything Congress did decide. The remaining options describe provisions the Articles do not contain."),

 dict(q="A delegate in 1787 argues that the Confederation's central defect is that it operates on states rather than on individuals. Which of the five weaknesses identified in the course framework is the most direct consequence of that defect?",
   choices=[
     "The lack of an executive branch to enforce laws, including taxation, since compliance depended on each state's own choice",
     "The lack of a written bill of rights, since individuals had no claim against the union",
     "The lack of a system for admitting new states to the union",
     "The lack of a rule requiring states to give faith and credit to one another's judgments",
     "The lack of any provision for making treaties with foreign powers"], ans=0,
   why="A government that reaches only states must ask rather than command, and the missing enforcement machinery is what EK 1.4.A.1.ii names. The Articles did provide for admitting new states and for treaty-making, so those options are false of the document."),

 dict(q="Which piece of evidence would most strongly support the claim that the weaknesses of the Articles were a matter of design rather than of accident?",
   choices=[
     "The Articles were drafted during a war against a distant central authority, and their provisions systematically deny the union the powers that authority had exercised",
     "The Articles were ratified later than their authors expected",
     "The Confederation Congress met in several different cities during its existence",
     "The Articles were written in a single session lasting only a few days",
     "The states adopted their own constitutions after the Articles were drafted"], ans=0,
   why="A design claim needs evidence that the omissions form a pattern serving a purpose, and a consistent refusal of exactly the powers the imperial government had wielded is that pattern. The other options concern timing and logistics, which bear on neither design nor accident."),

 dict(q="A modern county government can request but not compel neighboring counties to contribute to a shared emergency fund, and contributions fall each year as each county waits to see what the others will do. This dynamic most closely parallels which feature of the Articles of Confederation?",
   choices=[
     "The requisition system, under which Congress assessed the states but could not collect from them",
     "The unanimity requirement for amending the Articles",
     "The absence of a national court system",
     "The lack of the exclusive power to coin money",
     "The one-vote-per-state rule in the Confederation Congress"], ans=0,
   why="The parallel is the structure of the incentive: a body that may assess but not enforce invites each member to hold back and let others pay, which is exactly the requisition problem behind EK 1.4.A.1.ii. Unanimity and coinage are different defects."),

 dict(q="Which change made by the U.S. Constitution most directly addressed the weakness illustrated by Shays' Rebellion?",
   choices=[
     "Congress was given the power to raise and support armies and to call forth the militia to suppress insurrections",
     "Congress was given the power to establish uniform rules of naturalization",
     "The Constitution guaranteed each state a republican form of government",
     "The Constitution provided for a census every ten years",
     "The Constitution required that all revenue bills originate in the House"], ans=0,
   why="EK 1.4.A.1.i names the lack of centralized military power, and Article I Section 8 answers it directly with the powers to raise armies and to call forth the militia to suppress insurrections. A guarantee of republican government is a promise to the states, not a source of force."),

 dict(q="Which pairing of a weakness of the Articles with the constitutional provision that answered it is correct?",
   choices=[
     "No power over interstate commerce, answered by the Commerce Clause of Article I Section 8",
     "No national court system, answered by the Necessary and Proper Clause",
     "No executive to enforce the laws, answered by the Tenth Amendment",
     "No exclusive power over coinage, answered by the Full Faith and Credit Clause",
     "Unanimity required for amendment, answered by the Supremacy Clause"], ans=0,
   why="Only the first pairing matches a defect to the clause that cures it. Article III creates the courts, Article II the executive, Article I Section 10 bars the states from coining money, and Article V replaces unanimity with the two-thirds and three-fourths thresholds."),

 dict(q="A historian argues that the Confederation period was not a simple failure because the Confederation Congress did accomplish significant things. Which accomplishment would best support that argument?",
   choices=[
     "It organized the western territories and set the terms on which new states would enter the union",
     "It established a permanent national bank",
     "It created a federal judiciary with appellate authority over the states",
     "It levied and collected a national tax on individual incomes",
     "It negotiated an end to all interstate tariff disputes"], ans=0,
   why="Territorial organization is the accomplishment historians usually cite, and it is consistent with the five weaknesses because it required no coercion of the states. The other four name powers the Articles denied Congress, so it could not have exercised them."),

 dict(q=_POWERS + " Which conclusion is best supported by the table?",
   table=_POWERS_TABLE,
   choices=[
     "Every power listed was denied to the national legislature under the Articles and granted to it under the Constitution",
     "The two documents differ on some of the listed powers and agree on others",
     "The Articles granted a majority of the listed powers to the national legislature",
     "The Constitution withheld at least one of the listed powers from the national legislature",
     "The table shows that both documents treated commerce among the states identically"], ans=0,
   why="Reading down the two columns, every entry in the Articles column is a denial and every entry in the Constitution column is a grant, so the two documents differ on all six rows without exception."),

 dict(q=_POWERS + " A student writes that the table shows the Constitution simply reversed the Articles on every point of national power. What is the most important limitation of that inference?",
   table=_POWERS_TABLE,
   choices=[
     "The table lists only powers the Constitution added and omits any power the Articles granted or the Constitution withheld, so it cannot show whether the reversal was complete",
     "The table gives no information about which of the two documents came first",
     "The table reports opinions rather than the text of the two documents",
     "The table contains numerical data that cannot be compared across columns",
     "The table covers only one of the two documents"], ans=0,
   why="A list selected for the powers that changed will always show change; that is a property of the selection, not a finding about the documents. Recognizing that a table's rows were chosen is the data-limitation skill the CED describes at 3.E."),

 dict(q=_POWERS + " Which of the five weaknesses named in the course framework has NO row of its own in this table?",
   table=_POWERS_TABLE,
   choices=[
     "The lack of an executive branch to enforce laws, since the table lists legislative powers only",
     "The lack of centralized military power, which the row on raising an army leaves out",
     "The lack of a national court system, which no row mentions",
     "The lack of power to regulate interstate commerce, which no row mentions",
     "The lack of the exclusive power to coin money, which no row mentions"], ans=0,
   why="Four of the five weaknesses each have a row: raising an army, regulating commerce among the states, establishing courts, and coining money to the exclusion of the states. Nothing in a table of legislative powers can represent the absence of a whole branch, which is EK 1.4.A.1.ii."),

 dict(q=_REQ + " Which conclusion is best supported by the data?",
   table=_REQ_TABLE,
   choices=[
     "Every state paid a smaller share of its assigned amount in each successive year",
     "At least one state increased its payment share over the three years",
     "Every state paid more than half of its assigned share in every year",
     "The state paying the largest share in Year 1 paid the smallest share in Year 3",
     "The gap between the highest and lowest paying states narrowed over the three years"], ans=0,
   why="Reading each row left to right, all five decline every year without exception. Corwin leads in Year 1 and still leads in Year 3, and Dellwood never reaches half of its assigned share in any year."),

 dict(q=_REQ + " A delegate argues that the pattern in the data will worsen without a change to the confederation's structure. Which reasoning best supports the argument?",
   table=_REQ_TABLE,
   choices=[
     "Each state's willingness to pay depends on what it expects the others to pay, so declining compliance is self-reinforcing",
     "The states with the largest populations are contributing the least",
     "The central congress has set the assigned shares too high for any state to meet",
     "The states have agreed among themselves to stop paying entirely",
     "Payment shares fluctuate randomly from year to year with no discernible trend"], ans=0,
   why="A voluntary system rewards holding back, and each state's shortfall raises the cost to whoever still pays, which is the mechanism behind the uniform decline. The table gives no population figures, no state has stopped entirely, and the trend is monotonic rather than random."),

 dict(q=_REQ + " Which structural change would most directly address the problem the data reveal?",
   table=_REQ_TABLE,
   choices=[
     "Give the central congress the power to tax individuals directly and an executive able to collect",
     "Require unanimous agreement among the states before any assessment takes effect",
     "Reduce each state's assigned share in proportion to what it paid the previous year",
     "Transfer responsibility for assessments from the central congress to the state with the highest payment share",
     "Publish each state's payment share annually without any other change"], ans=0,
   why="The defect is that compliance is voluntary, so only a power that reaches individuals without a state's cooperation cures it, which is EK 1.4.A.1.ii's missing enforcement. Unanimity and proportional reduction both increase each state's incentive to withhold."),

 dict(q="Under the Articles of Confederation, each state cast one vote in Congress regardless of population, and the most important measures required the agreement of nine of the thirteen states. A critic in 1787 would most likely argue that this arrangement",
   choices=[
     "gave a minority of the population the power to block measures the great majority supported",
     "allowed the largest states to impose their preferences on the smallest",
     "made it impossible for Congress to consider more than one measure at a time",
     "gave the executive branch a veto over congressional action",
     "guaranteed that measures would pass whenever a simple majority of states agreed"], ans=0,
   why="Equal state votes plus a supermajority threshold means the least populous states could combine to defeat a measure supported by most Americans, which is the reverse of the fourth option's claim about large states. There was no executive branch to hold a veto."),

 dict(q="A student claims that the Articles of Confederation failed because the men who wrote them did not understand government. Which correction is best supported by the course framework?",
   choices=[
     "The Articles' weaknesses followed from a deliberate choice to keep sovereignty in the states, which the framework treats as the source of the specific defects it lists",
     "The Articles had no significant weaknesses, and the Constitution was adopted for unrelated reasons",
     "The Articles failed because they gave the national government too much power over the states",
     "The Articles failed because they created an executive too strong to be checked",
     "The Articles were never actually ratified by the states and so were never in force"], ans=0,
   why="EK 1.4.A.1 presents the five weaknesses as consequences of specific provisions rather than as blunders, and Article II states the sovereignty choice from which they follow. The third and fourth options describe the opposite of the document's design."),

 dict(q="Which question would best guide an evaluation of whether the Articles of Confederation should be judged a failure?",
   choices=[
     "Did the Articles supply the powers needed for the tasks the union was actually asked to perform?",
     "Were the Articles written in clearer language than the U.S. Constitution?",
     "Did more delegates sign the Articles than signed the Constitution?",
     "Were the Articles longer or shorter than the constitutions of the individual states?",
     "Did the Articles use the word federal more often than the Constitution does?"], ans=0,
   why="A frame of government is judged against what it must do, which is why the framework lists the weaknesses as incidents and legal challenges that the union could not meet. Length, clarity and word counts are not measures of institutional capacity."),

 dict(q="An essay argues that the debate over the Articles of Confederation is the same debate that continues today over the balance between national and state power. Which claim from the course framework most directly supports that argument?",
   choices=[
     "The debate over the role of the national government, the powers of state governments, and the rights of individuals remains at the heart of present-day constitutional issues",
     "The Articles of Confederation remain in force alongside the U.S. Constitution",
     "The Supreme Court has never revisited the allocation of power between the two levels",
     "The Constitution settled every question about national power at the moment of ratification",
     "The states have surrendered all reserved powers since the eighteenth century"], ans=0,
   why="EK 1.5.A.4 states in those terms that the national/state/individual balance remains at the heart of present-day constitutional issues, and EK 1.5.A.3 adds that the ratification compromises left matters unresolved."),
]
