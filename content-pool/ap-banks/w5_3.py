# AP WORLD HISTORY: MODERN 5.3 Industrial Revolution Begins
# CED effective Fall 2024, Unit 5 Revolutions, c. 1750 to c. 1900.
# Thematic focus: Humans and the Environment (ENV). Reasoning process: Causation.
# Suggested skill 1.B, explain a historical concept, development, or process.
#
# Learning objective:
#   Unit 5 LO D  Explain how environmental factors contributed to
#                industrialization from 1750 to 1900.
#
# Historical developments relied on, in the framework's own words:
#   KC-5.1.I.A  A variety of factors contributed to the growth of industrial
#               production and eventually resulted in the Industrial Revolution,
#               including:
#                 - Proximity to waterways; access to rivers and canals
#                 - Geographical distribution of coal, iron, and timber
#                 - Urbanization
#                 - Improved agricultural productivity
#                 - Legal protection of private property
#                 - Access to foreign resources
#                 - Accumulation of capital
#   KC-5.1.I.C  The development of the factory system concentrated production in a
#               single location and led to an increasing degree of specialization
#               of labor.
#
# ON THE SEVEN FACTORS. KC-5.1.I.A prints a bulleted list and introduces it with
# "a variety of factors" and "including". Both hedges are load-bearing: the
# framework neither ranks the seven nor claims the list is complete, so no key
# here asserts that one factor was decisive or that the list is exhaustive. Items
# 2 through 8 pair one illustrative situation with the one bullet it matches, and
# item 14 keys the hedges themselves.
#
# ON WHAT IS NOT KEYED. The framework does not name a first industrial country, a
# first factory, an inventor or a date in this statement, so neither does this
# module. Where a region has to be described, the description is explicitly
# illustrative and unattributed, and every key is recoverable from the stimulus
# plus a sentence the CED prints.
#
# The tables carry HYPOTHETICAL figures, labelled as such in the stem, because the
# CED prints no output or population data here. Each keyed conclusion is
# recomputed from the table alone in verify_w5_3.py.
TOPIC = ("5.3", "Industrial Revolution Begins", 5)

_T_DISTRICTS = dict(
    headers=["District (hypothetical)", "Miles of navigable river and canal",
             "Coal raised (thousands of tons per year)",
             "Population of the largest town"],
    rows=[["District 1", "48", "910", "62,000"],
          ["District 2", "6", "40", "9,000"],
          ["District 3", "31", "120", "18,000"],
          ["District 4", "2", "0", "4,000"]])

_T_YIELDS = dict(
    headers=["Decade of the sample", "Wheat yield per acre (bushels, hypothetical)",
             "Population of the nearby towns"],
    rows=[["First decade", "18", "24,000"],
          ["Second decade", "22", "39,000"],
          ["Third decade", "27", "58,000"]])

QUESTIONS = [
    dict(
        q="The course framework introduces the factors behind the growth of industrial "
          "production with the words a variety of factors and the word including. Which "
          "conclusion do those two words together support?",
        choices=[
            "No single factor is presented as sufficient on its own, and the list is not offered as complete",
            "The first factor listed is presented as the decisive one",
            "The seven factors listed are the only conditions that ever mattered anywhere",
            "The factors are presented as effects of industrialization rather than causes of it",
            "The framework presents the factors as unrelated to industrial production"],
        ans=0,
        why="KC-5.1.I.A opens by saying that a variety of factors contributed to the growth of "
            "industrial production, and introduces its bullets with including. Neither word "
            "ranks the factors or closes the list, and reading the framework's hedges is what "
            "keeps a key inside the CED.",
    ),
    dict(
        q="An illustrative account of a district describes goods moving cheaply to market "
          "along a river and a cut canal that joins it to a second valley. Which factor named "
          "by the course framework does the account describe?",
        choices=[
            "Proximity to waterways, with access to rivers and canals",
            "The accumulation of capital",
            "The legal protection of private property",
            "Improved agricultural productivity",
            "Access to foreign resources"],
        ans=0,
        why="KC-5.1.I.A's first bullet names proximity to waterways and access to rivers and "
            "canals among the factors contributing to the growth of industrial production. The "
            "account describes exactly that condition and says nothing about capital, law, "
            "farming or foreign supply.",
    ),
    dict(
        q="An illustrative survey reports that seams of coal, beds of iron ore and large stands "
          "of timber lie close together in one region and far apart in another. Which factor "
          "named by the course framework does the survey bear on?",
        choices=[
            "The geographical distribution of coal, iron, and timber",
            "Urbanization",
            "The accumulation of capital",
            "The legal protection of private property",
            "The specialization of labor inside a factory"],
        ans=0,
        why="KC-5.1.I.A's second bullet names the geographical distribution of coal, iron, and "
            "timber. The survey reports how those three are distributed, which is the factor "
            "itself rather than any of the demographic, financial or legal conditions on the "
            "same list.",
    ),
    dict(
        q="Which of the factors named by the course framework is described by an illustrative "
          "report that a growing share of a region's people had come to live in towns rather "
          "than on scattered farms?",
        choices=[
            "Urbanization",
            "Access to foreign resources",
            "Improved agricultural productivity",
            "Proximity to waterways",
            "The accumulation of capital"],
        ans=0,
        why="KC-5.1.I.A names urbanization among the factors contributing to the growth of "
            "industrial production. A shift of population from scattered farms into towns is "
            "that factor described; the framework lists it beside, not in place of, the "
            "agricultural and resource conditions.",
    ),
    dict(
        q="An illustrative estate record shows that the same acreage fed a larger number of "
          "people than it had a generation earlier, leaving hands free for other work. Which "
          "factor named by the course framework does the record illustrate?",
        choices=[
            "Improved agricultural productivity",
            "The legal protection of private property",
            "The geographical distribution of coal, iron, and timber",
            "Access to rivers and canals",
            "The concentration of production in a single location"],
        ans=0,
        why="KC-5.1.I.A names improved agricultural productivity among its factors. More food "
            "from the same land is that improvement, and the framework lists it as a "
            "contributor to industrial production rather than as a consequence of it.",
    ),
    dict(
        q="An illustrative legal code guarantees that a workshop, its machinery and its stock "
          "cannot be seized without compensation, and that contracts over them will be "
          "enforced. Which factor named by the course framework does the code supply?",
        choices=[
            "The legal protection of private property",
            "Access to foreign resources",
            "Urbanization",
            "Improved agricultural productivity",
            "The geographical distribution of coal, iron, and timber"],
        ans=0,
        why="KC-5.1.I.A names the legal protection of private property among the factors "
            "contributing to the growth of industrial production. A code securing ownership and "
            "enforcing contracts over productive assets is that protection, which the framework "
            "lists beside physical and demographic conditions.",
    ),
    dict(
        q="An illustrative merchant's ledger records raw fibers, dyestuffs and ores drawn from "
          "distant places and delivered to workshops at home. Which factor named by the course "
          "framework does the ledger document?",
        choices=[
            "Access to foreign resources",
            "The accumulation of capital",
            "Urbanization",
            "The legal protection of private property",
            "Proximity to waterways"],
        ans=0,
        why="KC-5.1.I.A names access to foreign resources among its factors. Materials drawn "
            "from distant places into domestic workshops is that access; the ledger says "
            "nothing about savings, town growth, law or river transport in itself.",
    ),
    dict(
        q="An illustrative account describes profits from decades of trade being held and "
          "reinvested rather than spent, until a sum large enough to build and equip a works "
          "had been assembled. Which factor named by the course framework does the account "
          "describe?",
        choices=[
            "The accumulation of capital",
            "Improved agricultural productivity",
            "Access to foreign resources",
            "The geographical distribution of coal, iron, and timber",
            "The specialization of labor"],
        ans=0,
        why="KC-5.1.I.A names the accumulation of capital among the factors contributing to the "
            "growth of industrial production. A fund built up over time and then committed to "
            "plant is that accumulation, which the framework treats as a condition for "
            "industrial growth.",
    ),
    dict(
        q="According to the course framework, what did the development of the factory system "
          "do to the location of production?",
        choices=[
            "It concentrated production in a single location",
            "It dispersed production across many rural households",
            "It moved production onto ships and away from any fixed site",
            "It left the location of production entirely unchanged",
            "It confined production to the estates of landholders"],
        ans=0,
        why="KC-5.1.I.C states that the development of the factory system concentrated "
            "production in a single location. Concentration is the framework's own word, and it "
            "is the change the rest of that statement then builds on.",
    ),
    dict(
        q="The course framework attaches a second consequence to the factory system besides "
          "the concentration of production. Which consequence is it?",
        choices=[
            "An increasing degree of specialization of labor",
            "A general reduction in the total quantity of goods produced",
            "The end of wage payment in industrial work",
            "The return of production to the household",
            "The abolition of the distinction between town and countryside"],
        ans=0,
        why="KC-5.1.I.C states that the factory system concentrated production in a single "
            "location and led to an increasing degree of specialization of labor. The two "
            "consequences are printed in one sentence, and only one of the listed options is "
            "the second of them.",
    ),
    dict(
        q="A student writes that an increasing specialization of labor came first and produced "
          "the factory system as its result. How does the course framework order the two?",
        choices=[
            "The factory system concentrated production and led to an increasing specialization of labor",
            "An increasing specialization of labor led to the development of the factory system",
            "The framework treats the two developments as having no connection",
            "The framework denies that specialization of labor increased at all",
            "The framework places both after the second industrial revolution"],
        ans=0,
        why="KC-5.1.I.C runs in one direction: the development of the factory system "
            "concentrated production in a single location AND LED TO an increasing degree of "
            "specialization of labor. The reasoning process for this topic is causation, so the "
            "order of the two clauses is the substance of the answer.",
    ),
    dict(
        q="This topic's learning objective concerns environmental factors. Which pair from the "
          "course framework's list of contributing factors is environmental in that sense?",
        choices=[
            "Proximity to waterways and the geographical distribution of coal, iron, and timber",
            "The accumulation of capital and the legal protection of private property",
            "Urbanization and the specialization of labor",
            "Access to foreign resources and the accumulation of capital",
            "The legal protection of private property and improved agricultural productivity"],
        ans=0,
        why="Unit 5 Learning Objective D asks how environmental factors contributed to "
            "industrialization, and the two bullets of KC-5.1.I.A that describe the physical "
            "setting are proximity to waterways and the distribution of coal, iron, and timber. "
            "The rejected pairs name legal, financial and demographic conditions instead.",
    ),
    dict(
        q="The table below reports hypothetical figures for four districts. Which district "
          "combines the largest endowment of the conditions the course framework names among "
          "its contributing factors?",
        table=_T_DISTRICTS,
        choices=[
            "District 1, which leads on navigable water, on coal raised and on town population",
            "District 2, which is smallest on every measure but one",
            "District 3, which leads on navigable water alone",
            "District 4, which raises no coal at all",
            "None of the four, because the table records no condition the framework names"],
        ans=0,
        why="KC-5.1.I.A names proximity to waterways, the distribution of coal and urbanization "
            "among its factors, and the table reports one column for each. Reading the columns "
            "together is what the question asks, and no single column decides it.",
    ),
    dict(
        q="The table below reports hypothetical figures across three decades of one region. "
          "Which conclusion does the table alone support?",
        table=_T_YIELDS,
        choices=[
            "Both the wheat yield and the town population rise in each successive decade",
            "The wheat yield rises while the town population falls",
            "The town population rises while the wheat yield falls",
            "Both figures remain unchanged across the three decades",
            "The table shows that higher yields caused the towns to grow"],
        ans=0,
        why="KC-5.1.I.A names improved agricultural productivity and urbanization as separate "
            "factors, and the table shows both moving upward together. What the table cannot "
            "show is that one produced the other, which is why the causal option is not "
            "supported by the figures alone.",
    ),
    dict(
        q="A historian studying an illustrative region finds abundant coal but no navigable "
          "water, no accumulated capital and no secure title to property. What does the course "
          "framework's account of the growth of industrial production suggest about drawing a "
          "conclusion from the coal alone?",
        choices=[
            "The framework names several contributing factors together, so one endowment settles little by itself",
            "The framework names coal as the single sufficient condition for industrial growth",
            "The framework denies that mineral resources contributed to industrial growth",
            "The framework treats secure title to property as irrelevant to industrial growth",
            "The framework treats navigable water as the only factor that ever mattered"],
        ans=0,
        why="KC-5.1.I.A lists a variety of factors, including waterways, minerals, urbanization, "
            "agricultural productivity, legal protection of property, foreign resources and "
            "accumulated capital. A region strong in one and weak in four is not what that "
            "statement describes, and the framework ranks none of them.",
    ),
    dict(
        q="An illustrative description of a workshop before the factory system reports that one "
          "worker carried a piece of cloth through every stage from raw fiber to finished bolt. "
          "According to the course framework, how did the factory system change this?",
        choices=[
            "It brought the stages into one location and divided them among specialized workers",
            "It left each worker responsible for every stage but moved the work to a town",
            "It returned every stage of the work to the household",
            "It removed the need for any human labor in the process",
            "It reduced the number of stages the cloth passed through to one"],
        ans=0,
        why="KC-5.1.I.C names both effects in a single sentence: production concentrated in a "
            "single location, and an increasing degree of specialization of labor. Splitting one "
            "worker's whole task among several is that specialization, and the concentration is "
            "what makes the split possible.",
    ),
    dict(
        q="Which statement best explains why the course framework treats urbanization as a "
          "factor contributing to industrial production rather than only as a result of it?",
        choices=[
            "The framework lists urbanization among the conditions that contributed to industrial growth",
            "The framework states that towns first appeared during the Industrial Revolution",
            "The framework denies that industrial production had any effect on towns",
            "The framework treats urbanization as a purely agricultural development",
            "The framework lists urbanization only among the effects of the factory system"],
        ans=0,
        why="KC-5.1.I.A places urbanization in its bulleted list of factors that contributed to "
            "the growth of industrial production. The framework treats urban growth as a "
            "consequence elsewhere, in KC-5.1.VI.C, but this statement is where it appears on "
            "the contributing side.",
    ),
    dict(
        q="An illustrative charter grants a company the exclusive right to work a mineral field "
          "and provides that no other party may take the ore or the ground without its consent. "
          "Which factor named by the course framework does the charter chiefly supply?",
        choices=[
            "The legal protection of private property",
            "The geographical distribution of coal, iron, and timber",
            "Access to foreign resources",
            "Improved agricultural productivity",
            "The accumulation of capital"],
        ans=0,
        why="KC-5.1.I.A names the legal protection of private property. The charter creates a "
            "secure claim rather than the mineral itself, so it supplies the legal condition and "
            "not the geological one, although the two work together in the same district.",
    ),
    dict(
        q="Two illustrative regions are compared. Both have coal and iron close together, but "
          "only one has rivers and cut canals reaching the coast. Using the course framework's "
          "list of factors, what is the most defensible comparison?",
        choices=[
            "The regions share one named factor and differ on another the framework also names",
            "The regions differ on no factor the framework names",
            "The framework names neither minerals nor waterways among its factors",
            "The region with waterways lacks every other named factor by definition",
            "The comparison is impossible because the framework ranks the factors"],
        ans=0,
        why="KC-5.1.I.A names the geographical distribution of coal, iron, and timber and, "
            "separately, proximity to waterways with access to rivers and canals. The two "
            "regions match on the first and differ on the second, and the framework's refusal to "
            "rank the bullets is what keeps the comparison at that level.",
    ),
    dict(
        q="An illustrative pamphlet of the period praises a new works for gathering under one "
          "roof what had been done in a hundred cottages. Which historical development does the "
          "pamphlet describe?",
        choices=[
            "The development of the factory system",
            "The accumulation of capital",
            "The improvement of agricultural productivity",
            "The legal protection of private property",
            "Access to foreign resources"],
        ans=0,
        why="KC-5.1.I.C describes the factory system as concentrating production in a single "
            "location. Work moving from scattered cottages under one roof is that concentration "
            "stated in the pamphlet's own terms.",
    ),
    dict(
        q="Which statement about the course framework's account of the origins of industrial "
          "production is most accurate?",
        choices=[
            "It presents the growth of industrial production as preceding and eventually resulting in the Industrial Revolution",
            "It presents the Industrial Revolution as arriving suddenly with no prior growth in production",
            "It presents the Industrial Revolution as a cause of the factors it lists",
            "It presents industrial production as unchanged throughout the period",
            "It presents the Industrial Revolution as confined to agriculture"],
        ans=0,
        why="KC-5.1.I.A says a variety of factors contributed to the GROWTH of industrial "
            "production and EVENTUALLY resulted in the Industrial Revolution. The framework "
            "puts a period of growth before the name, and the word eventually is its own signal "
            "that the process was not instantaneous.",
    ),
    dict(
        q="An illustrative traveller's account praises a district for the cheapness with which "
          "heavy goods reach it, noting that a ton moved by water costs a fraction of the same "
          "ton moved by road. Which factor named by the course framework does the account speak "
          "to?",
        choices=[
            "Proximity to waterways",
            "Urbanization",
            "The accumulation of capital",
            "The legal protection of private property",
            "Improved agricultural productivity"],
        ans=0,
        why="KC-5.1.I.A names proximity to waterways with access to rivers and canals among the "
            "factors contributing to the growth of industrial production. The cost of moving "
            "heavy goods by water is the practical form that factor takes.",
    ),
    dict(
        q="A student claims that the specialization of labor described by the course framework "
          "means each worker learned every task in the works. Which correction does the "
          "framework support?",
        choices=[
            "Specialization means the work was divided so that a worker performed a narrower part of it",
            "Specialization means each worker mastered the whole process from beginning to end",
            "Specialization means the works employed no workers at all",
            "Specialization means the works produced only a single kind of good",
            "Specialization means production returned to individual households"],
        ans=0,
        why="KC-5.1.I.C describes an increasing degree of specialization of labor following the "
            "concentration of production in a single location. An increasing degree of "
            "specialization narrows what any one worker does, which is the opposite of the "
            "student's reading.",
    ),
    dict(
        q="Which of the following would be the best evidence that the accumulation of capital "
          "named by the course framework was present in an illustrative district?",
        choices=[
            "Records of large sums held and then committed to building and equipping works",
            "A survey of the depth of the district's coal seams",
            "A census of the district's cattle",
            "A map of the district's parish boundaries",
            "A record of the rainfall in the district over one year"],
        ans=0,
        why="KC-5.1.I.A names the accumulation of capital as a distinct factor from mineral "
            "endowment and agricultural conditions. Evidence for it has to be evidence about "
            "funds gathered and invested, which the mineral, livestock, boundary and weather "
            "records do not supply.",
    ),
    dict(
        q="An illustrative report notes that a region's works depend on ores and fibers landed "
          "at its ports from other continents. Which pair of factors named by the course "
          "framework does the report bring together?",
        choices=[
            "Access to foreign resources and proximity to waterways",
            "Urbanization and the legal protection of private property",
            "Improved agricultural productivity and the accumulation of capital",
            "The distribution of coal, iron, and timber and improved agricultural productivity",
            "The accumulation of capital and the specialization of labor"],
        ans=0,
        why="KC-5.1.I.A names access to foreign resources and, separately, proximity to "
            "waterways with access to rivers and canals. Materials landed at ports and carried "
            "inland involves both bullets at once, which is why the report illustrates a pair "
            "rather than a single factor.",
    ),
    dict(
        q="Using the reasoning process assigned to this topic, causation, which question would "
          "a historian most need to answer before crediting one factor with the growth of "
          "industrial production in a district?",
        choices=[
            "Whether the other factors the framework names were also present in that district",
            "Whether the district's name appears in any surviving map",
            "Whether the district lay to the north or the south of a capital city",
            "How many churches the district contained",
            "In what year the district was first mentioned in writing"],
        ans=0,
        why="KC-5.1.I.A presents a variety of factors contributing together, so isolating one "
            "requires knowing what else was present. The rejected questions gather facts that "
            "leave the causal question exactly where it was.",
    ),
    dict(
        q="An illustrative comparison finds two districts alike in coal, waterways and capital, "
          "but only one had secure and enforceable title to land and machinery. What does the "
          "course framework allow a student to say about the difference?",
        choices=[
            "The difference falls on a factor the framework names, the legal protection of private property",
            "The difference falls on no factor the framework names",
            "The difference falls on the geographical distribution of timber",
            "The difference falls on access to foreign resources",
            "The framework treats legal arrangements as outside the growth of industrial production"],
        ans=0,
        why="KC-5.1.I.A names the legal protection of private property among the contributing "
            "factors, so a difference in enforceable title is a difference on the framework's "
            "own list. The rejected options relocate the difference onto bullets the comparison "
            "has already held equal.",
    ),
    dict(
        q="Which statement best describes the relationship the course framework draws between "
          "the factors it lists and the Industrial Revolution?",
        choices=[
            "The factors contributed to a growth in industrial production that eventually resulted in the Industrial Revolution",
            "The Industrial Revolution created each of the factors the framework lists",
            "The factors and the Industrial Revolution occurred at the same moment with no sequence between them",
            "The factors are named as barriers that the Industrial Revolution had to overcome",
            "The framework declines to connect the factors to the Industrial Revolution at all"],
        ans=0,
        why="KC-5.1.I.A states that a variety of factors contributed to the growth of industrial "
            "production and eventually resulted in the Industrial Revolution. The chain runs "
            "from the factors through growth to the Revolution, and no rejected option preserves "
            "that order.",
    ),
    dict(
        q="An illustrative account of a new works lists a foreman, a machine tender, a carder, a "
          "spinner, a weaver and a packer, each doing that task and no other, all under one "
          "roof. Which statement in the course framework does this arrangement illustrate most "
          "completely?",
        choices=[
            "That the factory system concentrated production in one place and increased the specialization of labor",
            "That improved agricultural productivity freed hands for other work",
            "That the legal protection of private property secured investment in machinery",
            "That access to foreign resources supplied raw materials to domestic works",
            "That proximity to waterways lowered the cost of moving heavy goods"],
        ans=0,
        why="KC-5.1.I.C names both halves of what the account describes: production concentrated "
            "in a single location and an increasing degree of specialization of labor. The "
            "rejected options are true statements of KC-5.1.I.A but each describes a condition "
            "outside the works rather than the arrangement inside it.",
    ),
    dict(
        q="Which single statement best summarizes what this topic asks students to understand "
          "about the beginning of the Industrial Revolution?",
        choices=[
            "Several environmental, economic and legal conditions together fed a growth in production that the factory system then reorganized",
            "A single invention transformed production everywhere at once",
            "Industrial production grew without any change in where or how work was organized",
            "The Industrial Revolution began in agriculture and never reached manufacturing",
            "The framework attributes the Industrial Revolution entirely to foreign trade"],
        ans=0,
        why="KC-5.1.I.A supplies the variety of contributing conditions and the growth in "
            "production, and KC-5.1.I.C supplies the reorganization of work in the factory "
            "system. The rejected options each contradict one of those two statements or "
            "collapse the framework's list to a single cause.",
    ),
]
