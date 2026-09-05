# AP WORLD HISTORY: MODERN 5.5 Technology of the Industrial Age
# CED effective Fall 2024, Unit 5 Revolutions, c. 1750 to c. 1900.
# Thematic focus: Technology and Innovation (TEC). Reasoning process: Causation.
# Suggested skill 1.B, explain a historical concept, development, or process.
#
# Learning objective:
#   Unit 5 LO F  Explain how technology shaped economic production over time.
#
# Historical developments relied on, in the framework's own words:
#   KC-5.1.I.B  The development of machines, including steam engines and the
#               internal combustion engine, made it possible to take advantage of
#               both existing and vast newly discovered resources of energy stored
#               in fossil fuels, specifically coal and oil. The fossil fuels
#               revolution greatly increased the energy available to human
#               societies.
#   KC-5.1.I.E  The "second industrial revolution" led to new methods in the
#               production of steel, chemicals, electricity, and precision
#               machinery during the second half of the 19th century.
#   KC-5.1.IV   Railroads, steamships, and the telegraph made exploration,
#               development, and communication possible in interior regions
#               globally, which led to increased trade and migration.
#
# ON THE ONE DATE KEYED HERE. KC-5.1.I.E prints "during the second half of the
# 19th century" itself, so item 5 keys the framework's own words. No other item
# in the module turns on a date, because the CED states that its periods are
# approximate and may begin before or continue after the years given.
#
# ON THE DIRECTION OF THE ARROWS. Both KC-5.1.I.B and KC-5.1.IV are causal
# sentences and both are easy to state backwards: it is the MACHINES that made it
# possible to take advantage of the fossil fuels, and it is the railroads,
# steamships and telegraph that made exploration, development and communication
# possible, which THEN led to increased trade and migration. Items 11, 19 and 24
# carry the reversed sentence as a distractor, and their anchors carry both
# clauses so the anchor cannot match the swap.
#
# WHAT IS NOT KEYED. The framework names no inventor, no country of origin for any
# machine, and no date for any of the five technologies its sample activity lists.
# None of that is asserted here. The consequences of these technologies for empire
# and for migration patterns belong to KC-5.2 and KC-5.4, which are unit 6.
#
# Table figures are HYPOTHETICAL and the stems say so; the CED prints no data.
TOPIC = ("5.5", "Technology of the Industrial Age", 5)

_T_ENERGY = dict(
    headers=["Decade of the sample", "Coal consumed (millions of tons)",
             "Energy available per person (index)"],
    rows=[["First decade", "12", "100"],
          ["Second decade", "31", "158"],
          ["Third decade", "74", "246"],
          ["Fourth decade", "150", "402"]])

_T_METHODS = dict(
    headers=["Development", "Where the framework names it"],
    rows=[["Steel", "Among the new methods of the second industrial revolution"],
          ["Chemicals", "Among the new methods of the second industrial revolution"],
          ["Electricity", "Among the new methods of the second industrial revolution"],
          ["Precision machinery", "Among the new methods of the second industrial revolution"],
          ["The steam engine", "Among the machines that made fossil fuel energy usable"]])

QUESTIONS = [
    dict(
        q="Which two machines does the course framework name when it describes the development "
          "that made stored fossil fuel energy usable?",
        choices=[
            "Steam engines and the internal combustion engine",
            "The spinning jenny and the power loom",
            "The telegraph and the telephone",
            "The blast furnace and the crucible",
            "The water wheel and the windmill"],
        ans=0,
        why="KC-5.1.I.B names them explicitly: the development of machines, including steam "
            "engines and the internal combustion engine, made it possible to take advantage of "
            "resources of energy stored in fossil fuels. The rejected pairs are machines the "
            "framework does not name in that statement.",
    ),
    dict(
        q="Which fossil fuels does the course framework specify when it describes the energy "
          "made usable by new machines?",
        choices=[
            "Coal and oil",
            "Peat and charcoal",
            "Natural gas and uranium",
            "Timber and whale oil",
            "Coke and hydrogen"],
        ans=0,
        why="KC-5.1.I.B says resources of energy stored in fossil fuels, specifically coal and "
            "oil. The word specifically is the framework's own, which is why the pair is keyed "
            "and no other fuel on the list is.",
    ),
    dict(
        q="What does the course framework say the fossil fuels revolution did?",
        choices=[
            "It greatly increased the energy available to human societies",
            "It reduced the energy available to human societies",
            "It left the energy available to human societies unchanged",
            "It replaced human labor with animal labor",
            "It ended the use of coal in industrial production"],
        ans=0,
        why="KC-5.1.I.B closes with that sentence: the fossil fuels revolution greatly increased "
            "the energy available to human societies. The framework's verb is increased, and "
            "greatly is its own adverb.",
    ),
    dict(
        q="The course framework names four kinds of production in which the second industrial "
          "revolution led to new methods. Which set names all four?",
        choices=[
            "Steel, chemicals, electricity, and precision machinery",
            "Coal, iron, timber, and canals",
            "Cotton, wool, linen, and silk",
            "Railroads, steamships, telegraphs, and canals",
            "Banking, insurance, shipping, and warehousing"],
        ans=0,
        why="KC-5.1.I.E names exactly those four: the second industrial revolution led to new "
            "methods in the production of steel, chemicals, electricity, and precision "
            "machinery. The rejected sets belong to KC-5.1.I.A, KC-5.1.IV and KC-5.1.III.B.",
    ),
    dict(
        q="When does the course framework place the new methods of the second industrial "
          "revolution?",
        choices=[
            "During the second half of the 19th century",
            "During the first half of the 18th century",
            "During the second half of the 20th century",
            "Before the development of the steam engine",
            "After the end of the period covered by this unit"],
        ans=0,
        why="KC-5.1.I.E prints the timing itself: during the second half of the 19th century. "
            "This is one of the few dates the framework fixes in this unit, which is why it can "
            "be keyed at all.",
    ),
    dict(
        q="Which three developments does the course framework group together as making "
          "exploration, development and communication possible in interior regions globally?",
        choices=[
            "Railroads, steamships, and the telegraph",
            "Steel, chemicals, and electricity",
            "Canals, turnpikes, and postal roads",
            "The steam engine, the internal combustion engine, and precision machinery",
            "Stock markets, limited liability, and transnational banking"],
        ans=0,
        why="KC-5.1.IV names the three together: railroads, steamships, and the telegraph made "
            "exploration, development, and communication possible in interior regions globally. "
            "The rejected sets are drawn from KC-5.1.I.E, KC-5.1.I.B and KC-5.1.III.B.",
    ),
    dict(
        q="According to the course framework, what did railroads, steamships and the telegraph "
          "make possible in interior regions globally?",
        choices=[
            "Exploration, development, and communication",
            "The abolition of slavery and serfdom",
            "The organization of labor unions",
            "The unification of fragmented regions into nation-states",
            "The reform of the Ottoman and Qing militaries"],
        ans=0,
        why="KC-5.1.IV states that these three made exploration, development, and communication "
            "possible in interior regions globally. The rejected options name developments the "
            "framework attaches to KC-5.3.I.C, KC-5.1.V.A, KC-5.3.II.iii and KC-5.1.V.B.",
    ),
    dict(
        q="According to the course framework, what followed from railroads, steamships and the "
          "telegraph reaching interior regions?",
        choices=[
            "Increased trade and migration",
            "A decline in long distance trade",
            "The end of migration between continents",
            "A fall in the energy available to human societies",
            "The abandonment of coal in favor of water power"],
        ans=0,
        why="KC-5.1.IV closes with the consequence: which led to increased trade and migration. "
            "The framework puts the three technologies first and the increase second, and the "
            "rejected options reverse or contradict that outcome.",
    ),
    dict(
        q="The table below reports hypothetical figures across four decades of one industrial "
          "region. Which conclusion does the table support?",
        table=_T_ENERGY,
        choices=[
            "Coal consumption and the energy available per person both rise in every decade shown",
            "Coal consumption rises while the energy available per person falls",
            "The energy available per person rises while coal consumption falls",
            "Both figures fall across the four decades",
            "Neither figure changes across the four decades"],
        ans=0,
        why="KC-5.1.I.B states that the fossil fuels revolution greatly increased the energy "
            "available to human societies, and the table shows coal use and available energy "
            "moving upward together. Both columns are read from the table itself rather than "
            "recalled.",
    ),
    dict(
        q="The table below sorts five developments by where the course framework names each "
          "one. Which development does the framework NOT place among the new methods of the "
          "second industrial revolution?",
        table=_T_METHODS,
        choices=[
            "The steam engine",
            "Steel",
            "Chemicals",
            "Electricity",
            "Precision machinery"],
        ans=0,
        why="KC-5.1.I.E lists steel, chemicals, electricity, and precision machinery as the "
            "second industrial revolution's new methods, while KC-5.1.I.B names the steam engine "
            "among the machines that made fossil fuel energy usable. The two statements are "
            "separate, and the table records which is which.",
    ),
    dict(
        q="A student writes that the discovery of coal and oil produced the steam engine and the "
          "internal combustion engine. How does the course framework order the two?",
        choices=[
            "The development of machines made it possible to take advantage of the energy stored in fossil fuels",
            "The discovery of fossil fuels made it possible to develop the machines that followed",
            "The framework treats the machines and the fuels as unconnected",
            "The framework denies that fossil fuels were used in industrial production",
            "The framework places both after the second industrial revolution"],
        ans=0,
        why="KC-5.1.I.B runs in one direction: the development of machines, including steam "
            "engines and the internal combustion engine, MADE IT POSSIBLE to take advantage of "
            "resources of energy stored in fossil fuels. The reasoning process for this topic is "
            "causation, so the order of that sentence is the answer.",
    ),
    dict(
        q="The course framework describes the machines of this period as making usable both "
          "existing and newly discovered energy resources. What does the pairing of those two "
          "words add?",
        choices=[
            "That already known deposits and newly found ones were both brought into use",
            "That only deposits discovered after the machines were built could be used",
            "That only deposits already known before the machines were built could be used",
            "That no new deposits were found during the period",
            "That the machines drew their energy from sources other than fossil fuels"],
        ans=0,
        why="KC-5.1.I.B says both existing AND vast newly discovered resources of energy stored "
            "in fossil fuels. The framework covers deposits of both kinds, which is what makes "
            "the increase it then describes so large.",
    ),
    dict(
        q="This topic's learning objective concerns technology and economic production. Which "
          "question is best matched to it?",
        choices=[
            "How new machines and new methods changed the way goods were produced over time",
            "How reform movements contributed to the expansion of rights",
            "How governments harnessed a sense of commonality to foster unity",
            "How Enlightenment philosophers reexamined the role of religion in public life",
            "How rapid urbanization produced housing shortages and public health crises"],
        ans=0,
        why="Unit 5 Learning Objective F asks students to explain how technology shaped economic "
            "production over time. The rejected questions belong to the objectives behind "
            "KC-5.3.I.C, KC-5.3.II.ii, KC-5.3.I.A and KC-5.1.VI.C.",
    ),
    dict(
        q="An illustrative account describes a works that abandoned a water wheel for an engine "
          "burning coal, and thereafter ran through frost and drought alike. Which framework "
          "statement does the account illustrate?",
        choices=[
            "That machines made it possible to take advantage of energy stored in fossil fuels",
            "That the second industrial revolution produced new methods in chemicals",
            "That railroads and steamships opened interior regions to trade",
            "That the factory system increased the specialization of labor",
            "That western European states adopted free trade policies"],
        ans=0,
        why="KC-5.1.I.B describes the development of machines making it possible to take "
            "advantage of the energy stored in fossil fuels, specifically coal and oil. An "
            "engine burning coal in place of a water wheel is that substitution, and the "
            "rejected options are framework statements about other developments.",
    ),
    dict(
        q="An illustrative report describes a new plant producing dyes and fertilizers by "
          "processes unknown a generation earlier. Which framework statement does the plant "
          "belong to?",
        choices=[
            "The new methods in chemical production brought by the second industrial revolution",
            "The development of the steam engine and the internal combustion engine",
            "The opening of interior regions by railroads and the telegraph",
            "The concentration of production in the factory system",
            "The proliferation of large scale transnational businesses"],
        ans=0,
        why="KC-5.1.I.E names chemicals among the four kinds of production in which the second "
            "industrial revolution led to new methods. The rejected options are KC-5.1.I.B, "
            "KC-5.1.IV, KC-5.1.I.C and KC-5.1.III.B, none of which covers chemical manufacture.",
    ),
    dict(
        q="An illustrative notice announces that a town's workshops and streets will be lit and "
          "driven from a central generating station. Which framework statement does the notice "
          "belong to?",
        choices=[
            "The new methods in the production of electricity brought by the second industrial revolution",
            "The fossil fuels revolution described in the framework's account of machines",
            "The opening of interior regions by railroads, steamships and the telegraph",
            "The development of the factory system and the specialization of labor",
            "The abandonment of mercantilism for free trade policies"],
        ans=0,
        why="KC-5.1.I.E names electricity among the four kinds of production transformed by the "
            "second industrial revolution during the second half of the 19th century. The "
            "rejected options are other framework statements that do not mention electricity.",
    ),
    dict(
        q="An illustrative catalogue advertises interchangeable parts cut to tolerances finer "
          "than any hand could judge. Which of the second industrial revolution's four new "
          "methods does the catalogue represent?",
        choices=[
            "Precision machinery",
            "Steel",
            "Chemicals",
            "Electricity",
            "Steam power"],
        ans=0,
        why="KC-5.1.I.E names precision machinery as one of the four kinds of production in "
            "which the second industrial revolution brought new methods. Steam power is named "
            "in KC-5.1.I.B instead, among the machines that made fossil fuel energy usable.",
    ),
    dict(
        q="An illustrative account describes a line of rail pushed into a river basin far from "
          "any coast, followed within a few years by traders, settlers and a wire carrying "
          "messages. Which framework statement does the account illustrate most completely?",
        choices=[
            "That railroads and the telegraph opened interior regions and led to increased trade and migration",
            "That the second industrial revolution produced new methods in steel and chemicals",
            "That machines made the energy stored in coal and oil available to societies",
            "That the factory system concentrated production in a single location",
            "That reform movements contributed to the expansion of rights"],
        ans=0,
        why="KC-5.1.IV joins both halves: railroads, steamships, and the telegraph made "
            "exploration, development, and communication possible in interior regions globally, "
            "which led to increased trade and migration. The account shows the opening and the "
            "traffic that followed it.",
    ),
    dict(
        q="A historian argues that increased trade and migration produced the railroads, "
          "steamships and telegraph lines of this period. How does the course framework order "
          "those developments?",
        choices=[
            "The railroads, steamships and telegraph came first and led to increased trade and migration",
            "Increased trade and migration came first and led to the railroads, steamships and telegraph",
            "The framework treats the technologies and the traffic as unrelated",
            "The framework denies that trade increased during the period",
            "The framework places both before the development of the steam engine"],
        ans=0,
        why="KC-5.1.IV puts the three technologies first and the traffic second: they made "
            "exploration, development, and communication possible in interior regions globally, "
            "WHICH LED TO increased trade and migration. The anchor carries both clauses because "
            "the distractor exchanges them.",
    ),
    dict(
        q="Which statement best explains why the course framework treats the fossil fuels "
          "revolution as significant for economic production?",
        choices=[
            "It greatly increased the energy available to human societies, which powered production",
            "It reduced the number of goods that could be produced anywhere",
            "It replaced machinery with hand labor in most industries",
            "It confined production to regions with flowing water",
            "It ended the need for any source of power in manufacturing"],
        ans=0,
        why="KC-5.1.I.B states that the fossil fuels revolution greatly increased the energy "
            "available to human societies, and Unit 5 Learning Objective F asks how technology "
            "shaped economic production. More available energy is what connects the two.",
    ),
    dict(
        q="An illustrative comparison sets a sailing packet against a steamship on the same "
          "route. Which framework statement does the comparison bear on most directly?",
        choices=[
            "That steamships helped open interior regions and increase trade and migration",
            "That steamships were among the new methods of the second industrial revolution",
            "That steamships ended the use of coal in transport",
            "That steamships were unrelated to the movement of people",
            "That the framework treats sea transport as outside its account of technology"],
        ans=0,
        why="KC-5.1.IV names steamships alongside railroads and the telegraph as making "
            "exploration, development, and communication possible in interior regions globally, "
            "which led to increased trade and migration. KC-5.1.I.E's four new methods are steel, "
            "chemicals, electricity and precision machinery, and steamships are not among them.",
    ),
    dict(
        q="Which of the following best distinguishes the two industrial phases the course "
          "framework names?",
        choices=[
            "The first turned on steam power and coal, the second on steel, chemicals, electricity and precision machinery",
            "The first turned on steel and electricity, the second on steam power and coal",
            "The two phases are described by the framework as identical in content",
            "The first is dated to the 20th century and the second to the 18th",
            "The framework names only one industrial revolution in this unit"],
        ans=0,
        why="KC-5.1.II.B names steam-powered industrial production during the first Industrial "
            "Revolution, and KC-5.1.I.E names steel, chemicals, electricity and precision "
            "machinery as the second industrial revolution's new methods. The anchor carries "
            "both phases because a distractor exchanges their contents.",
    ),
    dict(
        q="An illustrative works replaces wrought iron rails with rails of a harder metal made "
          "by a new process, and finds they last several times as long. Which of the second "
          "industrial revolution's new methods does the works illustrate?",
        choices=[
            "Steel",
            "Chemicals",
            "Electricity",
            "Precision machinery",
            "Internal combustion"],
        ans=0,
        why="KC-5.1.I.E names steel first among the four kinds of production in which the second "
            "industrial revolution brought new methods. Internal combustion belongs to "
            "KC-5.1.I.B's machines rather than to that list.",
    ),
    dict(
        q="A student writes that the second industrial revolution came before the machines that "
          "made fossil fuel energy usable. Which correction does the course framework support?",
        choices=[
            "The framework dates the second industrial revolution to the second half of the 19th century, after the machines that opened fossil fuel energy",
            "The framework dates the second industrial revolution to the first half of the 18th century, before those machines",
            "The framework gives the second industrial revolution no date at all",
            "The framework treats the two developments as the same thing",
            "The framework places the second industrial revolution outside this unit"],
        ans=0,
        why="KC-5.1.I.E places the second industrial revolution during the second half of the "
            "19th century, and KC-5.1.I.B describes the machines that made fossil fuel energy "
            "usable as part of the industrial growth this unit opens with. The anchor carries "
            "both the date and the order because a distractor reverses them.",
    ),
    dict(
        q="An illustrative message reaches a coastal office from a station a thousand miles "
          "inland on the day it was sent. Which framework statement does the message illustrate?",
        choices=[
            "That the telegraph made communication possible in interior regions globally",
            "That steamships carried goods between continents",
            "That railroads carried settlers into river basins",
            "That new methods in chemical production appeared in this period",
            "That the factory system concentrated production in one location"],
        ans=0,
        why="KC-5.1.IV names the telegraph among the three developments that made exploration, "
            "development, and communication possible in interior regions globally. Speed of "
            "message rather than movement of goods or people is the telegraph's part of that "
            "sentence.",
    ),
    dict(
        q="Using the reasoning process assigned to this topic, causation, which evidence would "
          "best support the claim that a new technology changed production in a district?",
        choices=[
            "Records of how goods were made in the district before and after the technology arrived",
            "A list of the patents registered anywhere in the world that year",
            "The names of the district's leading families",
            "A map of the district's parish boundaries",
            "The number of newspapers printed in the district's capital"],
        ans=0,
        why="Unit 5 Learning Objective F asks how technology shaped economic production over "
            "time, and KC-5.1.I.B and KC-5.1.I.E both describe technologies changing how things "
            "were made. A before and after record of production is what bears on that claim; the "
            "rejected options do not touch production at all.",
    ),
    dict(
        q="Which statement about the framework's account of the telegraph is accurate?",
        choices=[
            "It is grouped with railroads and steamships as opening interior regions",
            "It is named among the four new methods of the second industrial revolution",
            "It is named among the machines that made fossil fuel energy usable",
            "It is named as a cause of the factory system",
            "It is not named anywhere in the framework's account of this period"],
        ans=0,
        why="KC-5.1.IV groups railroads, steamships, and the telegraph together as making "
            "exploration, development, and communication possible in interior regions globally. "
            "KC-5.1.I.E's four methods are steel, chemicals, electricity and precision machinery, "
            "and KC-5.1.I.B's machines are the steam and internal combustion engines.",
    ),
    dict(
        q="An illustrative shipping list shows the same port handling several times the tonnage "
          "it handled a generation earlier, with new inland towns named among the origins of the "
          "cargo. Which framework statement does the list support?",
        choices=[
            "That the opening of interior regions led to increased trade",
            "That the second industrial revolution produced new methods in steel",
            "That machines made the energy stored in coal and oil usable",
            "That workers organized in labor unions to raise wages",
            "That governments promoted state sponsored visions of industrialization"],
        ans=0,
        why="KC-5.1.IV states that railroads, steamships, and the telegraph made exploration, "
            "development, and communication possible in interior regions globally, which led to "
            "increased trade and migration. Cargo arriving from newly named inland towns is that "
            "consequence in a port's own records.",
    ),
    dict(
        q="Which of the following claims goes beyond what the course framework states about the "
          "technologies of this period?",
        choices=[
            "That a single named inventor was responsible for the fossil fuels revolution",
            "That machines including steam engines made fossil fuel energy usable",
            "That the second industrial revolution brought new methods in steel and chemicals",
            "That railroads, steamships and the telegraph opened interior regions",
            "That the energy available to human societies greatly increased"],
        ans=0,
        why="KC-5.1.I.B, KC-5.1.I.E and KC-5.1.IV state the other four claims and name no "
            "inventor anywhere among them. Attributing the fossil fuels revolution to one person "
            "supplies a fact the CED does not print, which is what HISTORY_BRIEF.md forbids.",
    ),
    dict(
        q="Which single statement best summarizes what this topic asks students to understand "
          "about technology in the industrial age?",
        choices=[
            "New machines unlocked fossil fuel energy, later methods transformed further industries, and new transport and communication opened interior regions",
            "A single machine transformed every industry at once and nothing followed it",
            "Technology in this period left the energy available to societies unchanged",
            "The technologies of the period reached only the coasts and never the interior",
            "The framework treats technology as unrelated to economic production"],
        ans=0,
        why="The summary joins KC-5.1.I.B's machines and fossil fuels, KC-5.1.I.E's second "
            "industrial revolution, and KC-5.1.IV's railroads, steamships and telegraph. Each "
            "rejected option contradicts one of those three statements.",
    ),
]
