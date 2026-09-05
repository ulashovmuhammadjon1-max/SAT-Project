# AP WORLD HISTORY: MODERN 5.1 The Enlightenment
# CED effective Fall 2024, Unit 5 Revolutions, c. 1750 to c. 1900.
# Thematic focus: Cultural Developments and Interactions (CDI) and Social
# Interactions and Organization (SIO). Reasoning process: Continuity and Change.
# Suggested skill 3.A, identify and describe a claim and/or argument in a
# text-based or non-text-based source.
#
# Learning objectives:
#   Unit 5 LO A  Explain the intellectual and ideological context in which
#                revolutions swept the Atlantic world from 1750 to 1900.
#   Unit 5 LO B  Explain how the Enlightenment affected societies over time.
#
# Historical developments relied on, in the framework's own words:
#   KC-5.3.I.A   Enlightenment philosophies applied new ways of understanding and
#                empiricist approaches to both the natural world and human
#                relationships; they also reexamined the role that religion played
#                in public life and emphasized the importance of reason.
#                Philosophers developed new political ideas about the individual,
#                natural rights, and the social contract.
#   KC-5.3.I     The rise and diffusion of Enlightenment thought that questioned
#                established traditions in all areas of life often preceded
#                revolutions and rebellions against existing governments.
#   KC-5.3.II.i  Nationalism also became a major force shaping the historical
#                development of states and empires.
#   KC-5.3.I.C   Enlightenment ideas and religious ideals influenced various reform
#                movements. These reform movements contributed to the expansion of
#                rights, as seen in expanded suffrage, the abolition of slavery,
#                and the end of serfdom.
#   KC-5.3.IV.B  Demands for women's suffrage and an emergent feminism challenged
#                political and gender hierarchies.
#
# Illustrative examples printed on this topic's page, under "Demands":
#   Mary Wollstonecraft's A Vindication of the Rights of Woman; Olympe de Gouges's
#   Declaration of the Rights of Woman and of the Female Citizen; Seneca Falls
#   Conference (1848) organized by Elizabeth Cady Stanton and Lucretia Mott.
#
# ON THE SOURCES. AP World History Section I is stimulus based and this bank
# cannot display images, so every stimulus here is a TEXT. No quotation is
# attributed to a real person or document: the sources are explicitly illustrative
# and unattributed ("A pamphlet published during the period argues..."), and every
# key turns on reasoning from the source plus a sentence the CED prints, never on
# who wrote it. The three works named above are named because the CED names them.
#
# ON DATES. The CED states that events are not constrained by the given dates.
# No key here depends on a boundary the framework loosens; the one dated item,
# the Seneca Falls Conference of 1848, carries the date the CED itself prints.
TOPIC = ("5.1", "The Enlightenment", 5)

_T_PAMPHLETS = dict(
    headers=["Pamphlet (illustrative and unattributed)", "Central claim advanced"],
    rows=[["Pamphlet 1",
           "Rulers hold authority only through an agreement with the governed, who may withdraw it"],
          ["Pamphlet 2",
           "The rights of a person exist before any government and are not granted by it"],
          ["Pamphlet 3",
           "The customs handed down by our ancestors are the surest guide to good government"],
          ["Pamphlet 4",
           "Trade should be regulated by the crown for the benefit of the treasury"]])

_T_SUBJECTS = dict(
    headers=["Subject treated by the pamphlet", "Number of pamphlets"],
    rows=[["Natural rights and the social contract", "72"],
          ["The role of religion in public life", "54"],
          ["Improvement of agriculture", "38"],
          ["Ceremony and etiquette at court", "12"],
          ["Other subjects", "24"]])

QUESTIONS = [
    dict(
        q="An unattributed essay circulated during the period argues: \"Let us study the "
          "human being as the natural philosopher studies the motion of bodies, by "
          "observation and by trial, and not by asking what has always been believed.\" "
          "Which of the following best describes the intellectual move the essay makes?",
        choices=[
            "It extends to human relationships the empiricist approach already applied to the natural world",
            "It rejects the study of the natural world as a distraction from questions of the soul",
            "It treats inherited belief as the most reliable available evidence about human conduct",
            "It argues that the motion of bodies cannot be understood by observation at all",
            "It claims that human conduct is governed by laws that no inquiry can reach"],
        ans=0,
        why="KC-5.3.I.A states that Enlightenment philosophies applied new ways of "
            "understanding and empiricist approaches to both the natural world and human "
            "relationships. The essay does exactly that, carrying a method used for bodies "
            "over to the study of people.",
    ),
    dict(
        q="The course framework credits Enlightenment philosophers with developing new "
          "political ideas. Which grouping names those ideas as the framework states them?",
        choices=[
            "The individual, natural rights, and the social contract",
            "Divine right, hereditary rank, and corporate privilege",
            "Guild regulation, royal charter, and mercantile monopoly",
            "Clerical authority, canon law, and confessional unity",
            "Dynastic marriage, standing armies, and court patronage"],
        ans=0,
        why="KC-5.3.I.A closes by naming the three: philosophers developed new political "
            "ideas about the individual, natural rights, and the social contract. The other "
            "groupings name arrangements that Enlightenment thought questioned rather than "
            "ideas it produced.",
    ),
    dict(
        q="Which statement best expresses the relationship the course framework draws "
          "between Enlightenment thought and the revolts of the period?",
        choices=[
            "The questioning of established traditions often came before rebellions against existing governments",
            "Rebellions against existing governments produced the questioning of established traditions that followed them",
            "Enlightenment thought and armed rebellion arose independently and never met",
            "Every rebellion of the period was launched by philosophers themselves",
            "Established traditions went unquestioned until after new governments were in place"],
        ans=0,
        why="KC-5.3.I states that the rise and diffusion of Enlightenment thought that "
            "questioned established traditions in all areas of life often preceded revolutions "
            "and rebellions against existing governments. The framework puts the questioning "
            "first and says it often preceded, not that it always caused.",
    ),
    dict(
        q="A reform society of the period publishes a statement of its aims. Which set of "
          "achievements does the course framework name as the expansion of rights that "
          "reform movements of this period contributed to?",
        choices=[
            "Expanded suffrage, the abolition of slavery, and the end of serfdom",
            "Universal free trade, the gold standard, and limited liability",
            "Compulsory military service, tariff protection, and state pensions",
            "The confiscation of church lands, a state church, and a censorship board",
            "The chartering of colonial companies, monopolies, and royal patents"],
        ans=0,
        why="KC-5.3.I.C names the three outcomes together: reform movements contributed to "
            "the expansion of rights, as seen in expanded suffrage, the abolition of slavery, "
            "and the end of serfdom. The other sets name economic or administrative measures "
            "the framework does not attach to this statement.",
    ),
    dict(
        q="Two unattributed appeals of the period call for the same reform. One argues from "
          "the natural rights of the person; the other argues that the practice offends a "
          "religious duty. According to the course framework, what does the pairing "
          "illustrate about reform movements in this period?",
        choices=[
            "Both Enlightenment ideas and religious ideals influenced reform movements",
            "Only arguments from natural rights had any influence on reform movements",
            "Religious argument was confined to opposing reform throughout the period",
            "Reform movements drew on neither philosophy nor religion but only on economic interest",
            "Reform movements arose only where a government had already ordered the change"],
        ans=0,
        why="KC-5.3.I.C opens by naming two sources of influence at once: Enlightenment ideas "
            "and religious ideals influenced various reform movements. A source of each kind "
            "arguing for the same reform is that sentence in miniature.",
    ),
    dict(
        q="The course framework treats demands for women's suffrage and an emergent feminism "
          "as challenging which of the following?",
        choices=[
            "Political and gender hierarchies",
            "The distribution of coal and iron deposits",
            "The rules of banking and finance",
            "The boundaries between newly imagined national communities",
            "The organization of production inside the factory"],
        ans=0,
        why="KC-5.3.IV.B states that demands for women's suffrage and an emergent feminism "
            "challenged political and gender hierarchies. The other options name subjects the "
            "framework treats elsewhere in the unit, under industrial production, finance and "
            "nationalism.",
    ),
    dict(
        q="Which work does the course framework name as an example of the demands associated "
          "with an emergent feminism in this period?",
        choices=[
            "A Vindication of the Rights of Woman",
            "An Inquiry into the Nature and Causes of the Wealth of Nations",
            "The Condition of the Working Class in England",
            "Letter from Jamaica",
            "The Declaration of Independence"],
        ans=0,
        why="The illustrative examples printed on this topic's page under Demands name Mary "
            "Wollstonecraft's A Vindication of the Rights of Woman. The other titles appear in "
            "the framework or its activities under economics, industrial conditions, and the "
            "revolutionary documents of topic 5.2, not under this demand.",
    ),
    dict(
        q="A second work named by the course framework among the demands of this period "
          "deliberately echoes the title of a revolutionary declaration in order to press a "
          "claim on behalf of women. Which work is it?",
        choices=[
            "Declaration of the Rights of Woman and of the Female Citizen",
            "Declaration of the Rights of Man and of the Citizen",
            "A Vindication of the Rights of Woman",
            "The Communist Manifesto",
            "The Social Contract"],
        ans=0,
        why="The illustrative examples on this topic's page name Olympe de Gouges's "
            "Declaration of the Rights of Woman and of the Female Citizen. The framework "
            "separately names the Declaration of the Rights of Man and of the Citizen in "
            "KC-5.3.I.B as a French revolutionary document, which is the text being echoed.",
    ),
    dict(
        q="The course framework names a conference of 1848 as an illustrative example of "
          "demands challenging political and gender hierarchies. Who does the framework name "
          "as its organizers?",
        choices=[
            "Elizabeth Cady Stanton and Lucretia Mott",
            "Mary Wollstonecraft and Olympe de Gouges",
            "Adam Smith and Karl Marx",
            "Muhammad Ali and the Meiji reformers",
            "Lola Rodriguez de Tio and the Propaganda Movement"],
        ans=0,
        why="The illustrative examples on this topic's page name the Seneca Falls Conference "
            "(1848) organized by Elizabeth Cady Stanton and Lucretia Mott. The other names "
            "appear elsewhere in the framework: two as authors of the named works, and the "
            "rest under economics, state sponsored industrialization and nationalism.",
    ),
    dict(
        q="An unattributed treatise of the period argues that a person's standing before the "
          "law should not depend on which church that person attends, and that public office "
          "should be open regardless of confession. Which element of Enlightenment thought "
          "described by the course framework does the treatise most directly illustrate?",
        choices=[
            "A reexamination of the role that religion played in public life",
            "A rejection of empiricism in favor of revealed authority",
            "An argument that the state should have no revenue of its own",
            "A demand that national identity be fixed to the borders of the state",
            "A defense of hereditary privilege on grounds of long custom"],
        ans=0,
        why="KC-5.3.I.A states that Enlightenment philosophies reexamined the role that "
            "religion played in public life. Asking what part confession should play in law "
            "and office is that reexamination, and the framework does not describe it as "
            "hostility to belief itself.",
    ),
    dict(
        q="An unattributed pamphlet closes: \"Where custom and reason disagree, let reason "
          "decide, for custom can show only that a thing is old.\" Which emphasis described by "
          "the course framework does this closing line express?",
        choices=[
            "The emphasis on the importance of reason",
            "The emphasis on inherited custom as the test of truth",
            "The emphasis on the accumulation of capital",
            "The emphasis on a shared language as the basis of community",
            "The emphasis on the specialization of labor in a single location"],
        ans=0,
        why="KC-5.3.I.A states that Enlightenment philosophies emphasized the importance of "
            "reason. The line sets reason above age of custom, which is that emphasis stated "
            "as a rule of decision; the remaining options belong to industrial and national "
            "developments elsewhere in the unit.",
    ),
    dict(
        q="Alongside Enlightenment thought, the course framework identifies another force in "
          "this period as major in shaping the historical development of states and empires. "
          "Which force is it?",
        choices=[
            "Nationalism",
            "Monasticism",
            "Mercantilism",
            "Feudal vassalage",
            "Absolutist divine right"],
        ans=0,
        why="KC-5.3.II.i states that nationalism also became a major force shaping the "
            "historical development of states and empires. The word also places it beside "
            "Enlightenment thought rather than in place of it, and the other options name "
            "arrangements the period's movements challenged.",
    ),
    dict(
        q="The table below summarizes the central claim of four illustrative and unattributed "
          "pamphlets of the period. Which pamphlet advances a claim about natural rights as "
          "the course framework describes that idea?",
        table=_T_PAMPHLETS,
        choices=[
            "Pamphlet 2, because it places a person's rights before any government",
            "Pamphlet 1, because it makes authority rest on an agreement that may be withdrawn",
            "Pamphlet 3, because it makes inherited custom the standard of good government",
            "Pamphlet 4, because it makes the treasury the purpose of regulation",
            "None of the four, because natural rights are a claim about property alone"],
        ans=0,
        why="KC-5.3.I.A distinguishes the new political ideas about the individual, natural "
            "rights, and the social contract. Only the second pamphlet asserts rights that "
            "exist prior to government, which is the natural rights claim; the first states the "
            "social contract instead, and the others state neither.",
    ),
    dict(
        q="An unattributed source states: \"Government is not a gift bestowed from above but "
          "a compact entered into by those who are governed, and a compact that is broken by "
          "one side does not bind the other.\" Which of the new political ideas named by the "
          "course framework does this source advance?",
        choices=[
            "The social contract",
            "The balance of trade",
            "The specialization of labor",
            "The abolition of serfdom",
            "The unification of fragmented regions"],
        ans=0,
        why="KC-5.3.I.A names the social contract among the new political ideas developed by "
            "Enlightenment philosophers. A compact entered into by the governed, and one whose "
            "breach releases the other side, is that idea; the other options name economic, "
            "industrial and national developments treated elsewhere in the unit.",
    ),
    dict(
        q="A student writes that Enlightenment thought questioned established traditions only "
          "in matters of religion. Which correction is best supported by the course framework?",
        choices=[
            "The framework describes established traditions being questioned in all areas of life",
            "The framework limits the questioning to matters of trade and taxation",
            "The framework describes the questioning as confined to the universities",
            "The framework states that religion alone was left unquestioned",
            "The framework treats the questioning as beginning only after 1900"],
        ans=0,
        why="KC-5.3.I says the thought questioned established traditions in all areas of life. "
            "Religion is one of those areas rather than the boundary of the challenge, which is "
            "why the same statement can stand behind political, social and economic criticism "
            "in this unit.",
    ),
    dict(
        q="The course framework speaks of the rise AND the diffusion of Enlightenment thought. "
          "What does the second of those two words add to the first?",
        choices=[
            "That the thought spread beyond the settings in which it first appeared",
            "That the thought was confined to the place where it originated",
            "That the thought was suppressed wherever governments learned of it",
            "That the thought was rejected everywhere outside a single country",
            "That the thought lost its political content as it aged"],
        ans=0,
        why="KC-5.3.I pairs rise with diffusion, and the pairing is what allows the framework "
            "to connect one body of thought to revolutions and rebellions in several places. "
            "Diffusion is spread; the rise alone would describe origin without reach.",
    ),
    dict(
        q="An unattributed address to a reform society argues that holding a human being as "
          "property cannot be reconciled either with reason or with the duties of a "
          "Christian. Which achievement named by the course framework is this address "
          "arguing toward?",
        choices=[
            "The abolition of slavery",
            "The end of serfdom",
            "Expanded suffrage",
            "The adoption of free trade policies",
            "The organization of labor unions"],
        ans=0,
        why="KC-5.3.I.C names the abolition of slavery among the expansions of rights that "
            "reform movements contributed to, and the address argues from both an Enlightenment "
            "and a religious premise, which is the pairing that same statement describes. The "
            "other options are separate developments in the framework.",
    ),
    dict(
        q="Which statement about serfdom is supported by the course framework's treatment of "
          "reform movements in this period?",
        choices=[
            "Its end is named alongside expanded suffrage and the abolition of slavery as an expansion of rights",
            "Its end is named as a cause of the Enlightenment rather than a result of reform",
            "Its persistence is named as the principal achievement of reform movements",
            "It is named only as a feature of the factory system",
            "It is named as an outcome of the second industrial revolution"],
        ans=0,
        why="KC-5.3.I.C lists expanded suffrage, the abolition of slavery, and the end of "
            "serfdom together as the expansion of rights that reform movements contributed to. "
            "The framework places the end of serfdom on the result side of that sentence, not "
            "among causes or among industrial developments.",
    ),
    dict(
        q="A textbook chapter opens by describing the ideas circulating in the Atlantic world "
          "before turning to the revolutions of the period. Which purpose named by this "
          "topic's learning objective does that opening serve?",
        choices=[
            "Explaining the intellectual and ideological context in which revolutions swept the Atlantic world",
            "Explaining how technology shaped economic production over time",
            "Explaining how environmental factors contributed to industrialization",
            "Explaining the causes and effects of economic strategies of different states",
            "Explaining how industrialization caused change in existing social hierarchies"],
        ans=0,
        why="Unit 5 Learning Objective A asks students to explain the intellectual and "
            "ideological context in which revolutions swept the Atlantic world from 1750 to "
            "1900. The other options are the learning objectives of topics 5.5, 5.3, 5.6 and "
            "5.9, which concern industrial rather than intellectual context.",
    ),
    dict(
        q="The table below reports the subjects treated by a sample of two hundred "
          "illustrative pamphlets. Which conclusion does the table alone support?",
        table=_T_SUBJECTS,
        choices=[
            "More pamphlets in the sample treat natural rights and the social contract than treat the role of religion in public life",
            "Fewer pamphlets in the sample treat natural rights and the social contract than treat agriculture",
            "Most pamphlets in the sample treat ceremony and etiquette at court",
            "Every pamphlet in the sample treats a political subject of some kind",
            "The sample shows that pamphlets on religion were suppressed"],
        ans=0,
        why="The table is the whole basis for the answer: seventy two pamphlets treat natural "
            "rights and the social contract against fifty four on the role of religion in "
            "public life. The remaining options either reverse a comparison in the table or "
            "assert something the table does not record at all.",
    ),
    dict(
        q="Two unattributed sources of the period discuss the same proposed law. The first "
          "defends it because the arrangement it replaces has stood for centuries; the second "
          "defends it because observation shows it will do more good than harm. Which "
          "difference between the two is most relevant to this topic?",
        choices=[
            "The second argues from reason and evidence while the first argues from the age of a custom",
            "The first argues from reason and evidence while the second argues from the age of a custom",
            "Neither source offers an argument at all",
            "Both sources rest their case on religious duty",
            "The two sources differ only in the region where they were published"],
        ans=0,
        why="KC-5.3.I.A makes reason and empiricist approaches the mark of Enlightenment "
            "argument, and KC-5.3.I describes established traditions being questioned. Reading "
            "each source's ground of argument is exactly the work of suggested skill 3.A, "
            "identifying the claim advanced in a source.",
    ),
    dict(
        q="An unattributed writer of the period insists that the rights he defends belong to a "
          "person as a person, and are therefore not the crown's to give or to take away. How "
          "does this claim differ from a defense of rights grounded in a royal grant?",
        choices=[
            "It locates the rights before and outside the grant rather than in it",
            "It makes the rights depend on the crown's continued goodwill",
            "It restricts the rights to those who hold land from the crown",
            "It converts the rights into an obligation owed to the treasury",
            "It abandons any claim of right in favor of a claim of custom"],
        ans=0,
        why="KC-5.3.I.A names natural rights among the new political ideas. A right held as a "
            "person is not conferred by the authority it is asserted against, which is the "
            "difference from a granted privilege and the reason such a claim can be turned "
            "against existing political authority.",
    ),
    dict(
        q="Which of the following best describes what the idea of the social contract offered "
          "to critics of existing governments in this period?",
        choices=[
            "An account of political authority as resting on agreement, which supplies a standard the ruler can fail",
            "An account of political authority as inherited, which places the ruler beyond criticism",
            "An account of trade as best regulated for the benefit of the treasury",
            "An account of national identity as fixed by the borders of the state",
            "An account of production as best concentrated in a single location"],
        ans=0,
        why="KC-5.3.I.A names the social contract among the new political ideas, and KC-5.3.I "
            "describes such thought questioning established traditions and often preceding "
            "rebellions. Authority grounded in agreement can be judged against that agreement, "
            "which is what makes the idea usable by critics.",
    ),
    dict(
        q="Using the reasoning process assigned to this topic, continuity and change, which "
          "statement best describes European intellectual life across the period from 1750 to "
          "1900 as the course framework presents it?",
        choices=[
            "Established traditions continued to be defended even as new ways of understanding questioned them",
            "Established traditions vanished at once and left no defenders anywhere",
            "No new ways of understanding appeared during the period at all",
            "Change occurred only in the natural sciences and never in political thought",
            "The period saw continuity in every area of life except agriculture"],
        ans=0,
        why="KC-5.3.I describes traditions being questioned rather than instantly abolished, "
            "and KC-5.3.I.A describes new approaches being applied. A continuity and change "
            "answer has to hold both together, which is why an account of total rupture "
            "misreads the same sentences.",
    ),
    dict(
        q="A student claims that the expansion of suffrage in this period extended the vote to "
          "women as a matter of course. Which statement in the course framework most directly "
          "complicates that claim?",
        choices=[
            "That demands for women's suffrage and an emergent feminism challenged political and gender hierarchies",
            "That reform movements contributed to the end of serfdom",
            "That Enlightenment philosophies emphasized the importance of reason",
            "That nationalism became a major force shaping states and empires",
            "That the rise of Enlightenment thought often preceded rebellions"],
        ans=0,
        why="KC-5.3.IV.B presents women's suffrage as something demanded against standing "
            "hierarchies, which is language of contest rather than of automatic extension. The "
            "other statements are true of the period but say nothing about who the expanded "
            "suffrage of KC-5.3.I.C reached.",
    ),
    dict(
        q="A petition of the period asks a legislature to widen the franchise, and grounds the "
          "request in the claim that those who obey a law should have a voice in making it. "
          "Which pair of framework statements does the petition draw together?",
        choices=[
            "The new political ideas about natural rights and the social contract, and the reform movements that expanded suffrage",
            "The factory system, and the decline of Asian shares of global manufacturing",
            "The fossil fuels revolution, and the growth of transnational businesses",
            "State sponsored industrialization, and internal reform in Japan",
            "Rapid urbanization, and the emergence of new social classes"],
        ans=0,
        why="KC-5.3.I.A supplies the ideas the petition argues from and KC-5.3.I.C supplies "
            "the expanded suffrage it argues for, so the petition sits at the join between "
            "them. The other pairs are industrial and economic statements from topics 5.3 "
            "through 5.9 and do not touch the franchise.",
    ),
    dict(
        q="This topic's second learning objective asks students to explain how the "
          "Enlightenment affected societies over time. Which kind of evidence would best serve "
          "that objective?",
        choices=[
            "Reform movements appearing across several decades and drawing on the same body of ideas",
            "A single essay published in one year, considered on its own",
            "A list of the titles held in one private library",
            "The number of printing presses licensed in one city in one year",
            "A ruler's coronation oath, considered apart from any later event"],
        ans=0,
        why="Unit 5 Learning Objective B concerns effect over time, and KC-5.3.I.C attributes "
            "reform movements and their expansions of rights to Enlightenment ideas together "
            "with religious ideals. A body of movements across decades shows that duration; a "
            "single document at one moment cannot.",
    ),
    dict(
        q="An unattributed sermon of the period condemns a widespread practice as contrary to "
          "the equal standing of all people before God, and is later cited by a reform society "
          "in a campaign to abolish that practice. Which framework statement does this "
          "sequence illustrate?",
        choices=[
            "That religious ideals as well as Enlightenment ideas influenced reform movements",
            "That reform movements arose only where governments ordered them",
            "That religious argument played no part in the abolition of slavery",
            "That reform movements were confined to the expansion of suffrage",
            "That Enlightenment thought replaced religious argument entirely"],
        ans=0,
        why="KC-5.3.I.C names Enlightenment ideas and religious ideals together as influences "
            "on reform movements, so a religious argument feeding a campaign is that statement "
            "in operation. Nothing in the framework makes the two sources of argument mutually "
            "exclusive.",
    ),
    dict(
        q="A historian argues that Enlightenment thought caused each revolution of the period. "
          "Which feature of the course framework's own wording should make a student cautious "
          "about that argument?",
        choices=[
            "The framework says such thought often preceded rebellions rather than that it always caused them",
            "The framework denies that Enlightenment thought spread beyond one country",
            "The framework dates the diffusion of Enlightenment thought after 1900",
            "The framework attributes every rebellion of the period to religious ideals alone",
            "The framework treats revolutions as having no intellectual context at all"],
        ans=0,
        why="KC-5.3.I says the rise and diffusion of Enlightenment thought often preceded "
            "revolutions and rebellions. Precedence in time and the word often together fall "
            "short of universal causation, and reading the framework's hedges is part of "
            "reasoning honestly from it.",
    ),
    dict(
        q="Which single statement best summarizes what the course framework asks students to "
          "understand about the Enlightenment in this unit?",
        choices=[
            "It supplied new ways of understanding and new political ideas that questioned traditions and shaped later reform and revolt",
            "It was a movement in the fine arts with no bearing on political authority",
            "It was a program of industrial invention that produced the steam engine",
            "It was a settlement between churches that removed religion from dispute",
            "It was a scheme of trade regulation adopted by western European states"],
        ans=0,
        why="KC-5.3.I.A supplies the new ways of understanding and the new political ideas, "
            "KC-5.3.I supplies the questioning of traditions and the precedence over revolt, "
            "and KC-5.3.I.C supplies the later reform. The other options describe industrial, "
            "religious and economic developments the unit treats separately.",
    ),
]
