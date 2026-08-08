#!/usr/bin/env python3
"""
Reading & Writing authored for Test 14.

All 81 items are original. The transcribed pool was spent by Test 8, and for
R&W authoring is in any case the safer route: a transcribed answer key has to
be re-derived by hand before it can be trusted (Test 5 shipped 6 wrong answers
in 81 that way). Every item below carries a `why` recording the reasoning that
produced the key AND the reason the strongest distractor fails - that record IS
the verification, so no key exists here without one.

Rationales name options by their CONTENT, never by letter, so balance_rw.py is
free to rotate every question when it evens out the key distribution. (The
letter check in balance_rw.py fires on a standalone capital A/B/C/D, so no
rationale here opens a sentence with the article "A" either.)

Writing-domain choices are worded, never bare punctuation. Test 8 shipped
Boundaries items whose four options were ", " / "; " / ": " / " and ", which a
student sees as four empty rows; the real test repeats the words on either side
of the blank inside every option so each choice reads as the resulting
sentence. Every Boundaries item here is written that way from the start.
Form/Structure items whose options are genuinely words ("has" / "have",
"that" / "those") stay as words, which is also how the real test presents them.

Topics were checked by grep against rw_test8.py, rw_test9.py, rw_test10.py,
rw_test11.py and rw_test12.py in full, and nothing is reused. The subjects here
are: sandgrouse belly feathers, termite mound ventilation, dung-beetle Milky Way
orientation, the Persian yakhchal, Silbo Gomero, shape-note singing, Isotype
pictograms, dark-fibre acoustic sensing, nixtamalisation, super-black bird-of-
paradise plumage, the nilometer, the caravanserai, shellac, the iron bloom, a
ship's draught, the Icelandic turf house, the Athenian kleroterion, the Plimsoll
line, carillon tuning, Nicaraguan Sign Language, the Osborne firefinder,
Cahokia, owl wing serrations, the Cairo Geniza, the acequia, the mirror box,
Egyptian blue, canopy lidar, fig wasps, the Roquefort caves, wood frogs, Tyrian
purple, company scrip, cassowary seed dispersal, retrieval practice, the Indus
script, the kilogram redefinition, leap seconds, snow algae, the Chappe
semaphore, double-entry bookkeeping, gecko setae, speleothems, garum, Swahili
coral-rag towns, the Hardanger fiddle, varved lake sediments, flax retting,
railway time, Thonet bentwood, hummingbird torpor, the archerfish, the equation
of time, the Jacquard loom, diatom frustules, Mughal squirrel-hair brushes, the
Beaufort scale, alpine common grazing, Byzantine gold tesserae, bar-headed
geese, rotating savings clubs, Fayum encaustic portraits, the Great
Trigonometrical Survey, sand-battery heat storage, colour terms, sloth fur
algae, the penny post, flywheel storage, change blindness, woad and indigo,
spider silk glands, the McGurk effect, Conlon Nancarrow, Nan Madol, the
California condor, buzz pollination, Harry Beck's Underground diagram, the
Herculaneum scrolls, the American chestnut, Exchequer tally sticks and the iron
pillar at Delhi.

Block counts (fixed by the assembler's quota, 3 modules x 27):
    Words in Context 15, Text Structure and Purpose 6,
    Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
    Boundaries 12, Form, Structure, and Sense 9, Transitions 9,
    Rhetorical Synthesis 9                                        = 81
"""

SOURCE = "AUTHORED-T14"
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
     "A male sandgrouse may nest fifty kilometres from the nearest water. Each morning he flies to "
     "a waterhole, wades in and rocks his body from side to side; the feathers of his belly take up "
     "water the way a wick takes up oil, and he flies home with it still held there. The chicks "
     "drink by drawing the feathers through their beaks. The plumage of the belly is therefore best "
     "understood as a _____ rather than as insulation.",
     ["vessel", "shield", "decoration", "signal"], "A",
     "The belly feathers hold water across fifty kilometres and give it up to the chicks, which is "
     "the work of something that carries a liquid. The 'shield' option describes keeping something "
     "out, which is the insulating function the sentence explicitly sets aside."),

 wic("W2",
     "The colony does not live in the mound. The termites are in a nest below ground and the tower "
     "above it is hollow and largely empty. Sun on one face and shade on the other drive air up one "
     "set of channels and down another all day, carrying off the carbon dioxide that the colony and "
     "its fungus gardens produce. The tower is less a dwelling than a _____.",
     ["lung", "granary", "monument", "fortress"], "A",
     "The tower's described job is to move air in and out so that waste gas leaves and fresh air "
     "arrives, which is what a breathing organ does. The 'fortress' option names a defensive "
     "structure, and the passage attributes no protective role to the tower at all."),

 wic("W3",
     "A ball-rolling dung beetle that stops on top of its ball and turns a slow circle is taking a "
     "reading. On a moonless night the beetle still holds a straight line, and in a planetarium the "
     "line follows the band of the Milky Way once every other light is switched off. What the animal "
     "needs is not a destination but a _____: any fixed line leading away from the dung pile will "
     "serve.",
     ["bearing", "landmark", "shelter", "companion"], "A",
     "The sentence itself says that any fixed line away from the pile will do, so what the beetle "
     "takes from the sky is a direction to hold rather than a place to reach. The 'landmark' option "
     "names a particular feature to head towards, which is the destination the sentence rules out."),

 wic("W4",
     "A yakhchal is a mud-brick cone raised over a deep pit in country where the air temperature "
     "seldom drops to freezing. Water led into shallow channels on a clear winter night loses heat "
     "to the sky faster than the air can put it back, and a thin sheet of ice forms; the ice is cut "
     "and packed into the pit, where metre-thick walls and a vent at the apex hold it into high "
     "summer. The building does not make cold. It _____ it.",
     ["hoards", "circulates", "produces", "predicts"], "A",
     "Ice made outside on winter nights is packed away and kept for months, so what the structure "
     "does is store what has already been made. The 'circulates' option fastens on the vent, but "
     "moving air through the chamber is a means of keeping the store, not what the building is for."),

 wic("W5",
     "Silbo Gomero is Spanish carried on a whistle. The whistler reduces every vowel to one of two "
     "pitches and every consonant to a break or a slide between them, and the result crosses a "
     "ravine that would swallow a shout. Most of the sound of the language is thrown away in the "
     "process; what survives is just enough for a listener who knows the subject under discussion to "
     "_____ the rest.",
     ["reconstruct", "translate", "amplify", "record"], "A",
     "Since most of the acoustic detail is discarded, the listener has to build the missing part "
     "back from context, which is what the sentence describes. The 'translate' option would require "
     "a second language, and the passage says the whistle is Spanish."),

 wic("W6",
     "A shape-note tune book prints each degree of the scale as a triangle, oval, square or diamond, "
     "so a singer reads the shape and not the position on the staff. At an all-day singing the four "
     "parts sit in blocks facing one another around an open square and sing to each other rather "
     "than to an audience. The notation exists to make music _____ rather than to record any new "
     "sound: someone who had never seen a printed note could join a class on Monday and sing a "
     "fuguing tune by Friday.",
     ["quick to learn", "pleasant to look at", "cheap to print", "difficult to imitate"], "A",
     "The evidence offered in the same sentence is a beginner singing a fuguing tune within the "
     "week, which is a claim about how fast the system can be picked up. The 'cheap to print' option "
     "is plausible for a tune book but has no support anywhere in the passage."),

 wic("W7",
     "Otto Neurath's picture statistics use one small figure to stand for a fixed number of people "
     "and then repeat the figure; nothing is ever drawn larger. Twice as many figures means twice as "
     "many people, and the eye counts instead of judging an area. The method was designed to keep a "
     "chart _____ for a reader with no training in reading charts at all.",
     ["unambiguous", "decorative", "compact", "provisional"], "A",
     "Counting repeated figures replaces the guesswork of comparing areas, so the design removes "
     "the chance of misreading the quantity. The 'compact' option runs against the method, since "
     "repeating a figure for every unit makes a chart longer rather than smaller."),

 wic("W8",
     "Telecommunications firms laid far more optical fibre than the traffic required, and much of it "
     "has never carried a call. A pulse of light sent down one of these idle strands returns "
     "slightly altered wherever the glass is stretched or squeezed, so a single fibre under a city "
     "street reports every heavy lorry and every small earthquake along its length. Cable laid for "
     "one purpose has turned out to be _____ as a seismic array.",
     ["serviceable", "expendable", "unnecessary", "conspicuous"], "A",
     "The fibre does real work in its second role, detecting lorries and earthquakes along its "
     "whole length, so the blank has to say that it is fit for that use. The 'expendable' option "
     "says the cable could be given up, which is the opposite of the value the sentence is claiming "
     "for it."),

 wic("W9",
     "Maize simmered in water with wood ash or slaked lime and left to steep loses its skin and "
     "smells quite different afterwards. It also releases niacin that the untreated grain holds in a "
     "form the human gut cannot take up. Populations that adopted maize without the ash treatment "
     "suffered pellagra; those that took the treatment with it did not. The steeping is therefore "
     "not a matter of taste but of _____.",
     ["nutrition", "convenience", "storage", "ceremony"], "A",
     "The treatment frees a vitamin the body could not otherwise use, and the passage ties skipping "
     "it to a deficiency disease, so what is at stake is what the food supplies. The 'storage' "
     "option is never raised in the passage, which says nothing about keeping the grain."),

 wic("W10",
     "Feathers on the display patch of some birds of paradise send back less than a thousandth of "
     "the light that falls on them, which makes them darker than any black paint. The barbules carry "
     "no unusual pigment; they stand up from the shaft in a forest of curved spikes that sends a ray "
     "bouncing from spike to spike until it is absorbed. The blackness is _____ rather than "
     "chemical.",
     ["structural", "seasonal", "accidental", "inherited"], "A",
     "The passage rules out pigment and puts the effect down to the shape and arrangement of the "
     "barbules, so the blank names an effect of physical form. The 'accidental' option denies design "
     "in an arrangement the passage presents as an ordered forest of spikes doing a specific job."),

 wic("W11",
     "A nilometer is a stepped shaft cut down to river level with a scale carved on its wall. The "
     "reading taken as the flood rose changed nothing about the flood, but it fixed the tax that "
     "would be demanded on a harvest still months away, and it told the keepers of the granaries how "
     "much of last year's grain to hold back. The instrument was less a scientific device than an "
     "_____ one.",
     ["administrative", "ornamental", "experimental", "astronomical"], "A",
     "The readings set tax rates and granary policy, which is the work of government rather than of "
     "enquiry. The 'experimental' option would mean the shaft was used to test something, and the "
     "passage says outright that the reading changed nothing about the river."),

 wic("W12",
     "A caravanserai stands one day's march from the next, with a single gate, a courtyard for the "
     "animals and small rooms around it for the men. Merchants who had never met slept there beside "
     "their goods, and the keeper answered to the ruler who had built the place. Such buildings made "
     "a long journey possible not by shortening it but by making each night _____.",
     ["predictable", "profitable", "shorter", "solitary"], "A",
     "Fixed spacing, a single guarded gate and a keeper answerable to the ruler all remove the "
     "uncertainty of where and how a traveller will pass the night. The 'profitable' option "
     "introduces gain, and nothing in the passage says the halts made money for the merchants."),

 wic("W13",
     "Shellac is scraped off the branches where a scale insect has secreted it, dissolved in alcohol "
     "and brushed on. It dries in minutes, polishes to a mirror, and can be lifted again with more "
     "alcohol by anyone who wants to begin over. Conservators value the finish precisely because it "
     "is _____: nothing done to a surface in shellac forecloses what a later hand may decide to do.",
     ["reversible", "durable", "inexpensive", "waterproof"], "A",
     "The colon spells the blank out - the finish can be taken off again, so no decision made in it "
     "is final. The 'durable' option praises a coating for lasting, which is very nearly the "
     "opposite of the property the sentence singles out."),

 meaning("W14",
     "Iron smelted in a bloomery never melts. What is raked out of the furnace is a spongy mass of "
     "metal shot through with slag, and the smith drives the slag out by hammering the <u>bloom</u> "
     "while it is still glowing, folding it over and striking it again until the iron is solid all "
     "the way through.",
     "bloom",
     ["A flower at its fullest opening.",
      "A spongy mass of iron taken from a furnace.",
      "A period of rapid growth or prosperity.",
      "A dull film that forms on the surface of a varnish."],
     "B",
     "The passage defines the word in the sentence before it uses it: the spongy mass of metal and "
     "slag raked out of the furnace. The dull-film sense is a genuine meaning of the word but "
     "belongs to varnish and chocolate, not to something a smith hammers."),

 meaning("W15",
     "The channel was dredged to five metres, and the coasters that had worked the port for a "
     "century could still use it. The new container ships could not: a hull of that size needs seven "
     "metres beneath it, and a ship that touches bottom at low water is worth nothing to an owner. "
     "<u>Draught</u>, not the length of the quay, decided which ports survived the change.",
     "Draught",
     ["A current of cold air moving through a room.",
      "The depth of water a vessel needs in order to float.",
      "A first version of a written document.",
      "A single act of swallowing a liquid."],
     "B",
     "The word is used for the seven metres a big hull needs beneath it, measured against a channel "
     "dredged to five. The current-of-air sense is the commonest meaning of the word in ordinary "
     "speech but has nothing to do with the depth of a dredged channel."),

 # --------------------------------------------- Text Structure and Purpose (6)
 tsp("S1",
     "Iceland had lost most of its woodland within a century of settlement, and bare stone holds no "
     "heat. Builders raised their walls instead from blocks of turf cut in a herringbone pattern and "
     "stacked with the grass still living in them. <u>A wall built this way settles as the turf "
     "beneath compresses, so the roof timbers &mdash; scarce, salvaged, often driftwood &mdash; had "
     "to be taken down and reset every few decades.</u> Houses were rebuilt on the same spot so "
     "often that the mound under an old farm can be several metres deep.",
     "Which choice best describes the function of the underlined sentence in the text as a whole?",
     ["It identifies a consequence of the building method that accounts for the pattern described next.",
      "It explains why woodland disappeared from Iceland after settlement.",
      "It argues that turf was a poorer building material than stone.",
      "It describes the way turf blocks were cut for the walls."],
     "A",
     "Settling walls force the roof to be reset, and repeated rebuilding on one spot is exactly what "
     "produces the deep farm mound in the closing sentence. The disappearance of the woodland is "
     "stated in the first sentence and is background, not the work the underlined sentence does."),

 tsp("S2",
     "An Athenian jury was not chosen by anybody. Each citizen willing to serve pushed a bronze "
     "ticket into one of the columns of slots cut in a stone slab, and a tube fixed at the side was "
     "loaded with black and white balls. A crank let one ball fall at a time; a white ball sent a "
     "whole row of ticket-holders onto the jury and a black one sent the row home. The machine "
     "settled nothing about who was fit to judge. It settled only that no official had picked them.",
     "Which choice best states the main purpose of the text?",
     ["To describe a mechanism and identify the narrow question it was built to settle.",
      "To argue that Athenian juries reached sounder verdicts than modern ones.",
      "To trace the growth of Athenian democracy across the fifth century.",
      "To explain how the bronze tickets were manufactured and inscribed."],
     "A",
     "Most of the text is the working of the slab, the tube and the crank, and the last two "
     "sentences say precisely what the device did and did not decide. Nothing compares Athenian "
     "verdicts with modern ones, so the option about sounder verdicts asserts a claim the text never "
     "makes."),

 tsp("S3",
     "An overloaded ship rides low, and a sea that would run along the deck of a light vessel comes "
     "aboard instead. <u>The mark painted on the hull is not a limit on cargo but a limit on how "
     "deep the hull may sit in the water.</u> The same ship may load until the line reaches the "
     "surface in one sea and must stop short of it in another, because water of a different "
     "temperature and salinity lifts a hull differently. The tonnage the mark permits therefore "
     "changes with the voyage.",
     "Which choice best describes the function of the underlined sentence?",
     ["It draws a distinction that the rest of the text goes on to develop.",
      "It concedes that shipowners frequently ignored the mark.",
      "It explains why timber is a particularly dangerous cargo to carry.",
      "It describes the procedure by which the mark is painted on a hull."],
     "A",
     "Separating a limit on immersion from a limit on cargo is what makes the following sentences "
     "intelligible, since the permitted tonnage then varies with the water while the line stays put. "
     "Nothing in the text reports owners disregarding the mark, so there is no concession being "
     "made."),

 tsp("S4",
     "A carillon bell is cast too thick on purpose and then cut away. Any bell sounds five notes at "
     "once, and the intervals between them are fixed by the profile of the wall rather than by the "
     "size of the bell. The founder mounts the casting on a lathe and turns metal off the inside, "
     "testing after every pass, until the five partials fall into tune with one another. Metal taken "
     "off cannot be put back, so the whole procedure runs one way only, from a sharp bell towards a "
     "flat one.",
     "Which choice best describes the overall structure of the text?",
     ["It states an unexpected practice, explains the acoustics behind it, and notes a constraint the practice imposes.",
      "It compares carillon bells with the bells used in other instruments.",
      "It follows a single founder through the casting of one bell.",
      "It argues that machine tuning has displaced the founder's ear."],
     "A",
     "The text opens with the odd business of casting a bell too thick, explains it by way of the "
     "five partials, and closes on the one-way nature of removing metal. No other kind of bell is "
     "ever mentioned, so nothing is being set beside anything else."),

 tsp("S5",
     "Deaf children in Nicaragua were taught at home in isolation until new schools brought several "
     "hundred of them together at the end of the 1970s. What each child arrived with was the set of "
     "gestures improvised inside one family, and no two sets had a grammar in common. <u>Within a "
     "few years the youngest pupils in the school were signing with regularities that the older "
     "pupils who had started the system never used.</u> Linguists who recorded both groups describe "
     "a language that was made rather than taught.",
     "Which choice best describes the function of the underlined sentence?",
     ["It presents the observation on which the text's closing claim rests.",
      "It questions whether the older pupils were signing at all.",
      "It explains why the children had previously been taught at home.",
      "It describes the recording methods the linguists used."],
     "A",
     "Younger children producing grammar their teachers and elders never used is the evidence for "
     "the final sentence's claim that the language was made rather than passed on. The older pupils "
     "are said to sign without those regularities, which is not the same as not signing."),

 tsp("S6",
     "A fire lookout does not report where a fire is. Standing at the middle of a circular map "
     "table, the watcher turns a sighting ring until the smoke sits on the crosshair and reads a "
     "bearing off the rim. That bearing is a line, not a point, and every burning acre along it "
     "fits the observation equally well. Only when a second tower on another summit sends in a "
     "bearing of its own does the crossing of two lines put the fire on the map.",
     "Which choice best states the main purpose of the text?",
     ["To explain why one lookout's observation cannot by itself locate a fire.",
      "To describe how a circular map table is constructed.",
      "To argue that lookout towers ought to be replaced by aircraft.",
      "To recount the history of fire lookouts in the mountain west."],
     "A",
     "Every sentence builds towards the point that a single bearing gives a line and that two are "
     "needed to fix a point. The construction of the table is mentioned only as far as the sighting "
     "ring and the rim, which serve the argument rather than being its subject."),

 # ----------------------------------------------- Central Ideas and Details (6)
 cid("C1",
     "Cahokia, on the flood plain opposite present-day St Louis, held more people around 1100 than "
     "London did. Its central mound was raised basketload by basketload and covers more ground than "
     "the Great Pyramid. Within two centuries the plazas stood empty. Excavation has turned up no "
     "siege line, no mass grave and no single burnt layer; what it shows is a city that drew people "
     "in from several regions and then, across decades, let them go again.",
     "Which choice best states the main idea of the text?",
     ["Cahokia was destroyed in a war whose traces have not yet been located.",
      "Cahokia was a large city that emptied gradually rather than in a single catastrophe.",
      "Cahokia's central mound is the largest earthwork ever raised anywhere.",
      "Cahokia's population was drawn entirely from the surrounding flood plain."],
     "B",
     "The absence of a siege line, a mass grave or a burnt layer rules out a sudden end, and the "
     "closing clause puts the emptying across decades. The war option is what that same list of "
     "negative findings is there to exclude."),

 cid("C2",
     "The leading edge of an owl's outermost primary carries a row of stiff combs, the trailing edge "
     "is fringed into separate filaments, and the upper surface is covered in a velvet pile. Each of "
     "the three breaks up the sheet of turbulent air that would otherwise roll off the wing and "
     "hiss. Recordings place the sound of an owl's wingbeat below the hearing threshold of the mice "
     "it hunts. Fast owls that take insects on the wing in open air have none of the three.",
     "Which choice best states the main idea of the text?",
     ["Three feather structures work to quiet an owl's wing rather than to make its flight faster.",
      "Owls hear considerably better than the mice on which they prey.",
      "All owls fly more quietly than other birds of comparable size.",
      "The velvet pile on the wing keeps an owl warm in cold weather."],
     "A",
     "All three structures are said to break up the turbulence that would make noise, and the owls "
     "that lack them are the fast ones, which separates quiet from speed. The claim that every owl "
     "flies quietly is contradicted by the last sentence, where a whole group of owls has none of "
     "the features."),

 cid("C3",
     "For the better part of a thousand years a storeroom in a Cairo synagogue took in every scrap "
     "of paper the congregation could not bring itself to destroy, since anything that might carry "
     "the name of God was not to be thrown away. What accumulated was not a library. Beside prayer "
     "books lie a merchant's bill of lading, a schoolboy's alphabet, a wife's letter asking her "
     "husband to come home from India, and a shopping list. The collection is valuable to historians "
     "for exactly the reason it was never valuable to its owners.",
     "Which choice best states the main idea of the text?",
     ["The ordinary documents nobody thought worth keeping are what make the storeroom historically valuable.",
      "The congregation assembled the storeroom deliberately as a research library.",
      "Most of the documents in the storeroom turn out to be prayer books.",
      "The documents were preserved because of their commercial importance."],
     "A",
     "The passage lists bills, exercises, letters and a shopping list, then says the material is "
     "valuable to historians for the very reason it had no value to the people who left it. The "
     "research-library option is denied outright by the sentence saying that what accumulated was "
     "not a library."),

 cid("C4",
     "An acequia is a ditch and also the body of people whose fields it waters. The mayordomo sets "
     "the rotation, and every household owes days of labour on the annual cleaning in proportion to "
     "the water it draws. In a dry year the shortage is shared rather than allocated by seniority: "
     "every turn is shortened by the same fraction. Villages that have run the same ditch for three "
     "centuries have put almost none of this in writing.",
     "According to the text, how is a shortage of water handled?",
     ["Water goes first to the households holding the oldest rights.",
      "Every household's turn is cut back so that the shortfall falls on all of them.",
      "The mayordomo buys water from a neighbouring ditch association.",
      "Households that supplied the most labour receive the most water."],
     "B",
     "The text states the rule directly: the shortage is shared and every turn is shortened by the "
     "same fraction. Allocation by seniority is named in that same sentence as the thing the "
     "practice is not."),

 cid("C5",
     "A limb that has been amputated can go on hurting, and patients often describe the pain as a "
     "hand clenched too tightly to open. Vilayanur Ramachandran stood a mirror upright between a "
     "patient's arms so that the reflection of the intact hand appeared where the missing one had "
     "been. Patients asked to open both hands watched the missing hand open. For some the cramp "
     "eased at once, and for a few it did not come back.",
     "Which choice best states the main idea of the text?",
     ["The mirror restored feeling to the amputated limb itself.",
      "Giving patients a visual image of the missing hand moving relieved pain for some of them.",
      "Phantom pain is caused by damage to the nerve endings that remain in the stump.",
      "Every patient who used the mirror was permanently cured of the pain."],
     "B",
     "The mirror supplies a picture of the absent hand opening, and the closing sentence reports "
     "relief for some patients and lasting relief for a few. The permanent-cure option overstates "
     "those same two qualifications, which are the point of the sentence."),

 cid("C6",
     "Egyptian blue is manufactured rather than mined: sand, lime, a copper salt and natron heated "
     "together until they form crystals of calcium copper silicate. It was made for three thousand "
     "years, then not made at all, and the recipe was lost for fifteen centuries. It also has a "
     "property its makers cannot have known about &mdash; struck by red light it re-emits in the "
     "infrared &mdash; so conservators now photograph apparently blank stone in the dark and find "
     "the traces of decoration that nobody can see.",
     "Which choice best states the main idea of the text?",
     ["A manufactured ancient pigment now reveals lost decoration because of a property its makers could not have known it had.",
      "Egyptian blue was the first pigment ever manufactured instead of mined.",
      "The recipe for Egyptian blue has still not been recovered by chemists.",
      "Conservators can identify Egyptian blue by its colour alone."],
     "A",
     "The passage pairs the made-not-mined pigment with an infrared emission its makers could not "
     "have known about and the invisible decoration it now uncovers. Nothing claims priority over "
     "all other pigments, which the first-ever option would require."),

 # ---------------------------------------------------- Command of Evidence (9)
 coe("E1",
     "Aircraft flying over the Pet&eacute;n forest fire laser pulses through gaps in the canopy and "
     "time their return, building a model of the ground under the trees. Archaeologist Hana Duarte "
     "argues that the Maya population of the region has been badly underestimated, because survey on "
     "foot could record only what stood in ground already cleared.",
     "Which finding, if true, would most directly support Duarte's argument?",
     ["The laser models show house platforms, causeways and field walls spread across areas that ground survey had recorded as empty forest.",
      "The largest pyramids in the region were mapped by ground survey several decades ago.",
      "Laser pulses do not reach the ground where the canopy is completely unbroken.",
      "Many lowland Maya cities were abandoned during the ninth century."],
     "A",
     "Structures standing thick in ground that foot survey wrote off as empty is exactly what an "
     "undercount caused by cleared-ground sampling predicts. The mapping of the largest pyramids "
     "shows what the old method could find and says nothing about what it missed."),

 coe("E2",
     "A fig is an inflorescence turned outside in, and each species is entered by a wasp of its own "
     "through a hole barely wide enough to admit her. Biologist Tomas Oyelaran argues that the tree "
     "actively restrains cheating &mdash; wasps that lay eggs in every flower and carry no pollen.",
     "Which finding, if true, would most directly support Oyelaran's argument?",
     ["Figs entered by wasps that laid eggs without depositing pollen are dropped from the tree before the eggs can mature.",
      "A wasp that enters a fig loses her wings at the entrance and never leaves it.",
      "Fig trees of different species flower at different times of the year.",
      "Some wasps enter figs of a species other than their own and die inside them."],
     "A",
     "Aborting the fruit destroys the offspring of a wasp that pollinated nothing, which is a "
     "sanction imposed by the tree and falls only on cheats. Losing her wings at the entrance is a "
     "cost the wasp pays whether she pollinates or not, so it cannot discourage cheating."),

 coe("E3",
     "The cheeses ripen in caves in a limestone scree, where cool air moves constantly through the "
     "fissures. Cheesemaker Elodie Ferrand maintains that the character of the cheese comes from the "
     "airflow and humidity of the caves rather than from any strain of mould peculiar to them.",
     "Which finding, if true, would most directly support Ferrand's claim?",
     ["Cheese inoculated with mould grown in a laboratory and ripened in the caves is indistinguishable from cheese made the traditional way, while the same mould used in a warehouse is not.",
      "The mould growing in the caves has been given a species name of its own.",
      "The milk for the cheeses comes from a single local breed of sheep.",
      "The caves have been used for ripening cheese since the Middle Ages."],
     "A",
     "Swapping the mould changes nothing while moving the cheese out of the caves changes "
     "everything, which isolates the cave conditions as the cause. The mould having its own species "
     "name points towards the explanation the claim is arguing against."),

 coe("E4",
     "A wood frog in midwinter has ice between its organs, no heartbeat and no measurable breathing, "
     "and thaws in spring without injury. Physiologist Karin Aalto argues that survival depends on "
     "the frog flooding its cells with glucose before the freeze rather than on any inherent "
     "toughness of the tissues.",
     "Which finding, if true, would most directly support Aalto's argument?",
     ["Frogs whose livers were blocked from releasing glucose died at temperatures that untreated frogs survived unharmed.",
      "Wood frogs begin to freeze at a higher temperature than most other amphibians do.",
      "Wood frogs range further north than any other North American frog.",
      "Frozen wood frogs can be thawed and refrozen several times in one winter."],
     "A",
     "Removing the glucose and nothing else turns a survivable freeze into a lethal one, which is "
     "what a glucose-dependent mechanism predicts. The northern range shows only that the animal "
     "endures cold, which is the fact both explanations are trying to account for."),

 coe("E5",
     "Ten thousand murex snails yield a few grams of dye, and the colour deepens with age instead of "
     "fading. Historian Silvia Moretti argues that the price of Tyrian purple was set by the labour "
     "of collection rather than by any secret held by the dyers of Tyre.",
     "Which finding, if true, would most directly support Moretti's argument?",
     ["Workshops far from Tyre produced dye of the same quality as soon as the snails were available to them, and charged as much for it.",
      "Roman law reserved the deepest shades of purple for the emperor and his household.",
      "The chemistry of the dye was not worked out until the twentieth century.",
      "Vats of decomposing snails smelled so foul that dyeworks were kept outside the city walls."],
     "A",
     "Distant workshops matching the quality shows there was no proprietary knowledge to hold, "
     "while their equally high prices point at the shared cost of gathering snails. The law "
     "reserving purple for the emperor bears on demand rather than on where the cost came from."),

 coe("E6",
     "Nineteenth-century mining companies commonly paid part of a wage in tokens that could be spent "
     "only at the company store. Economic historian Lewis Adeyemi argues that the practice worked "
     "chiefly as a means of charging higher prices, not as a convenience in districts where coin was "
     "genuinely scarce.",
     "Which finding, if true, would most directly support Adeyemi's argument?",
     ["Where miners could reach an independent shop, company-store prices matched it; where they could not, the same goods cost a third more.",
      "Coin really was scarce in the remoter mining districts.",
      "Company stores routinely extended credit between paydays.",
      "Tokens were struck in denominations smaller than the smallest circulating coin."],
     "A",
     "Prices that rise precisely where the miner has nowhere else to spend show the tokens being "
     "used to extract more, not to solve a shortage of coin. The scarcity of coin is the rival "
     "explanation stated plainly, so confirming it works against the claim rather than for it."),

 coe("E7",
     "Several rainforest trees in northern Queensland bear fruit the size of a fist, with a stone "
     "too large for any other animal in the forest to swallow whole, and a seed that germinates "
     "poorly where it falls. Ecologist Marion Teo argues that these trees now depend on the "
     "cassowary for dispersal to a degree that puts them at risk.",
     "Which finding, if true, would most directly support Teo's argument?",
     ["Seedlings of these trees are found at any distance from a parent tree only in forest where cassowaries still range, and nowhere else.",
      "Cassowary numbers have fallen as roads have been cut through the forest.",
      "The fruit of these trees is brightly coloured when ripe.",
      "Cassowaries also eat fungi, insects and small animals."],
     "A",
     "Seed arriving away from the parent only where the bird survives ties dispersal to the "
     "cassowary and to nothing else. Falling cassowary numbers describe the threat but leave open "
     "whether the trees actually need the bird, which is the disputed half of the claim."),

 coe("E8",
     "Students given a passage to learn and then asked to write out what they remember outperform "
     "students who simply read it again, when both groups are tested a week later. Psychologist Dev "
     "Raman argues that the benefit comes from the act of retrieval itself and not from the extra "
     "exposure to the material that a recall attempt happens to provide.",
     "Which finding, if true, would most directly support Raman's argument?",
     ["Students whose recall attempts largely failed, and who were never shown the passage again afterwards, still outperformed the rereaders a week later.",
      "Students who reread a passage four times felt more confident about it than students who tried to recall it.",
      "Attempting recall took less time than rereading the passage did.",
      "Both groups remembered more immediately after studying than they did a week later."],
     "A",
     "Recall that fails supplies no exposure at all, so an advantage that survives it must come from "
     "the attempt rather than from seeing the material again. Greater confidence among rereaders "
     "concerns how students feel and leaves the source of the memory benefit untouched."),

 coe("E9",
     "The Indus valley seals carry short strings of signs that nobody can read, and it has been "
     "argued that they are not writing at all but emblems of office or ownership. Computational "
     "linguist Priya Raghavan maintains that the sequences behave statistically like a script "
     "encoding a language.",
     "Which finding, if true, would most directly support Raghavan's claim?",
     ["The probability of one sign following another falls in the range found in known scripts and far outside the range found in non-linguistic sign systems such as heraldic emblems.",
      "The seals were pressed into clay to seal bundles of goods for transport.",
      "Fewer than five hundred distinct signs have been catalogued in total.",
      "The longest sequence yet recovered contains seventeen signs."],
     "A",
     "Sign-to-sign transition probabilities matching scripts and missing the emblem systems is a "
     "measurable property of language, which is what the claim asserts. Using the seals to close "
     "bundles of goods is equally consistent with emblems of ownership."),

 # -------------------------------------------------------------- Inferences (6)
 inf("I1",
     "For 130 years the kilogram was a cylinder of platinum and iridium kept in a vault outside "
     "Paris, and every other kilogram in the world was a copy of it. Weighed against its own "
     "official copies over the decades, the cylinder drifted from them by a few tens of micrograms. "
     "Nothing could be said about which object had changed, because the cylinder defined the unit: "
     "whatever it weighed was a kilogram. The drift could therefore be detected but not _____",
     ["attributed to any particular object.",
      "measured with any accuracy at all.",
      "reported to the other national laboratories.",
      "reproduced in a second experiment."],
     "A",
     "Weighing shows only that the cylinder and its copies disagree, and the definition removes any "
     "standard against which the cylinder itself could be judged to have moved. The passage says "
     "the drift amounted to a few tens of micrograms, which means it was measured perfectly well."),

 inf("I2",
     "An atomic clock keeps a second defined by a transition in caesium, and that interval does not "
     "vary. The rotation of the Earth does vary: tides, the movement of the atmosphere and the slow "
     "rebound of land once buried under ice all change the length of a day by a millisecond or two. "
     "Civil time is held in step with the sky by inserting an extra second whenever the two have "
     "drifted a second apart. That these insertions are needed at unpredictable intervals shows that "
     "what is irregular is _____",
     ["the caesium transition on which the second is defined.",
      "the rotation of the Earth.",
      "the tides raised by the moon and nothing else.",
      "the accuracy of the clocks making the comparison."],
     "B",
     "The passage states that the atomic second does not vary and that the day does, so the "
     "unpredictable gap between them has to come from the turning Earth. Tides are offered as one "
     "cause among three, so singling them out as the whole story goes beyond the text."),

 inf("I3",
     "Fresh snow throws back most of the sunlight that lands on it. The alga that turns high summer "
     "snowfields pink is dark, and where it blooms the surface takes in light that would otherwise "
     "have been reflected away. The liquid water that results carries the nutrients the alga needs "
     "in order to grow. A bloom on a snowfield is therefore likely to _____",
     ["slow the melting of the snow beneath it.",
      "hasten the melting of the snow and, in doing so, favour its own growth.",
      "die back as soon as meltwater appears on the surface.",
      "appear only in years when snowfall has been unusually heavy."],
     "B",
     "Darkening the surface means more absorbed sunlight and faster melting, and the meltwater is "
     "said to bring the alga the nutrients it needs. Slowing the melt is the opposite of what "
     "replacing reflective white snow with a dark bloom would do."),

 inf("I4",
     "Chappe's towers stood on hilltops within sight of one another, each carrying a pair of jointed "
     "arms that a keeper could set to one of ninety-eight positions. A message from Paris to Lille "
     "passed through twenty-two stations in about ten minutes, and no keeper along the way knew what "
     "he was passing, since the code book was kept only at the two ends. On a foggy day, however, "
     "the line _____",
     ["carried messages more slowly than a mounted courier could.",
      "could not be operated at all.",
      "was read by keepers who had memorised the code.",
      "reversed the direction in which its messages travelled."],
     "B",
     "Every link in the chain depends on one keeper seeing the arms of the next tower, so weather "
     "that hides them stops the system rather than delaying it. The slower-than-a-courier option "
     "assumes messages still got through, which sight-line signalling in fog does not allow."),

 inf("I5",
     "In a double-entry ledger every transaction is written twice, once as a debit and once as a "
     "credit, and the two columns of the whole book must come to the same total. The system does "
     "nothing to stop a merchant inventing a sale outright, since a fiction entered on both sides "
     "balances as neatly as a fact. What the requirement reliably catches is _____",
     ["any deliberate misstatement of a firm's position.",
      "an entry made on one side of the book and not the other.",
      "a transaction recorded in the wrong currency.",
      "the theft of goods from a warehouse."],
     "B",
     "The only thing that puts the two totals out of agreement is an entry that fails to appear on "
     "both sides, which is what the balancing rule tests for. Deliberate misstatement is what the "
     "passage has just said the system cannot catch, because an invented sale balances too."),

 inf("I6",
     "A gecko's toe is covered in half a million hairs, each splitting at the tip into hundreds "
     "finer still, and the animal hangs from polished glass by one foot. The grip works on a dry "
     "surface, on a wet one and inside the vacuum of a test chamber, and the foot leaves no residue "
     "behind it. Suction and glue can both therefore be ruled out, which leaves an attraction "
     "arising simply from _____",
     ["the roughness of the surface being climbed.",
      "the extremely close contact of the split hairs with the surface.",
      "air pressure acting on the underside of the toe.",
      "a fluid secreted by the pads of the toe."],
     "B",
     "Working in a vacuum excludes air pressure and leaving no residue excludes an adhesive, so what "
     "remains is the intimate contact that the split hairs make with the surface. Roughness cannot "
     "be the answer when the passage has the animal hanging from polished glass."),

 # --------------------------------------------------------------- Boundaries (12)
 bnd("B1",
     "A stalagmite grows by a fraction of a millimetre a year, and each year's layer takes its "
     "chemistry from the water that dripped onto it. Cutting one down the middle exposes a record of "
     "local rainfall reaching back a hundred thousand _____ the layers can be dated from the uranium "
     "they contain to within a few decades.",
     ["years; the layers", "years, the layers", "years the layers", "years: and the layers"], "A",
     "Both halves of the sentence are complete statements and no conjunction joins them, so the "
     "semicolon is the only mark that will serve. Joining them with a comma alone, as the second "
     "option does, produces a splice."),

 bnd("B2",
     "Roman cooks reached for a sauce made by packing small fish in salt and leaving them in the sun "
     "for weeks on end. Because the fermentation broke the fish down completely and left a clear "
     "amber _____ garum tasted less of fish than of salt and of something nearer the savour of aged "
     "cheese.",
     ["liquid, garum", "liquid; garum", "liquid: garum", "liquid and garum"], "A",
     "The clause opening with 'Because' is dependent and has to be closed off with a comma before "
     "the main clause starts. Both the semicolon and the colon demand a complete sentence in front "
     "of them, and a dependent clause is not one."),

 bnd("B3",
     "Traders along the East African coast built in coral rag quarried from the living reef and cut "
     "while it was still soft enough to work. Kilwa, a town whose merchants handled the gold carried "
     "up from the Zimbabwe _____ a palace of more than a hundred rooms and a domed audience hall "
     "above the harbour.",
     ["plateau, had", "plateau; had", "plateau: had", "plateau had"], "A",
     "The appositive beginning 'a town whose merchants' was opened with a comma and must be closed "
     "with a matching comma before the verb belonging to the subject. Leaving the mark out runs the "
     "appositive straight into the predicate."),

 bnd("B4",
     "A Hardanger fiddle carries four extra strings that run under the fingerboard and are never "
     "touched by the bow. They are tuned to the notes of the tune being played and sound of their "
     "_____ the instrument gives the impression that a second fiddle is playing quietly in the next "
     "room.",
     ["own; the instrument", "own, the instrument", "own the instrument", "own: and the instrument"],
     "A",
     "Two independent statements meet at the blank with no conjunction between them, which is "
     "precisely the semicolon's work. The comma on its own splices them, and no punctuation at all "
     "leaves the two running together."),

 bnd("B5",
     "A lake fed by a glacier takes coarse silt through the summer melt and fine clay through the "
     "winter, and the two settle out as a pair of layers a practised eye can tell apart. Counting "
     "the pairs down a core gives a year-by-year _____ a bed of volcanic ash lying at one depth ties "
     "that count to a date established somewhere else entirely.",
     ["chronology; a bed", "chronology, a bed", "chronology the bed", "chronology: and a bed"], "A",
     "What stands on either side of the blank is a complete sentence, and nothing joins them, so the "
     "semicolon is required. The comma splices two independent clauses and the colon followed by "
     "'and' puts a conjunction where that mark does not take one."),

 bnd("B6",
     "Linen fibre lies in bundles inside the stem of the flax plant, held there by a gum that has to "
     "be rotted away before the fibre can be pulled free. Although a week in a slow river will "
     "loosen that gum in warm _____ the same stems left for a fortnight come apart in the hand.",
     ["weather, the same stems", "weather; the same stems", "weather: the same stems",
      "weather and the same stems"], "A",
     "'Although' opens a dependent clause, and a dependent clause standing in front of the main "
     "clause is separated from it by a comma. The semicolon would need an independent clause on both "
     "sides of it."),

 bnd("B7",
     "Before the railways every town kept its own noon, and a traveller reset a watch on arrival. "
     "Timetables for a line running east and west were unusable under that arrangement, so the "
     "companies imposed a single time along the whole of each _____ which Parliament made the legal "
     "standard for the country only forty years afterwards.",
     ["route, which", "route; which", "route: which", "route. Which"], "A",
     "The clause opening with 'which' is a non-essential relative clause and attaches to the main "
     "clause with a comma. The semicolon and the full stop both require an independent clause after "
     "them, and a relative clause is not independent."),

 bnd("B8",
     "Bending a chair leg out of steamed beech takes minutes, while carving the same leg takes "
     "hours. Michael Thonet, a cabinetmaker who patented the process in the 1850s and sold his "
     "chairs by the _____ the rods and screws unassembled, so that thirty-six chairs went into a "
     "crate a metre on each side.",
     ["million, shipped", "million; shipped", "million: shipped", "million shipped"], "A",
     "The appositive describing him opened with a comma and has to close with a comma before the "
     "verb that belongs to the subject. Any of the other marks would break the sentence at a point "
     "where the subject has not yet reached its verb."),

 bnd("B9",
     "A hummingbird would burn through its reserves overnight if it did nothing to stop it. On a "
     "cold night the bird lets everything slow down &mdash; body temperature, breathing, a heartbeat "
     "falling from twelve hundred beats a minute to about _____ and it takes twenty minutes of "
     "shivering at dawn to bring the bird out of the state.",
     ["fifty &mdash; and it takes", "fifty, and it takes", "fifty; and it takes", "fifty and it takes"],
     "A",
     "The list of things that slow down was opened with a dash, so a matching dash has to close it "
     "before the sentence resumes. Closing with a comma leaves the opening dash without its partner "
     "and blurs where the interruption ends."),

 bnd("B10",
     "An archerfish spits a jet of water at an insect resting on an overhanging leaf and knocks it "
     "down onto the surface. Because light bends as it leaves the water and the target is not "
     "actually where it appears to _____ the fish has to correct for the refraction before it "
     "fires.",
     ["be, the fish", "be; the fish", "be: the fish", "be and the fish"], "A",
     "The clause opening with 'Because' is dependent and needs a comma to close it before the main "
     "clause begins. The semicolon and the colon each require a complete sentence ahead of them, "
     "which a dependent clause is not."),

 bnd("B11",
     "A sundial and a clock agree with each other on only four days of the year. Two separate things "
     "are responsible for the _____ the ellipse of the Earth's orbit, which speeds the planet up as "
     "it passes nearest the sun, and the tilt of its axis, which swings the sun's apparent path "
     "north and south.",
     ["difference: the ellipse", "difference; the ellipse", "difference, and the ellipse",
      "difference the ellipse"], "A",
     "What comes before the blank is a complete sentence announcing two causes, and the colon is the "
     "mark that introduces the pair naming them. The semicolon would demand a full sentence after "
     "it, and the list that follows is not one."),

 bnd("B12",
     "A drawloom needed a boy sitting inside the frame to lift the warp threads by hand for every "
     "row of the pattern. Jacquard's mechanism replaced him with three _____ a loop of stiff cards "
     "punched with holes, a row of hooks that read the holes, and a cylinder pressing one card "
     "against the hooks for each pass of the shuttle.",
     ["things: a loop", "things; a loop", "things, and a loop", "things a loop"], "A",
     "The words before the blank form a complete sentence announcing three things, so the colon "
     "introduces the list that specifies them. The semicolon would require an independent clause "
     "after it, and a list of noun phrases is not one."),

 # ------------------------------------------------ Form, Structure, and Sense (9)
 fss("F1",
     "A diatom builds a shell of glass in two halves that fit together like a box and its lid, and "
     "no two species build the same pattern of pores. The collection of diatom slides prepared by "
     "the Victorian mounters, along with the notebooks that go with it, _____ still consulted by "
     "specialists today.",
     ["are", "have been", "were", "is"], "D",
     "The subject is the singular noun 'collection'; the interrupting phrase beginning 'along with' "
     "does not make a singular subject plural."),

 fss("F2",
     "The workshop's stock of squirrel-hair brushes was replaced early in the spring of that year. "
     "By the time the painter came to work on the border of the folio, the fine brush he had used "
     "for the faces _____ down to a stub.",
     ["wears", "had worn", "will wear", "is wearing"], "B",
     "The wearing down was finished before the painter reached the border, and reaching the border "
     "is itself in the past, so the past perfect is what places one past event before another."),

 fss("F3",
     "Francis Beaufort's scale describes the state of the sea rather than the wind itself, so an "
     "officer with no instrument aboard could still log a force. The purpose of the scale was to "
     "standardise what observers recorded, to make one ship's log comparable with another's and "
     "_____ a single number that could be entered in a column.",
     ["producing", "to produce", "it produces", "having produced"], "B",
     "The three items joined by 'and' all follow 'was to', and the first two are infinitives, so the "
     "third has to be an infinitive as well. The gerund and the finite clause both break the "
     "parallel structure."),

 fss("F4",
     "The alp above the village is grazed in common, and a household may send up only as many cows "
     "as it can feed on its own hay through the winter. The council inspects all four _____ hay "
     "lofts in the week before the herd goes up in June.",
     ["herdsmen", "herdsman's", "herdsmen's", "herdsmens'"], "C",
     "The lofts belong to all four herdsmen, so the noun has to be plural and possessive at once; "
     "because the plural is irregular and does not end in -s, the apostrophe comes before the s. The "
     "singular possessive would credit every loft to one herdsman."),

 fss("F5",
     "Gold tesserae are made by sinking gold leaf between two layers of glass, and the cubes are "
     "then set at slightly different angles so that the wall glitters as a viewer moves past it. "
     "Setting the tesserae into the wet plaster, _____",
     ["the angles were varied slightly from cube to cube.",
      "a slight variation was given to the angle of each cube.",
      "the mosaicists varied the angle of each cube slightly.",
      "there was a slight variation in the angle of each cube."],
     "C",
     "The opening participial phrase has to describe whoever was doing the setting, and only the "
     "option beginning with the mosaicists supplies that subject. Beginning with the angles has the "
     "angles setting the tesserae into the plaster."),

 fss("F6",
     "Bar-headed geese cross the Himalaya twice a year and beat their wings in air about a third as "
     "dense as the air at sea level. The oxygen-carrying capacity measured in the blood of these "
     "geese is markedly higher than _____ measured in the blood of related lowland species.",
     ["those", "that", "them", "which"], "B",
     "The pronoun stands in for the singular noun 'capacity', so the singular form is required; the "
     "plural form would need a plural antecedent and the sentence supplies none."),

 fss("F7",
     "A rotating savings club runs on nothing but the members' knowledge of one another: each pays "
     "in the same sum every week and each takes the whole pot in turn. Neither the organiser nor the "
     "members _____ any interest at all, and nothing is written down except the order of the turns.",
     ["receives", "receive", "has received", "is receiving"], "B",
     "With 'neither ... nor', the verb agrees with whichever subject stands nearer to it, and 'the "
     "members' is plural."),

 fss("F8",
     "The portraits were painted in coloured beeswax on thin wooden panels and bound into the "
     "wrappings over the face of the mummy. Each of the eleven panels recovered from the site _____ "
     "traces of the gilding that once surrounded the head.",
     ["show", "shows", "showing", "were showing"], "B",
     "'Each' is the subject and is singular; the prepositional phrase naming eleven panels does not "
     "change the number of the subject."),

 fss("F9",
     "Measuring an arc of the meridian across India took seventy years and cost more lives than most "
     "military campaigns of the period. The baseline laid out at Bangalore is one of the few "
     "nineteenth-century measurements that _____ been confirmed by satellite positioning to within a "
     "few centimetres.",
     ["has", "have", "having", "is"], "B",
     "The relative pronoun 'that' refers back to 'measurements', which is plural, so the plural verb "
     "is required; the singular would agree with 'one' instead, which is not what the clause "
     "describes."),

 # -------------------------------------------------------------- Transitions (9)
 trn("T1",
     "A silo of dry builder's sand heated by surplus wind electricity holds its heat for months, and "
     "the store costs a fraction of what a battery of the same capacity would. _____ the heat comes "
     "back out only as heat: nothing in the arrangement will drive a motor or charge a phone.",
     ["However,", "Therefore,", "Similarly,", "For instance,"], "A",
     "The restriction on what the stored energy can do cuts against the advantages just listed, so "
     "the transition has to mark a contrast rather than a consequence."),

 trn("T2",
     "Languages divide the spectrum differently, and a single word covering both blue and green is "
     "common enough across the world's languages. _____ speakers of such a language have no "
     "difficulty at all telling one shade from the other when they are asked to sort coloured chips.",
     ["Nevertheless,", "Consequently,", "Likewise,", "In short,"], "A",
     "Sorting the shades apart is the reverse of what a shared word might lead a reader to expect, "
     "so the transition concedes a contrast. Treating it as a consequence would make the single word "
     "the cause of the fine discrimination."),

 trn("T3",
     "A sloth's hair is grooved along its length, rainwater collects in the grooves, and algae grow "
     "in the water that stays there. The animal moves so slowly that the growth is never rubbed off "
     "against a branch. _____ a sloth in the wet season is faintly green, which in a canopy of "
     "leaves is not a bad colour to be.",
     ["As a result,", "By contrast,", "Nevertheless,", "In other words,"], "A",
     "The green tinge follows directly from algae growing undisturbed in the grooved hair, which is "
     "a cause-and-effect relation. Nothing in the second sentence works against the first, so the "
     "contrastive options misdescribe the link."),

 trn("T4",
     "Before 1840 the person who received a letter paid for it, on a scale that rose with the "
     "distance and with the number of sheets, and a letter refused at the door cost the Post Office "
     "the whole of the carriage. _____ Rowland Hill's uniform penny, prepaid by the sender and "
     "priced by weight alone, did away with the refusals and with the clerks who had calculated the "
     "charges.",
     ["By contrast,", "For instance,", "Moreover,", "Nonetheless,"], "A",
     "The prepaid flat rate is set against the old distance-and-sheets system in every particular, "
     "so the transition marks the opposition. The penny post is not an instance of the older "
     "arrangement, which is what the example transition would claim."),

 trn("T5",
     "A flywheel store spins a rotor in a vacuum on magnetic bearings and returns nine tenths of "
     "what is put into it within milliseconds of being asked, but it loses a few per cent of its "
     "charge every hour. _____ it is used to steady a grid over seconds and minutes rather than to "
     "carry power from one day to the next.",
     ["Accordingly,", "Nevertheless,", "By contrast,", "For example,"], "A",
     "Fast response together with hourly losses is exactly what confines the machine to short "
     "timescales, so the second sentence states a consequence. No contrast is being drawn, since the "
     "use described follows from both properties rather than defying either."),

 trn("T6",
     "Viewers watching a film shot in a caf&eacute; frequently fail to notice that the actor sitting "
     "opposite has been replaced between cuts by a different person in different clothes. _____ "
     "pedestrians who stop to give directions to a stranger often fail to notice when the stranger "
     "is swapped for another during a brief interruption.",
     ["Similarly,", "Consequently,", "By contrast,", "In short,"], "A",
     "The street experiment repeats the pattern of the film experiment in a different setting, so "
     "the transition signals a parallel. Neither result causes the other, which rules out the "
     "consequence transition."),

 trn("T7",
     "Woad and Indian indigo yield the same blue dye molecule, and a dyer cannot tell the finished "
     "cloth apart. _____ a woad crop gives perhaps a thirtieth of the dye that the same weight of "
     "indigo leaves does, which is why European woad growers spent two centuries petitioning for the "
     "import to be banned.",
     ["Even so,", "Therefore,", "Similarly,", "In particular,"], "A",
     "Identical dye from the two plants might suggest they compete on level terms, and the yield "
     "figure cuts against that, so the transition concedes a contrast. The consequence transition "
     "would make identical chemistry the reason for the thirtyfold difference in yield."),

 trn("T8",
     "A spider spins several different silks from separate glands and uses each of them for a "
     "different job. _____ the dragline that carries the animal's own weight is stiff and strong, "
     "while the capture spiral is stretchy enough to absorb the impact of a flying insect without "
     "throwing it back out of the web.",
     ["For example,", "Nevertheless,", "By contrast,", "Consequently,"], "A",
     "The dragline and the capture spiral are two instances of the different silks the first "
     "sentence describes, so the transition introduces examples. The contrast between those two "
     "silks lies inside the second sentence and is already carried by 'while'."),

 trn("T9",
     "Show a viewer a face mouthing 'ga' while the soundtrack plays 'ba', and the viewer hears "
     "'da', a syllable present in neither channel. Knowing about the illusion beforehand does not "
     "dispel it. _____ what reaches awareness is neither the sound nor the picture but a single "
     "settlement between the two.",
     ["In other words,", "Nevertheless,", "For instance,", "Meanwhile,"], "A",
     "The closing sentence restates in general terms what the demonstration has just shown, which is "
     "a restatement rather than a new case. It introduces no further example, which is what the "
     "instance transition would require."),

 # ------------------------------------------------------ Rhetorical Synthesis (9)
 syn("R1",
     ["Conlon Nancarrow wrote music for the player piano from the late 1940s onward.",
      "A player piano reads holes punched in a paper roll rather than a performer's hands.",
      "He punched the rolls himself, one hole at a time, on a machine he had built.",
      "The studies layer tempos in ratios such as 17:18 that no two human players can hold together.",
      "Only a handful of the studies were heard outside his Mexico City studio for thirty years."],
     "explain why Nancarrow wrote for the player piano.",
     ["Nancarrow wrote for the player piano from the late 1940s and punched every roll himself, one hole at a time.",
      "Because his studies layer tempos in ratios such as 17:18 that no two performers can hold together, Nancarrow wrote for a machine that reads punched holes instead of writing for players.",
      "Only a handful of Nancarrow's studies were heard outside his Mexico City studio for thirty years.",
      "A player piano reads holes punched in a paper roll rather than a performer's hands."],
     "B",
     "The goal asks for the reason behind the choice of instrument, and only the option that ties "
     "the impossible tempo ratios to a machine that needs no performer supplies one. The note about "
     "punching the rolls by hand describes his method without saying why players were ruled out."),

 syn("R2",
     ["Nan Madol is a complex of nearly a hundred artificial islets built in a lagoon off Pohnpei.",
      "Its walls are stacked from basalt columns, some of them weighing several tonnes.",
      "The basalt outcrops lie on the far side of the island from the site.",
      "The builders had no wheel, no draught animal and no metal tool.",
      "Oral tradition on Pohnpei says the stones were flown into place by sorcery."],
     "emphasise the practical difficulty the builders faced.",
     ["Nan Madol is a complex of nearly a hundred artificial islets built in a lagoon off Pohnpei.",
      "Oral tradition on Pohnpei holds that the stones were flown into place by sorcery.",
      "The builders moved basalt columns weighing several tonnes from outcrops on the far side of the island, without the wheel, draught animals or metal tools.",
      "The walls of Nan Madol are stacked from columns of basalt."],
     "C",
     "The goal is the difficulty of the work, and only the option that puts the weight, the distance "
     "and the absence of tools together conveys it. The tradition about sorcery reports how the feat "
     "was explained locally rather than what it actually demanded."),

 syn("R3",
     ["The California condor swallows fragments of metal when it feeds on a carcass shot with lead ammunition.",
      "Lead poisoning is the leading cause of death among released condors.",
      "Every free-flying condor is trapped twice a year, tested, and treated if its blood lead is high.",
      "California banned lead ammunition for all hunting in 2019.",
      "Blood lead levels in the wild flock have fallen since the ban but remain above the threshold in many birds."],
     "emphasise that the problem has been reduced without being solved.",
     ["The California condor swallows fragments of metal when it feeds on a carcass shot with lead ammunition.",
      "Since California banned lead ammunition in 2019, blood lead levels in the wild flock have fallen, but many birds still test above the threshold.",
      "Every free-flying condor is trapped twice a year and tested for lead.",
      "Lead poisoning is the leading cause of death among released condors."],
     "B",
     "The goal needs both halves at once, the improvement and what remains, and only the option "
     "pairing the fall in blood lead with the birds still over the threshold gives them. The note "
     "naming lead as the leading cause of death states the problem with none of the progress."),

 syn("R4",
     ["The anthers of a tomato flower release pollen only through a small pore at the tip.",
      "A bumblebee grips the anther and vibrates its flight muscles without moving its wings.",
      "The vibration shakes the pollen out through the pore.",
      "Honeybees cannot produce the vibration.",
      "Greenhouse growers pollinated tomato flowers by hand until commercial bumblebee colonies became available in the late 1980s."],
     "explain why greenhouse growers came to depend on bumblebees.",
     ["A bumblebee vibrates its flight muscles to shake pollen out through the pore of a tomato anther, which honeybees cannot do; growers who had pollinated by hand turned to bumblebee colonies from the late 1980s.",
      "The anthers of a tomato flower release pollen only through a small pore at the tip.",
      "Honeybees cannot produce the vibration that shakes pollen from a tomato anther.",
      "Commercial bumblebee colonies became available to greenhouse growers in the late 1980s."],
     "A",
     "The goal asks why the growers needed this particular insect, so the answer has to carry the "
     "vibration, the failure of honeybees and the switch from hand pollination together. The note "
     "that colonies became available in the late 1980s gives the date without the reason."),

 syn("R5",
     ["Harry Beck drew a new map of the London Underground in 1931, in his own time.",
      "He straightened every line to a horizontal, a vertical or a 45-degree diagonal.",
      "Distances on his map bear no fixed relation to distances on the ground.",
      "The publicity department first rejected the design as too radical.",
      "A trial printing of 750,000 copies in 1933 sold out within a month."],
     "emphasise that the distortion of the map was deliberate rather than a defect.",
     ["Harry Beck drew a new map of the London Underground in 1931, in his own time.",
      "Beck straightened every line to a horizontal, a vertical or a 45-degree diagonal, accepting that distances on the map would bear no fixed relation to distances on the ground.",
      "The publicity department first rejected Beck's design as too radical.",
      "A trial printing of 750,000 copies sold out within a month in 1933."],
     "B",
     "The goal turns on intention, and only the option showing the loss of true distance as the "
     "accepted price of straightening the lines presents it as a decision. The initial rejection by "
     "the publicity department reports an opinion of the design rather than the designer's purpose."),

 syn("R6",
     ["Several hundred papyrus scrolls were carbonised by the eruption of Vesuvius in 79 CE.",
      "Attempts to unroll them physically in the eighteenth century destroyed many of them.",
      "X-ray tomography records the internal shape of a rolled scroll without opening it.",
      "The carbon ink is very nearly the same density as the carbonised papyrus it sits on.",
      "Models trained to find the faint surface texture the ink leaves have recovered readable Greek."],
     "explain the obstacle the imaging had to overcome.",
     ["X-ray tomography records the internal shape of a rolled scroll without opening it.",
      "Several hundred papyrus scrolls were carbonised by the eruption of Vesuvius in 79 CE.",
      "Because the carbon ink is nearly the same density as the carbonised papyrus beneath it, the scans had to be read by models trained to pick out the faint texture the ink leaves.",
      "Attempts to unroll the scrolls physically in the eighteenth century destroyed many of them."],
     "C",
     "The goal names an obstacle to the imaging in particular, and matching densities are what stops "
     "an ordinary scan from showing the writing at all. The destruction caused by unrolling is an "
     "obstacle to the older physical method rather than to the scanning."),

 syn("R7",
     ["The American chestnut made up a quarter of the hardwood canopy in parts of the Appalachians.",
      "A fungus introduced about 1904 killed some four billion trees within fifty years.",
      "The fungus kills the trunk but not the root system, which goes on sending up shoots.",
      "The shoots die back before they are old enough to set seed.",
      "Breeders cross surviving trees with the blight-resistant Chinese chestnut and back-cross the offspring to American parents."],
     "explain why the species survives without recovering.",
     ["A fungus introduced about 1904 killed some four billion American chestnut trees within fifty years.",
      "The fungus kills the trunk but not the root system, so shoots keep coming up and then die back before they are old enough to set seed.",
      "Breeders cross surviving trees with the blight-resistant Chinese chestnut and back-cross the offspring to American parents.",
      "The American chestnut once made up a quarter of the hardwood canopy in parts of the Appalachians."],
     "B",
     "The goal asks how the tree can persist and still not come back, and only the option pairing the "
     "surviving roots with shoots that die before seeding answers both halves. The breeding "
     "programme describes an attempt at recovery rather than the reason recovery has not happened."),

 syn("R8",
     ["The English Exchequer recorded debts on notched hazel sticks for some six centuries.",
      "Each stick was split lengthways, and the payer and the Exchequer kept one half each.",
      "The grain of a split stick matches only its own partner.",
      "Tally sticks circulated as a form of credit, since a half-stick could be sold on.",
      "The accumulated sticks were burned in 1834, and the fire destroyed the Palace of Westminster."],
     "explain what made a tally stick hard to forge.",
     ["The English Exchequer recorded debts on notched hazel sticks for some six centuries.",
      "Tally sticks circulated as a form of credit, because a half-stick could be sold on to somebody else.",
      "A tally was split lengthways and the two halves kept apart, and the grain of a split stick matches only its own partner.",
      "The accumulated sticks were burned in 1834, and the fire destroyed the Palace of Westminster."],
     "C",
     "The goal is about forgery, and only the option joining the split halves to a grain that "
     "matches nothing else explains why a counterfeit would fail. The circulation of half-sticks as "
     "credit describes what the tallies were used for rather than what secured them."),

 syn("R9",
     ["The iron pillar at Delhi was forged about 400 CE and stands seven metres high.",
      "It carries almost no rust after sixteen centuries in the open air.",
      "The iron contains an unusually high proportion of phosphorus.",
      "A thin film of iron hydrogen phosphate hydrate forms on the surface and seals it.",
      "Modern iron is made with the phosphorus removed, because phosphorus makes steel brittle."],
     "explain why the pillar has not rusted while modern iron would.",
     ["The iron pillar at Delhi was forged about 400 CE and stands seven metres high.",
      "The pillar's high phosphorus content produces a sealing film of iron hydrogen phosphate hydrate, whereas modern iron has the phosphorus taken out because it makes steel brittle.",
      "The pillar carries almost no rust after sixteen centuries in the open air.",
      "Modern iron is made with the phosphorus removed, because phosphorus makes steel brittle."],
     "B",
     "The goal calls for the contrast between the two metals, and only the option that gives the "
     "sealing film and the deliberate removal of phosphorus from modern iron supplies both sides. "
     "The note on modern practice alone explains nothing about why the pillar survives."),
]

DROPPED = {}
