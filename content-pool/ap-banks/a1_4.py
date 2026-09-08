# AP U.S. HISTORY 1.4 Columbian Exchange, Spanish Exploration, and Conquest
# (title copied from US_HISTORY_topics.json)
# Unit 1, Period 1: 1491 to 1607. Suggested skill 3.A, identify and describe a claim
# and/or argument in a text-based or non-text-based source. Reasoning process printed
# for this topic: Causation.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 1 Learning Objective D
#       Explain causes of the Columbian Exchange and its effect on Europe and the
#       Americas during the period after 1492.
#
#   KC-1.2.I.B   The Columbian Exchange brought new crops to Europe from the Americas,
#                stimulating European population growth, and new sources of mineral
#                wealth, which facilitated the European shift from feudalism to
#                capitalism.
#   KC-1.2.I.C   Improvements in maritime technology and more organized methods for
#                conducting international trade, such as joint-stock companies, helped
#                drive changes to economies in Europe and the Americas.
#   KC-1.2.II.A  Spanish exploration and conquest of the Americas were accompanied and
#                furthered by widespread deadly epidemics that devastated native
#                populations and by the introduction of crops and animals not found in
#                the Americas.
#
#   Read with its parents, which this topic page sits under:
#   KC-1.2       Contact among Europeans, Native Americans, and Africans resulted in the
#                Columbian Exchange and significant social, cultural, and political
#                changes on both sides of the Atlantic Ocean.
#   KC-1.2.II    The Columbian Exchange and development of the Spanish Empire in the
#                Western Hemisphere resulted in extensive demographic, economic, and
#                social changes.
#
#   THEMATIC FOCUS printed on this topic page, Geography and the Environment GEO:
#       Geographic and environmental factors, including competition over and debates
#       about natural resources, shape the development of America and foster regional
#       diversity. The development of America impacts the environment and reshapes
#       geography, which leads to debates about environmental and geographic issues.
#
#   Reasoning Process 2, Causation, 2.ii: Explain the relationship between causes and
#   effects of a specific historical development or process.
#
# THE THREE HEDGED VERBS, which several items exist to hold. The framework does not say
# mineral wealth CAUSED capitalism: it says the wealth FACILITATED the European shift
# from feudalism to capitalism. It does not say maritime technology and joint-stock
# companies caused economic change: it says they HELPED DRIVE it. It does not say
# epidemics followed conquest: it says exploration and conquest were ACCOMPANIED AND
# FURTHERED by them. Each verb is weaker or differently timed than the one a student
# is likely to substitute, and each is exactly the kind of near-miss HISTORY_BRIEF.md
# warns about -- right process, wrong strength of claim.
#
# WHAT IS NOT KEYED. The encomienda system, the caste system, the trade in enslaved
# Africans and the divergent worldviews of KC-1.2.III belong to topics 1.5 and 1.6.
# They appear here only as distractors. Nothing here rests on the topic page's optional
# sources, which the CED itself says no exam question requires.
#
# NO FIGURES: the bank cannot display images, so the three data items carry a table=.
# PROSE ONLY: no LaTeX; a span of years is written "1491 to 1607", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("1.4", "Columbian Exchange, Spanish Exploration, and Conquest", 1)

_T_EUROPE = dict(
    headers=["Period (illustrative, after 1492)",
             "Land under the new crop (index)",
             "Population (index)"],
    rows=[["First period", "10", "100"],
          ["Second period", "35", "118"],
          ["Third period", "70", "141"]])

_T_DIRECTION = dict(
    headers=["Item the framework names (illustrative arrangement)",
             "Which way does the framework describe it moving?"],
    rows=[["New crops that stimulated European population growth",
           "Brought to Europe from the Americas"],
          ["New sources of mineral wealth",
           "Brought to Europe from the Americas"],
          ["Crops not found in the Americas",
           "Introduced into the Americas"],
          ["Animals not found in the Americas",
           "Introduced into the Americas"]])

QUESTIONS = [

 dict(q="Unit 1's Learning Objective D asks students to explain the causes of the "
        "Columbian Exchange and its effect on which places, during which period?",
      choices=[
        "Europe and the Americas, during the period after 1492",
        "Europe alone, during the period after 1492",
        "The Americas alone, during the period before 1492",
        "West Africa and the Americas, during the period after 1607",
        "Europe and West Africa, across the whole of Period 1"],
      ans=0,
      why="Unit 1 Learning Objective D reads 'Explain causes of the Columbian Exchange and "
          "its effect on Europe and the Americas during the period after 1492.' Confining "
          "the effect to one side contradicts KC-1.2's account of change on both sides of "
          "the Atlantic Ocean, and neither West Africa nor the period after 1607 appears "
          "in the objective."),

 dict(q="According to KC-1.2.I.B, what did the Columbian Exchange bring to Europe from "
        "the Americas, and with what effect on population?",
      choices=[
        "New crops, which stimulated European population growth",
        "New crops, which reduced European population",
        "New sources of mineral wealth, which stimulated European population growth",
        "New animals, which stimulated European population growth",
        "New crops, which left European population unchanged"],
      ans=0,
      why="KC-1.2.I.B states that the Columbian Exchange brought new crops to Europe from "
          "the Americas, stimulating European population growth. Mineral wealth is named "
          "in the same sentence but tied to a different consequence, the European shift "
          "from feudalism to capitalism, and the sentence describes growth rather than "
          "decline or stasis."),

 dict(q="KC-1.2.I.B ties new sources of mineral wealth to a change in Europe. Which "
        "change does the framework name?",
      choices=[
        "The European shift from feudalism to capitalism",
        "The European shift from capitalism to feudalism",
        "The growth of the European population",
        "The improvement of maritime technology",
        "The spread of epidemic disease in Europe"],
      ans=0,
      why="KC-1.2.I.B states that the Columbian Exchange brought new sources of mineral "
          "wealth, which facilitated the European shift from feudalism to capitalism. "
          "Reversing the direction of that shift inverts the sentence; population growth "
          "is what the same sentence attributes to the new crops; maritime technology is "
          "KC-1.2.I.C's subject and the epidemics of KC-1.2.II.A are placed among native "
          "populations in the Americas."),

 dict(q="A hypothetical revision card states that the Columbian Exchange carried new "
        "crops from Europe to the Americas and mineral wealth in the same direction. "
        "Which correction does KC-1.2.I.B require?",
      choices=[
        "Both the new crops and the new sources of mineral wealth are described as coming "
        "to Europe from the Americas",
        "Both are described as going from Europe to the Americas, as the card says",
        "The crops are described as coming to Europe and the mineral wealth as going to "
        "the Americas",
        "The crops are described as going to the Americas and the mineral wealth as coming "
        "to Europe",
        "The framework describes neither as moving in either direction"],
      ans=0,
      why="KC-1.2.I.B has the Columbian Exchange bring new crops to Europe from the "
          "Americas and new sources of mineral wealth, both arriving in Europe, with "
          "population growth attributed to the first and the shift from feudalism to "
          "capitalism to the second. Movement into the Americas is described by "
          "KC-1.2.II.A, and it concerns crops and animals not found there rather than "
          "these two items."),

 dict(q="KC-1.2.I.C names two developments that helped drive changes to economies. Which "
        "pair does the framework name?",
      choices=[
        "Improvements in maritime technology, and more organized methods for conducting "
        "international trade",
        "Improvements in maritime technology, and the introduction of animals not found in "
        "the Americas",
        "More organized methods for conducting international trade, and widespread deadly "
        "epidemics",
        "New sources of mineral wealth, and the growth of the European population",
        "The encomienda system, and the Spanish caste system"],
      ans=0,
      why="KC-1.2.I.C states that improvements in maritime technology and more organized "
          "methods for conducting international trade, such as joint-stock companies, "
          "helped drive changes to economies in Europe and the Americas. Introduced "
          "animals and epidemics belong to KC-1.2.II.A, mineral wealth and population "
          "growth to KC-1.2.I.B, and the encomienda and caste systems to KC-1.2.II.B and "
          "KC-1.2.II.D under a later topic."),

 dict(q="What example does KC-1.2.I.C give of a more organized method for conducting "
        "international trade?",
      choices=[
        "Joint-stock companies",
        "The encomienda system",
        "Royal monopolies over silver mining",
        "Chartered towns",
        "Guild membership requirements"],
      ans=0,
      why="KC-1.2.I.C names joint-stock companies as its example of more organized methods "
          "for conducting international trade. The encomienda system belongs to "
          "KC-1.2.II.B, where it is a labor arrangement rather than a method of trade, and "
          "royal mining monopolies, chartered towns and guild rules appear nowhere in the "
          "framework's account of this period."),

 dict(q="Where does KC-1.2.I.C locate the changes to economies that maritime technology "
        "and organized trade helped drive?",
      choices=[
        "In Europe and the Americas alike",
        "In Europe alone",
        "In the Americas alone",
        "In West Africa alone",
        "In Europe first and in the Americas only after 1607"],
      ans=0,
      why="KC-1.2.I.C states that these developments helped drive changes to economies in "
          "Europe and the Americas, naming both together, which matches KC-1.2's placement "
          "of significant change on both sides of the Atlantic Ocean and Unit 1 Learning "
          "Objective D's request for the effect on Europe and the Americas. The sentence "
          "gives no sequence and does not mention West Africa."),

 dict(q="According to KC-1.2.II.A, what accompanied and furthered Spanish exploration and "
        "conquest of the Americas?",
      choices=[
        "Widespread deadly epidemics that devastated native populations, and the "
        "introduction of crops and animals not found in the Americas",
        "Widespread deadly epidemics that devastated European populations, and the "
        "introduction of crops and animals not found in Europe",
        "The growth of the European population, and the shift from feudalism to capitalism",
        "Improvements in maritime technology, and joint-stock companies",
        "The encomienda system, and the Spanish caste system"],
      ans=0,
      why="KC-1.2.II.A states that Spanish exploration and conquest of the Americas were "
          "accompanied and furthered by widespread deadly epidemics that devastated native "
          "populations and by the introduction of crops and animals not found in the "
          "Americas. Moving the epidemics to Europe reverses the sentence; population "
          "growth and capitalism belong to KC-1.2.I.B, technology and companies to "
          "KC-1.2.I.C, and the labor and caste arrangements to KC-1.2.II.B and "
          "KC-1.2.II.D."),

 dict(q="KC-1.2.II.A says exploration and conquest were ACCOMPANIED AND FURTHERED by "
        "epidemics and introduced crops and animals. What does the second of those verbs "
        "add to the first?",
      choices=[
        "That these things did not merely coincide with the conquest but helped it along",
        "That these things came after the conquest was already complete",
        "That these things prevented the conquest from going further",
        "That these things had no bearing on the conquest either way",
        "That the conquest caused them and they had no effect of their own"],
      ans=0,
      why="KC-1.2.II.A joins accompanied to furthered, so the sentence claims both that "
          "these things ran alongside Spanish exploration and conquest and that they "
          "advanced it, which is more than coincidence and different from a consequence "
          "arriving afterwards. Nothing in the sentence describes them as obstructing the "
          "conquest or as inert."),

 dict(q="A hypothetical treatise, its author unnamed, argues that a plant lately brought "
        "across the ocean now feeds more people from the same ground than the old grains "
        "did. Which framework statement does that claim illustrate?",
      choices=[
        "KC-1.2.I.B, on new crops brought to Europe stimulating European population growth",
        "KC-1.2.I.B, on new sources of mineral wealth facilitating the shift from feudalism "
        "to capitalism",
        "KC-1.2.I.C, on maritime technology and organized trade driving economic change",
        "KC-1.2.II.A, on epidemics that devastated native populations",
        "KC-1.2, on contact producing social, cultural, and political change"],
      ans=0,
      why="KC-1.2.I.B attributes European population growth to the new crops the Columbian "
          "Exchange brought to Europe from the Americas, and a claim that a newly arrived "
          "plant feeds more people from the same ground is that link stated as an "
          "argument, which is what suggested skill 3.A asks students to identify. Mineral "
          "wealth, trade methods and epidemics are the subjects of the other sentences."),

 dict(q="Suppose an illustrative merchant's contract, its author unnamed, divides a "
        "voyage's costs and its returns among many investors, none of whom bears the whole "
        "risk. Which framework statement does it illustrate?",
      choices=[
        "KC-1.2.I.C, on more organized methods for conducting international trade, such as "
        "joint-stock companies",
        "KC-1.2.I.C, on improvements in maritime technology",
        "KC-1.2.I.B, on new crops stimulating European population growth",
        "KC-1.2.II.A, on the introduction of crops and animals not found in the Americas",
        "KC-1.2.II, on extensive demographic, economic, and social changes"],
      ans=0,
      why="KC-1.2.I.C names joint-stock companies as its example of the more organized "
          "methods for conducting international trade that helped drive economic change, "
          "and dividing a voyage's costs and returns among many investors is what such a "
          "company does. Improvements in maritime technology are the other half of the "
          "same sentence and concern ships rather than the arrangement of investment."),

 dict(q="A hypothetical parish record, its author unnamed, reports that the people of a "
        "settlement in the Americas fell to a fraction of their former number within a few "
        "years of strangers arriving, with sickness given as the cause. Which framework "
        "statement does it illustrate?",
      choices=[
        "KC-1.2.II.A, on widespread deadly epidemics that devastated native populations",
        "KC-1.2.I.B, on new crops stimulating European population growth",
        "KC-1.2.II.A, on the introduction of crops and animals not found in the Americas",
        "KC-1.2.I.C, on more organized methods for conducting international trade",
        "KC-1.2.III, on divergent worldviews asserted in interaction"],
      ans=0,
      why="KC-1.2.II.A states that Spanish exploration and conquest were accompanied and "
          "furthered by widespread deadly epidemics that devastated native populations, "
          "which is exactly the collapse the record describes and attributes to sickness. "
          "The other half of the same sentence concerns introduced crops and animals, "
          "which the record does not mention, and KC-1.2.I.B's population growth runs the "
          "other way."),

 dict(q="An illustrative traveller's account, its author unnamed, describes herds of "
        "grazing animals on land where the writer says no such beast had been seen before "
        "the ships came. Which framework statement does it illustrate?",
      choices=[
        "KC-1.2.II.A, on the introduction of crops and animals not found in the Americas",
        "KC-1.2.I.B, on new crops brought to Europe from the Americas",
        "KC-1.2.I.B, on new sources of mineral wealth reaching Europe",
        "KC-1.2.I.C, on improvements in maritime technology",
        "KC-1.2.II, on the development of the Spanish Empire in the Western Hemisphere"],
      ans=0,
      why="KC-1.2.II.A names the introduction of crops and animals not found in the "
          "Americas among the things that accompanied and furthered Spanish exploration "
          "and conquest, and an animal unknown there before the ships arrived is one of "
          "them. KC-1.2.I.B describes movement in the opposite direction, toward Europe, "
          "and concerns crops and mineral wealth rather than livestock."),

 dict(q="Using the table of illustrative index figures, which conclusion do the columns "
        "support?",
      table=_T_EUROPE,
      choices=[
        "Both the land under the new crop and the population rise at every step",
        "The population falls while the land under the new crop rises",
        "The land under the new crop is unchanged after the first period",
        "The population more than doubles across the three periods",
        "The land under the new crop falls at the last step"],
      ans=0,
      why="Read from the table alone: both columns are higher in each period than in the "
          "one before, and neither falls anywhere. That is the pattern KC-1.2.I.B "
          "describes when it says the new crops the Columbian Exchange brought to Europe "
          "stimulated European population growth. The population index ends below twice "
          "its opening value, so it does not more than double."),

 dict(q="Using the same table of illustrative index figures, which claim goes BEYOND what "
        "the columns can support?",
      table=_T_EUROPE,
      choices=[
        "That the new crop was the cause of the rise in population",
        "That the land under the new crop rises at every step",
        "That the population is higher in the third period than in the first",
        "That the land under the new crop rises by more index points than the population "
        "does",
        "That neither column falls at any step"],
      ans=0,
      why="The table reports two quantities rising together and nothing that ties one to "
          "the other, so causation is the one claim of the five it cannot reach on its own "
          "even though KC-1.2.I.B does assert it, saying the new crops stimulated European "
          "population growth. Identifying what a source can and cannot establish is what "
          "suggested skill 3.A asks for; the other four options are read straight off the "
          "columns."),

 dict(q="Using the table of items the framework names, which pairing of items with "
        "directions does the record give?",
      table=_T_DIRECTION,
      choices=[
        "The new crops and the new sources of mineral wealth are the two brought to "
        "Europe, and the crops and animals not found in the Americas are the two "
        "introduced into the Americas",
        "The crops and animals not found in the Americas are the two brought to Europe, "
        "and the new crops and the new sources of mineral wealth are the two introduced "
        "into the Americas",
        "All four items are recorded as brought to Europe",
        "All four items are recorded as introduced into the Americas",
        "The new sources of mineral wealth are recorded as introduced into the Americas"],
      ans=0,
      why="Read from the table alone: two rows are marked as brought to Europe and they "
          "are the new crops and the new sources of mineral wealth, which is KC-1.2.I.B's "
          "content, while the two marked as introduced into the Americas are the crops and "
          "animals not found there, which is KC-1.2.II.A's. Exchanging the two directions "
          "keeps every item and still misreports both sentences."),

 dict(q="The suggested skill printed on this topic page is 3.A. How does the framework "
        "state that skill?",
      choices=[
        "Identify and describe a claim and/or argument in a text-based or non-text-based "
        "source",
        "Identify the evidence used in a source to support an argument",
        "Compare the arguments or main ideas of two sources",
        "Identify a source's point of view, purpose, historical situation, and/or audience",
        "Identify patterns among or connections between historical developments and "
        "processes"],
      ans=0,
      why="Skill 3.A as printed on this topic page reads 'Identify and describe a claim "
          "and/or argument in a text-based or non-text-based source', and it is the skill "
          "Unit 1 Learning Objective D asks students to apply to sources about the "
          "Columbian Exchange. The other four are skills 3.B, 3.C, 2.A and 5.A, each "
          "printed on other topic pages of this course."),

 dict(q="The thematic focus printed on this topic page is Geography and the Environment. "
        "Which of its claims does the Columbian Exchange most directly illustrate?",
      choices=[
        "That the development of America impacts the environment and reshapes geography",
        "That geographic factors matter only where competition over resources is absent",
        "That environmental factors are unaffected by human activity",
        "That regional diversity is produced by government policy rather than by "
        "environment",
        "That debates about natural resources belong only to later periods"],
      ans=0,
      why="The Geography and the Environment thematic focus states that the development of "
          "America impacts the environment and reshapes geography, and KC-1.2.II.A's "
          "introduction of crops and animals not found in the Americas together with "
          "KC-1.2.I.B's new crops reaching Europe are exactly that reshaping, running in "
          "both directions. The same focus makes competition over resources part of what "
          "shapes development rather than a condition for it."),

 dict(q="Learning Objective D dates the effect it asks about to the period after 1492. "
        "What does that date mark in the framework's account?",
      choices=[
        "The point from which the Columbian Exchange's effects on Europe and the Americas "
        "are traced",
        "The end of the period this unit covers",
        "The beginning of the Spanish caste system",
        "The date the framework assigns to the shift from feudalism to capitalism",
        "The date after which native societies first developed agriculture"],
      ans=0,
      why="Unit 1 Learning Objective D asks students to explain causes of the Columbian "
          "Exchange and its effect on Europe and the Americas during the period after "
          "1492, so the date opens the span in which those effects are followed. The unit "
          "runs to 1607, the caste system is KC-1.2.II.D's subject with no such date, "
          "KC-1.2.I.B gives no year for the shift to capitalism, and native agriculture is "
          "placed before contact by KC-1.1.I.A."),

 dict(q="Which of the following does the framework NOT attribute to the Columbian Exchange "
        "in KC-1.2.I.B?",
      choices=[
        "The marshalling of Native American labor to extract precious metals",
        "New crops brought to Europe from the Americas",
        "The stimulation of European population growth",
        "New sources of mineral wealth",
        "The facilitation of the European shift from feudalism to capitalism"],
      ans=0,
      why="KC-1.2.I.B names new crops brought to Europe from the Americas, the stimulation "
          "of European population growth, new sources of mineral wealth, and the "
          "facilitation of the European shift from feudalism to capitalism. Marshalling "
          "Native American labor to extract precious metals is KC-1.2.II.B's description "
          "of the encomienda system, which belongs to a later topic of this unit and is "
          "not an item of the Exchange."),

 dict(q="KC-1.2.I.B says the new sources of mineral wealth FACILITATED the European shift "
        "from feudalism to capitalism. What does that verb allow that a stronger one would "
        "not?",
      choices=[
        "That the wealth helped a shift along without being its sole cause",
        "That the wealth was the only thing that produced the shift",
        "That the wealth prevented the shift from occurring",
        "That the shift occurred before the wealth arrived and was unaffected by it",
        "That no shift from feudalism to capitalism is described at all"],
      ans=0,
      why="KC-1.2.I.B's word is facilitated rather than caused, which credits the new "
          "sources of mineral wealth with helping the European shift from feudalism to "
          "capitalism without making them its whole explanation. The sentence plainly "
          "describes such a shift and places the wealth before it, so the remaining "
          "options each contradict something it says."),

 dict(q="KC-1.2.I.C says maritime technology and organized trade methods HELPED DRIVE "
        "changes to economies. What does that phrasing indicate about the framework's "
        "causal claim?",
      choices=[
        "It names contributing causes rather than a single sufficient one",
        "It names the only causes of economic change in the period",
        "It denies that the two developments had any effect",
        "It places the economic changes before the two developments",
        "It confines the economic changes to the Americas"],
      ans=0,
      why="KC-1.2.I.C says the two developments helped drive changes to economies in "
          "Europe and the Americas, which credits them with a share in the change rather "
          "than with the whole of it, in the same hedged way KC-1.2.I.B says mineral "
          "wealth facilitated the shift from feudalism to capitalism. The sentence puts "
          "the developments before the changes and names both sides of the Atlantic."),

 dict(q="What would be wrong with saying that the epidemics KC-1.2.II.A describes followed "
        "the Spanish conquest as its consequence?",
      choices=[
        "The sentence has them accompanying and furthering the conquest, so they run "
        "alongside it and advance it rather than merely resulting from it",
        "The sentence does not mention epidemics at all",
        "The sentence places the epidemics in Europe rather than in the Americas",
        "The sentence describes the epidemics as mild rather than deadly",
        "The sentence attributes the epidemics to the introduction of joint-stock "
        "companies"],
      ans=0,
      why="KC-1.2.II.A states that Spanish exploration and conquest of the Americas were "
          "accompanied and furthered by widespread deadly epidemics that devastated native "
          "populations, which places the epidemics beside the conquest and gives them a "
          "part in it, not merely after it. The same sentence calls them widespread and "
          "deadly and locates them among native populations; joint-stock companies belong "
          "to KC-1.2.I.C."),

 dict(q="Reasoning Process 2 asks students to explain the relationship between causes and "
        "effects. Which pairing from this topic states such a relationship in the "
        "framework's own terms?",
      choices=[
        "New crops brought to Europe, and the stimulation of European population growth",
        "New crops brought to Europe, and the improvement of maritime technology",
        "Joint-stock companies, and the devastation of native populations by epidemics",
        "The introduction of animals not found in the Americas, and the European shift from "
        "feudalism to capitalism",
        "Widespread deadly epidemics, and the growth of the European population"],
      ans=0,
      why="KC-1.2.I.B joins the two in one clause: the Columbian Exchange brought new "
          "crops to Europe from the Americas, stimulating European population growth. The "
          "other pairings join terms the framework keeps in separate sentences, and it "
          "nowhere connects joint-stock companies to epidemics, introduced animals to "
          "capitalism, or epidemics to European population growth."),

 dict(q="How does KC-1.2 place the Columbian Exchange in relation to contact among "
        "Europeans, Native Americans, and Africans?",
      choices=[
        "As one of the things that contact among those three groups resulted in",
        "As the cause of the contact among those three groups",
        "As an event unconnected to contact among those three groups",
        "As something confined to contact between Europeans and Africans",
        "As something that occurred before any of the three groups met"],
      ans=0,
      why="KC-1.2 states that contact among Europeans, Native Americans, and Africans "
          "resulted in the Columbian Exchange and significant social, cultural, and "
          "political changes on both sides of the Atlantic Ocean, so the Exchange follows "
          "the contact rather than producing it. Unit 1 Learning Objective D still asks "
          "for its causes, which is consistent: a result of one thing can be a cause of "
          "others."),

 dict(q="A hypothetical seminar handout claims that the Columbian Exchange's effects fell "
        "on the Americas alone. Which two framework sentences most directly refute it?",
      choices=[
        "KC-1.2.I.B on new crops and mineral wealth reaching Europe, and KC-1.2.I.C on "
        "changes to economies in Europe and the Americas",
        "KC-1.2.II.A on epidemics among native populations, and KC-1.2.II.B on the "
        "encomienda system",
        "KC-1.1.I.A on the spread of maize cultivation, and KC-1.1.I.B on mobile lifestyles",
        "KC-1.2.III on divergent worldviews, and KC-1.2.III.A on mutual misunderstandings",
        "KC-1.2.II.D on the Spanish caste system, and KC-1.2.II.C on enslaved laborers"],
      ans=0,
      why="KC-1.2.I.B has the Exchange bring new crops and new sources of mineral wealth "
          "to Europe with consequences for European population and economy, and KC-1.2.I.C "
          "locates the resulting economic changes in Europe and the Americas alike, which "
          "is also what Unit 1 Learning Objective D asks about. The other pairs describe "
          "events within the Americas or within the Spanish colonial system and do not "
          "speak to Europe."),

 dict(q="KC-1.2.I.B names two things the Exchange brought and gives each a different "
        "consequence. Which matching is the framework's?",
      choices=[
        "New crops with European population growth, and new sources of mineral wealth with "
        "the shift from feudalism to capitalism",
        "New crops with the shift from feudalism to capitalism, and new sources of mineral "
        "wealth with European population growth",
        "Both items with European population growth alone",
        "Both items with the shift from feudalism to capitalism alone",
        "New crops with improvements in maritime technology, and mineral wealth with "
        "joint-stock companies"],
      ans=0,
      why="KC-1.2.I.B attaches the stimulation of European population growth to the new "
          "crops and the facilitation of the European shift from feudalism to capitalism "
          "to the new sources of mineral wealth, in that order within one sentence. "
          "Exchanging the two consequences keeps every term and still misreports the "
          "sentence, and maritime technology and joint-stock companies belong to "
          "KC-1.2.I.C."),

 dict(q="Both KC-1.2.I.B and KC-1.2.II.A mention crops. What distinguishes the two "
        "mentions?",
      choices=[
        "KC-1.2.I.B has new crops arriving in Europe from the Americas, while KC-1.2.II.A "
        "has crops not found in the Americas introduced there",
        "KC-1.2.I.B has crops not found in the Americas introduced there, while "
        "KC-1.2.II.A has new crops arriving in Europe from the Americas",
        "Both sentences describe crops arriving in Europe",
        "Both sentences describe crops introduced into the Americas",
        "Neither sentence describes crops moving between the hemispheres"],
      ans=0,
      why="KC-1.2.I.B describes the Columbian Exchange bringing new crops to Europe from "
          "the Americas, and KC-1.2.II.A describes the introduction of crops and animals "
          "not found in the Americas as accompanying and furthering Spanish exploration "
          "and conquest there. The two sentences run in opposite directions, so exchanging "
          "them misstates both, and Unit 1 Learning Objective D asks about effects on "
          "Europe and the Americas alike."),

 dict(q="A hypothetical ship's inventory, its author unnamed, lists an outbound cargo of "
        "seed grain and breeding stock and a return cargo of bullion. Which two framework "
        "statements does it touch?",
      choices=[
        "KC-1.2.II.A, on crops and animals not found in the Americas, and KC-1.2.I.B, on "
        "new sources of mineral wealth reaching Europe",
        "KC-1.2.I.B, on crops and animals not found in the Americas, and KC-1.2.II.A, on "
        "new sources of mineral wealth reaching Europe",
        "KC-1.2.I.C, on improvements in maritime technology, and KC-1.2.III, on divergent "
        "worldviews",
        "KC-1.2.II.B, on the encomienda system, and KC-1.2.II.D, on the Spanish caste "
        "system",
        "KC-1.1.I.A, on the spread of maize cultivation, and KC-1.1.I.C, on permanent "
        "villages"],
      ans=0,
      why="KC-1.2.II.A names the introduction of crops and animals not found in the "
          "Americas, which is what seed grain and breeding stock carried outbound would "
          "be, and KC-1.2.I.B names the new sources of mineral wealth the Columbian "
          "Exchange brought to Europe, which is what bullion carried home would be. "
          "Attaching each description to the other code reverses both sentences; the "
          "remaining pairs concern ships, worldviews, colonial labor and native societies "
          "before contact."),

 dict(q="Which statement describes what this topic's Required Course Content asserts, "
        "without adding to it?",
      choices=[
        "The Exchange carried new crops and mineral wealth to Europe, crops and animals "
        "not found there into the Americas, and epidemics that devastated native "
        "populations accompanied and furthered the Spanish conquest, while better ships "
        "and organized trade helped drive economic change on both sides",
        "The Exchange carried new crops to Europe, which caused capitalism to replace "
        "feudalism throughout Europe within a generation",
        "The Exchange was confined to the movement of crops, and no other kind of thing "
        "moved between the hemispheres",
        "The Exchange devastated native populations, and had no consequences of any kind "
        "in Europe",
        "The Exchange followed rather than accompanied the Spanish conquest, and played no "
        "part in it"],
      ans=0,
      why="The first collects KC-1.2.I.B, KC-1.2.I.C and KC-1.2.II.A in the framework's "
          "own terms and adds nothing. The second replaces facilitated with caused and "
          "invents a timetable; the third omits mineral wealth, animals and disease; the "
          "fourth contradicts KC-1.2.I.B's European consequences; and the fifth contradicts "
          "KC-1.2.II.A's accompanied and furthered."),
]
