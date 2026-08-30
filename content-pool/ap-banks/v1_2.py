# AP U.S. GOVERNMENT AND POLITICS 1.2 Types of Democracy -- 30 questions
# CED V.1 (c) 2026, Unit 1 Foundations of American Democracy.
# Learning objective 1.2.A: explain how models of representative democracy are
# visible in major institutions, policies, events, or debates in the U.S.
#
# Essential knowledge relied on:
#   EK 1.2.A.1 -- a CLOSED list of three models, each with the framework's own
#     gloss: PARTICIPATORY democracy "emphasizes broad participation in
#     politics and civil society"; PLURALIST democracy "emphasizes group-based
#     activism by nongovernmental interests striving for impact on political
#     decision making"; ELITE democracy "emphasizes limited participation in
#     politics and civil society."
#   EK 1.2.A.2 -- different aspects of the Constitution, and the debate between
#     Federalist No. 10 and Brutus No. 1, reflect the tension between the broad
#     participatory model and the more FILTERED participation of the pluralist
#     and elite models.
#   EK 1.2.A.3 -- the three models continue to be reflected in contemporary
#     institutions and political behavior.
#
# The discriminating fact this topic turns on, and the reason nearly every
# scenario item below is built the same way: participatory and pluralist both
# involve many people, so the tell is WHETHER THE ACTORS ARE ORGANISED GROUPS.
# A town meeting open to every resident is participatory; the same policy
# fought over by three associations is pluralist; a decision taken by a small
# body of officeholders or experts is elite. Items are written so exactly one
# of those three descriptions fits the actors named.
#
# Required cases the CED attaches to 1.2.A (pp. 32-34): Baker v. Carr,
# Tinker v. Des Moines, Shaw v. Reno, Citizens United v. FEC.
#
# Quotations from Federalist No. 10 are verbatim. Brutus No. 1 is DESCRIBED
# rather than quoted wherever its exact wording could not be verified against
# the CED, per SOCIAL_BRIEF.md; the one quoted phrase, "mischiefs of faction,"
# is quoted by the CED itself at EK 1.3.A.1.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md; key written first throughout.
TOPIC = ("1.2", "Types of Democracy", 1)

QUESTIONS = [
 dict(q="Which model of representative democracy emphasizes group-based activism by nongovernmental interests seeking to influence political decision making?",
   choices=[
     "Pluralist democracy",
     "Participatory democracy",
     "Elite democracy",
     "Direct democracy",
     "Republicanism"], ans=0,
   why="EK 1.2.A.1 defines pluralist democracy in exactly those terms. Participatory democracy emphasizes broad individual participation and elite democracy emphasizes limited participation, so neither turns on organized nongovernmental groups."),

 dict(q="A state adopts a ballot-initiative process that lets any citizen who gathers enough signatures put a proposed law directly to the voters. The reform is best described as an expression of",
   choices=[
     "participatory democracy, because it emphasizes broad participation by individual citizens",
     "pluralist democracy, because organized interest groups compete for influence",
     "elite democracy, because participation is limited to those with specialized knowledge",
     "federalism, because a state rather than the national government adopted it",
     "republicanism, because the people act through elected representatives"], ans=0,
   why="EK 1.2.A.1 defines participatory democracy as emphasizing broad participation in politics and civil society. The initiative removes the representative filter entirely and opens the decision to any citizen, which is the participatory move."),

 dict(q="Three trade associations, two labor unions, and an environmental organization each testify at a congressional hearing on a proposed energy bill, and the final text reflects concessions to several of them. This process best illustrates",
   choices=[
     "pluralist democracy, in which organized nongovernmental interests compete for influence over policy",
     "participatory democracy, in which individual citizens deliberate and decide directly",
     "elite democracy, in which a small number of officeholders decide with little outside input",
     "a social contract, in which citizens surrender freedoms in exchange for order",
     "checks and balances, in which one branch restrains another"], ans=0,
   why="The actors are organized nongovernmental groups striving for impact on a decision, which is EK 1.2.A.1's definition of the pluralist model. No individual citizen participates as such, so the participatory description does not fit."),

 dict(q="A commission of eight retired judges and economists, appointed rather than elected, is given authority to set the salaries of federal officials. The arrangement most closely reflects",
   choices=[
     "elite democracy, because it emphasizes limited participation in politics",
     "participatory democracy, because the commissioners deliberate before deciding",
     "pluralist democracy, because the commissioners come from several professions",
     "popular sovereignty, because the officials who appointed the commission were elected",
     "federalism, because the commission's decisions bind more than one level of government"], ans=0,
   why="EK 1.2.A.1 defines elite democracy as emphasizing limited participation in politics and civil society. A small appointed body of experts is limited participation; drawing members from several professions is not group-based activism by nongovernmental interests."),

 dict(q="Read the following excerpt.\n\n“By a faction, I understand a number of citizens, whether amounting to a majority or a minority of the whole, who are united and actuated by some common impulse of passion, or of interest, adverse to the rights of other citizens, or to the permanent and aggregate interests of the community.”\n—James Madison, Federalist No. 10, 1787\n\nWhich statement best describes the argument this definition sets up?",
   choices=[
     "Factions are a permanent feature of free societies, so a government must be designed to control their effects rather than to abolish them",
     "Factions are created by bad laws and will disappear once a government is properly organized",
     "A faction is dangerous only when it is a minority of the population",
     "Factions are groups that always act in the permanent interests of the whole community",
     "A faction is any organization that participates in an election campaign"], ans=0,
   why="Madison's definition covers majorities and minorities alike and rests the danger on interests adverse to others' rights, which is why he turns next to controlling the EFFECTS of faction rather than removing its causes."),

 dict(q="Read the following excerpt.\n\n“Liberty is to faction what air is to fire, an aliment without which it instantly expires. But it could not be less folly to abolish liberty, which is essential to political life, because it nourishes faction, than it would be to wish the annihilation of air, which is essential to animal life, because it imparts to fire its destructive agency.”\n—James Madison, Federalist No. 10, 1787\n\nThe passage is best read as an argument that",
   choices=[
     "the cure of destroying liberty would be worse than the disease of faction",
     "liberty and faction are unrelated, so faction may be removed without cost",
     "government should suppress the organizations that give rise to faction",
     "a free society will eventually produce citizens who share a single interest",
     "faction can be eliminated by giving every citizen the same opinions and interests"], ans=0,
   why="The analogy concedes that liberty feeds faction and then rejects removing liberty as folly, which is the argument that the remedy would cost more than the ill. The fifth option names Madison's other method of removing causes, which he also rejects."),

 dict(q="Read the following excerpt.\n\n“Extend the sphere, and you take in a greater variety of parties and interests; you make it less probable that a majority of the whole will have a common motive to invade the rights of other citizens.”\n—James Madison, Federalist No. 10, 1787\n\nThe reasoning here most directly supports which claim about the size of a republic?",
   choices=[
     "A larger republic is safer for minority rights because a single majority faction is harder to assemble across many interests",
     "A smaller republic is safer because neighbors share the manners and interests needed for agreement",
     "The size of a republic has no bearing on the danger posed by faction",
     "A larger republic is more dangerous because it requires a stronger executive",
     "A republic is safe only when every citizen participates directly in lawmaking"], ans=0,
   why="Madison's mechanism is arithmetic about coalitions: more interests make a common motive across a majority less probable. The second option states the Anti-Federalist position that EK 1.3.A.2 attributes to Brutus No. 1, which is the argument on the other side of this debate."),

 dict(q="Brutus No. 1 argues that a republic covering a very large territory cannot remain free, because representatives will be too distant from and too few for the people they represent, and because the interests of a large and varied country are too dissimilar to be represented by one legislature. This argument favors",
   choices=[
     "a small, decentralized republic in which participation is broad and government is close to the people",
     "an extended republic in which many competing interests check one another",
     "an elite model in which a small number of experienced officials govern",
     "a national government with the exclusive power to regulate commerce",
     "a system in which organized interest groups replace geographic representation"], ans=0,
   why="EK 1.3.A.2 records that Anti-Federalist writings including Brutus No. 1 emphasized the benefits of a small, decentralized republic while warning of the dangers to personal liberty from a large centralized government; the reasoning given in the stem is that argument."),

 dict(q="EK 1.2.A.2 identifies the debate between Federalist No. 10 and Brutus No. 1 as reflecting a tension between which two things?",
   choices=[
     "The broad participatory model and the more filtered participation of the pluralist and elite models",
     "Judicial review and legislative supremacy",
     "The enumerated powers of Congress and the reserved powers of the states",
     "Direct democracy and monarchy",
     "The Establishment Clause and the Free Exercise Clause"], ans=0,
   why="EK 1.2.A.2 states this tension explicitly, and the word that matters is FILTERED: both the pluralist and the elite models route influence through something other than the citizen acting alone."),

 dict(q="Which feature of the original Constitution most clearly reflects a filtered, rather than a broadly participatory, model of representative democracy?",
   choices=[
     "The selection of senators by state legislatures rather than by the voters directly",
     "The requirement that the House of Representatives be apportioned by population",
     "The two-year term of a member of the House of Representatives",
     "The requirement that revenue bills originate in the House",
     "The guarantee of a republican form of government to every state"], ans=0,
   why="Filtering means placing an intermediary between the voters and the officeholder. Legislative selection of senators does exactly that; apportionment by population and short House terms move in the opposite direction, toward direct popular accountability."),

 dict(q="A student argues that the Electoral College reflects a filtered model of representative democracy. Which observation best supports the argument?",
   choices=[
     "Voters choose electors, and the electors rather than the voters formally choose the president",
     "The number of a state's electors equals its total representation in Congress",
     "Most states award all of their electors to the statewide winner",
     "A presidential candidate campaigns in a limited number of competitive states",
     "The Twelfth Amendment provides separate ballots for president and vice president"], ans=0,
   why="The claim is about a filter, so the supporting evidence has to name an intermediary between the voters and the outcome. The interposition of electors is that intermediary; the other options describe how electors are counted, awarded, or courted, which does not bear on whether an intermediary exists."),

 dict(q="A New England town holds an annual meeting at which any resident may speak and vote on the town budget. Which model of democracy does the meeting most closely approximate, and why?",
   choices=[
     "Participatory, because political decisions are made through broad direct involvement of ordinary citizens",
     "Pluralist, because residents belong to many different civic organizations",
     "Elite, because most residents do not in fact attend",
     "Pluralist, because the budget affects competing economic interests in the town",
     "Elite, because the town's selectmen prepare the budget in advance"], ans=0,
   why="EK 1.2.A.1's participatory model emphasizes broad participation in politics and civil society, and an assembly open to every resident is its clearest institutional form. Low attendance is a criticism of how well the institution realizes the model, not a change in which model it embodies."),

 dict(q="Which of the following would a political scientist cite as the best contemporary evidence that the pluralist model still describes national policymaking?",
   choices=[
     "Thousands of registered organizations lobby Congress, and major bills routinely bear the marks of bargaining among them",
     "Turnout in presidential elections is higher than turnout in midterm elections",
     "Supreme Court justices serve during good behavior and are not elected",
     "The president may issue executive orders without congressional approval",
     "Most Americans can name their own member of Congress"], ans=0,
   why="EK 1.2.A.1's pluralist model is about organized nongovernmental interests striving for impact on decisions, so the evidence has to be about organized groups affecting outcomes. Turnout figures speak to participation by individuals, and the other options describe institutional powers rather than group influence."),

 dict(q="A critic of the pluralist model argues that it describes American politics accurately but does not justify it. Which finding would most strengthen that criticism?",
   choices=[
     "Organized groups are drawn disproportionately from wealthier and better-educated segments of the public",
     "The number of organized groups registered to lobby has grown over the past fifty years",
     "Groups on opposite sides of an issue often reach a compromise",
     "Most organized groups are headquartered in the national capital",
     "Members of Congress meet with group representatives more often than with individual constituents"], ans=0,
   why="The criticism concedes that groups matter and attacks the fairness of the result, so it needs evidence that the group system is unrepresentative of the public. Growth in the number of groups and the location of their offices say nothing about whose interests they carry."),

 dict(q="In Citizens United v. Federal Election Commission (2010), the Supreme Court held that political spending by corporations, associations, and labor unions is protected speech under the First Amendment. A political scientist argues that the decision strengthened the pluralist model's description of American politics. Which reasoning best supports that argument?",
   choices=[
     "It expanded the ability of organized nongovernmental interests to spend in order to influence political outcomes",
     "It expanded the number of citizens eligible to vote in federal elections",
     "It required political parties to hold open primary elections",
     "It transferred campaign regulation from Congress to the states",
     "It limited the ability of individuals to contribute directly to candidates"], ans=0,
   why="The pluralist model is defined by the activity of organized nongovernmental interests, and the CED states the holding as protecting political spending by corporations, associations, and unions -- that is, by organizations rather than by individuals."),

 dict(q="A non-required case: a federal court hears a challenge to a state's legislative map, brought by voters who claim their districts contain far more people than others in the same state, and rules that the claim may be decided in court. Which required case established that such a claim is justiciable?",
   choices=[
     "Baker v. Carr (1962), which held that redistricting did not raise political questions and could be reviewed by federal courts",
     "Shaw v. Reno (1993), which held that majority-minority districts may be challenged if race is the only factor used in drawing them",
     "Marbury v. Madison (1803), which established the principle of judicial review",
     "McCulloch v. Maryland (1819), which established the supremacy of federal law over state law",
     "Citizens United v. FEC (2010), which held political spending by organizations to be protected speech"], ans=0,
   why="The CED states the Baker holding as redistricting not raising political questions, which is what allows federal courts to hear equal protection challenges to districting plans; Shaw governs the different question of race-based line-drawing, which the stem does not raise."),

 dict(q="Shaw v. Reno (1993) held that majority-minority districts created under the Voting Rights Act may be constitutionally challenged by voters if race is the only factor used in creating the district. Which statement best connects that holding to the models of representative democracy?",
   choices=[
     "It limits how far group identity may be built into the design of representation itself",
     "It requires that all legislative districts contain exactly equal populations",
     "It bars organized groups from contributing to legislative campaigns",
     "It transfers the drawing of district lines from state legislatures to federal courts",
     "It establishes that participation in redistricting must be open to every voter"], ans=0,
   why="The pluralist model is about groups influencing decisions; Shaw concerns whether a group characteristic may be the sole basis for constructing a district, which is a limit on group identity as a design principle rather than a rule about who may participate or contribute."),

 dict(q="The table reports turnout among registered voters in a hypothetical county across three kinds of election. Which conclusion is best supported by the data?",
   table=dict(headers=["Election type", "2018 turnout (%)", "2020 turnout (%)", "2022 turnout (%)"],
              rows=[["Presidential or midterm general", "51", "68", "49"],
                    ["Statewide primary", "24", "31", "22"],
                    ["Local school board", "12", "15", "11"]]),
   choices=[
     "Turnout is highest in general elections and lowest in school board elections in each of the three years",
     "Turnout rose in every type of election between 2018 and 2022",
     "School board turnout exceeded primary turnout in at least one year",
     "General election turnout was more than five times school board turnout in every year",
     "Primary turnout was closer to general election turnout than to school board turnout in every year"], ans=0,
   why="Reading each column top to bottom, the general-election figure is the largest and the school-board figure the smallest in 2018, 2020 and 2022. Turnout fell rather than rose between 2018 and 2022 in every row, and in 2020 the general figure is 68, which is not more than five times 15."),

 dict(q="Using the same data, a student argues that participatory democracy is least visible at the level of government closest to citizens. Which feature of the data most directly supports the argument?",
   table=dict(headers=["Election type", "2018 turnout (%)", "2020 turnout (%)", "2022 turnout (%)"],
              rows=[["Presidential or midterm general", "51", "68", "49"],
                    ["Statewide primary", "24", "31", "22"],
                    ["Local school board", "12", "15", "11"]]),
   choices=[
     "School board turnout never exceeds 15 percent, the lowest figure in the table in every year",
     "General election turnout varies by 19 percentage points across the three years",
     "Primary turnout is roughly half of general election turnout in each year",
     "All three rows reach their maximum in 2020",
     "The gap between primary and school board turnout is smaller than the gap between general and primary turnout"], ans=0,
   why="The argument is about how little participation the most local contest attracts, so the supporting evidence must be the school-board row's own level. The other options describe variation and gaps that are true of the table but say nothing about local participation being lowest."),

 dict(q="The table reports the share of respondents in a hypothetical survey who say each actor should have the most influence over a major national policy decision. Which conclusion is best supported?",
   table=dict(headers=["Actor", "All respondents (%)", "Under 35 (%)", "35 and older (%)"],
              rows=[["Ordinary citizens voting directly", "34", "43", "30"],
                    ["Organized interest groups and associations", "18", "20", "17"],
                    ["Elected representatives", "31", "24", "34"],
                    ["Nonpartisan experts", "17", "13", "19"]]),
   choices=[
     "Respondents under 35 favor direct citizen decision more than older respondents do, by 13 percentage points",
     "Organized groups are the most preferred actor among respondents under 35",
     "A majority of all respondents favor decision by elected representatives",
     "Older respondents prefer nonpartisan experts to elected representatives",
     "Every actor draws more support from respondents under 35 than from older respondents"], ans=0,
   why="43 minus 30 is 13 percentage points. Direct citizen decision, not organized groups, leads among the under-35 group; 31 percent is not a majority; and older respondents prefer representatives (34) to experts (19)."),

 dict(q="Using the same survey, which statement is the most defensible interpretation of what the data show about the three models of representative democracy?",
   table=dict(headers=["Actor", "All respondents (%)", "Under 35 (%)", "35 and older (%)"],
              rows=[["Ordinary citizens voting directly", "34", "43", "30"],
                    ["Organized interest groups and associations", "18", "20", "17"],
                    ["Elected representatives", "31", "24", "34"],
                    ["Nonpartisan experts", "17", "13", "19"]]),
   choices=[
     "No single model commands majority support, and preferences differ by age",
     "The public has decisively rejected the pluralist model in favor of participatory democracy",
     "Support for elite decision making is negligible in every age group",
     "The survey shows that younger respondents distrust all forms of representation equally",
     "The survey establishes that direct citizen decision produces better policy"], ans=0,
   why="The largest figure in any column is 43, so no model reaches a majority anywhere, and the under-35 and 35-and-older columns differ on all four actors, by as much as 13 points on direct citizen decision. The two filtered-decision categories, elected representatives and nonpartisan experts, together draw 48 percent of all respondents and 37 percent even among those under 35, which is not negligible, and a preference survey cannot establish policy quality."),

 dict(q="A student writes that participatory and pluralist democracy are the same model because both involve large numbers of people. What is the strongest objection?",
   choices=[
     "The two models differ in who acts: individual citizens in the participatory model, organized groups in the pluralist model",
     "The two models differ in scale, since participatory democracy is possible only in small communities",
     "The two models differ because only the pluralist model appears in the Constitution",
     "The two models differ because participatory democracy requires unanimous agreement",
     "The two models differ because pluralist democracy excludes elections"], ans=0,
   why="EK 1.2.A.1 distinguishes them on the identity of the actor -- broad participation by citizens against group-based activism by nongovernmental interests -- not on how many people are ultimately involved, which is why a mass-membership organization is still pluralist."),

 dict(q="A national veterans' organization, a union of federal employees, and a taxpayer advocacy group each publish competing analyses of a proposed change to federal pensions, and members of Congress cite all three during floor debate. This episode is best used as evidence for which claim?",
   choices=[
     "Nongovernmental organizations shape the terms on which elected officials debate policy",
     "Individual citizens deliberate directly on national policy questions",
     "Policy is set by a small group of officials insulated from outside influence",
     "Interest groups have replaced political parties as the organizers of Congress",
     "Congress is required by law to consider testimony from affected organizations"], ans=0,
   why="What the episode shows is organized nongovernmental interests supplying the material of a legislative debate, which is the pluralist model's core claim. It does not show individual citizens deliberating, and nothing in it establishes a legal requirement or displaces parties."),

 dict(q="Which of the following pairs an institution with the model of democracy it most clearly reflects?",
   choices=[
     "The United States Senate as originally designed, with elite democracy",
     "A statewide ballot referendum, with elite democracy",
     "A congressional hearing dominated by trade association testimony, with participatory democracy",
     "A recall election of a sitting governor, with pluralist democracy",
     "A public comment period open to any citizen, with elite democracy"], ans=0,
   why="Senators were originally chosen by state legislatures and served long terms, which is limited participation and the elite model. Each of the other pairings attaches an institution to the wrong model: referendums and recalls and open comment periods are participatory, and association testimony is pluralist."),

 dict(q="A member of Congress votes for a bill because a coalition of hospital associations, insurers, and patient advocacy organizations reached an agreement she considers workable. Her behavior best illustrates",
   choices=[
     "the pluralist model, because the decisive influence came from bargaining among organized interests",
     "the participatory model, because many people are affected by health policy",
     "the elite model, because a member of Congress is an elected official",
     "the participatory model, because patient advocacy groups represent ordinary people",
     "the elite model, because the associations employ professional staff"], ans=0,
   why="The model is identified by what actually moved the decision, and here it was an agreement among organizations. That a group's members are ordinary people does not convert group activity into individual participation, which is the distinction EK 1.2.A.1 draws."),

 dict(q="A commentator argues that the Constitution embodies no single model of democracy. Which pair of constitutional features best supports that argument?",
   choices=[
     "Direct popular election of the House of Representatives, alongside life tenure for federal judges",
     "The requirement that revenue bills originate in the House, alongside the president's veto",
     "The two-thirds Senate vote required to ratify a treaty, alongside the two-year House term",
     "The requirement of a census every ten years, alongside the guarantee of a republican form of government",
     "The president's power to grant pardons, alongside the vice president's role as president of the Senate"], ans=0,
   why="The argument needs one feature pulling toward broad participation and one pulling toward filtered or elite decision making. Popular election of a chamber and unelected judges holding office during good behavior are that pair; the other options pair two features that sit on the same side of the tension or on neither."),

 dict(q="Which question would a political scientist studying the elite model be most likely to ask?",
   choices=[
     "Do a small number of officeholders and advisers make the decisions that matter most, regardless of who wins elections?",
     "How many organized groups testify on a typical bill, and which of them prevail?",
     "What proportion of eligible citizens vote in local elections?",
     "How often do citizens attend public meetings in their own communities?",
     "Do interest groups on opposing sides of an issue reach compromises?"], ans=0,
   why="Each model implies its own research question. The elite model's claim is that effective decision making is confined to a few, so its question is about the size and continuity of the deciding group; the other four questions test the participatory and pluralist models instead."),

 dict(q="A state legislature replaces its closed party caucus for nominating candidates with a primary election open to all registered voters. The change moves the nominating process",
   choices=[
     "toward the participatory model, by transferring the decision from a small body to the electorate",
     "toward the elite model, by adding a formal stage before the general election",
     "toward the pluralist model, by increasing the influence of organized interests",
     "away from representative democracy altogether, since primaries are not mentioned in the Constitution",
     "toward the elite model, because primary turnout is usually low"], ans=0,
   why="The decision moves from a closed caucus of party officials to the whole registered electorate, which is a widening of participation. Low turnout is a fact about how many use the opportunity, not about who holds the decision, and EK 1.2.A.1 defines the models by the latter."),

 dict(q="Madison writes in Federalist No. 10 that a republic differs from a democracy in the delegation of government to a small number of citizens elected by the rest, and in the greater number of citizens and larger territory it can cover. A student cites this passage as evidence that Madison preferred a filtered form of participation. Is the citation apt?",
   choices=[
     "Yes, because delegation to elected representatives is itself a filter between the people and the decision",
     "No, because Madison argues that every citizen should vote on every law",
     "No, because the passage concerns only the geographic size of a republic",
     "Yes, because Madison argues that only property owners should be permitted to vote",
     "No, because the passage describes the Articles of Confederation rather than the proposed Constitution"], ans=0,
   why="The first of the two differences Madison names is delegation to a small number of elected citizens, which is precisely an intermediary between the people and the law -- the filtered participation EK 1.2.A.2 describes. The passage names size as the second difference, not the only one."),

 dict(q="A civic organization proposes replacing a city's elected council with a randomly selected assembly of residents who would serve one-year terms. A critic responds that the plan would maximize one democratic value at the cost of another. Which pair of values is the critic most likely describing?",
   choices=[
     "Broad participation, gained at the cost of accountability through elections",
     "Federalism, gained at the cost of separation of powers",
     "Judicial independence, gained at the cost of popular sovereignty",
     "Limited government, gained at the cost of natural rights",
     "Group representation, gained at the cost of individual rights"], ans=0,
   why="A randomly selected assembly maximizes the participatory model's value by making any resident eligible to decide, but no one selected by lot can be voted out, so the electoral accountability that republicanism supplies is what the plan gives up."),
]
