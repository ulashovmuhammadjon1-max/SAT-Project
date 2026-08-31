# AP U.S. GOVERNMENT AND POLITICS 4.3 Changes in Ideology -- 30 questions
# CED V.1 (c) 2026, Unit 4 American Political Ideologies and Beliefs.
# Learning objective 4.3.A: explain how SOCIAL FACTORS impact political ideology.
# Suggested skill for this topic (CED p. 104): 3.B, data analysis -- DESCRIBE
# PATTERNS AND TRENDS IN DATA.
#
# Essential knowledge relied on. One sentence, two terms, and both parentheses
# are the framework's own:
#   EK 4.3.A.1 -- "GENERATIONAL EFFECTS (experiences shared by people of a
#     common age) and LIFE CYCLE EFFECTS (experiences a person encounters during
#     different life stages) contribute to the development of a person's
#     political ideology."
#
# THE TWO DEFINITIONS DIFFER BY ONE WORD, AND THE WORD IS "SHARED".
#   generational  experiences SHARED BY PEOPLE OF A COMMON AGE -- the experience
#                 belongs to a cohort, is had once, and the cohort carries it
#                 forward.
#   life cycle    experiences a person encounters DURING DIFFERENT LIFE STAGES
#                 -- the experience belongs to a stage, and every cohort meets
#                 it in turn as it reaches that stage.
# They are hard to tell apart in prose and easy to tell apart in DATA, which is
# exactly why the CED assigns this topic skill 3.B rather than a concept skill.
# So this module carries three tables and nine data items, and the two effects
# are separated by the shape of the numbers rather than asserted:
#   * a cohort's figures holding steady as the cohort ages is generational;
#   * an age bracket's figures holding steady while its occupants turn over is
#     life cycle.
# Items 22 to 27 are that contrast, built as a matched pair.
#
# THE METHODOLOGICAL POINT ITEM 30 EXISTS FOR. Repeated cross sections report
# AGE GROUPS in different years, not the same PEOPLE over time, so no such table
# can show what happened to any individual as they aged. Reading one as though
# it followed people is the single commonest error with this kind of data, and
# it is the error that makes a life cycle effect and a generational effect look
# interchangeable. The framework's two definitions cannot be applied at all
# without it.
#
# WHAT THE FRAMEWORK DOES NOT SAY, and no key here supplies: which of the two
# effects is stronger, which ideology either produces, and whether any actual
# generation holds any particular view. EK 4.3.A.1 says both CONTRIBUTE to the
# development of a person's political ideology and stops. Every table in this
# module is therefore about an unnamed "particular position", because naming one
# would smuggle in an empirical claim the CED does not make. Item 21 makes that
# limit the question.
#
# Required cases the CED attaches to 4.3.A (p. 31): Brown v. Board of Education.
# Item 17 uses it to apply EK 4.3.A.1's definition of a generational effect --
# an experience shared by people of a common age -- rather than to assert any
# claim about what a generation concluded.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: all three tables are labelled
# hypothetical and none names a real position, party or generation.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("4.3", "Changes in Ideology", 4)

_COHORTS = ("A hypothetical survey measured the share of each birth cohort holding a particular "
            "political position. The same three cohorts were surveyed again after ten years and "
            "again after twenty.")
_COHORTS_TABLE = dict(
    headers=["Birth cohort", "Survey year 1 (%)", "Survey year 11 (%)", "Survey year 21 (%)"],
    rows=[["Born in the 1940s", "58", "57", "59"],
          ["Born in the 1960s", "41", "42", "40"],
          ["Born in the 1980s", "27", "28", "27"]])

_STAGES = ("A hypothetical survey measured the share of respondents in each age group holding a "
           "particular political position, in three survey years spaced ten years apart. "
           "Different individuals were interviewed each time.")
_STAGES_TABLE = dict(
    headers=["Age group", "Survey year 1 (%)", "Survey year 11 (%)", "Survey year 21 (%)"],
    rows=[["Ages 18 to 29", "22", "23", "21"],
          ["Ages 30 to 49", "38", "37", "39"],
          ["Ages 50 to 69", "54", "55", "53"],
          ["Age 70 and older", "61", "62", "60"]])

_TURNOUT = ("A hypothetical study reports turnout by age group in three successive elections. "
            "Different individuals were surveyed after each election.")
_TURNOUT_TABLE = dict(
    headers=["Age group", "First election (%)", "Second election (%)", "Third election (%)"],
    rows=[["Ages 18 to 24", "37", "41", "36"],
          ["Ages 25 to 44", "52", "56", "51"],
          ["Ages 45 to 64", "67", "70", "66"],
          ["Age 65 and older", "71", "74", "70"]])

QUESTIONS = [
 dict(q="According to the course framework, what are GENERATIONAL EFFECTS?",
   choices=[
     "Experiences shared by people of a common age",
     "Experiences a person encounters during different life stages",
     "Experiences that occur only during an election campaign",
     "Experiences shared by people living in the same state",
     "Experiences reported by a person to a survey interviewer"], ans=0,
   why="EK 4.3.A.1's parenthesis defines generational effects as experiences shared by people of a common age. The second option is the framework's definition of the other term in the same sentence."),

 dict(q="According to the course framework, what are LIFE CYCLE EFFECTS?",
   choices=[
     "Experiences a person encounters during different life stages",
     "Experiences shared by people of a common age",
     "Experiences confined to a single generation",
     "Experiences that occur only once in a country's history",
     "Experiences reported identically by every age group"], ans=0,
   why="EK 4.3.A.1's parenthesis defines life cycle effects as experiences a person encounters during different life stages. The experience belongs to the stage, so each cohort meets it in turn on reaching that stage."),

 dict(q="What do generational effects and life cycle effects both do, according to EK 4.3.A.1?",
   choices=[
     "Contribute to the development of a person's political ideology",
     "Determine a person's political party registration",
     "Establish the outcome of a national election",
     "Replace political socialization as an explanation",
     "Guarantee that a person's views will not change"], ans=0,
   why="EK 4.3.A.1's verb for both is CONTRIBUTE TO THE DEVELOPMENT of a person's political ideology. The framework claims contribution rather than determination, which is why neither effect fixes any particular outcome."),

 dict(q="What is the key difference between the two effects EK 4.3.A.1 names?",
   choices=[
     "A generational effect attaches to a cohort of people born around the same time, while a life cycle effect attaches to a stage of life that every cohort reaches in turn",
     "A generational effect attaches to a stage of life and a life cycle effect to a cohort",
     "A generational effect concerns economics and a life cycle effect concerns social issues",
     "A generational effect applies only to voters and a life cycle effect only to nonvoters",
     "The two terms describe the same thing"], ans=0,
   why="EK 4.3.A.1's two parentheses differ in what the experience belongs to: people of a common age in the first, different life stages in the second. Everything else about the distinction follows from that."),

 dict(q="An experience that people who were young at the same moment lived through together, and that continues to mark their outlook decades later, is which kind of effect?",
   choices=[
     "A generational effect, because the experience is shared by people of a common age",
     "A life cycle effect, because the people were young when it happened",
     "A life cycle effect, because decades passed afterward",
     "Neither, because the framework covers only current experiences",
     "Both equally, because the framework does not distinguish them"], ans=0,
   why="EK 4.3.A.1's first parenthesis is experiences shared by people of a common age, and an experience carried forward by the group that lived it is the definition applied. That the group was young is incidental; what matters is that the experience belongs to them rather than to the stage."),

 dict(q="A pattern in which people tend to take more interest in property taxes once they own homes, whatever decade they were born in, is which kind of effect?",
   choices=[
     "A life cycle effect, because the experience is encountered at a particular life stage rather than by one cohort",
     "A generational effect, because homeowners are a group",
     "A generational effect, because property taxes change over time",
     "Neither, because the framework concerns only national issues",
     "Both, because everyone eventually owns property"], ans=0,
   why="EK 4.3.A.1's second parenthesis is experiences a person encounters during different life stages. The phrase WHATEVER DECADE THEY WERE BORN IN is what rules out the cohort explanation, because a generational effect would be confined to one birth group."),

 dict(q="Why does EK 4.3.A.1 place both effects in a single sentence rather than treating one as the correct explanation?",
   choices=[
     "Because the framework says both contribute, without ranking them",
     "Because the framework says generational effects always outweigh life cycle effects",
     "Because the framework says life cycle effects always outweigh generational effects",
     "Because the framework says only one of the two actually exists",
     "Because the framework says neither has any effect on ideology"], ans=0,
   why="EK 4.3.A.1 names both as contributors to the development of a person's political ideology and supplies no weighting between them. A key asserting that one dominates would state a conclusion the framework declines to reach."),

 dict(q="LO 4.3.A asks how SOCIAL FACTORS impact political ideology. How do the two effects EK 4.3.A.1 names count as social factors?",
   choices=[
     "Each locates the influence in experiences a person has in common with others, whether by age or by life stage",
     "Each locates the influence in a person's genetic inheritance",
     "Each locates the influence in the text of the Constitution",
     "Each locates the influence in a decision by a government agency",
     "Neither is a social factor, since both concern individuals"], ans=0,
   why="Both of EK 4.3.A.1's parentheses describe experiences held in common: shared by people of a common age, or encountered by anyone reaching a given stage. That commonality is what makes them social rather than idiosyncratic."),

 dict(q="Which finding would be the strongest evidence of a GENERATIONAL effect rather than a life cycle effect?",
   choices=[
     "A cohort's distinctive views persist as that cohort grows older, so the distinctiveness moves up the age ladder over time",
     "Every age group holds the same views in every survey year",
     "Views shift for everyone at once in a single year",
     "Views differ between two states surveyed in the same year",
     "Views differ between people of the same age in the same year"], ans=0,
   why="EK 4.3.A.1 ties a generational effect to people of a common age, so its signature is that the difference travels with the cohort rather than staying attached to an age bracket. A cohort keeping its views as it ages is exactly that."),

 dict(q="Which finding would be the strongest evidence of a LIFE CYCLE effect rather than a generational effect?",
   choices=[
     "The same age brackets show the same views in survey after survey, even though the people occupying them have changed",
     "One birth cohort holds distinctive views throughout its life",
     "Views are identical across all age groups in every year",
     "Views change for every age group at the same moment",
     "Views differ between two cohorts surveyed in the same year"], ans=0,
   why="EK 4.3.A.1 ties a life cycle effect to different life stages, so its signature is that the pattern stays attached to the stage while the individuals in it turn over. That is what a stable age gradient across repeated surveys shows."),

 dict(q="Two analysts examine the same finding that older respondents hold a particular view more often than younger ones. One calls it generational and the other life cycle. What further information would settle the disagreement?",
   choices=[
     "Whether the pattern stays with the same age brackets or travels with the same cohorts as time passes",
     "Whether the survey was conducted by telephone or online",
     "Whether the respondents were registered to vote",
     "Whether the survey used a large enough sample",
     "Whether the question wording was neutral"], ans=0,
   why="A single cross section is consistent with both of EK 4.3.A.1's effects, because at one moment a cohort and an age bracket contain the same people. Only repeated measurement can separate an experience belonging to a common age from one belonging to a life stage."),

 dict(q="Why can a single survey taken at one moment never distinguish a generational effect from a life cycle effect?",
   choices=[
     "Because at any single moment every age group is also a single birth cohort, so the two explanations predict the same result",
     "Because surveys taken at one moment have no margin of error",
     "Because the framework says single surveys are unscientific",
     "Because a single survey cannot measure age",
     "Because a single survey cannot measure political ideology"], ans=0,
   why="EK 4.3.A.1's two effects differ in what the experience attaches to, and at one point in time age and birth year carry exactly the same information. Separating them requires watching how the pattern moves, which needs more than one observation."),

 dict(q="A person becomes more concerned about retirement income as they approach retirement age. Under EK 4.3.A.1, this is best described as",
   choices=[
     "a life cycle effect, since it is an experience encountered during a life stage",
     "a generational effect, since the person shares an age with others",
     "a generational effect, since retirement policy changes over time",
     "neither effect, since it concerns one individual",
     "both effects equally, since aging involves both"], ans=0,
   why="EK 4.3.A.1's second parenthesis covers experiences a person encounters during different life stages, and approaching retirement is such a stage. Every cohort reaches it in turn, which is what distinguishes it from an experience belonging to one birth group."),

 dict(q="A researcher finds that people who entered the workforce during a severe economic downturn hold distinctive views about economic policy thirty years later, regardless of their current age relative to others. Under EK 4.3.A.1, this is best described as",
   choices=[
     "a generational effect, since the experience was shared by people who reached a common point at the same moment",
     "a life cycle effect, since entering the workforce is a life stage",
     "a life cycle effect, since thirty years passed",
     "neither effect, since economic policy is not ideology",
     "both effects equally, since work and age are involved"], ans=0,
   why="The distinguishing detail is that the views persist regardless of current age, which locates them in the cohort rather than in a stage. EK 4.3.A.1's first parenthesis is experiences shared by people of a common age, and entering the workforce in one particular period is such a shared experience."),

 dict(q="In Brown v. Board of Education (1954), the Supreme Court held that race-based school segregation violates the equal protection clause of the Fourteenth Amendment. How could a decision of this kind produce a generational effect as EK 4.3.A.1 defines one?",
   choices=[
     "By giving people who were school-aged when it took effect an experience of schooling that people of other ages did not have",
     "By changing the views of every age group in the same way at the same time",
     "By altering the life stage at which people attend school",
     "By requiring schools to teach a particular political ideology",
     "It could not, since court decisions are not experiences"], ans=0,
   why="EK 4.3.A.1's definition of a generational effect is an experience shared by people of a common age, and a change taking effect in schools reaches those of school age at that moment and not others. The framework supplies the definition; it makes no claim about what any generation concluded."),

 dict(q="A student writes that EK 4.3.A.1 explains which political ideology a given generation holds. What is the most important correction?",
   choices=[
     "The framework says both effects contribute to the development of a person's ideology; it does not say which ideology results",
     "The framework says generational effects have no influence on ideology",
     "The framework names the ideology each generation holds",
     "The framework says ideology is fixed at birth",
     "The framework says only life cycle effects influence ideology"], ans=0,
   why="EK 4.3.A.1's claim is about contribution to a process of development, and it names no ideology and no generation. Supplying either would present an empirical claim to a student with the framework's authority behind it."),

 dict(q="How does EK 4.3.A.1 relate to the account of political socialization in EK 4.2.A.1?",
   choices=[
     "Both describe influences on how a person's political outlook develops, one through contributors such as family and media and the other through shared and stage-specific experiences",
     "The two statements describe unrelated processes",
     "EK 4.3.A.1 replaces political socialization with a different explanation",
     "EK 4.2.A.1 concerns institutions and EK 4.3.A.1 concerns courts",
     "Neither statement concerns the development of political attitudes"], ans=0,
   why="EK 4.2.A.1 names family, schools, peers, media and social environments as contributors to political attitudes and values; EK 4.3.A.1 adds generational and life cycle experiences as contributors to ideology. The two statements describe the same kind of developmental process from different angles."),

 dict(q="A commentator claims that because a certain age group holds distinctive views today, those views will define that group permanently. Which observation from this topic most directly qualifies the claim?",
   choices=[
     "If the pattern is a life cycle effect, the views belong to the stage and the group will hold different ones on reaching a later stage",
     "The framework says views never change once formed",
     "The framework says age groups never differ from one another",
     "The framework says only generational effects exist",
     "The framework says survey data cannot measure views"], ans=0,
   why="EK 4.3.A.1's life cycle parenthesis makes the experience belong to a stage rather than a person, so a pattern of that kind predicts change as the group ages rather than persistence. The commentator's inference assumes the generational reading without testing it."),

 dict(q="Which question would a political scientist studying LO 4.3.A be most likely to ask?",
   choices=[
     "Do the differences we see between age groups travel with those people as they age, or stay attached to the ages themselves?",
     "How many seats does each party hold in the Senate?",
     "What is the constitutional basis for judicial review?",
     "How long is a federal judge's term of office?",
     "How many states must ratify a constitutional amendment?"], ans=0,
   why="LO 4.3.A is about how social factors impact political ideology, and EK 4.3.A.1's two effects are distinguished precisely by whether a difference travels with people or stays with ages. The other four questions belong to Units 1 and 2."),

 dict(q="Why does the CED assign this topic a data analysis skill rather than a concept application skill?",
   choices=[
     "Because the two effects the topic names are difficult to tell apart in description and are separated by the shape of data over time",
     "Because the topic contains no concepts",
     "Because data analysis is the only skill used in Unit 4",
     "Because the topic concerns only numerical questions",
     "Because the framework provides its own data set for the topic"], ans=0,
   why="The suggested skill for 4.3 is 3.B, describe patterns and trends in data, and EK 4.3.A.1's two definitions are indistinguishable in a single description of a finding. Whether a difference belongs to a cohort or to a stage is visible only in how the numbers move."),

 dict(q="Which of the following does EK 4.3.A.1 NOT state?",
   choices=[
     "Which of the two effects has the greater influence on political ideology",
     "That generational effects are experiences shared by people of a common age",
     "That life cycle effects are experiences a person encounters during different life stages",
     "That both effects contribute to the development of a person's political ideology",
     "That both concern the development of political ideology"], ans=0,
   why="EK 4.3.A.1 supplies both definitions and the shared verb CONTRIBUTE, and supplies no comparison of magnitude. Every other option restates part of the framework's single sentence."),

 dict(q=_COHORTS + " Which statement best describes the pattern in the data?",
   table=_COHORTS_TABLE,
   choices=[
     "The three cohorts differ sharply from one another, and each one's share is nearly unchanged across the twenty years",
     "The three cohorts hold nearly identical shares in every year",
     "Each cohort's share rises sharply across the twenty years",
     "Each cohort's share falls sharply across the twenty years",
     "The cohorts converge toward a common share by the final year"], ans=0,
   why="The three rows sit at roughly 58, 41 and 27 percent and each moves by at most two points across the period. The gaps between the rows are more than 14 points and do not narrow."),

 dict(q=_COHORTS + " Which of the two effects named in EK 4.3.A.1 does this pattern support?",
   table=_COHORTS_TABLE,
   choices=[
     "A generational effect, because the differences stay attached to the birth cohorts as those cohorts age",
     "A life cycle effect, because the respondents grew older during the study",
     "A life cycle effect, because the shares changed slightly",
     "Neither, because the framework's two effects cannot be observed in data",
     "Both equally, because the study covers twenty years"], ans=0,
   why="EK 4.3.A.1 defines a generational effect as an experience shared by people of a common age, so its signature is a difference that travels with the cohort. Each cohort here carries its own level forward while aging twenty years, which is that signature."),

 dict(q=_COHORTS + " If this same position were instead produced by a life cycle effect, how would the table look different?",
   table=_COHORTS_TABLE,
   choices=[
     "Each cohort's share would move toward the level held by older cohorts as that cohort aged",
     "Each cohort's share would stay exactly where it is",
     "The cohorts would show no differences from one another in the first year",
     "Only the oldest cohort's share would change",
     "The table would report no figures at all"], ans=0,
   why="A life cycle effect belongs to a stage, so as each cohort reached an older stage it would take on that stage's level rather than keeping its own. The rows would converge on the age pattern instead of running parallel."),

 dict(q=_STAGES + " Which statement best describes the pattern in the data?",
   table=_STAGES_TABLE,
   choices=[
     "The share rises steadily with age within each survey year, and each age group's share is nearly unchanged across the twenty years",
     "The share falls with age within each survey year",
     "Each age group's share rises sharply across the twenty years",
     "The four age groups hold nearly identical shares in each year",
     "The age groups converge by the final survey year"], ans=0,
   why="Reading down any column gives 22, 38, 54 and 61, a rise of about 39 points from youngest to oldest, and reading across any row gives a change of at most two points. The gradient is by age, not by year."),

 dict(q=_STAGES + " Which of the two effects named in EK 4.3.A.1 does this pattern support, and why?",
   table=_STAGES_TABLE,
   choices=[
     "A life cycle effect, because the pattern stays attached to the age brackets even though different individuals occupy them each time",
     "A generational effect, because the youngest group differs from the oldest",
     "A generational effect, because twenty years elapsed",
     "Neither, because a survey cannot measure political positions",
     "Both equally, because age and time both appear in the table"], ans=0,
   why="The stem states that different individuals were interviewed each time, so a person who was in the youngest bracket in the first year is in an older bracket by the last, and the brackets nonetheless hold their levels. EK 4.3.A.1 defines a life cycle effect as belonging to a life stage, which is exactly what that shows."),

 dict(q=_STAGES + " A student concludes from this table that it shows a generational effect. What is the most important correction?",
   table=_STAGES_TABLE,
   choices=[
     "A generational effect would show the distinctive figures moving up the age ladder over time, and here they stay attached to the age brackets",
     "A generational effect would show every age group holding the same figure",
     "The table reports only one survey year, so no comparison is possible",
     "The table does not report age",
     "A generational effect cannot be observed in any table"], ans=0,
   why="If a cohort carried its level with it, the figure sitting at ages 18 to 29 in the first year would appear at ages 30 to 49 twenty years later. Instead each bracket holds its own level while its occupants turn over, which is the life cycle signature rather than the generational one."),

 dict(q=_TURNOUT + " Which statement best describes the patterns in the data?",
   table=_TURNOUT_TABLE,
   choices=[
     "Turnout rises with age in each election, and every age group's turnout is highest in the second election",
     "Turnout falls with age in each election",
     "Turnout is highest in the third election for every age group",
     "Turnout is identical across age groups within each election",
     "Only the youngest group's turnout changes across the three elections"], ans=0,
   why="Reading down any column gives a rise from the high thirties to the low seventies, and reading across any row gives the second election as the largest figure in all four rows. Every group moves, not only the youngest."),

 dict(q=_TURNOUT + " All four age groups turn out at a higher rate in the second election than in the first or third. Which explanation does that common movement best support?",
   table=_TURNOUT_TABLE,
   choices=[
     "Something particular to that election affected all age groups, rather than a change in any one group's life stage",
     "The youngest group reached a new life stage between elections",
     "One birth cohort changed its behavior and the others did not",
     "The oldest group alone responded to the second election",
     "Turnout is unrelated to the election being held"], ans=0,
   why="A life cycle effect belongs to a stage and a generational effect to a cohort, so neither predicts that every age group moves together in one election and back afterward. A movement common to all four groups points to the election rather than to the groups."),

 dict(q=_TURNOUT + " A student concludes from this table that the members of the youngest group became more likely to vote as they grew older. What is the most important correction?",
   table=_TURNOUT_TABLE,
   choices=[
     "The table reports age groups surveyed after each election rather than the same individuals over time, so it cannot show what happened to any person as they aged",
     "The table shows the youngest group's turnout falling to zero",
     "The table reports only one election, so no comparison is possible",
     "The table reports the same individuals in all three elections",
     "The table does not report turnout by age"], ans=0,
   why="The stem states that different individuals were surveyed after each election, so the youngest row describes a different set of people each time. Reading repeated cross sections as though they followed individuals is the error that makes EK 4.3.A.1's two effects look interchangeable."),
]
