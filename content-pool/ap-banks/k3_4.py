# AP COMPARATIVE GOVERNMENT AND POLITICS 3.4 Political Values and Beliefs
# CED effective Fall 2026, Unit 3 Political Culture and Participation. Enduring
# understanding IEF-1; learning objective IEF-1.D (explain how political values and
# beliefs frame policy choices to address particular political problems). Suggested
# skill 3.C, DATA ANALYSIS -- which is why this module carries three quantitative
# sets rather than one.
#
# Essential knowledge relied on:
#   IEF-1.D.1  contrasting political ideologies, INCLUDING RULE BY LAW AS OPPOSED TO
#              RULE OF LAW, affect how the state treats its citizens and deals with
#              specific problems, SUCH AS POLITICAL CORRUPTION
#     .a political beliefs associated with AUTHORITARIAN regimes tend to rely on
#        RULE BY LAW, in which THE STATE USES THE LAW TO REINFORCE THE AUTHORITY OF
#        THE STATE
#     .b political beliefs associated with DEMOCRATIC regimes tend to rely on RULE
#        OF LAW, in which THE STATE IS LIMITED TO THE SAME RULES AS ITS CITIZENS
#   IEF-1.D.2  beliefs about social and economic equality CAN BE HELD BY CITIZENS IN
#              BOTH democratic and authoritarian regimes, but can be contrasted by
#              the AMOUNT OF ENFORCEMENT RESPONSIBILITY TRANSFERRED TO THE GOVERNMENT
#              and the AMOUNT OF CHOICE AFFORDED TO CITIZENS to protect their health
#              and material well-being, RANGING FROM LIMITED GOVERNMENTAL SOCIAL
#              PROTECTIONS TO A WELFARE STATE
#   IEF-1.D.3  POST-MATERIALISM refers to social valuing of SELF-EXPRESSION AND
#              QUALITY OF LIFE that leads to applying pressure on governments to
#              address ENVIRONMENTAL ISSUES and SOCIAL AND ECONOMIC EQUALITY
#
# IEF-1.D.2 is another of the framework's difference-of-degree statements: the
# BELIEF in equality is available in both regime types, and what differs is how
# much enforcement is transferred to government and how much choice is left to
# citizens. Items 8 and 19 key that, because the intuitive reading -- that only one
# kind of regime's citizens hold such beliefs -- is not the framework's.
#
# Supporting statements, named in the verifier's claims: PAU-3.G.1.a (rule by law
# in China, the judicial system subservient to the party), PAU-3.G.1.i (common law
# enforcing the rule of law in the United Kingdom), PAU-1.B.1.a (the rule of law as
# governance by law rather than by arbitrary decisions), PAU-1.C.3 (corruption
# inhibits democratization), IEF-1.C.6.b and .d (neoliberalism and socialism).
#
# Table figures are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("3.4", "Political Values and Beliefs", 3)

_T_RULE = dict(
    headers=["Country (hypothetical)", "Senior officials prosecuted for corruption, 2010-2020",
             "Of those, the share who were officials of the governing party (percent)",
             "Share of prosecutions of opposition figures later overturned on appeal (percent)"],
    rows=[["Country H", "60", "45", "4"],
          ["Country J", "50", "4", "40"],
          ["Country K", "30", "30", "12"]])

_T_EQ = dict(
    headers=["Country (hypothetical)",
             "Share agreeing the government should guarantee everyone's basic needs (percent)",
             "Public social spending as a share of gross domestic product (percent)",
             "Share saying individuals should choose and pay for their own health cover (percent)"],
    rows=[["Country L", "78", "29", "19"],
          ["Country M", "74", "11", "62"],
          ["Country N", "41", "14", "55"]])

_T_PM = dict(
    headers=["Priority named as most important (hypothetical survey)",
             "Share in 1990 (percent)", "Share in 2020 (percent)"],
    rows=[["Economic growth and material security", "61", "34"],
          ["Self-expression and quality of life", "18", "39"],
          ["Environmental protection", "9", "19"],
          ["Social and economic equality", "12", "8"]])

QUESTIONS = [
 dict(q="According to the framework, what do contrasting political ideologies affect?",
   choices=[
     "how the state treats its citizens and how it deals with specific problems such as political corruption",
     "the territorial structure of the state",
     "the number of chambers in the legislature",
     "whether a state receives international recognition",
     "the length of the head of government's term"], ans=0,
   why="EK IEF-1.D.1 states that contrasting political ideologies, including rule by law as opposed to rule of law, affect how the state treats its citizens and deals with specific problems, such as political corruption. Institutional structure and recognition are treated under other statements."),
 dict(q="How does the framework define rule by law?",
   choices=[
     "an arrangement in which the state uses the law to reinforce the authority of the state",
     "an arrangement in which the state is limited to the same rules as its citizens",
     "an arrangement in which no written law exists",
     "an arrangement in which courts may strike down any statute",
     "an arrangement in which citizens vote directly on legal questions"], ans=0,
   why="EK IEF-1.D.1.a defines rule by law as an arrangement in which the state uses the law to reinforce the authority of the state, and associates it with political beliefs found in authoritarian regimes. EK PAU-3.G.1.a applies the same phrase to a judicial system subservient to a governing party."),
 dict(q="How does the framework define rule of law?",
   choices=[
     "an arrangement in which the state is limited to the same rules as its citizens",
     "an arrangement in which the state uses the law to reinforce its own authority",
     "an arrangement in which the legislature may not pass any law limiting citizens",
     "an arrangement in which judges are elected rather than appointed",
     "an arrangement in which the constitution may never be amended"], ans=0,
   why="EK IEF-1.D.1.b defines rule of law as an arrangement in which the state is limited to the same rules as its citizens, and associates it with political beliefs found in democratic regimes. EK PAU-1.B.1.a adds that the rule of law means governance by law rather than by arbitrary decisions of individual officials."),
 dict(q="Which regime types does the framework associate with each of these two arrangements?",
   choices=[
     "political beliefs associated with authoritarian regimes tend to rely on rule by law, and those associated with democratic regimes on rule of law",
     "political beliefs associated with authoritarian regimes tend to rely on rule of law, and those associated with democratic regimes on rule by law",
     "both regime types rely equally on rule by law",
     "both regime types rely equally on rule of law",
     "the framework does not associate either arrangement with a regime type"], ans=0,
   why="EK IEF-1.D.1.a and EK IEF-1.D.1.b make exactly this pairing, using the hedge 'tend to' in each case. Reversing the pairing contradicts both statements."),
 dict(q="In one country the government prosecutes journalists under a broadly worded statute whenever they criticize officials, while officials themselves are never charged. Which of the framework's two arrangements does this illustrate?",
   choices=[
     "rule by law, since the state is using the law to reinforce its own authority",
     "rule of law, since the state is applying a statute the legislature passed",
     "rule of law, since the courts are involved in the process",
     "neither, since the framework's distinction applies only to civil cases",
     "both equally, since law is being applied"], ans=0,
   why="EK IEF-1.D.1.a defines rule by law as the state using the law to reinforce the authority of the state, which a statute applied only against critics does. EK IEF-1.D.1.b's rule of law requires the state to be limited to the same rules as its citizens, which the immunity of officials denies."),
 dict(q="In a second country a minister who broke a public procurement rule is prosecuted under the same statute that governs private contractors, and the courts apply it identically. Which arrangement does this illustrate?",
   choices=[
     "rule of law, since the state is limited to the same rules as its citizens",
     "rule by law, since the state is enforcing a statute",
     "rule by law, since the prosecution strengthens confidence in the state",
     "neither, since the framework's distinction applies only to criminal cases",
     "both equally, since law is being applied"], ans=0,
   why="EK IEF-1.D.1.b defines rule of law as an arrangement in which the state is limited to the same rules as its citizens, and applying one procurement statute identically to a minister and a contractor is exactly that. That a prosecution may also strengthen confidence does not change which arrangement it illustrates."),
 dict(q="How does the framework's rule-by-law and rule-of-law distinction bear on political corruption specifically?",
   choices=[
     "the two arrangements produce different ways of dealing with corruption, since one exempts the state from the rules it enforces and the other does not",
     "the distinction has no bearing on corruption, which the framework treats separately",
     "both arrangements treat corruption identically",
     "corruption is possible only where the rule of law prevails",
     "corruption is possible only where rule by law prevails"], ans=0,
   why="EK IEF-1.D.1 names political corruption as one of the specific problems contrasting ideologies affect how a state deals with, and EK IEF-1.D.1.a and .b differ precisely on whether the state is bound by the rules it applies. EK PAU-1.C.3 adds that corruption inhibits democratization in either case."),
 dict(q="What does the framework say about who can hold beliefs about social and economic equality?",
   choices=[
     "such beliefs can be held by citizens in both democratic and authoritarian regimes",
     "such beliefs are held only by citizens in democratic regimes",
     "such beliefs are held only by citizens in authoritarian regimes",
     "such beliefs are held only where a welfare state already exists",
     "the framework does not discuss beliefs about equality"], ans=0,
   why="EK IEF-1.D.2 states that beliefs about social and economic equality can be held by citizens in both democratic and authoritarian regimes. The statement then contrasts the two by degree, which is the same pattern as EK DEM-1.C.2 on media and EK DEM-1.B.3 on participation."),
 dict(q="On what two dimensions does the framework say beliefs about equality can be contrasted?",
   choices=[
     "the amount of enforcement responsibility transferred to the government and the amount of choice afforded to citizens to protect their health and material well-being",
     "the number of political parties and the length of the electoral term",
     "the territorial structure of the state and its international recognition",
     "the length of judicial terms and the method of judicial appointment",
     "the rate of economic growth and the level of foreign investment"], ans=0,
   why="EK IEF-1.D.2 names exactly these two dimensions of contrast and gives their range, from limited governmental social protections to a welfare state. Institutional and economic features appear elsewhere in the framework and not under this heading."),
 dict(q="What range does the framework give for the arrangements that beliefs about equality can produce?",
   choices=[
     "from limited governmental social protections to a welfare state",
     "from no law at all to a written constitution",
     "from a unitary state to a federal state",
     "from one political party to many",
     "from rule by law to rule of law"], ans=0,
   why="EK IEF-1.D.2 gives the range as running from limited governmental social protections to a welfare state, which is a range of how much enforcement responsibility has been transferred to government. Rule by law and rule of law are the range EK IEF-1.D.1 gives for a different question."),
 dict(q="A state guarantees health care, pensions and unemployment support to every resident and funds them from general taxation. Where does this sit on the range the framework describes?",
   choices=[
     "at the welfare state end, where a large amount of enforcement responsibility has been transferred to government",
     "at the limited governmental social protections end",
     "outside the range, since the framework describes only economic ideologies",
     "at the rule by law end of a different range",
     "at the midpoint, since taxation is involved"], ans=0,
   why="EK IEF-1.D.2 makes the amount of enforcement responsibility transferred to the government one of its two dimensions and gives the welfare state as the upper end of the range. Universal provision funded from taxation transfers that responsibility to the government."),
 dict(q="A second state provides a minimal safety net and expects individuals to buy their own health cover and provide for their own retirement. Where does this sit on the same range?",
   choices=[
     "at the limited governmental social protections end, where more choice is left to citizens",
     "at the welfare state end",
     "outside the range, since the framework describes only political institutions",
     "at the rule of law end of a different range",
     "at the midpoint, since a safety net still exists"], ans=0,
   why="EK IEF-1.D.2 pairs the amount of enforcement responsibility transferred to government with the amount of choice afforded to citizens to protect their health and material well-being, and gives limited governmental social protections as the lower end of the range. This arrangement transfers little and leaves much to individual choice."),
 dict(q="How does the framework define post-materialism?",
   choices=[
     "social valuing of self-expression and quality of life",
     "belief in the abolition of private property",
     "belief in limited governmental intervention in the economy",
     "the lifelong process of acquiring political beliefs",
     "the collective attitudes and values of an entire citizenry"], ans=0,
   why="EK IEF-1.D.3 defines post-materialism as social valuing of self-expression and quality of life. The rejected options are EK IEF-1.C.6.c's communism, EK IEF-1.C.6.b's neoliberalism, EK IEF-1.C.3's socialization and EK IEF-1.C.1's political culture."),
 dict(q="According to the framework, what does post-materialism lead to?",
   choices=[
     "pressure on governments to address environmental issues and social and economic equality",
     "pressure on governments to privatize state-owned industry",
     "pressure on governments to abolish private property",
     "pressure on governments to lengthen the head of government's term",
     "pressure on governments to withdraw from supranational organizations"], ans=0,
   why="EK IEF-1.D.3 states that post-materialism leads to applying pressure on governments to address environmental issues and social and economic equality. Both objects of that pressure are named in the same sentence."),
 dict(q="Citizens in a prosperous country increasingly campaign for cleaner air, protected landscapes and narrower income gaps, and describe these as matters of the kind of life they want rather than of material security. Which framework concept does this illustrate?",
   choices=[
     "post-materialism",
     "neoliberalism",
     "rule by law",
     "political socialization",
     "civil society autonomy"], ans=0,
   why="EK IEF-1.D.3 defines post-materialism as social valuing of self-expression and quality of life leading to pressure on governments to address environmental issues and social and economic equality, which is exactly the combination described."),
 dict(q="Which comparison of post-materialism with the ideologies the framework defines is accurate?",
   choices=[
     "Post-materialism is described as a social valuing of self-expression and quality of life producing pressure on government, whereas an ideology is a set of values and beliefs about the goals of government, public policy or politics",
     "Post-materialism is one of the six ideologies the framework names",
     "Post-materialism and neoliberalism are defined identically",
     "Post-materialism and socialism are defined identically",
     "Post-materialism concerns only the ownership of industry"], ans=0,
   why="EK IEF-1.D.3 introduces post-materialism as a social valuing that generates pressure on governments, while EK IEF-1.C.6 defines a political ideology and names six of them, none of which is post-materialism. The two ideas sit under different learning objectives."),
 dict(q="Which of the framework's country descriptions is the clearest instance of rule by law?",
   choices=[
     "a judicial system subservient to the decisions of a governing party that controls most judicial appointments",
     "a judicial system using common law to enforce the rule of law",
     "a judiciary whose Supreme Court rules on devolution disputes",
     "a judiciary whose magistrates are approved by an elected senate for fifteen years",
     "a judiciary recommended by a judicial council and confirmed by an elected senate"], ans=0,
   why="EK PAU-3.G.1.a states that in China rule by law, instead of rule of law, means the judicial system is subservient to the decisions of the Chinese Communist Party, which controls most judicial appointments. EK IEF-1.D.1.a supplies the general definition that description instantiates."),
 dict(q="Which of the framework's country descriptions is the clearest instance of rule of law?",
   choices=[
     "a judicial system that uses common law to enforce the rule of law",
     "a judicial system subservient to a governing party's decisions",
     "a judiciary whose major function is to ensure the legal system rests on religious law",
     "courts that hold judicial review constitutionally but have not used it against the governing branches",
     "a government that uses the judicial system to target opposition"], ans=0,
   why="EK PAU-3.G.1.i states that the United Kingdom's judicial system uses common law to enforce the rule of law, and EK IEF-1.D.1.b defines rule of law as the state being limited to the same rules as its citizens. The rejected descriptions are the framework's own accounts of China, Iran and Russia."),
 dict(q="A student writes that only citizens of democratic regimes care about social and economic equality. What does the framework say?",
   choices=[
     "beliefs about social and economic equality can be held in both regime types, and what differs is how much enforcement is transferred to government and how much choice is left to citizens",
     "beliefs about equality are held only in democratic regimes",
     "beliefs about equality are held only in authoritarian regimes",
     "beliefs about equality have no effect on policy in any regime",
     "beliefs about equality are identical in every country"], ans=0,
   why="EK IEF-1.D.2 states that such beliefs can be held by citizens in both democratic and authoritarian regimes and then contrasts them by the amount of enforcement responsibility transferred to government and the amount of choice afforded to citizens. The difference is one of arrangement, not of who holds the belief."),
 dict(q="The table reports hypothetical corruption-prosecution records for three countries. Which record best fits the framework's description of rule by law?",
   table=_T_RULE,
   choices=[
     "Country J, where officials of the governing party are almost never among those prosecuted and most prosecutions of opposition figures are later overturned",
     "Country H, where nearly half of those prosecuted are officials of the governing party",
     "Country K, which prosecuted the fewest officials",
     "None of the three, since prosecution records say nothing about how law is used",
     "All three equally, since each prosecuted some officials"], ans=0,
   why="EK IEF-1.D.1.a defines rule by law as the state using the law to reinforce the authority of the state, so the pattern to look for is enforcement that spares the governing party and falls on its opponents without surviving review. One row shows both at once."),
 dict(q="Using the same table, which record best fits the framework's description of rule of law?",
   table=_T_RULE,
   choices=[
     "Country H, where officials of the governing party make up the largest share of those prosecuted and few prosecutions of opposition figures are overturned",
     "Country J, where prosecutions of opposition figures are most often overturned",
     "Country K, whose figures fall between the other two on both measures",
     "None of the three, since the rule of law cannot be observed in prosecutions",
     "Both Country H and Country K, since neither overturns most appeals"], ans=0,
   why="EK IEF-1.D.1.b defines rule of law as an arrangement in which the state is limited to the same rules as its citizens, so a record in which the governing party's own officials are prosecuted at a high rate and prosecutions survive appeal is the closest fit. EK PAU-1.B.1.a's governance by law rather than by arbitrary decision points the same way."),
 dict(q="According to the same table, the number of governing-party officials among the first country's prosecutions is",
   table=_T_RULE,
   choices=[
     "27",
     "45",
     "33",
     "60",
     "9"], ans=0,
   why="Applying that country's governing-party share to its total number of prosecutions gives the count. The alternatives offer the percentage itself, the number of prosecutions that were not of governing-party officials, the row's total, and the corresponding count for a different row."),
 dict(q="The table reports hypothetical figures on equality and social provision. Which pair of countries best illustrates the framework's claim that similar beliefs about equality can go with very different arrangements?",
   table=_T_EQ,
   choices=[
     "Country L and Country M, whose shares agreeing that government should guarantee basic needs are within a few points of each other while their social spending differs by 18 points of gross domestic product",
     "Country L and Country N, whose shares agreeing differ by 37 points",
     "Country M and Country N, whose social spending differs by 3 points",
     "None of the three pairs, since belief and provision always move together",
     "All three pairs equally, since every pair differs on something"], ans=0,
   why="EK IEF-1.D.2 states that beliefs about social and economic equality can be held in both regime types but contrasted by the amount of enforcement responsibility transferred to government. The pair that agrees on the belief and diverges sharply on the provision is the one that shows the claim."),
 dict(q="According to the same table, the difference in public social spending between the two countries whose shares agreeing are closest together is",
   table=_T_EQ,
   choices=[
     "18 percentage points of gross domestic product",
     "15 percentage points of gross domestic product",
     "3 percentage points of gross domestic product",
     "4 percentage points of gross domestic product",
     "29 percentage points of gross domestic product"], ans=0,
   why="Identifying the two rows whose agreement shares are nearest each other and subtracting their social spending figures gives the difference. The alternatives are the spending gaps between other pairs, the gap in the agreement column for the same pair, and the largest single spending figure."),
 dict(q="Using the same table, which country sits nearest the limited governmental social protections end of the framework's range?",
   table=_T_EQ,
   choices=[
     "Country M, with the lowest social spending and the highest share saying individuals should choose and pay for their own health cover",
     "Country L, with the highest social spending",
     "Country N, with the lowest share agreeing that government should guarantee basic needs",
     "None of the three, since every country provides something",
     "Both Country M and Country N, since neither spends as much as Country L"], ans=0,
   why="EK IEF-1.D.2 pairs the amount of enforcement responsibility transferred to government with the amount of choice afforded to citizens, so the row that is lowest on the first and highest on the second sits nearest the limited-protections end. A low share agreeing about government's duty is a belief rather than an arrangement."),
 dict(q="The table reports how a hypothetical population's stated priorities changed over thirty years. Which change best matches the framework's account of post-materialism?",
   table=_T_PM,
   choices=[
     "the rise of self-expression and quality of life, alongside a rise in environmental protection and a fall in economic growth and material security",
     "the fall in social and economic equality, alongside the fall in economic growth",
     "the rise in environmental protection alone, with no other change",
     "the fall in economic growth alone, with no other change",
     "no change consistent with post-materialism appears in the table"], ans=0,
   why="EK IEF-1.D.3 defines post-materialism as social valuing of self-expression and quality of life that leads to pressure on governments to address environmental issues and social and economic equality. The rise of the value itself, together with a rise in one of the objects of that pressure and a fall in material priorities, is the pattern the definition predicts."),
 dict(q="According to the same table, the combined 2020 share for the two priorities the framework names as the objects of post-materialist pressure is",
   table=_T_PM,
   choices=[
     "27 percent",
     "58 percent",
     "39 percent",
     "21 percent",
     "19 percent"], ans=0,
   why="EK IEF-1.D.3 names environmental issues and social and economic equality as what post-materialism presses governments to address, so the two corresponding rows are the ones to add in the 2020 column. The alternatives add the wrong rows, use the wrong year, or read a single row."),
 dict(q="Which finding would most strongly indicate that a country is moving toward the framework's rule of law rather than rule by law?",
   choices=[
     "Officials of the governing party are now prosecuted under the same statutes as private citizens, and courts have annulled executive actions taken outside the law",
     "The legislature has passed a larger number of statutes than in previous years",
     "The government has created a new anticorruption agency reporting to the head of government",
     "Prosecutions of opposition figures have increased",
     "The constitution has been amended to lengthen judicial terms without changing who appoints judges"], ans=0,
   why="EK IEF-1.D.1.b defines rule of law as an arrangement in which the state is limited to the same rules as its citizens, so the evidence must show the state being bound. A larger statute book, an agency answering to the executive, more prosecutions of opponents and a longer term under unchanged appointment do not show that."),
 dict(q="Which finding would most strongly indicate rising post-materialism in the framework's sense?",
   choices=[
     "Over a generation, more citizens name self-expression and quality of life as their leading priority and press government on environmental and equality questions",
     "Over a generation, incomes have risen and unemployment has fallen",
     "Over a generation, turnout at national elections has risen",
     "Over a generation, the number of registered political parties has increased",
     "Over a generation, public spending on defence has grown"], ans=0,
   why="EK IEF-1.D.3 defines post-materialism as social valuing of self-expression and quality of life leading to pressure on governments to address environmental issues and social and economic equality, so the evidence must include both the valuing and the pressure. Prosperity, turnout, party counts and defence spending are none of that."),
 dict(q="Taking the framework's statements on political values and beliefs together, which summary is most accurate?",
   choices=[
     "Contrasting ideologies shape how a state treats citizens and handles corruption, with rule by law and rule of law as the framework's leading contrast; beliefs about equality exist in both regime types and differ in how much enforcement is transferred to government; and post-materialism presses governments on environmental and equality questions",
     "Political values are identical across regime types and have no effect on policy",
     "Rule by law and rule of law are two names for the same arrangement",
     "Beliefs about equality are held only where a welfare state already exists",
     "Post-materialism refers to a preference for material security over self-expression"], ans=0,
   why="EK IEF-1.D.1 with its two sub-points supplies the rule-by-law and rule-of-law contrast and the corruption application, EK IEF-1.D.2 the cross-regime availability of equality beliefs and the two dimensions of contrast, and EK IEF-1.D.3 the definition of post-materialism and the pressure it produces."),
]
