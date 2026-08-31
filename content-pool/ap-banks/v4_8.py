# AP U.S. GOVERNMENT AND POLITICS 4.8 Ideology and Policymaking -- 30 questions
# CED V.1 (c) 2026, Unit 4 American Political Ideologies and Beliefs.
# Learning objective 4.8.A: explain how U.S. POLITICAL CULTURE (democratic
# ideals, principles, and core values) influences the FORMATION, GOALS, AND
# IMPLEMENTATION of public policy OVER TIME.
# Suggested skill for this topic (CED p. 109): 4.D, source analysis -- explain
# how the VISUAL ELEMENTS OF THE SOURCE (a cartoon, map, or infographic)
# illustrate or relate to political principles, institutions, processes,
# policies, and behaviors.
#
# Essential knowledge relied on:
#   EK 4.8.A.1 -- "Because the U.S. is a democracy with a DIVERSE SOCIETY, public
#     policies generated at any given time reflect the attitudes and beliefs of
#     citizens WHO CHOOSE TO PARTICIPATE IN POLITICS AT THAT TIME."
#   EK 4.8.A.2 -- "The BALANCING DYNAMIC of INDIVIDUAL LIBERTY and GOVERNMENT
#     EFFORTS TO PROMOTE STABILITY AND ORDER has been reflected in policy debates
#     AND THEIR OUTCOMES OVER TIME."
#
# THE CLAUSE THAT CARRIES EK 4.8.A.1 IS "WHO CHOOSE TO PARTICIPATE". Drop it and
# the sentence becomes "policies reflect the attitudes of citizens", which is a
# different and much weaker claim -- and one the framework was careful not to
# make. What the statement actually says is that policy reflects a SUBSET, the
# people who took part, and that the subset is not the population. That is why
# the first table in this module compares the adult population with the voting
# population and with the contacting population: the three columns are not the
# same people, and EK 4.8.A.1's clause is precisely about the difference. It is
# also the sentence that connects this unit to Unit 5's work on turnout.
# Items 3 to 7 turn on it and the verifier refuses its loss.
#
# EK 4.8.A.2 IS A DYNAMIC, NOT A WINNER. The framework says the balancing of
# individual liberty against government efforts to promote stability and order
# "has been REFLECTED IN policy debates AND THEIR OUTCOMES OVER TIME". Three
# things follow, and all three are droppable: it is ongoing rather than settled,
# it shows up in outcomes as well as in argument, and neither side is said to
# prevail. A module that let either side win would be stating a political
# position as course content, so the second table is built with the liberty side
# leading one debate, the order side leading two, and one near even.
#
# WHY THE VISUAL SOURCES ARE LABELLED HYPOTHETICAL AND ATTRIBUTED TO NO ONE.
# The suggested skill is 4.D, which asks about a cartoon, map or infographic --
# and this bank is text. A described cartoon is an honest stimulus: the visual
# elements are stated so the student can reason about them, exactly as skill 4.D
# requires. An INVENTED cartoon attributed to a real cartoonist or publication
# would not be, and it is the same failure mode as a fabricated quotation in
# 4.4: nothing downstream could catch it, because a made-up attribution reads
# exactly like a real one. So items 15 to 19 open "A hypothetical political
# cartoon" and name no artist and no publication, and the verifier enforces it.
#
# Documents the CED attaches to 4.8.A (p. 27): Federalist No. 10 and Adam
# Smith's "The Wealth of Nations". Both are quoted verbatim.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("4.8", "Ideology and Policymaking", 4)

_WHO = ("A hypothetical study compared three populations in one state in the same year: all "
        "adults, those who actually voted, and those who contacted a legislator about a policy "
        "question.")
_WHO_TABLE = dict(
    headers=["Age group", "Share of all adults (%)", "Share of those who voted (%)",
             "Share of those who contacted a legislator (%)"],
    rows=[["Ages 18 to 29", "21", "13", "8"],
          ["Ages 30 to 49", "33", "29", "26"],
          ["Ages 50 to 64", "24", "27", "29"],
          ["Age 65 and older", "22", "31", "37"]])

_BALANCE = ("A hypothetical survey asked about four separate policy questions, each of which "
            "set a claim of individual liberty against a government effort to promote stability "
            "and order. The table reports which side respondents favored in each.")
_BALANCE_TABLE = dict(
    headers=["Policy question", "Favored the individual liberty side (%)",
             "Favored the stability and order side (%)", "Undecided (%)"],
    rows=[["Question 1", "58", "31", "11"],
          ["Question 2", "34", "55", "11"],
          ["Question 3", "47", "44", "9"],
          ["Question 4", "29", "62", "9"]])

QUESTIONS = [
 dict(q="According to the course framework, whose attitudes and beliefs do public policies generated at any given time reflect?",
   choices=[
     "Citizens who choose to participate in politics at that time",
     "All citizens equally, whether they participate or not",
     "Only citizens who hold elective office",
     "Only citizens who belong to a political party",
     "Citizens of other countries as well as the United States"], ans=0,
   why="EK 4.8.A.1's own clause is 'citizens who choose to participate in politics at that time'. The framework's subject is a subset of the population, not the population, and the words WHO CHOOSE TO PARTICIPATE are what make it so."),

 dict(q="Why does EK 4.8.A.1 begin with the observation that the United States is a democracy with a DIVERSE SOCIETY?",
   choices=[
     "Because a diverse society contains many different attitudes, so which of them policy reflects depends on who takes part",
     "Because a diverse society has no shared political culture",
     "Because diversity guarantees that every view is represented in policy",
     "Because diversity prevents any policy from being adopted",
     "Because the framework treats diversity as a recent development"], ans=0,
   why="The sentence's two halves are connected: diversity means the attitudes present in the society differ, and participation determines which of them policy reflects. If everyone held the same views, the participation clause would not change the result."),

 dict(q="What would be lost from EK 4.8.A.1 if the phrase WHO CHOOSE TO PARTICIPATE were dropped?",
   choices=[
     "The claim would become one about all citizens rather than about the subset that takes part, which is a weaker and different statement",
     "Nothing, since the two versions say the same thing",
     "The reference to public policy would be lost",
     "The reference to diversity would be lost",
     "The claim would become stronger and more accurate"], ans=0,
   why="Without the clause, the sentence asserts that policy reflects citizens generally, which the framework does not claim. With it, the sentence is about a group defined by an action, and the difference between that group and the population is the whole subject."),

 dict(q="A policy is adopted that a majority of the adult population opposes, but that a majority of those who voted and contacted officials supported. How does EK 4.8.A.1 describe this?",
   choices=[
     "As policy reflecting the attitudes of citizens who chose to participate, which is what the framework says policy reflects",
     "As a violation of the framework's account of policymaking",
     "As evidence that public opinion has no effect on policy",
     "As an outcome the framework says cannot occur",
     "As proof that the adult population was not surveyed correctly"], ans=0,
   why="EK 4.8.A.1's clause makes participants rather than the population the reference group, so the scenario is the framework's claim operating rather than a counterexample to it. The gap between the two groups is exactly what the clause was written to allow for."),

 dict(q="EK 4.8.A.1 says policies generated AT ANY GIVEN TIME reflect the attitudes of participants AT THAT TIME. What does that repetition indicate?",
   choices=[
     "That the group whose attitudes policy reflects can change from one period to another",
     "That policy never changes once adopted",
     "That participation is fixed across generations",
     "That the framework concerns only a single historical moment",
     "That policies are reviewed on a fixed schedule"], ans=0,
   why="The framework times both the policy and the participants to the same moment, so a change in who participates can change what policy reflects. LO 4.8.A's phrase OVER TIME depends on that being possible."),

 dict(q="How does EK 4.8.A.1 connect this topic to the study of voter turnout?",
   choices=[
     "By making the composition of the participating group the thing that determines whose attitudes policy reflects",
     "By stating that turnout is always high enough to be representative",
     "By stating that turnout has no bearing on policy",
     "By stating that only turnout, and not other forms of participation, matters",
     "By stating that turnout is set by law"], ans=0,
   why="If policy reflects those who choose to participate, then who participates is a question about policy and not only about elections. The framework says CHOOSE TO PARTICIPATE rather than naming voting alone, so contacting officials and other participation count too."),

 dict(q="Which of the following is the most accurate restatement of EK 4.8.A.1?",
   choices=[
     "In a diverse democracy, the policies adopted at a given moment reflect the views of the people who took part in politics at that moment",
     "In a diverse democracy, policies reflect the views of every citizen equally",
     "In a diverse democracy, policies reflect the views of elected officials alone",
     "In a diverse democracy, policies reflect no one's views in particular",
     "In a diverse democracy, policies are determined by the courts"], ans=0,
   why="The restatement keeps the diversity premise, the timing, and the participation clause, which are the three working parts of the framework's sentence. Every other option removes at least one and changes what is claimed."),

 dict(q="According to the course framework, what has been reflected in policy debates and their outcomes over time?",
   choices=[
     "The balancing dynamic of individual liberty and government efforts to promote stability and order",
     "The steady expansion of individual liberty at the expense of order",
     "The steady expansion of order at the expense of individual liberty",
     "The absence of any conflict between liberty and order",
     "The replacement of both concerns by economic questions"], ans=0,
   why="EK 4.8.A.2 states this in exactly these words. Its noun is a BALANCING DYNAMIC, which is an ongoing relationship between two considerations rather than a trend in either direction."),

 dict(q="What does the framework's word DYNAMIC indicate about the relationship between individual liberty and government efforts to promote stability and order?",
   choices=[
     "That the relationship is ongoing and unsettled rather than resolved in favor of either",
     "That the relationship was settled at the founding",
     "That liberty has permanently prevailed",
     "That order has permanently prevailed",
     "That the two are the same consideration"], ans=0,
   why="A dynamic is a continuing interaction, and EK 4.8.A.2 attaches it to debates and outcomes OVER TIME. The framework names no winner, which is what makes it a description of a recurring tension rather than of a resolution."),

 dict(q="EK 4.8.A.2 says the balancing dynamic is reflected in policy debates AND THEIR OUTCOMES. Why does adding outcomes matter?",
   choices=[
     "Because it locates the tension in what governments actually did, not only in what was argued about",
     "Because it means every debate is resolved in the same way",
     "Because it means debates have no effect on outcomes",
     "Because it means outcomes are decided before debates begin",
     "Because it means only outcomes are worth studying"], ans=0,
   why="A tension visible only in argument might be rhetorical. EK 4.8.A.2 says it appears in outcomes as well, which makes it a feature of the policies adopted rather than only of the discussion around them."),

 dict(q="A legislature debates a requirement that would reduce a risk to the public while limiting what individuals may do. Which framework statement does the structure of this debate illustrate?",
   choices=[
     "EK 4.8.A.2's balancing dynamic of individual liberty and government efforts to promote stability and order",
     "EK 4.8.A.1's statement about citizens who choose to participate",
     "EK 4.5.A.2's account of polling methodology",
     "EK 4.3.A.1's account of generational effects",
     "EK 4.2.A.2's account of globalization"], ans=0,
   why="The debate sets a restriction on individual action against a government effort to reduce risk, which is EK 4.8.A.2's two considerations in their usual arrangement. The other statements concern who participates, how polls are conducted, and how attitudes develop."),

 dict(q="How does EK 4.8.A.2's balancing dynamic relate to the topics on civil liberties in Unit 3?",
   choices=[
     "Both describe a tension between individual freedom and government interests in order and safety, one in policy debates and the other in constitutional doctrine",
     "The two describe unrelated tensions",
     "Unit 3 concerns only economic questions",
     "EK 4.8.A.2 concerns only the courts",
     "Neither concerns individual liberty"], ans=0,
   why="EK 3.8.A.1 records that some government interests may justify restricting individual rights, with public safety as its example, and EK 4.8.A.2 names the same pair as a dynamic in policy debates. The framework describes one tension appearing in two settings."),

 dict(q="LO 4.8.A asks how political culture influences the FORMATION, GOALS, AND IMPLEMENTATION of public policy. What does naming all three stages indicate?",
   choices=[
     "That culture bears on how a policy is made, what it is meant to achieve, and how it is carried out, rather than on any one of these alone",
     "That the three stages occur simultaneously",
     "That only the formation stage is influenced by culture",
     "That implementation is unrelated to policy goals",
     "That the three stages are alternative names for one step"], ans=0,
   why="The objective lists three distinct stages, and a policy can be shaped by prevailing values at any of them. Confining the influence to formation would leave two of the objective's own three terms unaccounted for."),

 dict(q="LO 4.8.A defines U.S. political culture by example as democratic ideals, principles, and core values. Which statement elsewhere in the framework supplies those core values?",
   choices=[
     "EK 4.1.A.1's list of individualism, equality of opportunity, free enterprise, and the rule of law",
     "EK 4.5.A.1's list of types of scientific poll",
     "EK 3.11.A.1's list of government responses to social movements",
     "EK 4.3.A.1's account of generational and life cycle effects",
     "EK 4.6.A.1's two factors affecting polling"], ans=0,
   why="EK 4.1.A.1 names four core values with a gloss for each, and EK 4.2.A.2 says U.S. political culture is defined by its democratic ideals, principles and core values. LO 4.8.A's parenthetical points back to that content."),

 dict(q="A hypothetical political cartoon shows a set of scales. On one pan sits a figure labeled INDIVIDUAL LIBERTY; on the other, a larger figure labeled PUBLIC SAFETY. The beam tilts toward the safety pan, and a hand is shown adding a small weight to the liberty pan. Which framework statement do the visual elements most directly illustrate?",
   choices=[
     "EK 4.8.A.2's balancing dynamic, since scales show two considerations weighed against each other and a beam that can still move",
     "EK 4.8.A.1's statement about citizens who choose to participate",
     "EK 4.1.A.1's definition of the rule of law",
     "EK 4.5.A.2's account of neutral framing",
     "EK 4.2.A.1's list of contributors to political socialization"], ans=0,
   why="The scales are the visual form of a balance between two things, and the hand adding weight shows the balance as adjustable rather than fixed. That is EK 4.8.A.2's word DYNAMIC rendered as an image, which is what skill 4.D asks a student to read."),

 dict(q="A hypothetical political cartoon shows a voting booth with a long line of older figures waiting outside it, while a much shorter line of younger figures stands beside a doorway labeled SITTING THIS ONE OUT. A legislator in the background reads a document titled WHAT THE VOTERS WANT. Which framework statement do the visual elements most directly illustrate?",
   choices=[
     "EK 4.8.A.1's statement that policy reflects the attitudes of citizens who choose to participate",
     "EK 4.8.A.2's balancing dynamic of liberty and order",
     "EK 4.7.A.1's statement about party platforms",
     "EK 4.6.A.1's factors affecting polling",
     "EK 4.4.A.1's chain from events to ideology"], ans=0,
   why="The cartoon's two lines make the participating group different from the population, and the legislator reading what THE VOTERS want completes the connection to policy. That is EK 4.8.A.1's clause WHO CHOOSE TO PARTICIPATE presented visually."),

 dict(q="A hypothetical political cartoon shows a long banquet table labeled PUBLIC POLICY, set with many chairs. Most chairs are empty; the few that are occupied are drawn close to the head of the table. What does the arrangement of the visual elements suggest?",
   choices=[
     "That the outcome is being determined by those present, while the empty chairs represent people whose views are not being registered",
     "That the table is too large for the number of people invited",
     "That everyone present agrees with everyone else",
     "That the meal has not yet been served",
     "That the people present were chosen by the government"], ans=0,
   why="Skill 4.D asks what visual elements illustrate, and the contrast between empty and occupied chairs at a table labeled for policy is a picture of decisions made by those who show up. Nothing in the described image indicates who was invited or whether those present agree."),

 dict(q="A hypothetical infographic shows two bars for each of five decades. The first bar in each pair is labeled RESTRICTIONS ADOPTED FOR PUBLIC ORDER and the second PROTECTIONS ADDED FOR INDIVIDUAL LIBERTY. Neither bar is consistently taller across the five decades. What does this best illustrate?",
   choices=[
     "EK 4.8.A.2's claim that the balancing dynamic has been reflected in policy outcomes over time, with neither consideration prevailing throughout",
     "That individual liberty has steadily expanded across the five decades",
     "That public order has steadily expanded across the five decades",
     "That the two considerations never appear in the same decade",
     "That policy outcomes are unrelated to either consideration"], ans=0,
   why="EK 4.8.A.2 places the dynamic in outcomes over time, and an alternating pattern across decades is that claim in visual form. A bar consistently taller would show a trend, which is what the framework's word DYNAMIC declines to assert."),

 dict(q="A student is asked to analyze a political cartoon for this topic and writes only a description of what it depicts. What does skill 4.D require beyond that?",
   choices=[
     "An explanation of how the visual elements illustrate or relate to a political principle, process, or policy",
     "A judgment of whether the cartoon is well drawn",
     "An identification of the artist and the publication",
     "A count of the figures appearing in the image",
     "A prediction of how the policy debate will end"], ans=0,
   why="Skill 4.D asks how the visual elements ILLUSTRATE OR RELATE TO political principles, institutions, processes, policies and behaviors, which is a step past describing the image. Identifying the artist is not part of what the skill asks for."),

 dict(q="Read the following excerpt.\n\n“The latent causes of faction are thus sown in the nature of man; and we see them everywhere brought into different degrees of activity, according to the different circumstances of civil society.”\n—James Madison, Federalist No. 10, 1787\n\nHow does this passage relate to EK 4.8.A.1's premise about a diverse society?",
   choices=[
     "Both treat difference among citizens as a permanent condition that a political system has to operate within rather than remove",
     "Both argue that differences among citizens can be eliminated by good government",
     "Both argue that a diverse society cannot adopt any policy",
     "The passage concerns economics and the framework statement concerns culture",
     "Neither passage concerns differences among citizens"], ans=0,
   why="Madison locates the causes of faction in human nature and in the circumstances of civil society, and EK 4.8.A.1 begins from the United States being a democracy with a diverse society. Both take difference as the starting condition rather than as a problem to be solved."),

 dict(q="Read the following excerpt.\n\n“It is not from the benevolence of the butcher, the brewer, or the baker, that we expect our dinner, but from their regard to their own interest.”\n—Adam Smith, The Wealth of Nations, 1776\n\nHow does this passage bear on the formation of public policy as this topic describes it?",
   choices=[
     "It supplies the reasoning behind the free enterprise value the framework lists, which is one of the cultural commitments policy debates draw on",
     "It states that public policy should be made by merchants",
     "It states that self-interest plays no part in politics",
     "It states that government should own the means of production",
     "It has no connection to the course framework"], ans=0,
   why="EK 4.1.A.1.iii names free enterprise as a core value and attributes it to Adam Smith in this work, and the CED attaches the text to 4.8.A. LO 4.8.A asks how core values influence the formation of policy, and this is the source of one of them."),

 dict(q="A commentator claims that public policy in a democracy necessarily reflects the will of the majority of citizens. Which part of the course framework most directly qualifies the claim?",
   choices=[
     "EK 4.8.A.1's clause that policy reflects the attitudes of citizens who choose to participate",
     "EK 4.8.A.2's balancing dynamic",
     "EK 4.7.A.1's statement about party platforms",
     "EK 4.1.A.1's definition of individualism",
     "EK 4.2.A.2's account of globalization"], ans=0,
   why="The commentator's claim is about all citizens and the framework's sentence is about participants, so the qualification is exactly the clause the framework adds. A majority of the population and a majority of those who take part need not agree."),

 dict(q="Which of the following does EK 4.8.A.2 NOT state?",
   choices=[
     "Which of the two considerations should prevail in a policy debate",
     "That a balancing dynamic exists between individual liberty and government efforts to promote stability and order",
     "That the dynamic has been reflected in policy debates",
     "That the dynamic has been reflected in policy outcomes",
     "That the dynamic has operated over time"], ans=0,
   why="EK 4.8.A.2 describes a dynamic and names no winner. Every other option restates part of its single sentence, and the framework's silence on which side should prevail is what keeps the statement descriptive."),

 dict(q="Which question would a political scientist studying LO 4.8.A be most likely to ask?",
   choices=[
     "How did prevailing values shape what this policy was meant to achieve and how it was carried out?",
     "How many words long is the statute?",
     "Which committee reported the bill to the floor?",
     "How many amendments were offered during debate?",
     "On which date was the statute signed?"], ans=0,
   why="LO 4.8.A names the formation, goals and implementation of public policy as what political culture influences, so a matching research question asks about goals and implementation. The other four are procedural facts that bear on none of the objective's three stages."),

 dict(q=_WHO + " Which conclusion is best supported by the data?",
   table=_WHO_TABLE,
   choices=[
     "The oldest group makes up a larger share of participants than of adults, and the youngest group a smaller share, with the gap wider among those who contacted a legislator than among voters",
     "The three columns are identical",
     "The youngest group is over-represented among participants",
     "The oldest group makes up a smaller share of voters than of adults",
     "Every age group makes up the same share of each column"], ans=0,
   why="The oldest group runs 22, 31 and 37 percent across the three columns while the youngest runs 21, 13 and 8. The oldest group's excess over its population share grows from 9 points among voters to 15 among those contacting a legislator."),

 dict(q=_WHO + " Which statement in the course framework does this pattern most directly illustrate?",
   table=_WHO_TABLE,
   choices=[
     "That public policies reflect the attitudes and beliefs of citizens who choose to participate in politics at that time",
     "That the balancing dynamic of liberty and order is reflected in policy outcomes",
     "That party platforms align with ideological positions",
     "That political socialization develops beliefs, values, opinions, and behaviors",
     "That generational effects are experiences shared by people of a common age"], ans=0,
   why="EK 4.8.A.1's clause makes participants rather than the population the group whose attitudes policy reflects, and this table shows those two groups differing in composition. That difference is what the clause exists to record."),

 dict(q=_WHO + " A student uses the second and third columns to describe what all adults in the state want. What is the most important correction?",
   table=_WHO_TABLE,
   choices=[
     "Those columns describe voters and people who contacted a legislator, and their age composition differs from that of all adults, which the first column reports",
     "The table does not report the composition of all adults",
     "The three columns report identical compositions",
     "The table reports counts rather than shares",
     "The table covers a single adult, so no share can be computed"], ans=0,
   why="The first column is the population and the other two are participants, and they differ by up to 15 percentage points in a single row. EK 4.8.A.1's clause is precisely about that difference, so treating a participant column as the population is the error the framework's wording anticipates."),

 dict(q=_BALANCE + " Which conclusion is best supported by the data?",
   table=_BALANCE_TABLE,
   choices=[
     "Neither side leads across all four questions: each side leads two, and one of the four is close to even",
     "The liberty side leads all four questions",
     "The order side leads all four questions",
     "The two sides are tied on every question",
     "A majority favored the liberty side on every question"], ans=0,
   why="The liberty side leads Questions 1 and 3 and the order side leads Questions 2 and 4, so neither leads throughout. Question 3 is 47 to 44, a gap of 3 points, and the liberty side reaches an outright majority only on Question 1."),

 dict(q=_BALANCE + " Which statement in the course framework does this pattern most directly illustrate?",
   table=_BALANCE_TABLE,
   choices=[
     "That a balancing dynamic of individual liberty and government efforts to promote stability and order is reflected in policy debates",
     "That policies reflect citizens who choose to participate",
     "That party platforms generally align with ideological positions",
     "That major political events influence individual attitudes",
     "That accurate sampling includes calculating a margin of error"], ans=0,
   why="EK 4.8.A.2 names exactly these two considerations and calls their relationship a balancing dynamic, and a table in which neither side leads throughout is that dynamic in observable form. A consistent winner would show a trend instead."),

 dict(q=_BALANCE + " A student concludes from this table that the public consistently prefers order to liberty. What is the most important correction?",
   table=_BALANCE_TABLE,
   choices=[
     "On Question 1 the liberty side drew 58 percent against 31, so the preference is not consistent across the four questions",
     "The order side led on every question in the table",
     "The table reports no figures for the liberty side",
     "The liberty side led on every question in the table",
     "The table covers a single question, so no pattern can be described"], ans=0,
   why="The order side leads two of the four questions and trails clearly on one, so the pattern varies by question rather than holding across them. EK 4.8.A.2's word DYNAMIC is what accommodates that variation, and a consistent preference is what it declines to assert."),
]
