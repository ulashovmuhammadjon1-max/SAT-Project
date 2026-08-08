#!/usr/bin/env python3
"""
Reading & Writing authored for Test 18.

All 81 items are original. The transcribed pool was spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed answer key has to
be re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers
in 81 that way). Every item below carries a `why` that records the reasoning
which produced the key AND the reason the strongest distractor fails - that
record IS the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are never bare punctuation. Test 8 shipped Boundaries
items whose four options were ", " / "; " / ": " / " and ", which a student
sees as four empty rows. The real test repeats the words on either side of the
blank inside every option so each choice reads as the resulting sentence, and
every Boundaries item here is written that way from the start. Form/Structure
items whose options are genuinely words ("was" / "were", "has" / "have") stay
as words, which is also how the real test presents them.

Topics were screened programmatically against content-pool/rw_authored_corpus
.json - 809 passages banked or authored across Tests 1-15 - with a keyword
check and a shared-5-gram / Jaccard check, using check_originality.py in this
directory. Test 18 was assigned fifteen subject territories to keep it clear of
the sibling Test 16 and Test 17 builds: aviation and flight, brewing and food
microbiology, watchmaking and precision mechanics, quarrying and building
stone, orchards and fruit breeding, epidemiology and public health history,
medieval manuscripts and palaeography, desert ecology and arid-land
agriculture, semiconductors and computing hardware, West African metallurgy
and empires, sleep and circadian science, tidal and wave energy, Japanese
woodblock printing and paper arts, seed banks and crop diversity, and sports
biomechanics.

Candidates that collided with an existing passage were dropped before drafting
rather than paraphrased around: sourdough starters, the Whitworth screw thread,
pellagra and niacin, palimpsests and iron-gall ink, qanats, Nok terracotta, the
bloomery furnace, Benin lost-wax casting, Igbo-Ukwu, Prussian blue in prints,
the Svalbard seed vault, punched-card tabulating, the woodblock cutter
destroying the artist's drawing, fog nets, the trans-Saharan salt-and-gold
caravan, wind tunnels, aerial survey, and sleep-spindle memory consolidation.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T18"
MODULE = "RW"


def wic(num, passage, choices, answer, why):
    return dict(num=num, skill="Words in Context", passage=passage,
                stem="Which choice completes the text with the most logical and precise word or phrase?",
                choices=choices, answer=answer, why=why)


def meaning(num, passage, word, choices, answer, why):
    """Underlined-word-meaning variant of a Words in Context item."""
    return dict(num=num, skill="Words in Context", passage=passage,
                stem=f"As used in the text, what does the word &ldquo;{word}&rdquo; most nearly mean?",
                choices=choices, answer=answer, why=why)


def tsp(num, passage, stem, choices, answer, why):
    return dict(num=num, skill="Text Structure and Purpose", passage=passage,
                stem=stem, choices=choices, answer=answer, why=why)


def cid(num, passage, stem, choices, answer, why):
    return dict(num=num, skill="Central Ideas and Details", passage=passage,
                stem=stem, choices=choices, answer=answer, why=why)


def coe(num, passage, stem, choices, answer, why):
    return dict(num=num, skill="Command of Evidence", passage=passage,
                stem=stem, choices=choices, answer=answer, why=why)


def inf(num, passage, choices, answer, why):
    return dict(num=num, skill="Inferences", passage=passage,
                stem="Which choice most logically completes the text?",
                choices=choices, answer=answer, why=why)


def bnd(num, passage, choices, answer, why):
    return dict(num=num, skill="Boundaries", passage=passage,
                stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
                choices=choices, answer=answer, why=why)


def fss(num, passage, choices, answer, why):
    return dict(num=num, skill="Form, Structure, and Sense", passage=passage,
                stem="Which choice completes the text so that it conforms to the conventions of Standard English?",
                choices=choices, answer=answer, why=why)


def trn(num, passage, choices, answer, why):
    return dict(num=num, skill="Transitions", passage=passage,
                stem="Which choice completes the text with the most logical transition?",
                choices=choices, answer=answer, why=why)


def syn(num, notes, goal, choices, answer, why):
    bullets = "".join(f"<li>{n}</li>" for n in notes)
    return dict(
        num=num, skill="Rhetorical Synthesis",
        passage=f"While researching a topic, a student has taken the following notes:<ul>{bullets}</ul>",
        stem=f"The student wants to {goal} Which choice most effectively uses relevant "
             "information from the notes to accomplish this goal?",
        choices=choices, answer=answer, why=why)


QUESTIONS = [

 # ------------------------------------------------------ Words in Context (15)
 wic("W1",
     "A rigid airship held its shape from a metal framework rather than from the pressure of the "
     "gas inside it, so its hull could be built long enough to lift a heavy load over a long "
     "distance. The lifting gas itself, however, was hydrogen, which burns readily in air. "
     "Designers who wanted more range had to weigh that advantage against a hazard they could not "
     "entirely _____.",
     ["eliminate", "measure", "welcome", "postpone"], "A",
     "The sentence sets the gain in lift against a danger that stays with the design whatever else "
     "is done, so the blank names something the designers could not get rid of. The 'measure' "
     "option would make the hazard unknown, but the text has already described how hydrogen "
     "behaves in air."),

 wic("W2",
     "Barley starch is not fermentable, and yeast can make nothing of it. Malting wakes the grain "
     "just far enough to produce the enzymes that will break the starch down, and the maltster then "
     "kills the sprout with heat before the seedling can consume what it has made. The whole "
     "operation is a question of _____: halted too early it yields too little enzyme, and halted "
     "too late it leaves the brewer nothing to work on.",
     ["timing", "temperature", "cleanliness", "scale"], "A",
     "The colon sets halting too early against halting too late, so the blank names the judgement "
     "of when to stop. The 'temperature' option picks out the means by which the sprouting is "
     "arrested rather than the thing the sentence identifies as decisive."),

 wic("W3",
     "A balance wheel swings back and forth against a flat spiral spring, and the rate of a watch "
     "depends on how regularly it does so. Ordinary steel springs stiffen as they cool and slacken "
     "as they warm, so a watch adjusted in a warm room ran fast through the winter. The nickel-iron "
     "alloy that Guillaume developed held its stiffness across the range of temperatures a pocket "
     "meets, leaving the rate largely _____ by the weather.",
     ["unaffected", "governed", "obscured", "improved"], "A",
     "The alloy is said to hold its stiffness across the ordinary temperature range, so the weather "
     "stops changing the rate. The 'governed' option would have the weather still controlling the "
     "rate, which is the very fault the alloy removed."),

 wic("W4",
     "The beds of oolitic limestone quarried on the Isle of Portland lie in a fixed sequence, and "
     "the sequence matters as much as the rock. A block cut from the wrong bed carries shell so "
     "coarse that a carved edge crumbles under the chisel. Masons therefore ordered stone by the "
     "name of the bed rather than by the name of the quarry, a distinction that looks _____ until a "
     "cornice has had to be cut twice.",
     ["pedantic", "profitable", "obligatory", "traditional"], "A",
     "The sentence needs a word for how the distinction strikes an outsider before its point is "
     "felt, and an over-fine piece of hair-splitting is what 'pedantic' names. The 'obligatory' "
     "option destroys the contrast, since something already binding does not stop seeming so once a "
     "cornice is spoiled."),

 wic("W5",
     "An apple grown from seed does not reproduce the fruit of its parent, so every variety in an "
     "orchard is a cutting joined onto a root raised separately. The root leaves the fruit "
     "unchanged, but it fixes the size the tree will reach: a dwarfing stock keeps a tree short "
     "enough to be picked from the ground, while a vigorous stock sends the same variety up beyond "
     "a ladder. The choice of root is therefore _____ the choice of fruit.",
     ["independent of", "identical to", "dictated by", "a consequence of"], "A",
     "The passage states that the root sets the size while leaving the fruit alone, so the two "
     "decisions are made separately from one another. Making the root choice a consequence of the "
     "fruit choice contradicts the clause saying the root does not change the fruit."),

 wic("W6",
     "When cholera broke out around Broad Street in 1854, the prevailing account held that the "
     "disease travelled in foul air. John Snow plotted every death on a map of the parish and found "
     "them clustered tightly around a single pump. The pattern was _____ an airborne cause, which "
     "would have thinned out evenly in all directions from any source of stench rather than "
     "following the reach of one well.",
     ["difficult to reconcile with", "consistent with", "indistinguishable from", "readily explained by"], "A",
     "The clause after the blank says an airborne cause predicts an even spread while the deaths "
     "followed one well, so the map sat badly with the prevailing account. The 'consistent with' "
     "option asserts the opposite of the explanation the sentence goes on to give."),

 wic("W7",
     "Scripts used across Europe in the eighth century differed so much from region to region that "
     "a reader trained in one could labour over a book copied in another. The hand promoted in "
     "Charlemagne's scriptoria used clearly separated letters of uniform height, with spaces left "
     "between the words. Its purpose was not beauty but _____: a book copied in this hand could be "
     "read anywhere the reform had reached.",
     ["legibility", "economy", "novelty", "secrecy"], "A",
     "The colon states that a book in this hand could be read anywhere, and every feature listed is "
     "one that makes letters easier to make out. The 'economy' option would point to savings of "
     "parchment or of time, and the passage mentions neither."),

 wic("W8",
     "A saguaro's roots run outward just below the surface rather than downward, reaching as far "
     "from the trunk as the plant stands tall. Rain in the Sonoran Desert falls hard and briefly "
     "and has drained or evaporated within hours. A shallow, wide root system is _____ that "
     "pattern: it takes up a large share of a brief soaking before the water is gone.",
     ["well suited to", "indifferent to", "opposed to", "prior to"], "A",
     "The colon spells out the fit, since wide shallow roots catch a short-lived soaking of exactly "
     "the kind described. The 'indifferent to' option denies any relation between root form and "
     "rainfall, which is the relation the rest of the sentence sets out."),

 wic("W9",
     "The features etched onto a modern wafer are smaller than a particle of household dust, so a "
     "single speck settling on the surface ruins every circuit it covers. Fabrication plants filter "
     "their air continuously, dress workers in sealed suits and hold the rooms at a pressure "
     "slightly above the pressure outside, so that air leaks out rather than in. The measures look "
     "extravagant, but at these dimensions ordinary cleanliness is simply _____.",
     ["inadequate", "expensive", "unavailable", "customary"], "A",
     "The opening establishes that a speck of dust is larger than the features being made, so the "
     "everyday standard cannot protect them. The 'expensive' option speaks to cost, whereas the "
     "sentence contrasts the cost of the measures with what ordinary cleanliness fails to do."),

 wic("W10",
     "Mali's wealth rested on gold mined south of the empire and taxed as it moved north. When "
     "Mansa Musa passed through Cairo in 1324 he spent and gave away so much of it that the price "
     "of gold in the city's markets was still _____ more than a decade afterwards, a detail "
     "Egyptian chroniclers recorded with some irritation.",
     ["depressed", "climbing", "unrecorded", "fixed"], "A",
     "A large quantity of metal released into one market drives its price down, and the "
     "chroniclers' irritation fits a loss of value that persisted for years. The 'climbing' option "
     "would follow from gold becoming scarce in Cairo, the reverse of what the passage describes."),

 wic("W11",
     "The body's clock is set each day by light reaching a small group of cells in the retina that "
     "respond most strongly to the blue part of the spectrum. Evening light of that kind delays the "
     "clock, pushing the onset of sleepiness later. The effect is _____: an hour of bright screen "
     "light before bed shifts the following night's timing measurably, while the same light at noon "
     "shifts it hardly at all.",
     ["strongly dependent on timing", "negligible in every case",
      "confined to the laboratory", "the same throughout the day"], "A",
     "The colon compares identical light given in the evening and at midday and reports very "
     "different results, so when the light arrives is what governs the outcome. The option calling "
     "the effect the same throughout the day denies precisely the difference the sentence "
     "reports."),

 wic("W12",
     "The tide in the Bay of Fundy rises and falls by as much as sixteen metres, far more than on "
     "the open Atlantic beside it. The bay's length and depth give it a natural period of "
     "oscillation close to the period of the tide itself, so each incoming tide arrives in step "
     "with the water already sloshing in the basin and the two _____ one another.",
     ["reinforce", "cancel", "resemble", "displace"], "A",
     "Arriving in step is the condition under which two oscillations add together, and that is what "
     "produces a range far above the ocean outside. The 'cancel' option describes what happens when "
     "they arrive out of step, the opposite of the situation stated."),

 meaning("W13",
     "A colour woodblock print is built up from a separate block for each colour, and every block "
     "must lay its ink exactly where the last one left the paper clear. Japanese printers cut two "
     "small marks into every block of a set, an angled corner and a straight notch along one edge, "
     "and the sheet is laid against those marks at each pass. Where the marks are cut accurately "
     "the <u>register</u> holds through a dozen impressions.",
     "register",
     ["A formal list kept as a permanent record.",
      "The exact alignment of one printed colour with those already laid down.",
      "The range of pitch available to a voice or an instrument.",
      "A grating through which warm air is admitted to a room."],
     "B",
     "The marks described exist to place each sheet identically so that every colour falls where it "
     "should, and the word names that alignment. The record-keeping sense is the commonest meaning "
     "of the word but has nothing to do with marks cut into a block."),

 meaning("W14",
     "Most named apple varieties began as a single seedling and are propagated only by cutting, so "
     "an orchard of one variety is in effect one tree many times over. Occasionally a single branch "
     "on such a tree bears fruit that ripens earlier, or colours more deeply, than the rest. "
     "Nurseries watch for these, because a <u>sport</u> that keeps its character when grafted onto "
     "fresh rootstock can be introduced as a variety in its own right.",
     "sport",
     ["An activity undertaken for amusement or exercise.",
      "A shoot that differs in character from the tree that bore it.",
      "A person who accepts a setback with good humour.",
      "A display made in order to attract attention."],
     "B",
     "The passage describes a single branch bearing fruit unlike the rest of the tree and then "
     "applies the word to it, so it names that deviating shoot. The amusement sense is the word's "
     "everyday meaning and cannot be grafted onto a rootstock."),

 meaning("W15",
     "A seed bank holds samples rather than varieties. Each lot that arrives, a handful gathered "
     "from one farmer's field in one season, is numbered, dried, sealed and stored apart from every "
     "other lot, because two collections of the same named variety taken from different valleys may "
     "not carry the same genes. A large bank may hold half a million such <u>accessions</u>.",
     "accessions",
     ["Formal acts of coming to a throne or an office.",
      "Distinct samples entered into a collection and kept separately.",
      "Agreements by which a state joins an existing treaty.",
      "Increases in the total quantity of something held."],
     "B",
     "The passage defines what it is counting before it names it: individual numbered lots stored "
     "apart from one another. The 'increase in quantity' sense treats the word as a measure of "
     "growth, but a bank is said to hold half a million of them, which requires countable items."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "The first jet airliner entered service in 1952, and two of them broke up in flight within a "
     "year. Investigators recovered the wreckage from the sea, rebuilt one fuselage inside a water "
     "tank and pumped it up and down through thousands of simulated flights until it split. The "
     "crack began at the corner of a window, where every pressurisation had concentrated a stress "
     "that no single flight would have come near to breaking. Later airliners were built with "
     "rounded openings.",
     "Which choice best states the main purpose of the text?",
     ["To describe how the cause of a series of accidents was identified and what was changed as a result.",
      "To argue that jet airliners were put into service before they were ready.",
      "To explain the principles by which a cabin is held at a comfortable pressure.",
      "To compare the first jet airliner with the piston aircraft it replaced."],
     "A",
     "The text runs from the accidents to the tank test, to the crack at the window corner, to the "
     "rounded openings adopted afterwards, which is an account of a diagnosis and its consequence. "
     "How a cabin is pressurised is taken for granted throughout and never explained."),

 tsp("T2",
     "A workshop can work only to the accuracy of the standards it holds. <u>Carl Edvard Johansson "
     "ground small steel blocks to lengths that could be stacked in combination, so that a set of "
     "about a hundred would build any dimension in the working range to within a fraction of a "
     "micrometre.</u> Two such blocks pressed together adhere strongly enough to be lifted as one. "
     "Machinists who had previously trusted a rule and a practised eye could now set a tool against "
     "a physical length and check it.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It introduces the standards whose availability accounts for the change described at the end of the text.",
      "It explains why two ground steel surfaces adhere when they are pressed together.",
      "It questions whether a practised eye is less accurate than a physical standard.",
      "It describes the market for precision instruments in Johansson's lifetime."],
     "A",
     "The sentence supplies the combinable steel lengths, and the closing sentence has machinists "
     "setting a tool against exactly such a length instead of trusting a rule. Why the surfaces "
     "adhere is asserted in the following sentence and left unexplained there too."),

 tsp("T3",
     "Deliberate infection with material from a mild case of smallpox was practised in Asia and "
     "Africa long before it reached Europe, and it worked: those inoculated usually took a light "
     "illness and were protected afterwards. It also killed a small proportion of them, and every "
     "inoculated person could pass true smallpox to others while ill. Jenner's substitution of "
     "cowpox material kept the protection and removed both objections, since cowpox is mild in "
     "humans and gives no one smallpox to catch.",
     "Which choice best describes the overall structure of the text?",
     ["It describes an established practice, states the drawbacks that came with it, and explains how a later method kept its benefit without them.",
      "It traces the spread of smallpox inoculation from Asia and Africa into Europe.",
      "It argues that Jenner's contemporaries were slow to accept his method.",
      "It contrasts the severity of smallpox with the severity of cowpox in humans."],
     "A",
     "The text sets out the older practice, names two specific costs of it, and then shows the "
     "cowpox method retaining the protection while removing both. Whether the method met resistance "
     "is a question the passage never raises."),

 tsp("T4",
     "A vacuum tube amplifies by controlling a stream of electrons crossing an evacuated space, and "
     "it needs a heated filament to release them. In 1947 two physicists at Bell Laboratories "
     "pressed two gold contacts a fraction of a millimetre apart onto a block of germanium and "
     "found that a small current at one contact controlled a much larger current at the other. "
     "Nothing was heated and nothing was evacuated. The amplification took place inside the solid "
     "itself.",
     "Which choice best states the main purpose of the text?",
     ["To set out what amplification had previously required and to describe a device that dispensed with it.",
      "To explain how impurities are introduced into a crystal of germanium.",
      "To argue that the vacuum tube remained useful after 1947.",
      "To describe the commercial products that followed from the discovery."],
     "A",
     "The opening names the filament and the vacuum a tube depends on, and the rest describes an "
     "arrangement that amplified without either of them. Doping the crystal is a step the text "
     "never mentions."),

 tsp("T5",
     "An oasis garden in the Sahara is planted in three storeys: date palms above, fruit trees "
     "beneath them and vegetables at ground level. <u>The palms are not the most valuable crop but "
     "the condition of the others, since their crowns cut the sun to a fraction of what falls in "
     "the open and slow the wind that would otherwise strip moisture from every leaf below.</u> "
     "Growers who lose a stand of palms lose the plots beneath them within a few seasons.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It explains the role that makes the loss described in the final sentence follow.",
      "It compares the market value of dates with the market value of vegetables.",
      "It identifies the species of fruit tree grown at the middle level.",
      "It concedes that the three-storey arrangement is difficult to maintain."],
     "A",
     "The sentence says the palms supply the shade and shelter the lower plots depend on, which is "
     "why losing them takes those plots with them. Relative value is raised only to be set aside in "
     "favour of the sheltering role."),

 tsp("T6",
     "Living at altitude raises the number of red cells in the blood, which ought to help an "
     "endurance athlete. Training at altitude, though, has to be done slower, because less oxygen "
     "reaches the muscle at every pace. Coaches resolved the conflict by separating the two: "
     "athletes sleep and pass their idle hours high, then descend to train at speeds they could not "
     "hold above. The arrangement asks a great deal of the logistics and very little of the "
     "physiology.",
     "Which choice best states the main purpose of the text?",
     ["To describe two conflicting effects of altitude and the arrangement that captures one while avoiding the other.",
      "To argue that altitude confers no advantage at all on endurance athletes.",
      "To explain the process by which the body produces additional red cells.",
      "To recommend a particular elevation for an athlete's sleeping quarters."],
     "A",
     "The text names the benefit of living high and the cost of training high, then describes "
     "sleeping high and training low as the way of taking one without the other. How red cells are "
     "produced is asserted in the first sentence and never explained."),

 # ---------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "Hops were put into beer long before anyone could say what they did. Boiling the cone in the "
     "wort converts its resins into compounds that are bitter and, more usefully, hostile to the "
     "lactic bacteria that would otherwise sour a cask within weeks. A heavily hopped beer "
     "therefore survived a voyage that a lightly hopped one did not. Brewers who selected for "
     "bitterness were selecting, without knowing it, for keeping quality.",
     "Which choice best states the main idea of the text?",
     ["The bitterness hops give beer is inseparable from a preservative effect that brewers exploited before they understood it.",
      "Hops were the only means available for preserving beer on a long voyage.",
      "Lactic bacteria are the principal cause of spoilage in every fermented drink.",
      "Brewers deliberately chose hop varieties for their antibacterial compounds."],
     "A",
     "The passage traces one chemical change to both the taste and the resistance to souring, then "
     "says brewers chose for the first without knowing of the second. The option describing a "
     "deliberate choice of antibacterial varieties contradicts that closing sentence."),

 cid("C2",
     "Slate splits into sheets a few millimetres thick because the clay minerals in it were "
     "flattened into parallel alignment when the rock was squeezed during mountain building. That "
     "alignment has nothing to do with the original bedding of the mud, and in many quarries the "
     "two run across each other. A splitter works to the cleavage and ignores the bedding, which is "
     "why a good roofing slate may show its old sedimentary layers running diagonally across the "
     "face.",
     "Which choice best states the main idea of the text?",
     ["Slate splits along a fabric produced by later deformation rather than along the layers in which it was deposited.",
      "Roofing slates are cut to a standard thickness of a few millimetres.",
      "Quarries prefer slate in which the bedding and the cleavage run in the same direction.",
      "The clay minerals in slate are aligned as the mud settles on the sea floor."],
     "A",
     "The passage separates the squeezed alignment that governs splitting from the original bedding "
     "and notes that the two often cross, which is why old layers show diagonally on a finished "
     "slate. Placing the alignment at the moment of deposition reverses the sequence the passage "
     "sets out."),

 cid("C3",
     "Arabic accounts of the eleventh century describe the capital of Ghana as two towns some "
     "distance apart. One held the king, his court and a sacred grove closed to outsiders; the "
     "other held Muslim merchants, a dozen mosques and the scholars who kept the accounts of the "
     "trade. The king taxed every load of salt entering and leaving the country, and he drew his "
     "authority from the older town while the wealth that paid for it passed through the newer "
     "one.",
     "Which choice best states the main idea of the text?",
     ["The capital's two settlements separated the sources of the king's authority from the sources of his revenue.",
      "Ghana's kings adopted Islam in order to secure the loyalty of the merchants.",
      "The salt trade was controlled entirely by scholars resident in the merchant town.",
      "The two towns were laid out at the same date and to the same plan."],
     "A",
     "The closing sentence assigns authority to the older town and wealth to the newer, and the "
     "description of each town supports that division. Nothing states that the kings adopted Islam, "
     "and the sacred grove closed to outsiders points the other way."),

 cid("C4",
     "A medieval book was not written page by page. Sheets were folded once, gathered in groups of "
     "four or five and sewn through the fold, so that a scribe writing on what would become the "
     "first page of a gathering was writing on the same physical sheet as its last. Copying "
     "therefore required the length of the text to be judged in advance, since a passage that ran "
     "long could not be given an extra leaf without disturbing the whole gathering.",
     "Which choice best states the main idea of the text?",
     ["The way a book's sheets were folded and sewn obliged the scribe to plan the length of the text before writing.",
      "Medieval scribes copied texts one page at a time and in the order a reader would meet them.",
      "Gatherings of four or five sheets proved stronger than gatherings of a single sheet.",
      "Judging the length of a text was the binder's responsibility rather than the scribe's."],
     "A",
     "The passage explains that one sheet carries both an early and a late page of a gathering and "
     "concludes that the length had to be judged before writing began. The option describing "
     "page-by-page copying is the practice the first sentence denies."),

 cid("C5",
     "An oscillating water column is a chamber open to the sea below the waterline and open to the "
     "air through a duct above it. Each passing wave drives the water inside up and down, and the "
     "trapped air is pushed out through the duct and drawn back in. The turbine in the duct is "
     "built to turn the same way whichever direction the air is moving, so no valve is needed and "
     "the only moving part sits above the water, out of reach of the sea.",
     "Which choice best states the main idea of the text?",
     ["The design converts wave motion into airflow so that its one moving part can be kept clear of the water.",
      "Waves of greater height produce proportionally more power in such a chamber.",
      "Valves are the component of a wave-energy device most likely to fail.",
      "The turbine must be reversed each time the direction of the airflow changes."],
     "A",
     "The passage follows the wave to the water column, the column to the air and the air to the "
     "turbine, then notes that the moving part sits above the water and out of the sea's reach. The "
     "option about reversing the turbine contradicts the statement that it turns the same way in "
     "either airflow."),

 cid("C6",
     "Nikolai Vavilov collected seed on five continents and noticed that the varieties of a given "
     "crop are not spread evenly across the world. Wheat showed most of its diversity in a band "
     "running through the Caucasus and the Near East; potatoes showed theirs in the Andes. He "
     "proposed that a crop's diversity is greatest where it was first domesticated, because the "
     "longest period of cultivation has produced the largest number of local forms.",
     "Which choice best states the main idea of the text?",
     ["Vavilov inferred where a crop was first domesticated from where its varieties are most numerous.",
      "Vavilov's collections showed that wheat and potatoes were domesticated at about the same date.",
      "Crop varieties are distributed evenly wherever the crop is grown commercially.",
      "The Andes hold more varieties of every major crop than any other region."],
     "A",
     "The passage reports the uneven distribution he found and then the principle he drew from it, "
     "which ties maximum diversity to the place of first domestication. The claim of even "
     "distribution is exactly what his observations are said to contradict."),

 # ---------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "An autogyro's rotor is not driven; air flowing up through it as the machine moves forward "
     "keeps it turning. The earliest machines rolled over on take-off, because the blade advancing "
     "into the airflow generated more lift than the blade retreating from it. Engineer Juan de la "
     "Cierva argued that the imbalance had to be relieved at the root of each blade rather than "
     "corrected by the pilot at the controls.",
     "Which finding, if true, would most directly support Cierva's argument?",
     ["Machines whose blades were mounted on hinges that let each blade rise and fall freely through every revolution took off without rolling, while machines with rigid blades of the same profile continued to roll.",
      "Autogyro rotors turn more slowly than the powered rotors of helicopters.",
      "Pilots of the earliest autogyros reported that the roll developed too quickly to be caught.",
      "The lift a blade produces increases with the square of its speed through the air."],
     "A",
     "Comparing hinged blades with rigid blades of the same profile isolates the mounting at the "
     "root as the thing that cures the roll, which is the claim at issue. The report that the roll "
     "developed too quickly to catch shows only that the pilot could not react in time, leaving "
     "open where in the machine the remedy had to be applied."),

 coe("E2",
     "Lager yeast is a hybrid: half its genome comes from the ale yeast long used in brewing, and "
     "the other half from a cold-tolerant relative that went unrecorded in the wild for more than a "
     "century after the hybrid was first described. Geneticist Marisol Arrieta argues that the "
     "missing parent is a species living in the beech forests of Patagonia rather than a European "
     "organism that has since died out.",
     "Which finding, if true, would most directly support Arrieta's argument?",
     ["The non-ale half of the lager genome differs from the Patagonian species by about the amount expected from a few centuries of separation, and by far more from every European yeast yet sequenced.",
      "The Patagonian species grows well at the low temperatures at which lager is fermented.",
      "Lager brewing was first recorded in Bavaria in the fifteenth century.",
      "Hybrid yeasts arise readily when two species are cultured together in a laboratory."],
     "A",
     "A close genomic match to the Patagonian species together with a distant one to every European "
     "yeast is what descent from that particular parent predicts and what an extinct European "
     "parent could not produce. Cold tolerance is shared by many yeasts and would be expected of "
     "any plausible parent, so it fails to separate the two accounts."),

 coe("E3",
     "A running shoe's midsole compresses when the foot lands and pushes back as it leaves the "
     "ground, and the fraction of the stored energy it returns rather than losing as heat differs "
     "from foam to foam. Four foams were tested on the same machine at the same compression, and "
     "the oxygen cost of running in shoes built from each was measured on one group of runners at a "
     "fixed pace. Biomechanist Idris Fanning argues that the saving in oxygen cost tracks the "
     "energy a midsole returns rather than the family of material it belongs to."
     "<table style=\"border-collapse:collapse;margin:0.75rem 0;\">"
     "<tr>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Midsole foam</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Energy returned (%)</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Oxygen cost (mL/kg/km)</th>"
     "</tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Conventional EVA</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">66</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">213</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Compression-moulded EVA</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">71</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">210</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Polyether block amide</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">87</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">199</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Supercritical foamed TPU</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">84</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">201</td></tr>"
     "</table>",
     "Which choice most effectively uses data from the table to support Fanning's argument?",
     ["The polyether block amide midsole returned 87 per cent of the stored energy and gave the lowest oxygen cost, 199 mL/kg/km, while the conventional EVA returned 66 per cent and gave the highest, 213 mL/kg/km.",
      "The two EVA midsoles returned 66 per cent and 71 per cent of the stored energy respectively.",
      "The supercritical foamed TPU returned 84 per cent of the stored energy, slightly less than the polyether block amide.",
      "The conventional EVA gave an oxygen cost of 213 mL/kg/km, the highest of the four foams tested."],
     "A",
     "The argument needs the extremes of energy return paired with the extremes of oxygen cost, and "
     "only the response quoting both figures for the best foam and for the worst supplies that "
     "pairing. Giving the highest oxygen cost on its own reports one value with no energy return "
     "set against it."),

 coe("E4",
     "Two maternity wards of the Vienna General Hospital admitted women on alternate days. Deaths "
     "from puerperal fever in the ward staffed by medical students ran at three or four times the "
     "rate in the ward staffed by midwives, and the students came to the ward directly from the "
     "dissecting room. Physician Ignaz Semmelweis argued that the students were carrying something "
     "from the cadavers to the women they then examined.",
     "Which finding, if true, would most directly support Semmelweis's argument?",
     ["After the students were required to scrub their hands in a chlorinated solution before entering the ward, deaths there fell within months to the rate recorded among the midwives.",
      "The two wards admitted women in similar numbers over the course of a year.",
      "Puerperal fever was reported from maternity hospitals across Europe in the same period.",
      "Medical students received more hours of instruction in anatomy than midwives did."],
     "A",
     "Removing the material from the students' hands and watching the gap between the wards close "
     "is what a carried agent predicts and what no other difference between the two staffs would "
     "explain. More hours of anatomy teaching restates the exposure without testing whether it was "
     "the cause."),

 coe("E5",
     "A worker on a night shift is awake through the hours when the internal clock is calling most "
     "strongly for sleep, and the effect does not wear off with experience. Errors recorded at a "
     "single plant over three years were sorted by how long the worker had been on duty, separately "
     "for shifts beginning at 07:00 and at 23:00. Occupational physician Bettina Kruse argues that "
     "the risk follows the clock rather than the time spent working."
     "<table style=\"border-collapse:collapse;margin:0.75rem 0;\">"
     "<tr>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Hours on duty</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Errors per thousand operations, shift starting 07:00</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Errors per thousand operations, shift starting 23:00</th>"
     "</tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">1 to 2</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">1.8</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">4.1</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">3 to 4</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">2.0</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">5.6</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">5 to 6</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">2.4</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">6.8</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">7 to 8</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">2.9</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">5.2</td></tr>"
     "</table>",
     "Which choice most effectively uses data from the table to support Kruse's argument?",
     ["On the night shift the error rate peaked at 6.8 per thousand after five to six hours on duty and then fell to 5.2, whereas on the day shift it climbed steadily from 1.8 to 2.9 across the same eight hours.",
      "The night shift recorded 4.1 errors per thousand operations in its first two hours, more than twice the day shift's 1.8.",
      "The day shift's error rate rose from 1.8 to 2.9 errors per thousand operations over eight hours on duty.",
      "Both shifts recorded fewer than seven errors per thousand operations in every period measured."],
     "A",
     "The argument requires the night rate to turn back down while the hours on duty go on rising, "
     "and only the response quoting the peak at five to six hours, the fall after it and the steady "
     "day-shift climb contains that comparison. The difference in the opening hours shows the night "
     "shift is worse from the start without showing that its pattern follows the clock."),

 coe("E6",
     "A twelfth-century copy of Boethius carries no colophon, the note in which a scribe recorded "
     "where and when he finished a book, and successive catalogues have assigned it to three "
     "different houses in the Low Countries and northern France. Palaeographer Aldo Ferrini argues "
     "that it was written at the abbey of Saint-Amand rather than at any of the others that have "
     "been proposed for it.",
     "Which finding, if true, would most directly support Ferrini's argument?",
     ["The manuscript's ruling pattern, its unusual system of abbreviation and the shape of its ampersand all match dated books written at Saint-Amand within the same decade, and none of the three appears in books from the other houses proposed.",
      "Saint-Amand is known to have owned a copy of Boethius in the twelfth century.",
      "The manuscript is written on calfskin, as most books of the period were.",
      "The text of the manuscript agrees closely with the version circulating in northern France."],
     "A",
     "A cluster of scribal habits shared with dated books from one house and absent from the others "
     "points to the place where the copying was done, which is what the claim concerns. That a "
     "house owned a copy of the work shows only that such a book reached its library, which any of "
     "the proposed houses might equally have managed."),

 coe("E7",
     "Most apple varieties will not set fruit from their own pollen, so an orchard carries a second "
     "variety among the rows to supply it. Growers disagree about how close those trees have to "
     "stand. One block of a single variety, whose pollinizer trees stood about twenty metres apart, "
     "was surveyed after flowering, and the proportion of flowers setting fruit was recorded by "
     "distance from the nearest pollinizer. Pomologist H&eacute;l&egrave;ne Duclos argues that the "
     "spacing used in the block was too wide."
     "<table style=\"border-collapse:collapse;margin:0.75rem 0;\">"
     "<tr>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Distance to nearest pollinizer tree</th>"
     "<th style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;\">Flowers setting fruit (%)</th>"
     "</tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Under 6 m</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">41</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">6 to 12 m</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">34</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">12 to 18 m</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">22</td></tr>"
     "<tr><td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">Over 18 m</td>"
     "<td style=\"border:1px solid #D9DEE5;padding:0.35rem 0.6rem;\">11</td></tr>"
     "</table>",
     "Which choice most effectively uses data from the table to support Duclos's argument?",
     ["Fruit set fell from 41 per cent within six metres of a pollinizer to 11 per cent beyond eighteen metres, so trees in a block whose pollinizers stand twenty metres apart set a fraction of the fruit they might.",
      "Fruit set was 34 per cent at distances of six to twelve metres from the nearest pollinizer.",
      "Fruit set beyond eighteen metres from a pollinizer was 11 per cent.",
      "Fruit set at twelve to eighteen metres was a little over half the figure recorded within six metres."],
     "A",
     "The argument is about the spacing actually used, so it needs the fall across the whole range "
     "tied back to the twenty-metre spacing in the block, which only one response supplies. The "
     "figure for the farthest band alone gives the low end with nothing to compare it against and "
     "no mention of the spacing at all."),

 coe("E8",
     "Before 1959 a transistor's junctions were exposed at the surface of the crystal, where a "
     "trace of moisture or sodium could change how the device behaved, and yields were poor. Jean "
     "Hoerni's planar process grew a layer of silicon dioxide over the whole wafer, cut windows in "
     "it for the doping steps and left the oxide in place afterwards. Historian Vikram Sethi argues "
     "that leaving the oxide on the finished device, rather than the patterning it made possible, "
     "was what the industry gained most from.",
     "Which finding, if true, would most directly support Sethi's argument?",
     ["Devices made by the new process and then stripped of their oxide drifted as badly as the older ones, while identical devices that kept the oxide held their characteristics through the same tests.",
      "The planar process allowed several transistors to be formed on one piece of silicon and connected by metal laid over the oxide.",
      "Silicon dioxide can be grown on a silicon wafer simply by heating it in oxygen.",
      "Yields at several plants improved in the years after the planar process was introduced."],
     "A",
     "Stripping the oxide from finished devices and watching them fail while identical devices that "
     "keep it do not isolates the surviving layer as the source of the benefit. Connecting several "
     "transistors over the oxide credits the patterning, which is the alternative being argued "
     "against."),

 coe("E9",
     "A kangaroo rat lives on dry seed and has never been seen to drink. Its kidneys concentrate "
     "urine further than those of almost any other mammal, and the passages of its nose are cool "
     "enough that much of the water in its breath condenses before it leaves the body. Zoologist "
     "Renata Okonjo argues that the animal's water comes chiefly from the oxidation of its food "
     "rather than from moisture the seeds have taken up from the air.",
     "Which finding, if true, would most directly support Okonjo's argument?",
     ["Animals fed seed dried to constant weight and held in air below five per cent humidity maintained their body mass as well as animals given seed stored in a damp burrow.",
      "Seeds stored in a burrow take up a measurable quantity of water from the air around them.",
      "The animal's kidneys concentrate urine about four times as far as a laboratory rat's do.",
      "Kangaroo rats forage at night, when the air near the ground is coolest."],
     "A",
     "Removing every trace of absorbed moisture from the diet and finding the animals unaffected "
     "leaves oxidation of the food as the remaining source of water. That seeds in a burrow take up "
     "water supports the competing account rather than the one at issue."),

 # ------------------------------------------------------------- Inferences (6)
 inf("I1",
     "The pivot at the end of a balance staff is thinner than a hair, and it turns in its bearing "
     "several hundred thousand times a day. A brass bearing wears into an oval within a few years, "
     "and a pivot running in an oval hole no longer keeps a fixed centre. Ruby is far harder than "
     "brass and takes a polish that brass cannot hold. A maker who fits ruby bearings at the "
     "fastest-turning pivots is therefore chiefly buying _____",
     ["a rate that stays true for far longer than the brass version's would.",
      "a lower cost of manufacture for the movement as a whole.",
      "a watch that needs to be wound less frequently.",
      "protection against magnetic fields near the balance."],
     "A",
     "The passage links wear in the bearing to the loss of a fixed centre and so to the loss of an "
     "accurate rate, which a harder bearing postpones. Winding frequency depends on the mainspring, "
     "which the passage never mentions."),

 inf("I2",
     "Granite carries a grain: it parts more readily along one direction than along the two at "
     "right angles to it, a property quarrymen judge by eye and by the sound of a hammer. A row of "
     "shallow holes is drilled along the intended line and a pair of shims and a wedge driven into "
     "each in turn until the block splits. Where that line runs across the grain rather than with "
     "it, the same row of holes _____",
     ["has to be drilled at closer spacing if the break is to follow it.",
      "produces a face far smoother than one split along the grain.",
      "parts the block with less effort than a line along the grain.",
      "makes no difference to the direction the break will take."],
     "A",
     "Splitting against the easier direction means the rock is less willing to part, so the wedges "
     "must be set closer together to force the break onto the intended line. The response promising "
     "less effort reverses the property the opening sentence establishes."),

 inf("I3",
     "Most crop seeds can be dried to a few per cent moisture and held at minus twenty degrees for "
     "decades, and a bank stores them in sealed foil packets. The seeds of cacao, mango and many "
     "forest trees are killed by that drying: the embryo is damaged as the last of the water leaves "
     "it, and no amount of care at the freezing stage brings it back. A collection intending to "
     "hold such species must therefore _____",
     ["keep them by some means other than the dried and frozen packet.",
      "dry them more slowly than it dries the seeds of cereals.",
      "store them at a temperature a little above minus twenty degrees.",
      "collect them more often than it collects cereal seed."],
     "A",
     "The damage is done by the removal of the water itself and is not repaired by anything that "
     "follows, so the standard route is closed and another has to be found. Drying more slowly "
     "still ends with the water gone, which is the step the passage says kills the embryo."),

 inf("I4",
     "The output of a wind farm can be forecast a day or two ahead and no further, because the "
     "weather cannot be forecast further. Tides are driven by the positions of the moon and the "
     "sun, which are known centuries in advance, so the output of a tidal generator can be "
     "tabulated years before it is produced. A tidal station and a wind farm of equal average "
     "output are therefore not equivalent to a grid operator, because the tidal station _____",
     ["allows the rest of the system to be scheduled around it far ahead of time.",
      "delivers its power at a steadier rate through the day.",
      "can be relied on to be generating during periods of peak demand.",
      "removes any need to hold other plant in reserve."],
     "A",
     "The difference the passage draws is between output that can be known years ahead and output "
     "that cannot, and knowing it in advance is what lets everything else be planned around it. "
     "Steadiness is a separate property, and a flow that stops four times a day is not steady."),

 inf("I5",
     "The fibres in ordinary wood pulp are a few millimetres long and are cut shorter still in "
     "processing. The inner bark of the paper mulberry yields fibres several times that length, and "
     "the Japanese papermaker keeps them long, beating them only enough to separate one from "
     "another. A sheet's strength comes from the number of points at which its fibres cross and "
     "cling. A sheet of long-fibred paper can therefore be made very thin and still _____",
     ["hold together under handling.",
      "take up more ink than a thicker sheet would.",
      "be produced more cheaply than a sheet of wood pulp.",
      "resist yellowing over very long periods."],
     "A",
     "Strength is attributed to fibres crossing and clinging, and long fibres go on making those "
     "crossings even in a very thin sheet, so thinness need not cost strength. Ink absorption and "
     "cost are properties the passage says nothing about."),

 inf("I6",
     "A runner's Achilles tendon stretches as the foot takes the body's weight and shortens again "
     "as the foot leaves the ground, returning most of the energy that stretched it. Muscle, by "
     "contrast, must burn fuel to produce the same force. The share of a stride's work done by the "
     "tendon rises as the stride rate rises, since a quicker cycle leaves the tendon less time to "
     "shed its stored energy as heat. Two runners holding one speed, one with a short quick stride "
     "and one with a long slow one, will therefore differ in _____",
     ["how much of the work of each stride is paid for by fuel burned in muscle.",
      "the total distance each covers in a given time.",
      "the elastic properties their tendons possess.",
      "the number of muscles each recruits in the lower leg."],
     "A",
     "The passage says the tendon's share of the work rises with stride rate, and whatever the "
     "tendon does not supply has to be produced by muscle burning fuel. Distance covered in a given "
     "time is fixed by the stated condition that both runners are holding one speed."),

 # ------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "A glider has no engine and sinks steadily through still air, so a cross-country flight is "
     "made entirely out of the height the air itself supplies. Warm ground releases columns of "
     "rising air through the middle of the day, and a pilot flies from one column to the _____ "
     "climbs in each of them and gives most of that height back on the glide to the next.",
     ["next; the aircraft", "next, the aircraft", "next the aircraft", "next: and the aircraft"],
     "A",
     "Two complete statements meet at the blank with no conjunction between them, and the semicolon "
     "is the mark that joins a pair like that. The comma alone leaves a splice, and with no mark at "
     "all the two statements run together with no boundary."),

 bnd("B2",
     "Wine left open to the air turns to vinegar, because a film of bacteria settles on the surface "
     "and oxidises the alcohol. Vinegar makers keep that film alive from batch to batch, and since "
     "the organisms need air as much as the yeast before them needed its _____ vessels are broad "
     "and shallow rather than deep and narrow.",
     ["absence, the", "absence; the", "absence: the", "absence and the"], "A",
     "The clause opening with 'since' is dependent, and a dependent clause standing in front of its "
     "main clause is closed off with a comma. Both the semicolon and the colon require a complete "
     "sentence in front of them, which a dependent clause is not."),

 bnd("B3",
     "A pendulum will not go on swinging by itself, and a falling weight left to itself would run "
     "down in seconds. The lever escapement does two things at _____ small push delivered to the "
     "balance at every swing, and a count of those swings taken by releasing the train one tooth at "
     "a time.",
     ["once: a small", "once; a small", "once, and a small", "once a small"], "A",
     "The words before the blank form a complete sentence announcing two things, and the colon is "
     "the mark that introduces the phrases naming them. The semicolon would require a complete "
     "sentence after it, and what follows is a pair of noun phrases."),

 bnd("B4",
     "Marble is quarried in benches from the mountainside above Carrara, and a wire loaded with "
     "abrasive cuts each block free along three faces. Michelangelo, who spent months in the "
     "quarries choosing stone before he would begin a _____ blocks rejected on the mountain rather "
     "than have them carted to Florence and found faulty there.",
     ["figure, left", "figure; left", "figure: left", "figure left"], "A",
     "The relative clause describing him was opened with a comma and must be closed with a matching "
     "comma before the verb belonging to the subject. Leaving the mark out runs the clause straight "
     "into the predicate."),

 bnd("B5",
     "A dessert apple makes a thin cider, since it carries almost no tannin. The varieties grown "
     "for cider in Somerset are barely edible raw, and their tannin is what gives the finished "
     "drink its body, so the orchards planted for the press are quite unlike the orchards planted "
     "for the _____ trees in them would disappoint anyone who picked one.",
     ["table; the", "table, the", "table the", "table: and the"], "A",
     "Two independent statements sit either side of the blank with no conjunction between them, "
     "which is the semicolon's work. A comma in that position produces a splice."),

 bnd("B6",
     "Ragusa ordered arriving ships to wait thirty days offshore in 1377, and Venice later extended "
     "the wait to forty. The number was not arrived at by measuring anything; it came from the "
     "length of a fast in scripture. It happened nonetheless to exceed the incubation period of "
     "plague, so a ship whose crew was still well after forty days was in fact _____ was a piece of "
     "luck nobody at the time was in a position to know about.",
     ["safe, which", "safe; which", "safe: which", "safe. Which"], "A",
     "The clause beginning 'which was a piece of luck' is a non-essential relative clause and "
     "attaches to the main clause with a comma. The semicolon and the full stop each need an "
     "independent clause after them, and a relative clause is not one."),

 bnd("B7",
     "A medieval reader wrote in the margins as a matter of course, and the notes are often more "
     "revealing than the text beside them. Every kind of mark found in one Bodleian manuscript "
     "&mdash; a pointing hand, a cross-reference, an English translation above a Latin _____ a "
     "reader working slowly, and not one of them was made by the scribe who copied the book.",
     ["word &mdash; suggests", "word, suggests", "word; suggests", "word: suggests"], "A",
     "The list of marks was opened with a dash, so a matching dash is needed to close it before the "
     "sentence resumes. Closing with a comma leaves the opening dash without its partner and blurs "
     "where the interruption ends."),

 bnd("B8",
     "Rain in the Negev falls in a handful of storms a year and runs off the stony slopes almost as "
     "fast as it lands. The farmers of the first century built low walls across the wadi floors and "
     "channels down the hillsides above them, and what those works gathered was the one thing the "
     "fields could not otherwise _____ from an area of hillside many times the size of the plot it "
     "watered.",
     ["get: runoff", "get; runoff", "get, runoff", "get runoff"], "A",
     "The words before the blank form a complete sentence, and what follows names the very thing "
     "that sentence has just pointed at, which is the colon's function. The comma on its own "
     "splices two statements together, and the semicolon would need a complete sentence after it."),

 bnd("B9",
     "Every chip begins in a crucible of molten silicon. A seed crystal is touched to the surface "
     "and drawn slowly upward while it turns, and the melt freezes onto it in the seed's own "
     "orientation, so the whole ingot grows as a single _____ boule two metres long may contain no "
     "grain boundary at all.",
     ["crystal; a", "crystal, a", "crystal a", "crystal: and a"], "A",
     "The blank falls between two complete statements with no conjunction between them, so the "
     "semicolon is the mark required. The comma alone gives a splice, and with no mark at all "
     "'crystal a boule' reads as two nouns jammed together."),

 bnd("B10",
     "Gold dust served as currency in Asante, and every trader carried a set of small brass weights "
     "to measure it out. Because a weight had to be recognisable at a glance and impossible to "
     "confuse with its neighbour on the _____ cast them as beetles, sandals, drums and knotted "
     "cords rather than as plain geometric blocks.",
     ["scale, casters", "scale; casters", "scale: casters", "scale and casters"], "A",
     "The clause opening with 'Because' is dependent and is closed off with a comma before the main "
     "clause begins. The semicolon and the colon each require a complete sentence in front of "
     "them."),

 bnd("B11",
     "A traveller's body clock does not jump to the new time; it moves an hour or so a day until it "
     "arrives. Nothing about the flight itself alters that rate of _____ for a few days after "
     "landing the traveller is living on two schedules at once, one set by the sun outside and one "
     "still set by the city left behind.",
     ["adjustment, and", "adjustment; and", "adjustment: and", "adjustment and"], "A",
     "Two independent clauses joined by the coordinating conjunction 'and' take a comma in front of "
     "that conjunction. Neither the semicolon nor the colon is used before a coordinating "
     "conjunction, and dropping the comma altogether leaves two full clauses unseparated."),

 bnd("B12",
     "Every high jumper before 1968 crossed the bar face down, and the landing area was a pit of "
     "sand or wood chips that would never have received a jumper's back. Foam landing beds, "
     "introduced in the years just before the Mexico City _____ a jumper to land on the shoulders "
     "in safety, and the backward technique became possible in practice as well as on paper.",
     ["Games, allowed", "Games; allowed", "Games: allowed", "Games allowed"], "A",
     "The phrase saying when the beds were introduced was opened with a comma and must be closed "
     "with a matching comma before the verb that belongs to the subject. Any other mark breaks the "
     "sentence at a point where the subject has not yet reached its verb."),

 # ------------------------------------------------ Form, Structure, and Sense (9)
 fss("F1",
     "An ejection seat has to clear the tail of the aircraft before the parachute opens, and the "
     "whole sequence takes under two seconds from the moment the handle is pulled. Because nothing "
     "in it can be tested twice, the seat's main charge, along with the drogue gun and the two "
     "barostatic timers, _____ replaced after every live firing.",
     ["are", "have been", "is", "were"], "C",
     "The subject is the singular noun 'charge'; the interrupting phrase beginning 'along with' "
     "does not make a singular subject plural, and the sentence states standing practice rather "
     "than a completed past event."),

 fss("F2",
     "A washed-rind cheese is wiped with brine every few days as it matures, which favours one "
     "group of bacteria on the surface over the moulds that would otherwise take hold. By the time "
     "the cheesemaker cut into the first wheel of the new make, the rind _____ a deep orange that "
     "the earlier batches had never reached.",
     ["turns", "had turned", "will turn", "is turning"], "B",
     "The colour change was complete before the wheel was cut, and the cutting is itself in the "
     "past, so the past perfect is what places one past event before another."),

 fss("F3",
     "A dividing engine cuts the teeth of a wheel by indexing a blank round a master plate one step "
     "at a time, and a worn plate spoils every wheel cut from it. Each of the three engines in the "
     "workshop _____ its own master plate, its own worm and a spindle that has never been taken "
     "out.",
     ["have", "has", "having", "were having"], "B",
     "'Each' is the subject of the sentence and is singular; the prepositional phrase naming three "
     "engines does not change the number of the subject."),

 fss("F4",
     "A fruit tree will not break dormancy until it has spent enough hours below about seven "
     "degrees, and a mild winter leaves the buds opening raggedly in spring. The number of such "
     "hours a variety requires _____ from under three hundred in some Californian selections to "
     "more than a thousand in the old northern kinds.",
     ["range", "ranges", "have ranged", "are ranging"], "B",
     "The subject is 'the number', which is singular, and the words following it name what is being "
     "counted rather than replacing the subject. The plural verb would agree with 'hours', which "
     "sits inside a modifying clause."),

 fss("F5",
     "Goitre was common through the Alps and around the American Great Lakes until iodine began to "
     "be added to table salt in the 1920s. The health office's brief was to license the additive, "
     "to persuade the salt companies to adopt it and _____ the result in schoolchildren over the "
     "following decade.",
     ["measuring", "to measure", "it measured", "having measured"], "B",
     "The three items joined by 'and' all follow 'was to', and the first two are infinitives, so "
     "the third has to be an infinitive as well. The gerund and the finite clause each break the "
     "parallel structure."),

 fss("F6",
     "A binder working from a stack of loose gatherings needs to know which one follows which, and "
     "the scribe supplies the answer at the foot of the last page: the opening word or two of the "
     "gathering to come. Checking those catchwords against the first words of each gathering, "
     "_____",
     ["the order of the book was quickly established.",
      "a misbound quire was found near the middle of the volume.",
      "the cataloguer established the order of the book in an afternoon.",
      "there turned out to be a quire out of place near the middle."],
     "C",
     "The opening participial phrase has to describe whoever did the checking, and only the version "
     "beginning with the cataloguer supplies that subject. Beginning with the order of the book "
     "says that the order was doing the checking."),

 fss("F7",
     "Two drives of the same model were opened after a decade in a server room, one from a bay with "
     "a working fan and one from a bay whose fan had failed early. The wear on the bearings of the "
     "hotter drive is roughly double _____ found on the drive that stayed cool.",
     ["that", "those", "them", "which"], "A",
     "The pronoun stands in for the singular noun 'wear', so the singular form is required; the "
     "plural would need a plural antecedent and the sentence supplies none."),

 fss("F8",
     "A print is taken without a press: the printer lays the paper on the inked block and rubs the "
     "back of the sheet with a disc of coiled cord wrapped in a bamboo sheath. The studio kept a "
     "rack of six such discs and inspected all six _____ sheaths at the end of every week, since a "
     "split sheath scores the paper.",
     ["discs", "disc's", "discs'", "discs's"], "C",
     "The sheaths belong to all six of the tools, so the noun has to be plural and possessive at "
     "once, which puts the apostrophe after the plural ending. The singular possessive would credit "
     "the sheaths to one disc only."),

 fss("F9",
     "A blade left in a tidal race gathers barnacles and weed within a season, and a fouled blade "
     "loses efficiency long before it loses strength. The two turbines lifted for inspection last "
     "autumn were among the few in the array that _____ never been cleaned in service.",
     ["has", "have", "having", "is"], "B",
     "The relative pronoun refers back to 'the few', which is plural, so the plural verb is "
     "required; the singular would agree with a single turbine, which is not what the clause "
     "describes."),

 # -------------------------------------------------------------- Transitions (9)
 trn("N1",
     "A rivet head standing proud of a wing skin trips the airflow passing over it, and an aircraft "
     "carries tens of thousands of rivets. Countersinking every hole so that the head sits flush "
     "costs more to build and complicates every later repair. _____ every aircraft designed for "
     "high speed is built that way, because the drag saved across thirty years of service dwarfs "
     "the extra cost of assembly.",
     ["Nonetheless,", "Consequently,", "Likewise,", "In short,"], "A",
     "Flush riveting is adopted in spite of the costs just listed, so the transition has to concede "
     "a contrast. Treating it as a consequence would make the extra expense the reason for choosing "
     "the method."),

 trn("N2",
     "Limestone dissolves slowly in rainwater made faintly acid by the air, and a wall exposed to "
     "driving rain is washed clean of the crust that forms on it. _____ the sheltered parts of the "
     "same facade, under a cornice or behind a column, gather a black skin of gypsum and soot that "
     "eats into the carving beneath.",
     ["By contrast,", "Consequently,", "In addition,", "For example,"], "A",
     "The sheltered surfaces behave in the opposite way to the washed ones just described, so the "
     "transition sets the two against each other. Presenting the second as a consequence would make "
     "the washing of exposed stone the cause of the crust elsewhere."),

 trn("N3",
     "A mobile dune advances by rolling sand over its crest, and marram or spinifex planted on the "
     "windward face traps that sand before it reaches the top. _____ the planting holds only while "
     "the roots survive, and a single season of drought on a stabilised dune can put it back in "
     "motion within months.",
     ["However,", "Therefore,", "Likewise,", "For instance,"], "A",
     "The failure of the planting works against the effect just described, so the transition marks "
     "a contrast rather than a consequence."),

 trn("N4",
     "The number of transistors on a chip doubled roughly every two years for four decades, and the "
     "doubling was never a law of physics but a target the industry organised itself to meet. "
     "Equipment makers, materials suppliers and circuit designers all planned to one published "
     "schedule. _____ the pace was in large part a prediction that the industry arranged to "
     "fulfil.",
     ["In other words,", "Nevertheless,", "For instance,", "Meanwhile,"], "A",
     "The closing sentence states in general terms what the coordinated planning just described "
     "amounts to, which makes it a restatement. It is not a further instance, since it introduces "
     "no new case."),

 trn("N5",
     "The internal clock is reset each morning by light, and without that daily correction it runs "
     "on a cycle of its own, typically a little longer than twenty-four hours. _____ some people "
     "with no light perception at all sleep well for a fortnight and badly for the next, in a cycle "
     "that repeats indefinitely as their clock drifts through the calendar.",
     ["Consequently,", "Nevertheless,", "Similarly,", "In contrast,"], "A",
     "The drifting sleep pattern follows directly from a clock that never receives its daily "
     "correction, which is a cause-and-effect relation. No contrast is being drawn between the two "
     "sentences."),

 trn("N6",
     "Water is some eight hundred times denser than air, so a tidal turbine draws as much power "
     "from a slow current as a wind turbine draws from a fast wind, and it does so with far smaller "
     "blades. _____ that same density loads the blades much more heavily, and the machines have to "
     "be built to a strength no wind turbine requires.",
     ["However,", "For example,", "Similarly,", "As a result,"], "A",
     "The heavy loading is a penalty set against the advantage just stated, so a contrastive "
     "transition is what the relation calls for. Presenting it as a result would suggest the "
     "smaller blades brought the loading about, whereas the passage traces both to the density of "
     "water."),

 trn("N7",
     "A sheet that is to fold flat obeys a rule which can be checked before any folding is done: "
     "around every interior vertex the mountain folds and the valley folds must differ in number by "
     "exactly two. _____ a designer can draw a pattern of creases on a computer, test it against "
     "the rule and know the sheet will lie flat without ever picking up paper.",
     ["For this reason,", "By contrast,", "Even so,", "Similarly,"], "A",
     "Being able to test a design without folding follows from having a rule that can be checked in "
     "advance, so the transition marks a result. Nothing in the second sentence stands against the "
     "first, which rules out the concessive and contrastive options."),

 trn("N8",
     "Seed in a bank does not keep indefinitely, and a packet that has lost its viability is worse "
     "than useless, since the collection goes on listing it as secure. Banks guard against this by "
     "testing rather than by trusting their storage conditions. _____ the national collection "
     "samples every accession on a fixed cycle, sows the seed in trays and counts what comes up, "
     "and any lot falling below about eighty-five per cent germination is grown out in a field and "
     "replaced.",
     ["For example,", "Nevertheless,", "In contrast,", "Consequently,"], "A",
     "The sampling routine described is one instance of the stated policy of testing rather than "
     "trusting, so the transition introduces an example. Nothing in the final sentence works "
     "against what precedes it, which rules out the contrastive options."),

 trn("N9",
     "Running continuously at a moderate pace builds the heart and the capillary bed but leaves the "
     "fastest muscle fibres barely used, since they are recruited only when the slower ones cannot "
     "meet the demand. _____ a session of short repetitions run well above race pace recruits those "
     "fibres on every repetition, at the cost of covering far less ground in the hour.",
     ["By contrast,", "Consequently,", "In addition,", "For example,"], "A",
     "The interval session engages the fibres the steady run leaves idle, so the two methods are "
     "being set against each other. Presenting the second as a consequence would make the steady "
     "running the cause of the interval work."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("R1",
     ["Early parachutes were flat circular canopies of silk that descended straight down and could not be steered.",
      "A ram-air canopy is a fabric wing built from cells that inflate through openings at the front.",
      "The inflated cells give the canopy an aerofoil section, so it generates lift as well as drag.",
      "A ram-air canopy descends more slowly and can be flown to a chosen landing point.",
      "Sport parachutists adopted ram-air canopies through the 1970s."],
     "explain how the newer canopy differs from the older one in the way it holds a jumper up.",
     ["A ram-air canopy is built from cells that inflate through openings at the front, giving it an aerofoil section that generates lift, whereas the earlier flat circular canopy of silk produced only drag as it descended.",
      "Sport parachutists adopted ram-air canopies through the 1970s, and the canopies used before then were made of silk.",
      "A ram-air canopy descends more slowly than a flat circular canopy and can be flown to a chosen landing point.",
      "Early parachutes were flat circular canopies of silk that descended straight down and could not be steered."],
     "A",
     "The goal asks about the mechanism, and only the response naming the inflated cells, the "
     "aerofoil section and the lift they generate contrasts that with a canopy producing drag "
     "alone. The note about slower descent and steering reports consequences without saying what "
     "produces them."),

 syn("R2",
     ["Cabbage for kimchi is salted before the other ingredients are added.",
      "Salting draws water out of the leaves and leaves a brine standing in the vessel.",
      "Most of the soil bacteria carried on the leaves cannot grow in that brine.",
      "Lactic acid bacteria tolerate salt and multiply in it, producing acid as they do.",
      "The acid they produce lowers the pH far enough to keep spoilage organisms out later."],
     "explain how the salting stage determines which organisms carry out the fermentation.",
     ["Salting draws water from the leaves into a brine that most soil bacteria cannot grow in, while the salt-tolerant lactic acid bacteria multiply in it and acidify the vessel.",
      "Cabbage for kimchi is salted in the vessel before any of the other ingredients are added.",
      "Lactic acid bacteria produce acid that lowers the pH far enough to keep spoilage organisms out later.",
      "Most of the bacteria found on cabbage leaves have come from the soil the plants grew in."],
     "A",
     "The goal asks how salting selects the fermenting organisms, and only the response pairing the "
     "brine that excludes soil bacteria with the salt-tolerant ones that thrive in it answers it. "
     "The note about pH describes what happens after the selection has already been made."),

 syn("R3",
     ["A quartz crystal cut to a particular shape vibrates at a nearly fixed frequency when a voltage is applied.",
      "The frequency chosen for wristwatches is 32,768 hertz.",
      "That number is two raised to the fifteenth power.",
      "A chain of fifteen halving circuits reduces it to one pulse per second.",
      "The balance of a mechanical watch beats about five times a second."],
     "explain why that particular frequency was chosen.",
     ["The frequency used in wristwatches, 32,768 hertz, is two raised to the fifteenth power, so a chain of fifteen halving circuits turns it into one pulse per second.",
      "A quartz crystal cut to a particular shape vibrates at a nearly fixed frequency when a voltage is applied across it.",
      "A quartz watch's crystal vibrates far faster than the balance of a mechanical watch, which beats about five times a second.",
      "The frequency chosen for quartz wristwatches is 32,768 hertz, and a chain of circuits reduces it to one pulse per second."],
     "A",
     "Only the response identifying the frequency as a power of two, and connecting that to fifteen "
     "successive halvings, explains why that number rather than another was picked. Mentioning a "
     "chain of circuits without naming the power of two states the outcome and leaves the reason "
     "out."),

 syn("R4",
     ["Flint occurs as nodules in chalk and has no naturally flat faces.",
      "A knapper strikes a nodule to remove a slice, leaving one flat, glassy face.",
      "In East Anglian churches the knapped faces are set outward in the wall.",
      "The rest of each nodule stays rough and is bedded in the mortar behind.",
      "Such a wall shows a flat glassy surface but is held together by the irregular backs of its stones."],
     "explain how one operation on the stone accounts for both the wall's surface and its strength.",
     ["The knapper strikes each nodule to leave one flat glassy face, and that face is set outward while the rough back of the same stone is bedded in the mortar that holds the wall together.",
      "Flint occurs as nodules in chalk and has no naturally flat faces of its own.",
      "In East Anglian churches the knapped faces of the flints are set outward in the wall.",
      "A wall of knapped flint presents a flat glassy surface to anyone standing in front of it."],
     "A",
     "The goal asks for one operation accounting for two properties, and only the response "
     "following a single nodule from the strike to the outward face and the mortared back does "
     "that. Describing the outward faces alone gives the surface and says nothing about what holds "
     "the wall up."),

 syn("R5",
     ["Commercial bananas are sterile and are propagated from suckers, so a plantation is a single genotype.",
      "The Gros Michel variety dominated the export trade until the 1950s.",
      "A soil fungus causing Panama disease spread through Gros Michel plantations and made the variety uncommercial.",
      "Growers replaced it with Cavendish, which resisted the strain then circulating.",
      "A newer strain of the same fungus now attacks Cavendish."],
     "explain why the industry's answer to the first outbreak left it open to the second.",
     ["Growers met Panama disease by replacing one sterile, sucker-propagated variety with another, so the Cavendish plantations that resisted the old strain are as uniform as the Gros Michel ones were, and a newer strain now spreads through them.",
      "The Gros Michel variety dominated the export trade until a soil fungus made it uncommercial in the 1950s.",
      "Commercial bananas are sterile and are propagated from suckers rather than grown from seed.",
      "A newer strain of the fungus that causes Panama disease now attacks the Cavendish variety."],
     "A",
     "The goal asks why the remedy failed later, and only the response noting that the replacement "
     "was itself a single clone connects the first fix to the second outbreak. Reporting that a new "
     "strain attacks Cavendish states the outcome without giving the reason."),

 syn("R6",
     ["In 1951 Doll and Hill wrote to every doctor on the British medical register asking about smoking habits.",
      "Some 34,000 replied and were then followed for decades.",
      "Deaths among the respondents were matched to their stated habits as they occurred.",
      "Earlier studies had asked patients already ill with lung cancer what they had smoked.",
      "In the new design the habit was on record before any of the diseases appeared."],
     "explain what the design of the 1951 study changed.",
     ["Doll and Hill recorded the doctors' smoking habits in 1951 and matched deaths to them as they occurred over the following decades, so the habit was on record before any disease appeared, unlike earlier studies that asked patients already ill what they had smoked.",
      "Doll and Hill wrote to every doctor on the British medical register in 1951, and some 34,000 of them replied.",
      "Earlier studies of smoking had asked patients already ill with lung cancer to recall what they had smoked.",
      "Deaths among the doctors who replied were matched to their stated habits as those deaths occurred."],
     "A",
     "The goal asks what the design changed, and only the response contrasting habits recorded in "
     "advance with habits recalled after illness names that change. Describing the earlier studies "
     "alone gives one side of the comparison and leaves the new design unstated."),

 syn("R7",
     ["A camel can lose a quarter of its body water without its blood thickening dangerously.",
      "Its red cells are oval and stay flexible as the blood concentrates.",
      "Its body temperature is allowed to rise several degrees through the day rather than being held constant by sweating.",
      "The heat stored during the day is shed at night at no cost in water.",
      "A camel can drink over a hundred litres in a few minutes once water is reached."],
     "explain how the animal reduces the water it must spend on keeping cool.",
     ["Rather than sweating to hold a constant temperature, a camel lets its body temperature rise several degrees through the day and sheds the stored heat at night, which costs it no water at all.",
      "A camel can lose a quarter of its body water without its blood thickening dangerously.",
      "A camel's red cells are oval and stay flexible as the blood concentrates.",
      "A camel can drink over a hundred litres in a few minutes once water is reached."],
     "A",
     "The goal concerns the water spent on cooling, and only the response describing the daytime "
     "rise in temperature and the night-time release explains how sweating is avoided. Tolerance of "
     "water loss says how much the animal can afford to lose, not how it avoids losing it."),

 syn("R8",
     ["Songhai's rulers governed a territory stretching along more than a thousand miles of the Niger.",
      "Askia Muhammad, who came to power in 1493, replaced hereditary provincial lords with appointed governors.",
      "He created ministries for the treasury, for agriculture and for the fleet of river canoes.",
      "Standard weights and measures were imposed on the markets of the trading towns.",
      "The river fleet moved troops and grain between provinces in days rather than weeks."],
     "explain how the reforms addressed the difficulty of governing a territory of that size.",
     ["Askia Muhammad replaced hereditary provincial lords with appointed governors and built a river fleet that carried troops and grain between provinces in days rather than weeks, bringing a thousand miles of the Niger under one administration.",
      "Songhai's rulers governed a territory stretching along more than a thousand miles of the Niger.",
      "Askia Muhammad came to power in 1493 and created ministries for the treasury, for agriculture and for the fleet of river canoes.",
      "Standard weights and measures were imposed on the markets of Songhai's trading towns."],
     "A",
     "The goal asks how distance was overcome, and only the response pairing appointed governors "
     "with a fleet that moved men and grain in days speaks to the size of the territory. Listing "
     "the new ministries records what was created without connecting it to the problem of "
     "distance."),

 syn("R9",
     ["The ulnar collateral ligament resists the outward force on the elbow during a pitch.",
      "High-speed measurement puts the peak torque at the elbow close to the ligament's measured failure strength on a single throw.",
      "The ligament therefore has almost no margin at maximum effort.",
      "Damage accumulates across many throws rather than occurring in one.",
      "Leagues have adopted pitch counts and mandatory rest days rather than limits on velocity."],
     "explain why the rules adopted target the number of throws rather than their speed.",
     ["Since the peak torque of a single pitch already sits close to the ligament's failure strength, the damage that ends careers builds up across many throws, which is what pitch counts and mandatory rest days are designed to limit.",
      "The ulnar collateral ligament is the structure that resists the outward force on the elbow during a pitch.",
      "High-speed measurement puts the peak torque at the elbow close to the ligament's measured failure strength.",
      "Leagues have adopted pitch counts and mandatory rest days rather than limits on velocity."],
     "A",
     "The goal asks for the reasoning behind the rules, and only the response linking the "
     "accumulation of damage across throws to the counts and the rest days supplies it. Reporting "
     "the peak torque alone establishes that one throw is demanding without explaining why the "
     "limit falls on the number of throws."),

]

DROPPED = {}

