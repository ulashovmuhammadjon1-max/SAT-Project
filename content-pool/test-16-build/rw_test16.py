#!/usr/bin/env python3
"""
Reading & Writing authored for Test 16.

All 81 items are original. The transcribed pool was spent long ago, and for R&W
authoring is in any case the safer route: a transcribed answer key has to be
re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers in
81 that way). Every item below carries a `why` recording the reasoning that
produced the key AND the reason the strongest distractor fails - that record IS
the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution.

Writing-domain choices are worded, never bare punctuation. Test 8 shipped
Boundaries items whose four options were ", " / "; " / ": " / " and ", which a
student sees as four empty rows; the real test repeats the words on either side
of the blank inside every option so that each choice reads as the resulting
sentence. Every Boundaries item here is written that way from the start.
Form/Structure items whose options are genuinely words ("was" / "were",
"has" / "have") are left as words, which is also how the real test presents
them.

Command of Evidence mixes three quotation items, three finding-if-true items
and three data items. The data items carry a real <table> in the passage using
the house style block; none of them describes a graph in prose, because no
image can be produced from here.

Topics were screened against content-pool/rw_authored_corpus.json - all 809
passages banked or authored across Tests 1-15 - by keyword and by 5-gram /
Jaccard overlap (see screen_topics.py in this directory), before anything was
drafted. Test 16 was assigned these territories: printing, papermaking and
bookbinding; navigation and cartography at sea; textile and dye technology;
beekeeping and pollination; glass and ceramics chemistry; harbour and canal
engineering; Andean and Amazonian archaeology; birdsong and animal acoustics;
the history of colour pigments; timekeeping at sea; museum conservation
science; Pacific island seafaring; fungi and lichens; polar exploration
logistics; the economics of ports.

Candidates dropped at the planning stage because the corpus already covers
them, rather than written and later discovered:

    Egyptian blue, Prussian blue, ultramarine and lapis, Tyrian purple and
    murex, cochineal, indigo and woad, flax retting, quipus and Inca record
    keeping, terra preta, the Acre geoglyphs, Marshall Islands stick charts and
    swell refraction, portolan charts, the marine chronometer and the Board of
    Longitude, lunar distances, the Mercator projection, plotting soundings by
    hand, watermarks as dating evidence, containerisation, draught as a limit
    on which ports a ship can use, dredging and littoral drift, the waggle
    dance, buzz pollination, the Vasa and polyethylene glycol, XRF and Raman
    pigment identification, retouching detected by an anachronistic pigment,
    lichens as a fungus-alga partnership, glaze crazing and blistering, celadon
    reduction glazes, and the drawloom with Jacquard's cards.

What is left, and what this file is built from:

    type metal and antimony, gelatine sizing, iron gall ink, the Fourdrinier
    machine, the printer's run, gold tooling, hydraulic lime at the Eddystone,
    saggars, bone china, tin glazes, slip casting, the annealing lehr, alum
    mordants, mercerised cotton, fulling, tapestry cartoons, orchil, fastness
    testing, propolis, mason bees, skeps, varroa, ultraviolet nectar guides,
    the chip log, chart datum, training walls at a river mouth, the inclined
    plane, the Pontcysyllte aqueduct, the half-tide dock, the transit shed,
    lighterage, the entrepot trade, quay turnaround, waru waru raised fields,
    chuno, Moche portrait vessels, Caral, Machu Picchu's drainage, the vertical
    archipelago, Chachapoya cliff tombs, bitter manioc, the syrinx, lyrebird
    mimicry, song learning in zebra finches, white-crowned sparrow dialects,
    the Lombard effect, lead white, smalt, lightfastness trials, anoxic pest
    treatment, deacidification, bronze disease, reversible adhesives, the star
    compass and etak, the crab-claw sail, Hokule'a, lichenometry, fairy rings,
    brown rot and white rot, depot laying, sastrugi, snow blindness and the
    Fram's rounded hull.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T16"
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
     "Lead on its own casts a letter with soft corners, and the shoulders of the type crumble after "
     "a few thousand impressions. Tin and antimony added to the melt give an alloy that expands very "
     "slightly as it sets, so the metal is pressed into every angle of the mould instead of shrinking "
     "away from it. A founder chooses the mixture for the _____ of the face it produces rather than "
     "for the strength of the bar it casts.",
     ["sharpness", "colour", "weight", "cheapness"], "A",
     "Metal that expands into every angle of the mould reproduces the letter's corners exactly, "
     "which is what the passage sets against the crumbling produced by lead alone. The 'weight' "
     "option names a property of the bar of metal, and the sentence expressly sets the printed face "
     "against the bar."),

 wic("W2",
     "A sheet lifted from the vat is a mat of felted fibre that drinks up whatever is written on it, "
     "so a line of ink spreads outward until the letter is a blot. Papermakers therefore dip the "
     "dried sheet in a bath of gelatine, which fills the spaces between the fibres and leaves a "
     "surface the ink can sit on. Sizing does not alter the fibre; it alters how _____ the sheet is.",
     ["opaque", "absorbent", "durable", "expensive"], "B",
     "The bath fills the spaces that were drinking up the ink, so what the treatment changes is how "
     "much liquid the sheet takes in. The 'durable' option names a strength the passage never claims "
     "for the size, which is described only as filling the spaces between fibres."),

 wic("W3",
     "Iron gall ink is made by steeping crushed oak galls in water and adding green vitriol, and the "
     "black it produces bites into the fibre of the page rather than resting on top of it. A scribe's "
     "error could not be brushed away; it had to be scraped off with a knife, taking a layer of the "
     "parchment with it. What made the ink so useful to a chancery is exactly what made it _____.",
     ["irreversible", "illegible", "inexpensive", "fashionable"], "A",
     "An ink that sinks into the fibre and can be removed only by cutting the surface away cannot be "
     "undone, and the sentence asks for the other face of the quality a chancery valued. The "
     "'inexpensive' option raises cost, which the passage never mentions at all."),

 wic("W4",
     "Ordinary lime mortar sets by drying and will not harden at all under water, which is why the "
     "first towers on the Eddystone reef were built of timber and were washed away. Burning "
     "limestones from one quarry after another, John Smeaton found that those containing clay set "
     "hard while submerged. The mortar he settled on was _____ in the one condition that had defeated "
     "everything used before it.",
     ["visible", "decorative", "dependable", "inexpensive"], "C",
     "A lime that hardens while under water performs in precisely the condition that ruined the "
     "earlier work, so the blank names reliability there. The 'inexpensive' option introduces cost, "
     "which nothing in the passage weighs."),

 wic("W5",
     "Wood and coal fires throw ash and flame across the ware, and a pot standing open in the kiln "
     "comes out flecked wherever a cinder has struck the glaze. Potters therefore stack their pieces "
     "inside lidded boxes of coarse fireclay, which take up the heat but keep everything else out. "
     "The box is no part of the pot; it is a _____ for the hours the firing lasts.",
     ["mould", "shield", "measure", "decoration"], "B",
     "The box lets heat through while stopping ash and flame from reaching the glaze, which is "
     "protection rather than shaping, and the sentence separates it from the pot itself. The 'mould' "
     "option would have the box give the pot its form, but the ware is already made when it goes in."),

 wic("W6",
     "Add the ash of calcined bone to a porcelain body and the fired result passes light where a "
     "stoneware cup would not, yet it chips less readily than the hard-paste porcelains made on the "
     "continent. English factories took up the recipe because a crate of it survived carriage and "
     "still looked like porcelain on the table. The material's appeal lay in being at once "
     "translucent and _____.",
     ["porous", "tough", "heavy", "coarse"], "B",
     "Chipping less readily and coming through a journey in a crate both describe resistance to "
     "damage, which the sentence pairs with translucency. The 'porous' option contradicts the "
     "description of a fired porcelain body that light passes through."),

 wic("W7",
     "Most plant dyes will colour a fibre and then leave it again in the first wash. A mordant such "
     "as alum is taken up by the fibre beforehand and forms a link that the dye molecule afterwards "
     "attaches to, so the colour is held by the fibre instead of merely lying on it. The mordant "
     "contributes almost no colour of its own; its work is entirely _____.",
     ["decorative", "accidental", "preparatory", "temporary"], "C",
     "The alum goes on before the dye and builds the link the colour later attaches to, which makes "
     "its role a matter of getting the fibre ready. The 'temporary' option reverses the point, since "
     "the mordant is what makes the colour last."),

 wic("W8",
     "Cotton yarn held under tension in a bath of caustic soda swells, and the flat twisted ribbon of "
     "each fibre rounds out. The yarn is stronger afterwards, takes up dye more readily, and reflects "
     "light along its length instead of scattering it in all directions. John Mercer's treatment "
     "leaves the cotton chemically what it was and _____ what it looks like.",
     ["preserves", "transforms", "conceals", "predicts"], "B",
     "A fibre that rounds out and throws light along its length no longer looks like the flat ribbon "
     "it was, and the sentence sets that change against the chemical sameness. The 'preserves' option "
     "would make both halves of the contrast say the same thing."),

 wic("W9",
     "Bees gather resin from buds and bark and work it with wax into a material they smear over every "
     "crack and rough surface inside the hive. It closes draughts, stiffens the comb where it meets "
     "the wall, and holds down moulds and bacteria on the surfaces the colony walks over. Propolis is "
     "best described not as a food and not as a building block but as a _____.",
     ["fuel", "sealant", "signal", "reserve"], "B",
     "The material is pressed into cracks, stiffens joints and coats the surfaces the bees use, which "
     "is the work of something that closes and covers, and the sentence rules out food and structure. "
     "The 'reserve' option would make it a store held against future need, which nothing in the "
     "passage suggests."),

 wic("W10",
     "Coils of lead were laid in earthenware pots over vinegar, the pots were buried in spent tanning "
     "bark, and the stack was left for three months while the heat of the rotting bark drove the "
     "reaction. What came out was a dense white carbonate that covered better than any other pigment "
     "then available. Painters accepted a material slow to make and dangerous to grind because "
     "nothing else was so _____.",
     ["transparent", "opaque", "portable", "colourful"], "B",
     "The pigment is praised for covering better than anything else, and covering is what a paint "
     "does when light will not pass through it. The 'transparent' option names the opposite property."),

 wic("W11",
     "A navigator trained in the Caroline Islands holds a course by the point on the horizon at which "
     "a known star rises or sets, changing star as each one climbs too high to be of use. The canoe "
     "is treated as still, with the sea and the islands moving past it, and progress is tracked by "
     "counting off the changing bearing of an island that lies out of sight to one side. The whole "
     "reckoning is kept _____.",
     ["on paper", "in the head", "by instrument", "in company"], "B",
     "Stars are read off the horizon and the passing island is counted off from memory, with nothing "
     "written down and no device named anywhere in the passage. The 'by instrument' option supplies "
     "equipment the text never mentions."),

 wic("W12",
     "A lichen colonising bare rock spreads outward at a rate that varies little from year to year on "
     "a given site, so the largest disc on a boulder gives a minimum age for the surface beneath it. "
     "Where a glacier has left a moraine that no document records and no wood survives to be dated, "
     "measuring the discs supplies a figure that would otherwise be _____.",
     ["unobtainable", "disputed", "costly", "arbitrary"], "A",
     "The moraine is described as recorded by no document and holding no datable wood, so without the "
     "lichens there would be no figure at all. The 'disputed' option implies a rival date already "
     "exists to argue over, which the passage rules out."),

 meaning("W13",
     "A thrower judges a clay by how far it will stand up before it slumps. Ball clay is plastic and "
     "takes a shape easily but shrinks and warps in the kiln; coarse sand worked into it stiffens the "
     "mixture at the cost of some of that ease. The <u>body</u> a workshop settles on is always a "
     "compromise between what the wheel wants and what the fire will allow.",
     "body",
     ["The main part of a written work.",
      "A group of people acting together as a unit.",
      "A prepared mixture of clay from which ware is made.",
      "The physical structure of a person or an animal."],
     "C",
     "The word is applied to something a workshop settles on, mixed from ball clay and sand and "
     "judged by how it behaves on the wheel and in the kiln, so it names the material itself. The "
     "sense of a group acting together is a common meaning of the word, but nothing here concerns "
     "people."),

 meaning("W14",
     "A dyer testing a new red pins one strip of the cloth in a south-facing window, leaves an "
     "identical strip in a drawer, and compares the two after a month. A third strip goes through six "
     "washes at forty degrees. A colour that comes through both trials without shifting is <u>fast</u>, "
     "and a dyehouse will not sell cloth whose colour is not.",
     "fast",
     ["Moving at high speed.",
      "Firmly fixed and not liable to change.",
      "Going without food for a period.",
      "Slightly ahead of the correct time."],
     "B",
     "The word is applied to a colour that survives sunlight and repeated washing without shifting, "
     "which is a matter of staying put rather than of speed. The high-speed sense is the commonest "
     "meaning of the word, but nothing in the passage concerns motion."),

 meaning("W15",
     "The compositor's work is over once the forme is locked up, and from that point the cost of a "
     "book falls almost entirely on paper and press time. Setting the type a second time would cost "
     "what the first setting cost; pulling more sheets while the type is still standing costs little "
     "beyond the paper. A publisher therefore fixes the size of the <u>run</u> before the first sheet "
     "is pulled.",
     "run",
     ["A continuous period of a particular condition.",
      "The number of copies printed at one time.",
      "A journey made regularly by a vehicle.",
      "An enclosure in which animals are kept."],
     "B",
     "The word names something whose size a publisher fixes and which is weighed against paper and "
     "press time for a batch of sheets, so it refers to the quantity printed at one go. The sense of "
     "a continuous spell of something is a genuine meaning of the word, but nothing here concerns a "
     "stretch of time."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("T1",
     "A vatman making paper by hand dips a mould, shakes it until the fibres lock, and couches off a "
     "single sheet; a good pair might manage a thousand a day between them. <u>The machine patented "
     "for the Fourdrinier brothers ran the pulp onto an endless belt of woven wire, so that a sheet "
     "was never formed at all but cut out of a continuous web.</u> Deckle edges disappeared, sheet "
     "sizes became arbitrary, and the length of a sheet ceased to be set by the reach of a man's arms.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It identifies the change in method whose consequences the rest of the text sets out.",
      "It explains why printers continued to prefer handmade paper.",
      "It reports the daily output a pair of hand papermakers could manage.",
      "It questions whether the brothers deserve the credit for the design."],
     "A",
     "The sentence states that the sheet stopped being formed one at a time and became a length cut "
     "from a continuous web, and the closing sentence lists what followed from that. The daily output "
     "of the hand workers is given in the opening sentence, not in the underlined one."),

 tsp("T2",
     "A chip log is a weighted board on a line knotted at even intervals. Thrown over the stern, the "
     "board stays roughly where it entered the water while the ship draws line off a reel, and a hand "
     "counts the knots that pass through his fingers while a small sand glass empties. Speed is read "
     "off directly in knots, because the spacing of the knots and the running time of the glass are "
     "chosen to make the count come out in sea miles an hour. Nothing has to be worked out on deck.",
     "Which choice best states the main purpose of the text?",
     ["To explain how a simple device turns a physical measurement into a figure that can be used at once.",
      "To argue that the chip log was more accurate than the instruments that replaced it.",
      "To describe the manufacture of the sand glasses carried at sea.",
      "To trace the adoption of the sea mile as a unit of distance."],
     "A",
     "The text describes the board, the knotted line and the glass, then explains that the spacing "
     "and the timing are set so that the count is already the answer. Accuracy against later "
     "instruments is never discussed, so no such comparison is being urged."),

 tsp("T3",
     "Beetle larvae in a wooden frame can be killed with a fumigant, but residues stay in the object "
     "and reach the conservator who handles it afterwards. <u>Sealing the frame in a barrier bag and "
     "flushing it with nitrogen until the oxygen falls below half a per cent kills the larvae and "
     "leaves nothing behind.</u> The treatment takes three weeks rather than an afternoon, and the "
     "frame comes out of the bag chemically as it went in.",
     "Which choice best describes the function of the underlined sentence in the text?",
     ["It presents the alternative whose advantage the rest of the text explains.",
      "It concedes that the treatment frequently fails to kill the larvae.",
      "It explains why beetle larvae attack wooden frames in the first place.",
      "It describes the residues that a fumigant leaves in an object."],
     "A",
     "The sentence introduces the nitrogen method, and the closing sentence weighs its slowness "
     "against the fact that nothing remains in the object. The residues are described in the opening "
     "sentence, which states the problem the underlined sentence answers."),

 tsp("T4",
     "Moche potters made stirrup-spouted vessels moulded as human heads, and the same face recurs on "
     "vessels recovered from sites a hundred kilometres apart, ageing from one example to the next. "
     "Scars, a missing eye and a swollen lip are rendered as carefully as the headdresses. Whether "
     "the faces are likenesses of particular people or standard types is argued over, but the "
     "repetition of individual features across separate finds is hard to explain if the potters were "
     "working from a repertoire alone.",
     "Which choice best states the main purpose of the text?",
     ["To describe a body of ceramic evidence and the interpretive question it raises.",
      "To explain the technique by which a stirrup spout was formed.",
      "To argue that Moche potters worked exclusively from living sitters.",
      "To compare Moche ceramics with those of neighbouring cultures."],
     "A",
     "The text sets out what the vessels show and then names the unsettled dispute about whether the "
     "faces are individuals, without deciding it. The claim that the potters worked only from living "
     "sitters goes further than the text, which says merely that the repetition is hard to explain "
     "otherwise."),

 tsp("T5",
     "A male lyrebird's song is largely other birds' songs. Recordings from one Victorian population "
     "carry the calls of a dozen species, delivered in sequence and with the timing of the originals. "
     "Young males copy from older males rather than from the species themselves, so a phrase can "
     "persist in a lyrebird population long after the bird that supplied it has left the district. "
     "The song is in that sense a record of what was once heard there, kept by birds that never heard "
     "it.",
     "Which choice best describes the overall structure of the text?",
     ["It states a general claim, gives evidence for it, and draws out a consequence of the way the songs are learned.",
      "It presents two rival accounts of the song and endorses one of them.",
      "It traces the spread of a species from one region into another.",
      "It lists the imitated species in order of how often they occur."],
     "A",
     "The opening asserts what the song consists of, the recordings supply the evidence, and the "
     "copying from older males produces the closing point about a song outlasting its source. No "
     "second account of the song is ever stated, so nothing is being weighed against anything."),

 tsp("T6",
     "A flight of locks lifts a boat up a hillside by filling and emptying chambers, and every "
     "passage sends a lockful of water down to the level below. <u>An inclined plane instead carries "
     "the boat itself, afloat in a tank that runs up a slope on rails, with the two tanks "
     "counterweighted against each other.</u> Water is spent only in topping up the tanks, and a boat "
     "that would have taken half a day in a staircase of chambers reaches the summit in twenty "
     "minutes.",
     "Which choice best describes the function of the underlined sentence?",
     ["It describes the arrangement whose advantages the final sentence reports.",
      "It explains why locks came to be built in flights rather than singly.",
      "It concedes a drawback of the inclined plane that was never overcome.",
      "It gives the cost of building an inclined plane."],
     "A",
     "The sentence sets out the tank on rails and the counterweighting, and the closing sentence "
     "reports the water and the time saved that follow from them. Why locks were built in flights is "
     "not addressed anywhere in the text."),

 # ----------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "On the plain around Lake Titicaca, fields were built up into long platforms with water-filled "
     "channels dug between them. A ridge raised in this way sits above the cold air that pools on the "
     "plain at night, and the water in the channels gives back through the small hours the heat it "
     "took up during the day. Trial plots rebuilt on the old pattern in the 1980s came through frosts "
     "that killed the crop in flat fields alongside them.",
     "Which choice best states the main idea of the text?",
     ["The raised-field layout shields a crop from frost, and rebuilt plots have shown the effect directly.",
      "The channels between the platforms were dug chiefly to irrigate the crop in dry months.",
      "Flat fields around the lake yield more than raised ones in most years.",
      "The platforms were built to bring the crop within easier reach of harvesters."],
     "A",
     "The text explains that the ridges rise above the pooled cold air and that the channels release "
     "stored heat, then reports that rebuilt plots survived a frost that killed the neighbouring flat "
     "fields. The irrigation option assigns the channels a purpose the passage never gives them, "
     "since their stated work is thermal."),

 cid("C2",
     "A varroa mite feeds on a developing bee inside its cell and on the adult that emerges from it. "
     "Colonies collapse with far more damage than the feeding alone accounts for: the wound is a "
     "doorway, and viruses that sit at low levels in untroubled colonies multiply once a mite is "
     "carrying them from bee to bee. A beekeeper counting mites on a sticky board is watching a "
     "vector rather than a parasite.",
     "Which choice best states the main idea of the text?",
     ["Much of the harm the mite does comes from the viruses it transmits rather than from its feeding.",
      "The mite feeds on adult bees only and not on developing ones.",
      "Viruses are absent from colonies in which no mites are found.",
      "Counting mites tells a beekeeper very little about the health of a colony."],
     "A",
     "The text says the collapse exceeds what feeding explains and credits the difference to viruses "
     "moved from bee to bee, closing by calling the mite a vector. The option denying viruses in "
     "mite-free colonies contradicts the statement that they are present there at low levels."),

 cid("C3",
     "Common earthenware fires to a buff or a red that no transparent glaze will hide. Tin oxide "
     "stirred into a lead glaze makes it opaque and white, so a cheap clay leaves the kiln looking "
     "like something else, and the painter works on a white ground with much of the freedom a "
     "porcelain decorator has. The glaze is unforgiving in one respect: a brushstroke sinks into the "
     "raw powdery surface at once and cannot be lifted off again.",
     "Which choice best states the main idea of the text?",
     ["The tin glaze gives a common clay a white surface to paint on, at the cost of allowing no correction.",
      "Tin-glazed earthenware is fired at a higher temperature than porcelain is.",
      "Painters preferred earthenware to porcelain because of its warmer colour.",
      "The opacity of the glaze comes from the lead in it rather than from the tin."],
     "A",
     "The passage credits tin oxide with an opaque white surface that frees the painter and then "
     "names the single drawback, a stroke that cannot be taken back. The option attributing the "
     "opacity to lead contradicts the sentence naming tin oxide as the addition that produces it."),

 cid("C4",
     "A young zebra finch raised where it can hear an adult male copies that bird's song, and by "
     "about ninety days its own song has stopped changing. Birds kept in silence through that period "
     "do sing as adults, but the song resembles no wild song and never settles into the same fixed "
     "form. Playing a tutor's song to such a bird after the period has closed changes very little.",
     "Which choice best states the main idea of the text?",
     ["The song is learned within a limited early window, after which a model has little effect.",
      "Birds raised in silence do not sing at all once they are adult.",
      "A zebra finch copies whichever song it hears most often throughout its life.",
      "Adult males rework their songs at the start of each breeding season."],
     "A",
     "The text fixes the copying within the first ninety days and reports that a tutor supplied later "
     "changes very little, which is a window that closes. The option saying silent-reared birds never "
     "sing contradicts the statement that they do sing, only not a normal song."),

 cid("C5",
     "A port that lands cargo only for the country behind it depends on what that country buys. An "
     "entrepot takes in goods that were never intended for its own market, holds them, breaks the "
     "consignments up and ships them out again, and it earns from the handling rather than from the "
     "sale. Such a port can prosper while the region behind it stays poor, and it suffers when a "
     "route it sits on is bypassed rather than when its neighbours' harvests fail.",
     "Which choice best states the main idea of the text?",
     ["An entrepot's fortunes follow the routes running through it rather than the demand of the region behind it.",
      "An entrepot earns most of its income by selling goods to buyers in its own market.",
      "Ports serving only their own hinterland are more profitable than entrepots are.",
      "The prosperity of an entrepot depends on the harvests of the surrounding region."],
     "A",
     "The passage says such a port earns by handling goods bound elsewhere and is hurt by being "
     "bypassed rather than by local failure, which ties its fortunes to the route. The option about "
     "local harvests states precisely the dependence the final sentence denies."),

 cid("C6",
     "Potatoes spread on the ground of the high plateau freeze through the night and thaw in the "
     "day's sun, and the villagers tread them to press out the water that the freezing has driven "
     "from the cells. Repeated over several days, the tubers become light, hard and pale, and they "
     "keep for years in a dry store. The alternation of hard frost and strong sun belongs to the "
     "altitude, so the food is a product of the plateau rather than something carried up onto it.",
     "Which choice best states the main idea of the text?",
     ["The method of preservation depends on conditions particular to the high plateau.",
      "The treated tubers keep for a single season and no longer.",
      "The process requires a fire to dry the tubers at the end.",
      "Villagers took the technique from neighbours in the lowlands."],
     "A",
     "The alternating frost and sun of the plateau are named as what makes the process work, and the "
     "closing sentence calls the food a product of the altitude. The option about a lowland origin "
     "contradicts that closing sentence directly."),

 # ------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "In 1868 the engineer to a small tidal harbour submitted a report on a proposed extension of the "
     "north pier. Historian Ada Kerrigan argues that the report's real object was to warn the "
     "trustees that the harbour's difficulty lay in the annual cost of keeping its channel open, and "
     "not in the length of its pier.",
     "Which quotation from the report most effectively illustrates Kerrigan's claim?",
     ["&ldquo;Whatever is built, the sand returns each winter, and the sum laid out in clearing it has for eleven years together exceeded the sum laid out in building.&rdquo;",
      "&ldquo;The extension would carry the pier head some ninety feet further into deep water.&rdquo;",
      "&ldquo;The masonry of the existing pier was examined and found sound throughout its length.&rdquo;",
      "&ldquo;Vessels of the coasting trade have increased in number since the last survey was made.&rdquo;"],
     "A",
     "The quotation naming eleven years in which clearing the channel cost more than building is "
     "exactly the recurring expense the claim says the report was written to expose. The line about "
     "carrying the pier head into deep water describes the proposal itself and says nothing about "
     "what the harbour costs to keep."),

 coe("E2",
     "A conservator who treated a group of painted panels in the 1950s kept a working notebook "
     "alongside the formal treatment records. Curator Piet Vandenberg argues that the notebook shows "
     "her subordinating the appearance of a finished panel to the requirement that anything she added "
     "could later be taken off again.",
     "Which quotation from the notebook most effectively illustrates Vandenberg's claim?",
     ["&ldquo;The panel was photographed under raking light before any work began.&rdquo;",
      "&ldquo;Chose the weaker adhesive for the flaking edge although the stronger holds better, since the stronger cannot be got off again without the paint.&rdquo;",
      "&ldquo;The losses along the lower edge are numerous but small.&rdquo;",
      "&ldquo;Worked four days on the sky, which is the part a visitor sees first.&rdquo;"],
     "B",
     "Choosing the weaker adhesive precisely because the stronger could not be removed later puts "
     "removability ahead of the better result, which is the preference the claim describes. "
     "Photographing the panel before work began is ordinary documentation and shows nothing about "
     "how she chose her materials."),

 coe("E3",
     "A member of a 1911 Antarctic party kept a diary through the season of depot-laying that "
     "preceded the main journey. Historian Sofia Lindqvist argues that the diary treats the placing "
     "of the supply depots, rather than the journey they were meant to support, as the work on which "
     "everything turned.",
     "Which quotation from the diary most effectively illustrates Lindqvist's claim?",
     ["&ldquo;The wind dropped towards evening and the light on the barrier was very fine.&rdquo;",
      "&ldquo;The ponies took their feed badly and one is lame in the near fore.&rdquo;",
      "&ldquo;We are eleven miles short of where the depot should stand, and every mile we fail to carry now is a mile the party must carry in the spring, when it can least afford to.&rdquo;",
      "&ldquo;Read aloud in the tent for an hour after the evening meal.&rdquo;"],
     "C",
     "The entry measuring a shortfall now against a burden the main party will carry later makes the "
     "depot work the thing the whole undertaking rests on, which is the claim. The lame pony records "
     "a difficulty of the depot season without indicating what depends on it."),

 coe("E4",
     "Timber decayed by brown-rot fungi is left dark, cracked into cubes and much weakened, while "
     "timber attacked by white-rot fungi turns pale and fibrous. Mycologist Rafael Ibarra argues that "
     "the brown-rot fungi break down the cellulose and leave the lignin behind, rather than removing "
     "both as the white-rot fungi do.",
     "Which finding, if true, would most directly support Ibarra's argument?",
     ["Analysis of brown-rotted timber finds the lignin fraction nearly unchanged while most of the cellulose has gone, whereas white-rotted timber has lost both.",
      "Brown-rot fungi are more common in conifer timber than in hardwoods.",
      "Brown-rotted timber crumbles under the thumb far more readily than sound timber does.",
      "Both kinds of fungus require the timber to be damp before they can grow at all."],
     "A",
     "Measuring the two components separately in each kind of decayed wood is what distinguishes the "
     "selective removal of cellulose from the removal of everything, which is the contrast being "
     "argued. That brown-rotted timber crumbles easily is agreed by both accounts, since any loss of "
     "substance would weaken the wood."),

 coe("E5",
     "Male white-crowned sparrows in adjoining valleys sing recognisably different versions of the "
     "species song, and the boundary between the two versions falls in the same place from year to "
     "year. Ornithologist Beata Nowicka argues that the boundary persists because young males learn "
     "from the neighbours they settle among, rather than because birds from the two valleys are "
     "unwilling to breed with each other.",
     "Which finding, if true, would most directly support Nowicka's argument?",
     ["Males ringed as nestlings in one valley and later found breeding in the other sing the version of the valley they settled in, and pairings across the boundary are as frequent as pairings within it.",
      "The two versions of the song differ mainly in the length of the opening whistle.",
      "The boundary follows a ridge that the birds seldom cross in winter.",
      "Males respond more strongly to playback of their own valley's version than to the neighbouring one."],
     "A",
     "Birds that move and then sing the local song take the dialect from where they settle, and equal "
     "rates of crossing pairs remove the reluctance to interbreed that the rival account requires. A "
     "stronger response to the local playback fits either account, since a learned dialect would be "
     "recognised just as a breeding barrier would."),

 coe("E6",
     "Households in some Andean valleys held plots at several altitudes at once, from maize land low "
     "down to herding ground on the high grassland. Archaeologist Neil Ostrander argues that the "
     "arrangement was a deliberate way of drawing on several climates at once, rather than a "
     "consequence of population pressure pushing families onto marginal land.",
     "Which finding, if true, would most directly support Ostrander's argument?",
     ["Households holding high and low plots together were among the largest and best provided in their communities, and the outlying plots were taken up in years when land on the valley floor was still unclaimed.",
      "Journeys between the highest and the lowest plots took several days on foot.",
      "Maize was grown only below a certain altitude.",
      "Some communities held plots on both slopes of the same valley."],
     "A",
     "Well-provided households taking up distant plots while land at home was still unclaimed is what "
     "a deliberate spread across climates looks like, and it is not what pressure onto marginal "
     "ground would produce. The several days' walk between plots describes the cost of the "
     "arrangement without indicating why it was adopted."),

 coe("E7",
     "Honey sealed under a wax capping keeps indefinitely, while honey left uncapped takes up water "
     "from the air and may ferment; fermentation becomes likely above about twenty per cent water. A "
     "beekeeper recorded the water content of honey drawn from sealed and from unsealed comb at four "
     "apiaries in the same season."
     + table(["Apiary", "Water content, sealed comb (%)", "Water content, unsealed comb (%)"],
             [["Ashgrove", "17.2", "20.9"], ["Braemore", "16.8", "21.4"],
              ["Cairnhead", "17.6", "19.8"], ["Dunmore", "17.1", "22.3"]])
     + "The unsealed honey passed twenty per cent at three of the four apiaries, and the widest "
       "difference between sealed and unsealed honey was recorded at _____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["Dunmore, where 22.3 per cent in the unsealed comb stood against 17.1 per cent in the sealed comb.",
      "Cairnhead, where the unsealed comb held 19.8 per cent water.",
      "Braemore, where the sealed comb held the least water of any apiary.",
      "Ashgrove, where the unsealed comb held 20.9 per cent water."],
     "A",
     "The gap between the two combs is largest where 22.3 per cent stands against 17.1 per cent, a "
     "difference of 5.2 points, which is wider than any other pair in the table. The Braemore entry "
     "reports the lowest sealed figure rather than the widest gap, and its difference of 4.6 points "
     "is smaller."),

 coe("E8",
     "A conservation studio tested four traditional lake pigments by exposing painted swatches to a "
     "controlled light source and measuring the colour change after 200 and after 600 hours; a change "
     "of more than four units is visible to the unaided eye."
     + table(["Pigment", "Change at 200 hours (units)", "Change at 600 hours (units)"],
             [["Kermes lake", "0.9", "2.6"], ["Madder lake", "1.2", "3.1"],
              ["Weld lake", "3.9", "9.4"], ["Brazilwood lake", "6.8", "14.2"]])
     + "Two of the four pigments were still below the visible threshold at 600 hours, and the pigment "
       "that had shifted furthest by 200 hours _____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["was brazilwood lake, which had already moved 6.8 units by then and reached 14.2 units at 600 hours.",
      "was weld lake, which moved 3.9 units in the first 200 hours.",
      "was madder lake, whose change reached 3.1 units at 600 hours.",
      "was kermes lake, which changed least of the four pigments tested."],
     "A",
     "Brazilwood lake shows 6.8 units at 200 hours, the largest first-stage change in the table, and "
     "its 14.2 units at 600 hours confirms it as the least stable of the four. Weld lake moved 3.9 "
     "units over the same period, a real change but a smaller one than brazilwood's."),

 coe("E9",
     "A port authority compared four quays over a single year, recording the cargo handled at each "
     "and the average time a ship spent alongside it."
     + table(["Quay", "Cargo handled (thousand tonnes)", "Average time alongside (hours)"],
             [["North Quay", "410", "31"], ["East Jetty", "390", "19"],
              ["Old Basin", "240", "44"], ["Ferry Quay", "155", "12"]])
     + "The authority argued that tonnage on its own is a poor measure of how hard a quay is worked, "
       "pointing out that the quay handling the most cargo was not the quickest to turn a ship round: "
       "_____",
     "Which choice most effectively uses data from the table to complete the text?",
     ["North Quay handled 410 thousand tonnes but held a ship 31 hours on average, while East Jetty handled 390 thousand tonnes in 19 hours.",
      "Old Basin handled 240 thousand tonnes and held a ship alongside for 44 hours.",
      "Ferry Quay turned a ship round in 12 hours, the shortest average time recorded.",
      "East Jetty handled 390 thousand tonnes, the second largest figure in the table."],
     "A",
     "Setting 410 thousand tonnes at 31 hours beside 390 thousand tonnes at 19 hours puts nearly "
     "equal tonnage against very different times alongside, which is what the argument about tonnage "
     "requires. The Ferry Quay entry gives the shortest time but pairs it with the smallest tonnage, "
     "so it does not separate the two measures."),

 # --------------------------------------------------------------- Inferences (6)
 inf("I1",
     "A bronze that has lain in salty ground takes chloride into its corrosion layer, and in a damp "
     "room the chloride, the copper and the air together produce a pale green powder that eats "
     "further into the metal as it forms. Brushing the powder away does not stop the process, because "
     "the chloride sits beneath it. A curator who finds fresh green powder on a bronze cleaned two "
     "years earlier can therefore reasonably conclude that _____",
     ["chloride remains in the object and the air around it is damp enough for the reaction to run.",
      "the object cannot have been buried in salty ground.",
      "the powder forms a stable surface that will protect the metal beneath it.",
      "the bronze contains no copper."],
     "A",
     "The powder appears only where chloride is still present and moisture is available, so its "
     "return points to both conditions rather than to the success of the earlier cleaning. The option "
     "calling the powder protective contradicts the statement that it eats into the metal as it "
     "forms."),

 inf("I2",
     "Paper ground from wood carries acids left in the sheet when it was made, and those acids go on "
     "cutting the cellulose chains for as long as they remain there. Washing a sheet in an alkaline "
     "solution leaves a small reserve in the fibre that neutralises acid as it is produced. The "
     "treatment cannot give back the strength a brittle sheet has already lost, which means its value "
     "lies in _____",
     ["slowing the damage still to come rather than repairing the damage already done.",
      "returning the sheet to the strength it had when it was new.",
      "removing the printed image so that the fibre can be used again.",
      "identifying the mill at which the paper was made."],
     "A",
     "The reserve acts on acid produced from that point onward, and the passage denies that lost "
     "strength can be recovered, so what is gained is protection against future loss. The option "
     "about restoring the original strength states exactly what the final sentence rules out."),

 inf("I3",
     "A crab-claw sail is a triangle held between two spars with its point at the foot, and it drives "
     "a hull well with the wind on the beam or behind. Voyaging canoes carrying it could not be "
     "pushed far into a headwind, and the sailing directions preserved in the islands describe "
     "waiting out a season rather than beating against it. It follows that the timing of a voyage in "
     "such a canoe was _____",
     ["governed by the prevailing wind rather than chosen freely.",
      "unaffected by the direction from which the wind blew.",
      "determined chiefly by the length of the hull.",
      "settled by the number of paddlers who could be found."],
     "A",
     "A rig that will not work to windward, together with directions that advise waiting for the "
     "season, leaves the wind to decide when a canoe could leave. The option calling the timing "
     "unaffected by wind direction contradicts the whole passage."),

 inf("I4",
     "Snow returns most of the ultraviolet light falling on it, so a traveller on an ice sheet takes "
     "it from below as well as from above, and an overcast day gives little protection because cloud "
     "scatters the light without absorbing much of it. The injury it causes appears some hours after "
     "the exposure that produced it. A party that has spent a grey day on the ice without eye "
     "protection will therefore _____",
     ["not know until the evening how much damage the day has done.",
      "have been shielded from harm by the cloud cover.",
      "notice the injury within the first minutes of exposure.",
      "have received ultraviolet light only from directly overhead."],
     "A",
     "The passage states that the injury shows itself some hours after the exposure, so a day's "
     "damage is not apparent while it is being done. The option about noticing it within minutes "
     "contradicts that delay, which is the one fact about timing the text supplies."),

 inf("I5",
     "The mycelium of certain meadow fungi spreads outward from a starting point at a fairly steady "
     "rate, exhausting the nutrients behind it as it goes, and it fruits at the advancing edge. A "
     "ring of mushrooms is therefore a cross-section of one organism's growth, and a wider ring is an "
     "older one. Where two rings meet, neither can advance into ground the other has already stripped, "
     "so the arcs _____",
     ["flatten against each other and leave a straight edge along the line of contact.",
      "merge into a single larger circle.",
      "reverse direction and grow back towards their own centres.",
      "fruit more heavily along the line of contact than elsewhere."],
     "A",
     "Neither ring can move into exhausted ground, so growth stops along the line where they touch "
     "while the rest of each ring continues, which straightens the arcs there. The option about "
     "merging into one circle would require each ring to cross the other's spent ground, which the "
     "passage rules out."),

 inf("I6",
     "Glass cools from the outside inward, and the surface that sets first is put under strain as the "
     "interior contracts behind it. A vessel taken straight from the blowing iron into the open air "
     "may hold enough of that strain to fly apart days later without being touched. Passing it slowly "
     "down a heated tunnel lets the whole thickness come down together, which means that the tunnel's "
     "purpose is to _____",
     ["even out the rate at which different parts of the glass cool.",
      "raise the glass to a temperature higher than the furnace reached.",
      "harden the surface of the glass against scratching.",
      "shape the vessel after it has left the blowing iron."],
     "A",
     "The trouble described is one part of the glass setting before another, and the tunnel is said "
     "to bring the whole thickness down together, which removes that difference. The option about "
     "shaping the vessel gives the tunnel work that the blowing iron has already finished."),

 # -------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "A plaster mould draws water out of the liquid clay poured into it, so a skin thickens against "
     "the wall while the middle stays fluid. The caster tips the surplus back out after a few _____ "
     "of even thickness is left standing in the mould.",
     ["minutes; a wall", "minutes, a wall", "minutes a wall", "minutes: and a wall"], "A",
     "Two complete statements stand on either side of the blank with no conjunction between them, "
     "which is what the semicolon is for. The comma on its own splices the two together, and a colon "
     "does not take a conjunction after it."),

 bnd("B2",
     "A mason bee lives alone and makes no honey. Each female stocks a row of cells in a hollow stem "
     "with pollen and seals them off with _____ garden wall fitted with bundles of cut stems will "
     "hold hundreds of them by the second season.",
     ["mud, and a", "mud; and a", "mud: and a", "mud and a"], "A",
     "Two independent clauses joined by a coordinating conjunction take a comma in front of that "
     "conjunction. Neither the semicolon nor the colon is used before a coordinating conjunction, and "
     "dropping the comma runs the two clauses together."),

 bnd("B3",
     "The site at Caral lies in a dry valley some twenty kilometres from the Peruvian coast. Because "
     "its platform mounds and sunken plazas were raised at a date close to that of the earliest "
     "pyramids in _____ chronology of monumental building in the Americas had to be carried back by "
     "more than a thousand years.",
     ["Egypt, the", "Egypt; the", "Egypt: the", "Egypt and the"], "A",
     "The clause opening with 'Because' is dependent and has to be closed off with a comma before the "
     "main clause begins. A semicolon or a colon needs a complete sentence in front of it, and a "
     "dependent clause is not one."),

 bnd("B4",
     "A mushroom flicks its spores sideways into the still air between the gills, and it does so with "
     "no moving part at all. The mechanism needs three _____ a drop of water condensed at the base of "
     "the spore, a film of water spread over the spore's surface, and the sudden merging of the two.",
     ["things: a drop", "things; a drop", "things, and a drop", "things a drop"], "A",
     "The words in front of the blank make a complete sentence announcing that three things are "
     "needed, and the colon is the mark that introduces the list naming them. The semicolon would "
     "demand a complete sentence after it, and a series of noun phrases is not one."),

 bnd("B5",
     "A pony breaks through crust that a dog runs over, and it cannot be fed on what a sledging party "
     "is already hauling for itself. Roald Amundsen, an experienced traveller in the Canadian _____ "
     "dogs from the outset and planned to kill the weaker ones as the loads went down.",
     ["Arctic, took", "Arctic; took", "Arctic: took", "Arctic took"], "A",
     "The appositive beginning 'an experienced traveller' was opened with a comma and has to be "
     "closed with a matching comma before the verb arrives. Any other mark would cut the subject off "
     "from its verb."),

 bnd("B6",
     "A transit shed stands on the quay itself and holds cargo only until the consignee's carts come "
     "for it. Nothing in it is meant to sit through a _____ that wait on a market are sent inland to "
     "a warehouse, where the land costs less.",
     ["season. Goods", "season, goods", "season; and goods", "season goods"], "A",
     "Two complete sentences meet at the blank, so a full stop and a capital letter separate them "
     "properly. The comma on its own leaves two independent clauses spliced together, and a semicolon "
     "is not followed by a coordinating conjunction."),

 bnd("B7",
     "A tapestry is woven from the back, at full size, against a painted cartoon hung behind the "
     "warp. Everything the painter put into that cartoon &mdash; the fall of a sleeve, the modelling "
     "of a cheek, the depth of a _____ has to be rendered in wool by a weaver who cannot see the "
     "front of the work.",
     ["shadow &mdash; has", "shadow, has", "shadow; has", "shadow: has"], "A",
     "The list of details was opened with a dash and needs a matching dash to close it before the "
     "sentence resumes. Closing it with a comma leaves the opening dash without a partner and blurs "
     "where the interruption ends."),

 bnd("B8",
     "Depths on a chart are reckoned from a level chosen so that the tide will very seldom fall below "
     "it. The figure printed beside a shoal is therefore not the depth a ship will find _____ is the "
     "depth it can count on finding at almost any state of the tide.",
     ["there; it", "there, it", "there it", "there: and it"], "A",
     "Two complete statements meet at the blank with no conjunction between them, which is the "
     "semicolon's work. The comma alone splices them together, and a colon does not take a "
     "conjunction after it."),

 bnd("B9",
     "Two thirds of the building at Machu Picchu is said to lie out of sight below the surface. "
     "Because the site sits on a ridge that takes some two metres of rain a _____ builders laid a bed "
     "of broken stone under every terrace and cut channels to carry the water off the rock face.",
     ["year, the", "year; the", "year: the", "year and the"], "A",
     "The opening clause begins with 'Because' and is dependent, so a comma closes it before the main "
     "clause starts. Both the semicolon and the colon require a complete sentence in front of them."),

 bnd("B10",
     "A songbird's voice box sits where the windpipe divides in two, and a set of vibrating membranes "
     "is carried on each _____ two sources of sound, two sets of muscles controlling them, and a bird "
     "able to sing two independent lines at once.",
     ["branch: two", "branch; two", "branch, and two", "branch two"], "A",
     "The words in front of the blank form a complete sentence, and the colon introduces the list "
     "that spells out what the arrangement yields. The semicolon would require a complete sentence "
     "after it, and a series of noun phrases is not one."),

 bnd("B11",
     "Wool fibres carry microscopic scales that all lie in one direction. Agitate the cloth in hot "
     "water and the scales lock against one another and will not come _____ shrinks, thickens and "
     "stops fraying at a cut edge, which is what a fuller is paid to bring about.",
     ["apart; the cloth", "apart, the cloth", "apart the cloth", "apart: and the cloth"], "A",
     "Two independent clauses meet at the blank with no conjunction, and the semicolon is the mark "
     "that joins them. The comma by itself produces a splice, and a colon is not used in front of a "
     "coordinating conjunction."),

 bnd("B12",
     "A river reaching the sea across a flat coast spreads out, slows down and drops the sand it is "
     "carrying, and the bar that forms shifts with every storm. Engineers narrow the mouth between "
     "two low walls so that the same volume of water runs through a smaller _____ current that "
     "results scours the channel deeper than the river would ever have run of its own accord.",
     ["section, and the", "section; and the", "section: and the", "section and the"], "A",
     "Two independent clauses joined by a coordinating conjunction take a comma before that "
     "conjunction. The semicolon and the colon are not used in front of a coordinating conjunction, "
     "and omitting the comma runs the clauses together."),

 # --------------------------------------------- Form, Structure, and Sense (9)
 fss("F1",
     "The harbour's dues books run back to 1840, but the volumes covering the war years were never "
     "bound and have come apart into loose sheets. Neither the archivist nor the two volunteers "
     "sorting them _____ willing to guess at the order the sheets once stood in.",
     ["is", "are", "was", "has been"], "B",
     "With 'neither ... nor', the verb agrees with whichever subject stands nearer to it, and 'the "
     "two volunteers' is plural. The singular forms would agree with the archivist, who is the "
     "further of the two subjects."),

 fss("F2",
     "Every colony is weighed on the same scale at the end of the season and the figure entered "
     "against the hive number. The average weight of the eight colonies on the moorland site _____ "
     "well below the average for the apiary as a whole this year.",
     ["are", "were", "is", "have been"], "C",
     "The subject is the single average weight, not the eight colonies named inside the prepositional "
     "phrase, so the verb is singular, and the present tense matches 'this year'. The plural forms "
     "would agree with the colonies, which are not what the sentence says was low."),

 fss("F3",
     "The kiln is drawn on a Friday, and every piece is checked against the firing book before it is "
     "packed. When the crate reached Bristol and the dealer's men lifted the straw out of it, they "
     "found that three of the plates _____ somewhere between the bench and the carrier's cart.",
     ["crack", "had cracked", "will crack", "are cracking"], "B",
     "The cracking took place before the crate was opened, and the opening is itself reported in the "
     "past, so the past perfect puts one past event ahead of another. The simple present would place "
     "the cracking in the present, which the account of a finished journey rules out."),

 fss("F4",
     "The volume came in with its spine gone and half the sections loose in the covers. The binder "
     "will pull the book apart, resew the sections onto new cords and _____ the original boards back "
     "on.",
     ["lacing", "laces", "lace", "to lace"], "C",
     "The three actions share the auxiliary 'will', so the third has to take the same bare form as "
     "'pull' and 'resew'. The participle breaks the series and leaves the auxiliary with no third "
     "verb to govern."),

 fss("F5",
     "Two dyehouses worked the same weld and the same alum on cloth from the same weaver, and the "
     "finished pieces were hung side by side under a north light. The yellow struck in the eastern "
     "house is markedly deeper than _____ in the western one.",
     ["the western house", "that struck", "those struck", "they struck"], "B",
     "The comparison is between one yellow and another yellow, so the second term has to be a "
     "singular stand-in for the colour rather than for the house that produced it. Comparing a yellow "
     "with a house sets unlike things beside each other."),

 fss("F6",
     "The depot was laid in March and marked with a line of flags set at right angles to the route, "
     "so that a party coming back on any bearing would cross the line before it crossed the depot. "
     "Running low on fuel on the return, _____",
     ["the flags were sighted an hour before dark.",
      "the party sighted the flags an hour before dark.",
      "an hour before dark brought the flags into sight.",
      "sighting the flags happened an hour before dark."],
     "B",
     "The opening phrase describes the party, so the party has to be the subject of the clause that "
     "follows it. Beginning with the flags makes it the flags that were running low on fuel."),

 fss("F7",
     "Beekeepers who open a hive in cold weather do more harm than good, and a colony chilled in "
     "March may never build up. The inspector, together with the two volunteers who hold the frames, "
     "_____ to work quickly once the crown board is off.",
     ["need", "needs", "needing", "have needed"], "B",
     "A phrase introduced by 'together with' does not add to the subject, which remains the single "
     "inspector, so the verb is singular. The plural verb would agree with the volunteers named "
     "inside that phrase."),

 fss("F8",
     "The survey flew the valley in 2019 and flew it again after the fire of 2023. Comparing the two "
     "sets of images, the team found that the earthworks it _____ under closed canopy four years "
     "earlier were now plainly visible from the air.",
     ["maps", "has mapped", "had mapped", "will map"], "C",
     "The mapping happened four years before a discovery that is itself reported in the past, so the "
     "past perfect is the form that puts one past action ahead of another. The present perfect would "
     "tie the mapping to the present rather than to the earlier survey."),

 fss("F9",
     "The store is arranged by fibre rather than by date, and nothing is shelved until it has been "
     "entered in the register. On the shelf beside the weld samples _____ three boxes of lichen-dyed "
     "wool that no one has yet catalogued.",
     ["is", "sits", "are", "was"], "C",
     "The subject follows the verb in this sentence and is the three boxes, which is plural, so the "
     "verb has to be plural too. The singular forms would agree with the shelf, which sits inside the "
     "introductory phrase rather than being the thing counted."),

 # -------------------------------------------------------------- Transitions (9)
 trn("N1",
     "Birds singing in traffic noise sing louder, and many of them sing higher as well, which lifts "
     "the song clear of the low rumble that would otherwise mask it. _____ a bird singing higher is "
     "also singing a song that carries less far, so the gain in one respect is paid for in another.",
     ["However,", "Therefore,", "Likewise,", "For instance,"], "A",
     "The second sentence names a cost that cuts against the benefit described in the first, so the "
     "transition has to mark a contrast rather than a consequence."),

 trn("N2",
     "Glassmakers around the Mediterranean used soda from mineral sources and from the ash of coastal "
     "plants, and their glass has lain two thousand years in the ground with little change. _____ the "
     "forest glasshouses of northern Europe used potash from burnt beech, and their windows weather "
     "into a crust that eats the surface away.",
     ["Nevertheless,", "As a result,", "By contrast,", "In other words,"], "C",
     "The two sentences set one kind of glass against another with opposite durability, which calls "
     "for a transition marking difference. Treating the second as a consequence of the first would be "
     "wrong, since neither practice caused the other."),

 trn("N3",
     "A skep is a basket of coiled straw, and the comb inside it is fastened to the walls, so a "
     "beekeeper cannot look into the colony without cutting the comb away. _____ inspection meant "
     "destroying most of what was inspected, and the honey crop was taken by killing the bees.",
     ["Accordingly,", "Nevertheless,", "By contrast,", "For example,"], "A",
     "Being unable to see inside without cutting the comb is exactly what makes an inspection "
     "destructive, so the second sentence states a result of the first. Marking it as a contrast "
     "would deny the link the first sentence sets up."),

 trn("N4",
     "A breakwater faced with rough quarry stone loses blocks in the first heavy winter, because a "
     "rounded boulder rolls once the sea has undercut it. _____ modern breakwaters are armoured with "
     "cast concrete shapes whose limbs hook into their neighbours and which lock tighter as the sea "
     "works on them.",
     ["For this reason,", "Nevertheless,", "Similarly,", "In fact,"], "A",
     "The failure of rounded stone is what the interlocking concrete units exist to prevent, so the "
     "second sentence gives the response to the problem stated in the first. Marking it as a "
     "similarity would ignore the difference between blocks that roll and blocks that lock."),

 trn("N5",
     "Bitter manioc holds compounds that release cyanide as soon as the root is damaged, and a meal "
     "made from the raw root can kill. _____ the root is grated, packed into a long woven tube and "
     "squeezed, and the liquid pressed out of it is boiled hard before anything is eaten.",
     ["Instead,", "Accordingly,", "By contrast,", "Even so,"], "B",
     "The grating, the squeezing and the boiling are done because the raw root is dangerous, so the "
     "second sentence follows from the first as a response to it. 'Instead' would require the second "
     "sentence to replace an alternative that the first had proposed, and it proposes none."),

 trn("N6",
     "A dyed textile fades in proportion to the total light that has fallen on it over its whole "
     "life, and no part of that fading is ever recovered. _____ a gallery showing costume keeps its "
     "light levels low, keeps its exhibitions short, and returns each piece to a dark store for years "
     "at a time.",
     ["Consequently,", "Nevertheless,", "By contrast,", "For example,"], "A",
     "Permanent and cumulative fading is precisely what low light and short exposure are meant to "
     "limit, so the second sentence follows from the first. No contrast is being drawn between them."),

 trn("N7",
     "Books printed on rag paper before 1800 are often still supple, and their leaves turn without "
     "cracking at the fold. _____ a novel printed in 1890 on paper ground from wood may break along "
     "the fold in the hand, because the process that made the pulp cheap also left acid in the sheet.",
     ["Likewise,", "By contrast,", "Therefore,", "In short,"], "B",
     "The supple older book and the brittle later one are set against each other, so the transition "
     "has to mark the difference. Treating the second as a consequence of the first would make the "
     "older books somehow cause the later ones to decay."),

 trn("N8",
     "Wind-carved ridges of hard snow run parallel to the prevailing wind, and a party crossing them "
     "at an angle spends its day lifting sledges over one ridge after another. _____ the ridges serve "
     "as a compass of a kind, and a driver who has lost the sun can hold a course by the angle at "
     "which they strike the runners.",
     ["Even so,", "For instance,", "As a result,", "In other words,"], "A",
     "The ridges are first described as an obstacle and then credited with a use, so the transition "
     "has to concede the difficulty before the benefit. Presenting the benefit as a result of the "
     "difficulty misstates the relation, since it is the alignment of the ridges and not the labour "
     "of crossing them that makes them useful."),

 trn("N9",
     "Before the deep-water docks were cut, a ship too big for the quay lay at anchor in the river "
     "and her cargo was carried ashore in barges. Every ton was handled twice and paid for twice. "
     "_____ a port that could bring a ship alongside undercut its neighbours long before it could "
     "load one any faster.",
     ["Nevertheless,", "For example,", "As a result,", "By contrast,"], "C",
     "Double handling and double payment are the costs a quayside berth removes, so the closing "
     "sentence states what followed from them. Marking it as a contrast would set the sentence "
     "against the facts it actually rests on."),

 # -------------------------------------------------------- Rhetorical Synthesis (9)
 syn("R1",
     ["The Pontcysyllte aqueduct carries a canal 38 metres above the River Dee in north Wales.",
      "It was completed in 1805 to designs by Thomas Telford and William Jessop.",
      "The trough is made of cast-iron plates bolted together and bedded in Welsh flannel and lead.",
      "Masonry piers carry the trough, and the upper part of each pier is hollow.",
      "A hollow pier weighs far less than a solid pier of the same height and section."],
     "emphasise a design decision that reduced the load the structure had to carry.",
     ["The Pontcysyllte aqueduct carries a canal 38 metres above the River Dee and was completed in 1805.",
      "Because the upper part of each masonry pier was built hollow, it weighs far less than a solid pier of the same height and section would.",
      "The trough is made of cast-iron plates bolted together and bedded in Welsh flannel and lead.",
      "Thomas Telford and William Jessop designed the aqueduct together."],
     "B",
     "The goal asks for a decision that lightened the structure, and only the hollow upper piers are "
     "described in the notes as a saving in weight. The cast-iron trough is a construction detail "
     "whose bearing on the load is never stated in the notes."),

 syn("R2",
     ["A finisher decorates a leather binding by pressing heated brass tools into the leather.",
      "Gold leaf is laid over an adhesive of egg white and vinegar called glaire.",
      "The tool must be hot enough to fix the leaf but not so hot that it scorches the leather.",
      "A finisher judges the heat by touching the tool to a damp sponge and listening to it.",
      "An impression made at the wrong heat cannot be removed and the cover is spoiled."],
     "explain why the finisher's judgement of the tool's heat matters so much.",
     ["A finisher decorates a leather binding by pressing heated brass tools into the leather.",
      "Gold leaf is laid over an adhesive of egg white and vinegar called glaire.",
      "Because an impression made at the wrong heat cannot be removed, the finisher tests the tool by ear against a damp sponge before it ever touches the cover.",
      "A finisher judges the heat by touching the tool to a damp sponge and listening to it."],
     "C",
     "The goal asks why the judgement matters, so the choice has to join the test to the consequence "
     "of getting it wrong, and only one option carries both. The note about the sponge on its own "
     "describes the test without saying what is at stake."),

 syn("R3",
     ["Smalt is powdered blue glass coloured with cobalt.",
      "It was the cheapest strong blue available to painters in the sixteenth century.",
      "The colour is strong only while the particles are coarse; ground finer, smalt turns pale.",
      "Coarse particles are hard to disperse in oil and leave a gritty paint.",
      "Potassium leaches out of the glass over time and many smalt passages have turned grey."],
     "explain the difficulty a painter faced in working with smalt.",
     ["Smalt is powdered blue glass coloured with cobalt.",
      "A painter had to choose between a strong blue in coarse particles that left the paint gritty and a smoother paint that finer grinding had made pale.",
      "Potassium leaches out of the glass over time, and many smalt passages have turned grey.",
      "Smalt was the cheapest strong blue available to painters in the sixteenth century."],
     "B",
     "The goal asks about a difficulty in using the pigment, and the trade-off between colour "
     "strength and workable particle size is the one the notes set up directly. The leaching of "
     "potassium describes what happens to the paint long after the painter has finished, rather than "
     "a problem met in using it."),

 syn("R4",
     ["The Chachapoya buried some of their dead in tombs built into cliff faces in northern Peru.",
      "At Revash the tombs stand out from the ledges as small houses with painted walls.",
      "The ledges can be reached only from above, by rope.",
      "Looting has emptied many of the tombs that are easier to reach.",
      "Tombs on the least accessible ledges have been found with their contents undisturbed."],
     "explain why some of the tombs have survived intact.",
     ["The Chachapoya buried some of their dead in tombs built into cliff faces in northern Peru.",
      "At Revash the tombs stand out from the ledges as small houses with painted walls.",
      "Looting has emptied many of the tombs that are easier to reach.",
      "Because the least accessible ledges can be reached only from above by rope, the tombs standing on them have been found with their contents undisturbed."],
     "D",
     "The goal asks why some tombs are still intact, and only one choice joins the difficulty of "
     "reaching a ledge to the undisturbed contents found there. The note that looters emptied the "
     "easier tombs reports the fate of the others rather than the reason these survived."),

 syn("R5",
     ["Orchil is a purple dye made from lichens of the genus Roccella.",
      "The lichen is steeped for weeks in an ammoniacal liquor.",
      "The raw lichen shows no purple at all before the steeping begins.",
      "Orchil dyes wool a rich purple without any mordant.",
      "The colour fades badly in sunlight and was often used to shade cheaper cloth."],
     "emphasise that the colour is produced by the process rather than extracted from the lichen.",
     ["Orchil dyes wool a rich purple without any mordant.",
      "The raw lichen shows no purple at all, and the colour appears only after weeks of steeping in an ammoniacal liquor.",
      "Orchil is a purple dye made from lichens of the genus Roccella.",
      "The colour fades badly in sunlight and was often used to shade cheaper cloth."],
     "B",
     "The goal turns on the colour being made rather than found, and only the choice pairing the "
     "colourless raw lichen with the weeks of steeping shows that. The note that no mordant is needed "
     "describes how the dye behaves on wool, not where the colour comes from."),

 syn("R6",
     ["H&#333;k&#363;le&lsquo;a is a double-hulled canoe launched in Hawaii in 1975.",
      "It was built to test whether long Pacific passages could be sailed without instruments.",
      "Its 1976 passage to Tahiti was navigated by Mau Piailug of Satawal.",
      "No compass, chart or clock was carried on that passage.",
      "Piailug afterwards taught the method to Hawaiian navigators."],
     "explain what the 1976 passage was intended to demonstrate.",
     ["H&#333;k&#363;le&lsquo;a is a double-hulled canoe launched in Hawaii in 1975.",
      "Sailed to Tahiti in 1976 with no compass, chart or clock aboard, the canoe was meant to show that a long Pacific passage could be navigated without instruments.",
      "Mau Piailug of Satawal navigated the passage and afterwards taught the method to Hawaiian navigators.",
      "The canoe was launched in Hawaii in 1975 and reached Tahiti the following year."],
     "B",
     "The goal asks what the passage was meant to demonstrate, and only the choice naming both the "
     "absence of instruments and the claim under test answers it. The note about Piailug teaching "
     "Hawaiian navigators reports what followed the voyage rather than its purpose."),

 syn("R7",
     ["Fridtjof Nansen had the Fram built with a rounded hull and no sharp turn of bilge.",
      "Ice closing on a conventional hull grips its sides and crushes it.",
      "Pressure on the Fram's hull pushed the ship upward instead of inward.",
      "The Fram drifted in the polar pack from 1893 to 1896 and was not damaged.",
      "The design cost the ship much of its sailing quality in open water."],
     "explain how the shape of the hull protected the ship.",
     ["Fridtjof Nansen had the Fram built with a rounded hull and no sharp turn of bilge.",
      "Because the rounded hull gave the closing ice nothing to grip, the pressure lifted the ship instead of crushing it, and it drifted three years in the pack undamaged.",
      "The design cost the ship much of its sailing quality in open water.",
      "The Fram drifted in the polar pack from 1893 to 1896."],
     "B",
     "The goal asks how the shape gave protection, and only one option carries the mechanism, ice "
     "with nothing to grip and a ship lifted rather than crushed, together with the result. Naming "
     "the rounded hull on its own describes the design without saying what it did."),

 syn("R8",
     ["Many flowers carry markings that reflect ultraviolet light.",
      "Bees see ultraviolet light; people do not.",
      "Photographed through an ultraviolet filter, a plain yellow flower may show a dark centre.",
      "The markings converge on the nectar and the anthers.",
      "Flowers whose markings are masked receive fewer and shorter visits from bees."],
     "explain the evidence that the markings guide bees to the nectar.",
     ["Many flowers carry markings that reflect ultraviolet light.",
      "Photographed through an ultraviolet filter, a plain yellow flower may show a dark centre.",
      "The markings converge on the nectar, and flowers whose markings are masked receive fewer and shorter visits from bees.",
      "Bees see ultraviolet light and people do not."],
     "C",
     "The goal asks for the evidence of guidance, and only the choice pairing markings that point at "
     "the nectar with the drop in visits when they are masked supplies it. The photograph through a "
     "filter shows that the markings exist without showing what they do."),

 syn("R9",
     ["A tidal harbour empties as the tide falls, and the ships in it take the ground twice a day.",
      "A wet dock holds water behind gates and keeps ships afloat at every state of the tide.",
      "The gates can be opened only while the water outside stands level with the water inside.",
      "At Liverpool a half-tide basin was built in front of the wet dock.",
      "The basin lengthened the period each day during which ships could pass in and out."],
     "explain the purpose of the half-tide basin.",
     ["A tidal harbour empties as the tide falls, and the ships in it take the ground twice a day.",
      "The gates of a wet dock can be opened only while the water outside stands level with the water inside.",
      "Because a wet dock's gates open only at level water, an intermediate basin was built in front of it to lengthen the period each day during which ships could pass.",
      "At Liverpool a half-tide basin was built in front of the wet dock."],
     "C",
     "The goal asks what the basin was for, and only the choice joining the level-water restriction "
     "to the lengthened period of access explains it. Stating that the basin was built at Liverpool "
     "locates it without giving any purpose."),
]

DROPPED = {}
