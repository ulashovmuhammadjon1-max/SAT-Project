# AP WORLD HISTORY: MODERN 5.9 Society and the Industrial Age
# CED effective Fall 2024, Unit 5 Revolutions, c. 1750 to c. 1900.
# Thematic focus: Social Interactions and Organization (SIO). Reasoning process:
# Continuity and Change. Suggested skill 4.B, explain how a specific historical
# development or process is situated within a broader historical context.
#
# Learning objective:
#   Unit 5 LO J  Explain how industrialization caused change in existing social
#                hierarchies and standards of living.
#
# Historical developments relied on, in the framework's own words:
#   KC-5.1.VI.A  New social classes, INCLUDING the middle class and the industrial
#                working class, developed.
#   KC-5.1.VI.B  While women and OFTEN children in working class families
#                TYPICALLY held wage-earning jobs to supplement their families'
#                income, middle-class women WHO DID NOT HAVE THE SAME ECONOMIC
#                DEMANDS TO SATISFY were INCREASINGLY LIMITED to roles in the
#                household or roles focused on child development.
#   KC-5.1.VI.C  The rapid urbanization that ACCOMPANIED global capitalism AT TIMES
#                led to a variety of challenges, INCLUDING pollution, poverty,
#                increased crime, public health crises, housing shortages, and
#                insufficient infrastructure to accommodate urban growth.
#
# The CED prints NO illustrative example on this topic's page. Nothing here names
# a city, a survey, a reformer or a date, because the framework names none.
#
# THE HEDGES, and the items that turn on each. KC-5.1.VI.B in particular is one
# long sentence with four qualifications in it, and stripping any of them produces
# a claim that reads well and is not the framework's:
#   "INCLUDING the middle class and the industrial working class"   -- item 3
#   "OFTEN children"                                                 -- item 9
#   "TYPICALLY held wage-earning jobs"                              -- item 10
#   "INCREASINGLY limited"                                          -- item 11
#   "AT TIMES led to"                                                -- item 16
#   "a variety of challenges, INCLUDING ..."                        -- item 17
# Items 25 and 26 make two of those hedges into goes-beyond items, so the
# qualification is keyed rather than merely observed.
#
# THE SWAP THIS TOPIC INVITES. KC-5.1.VI.B contrasts two groups of women in one
# sentence, and exchanging them is the single easiest wrong key here: it is the
# WORKING CLASS women and often children who typically held wage-earning jobs, and
# the MIDDLE-CLASS women who were increasingly limited to roles in the household.
# Item 8 carries the exchange as a distractor and its anchor carries BOTH clauses.
# Item 7 keys the reason the framework itself gives for the difference -- that
# middle-class women did not have the same economic demands to satisfy -- rather
# than any reason supplied from outside the CED.
#
# ON "ACCOMPANIED". KC-5.1.VI.C says the rapid urbanization ACCOMPANIED global
# capitalism and that the urbanization AT TIMES LED TO the challenges. Those are
# two different relations in one sentence, and item 20 keys the first while item
# 18 keys the second against its reversal.
#
# ON SOURCES AND FIGURES. Section I is stimulus based and this bank cannot display
# images, so every stimulus is a TEXT or a table. No quotation is attributed to a
# real person or document -- each source is explicitly illustrative and
# unattributed. Table figures are HYPOTHETICAL and the stems say so; the CED
# prints no data.
TOPIC = ("5.9", "Society and the Industrial Age", 5)

_T_CLASSES = dict(
    headers=["Decade of the illustrative sample",
             "Households counted as middle class (percent)",
             "Households counted as industrial working class (percent)",
             "Households in older rural occupations (percent)"],
    rows=[["First decade", "6", "11", "83"],
          ["Second decade", "11", "27", "62"],
          ["Third decade", "17", "44", "39"],
          ["Fourth decade", "24", "58", "18"]])

_T_REPORTS = dict(
    headers=["Illustrative report on a growing town", "What the report describes"],
    rows=[["Report 1", "Smoke and fouled water"],
          ["Report 2", "Families crowded for want of houses"],
          ["Report 3", "Deaths from fever spreading through a district"],
          ["Report 4", "A rise in the number of thefts"],
          ["Report 5", "A shortage of laborers in the surrounding countryside"]])

_T_SURVEY = dict(
    headers=["Group in the illustrative survey", "Share holding wage-earning jobs (percent)"],
    rows=[["Women in working class families", "71"],
          ["Children in working class families", "44"],
          ["Women in middle class families", "9"]])

QUESTIONS = [
    dict(
        q="What does the course framework say developed in societies as they industrialized?",
        choices=[
            "New social classes, including the middle class and the industrial working class",
            "A single undivided class of wage earners",
            "The disappearance of all class distinctions",
            "A return to the older rural social order",
            "New classes confined entirely to rural districts"],
        ans=0,
        why="KC-5.1.VI.A is one short sentence and it says exactly that: new social classes, "
            "including the middle class and the industrial working class, developed. The rejected "
            "options each deny that new and distinct classes appeared.",
    ),
    dict(
        q="Which two classes does the course framework name among the new social classes of this "
          "period?",
        choices=[
            "The middle class and the industrial working class",
            "The landed nobility and the peasantry",
            "The merchant guilds and the clergy",
            "The salaried officials and the military officers",
            "The transnational business owners and the free traders"],
        ans=0,
        why="KC-5.1.VI.A names those two and no others. The framework describes them as NEW, "
            "which is what separates them from the older groups the rejected options name.",
    ),
    dict(
        q="The course framework names the middle class and the industrial working class with the "
          "word including. What does that establish?",
        choices=[
            "That the two named are examples and the framework does not say they were the only new classes",
            "That the two named were the only new classes that developed",
            "That no new classes developed during the period",
            "That the framework counts the new classes exactly",
            "That the two named classes existed before industrialization began"],
        ans=0,
        why="KC-5.1.VI.A says new social classes, INCLUDING the middle class and the industrial "
            "working class. The word leaves the list open, so a key treating the two as the whole "
            "of it would assert more than the framework does.",
    ),
    dict(
        q="What does the course framework say women and often children in working class families "
          "typically held?",
        choices=[
            "Wage-earning jobs",
            "Positions in the government of their towns",
            "Land of their own in the countryside",
            "Shares in transnational businesses",
            "Places in the new secondary schools"],
        ans=0,
        why="KC-5.1.VI.B opens with it: women and often children in working class families "
            "typically held wage-earning jobs. The framework mentions no other holding for those "
            "families anywhere in the statement.",
    ),
    dict(
        q="According to the course framework, why did women and often children in working class "
          "families hold those jobs?",
        choices=[
            "To supplement their families' income",
            "To qualify for the vote",
            "To join a labor union",
            "To meet a requirement of the factory system",
            "To replace men who had left for the colonies"],
        ans=0,
        why="KC-5.1.VI.B gives the purpose in the same clause: they held wage-earning jobs to "
            "supplement their families' income. Suffrage belongs to KC-5.3.I.C and unions to "
            "KC-5.1.V.A, neither of which is offered here as a reason for the work.",
    ),
    dict(
        q="What does the course framework say middle-class women were increasingly limited to?",
        choices=[
            "Roles in the household or roles focused on child development",
            "Wage-earning jobs in factories and workshops",
            "Positions in the government of their towns",
            "Work in the fields of the surrounding countryside",
            "Membership of workers' political parties"],
        ans=0,
        why="KC-5.1.VI.B closes with those two roles and names no third. Wage-earning work is "
            "what the same sentence attaches to working class families instead, which is the "
            "contrast the whole statement is built on.",
    ),
    dict(
        q="What reason does the course framework give for the position it describes for "
          "middle-class women?",
        choices=[
            "They did not have the same economic demands to satisfy",
            "They were forbidden by law from holding any employment",
            "They had joined labor unions in large numbers",
            "They had been displaced by machinery in the factories",
            "They had emigrated from the industrializing states"],
        ans=0,
        why="KC-5.1.VI.B supplies the reason itself: middle-class women WHO DID NOT HAVE THE SAME "
            "ECONOMIC DEMANDS TO SATISFY were increasingly limited to those roles. The rejected "
            "options are reasons the framework nowhere gives.",
    ),
    dict(
        q="A student writes that middle-class women typically held wage-earning jobs while women "
          "in working class families were increasingly limited to the household. How does the "
          "course framework describe the two?",
        choices=[
            "Working class women typically held wage-earning jobs, while middle-class women were increasingly limited to roles in the household",
            "Middle-class women typically held wage-earning jobs, while working class women were increasingly limited to roles in the household",
            "The framework describes both groups as holding wage-earning jobs equally",
            "The framework describes both groups as limited to roles in the household",
            "The framework makes no distinction between the two groups"],
        ans=0,
        why="KC-5.1.VI.B contrasts the two groups in a single sentence and the exchange is the "
            "easiest wrong key in this topic, so the anchor carries both clauses. The framework "
            "attaches the wage-earning work to working class families and the household roles to "
            "middle-class women.",
    ),
    dict(
        q="The course framework writes that women and often children in working class families "
          "held wage-earning jobs. What does the word often establish about the children?",
        choices=[
            "That children frequently did so, without the framework claiming all of them did",
            "That every child in such families did so",
            "That no children did so",
            "That children did so more frequently than the women of those families",
            "That the framework gives the proportion of children who did so"],
        ans=0,
        why="KC-5.1.VI.B qualifies only the children with often, and it prints no figure for "
            "either group. The sentence therefore supports neither a universal claim about "
            "children nor any comparison of how frequently the two groups worked.",
    ),
    dict(
        q="The course framework says women in working class families typically held wage-earning "
          "jobs. What does that word establish?",
        choices=[
            "That it was the usual case rather than a universal one",
            "That it was true of every such woman without exception",
            "That it was true of none of them",
            "That it became true only after the period ended",
            "That the framework counts how many did so"],
        ans=0,
        why="KC-5.1.VI.B says TYPICALLY held wage-earning jobs. The adverb describes the usual "
            "case and stops there, and the framework supplies no count anywhere in the statement.",
    ),
    dict(
        q="The course framework says middle-class women were increasingly limited to certain "
          "roles. What does that word establish?",
        choices=[
            "That the framework describes a trend growing over time rather than a fixed condition",
            "That the limitation was complete from the start of the period",
            "That the limitation was lifted over the course of the period",
            "That no such limitation is described at all",
            "That the limitation applied equally to working class women"],
        ans=0,
        why="KC-5.1.VI.B says INCREASINGLY limited, which is a direction of change rather than a "
            "settled state, and this topic's reasoning process is continuity and change. The "
            "same sentence attaches wage-earning work to working class families, so the "
            "limitation is not described as applying to them equally.",
    ),
    dict(
        q="What does the course framework say the rapid urbanization of this period accompanied?",
        choices=[
            "Global capitalism",
            "The decline of manufacturing",
            "The abolition of serfdom in eastern Europe",
            "The reform of Asian and African militaries",
            "The abandonment of free trade policies"],
        ans=0,
        why="KC-5.1.VI.C opens with the phrase: the rapid urbanization that accompanied global "
            "capitalism. The framework's verb is accompanied, which places the two side by side "
            "without making either the cause of the other.",
    ),
    dict(
        q="According to the course framework, what did the rapid urbanization of this period at "
          "times lead to?",
        choices=[
            "A variety of challenges",
            "A uniform improvement in living conditions",
            "The end of migration into cities",
            "The disappearance of the new social classes",
            "A fall in the population of the industrial towns"],
        ans=0,
        why="KC-5.1.VI.C says the rapid urbanization at times led to a variety of challenges, and "
            "then lists them. The rejected options each contradict that outcome rather than "
            "qualifying it.",
    ),
    dict(
        q="Which set names challenges the course framework lists in its account of rapid "
          "urbanization?",
        choices=[
            "Pollution, poverty, increased crime, public health crises and housing shortages",
            "Famine, plague, invasion and civil war",
            "Deforestation, soil exhaustion, flooding and drought",
            "Illiteracy, superstition, idleness and vagrancy",
            "Inflation, unemployment, bankruptcy and default"],
        ans=0,
        why="KC-5.1.VI.C prints pollution, poverty, increased crime, public health crises, "
            "housing shortages, and insufficient infrastructure to accommodate urban growth. The "
            "rejected sets name difficulties the framework does not attach to urbanization here.",
    ),
    dict(
        q="The course framework also names a sixth difficulty alongside pollution, poverty, "
          "increased crime, public health crises and housing shortages. What is it?",
        choices=[
            "Insufficient infrastructure to accommodate urban growth",
            "A shortage of laborers in the surrounding countryside",
            "The closure of the older craft guilds",
            "The collapse of trade over long distances",
            "The prohibition of new building in the towns"],
        ans=0,
        why="KC-5.1.VI.C closes its list with insufficient infrastructure to accommodate urban "
            "growth. That is the sixth item the framework prints, and none of the rejected "
            "options appears in the statement at all.",
    ),
    dict(
        q="The course framework says rapid urbanization at times led to these challenges. What "
          "does that phrase establish?",
        choices=[
            "That the framework describes an outcome that sometimes followed rather than one that always did",
            "That the outcome followed in every case without exception",
            "That the outcome never followed",
            "That the framework dates each occasion on which it followed",
            "That the challenges came before the urbanization"],
        ans=0,
        why="KC-5.1.VI.C says AT TIMES led to a variety of challenges. The phrase limits how often "
            "the outcome followed and the framework supplies no dates, so neither a universal "
            "claim nor a dated one can be keyed.",
    ),
    dict(
        q="The course framework introduces its list of urban difficulties with the words a "
          "variety of challenges, including. What do those words establish?",
        choices=[
            "That the list gives examples and the framework does not present it as complete",
            "That the list is the complete set of challenges that arose",
            "That only one difficulty arose in the growing towns",
            "That the framework ranks the challenges by severity",
            "That the challenges were confined to a single named city"],
        ans=0,
        why="KC-5.1.VI.C says a VARIETY of challenges, INCLUDING the six it then names. Both "
            "words leave the list open, and the framework neither ranks the six nor attaches them "
            "to any named place.",
    ),
    dict(
        q="A student writes that the challenges of pollution, poverty and overcrowding produced "
          "the rapid urbanization of this period. How does the course framework order the two?",
        choices=[
            "The rapid urbanization came first and at times led to those challenges",
            "The challenges came first and led to the rapid urbanization",
            "The framework treats the two as unconnected",
            "The framework denies that urbanization was rapid in this period",
            "The framework places both before the beginning of industrialization"],
        ans=0,
        why="KC-5.1.VI.C puts the rapid urbanization first and the challenges second, and it "
            "keeps the qualification at times. The anchor carries both clauses because a "
            "distractor exchanges them.",
    ),
    dict(
        q="This topic's learning objective concerns social hierarchies and standards of living. "
          "Which question is best matched to it?",
        choices=[
            "How industrialization changed existing social hierarchies and standards of living",
            "How environmental factors contributed to the beginning of industrial production",
            "How economic systems and institutions contributed to change in the period",
            "How the causes and effects of the period's revolutions can be explained",
            "How technology shaped economic production over time"],
        ans=0,
        why="Unit 5 Learning Objective J asks students to explain how industrialization caused "
            "change in existing social hierarchies and standards of living. The rejected "
            "questions belong to the objectives behind KC-5.1.I.A, KC-5.1.III.A, KC-5.3 and "
            "KC-5.1.I.B.",
    ),
    dict(
        q="This topic's suggested skill asks students to situate a development within a broader "
          "context. Within which broader development does the course framework place the rapid "
          "urbanization of this period?",
        choices=[
            "Global capitalism, which the framework says that urbanization accompanied",
            "The abandonment of mercantilism by western European states",
            "The reform of economies and militaries in Asia and Africa",
            "The revolutions and rebellions against existing governments",
            "The rise and diffusion of Enlightenment thought"],
        ans=0,
        why="KC-5.1.VI.C situates the urbanization itself: the rapid urbanization that "
            "accompanied global capitalism. The rejected options are the broader contexts named "
            "in KC-5.1.III.A, KC-5.1.V.B, KC-5.3 and KC-5.3.I, none of which the framework "
            "attaches to urban growth.",
    ),
    dict(
        q="An illustrative and unattributed town directory from the period lists, alongside the "
          "older trades, a growing number of clerks, managers and shopkeepers on one page and of "
          "mill hands on another. Which framework statement does the directory illustrate?",
        choices=[
            "That new social classes, including the middle class and the industrial working class, developed",
            "That rapid urbanization at times led to housing shortages",
            "That middle-class women were increasingly limited to roles in the household",
            "That many workers organized themselves in labor unions",
            "That some governments promoted industrial visions of their own"],
        ans=0,
        why="KC-5.1.VI.A says new social classes, including the middle class and the industrial "
            "working class, developed. A directory recording two growing groups of townspeople "
            "beside the older trades is that development in a record of the period.",
    ),
    dict(
        q="An illustrative and unattributed household budget from a working class family in an "
          "industrial town shows earnings entered for the mother and for two of the children as "
          "well as for the father. Which framework statement does the budget illustrate?",
        choices=[
            "That women and often children in working class families typically held wage-earning jobs to supplement their families' income",
            "That middle-class women were increasingly limited to roles focused on child development",
            "That new social classes developed in industrializing societies",
            "That rapid urbanization at times led to public health crises",
            "That workers organized themselves to gain higher wages"],
        ans=0,
        why="KC-5.1.VI.B attaches wage-earning work to women and often children in working class "
            "families, and gives supplementing the family's income as its purpose. A budget with "
            "three sets of earnings in one household is that arrangement written down.",
    ),
    dict(
        q="An illustrative and unattributed manual addressed to the wives of salaried men devotes "
          "its chapters to the ordering of a household and the upbringing of children, and says "
          "nothing of paid employment. Which framework statement does the manual illustrate?",
        choices=[
            "That middle-class women were increasingly limited to roles in the household or roles focused on child development",
            "That working class women typically held wage-earning jobs",
            "That new social classes developed in industrializing societies",
            "That rapid urbanization at times led to increased crime",
            "That discontent encouraged the development of new ideologies"],
        ans=0,
        why="KC-5.1.VI.B names exactly those two roles for middle-class women, and the manual's "
            "two subjects are those two roles. Its intended readers are the wives of salaried "
            "men, which is the group the framework's clause is about.",
    ),
    dict(
        q="An illustrative and unattributed inspector's report on a growing town describes cellars "
          "let as dwellings, a water supply drawn from a fouled river, and streets without drains. "
          "Which framework statement does the report illustrate?",
        choices=[
            "That rapid urbanization at times led to housing shortages, pollution and insufficient infrastructure",
            "That new social classes developed in industrializing societies",
            "That middle-class women were limited to roles in the household",
            "That some governments in Asia sought to modernize their economies",
            "That western European countries adopted free trade policies"],
        ans=0,
        why="KC-5.1.VI.C names housing shortages, pollution and insufficient infrastructure to "
            "accommodate urban growth among the challenges rapid urbanization at times brought. "
            "Cellars used as dwellings, a fouled water supply and streets without drains are "
            "those three together.",
    ),
    dict(
        q="Which of the following claims goes beyond what the course framework states about "
          "women's work in this period?",
        choices=[
            "That every middle-class woman was barred from paid employment throughout the period",
            "That women in working class families typically held wage-earning jobs",
            "That those jobs supplemented their families' income",
            "That middle-class women were increasingly limited to roles in the household",
            "That the framework gives a reason for the difference between the two groups"],
        ans=0,
        why="KC-5.1.VI.B says middle-class women were INCREASINGLY LIMITED to certain roles, which "
            "describes a trend and not a bar. The framework states the other four claims and "
            "supplies the reason itself, so only the universal prohibition is added from outside.",
    ),
    dict(
        q="Which claim about rapid urbanization goes beyond what the course framework asserts?",
        choices=[
            "That the challenges named followed in every town that grew during the period",
            "That rapid urbanization accompanied global capitalism",
            "That rapid urbanization at times led to a variety of challenges",
            "That pollution is among the challenges the framework names",
            "That insufficient infrastructure is among the challenges the framework names"],
        ans=0,
        why="KC-5.1.VI.C says the urbanization AT TIMES led to those challenges and names no "
            "town. Turning that into a claim about every growing town drops the framework's own "
            "qualification, while the other four options restate parts of the same sentence.",
    ),
    dict(
        q="The table below reports hypothetical figures for one illustrative industrializing "
          "society across four decades. Which conclusion does the table support?",
        table=_T_CLASSES,
        choices=[
            "The shares in both new classes rise in every decade while the share in older rural occupations falls in every decade",
            "The shares in both new classes fall while the share in older rural occupations rises",
            "All three shares rise across the four decades",
            "None of the three shares changes across the four decades",
            "The share in older rural occupations reaches zero by the fourth decade"],
        ans=0,
        why="KC-5.1.VI.A says new social classes, including the middle class and the industrial "
            "working class, developed, and the sample shows what that looks like in figures. "
            "Every column is read from the table, the three shares in each row account for the "
            "whole society, and the rural share is still above zero in the last decade.",
    ),
    dict(
        q="The table below records what each of five illustrative reports on a growing town "
          "describes. Which of the five is NOT one of the challenges the course framework lists "
          "by name?",
        table=_T_REPORTS,
        choices=[
            "A shortage of laborers in the surrounding countryside",
            "Smoke and fouled water",
            "Families crowded for want of houses",
            "Deaths from fever spreading through a district",
            "A rise in the number of thefts"],
        ans=0,
        why="KC-5.1.VI.C lists pollution, poverty, increased crime, public health crises, housing "
            "shortages, and insufficient infrastructure. Four of the reports answer to one of "
            "those named challenges each, and a scarcity of rural labor answers to none of them.",
    ),
    dict(
        q="The table below reports hypothetical figures from one illustrative survey. Which "
          "conclusion does the table support?",
        table=_T_SURVEY,
        choices=[
            "The share holding wage-earning jobs is highest among women in working class families and lowest among women in middle class families",
            "The share holding wage-earning jobs is highest among women in middle class families",
            "The three groups hold wage-earning jobs in equal shares",
            "No group in the survey holds a wage-earning job",
            "The share is highest among the children of working class families"],
        ans=0,
        why="KC-5.1.VI.B attaches wage-earning work to women and often children in working class "
            "families and household roles to middle-class women, and the survey ranks the same "
            "way. Both ends of the keyed conclusion are read from the table's one numeric column.",
    ),
    dict(
        q="Which single statement best summarizes what this topic asks students to understand "
          "about society in the industrial age?",
        choices=[
            "New classes developed, work and household roles differed between working class and middle-class families, and rapid urbanization at times brought pollution, poverty, crime, disease, housing shortages and strained infrastructure",
            "Industrialization left the existing social hierarchy exactly as it had been",
            "Every family in an industrializing society experienced the same change in the same way",
            "Rapid urbanization brought no difficulties of any kind",
            "The framework treats industrialization as unrelated to standards of living"],
        ans=0,
        why="The summary joins KC-5.1.VI.A, KC-5.1.VI.B and KC-5.1.VI.C, the three statements "
            "this topic prints, and it keeps the qualification at times on the last of them. Each "
            "rejected option contradicts one of the three.",
    ),
]
