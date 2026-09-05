# AP WORLD HISTORY: MODERN 9.1 Advances in Technology and Exchange After 1900
# CED effective Fall 2026 (Course Framework V.1), Unit 9 Globalization,
# c. 1900 to the present. Thematic focus: Technology and Innovation (TEC).
# Reasoning process: Continuity and Change.
#
# TITLE. WORLD_HISTORY_topics.json gives this topic as "Advances in Technology
# and Exchange After 1900", and that is what is used here. The CED prints the
# title across three lines beside the skill statement, so a shorter form can be
# reconstructed from the text dump by mistake; the JSON is the authority per the
# authoring brief and it matches the CED page read in full.
#
# Learning Objective: Unit 9 Learning Objective A -- explain how the development
# of new technologies changed the world from 1900 to present. Suggested skill
# 5.A, identify patterns among or connections between historical developments
# and processes. That skill is the shape of this bank: a large share of the items
# ask what several of these technologies have in common, or which connection the
# framework draws between one development and another, rather than asking for a
# definition.
#
# HISTORICAL DEVELOPMENTS this topic prints -- five sentences, and the only
# sentences the keys below rest on:
#   KC-6.1.I.A    New modes of communication -- including radio communication,
#                 cellular communication, and the internet -- as well as
#                 transportation, including air travel and shipping containers,
#                 reduced the problem of geographic distance.
#   KC-6.1.I.D    Energy technologies, including the use of petroleum and nuclear
#                 power, raised productivity and increased the production of
#                 material goods.
#   KC-6.1.III.B  More effective forms of birth control gave women greater
#                 control over fertility, transformed reproductive practices, and
#                 contributed to declining rates of fertility in much of the
#                 world.
#   KC-6.1.I.B    The Green Revolution and commercial agriculture increased
#                 productivity and sustained the earth's growing population as it
#                 spread chemically and genetically modified forms of
#                 agriculture.
#   KC-6.1.I.C    Medical innovations, including vaccines and antibiotics,
#                 increased the ability of humans to survive and live longer
#                 lives.
# The CED prints NO illustrative examples on this page, so no item here turns on
# any, and none is invented to fill the space. The named technologies above --
# radio, cellular communication, the internet, air travel, shipping containers,
# petroleum, nuclear power, vaccines, antibiotics -- are inside the key concepts
# themselves and are therefore required content rather than optional examples.
#
# THE QUALIFIERS ARE LOAD-BEARING. KC-6.1.III.B says declining fertility IN MUCH
# OF THE WORLD, not everywhere. KC-6.1.I.B says the Green Revolution sustained
# the growing population AS IT SPREAD chemically and genetically modified forms
# of agriculture, so the sentence carries a consequence alongside the benefit and
# a bank that reported only one half would not be reporting the sentence. Items
# 14, 18, 22 and 27 hold those open.
#
# CONTESTED GROUND. Birth control and genetically modified agriculture are
# subjects on which people disagree today. Every key here is limited to what the
# framework's descriptive sentences state and NONE endorses, condemns or
# recommends any of these technologies. Where a question involves a source
# arguing for or against one of them, it asks what the source claims or what
# would test the claim, never whether the source is right.
#
# DEDUPE NOTE. Topic 9.2 takes up disease, including the diseases that persisted
# and the ones that emerged; 9.3 takes up the environmental debates; 9.9 is the
# unit's reasoning topic and reviews these same five sentences as ARGUMENTATION
# rather than as content. This module stays on what the technologies were and
# what the framework says each of them changed. Medical innovation appears here
# under KC-6.1.I.C, longer life and survival, and is left to 9.2 wherever the
# question is about disease itself.
#
# SOURCES. Section I is stimulus-based and this bank cannot display an image, so
# every stimulus is TEXT and none is attributed to a real person or document.
# TABLES are hypothetical, each states a whole and its parts, and every keyed
# conclusion is recomputed from the table alone. DATES are written "1950 to
# 1990", never with a hyphen; the CED states that events and processes are not
# constrained by its given dates, so no key here depends on a boundary year.
#
# FIVE choices (A-E) per HISTORY_BRIEF.md; the real Section I prints four.
TOPIC = ("9.1", "Advances in Technology and Exchange After 1900", 9)

_T_FREIGHT = dict(
    headers=["Period (hypothetical record of long-distance consignments)",
             "Consignments recorded",
             "Of those, carried by container ship or by air",
             "Of those, carried by other means"],
    rows=[["1950s", "120", "14", "106"],
          ["1970s", "260", "120", "140"],
          ["1990s", "480", "372", "108"]])

_T_ENERGY = dict(
    headers=["Period (hypothetical energy index, first period = 100)",
             "Total energy consumed",
             "Of that, from petroleum and nuclear sources",
             "Of that, from other sources"],
    rows=[["1920s", "100", "25", "75"],
          ["1950s", "180", "80", "100"],
          ["1980s", "320", "190", "130"]])

_T_FERTILITY = dict(
    headers=["Period (hypothetical survey of women of childbearing age, thousands)",
             "Women surveyed",
             "Of those, reporting use of a modern method of birth control",
             "Of those, not reporting such use"],
    rows=[["1960s", "500", "75", "425"],
          ["1970s", "520", "182", "338"],
          ["1980s", "540", "324", "216"]])

QUESTIONS = [

 dict(q="A shipping company's handbook of 1975 explains that goods packed once at the factory can now travel by sea and by road to a buyer overseas without being unpacked, and that a message confirming their arrival reaches the seller the same day. The handbook describes developments this course groups together because they",
   choices=[
     "reduced the problem of geographic distance",
     "raised the productivity of agriculture in the regions they reached",
     "increased the ability of humans to survive and live longer lives",
     "gave women greater control over fertility",
     "contributed to debates about the nature and causes of climate change"],
   ans=0,
   why="KC-6.1.I.A states that new modes of communication, including radio communication, cellular communication, and the internet, as well as transportation, including air travel and shipping containers, reduced the problem of geographic distance. A container moving unopened across an ocean and a message arriving the same day are the transport and communication halves of that one sentence, which is why the framework groups them."),

 dict(q="Which modes of communication does this course name as having reduced the problem of geographic distance?",
   choices=[
     "Radio communication, cellular communication, and the internet",
     "Printed newspapers, the postal service, and the telegraph",
     "Shipping containers, air travel, and railways",
     "Vaccines, antibiotics, and modern methods of birth control",
     "Petroleum, nuclear power, and commercial agriculture"],
   ans=0,
   why="KC-6.1.I.A names radio communication, cellular communication, and the internet as the new modes of communication that, together with transportation, reduced the problem of geographic distance. Shipping containers and air travel appear in that sentence as transportation rather than communication, and the remaining lists belong to KC-6.1.I.C, KC-6.1.III.B, KC-6.1.I.D and KC-6.1.I.B."),

 dict(q="A hypothetical engineering report of 1962 argues that a new power station will allow the district's factories to run more shifts and to produce a far larger quantity of goods each year. The report describes a development this course places under",
   choices=[
     "energy technologies raising productivity and increasing the production of material goods",
     "new modes of communication reducing the problem of geographic distance",
     "medical innovations increasing the ability of humans to live longer lives",
     "the Green Revolution sustaining the earth's growing population",
     "more effective forms of birth control transforming reproductive practices"],
   ans=0,
   why="KC-6.1.I.D states that energy technologies, including the use of petroleum and nuclear power, raised productivity and increased the production of material goods. A power station letting factories run longer and produce more is both halves of that sentence, the productivity and the output."),

 dict(q="A hypothetical record divides the consignments of each period into two groups. Which conclusion does the table alone support?",
   table=_T_FREIGHT,
   choices=[
     "The number of consignments rose in each period, and the share carried by container ship or by air rose with it",
     "The number of consignments fell in each period after the first one recorded",
     "The share carried by container ship or by air fell across the record",
     "No consignment recorded in the 1950s was carried by container ship or by air",
     "Consignments carried by other means rose in each period recorded"],
   ans=0,
   why="KC-6.1.I.A names shipping containers and air travel among the transportation developments that reduced the problem of geographic distance, and a rising share of freight moving by those means is one form that reduction takes. The record is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="A public health bulletin of 1958 reports that a disease which had killed many children in the district now appears only rarely, following a programme of inoculation, and that a class of medicines introduced after the war has made once-fatal infections routinely survivable. According to this course, these developments belong to",
   choices=[
     "medical innovations, including vaccines and antibiotics, that increased the ability of humans to survive and live longer lives",
     "energy technologies that raised productivity and increased the production of material goods",
     "new modes of transportation that reduced the problem of geographic distance",
     "commercial agriculture that sustained the earth's growing population",
     "more effective forms of birth control that transformed reproductive practices"],
   ans=0,
   why="KC-6.1.I.C states that medical innovations, including vaccines and antibiotics, increased the ability of humans to survive and live longer lives. Inoculation against a childhood disease and a postwar class of medicines making infections survivable are the two innovations that sentence names."),

 dict(q="An agricultural extension pamphlet of 1968 announces new seed varieties, together with the fertilizers and pesticides they require, and promises a far larger harvest from the same land. This course describes the process the pamphlet belongs to as one that",
   choices=[
     "increased productivity and sustained the earth's growing population as it spread chemically modified forms of agriculture",
     "reduced productivity while limiting the growth of the earth's population",
     "raised the production of material goods by introducing new energy technologies",
     "reduced the problem of geographic distance by improving transportation",
     "increased the ability of humans to survive by introducing vaccines and antibiotics"],
   ans=0,
   why="KC-6.1.I.B states that the Green Revolution and commercial agriculture increased productivity and sustained the earth's growing population as it spread chemically and genetically modified forms of agriculture. The framework's sentence carries the yield and the spread of modified agriculture together, so the key states both rather than reporting one half of it."),

 dict(q="Which pattern connects the developments this topic gathers under new technologies after 1900?",
   choices=[
     "Each changed something about how far, how much, how long or how many people could live and produce",
     "Each was confined to a single country and had no effect beyond its borders",
     "Each was introduced before 1900 and unchanged during the twentieth century",
     "Each concerned the organization of governments rather than the conditions of life",
     "Each reduced the total quantity of goods available to the world's population"],
   ans=0,
   why="KC-6.1.I.A reduces the problem of distance, KC-6.1.I.D raises productivity and output, KC-6.1.I.C lengthens life, KC-6.1.I.B sustains a growing population and KC-6.1.III.B alters fertility. Skill 5.A asks a student to identify patterns among or connections between developments, and the common effect on distance, quantity, duration and population is that pattern."),

 dict(q="A hypothetical index divides the energy consumed in each period into two parts. Which conclusion does the table alone support?",
   table=_T_ENERGY,
   choices=[
     "Total energy consumed rose in each period, and the portion from petroleum and nuclear sources rose as a share of the total",
     "Total energy consumed fell in each period after the first one recorded",
     "The portion from petroleum and nuclear sources fell as a share of the total",
     "Energy from other sources fell in each period recorded",
     "Petroleum and nuclear sources supplied more than half of the total in every period recorded"],
   ans=0,
   why="KC-6.1.I.D states that energy technologies, including the use of petroleum and nuclear power, raised productivity and increased the production of material goods, and a rising share of a rising total is one form the growth of those technologies takes. The index is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="A demographic study of the 1980s reports that in the districts it covers women are having fewer children than their mothers did and that they describe the timing of births as something they now decide. According to this course, this pattern is associated with",
   choices=[
     "more effective forms of birth control, which gave women greater control over fertility and contributed to declining rates of fertility",
     "medical innovations such as vaccines and antibiotics, which lengthened lives",
     "energy technologies, which raised productivity and the output of goods",
     "shipping containers and air travel, which reduced the problem of distance",
     "the Green Revolution, which increased agricultural productivity"],
   ans=0,
   why="KC-6.1.III.B states that more effective forms of birth control gave women greater control over fertility, transformed reproductive practices, and contributed to declining rates of fertility in much of the world. Fewer births and decisions about their timing are the control and the decline that sentence names together."),

 dict(q="An airline's timetable of 1969 advertises a journey that had taken weeks by sea as a matter of hours. The change the timetable records is one this course places alongside",
   choices=[
     "the spread of new modes of communication, as part of the reduction of the problem of geographic distance",
     "the introduction of vaccines and antibiotics, as part of the lengthening of human life",
     "the adoption of new seed varieties, as part of the growth of agricultural productivity",
     "the use of petroleum and nuclear power, as part of the growth of material output",
     "the adoption of modern methods of birth control, as part of the change in reproductive practices"],
   ans=0,
   why="KC-6.1.I.A puts new modes of communication and new modes of transportation, air travel among them, in a single sentence whose effect is the reduction of the problem of geographic distance. Skill 5.A asks a student to identify connections between developments, and the framework's own sentence is what places these two side by side."),

 dict(q="Which statement about the technologies described in this topic is NOT supported by this course?",
   choices=[
     "The new energy technologies of the century reduced the production of material goods",
     "New modes of communication and transportation reduced the problem of geographic distance",
     "Medical innovations increased the ability of humans to survive and live longer lives",
     "The Green Revolution and commercial agriculture increased productivity",
     "More effective forms of birth control transformed reproductive practices"],
   ans=0,
   why="KC-6.1.I.D states that energy technologies, including the use of petroleum and nuclear power, raised productivity and INCREASED the production of material goods, so a reduction in that output reverses the framework's sentence. The other four restate KC-6.1.I.A, KC-6.1.I.C, KC-6.1.I.B and KC-6.1.III.B."),

 dict(q="A hypothetical survey divides the women it records in each period into two groups. Which conclusion does the table alone support?",
   table=_T_FERTILITY,
   choices=[
     "The share reporting use of a modern method rose in each period, and in the last period recorded it was a majority",
     "The share reporting use of a modern method fell across the record",
     "No woman surveyed in the 1960s reported use of a modern method",
     "The share reporting such use was a majority in every period recorded",
     "The number of women surveyed fell in each period after the first one recorded"],
   ans=0,
   why="KC-6.1.III.B states that more effective forms of birth control gave women greater control over fertility and contributed to declining rates of fertility in much of the world, and a rising share reporting use is one measure of that spread. The survey is hypothetical and the keyed conclusion, with the falsity of each distractor, is recomputed from the table alone in the verifier."),

 dict(q="Two developments of the twentieth century are set side by side: the spread of vaccines and antibiotics, and the spread of new seed varieties and commercial agriculture. What connection does this course draw between them?",
   choices=[
     "The first lengthened lives and the second sustained the growing population that resulted",
     "The first lengthened lives and the second reduced the world's population",
     "Both reduced the problem of geographic distance for the regions they reached",
     "Both raised the production of material goods by supplying new energy sources",
     "Neither is treated by the framework as bearing on population at all"],
   ans=0,
   why="KC-6.1.I.C states that medical innovations increased the ability of humans to survive and live longer lives, and KC-6.1.I.B that the Green Revolution and commercial agriculture sustained the earth's GROWING population. Skill 5.A asks for connections between developments, and the framework's two sentences fit together as the lengthening of life and the feeding of the people whose lives were lengthened."),

 dict(q="A student writes that this course says birth control caused fertility to fall everywhere in the world. What is the best correction?",
   choices=[
     "The framework says it contributed to declining rates of fertility in much of the world, not in all of it",
     "The framework says it had no effect on rates of fertility anywhere",
     "The framework says rates of fertility rose wherever birth control spread",
     "The framework says fertility fell everywhere but for reasons unconnected with birth control",
     "The framework says birth control was available only after the year 2000"],
   ans=0,
   why="KC-6.1.III.B states that more effective forms of birth control contributed to declining rates of fertility IN MUCH OF THE WORLD. Two qualifiers are the framework's own, contributed rather than caused and much of the world rather than all of it, and the correction has to keep both rather than replace one overstatement with another."),

 dict(q="A trade journal of 1990 reports that a design office in one country can now send a complete set of drawings to a factory on another continent within minutes, and that the finished goods can be shipped back in standard steel boxes. The two halves of this arrangement illustrate",
   choices=[
     "communication and transportation working together to reduce the problem of geographic distance",
     "energy technologies working together to raise the production of material goods",
     "medical innovations working together to extend the human lifespan",
     "agricultural innovations working together to sustain a growing population",
     "reproductive technologies working together to transform reproductive practices"],
   ans=0,
   why="KC-6.1.I.A names new modes of communication and new modes of transportation, including shipping containers, in one sentence whose stated effect is the reduction of the problem of geographic distance. Drawings sent in minutes and goods returned in standard boxes are the two halves of that sentence in a single commercial arrangement."),

 dict(q="Which pairing correctly matches a technology this course names to the change the framework attributes to it?",
   choices=[
     "Antibiotics, matched with an increased ability of humans to survive and live longer lives",
     "Antibiotics, matched with a reduction in the problem of geographic distance",
     "Shipping containers, matched with declining rates of fertility",
     "Nuclear power, matched with the transformation of reproductive practices",
     "The internet, matched with an increase in the productivity of agriculture"],
   ans=0,
   why="KC-6.1.I.C names vaccines and antibiotics as the medical innovations that increased the ability of humans to survive and live longer lives. Each distractor takes a technology the framework names in one sentence and attaches it to the effect stated in a different one, which is the error a pattern-matching item is built to catch."),

 dict(q="An unattributed newspaper column of 1972 argues that the new agricultural methods should be judged by their yields alone. According to this course, what else does the same development involve?",
   choices=[
     "The spread of chemically and genetically modified forms of agriculture",
     "The reduction of the world's population through falling birth rates",
     "The replacement of petroleum and nuclear power as sources of energy",
     "The introduction of vaccines and antibiotics into rural districts",
     "The reduction of the problem of geographic distance for farm produce"],
   ans=0,
   why="KC-6.1.I.B states that the Green Revolution and commercial agriculture increased productivity and sustained the earth's growing population AS IT SPREAD chemically and genetically modified forms of agriculture. The framework reports the spread of modified agriculture in the same sentence as the yields, so an account confined to yields leaves out half of what it says. The key states what the framework states and takes no position on whether the methods are good or bad."),

 dict(q="According to this course, what did more effective forms of birth control change, beyond rates of fertility?",
   choices=[
     "They gave women greater control over fertility and transformed reproductive practices",
     "They raised the productivity of agriculture and of industry alike",
     "They reduced the problem of geographic distance between regions",
     "They increased the production of material goods in industrial economies",
     "They introduced new sources of energy into domestic use"],
   ans=0,
   why="KC-6.1.III.B states that more effective forms of birth control gave women greater control over fertility, transformed reproductive practices, and contributed to declining rates of fertility in much of the world. The sentence names three changes and the question asks for the two beyond the rate itself, which is what the key supplies."),

 dict(q="A historian argues that the twentieth century's technologies mattered chiefly because of how they changed the scale on which people could act. Which set of evidence from this course best supports that reading?",
   choices=[
     "Distance made less of an obstacle, output raised, harvests enlarged, and lives lengthened",
     "Governments reorganized, frontiers redrawn, and empires dissolved",
     "New military alliances formed and nuclear weapons proliferated",
     "Consumer culture globalized and popular entertainment spread across borders",
     "Movements protested the inequality of the consequences of global integration"],
   ans=0,
   why="KC-6.1.I.A, KC-6.1.I.D, KC-6.1.I.B and KC-6.1.I.C between them record a reduced problem of distance, raised productivity and output, a sustained growing population and longer lives. Skill 5.A asks a student to identify a pattern among developments, and the distractor sets name developments the framework places in other units and topics."),

 dict(q="An unattributed engineering lecture of 1955 claims that a single new fuel will make every other source of power obsolete within twenty years. Judged against this course's framework, the claim",
   choices=[
     "goes beyond the framework, which names petroleum and nuclear power together rather than one replacing all others",
     "matches the framework, which names one fuel as having replaced all other sources of power",
     "goes beyond the framework, which denies that energy technologies raised productivity",
     "matches the framework, which states that energy technologies had no effect on output",
     "goes beyond the framework, which places all energy technologies before 1900"],
   ans=0,
   why="KC-6.1.I.D states that energy technologies, INCLUDING the use of petroleum and nuclear power, raised productivity and increased the production of material goods. The sentence names two together inside a wider class and asserts no replacement of one by another, so a claim of universal obsolescence goes past what the framework supports."),

 dict(q="A radio manufacturer's catalogue of 1935 advertises that a listener in a rural district can hear an event as it happens in a distant capital. This course would treat the catalogue as evidence about",
   choices=[
     "a new mode of communication reducing the problem of geographic distance",
     "a new mode of transportation reducing the cost of moving goods",
     "an energy technology raising the productivity of industry",
     "a medical innovation lengthening the lives of rural populations",
     "an agricultural innovation raising the yields of rural districts"],
   ans=0,
   why="KC-6.1.I.A names radio communication first among the new modes of communication that reduced the problem of geographic distance. Hearing a distant event as it happens is that reduction in its earliest form, and the framework distinguishes communication from the transportation named in the same sentence."),

 dict(q="Which statement about the Green Revolution and commercial agriculture does this course support?",
   choices=[
     "They increased productivity and sustained a growing population while spreading modified forms of agriculture",
     "They reduced productivity and were unable to feed a growing population",
     "They increased productivity without any accompanying change in agricultural methods",
     "They were confined to the years before 1900 and had no bearing on the twentieth century",
     "They replaced agriculture entirely with the production of manufactured goods"],
   ans=0,
   why="KC-6.1.I.B states that the Green Revolution and commercial agriculture increased productivity and sustained the earth's growing population as it spread chemically and genetically modified forms of agriculture. The key carries the yield, the population and the spread of modified methods, because the framework's sentence names all three."),

 dict(q="A researcher wants to test the claim that a region's life expectancy rose because of the innovations this topic describes. Which evidence would bear most directly on the claim?",
   choices=[
     "Records of vaccination coverage and of deaths from infections treatable by antibiotics",
     "Records of the tonnage of freight moved through the region's ports",
     "Records of the region's total consumption of petroleum by decade",
     "Records of the number of radio receivers sold in the region",
     "Records of the acreage sown with new seed varieties in the region"],
   ans=0,
   why="KC-6.1.I.C states that medical innovations, INCLUDING vaccines and antibiotics, increased the ability of humans to survive and live longer lives, so vaccination coverage and deaths from treatable infections are the direct measures. The other records bear on KC-6.1.I.A, KC-6.1.I.D and KC-6.1.I.B rather than on the claim in question."),

 dict(q="Two accounts describe the same technological change: a firm's advertisement praising it and a critic's article warning against it. Which use of the pair best fits the reasoning this topic asks for?",
   choices=[
     "Use both to identify what the change actually consisted of, since each describes the same development from a different position",
     "Use the advertisement alone, since a firm knows its own product best",
     "Use the critic's article alone, since criticism is always more careful than promotion",
     "Discard both, since a technology cannot be studied through what people wrote about it",
     "Treat the two as describing unrelated developments that happen to share a name"],
   ans=0,
   why="Skill 5.A asks a student to identify patterns among or connections between historical developments, which requires establishing what the development was before any judgement of it. KC-6.1.I.B and KC-6.1.III.B describe changes about which people argued at the time and still do, and the framework's sentences describe the changes rather than settling the arguments."),

 dict(q="A logistics study of 1985 finds that the cost of moving a ton of goods between two continents has fallen far faster than the cost of producing the goods themselves. According to this course, the fall in transport cost belongs to",
   choices=[
     "the reduction of the problem of geographic distance by new modes of transportation",
     "the rise in productivity produced by new energy technologies",
     "the increase in agricultural yields produced by new seed varieties",
     "the lengthening of human life produced by medical innovation",
     "the transformation of reproductive practices produced by birth control"],
   ans=0,
   why="KC-6.1.I.A states that transportation, including air travel and shipping containers, reduced the problem of geographic distance. A cost of moving goods that falls faster than the cost of making them is that reduction stated economically, and it is distinct from the productivity gain KC-6.1.I.D attributes to energy technologies."),

 dict(q="Which of the following would this course count as a change in reproductive practices rather than simply a change in fertility rates?",
   choices=[
     "A change in when and whether people have children, decided by the women concerned",
     "A change in the total number of children born in a country in a given year",
     "A change in the number of hospitals built in a country over a decade",
     "A change in the average age at which people die in a country",
     "A change in the number of children enrolled in schools in a district"],
   ans=0,
   why="KC-6.1.III.B distinguishes three things in one sentence: greater control over fertility, transformed reproductive practices, and declining rates of fertility. A change in who decides and when is the practice, while a count of births in a year is the rate, which is why the item separates them."),

 dict(q="An unattributed policy paper of 1978 argues that a country cannot raise its industrial output without first securing new sources of power. Which of this course's statements does the paper's premise rest on?",
   choices=[
     "That energy technologies raised productivity and increased the production of material goods",
     "That new modes of communication reduced the problem of geographic distance",
     "That vaccines and antibiotics lengthened human lives",
     "That commercial agriculture sustained the earth's growing population",
     "That birth control contributed to declining rates of fertility"],
   ans=0,
   why="KC-6.1.I.D states that energy technologies, including the use of petroleum and nuclear power, raised productivity and increased the production of material goods. The paper's premise, that output depends on power, is that sentence used as an argument, and each distractor names a change the framework attributes to a different technology."),

 dict(q="Considered together, what do the five developments in this topic have in common in the way this course presents them?",
   choices=[
     "Each is a technology whose spread the framework connects to a measurable change in how people lived",
     "Each is a form of government adopted by states after 1900",
     "Each is a treaty signed between states during the twentieth century",
     "Each is a movement organized to oppose an existing power structure",
     "Each is an international organization founded to keep the peace"],
   ans=0,
   why="KC-6.1.I.A, KC-6.1.I.B, KC-6.1.I.C, KC-6.1.I.D and KC-6.1.III.B each pair a technology with a stated change: distance, yields and population, survival and longevity, productivity and output, and control over fertility. Skill 5.A asks a student to identify the pattern among developments, and technology joined to a measurable change in living is that pattern."),

 dict(q="A curriculum planner asks which single question this topic is built to answer. Which is it?",
   choices=[
     "How the development of new technologies changed the world from 1900 to the present",
     "How states responded to the economic challenges of the twentieth century",
     "How and why globalization changed culture over time",
     "How political changes led to territorial and demographic developments",
     "How globalization changed international interactions among states"],
   ans=0,
   why="Unit 9 Learning Objective A is to explain how the development of new technologies changed the world from 1900 to present, and it is the objective printed on this topic's page. The other options are the learning objectives of other topics in this course."),

 dict(q="Taking the topic as a whole, which single sentence best states what this course says about technology after 1900?",
   choices=[
     "Communication and transport shrank the obstacle of distance, new energy sources raised output, new agriculture fed a growing population while spreading modified methods, medicine lengthened life, and better birth control gave women more control over fertility",
     "Technology changed how goods were transported and had no bearing on health, food, energy or family life",
     "Technology after 1900 reduced output, shortened lives and left distance as great an obstacle as before",
     "Technology after 1900 was confined to a single field of invention and to a single region of the world",
     "Technology after 1900 changed the organization of governments but not the conditions in which people lived"],
   ans=0,
   why="KC-6.1.I.A supplies the reduction of the problem of geographic distance, KC-6.1.I.D the raised productivity and output, KC-6.1.I.B the sustained growing population and the spread of modified agriculture, KC-6.1.I.C the longer lives, and KC-6.1.III.B the greater control over fertility. The key is the conjunction of those five sentences and each distractor contradicts at least one."),
]
