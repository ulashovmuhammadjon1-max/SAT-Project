# AP COMPARATIVE GOVERNMENT AND POLITICS 1.4 Democratization
# CED effective Fall 2026, Unit 1 Political Systems, Regimes, and Governments.
# Enduring understanding PAU-1; learning objective PAU-1.C (explain the process
# and goals of democratization). Suggested skill 1.D, Concept Application.
#
# Essential knowledge relied on:
#   PAU-1.C.1  democratization is a TRANSITION FROM AN AUTHORITARIAN REGIME TO A
#              DEMOCRATIC REGIME; the process can start or temporarily change
#              direction, and aims to result over time in
#     .a more competition, fairness, and transparency in elections
#     .b increased citizen participation in policy-making processes
#     .c universal suffrage for adult citizens
#     .d greater governmental transparency
#     .e protected civil rights and liberties
#     .f equal treatment of citizens
#     .g establishment of the rule of law
#   PAU-1.C.2  democratic electoral systems can accommodate ethnic diversity and
#              increase multiparty competition with rule adjustments including
#              gender or cultural quotas, proportional representation, and changes
#              in vote thresholds and district boundaries
#   PAU-1.C.3  political corruption inhibits democratization; independent
#              judiciaries can reduce such corruption while protecting individual
#              liberties and civil rights
#   PAU-1.C.4  democratization can STALL OR BE REVERSED; policy changes regarding
#              election rules and civil liberties can SUPPORT OR IMPEDE it
#   PAU-1.C.5  democratic consolidation is the process by which a democratic
#              regime matures in terms of election rules, separation of powers,
#              and protection of civil liberties, making it unlikely to revert to
#              authoritarianism WITHOUT AN EXTERNAL SHOCK
#   PAU-1.C.6  consensus among competing cultural and political groups about
#              governmental policies associated with democratization and economic
#              development can advance the process and make it sustainable
#
# Country statements used, each cited in the verifier's claim:
#   PAU-1.D.1c Nigeria and Mexico transitioned to multiparty republics following
#              MILITARY RULE and SINGLE-PARTY DOMINANCE respectively
#   PAU-4.A.4  rules facilitating Mexico's transition away from one-party
#              dominance: eliminating el dedazo, privatizing state-owned
#              corporations to decrease patronage, decentralizing and reducing
#              one-party power at the subnational level, and establishing and
#              strengthening the National Electoral Institute (IFE)
#   PAU-4.A.3  rules ensuring one-party dominance in Russia, including increasing
#              party registration requirements and increasing threshold rules to
#              limit party access to the ballot
#   DEM-2.A.1c gender quotas in Mexico's party list system have helped increase
#              female representation in the legislature
#   DEM-2.B.1  proportional representation can increase the number of parties and
#              the election of minority and women candidates
#   DEM-2.B.4b Mexico and Nigeria created independent election commissions as part
#              of their democratic transitions
#
# Nothing here turns on how far along any real country currently is: that would
# be a current-events fact the framework does not supply and that would date.
# The country items ask only what the framework itself asserts about a transition
# that has already happened, and the trend items use HYPOTHETICAL data, labelled.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("1.4", "Democratization", 1)

_T_TREND = dict(
    headers=["Country (hypothetical)", "Share of adult citizens eligible to vote, 2000",
             "Share of adult citizens eligible to vote, 2020",
             "Elections judged competitive by observers, 2000-2020 (out of 5 held)"],
    rows=[["Country A", "62 percent", "98 percent", "4"],
          ["Country B", "95 percent", "96 percent", "5"],
          ["Country C", "71 percent", "55 percent", "1"]])

_T_QUOTA = dict(
    headers=["Legislature (hypothetical)", "Electoral rule",
             "Gender quota applied to party lists", "Women as a share of members"],
    rows=[["Legislature 1", "proportional representation with party lists", "yes", "46 percent"],
          ["Legislature 2", "proportional representation with party lists", "no", "28 percent"],
          ["Legislature 3", "single-member district plurality", "no", "19 percent"]])

QUESTIONS = [
 dict(q="The framework defines democratization as",
   choices=[
     "a transition from an authoritarian regime to a democratic regime",
     "a transition from a unitary state to a federal state",
     "the replacement of one governing party by another after an election",
     "the maturing of an already democratic regime until reversal becomes unlikely",
     "the adoption of a written constitution by a state that lacked one"], ans=0,
   why="EK PAU-1.C.1 gives this definition. The maturing of a regime that is already democratic is democratic consolidation, defined separately at EK PAU-1.C.5, and a change of governing party is a change of government under EK PAU-1.A.2."),
 dict(q="Which statement best captures what the framework says about the shape democratization takes over time?",
   choices=[
     "It can start or temporarily change direction, so progress toward its goals is not guaranteed to be continuous",
     "Once begun it proceeds at a steady rate until every one of its goals is reached",
     "It occurs only through a single sudden event such as a revolution",
     "It is completed as soon as a country holds its first election",
     "It cannot begin unless a country is already federal"], ans=0,
   why="EK PAU-1.C.1 states that the process can start or temporarily change direction while aiming at its listed results over time, and EK PAU-1.C.4 adds that democratization can stall or be reversed. Both statements deny that the path is a straight line."),
 dict(q="A state that had restricted voting to property owners and to men extends the franchise to every adult citizen. Which of democratization's aims does this most directly serve?",
   choices=[
     "universal suffrage for adult citizens",
     "greater governmental transparency",
     "establishment of the rule of law",
     "increased citizen participation in policy-making processes between elections",
     "protection of civil rights and liberties for religious minorities"], ans=0,
   why="EK PAU-1.C.1.c names universal suffrage for adult citizens among the outcomes democratization aims at. Extending the vote to every adult is that outcome directly, whereas the other aims listed concern information, law, policy consultation and liberties rather than eligibility to vote."),
 dict(q="A state repeals statutes that had barred members of a religious minority from public employment and from giving evidence in court. Which of democratization's aims does this most directly serve?",
   choices=[
     "equal treatment of citizens",
     "universal suffrage for adult citizens",
     "more competition and fairness in elections",
     "greater governmental transparency",
     "increased citizen participation in policy-making processes"], ans=0,
   why="EK PAU-1.C.1.f names equal treatment of citizens among democratization's aims, and legal disabilities attached to membership of a religious group are the clearest denial of it. The repeal changes neither the franchise, the conduct of elections, nor the flow of information about policy making."),
 dict(q="Officials in a state have long allocated construction permits by discretionary decision. A new law sets published criteria, requires written reasons, and makes each decision reviewable in court. Which of democratization's aims does this most directly serve?",
   choices=[
     "establishment of the rule of law",
     "universal suffrage for adult citizens",
     "increased citizen participation in policy-making processes",
     "more competition and fairness in elections",
     "equal treatment of citizens in the allocation of legislative seats"], ans=0,
   why="EK PAU-1.C.1.g names establishment of the rule of law among democratization's aims, and EK PAU-1.B.1.a describes the rule of law as governance by law rather than by arbitrary decisions of individual officials. Published criteria, stated reasons and judicial review replace exactly that discretion."),
 dict(q="A state begins requiring ministries to publish draft regulations, take written comments from the public, and respond to them before a regulation takes effect. Which of democratization's aims does this most directly serve?",
   choices=[
     "increased citizen participation in policy-making processes",
     "universal suffrage for adult citizens",
     "equal treatment of citizens before the courts",
     "establishment of the rule of law in commercial disputes",
     "more competition among candidates at elections"], ans=0,
   why="EK PAU-1.C.1.b names increased citizen participation in policy-making processes among democratization's aims, and a consultation requirement creates participation between elections rather than at them. Voting eligibility, court treatment and candidate competition are separate aims on the same list."),
 dict(q="Which pair of changes would the framework treat as advancing democratization's electoral aims specifically, rather than its other aims?",
   choices=[
     "Allowing previously barred parties to nominate candidates, and publishing results constituency by constituency",
     "Extending the vote to adults who had been excluded, and repealing employment restrictions on a minority",
     "Publishing draft regulations for comment, and requiring ministries to answer written questions",
     "Making administrative decisions reviewable in court, and setting published criteria for permits",
     "Transferring several services from national to regional administration"], ans=0,
   why="EK PAU-1.C.1.a names more competition, fairness and transparency in elections, and both halves of the keyed pair change how an election is contested and reported. The other pairings serve suffrage and equal treatment, participation in policy making, the rule of law, and territorial administration respectively."),
 dict(q="A government that had published only its final decisions begins releasing the analyses, cost estimates and internal advice behind them. The framework would count this as progress toward",
   choices=[
     "greater governmental transparency",
     "universal suffrage for adult citizens",
     "protected civil rights and civil liberties",
     "establishment of the rule of law",
     "equal treatment of citizens"], ans=0,
   why="EK PAU-1.C.1.d names greater governmental transparency among democratization's aims and EK DEM-1.C.4 defines a transparent government as one that lets information about government and policy making circulate openly. Releasing the reasoning behind decisions is that, and it changes no rule about voting, liberties, law or equal treatment."),
 dict(q="A country undertakes all of the following at once. Which of them is NOT among the outcomes the framework lists as aims of democratization?",
   choices=[
     "replacing its federal structure with a unitary one",
     "protecting civil rights and civil liberties",
     "extending the vote to all adult citizens",
     "increasing the transparency of government decision making",
     "establishing the rule of law"], ans=0,
   why="EK PAU-1.C.1 lists seven aims and territorial structure is not among them; EK PAU-2.A.1 treats federal and unitary organization as a separate classification, and the framework's own lists put a clear democracy and a one-party state in the same unitary group. The other four options are items .e, .c, .d and .g of the aims list."),
 dict(q="According to the framework, democratic electoral systems can accommodate ethnic diversity and increase multiparty competition through rule adjustments. Which set of adjustments does it name?",
   choices=[
     "gender or cultural quotas, proportional representation, and changes in vote thresholds and district boundaries",
     "term limits on the head of government and fixed dates for elections",
     "replacing a bicameral legislature with a unicameral one",
     "transferring the certification of results from a commission to the courts",
     "raising the minimum age at which citizens may vote"], ans=0,
   why="EK PAU-1.C.2 names exactly these adjustments as ways a democratic electoral system can accommodate ethnic diversity and increase multiparty competition. Term limits, chamber structure, certification and voting age are treated by the framework under other statements and are not offered as tools for this purpose."),
 dict(q="The framework credits gender quotas in one course country's party list system with helping to increase female representation in its legislature. That country is",
   choices=[
     "Mexico",
     "China",
     "Iran",
     "Russia",
     "Nigeria"], ans=0,
   why="EK DEM-2.A.1.c states that gender quotas in the party list system have helped increase female representation in Mexico's legislature, alongside its 300 district and 200 list deputies. The framework attributes no such quota effect to the other course countries."),
 dict(q="Why does the framework treat proportional representation as a tool for accommodating ethnic diversity?",
   choices=[
     "Because it can raise the number of parties represented in a legislature and the election of minority candidates, so a group too small to win any district can still be represented",
     "Because it requires every party to nominate candidates from every ethnic group",
     "Because it eliminates the need for political parties altogether",
     "Because it guarantees that the largest party will hold a majority of the seats",
     "Because it replaces elections with appointment by an independent commission"], ans=0,
   why="EK PAU-1.C.2 names proportional representation among the adjustments accommodating ethnic diversity and EK DEM-2.B.1 supplies the mechanism, an increase in the number of parties represented and in the election of minority and women candidates. A dispersed minority that loses every district can still clear a list threshold."),
 dict(q="The framework's account of the relationship between corruption and democratization is that",
   choices=[
     "political corruption inhibits democratization, and independent judiciaries can reduce it while protecting individual liberties and civil rights",
     "political corruption has no bearing on democratization, which depends only on election rules",
     "corruption advances democratization by drawing new participants into politics",
     "corruption can be removed only by concentrating power in a single executive",
     "corruption is a problem only in regimes that have already consolidated"], ans=0,
   why="EK PAU-1.C.3 states that political corruption inhibits democratization and that independent judiciaries can reduce such corruption while protecting individual liberties and civil rights. The framework thus makes judicial independence do two jobs at once rather than treating corruption as a separate technical problem."),
 dict(q="A state seeking to reduce corruption creates an anticorruption agency whose director serves at the pleasure of the head of government and whose cases are heard by judges the head of government may remove. A comparativist applying the framework would object that",
   choices=[
     "the arrangement lacks the judicial independence the framework identifies as what makes corruption control effective",
     "anticorruption agencies are not mentioned anywhere in the framework's account of democratization",
     "corruption cannot be reduced in a unitary state",
     "the agency should be abolished because corruption advances democratization",
     "the arrangement is acceptable because the agency exists in written law"], ans=0,
   why="EK PAU-1.C.3 assigns the corruption-reducing role specifically to independent judiciaries, and EK PAU-1.B.2 treats independence among branches as what stops one branch from controlling all governmental power. Investigators and judges removable by the official they might investigate supply neither."),
 dict(q="Which statement most accurately reflects the framework's view of how policy changes to election rules and civil liberties bear on democratization?",
   choices=[
     "They can either support or impede it, and democratization can stall or be reversed",
     "They can only support it, since any change to election rules widens competition",
     "They have no effect, because democratization depends on economic growth alone",
     "They matter only after a regime has already consolidated",
     "They determine whether a state is federal or unitary"], ans=0,
   why="EK PAU-1.C.4 states that democratization can stall or be reversed and that policy changes regarding election rules and civil liberties can support or impede it. The framework is deliberately two-sided here, so a claim that rule changes only ever help contradicts it."),
 dict(q="The framework defines democratic consolidation as the process by which a democratic regime matures in terms of",
   choices=[
     "election rules, separation of powers, and protection of civil liberties",
     "population size, territory, and international recognition",
     "economic growth, resource wealth, and trade openness",
     "the number of registered parties and the size of the legislature",
     "the length of terms served by the head of state and the head of government"], ans=0,
   why="EK PAU-1.C.5 names exactly these three dimensions of maturing, and adds that consolidation makes reversion to authoritarianism unlikely without an external shock. The rejected lists describe statehood, economic performance, party arithmetic and terms of office."),
 dict(q="Which comparison correctly distinguishes democratization from democratic consolidation?",
   choices=[
     "Democratization is the transition out of an authoritarian regime, whereas consolidation is the maturing of a regime that is already democratic",
     "Democratization is the maturing of a democratic regime, whereas consolidation is the transition out of authoritarianism",
     "Both terms describe the same process at different speeds",
     "Democratization applies only to federal states and consolidation only to unitary ones",
     "Consolidation must be completed before democratization can begin"], ans=0,
   why="EK PAU-1.C.1 defines democratization as a transition from an authoritarian to a democratic regime and EK PAU-1.C.5 defines consolidation as the maturing of a democratic regime until reversion becomes unlikely. The second presupposes the first has succeeded, so the order cannot be inverted."),
 dict(q="The framework says a consolidated democracy is unlikely to revert to authoritarianism without an external shock. The point of that qualification is that",
   choices=[
     "consolidation makes reversal improbable rather than impossible, since a sufficiently severe outside disturbance could still produce one",
     "consolidation guarantees that reversal can never occur under any circumstances",
     "reversal is likely in every consolidated democracy within a generation",
     "only foreign invasion can end a democratic regime",
     "consolidation is complete only when a country joins a supranational organization"], ans=0,
   why="EK PAU-1.C.5 states that consolidation makes reversion unlikely WITHOUT an external shock, which is a statement about probability with a named exception rather than a guarantee. EK PAU-1.C.4's warning that democratization can be reversed is the reason the framework hedges."),
 dict(q="According to the framework, what makes a democratization process sustainable?",
   choices=[
     "consensus among competing cultural and political groups about the policies associated with democratization and economic development",
     "a single party winning every election by a wide margin",
     "the concentration of decision making in the national executive",
     "the exclusion of groups whose views differ from the governing party's",
     "the postponement of elections until economic growth resumes"], ans=0,
   why="EK PAU-1.C.6 states that consensus among competing cultural and political groups about governmental policies associated with democratization and economic development can advance the process and make it sustainable. The agreement it describes is across rival groups, which is the opposite of excluding them."),
 dict(q="The table reports hypothetical figures for three countries over two decades. Which country's record best fits the framework's description of democratization?",
   table=_T_TREND,
   choices=[
     "Country A, whose electorate widened by 36 percentage points and which held competitive elections in four of five contests",
     "Country B, whose electorate was already nearly universal and widened by 1 percentage point",
     "Country C, whose electorate narrowed by 16 percentage points",
     "All three equally, since each held five elections over the period",
     "None of the three, because the framework gives no figures for any country"], ans=0,
   why="EK PAU-1.C.1 defines democratization as a transition out of an authoritarian regime aiming at universal suffrage and at more competition and fairness in elections. Only one row shows a large widening of the franchise together with mostly competitive contests, which is what a transition looks like in data."),
 dict(q="Using the same table, which country's record best illustrates the framework's statement that democratization can stall or be reversed?",
   table=_T_TREND,
   choices=[
     "Country C, whose electorate narrowed and which held only one competitive election out of five",
     "Country A, whose electorate widened sharply",
     "Country B, whose electorate barely changed but whose elections were all competitive",
     "None of the three, because reversal cannot be seen in numbers",
     "All three, because every country's figures changed to some degree"], ans=0,
   why="EK PAU-1.C.4 states that democratization can stall or be reversed and that policy changes regarding election rules and civil liberties can impede it. A shrinking franchise combined with contests that observers judge uncompetitive is movement away from two of the aims at once."),
 dict(q="A student concludes from the table that the country whose figures changed least is the one democratizing fastest. The best objection is that",
   table=_T_TREND,
   choices=[
     "that country's franchise was already nearly universal and its elections already competitive, so there is little for a transition to change and no authoritarian starting point in the data",
     "the table does not report any information about elections",
     "a country with competitive elections cannot be democratic",
     "the table's figures are hypothetical and therefore cannot be compared with one another",
     "democratization is measured only by economic growth"], ans=0,
   why="EK PAU-1.C.1 makes democratization a transition FROM an authoritarian regime, so a country already at the top of both measures has no such transition under way. EK PAU-1.C.5 would describe its situation as consolidation instead, which is a different process with a different definition."),
 dict(q="The table compares three hypothetical legislatures. Which comparison isolates the association between a gender quota and the share of women serving?",
   table=_T_QUOTA,
   choices=[
     "The first two legislatures, because they use the same electoral rule and differ only in whether a quota applies",
     "The first and third legislatures, because they differ by the largest margin",
     "The second and third legislatures, because neither applies a quota",
     "All three at once, because more comparisons always give a firmer conclusion",
     "None of them, because a quota cannot affect who is elected"], ans=0,
   why="EK PAU-1.C.2 names gender quotas and proportional representation as two separate adjustments, so a comparison meant to speak to the quota must hold the electoral rule constant. EK MPA-1.A.3's warning that numerous variables influence an outcome is exactly the reason for holding one of them fixed."),
 dict(q="Using the same table, comparing the second and third legislatures speaks most directly to",
   table=_T_QUOTA,
   choices=[
     "the association between the electoral rule itself and women's share of the seats, since neither of those two legislatures applies a quota",
     "the effect of a gender quota, since both legislatures use party lists",
     "the effect of a cultural quota on minority representation",
     "the difference between a unitary and a federal state",
     "nothing at all, because the two legislatures differ in more than one respect"], ans=0,
   why="Those two rows differ in electoral rule and agree in having no quota, so the rule is the variable left standing. EK DEM-2.B.1 predicts the direction, since proportional representation is associated with a higher election rate for women and minority candidates than single-member district plurality."),
 dict(q="Which comparison correctly states what the framework says each of these two course countries transitioned away from on its route to becoming a multiparty republic?",
   choices=[
     "Nigeria transitioned away from military rule and Mexico away from single-party dominance",
     "Nigeria transitioned away from single-party dominance and Mexico away from military rule",
     "Both transitioned away from theocratic rule",
     "Both transitioned away from rule by a hereditary monarch",
     "Neither transitioned, since both have always been multiparty republics"], ans=0,
   why="EK PAU-1.D.1.c states the transition of power in Nigeria and Mexico to multiparty republics following military rule and single-party dominance respectively. The order matters, and the framework's word 'respectively' fixes it."),
 dict(q="Which set of measures does the framework name as having facilitated one course country's transition away from one-party dominance?",
   choices=[
     "eliminating el dedazo, privatizing state-owned corporations to decrease patronage, reducing one-party power at the subnational level, and establishing and strengthening a national electoral institute",
     "nationalizing broadcast media and raising the threshold for party registration",
     "appointing regional governors from a list approved by the head of state",
     "vetting candidates for their support of the state religion before each election",
     "replacing proportional representation with appointment to the upper chamber"], ans=0,
   why="EK PAU-4.A.4 names exactly these rules as facilitating Mexico's transition away from one-party dominance. The rejected options are the framework's descriptions of measures in Russia and Iran, which EK PAU-4.A.3 and EK DEM-2.B.4.a present as narrowing competition rather than widening it."),
 dict(q="The elimination of el dedazo is presented by the framework as a step away from one-party dominance because it ended",
   choices=[
     "the outgoing leader's personal designation of the governing party's next presidential nominee",
     "the direct election of members of the lower chamber of the legislature",
     "the requirement that presidential candidates win a plurality of the national vote",
     "the independence of the body that administers elections",
     "the practice of holding legislative and presidential elections on the same day"], ans=0,
   why="EK PAU-4.A.4 lists eliminating el dedazo among the rules facilitating Mexico's transition away from one-party dominance, alongside measures reducing patronage and subnational one-party power. What the practice supplied was a succession decided inside the dominant party rather than by voters, which is why ending it loosens that dominance."),
 dict(q="Mexico and Nigeria each created an independent election commission during its democratic transition. The framework presents these bodies as serving democratization by",
   choices=[
     "reducing voter fraud and manipulation and enhancing electoral competition",
     "selecting which candidates are ideologically acceptable to stand",
     "appointing the members of the upper chamber of the legislature",
     "setting the length of the president's term in office",
     "allocating legislative seats to parties in proportion to the national vote"], ans=0,
   why="EK DEM-2.B.4.b states that Mexico and Nigeria created independent election commissions as part of their democratic transitions to reduce voter fraud and manipulation and enhance electoral competition, which is EK PAU-1.C.1.a's aim of more competition and fairness in elections stated as an institution."),
 dict(q="Which set of measures would the framework treat as impeding democratization rather than advancing it?",
   choices=[
     "raising party registration requirements, allowing only registered parties to stand, and raising the threshold parties must clear for ballot access",
     "creating an election commission independent of the governing party",
     "extending the franchise to adult citizens previously excluded",
     "publishing the reasoning behind ministerial decisions",
     "making administrative decisions reviewable by an independent court"], ans=0,
   why="EK PAU-4.A.3 lists increasing party registration requirements, restricting candidacy to legally registered parties and increasing threshold rules to limit ballot access among the rules ensuring one-party dominance in Russia, and EK PAU-1.C.4 says policy changes to election rules can impede democratization. The other four options are the framework's own aims and instruments."),
 dict(q="Which finding would most strongly support a claim that a democracy has consolidated in the framework's sense?",
   choices=[
     "Over several decades power has changed hands peacefully under stable election rules, the courts have repeatedly ruled against the government, and civil liberties protections have been extended rather than narrowed",
     "The governing party has won every election since the founding of the regime",
     "The economy has grown in each of the past ten years",
     "The country has recently joined several international economic organizations",
     "The head of government is popular in opinion polls"], ans=0,
   why="EK PAU-1.C.5 defines consolidation by maturity in election rules, separation of powers and protection of civil liberties, and the keyed finding reports exactly those three. Uninterrupted victory by one party bears on EK PAU-4.A.1's dominant party systems, and growth, treaty membership and popularity touch none of the three dimensions."),
]
