#!/usr/bin/env python3
"""
Reading & Writing authored for Test 22.

All 81 items are original. The transcribed pools were spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed answer key has to
be re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers
in 81 that way). Every item below carries a `why` recording the reasoning that
produced the key AND the reason the strongest distractor fails — that record IS
the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are worded, never bare punctuation. Test 8 shipped
Boundaries items whose four options were ", " / "; " / ": " / " and ", which a
student sees as four empty rows; the real test repeats the words on either side
of the blank inside every option so that each choice reads as the resulting
sentence. Every Boundaries item here is written that way from the start.
Form/Structure items whose options are genuinely words ("stands" / "stand") are
left as words, which is also how the real test presents them.

Command of Evidence mixes three quotation items, three data-table items and
three finding-if-true items. The data items carry a real <table> in the passage
using the house style block; none of them describes a graph in prose, because
no image can be produced from here.

Test 22's assigned territory is beekeeping and apiaries, honey extraction,
sugar refining, beet processing, confectionery boiling, and beeswax and candle
making, and every passage below sits inside it. Topics were screened against
../rw_authored_corpus.json — all 1,295 passages banked or authored across
Tests 1-21 — by keyword and by 5-gram / Jaccard overlap (see
check_originality.py in this directory) BEFORE anything was drafted.

Candidates dropped at the planning stage because the corpus already covers
them, rather than written and later discovered:

    propolis as a hive material, varroa as a virus vector, the waggle dance,
    ultraviolet nectar guides, mason bees and their stem nests, skeps and the
    destruction of the colony at harvest, hive weights recorded on a scale,
    honey moisture and fermentation above twenty per cent water, honeyguides
    and honey hunting, buzz pollination, lost-wax casting, polyethylene glycol
    replacing water in waterlogged wood, the lotus effect and cuticular wax,
    lime burning, and colony life framed as a general lesson in eusociality
    (the corpus already carries naked mole-rats, army ants and honeypot ants).

What is left, and what this file is built from:

    queen mandibular pheromone, swarm quorum sensing, the winter cluster,
    royal jelly and caste, laying workers, hygienic behaviour, drone
    congregation areas, comb cell size, wax scales and festooning, stingless
    bees and their honey pots, the bee space and the movable frame, the queen
    excluder, granulation and seeding, heather honey and thixotropy, honeydew
    honey, melissopalynology, HMF as a heating marker, honey as a wound
    dressing, mead, bone char, the vacuum pan, molasses exhaustion,
    polarimetry, the sugar loaf and the nippers, carbon isotopes as a cane/beet
    test, the Brix hydrometer, the diffusion battery, soil tare, Marggraf and
    Achard, the Continental blockade, bolting and vernalisation, raffinose,
    the boiling stages, invert sugar and graining, the plaited wick, wax bloom,
    the spermaceti standard candle, and Faraday on the structure of a flame.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T22"
MODULE = "RW"

TBL = 'style="border-collapse:collapse;margin:0.75rem 0;"'
TH = ('style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;'
      'text-align:left;background:#F4F6F8;"')
TD = 'style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;"'


def table(headers, rows):
    """The house-style data table used by the Command of Evidence data items."""
    head = "".join(f"<th {TH}>{h}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table {TBL}><tr>{head}</tr>{body}</table>"


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
     "A queen honeybee secretes a blend of compounds from glands in her head. Workers that touch "
     "her lick the blend from her body and carry it on as they groom one another, so within an hour "
     "a colony of thirty thousand has registered that she is present. The chemistry never travels "
     "through the air; it is _____ from bee to bee.",
     ["relayed", "broadcast", "concealed", "diluted"], "A",
     "The passage says the compounds move by touch and grooming and expressly rules out travel "
     "through the air, so the word must name a hand-to-hand passage. The 'broadcast' option names "
     "exactly the airborne spread the last clause denies."),

 wic("W2",
     "Scouts returning from a hollow tree dance for it on the surface of a hanging swarm, and a "
     "scout persuaded by another's dance flies out to inspect that cavity for herself. No bee ever "
     "compares the candidate sites. A site wins because it keeps drawing inspectors until the "
     "number gathered there passes a threshold, so the choice is _____ rather than made by any one "
     "individual.",
     ["accumulated", "imposed", "inherited", "rehearsed"], "A",
     "The text describes a count building up at one site until a threshold is crossed, which is a "
     "decision that adds up rather than one anybody takes. The 'imposed' option would require some "
     "authority to hand the decision down, and the passage says no individual makes it."),

 wic("W3",
     "Through the winter a colony forms a ball on the comb and shivers its flight muscles without "
     "moving its wings. The bees packed on the outside act as a coat while those inside generate "
     "the heat. The coat is not something the colony builds but something it _____, since every "
     "part of it is a live animal that will trade places with a warmer bee once it chills.",
     ["occupies", "constitutes", "imports", "conceals"], "B",
     "The last clause explains that the coat is made of the bees themselves, so the word must say "
     "that they are what it consists of. The 'occupies' option would place the bees inside a coat "
     "that already existed, which is the reading the sentence rejects."),

 wic("W4",
     "Any female larva in a colony can become a queen, and which one does is settled entirely by "
     "what she is fed in her first days. Larvae given royal jelly throughout develop the ovaries "
     "and the long abdomen of a queen; those moved onto a coarser diet become workers. Caste here "
     "is not written into the egg but _____ after it hatches.",
     ["conferred", "predicted", "inherited", "reversed"], "A",
     "The sentence contrasts something fixed at the egg with something done to the larva later, and "
     "feeding is what does it, so the word must mean granted from outside. The 'inherited' option "
     "restates the very thing the sentence rules out."),

 wic("W5",
     "Honey holds more sugar than water at room temperature can keep in solution, so sooner or "
     "later glucose comes out of it as crystals. A packer who wants a smooth set does not fight "
     "this. A little finely crystallised honey is stirred in, which gives the sugar thousands of "
     "small starting points so that no single crystal grows coarse. The treatment does not prevent "
     "the change so much as _____ it.",
     ["govern", "delay", "reverse", "conceal"], "A",
     "Seeding does not stop crystallisation; it settles how many crystals form and therefore how "
     "coarse they are, which is control rather than prevention. The 'delay' option claims the "
     "change is postponed, but the passage has the seeded honey setting rather than setting later."),

 wic("W6",
     "Honey from ling heather sets to a jelly in the comb and will not fly out of a spinning "
     "extractor, so a pricking machine or a press is used instead. Stirred hard, the same honey "
     "turns fluid again, and left alone it stiffens once more. Its thickness is therefore not a "
     "fixed property of the honey but one _____ by handling.",
     ["altered", "measured", "certified", "preserved"], "A",
     "The honey is described as stiff, then fluid under stirring, then stiff again, so handling "
     "changes the thickness rather than recording it. The 'measured' option would make the stirring "
     "an act of assessment, and nothing in the text takes a reading."),

 wic("W7",
     "Every jar of honey carries a dust of pollen grains picked up by the bees that made it, and "
     "each grain keeps the shape of the plant that shed it. A microscopist who counts them can say "
     "which flowers a colony worked and, from the mixture, roughly where it stood. The pollen is an "
     "entirely unintended _____ of the honey's origin.",
     ["record", "guarantee", "advertisement", "flavouring"], "A",
     "The grains preserve which plants were visited and let an analyst reconstruct a location, "
     "which is what a record does. The 'guarantee' option imports an assurance to a buyer, and the "
     "passage says the pollen arrives without anyone intending it."),

 wic("W8",
     "Raw cane liquor is brown, and the colour sits in compounds that no amount of boiling drives "
     "off. Refiners once ran the liquor through beds of charred bone, whose porous carbon holds "
     "coloured molecules on its surface while the sugar passes on through. The bed changes nothing "
     "about the sugar; it merely _____ what would otherwise travel with it.",
     ["intercepts", "dissolves", "sweetens", "multiplies"], "A",
     "The carbon catches the coloured molecules and lets the sugar go by, which is a matter of "
     "stopping something in transit. The 'dissolves' option describes taking the colour into "
     "solution, and the passage has it held on a surface instead."),

 wic("W9",
     "A syrup boiled at ordinary pressure scorches long before the last of its water is gone. Under "
     "a partial vacuum the same syrup boils at a far lower temperature, so a refiner can drive off "
     "water until crystals appear without darkening what remains. The vacuum pan's whole advantage "
     "is that it makes a hard boil _____.",
     ["gentle", "faster", "cheaper", "unnecessary"], "A",
     "The pan's benefit is described entirely as boiling at a lower temperature and avoiding "
     "scorching, which is mildness rather than speed or economy. The 'unnecessary' option would "
     "mean no boiling happens, but the syrup is still boiled until crystals form."),

 wic("W10",
     "Each time a massecuite is spun, crystals are thrown out of it and a darker syrup is left "
     "behind. That syrup still holds sugar, so it is boiled and spun again, and again, until what "
     "remains would cost more to work than the sugar in it is worth. The final liquor is not free "
     "of sugar; it is simply _____.",
     ["exhausted", "purified", "wasted", "concentrated"], "A",
     "The syrup is worked until further recovery stops paying, so what has run out is the "
     "worthwhile sugar rather than all of it, which is exactly the distinction the last sentence "
     "draws. The 'purified' option would mean impurities had been removed, and the liquor is the "
     "impure fraction."),

 wic("W11",
     "Sliced beet is never pressed. The cossettes travel through a chain of vessels against a "
     "current of hot water, and the sugar leaves the plant cells by passing through their walls "
     "into the weaker liquid outside. Each vessel meets water a little poorer in sugar than the one "
     "before it, so the difference that drives the sugar out is continually _____.",
     ["renewed", "reduced", "measured", "reversed"], "A",
     "Sending the cossettes towards ever weaker water keeps re-establishing the gap in "
     "concentration that moves the sugar, so the difference is restored rather than worn away. The "
     "'reduced' option describes what would happen if the water were not replaced, which is the "
     "problem the arrangement is built to avoid."),

 wic("W12",
     "A boiled sweet is a sugar syrup cooled so quickly that its molecules never line up into "
     "crystals. Left as pure sucrose it grains anyway within a few weeks, so confectioners add a "
     "little acid during the boil, which splits some of the sucrose into two simpler sugars that "
     "get in the way of the crystal lattice. The addition is made to keep the sweet _____.",
     ["clear", "sweeter", "harder", "cheaper"], "A",
     "Graining is the formation of crystals in what was a glassy solid, so preventing it preserves "
     "transparency. The 'sweeter' option names a taste, and splitting sucrose is described here "
     "purely as an obstacle to the lattice."),

 meaning("W13",
     "Faraday's lectures on the candle turned on one observation: the flame is hollow. Wax drawn up "
     "the wick is vaporised inside a dark cone at the centre, where too little air reaches it to "
     "burn. Only at the surface of that cone does the vapour meet oxygen. The luminous yellow an "
     "audience sees is solid carbon, heated until it glows and then <u>spent</u> at the outer edge "
     "where the air arrives.",
     "spent",
     ["burned away", "paid out", "exhausted by effort", "scattered widely"], "A",
     "The carbon glows and then meets oxygen at the outer edge, so what happens to it is "
     "combustion. The 'paid out' reading takes the commercial sense of the word, which has no place "
     "in a description of a flame."),

 meaning("W14",
     "Before instruments could measure light directly, the brightness of a lamp was reported by "
     "comparing it with a candle of stated composition burning at a stated rate. The comparison was "
     "made by eye, in a darkened room, by sliding a screen until two patches of light looked equal. "
     "Because the standard was a burning object rather than an instrument, its value <u>drifted</u> "
     "with the quality of the wax and the trim of the wick.",
     "drifted",
     ["varied", "floated", "wandered off course", "gathered"], "A",
     "The sentence attributes the change to the wax and the wick, so the word describes a standard "
     "that fails to hold one value. The 'floated' reading takes the literal sense of moving on a "
     "liquid, which nothing in the passage supports."),

 meaning("W15",
     "Beet juice leaves the diffusers carrying substances that would stop sugar crystallising. Milk "
     "of lime is stirred in, which reacts with many of them, and carbon dioxide is then bubbled "
     "through, turning the surplus lime into chalk. The chalk settles out and takes the trapped "
     "impurities down with it, so the process <u>fixes</u> what would otherwise stay in solution.",
     "fixes",
     ["immobilises", "repairs", "determines", "prepares"], "A",
     "The impurities end up locked into a solid that settles out, so the word names their being "
     "held fast. The 'repairs' reading treats the impurities as damage to be mended, and nothing is "
     "mended here."),

 # ------------------------------------------- Text Structure and Purpose (6)
 tsp("S1",
     "Before 1851 a beekeeper who wanted comb out of a hive cut it out. Lorenzo Langstroth measured "
     "the gaps bees leave open as they build and found that a space of roughly eight millimetres is "
     "left clear, while anything wider is filled with comb and anything narrower is sealed shut. "
     "<u>He hung his frames so that a gap of that width surrounded every one of them.</u> The comb "
     "was then fastened to the frame and to nothing else, and a hive could be opened and closed "
     "without being damaged.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It applies the measurement just reported in order to explain how a hive became openable.",
      "It questions whether the measurement Langstroth reported was accurate.",
      "It introduces a difficulty that the rest of the text goes on to resolve.",
      "It compares Langstroth's hive with those used by his contemporaries."],
     "A",
     "The sentence takes the eight-millimetre figure established just before it and turns it into a "
     "construction decision whose consequence the closing sentence states, so it is the hinge "
     "between measurement and result. The option calling it a difficulty gets the direction wrong: "
     "what follows is the benefit, not a problem."),

 tsp("S2",
     "A lorry arriving at a beet factory is weighed, and so is the earth that comes with the crop. "
     "A sample is drawn from the load, washed and reweighed, and the difference is charged against "
     "the grower. The practice looks like an accountant's nicety, but a wet lifting season can "
     "leave a fifth of a load's weight as soil, and a factory that paid for that would be paying to "
     "haul it and to wash it as well.",
     "Which choice best states the main purpose of the text?",
     ["To explain why a deduction that appears petty is in fact substantial.",
      "To argue that growers are charged unfairly for the soil on their crop.",
      "To describe the equipment used to weigh a lorry at a factory.",
      "To compare a wet lifting season with a dry one."],
     "A",
     "The text sets up the deduction as something that looks trivial and then gives the figure and "
     "the extra costs that make it matter, which is a correction of a first impression. The option "
     "about unfairness takes a side the passage never takes; it justifies the charge rather than "
     "objecting to it."),

 tsp("S3",
     "A hydrometer floats higher in a dense liquid than in a thin one, and the density of a syrup "
     "rises as the sugar in it rises. <u>A scale can therefore be printed along the stem in "
     "percentage of sugar rather than in units of density.</u> A boiler reads the figure straight "
     "off and calculates nothing. The instrument measures one property and reports another, which "
     "is convenient so long as nothing but sugar is dissolved in the liquid.",
     "Which choice best describes the function of the underlined sentence in the text?",
     ["It states the step that turns a density reading into the figure a boiler actually wants.",
      "It concedes a limitation that the final sentence then withdraws.",
      "It offers an example of a syrup whose density has been measured.",
      "It explains the physical reason that a hydrometer floats at all."],
     "A",
     "The sentence sits between the physics of flotation and the boiler's practice, and what it "
     "adds is the relabelling of the scale that connects them. The option calling it a concession "
     "misreads the order: the limitation arrives only in the last sentence and is not withdrawn."),

 tsp("S4",
     "Stingless bees of the American tropics store honey not in hexagonal comb but in clusters of "
     "egg-shaped pots of wax and resin, each far larger than a brood cell and closed with a lid. "
     "The honey in them is thinner and more acid than a honeybee's and ferments readily, which is "
     "why it travels badly and has stayed a local product. Keepers in Yucat&aacute;n have worked "
     "these colonies in hollow logs for centuries, and a log is opened at the end rather than at "
     "the top.",
     "Which choice best states the main purpose of the text?",
     ["To set out several respects in which keeping stingless bees differs from keeping honeybees.",
      "To argue that stingless-bee honey deserves a wider market than it has.",
      "To trace the history of beekeeping in Yucat&aacute;n from its beginnings.",
      "To explain why stingless bees have no sting."],
     "A",
     "Storage vessels, the character of the honey and the way a hive is opened are each given in "
     "contrast with honeybee practice, so the text is an inventory of differences. The option about "
     "a wider market runs against the passage, which explains why the honey stays local."),

 tsp("S5",
     "Refined sugar reached a nineteenth-century kitchen as a hard cone wrapped in blue paper, and "
     "a cook broke lumps from it with iron nippers. <u>The cone was not a shape chosen for the shop "
     "counter.</u> It was the mould in which the sugar had drained: syrup was run into a conical "
     "pot with a hole at the point, and the molasses that would have kept the sugar dark ran out of "
     "the hole while the crystals stayed behind.",
     "Which choice best describes the function of the underlined sentence in the text?",
     ["It rejects one explanation of the cone's shape so that the real one can be given.",
      "It introduces the tools a cook needed in order to use the sugar.",
      "It qualifies the claim that the sugar had been refined at all.",
      "It contrasts two kinds of mould used in the same trade."],
     "A",
     "The sentence denies that the shape was a matter of presentation, and the sentence after it "
     "supplies the draining process that actually produced it, so its work is to clear the ground. "
     "The option about a cook's tools describes the sentence before it, not the underlined one."),

 tsp("S6",
     "A brood disease spreads through a colony when a larva dies sealed in its cell. Some colonies "
     "contain bees that find such a cell, uncap it and drag the contents out within a day or two, "
     "and a breeder can test a colony for the trait by killing a patch of brood with liquid "
     "nitrogen and counting how much of it has been cleared two days later. The test says nothing "
     "about the disease itself, only about the colony's housekeeping, and it is the housekeeping "
     "that is passed on.",
     "Which choice best states the main purpose of the text?",
     ["To explain how a heritable behaviour can be measured without using the disease it guards against.",
      "To describe the symptoms by which a brood disease is recognised.",
      "To warn that liquid nitrogen is hazardous in an apiary.",
      "To compare two diseases that affect sealed brood."],
     "A",
     "The passage introduces the removal behaviour, gives a test that substitutes frozen brood for "
     "diseased brood, and closes by saying the behaviour is what is inherited, so the point is the "
     "measurement. The option about symptoms fails because no symptom is described anywhere in the "
     "text."),

 # ---------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "Drones from many colonies gather each afternoon at the same few places, thirty metres up and "
     "often above one particular fold in the landscape, and a queen on her mating flight goes to "
     "one of them. The same places are used year after year, although no drone lives long enough to "
     "have visited one in a previous season. What draws them there is still argued over. What is "
     "clear is that a queen meets drones from colonies other than her own, which is the point of "
     "the arrangement.",
     "Which choice best states the main idea of the text?",
     ["Drone gathering places mix bees from different colonies, though how each generation finds them is unsettled.",
      "Drones return each year to sites they remember from earlier seasons.",
      "A queen mates with drones drawn from her own colony.",
      "The location of the sites is fully accounted for by the shape of the land."],
     "A",
     "The text states the outcome that matters, a queen meeting drones from elsewhere, and says "
     "plainly that what draws the drones is still disputed, so both halves belong in the main idea. "
     "The option about remembered sites contradicts the sentence saying no drone lives long enough "
     "to have been there before."),

 cid("C2",
     "Beet molasses holds sugar that will not crystallise, and one reason is a three-part sugar "
     "called raffinose. A raffinose molecule is close enough in shape to sucrose to take a place at "
     "the growing face of a sucrose crystal, and different enough that the next layer cannot sit "
     "cleanly on top of it. A small proportion is therefore enough to slow crystallisation and to "
     "deform whatever crystals do form.",
     "Which choice best states the main idea of the text?",
     ["Raffinose disrupts sugar crystals because it resembles sucrose closely but not exactly.",
      "Raffinose is the only substance in beet molasses that affects crystallisation.",
      "Raffinose prevents any sucrose crystals from forming in molasses.",
      "Raffinose is chemically unrelated to sucrose."],
     "A",
     "The passage turns on the double fact that raffinose fits the crystal face and then blocks the "
     "next layer, and both depend on a resemblance that is not quite exact. The option calling it "
     "the only such substance overreaches the text, which introduces it as one reason among "
     "others."),

 cid("C3",
     "Honey taken from a hive is not sterile, yet bacteria placed in it die. It holds so little "
     "free water that a cell in contact with it loses its own, and an enzyme the bees add releases "
     "hydrogen peroxide slowly as the honey draws moisture out of a wound. Dressings made from "
     "honey are nevertheless sterilised by irradiation before use, because the spores of certain "
     "soil organisms survive what kills everything else.",
     "According to the text, why are honey dressings irradiated before they are used?",
     ["Certain spores are not destroyed by the effects that kill other organisms in honey.",
      "Irradiation raises the concentration of hydrogen peroxide in the honey.",
      "Honey loses its low water content once it is packed into a dressing.",
      "Bacteria multiply in honey unless the honey is treated first."],
     "A",
     "The final clause names surviving spores as the reason, in contrast with everything else the "
     "honey kills. The option about bacteria multiplying reverses the second sentence, which says "
     "bacteria placed in honey die."),

 cid("C4",
     "Cane sugar reached Europe by sea, and when the British fleet closed the Atlantic to French "
     "shipping after 1806 the price of sugar in Paris rose beyond most households. Napoleon ordered "
     "land planted with beet, subsidised factories and licensed schools to teach the extraction. "
     "The industry he built could not compete once the blockade was lifted and much of it failed, "
     "but the beet varieties and the extraction plant survived to be taken up again a generation "
     "later.",
     "Which choice best states the main idea of the text?",
     ["An industry created for wartime reasons collapsed commercially yet left behind what a later revival used.",
      "The blockade of French shipping succeeded in raising the price of cane sugar.",
      "Napoleon's beet factories were profitable from the moment they opened.",
      "Beet sugar replaced cane sugar in Europe within a single generation."],
     "A",
     "The last sentence sets the industry's commercial failure against the survival of its "
     "varieties and plant, and that pairing is the point of the passage. The option calling the "
     "factories profitable contradicts the statement that they could not compete."),

 cid("C5",
     "Workers build two sizes of cell, the smaller for workers and the larger for drones, and a "
     "queen lays an unfertilised egg in a large cell and a fertilised one in a small cell. The comb "
     "therefore records a colony's intentions: a beekeeper who finds a frame of drone comb in June "
     "is looking at a decision the workers took some weeks earlier, before there was any brood in "
     "it to see.",
     "Which choice best states the main idea of the text?",
     ["The proportions of cell sizes in a comb reveal choices the colony made before any brood was laid.",
      "A queen chooses the size of cell in which each of her eggs will be laid.",
      "Drone brood and worker brood are indistinguishable once the cells are sealed.",
      "Workers build comb only when a beekeeper gives them a frame to build on."],
     "A",
     "The passage moves from who builds which cell to what a beekeeper can read off a comb, and the "
     "closing clause makes the timing explicit. The option putting the choice with the queen "
     "reverses the text, in which the workers build the cells and the queen responds to them."),

 cid("C6",
     "A solution of sucrose turns the plane of polarised light to the right, and the angle it turns "
     "is proportional to how much sucrose is present. That made an optical instrument the standard "
     "assay of the sugar trade, and the word &ldquo;polarisation&rdquo; came to mean a purity "
     "figure printed on a contract. The method fails, though, whenever other optically active "
     "substances are in the sample, and beet molasses contains several.",
     "According to the text, what limits the usefulness of the polarimeter?",
     ["Other substances in a sample can rotate polarised light as sucrose does.",
      "The angle turned is not proportional to the amount of sucrose present.",
      "Contracts in the sugar trade record purity in other units.",
      "Beet molasses contains no sucrose at all."],
     "A",
     "The final sentence names optically active substances other than sucrose as what defeats the "
     "reading, and gives beet molasses as the case. The option denying proportionality contradicts "
     "the first sentence, which is what makes the assay work in the first place."),

 # ----------------------------------------------- Command of Evidence (9)
 coe("E1",
     "In her 1908 handbook <em>The Cottage Apiary</em>, the beekeeper Hannah Verrell describes a "
     "year's work with bees. One scholar argues that Verrell consistently presents the hive as a "
     "workplace to be managed rather than a wonder to be admired.",
     "Which quotation from <em>The Cottage Apiary</em> most effectively illustrates the scholar's claim?",
     ["&ldquo;Set the smoker going before you touch the roof, and have the spare box at your elbow; a colony left standing open loses more in ten minutes than it makes in a day.&rdquo;",
      "&ldquo;There is no sound in nature like the roar of a swarm rising, and I have stood in the orchard and let the work wait.&rdquo;",
      "&ldquo;The bee is a creature of the sun, and its year is written in the flowers of the parish.&rdquo;",
      "&ldquo;My grandmother kept her hives under the south wall, as her mother had before her.&rdquo;"],
     "A",
     "The quotation about the smoker and the spare box gives instructions and then justifies them "
     "by a loss of yield, which is management and nothing else. The quotation about the roar of a "
     "swarm shows the opposite, since the writer stops working in order to admire it."),

 coe("E2",
     "In the poem &ldquo;The Chandler's Shop,&rdquo; the speaker recalls a working life spent "
     "making candles. A student claims that the poem presents the trade as work that leaves its "
     "mark on the maker's own body.",
     "Which quotation from &ldquo;The Chandler's Shop&rdquo; most effectively illustrates the student's claim?",
     ["&ldquo;My thumbs are ridged where the wick ran through, / and the smell of it goes home with me.&rdquo;",
      "&ldquo;The tapers hang in rows like winter rain, / each one a finger's length.&rdquo;",
      "&ldquo;Outside, the street is dark by four, / and the shutters take the wind.&rdquo;",
      "&ldquo;Wax is a patient thing; it keeps / whatever shape you leave it in.&rdquo;"],
     "A",
     "Ridged thumbs and a smell carried home are both marks the work has left on the speaker "
     "personally, which is exactly the claim. The lines comparing hanging tapers to winter rain "
     "describe the goods rather than the maker."),

 coe("E3",
     "In his account of a season spent working at a beet factory, the engineer Tom&aacute;s Weisz "
     "describes the plant and its routine. A student argues that Weisz emphasises the factory's "
     "unbroken timetable rather than its size.",
     "Which quotation from Weisz's account most effectively supports the student's argument?",
     ["&ldquo;From the first slice in September to the last in January the diffusers never stopped, and neither, in eight-hour turns, did we.&rdquo;",
      "&ldquo;The evaporator hall was long enough that a man at one end could not be recognised from the other.&rdquo;",
      "&ldquo;Beet came in by rail and by road, and the yard held twelve thousand tonnes of it at a time.&rdquo;",
      "&ldquo;The pans stood four storeys high and were lagged in white.&rdquo;"],
     "A",
     "The quotation about September to January and eight-hour turns is entirely about continuous "
     "running, which is the timetable the argument names. The quotation about the length of the "
     "evaporator hall speaks to size, the very thing the student says Weisz subordinates."),

 coe("E4",
     "Honeys richer in glucose are expected to crystallise sooner than honeys with less of it. A "
     "beekeeper recorded the glucose content of honey from four sources and the number of weeks "
     "each took to set solid in a jar held at 14&nbsp;&deg;C."
     + table(["Source", "Glucose (%)", "Weeks to set"],
             [["Oilseed rape", "40", "2"], ["Clover", "33", "9"],
              ["Lime", "30", "14"], ["Ling heather", "28", "26"]])
     + "The beekeeper's results bear the expectation out: _____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["the oilseed rape honey, at 40 per cent glucose, set in 2 weeks, while the ling heather honey, at 28 per cent, took 26.",
      "the clover honey took 9 weeks to set solid in the jar.",
      "the lime honey contained 30 per cent glucose.",
      "the ling heather honey took longer to set than any of the other three."],
     "A",
     "Only the pairing of the richest honey with the shortest time and the poorest with the longest "
     "puts both variables together, which is what supporting the expectation requires. The entry "
     "reporting the clover honey's nine weeks gives a setting time with no glucose figure beside "
     "it, so it cannot show the relationship."),

 coe("E5",
     "A wax that melts at a higher temperature is expected to burn more slowly in a candle. A "
     "chandler measured the melting point of four waxes and how many minutes a candle of each took "
     "to burn down one centimetre."
     + table(["Wax", "Melting point (&deg;C)", "Minutes per centimetre"],
             [["Paraffin", "52", "38"], ["Blend", "58", "43"],
              ["Stearin", "63", "47"], ["Beeswax", "64", "52"]])
     + "The chandler's measurements support the expectation: _____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["beeswax, melting at 64&nbsp;&deg;C, burned at 52 minutes per centimetre, while paraffin, melting at 52&nbsp;&deg;C, burned at only 38.",
      "the blend melted at 58&nbsp;&deg;C, between the melting points of paraffin and stearin.",
      "stearin took 47 minutes to burn down one centimetre.",
      "beeswax had the highest melting point of the four waxes tested."],
     "A",
     "The comparison of the highest-melting wax with the lowest-melting one, giving both the "
     "temperature and the burning rate for each, is the only option that shows the two quantities "
     "moving together. The entry giving beeswax the highest melting point supplies one variable and "
     "stops."),

 coe("E6",
     "Beet left in the ground longer accumulates more sugar, but late lifting also takes place when "
     "the fields are wettest, so more soil is carried in with the crop. A factory recorded the "
     "sugar content of the beet and the soil tare of the load on four dates in one campaign."
     + table(["Lifting date", "Sugar in beet (%)", "Soil tare (%)"],
             [["20 September", "15.8", "6"], ["15 October", "17.1", "9"],
              ["10 November", "17.9", "14"], ["5 December", "18.2", "21"]])
     + "The factory's records show both halves of this pattern: _____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["between 20 September and 5 December the sugar in the beet rose from 15.8 to 18.2 per cent while the soil tare rose from 6 to 21 per cent.",
      "the beet lifted on 10 November contained 17.9 per cent sugar.",
      "the soil tare on 15 October was 9 per cent, higher than it had been in September.",
      "the sugar content rose on every one of the four dates recorded."],
     "A",
     "Both halves of the pattern are named in the text, so the completion has to report both the "
     "rise in sugar and the rise in tare across the campaign, and only one option does. The entry "
     "giving November's sugar content alone leaves the soil tare, which is half the claim, "
     "unaddressed."),

 coe("E7",
     "A colony survives the winter inside a tight cluster of bees whose centre stays warm. "
     "Researchers propose that the warmth comes from heat the bees themselves generate rather than "
     "from the nest cavity holding heat in.",
     "Which finding, if true, would most directly support the researchers' proposal?",
     ["Colonies in thin-walled hives hold the same cluster-centre temperature as colonies in thickly insulated hives, but eat considerably more stores to do it.",
      "The temperature at the centre of a cluster falls as the outside temperature falls.",
      "Bees on the outside of a cluster are cooler than bees at its centre.",
      "Colonies that enter winter with more stores survive it more often than colonies with fewer."],
     "A",
     "If the same centre temperature is reached whatever the insulation, and the poorly insulated "
     "colonies pay for it in food, then the heat is being made rather than merely retained. The "
     "finding that outer bees are cooler than inner ones is consistent with either explanation and "
     "so distinguishes nothing."),

 coe("E8",
     "Confectioners add a little acid to a sugar syrup during the boil, and sweets made that way "
     "resist graining. One confectioner claims that the acid works by converting part of the "
     "sucrose into simpler sugars, not by making the syrup acidic as such.",
     "Which finding, if true, would most directly support the confectioner's claim?",
     ["Sweets boiled with an acid that does not split sucrose grain as quickly as sweets boiled with no acid at all.",
      "Sweets boiled with acid taste slightly sharper than sweets boiled without it.",
      "Acid is normally added towards the end of the boil rather than at the beginning.",
      "Boiled sweets of every kind grain more quickly in damp weather than in dry."],
     "A",
     "An acid that acidifies the syrup but leaves the sucrose intact, and that fails to prevent "
     "graining, isolates the splitting as the effective step. The finding about damp weather "
     "concerns storage rather than what the acid does during the boil."),

 coe("E9",
     "The pollen in a jar of honey is sometimes used to say where the honey was made. A laboratory "
     "claims that the pollen identifies a place rather than merely a season's flowering.",
     "Which finding, if true, would most directly support the laboratory's claim?",
     ["Honeys made in the same month at two apiaries fifty kilometres apart carry pollen assemblages that differ more than honeys made at one apiary in different months.",
      "Honey contains pollen from plants that bees visit for pollen but not for nectar.",
      "Pollen grains keep their shape in honey for decades after the honey is jarred.",
      "The same plant comes into flower on different dates in different years."],
     "A",
     "Setting variation between places against variation between times is the only way to show that "
     "place is what the pollen tracks, and the comparison described does exactly that. The finding "
     "about grains keeping their shape supports the method's durability without saying what the "
     "pollen identifies."),

 # ------------------------------------------------------------ Inferences (6)
 inf("I1",
     "A colony that loses its queen and has no young larvae from which to raise another will, after "
     "a few weeks, contain workers that lay eggs. Those workers have never mated, so every egg they "
     "lay is unfertilised and can only become a drone, and a worker lays untidily, often several "
     "eggs to a cell. A beekeeper who finds several eggs in each cell and drone brood raised in "
     "worker-sized cells can therefore conclude that _____",
     ["the colony has been without a queen long enough for its workers to have started laying.",
      "the colony's queen has been superseded recently and is laying poorly.",
      "the colony's queen mated with drones from a distant apiary.",
      "the colony's workers have been fed royal jelly throughout their development."],
     "A",
     "Multiple eggs to a cell and drone brood in worker cells are the two signs the passage assigns "
     "to unmated laying workers, and it says those appear only after weeks without a queen. The "
     "option about a recently superseded queen would leave a mated layer in the hive, which could "
     "not produce drone brood in worker cells."),

 inf("I2",
     "Honey fresh from the comb contains none of the compound HMF, which accumulates as honey is "
     "stored and accumulates faster the warmer the honey is kept. Regulations set a ceiling on how "
     "much of it honey sold as honey may contain. A packer who has blended honeys of unknown "
     "history and finds the blend close to the ceiling can reasonably conclude that _____",
     ["at least one of the honeys in the blend was kept warm or kept for a long time.",
      "sugar syrup has been added to at least one of the honeys in the blend.",
      "the honey was drawn from comb that had not been sealed.",
      "the ceiling set by the regulations is lower than it needs to be."],
     "A",
     "The passage gives only two things that raise the compound, age and warmth, so a high figure "
     "in a blend points back to a component with one of them. The option about added syrup "
     "introduces an adulteration the text never links to the compound at all."),

 inf("I3",
     "Sugar beet is grown for its root and is lifted at the end of its first season. Like other "
     "biennials it flowers only after a spell of cold, and a plant that meets a cold April may run "
     "to seed in its first summer, putting its sugar into a flowering stem instead of into the "
     "root. Growers therefore hold back sowing until the risk of a cold spell has passed, since "
     "sowing earlier would _____",
     ["expose young plants to the chilling that sets flowering off.",
      "leave too little of the season for the root to reach a useful size.",
      "make the crop more vulnerable to drought later in the summer.",
      "reduce the proportion of sown seed that comes up at all."],
     "A",
     "The passage explains bolting entirely by a cold spell met early in life, so the danger of "
     "sowing early is that the seedlings are up in time to feel it. The option about too little "
     "season describes the cost of sowing late, which is the opposite decision."),

 inf("I4",
     "A stored beeswax candle often develops a pale, powdery film. The film is neither mould nor "
     "dust: it consists of the wax's own longer-chain components, which migrate slowly to the "
     "surface and crystallise there. Warming the candle and rubbing it with a cloth clears the "
     "film, and in time the film returns. A chandler who wants candles to reach a customer without "
     "it must therefore _____",
     ["treat them again shortly before they are sold, since any clearing is temporary.",
      "keep them in a sealed box, since the film is deposited on them out of the air.",
      "wash them, since the film is a residue left behind by handling.",
      "discard any candle that develops the film, since the wax beneath it is spoiled."],
     "A",
     "The film is said to come back after every clearing, so the only remedy consistent with the "
     "passage is to repeat the treatment close to the sale. The option about a sealed box assumes "
     "the film arrives from outside, which the second sentence denies."),

 inf("I5",
     "A beet factory does not wash a whole lorry-load to find its soil tare. A mechanical grab "
     "takes a sample, the sample is washed, and the proportion of soil found in it is applied to "
     "the load. The grab draws from a single point, and soil does not sit evenly in a load: clay "
     "lifted from a wet field works its way to the bottom as the lorry travels. If a grab always "
     "samples from the top of a load, the factory's tare figures will _____",
     ["understate the soil in loads that came from wet fields.",
      "overstate the soil in every load by roughly the same margin.",
      "be accurate as long as the same grab is used all season.",
      "vary at random rather than in any one direction."],
     "A",
     "Clay is said to settle to the bottom, so a sample taken only from the top misses most of it, "
     "and it is the wet-field loads that carry the clay. The option calling the error random "
     "ignores the stated direction of the settling, which biases the sample the same way every "
     "time."),

 inf("I6",
     "Honey holds so little free water that most yeasts cannot grow in it, which is why a sealed "
     "jar keeps for years. To make mead the honey must first be diluted with water, and the more "
     "freely it is diluted the more readily the ferment runs. A maker whose ferment has stopped "
     "early, with a great deal of sugar still unfermented, should first suspect that _____",
     ["the must was never diluted enough for the yeast to keep working in it.",
      "the honey was too old to have contained any fermentable sugar.",
      "the yeast had already used up all the sugar available to it.",
      "the vessel was left unsealed while the ferment was running."],
     "A",
     "The passage names dilution as the one condition that lets yeast work in honey, so a ferment "
     "that stalls with sugar left points back to too little water. The option saying the sugar was "
     "used up contradicts the premise that a great deal of it remains."),

 # ------------------------------------------------------------ Boundaries (12)
 bnd("B1",
     "A swarm hanging in a hedge has no comb, no stores and no roof over it, and it will die within "
     "a few days if it finds nowhere to _____ scouts that leave it are looking for a dry cavity of "
     "about forty litres, high enough off the ground to be safe from damp.",
     ["live. The", "live, the", "live the", "live: and the"], "A",
     "A complete statement stands on each side of the blank with no conjunction between them, so a "
     "full stop is needed. Setting a comma between them splices two sentences together, and a colon "
     "is never followed by a coordinating conjunction."),

 bnd("B2",
     "A queen excluder is a grid whose gaps a worker can pass through and a queen _____ the brood "
     "stays below the grid and the honey is stored above it.",
     ["cannot, so", "cannot so", "cannot; so", "cannot: so"], "A",
     "Two complete statements are joined by a coordinating conjunction, which takes a comma in "
     "front of it. Neither a semicolon nor a colon is used before a coordinating conjunction, and "
     "leaving out the comma runs the two statements together."),

 bnd("B3",
     "A boiled sweet asks three things of the syrup it is made _____ enough acid to invert part of "
     "the sugar, a cooling fast enough to stop crystals forming, and a final moisture low enough to "
     "keep the sweet hard.",
     ["from:", "from,", "from;", "from"], "A",
     "A complete statement stands in front of the blank and a list explaining it follows, which is "
     "the colon's job. A semicolon would require a complete statement after it, and the list that "
     "follows is not one."),

 bnd("B4",
     "Lorenzo _____ a Presbyterian minister in Philadelphia, published his book on the movable "
     "frame in 1853 and spent the rest of his life defending the patent.",
     ["Langstroth,", "Langstroth", "Langstroth:", "Langstroth;"], "A",
     "The description of Langstroth's calling interrupts the sentence between its subject and its "
     "verb and is not needed to identify him, so it is set off with a pair of commas and the first "
     "of them belongs at the blank. A semicolon or colon would break the sentence before its verb "
     "arrives."),

 bnd("B5",
     "A vacuum pan boils syrup a long way below the temperature an open pan _____ the sugar leaves "
     "it far lighter in colour than it otherwise would be.",
     ["needs; consequently,", "needs, consequently,", "needs consequently,",
      "needs: consequently,"], "A",
     "Two complete statements meet at the blank and the second opens with a linking adverb rather "
     "than a conjunction, so a semicolon is required before it. Using a comma there leaves the two "
     "statements spliced, since a linking adverb cannot join them."),

 bnd("B6",
     "The diffusion _____ which replaced the older presses in the 1870s, draws the sugar out of "
     "sliced beet without crushing it and leaves a pulp that can be dried and sold for fodder.",
     ["battery,", "battery", "battery;", "battery:"], "A",
     "The clause beginning with 'which' adds information that is not needed to identify the "
     "battery, so it is enclosed in commas and the opening one falls at the blank. Both the "
     "semicolon and the colon would demand a complete statement on the far side, and a relative "
     "clause is not one."),

 bnd("B7",
     "Because wax scales form only while a bee is young and generously _____ a colony that has lost "
     "its youngest workers cannot draw new comb however much nectar it carries in.",
     ["fed,", "fed", "fed;", "fed:"], "A",
     "An introductory subordinate clause runs up to the blank and the main statement follows it, "
     "which calls for a comma. A semicolon or colon between them would treat the opening clause as "
     "though it could stand alone."),

 bnd("B8",
     "Three of the four sugars in honey are simple ones &mdash; glucose, fructose and a trace of "
     "_____ and the fourth, sucrose, survives only in the smallest amounts.",
     ["maltose &mdash;", "maltose,", "maltose;", "maltose"], "A",
     "A dash already opens the inserted list of sugars, so a matching dash has to close it before "
     "the sentence resumes. Ending the insertion with a comma or a semicolon leaves the opening "
     "dash unpaired."),

 bnd("B9",
     "The rule that the chandlers of the old companies gave their apprentices was _____ never let "
     "the wick stand straight, and never let the wax boil.",
     ["simple:", "simple,", "simple;", "simple"], "A",
     "A complete statement precedes the blank and what follows spells out the rule it announces, "
     "which is what a colon introduces. A semicolon would need a complete statement after it, and "
     "two imperatives offered as the content of a rule are not one."),

 bnd("B10",
     "Bees do not gather honeydew from _____ they gather it from the sticky drops aphids leave on "
     "leaves, and the honey it makes is dark, slow to granulate and low in glucose.",
     ["flowers;", "flowers,", "flowers", "flowers:"], "A",
     "Two complete statements meet at the blank with no conjunction between them, so a semicolon is "
     "the mark that fits. A comma alone splices them, and a colon would announce the second "
     "statement as an explanation of a term rather than as a correction."),

 bnd("B11",
     "The only colonies _____ clear a patch of killed brood within two days are the ones a breeder "
     "will take queens from.",
     ["that", "that,", ", that", ", that,"], "A",
     "The clause identifies which colonies are meant and cannot be removed without changing the "
     "sentence, so it takes no commas at all. Any of the punctuated versions would mark it as an "
     "aside, which contradicts the word 'only' in front of it."),

 bnd("B12",
     "A refiner spins the massecuite in a basket of fine _____ and washes the crystals with a "
     "little clean syrup while the basket is still turning.",
     ["mesh", "mesh,", "mesh;", "mesh:"], "A",
     "One subject governs both 'spins' and 'washes', so the conjunction joins two verbs rather than "
     "two statements and no punctuation belongs in front of it. A comma, semicolon or colon would "
     "all signal a second statement that never arrives, since no new subject follows."),

 # -------------------------------------------- Form, Structure, and Sense (9)
 fss("F1",
     "The number of frames of comb a colony draws in a season _____ on the weather far more than on "
     "the size of the hive it is given.",
     ["depends", "depend", "have depended", "are depending"], "A",
     "The subject is the single number, not the frames or the colonies named in the phrases after "
     "it, so a singular present-tense verb is required. The plural forms would agree with the "
     "frames, which are not what the sentence is about."),

 fss("F2",
     "Marggraf showed in 1747 that the sugar in beet was the same substance as the sugar in cane, "
     "but nobody _____ a way of extracting it cheaply until his pupil Achard opened a factory fifty "
     "years afterwards.",
     ["had found", "finds", "will find", "is finding"], "A",
     "The clause describes a state of affairs that lasted up to a later past event, so the past "
     "perfect is what fits alongside the two past-tense verbs around it. The present and future "
     "forms clash with a sentence anchored in 1747."),

 fss("F3",
     "A colony sometimes supersedes its queen so quietly that mother and daughter lay side by side "
     "for weeks, and neither the workers nor the old queen _____ any sign of the change.",
     ["shows", "show", "have shown", "are showing"], "A",
     "With 'neither ... nor' the verb agrees with the nearer subject, which is the singular old "
     "queen, so the singular form is right. The plural forms would agree with the workers, which "
     "sit on the far side of the correlative."),

 fss("F4",
     "The two _____ readings differed by a full degree, and the boiler trusted the one that had "
     "been checked against boiling water that morning.",
     ["thermometers'", "thermometer's", "thermometers", "thermometers's"], "A",
     "Two thermometers own the readings, so the plural possessive with the apostrophe after the "
     "final s is required. The singular possessive would leave only one instrument, which cannot "
     "produce two readings that differ."),

 fss("F5",
     "Opened in cold weather, _____",
     ["a hive loses more heat than the colony inside it can replace.",
      "the colony loses more heat than it can replace inside a hive.",
      "beekeepers should not disturb a colony until spring.",
      "it is a mistake to lift the roof off a colony at all."], "A",
     "The opening phrase describes the thing that is opened, so the subject that follows the comma "
     "has to be the hive. Beginning the main clause with the beekeepers makes the beekeepers the "
     "thing opened in cold weather."),

 fss("F6",
     "A confectioner's day was spent boiling syrup, pulling it over a hook until it turned to "
     "satin, and _____ it into ropes for the cutting machine.",
     ["drawing", "drew", "to draw", "draws"], "A",
     "The three activities are joined in one series governed by 'spent', and the first two are "
     "'-ing' forms, so the third must match. The infinitive and the finite verbs both break the "
     "pattern the sentence has already set."),

 fss("F7",
     "A row of wax moulds, each of them fitted with its own wick and clamped to the bench, _____ "
     "under the window where the light is best.",
     ["stands", "stand", "have stood", "were standing"], "A",
     "The subject is the row, a singular noun, and the moulds appear only inside a phrase "
     "describing it, so the verb is singular and present. The plural forms would agree with the "
     "moulds rather than with the row."),

 fss("F8",
     "A colony that has lost _____ queen begins raising a new one within a day, provided there are "
     "larvae young enough to be fed on royal jelly.",
     ["its", "it's", "its'", "their"], "A",
     "The possessive form of 'it' takes no apostrophe, and the singular colony calls for a singular "
     "possessive. The contracted form would produce 'it is queen', and the plural possessive would "
     "have no plural noun to refer back to."),

 fss("F9",
     "By the time the blockade was lifted in 1814, France _____ more than three hundred beet "
     "factories, most of which closed within five years of the peace.",
     ["had built", "has built", "builds", "will build"], "A",
     "The building was finished before the past moment the sentence names, which is what the past "
     "perfect marks. The present perfect and the present would tie the construction to the "
     "writer's own time rather than to 1814."),

 # ---------------------------------------------------------- Transitions (9)
 trn("N1",
     "A queen excluder keeps the queen below it, so no brood is ever raised in the boxes above. "
     "_____ the combs in those boxes stay pale year after year and can be cut and sold as comb "
     "honey.",
     ["Consequently,", "Nevertheless,", "For instance,", "Meanwhile,"], "A",
     "Comb that never holds brood is precisely why the comb stays pale, so the second sentence "
     "states the result of the first. Marking it as a contrast would deny the link the first "
     "sentence has just set up."),

 trn("N2",
     "Cane sugar and beet sugar are the same molecule and no palate can tell them apart. _____ a "
     "mass spectrometer separates them without difficulty, because the two plants fix carbon by "
     "different routes and leave different proportions of its isotopes behind.",
     ["However,", "Likewise,", "Therefore,", "In addition,"], "A",
     "The first sentence says the two sugars cannot be told apart and the second says an instrument "
     "tells them apart easily, which is a reversal. A word of addition would present the "
     "spectrometer as a second example of indistinguishability, which is the opposite of what it "
     "does."),

 trn("N3",
     "Several additions to a boiling syrup will keep it from graining. _____ a spoonful of glucose "
     "syrup supplies sugar chains too long to fit into a sucrose lattice.",
     ["For example,", "Instead,", "Nonetheless,", "By comparison,"], "A",
     "The first sentence announces a category of additions and the second names one of them and "
     "says how it works, which is illustration. A word of contrast would set the glucose syrup "
     "against the category it belongs to."),

 trn("N4",
     "Honey in a sealed jar never spoils. _____ a jar left open takes up water from the air until "
     "the surface is dilute enough for yeasts to work in.",
     ["Even so,", "Accordingly,", "Similarly,", "In short,"], "A",
     "Keeping indefinitely and spoiling once opened stand against each other, so the second "
     "sentence qualifies the first. A word of result would make spoilage follow from the honey's "
     "keeping quality, which reverses the relationship."),

 trn("N5",
     "Beet arriving at a factory is washed, weighed and sliced into cossettes. _____ the cossettes "
     "pass into the diffusion battery, where hot water draws the sugar out of them.",
     ["Next,", "Instead,", "By contrast,", "Nevertheless,"], "A",
     "The two sentences describe consecutive stages of one process, so what is needed is a marker "
     "of sequence. A word of contrast would imply the diffusion battery replaces the washing and "
     "slicing rather than following it."),

 trn("N6",
     "A wick that stands upright in a flame chars into a stub and blocks the wax climbing behind "
     "it. _____ a candle with an unplaited wick has to be trimmed every few minutes if it is not to "
     "smoke.",
     ["As a result,", "On the other hand,", "For example,", "Admittedly,"], "A",
     "Charring and blockage are the cause and constant trimming is the consequence, so a result "
     "marker is what belongs. A concessive word would treat the trimming as an objection to the "
     "first sentence rather than as its outcome."),

 trn("N7",
     "Beet is lifted late in the year, when its roots hold the most sugar they will ever hold. "
     "_____ late lifting brings the crop in when the fields are wettest and the soil tare is at its "
     "highest.",
     ["At the same time,", "Consequently,", "For instance,", "In other words,"], "A",
     "The second sentence sets a drawback of late lifting beside the advantage given in the first, "
     "so what is wanted is a marker that holds two things together. A result marker would make the "
     "high soil tare follow from the sugar in the roots, which it does not."),

 trn("N8",
     "The pollen in a jar of honey comes from the flowers the colony actually worked, not from "
     "whatever the beekeeper planted nearby. _____ the jar records the bees' choices rather than "
     "the choices offered to them.",
     ["In other words,", "Nevertheless,", "For example,", "Earlier,"], "A",
     "The second sentence restates the first in more general terms without adding any new fact, "
     "which is what a restatement marker signals. A contrast marker would suggest the second "
     "sentence pulls against the first, and it agrees with it."),

 trn("N9",
     "A hydrometer floating in a syrup reports density, and a scale printed on its stem turns that "
     "reading into a percentage of sugar. _____ the conversion holds only when sugar is the sole "
     "substance dissolved, which in a beet juice it never is.",
     ["However,", "Similarly,", "Consequently,", "Finally,"], "A",
     "The second sentence limits the convenience the first describes, so a contrast marker is "
     "required. A result marker would present the limitation as something the printed scale brings "
     "about, when it is a condition the scale quietly assumes."),

 # ------------------------------------------------- Rhetorical Synthesis (9)
 syn("R1",
     ["Before 1851 comb was fastened to the walls of a hive and had to be cut out.",
      "Lorenzo Langstroth measured the gap bees leave clear as they build: about 8 millimetres.",
      "A gap wider than that is filled with comb; a narrower one is sealed shut.",
      "Langstroth hung his frames so that a gap of that width surrounded each of them.",
      "The comb then attached only to the frame, and a hive could be opened without damage."],
     "explain how Langstroth's measurement made a hive openable.",
     ["Because bees leave a gap of about 8 millimetres clear, Langstroth hung his frames with a gap of that width all round them, so comb attached only to the frame and a hive could be opened without damage.",
      "Langstroth measured the gap that bees leave clear as they build and found it to be about 8 millimetres.",
      "A gap wider than 8 millimetres is filled with comb, while a gap narrower than that is sealed shut.",
      "Before 1851, comb was fastened to the walls of a hive and had to be cut out whenever a beekeeper wanted it."],
     "A",
     "The goal asks for the route from a measurement to an openable hive, and only the choice that "
     "carries the gap through to the frames and then to the undamaged opening covers it. The choice "
     "reporting the measurement on its own stops before the frames and so never reaches the hive."),

 syn("R2",
     ["A lorry of beet is weighed as it arrives at the factory.",
      "A sample is drawn from the load, washed and reweighed.",
      "The difference is the soil tare and is deducted from the grower's payment.",
      "In a wet lifting season soil can be a fifth of a load's weight.",
      "A factory that paid for the soil would also pay to haul it and to wash it."],
     "explain to an audience unfamiliar with the trade why the deduction is made.",
     ["Because soil can be a fifth of a load's weight in a wet season, and a factory would otherwise pay to buy it, haul it and wash it, each load is sampled and the soil found is deducted from the payment.",
      "A lorry of beet is weighed on arrival, and a sample is then drawn from the load, washed and reweighed.",
      "The difference between the weight of the sample and the weight of the washed sample is called the soil tare.",
      "In a wet lifting season, the soil that comes in with a load of beet can be a fifth of its weight."],
     "A",
     "The goal is to justify the deduction, so the answer has to give both the size of the problem "
     "and the costs a factory would carry, and one choice does. The choice describing the weighing "
     "and washing sets out the procedure without ever saying why anyone bothers."),

 syn("R3",
     ["Honey holds more sugar than water at room temperature can keep dissolved.",
      "Glucose comes out of the solution as crystals sooner or later.",
      "A few large crystals feel gritty; many small crystals feel smooth.",
      "Packers stir a little finely crystallised honey into the batch as a seed.",
      "A seeded batch sets smooth within about a fortnight."],
     "explain how packers control the texture of set honey.",
     ["Since glucose will crystallise out of honey whatever a packer does, packers stir in finely crystallised honey as a seed so that many small crystals form instead of a few large ones and the batch sets smooth.",
      "Honey holds more sugar than water at room temperature can keep dissolved, so glucose comes out of it as crystals.",
      "A honey with a few large crystals in it feels gritty, while a honey with many small crystals feels smooth.",
      "Packers stir a little finely crystallised honey into a batch, and the batch sets within about a fortnight."],
     "A",
     "Control is the point of the goal, so the answer must join the inevitability of crystallising "
     "to the seeding that decides the crystal size, and only one choice does both. The choice about "
     "gritty and smooth honey gives the standard being aimed at but not the means of hitting it."),

 syn("R4",
     ["Spinning a massecuite throws out crystals and leaves a darker syrup behind.",
      "That syrup still contains sugar.",
      "It is boiled and spun again, and the process can be repeated.",
      "Each round recovers less sugar than the one before it at much the same cost.",
      "The last syrup is sold as molasses."],
     "explain why refiners stop recovering sugar before the syrup is free of it.",
     ["Each boiling and spinning recovers less sugar than the last at much the same cost, so refiners stop once the sugar still in the syrup is worth less than recovering it, and sell what is left as molasses.",
      "Spinning a massecuite throws out crystals and leaves behind a darker syrup that still contains sugar.",
      "A syrup left after spinning can be boiled and spun again, and the process can be repeated several times.",
      "The syrup that remains at the end of the process is sold as molasses rather than discarded."],
     "A",
     "The goal asks why the recovery stops, which requires the falling yield at a steady cost, and "
     "only one choice states that trade-off. The choice noting that the syrup still contains sugar "
     "sets up the puzzle without answering it."),

 syn("R5",
     ["A wick that stands upright in a flame chars into a stub that smokes.",
      "Snuffers were used to cut the stub off every few minutes.",
      "A plaited wick curls out towards the tip of the flame.",
      "The tip of a flame is its hottest part and the part best supplied with air.",
      "A wick that curls out to the tip burns away completely."],
     "explain to an audience unfamiliar with candles how the plaited wick did away with snuffing.",
     ["A plaited wick curls out to the tip of the flame, the hottest and best-aired part, where it burns away completely instead of charring into the smoking stub that snuffers had to cut off.",
      "Snuffers were used every few minutes to cut off the charred stub that formed on an upright wick.",
      "The tip of a candle flame is its hottest part and the part best supplied with air.",
      "A wick that is plaited rather than laid straight curls outward as the candle burns."],
     "A",
     "The goal names both the mechanism and the outcome, so the answer must carry the curl to the "
     "hot tip and then to the disappearance of the stub. The choice describing the snuffers gives "
     "only the practice that was abandoned."),

 syn("R6",
     ["Brood diseases spread from larvae that die sealed inside their cells.",
      "Some colonies uncap such cells and remove the contents within two days.",
      "The removal behaviour is heritable.",
      "Breeders test for it by killing a patch of brood with liquid nitrogen.",
      "The proportion of the patch cleared in 48 hours is the colony's score."],
     "explain how a breeder measures the behaviour.",
     ["A breeder kills a patch of brood with liquid nitrogen and records what proportion of it the colony uncaps and clears within 48 hours, which scores the heritable removal behaviour.",
      "Brood diseases spread through a colony from larvae that have died sealed inside their cells.",
      "Some colonies contain bees that uncap a cell holding a dead larva and remove the contents within two days.",
      "The behaviour by which a colony removes dead brood from sealed cells is passed from one generation to the next."],
     "A",
     "Measurement is what the goal asks for, so the answer has to name the frozen patch and the "
     "proportion cleared in a fixed time. The choice stating that the behaviour is heritable gives "
     "the reason for measuring it and not the method."),

 syn("R7",
     ["Beet molasses holds sugar that will not crystallise.",
      "Raffinose is a three-part sugar present in beet.",
      "Its shape is close to that of sucrose.",
      "It can take a place at the growing face of a sucrose crystal.",
      "The next layer of sucrose cannot then sit cleanly on top of it."],
     "explain why a small proportion of raffinose has a large effect.",
     ["Raffinose is close enough to sucrose in shape to take a place at the growing face of a crystal but different enough that the next layer cannot sit cleanly on it, so even a little of it disrupts crystallisation.",
      "Raffinose is a three-part sugar found in beet, and beet molasses holds sugar that will not crystallise.",
      "The shape of a raffinose molecule is close to the shape of a sucrose molecule.",
      "A raffinose molecule can occupy a place at the growing face of a sucrose crystal."],
     "A",
     "The effect the goal asks about comes from the two-sided resemblance, so the answer must give "
     "both the fit and the failure of the next layer. The choice noting only that the shapes are "
     "close leaves out the mismatch that does the damage."),

 syn("R8",
     ["Drones from many colonies gather at the same few places each afternoon.",
      "The same places are used year after year.",
      "No drone lives long enough to have visited one in a previous year.",
      "Queens fly to these places on their mating flights.",
      "A queen there meets drones from colonies other than her own."],
     "emphasise what remains unexplained about the gathering places.",
     ["The same gathering places are used year after year even though no drone lives long enough to have visited one before, so how each generation finds them is unaccounted for.",
      "Drones from many colonies gather at the same few places each afternoon, and queens fly to those places on their mating flights.",
      "A queen that flies to a gathering place meets drones from colonies other than her own.",
      "Queens make their mating flights to places where drones from many colonies have gathered."],
     "A",
     "The goal singles out the unexplained part, which is the persistence of the sites across "
     "generations that cannot have learned them, and only one choice puts those two notes together. "
     "The choice about a queen meeting drones from other colonies reports the arrangement's purpose "
     "rather than its mystery."),

 syn("R9",
     ["Honey fresh from the comb contains no HMF.",
      "HMF accumulates as honey is stored, and faster the warmer it is kept.",
      "Regulations set a ceiling on the HMF in honey sold as honey.",
      "The ceiling applies to the blend that is sold, not to its components.",
      "Blending mixes honeys of different ages and histories."],
     "explain to a packer why blending calls for care.",
     ["Because HMF rises with age and warmth and the legal ceiling applies to the blend rather than to its components, a single old or warm-stored honey can carry a whole batch past the limit.",
      "Honey that has just been taken from the comb contains no HMF at all.",
      "HMF accumulates in honey as it is stored, and it accumulates faster the warmer the honey is kept.",
      "Regulations set a ceiling on how much HMF honey sold as honey may contain."],
     "A",
     "The warning the goal asks for depends on the ceiling applying to the finished blend, so the "
     "answer must combine that with the way the compound accumulates. The choice stating how the "
     "compound accumulates omits the rule that turns one bad component into a spoiled batch."),
]
