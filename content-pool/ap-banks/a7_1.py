# AP U.S. HISTORY 7.1 Contextualizing Period 7  (title copied from US_HISTORY_topics.json)
# Unit 7, Period 7: 1890 to 1945. Suggested skill 4.B, explain how a specific historical
# development or process is situated within a broader historical context. Reasoning
# process: contextualization.
#
# THE CED SENTENCES EVERY KEY IN THIS MODULE RESTS ON, in the framework's own words:
#
#   Unit 7 Learning Objective A
#       Explain the context in which America grew into its role as a world power.
#
#   KC-7.1      Growth expanded opportunity, while economic instability led to new
#               efforts to reform U.S. society and its economic system.
#   KC-7.1.I    The United States continued its transition from a rural, agricultural
#               economy to an urban, industrial economy led by large companies.
#   KC-7.1.II   In the Progressive Era of the early 20th century, Progressives responded
#               to political corruption, economic instability, and social concerns by
#               calling for greater government action and other political and social
#               measures.
#   KC-7.1.III  During the 1930s, policymakers responded to the mass unemployment and
#               social upheavals of the Great Depression by transforming the U.S. into a
#               limited welfare state, redefining the goals and ideas of modern American
#               liberalism.
#   KC-7.2      Innovations in communications and technology contributed to the growth of
#               mass culture, while significant changes occurred in internal and
#               international migration patterns.
#   KC-7.2.I    Popular culture grew in influence in U.S. society, even as debates
#               increased over the effects of culture on public values, morals, and
#               American national identity.
#   KC-7.2.II   Economic pressures, global events, and political developments caused sharp
#               variations in the numbers, sources, and experiences of both international
#               and internal migrants.
#   KC-7.3      Participation in a series of global conflicts propelled the United States
#               into a position of international power while renewing domestic debates
#               over the nation's proper role in the world.
#   KC-7.3.I    In the late 19th century and early 20th century, new U.S. territorial
#               ambitions and acquisitions in the Western Hemisphere and the Pacific
#               accompanied heightened public debates over America's role in the world.
#   KC-7.3.II   World War I and its aftermath intensified ongoing debates about the
#               nation's role in the world and how best to achieve national security and
#               pursue American interests.
#   KC-7.3.III  U.S. participation in World War II transformed American society, while the
#               victory of the United States and its allies over the Axis powers vaulted
#               the U.S. into a position of global, political, and military leadership.
#
#   The topic page's own instruction on what context is: students could examine "change
#   from and/or continuity with preceding historical developments" and "similarities
#   and/or differences with contemporaneous historical developments in different regions
#   or geographical areas."
#
# WHAT IS NOT KEYED, DELIBERATELY. This is a CONTEXTUALIZING topic and its Required
# Course Content is printed under the heading PREVIEW: UNIT 7 KEY CONCEPTS, not the
# detail behind them. The lettered sub-points -- KC-7.1.I.A through KC-7.3.III.E --
# belong to topics 7.2 through 7.14, which have their own pages. So no key here names a
# president, a statute, a treaty, a war other than the two the preview itself names, a
# programme, a movement, a court case or a place beyond the two regions KC-7.3.I states.
# Several items exist precisely to test that boundary, and `no_period_detail` in the
# verifier asserts it.
#
# NO FIGURES: the bank cannot display images, so every data item carries a table=.
# PROSE ONLY: no LaTeX; a span of years is written "1890 to 1945", never with a hyphen.
# FIVE choices (A-E). Invented sources are marked hypothetical, per HISTORY_BRIEF.md.
TOPIC = ("7.1", "Contextualizing Period 7", 7)

_T_TRANSITION = dict(
    headers=["Decade of the period (illustrative)",
             "Share of the population living in urban places (percent)",
             "Share of the workforce employed in agriculture (percent)"],
    rows=[["Decade 1", "28", "43"],
          ["Decade 2", "36", "37"],
          ["Decade 3", "46", "30"],
          ["Decade 4", "54", "25"]])

_T_MIGRANTS = dict(
    headers=["Stretch of the period (illustrative)",
             "International migrants recorded (thousands)",
             "Internal migrants recorded (thousands)"],
    rows=[["Stretch 1", "820", "310"],
          ["Stretch 2", "240", "540"],
          ["Stretch 3", "90", "760"]])

_T_CONCEPTS = dict(
    headers=["Statement offered as context (illustrative)",
             "Preview key concept it is drawn from"],
    rows=[["The United States continued its transition to an urban, industrial economy "
           "led by large companies", "KC-7.1.I"],
          ["Popular culture grew in influence even as debates over its effects increased",
           "KC-7.2.I"],
          ["New territorial ambitions and acquisitions accompanied heightened public "
           "debates", "KC-7.3.I"],
          ["Policymakers transformed the nation into a limited welfare state during the "
           "1930s", "KC-7.1.III"]])

QUESTIONS = [

 dict(q="Unit 7's Learning Objective A asks students to explain the context in which America "
        "grew into a particular role. Which role does the framework name?",
      choices=[
        "Its role as a world power",
        "Its role as a continental republic bounded by its own frontier",
        "Its role as an exporter of agricultural staples to Europe",
        "Its role as a neutral mediator among the states of Europe",
        "Its role as a federation of largely self-governing regions"],
      ans=0,
      why="Unit 7 Learning Objective A reads 'Explain the context in which America grew into "
          "its role as a world power.' The other four roles are not the one the objective "
          "names, and KC-7.3 states that participation in a series of global conflicts "
          "propelled the United States into a position of international power."),

 dict(q="The framework divides U.S. history into numbered periods. Which span of years does "
        "it give for Period 7, the period this unit covers?",
      choices=[
        "1890 to 1945",
        "1865 to 1898",
        "1945 to 1980",
        "1877 to 1929",
        "1900 to 1939"],
      ans=0,
      why="The unit is titled Period 7: 1890 to 1945, and Unit 7 Learning Objective A asks for "
          "the context in which America grew into its role as a world power across it. The "
          "span 1865 to 1898 is Period 6's and 1945 to 1980 is Period 8's; the remaining two "
          "appear nowhere in the framework's periodisation."),

 dict(q="According to KC-7.1, what accompanied the expansion of opportunity that growth "
        "produced?",
      choices=[
        "Economic instability, which led to new efforts to reform U.S. society and its "
        "economic system",
        "A settled economic system that required no reform during the period",
        "A steady decline in opportunity across U.S. society",
        "The withdrawal of government from economic life altogether",
        "A halt to economic growth at the opening of the 20th century"],
      ans=0,
      why="KC-7.1 states that growth expanded opportunity, while economic instability led to "
          "new efforts to reform U.S. society and its economic system. The sentence pairs "
          "expanded opportunity with instability and reform, so a settled system, a decline in "
          "opportunity, a withdrawal of government or a halt to growth each contradict part "
          "of it."),

 dict(q="KC-7.1.I describes a transition the United States continued through this period. "
        "Which transition does it name?",
      choices=[
        "From a rural, agricultural economy to an urban, industrial economy led by large "
        "companies",
        "From an urban, industrial economy back to a rural, agricultural one",
        "From an economy led by large companies to one led by small independent producers",
        "From a wage-earning economy to one based on household self-sufficiency",
        "From an industrial economy to one resting on the export of raw materials"],
      ans=0,
      why="KC-7.1.I states that the United States continued its transition from a rural, "
          "agricultural economy to an urban, industrial economy led by large companies. The "
          "second option reverses that direction, and the remaining three reverse the "
          "framework's account of scale, of wage work or of industry."),

 dict(q="KC-7.1.I says the United States CONTINUED its transition. What does that word "
        "establish for a student contextualising the period?",
      choices=[
        "That the transition was already under way before the period opened and carried on "
        "inside it",
        "That the transition began only after 1890",
        "That the transition had been completed before the period opened",
        "That the transition reversed itself during the period",
        "That the framework treats the transition as unimportant to the period"],
      ans=0,
      why="KC-7.1.I's verb is 'continued', which places the transition before the period as "
          "well as inside it, and the topic page names change from or continuity with "
          "preceding historical developments as one of the two ways into context. A "
          "transition that began in the period, ended before it, or reversed would not be a "
          "continuation."),

 dict(q="To what does KC-7.1.II say Progressives responded?",
      choices=[
        "Political corruption, economic instability, and social concerns",
        "Foreign invasion, tariff reduction, and territorial expansion",
        "The mass unemployment and social upheavals of the Great Depression",
        "Debates over the effects of culture on public values and morals",
        "Sharp variations in the numbers and sources of migrants"],
      ans=0,
      why="KC-7.1.II states that in the Progressive Era of the early 20th century, "
          "Progressives responded to political corruption, economic instability, and social "
          "concerns. The third option belongs to KC-7.1.III, the fourth to KC-7.2.I and the "
          "fifth to KC-7.2.II, which is why each reads plausibly and none is this sentence."),

 dict(q="By what means does KC-7.1.II say the Progressives responded?",
      choices=[
        "By calling for greater government action and other political and social measures",
        "By calling for the removal of government from the economy",
        "By calling for the acquisition of territory overseas",
        "By calling for the courts alone to settle economic questions",
        "By calling for a return to a rural, agricultural way of life"],
      ans=0,
      why="KC-7.1.II states that Progressives responded by calling for greater government "
          "action and other political and social measures. Removing government reverses that "
          "claim; territorial acquisition belongs to KC-7.3.I, and neither the courts alone "
          "nor a return to rural life appears in the sentence."),

 dict(q="Where in time does KC-7.1.II place the Progressive Era?",
      choices=[
        "In the early 20th century",
        "In the middle of the 19th century",
        "In the final quarter of the 20th century",
        "In the years following the Second World War",
        "In the decade of the 1930s"],
      ans=0,
      why="KC-7.1.II opens 'In the Progressive Era of the early 20th century'. The 1930s are "
          "where KC-7.1.III places the response to the Great Depression, and the years after "
          "the Second World War fall outside the period Unit 7 Learning Objective A covers."),

 dict(q="According to KC-7.1.III, to what did policymakers respond during the 1930s?",
      choices=[
        "The mass unemployment and social upheavals of the Great Depression",
        "The political corruption and social concerns of the Progressive Era",
        "The growth of mass culture and its effects on public values",
        "The sharp variations in the sources of international migration",
        "The heightened public debates over new territorial acquisitions"],
      ans=0,
      why="KC-7.1.III states that during the 1930s, policymakers responded to the mass "
          "unemployment and social upheavals of the Great Depression. Political corruption "
          "and social concerns are what KC-7.1.II says Progressives responded to, and the "
          "remaining three options are drawn from KC-7.2.I, KC-7.2.II and KC-7.3.I."),

 dict(q="How does KC-7.1.III say policymakers responded during the 1930s?",
      choices=[
        "By transforming the nation into a limited welfare state and redefining the goals and "
        "ideas of modern American liberalism",
        "By transferring the whole of the economy into public ownership",
        "By leaving relief entirely to private charity and the states",
        "By restricting the franchise until the emergency had passed",
        "By reversing the transition to an urban, industrial economy"],
      ans=0,
      why="KC-7.1.III states that policymakers responded by transforming the U.S. into a "
          "limited welfare state, redefining the goals and ideas of modern American "
          "liberalism. Public ownership of the whole economy, private charity alone, a "
          "restricted franchise and a reversal of KC-7.1.I's transition are none of them in "
          "that sentence."),

 dict(q="KC-7.1.III calls the result a LIMITED welfare state. What work does that word do in "
        "the sentence?",
      choices=[
        "It qualifies the transformation rather than claiming a complete welfare state",
        "It states that the transformation was undone before the period ended",
        "It confines the transformation to a single region of the country",
        "It means the framework treats the transformation as insignificant",
        "It restricts the transformation to the years before the 1930s"],
      ans=0,
      why="KC-7.1.III says policymakers transformed the U.S. into a LIMITED welfare state, so "
          "the adjective qualifies how far the transformation went while the sentence still "
          "calls it a transformation that redefined the goals and ideas of modern American "
          "liberalism. Nothing in the sentence undoes it, confines it to a region, dismisses "
          "it or moves it before the 1930s."),

 dict(q="KC-7.2 joins two developments in a single sentence. Which pair does it join?",
      choices=[
        "The growth of mass culture and significant changes in migration patterns",
        "The growth of mass culture and the end of migration to the United States",
        "The decline of mass culture and an unchanging pattern of migration",
        "Industrial growth and the reform of the financial regulatory system",
        "New territorial acquisitions and public debates over America's role in the world"],
      ans=0,
      why="KC-7.2 states that innovations in communications and technology contributed to the "
          "growth of mass culture, while significant changes occurred in internal and "
          "international migration patterns. An end to migration or an unchanging pattern "
          "contradicts the second half; the last option is KC-7.3.I's sentence rather than "
          "this one."),

 dict(q="According to KC-7.2.I, what increased even as popular culture grew in influence?",
      choices=[
        "Debates over the effects of culture on public values, morals, and American national "
        "identity",
        "Agreement about the proper content of popular culture",
        "The isolation of regional cultures from one another",
        "Restrictions placed by the framework on the study of culture",
        "The share of the workforce employed in agriculture"],
      ans=0,
      why="KC-7.2.I states that popular culture grew in influence in U.S. society, even as "
          "debates increased over the effects of culture on public values, morals, and "
          "American national identity. Agreement is the opposite of increased debate, and "
          "KC-7.1.I describes a transition away from an agricultural economy rather than "
          "towards one."),

 dict(q="KC-7.2.I says popular culture grew in influence EVEN AS debates increased. Which "
        "reading does that construction rule out?",
      choices=[
        "That the growing influence of popular culture met no argument",
        "That popular culture grew in influence during the period",
        "That debates touched on public values and morals",
        "That American national identity was among the things debated",
        "That the framework treats popular culture as worth studying"],
      ans=0,
      why="KC-7.2.I sets the growth of popular culture alongside increasing debate over its "
          "effects, so the reading it excludes is the one in which that growth went "
          "unargued. The other four are things the sentence asserts rather than excludes: it "
          "names the growth, the public values, the morals and the American national identity "
          "at issue."),

 dict(q="KC-7.2.II names three things that caused sharp variations in migration. Which set "
        "names all three?",
      choices=[
        "Economic pressures, global events, and political developments",
        "Economic pressures, religious revival, and the growth of mass culture",
        "Global events, judicial rulings, and changes in the climate",
        "Political developments, military conscription, and industrial invention",
        "Economic pressures, territorial acquisition, and the reform of the financial system"],
      ans=0,
      why="KC-7.2.II states that economic pressures, global events, and political developments "
          "caused sharp variations in the numbers, sources, and experiences of migrants. "
          "Religious revival, judicial rulings, climate, conscription, invention, territorial "
          "acquisition and financial reform are not in that list."),

 dict(q="KC-7.2.II says sharp variations occurred in the numbers, sources, and experiences of "
        "which migrants?",
      choices=[
        "Both international and internal migrants",
        "International migrants only",
        "Internal migrants only",
        "Migrants leaving the United States only",
        "Migrants moving between two foreign countries"],
      ans=0,
      why="KC-7.2.II names the numbers, sources, and experiences of BOTH international and "
          "internal migrants, and KC-7.2 makes the same pairing when it says significant "
          "changes occurred in internal and international migration patterns. Keeping only "
          "one of the two drops half of what the framework states."),

 dict(q="KC-7.3 attributes two consequences to participation in a series of global conflicts. "
        "Which pair does it name?",
      choices=[
        "A position of international power abroad, and renewed domestic debate over the "
        "nation's proper role in the world",
        "A position of international power abroad, and an end to domestic debate about the "
        "nation's role",
        "A withdrawal from international affairs, and renewed domestic debate",
        "A settled agreement at home, and no change in the nation's international standing",
        "A transition to an agricultural economy, and a decline in migration"],
      ans=0,
      why="KC-7.3 states that participation in a series of global conflicts propelled the "
          "United States into a position of international power WHILE renewing domestic "
          "debates over the nation's proper role in the world. The sentence gives an outward "
          "consequence and a domestic one together, so ending debate, withdrawing, or "
          "reporting no change each drops or reverses one of them."),

 dict(q="According to KC-7.3.I, where were the new U.S. territorial ambitions and "
        "acquisitions of the late 19th century and early 20th century?",
      choices=[
        "In the Western Hemisphere and the Pacific",
        "In continental Europe and North Africa",
        "In Central Asia and the Arctic",
        "In the Western Hemisphere only",
        "In the Pacific and in southern Africa"],
      ans=0,
      why="KC-7.3.I states that new U.S. territorial ambitions and acquisitions in the Western "
          "Hemisphere and the Pacific accompanied heightened public debates over America's "
          "role in the world. The fourth option keeps only one of the two regions the "
          "sentence names, and Europe, North Africa, Central Asia, the Arctic and southern "
          "Africa are not named in it at all."),

 dict(q="KC-7.3.II says that World War I and its aftermath INTENSIFIED debates about the "
        "nation's role in the world. What does that verb establish?",
      choices=[
        "That the debates were already ongoing and the war and its aftermath sharpened them",
        "That the debates began with the war and had no earlier history",
        "That the debates were settled by the war and its aftermath",
        "That the debates concerned only the conduct of the fighting itself",
        "That the framework places those debates after 1945"],
      ans=0,
      why="KC-7.3.II states that World War I and its aftermath intensified ONGOING debates "
          "about the nation's role in the world and how best to achieve national security and "
          "pursue American interests, and KC-7.3.I already places heightened public debates "
          "over America's role in the world in the late 19th century and early 20th century. "
          "So the debates precede the war rather than beginning or ending with it."),

 dict(q="What two things does KC-7.3.III attribute to U.S. participation in World War II and "
        "to the victory over the Axis powers?",
      choices=[
        "A transformation of American society, and a position of global, political, and "
        "military leadership",
        "A transformation of American society, and a return to the foreign policy of the "
        "1890s",
        "An unchanged American society, and a position of global leadership",
        "A transformation of American society, and the loss of the territories acquired "
        "earlier in the period",
        "A decline in industrial capacity, and a reduced international standing"],
      ans=0,
      why="KC-7.3.III states that U.S. participation in World War II transformed American "
          "society, while the victory of the United States and its allies over the Axis "
          "powers vaulted the U.S. into a position of global, political, and military "
          "leadership. The sentence carries both a domestic transformation and an "
          "international standing, so options that keep one and reverse the other fail on the "
          "half they change."),

 dict(q="Using the table of illustrative decades, which reading matches the transition "
        "KC-7.1.I describes?",
      table=_T_TRANSITION,
      choices=[
        "The urban share rises in every decade recorded while the agricultural share falls in "
        "every decade recorded",
        "Both recorded shares fall across the four decades",
        "The urban share falls while the agricultural share rises",
        "The two recorded shares stay level across the four decades",
        "The agricultural share is the larger of the two in every decade recorded"],
      ans=0,
      why="Read from the table alone: the urban column rises at every step and the "
          "agricultural column falls at every step, which is the direction of the transition "
          "KC-7.1.I states, from a rural, agricultural economy to an urban, industrial one. "
          "The agricultural share is the larger only in the first two decades recorded, so "
          "the last option is false as well."),

 dict(q="Reading the same table of illustrative decades, in which decade does the urban share "
        "first exceed the agricultural share?",
      table=_T_TRANSITION,
      choices=[
        "Decade 3",
        "Decade 1",
        "Decade 2",
        "Decade 4",
        "The urban share never exceeds the agricultural share in the record"],
      ans=0,
      why="Read from the table alone: the urban share is below the agricultural share in the "
          "first two decades recorded and above it in the last two, so the crossing falls in "
          "the third. KC-7.1.I describes exactly this transition from a rural, agricultural "
          "economy to an urban, industrial economy led by large companies, and the framework "
          "supplies no date for the crossing, which is why the table has to."),

 dict(q="Using the table of illustrative migration figures, which conclusion does the record "
        "support?",
      table=_T_MIGRANTS,
      choices=[
        "The recorded numbers vary sharply from one stretch to the next, and both kinds of "
        "migrant appear throughout",
        "The international figure rises across the three stretches recorded",
        "Only internal migrants are recorded in this table",
        "The two figures move in the same direction across the stretches",
        "Neither figure changes by much across the stretches recorded"],
      ans=0,
      why="Read from the table alone: the international column falls steeply while the "
          "internal column rises steeply, and every stretch records a figure in both columns. "
          "That is the variation KC-7.2.II describes, sharp variations in the numbers of both "
          "international and internal migrants, and it falsifies the four other readings at "
          "the same time."),

 dict(q="Using the table of illustrative statements, which pair is drawn from the SAME "
        "top-level key concept of the unit preview?",
      table=_T_CONCEPTS,
      choices=[
        "The statement about the transition to an urban, industrial economy and the statement "
        "about a limited welfare state",
        "The statement about popular culture and the statement about territorial ambitions",
        "The statement about the transition to an urban, industrial economy and the statement "
        "about popular culture",
        "The statement about territorial ambitions and the statement about a limited welfare "
        "state",
        "No two statements in the record come from the same top-level key concept"],
      ans=0,
      why="Read from the table alone: the codes recorded are KC-7.1.I, KC-7.2.I, KC-7.3.I and "
          "KC-7.1.III, so the only two sharing a top-level concept are the two under KC-7.1, "
          "which is the sentence about growth, instability and reform. The pairs offered in "
          "the other options cross from KC-7.1 to KC-7.2 or KC-7.3."),

 dict(q="This topic practises a suggested skill printed on its own page. Which statement is "
        "that skill?",
      choices=[
        "Explain how a specific historical development or process is situated within a "
        "broader historical context",
        "Explain the point of view, purpose, historical situation, and audience of a source",
        "Explain how a historical development or process relates to another historical "
        "development or process",
        "Explain a historical concept, development, or process",
        "Use historical reasoning to explain relationships among pieces of historical "
        "evidence"],
      ans=0,
      why="The suggested skill printed on this topic page is 4.B, explain how a specific "
          "historical development or process is situated within a broader historical context, "
          "and it is the skill Unit 7 Learning Objective A asks students to apply when they "
          "explain the context in which America grew into its role as a world power. The "
          "other four are skills 2.B, 5.B, 1.B and 6.C, each printed on other topic pages of "
          "this unit."),

 dict(q="A hypothetical revision guide, offered as an illustration only, claims that this "
        "topic's Required Course Content supplies the detail of the reform programmes of the "
        "1930s. What is wrong with that claim?",
      choices=[
        "This topic's Required Course Content is a PREVIEW of the unit's key concepts, and "
        "the detail sits in the later topics of the unit",
        "The framework does not cover the 1930s anywhere in Unit 7",
        "The reform programmes of the 1930s belong to Period 8 rather than to Period 7",
        "The Required Course Content for this topic lists no key concepts at all",
        "The framework treats those programmes as context rather than as content"],
      ans=0,
      why="The topic page prints the unit's key concepts under the heading PREVIEW and tells "
          "the teacher to select one or two for which students most need context, so the "
          "detail belongs to the later topics rather than here. KC-7.1.III does place the "
          "response to the Great Depression in the 1930s inside Unit 7, so the framework "
          "neither omits the decade nor defers it to a later period, and the preview does "
          "list key concepts."),

 dict(q="The topic page tells students that to understand context they could examine change "
        "from or continuity with PRECEDING developments, and similarities or differences with "
        "CONTEMPORANEOUS developments in different regions. Which pair of moves matches those "
        "two approaches in that order?",
      choices=[
        "Noting that the transition to an urban, industrial economy was already under way "
        "before 1890, then comparing U.S. debates over empire with debates elsewhere in the "
        "same years",
        "Comparing U.S. debates over empire with debates elsewhere in the same years, then "
        "noting that the transition to an urban, industrial economy was already under way "
        "before 1890",
        "Treating both moves as comparisons with developments in other regions",
        "Treating both moves as accounts of what preceded the period",
        "Neither move is of the kind the topic page describes"],
      ans=0,
      why="The topic page names two ways into context in this order: change from or "
          "continuity with preceding developments, then similarities or differences with "
          "contemporaneous developments in different regions. KC-7.1.I's word 'continued' "
          "supplies the first, and KC-7.3.I's heightened public debates over America's role "
          "in the world sit beside the period rather than before it. Reversing the pair, or "
          "calling both moves the same kind, misapplies the page's own distinction."),

 dict(q="A hypothetical school textbook account, its author unnamed, opens by stating that "
        "the United States was already a world power when the period began. Which part of the "
        "framework most directly qualifies that statement?",
      choices=[
        "Unit 7 Learning Objective A, which asks for the context in which America GREW INTO "
        "that role",
        "KC-7.1.II, which describes the Progressive response to political corruption",
        "KC-7.2.I, which describes debates over the effects of culture",
        "KC-7.2.II, which describes sharp variations in migration",
        "KC-7.1.III, which describes a limited welfare state"],
      ans=0,
      why="Unit 7 Learning Objective A asks students to explain the context in which America "
          "GREW INTO its role as a world power, and KC-7.3 says participation in a series of "
          "global conflicts propelled the United States into a position of international "
          "power, so the framework treats that standing as reached during the period. The "
          "other four sentences concern reform, culture and migration and say nothing about "
          "when the United States acquired international power."),

 dict(q="A hypothetical student essay, invented for this question, opens with the victory over "
        "the Axis powers and calls it the context for the whole of Period 7. Why does that use "
        "of the term not match the topic page's instruction?",
      choices=[
        "That victory is where the period's developments arrive, so it cannot be the context "
        "that preceded or surrounded them",
        "The victory over the Axis powers is not mentioned anywhere in Unit 7",
        "Context must always be economic rather than military",
        "The essay should have confined itself to a single region",
        "Contextualization requires the student to name a date"],
      ans=0,
      why="The topic page defines context as preceding developments or contemporaneous "
          "developments elsewhere, and KC-7.3.III places the victory over the Axis powers at "
          "the end of the sequence, as what vaulted the United States into a position of "
          "global, political, and military leadership. Using that outcome as the context "
          "inverts the relationship. KC-7.3.III does name the victory, and the framework "
          "restricts context neither to one kind of subject, nor to one region, nor to a "
          "stated date."),

 dict(q="Which single sentence best states the whole of what the framework previews for Unit "
        "7, without adding to it?",
      choices=[
        "Growth expanded opportunity while instability brought reform, innovations in "
        "communications and technology grew a mass culture while migration patterns shifted, "
        "and participation in global conflicts brought international power and renewed debate "
        "about the nation's role",
        "The United States fought two world wars and emerged from them without changes at "
        "home",
        "Reform of the economy is the whole of what Period 7 covers",
        "Innovations in communications and technology are the only cause the framework gives "
        "for anything in the period",
        "The United States expanded overseas while its economy and its culture stayed as they "
        "had been"],
      ans=0,
      why="The first collects KC-7.1, KC-7.2 and KC-7.3 in the order the framework prints "
          "them and adds nothing to them. The second contradicts KC-7.3.III, which says U.S. "
          "participation in World War II transformed American society; the third and fourth "
          "reduce the preview to one of its three concepts; and the fifth contradicts both "
          "KC-7.1.I's transition and KC-7.2's growth of mass culture."),
]
