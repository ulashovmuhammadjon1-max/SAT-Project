# AP U.S. GOVERNMENT AND POLITICS 1.3 Government Power and Individual Rights -- 30 questions
# CED V.1 (c) 2026, Unit 1 Foundations of American Democracy.
# Learning objective 1.3.A: explain Federalist and Anti-Federalist views on
# central government and democracy.
#
# Essential knowledge relied on, quoted from the CED:
#   EK 1.3.A.1 -- "Federalists supported ratification of the Constitution and a
#     strong central government. Madison's arguments in Federalist No. 10
#     focused on the superiority of a large republic in controlling the
#     'mischiefs of faction,' delegating authority to elected representatives
#     and dispersing power between the states and national government."
#     Note the STRUCTURE of that sentence: three things, not one. A student who
#     knows only "large republic" cannot answer items 4, 9 or 26.
#   EK 1.3.A.2 -- "Anti-Federalists opposed the ratification of the Constitution
#     and wanted more power reserved to state governments rather than a strong
#     central government. Anti-Federalist writings, including Brutus No. 1,
#     adhered to popular democratic theory that emphasized the benefits of a
#     small, decentralized republic while warning of the dangers to personal
#     liberty from a large, centralized government."
#
# The discriminator this topic turns on: BOTH sides claimed to be protecting
# liberty, so "which side protects rights" is not the question. The tell is
# WHERE each side located the danger -- Federalists in an unchecked popular
# majority within a small polity, Anti-Federalists in a distant central
# government too large to be watched. Nearly every scenario item below is built
# so that exactly one of those two locations of danger fits the speaker.
#
# Documents the CED attaches to 1.3.A (p. 26): the Articles of Confederation,
# Brutus No. 1, the Declaration of Independence, Federalist No. 10.
# Required cases the CED attaches to 1.3.A (p. 31-32): McCulloch v. Maryland,
# Tinker v. Des Moines, Wisconsin v. Yoder. The SCOTUS-comparison items use
# only those three and print the non-required case's facts in the stem, which
# is what the CED promises the exam will do (p. 29).
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md. Federalist No. 10, the Declaration of
# Independence and the Articles of Confederation are quoted verbatim. BRUTUS
# NO. 1 IS DESCRIBED, NEVER QUOTED -- the same decision v1_2.py records, for the
# same reason: its wording could not be verified against the CED, which quotes
# only the Federalist side. A described argument attributed correctly is worth
# more than a quotation that might be invented.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md; the CED's own samples carry four, see
# AP_US_GOV_CED.md note 10. Key written first throughout; export_units.py
# redistributes it across A-E.
TOPIC = ("1.3", "Government Power and Individual Rights", 1)

_RATIFY = ("The table reports the recorded vote on ratification of the U.S. Constitution in "
           "five state conventions.")

QUESTIONS = [
 dict(q="According to the CED's account of the ratification debate, which pair of positions correctly matches each side?",
   choices=[
     "Federalists supported ratification and a strong central government; Anti-Federalists opposed ratification and wanted more power reserved to the states",
     "Federalists opposed ratification because the document lacked a bill of rights; Anti-Federalists supported it as a guarantee of order",
     "Both sides supported ratification but disagreed about who should be the first president",
     "Federalists wanted the Articles of Confederation amended; Anti-Federalists wanted them replaced",
     "Federalists favored a small decentralized republic; Anti-Federalists favored an extended one"], ans=0,
   why="EK 1.3.A.1 and EK 1.3.A.2 state the two positions in exactly these terms. The fifth option reverses them: it is the Anti-Federalists who adhered to popular democratic theory emphasizing a small, decentralized republic."),

 dict(q="Anti-Federalist writings such as Brutus No. 1 warned that a large, centralized government posed a danger to",
   choices=[
     "personal liberty, because a government spread over a vast territory would grow too distant from the people to be watched",
     "commercial prosperity, because a single national market would ruin local manufacturers",
     "military readiness, because state militias would be disbanded",
     "religious uniformity, because a national church would be established",
     "the amendment process, because three-fourths of the states would rarely agree"], ans=0,
   why="EK 1.3.A.2 states that Anti-Federalist writings warned of “the dangers to personal liberty from a large, centralized government.” The other options name concerns the CED does not attach to this objective."),

 dict(q="A delegate to a state ratifying convention argues that the proposed Congress will tax, raise armies, and make law directly on individuals across an area too large for any representative body to know, and that liberty will be safer if most authority stays with the states. This delegate is best identified as",
   choices=[
     "an Anti-Federalist, locating the danger to liberty in a distant central government",
     "a Federalist, locating the danger to liberty in unchecked local majorities",
     "an Anti-Federalist, arguing that the states should be abolished in favor of one national republic",
     "a Federalist, arguing that a bill of rights would be unnecessary in a large republic",
     "a delegate committed to neither side, since both accepted direct national taxation"], ans=0,
   why="The two sides are distinguished by where each located the danger, and this speaker locates it in distance and scale, which is EK 1.3.A.2's Anti-Federalist position. The third option contradicts itself, since reserving power to the states is the Anti-Federalist demand."),

 dict(q="EK 1.3.A.1 says Madison's argument in Federalist No. 10 focused on three things. Which of the following is NOT one of them?",
   choices=[
     "Guaranteeing a written list of individual rights against the national government",
     "The superiority of a large republic in controlling the mischiefs of faction",
     "Delegating authority to elected representatives",
     "Dispersing power between the states and the national government",
     "Treating faction as a permanent feature to be managed rather than removed"], ans=0,
   why="EK 1.3.A.1 names the large republic, delegation to elected representatives, and dispersal of power between the levels. A written enumeration of rights was the Anti-Federalist demand that EK 1.5.A.1 records as a ratification compromise, not part of Madison's argument in Federalist No. 10."),

 dict(q="Read the following excerpt.\n\n“The latent causes of faction are thus sown in the nature of man; and we see them everywhere brought into different degrees of activity, according to the different circumstances of civil society.”\n—James Madison, Federalist No. 10, 1787\n\nThe claim in this sentence is most important to Madison's argument because it implies that",
   choices=[
     "faction can never be legislated out of existence, so a constitution must be designed to manage its effects",
     "faction arises only in societies that have already become corrupt",
     "a well-written constitution can produce citizens who share the same interests",
     "the causes of faction are economic rather than rooted in human nature",
     "faction will disappear once property is distributed equally"], ans=0,
   why="If the causes are sown in human nature, then no arrangement of institutions can remove them, which is precisely why Madison turns from removing causes to controlling effects. The fifth option names a remedy Madison treats as both impracticable and unjust."),

 dict(q="Read the following excerpt.\n\n“The two great points of difference between a democracy and a republic are: first, the delegation of the government, in the latter, to a small number of citizens elected by the rest; secondly, the greater number of citizens, and greater sphere of country, over which the latter may be extended.”\n—James Madison, Federalist No. 10, 1787\n\nWhich Anti-Federalist response engages this passage most directly?",
   choices=[
     "That the greater sphere Madison praises is exactly what makes representatives too few and too distant to reflect the people",
     "That elected representatives should be chosen for life rather than for fixed terms",
     "That the national government should have no power to tax under any circumstances",
     "That a republic and a democracy are identical in every respect",
     "That the states should surrender their militias to the national government"], ans=0,
   why="Brutus No. 1 turns Madison's second point against him: the same extent that dilutes faction also stretches representation past the point where it can mirror the people. That is the popular democratic theory of a small, decentralized republic in EK 1.3.A.2."),

 dict(q="Read the following excerpt.\n\n“There are again two methods of removing the causes of faction: the one, by destroying the liberty which is essential to its existence; the other, by giving to every citizen the same opinions, the same passions, and the same interests.”\n—James Madison, Federalist No. 10, 1787\n\nMadison introduces these two methods in order to",
   choices=[
     "reject both of them and shift the argument to controlling the effects of faction instead",
     "recommend the second as the proper task of a national system of education",
     "argue that the first is acceptable during wartime",
     "show that the Articles of Confederation had already accomplished the second",
     "prove that faction is confined to large republics"], ans=0,
   why="Madison presents the pair only to dismiss them, the first as a cure worse than the disease and the second as impracticable, and concludes that relief must be sought in controlling the effects. Reading the sentence as a recommendation inverts the argument."),

 dict(q="Read the following excerpt.\n\n“That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government.”\n—Declaration of Independence, 1776\n\nBoth Federalists and Anti-Federalists could cite this passage in 1787 because it establishes that",
   choices=[
     "government is legitimate only insofar as it protects rights and rests on consent, which is a standard each side claimed its own plan met",
     "a confederation of sovereign states is the only legitimate form of government",
     "the people may not alter a government once it has been established by consent",
     "a written enumeration of rights is required before any government may be instituted",
     "only a large republic can secure the rights the passage names"], ans=0,
   why="The passage states a test of legitimacy rather than a design, so both sides could accept it and disagree about which constitution satisfied it. Neither the confederation form nor the extended republic is named or implied in the sentence."),

 dict(q="Read the following excerpt.\n\n“Each state retains its sovereignty, freedom, and independence, and every power, jurisdiction, and right, which is not by this Confederation expressly delegated to the United States, in Congress assembled.”\n—Articles of Confederation, Article II\n\nAn Anti-Federalist would most likely use this provision to argue that",
   choices=[
     "the proposed Constitution abandons a principle worth keeping, since it does not confine the central government to expressly delegated powers",
     "the Articles gave Congress too much authority over the internal affairs of the states",
     "state sovereignty had already been surrendered before 1787, so the Constitution changed nothing",
     "the Constitution's Necessary and Proper Clause simply restates this provision in different words",
     "the Confederation Congress possessed an executive capable of enforcing its decisions"], ans=0,
   why="Article II confines the union to powers expressly delegated, and the proposed Constitution's Necessary and Proper Clause deliberately does not. That contrast is the Anti-Federalist objection EK 1.3.A.2 describes, and the fourth option denies the very difference the argument depends on."),

 dict(q="Federalists answered the Anti-Federalist charge that the new government would be too powerful in part by pointing to the division of authority between the states and the national government. That answer relies on which claim?",
   choices=[
     "That a government whose powers are split between two levels is harder for any single interest to capture",
     "That the states would retain the power to nullify national laws they judged unconstitutional",
     "That the national government would exercise only powers listed word for word in the text",
     "That the states would be permitted to withdraw from the union at will",
     "That the national government would depend on the states to collect all of its revenue"], ans=0,
   why="EK 1.3.A.1 names dispersing power between the states and the national government as one of Madison's three focuses; the point of the dispersal is that capture of one level does not deliver the whole government. Nullification and secession are not Federalist claims."),

 dict(q="A modern commentator writes: “The Anti-Federalists lost the ratification fight but won a permanent place in American argument.” Which contemporary claim is the most direct descendant of the Anti-Federalist position as the CED describes it?",
   choices=[
     "That decisions should be made at the level of government closest to the people affected by them",
     "That the Supreme Court should have the final word on the meaning of the Constitution",
     "That the president needs broad discretion to act quickly in a crisis",
     "That a national majority should be able to enact its program without obstruction",
     "That interstate commerce requires uniform national regulation"], ans=0,
   why="EK 1.3.A.2 describes the Anti-Federalists as adhering to popular democratic theory that emphasized the benefits of a small, decentralized republic. A preference for the closest competent level of government is that argument in modern form; the other four all favor consolidated national authority."),

 dict(q="In McCulloch v. Maryland (1819), the Supreme Court upheld Congress's power to charter a national bank and held that Maryland could not tax it, establishing the supremacy of the U.S. Constitution and federal laws over state laws. Which side of the ratification debate does the reasoning of that decision most closely follow?",
   choices=[
     "The Federalists, because it reads national power broadly and subordinates conflicting state action",
     "The Anti-Federalists, because it protects a state's authority over institutions operating inside its borders",
     "Neither side, because the case concerned banking rather than constitutional structure",
     "The Anti-Federalists, because it requires that every national power be expressly delegated",
     "The Federalists, because it holds that the states may tax any institution they choose"], ans=0,
   why="The CED states the McCulloch holding as establishing supremacy of the U.S. Constitution and federal laws over state laws, which is the Federalist reading of the union. The fourth option describes the Articles of Confederation's express-delegation rule, which the decision rejects."),

 dict(q="A non-required case: a state enacts a licensing fee that applies only to businesses chartered by the federal government and operating within the state. A federal court strikes the fee down. Which required case supplies the controlling principle, and what is it?",
   choices=[
     "McCulloch v. Maryland (1819), which established the supremacy of the U.S. Constitution and federal laws over state laws",
     "Wisconsin v. Yoder (1972), which held that compelling Amish students to attend school past the eighth grade violates the Free Exercise Clause",
     "Tinker v. Des Moines (1969), which held that a ban on students wearing black armbands violated their freedom of speech",
     "Marbury v. Madison (1803), which established the principle of judicial review",
     "Baker v. Carr (1962), which held that redistricting does not raise political questions"], ans=0,
   why="A state levy aimed at a federally chartered entity is the McCulloch fact pattern, and the CED states that holding as federal supremacy over state law. Judicial review is how a court reaches the question, not the rule that decides it."),

 dict(q="In Wisconsin v. Yoder (1972), the Supreme Court held that compelling Amish students to attend school past the eighth grade violates the Free Exercise Clause of the First Amendment. A student argues that the decision vindicates an Anti-Federalist concern. Which reasoning best supports that argument?",
   choices=[
     "It shows that a government pursuing a general public good can still burden the liberty of a small community, which is the harm the Anti-Federalists feared",
     "It shows that state governments are always more protective of liberty than the national government",
     "It shows that the Constitution's original text contained no protection for religious practice",
     "It shows that compulsory education laws must be enacted by Congress rather than by the states",
     "It shows that the Supreme Court may not review the constitutionality of a state statute"], ans=0,
   why="The Anti-Federalist worry EK 1.3.A.2 records is that a distant majority will not notice the liberty of those unlike itself, and Yoder is exactly that harm. The second option is refuted by the case, in which the burden came from a state law."),

 dict(q="In Tinker v. Des Moines Independent Community School District (1969), the Supreme Court held that a prohibition against public school students wearing black armbands to protest the Vietnam War violated the students' freedom of speech under the First Amendment. Which use of the case in an essay about the ratification debate would be accurate?",
   choices=[
     "As evidence that the Bill of Rights the Anti-Federalists demanded became an enforceable limit on government rather than a statement of aspiration",
     "As evidence that the Federalists were correct that no bill of rights was needed",
     "As evidence that the First Amendment applies only to Congress and not to state institutions",
     "As evidence that students possess no constitutional rights while at school",
     "As evidence that the Supreme Court may not hear cases arising from public schools"], ans=0,
   why="EK 1.5.A.1 records the agreement to add a Bill of Rights as a compromise necessary to secure ratification, and Tinker is a case in which those words defeated a government policy. The third and fourth options contradict the holding."),

 dict(q="Which statement best captures why the absence of a bill of rights in the original Constitution became the central Anti-Federalist objection?",
   choices=[
     "Without an enumeration of protected rights, they argued, a government of broad and elastic powers would define the limits of its own authority",
     "They believed that the original text protected too many individual rights at the expense of order",
     "They objected that the Constitution enumerated rights but failed to create courts to enforce them",
     "They argued that a bill of rights would make ratification by nine states impossible",
     "They wanted the rights of the states enumerated but opposed listing rights of individuals"], ans=0,
   why="The objection follows from the structural argument in EK 1.3.A.2: a large central government with implied powers cannot be trusted to police its own boundary, so the boundary must be written down. A written list was the remedy they sought, not the thing they opposed."),

 dict(q="A Federalist replies to that objection that enumerating rights is dangerous because any right left off the list may be presumed surrendered. Which later provision of the Constitution responds most directly to that Federalist worry?",
   choices=[
     "The Ninth Amendment, which provides that the enumeration of certain rights shall not be construed to deny or disparage others retained by the people",
     "The Tenth Amendment, which reserves to the states the powers not delegated to the national government",
     "The Supremacy Clause, which makes federal law the supreme law of the land",
     "The Necessary and Proper Clause, which lets Congress carry its enumerated powers into execution",
     "Article V, which sets out the process for amending the Constitution"], ans=0,
   why="The Ninth Amendment addresses exactly the inference the Federalist feared, that an unlisted right is a surrendered right. The Tenth answers the parallel worry about powers rather than rights, which is a different objection."),

 dict(q="A newspaper essayist in 1788 writes that the proposed Senate, chosen by state legislatures for six-year terms, will become a permanent aristocracy insulated from the people. This argument belongs to which tradition, and why?",
   choices=[
     "The Anti-Federalist tradition, because it treats distance between the people and their governors as the primary danger",
     "The Federalist tradition, because it treats an unchecked popular majority as the primary danger",
     "The Anti-Federalist tradition, because it demands that senators be given longer terms still",
     "The Federalist tradition, because it favors selection of senators by state legislatures",
     "Neither tradition, because the Senate's design was not debated during ratification"], ans=0,
   why="EK 1.3.A.2's Anti-Federalists adhered to popular democratic theory, so an institution designed to be insulated from popular pressure is precisely their target. The third option contradicts its own premise by asking for more insulation."),

 dict(q="Madison argued that a large republic makes it harder for a majority faction to form. An Anti-Federalist could accept that empirical claim and still reject the conclusion by arguing that",
   choices=[
     "a majority that is hard to assemble is also a public that is hard to represent, so the cure weakens accountability",
     "factions do not in fact exist in societies with a written constitution",
     "the number of factions in a society has no relationship to its geographic extent",
     "an extended republic would make amendment of the constitution impossible",
     "the danger of faction disappears once representatives are elected rather than appointed"], ans=0,
   why="The strongest form of the Anti-Federalist reply concedes Madison's mechanism and attacks its cost: the same diversity that prevents a common motive also prevents a representative from mirroring a district. The other options deny premises rather than dispute the inference."),

 dict(q="A student writes that the Federalists trusted government and the Anti-Federalists distrusted it. What is the most important correction?",
   choices=[
     "Both distrusted concentrated power; they disagreed about whether the greater threat came from a distant central government or from unchecked majorities in the states",
     "Neither side distrusted government, since both supported the Constitution as written",
     "The Federalists distrusted government more, which is why they proposed a bill of rights",
     "The disagreement concerned only who would hold office, not the design of institutions",
     "The Anti-Federalists trusted the national government but distrusted the states"], ans=0,
   why="Federalist No. 10 is an argument about controlling a danger, not a claim that power is safe, so the difference is the location of the threat rather than a difference in trust. The Anti-Federalists, not the Federalists, pressed for a bill of rights."),

 dict(q=_RATIFY + " Which conclusion is best supported by the data?",
   table=dict(headers=["State", "Convention year", "Votes for", "Votes against"],
              rows=[["Delaware", "1787", "30", "0"],
                    ["Massachusetts", "1788", "187", "168"],
                    ["Virginia", "1788", "89", "79"],
                    ["New York", "1788", "30", "27"],
                    ["Rhode Island", "1790", "34", "32"]]),
   choices=[
     "Ratification was unanimous in one state and carried by a margin of fewer than twenty votes in each of the other four",
     "Every state listed ratified by a margin of at least fifty votes",
     "The narrowest recorded margin in the table occurred in Massachusetts",
     "No state in the table recorded any votes against ratification",
     "The total votes cast against ratification exceeded the total votes cast for it"], ans=0,
   why="Delaware records no opposing votes at all, and the four contested margins are 19 in Massachusetts, 10 in Virginia, 3 in New York and 2 in Rhode Island, every one of them under twenty. Massachusetts is the widest of those four, not the narrowest, and the totals for ratification exceed the totals against."),

 dict(q=_RATIFY + " A student argues that the data undercut the claim that the Constitution enjoyed overwhelming popular support at ratification. Which feature of the table most directly supports that argument?",
   table=dict(headers=["State", "Convention year", "Votes for", "Votes against"],
              rows=[["Delaware", "1787", "30", "0"],
                    ["Massachusetts", "1788", "187", "168"],
                    ["Virginia", "1788", "89", "79"],
                    ["New York", "1788", "30", "27"],
                    ["Rhode Island", "1790", "34", "32"]]),
   choices=[
     "In four of the five conventions the losing side drew more than forty percent of the recorded vote",
     "The conventions were held in three different years",
     "Delaware cast the fewest total votes of any state listed",
     "Rhode Island did not hold its convention until 1790",
     "Massachusetts cast more total votes than any other state listed"], ans=0,
   why="The argument is about how divided the delegates were, so the supporting evidence must be the size of the losing side: opposition took 47, 47, 47 and 48 percent in Massachusetts, Virginia, New York and Rhode Island. Timing and turnout figures do not speak to division."),

 dict(q=_RATIFY + " Which limitation of these data would a careful analyst raise first?",
   table=dict(headers=["State", "Convention year", "Votes for", "Votes against"],
              rows=[["Delaware", "1787", "30", "0"],
                    ["Massachusetts", "1788", "187", "168"],
                    ["Virginia", "1788", "89", "79"],
                    ["New York", "1788", "30", "27"],
                    ["Rhode Island", "1790", "34", "32"]]),
   choices=[
     "Convention delegates were themselves selected under restrictive suffrage rules, so their votes are not a direct measure of public opinion",
     "The table reports votes rather than years, so no trend over time can be seen",
     "The table omits the votes of the Confederation Congress, which had the final say on ratification",
     "The number of delegates is identical in every state, which makes comparison meaningless",
     "The table gives no information about which states ratified and which rejected the Constitution"], ans=0,
   why="Every figure here is a delegate vote, and delegates were chosen by an electorate far narrower than the adult population, so the table measures elite opinion at best. The Confederation Congress did not ratify, and the delegate totals plainly differ across rows."),

 dict(q="The table reports responses in a hypothetical survey asking which level of government respondents trust most to protect individual rights. Which conclusion is best supported?",
   table=dict(headers=["Level of government", "All adults (%)", "Urban (%)", "Rural (%)"],
              rows=[["The national government", "38", "46", "27"],
                    ["State government", "34", "29", "41"],
                    ["Local government", "21", "18", "25"],
                    ["No opinion", "7", "7", "7"]]),
   choices=[
     "Rural respondents place the two subnational levels above the national government, while urban respondents do the reverse",
     "A majority of all adults trust the national government most",
     "Urban and rural respondents differ by more than twenty points on every level of government",
     "Local government is the most trusted level among rural respondents",
     "Rural respondents are more likely than urban respondents to have no opinion"], ans=0,
   why="Among rural respondents state and local together take 66 percent against 27 for the national level, while among urban respondents the national level leads at 46. No figure reaches 50, and the no-opinion share is identical in both columns."),

 dict(q="Using the same survey, a student argues that the Anti-Federalist preference for governing close to home survives most strongly outside cities. Which comparison in the data most directly supports the argument?",
   table=dict(headers=["Level of government", "All adults (%)", "Urban (%)", "Rural (%)"],
              rows=[["The national government", "38", "46", "27"],
                    ["State government", "34", "29", "41"],
                    ["Local government", "21", "18", "25"],
                    ["No opinion", "7", "7", "7"]]),
   choices=[
     "State government leads among rural respondents at 41 percent but trails the national government among urban respondents",
     "The no-opinion share is 7 percent in both columns",
     "Local government draws its smallest share from urban respondents",
     "The national government's overall figure of 38 percent is the largest in the first column",
     "Every category's rural figure differs from its urban figure"], ans=0,
   why="The claim is about a preference for the nearer level, so the evidence has to be a level-by-level comparison across the two groups, and the state row supplies it: 41 leads among rural respondents while 29 trails 46 among urban ones. The remaining options are true of the table but say nothing about relative preference."),

 dict(q="Which of the following would a Federalist and an Anti-Federalist have been most likely to AGREE on in 1788?",
   choices=[
     "That government derives its just powers from the consent of the governed",
     "That the national government should have the power to tax individuals directly",
     "That a standing army in peacetime is a necessary institution",
     "That the states should be reduced to administrative districts of the union",
     "That the Necessary and Proper Clause should be read broadly"], ans=0,
   why="Consent of the governed is the Declaration of Independence's premise and was common ground; the dispute was over which constitution honored it. Each of the other four was contested precisely because it involved the scope of central power."),

 dict(q="A student is asked to explain how EK 1.3.A.1's three focuses of Federalist No. 10 fit together. Which explanation is most accurate?",
   choices=[
     "A large republic supplies many competing interests, delegation filters those interests through representatives, and dispersal of power keeps any winning coalition from controlling everything at once",
     "A large republic guarantees unanimity, delegation removes the need for elections, and dispersal of power gives each state a veto over national law",
     "Delegation eliminates faction, the large republic makes representation unnecessary, and dispersal of power abolishes the states",
     "The three focuses are alternatives, and Madison expected only one of them to be adopted",
     "The three focuses describe the Articles of Confederation rather than the proposed Constitution"], ans=0,
   why="EK 1.3.A.1 lists the three as parts of one design, and each does distinct work: scale multiplies interests, representation refines them, and dividing power between levels limits what any coalition can seize. Madison never claims delegation eliminates faction."),

 dict(q="A city council is deciding whether to accept a national grant that carries detailed conditions on how the money may be spent. A council member objects that accepting it would let officials hundreds of miles away set local priorities. That objection is a modern version of which ratification-era argument?",
   choices=[
     "The Anti-Federalist argument that a distant central government cannot know or serve local circumstances",
     "The Federalist argument that a large republic dilutes the power of any single faction",
     "The Federalist argument that dispersing power between levels protects liberty",
     "The Anti-Federalist argument that a bill of rights should enumerate individual protections",
     "The argument from the Declaration of Independence that all men are created equal"], ans=0,
   why="The objection is about distance and local knowledge, which is the Anti-Federalist case for a small, decentralized republic in EK 1.3.A.2. A demand for an enumeration of rights is a different Anti-Federalist argument and is not what the council member raises."),

 dict(q="Which piece of evidence would most WEAKEN the Anti-Federalist prediction that a large republic must end in the loss of personal liberty?",
   choices=[
     "Courts in a large republic have repeatedly enforced written guarantees against the national government itself",
     "The population of the United States has grown steadily since 1790",
     "The national government now spends far more than it did in the eighteenth century",
     "Most Americans express low levels of trust in the national government",
     "Congress has delegated substantial rulemaking authority to executive agencies"], ans=0,
   why="The prediction is that scale makes liberty unenforceable, so the strongest rebuttal is evidence that guarantees are in fact enforced against the largest government. Growth in size, spending and delegation are all consistent with the prediction rather than against it."),

 dict(q="An essay claims that the ratification debate was settled in 1788 and has no bearing on current politics. Which response draws most directly on the CED's account of Unit 1?",
   choices=[
     "The compromises that secured ratification left the balance between national power, state power and individual rights unresolved, and that debate continues today",
     "The debate ended when the Bill of Rights was adopted in 1791, after which no serious disagreement remained",
     "The debate was resolved by the Supreme Court in McCulloch v. Maryland and has not been revisited",
     "The debate concerned only the personalities of the delegates and never involved constitutional principle",
     "The debate has no modern relevance because the Anti-Federalists lost every vote"], ans=0,
   why="EK 1.5.A.3 states that the compromises left matters unresolved that continue to generate debate, and EK 1.5.A.4 places the role of the national government, the powers of the states, and individual rights at the heart of present-day constitutional issues."),
]
