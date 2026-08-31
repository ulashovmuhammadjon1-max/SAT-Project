# AP U.S. GOVERNMENT AND POLITICS 4.4 Influence of Political Events on Ideology
# -- 30 questions
# CED V.1 (c) 2026, Unit 4 American Political Ideologies and Beliefs.
# Learning objective 4.4.A: explain how MAJOR POLITICAL EVENTS influence
# political ideology.
# Suggested skill for this topic (CED p. 105): 4.B, source analysis -- explain
# how the ARGUMENT OR PERSPECTIVE IN THE SOURCE relates to political principles,
# institutions, processes, policies, and behaviors.
#
# Essential knowledge relied on. Two sentences, and between them they state a
# CHAIN WITH THREE LINKS AND A NAMED MIDDLE:
#   EK 4.4.A.1 -- "Major political events CAN INFLUENCE the development of
#     INDIVIDUAL POLITICAL ATTITUDES, WHICH IS AN EXAMPLE OF POLITICAL
#     SOCIALIZATION. Political socialization, IN TURN, influences POLITICAL
#     IDEOLOGY."
#
#     events  ->  individual political attitudes  ->  political ideology
#                 (= political socialization)
#
# THE ORDER IS THE CONTENT, AND THE MIDDLE LINK IS WHAT A SUMMARY DELETES.
# "Major events shape ideology" is the sentence everyone writes, and it skips
# the step the framework troubled to name. Two things follow from keeping it:
#   * The route runs through the individual. An event does not act on an
#     ideology; it acts on a person's attitudes, and the process by which those
#     attitudes develop is the one EK 4.2.A.1 defines.
#   * Ideology is DOWNSTREAM and therefore slower. An event that moves an
#     attitude sharply has not thereby moved an ideology, which is exactly what
#     the second table in this module shows and what item 30 exists to correct.
# Items 1 to 8 build the chain; the verifier refuses any key that reverses it or
# routes an event to ideology directly.
#
# "CAN INFLUENCE" IS A POSSIBILITY CLAIM. The framework's modal verb is CAN, and
# its noun is INFLUENCE rather than determination. So no event is said to
# produce any particular attitude, and no key here says one does. Items 9 and 10
# make the modal itself the question.
#
# WHY THIS MODULE DESCRIBES ITS SOURCES INSTEAD OF QUOTING THEM. The suggested
# skill is 4.B, source analysis -- but the CED attaches NO foundational document
# and NO required case to 4.4.A. Every other source-analysis topic in this bank
# quotes the document the framework itself supplies; here there is none to quote.
# SOCIAL_BRIEF.md's rule is to quote accurately or to DESCRIBE INSTEAD, and never
# to invent a quotation, so items 13 to 18 state each argument in the third
# person and attribute it to no one. Inventing a plausible quotation and hanging
# a name on it would be the one failure in this bank that no checker downstream
# could ever detect, because a fabricated source reads exactly like a real one.
# The verifier enforces the choice: no quotation marks around an attributed
# passage anywhere in the module.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("4.4", "Influence of Political Events on Ideology", 4)

_FORMATIVE = ("A hypothetical survey asked respondents, years afterward, how important one major "
              "political event had been to their own political outlook. The table groups "
              "respondents by how old they were when the event occurred.")
_FORMATIVE_TABLE = dict(
    headers=["Age when the event occurred", "Called it important to their outlook (%)",
             "Called it unimportant to their outlook (%)"],
    rows=[["Under 10", "18", "82"],
          ["Ages 10 to 17", "47", "53"],
          ["Ages 18 to 25", "61", "39"],
          ["Ages 26 to 40", "44", "56"],
          ["Over 40", "29", "71"]])

_BEFORE_AFTER = ("A hypothetical survey interviewed the same respondents shortly before and "
                 "shortly after one major political event. The table reports the share holding "
                 "each view on each occasion.")
_BEFORE_AFTER_TABLE = dict(
    headers=["View measured", "Before the event (%)", "After the event (%)"],
    rows=[["Trust that the national government will act effectively", "41", "63"],
          ["Support for increased spending in the affected policy area", "37", "58"],
          ["Belief that the issue is among the most important facing the country", "12", "49"],
          ["General view of how much government should do across all areas", "44", "46"]])

QUESTIONS = [
 dict(q="According to the course framework, what can major political events influence?",
   choices=[
     "The development of individual political attitudes",
     "The text of the Constitution",
     "The jurisdiction of the federal courts",
     "The number of seats in the House of Representatives",
     "The length of a senator's term"], ans=0,
   why="EK 4.4.A.1 says major political events can influence the development of individual political attitudes. The framework's object is a person's attitudes, not an institution or a rule."),

 dict(q="EK 4.4.A.1 says that the influence of major political events on individual political attitudes is an example of what?",
   choices=[
     "Political socialization",
     "Judicial review",
     "Federalism",
     "Checks and balances",
     "Selective incorporation"], ans=0,
   why="EK 4.4.A.1's own clause is 'which is an example of political socialization', which places events among the influences EK 4.2.A.1 describes rather than in a separate category."),

 dict(q="According to EK 4.4.A.1, what does political socialization in turn influence?",
   choices=[
     "Political ideology",
     "The outcome of a Supreme Court case",
     "The wording of a statute",
     "The size of the federal bureaucracy",
     "The date of a national election"], ans=0,
   why="EK 4.4.A.1's second sentence says political socialization in turn influences political ideology. The phrase IN TURN is what makes the statement a chain rather than two unrelated claims."),

 dict(q="Which sequence correctly states the chain EK 4.4.A.1 describes?",
   choices=[
     "Major political events influence individual attitudes, and that process of socialization in turn influences political ideology",
     "Political ideology influences political socialization, which in turn produces major political events",
     "Political socialization influences major political events, which in turn shape attitudes",
     "Political ideology influences major political events, which in turn shape socialization",
     "Major political events influence political ideology, which in turn produces attitudes"], ans=0,
   why="EK 4.4.A.1 runs from events to attitudes to ideology, and names the middle step political socialization. Each of the other options reverses at least one link of the framework's own order."),

 dict(q="Why does it matter that EK 4.4.A.1 places individual attitudes BETWEEN events and ideology rather than connecting events to ideology directly?",
   choices=[
     "Because it makes the route run through a person, so an event acts on attitudes and reaches ideology only through the process by which those attitudes develop",
     "Because it means events have no effect on ideology at all",
     "Because it means ideology changes faster than attitudes do",
     "Because it means only government officials are affected by events",
     "Because it means attitudes and ideology are the same thing"], ans=0,
   why="The framework's middle term is the development of individual political attitudes, named as political socialization, and EK 4.2.A.1 describes that as a process running over time. An event that reaches ideology does so by way of a person, which is what the intermediate step records."),

 dict(q="A student writes that major political events shape political ideology. What does the framework's own sentence add that this summary leaves out?",
   choices=[
     "The intermediate step, in which events influence individual attitudes through political socialization",
     "That events have no influence of any kind",
     "That ideology is fixed before any event occurs",
     "That only elections count as major political events",
     "That the influence runs from ideology to events"], ans=0,
   why="The summary is not false; it skips the link EK 4.4.A.1 names. The framework routes the influence through the development of individual attitudes and identifies that development as political socialization."),

 dict(q="How does EK 4.4.A.1 connect this topic to EK 4.2.A.1?",
   choices=[
     "By identifying the influence of events on attitudes as an example of the political socialization EK 4.2.A.1 defines",
     "By replacing political socialization with a different process",
     "By stating that events are a sixth contributor that EK 4.2.A.1 omitted",
     "By stating that political socialization concerns only children",
     "By stating that the two topics are unrelated"], ans=0,
   why="EK 4.4.A.1's clause 'which is an example of political socialization' makes events an instance of the process EK 4.2.A.1 defines rather than a competing explanation or a missing item on its list of contributors."),

 dict(q="Which of the following is the best restatement of both sentences of EK 4.4.A.1 together?",
   choices=[
     "Events can move a person's attitudes, that movement is a case of political socialization, and socialization in turn bears on ideology",
     "Events determine a person's ideology immediately and completely",
     "Ideology determines which events a person notices",
     "Socialization and ideology are two names for the same thing",
     "Events affect institutions rather than people"], ans=0,
   why="The restatement keeps all three links and the framework's modal verb CAN. EK 4.4.A.1 says events CAN INFLUENCE attitudes and that socialization IN TURN influences ideology, which is a chain of influences rather than a determination."),

 dict(q="EK 4.4.A.1 says major political events CAN influence the development of individual political attitudes. What does that modal verb indicate?",
   choices=[
     "That such influence is possible rather than guaranteed in every case",
     "That such influence occurs in every case without exception",
     "That such influence has never actually been observed",
     "That such influence occurs only during wartime",
     "That such influence is prohibited by law"], ans=0,
   why="The framework writes CAN INFLUENCE rather than DOES DETERMINE, so it claims possibility and not necessity. A key asserting that every major event changes every person's attitudes would state more than the sentence does."),

 dict(q="Two people live through the same major political event and reach opposite conclusions about what government should do. Does this contradict EK 4.4.A.1?",
   choices=[
     "No, because the framework says events can influence the development of attitudes without saying which attitudes result",
     "Yes, because the framework says an event produces the same attitude in everyone",
     "Yes, because the framework says attitudes cannot differ within a generation",
     "No, because the framework says events have no influence at all",
     "No, because the framework says only one of the two people experienced the event"], ans=0,
   why="EK 4.4.A.1 names no attitude and no direction of change. Its claim is that events can influence the development of attitudes, which is compatible with the same event contributing to different conclusions in different people."),

 dict(q="How does the account in EK 4.4.A.1 relate to the generational effects EK 4.3.A.1 describes?",
   choices=[
     "A major political event is the kind of experience that can be shared by people of a common age, which is EK 4.3.A.1's definition of a generational effect",
     "The two statements describe unrelated processes",
     "EK 4.4.A.1 says events produce life cycle effects rather than generational ones",
     "EK 4.3.A.1 says generational effects cause major political events",
     "Neither statement concerns political ideology"], ans=0,
   why="EK 4.3.A.1 defines a generational effect as an experience shared by people of a common age, and a major political event lived through at the same point in life is such an experience. EK 4.4.A.1 supplies the mechanism by which it reaches ideology."),

 dict(q="Which of the following is the clearest example of the process EK 4.4.A.1 describes?",
   choices=[
     "A person who lived through a national crisis forms lasting views about what government should be prepared to do, and those views shape a broader outlook over time",
     "A statute is enacted and later amended by Congress",
     "A court decides a case and issues a written opinion",
     "A federal agency publishes a new regulation",
     "A state redraws its legislative district lines"], ans=0,
   why="The example runs the framework's whole chain: an event, a change in an individual's attitudes, and a broader outlook shaped over time. The other four describe government actions without reference to any individual's attitudes."),

 dict(q="A commentator argues that dramatic national events matter less to a person's politics than the daily influence of family and workplace, because the daily influences operate continuously while an event is over quickly. How does this argument relate to the course framework?",
   choices=[
     "It disputes the relative weight of contributors the framework lists without ranking them, since EK 4.2.A.1 names several and EK 4.4.A.1 adds events without saying which matters most",
     "It contradicts the framework, which states that events are the strongest influence",
     "It contradicts the framework, which states that family has no influence",
     "It restates the framework's own ranking of the contributors",
     "It is unrelated to the framework, which does not discuss family"], ans=0,
   why="EK 4.2.A.1 names family, schools, peers, media and social environments; EK 4.4.A.1 adds major political events as an example of the same process. Neither statement ranks them, so an argument about relative weight goes beyond what the framework settles rather than contradicting it."),

 dict(q="A commentator argues that a major political event changes a country's politics only when people who were young at the time later reach positions of influence. Which political process does this argument depend on?",
   choices=[
     "Political socialization, since the argument turns on attitudes formed earlier persisting and later shaping decisions",
     "Judicial review, since the argument concerns constitutional interpretation",
     "Federalism, since the argument concerns the division of power",
     "Checks and balances, since the argument concerns officeholders",
     "Selective incorporation, since the argument concerns rights"], ans=0,
   why="EK 4.4.A.1 identifies the influence of events on attitudes as an example of political socialization and says socialization in turn influences ideology. An argument about a delay between the event and its political effect is an argument about that process operating over time."),

 dict(q="A commentator argues that surveys taken immediately after a dramatic event overstate its lasting effect, because people answer in the mood of the moment. What does this argument imply for how EK 4.4.A.1's chain should be tested?",
   choices=[
     "That evidence of an effect on ideology requires measurement well after the event, since ideology sits downstream of attitudes that may move temporarily",
     "That surveys can never measure political attitudes",
     "That events have no influence on attitudes at all",
     "That ideology changes faster than attitudes",
     "That only surveys taken before an event are meaningful"], ans=0,
   why="EK 4.4.A.1 places ideology at the end of a chain that runs through the development of attitudes, so a momentary movement in an attitude is not yet evidence about the far end of the chain. The argument is about the timing of measurement, not about whether attitudes can be measured."),

 dict(q="A commentator argues that because different people draw opposite lessons from the same event, events cannot be said to influence ideology at all. What is the strongest response from the course framework?",
   choices=[
     "EK 4.4.A.1 claims that events can influence the development of attitudes, not that they produce a uniform attitude, so divergent lessons are consistent with the claim",
     "The framework states that everyone draws the same lesson from an event",
     "The framework states that events influence institutions rather than people",
     "The framework states that ideology is unaffected by anything",
     "The framework states that only unanimous reactions count as influence"], ans=0,
   why="The commentator's inference requires the framework to have claimed uniformity, and it did not: its verb is CAN INFLUENCE and it names no resulting attitude. Divergent conclusions from a shared experience are influence with different results, not an absence of influence."),

 dict(q="A commentator argues that political leaders deliberately frame a major event in order to shape how people understand it. Which part of the framework does this argument connect to most directly?",
   choices=[
     "EK 4.2.A.1's naming of media among the contributors to political socialization, since framing reaches people through what they read and hear",
     "EK 4.3.A.1's definition of a life cycle effect",
     "EK 4.1.A.1's list of core values",
     "EK 4.5.A.1's list of types of scientific poll",
     "EK 4.7.A.1's description of party platforms"], ans=0,
   why="EK 4.4.A.1 makes the influence of events an example of political socialization, and EK 4.2.A.1 lists media among the contributors to that process. An argument about how an event is presented is an argument about that contributor."),

 dict(q="A commentator argues that an event only becomes a MAJOR political event in the framework's sense once large numbers of people treat it as one. What does this argument add to EK 4.4.A.1?",
   choices=[
     "A suggestion about what makes an event major, which the framework itself does not define",
     "A contradiction of the framework, which defines major events precisely",
     "A restatement of the framework's own definition of a major event",
     "A claim that events cannot influence attitudes",
     "A claim that political socialization does not exist"], ans=0,
   why="EK 4.4.A.1 uses the phrase MAJOR POLITICAL EVENTS without defining what makes an event major. An argument supplying a criterion is adding to the framework rather than agreeing or disagreeing with it, which is worth noticing before treating the criterion as course content."),

 dict(q="Which of the following does EK 4.4.A.1 NOT state?",
   choices=[
     "Which attitudes a major political event produces",
     "That major political events can influence the development of individual political attitudes",
     "That the influence of events on attitudes is an example of political socialization",
     "That political socialization in turn influences political ideology",
     "That the influence described runs through individuals"], ans=0,
   why="EK 4.4.A.1 names no attitude and no direction of change. Every other option restates part of its two sentences, and the last follows from its object being the development of INDIVIDUAL political attitudes."),

 dict(q="Why is it useful that EK 4.4.A.1 identifies the influence of events as an EXAMPLE of political socialization rather than as a separate process?",
   choices=[
     "Because it means everything the framework says about how socialization works applies to events as well",
     "Because it means events are less important than other influences",
     "Because it means events operate only on people who are already politically active",
     "Because it means the framework has two competing explanations of ideology",
     "Because it means socialization occurs only when an event happens"], ans=0,
   why="Calling something an example places it inside a category, so EK 4.2.A.1's account of a process running over time through several contributors governs events too. Two separate processes would need two separate accounts."),

 dict(q="A researcher wants to test whether a particular event influenced political ideology as EK 4.4.A.1 describes. Which design would bear most directly on the framework's claim?",
   choices=[
     "Measuring the same people's broader political outlook before the event and again well afterward",
     "Measuring different people's opinions on the day after the event only",
     "Counting how many news stories mentioned the event",
     "Asking political leaders what they think the event meant",
     "Comparing the length of the event with that of earlier events"], ans=0,
   why="EK 4.4.A.1's chain ends in political ideology, which is a broader outlook, and its middle term is a process of development. Testing the end of that chain requires the same people measured across enough time for development to occur."),

 dict(q="A student argues that EK 4.4.A.1 makes political ideology unstable, since events happen constantly. What is the most important qualification?",
   choices=[
     "The framework routes events to ideology through the development of attitudes, which is a process rather than an immediate transfer, so ideology need not track every event",
     "The framework says ideology never changes at all",
     "The framework says events occur only rarely",
     "The framework says ideology changes with every news story",
     "The framework says attitudes and ideology are unrelated"], ans=0,
   why="EK 4.4.A.1's middle term is the DEVELOPMENT of individual political attitudes, named as political socialization, and EK 4.2.A.1 describes that as something contributors build over time. A chain with a developmental step in it does not transmit every input immediately."),

 dict(q="Which question would a political scientist studying LO 4.4.A be most likely to ask?",
   choices=[
     "Did people who lived through a particular event later hold a broader political outlook different from those who did not?",
     "How many votes are needed to override a presidential veto?",
     "Which clause of the Constitution establishes judicial review?",
     "How long may a filibuster continue in the Senate?",
     "How many federal district courts are there?"], ans=0,
   why="LO 4.4.A is how major political events influence political ideology, and EK 4.4.A.1 routes that influence through individuals. A research question matching the objective compares the broader outlook of people who did and did not live through the event."),

 dict(q="Which statement best summarizes the limit of what EK 4.4.A.1 establishes?",
   choices=[
     "It establishes a route by which events can reach ideology, without naming any event, any attitude, or any resulting ideology",
     "It establishes which events have shaped American ideology",
     "It establishes that ideology is determined by the most recent major event",
     "It establishes that political socialization ends in adolescence",
     "It establishes a ranking of the influences on political ideology"], ans=0,
   why="EK 4.4.A.1's two sentences supply a mechanism and nothing else: events, attitudes, socialization, ideology, with a modal verb at the front. Names, magnitudes and rankings would all have to come from somewhere other than the framework."),

 dict(q=_FORMATIVE + " Which statement best describes the data?",
   table=_FORMATIVE_TABLE,
   choices=[
     "The share calling the event important is highest among those who were 18 to 25 when it occurred and lowest among those who were under 10",
     "The share calling the event important rises steadily with age at the time of the event",
     "The share calling the event important falls steadily with age at the time of the event",
     "Every age group reports the same share",
     "No age group calls the event important"], ans=0,
   why="The important column reads 18, 47, 61, 44 and 29, which rises to a peak in the 18 to 25 bracket and falls on either side. A steady rise or a steady fall would require the column to be ordered throughout, and it is not."),

 dict(q=_FORMATIVE + " Which statement in the course framework does this pattern most directly illustrate?",
   table=_FORMATIVE_TABLE,
   choices=[
     "That major political events can influence the development of individual political attitudes, which is an example of political socialization",
     "That political socialization is completed before the age of 10",
     "That life cycle effects are experiences encountered during different life stages",
     "That U.S. political culture is defined by its democratic ideals",
     "That liberal ideologies favor more governmental regulation of the marketplace"], ans=0,
   why="EK 4.4.A.1 makes exactly this claim, and respondents attributing part of their political outlook to an event is that claim in observable form. The framework does not say socialization is completed at any age, and the other options belong to other topics."),

 dict(q=_FORMATIVE + " A student concludes from the table that the event had no influence on those who were over 40 when it occurred. What is the most important correction?",
   table=_FORMATIVE_TABLE,
   choices=[
     "Twenty-nine percent of that group called the event important to their outlook, which is a smaller share than in other groups but is not none",
     "The table reports no figures for that group",
     "That group reports the highest share in the table",
     "Every group in the table reports the same share",
     "The table covers a single respondent, so no share can be computed"], ans=0,
   why="The over 40 row reads 29 percent important against 71 percent unimportant, so the group is the second lowest rather than empty. A smaller share is a weaker pattern, not an absent one, and EK 4.4.A.1's verb is CAN INFLUENCE rather than always influences."),

 dict(q=_BEFORE_AFTER + " Which statement best describes the data?",
   table=_BEFORE_AFTER_TABLE,
   choices=[
     "The three issue-specific views each moved by more than 20 percentage points, while the general view of how much government should do moved by 2",
     "All four views moved by similar amounts",
     "The general view moved more than any issue-specific view",
     "No view changed between the two interviews",
     "Every view moved downward after the event"], ans=0,
   why="Trust rose 22 points, support for spending 21, and belief in the issue's importance 37, while the general view rose from 44 to 46. Every movement in the table is upward, and they are not similar in size."),

 dict(q=_BEFORE_AFTER + " Which part of EK 4.4.A.1's chain does this pattern bear on most directly?",
   table=_BEFORE_AFTER_TABLE,
   choices=[
     "The first link, in which events influence the development of individual attitudes, with ideology reached later through political socialization rather than at once",
     "The claim that ideology influences events",
     "The claim that political socialization is unrelated to attitudes",
     "The claim that events act on institutions rather than on individuals",
     "The claim that events have no influence on anything"], ans=0,
   why="The sharply moving rows are attitudes about a particular issue, which is EK 4.4.A.1's first link. The barely moving row is the broader orientation that sits at the end of the chain, and the framework routes events there through the development of attitudes rather than directly."),

 dict(q=_BEFORE_AFTER + " A student concludes from the table that the event changed these respondents' political ideology. What is the most important correction?",
   table=_BEFORE_AFTER_TABLE,
   choices=[
     "The general view of how much government should do moved only 2 points, and the framework routes events to ideology through the development of attitudes rather than directly",
     "The table reports no change in any view",
     "The general view moved more than the issue-specific views",
     "The table reports views after the event only",
     "The table covers a single respondent, so no share can be computed"], ans=0,
   why="The measure closest to a broader outlook moved from 44 to 46 while the issue-specific measures moved by 21 points or more. EK 4.4.A.1 places political socialization between an event and ideology, so a short-run shift in attitudes is not yet a change at the far end of the chain."),
]
