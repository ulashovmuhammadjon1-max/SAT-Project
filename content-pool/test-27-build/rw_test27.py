#!/usr/bin/env python3
"""
Reading & Writing authored for Test 27 — all 81 items original.

WHY EVERY ITEM IS AUTHORED
The transcribed pool was spent by Test 8. For R&W that is no loss: a
transcribed answer key has to be re-derived by hand before it can be trusted,
and Test 5 shipped six wrong answers in 81 items that way. Every item below
carries a `why` that records both the reasoning which produced the key and the
reason the strongest distractor fails. That record IS the verification — no key
exists here without one.

Rationales name options by their CONTENT and never by letter, so balance_rw.py
is free to rotate every one of the 81 when it evens out the key distribution.

THE SIZING RULE THIS BUILD IS SHAPED BY
Test 23 had the lowest corpus overlap of any build (0.14) and still failed on
fifteen same-subject pairs *internally*, one at 0.56 where the same paragraph
had effectively been written twice. Nothing in the corpus screen can catch
that: it is a collision of a test with itself, and it is the DEFAULT outcome
when a narrow territory is spread across only a handful of subjects, because a
Rhetorical Synthesis note list is a sub-topic's core facts stated plainly and a
Words-in-Context passage on the same sub-topic is the same facts in prose.

So the topic list here is sized to the ITEM count, not the block count:
**81 items, 81 distinct sub-topics**, and no Rhetorical Synthesis note list
sits on a sub-topic that any passage item uses. The sub-topics are drawn from
sixteen subject territories:

  1  ice harvesting and the ice-house trade      9  hypersaline microbiology
  2  salt pans, salterns and evaporation        10  karst caves and cave climate
  3  fish curing and smokehouses                11  polar provisioning
  4  cheese caves and affinage                  12  seed banking and longevity
  5  root cellars and tuber storage             13  the salt trade and its taxes
  6  cold-adapted animal physiology             14  amphorae and residue analysis
  7  latent heat and phase change               15  estuarine fish runs
  8  food-spoilage microbiology                 16  evaporative cooling

Territories the sibling builds hold were left alone: canal works (Test 23),
papermaking and dyeing (25), bell founding (26), coaching and farriery (28),
brickworks and stonemasonry (29), physic gardens and distilling (30), poultry
and eel traps (31). Two near-misses inside this build were steered rather than
paraphrased: the cheese work starts at the cave door and never touches milking
or creameries (Test 17 holds dairying), and lime burning is left out of the
salt chemistry entirely (Test 19 holds it).

WRITING-DOMAIN CHOICES ARE NEVER BARE PUNCTUATION
Test 8 shipped Boundaries items whose four options were ", " / "; " / ": " /
" and ", which a student sees as four empty rows. Every Boundaries item here
repeats the words on either side of the blank inside each option, so each
choice reads as the resulting sentence. Form/Structure items whose options are
genuinely words ("was"/"were", "its"/"their") stay as words, which is how the
real test presents them too.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T27"
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


# The CLAUDE.md table style block, emitted as real <table> markup. A data-based
# Command of Evidence item gets a genuine table; a prose description of a graph
# is never acceptable, since no image can be produced for this pool.
_TSTY = "border-collapse:collapse;margin:0.75rem 0;"
_TH = "border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;"
_TD = "border:1px solid #D9DEE5;padding:0.35rem 0.6rem;"


def table(headers, rows):
    head = "".join(f'<th style="{_TH}">{h}</th>' for h in headers)
    body = "".join(
        "<tr>" + "".join(f'<td style="{_TD}">{c}</td>' for c in r) + "</tr>"
        for r in rows)
    return f'<table style="{_TSTY}"><tr>{head}</tr>{body}</table>'


QUESTIONS = [

 # ------------------------------------------------------ Words in Context (15)
 wic("W1",
     "Before a gang set foot on a frozen pond, a horse dragged a marking plough across it, scoring "
     "a grid of shallow grooves into the surface. The grooves cut nothing free; a second pass with "
     "a deeper blade, and finally a hand saw, did that. What the grid did was fix the size of every "
     "block hours before the first one floated loose, so that a hundred men working across a "
     "hundred yards of ice all produced the same rectangle. The marking pass was therefore less a "
     "cut than a _____.",
     ["plan", "risk", "delay", "flourish"], "A",
     "The passage says the grooves free nothing and instead settle the dimensions in advance for "
     "everyone working the pond, which makes the pass an act of laying out rather than of cutting. "
     "Calling it a delay would treat the marking as time lost, but the text presents it as the "
     "step that makes the later cutting uniform."),

 wic("W2",
     "The Massachusetts ice house was built as two buildings, one inside the other, with a foot of "
     "sawdust packed between them and a gap left under the eaves for warm air to escape. Nothing in "
     "it made cold. The whole structure worked by _____ the heat that would otherwise reach the "
     "stack, and the ice it held all summer was simply the ice that had not yet melted.",
     ["slowing", "generating", "measuring", "welcoming"], "A",
     "The text states plainly that nothing in the building made cold and that the surviving ice was "
     "merely what had not yet melted, so the structure can only be delaying heat rather than "
     "removing it. Choosing a word for producing cold contradicts the sentence that rules exactly "
     "that out."),

 wic("W3",
     "A working saltern is not one pond but a staircase of them. Sea water enters the highest and "
     "widest, where it may sit for weeks losing volume to the sun; it is then let down into a "
     "smaller pond, and then a smaller one again, growing heavier at every step until the last and "
     "shallowest pan is close enough to saturation that a night's cooling throws down crystals. "
     "The design is _____: each pond does one part of a concentration that no single pond could "
     "manage.",
     ["sequential", "wasteful", "symbolic", "improvised"], "A",
     "The passage describes water passing through ponds of decreasing size, each carrying the "
     "concentration further, and states that no single pond could do the whole job. Calling the "
     "design improvised would suggest it was arrived at without order, while the text sets out a "
     "fixed series of steps."),

 wic("W4",
     "The Yarmouth curer and the Aberdeen curer were working towards different customers. A hard "
     "cure meant three weeks in dry salt and a fortnight in smoke, and produced a fish that would "
     "cross the equator in a sailing ship's hold. A mild cure meant a few hours in brine and a "
     "night over smouldering oak, and produced a fish that had to be eaten within the week. The two "
     "trades used the same rooms and the same wood, and their products were nonetheless barely "
     "_____.",
     ["comparable", "edible", "profitable", "portable"], "A",
     "The passage sets a fish built to survive an ocean crossing against one that spoils in a week "
     "and stresses that the shared rooms and wood do not make them alike, so the blank must deny "
     "likeness. Saying the products were barely edible introduces a judgement of quality the "
     "passage never makes about either cure."),

 wic("W5",
     "An affineur's daily round looks like housekeeping and is not. Brushing a wheel does not merely "
     "remove the grey bloom that has risen on it; it redistributes the organisms in that bloom "
     "across the surface and presses them into the paste beneath, so that the rind thickens evenly "
     "instead of in patches. Turning the wheel does not merely stop it flattening; it moves the "
     "moisture that has settled to the underside back through the body of the cheese. Every "
     "gesture in the cave is _____.",
     ["formative", "ceremonial", "hurried", "optional"], "A",
     "Both examples show a routine motion doing work on the cheese itself rather than tidying it, "
     "so the blank must credit the gestures with shaping the product. Describing them as ceremonial "
     "would empty them of the physical effects the passage takes two sentences to spell out."),

 wic("W6",
     "A potato kept at 4&deg;C will not sprout, but it turns its starch to sugar and fries black. A "
     "potato kept at 10&deg;C fries well and sprouts by February. Growers who need both qualities "
     "store at the lower temperature and then warm the crop for two weeks before it leaves the "
     "shed, which converts the sugar back without waking the eyes. The practice treats the two "
     "faults as _____ rather than as a single problem with a single setting.",
     ["separable", "identical", "unavoidable", "trivial"], "A",
     "The two-stage regime works precisely because the sugar fault and the sprouting fault are "
     "handled at different times and different temperatures, which means the grower has pulled them "
     "apart. Treating them as unavoidable would contradict a passage whose whole point is that both "
     "are avoided."),

 wic("W7",
     "The pointed toe of a Roman amphora is often taken for a defect of design, since a jar that "
     "will not stand up seems a poor container. On a ship it never had to stand: it was bedded in "
     "sand or wedged between the shoulders of the row below, and the point was a third handle, "
     "gripped by one man while two others took the loops at the neck. The shape that looks like an "
     "oversight is a piece of _____ for the only place the jar ever spent a long journey.",
     ["design", "decoration", "salvage", "guesswork"], "A",
     "The passage explains that the point served as a third handle and suited the ship's hold, so "
     "the blank must credit the shape with being purposeful. Calling it guesswork would keep the "
     "reading the passage sets out to overturn, since it says the shape only looks like an "
     "oversight."),

 wic("W8",
     "A kilogram of ice at 0&deg;C and a kilogram of water at 0&deg;C are at the same temperature, "
     "and a thermometer cannot tell them apart. Turning the first into the second takes about 334 "
     "kilojoules, and every one of those joules has to come out of whatever surrounds the ice. That "
     "is the whole of the ice house's usefulness: the heat that a summer forces into the building "
     "is _____ by the melting rather than by any fall in temperature.",
     ["absorbed", "reflected", "recorded", "multiplied"], "A",
     "The passage states that the energy of melting must be drawn from the surroundings and that "
     "this, not a temperature change, is what the store accomplishes, so the blank names heat being "
     "taken up. Saying the heat is reflected would describe it being turned back at the surface, "
     "which is not what a phase change does."),

 wic("W9",
     "The last pond of a saltern often runs a deep pink, and visitors take the colour for a trick of "
     "the sunset. It is a population. At a salinity approaching thirty per cent almost nothing will "
     "grow, but certain archaea flourish there and pack their membranes with red carotenoid "
     "pigments; the water carries so many of them that it takes their colour. The pink is thus not "
     "an effect of the light but a direct _____ of how salty the pond has become.",
     ["index", "cause", "rehearsal", "exception"], "A",
     "The colour is produced by organisms that only thrive at extreme salinity, so its presence "
     "reports the concentration of the pond. Calling it a cause reverses the relationship the "
     "passage sets out, in which the salinity produces the population and the population produces "
     "the colour."),

 meaning("W10",
     "For most of the twentieth century a food was judged safe by how much water it contained. The "
     "measure that displaced it, water activity, asks instead how much of that water is free to "
     "take part in a reaction rather than bound to sugar, salt or protein. Honey and a fresh fig "
     "can hold similar amounts of water and behave completely differently, because in the honey "
     "almost none of it is <u>available</u>. Below an activity of 0.85, most bacteria that cause "
     "illness will not grow at all.",
     "available",
     ["free to react", "plainly visible", "easy to remove", "fit to drink"], "A",
     "The passage defines water activity as the share of water free to take part in a reaction "
     "rather than bound to other molecules, and the honey example turns on exactly that "
     "distinction. Reading the word as easy to remove imports a question about drying that the "
     "passage does not raise."),

 meaning("W11",
     "A limestone cave a hundred metres in holds the mean annual temperature of the rock above it, "
     "and it holds it whatever the season. Summer air entering the mouth gives up its heat to "
     "kilometres of stone long before it reaches the back; winter air does the reverse. A surveyor "
     "logging a chamber over three years found the swing between her highest and lowest readings "
     "smaller than the swing outside on a single April afternoon. Deep cave air is, in the useful "
     "sense, <u>still</u>.",
     "still",
     ["unvarying", "silent", "motionless", "undisturbed"], "A",
     "Every detail concerns temperature — heat given up to the rock, a three-year swing smaller "
     "than one afternoon's — so the word reports constancy of condition. Reading it as motionless "
     "would describe the air's movement, which the passage in fact has flowing in from the mouth "
     "in both seasons."),

 meaning("W12",
     "A man-hauled sledge journey is an arithmetic problem before it is anything else. Every day of "
     "food must itself be dragged, and the food dragged for the later days must be fed for on the "
     "earlier ones, so a party's range grows far more slowly than the weight it starts with. "
     "Nineteenth-century expeditions answered this by laying depots on the outward march, which "
     "did not add a gram to what could be carried but did <u>redistribute</u> when it had to be "
     "carried.",
     "redistribute",
     ["reschedule", "divide equally", "hand over", "reduce"], "A",
     "The sentence contrasts adding weight, which depots do not do, with altering when the weight "
     "must be moved, which is a change of timing. Reading the word as dividing equally would "
     "suggest shares between people, and the passage is concerned with stages of a march."),

 wic("W13",
     "A bank cannot open every packet it holds to find out whether the seed inside is still alive, "
     "and a germination test destroys the seed it tests. The usual compromise is to germinate a "
     "small sample on a fixed cycle and treat the result as standing for the rest. Curators are "
     "candid that the practice is _____: a packet that has been sampled once in twenty years is "
     "described by a figure drawn from a few dozen of its neighbours, and nothing in the record "
     "says what has happened to the packet itself.",
     ["inferential", "wasteful", "recent", "automated"], "A",
     "The passage has a figure from a small sample standing in for packets nobody has opened, and "
     "says the record holds nothing about the packet itself, so the blank must name a conclusion "
     "drawn indirectly. Calling the practice wasteful would fix on the seed the test destroys, "
     "which the passage raises only as the reason the sampling is small."),

 wic("W14",
     "Under the French gabelle, salt cost roughly twenty times more in one province than in another "
     "a day's walk away, and the state was obliged to police an internal frontier drawn for no "
     "reason but the tax. Whole villages on the cheap side lived by carrying sacks across it. The "
     "smuggling was not a failure of enforcement but an entirely _____ response to a price "
     "difference the law had itself created.",
     ["predictable", "criminal", "unprofitable", "recent"], "A",
     "The final sentence sets a failure of enforcement against something that follows from the "
     "price gap the tax produced, so the blank must mark the smuggling as the expected consequence. "
     "Calling it criminal restates the legal position the sentence is trying to look past."),

 wic("W15",
     "An amphora is an awkward object to interpret. Its shape names a workshop and often a decade, "
     "and its stamps sometimes name an owner, but what it carried leaves almost nothing behind "
     "except the pine resin the potter used to seal the porous clay. Gas chromatography can now "
     "read the fatty acids that soaked into the fabric beneath that lining, and a jar whose contents "
     "were _____ for two centuries can be assigned to wine, oil or fish sauce.",
     ["indeterminate", "notorious", "spilled", "priceless"], "A",
     "The passage says the jar preserves its date and its owner but not its contents, and then "
     "describes a technique that finally settles what it held. Describing the contents as spilled "
     "would name a physical event, whereas the sentence is about what scholars could not decide."),

 # ---------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "Naval surgeons had known since the 1750s that citrus cured scurvy, and by 1850 the Admiralty "
     "issued lime juice as a matter of course. <u>Polar parties nonetheless went on developing the "
     "disease, and the failures were read at the time as evidence that the citrus theory had been "
     "overstated.</u> The juice being issued had by then been boiled for keeping and stored in "
     "copper, and both treatments destroy most of the ascorbic acid in it. A remedy that worked was "
     "being discredited by a change in how it was prepared, and nobody at the time was in a "
     "position to see the difference.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It reports a contemporary conclusion that the rest of the text goes on to explain away.",
      "It offers the evidence that persuaded the Admiralty to begin issuing lime juice in 1850.",
      "It concedes that scurvy has more than one cause besides a want of citrus.",
      "It contrasts the experience of naval crews with that of merchant crews on the same rations."],
     "A",
     "The sentence records what observers concluded from the continuing outbreaks, and the "
     "sentences after it supply the boiling and the copper that account for the failures without "
     "touching the theory. The option about multiple causes attributes to the passage a claim it "
     "never makes, since it traces every failure to the preparation of the juice."),

 tsp("T2",
     "Cold smoking holds the fish below about 30&deg;C. The proteins never set, so the flesh keeps "
     "the texture of raw fish, and everything that preserves it — the salt already in it, the drying "
     "of the surface, the phenols laid down by the smoke — must do so without help from heat. Hot "
     "smoking runs above 60&deg;C and cooks the fish outright, which kills what is present at the "
     "time but leaves a moist product that spoils quickly afterwards. The two methods share "
     "equipment and share almost nothing else.",
     "Which choice best states the main purpose of the text?",
     ["To distinguish two smoking methods by what each one relies on to preserve the fish",
      "To argue that cold smoking produces a better product than hot smoking does",
      "To trace the historical development of smoking as a method of preservation",
      "To explain why smokehouses are built to hold more than one kind of fire"],
     "A",
     "The passage assigns each method a temperature range and then names what does the preserving "
     "in each case, closing on the point that they have little in common beyond the equipment. The "
     "option about which product is better states a preference the passage withholds, since it "
     "credits hot smoking with killing organisms and cold smoking with nothing more than "
     "durability."),

 tsp("T3",
     "The Venetian state did not chiefly want to sell salt; it wanted to control who else could. "
     "<u>From the thirteenth century a ship returning to the lagoon from any port in the "
     "Mediterranean was required to load salt as ballast and to sell it only to the Salt Office at "
     "a price the Office set.</u> A merchant who would have carried stone for nothing was thereby "
     "paid to carry a commodity the state could resell across northern Italy, and rival producers "
     "on the Adriatic found their own outlets bought up by the same fleet. The tax was collected "
     "before anyone had thought of it as a tax.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It states the specific requirement whose several consequences the rest of the text then "
      "traces.",
      "It supplies the historical date on which the Venetian salt monopoly was formally abolished.",
      "It contrasts the price the Salt Office paid with the price rival producers could command.",
      "It concedes a limitation of the policy that the text goes on to answer."],
     "A",
     "The underlined sentence sets out the ballast rule, and the sentences after it work through "
     "what the rule did to shipowners, to the state's resale trade and to Adriatic rivals, so it "
     "supplies the premise the passage then develops. The option about a contrast in prices names "
     "a comparison the passage never makes, since no rival's price is given anywhere in it."),

 tsp("T4",
     "Sea ice does not always begin as a sheet. In water roughened by swell, the first crystals "
     "gather into a grey slush that the waves keep breaking apart, and each fragment is jostled "
     "against its neighbours until it wears a raised white rim and a rounded outline. <u>The result "
     "is a field of pale discs a metre across, packed edge to edge and rising and falling with the "
     "sea beneath them.</u> Only when the swell dies do the discs freeze into one another, and the "
     "rims stay visible in the finished sheet as a record of how it formed.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It describes the intermediate stage whose distinctive shape the final sentence then reads as "
      "evidence of the ice's history.",
      "It provides the measurement that allows pancake ice to be told apart from other kinds of sea "
      "ice.",
      "It explains why a swell prevents sea ice from forming at all in rough water.",
      "It contrasts the appearance of new sea ice with the appearance of ice formed in calm water."],
     "A",
     "The sentence pictures the discs, and the passage ends by saying their rims survive in the "
     "finished sheet as a record of its formation, so the description sets up that later reading. "
     "The option about swell preventing ice contradicts the passage, in which ice forms in rough "
     "water and merely takes a different shape."),

 tsp("T5",
     "A curer adding sodium nitrite to a barrel is doing at least three things at once. The nitrite "
     "reacts with myoglobin to fix the pink colour that customers read as freshness; it slows the "
     "oxidation that would otherwise give the fat a stale flavour within days; and, at "
     "concentrations far below those needed for either of the first two effects, it prevents "
     "Clostridium botulinum from producing toxin in an anaerobic pack. Proposals to remove it have "
     "generally foundered on the third function, which nothing else performs as cheaply.",
     "Which choice best states the main purpose of the text?",
     ["To set out the several distinct functions of one additive and identify which of them is "
      "hardest to replace",
      "To warn that an additive used for cosmetic reasons carries an unacknowledged risk",
      "To describe the chemical reaction by which cured meat acquires its characteristic colour",
      "To compare sodium nitrite with the alternatives that curers have proposed in its place"],
     "A",
     "The passage lists three effects and closes by singling out the safety function as the one no "
     "cheap substitute matches, which is a survey ending in a judgement of replaceability. The "
     "option about an unacknowledged risk inverts the passage, which presents the additive as "
     "preventing a hazard rather than creating one."),

 tsp("T6",
     "The natural caves of Roquefort are cut through by narrow fissures that run from the plateau "
     "above down into the cellars, and air moves through them all year. In summer the cellars are "
     "cooler than the outside and draw air downward; in winter the flow reverses. The result is a "
     "chamber that is never sealed and never dry, and it is the humidity, more than the "
     "temperature, that the cheesemakers found impossible to reproduce when they first tried "
     "building cellars above ground.",
     "Which choice best states the main purpose of the text?",
     ["To explain how a cave's natural ventilation maintains a condition that proved difficult to "
      "imitate artificially",
      "To describe the geological processes by which the fissures above Roquefort were formed",
      "To argue that cheese ripened in natural caves is superior to cheese ripened above ground",
      "To identify the season in which the cellars of Roquefort are at their most productive"],
     "A",
     "The passage traces the airflow through the fissures, states that it keeps the cellars humid, "
     "and ends on the failure of built cellars to match that humidity. The option about superior "
     "cheese asserts a quality judgement the passage avoids, since it speaks only of a condition "
     "that was hard to reproduce."),

 # -------------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "A cell sitting in brine is under constant pressure to lose its water to the outside, and "
     "there are only two ways to answer it. One group of organisms lets potassium chloride into the "
     "cytoplasm until the inside is as concentrated as the outside; every enzyme it owns must then "
     "be rebuilt to work in strong salt, and the organism can no longer live anywhere else. The "
     "other group manufactures small neutral molecules that raise the internal concentration "
     "without interfering with any enzyme, which is costly in energy but leaves the cell free to "
     "move between waters of different strength.",
     "Which choice best states the main idea of the text?",
     ["Two solutions to the same osmotic problem carry different costs, one paid in flexibility and "
      "the other in energy.",
      "Organisms that admit potassium chloride into the cytoplasm are unable to survive in brine at "
      "all.",
      "Manufacturing neutral molecules is the more effective of the two responses to osmotic "
      "pressure.",
      "A cell in brine loses water to its surroundings unless the surrounding water is diluted."],
     "A",
     "The passage sets one strategy that commits an organism to strong salt for good against "
     "another that costs energy but keeps its options open, which is a comparison of what each "
     "response costs. The option calling the neutral-molecule route more effective picks a winner "
     "the passage declines to pick, since it presents each as paying a different price."),

 cid("C2",
     "Sea water does not give up its salts all at once. As it concentrates, calcium carbonate comes "
     "out first, at about twice the original strength; calcium sulphate follows at four or five "
     "times; and only beyond ten times does sodium chloride begin to crystallise. A saltmaker who "
     "wants clean salt therefore runs the brine through ponds where the first two are deliberately "
     "shed and left behind, and admits to the crystallising pan only water that has already "
     "surrendered them.",
     "Which choice best states the main idea of the text?",
     ["Salts leave concentrating sea water in a fixed order, and a saltworks is laid out to exploit "
      "that order.",
      "Calcium carbonate and calcium sulphate must be removed from salt after it has crystallised.",
      "Sea water must be concentrated to ten times its original strength before any salt will form.",
      "Clean salt can be obtained only from sea water that is unusually low in calcium."],
     "A",
     "The passage gives the sequence in which three salts crystallise and then describes ponds "
     "arranged to discard the first two before the third forms, which links the chemistry to the "
     "layout. The option about removing the calcium salts afterwards reverses the arrangement, "
     "since the passage has them shed in earlier ponds and never admitted to the crystallising "
     "pan."),

 cid("C3",
     "A curing season is not chosen; it is imposed. Herring shoal along a coast for a matter of "
     "weeks, and a barrel packed from the first week of a run and a barrel packed from the last can "
     "differ by half in fat content, which changes how much salt the fish will take up and how long "
     "it will keep. Nineteenth-century Scottish curers followed the shoals north to south down the "
     "coast through the summer, and a crew's year was set by the fish's calendar rather than by any "
     "decision of its own.",
     "Which choice best states the main idea of the text?",
     ["The timing and the character of a curing season were dictated by the movements and condition "
      "of the fish.",
      "Scottish curers preferred to pack herring caught in the first week of a run.",
      "The fat content of herring can be adjusted by changing the amount of salt used in packing.",
      "Following the shoals down the coast allowed curers to extend their season indefinitely."],
     "A",
     "The passage has the run's length fixing the season, the fish's fat fixing the salt and the "
     "keeping, and the crews chasing the shoals rather than setting their own year. The option "
     "about adjusting fat content by salting inverts the stated relationship, in which fat content "
     "determines how much salt the fish takes up."),

 cid("C4",
     "A wheel floated in a saturated salt bath takes up almost nothing on the first day. Salt "
     "enters by diffusion, and diffusion is slow through a solid paste, so a forty-kilogram wheel "
     "may sit in the bath for three days and still be unsalted at its centre; the concentration "
     "evens out over the weeks that follow, in the cave and not in the bath. Time in the bath "
     "therefore fixes how much salt the wheel receives in total, while the months afterwards fix "
     "where in the wheel it ends up.",
     "Which choice best states the main idea of the text?",
     ["The salting of a large cheese is settled in two stages, one governing the quantity taken up "
      "and a later one governing its distribution.",
      "A forty-kilogram wheel must remain in a salt bath until its centre has reached the same "
      "concentration as its surface.",
      "Diffusion through a solid paste is too slow for salt bathing to be a practical way of "
      "salting a large cheese.",
      "The concentration of the bath determines how quickly salt reaches the centre of a wheel."],
     "A",
     "The closing sentence divides the process explicitly, giving the bath the total quantity and "
     "the following months the distribution, and the rest of the passage supplies the slow "
     "diffusion that makes the division necessary. The option that bathing is impractical "
     "contradicts a passage that describes the method working, merely in two stages."),

 cid("C5",
     "The old rule that apples and potatoes must not share a cellar has a mechanism behind it. "
     "Ripening apples give off ethylene, a gas active at a few parts per million, and potatoes "
     "exposed to it break dormancy and sprout weeks early. The same gas is why a cellar for roots "
     "wants a through draught and a cellar for fruit does not, and why the two were traditionally "
     "given separate doors even when they shared a single hillside.",
     "Which choice best states the main idea of the text?",
     ["A gas released by one stored crop damages another, which accounts for how storage spaces "
      "were arranged.",
      "Ethylene is harmless to apples but causes potatoes to rot in storage.",
      "Root cellars require a through draught in order to keep their temperature stable.",
      "Traditional storage practices were based on observation rather than on any understanding of "
      "chemistry."],
     "A",
     "The passage names ethylene, states its effect on potatoes, and derives from it both the "
     "ventilation difference and the separate doors. The option about tradition without chemistry "
     "runs against the opening sentence, which says the old rule has a mechanism behind it."),

 cid("C6",
     "A wood frog spends the winter frozen. Ice fills the spaces between its cells and as much as "
     "two thirds of its body water becomes solid; the heart stops and the animal shows no measurable "
     "respiration. What keeps it alive is that the ice stays outside the cells. In the hours before "
     "freezing the liver floods the blood with glucose, which enters the cells and holds enough "
     "water inside them that they never dehydrate to the point of collapse, and in spring the frog "
     "thaws from the inside out and hops away.",
     "Which choice best states the main idea of the text?",
     ["The frog survives freezing because a chemical change protects its cells while ice forms "
      "around them.",
      "The frog avoids freezing altogether by producing glucose before winter begins.",
      "Two thirds of the frog's body water must freeze if the animal is to survive the winter.",
      "The frog's heart continues to beat slowly throughout the period in which it is frozen."],
     "A",
     "The passage states that the animal does freeze, that survival depends on the ice remaining "
     "outside the cells, and that glucose is what keeps the cells from collapsing. The option "
     "saying the frog avoids freezing contradicts the first sentence, which has ice filling the "
     "spaces between its cells."),

 # --------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "Cheeses lose mass in the cave, and how much they lose depends on the humidity they are held "
     "at. A team weighed batches of identical wheels held for ninety days at three humidities and "
     "recorded the mean loss. " +
     table(["Relative humidity", "Mean mass lost in 90 days"],
           [["80%", "11.4%"], ["88%", "6.9%"], ["95%", "3.1%"]]) +
     "The team concluded that a maker who wants a thin rind and a moist paste should hold the cave "
     "near the top of this range.",
     "Which choice best describes data from the table that support the team's conclusion?",
     ["Wheels at 95% humidity lost 3.1% of their mass, less than a third of the 11.4% lost at 80%.",
      "Wheels at 88% humidity lost 6.9% of their mass, a figure between the other two results.",
      "Wheels at 80% humidity lost 11.4% of their mass, the largest loss the team recorded.",
      "The three humidities tested differed from one another by no more than fifteen percentage "
      "points."],
     "A",
     "The conclusion recommends the humid end of the range, so the supporting datum has to be the "
     "one showing the smallest loss there and the contrast with the dry end. Citing the middle "
     "result alone reports a figure without connecting it to any recommendation about where to hold "
     "the cave."),

 coe("E2",
     "Solar salt production is seasonal in a way that surprises visitors, because the limit is not "
     "sunshine alone but the difference between evaporation and rainfall. A works on the Atlantic "
     "coast recorded its yield across four months of one season. " +
     table(["Month", "Rainfall (mm)", "Salt drawn (tonnes)"],
           [["June", "38", "210"], ["July", "16", "480"], ["August", "11", "540"],
            ["September", "74", "95"]]) +
     "The manager argued that a wet month costs the works far more than the water it adds, because "
     "rain dilutes ponds that have taken weeks to concentrate.",
     "Which choice best describes data from the table that support the manager's argument?",
     ["September had the highest rainfall of the four months and a yield below a fifth of August's.",
      "August had the lowest rainfall of the four months and the highest salt yield.",
      "July and August together account for more than two thirds of the salt drawn in the season.",
      "June's rainfall was more than twice July's, and June's yield was less than half July's."],
     "A",
     "The argument is that rain is disproportionately costly, so the datum needed is the wettest "
     "month set against the collapse in its yield. The option pairing August's dryness with its "
     "high yield shows the favourable case and says nothing about what a wet month costs."),

 coe("E3",
     "Antifreeze glycoproteins are expensive for a fish to make, and biologists expect an animal to "
     "make only as much as its habitat requires. Because the sea surface in the Southern Ocean sits "
     "at the freezing point while deeper water is a fraction of a degree warmer and holds no ice "
     "crystals at all, one team predicted that _____",
     "Which finding, if true, would most directly support the team's prediction?",
     ["Species that feed in the top fifty metres carry markedly higher plasma concentrations of the "
      "glycoproteins than closely related species restricted to depths below five hundred metres.",
      "The glycoproteins found in Antarctic fish are chemically almost identical to those found in "
      "several unrelated Arctic species.",
      "Fish held in aquarium water a full degree above the freezing point continue to produce the "
      "glycoproteins for several months.",
      "The gene coding for the glycoprotein appears to have arisen from a duplicated digestive "
      "enzyme gene."],
     "A",
     "The prediction ties the amount produced to the risk of encountering ice, which is highest at "
     "the surface, so the supporting finding must compare shallow and deep species and find more of "
     "the protein in the shallow ones. The finding about Arctic species concerns where the molecule "
     "came from and bears on convergence rather than on how much any fish makes."),

 coe("E4",
     "Water activity, rather than total moisture, sets the limit below which an organism cannot "
     "grow. A laboratory measured the lowest activity at which each of four organisms would "
     "multiply. " +
     table(["Organism", "Lowest water activity permitting growth"],
           [["Clostridium botulinum", "0.94"], ["Staphylococcus aureus", "0.86"],
            ["Most yeasts", "0.80"], ["Xerophilic moulds", "0.61"]]) +
     "A curer who dries fish to a water activity of 0.83 argued that the product is safe from every "
     "organism on this list that causes acute illness, though not from spoilage.",
     "Which choice best describes data from the table that support the curer's argument?",
     ["Both bacteria on the list require an activity above 0.83, while the yeasts and moulds do not.",
      "Xerophilic moulds grow at 0.61, the lowest activity recorded for any organism on the list.",
      "Clostridium botulinum requires 0.94, the highest activity recorded for any organism on the "
      "list.",
      "The four organisms span a range of water activities from 0.61 to 0.94."],
     "A",
     "The claim is that the illness-causing organisms are excluded at 0.83 while spoilage organisms "
     "are not, which needs the two bacteria placed above that figure and the yeasts and moulds "
     "below it. Citing the mould's 0.61 alone establishes that spoilage remains possible but says "
     "nothing about the bacteria the curer claims to have excluded."),

 coe("E5",
     "Potatoes break dormancy sooner the warmer they are kept, but the relationship is not a "
     "straight line, and growers want to know where the useful threshold lies. A store recorded the "
     "proportion of tubers that had sprouted after twenty weeks at four temperatures. " +
     table(["Storage temperature", "Sprouted after 20 weeks"],
           [["3&deg;C", "2%"], ["6&deg;C", "9%"], ["9&deg;C", "41%"], ["12&deg;C", "78%"]]) +
     "The store's manager concluded that the cost of chilling below 6&deg;C buys much less than the "
     "cost of chilling from 9&deg;C down to 6&deg;C.",
     "Which choice best describes data from the table that support the manager's conclusion?",
     ["Moving from 9&deg;C to 6&deg;C cut sprouting by 32 percentage points, while moving from "
      "6&deg;C to 3&deg;C cut it by 7 more.",
      "Only 2% of tubers had sprouted at 3&deg;C, the lowest figure recorded in the trial.",
      "At 12&deg;C, 78% of tubers had sprouted, more than at any other temperature tested.",
      "Sprouting increased at every step as the storage temperature was raised."],
     "A",
     "The conclusion compares the benefit of two equal three-degree steps, so the supporting datum "
     "must give both drops and show the lower step yielding far less. Reporting the 2% at 3&deg;C "
     "gives one endpoint without the comparison the conclusion rests on."),

 coe("E6",
     "The phenols carried in wood smoke are antimicrobial, but they are deposited only on the "
     "surface of a fish and penetrate a few millimetres at most. A researcher who suspected that "
     "smoke therefore does little for a thick fillet proposed to test the idea by counting bacteria "
     "at different depths after smoking, expecting that _____",
     "Which finding, if true, would most directly support the researcher's expectation?",
     ["Counts taken two millimetres below the surface were reduced by more than ninety per cent, "
      "while counts taken twenty millimetres down were unchanged from those in unsmoked controls.",
      "Fillets smoked for eight hours carried roughly twice the surface phenol concentration of "
      "fillets smoked for four hours.",
      "Thin fillets and thick fillets showed the same surface phenol concentration after identical "
      "smoking.",
      "Bacterial counts in unsmoked fillets rose steadily at every depth over the six days "
      "following filleting."],
     "A",
     "The expectation is that the effect stops at the surface, which requires a comparison between "
     "a shallow depth where counts fall and a deep one where they do not. The finding about smoking "
     "time and phenol concentration concerns how much is deposited, not how far into the flesh the "
     "deposit reaches."),

 coe("E7",
     "The mass of ice an ice house loses over a summer depends heavily on how its walls are built. "
     "A survey of four ice houses of similar size recorded the proportion of the winter's stack "
     "still fit to sell in September. " +
     table(["Wall construction", "Proportion of stack remaining"],
           [["Single brick, no cavity", "34%"], ["Double brick, air cavity", "58%"],
            ["Double brick, sawdust-filled cavity", "77%"],
            ["Double brick, sawdust cavity, earth bank", "83%"]]) +
     "A surveyor argued that filling the cavity was a far better investment than banking earth "
     "against a wall that was already filled.",
     "Which choice best describes data from the table that support the surveyor's argument?",
     ["Filling the cavity raised the proportion remaining from 58% to 77%, while adding the earth "
      "bank raised it only to 83%.",
      "The best-performing ice house retained 83% of its stack, the highest figure in the survey.",
      "The single-brick ice house retained 34% of its stack, less than half the figure for the "
      "sawdust-filled cavity.",
      "Every ice house with a double brick wall retained more than half of its stack."],
     "A",
     "The argument ranks two successive improvements against each other, so it needs the gain from "
     "filling the cavity and the smaller gain from the earth bank side by side. Naming the "
     "best-performing house reports the top of the table without comparing the two steps at issue."),

 coe("E8",
     "Halite crystallising from a brine traps microscopic pockets of that brine inside itself, and "
     "the pockets do not exchange with anything afterwards. A geochemist proposed that this makes "
     "an ancient salt bed a record of the water it grew in, and that the proposal could be tested "
     "on beds whose composition is already known from other evidence, since _____",
     "Which finding, if true, would most directly support the geochemist's proposal?",
     ["Inclusions in halite from a bed independently dated to the Permian yield ion ratios matching "
      "those reconstructed for Permian sea water from marine fossils.",
      "Halite crystals grown in the laboratory trap fluid inclusions of a size comparable to those "
      "found in ancient beds.",
      "Modern salterns produce halite whose inclusions vary considerably from one pond to the next.",
      "Fluid inclusions can be opened and analysed without contaminating the surrounding crystal."],
     "A",
     "The proposal is that the inclusions preserve the parent water, and the test named is a bed "
     "whose water is known by other means, so the supporting finding must show the two agreeing. "
     "The finding about laboratory crystals establishes that inclusions form at a comparable size "
     "and leaves untouched the question of whether they preserve composition faithfully."),

 coe("E9",
     "Seed banks store at &minus;20&deg;C on the assumption that the colder the store, the longer "
     "the seed lives, but the size of the gain matters for deciding whether the electricity is "
     "worth it. A bank germinated samples of one wheat accession after twenty years at two "
     "temperatures. " +
     table(["Storage temperature", "Germination at 20 years"],
           [["&minus;20&deg;C", "94%"], ["4&deg;C", "31%"]]) +
     "The bank's director argued that the figures justify the running cost of the colder store for "
     "accessions that are not duplicated elsewhere.",
     "Which choice best describes data from the table that support the director's argument?",
     ["After twenty years, 94% of seed held at &minus;20&deg;C germinated, against 31% of seed held "
      "at 4&deg;C.",
      "Seed held at 4&deg;C still showed 31% germination after twenty years.",
      "The two storage temperatures tested differed by 24 degrees Celsius.",
      "The bank tested only a single wheat accession over the twenty-year period."],
     "A",
     "The argument is that the colder store earns its running cost, which requires both figures set "
     "against each other to show the size of the difference. Reporting only the 31% at 4&deg;C "
     "shows that some seed survives the warmer store and gives no measure of what the colder one "
     "adds."),

 # ------------------------------------------------------------- Inferences (6)
 inf("I1",
     "The natural ice trade did not shrink gradually. Mechanical plants using compressed ammonia "
     "were producing ice in New Orleans by the 1870s at a price that pond ice could still undercut, "
     "and the harvesters were untroubled. What finished them was that a mechanical plant could be "
     "put up wherever ice was wanted, while a pond crop had to be cut in one place, held through a "
     "summer and carried hundreds of miles. Once the plants had multiplied, the harvester's price "
     "advantage applied to a product whose costs the buyer no longer had to bear at all. This "
     "suggests that the trade's collapse turned less on price than on _____",
     ["the disappearance of the distance that had made the harvesters' service necessary.",
      "the failure of harvesters to reduce their costs as quickly as their competitors did.",
      "the unwillingness of buyers to accept ice produced by an unfamiliar method.",
      "a decline in the quality of the ice that ponds were able to yield."],
     "A",
     "The passage grants the harvesters a lasting price advantage and locates the decisive change "
     "in plants being built where the ice was wanted, which removes the storage and carriage the "
     "trade existed to perform. The option about costs rising too slowly contradicts the passage's "
     "statement that pond ice could still undercut the plants."),

 inf("I2",
     "Industrial salterns are among the most productive shorebird sites in Europe, which is not "
     "what a visitor expects of a set of rectangular concrete-edged ponds. The reason is that the "
     "ponds hold a graded series of salinities, each supporting its own invertebrates and each held "
     "at a constant depth by a works that has no interest in tides. A natural lagoon offers the "
     "same range of conditions only briefly and only in patches. Conservationists have found that "
     "when a saltworks closes, the bird numbers fall within a few seasons, which implies that the "
     "habitat's value depends on _____",
     ["the continued operation of the industry that maintains the ponds' distinct conditions.",
      "the absence of the tidal movement that would otherwise scour the ponds.",
      "the concrete edging that separates one pond from another.",
      "the invertebrates being introduced deliberately by the works."],
     "A",
     "The passage attributes the richness to a managed set of salinities and depths and then "
     "reports the birds leaving once the works shuts, so the value rests on the industry going on "
     "working. The option about tidal scouring picks up a contrast the passage draws with natural "
     "lagoons and turns it into the cause, when the text credits the graded salinities instead."),

 inf("I3",
     "Consumer pressure to remove nitrite from cured fish and meat has been steady for forty years, "
     "and the industry has answered with celery powder, which is marketed as a natural alternative. "
     "Celery is rich in nitrate, and the bacteria added alongside it reduce that nitrate to "
     "nitrite in the pack. The finished product contains nitrite at concentrations comparable to "
     "those of a conventional cure, arrived at by a longer route and labelled differently. It "
     "follows that the substitution has, in chemical terms, _____",
     ["changed the source of the compound rather than its presence in the food.",
      "reduced the quantity of the compound while preserving its preservative effect.",
      "introduced a compound that had not previously been present in cured products.",
      "removed the need for any bacterial activity during the curing process."],
     "A",
     "The passage says the finished product contains comparable nitrite concentrations reached by a "
     "longer route, so what has altered is where the compound comes from. The option about reducing "
     "the quantity contradicts the word comparable, which the passage uses precisely to deny a "
     "difference in amount."),

 inf("I4",
     "For most of the nineteenth century, cheesemakers who tried to build a ripening cellar rather "
     "than use a cave were defeated by humidity. Temperature could be held by digging deep enough, "
     "and airflow by a shaft and a damper, but a built cellar with dry walls pulls moisture out of "
     "the wheels, and the rinds crack. Caves solve it without machinery because their limestone is "
     "permanently wet and gives water back to the air as fast as the air takes it. Once mechanical "
     "humidification became cheap and reliable in the twentieth century, the advantage of the cave "
     "_____",
     ["ceased to rest on anything a built cellar could not now supply.",
      "was recognised for the first time by makers who had ignored it.",
      "shifted from humidity to the constancy of the cave's temperature.",
      "proved to depend on the mineral composition of the limestone itself."],
     "A",
     "The passage names humidity as the one condition a built cellar could not reproduce and lists "
     "temperature and airflow as already solved, so cheap humidification leaves nothing exclusive "
     "to the cave. The option about the temperature taking over is ruled out by the passage's "
     "statement that digging deep enough already handled temperature."),

 inf("I5",
     "The hillside root cellars of Appalachia are almost always cut into a north-facing slope, and "
     "the reason is not that north-facing ground is colder in winter. In winter the door is shut "
     "and the earth around the chamber governs everything. It is in the shoulder seasons, when the "
     "door must be opened daily and the sun is low enough to reach into a doorway, that a "
     "south-facing entrance admits a wedge of direct light and a pulse of warm air with every "
     "visit. The orientation is therefore chosen to protect the store during _____",
     ["the periods when the cellar is opened rather than the coldest part of the year.",
      "the winter months, when the surrounding earth is least able to insulate the chamber.",
      "the hours of darkness, when the temperature outside falls furthest.",
      "the summer, when the sun stands too high to enter a doorway at all."],
     "A",
     "The passage rules out winter, when the door stays shut, and points to the shoulder seasons of "
     "daily opening and a low sun as the vulnerable time. The option about summer is excluded by "
     "the passage's own detail that a high sun cannot reach into the doorway."),

 inf("I6",
     "A well-preserved amphora tells an archaeologist where it was made and often when, because "
     "shape and stamp are local and datable. What it carried is a harder question, and for a long "
     "time was answered by shape alone, on the assumption that a form used for oil in one province "
     "was used for oil everywhere. Residue analysis has now found wine markers in jars whose form "
     "had been catalogued as an oil type, and in some cases has found both markers in a single jar. "
     "The findings suggest that inferences drawn from form alone were _____",
     ["less reliable than the completeness of the typologies had implied.",
      "correct in most cases but impossible to confirm without chemical evidence.",
      "based on stamps that had been misread by earlier scholars.",
      "unnecessary once the stamps on a jar could be dated accurately."],
     "A",
     "The passage reports jars classified as one type carrying markers of another, and sometimes of "
     "both, which undercuts the assumption that form fixed contents. The option that the "
     "inferences were correct in most cases is not supported, since the passage gives no count and "
     "reports the assumption failing rather than holding."),

 # ------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "The tool that did the real work on a frozen pond was not the saw but the ice _____ a heavy "
     "toothed blade set in a wooden frame and dragged behind a horse, it cut a groove two thirds of "
     "the way through the sheet in a single pass.",
     ["plough. A", "plough, a", "plough a", "plough; a"], "A",
     "A complete sentence ends at the tool's name, and what follows is a second complete sentence "
     "beginning with the article that introduces the description. A comma between them joins two "
     "independent clauses without a conjunction."),

 bnd("B2",
     "The last pan of a saltern is worked differently from the rest. Because the brine there is "
     "already close to saturation and a night's cooling is enough to precipitate _____ raked into "
     "ridges every morning and left to drain before it is carried off.",
     ["it, the crop is", "it the crop is", "it; the crop is", "it: the crop is"], "A",
     "The introductory clause opening with the subordinating conjunction has to be marked off from "
     "the main clause that completes the sentence, and only a comma does that. A semicolon would "
     "require an independent clause on its left, which a clause beginning with a subordinator is "
     "not."),

 bnd("B3",
     "Gutting a herring by hand takes a fraction of a second and removes only the gills and the "
     "long gut, leaving the pyloric caeca in _____ they carry the digestive enzymes that ripen the "
     "flesh during the weeks the fish spends in salt.",
     ["place; deliberately, since", "place, deliberately since", "place deliberately since",
      "place: deliberately, since"], "A",
     "Two independent statements meet here, and the semicolon separates them while the comma sets "
     "off the single word that comments on the first. Running them together with no mark at all "
     "leaves the second statement grafted onto the first without any boundary."),

 bnd("B4",
     "A young wheel is turned every day, an older one every third day, and one that has been in the "
     "cave for six months perhaps once a _____ the schedule follows the rate at which moisture "
     "still moves inside the paste.",
     ["week. Throughout,", "week, throughout", "week throughout", "week; throughout"], "A",
     "The list of intervals completes a sentence, and the explanation that follows is a second "
     "sentence whose opening adverb is set off by a comma. Placing only a comma after the interval "
     "would splice two independent clauses together."),

 bnd("B5",
     "An earth clamp is built without any structure at all: the roots are heaped on a bed of straw, "
     "covered with more _____ and finished with a skin of soil beaten smooth so that rain runs off "
     "instead of soaking in.",
     ["straw,", "straw;", "straw:", "straw"], "A",
     "The three actions form a series of parallel past participles, and a comma is the mark that "
     "separates items in such a series. A semicolon separates items only when the items themselves "
     "contain commas, which these do not."),

 bnd("B6",
     "When Arthur DeVries drew blood from an Antarctic fish in the early 1960s and found that it "
     "resisted freezing far better than its salt content could _____ was looking at a class of "
     "molecule that nobody had proposed and that no existing theory of cold tolerance required.",
     ["explain, he", "explain he", "explain; he", "explain: he"], "A",
     "The long opening clause introduced by the subordinating conjunction must be closed with a "
     "comma before the main clause begins. A semicolon cannot follow a dependent clause, and "
     "omitting the mark leaves the reader to find the join unaided."),

 bnd("B7",
     "Joseph Black noticed something that his contemporaries had all seen and none had thought "
     "worth explaining: a lump of ice in a warm room takes hours to melt, while the same lump of "
     "water, once melted, warms measurably within _____ concluded that melting itself consumes "
     "heat, and named the quantity latent.",
     ["minutes. He", "minutes, he", "minutes he", "minutes; and he"], "A",
     "The observation is a complete sentence and the conclusion drawn from it is another, so a full "
     "stop belongs between them. A comma would join two independent clauses with no conjunction to "
     "carry the join."),

 bnd("B8",
     "The red that colours a saturating pond comes from bacterioruberin, a carotenoid that sits in "
     "the archaeal cell _____ stiffens it against the osmotic stress of the surrounding brine and, "
     "incidentally, screens the cell from ultraviolet light.",
     ["membrane. It", "membrane, it", "membrane it", "membrane, and it"], "A",
     "The description of where the pigment sits ends a complete sentence, and the account of what "
     "it does forms a second one. Joining them with only a comma produces a run-on, since neither "
     "half depends on the other."),

 bnd("B9",
     "A logger left in a chamber a hundred metres from the entrance recorded temperatures over "
     "three years, and the spread between the highest and lowest readings across the whole period "
     "was _____ tenths of a degree.",
     ["four", "four,", "four;", "four:"], "A",
     "Nothing here interrupts the sentence: the measurement completes the predicate directly and "
     "takes no mark before it. Any punctuation after the number would separate a verb from its own "
     "complement."),

 bnd("B10",
     "Depot laying looks like a detour and is arithmetic. A party that carries food forward, buries "
     "it and returns has spent days without advancing, but every kilogram left behind is a kilogram "
     "the same party will not have to drag on the outward march _____ and the saving compounds at "
     "every stage of the journey.",
     ["proper,", "proper;", "proper", "proper:"], "A",
     "A comma belongs before the coordinating conjunction that joins two independent clauses. "
     "Leaving the mark out runs a full clause on after another with only the conjunction between "
     "them, which the convention does not allow at this length."),

 bnd("B11",
     "The vault at Svalbard was cut into a mountain of permafrost for a reason that has nothing to "
     "do with security. Should the refrigeration fail and stay failed, the surrounding rock would "
     "hold the chambers below &minus;3&deg;C on its _____ that is not cold enough for centuries of "
     "storage, but it is cold enough to keep the collection alive while the plant is repaired.",
     ["own; ", "own, ", "own ", "own: "], "A",
     "Two independent clauses stand on either side of the blank and the second opens with a "
     "demonstrative pronoun rather than a conjunction, so a semicolon is required. A comma in that "
     "position splices the clauses together."),

 bnd("B12",
     "Because the stamps pressed into an amphora's handle before firing name a workshop, and "
     "sometimes a consular year, a single sherd can be dated more precisely than the layer it was "
     "found _____ archaeologists have occasionally used the pottery to correct the stratigraphy "
     "rather than the other way about.",
     ["in, and", "in and", "in; and", "in: and"], "A",
     "The comma before the coordinating conjunction marks the boundary between two independent "
     "clauses. A semicolon before a conjunction that is already doing the joining doubles the mark "
     "unnecessarily."),

 # ------------------------------------------- Form, Structure, and Sense (9)
 fss("F1",
     "The floor of a well-built ice house slopes to a central drain, and the drain _____ through a "
     "water trap so that the melt can leave without letting warm air in behind it.",
     ["runs", "run", "running", "to run"], "A",
     "The subject of the second clause is a single drain, so the verb takes the singular form. The "
     "plural form would agree with nothing in the sentence, and neither non-finite form supplies "
     "the clause with a main verb."),

 fss("F2",
     "The channel that feeds the highest pond is fitted with a sluice, and its gate is raised only "
     "on a spring tide, when the water arriving is saltier than at any other point in the month and "
     "_____ the works several days of evaporation.",
     ["saves", "save", "saving", "having saved"], "A",
     "The verb shares its subject with the earlier clause about the arriving water and must be "
     "finite and singular to match. A participle would leave the clause after the conjunction "
     "without a main verb of its own."),

 fss("F3",
     "Racks in a smokehouse are hung with a hand's width between them, since fish that touch one "
     "another leave pale patches where the smoke never reached _____ surfaces.",
     ["their", "its", "they're", "there"], "A",
     "The surfaces belong to the fish, which is plural in this sentence, so the plural possessive "
     "is required. The contraction is a subject and a verb and cannot modify a noun at all."),

 fss("F4",
     "Cave shelving is cut from unplaned spruce rather than oak, because the resinous timber "
     "_____ far less readily in air kept near saturation than a close-grained hardwood does.",
     ["warps", "warp", "warping", "have warped"], "A",
     "The subject is the singular timber, so the present-tense verb takes the singular form and "
     "matches the comparison with what a hardwood does. The plural form agrees with nothing "
     "available in the clause."),

 fss("F5",
     "Keepers of an old orchard cellar knew that a Bramley and a Cox will not sit together for "
     "long, because the two varieties differ in how much gas each _____ as it ripens.",
     ["gives off", "give off", "giving off", "are giving off"], "A",
     "The pronoun each is singular and governs the verb in this clause, so the singular form is "
     "required. The plural form would agree with the varieties rather than with the pronoun that "
     "actually stands as the subject."),

 fss("F6",
     "The Antarctic icefishes are the only vertebrates with no haemoglobin at all, and their blood, "
     "which carries oxygen in simple solution, _____ about a tenth of the oxygen that a comparable "
     "red-blooded fish's blood does.",
     ["holds", "hold", "holding", "to hold"], "A",
     "The subject is the singular blood, and the clause between the commas does not change what the "
     "verb must agree with. Choosing the plural form takes the nearby plural noun for the subject "
     "instead of the one the sentence actually supplies."),

 fss("F7",
     "Freezer burn is not burning and not really freezing either. Ice on the surface of a stored "
     "food passes straight to vapour without melting, and the dry, discoloured patch it _____ "
     "behind is what the name describes.",
     ["leaves", "leave", "leaving", "had left"], "A",
     "The relative clause has the singular ice as its subject and needs a present-tense singular "
     "verb to match the sentence's other verbs. The past perfect form places the action before a "
     "past reference point that the sentence never establishes."),

 fss("F8",
     "A salt marsh gains height by trapping sediment among its stems, and because the rate at which "
     "it does so _____ with the depth of water that covers it, a marsh tends to rise until it is "
     "flooded only on the highest tides.",
     ["falls", "fall", "falling", "have fallen"], "A",
     "The subject of the clause is the singular rate, and the verb must agree with it rather than "
     "with the plural noun nearest to it. A participle would leave the subordinate clause without a "
     "finite verb."),

 fss("F9",
     "Amphora typologies are built from measurements of rim, handle and foot, and a form once "
     "assigned a number _____ that number in the literature even after the province it was made in "
     "has been reassigned.",
     ["keeps", "keep", "keeping", "to keep"], "A",
     "The subject is a single form, so the verb is singular. The plural form would agree with the "
     "typologies named in the first clause, which is not the subject of the clause containing the "
     "blank."),

 # ------------------------------------------------------------ Transitions (9)
 trn("N1",
     "The Hudson's ice houses stood on the river bank rather than beside the ponds inland, and the "
     "reason was carriage: a block cut on the river could be pushed up a chute directly into the "
     "house, and later slid down another chute into a barge. Ice cut inland had to be carted to the "
     "water, and a cart could take twenty blocks where a barge took two thousand. _____ the river "
     "houses could pay more for their crop and still deliver it cheaper.",
     ["Accordingly,", "Nevertheless,", "For example,", "In contrast,"], "A",
     "The sentence states a consequence of the carriage advantage the preceding sentences "
     "establish, so the transition must signal a result. A contrast marker would announce that what "
     "follows cuts against the carriage argument, and it plainly follows from it."),

 trn("N2",
     "Rock salt is mined from beds laid down when an ancient sea dried, and it comes out of the "
     "ground already pure enough for most industrial uses. Solar salt is made by drying sea water "
     "in ponds, and arrives carrying magnesium and calcium that have to be washed out. _____ solar "
     "salt is cheaper wherever the climate allows it, because the sun does for nothing the work "
     "that a mine does with machinery.",
     ["Even so,", "Consequently,", "Likewise,", "In short,"], "A",
     "The preceding sentences give solar salt the disadvantage of impurity, and the sentence then "
     "asserts a price advantage in spite of it, so a concessive transition is needed. A "
     "consequence marker would claim the cheapness follows from the impurity, which the passage "
     "does not say."),

 trn("N3",
     "Smoke reaches a fish as a suspension of droplets, and what settles on the skin depends on how "
     "wet that skin is. A fish taken straight from the brine carries a film of water that the "
     "droplets dissolve into and run off. _____ curers hang the fish for several hours first, until "
     "the surface has dried to the tacky, glossy layer they call the pellicle.",
     ["For this reason,", "By comparison,", "Admittedly,", "Meanwhile,"], "A",
     "The practice described is the response to the problem set out in the previous sentence, so "
     "the transition marks a consequence. A comparison marker would set the drying against "
     "something else in the passage, and nothing else is offered for it to be compared with."),

 trn("N4",
     "A soft-ripened cheese firms in the middle long after its edge has softened. The organisms "
     "that break down the paste live on the surface and work inward, so a young wheel cut in half "
     "shows a chalky core inside a ring that has already turned to cream. _____ the core is the "
     "part of the cheese that has been changed least, not the part that has been changed most.",
     ["In other words,", "However,", "Similarly,", "Afterward,"], "A",
     "The sentence restates the inward progression in terms of how far each region has changed, "
     "which is a rephrasing rather than a qualification. A contrastive marker would set the "
     "statement against the account of surface ripening, and it simply repeats it in different "
     "terms."),

 trn("N5",
     "A newly lifted potato will not sprout however warm it is kept, because it carries a dormancy "
     "that has to run its course. The length of that dormancy is a property of the variety and can "
     "be six weeks in one and five months in another. _____ a store that suits a long-dormant "
     "variety may be useless for a short-dormant one lifted from the next field.",
     ["Thus,", "Instead,", "Nonetheless,", "Previously,"], "A",
     "The variation in dormancy length is the premise and the mismatch between stores is what "
     "follows from it, so the transition marks an inference. A concessive marker would signal that "
     "the mismatch holds despite the variation, when it holds because of it."),

 trn("N6",
     "A wood frog begins converting liver glycogen to glucose within minutes of ice touching its "
     "skin, and the blood concentration can rise sixtyfold in eight hours. In a mammal a "
     "concentration of that order would be a medical emergency. _____ the frog clears it over "
     "several days after thawing with no lasting damage that anyone has been able to detect.",
     ["Yet", "Therefore", "In addition,", "That is,"], "A",
     "The sentence sets the frog's harmless recovery against the emergency the same figure would "
     "represent in a mammal, so a contrastive transition is required. A consequence marker would "
     "make the harmless clearance follow from the emergency, which reverses the relation."),

 trn("N7",
     "The pot-in-pot cooler is two earthenware jars with wet sand between them, and it works "
     "because water evaporating from the outer jar draws heat from whatever the inner jar holds. "
     "The effect depends entirely on the surrounding air being dry enough to take up that water. "
     "_____ the same device that holds vegetables ten degrees below air temperature in the Sahel "
     "does almost nothing on a humid coast.",
     ["Consequently,", "Even so,", "Similarly,", "Beforehand,"], "A",
     "The failure on a humid coast follows directly from the stated dependence on dry air, so the "
     "transition marks a consequence. A concessive marker would present the failure as running "
     "against the explanation, when it is exactly what the explanation predicts."),

 trn("N8",
     "The Romans drew salt at Droitwich from natural brine springs rather than from the sea, and "
     "the springs were strong enough to be boiled straight down without any preliminary "
     "concentration. Sea water at three per cent needs enormous quantities of fuel before it will "
     "yield anything. _____ an inland spring at twenty-five per cent could be worked profitably in "
     "a climate where a coastal saltern would never have dried a pond.",
     ["By contrast,", "For instance,", "Accordingly,", "Furthermore,"], "A",
     "The sentence sets the workable inland spring against the fuel-hungry sea water just "
     "described, so the transition marks an opposition. An example marker would present the spring "
     "as an instance of the sea-water difficulty rather than as its counterpart."),

 trn("N9",
     "Seed destined for long storage is dried to about five per cent moisture before it is frozen, "
     "and the drying is not a convenience. Water left in a seed expands as it freezes and ruptures "
     "the cell walls, so a seed frozen wet is killed by the very step meant to preserve it. _____ "
     "the drying room, not the freezer, is where a bank's collection is most often lost.",
     ["Indeed,", "Otherwise,", "In contrast,", "Later,"], "A",
     "The sentence carries the point about drying further, naming the drying room as the place "
     "where collections are lost, which intensifies rather than qualifies what precedes it. A "
     "contrastive marker would set the claim against the account of why drying matters, and it "
     "extends that account instead."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("S1",
     ["Norway exported lake and fjord ice to Britain from the 1850s.",
      "Norwegian ice was cut closer to its market than American ice was.",
      "A shorter voyage meant a smaller proportion of each cargo melted in transit.",
      "By 1900 Norway was supplying most of the ice landed at British ports.",
      "American shippers kept the longer Boston route and competed on price alone."],
     "explain how the length of the voyage shaped the competition between the two suppliers.",
     ["Because Norwegian ice was cut nearer its British market, a smaller share of each cargo "
      "melted on the way, and Norway had taken most of the British trade by 1900 while American "
      "shippers on the longer Boston route were left competing on price alone.",
      "Norway began exporting lake and fjord ice to Britain in the 1850s and by 1900 was supplying "
      "most of the ice landed at British ports.",
      "American shippers competed on price alone on the longer route from Boston to Britain.",
      "A shorter voyage meant that a smaller proportion of each cargo of ice melted in transit."],
     "A",
     "The goal asks how voyage length shaped the competition, so the response has to link the "
     "shorter passage to the smaller melting loss and then to the outcome for both suppliers. "
     "Reporting the start and end dates of the Norwegian trade records what happened without "
     "naming the voyage as the reason it happened."),

 syn("S2",
     ["At Gu&eacute;rande the salt is raked by hand rather than mechanically.",
      "The paludier draws grey salt from the floor of the pan each afternoon.",
      "A thin crust also forms on the surface of the brine on still, warm evenings.",
      "That surface crust is skimmed separately and sold as fleur de sel.",
      "Fleur de sel forms only when the evening air is dry and the water unruffled."],
     "explain why two products of different value come out of the same pan.",
     ["The paludier rakes grey salt from the floor of the pan each afternoon, but on still, warm "
      "evenings with dry air a thin crust also forms on the surface of the brine, and it is that "
      "separately skimmed crust, which appears only in those conditions, that is sold as fleur de "
      "sel.",
      "At Gu&eacute;rande the salt is raked by hand rather than mechanically, and the paludier "
      "works the pan each afternoon.",
      "Fleur de sel is the thin crust that forms on the surface of the brine and is skimmed "
      "separately.",
      "Grey salt is drawn from the floor of the pan while fleur de sel forms on the surface of the "
      "brine."],
     "A",
     "The goal asks why one pan yields two products of unequal value, which needs the two "
     "harvesting positions, the conditions that produce the surface crust, and the fact that only "
     "that crust is sold as the premium salt. Noting that the salt is raked by hand describes the "
     "method and leaves the two products unexplained."),

 syn("S3",
     ["The Yarmouth red herring was salted for up to three weeks before smoking.",
      "It was then hung in a smokehouse over oak fires for as long as six weeks.",
      "The finished fish was hard, deep red and would keep for a year unrefrigerated.",
      "It was exported in quantity to the Mediterranean and to the Caribbean.",
      "The bloater, cured overnight in the same town, kept for only a few days."],
     "explain why one of the two Yarmouth cures was suited to export and the other was not.",
     ["Three weeks in salt and as much as six weeks over oak fires left the red herring hard and "
      "able to keep for a year without refrigeration, which is why it travelled to the "
      "Mediterranean and the Caribbean while the overnight-cured bloater from the same town lasted "
      "only days.",
      "The Yarmouth red herring was salted for up to three weeks and then hung over oak fires for "
      "as long as six weeks.",
      "The bloater was cured overnight in Yarmouth and kept for only a few days.",
      "Red herrings were exported in quantity to the Mediterranean and to the Caribbean."],
     "A",
     "The goal contrasts two cures by their fitness for export, so the response must give the "
     "long cure, the keeping quality it produced, the markets reached, and the short-cured fish "
     "that could not reach them. Listing the salting and smoking times alone describes one process "
     "without reaching the comparison the goal asks for."),

 syn("S4",
     ["Mimolette is ripened with a mite, Acarus siro, living on its crust.",
      "The mites graze the crust and leave it pitted and grey.",
      "The pitting increases the crust's surface area many times over.",
      "Air and moisture reach the paste more readily through a pitted crust than a smooth one.",
      "Wheels kept free of mites ripen more slowly and taste flatter."],
     "explain how an organism usually treated as a pest contributes to the finished cheese.",
     ["Grazing mites leave the crust pitted and grey, which multiplies its surface area so that air "
      "and moisture reach the paste far more readily than through a smooth crust, and wheels kept "
      "free of them ripen more slowly and taste flatter.",
      "Mimolette is ripened with a mite, Acarus siro, that lives on the crust of the wheel.",
      "The mites graze the crust of the cheese and leave it pitted and grey rather than smooth.",
      "Wheels kept free of mites ripen more slowly than wheels on which the mites are allowed to "
      "graze."],
     "A",
     "The goal asks what the organism contributes, so the response must carry the pitting through "
     "to the enlarged surface, the readier exchange of air and moisture, and the poorer result "
     "without it. Reporting that the mites leave the crust pitted describes the damage and stops "
     "before the benefit the goal asks about."),

 syn("S5",
     ["An Irish turnip pit was dug shallow and lined with rushes.",
      "The roots were heaped in a long ridge rather than a round heap.",
      "A ridge has more surface for its volume than a heap of the same size.",
      "Roots respire in store and the heat they give off has to escape.",
      "A round heap of any size tends to heat at its centre and rot."],
     "explain why the shape of the pit mattered to the keeping of the crop.",
     ["Because roots go on respiring in store and the heat must escape, the crop was heaped in a "
      "long ridge rather than a round heap: a ridge presents more surface for its volume, while a "
      "round heap of any size tends to heat at its centre and rot.",
      "An Irish turnip pit was dug shallow and lined with rushes before the roots were put in.",
      "Roots continue to respire while they are in store and give off heat as they do so.",
      "The roots were heaped in a long ridge rather than in a round heap of the same size."],
     "A",
     "The goal is why the shape mattered, which requires the respiratory heat, the surface-to-"
     "volume advantage of the ridge and the failure of the round heap. Recording that the pit was "
     "dug shallow and lined describes its construction and never reaches the question of shape."),

 syn("S6",
     ["Antarctic fishes and several northern beetles both survive below the freezing point of "
      "their body fluids.",
      "The fishes use glycoproteins built from a repeating sugar-bearing tripeptide.",
      "The beetles use a protein with no sugar and an unrelated repeating structure.",
      "Both molecules bind to the surface of a growing ice crystal and stop it enlarging.",
      "The two lineages have been separate for hundreds of millions of years."],
     "explain what the comparison between the two groups shows about how the trait arose.",
     ["Lineages separate for hundreds of millions of years arrived at molecules with nothing in "
      "common structurally, a sugar-bearing tripeptide in the fishes and a sugarless protein in "
      "the beetles, yet both bind to a growing ice crystal and stop it enlarging, so the trait was "
      "reached twice rather than inherited once.",
      "Antarctic fishes and several northern beetles both survive below the freezing point of "
      "their body fluids.",
      "The fishes use glycoproteins built from a repeating sugar-bearing tripeptide, while the "
      "beetles use a protein with no sugar at all.",
      "Both molecules work by binding to the surface of a growing ice crystal and stopping it from "
      "enlarging."],
     "A",
     "The goal asks what the comparison shows about the trait's origin, so the response must set "
     "the unrelated structures against the shared function and the long separation, and draw the "
     "conclusion that the trait arose twice. Naming the two different molecules states the "
     "difference without saying what follows from it."),

 syn("S7",
     ["A trial in northern Nigeria stored aubergines in pot-in-pot coolers and in open baskets.",
      "Aubergines in open baskets were unsaleable after three days.",
      "Aubergines in the coolers remained saleable for twenty-seven days.",
      "The coolers cost about two dollars each to make from local clay.",
      "Sellers using the coolers could hold stock until prices rose instead of selling at once."],
     "explain how a low-cost device changed the sellers' commercial position, not merely the "
     "condition of the crop.",
     ["Coolers costing about two dollars to make from local clay kept aubergines saleable for "
      "twenty-seven days against three days in open baskets, which let sellers hold their stock "
      "until prices rose rather than selling everything at once.",
      "Aubergines held in pot-in-pot coolers remained saleable for twenty-seven days, while those "
      "in open baskets were unsaleable after three.",
      "The pot-in-pot coolers used in the trial cost about two dollars each to make from local "
      "clay.",
      "A trial in northern Nigeria compared aubergines stored in pot-in-pot coolers with aubergines "
      "stored in open baskets."],
     "A",
     "The goal asks for the commercial change and not just the storage life, so the response has "
     "to carry the cost and the twenty-seven days through to the sellers' new freedom to wait for "
     "a better price. Giving the two storage lives reports the crop's condition and stops short of "
     "the commercial point the goal names."),

 syn("S8",
     ["Lake Magadi in Kenya is both extremely alkaline and extremely saline.",
      "Its surface is covered by a crust of sodium carbonate up to forty metres thick.",
      "Dense blooms of cyanobacteria grow in the brine beneath the crust.",
      "Lesser flamingos feed almost exclusively on those cyanobacteria.",
      "The lake supports one of the largest concentrations of the species in Africa."],
     "explain how conditions that exclude most life come to support a large bird population.",
     ["Water so alkaline and saline that most organisms are excluded still carries dense blooms of "
      "cyanobacteria beneath its sodium carbonate crust, and because lesser flamingos feed almost "
      "exclusively on those cyanobacteria the lake supports one of the largest concentrations of "
      "the species in Africa.",
      "Lake Magadi in Kenya is both extremely alkaline and extremely saline, and its surface "
      "carries a crust of sodium carbonate up to forty metres thick.",
      "Dense blooms of cyanobacteria grow in the brine beneath the crust at Lake Magadi.",
      "Lesser flamingos feed almost exclusively on cyanobacteria and gather at Lake Magadi in large "
      "numbers."],
     "A",
     "The goal asks how hostile conditions end in abundance, which needs the exclusion, the "
     "organism that tolerates it, the bird that eats only that organism, and the resulting numbers. "
     "Describing the lake's chemistry and its crust establishes the hostility and never reaches the "
     "birds."),

 syn("S9",
     ["A collecting team gathers seed from at least fifty plants at a site.",
      "Seed from a single plant would capture only a fraction of the population's variation.",
      "The team records the coordinates, the soil and the associated species at each site.",
      "A sample without those records cannot be matched to a habitat if the site is later lost.",
      "About a fifth of accessions are rejected on arrival for insufficient sampling or records."],
     "explain why a collection is judged on more than the quantity of seed it contains.",
     ["Seed is gathered from at least fifty plants because one plant would capture only a fraction "
      "of a population's variation, and the coordinates, soil and associated species are recorded "
      "because a sample without them cannot be matched to a habitat if the site is lost, which is "
      "why about a fifth of accessions are rejected on arrival.",
      "A collecting team gathers seed from at least fifty plants at each site it visits.",
      "About a fifth of accessions are rejected on arrival for insufficient sampling or records.",
      "The team records the coordinates, the soil and the associated species at each collecting "
      "site."],
     "A",
     "The goal asks why quantity alone is not the measure, so the response must give both "
     "requirements — breadth of sampling and the site records — with the reason for each and the "
     "rejection rate that enforces them. Stating the fifty-plant rule covers one requirement and "
     "leaves the records out."),

]

DROPPED = {}
